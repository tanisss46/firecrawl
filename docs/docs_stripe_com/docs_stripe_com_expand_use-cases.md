# Use cases for expanding responses

## Learn how the expand attribute helps you perform common tasks.

## See the Stripe fee for a given payment

You can check the processing fees for a payment after the payment is processed
and the balance transaction is created. Stripe automatically creates this
[balance
transaction](https://docs.stripe.com/api/balance_transactions/object#balance_transaction_object-fee_details)
in the background. The `charge.updated` event includes a reference to the
balance transaction through the `balance_transaction` property (for example,
`txn_123`), indicating that the balance transaction has been created and is
ready for use.

Instead of looking up the balance transaction separately, you can retrieve it in
a single call using `expand`. For example:

```
curl https://api.stripe.com/v1/payment_intents/pi_1Gpl8kLHughnNhxyIb1RvRTu \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "expand[]"="latest_charge.balance_transaction" \
 -G
```

Users on API version [2022-08-01](https://docs.stripe.com/upgrades#2022-08-01)
or older:

```
curl https://api.stripe.com/v1/payment_intents/pi_1Gpl8kLHughnNhxyIb1RvRTu \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "expand[]"="charges.data.balance_transaction" \
 -G
```

#### Note

A payment intent must be
[captured](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method#capture-funds)
and have a
[status](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-status)
of `succeeded` for the Stripe fees to be available.

## See the charges included in a payout

Every automatic [payout](https://docs.stripe.com/payouts) is tied to historical
changes to the balance of your Stripe account. The API records these historical
changes as [balance
transactions](https://docs.stripe.com/api/balance_transactions/object), which
you can retrieve using [List Balance
Transactions](https://docs.stripe.com/api/balance_transactions/list). From a
list of balance transactions, you can expand the
[source](https://docs.stripe.com/api/balance_transactions/object#balance_transaction_object-source)
property to gather information on what triggered the change to the account
balance (Charge, Refund, Transfer, and so on). For example:

```
curl https://api.stripe.com/v1/balance_transactions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d payout=po_1Gl3ZLLHughnNhxyDrOia0vI \
 -d type=charge \
 -d "expand[]"="data.source" \
 -G
```

#### Note

You can only retrieve balance transaction history on *automatic* payouts. If you
have manual payouts enabled, you must track transaction history on your own.

Learn more about [payout
reconciliation](https://docs.stripe.com/payouts/reconciliation).

If you’re using [Connect](https://docs.stripe.com/connect) with destination
charges, you can retrieve the same information on behalf of your connected
accounts. One difference is that destination charges involve both a transfer and
a linked payment (in the form of a Charge object) to move funds to a connected
account. So when listing the balance transactions bundled in your connected
account’s payouts, each balance transaction’s source is linked to the transfer’s
payment rather than the originating Charge. To retrieve the originating Charge,
you need to expand a payment’s linked transfer through the
[source_transfer](https://docs.stripe.com/api/charges/object#charge_object-source_transfer)
property; and from there, expand the transfer’s
[source_transaction](https://docs.stripe.com/api/transfers/object#transfer_object-source_transaction)
property:

```
curl https://api.stripe.com/v1/balance_transactions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d payout=po_1G7bnaD2wdkPsFGzdVOqU44u \
 -d type=payment \
 -d "expand[]"="data.source.source_transfer.source_transaction" \
 -H "Stripe-Account: acct_1G7PaoD2wdkPsFGz" \
 -G
```

## Links

- [balance
transaction](https://docs.stripe.com/api/balance_transactions/object#balance_transaction_object-fee_details)
- [2022-08-01](https://docs.stripe.com/upgrades#2022-08-01)
-
[captured](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method#capture-funds)
-
[status](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-status)
- [payout](https://docs.stripe.com/payouts)
- [balance
transactions](https://docs.stripe.com/api/balance_transactions/object)
- [List Balance
Transactions](https://docs.stripe.com/api/balance_transactions/list)
-
[source](https://docs.stripe.com/api/balance_transactions/object#balance_transaction_object-source)
- [payout reconciliation](https://docs.stripe.com/payouts/reconciliation)
- [Connect](https://docs.stripe.com/connect)
-
[source_transfer](https://docs.stripe.com/api/charges/object#charge_object-source_transfer)
-
[source_transaction](https://docs.stripe.com/api/transfers/object#transfer_object-source_transaction)