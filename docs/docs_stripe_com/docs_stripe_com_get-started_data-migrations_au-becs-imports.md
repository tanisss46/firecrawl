# Import AU BECS data

## Migrate your AU BECS data to Stripe, including mandate handling, migration notification, and file formatting requirements.

When you migrate AU BECS data from your previous processor, you import the data
in Stripe as a payment method object (pm_).

## Import the mandates

During the customer onboarding process, businesses must collect a mandate that
authorizes them to debit the account. In the BECS Direct Debit system, these
mandates are called Direct Debit Requests (DDRs).

These mandates or DDRs refer to the original authorized agreement that the
customer and the business have already established.

In migrating payment details to Stripe, we create a new Direct Debit Request for
you to replace your existing direct debit request mandates. This new DDR:

- Represents the same agreement the customer initially authorized for the first
direct debit instruction.
- Requires no new information from the customer. The original agreement stays
the same.

### Account limits

New users are subject to default limits of 1,500 AUD per transaction and 4,500
AUD per week for Australia BECS Direct Debit transactions. If you need higher
limits, let us know in your [migration request
form](https://docs.stripe.com/get-started/data-migrations/pan-import#request-migration).

## Migration notification

Inform your customers about the migration before it happens. The original
approval is sufficient, so they don’t need to give permission again or set up a
new AU BECS Direct Debit mandate.

Reassure your customers that their current mandates are valid and require no
action from them, unless they choose to cancel the mandate.

## AU BECS debit notification

AU BECS regulations require you to [notify your
customers](https://docs.stripe.com/payments/au-becs-debit#debit-notification-emails)
when debiting their AU BECS payment method.

You can choose to have Stripe automatically send this email notification, or you
can send it manually. Stripe requires the customer email address in the
migration data to comply with this regulation.

## AU BECS file guidance

- A processor can provide a number of different fields.
- We advise your processor to provide a full export of all customer and payment
method data to Stripe.
- Stripe can filter out any unnecessary fields from the previous processor’s
data as needed.
- Stripe can merge multiple received files if either the old customer ID or the
old source ID is present in both files.

## File formatting requirements

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
must not denote a missing field with `NULL`, `N/A`, or any other value.
- Escape any double quotes that are part of the content with another double
quote per the CSV RFC. Example: `"William` `""Bard of Avon""` `Shakespeare"`
- Fields can’t contain newline characters (`\r` or `
`) within a field. An example of what to avoid would be: `101 1st Ave
Apt 1`.
- All rows must have the same number of columns.
- Columns support any order.
- You must encrypt sensitive data files with our [PGP
key](https://docs.stripe.com/get-started/data-migrations/pan-import#migration-pgp-key)
before submitting them through SFTP.

## AU BECS data fields

FieldRequiredAdditional infoOld customer IDRequiredWe create a customer ID for
each unique old customer ID provided.NameRequiredWe must include the name of the
person on the mandate.Account NumberRequiredThe bank account number.BSB
NumberRequiredThe 6 digit bank state branch number of the bank
account.EmailRequiredAU BECS requires you to email a notification to the
customer upon signup and debit of their AU BECS payment method. Stripe can send
this email notification automatically or you can manually send it.Stripe
customer IDOptionalStripe customer ID to map the mandates to if required.Old
source IDOptionalUnique representation of a payment method.Address line
1OptionalFirst line of the address for the customer’s AU BECS mandate.Address
line 2OptionalSecondary details of the address for the customer’s AU BECS
mandate.CityOptionalCity address for the customer’s AU BECS
mandate.StateOptionalState of the address for the customer’s AU BECS
mandate.PostalOptionalZip code of the address for the customer’s AU BECS
mandate.CountryOptionalMust be in the form of the ISO 2 letter country
code.PhoneOptionalPhone number of the account holder.Customer/AU BECS
MetadataOptionalAny additional metadata.

## Links

- [Request a payment data
import](https://docs.stripe.com/get-started/data-migrations/pan-import)
- [AU BECS](https://docs.stripe.com/payments/au-becs-debit)
- [migration request
form](https://docs.stripe.com/get-started/data-migrations/pan-import#request-migration)
- [notify your
customers](https://docs.stripe.com/payments/au-becs-debit#debit-notification-emails)
- [PGP
key](https://docs.stripe.com/get-started/data-migrations/pan-import#migration-pgp-key)