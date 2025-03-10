# Issuing transactions

## Learn how to use Issuing to handle transactions.

After an
[authorization](https://docs.stripe.com/issuing/purchases/authorizations) is
approved and is captured, the `status` on the authorization is set to `closed`
and a [Transaction](https://docs.stripe.com/api#issuing_transaction_object)
object is created. This normally happens within 24 hours; however hotels,
airlines, and car rental companies are able to capture up to 31 days after
authorization.

When an authorization is captured, two things happen.

- The `status` on the authorization is set to `closed`, releasing the purchase
amount held by that authorization. A [balance
transaction](https://docs.stripe.com/reports/balance-transaction-types) of type
`issuing_authorization_release` is created to represent this.
- A new transaction object of type `capture` is created. The purchase amount is
deducted from the [balance you’re using for
Issuing](https://docs.stripe.com/issuing/funding/balance).
hide sample argumentsIDiauth_123statusclosedamount10
USDtransactionsipi_123balance_transactionstxn_123, txn_456hide sample
argumentsIDipi_123typecaptureamount-10
USDauthorization`iauth_123`balance_transactiontxn_789hide sample
argumentsIDtxn_123typeissuing_authorization_holdamount-10 USDhide sample
argumentsIDtxn_456typeissuing_authorization_releaseamount10 USDhide sample
argumentsIDtxn_789typeissuing_transactionamount-10 USD
[Spending controls](https://docs.stripe.com/issuing/controls/spending-controls),
[real time authorization
controls](https://docs.stripe.com/issuing/controls/real-time-authorizations),
and card status (whether a card is active or not) don’t apply for capture. They
can be used to determine whether authorizations are approved, but captures for
approved authorizations always succeed.

## Handling other transactions

In addition to regular transactions, there are a few other cases that you should
be ready to handle.

RefundsPartial captureOver captureMulti captureForce capture
Refunds are transactions with `type` of `refund`.

When we create a transaction representing a refund or credit, we try to link it
to the original payment authorization. Refunds aren’t necessarily tied to the
original payment transaction or authorization, so linking them is an inexact
science. As a result, we might link to an unrelated authorization or be unable
to link to an authorization at all (for example, if the card is credited rather
than refunded). In these cases, the `authorization` field of the transaction is
set to `null`, and the transaction won’t be linked to the authorization. We
process all refunds and credits the same way, regardless of their linkage to a
payment authorization.

```
{
 "id": "ipi_1GTG10EEsyYlpYZ9VJn2xV3B",
 "object": "issuing.transaction",
 "amount": 100,
 "authorization": "iauth_1GBZQyEEsyYlpYZ9255L8GQC",
 "balance_transaction": null,
 "card": "ic_1GBZQJEEsyYlpYZ99v6rq38S",
 "cardholder": null,
 "created": 1585783834,
 "currency": "usd",
 "livemode": false,
 "merchant_amount": 100,
 "merchant_currency": "usd",
 "merchant_data": {
 "category": "taxicabs_limousines",
 "city": "San Francisco",
 "country": "US",
 "name": "Rocket Rides",
 "network_id": "1234567890",
 "postal_code": "94111",
 "state": "CA",
 "url": null
 },
 "metadata": {},
 "type": "refund",
}
```

### Testing

To simulate the creation of a refund transaction, you can use the [Transaction
Refund API](https://docs.stripe.com/api/issuing/transactions/test_mode_refund)
in the Issuing test helpers.

```
curl -X POST
https://api.stripe.com/v1/test_helpers/issuing/transactions/{{TRANSACTION_ID}}/refund
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

To create a refund transaction that doesn’t link to an authorization, use the
[Create Unlinked Refund
API](https://docs.stripe.com/api/issuing/transactions/test_mode_create_unlinked_refund)
in the Issuing test helpers.

```
curl
https://api.stripe.com/v1/test_helpers/issuing/transactions/create_unlinked_refund
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d card={{CARD_ID}} \
 -d amount=1000
```

## Links

- [authorization](https://docs.stripe.com/issuing/purchases/authorizations)
- [Transaction](https://docs.stripe.com/api#issuing_transaction_object)
- [balance
transaction](https://docs.stripe.com/reports/balance-transaction-types)
- [balance you’re using for
Issuing](https://docs.stripe.com/issuing/funding/balance)
- [Authorization](https://docs.stripe.com/api/authorizations/object)
- [Transaction](https://docs.stripe.com/api/transactions/object)
- [Balance Transaction](https://docs.stripe.com/api/balance_transactions/object)
- [Spending
controls](https://docs.stripe.com/issuing/controls/spending-controls)
- [real time authorization
controls](https://docs.stripe.com/issuing/controls/real-time-authorizations)
- [Transaction Refund
API](https://docs.stripe.com/api/issuing/transactions/test_mode_refund)
- [Create Unlinked Refund
API](https://docs.stripe.com/api/issuing/transactions/test_mode_create_unlinked_refund)