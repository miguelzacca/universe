"""Verifique autorização de orçamento, registro e retomada com respostas simuladas."""

from argparse import Namespace
from decimal import Decimal
import importlib.util
from io import BytesIO
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "video-openrouter.py"
SPEC = importlib.util.spec_from_file_location("video_openrouter", SCRIPT)
VIDEO = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VIDEO)


class VideoJobTest(unittest.TestCase):
    def setUp(self):
        directory = TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.args = Namespace(
            job=self.root / ".universe" / "scene.json",
            model=VIDEO.DEFAULT_MODEL,
            env_file=self.root / ".env",
            duration=4,
            resolution="720p",
            aspect="16:9",
            max_usd=Decimal("0.12"),
            estimate_usd=None,
            first=str(self.root / "first.jpg"),
            last="https://example.com/last.jpg",
            prompt=self.root / "shot.txt",
        )
        Path(self.args.first).write_bytes(b"fixture-frame")
        self.args.prompt.write_text("Keep one fixed camera and settle on the box.", encoding="utf-8")
        self.catalog = {"data": [{
            "id": VIDEO.DEFAULT_MODEL,
            "supported_frame_images": ["first_frame", "last_frame"],
            "supported_durations": [4, 6, 8],
            "supported_resolutions": ["720p", "1080p"],
            "supported_aspect_ratios": ["16:9", "9:16"],
            "pricing_skus": {"duration_seconds_without_audio_720p": "0.03"},
        }]}

    def test_two_frames_and_one_post(self):
        with patch.object(VIDEO, "api_key", return_value="fixture-key"), patch.object(
            VIDEO, "read_json", side_effect=[self.catalog, {"id": "job-42"}]
        ) as response:
            VIDEO.submit(self.args)
            post = response.call_args.args
            self.assertEqual(post[:2], ("", "fixture-key"))
            self.assertFalse(post[2]["generate_audio"])
            self.assertEqual(post[2]["prompt"], self.args.prompt.read_text(encoding="utf-8"))
            first, last = post[2]["frame_images"]
            self.assertEqual([first["frame_type"], last["frame_type"]], list(VIDEO.FRAME_ROLES))
            self.assertTrue(first["image_url"]["url"].startswith("data:image/jpeg;base64,"))
            self.assertEqual(last["image_url"]["url"], self.args.last)
            self.assertEqual(json.loads(self.args.job.read_text())["id"], "job-42")
            with self.assertRaises(VIDEO.VideoError):
                VIDEO.submit(self.args)
            self.assertEqual(response.call_count, 2)

    def test_catalog_cost_outranks_supplied_estimate(self):
        self.args.max_usd = Decimal("0.11")
        self.args.estimate_usd = Decimal("0.09")
        with patch.object(VIDEO, "api_key", return_value="fixture-key"), patch.object(
            VIDEO, "read_json", return_value=self.catalog
        ) as response:
            with self.assertRaisesRegex(VIDEO.VideoError, "acima do limite"):
                VIDEO.submit(self.args)
            response.assert_called_once_with("/models")
            self.assertFalse(self.args.job.exists())

    def test_model_with_first_frame_only_never_submits(self):
        self.catalog["data"][0]["supported_frame_images"] = ["first_frame"]
        with patch.object(VIDEO, "api_key", return_value="fixture-key"), patch.object(
            VIDEO, "read_json", return_value=self.catalog
        ) as response:
            with self.assertRaisesRegex(VIDEO.VideoError, "compatibilidade"):
                VIDEO.submit(self.args)
            response.assert_called_once_with("/models")
            self.assertFalse(self.args.job.exists())

    def test_ambiguous_submission_keeps_record(self):
        with patch.object(VIDEO, "api_key", return_value="fixture-key"), patch.object(
            VIDEO, "read_json", side_effect=[self.catalog, VIDEO.VideoError("timeout")]
        ) as response:
            with self.assertRaisesRegex(VIDEO.VideoError, "timeout"):
                VIDEO.submit(self.args)
            self.assertEqual(json.loads(self.args.job.read_text())["status"], "submitting")
            with self.assertRaisesRegex(VIDEO.VideoError, "registro"):
                VIDEO.submit(self.args)
            self.assertEqual(response.call_count, 2)

    def test_resume_downloads_only_by_known_job(self):
        output = self.root / "media" / "video.mp4"
        args = Namespace(job=None, id="job-42", env_file=self.args.env_file, wait=True, output=output)
        sample = b"\x00\x00\x00\x18ftypisom"
        with patch.object(VIDEO, "api_key", return_value="fixture-key"), patch.object(
            VIDEO, "read_json", side_effect=[{"status": "in_progress"}, {"status": "completed", "usage": {"cost": 0.12}}]
        ) as status, patch.object(VIDEO, "request", return_value=BytesIO(sample)) as download, patch.object(
            VIDEO.time, "sleep"
        ) as wait:
            VIDEO.resume(args)
            self.assertEqual(status.call_count, 2)
            wait.assert_called_once_with(30)
            download.assert_called_once_with("/job-42/content?index=0", "fixture-key")
            self.assertEqual(output.read_bytes(), sample)


if __name__ == "__main__":
    unittest.main()
