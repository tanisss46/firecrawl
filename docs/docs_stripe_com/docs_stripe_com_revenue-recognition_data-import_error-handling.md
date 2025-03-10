# Error handling for data import

## Learn how to handle and recover from errors received when importing revenue recognition data.

You might encounter errors when importing revenue recognition data. The
following list describes data import errors and how to resolve them. In most
cases, you need to reimport the data to recover from the error.

## General imports

The following list contains errors you might encounter with general imports and
how you can resolve them.

### CSV file errors

The table below describes the errors related to the CSV file and how to handle
them.

ErrorDescriptionRecommendationEmpty fileThe CSV file doesn’t contain any lines
(rows) or a header. It’s a zero-length file.[Download the CSV
template](https://dashboard.stripe.com/revenue-recognition/data-import) from the
Stripe Dashboard and add your transaction data. See [Importing
data](https://docs.stripe.com/revenue-recognition/data-import#general-import)
for data format details.
Invalid data

A line in the CSV file contains invalid data.

Make sure each line includes:

- a `transaction_id`
- a date in the YYYY-MM-DD format
- a valid amount
- the currency’s three-letter ISO format

If you’re managing your data with Microsoft Excel, check that it didn’t
automatically change the date format before you import the data. The date must
be in the YYYY-MM-DD format.

See [Importing
data](https://docs.stripe.com/revenue-recognition/data-import#general-import)
for data format details.

Invalid fileCouldn’t read the CSV file.[Download the CSV
template](https://dashboard.stripe.com/revenue-recognition/data-import) from the
Stripe Dashboard and add your transaction data. See [Importing
data](https://docs.stripe.com/revenue-recognition/data-import#general-import)
for data format details.Unknown failureThe CSV file failed to import due to
unknown reasons. Some transactions might not have been imported.Please [contact
Stripe support](https://support.stripe.com/contact) for help.
### Transaction ID errors

The table below describes the errors related to transaction IDs when doing
general imports and how to handle them.

ErrorDescriptionRecommendation
Invalid transaction ID

The transaction ID doesn’t refer to any Stripe transaction.

Make sure the ID is correct.

If you’re importing third-party transactions, you must change the source to a
different identifier than `Stripe`. See [Importing
data](https://docs.stripe.com/revenue-recognition/data-import#general-import)
for data format details.

Overriding a charge linked to an invoiceA charge is linked to an invoice.A
charge that’s linked to an invoice can’t be overridden. Instead, override the
invoice.Transaction doesn’t existThe transaction ID couldn’t be found in test or
live mode.Make sure the ID is correct. If it does exist, switch to the
appropriate mode ([test or live](https://docs.stripe.com/keys#test-live-modes))
and reimport the transaction.Unsupported characterThe tilde (`~`) character is
reserved for Stripe internal usage only.Use another character in the transaction
ID.
### Split transaction ID errors

The table below describes the errors related to split transaction IDs and how to
handle them.

ErrorDescriptionRecommendation
Duplicate split transaction IDs

There are duplicate split transaction IDs.

If you’re overriding the service period for an invoice line item, make sure the
invoice line item IDs are correct.

If you’re splitting a transaction, use unique identifiers for each split
transaction.

Missing split transaction ID

A split transaction ID is missing.

If you’re overriding the service period for an invoice line item, use the
invoice line item ID.

If you’re splitting a charge, use unique identifiers for each split transaction.

Split transaction doesn’t existThe split transaction ID couldn’t be found in
test or live mode.Make sure the ID is correct. If it does exist, switch to the
appropriate mode ([test or live](https://docs.stripe.com/keys#test-live-modes))
and reimport the transaction.
Split transaction mismatch

There’s a split transaction mismatch.

Check the split transaction ID and see that it matches what was imported.

If you want to resplit the transaction, delete the existing transactions and
reimport it.

Unsupported characterThe tilde (`~`) character is reserved for Stripe internal
usage only.Use another character in the split transaction ID.
### Booked date errors

The table below describes the errors related to booked dates and how to handle
them.

ErrorDescriptionRecommendationMissing booked dateA booked date is missing from a
third-party transaction.Check and see if there’s a booked date for the
transaction.Nonempty booked dateThere is a booked date for a Stripe invoice when
none is expected.The booked date of a Stripe invoice can’t be overridden. The
field must be empty.
### Recognition date errors

The table below describes the errors related to recognition start and end dates
and how to handle them.

ErrorDescriptionRecommendationMissing recognition end dateA recognition end date
is missing from a third-party transaction.Check and see if there’s a recognition
end date for the transaction. If you’re overriding a Stripe transaction, you
must provide both the recognition start date and end date.Missing recognition
start dateA recognition start date is missing from a third-party
transaction.Check and see if there’s a recognition start date for the
transaction. If you’re overriding a Stripe transaction, you must provide both
the recognition start date and end date.Recognition end date is earlier than
start dateThe recognition end date can’t be earlier than the start date.Make
sure the start and end dates are correct.
### Amount errors

The table below describes the errors related to transaction amounts and how to
handle them.

ErrorDescriptionRecommendationAmount mismatchThe amount doesn’t match the actual
amount of the transaction.The amount of a Stripe transaction can’t be
overridden. The field must be empty.Missing amountAn amount is missing from a
third-party transaction.Check and see if there’s an amount for the
transaction.Total amount mismatchThe amounts of all split transactions don’t sum
up to the total amount of the split charge.Check that all amounts match.
### Currency errors

The table below describes the errors related to currency and how to handle them.

ErrorDescriptionRecommendationCurrency mismatchThe currency doesn’t match the
actual currency of the transaction.The currency of a Stripe transaction can’t be
overridden. The field must be empty.Missing currencyCurrency is missing from a
third-party transaction.Check and see if there’s currency for the transaction.
Make sure to use the currency’s three-letter ISO format.Unsupported currencyThe
currency you provided is not supported for your account.Convert it to one of the
currencies listed in the error message. See [Supported
currencies](https://docs.stripe.com/currencies) for more details.
## Exclusion imports

The following list contains errors you might encounter with exclusion imports
and how you can resolve them.

## Transaction ID errors

The table below describes the errors related to transaction IDs when doing
exclusion imports and how to handle them.

ErrorDescriptionRecommendationInvalid transaction IDThe transaction ID doesn’t
refer to a Stripe transaction.Make sure the ID is correct, according to the
[data format
requirements](https://docs.stripe.com/revenue-recognition/data-import#general-import).Unsupported
exclusion for charge or payment with an invoiceYou can’t exclude a charge or
payment that’s linked to an invoice. Instead, exclude the invoice.Find the
invoice ID for the charge or payment and exclude the invoice ID.

## Links

- [Download the CSV
template](https://dashboard.stripe.com/revenue-recognition/data-import)
- [Importing
data](https://docs.stripe.com/revenue-recognition/data-import#general-import)
- [contact Stripe support](https://support.stripe.com/contact)
- [test or live](https://docs.stripe.com/keys#test-live-modes)
- [Supported currencies](https://docs.stripe.com/currencies)