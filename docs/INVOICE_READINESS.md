# UK bank-transfer invoice readiness

Prepared: 2026-09-10 20:41 Europe/London

Use only after a buyer has agreed the service, price, inputs, delivery trigger,
and payment method in writing. This checklist does not determine Nathan's tax,
VAT, employment, or banking status.

## User-only facts required before issue

Nathan supplies or confirms these at the point of sale. Do not store them in Git:

- Legal name and any trading name actually used.
- An invoice address and contact details. If a business name is used as a sole
  trader, include an address where legal documents can be delivered.
- VAT-registration status. Never charge or itemise VAT without confirmation that
  it applies and that the invoice contains the required VAT information.
- Whether the intended bank account may be used for business receipts under its
  terms, plus account name, sort code, and account number.

## Buyer facts to confirm

- Legal company or trading name.
- Billing address.
- Accounts-payable email or portal, if different from the sales contact.
- Purchase-order number if the buyer requires or supplies one.
- Agreed payment terms and due date.

## Required invoice fields

The issued invoice should contain:

- The word `Invoice` and a unique sequential identification number.
- Invoice date and the accurate service supply date or service period.
- Supplier name, address, and contact information.
- Customer name and address.
- A clear service description, quantity or scope, and amount charged.
- VAT amount if applicable and the total amount owed.
- Agreed payment due date and payment instructions.

For the primary offer, describe the line item as:

`Listing rescue sprint: 15 listing title/copy revisions, item-specific QA flags,
structured Excel handoff, and one revision pass. Buyer approves all copy before
publishing. No marketplace access.`

## Copy-ready shell

```text
INVOICE

Invoice number: [UNIQUE SEQUENTIAL NUMBER]
Invoice date: [YYYY-MM-DD]
Supply date or agreed service period: [ENTER ACCURATELY]
Due date: [AGREED DATE]
Purchase order: [IF SUPPLIED]

From:
[LEGAL NAME]
[TRADING NAME, IF USED]
[ADDRESS]
[CONTACT DETAILS]

Bill to:
[BUYER LEGAL/TRADING NAME]
[BILLING ADDRESS]
[ACCOUNTS-PAYABLE CONTACT]

Description: Listing rescue sprint — 15 listings, structured copy/QA handoff,
one revision, delivery within 24 hours of cleared payment and receipt of the
required inputs. Buyer approval is required before publishing.
Quantity: 1
Subtotal: £99.00
VAT: [ENTER ONLY AFTER CONFIRMING VAT TREATMENT]
Total due: [CALCULATE FROM CONFIRMED VAT TREATMENT]

Payment method: UK bank transfer
Account name: [NATHAN ENTERS]
Sort code: [NATHAN ENTERS]
Account number: [NATHAN ENTERS]
Payment reference: [USE INVOICE NUMBER OR OTHER UNIQUE REFERENCE]

No bank-detail change will be made by email. Work beyond the free preview begins
after cleared funds are visible in the named account.
```

## Issue and evidence controls

1. Re-read the buyer agreement and confirm the invoice matches it exactly.
2. Check the recipient address or required accounts-payable route.
3. Have Nathan enter and verify every legal, VAT, address, and bank field.
4. Save the issued invoice and agreement outside Git with access limited to what
   is needed for bookkeeping and fulfilment.
5. Record an issued invoice as pending only. Do not count it as cash or an
   agreement that did not already exist.
6. Count cash only after the actual bank account shows cleared, accessible funds;
   record the amount and evidence reference in `ops/FINANCE.md`.
7. Retain accurate income evidence, which may include invoice copies, buyer
   emails, and bank statements.

## Official sources checked 2026-09-10

- GOV.UK invoice contents and sole-trader fields:
  https://www.gov.uk/invoicing-and-taking-payment-from-customers/invoices-what-they-must-include
- GOV.UK trading allowance and income-record examples:
  https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income
- GOV.UK self-employed record requirements:
  https://www.gov.uk/self-employed-records/what-records-to-keep
- Office of the Small Business Commissioner invoicing guide:
  https://www.smallbusinesscommissioner.gov.uk/help-and-guidance/all-advice/a-guide-for-effective-invoicing/
