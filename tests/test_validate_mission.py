import csv
import tempfile
import unittest
from pathlib import Path

from tools.validate_mission import (
    OPPORTUNITY_COLUMNS,
    validate_followup,
    validate_opportunities,
    validate_repository,
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


if __name__ == "__main__":
    unittest.main()
