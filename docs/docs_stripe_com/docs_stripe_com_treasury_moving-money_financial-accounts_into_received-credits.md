# Moving money with Treasury using ReceivedCredit objects

## Learn how to move money into a Treasury financial account from another Treasury financial account or bank account.

When funds move into a financial account, Stripe creates a corresponding
[ReceivedCredit](https://docs.stripe.com/api/treasury/received_credits) object
on the account. A `ReceivedCredit` contains information on how the funds were
sent and from what account, where possible. You can send funds to a financial
account with the account’s routing and account numbers for `ach` and
`us_domestic_wire`, or the financial account ID for transfers between financial
accounts.

When the origin of the funds is another Treasury financial account, the
`ReceivedCredit` contains a `linked_flows.source_flow` reference to the
originating money movement. In this case, the source `OutboundPayment` has
`stripe` as its `network` value.

## Retrieve a ReceivedCredit

Use `GET /v1/treasury/received_credits/{{RECEIVED_CREDIT_ID}}` to retrieve the
[ReceivedCredit](https://docs.stripe.com/api/treasury/received_credits) with the
specified ID.

The following request retrieves the `ReceivedCredit` with the specified ID. The
response for this request includes expanded [Transaction
object](https://docs.stripe.com/api/treasury/transactions) details.

```
curl -G
https://api.stripe.com/v1/treasury/received_credits/{{RECEIVED_CREDIT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "expand[]"=transaction
```

If successful, the response provides the requested `ReceivedCredit` object. Some
of the parameters in the response have additional details that are only returned
when you add them as values to the `expand[]` parameter of your request. The
fields that you can expand have an `Expandable` comment in the following
response example. See [Expanding
Responses](https://docs.stripe.com/api/expanding_objects) to learn more about
expanding object responses.

```
{
 "id": "{{RECEIVED_CREDIT_ID}}",
 "object": "received_credit",
 "livemode": true | false,
 "created": "{{Timestamp}}",
 // The FinancialAccount that received the funds
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}", // Expandable
 "amount": 1000,
 "currency": "usd",
 // The description of this movement sent by the originator
```

See all 79 lines
## List ReceivedCredits

Use `GET /v1/treasury/received_credits` to retrieve all of the `ReceivedCredits`
for the financial account with the ID of the required `financial_account`
parameter. You can filter the list with the standard list parameters, by
`status`, or by `linked_flows.source_flow_type`.

```
{
 // Standard list parameters
 "limit", "starting_after", "ending_before",
 // Filter by FinancialAccount (required)
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
 // Filter by status
 "status": "succeeded" | "failed",
 // Filter by `source_flow_type`
 "linked_flows.source_flow_type": nil | "payout" | "outbound_payment"
}

```

The following request retrieves the `ReceivedCredits` that have a status of
`failed` for the specified financial account.

```
curl -G https://api.stripe.com/v1/treasury/received_credits \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
 -d status=failed
```

If successful, the response includes the
[ReceivedCredit](https://docs.stripe.com/api/treasury/received_credits) objects
that match the criteria specified in the request.

## Test ReceivedCredits

Use `POST /v1/test_helpers/treasury/received_credits` to simulate receiving
funds in a financial account. To simulate a bank transfer from an account
outside of Stripe to your financial account, set
`initiating_payment_method_details` to the values of the external bank account,
and set `network` to `ach` or `us_domestic_wire`.

The following request creates a test mode `ReceivedCredit` from an external bank
account using an `OutboundPayment` between two financial accounts on the same
platform.

```
curl https://api.stripe.com/v1/test_helpers/treasury/received_credits \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d financial_account={{DESTINATION_FINANCIAL_ACCOUNT_ID}} \
 -d network=ach \
 -d amount=1234 \
 -d currency=usd
```

If successful, the response returns a `ReceivedCredit` object. The following is
an example of a response for a bank transfer.

```
{
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
 "network": "ach",
 "amount": "1234",
 "currency": "usd",
 "description": "Test",
 "source_details": {
 "type": "aba",
 "aba": {
 "country": "US",
 "routing_number": "12341234",
 "account_number": "0123456789",
 "account_holder_name": "Jenny Rosen",
 }
 }
}
```

## ReceivedCredit webhooks

Stripe emits the following `ReceivedCredit` events to your
[webhook](https://docs.stripe.com/webhooks) endpoint:

- `treasury.received_credit.created` on `ReceivedCredit` creation.
- `treasury.received_credit.{{new_status}}` when an `ReceivedCredit` changes
status. Available status value options include:-
`treasury.received_credit.succeeded`
- `treasury.received_credit.failed`

## Links

- [ReceivedCredit](https://docs.stripe.com/api/treasury/received_credits)
- [Transaction object](https://docs.stripe.com/api/treasury/transactions)
- [Expanding Responses](https://docs.stripe.com/api/expanding_objects)
- [webhook](https://docs.stripe.com/webhooks)