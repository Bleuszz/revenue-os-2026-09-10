# Seven-Day Revenue OS

Private operating repository for a seven-day, evidence-led revenue mission beginning 2026-09-10.

## What the system does

It keeps the commercial state, opportunity scoring, outreach evidence, experiments, risk controls, and cash ledger needed to test small legitimate offers and maximise verified net cash received within seven days.

## Why it exists

The mission must recover at least £70 net cash while risking no more than £30 of additional capital. Pipeline and promises never count as cash.

## How to run it

1. Read `ops/STATE.md`.
2. Read `ops/DASHBOARD.md` and `ops/NEXT_ACTIONS.md`.
3. Execute the highest expected-value unblocked action.
4. Record evidence in `ops/EXPERIMENTS.md`, `ops/LEADS.csv`, and `ops/MISSION_LOG.md`.
5. Update `ops/FINANCE.md` only from verifiable payment or expense evidence.
6. Maintain `ops/FINAL_REPORT.md` as a draft evidence map; remove its draft marker only after the fixed deadline and a full evidence audit.

## Requirements

- Git
- Web access for current research
- An authorised communication channel for outreach
- A legitimate payment method before accepting an order
- Optional local scripting tools only when repeatable fulfilment justifies them

## Environment variables

No environment variables are required at present. Secrets must remain outside Git. If code later needs configuration, document placeholders in `.env.example`.

## Architecture

- `ops/`: durable commercial state and evidence
- `docs/`: research and customer-facing working documentation
- `tools/`: deterministic fulfilment utilities
- `templates/`: fictional input/output examples that contain no customer data
- `tests/`: automated checks for fulfilment utilities

## Operating procedure

Use manual-first demand tests, contact a small number of highly relevant business prospects, provide concrete value in the first message, fulfil paid work before speculative building, and reallocate effort from observed outcomes.

## Catalogue workflow

Create review-only product drafts from buyer-approved facts:

```powershell
python tools/catalogue_workflow.py templates/catalogue_input_demo.csv templates/catalogue_output_demo.csv --report-md docs/samples/catalogue-workflow-report.md
```

The CSV and Markdown report always require human factual review and are never automatically published. The checked-in three-product demo is fictional and demonstrates clean input, missing optional fields, and prohibited-claim detection; it is not client work or performance evidence.

## Listing-rescue delivery workbook

Regenerate the buyer-review workbook for the £99 primary offer:

```powershell
node tools/build_listing_rescue_workbook.mjs
```

The workbook is written to `outputs/listing-rescue-delivery-template.xlsx`. It
contains fifteen listing rows, fact-source and buyer-approval controls, dynamic
row statuses, and no prospect data. The generated file is excluded from Git;
the builder is tracked so a clean template can be reproduced before fulfilment.

Run verification:

```powershell
python -m unittest discover -s tests -v
python tools/validate_mission.py
```

The mission validator is read-only. It checks the required command-centre files,
CSV schemas and IDs, accounting reconciliation, selected strategy roles,
follow-up timing safeguards, and primary-preview factual controls.

## Deployment

No deployment exists. A website will be created only if it materially improves conversion.

## Known limitations

- Stripe live payments are unavailable under the standing no-photo-ID constraint. Direct UK bank transfer is the primary post-agreement route; an existing usable PayPal account is conditional fallback only.
- No sale, payment, customer, testimonial, traffic, or conversion result exists at mission start.
- Cold outreach must use relevant public business channels, honest identity, low volume, and a clear opt-out.

## Security notes

Do not commit credentials, verification codes, customer-sensitive data, inbox contents, or payment details. Store the minimum information required to operate.

## Current mission status

Day 1. Twenty-eight strategies scored, primary offer live, 17 leads researched and 10 tailored messages sent. The secondary offer and five previews are ready but not activated. A tested £399 catalogue-workflow pilot is the asymmetric expansion. Verified cash received: £0.00; spend: £0.00; signed work: £0.00. See `ops/DASHBOARD.md` for the current pipeline and next action.
