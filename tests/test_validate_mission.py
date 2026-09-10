import csv
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from tools.update_progress import build_progress, compute_repo_fingerprint, progress_is_current
from tools.validate_mission import (
    FINAL_REPORT_HEADINGS,
    OPPORTUNITY_COLUMNS,
    validate_followup,
    validate_opportunities,
    validate_repository,
    validate_secondary_draft,
)


ROOT = Path(__file__).resolve().parents[1]


class MissionValidationTests(unittest.TestCase):
    def test_current_repository_passes(self):
        self.assertEqual(validate_repository(ROOT), [])

    def test_opportunity_rank_gap_is_rejected(self):
        with (ROOT / "ops/OPPORTUNITIES.csv").open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(tuple(rows[0]), OPPORTUNITY_COLUMNS)
        rows[1] = dict(rows[1], rank="99")
        errors = validate_opportunities(rows)
        self.assertTrue(any("sequential" in error for error in errors))

    def test_followup_without_safety_markers_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "unsafe.md"
            path.write_text("# Follow-up\n\nSend this now.\n", encoding="utf-8")
            errors = validate_followup(path)
        self.assertTrue(any("UNSENT" in error for error in errors))
        self.assertTrue(any("Earliest use" in error for error in errors))
        self.assertTrue(any("SUPPRESSION" in error for error in errors))

    def test_secondary_draft_without_activation_gate_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "unsafe-secondary.md"
            path.write_text("# Secondary outreach — UNSENT\n\nOffer: £149.\n", encoding="utf-8")
            errors = validate_secondary_draft(path)
        self.assertTrue(any("Earliest use" in error for error in errors))
        self.assertTrue(any("primary 24-hour review" in error for error in errors))
        self.assertTrue(any("SUPPRESSION" in error for error in errors))

    def test_final_report_covers_all_required_sections_once(self):
        text = (ROOT / "ops/FINAL_REPORT.md").read_text(encoding="utf-8")
        self.assertEqual(len(FINAL_REPORT_HEADINGS), 17)
        for heading in FINAL_REPORT_HEADINGS:
            self.assertEqual(text.count(heading), 1, heading)

    def test_progress_snapshot_is_evidence_bound(self):
        now = datetime(
            2026,
            9,
            10,
            20,
            55,
            tzinfo=timezone(timedelta(hours=1), name="BST"),
        )
        text = build_progress(ROOT, now=now)
        self.assertIn("Generated: 2026-09-10 20:55:00 BST", text)
        self.assertIn("Time remaining: 6d 22h 14m", text)
        self.assertIn("Gross cash received: £0.00", text)
        self.assertIn("Weekly Codex usage consumed: 10%", text)
        self.assertIn("Contacted: 10", text)
        self.assertIn(
            f"Repository content fingerprint: {compute_repo_fingerprint(ROOT)}",
            text,
        )
        self.assertIn(
            "Only cleared, accessible external-customer cash counts as realised revenue.",
            text,
        )
        self.assertTrue(progress_is_current(ROOT))


if __name__ == "__main__":
    unittest.main()
