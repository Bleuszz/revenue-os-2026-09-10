"""Create review-only catalogue drafts from buyer-approved CSV fields.

This utility is deliberately deterministic. It never invents product facts and it
never marks copy ready to publish. A human must verify every row before use.
"""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REQUIRED_COLUMNS = {
    "sku",
    "product_name",
    "category",
    "confirmed_features",
    "brand",
    "audience",
    "approved_benefit",
    "usage",
    "warranty",
    "cta",
    "prohibited_terms",
}

OUTPUT_COLUMNS = [
    "sku",
    "draft_title",
    "draft_description",
    "confirmed_features",
    "qa_flags",
    "structure_checks_pass",
    "review_status",
]


class ValidationError(ValueError):
    """Raised when the input cannot be processed safely."""


@dataclass(frozen=True)
class Draft:
    sku: str
    title: str
    description: str
    features: str
    flags: tuple[str, ...]
    checks_pass: bool

    def as_row(self) -> dict[str, str]:
        return {
            "sku": self.sku,
            "draft_title": self.title,
            "draft_description": self.description,
            "confirmed_features": self.features,
            "qa_flags": " | ".join(self.flags),
            "structure_checks_pass": "yes" if self.checks_pass else "no",
            "review_status": "HUMAN FACTUAL REVIEW REQUIRED",
        }


def clean(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def split_pipe(value: str) -> list[str]:
    return [clean(item) for item in value.split("|") if clean(item)]


def sentence(value: str) -> str:
    value = clean(value)
    if not value:
        return ""
    return value if value.endswith((".", "!", "?")) else f"{value}."


def truncate_title(value: str, limit: int) -> tuple[str, bool]:
    if len(value) <= limit:
        return value, False
    shortened = value[: limit + 1].rsplit(" ", 1)[0].rstrip(" |,-")
    if not shortened:
        shortened = value[:limit].rstrip(" |,-")
    return shortened, True


def make_draft(row: dict[str, str], title_limit: int = 80) -> Draft:
    sku = clean(row.get("sku"))
    product_name = clean(row.get("product_name"))
    category = clean(row.get("category"))
    features = split_pipe(clean(row.get("confirmed_features")))

    missing_required = [
        name
        for name, value in (
            ("sku", sku),
            ("product_name", product_name),
            ("category", category),
            ("confirmed_features", "|".join(features)),
        )
        if not value
    ]
    if missing_required:
        raise ValidationError(
            f"Row with SKU {sku or '<missing>'} lacks: {', '.join(missing_required)}"
        )

    brand = clean(row.get("brand"))
    audience = clean(row.get("audience"))
    approved_benefit = clean(row.get("approved_benefit"))
    usage = clean(row.get("usage"))
    warranty = clean(row.get("warranty"))
    cta = clean(row.get("cta"))
    prohibited_terms = split_pipe(clean(row.get("prohibited_terms")))

    title_parts = [part for part in (brand, product_name, category) if part]
    title, title_was_truncated = truncate_title(" | ".join(title_parts), title_limit)

    description_parts: list[str] = []
    if audience:
        description_parts.append(sentence(f"{product_name} for {audience}"))
    else:
        description_parts.append(sentence(product_name))
    if approved_benefit:
        description_parts.append(sentence(approved_benefit))
    description_parts.append(sentence(f"Confirmed features: {'; '.join(features)}"))
    if usage:
        description_parts.append(sentence(f"Usage: {usage}"))
    if warranty:
        description_parts.append(sentence(f"Warranty: {warranty}"))
    if cta:
        description_parts.append(sentence(cta))
    description = " ".join(description_parts)

    flags: list[str] = []
    for field_name, value in (
        ("brand", brand),
        ("audience", audience),
        ("approved_benefit", approved_benefit),
        ("usage", usage),
        ("warranty", warranty),
        ("cta", cta),
    ):
        if not value:
            flags.append(f"missing optional field: {field_name}")
    if title_was_truncated:
        flags.append(f"title truncated to {title_limit} characters")

    combined = f"{title} {description}".casefold()
    matched_terms = [term for term in prohibited_terms if term.casefold() in combined]
    if matched_terms:
        flags.append(f"prohibited term present: {', '.join(matched_terms)}")

    checks_pass = not title_was_truncated and not matched_terms
    return Draft(
        sku=sku,
        title=title,
        description=description,
        features=" | ".join(features),
        flags=tuple(flags),
        checks_pass=checks_pass,
    )


def process_rows(rows: Iterable[dict[str, str]], title_limit: int = 80) -> list[Draft]:
    drafts: list[Draft] = []
    seen_skus: set[str] = set()
    for row in rows:
        draft = make_draft(row, title_limit=title_limit)
        sku_key = draft.sku.casefold()
        if sku_key in seen_skus:
            raise ValidationError(f"Duplicate SKU: {draft.sku}")
        seen_skus.add(sku_key)
        drafts.append(draft)
    if not drafts:
        raise ValidationError("Input contains no product rows")
    return drafts


def run(input_path: Path, output_path: Path, title_limit: int = 80) -> int:
    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing_columns = sorted(REQUIRED_COLUMNS - columns)
        if missing_columns:
            raise ValidationError(
                f"Input is missing required columns: {', '.join(missing_columns)}"
            )
        drafts = process_rows(reader, title_limit=title_limit)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(draft.as_row() for draft in drafts)
    return len(drafts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate review-only catalogue drafts from approved product facts."
    )
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    parser.add_argument("--title-limit", type=int, default=80)
    args = parser.parse_args()
    if args.title_limit < 20:
        parser.error("--title-limit must be at least 20")
    return args


def main() -> int:
    args = parse_args()
    try:
        count = run(args.input_csv, args.output_csv, title_limit=args.title_limit)
    except (OSError, ValidationError) as exc:
        raise SystemExit(f"error: {exc}") from exc
    print(f"wrote {count} review-only draft row(s) to {args.output_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
