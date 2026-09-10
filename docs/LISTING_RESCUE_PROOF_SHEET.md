# Listing-rescue proof sheet

Status: **UNSENT**

Purpose: a one-page, claim-safe capability sheet for a genuine buyer reply or a
revalidated follow-up. It is not client work, a testimonial, or performance
evidence.

## Contents

- Fixed £99 scope: fifteen reviewed listing fixes within 24 hours.
- Free one-to-three-listing preview before purchase.
- Fictional before-and-after QA example.
- Explicit buyer-approval and source-fact boundary.
- No login, publishing access, or invented product facts.

## Generate

```powershell
python tools/build_listing_rescue_proof_pdf.py
```

Output: `outputs/listing-rescue-proof-sheet.pdf` (excluded from Git; reproducible
from the tracked builder).

## Use gate

Before sending, read the complete Gmail thread, check `ops/SUPPRESSION.csv`,
confirm the prospect has not replied, opted out, or bounced, and confirm the
relevant follow-up timing gate has elapsed. Do not attach it in an additional
unsolicited message merely because it exists.

The final PDF must remain one A4 page. Verify it with `pdfinfo`, extract its text
with `pypdf`, render it with `pdftoppm`, and visually inspect the rendered PNG.
