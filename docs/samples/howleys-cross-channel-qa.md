# Howleys cross-channel catalogue QA snapshot

Prepared from public pages on 2026-09-10. This is an unsent, no-obligation capability sample, not client work or a claim about Howleys' internal systems or commercial results. Revalidate every page immediately before any use.

## Finding 1 — the same title issue appears on two channels

The product title `Barbie Reuseable Bag For Life Shopping Bag` appears on:

- Howleys' own product page, with SKU `RM99-0198`, UPC `5015934890479`, and MPN `99-0198`: https://www.howleys.co.uk/barbie-reuseable-bag-for-life-shopping-bag/
- a live OnBuy offer sold by Howleys Toys, with EAN `5015934890479` and MPN `99-0198`: https://www.onbuy.com/gb/p/barbie-reuseable-bag-for-life-shopping-bag~p134694065/

Both descriptions use the standard spelling `Reusable`, so a safe proposed title correction is:

`Barbie Reusable Bag for Life Shopping Bag`

The matching identifiers and title suggest—but do not prove—that a shared product-data field may be propagating the typo across channels. Confirm the canonical source and all active destinations before editing.

## Finding 2 — a current eBay title ends mid-phrase

The live listing `SwimWays Spring Float SunSeat Pool Lounge Chair for` ends on the preposition `for`: https://www.ebay.co.uk/itm/366547022465

The public page showed 24 sold, 3 available, and a last revision on 2026-09-10. The error is safe to flag, but a corrected title is blocked until Howleys confirms the missing intended object, compatibility, or age/use qualifier. Do not guess it from similar third-party listings.

## Example handoff

### UPC 5015934890479 / MPN 99-0198

- Current issue: `Reuseable` appears in the title on two channels while both descriptions say `Reusable`.
- Safe action: correct the canonical title spelling, then verify every feed destination.
- Confirmation needed: identify the source-of-truth field and active channels.

### eBay item 366547022465

- Current issue: the title ends with `for`.
- Safe action: hold the rewrite and flag it as incomplete.
- Confirmation needed: identify the missing intended term.

## What the paid sprint would add

- Thirteen more current listing checks, for 15 total.
- A structured CSV containing source URL, current title, proposed title, confirmed facts, and QA flags.
- Catalogue-level patterns separated from one-off corrections.
- One factual/copy revision and a human-review gate before publication.

No marketplace credentials or automatic publishing are required.
