# Expected-Value Queue

Scales: value in expected seven-day net cash; probability 0–1; time in operator minutes; compute Low/Medium/High.

1. Monitor the 10 tracked Gmail threads for replies, opt-outs, or mission-related bounces; do not infer delivery from Gmail's SENT label.
   - Value if successful: converts or repairs £990 nominal pipeline
   - Probability: 0.10 per lead is a provisional planning weight, not observed conversion
   - Time: 5 minutes per checkpoint
   - Money: £0
   - Compute: Low
   - Dependencies: Gmail connection

2. On a positive reply, deliver the saved three-listing preview or a prospect-specific equivalent, optionally include the claim-safe one-page proof sheet, request explicit agreement for the £99 sprint, and prepare the remaining handoff in the generated listing-rescue workbook.
   - Value if successful: £99 cash per sale
   - Probability: conditional on response
   - Time: 25 minutes
   - Money: £0
   - Compute: Medium
   - Dependencies: prospect reply and listings; use `docs/BUYER_CLOSE_KIT.md`, obey `docs/LISTING_RESCUE_PROOF_SHEET.md`, generate the clean workbook with `tools/build_listing_rescue_workbook.mjs`, and adapt the response to the actual thread. If the buyer agrees, use `docs/INVOICE_READINESS.md` before requesting bank payment.

3. At the 2026-09-11 07:36 BST checkpoint, use the overnight primary evidence to decide whether to launch a three-prospect secondary calibration to LBC Logistics, Totally Floorsome, and Arrow Engineering. Recheck page evidence, refresh the saved preview, and use the matching guarded draft only after every pre-send check passes. Keep FMSG and Live Innovative Solutions behind the 19:35 gate.
   - Value if successful: starts a distinct £149 offer during the next business morning while preserving two secondary reserves; all £745 remains excluded from pipeline until contact
   - Probability: 0.05 per eventual qualified contact is an untested planning estimate
   - Time: 5–10 minutes per activated prospect
   - Money: £0
   - Compute: Medium
   - Dependencies: at least twelve hours since the final primary send; no primary reply requiring immediate fulfilment; no bounce or channel warning; matching file in `docs/secondary_outreach/`; fresh public-page, Gmail, corporate-channel, and suppression checks

4. At the 24-hour checkpoint, inspect response/bounce and any secondary-calibration evidence; either keep the saved Howleys and Pizzazz cross-channel follow-ups queued for revalidation at 48 hours, refine the message/channel, or activate the remaining two secondary prospects.
   - Value if successful: protects deliverability and improves conversion learning
   - Probability: conditional on evidence
   - Time: 20 minutes
   - Money: £0
   - Compute: Medium
   - Dependencies: adequate observation window; recheck the relevant file in `docs/followups/`, the full Gmail thread, `ops/SUPPRESSION.csv`, and every cited page before sending

5. On buyer agreement, offer UK bank transfer first and PayPal invoice only if an existing account is already usable without document verification or a hold that extends beyond the deadline.
   - Value if successful: converts an agreed £99 or £149 service into accessible cash without an ID-dependent signup
   - Probability: conditional on buyer intent and payment-account evidence
   - Time: 10 minutes
   - Money: £0 preferred; record actual PayPal fee if used
   - Compute: Low
   - Dependencies: buyer agreement; Nathan supplies bank details only then, or confirms an existing usable PayPal account

6. If no meaningful response after 20 qualified sends or by day 3, choose between the £149 landing-page patch and the £399 catalogue-workflow pilot based on observed buyer pain; use the fictional three-product proof set only as capability evidence, and activate the eBay-inventory contingency if the user supplies inventory and photographs.
   - Value if successful: £70–£799+
   - Probability: to be measured
   - Time: 60 minutes
   - Money: £0 preferred
   - Compute: Medium
   - Dependencies: experiment threshold, explicit bulk-catalogue pain, or user-supplied inventory
