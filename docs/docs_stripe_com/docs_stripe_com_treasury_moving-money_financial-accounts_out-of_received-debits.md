# Moving money with Treasury using ReceivedDebit objects

## Learn how external account holders can pull funds from a Treasury financial account.

Certain processes initiated outside of Stripe Treasury result in money being
pulled out of a Treasury financial account. This includes:

- Spending money on a card through [Stripe
Issuing](https://docs.stripe.com/issuing/purchases/transactions#using-with-stripe-treasury)
- Pulling money out of a financial account into an external account using ACH
debits
- Pulling money out of a platform’s financial account into that platform’s
Stripe Payments balance using
[top-ups](https://docs.stripe.com/treasury/moving-money/payouts#top-ups)

These money movements result in the creation of `ReceivedDebit` objects. You
don’t create `ReceivedDebits` directly, rather you observe `ReceivedDebit`
object creation with webhooks. If there are insufficient funds in the account,
the `ReceivedDebit` fails in most cases.

## Retrieve a ReceivedDebit

Use `GET /v1/treasury/received_debits/{{RECEIVED_DEBIT_ID}}` to retrieve the
`ReceivedDebit` with the associated ID.

```
curl https://api.stripe.com/v1/treasury/received_debits/{{RECEIVED_DEBIT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

If successful, the response returns the `ReceivedDebit` object with the
associated ID. Some of the parameters in the response have additional details
that are only returned when you add them as values to the `expand[]` parameter.
The fields that you can expand have an “Expandable” comment in the following
response example. See [Expanding
Responses](https://docs.stripe.com/api/expanding_objects) to learn more about
expanding object responses.

```
{
 "id": "{{RECEIVED_DEBIT_ID}}",
 "object": "received_debit",
 "livemode": Boolean,
 "created": Timestamp,
 // The FinancialAccount funds have been pulled from
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}", // Expandable
 "amount": 1000,
 "currency": "usd",
 "description": "Testing",
```

See all 71 lines
## List ReceivedDebits

Use `GET /v1/treasury/received_debits` to retrieve all `ReceivedDebits` for a
financial account. You must specify a financial account ID for the
`financial_account` parameter. You can filter the results by the standard list
parameters or by `status`.

```
{
 // Standard list parameters
 "limit", "starting_after", "ending_before",
 // Filter by FinancialAccount (Required)
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
 // Filter by status
 "status": "succeeded" | "failed"
}
```

The following request retrieves the last successful [ReceivedDebit
object](https://docs.stripe.com/api/treasury/received_debits/object) that
occurred before the provided `ReceivedDebit` for the financial account
identified.

```
curl -G https://api.stripe.com/v1/treasury/received_debits \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
 -d limit=1 \
 -d ending_before={{RECEIVED_DEBIT_ID}}
```

## Test ReceivedDebits

Stripe Treasury provides test endpoints for `ReceivedDebit` objects. Use `POST
/v1/test_helpers/treasury/received_debits` to simulate `ReceivedDebit` creation
in test mode. You can’t create `ReceivedDebit` objects in live mode, so using
this endpoint enables you to test the flow of funds when a third party initiates
creation of a `ReceivedDebit`. Set `financial_account` to the ID of the
financial account to send money from. Set `network` to `ach` and optionally
provide the ABA financial address details for the `source_details.aba`
parameter. As in live mode, test mode `ReceivedDebits` fail if there are
insufficient funds available.

## ReceivedDebit webhooks

Stripe emits the following `ReceivedDebit` events to your
[webhook](https://docs.stripe.com/webhooks) endpoint:

- `treasury.received_debit.created` on `ReceivedDebit` creation.

## Links

- [Stripe
Issuing](https://docs.stripe.com/issuing/purchases/transactions#using-with-stripe-treasury)
- [top-ups](https://docs.stripe.com/treasury/moving-money/payouts#top-ups)
- [Expanding Responses](https://docs.stripe.com/api/expanding_objects)
- [ReceivedDebit
object](https://docs.stripe.com/api/treasury/received_debits/object)
- [webhook](https://docs.stripe.com/webhooks)