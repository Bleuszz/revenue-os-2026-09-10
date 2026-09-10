# Payment collection — no-ID operating path

Last reviewed: 2026-09-10 19:49 Europe/London

## Standing constraint

Assume Nathan cannot complete photo-ID or selfie verification. Do not open or depend on a payment service that requires identity documents unless payment is otherwise impossible and Nathan explicitly changes this constraint. Ordinary 18+ account eligibility does not imply access to an ID card.

## Route 1 — direct UK bank transfer

Use this first when a buyer agrees the scope.

1. Confirm the legal buyer name, service, price, delivery deadline, and revision terms in writing.
2. Ask whether the buyer can pay by UK bank transfer.
3. Complete the legal, VAT, buyer, and bank fields in `INVOICE_READINESS.md`; Nathan verifies every user-only field before the invoice is issued.
4. Nathan provides the account-holder name, sort code, account number, and a unique payment reference directly at that point. Do not store those details in this repository or reusable prospect notes.
5. Tell the buyer that work beyond the promised free preview begins when cleared funds are visible.
6. Verify receipt inside Nathan's actual bank account. An email, message, PDF, or screenshot saying `paid` is not payment evidence.
7. Record gross cash, any observed bank charge, cleared/accessibility status, and net cash in `ops/FINANCE.md`.

Expected platform fee: £0, subject to Nathan's own bank terms. Faster Payments operates continuously, but actual arrival and accessibility must be observed rather than assumed.

Security controls:

- Prefer a business account if Nathan already has one; do not open a new bank account for this mission.
- If using a personal account, Nathan must first check that its terms allow business receipts; GOV.UK notes that either may be possible and directs users to check with their bank.
- Give the account-holder name exactly as held by the bank so the buyer can use Confirmation of Payee where available.
- Never announce changed bank details in an existing email thread without a second verification channel.
- Never request the buyer's online-banking credentials, card number, PIN, password, or one-time code.

## Route 2 — existing PayPal account

Use only if Nathan already has a PayPal account that can receive a commercial payment without document verification and the proceeds are expected to become accessible before the mission deadline.

Preferred method: a PayPal invoice describing the agreed service, price, delivery window, and revision. Do not ask a commercial buyer to mark the transaction as friends and family.

Current planning assumptions from PayPal UK's published fee page:

- Standard domestic `all other commercial transactions`: 2.9% plus £0.30.
- A £99 payment would therefore net about £95.83 before any other adjustment.
- A £149 payment would therefore net about £144.38 before any other adjustment.

These are forecasts only. Record the actual fee and accessible balance shown by PayPal. PayPal says initial payments for new or inactive sellers can be held for up to 21 days and identity confirmation may be required, so a new PayPal setup is not a dependable seven-day route.

Verification controls:

- Check the transaction by signing in to PayPal directly; do not trust a payment email or screenshot.
- Confirm status, fee, reserve/hold, dispute state, and whether funds can be withdrawn.
- A held, pending, reversed, or inaccessible balance is not recovered cash.

## Route 3 — Stripe

Inactive. The existing account is authenticated only in its sandbox and live activation requires photo-ID/selfie verification. Do not continue activation, create a live Payment Link, or use any exposed test key under the standing no-ID constraint.

## Buyer-facing payment language

After explicit agreement:

> Thanks — the £99 listing-rescue scope is confirmed: 15 listings, the agreed QA/copy handoff, one revision, and delivery within 24 hours of cleared payment. I can take UK bank transfer, or PayPal invoice if that is easier. Which do you prefer?

Do not send payment instructions before a buyer has agreed the scope. Do not call an invoice, request, promised transfer, pending balance, or screenshot `cash received`.
