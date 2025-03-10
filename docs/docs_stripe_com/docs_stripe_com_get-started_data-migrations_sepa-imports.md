# Import SEPA Data

Stripe migrates all SEPA payment data as payment methods. This guide provides
instructions for migrating your existing SEPA mandates from your previous
payment processors into Stripe.

## Importing the mandates

In the context of SEPA, mandates refer to the original authorized agreement that
the customer and the business have already established.

In Stripe, *creating a new mandate object* doesn’t mean creating a new mandate
from scratch. On import, we create a new *mandate object* that:

- Uses the same `mandate_reference` as your original agreement.
- Represents the same agreement the customer initially authorized for the first
direct debit instruction.

No new information is required from the customer. The original agreement stays
the same.

### Creditor ID

A SEPA Creditor Identifier (Creditor ID) is an ID associated with each SEPA
Direct Debit payment that identifies the company requesting the payment. While
companies might have multiple creditor identifiers, each creditor identifier is
unique and allows your customers to identify the debits on their account.

By default, your Stripe account uses a Stripe Creditor ID when collecting SEPA
Direct Debit Payments. **Stripe Payments** appears on bank statements alongside
your configurable [Stripe statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors).
We recommend that you:

- Configure a recognizable statement descriptor to make sure customers recognize
payments and to reduce the risk of disputes.
- Use your own Creditor ID to reduce dispute rates and improve your customer’s
recognition of their payment to you.
- If you’re using the Stripe Creditor ID, use Stripe Checkout to collect
mandates from your customers for SEPA Direct Debits.

You can configure your own Creditor ID in the [Payment Method
Settings](https://dashboard.stripe.com/settings/payment_methods) page. When
using your own Creditor ID, your name appears on statements instead of Stripe’s.

#### Example SEPA Bank Mandate if using Stripe’s Creditor ID

```
From Account
Account name: CURRENT-ACCOUNT
BIC: BANBICKIEXXXXX
IBAN: IE11BANK11111111111111

Originator Details
Originator name: Stripe Payments Europe Ltd
Creditor Identifier: BE111111111111
The Creditor Identifier is a unique identifier used by
the company to process collections.

UMR: UMR123 PSP
The Unique Mandate Reference (UMR) is specific to the
mandate you have signed and identifies each direct
debit mandate.

Additional details
Status: Active

```

#### Example SEPA Bank Mandate if using your own Creditor ID

```
From Account
Account name: CURRENT-ACCOUNT
BIC: BANBICKIEXXXXX
IBAN: IE11BANK11111111111111

Originator Details
Originator name: Merchant Creditor ID Name
Creditor Identifier: BE222222222222
The Creditor Identifier is a unique identifier used by
the company to process collections.

UMR: UMR123 PSP
The Unique Mandate Reference (UMR) is specific to the
mandate you have signed and identifies each direct
debit mandate.

Additional details
Status: Active

```

## Migration notification

Inform your customers about the migration before it happens. They don’t need to
give permission again or set up a new SEPA Direct Debit mandate. The approval
you already have is sufficient.

### General guidelines for communication:

Point out any changes such as:

- Creditor ID if you opt for Stripe’s Creditor ID
- Creditor name if you opt for Stripe’s Creditor ID
- Recipient bank IBAN

Make sure the communication reassures customers their current mandates are valid
without requiring any action from them, unless they choose to cancel the
mandate.

## SEPA debit notification

SEPA rules state that you must [notify your
customers](https://docs.stripe.com/payments/sepa-debit#debit-notification-emails)
when debiting their SEPA payment method.

By default, Stripe automatically sends these email notifications on your behalf.

## SEPA file guidance

- A processor can provide a number of different fields.
- We advise your processor to provide a full export of all customer and payment
method data to Stripe.
- Stripe can filter out any unnecessary fields from the previous processor’s
data as needed.
- Stripe can merge multiple received files if either the old customer ID or the
old source ID is present in both files.

### File formatting requirements

Export data files must meet the following data standards for us to proceed with
an import:

- The file must be in CSV format.
- The file must be UTF-8 encoded.
- Delimit rows by a single newline character `
` (not `\r
`).
- Delimit columns by a comma (`,`).
- You must wrap all fields containing commas in double quotes (`"`). We
recommend wrapping all fields in double quotes.
- Leave empty fields entirely empty (no character in between delimiters). You
must *not* denote a missing field with `NULL`, `N/A`, or any other value.
- Escape any double quotes that are part of the content with another double
quote per the CSV RFC. Example: `"``William` `""``Bard of Avon``""`
`Shakespeare``"`
- Fields can’t contain newline characters (`\r` or `
`) within a field. An example of what to avoid would be: `101 1st Ave
Apt 1`.
- All rows must have the same number of columns.
- Columns support any order.
- You must encrypt sensitive data files with our [PGP
key](https://docs.stripe.com/get-started/data-migrations/pan-import#migration-pgp-key)
before submitting them through SFTP.

### SEPA data Fields

FieldRequiredAdditional infoOld customer IDRequiredWe create a customer ID for
each unique old customer ID provided.NameRequiredWe must include the name of the
person on the mandate.IBANRequiredFollow Stripe’s valid IBAN structure.Mandate
referenceRequiredExisting mandate reference IDEmailRequiredSEPA requires you to
email a notification to the customer upon debiting their SEPA payment method.
Stripe can send this email notification automatically or you can manually send
it.Address line 1Required**Mandatory for non EU IBANsCountryRequired**Mandatory
for non EU IBANs. This must be in the form of the ISO 2 letter country
code.PostalOptionalAdditional metadataCountryOptionalAdditional
metadataPhoneOptionalAdditional metadataAddress line 2OptionalAdditional
metadataStateOptionalAdditional metadataStripe customer IDOptionalAdditional
metadataOld source IDOptionalAdditional metadataCustomer/SEPA
MetadataOptionalAny additional metadata

## Links

- [Request a payment data
import](https://docs.stripe.com/get-started/data-migrations/pan-import)
- [Stripe statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
- [Payment Method
Settings](https://dashboard.stripe.com/settings/payment_methods)
- [notify your
customers](https://docs.stripe.com/payments/sepa-debit#debit-notification-emails)
- [PGP
key](https://docs.stripe.com/get-started/data-migrations/pan-import#migration-pgp-key)