"""Validate the durable state of the seven-day revenue mission.

This is intentionally read-only and standard-library-only. It checks structural
and accounting invariants that should hold before any mission-state commit.
"""

from __future__ import annotations

import csv
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable


REQUIRED_FILES = (
    "ops/STATE.md",
    "ops/DECISIONS.md",
    "ops/NEXT_ACTIONS.md",
    "ops/EXPERIMENTS.md",
    "ops/FINANCE.md",
    "ops/LEADS.csv",
    "ops/CONTACTS.csv",
    "ops/METRICS.md",
    "ops/COMPUTE_BUDGET.md",
    "ops/RISK_REGISTER.md",
    "ops/MISSION_LOG.md",
    "ops/ENVIRONMENT.md",
    "ops/ACCOUNTS.md",
    "ops/DASHBOARD.md",
    "ops/OPPORTUNITIES.csv",
    "ops/SUPPRESSION.csv",
    "docs/INVOICE_READINESS.md",
    "tools/build_listing_rescue_workbook.mjs",
)

LEAD_COLUMNS = (
    "lead_id", "business", "person_if_public", "sector", "location",
    "website", "public_contact_channel", "problem_observed", "evidence",
    "proposed_solution", "estimated_value", "personalisation_note",
    "lead_score", "status", "last_contact", "next_action", "reply",
    "quoted_value", "expected_value", "cash_received",
)

CONTACT_COLUMNS = (
    "contact_id", "lead_id", "datetime", "channel", "direction",
    "subject_or_summary", "status", "evidence_reference", "next_action",
    "opt_out",
)

OPPORTUNITY_COLUMNS = (
    "rank", "id", "strategy", "category", "what_is_sold", "buyer",
    "price_gbp", "build_hours", "time_to_cash_days", "capital_gbp",
    "cash_chance", "margin", "speed", "ai_leverage", "channel_access",
    "demand_evidence", "repeatability", "capital_safety", "score",
    "primary_channel", "trust_barrier", "likely_failure_mode",
    "evidence_ref", "status",
)

PRIMARY_PREVIEWS = (
    "vws.md", "startoys.md", "fullyretro.md", "voodoo-vixen.md",
    "pizzazz.md", "howleys.md", "simply-toys.md", "rockthosecurves.md",
    "g5-apparel.md", "retro-sweet-kings.md",
)


def _load_csv(path: Path, columns: tuple[str, ...], errors: list[str]) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != columns:
            errors.append(f"{path.name}: unexpected CSV schema")
            return []
        return list(reader)


def _unique(rows: Iterable[dict[str, str]], key: str, label: str, errors: list[str]) -> None:
    values = [row[key].strip() for row in rows]
    if any(not value for value in values):
        errors.append(f"{label}: blank {key}")
    duplicates = sorted({value for value in values if values.count(value) > 1})
    if duplicates:
        errors.append(f"{label}: duplicate {key}: {', '.join(duplicates)}")


def _money(row: dict[str, str], field: str, label: str, errors: list[str]) -> Decimal:
    try:
        value = Decimal(row[field].strip())
    except (InvalidOperation, KeyError):
        errors.append(f"{label}: invalid {field}")
        return Decimal("0")
    if not value.is_finite() or value < 0:
        errors.append(f"{label}: {field} must be finite and non-negative")
        return Decimal("0")
    return value


