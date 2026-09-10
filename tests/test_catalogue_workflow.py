import csv
import tempfile
import unittest
from pathlib import Path

from tools.catalogue_workflow import ValidationError, make_draft, process_rows, run


def row(**overrides: str) -> dict[str, str]:
    base = {
        "sku": "SKU-001",
        "product_name": "Fictional Work Lamp",
        "category": "Rechargeable inspection light",
        "confirmed_features": "USB-C charging | magnetic base | 3 brightness settings",
        "brand": "Example Brand",
        "audience": "workshop technicians",
        "approved_benefit": "Position the light hands-free using the magnetic base",
        "usage": "Charge fully before first use",
        "warranty": "12 months under the seller's published terms",
        "cta": "Check the specification and order the required quantity",
        "prohibited_terms": "best in the world | guaranteed savings",
    }
    base.update(overrides)
    return base


class CatalogueWorkflowTests(unittest.TestCase):
    def test_draft_uses_approved_fields_and_requires_review(self) -> None:
        draft = make_draft(row())
        self.assertIn("Example Brand", draft.title)
        self.assertIn("USB-C charging", draft.description)
        self.assertNotIn("best in the world", draft.description)
        self.assertTrue(draft.checks_pass)
        self.assertEqual(draft.as_row()["review_status"], "HUMAN FACTUAL REVIEW REQUIRED")

    def test_missing_required_value_fails(self) -> None:
        with self.assertRaisesRegex(ValidationError, "confirmed_features"):
            make_draft(row(confirmed_features=""))

    def test_duplicate_sku_fails_case_insensitively(self) -> None:
        with self.assertRaisesRegex(ValidationError, "Duplicate SKU"):
            process_rows([row(), row(sku="sku-001")])

    def test_prohibited_term_is_flagged(self) -> None:
        draft = make_draft(
            row(
                approved_benefit="Guaranteed savings for every workshop",
                prohibited_terms="guaranteed savings",
            )
        )
        self.assertFalse(draft.checks_pass)
        self.assertIn("prohibited term present", " | ".join(draft.flags))

    def test_long_title_is_truncated_and_flagged(self) -> None:
        draft = make_draft(row(product_name="Very Long " * 20), title_limit=40)
        self.assertLessEqual(len(draft.title), 40)
        self.assertFalse(draft.checks_pass)
        self.assertIn("title truncated", " | ".join(draft.flags))

    def test_csv_run_checks_schema_and_writes_rows(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = Path(temp_dir) / "input.csv"
            output_path = Path(temp_dir) / "output.csv"
            with input_path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(row().keys()))
                writer.writeheader()
                writer.writerow(row())
            self.assertEqual(run(input_path, output_path), 1)
            with output_path.open("r", encoding="utf-8", newline="") as handle:
                result = list(csv.DictReader(handle))
            self.assertEqual(result[0]["sku"], "SKU-001")
            self.assertEqual(result[0]["structure_checks_pass"], "yes")


if __name__ == "__main__":
    unittest.main()
