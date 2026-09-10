# Risk Register

| Risk | Likelihood | Impact | Control | Trigger |
|---|---:|---:|---|---|
| No buyer within seven days | High | High | Favour urgent, high-trust, fast-fulfilment offers; test early | No meaningful signal by day 3 |
| Payment path unavailable | Medium | High | Default to user-controlled UK bank transfer after agreement; use only an already-usable PayPal account as fallback; treat Stripe as inactive | Positive buying intent or buyer cannot use bank transfer |
| Cold outreach is irrelevant or non-compliant | Medium | High | Low volume, public business channels, specific relevance, honest identity, opt-out, suppression log | Complaint, opt-out, bounce pattern |
| User identity/authority is overstated | Low | High | Use only verified name/account; make no experience or company claims | Any claim requiring proof |
| AI output quality fails customer need | Medium | High | Human-style review, scoped deliverable, factual verification | Sample defect or prospect objection |
| Compute depletion | Low at start | High | Batch research, persist state, use scripts for deterministic work | >35% used before day 3 |
| Capital leakage | Low | Medium | £0-first tests; log before/after spend | Any proposed paid tool/account |
| Secrets or customer data enter Git | Low | High | `.gitignore`, pre-commit inspection, minimal stored data | Before every push |
| Email reputation damage | Medium | High | Small batches, personalised content, no deceptive urgency, pause at 10 sends for an observation window, stop on negative signals | No engagement after 24 hours, any complaint, or bounce pattern |
| Stripe test key exposure in UI output | Medium | Medium | Key was not copied, used, or stored; do not use it and have the user rotate it in the Stripe Dashboard | Before any Stripe API work or after activation |
| PayPal hold or identity gate misses deadline | High for a new/inactive seller | High | Do not create or rely on a fresh account; verify commercial-payment eligibility, hold status, withdrawal access, and actual fee before offering it | Buyer requests PayPal or account shows a limitation |
| Fake bank-transfer confirmation | Medium | High | Verify cleared funds only inside Nathan's bank account; ignore screenshots and payment-notification emails as proof | Buyer claims payment was sent |
| Bank details leaked or fraudulently changed | Low | High | Keep details out of Git and reusable notes; Nathan supplies them only after agreement; verify any later change on a second channel | Any request to change payee details or resend them |
