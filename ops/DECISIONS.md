# Decision Log

## D-001 — Preserve cash during discovery

- Date: 2026-09-10
- Decision: Commit £0 during environment audit and initial market testing.
- Reason: Connected email, GitHub, web, browser, local coding, and private hosting are already available.
- Revisit when: A proven bottleneck has a paid remedy with a plausible seven-day payback.

## D-002 — Manual-first sales validation

- Date: 2026-09-10
- Decision: Do not build a platform before a buyer signal.
- Reason: Seven-day time-to-cash dominates speculative scalability.

## D-003 — Honest low-volume B2B outreach only

- Date: 2026-09-10
- Decision: If outbound email is selected, use a small number of relevant public corporate channels with specific evidence, truthful identity, and an easy opt-out.
- Reason: Conversion quality, reputation, UK privacy/marketing rules, and platform safety.

## D-004 — Lead with the listing-rescue sprint

- Date: 2026-09-10
- Decision: Offer established UK corporate e-commerce sellers a fixed £99 sprint covering 15 titles, description improvements, and catalogue QA flags within 24 hours.
- Reason: It scored highest on seven-day cash probability, speed, margin, accessible distribution, and the ability to demonstrate value before purchase.
- Revisit when: Ten qualified sends produce no engagement or 20 produce no meaningful response.

## D-005 — Avoid slow-clearing marketplaces as the primary cash path

- Date: 2026-09-10
- Decision: Do not rely on new Upwork, Fiverr, PeoplePerHour, research-panel, or digital-product payouts for the seven-day floor.
- Reason: Published review, security, or payout holds can extend beyond the mission deadline. These remain secondary discovery channels only where settlement timing is verified.

## D-006 — Use a three-message calibration batch

- Date: 2026-09-10
- Decision: Start with three high-specificity corporate prospects before increasing volume.
- Reason: This provides early feedback while limiting deliverability, reputation, and compliance risk. No delivery or engagement claim will be made without evidence.

## D-007 — Pause primary outbound at 10 sends for measurement

- Date: 2026-09-10
- Decision: Do not send more primary-offer email until a 24-hour observation window has elapsed or an earlier reply/bounce provides actionable evidence.
- Reason: The planned volume trigger is reached, but minutes of silence are not evidence of offer failure. Continuing immediately would increase reputation risk and weaken experiment learning.

## D-008 — Defer Stripe setup until buyer intent

- Date: 2026-09-10
- Decision: Keep direct bank transfer as the assumed zero-fee option and defer Stripe account/login work until a prospect requests card payment or signals intent.
- Reason: Stripe-hosted Payment Links are a good simple-product route, but no Stripe connector or signed-in browser account is available. Signup/login would add user friction before a payment need exists.

- Status: Superseded by D-009 after the authenticated sandbox revealed a mandatory identity-verification gate.

## D-009 — Use an ID-free payment hierarchy

- Date: 2026-09-10
- Decision: Use direct UK bank transfer as the primary route after buyer agreement. Use a PayPal commercial invoice only if an existing account is already usable without document verification and funds will be accessible inside the mission window. Treat Stripe as inactive.
- Reason: Nathan cannot supply photo ID. Stripe live activation is blocked on ID/selfie, while PayPal states that new or inactive seller funds may be held for up to 21 days and identity confirmation can be required. Direct transfer avoids a new intermediary and has the best chance of accessible cash before the deadline.
- Controls: Never store bank details in Git; verify receipts inside the real account; never accept screenshots as proof; do not use PayPal friends-and-family for a commercial service; record actual fees and holds.
- Revisit when: A buyer cannot use bank transfer and Nathan confirms an existing PayPal account is currently able to receive and release commercial funds without ID.

## D-010 — Separate product facts from storefront identity

- Date: 2026-09-10
- Decision: Never infer a product's brand, model, specification, colour, size, or compatibility from the seller's storefront name or from a third-party retailer. Use the seller's own item specifics or buyer-approved source data; otherwise keep a visible confirmation placeholder.
- Reason: A quality audit found that the local Voodoo Vixen sample had inserted the storefront brand into a product title even though third-party records attribute that product name to Jawbreaker. The sent email described only the observed duplication and contained no proposed brand or rewritten title, so the unsupported inference did not reach the prospect.
- Control: Treat third-party product pages as leads for verification, not authoritative replacement data. Preserve every unaffected source term when making a narrow correction, and use visible placeholders for ambiguous text. Keep the Voodoo follow-up unprepared until the exact seller listing or a buyer-approved source confirms the brand.