def validate_opportunities(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    if len(rows) < 20:
        errors.append(f"OPPORTUNITIES.csv: expected at least 20 rows, found {len(rows)}")
    _unique(rows, "id", "OPPORTUNITIES.csv", errors)
    try:
        ranks = [int(row["rank"]) for row in rows]
    except (KeyError, ValueError):
        errors.append("OPPORTUNITIES.csv: ranks must be integers")
    else:
        if ranks != list(range(1, len(rows) + 1)):
            errors.append("OPPORTUNITIES.csv: ranks must be sequential in file order")
    for role in ("PRIMARY", "SECONDARY", "ASYMMETRIC", "EMERGENCY"):
        count = sum(row.get("status") == role for row in rows)
        if count != 1:
            errors.append(f"OPPORTUNITIES.csv: expected exactly one {role}, found {count}")
    return errors


def validate_followup(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for required in ("UNSENT", "Earliest use:", "ops/SUPPRESSION.csv"):
        if required not in text:
            errors.append(f"{path.name}: missing safety marker {required!r}")
    earliest = re.search(r"^Earliest use:\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) Europe/London\.$", text, re.MULTILINE)
    if not earliest:
        errors.append(f"{path.name}: earliest-use gate is not in the expected format")
    if "complete Gmail thread" not in text:
        errors.append(f"{path.name}: missing full-thread recheck instruction")
    return errors


def validate_secondary_draft(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for required in (
        "UNSENT",
        "Earliest use: 2026-09-11 19:35 Europe/London.",
        "ops/SUPPRESSION.csv",
        "Search Gmail for prior contact",
        "Send only if the primary 24-hour review supports secondary activation.",
        "£149",
        "No site access is needed",
        "reply `no thanks`",
    ):
        if required not in text:
            errors.append(f"{path.name}: missing secondary-outreach safeguard {required!r}")
    return errors


def _ledger_amount(text: str, label: str, errors: list[str]) -> Decimal | None:
    match = re.search(rf"^- {re.escape(label)}: £([\d,]+(?:\.\d+)?)", text, re.MULTILINE)
    if not match:
        errors.append(f"FINANCE.md: missing {label!r} line")
        return None
    return Decimal(match.group(1).replace(",", ""))


def _compare_amount(actual: Decimal, stated: Decimal | None, label: str, errors: list[str]) -> None:
    if stated is not None and actual != stated:
        errors.append(f"FINANCE.md: {label} is £{stated:.2f}, but CSV total is £{actual:.2f}")


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    leads = _load_csv(root / "ops/LEADS.csv", LEAD_COLUMNS, errors)
    contacts = _load_csv(root / "ops/CONTACTS.csv", CONTACT_COLUMNS, errors)
    opportunities = _load_csv(root / "ops/OPPORTUNITIES.csv", OPPORTUNITY_COLUMNS, errors)

    _unique(leads, "lead_id", "LEADS.csv", errors)
    _unique(contacts, "contact_id", "CONTACTS.csv", errors)
    errors.extend(validate_opportunities(opportunities))

    lead_ids = {row["lead_id"] for row in leads}
    contact_lead_ids = {row["lead_id"] for row in contacts}
    for row in contacts:
        if row["lead_id"] not in lead_ids:
            errors.append(f"CONTACTS.csv: {row['contact_id']} references unknown lead {row['lead_id']}")
        if row["direction"] == "outbound" and row["status"] == "sent" and not row["evidence_reference"]:
            errors.append(f"CONTACTS.csv: sent contact {row['contact_id']} lacks evidence")
        if row["opt_out"].lower() not in {"true", "false"}:
            errors.append(f"CONTACTS.csv: {row['contact_id']} has invalid opt_out value")

    quoted_total = Decimal("0")
    expected_total = Decimal("0")
    cash_total = Decimal("0")
    reserve_total = Decimal("0")
    for row in leads:
        label = f"LEADS.csv: {row['lead_id']}"
        estimated = _money(row, "estimated_value", label, errors)
        quoted = _money(row, "quoted_value", label, errors)
        expected = _money(row, "expected_value", label, errors)
        cash = _money(row, "cash_received", label, errors)
        quoted_total += quoted
        expected_total += expected
        cash_total += cash
        if row["status"] == "qualified_hold_secondary":
            reserve_total += estimated
        if row["status"] == "contacted" and row["lead_id"] not in contact_lead_ids:
            errors.append(f"{label} is contacted but has no contact record")
        if row["status"] != "contacted" and (quoted or expected):
            errors.append(f"{label} is not contacted but carries quoted/expected value")

    followups = sorted((root / "docs/followups").glob("*.md"))
    if not followups:
        errors.append("docs/followups: expected at least one guarded follow-up")
    for path in followups:
        errors.extend(validate_followup(path))

    secondary_drafts = sorted((root / "docs/secondary_outreach").glob("*.md"))
    if len(secondary_drafts) != 5:
        errors.append(f"docs/secondary_outreach: expected 5 guarded drafts, found {len(secondary_drafts)}")
    for path in secondary_drafts:
        errors.extend(validate_secondary_draft(path))

    sample_dir = root / "docs/samples"
    for filename in PRIMARY_PREVIEWS:
        if not (sample_dir / filename).is_file():
            errors.append(f"missing primary preview: docs/samples/{filename}")
    safeguards = {
        "vws.md": ("[Confirm buyer category]",),
        "voodoo-vixen.md": ("[confirm product brand]", "Do not infer the product brand"),
        "simply-toys.md": ("24-Day Ultimate Ideas Kit",),
    }
    for filename, required_phrases in safeguards.items():
        path = sample_dir / filename
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for phrase in required_phrases:
                if phrase not in text:
                    errors.append(f"{filename}: missing factual-safety phrase {phrase!r}")
    voodoo = sample_dir / "voodoo-vixen.md"
    if voodoo.is_file() and "Jumpsuit – Voodoo Vixen" in voodoo.read_text(encoding="utf-8"):
        errors.append("voodoo-vixen.md: unsupported product-brand inference reintroduced")

    finance = root / "ops/FINANCE.md"
    if finance.is_file():
        text = finance.read_text(encoding="utf-8")
        _compare_amount(cash_total, _ledger_amount(text, "Gross cash received", errors), "gross cash", errors)
        _compare_amount(quoted_total, _ledger_amount(text, "Pipeline", errors), "pipeline", errors)
        _compare_amount(expected_total, _ledger_amount(text, "Probability-weighted pipeline", errors), "weighted pipeline", errors)
        _compare_amount(reserve_total, _ledger_amount(text, "Uncontacted secondary reserve", errors), "secondary reserve", errors)

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        print(f"MISSION VALIDATION FAILED ({len(errors)} error(s))")
        for error in errors:
            print(f"- {error}")
        return 1

    with (root / "ops/LEADS.csv").open(encoding="utf-8-sig", newline="") as handle:
        leads = list(csv.DictReader(handle))
    with (root / "ops/CONTACTS.csv").open(encoding="utf-8-sig", newline="") as handle:
        contacts = list(csv.DictReader(handle))
    with (root / "ops/OPPORTUNITIES.csv").open(encoding="utf-8-sig", newline="") as handle:
        opportunities = list(csv.DictReader(handle))
    print(
        "MISSION VALIDATION PASSED - "
        f"{len(opportunities)} opportunities, {len(leads)} leads, "
        f"{len(contacts)} contacts, {len(PRIMARY_PREVIEWS)} primary previews"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
