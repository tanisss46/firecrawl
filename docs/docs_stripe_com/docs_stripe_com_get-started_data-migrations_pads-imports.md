# Import PADs/ACSS Data

## Mandate requirements

[Payments Canada Rules for pre-authorized
debits](https://www.payments.ca/sites/default/files/h1eng.pdf) (PADs) require
businesses to present a mandate agreement with clear and specific terms for
one-time or recurring debits prior to debiting a customer’s bank account. After
you collect customer agreement, this
[mandate](https://docs.stripe.com/payments/acss-debit#mandates) gives your
business authorization to debit the customer’s bank account on a specified
schedule. The mandate includes the customer’s institution number, transit
number, account number, name and email.

Stripe can only import the PADs that you confirm you hold the mandates for.
After determining mandate status for all, some, or none of the bank accounts,
inform us so we can instruct you which steps to take next.

## Migration Notification

You must notify your customers that you’re migrating payment processing to
Stripe.

## Debiting PADs/ACSS

In our [intake form](https://support.stripe.com/contact/email?topic=migrations),
choose how you’ll debit the PADs:

- **Only for automatic** use with invoices, subscriptions, or recurring payment
schedules.
- **Only for on-demand** customer-initiated payments.
#### Note

You can’t debit these PADs for automatic use with invoices, subscriptions, or
recurring payment schedules.
- **For both** on-demand customer-initiated payments and automatic use with
invoices, subscriptions, or recurring payment schedules.

## PADs/ACSS file guidance

- A processor can provide a number of different fields.
- We advise your processor to provide a full export of all customer and payment
method data to Stripe.
- Stripe can filter out any unnecessary fields from the previous processor’s
data as needed.
- Stripe can merge multiple received files if either the old customer ID or the
old source ID is present in both files.
- Stripe can only import PADs that are pre-authorized because verification is a
requirement of ACSS scheme rules.

### File formatting requirements

Export data files must meet the following data standards for us to proceed with
an import:

- The file must be in CSV format.
- The file must be UTF-8 encoded.
- Delimit rows by a single newline character `
` (not `\r
`).
- Delimit columns by `,`
- You must wrap all fields containing commas in double quotes `"`. We recommend
wrapping all fields in double quotes.
- Leave empty fields entirely empty (no character in between delimiters). You
must *not* denote a missing field with `NULL`, `N/A`, or any other value.
- Escape any double quotes that are part of the content with another double
quote per the CSV RFC. For example: `"``William` `""``Bard of Avon``""`
`Shakespeare``"`
- Fields can’t contain newline characters (`\r` or `
`) within a field. Example of what to avoid: `101 1st Ave
Apt 1`
- All rows must have the same number of columns.
- Columns support any order.
- You must encrypt sensitive data files with our [PGP
key](https://docs.stripe.com/get-started/data-migrations/pan-import#migration-pgp-key)
before submitting through SFTP.

## PADs/ACSS data fields

FieldRequiredAdditional infoOld customer IDRequiredWe create a customer ID for
each unique old customer ID provided.Institution NumberRequiredThe 3-digit
institution number identifies your bank.Transit NumberRequiredThe transit number
(5 digits) identifies the branch where you opened your account.Account
NumberRequiredThe account number (11 digits) identifies your individual
account.EmailRequired/Optional1Additional metadata (Optional if full address is
provided instead).Address line 1Required/Optional1Additional metadata (Optional
if email is provided instead).Address line 2Required/Optional1Additional
metadata (Optional if email is provided
instead).CityRequired/Optional1Additional metadata (Optional if email is
provided instead).StateRequired/Optional1Additional metadata (Optional if email
is provided instead).PostalRequired/Optional1Additional metadata (Optional if
email is provided instead).CountryRequired/Optional1Additional metadata
(Optional if email is provided instead).PhoneOptionalAdditional
metadataNameOptionalAdditional metadataStripe customer IDOptionalAdditional
metadataOld source IDOptionalAdditional metadataDescriptionOptionalAdditional
metadataCustomer metadataOptionalAny additional metadata
1 Either the customer email address or their full address must be present within
the data file to import PADs/ACSS. If you provide neither an email address nor a
full address, the PAD fails to import.

## PADs/ACSS Data Migration Certification and Disclaimer Language

By submitting the [PADs/ACSS Data Migration intake
form](https://support.stripe.com/contact/email?topic=migrations), you certify
that all of the following statements are true and that you have authority to
make these statements.

You agree to comply with [Rule
H1](https://www.payments.ca/sites/default/files/h1eng.pdf) of Payments Canada
and the other
[Rules](https://www.payments.ca/systems-services/rules-documentation?field_rules_type=170&field_category_type=All)
of Payments Canada that supplement Rule H1 (“PAD Rules”) when using Stripe
services to process Pre-Authorized Debits (“PADs”).

You understand that you, as the Payee (as defined in the PAD Rules), are solely
responsible for collecting and retaining PAD authorizations from your customers
that comply with the PAD Rules, as described in Stripe’s [ACSS Payment Method
Terms](https://stripe.com/en-de/legal/pad) and [mandate agreement
requirements](https://docs.stripe.com/payments/acss-debit/custom-pad-agreement#mandate-agreement-requirements).

If you don’t meet the PAD rules requirements for previously-collected
authorizations, you understand that you must collect new authorizations before
processing PADs on Stripe.

For authorizations collected prior to migration to Stripe, you must provide
Stripe with evidence of any relevant authorization for PAD transactions upon
request. When contesting a dispute, you are solely responsible for providing a
copy of the authorization.

## Links

- [Request a payment data
import](https://docs.stripe.com/get-started/data-migrations/pan-import)
- [Payments Canada Rules for pre-authorized
debits](https://www.payments.ca/sites/default/files/h1eng.pdf)
- [mandate](https://docs.stripe.com/payments/acss-debit#mandates)
- [intake form](https://support.stripe.com/contact/email?topic=migrations)
- [PGP
key](https://docs.stripe.com/get-started/data-migrations/pan-import#migration-pgp-key)
-
[Rules](https://www.payments.ca/systems-services/rules-documentation?field_rules_type=170&field_category_type=All)
- [ACSS Payment Method Terms](https://stripe.com/en-de/legal/pad)
- [mandate agreement
requirements](https://docs.stripe.com/payments/acss-debit/custom-pad-agreement#mandate-agreement-requirements)