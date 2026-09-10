# Pizzazz marketplace-feed QA snapshot

Prepared from public pages on 2026-09-10. This is an unsent, no-obligation capability sample, not client work or a claim about Pizzazz's internal systems or commercial results. Revalidate every page immediately before any use.

## Finding 1 - one title typo spans two marketplaces

The title `Xtralite Omni MotionGlo LED Motion Sensor Reachargeable Wall Mounted Night Light, Twin Pack` appears on:

- Tesco Marketplace, where the page says it is sold and sent by Pizzazz Retail Limited: https://www.tesco.com/shop/en-GB/products/326298125
- B&Q, where the page says it is sold and shipped by Pizzazz Retail Limited and identifies product code `5060195207610`: https://www.diy.com/departments/xtralite-omni-motionglo-led-motion-sensor-reachargeable-wall-mounted-night-light-twin-pack/5060195207610_BQ.prd

Both pages use `Rechargeable` correctly in their feature or description copy. A safe title spelling correction is therefore:

`Xtralite Omni MotionGlo LED Motion Sensor Rechargeable Wall Mounted Night Light, Twin Pack`

## Finding 2 - the typo appears on another Xtralite product

B&Q also shows `Reachargeable` in the title of the separate Omni FlexiGlo product, code `5060195207603`, sold and shipped by Pizzazz Retail Limited: https://www.diy.com/departments/xtralite-omni-flexiglo-led-motion-sensor-reachargeable-night-light-wall-mounted-or-freestanding/5060195207603_BQ.prd

The page's feature and product-information sections use `Rechargeable` correctly. The repeated title-only typo across at least two products makes a small title-field audit more useful than treating the first row as isolated.

## Finding 3 - the matching MotionGlo product differs on eBay

Pizzazz's eBay listing for EAN `5060195207610` uses a different, correctly spelt title: https://www.ebay.co.uk/itm/168169062947

This suggests—but does not prove—that marketplace-specific title fields or feeds are out of sync. It does not identify which system is authoritative. Confirm the source of truth and channel rules before editing or syndicating anything.

## Example handoff

### Product code / EAN 5060195207610

- Current issue: Tesco and B&Q titles contain `Reachargeable`; eBay uses `Rechargeable` in a different title.
- Safe action: correct the spelling in the affected title fields and reconcile the approved channel-specific title structure.
- Confirmation needed: identify the authoritative source, marketplace limits, and intended naming order.

### Product code 5060195207603

- Current issue: the B&Q title contains the same `Reachargeable` typo, while the page body uses `Rechargeable`.
- Safe action: correct the title spelling after confirming the relevant source field.
- Confirmation needed: identify the source field used for B&Q and check every active destination for the same SKU.

## What the paid sprint would add

- Thirteen more current listing checks, for 15 total.
- A structured CSV containing channel, product identifier, current title, proposed title, confirmed facts, and QA flags.
- Cross-channel differences separated from safe universal corrections.
- One factual/copy revision and a human-review gate before publication.

No marketplace credentials or automatic publishing are required.
