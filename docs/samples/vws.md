# Vintage Wholesale Store public listing preview

Sources checked 2026-09-10:

- Store: https://www.ebay.co.uk/str/vintagewholesalestoreltd
- Listing: https://www.ebay.co.uk/itm/183768167192

## Observed public facts

- Store has 45 active items, 1.5K historical sales and 100% positive feedback at check.
- Current title: `JOB LOT X 10 ME SHORTS, BRIGHT COLOURS, CRAZY PRINTS, HOLIDAY, FESTIVAL (52)`
- Price: £35 or Best Offer
- Condition: Pre-owned — Good
- Seller note mentions expected vintage wear.
- Title syntax across the store varies between `JOB LOT`, `JOBLOT`, `JOB LOTX`, `X10` and `10 X`.

## Example title

`10x [Confirm buyer category] Vintage Festival Shorts Job Lot Bright Mixed Prints Wholesale`

If the seller confirms that `ME SHORTS` means `MEN'S SHORTS`, replace the placeholder with `Men's`. Do not resolve the truncated source text by assumption.

## QA flags

- Confirm whether `ME` is a truncation/typo for `MEN'S`.
- Move the internal `(52)` reference to a SKU field if it is not useful to buyers.
- Normalise job-lot syntax and capitalisation across the catalogue.
- Preserve the wear disclaimer and add verified lot-level sizing/brand distribution where available.
