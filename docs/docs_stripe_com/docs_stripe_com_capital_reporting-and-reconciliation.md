# Reporting and ReconciliationPrivate preview

## Learn how to report on and reconcile Capital transactions.

Throughout the lifecycle of a Capital financing offer, there are three types of
transactions:

- **Payout**: A payout occurs when funds are disbursed to the connected account
in accordance with their accepted financing agreement.
- **Paydown**: A paydown is a payment towards paying down the financed amount.
- **Reversal**: A reversal occurs when a payout or paydown transaction is
reversed.

Stripe exposes Capital transactions so you can provide reporting to connected
accounts (users). You might want to include Capital transactions in your
platform or accounting software so your users can reconcile their transactions.

We offer two options for fetching transactions:

- [Financing Transactions
API](https://docs.stripe.com/api/capital/financing_transactions): We recommend
using the Financing Transactions API, which includes extra transaction
information specific to Capital.
- [Balance Transactions API](https://docs.stripe.com/api/balance_transactions):
If you already have an integration with the Balance Transactions API, Capital
Balance Transactions return most transaction types, but they lack additional
detail (such as the associated Capital [Financing
Offer](https://docs.stripe.com/api/capital/connect_financing_object)).
Financing TransactionsRecommendedBalance Transactions
## Payout transactions

When you enable an automatic [payout](https://docs.stripe.com/payouts) schedule,
your connected account receives their financing payout automatically. Otherwise,
you need to [Create a payout](https://docs.stripe.com/api/payouts/create) of
`source_type=financing` to manually pay out the user’s financing.

Financing payouts have a corresponding [Financing
Transaction](https://docs.stripe.com/api/capital/financing_transaction_object)
of type `payout`. After a `payout` Financing Transaction is created, Stripe
sends a [capital.financing_transaction.created
webhook](https://docs.stripe.com/api/events/types#event_types-capital.financing_transaction.created).
However, it might take several business days for the ACH funds to arrive in the
connected account’s bank account.

## Paydown transactions

Capital has three types of paydown transactions:

- **Witholding paydowns**: When connected accounts (users) apply for financing,
they agree that Stripe can withhold a fixed percentage of their future earnings
until they’ve paid back the total financing amount.
- **User-initiated paydowns**: Users can manually make a payment towards their
financing on the [Hosted Capital Reporting
page](https://docs.stripe.com/capital/api-integration#approve-application).
- **Collection attempts**: Stripe’s Servicing team might initiate paydowns in
accordance with the [Capital collections
policy](https://docs.stripe.com/capital/how-capital-for-platforms-works#capital-collections).

All paydowns have a corresponding [Financing
Transaction](https://docs.stripe.com/api/capital/financing_transaction_object)
of type `payment`. You can [Retrieve Financing
Transactions](https://docs.stripe.com/api/capital/financing_transactions/retrieve)
and filter by transaction type if you want to display withholding transactions
in your UI. Make sure you provide the account ID of the connected account in the
`Stripe-Account` header.

```
curl -G https://api.stripe.com/v1/capital/financing_transactions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d type=paydown
```

If the retrieval of the Financing Transactions list is successful, you receive a
response similar to the following:

```
{
 "object": "list",
"url":
"/v1/capital/financing_transactions?financing_offer=financingoffer_1NAdVWJQ3aJgxqz5nh90Zqrs&charge=ch_1HoZftJQ3aJgxqz50EbvL8zU",
 "has_more": false,
 "data": [
 {
 "id": "cptxn_1NAdVWJQ3aJgxqz5FSScvJaF",
 "object": "capital.financing_transaction",
 "account": "acct_1HLGiXJQ3aJgxqz5",
 "created_at": 1684780258,
 "details": {
 "advance_amount": 10000,
 "currency": "usd",
 "fee_amount": 1000,
 "linked_payment": "ch_1HoZftJQ3aJgxqz50EbvL8zU",
 "reason": "automatic_withholding",
 "total_amount": 11000,
 "transaction": {
 "charge": "ch_1HoZftJQ3aJgxqz50EbvL8zU"
 }
 },
 "financing_offer": "financingoffer_1NAdVWJQ3aJgxqz5nh90Zqrs",
 "livemode": true,
 "type": "payment",
 "user_facing_description": "Paydown of your loan"
 },
 {...},
 {...}
 ]
}
```

The response contains information describing how this particular paydown
affected the outstanding financed amount. If the paydown occurred because of
`"details.reason": "automatic_withholding"`, it also contains a reference to the
original Stripe payment in the `details.transaction` field.

### Destination Charges

If your platform processes payments using [Destination
Charges](https://docs.stripe.com/connect/destination-charges) and you’d like to
reconcile the [Financing
Transaction](https://docs.stripe.com/api/capital/financing_transaction_object)
paydown with the original charge which occurred on your platform, you can do
this by first extracting the charge ID in the [Financing
Transaction](https://docs.stripe.com/api/capital/financing_transaction_object)’s
`details.transaction` field. This will be set to the payment ID which occurred
as a result of the automatic
[Transfer](https://docs.stripe.com/api/transfers/object) to the connected
account.

```
{
 "id": "cptxn_1NBJQR2eZvKYlo2CBUy2GQ1S",
 "object": "capital.financing_transaction",
 "details": {
 "reason": "automatic_withholding",
 "transaction": {
 "charge": "py_1NBJI62c99H72o8MUEN0fIZx"
 },
 ...
 },
 "type": "payment",
 ...
}
```

You can then use the [Retrieve Charge
API](https://docs.stripe.com/api/charges/retrieve) to get back the charge
object:

```
curl https://api.stripe.com/v1/charges/py_1NBJI62c99H72o8MUEN0fIZx \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

```
{
 "id": "py_1NBJI62c99H72o8MUEN0fIZx",
 "object": "charge",
 "source_transfer": "tr_3NBJGW2eZvKYlo2C1jQOxNwF",
 ...
}
```

Because this is a Destination Charge, the `source_transfer` is populated with
the [Transfer](https://docs.stripe.com/api/transfers/object) ID. Finally, you
can then use the [Retrieve Transfer
API](https://docs.stripe.com/api/transfers/retrieve) to get back the Transfer
object:

```
curl https://api.stripe.com/v1/transfers/tr_3NBJGW2eZvKYlo2C1jQOxNwF \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

```
{
 "id": "tr_3NBJGW2eZvKYlo2C1jQOxNwF",
 "object": "transfer",
 "source_transaction": "ch_3NBJGW2eZvKYlo2C17oDFajw",
 ...
}
```

The `source_transaction` field contains the ID of the
[Charge](https://docs.stripe.com/api/payment_provider/payment/object) which
occurred on your platform, triggering a
[Transfer](https://docs.stripe.com/api/transfers/object) to the connected
account.

## Reversal transactions

Payout and paydown transactions can be reversed for any of the following
reasons:

- **Failed ACH debit:** A connected account’s bank account might have
insufficient funds to cover the paydown.
- **Financing cancelation:** If a connected account cancels the financing offer
after accepting, we issue a debit to recoup the funds and reverse the payout of
the financing.
- **One-off manual reversals:** When a charge is refunded, we don’t reverse the
paydown [Financing
Transaction](https://docs.stripe.com/api/capital/financing_transaction_object).
However, users can contact
[capital-support@stripe.com](mailto:capital-support@stripe.com) to request that
we reverse the paydown, which we might honor depending on the nature of the
reversal. If this happens, we ask you provide as much information and context as
to the original charge and why it was refunded.

Reversal of a paydown or payout transaction creates a [Financing
Transaction](https://docs.stripe.com/api/capital/financing_transaction_object)
of type `reversal`.

## Links

- [Financing Transactions
API](https://docs.stripe.com/api/capital/financing_transactions)
- [Balance Transactions API](https://docs.stripe.com/api/balance_transactions)
- [Financing
Offer](https://docs.stripe.com/api/capital/connect_financing_object)
- [payout](https://docs.stripe.com/payouts)
- [Create a payout](https://docs.stripe.com/api/payouts/create)
- [Financing
Transaction](https://docs.stripe.com/api/capital/financing_transaction_object)
- [capital.financing_transaction.created
webhook](https://docs.stripe.com/api/events/types#event_types-capital.financing_transaction.created)
- [Hosted Capital Reporting
page](https://docs.stripe.com/capital/api-integration#approve-application)
- [Capital collections
policy](https://docs.stripe.com/capital/how-capital-for-platforms-works#capital-collections)
- [Retrieve Financing
Transactions](https://docs.stripe.com/api/capital/financing_transactions/retrieve)
- [Destination Charges](https://docs.stripe.com/connect/destination-charges)
- [Transfer](https://docs.stripe.com/api/transfers/object)
- [Retrieve Charge API](https://docs.stripe.com/api/charges/retrieve)
- [Retrieve Transfer API](https://docs.stripe.com/api/transfers/retrieve)
- [Charge](https://docs.stripe.com/api/payment_provider/payment/object)