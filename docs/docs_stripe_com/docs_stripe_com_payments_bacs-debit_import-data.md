# Import Bacs data to Stripe

## Learn how to import your Bacs data from your current payment processor to Stripe.

You can migrate your data from your current payment processor to your Stripe
account using the Bacs bulk change process. We work with other payment
processors and Bacs sponsor banks throughout the migration to securely migrate
your Bacs data. A Bacs migration takes at least 6 weeks to complete.

To export Bacs data from Stripe to another payment processor, see [Export Bacs
data from Stripe](https://docs.stripe.com/payments/bacs-debit/export-data).

[Submit your Bacs import migration
request](https://docs.stripe.com/payments/bacs-debit/import-data#submit-bacs-request)
Start the migration process by submitting a data migration request.

- Navigate to the [Stripe Support form for data
migrations](https://support.stripe.com/contact/email?topic=migrations). If
you’re not signed in, select **Sign in** and enter the credentials of the
account that you want to migrate your data to.
- Select **Import data from a third party into a Stripe account**.
- Select **Bacs** as the data type you want to import.
- Complete the remaining fields and select **Send email**.

Within three days of receiving your request, our Data Migrations team emails you
to request a signed Bulk Change Deed.

You need a Service User Number (SUN) on Stripe to migrate your Bacs data to your
Stripe account. You can either use Stripe’s shared SUN or upgrade to Custom
Branding and use a custom SUN.

SUN typeDescriptionPriceStripe’s shared SUNStripe’s name will appear on
statements, payment pages, and emails.FreeCustom SUNAdd your business’s name and
brand on statements, payment pages, and emails.50 GBP per active month
To use Stripe’s shared SUN, select this option when initiating your migration
request.

To request your own custom SUN on Stripe:

- In the Dashboard, navigate to [Payment
Methods](https://dashboard.stripe.com/test/settings/payment_methods).
- Expand Bacs Direct Debit and click **Configure**.
- Select the option to upgrade your Bacs Direct Debit plan.
- Specify your Business Display Name.
- Specify your Business Support Email.
- Check the box to confirm that you understand the conditions and select
**Customise**.
[Print, sign, and send your Bulk Change
Deed](https://docs.stripe.com/payments/bacs-debit/import-data#sign-bulk-change-deed)
To complete the migration, your current Bacs provider needs to sign a bulk
change deed. This agreement authorizes the transfer of your mandates from your
current payment processor to Stripe.

#### Caution

[Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Fimport-data)
to download the Bulk Change Deed.

[Determine your switch
date](https://docs.stripe.com/payments/bacs-debit/import-data#determine-switch-date)
After we receive your Bulk Change Deed, Stripe’s Data Migrations team works with
you, your current payment processor, and our sponsor bank to agree on a switch
date. The actual import into Stripe takes place on your switch date.

[Send communications to your
customers](https://docs.stripe.com/payments/bacs-debit/import-data#send-communications)
The Letter to Payers explains why the migration is needed, how it affects
Payers, and the Direct Debit Guarantee.

Download the pre-approved Letter to Payers template and send it to your
customers at least 2 days before your switch date. You can’t make any edits
outside of the highlighted fields. If you want to make edits to the Letter to
Payers, a review is required by Stripe’s sponsor bank.

#### Caution

[Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Fimport-data)
to download the Letter to Payers template.

You can decide how to communicate the letter to your customers. For example
email, mail, and text message are all valid communication options. Not alerting
payers to this change can result in failed payments and disputes.

The payer might see two references to the business in the bank portal for 1-3
business days when Stripe imports the business’s existing mandates. This is
because one is the mandate with the former provider, and the other is Stripe’s
mandate.

[Wait for your data
import](https://docs.stripe.com/payments/bacs-debit/import-data#wait-for-import)
Your current payment processor needs to send on your existing mandates and
payers bank account details after we’ve gained authority for them.

Your current payment processor cancels your mandates and our Data Migrations
team completes the import of these mandates on the agreed-upon date. Our Data
Migrations team sends you a confirmation email when your import is complete. You
can’t charge your customers on your current payment processor after they cancel
the mandates on the switch date.

This table shows the Bacs timeline in business days from the time (T) that a
payment is made to when a new mandate must be collected:

T+0Migration complete and mandate submittedT+3Mandate is active and the payment
is submittedT+5Funds leave the customer’s bank accountT+6Funds are available in
Stripe
Timelines and document information might differ when exporting data from Stripe
to a new payment processor. See [Export Bacs data from
Stripe](https://docs.stripe.com/payments/bacs-debit/export-data) for more
information.

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

## Bacs data fields

FieldRequiredAdditional infoOld customer IDRequiredWe create a customer ID for
each unique old customer ID provided.NameRequiredMust include the first and last
name of the person on the mandate.Sort codeRequiredMust be 6 digits in length
and include leading zeros.Account numberRequiredMust be 8 digits in length and
include leading zeros.EmailRequiredStripe requires your customer’s email so we
can send out notifications. Contact us if your customers don’t have email
addresses.Address line 1RequiredFirst line of the address for the customer’s
Bacs mandate.CityRequiredCity address for the customer’s Bacs
mandate.PostalRequiredZip code of the address for the customer’s Bacs
mandate.CountryRequiredMust be in the form of the ISO 2 letter country
code.PhoneOptionalPhone number of the account holder.Address line
2OptionalSecondary details of the address for the customer’s Bacs
mandate.StateOptionalState of the address for the customer’s Bacs mandate.DDI
dateOptionalAdditional metadata (date the Bacs mandate was created).Date of
first collectionOptionalAdditional metadata (date the mandate was first
charged).Stripe customer IDOptionalStripe customer ID to map the mandates to if
required.Old source IDOptionalUnique representation of a payment
method.Customer/Bacs MetadataOptionalAny additional metadata.

## Links

- [Export Bacs data from
Stripe](https://docs.stripe.com/payments/bacs-debit/export-data)
- [Stripe Support form for data
migrations](https://support.stripe.com/contact/email?topic=migrations)
- [Payment Methods](https://dashboard.stripe.com/test/settings/payment_methods)
- [Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Fimport-data)
- [PGP
key](https://docs.stripe.com/get-started/data-migrations/pan-import#migration-pgp-key)