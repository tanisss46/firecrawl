# Moving money with Treasury using OutboundPayment objects

## Learn how to create outbound payments to move money out of Treasury financial accounts to third parties.

`OutboundPayment` objects represent push-based transfers from your Treasury
financial account to a third-party external account using ACH or wire transfer,
or another financial account associated with the same platform instantly using
the `stripe` network. For example, if you want to send money from your financial
account to your vendor’s external US bank account, you create an
`OutboundPayment` to move the funds. The receiving accounts for an
`OutboundPayment` are either an external bank account or another financial
account.

The typical transfer time for outbound payments can range from minutes (when
using the Stripe network), same day, to 1-2 business days (when using the ACH
network). For more information, see the [Money movement
timelines](https://docs.stripe.com/treasury/money-movement/timelines#outboundpayment-and-outboundtransfer-transactions)
guide.

## Create an OutboundPayment

Use `POST /v1/treasury/outbound_payments` to create an `OutboundPayment`. Among
the request’s possible parameters, the following are required:

- `amount`: Amount in cents to pay.
- `currency`: Three-letter ISO currency code (only `usd` supported).
- `financial_account`: The source financial account funds are sent from.
- `destination_payment_method` or `destination_payment_method_data`: Information
about the destination of funds for the payment.- With
`destination_payment_method`, you must first set up the `PaymentMethod` for
outbound flows using a [SetupIntent](https://docs.stripe.com/api/setup_intents).
You must also specify the customer ID that matches the `Customer` object the
`PaymentMethod` is attached to. Alternatively, you can use an existing legacy
[BankAccount](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges)
attached to the `Customer` in place of a `PaymentMethod`.
- With `destination_payment_method_data`, you can specify payment method details
inline. You can use this parameter to specify bank account details or when
you’re [sending funds to another financial
account](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments#create-obp-for-fa)
over the Stripe network.

## Create an OutboundPayment to an external bank account

Use `POST /v1/treasury/outbound_payments` to create an `OutboundPayment` from
the financial account identified by the ID in the `financial_account` parameter
value of the body. The following request adds `statement_descriptor` and
`destination_payment_method_data` information.

```
curl https://api.stripe.com/v1/treasury/outbound_payments \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
 -d amount=2000 \
 -d currency=usd \
 -d statement_descriptor=payment_1 \
 -d "destination_payment_method_data[type]"=us_bank_account \
-d
"destination_payment_method_data[us_bank_account][account_holder_type]"=individual
\
-d "destination_payment_method_data[us_bank_account][routing_number]"=110000000
\
-d "destination_payment_method_data[us_bank_account][account_number]"=1234567890
\
--data-urlencode
"destination_payment_method_data[billing_details][email]"="jenny@example.com" \
 -d "destination_payment_method_data[billing_details][phone]"=7135551212 \
 -d "destination_payment_method_data[billing_details][address][city]"=Alvin \
 -d "destination_payment_method_data[billing_details][address][state]"=TX \
-d
"destination_payment_method_data[billing_details][address][postal_code]"=77511 \
-d "destination_payment_method_data[billing_details][address][line1]"="123 Main
St." \
 -d "destination_payment_method_data[billing_details][name]"="Jenny Rosen"
```

If successful, the response returns the newly created `OutboundPayment`.

```
{
 "id": "{{OUTBOUND_PAYMENT_ID}}",
 "object": "outbound_payment",
 // The source FinancialAccount. Funds are pulled from this account.
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
 // The amount to send. 10.00 USD in this case.
 "amount": 1000,
 "cancelable": true | false,
 "currency": "usd",
// The destination payment method. Either this or
`destination_payment_method_data`
```

See all 73 lines
### Same-day ACH

#### Private preview

Same-day ACH is currently in preview with limited availability, subject to
Stripe review and approval. To request access, email
[treasury-support@stripe.com](mailto:treasury-support@stripe.com).

If you don’t have access, API calls that include same-day ACH features or
parameters return an error.

Using same-day ACH enables sending funds that arrive the same business day if
the `OutboundPayment` call successfully completes before the [cutoff
time](https://docs.stripe.com/treasury/money-movement/timelines#evolve-bank-and-trust--outbound).
To use same-day ACH, set the
`destination_payment_method_options.us_bank_account.network` parameter to `ach`
and the `destination_payment_method_options.us_bank_account.ach.submission`
parameter to `same_day`.

### Wire transfer: routing numbers

Some banks might use a separate wire transfer routing number that differs from
ACH. Consequently, you might receive an error during wire creation if the
routing number on the payment method doesn’t support wire transfers. If you
receive this error, you need to add a new payment method with your bank’s wire
routing number.

### Wire transfer: recipient address

Wire transfers require ACH metadata plus recipient name and billing address. The
address is the address of the account holder receiving the wire, not the address
of their bank.

When entering the `billing_details.address` for a payment method, all address
fields must be complete. Attempting to send a wire with incomplete fields on the
`billing_details.address` results in an error.

#### Note

When sending a wire using an `OutboundTransfer`, if you don’t fill out any
address fields, Stripe defaults to the legal entity of the primary Stripe
account holder.

## Create an OutboundPayment to a financial account

To move money between financial accounts, call `POST
/v1/treasury/outbound_payments` on the origin account and specify the
destination account in the `destination_payment_method_data` parameter. Both
financial accounts must be associated with the same platform, but can’t be
associated with the same connected account. To transfer money between financial
accounts associated with the same connected account, use an
[OutboundTransfer](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-transfers).

```
curl https://api.stripe.com/v1/treasury/outbound_payments \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d financial_account={{SOURCE_FINANCIAL_ACCOUNT_ID}} \
 -d amount=2000 \
 -d currency=usd \
 -d statement_descriptor="Test outbound payment to FA" \
 -d "destination_payment_method_data[type]"=financial_account \
-d
"destination_payment_method_data[financial_account]"={{DESTINATION_FINANCIAL_ACCOUNT_ID}}
```

The body of your request must be `x-www-form-urlencoded`, but the following JSON
defines the data you can send.

```
{
 // The source FinancialAccount. Funds are pulled from this account.
 "financial_account": "{{SOURCE_FINANCIAL_ACCOUNT_ID}}",
 // The amount to send.
 "amount": 1000,
 "currency": "usd",
 // The destination payment method. This parameter is the only way to
 // send an OutboundPayment via the `stripe` network.
 "destination_payment_method_data": {
 "type": "financial_account",
```

See all 34 lines
## Retrieve an OutboundPayment

Use `GET /v1/treasury/outbound_payments/{{OUTBOUND_PAYMENT_ID}}` to retrieve
details for the `OutboundPayment` with the associated ID.

```
curl
https://api.stripe.com/v1/treasury/outbound_payments/{{OUTBOUND_PAYMENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

If successful, the response returns the `OutboundPayment` object with the
associated ID. Some of the parameters in the response have additional details
that are only returned when you add them as values to the `expand[]` parameter.
The fields that you can expand have an “Expandable” comment in the following
response example. See [Expanding
Responses](https://docs.stripe.com/api/expanding_objects) to learn more about
expanding object responses.

```
{
 "id": "{{OUTBOUND_PAYMENT_ID}}",
 "object": "outbound_payment",
 "livemode": true | false,
 "created": "{{Timestamp}}",
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}", // Expandable
 "amount": 1000,
 "currency": "usd",
// Will only be set if `destination_payment_method` was used during the creation
of
 // the OutboundPayment
```

See all 122 lines
## Cancel an OutboundPayment

Use `POST /v1/treasury/outbound_payments/{{OUTBOUND_PAYMENT_ID}}/cancel` to
cancel the `OutboundPayment` with the associated ID. The `OutboundPayment`
object includes a `cancelable` parameter with a Boolean value to indicate
whether you can cancel the transfer. After an `OutboundPayment` submits to the
network, the `cancelable` value becomes `false` and you receive an error from
this endpoint for that transfer.

```
curl -X POST
https://api.stripe.com/v1/treasury/outbound_payments/{{OUTBOUND_PAYMENT_ID}}/cancel
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

If successful, the response returns the `OutboundPayment` object with the
`status` value set to `canceled`.

```
{
 "id": "{{OUTBOUND_PAYMENT_ID}}",
 "object": "outbound_payment",
 "livemode": false,
 "created": 123456,
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
 "amount": 1000,
 "currency": "usd",
 ...
 "status": "canceled",
```

See all 19 lines
## List OutboundPayments

Use `GET /v1/treasury/outbound_payments` to list the `OutboundPayments` from the
financial account with the associated ID. You can filter the list with the
standard list parameters or by `status` or by `customer`.

```
{
 // Standard list parameters
 "limit", "starting_after", "ending_before",
 // Filter by status
 "status": "processing" | "canceled" | "failed" | "posted" | "returned",
 // Filter by FinancialAccount (Required)
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
 // Filter by Customer
 "customer": "{{CUSTOMER_ID}}",
}

```

The following request retrieves the last five [OutboundPayment
objects](https://docs.stripe.com/api/treasury/outbound_payments/object) for the
financial account attached to the platform and paid to the identified
`Customer`.

```
curl -G https://api.stripe.com/v1/treasury/outbound_payments \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
 -d limit=5 \
 -d customer={{CUSTOMER_ID}}
```

## OutboundPayment states

The following table describes each status and what the possible transition
states are.

STATUSDESCRIPTIONCAN TRANSITION TO STATE`processing`The `OutboundPayment`
starting state. Funds are allotted to a pending transaction (but are still part
of the current balance). The user can cancel the `OutboundPayment` while the
value of the `cancelable` parameter is `true`.`posted`, `canceled`,
`failed``failed` (terminal)`OutboundPayment` failed to confirm. Stripe voids the
pending transaction and returns the funds to the user.N/A`canceled` (terminal)A
user canceled the `OutboundPayment` before posting. Stripe voids the pending
transaction and returns the funds to the user.N/A`posted`The `OutboundPayment`
posted and funds have left the account. The underlying transaction
posts.`returned``returned` (terminal)`OutboundPayment` failed to successfully
arrive at the destination. Funds return to the user with a transaction
(`returned_details[transaction]`).N/A
## Test OutboundPayments

To test your integration end-to-end, we recommend using the [SetupIntent
requests in test
mode](https://docs.stripe.com/treasury/moving-money/working-with-bankaccount-objects#setupintents)
to create a `PaymentMethod`, then passing that `PaymentMethod` into an
`OutboundPayment` creation request using the `destination_payment_method`
parameter.

Stripe also allows test `PaymentMethod` tokens and numbers to trigger specific
functionality:

- By passing in a test `PaymentMethod` token to `destination_payment_method`
(for `ach` and `us_domestic_wire` networks)- If you’re passing in a test
`PaymentMethod` token directly into `destination_payment_method`, you must still
pass in a customer ID to the `customer` parameter. For convenience, Stripe
allows you to pass in any existing test mode customer. This differs from live
mode, which requires the existing `PaymentMethod` to be attached to a `Customer`
and that same customer ID passed into the `customer` parameter.
- By passing in test routing and account numbers to
`destination_payment_method_data[us_bank_account]` (for `ach` and
`us_domestic_wire` networks).
- By passing in the ID of an existing test mode financial account owned by an
intra-platform account to `destination_payment_method_data[financial_account]`
(for Stripe network).

In all cases, the `OutboundPayment` response returns the processing status.
Stripe triggers [webhooks](https://docs.stripe.com/webhooks) for the relevant
state transitions, and fetching the `OutboundPayment` after creation returns the
expected state.

CREATESDESTINATION_PAYMENT_METHOD (WITH ANY EXISTING TEST MODE
CUSTOMER)DESTINATION_PAYMENT_METHOD_DATA[US_BANK_ACCOUNT]`OutboundPayment` in
initial processing state`pm_usBankAccount_processing`- `routing_number`:
110000000
- `account_number`: 000000000009
`OutboundPayment` that transitions to `posted` (from
`processing`)`pm_usBankAccount`- `routing_number`: 110000000
- `account_number`: 000123456789
`OutboundPayment` that transitions to `posted` (from `processing`), additionally
adding one day to the original
`expected_arrival_date``pm_usBankAccount_expectedArrivalDateUpdated`-
`routing_number`: 110000000
- `account_number`: 000123457890
`OutboundPayment` that transitions to `canceled` (from
`processing`)`pm_usBankAccount_canceledByUser`- `routing_number`: 110000000
- `account_number`: 000000000123
`OutboundPayment` that transitions to `failed` (from
`processing`)`pm_usBankAccount_internalFailure`- `routing_number`: 110000000
- `account_number`: 000000000234
`OutboundPayment` that transitions to `returned` due to account closure (from
processing after posted)`pm_usBankAccount_accountClosed`- `routing_number`:
110000000
- `account_number`: 000111111113
`OutboundPayment` that transitions to returned due to no account (from
processing after posted)`pm_usBankAccount_noAccount`- `routing_number`:
110000000
- `account_number`: 000111111116
`OutboundPayment` that transitions to `returned` due to invalid account number
(from processing after posted)`pm_usBankAccount_invalidAccountNumber`-
`routing_number`: 110000000
- `account_number`: 000111111119

### OutboundPayment test helper endpoints

Stripe provides endpoints to help you test `OutboundPayments` in different
states. Use the test endpoints to move an `OutboundPayment` you create directly
to a new state of `posted`, `failed`, or `returned`.

- Use the [test post
endpoint](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_post)
to move the identified `OutboundPayment` from `processing` to `posted`.

`POST /v1/test_helpers/treasury/outbound_payments/{{OUTBOUND_PAYMENT_ID}}/post`
- Use the [test fail
endpoint](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_fail)
to move the identified `OutboundPayment` from `processing` to `failed`.

`POST /v1/test_helpers/treasury/outbound_payments/{{OUTBOUND_PAYMENT_ID}}/fail`
- Use the [test return
endpoint](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_return)
to move the identified `OutboundPayment` from `processing` to `returned`.

`POST
/v1/test_helpers/treasury/outbound_payments/{{OUTBOUND_PAYMENT_ID}}/return`

These endpoints are particularly useful when testing error scenarios, such as
returns, which would otherwise require outside action.

For the `return` endpoint, include the optional `returned_details.code`
parameter in the body to indicate why the transfer was returned. If not
provided, the transfer defaults to the `declined` return code.

```
{
 "returned_details": {
 "code": "account_closed" |
 "account_frozen" |
 "bank_account_restricted" |
 "bank_ownership_changed" |
 "could_not_process" |
 "invalid_account_number" |
 "incorrect_account_holder_name" |
 "invalid_currency" |
 "no_account" |
 "declined"
 }
}
```

We also provide a [test update
endpoint](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_update)
to simulate the posting of tracking details on a test mode `Outbound Payment`.
The `tracking_details` field can only be set for test mode objects.

In all cases, Stripe triggers [webhooks](https://docs.stripe.com/webhooks) for
each relevant state transition, and fetching the `OutboundPayment` after
transition returns the expected state.

## OutboundPayment webhooks

Stripe emits the following `OutboundPayment` events to your
[webhook](https://docs.stripe.com/webhooks) endpoint:

- `treasury.outbound_payment.created` on `OutboundPayment` creation.
- `treasury.outbound_payment.{{new_status}}` when an `OutboundPayment` changes
status. Available status value options include:-
`treasury.outbound_payment.posted`
- `treasury.outbound_payment.failed`
- `treasury.outbound_payment.canceled`
- `treasury.outbound_payment.returned`
- `treasury.outbound_payment.expected_arrival_date_updated` when the
`expected_arrival_date` of an `OutboundPayment` changes.
- `treasury.outbound_payment.tracking_details_updated` when the tracking details
for an `OutboundPayment` are updated.

## Links

- [Money movement
timelines](https://docs.stripe.com/treasury/money-movement/timelines#outboundpayment-and-outboundtransfer-transactions)
- [SetupIntent](https://docs.stripe.com/api/setup_intents)
-
[BankAccount](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges)
- [cutoff
time](https://docs.stripe.com/treasury/money-movement/timelines#evolve-bank-and-trust--outbound)
-
[OutboundTransfer](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-transfers)
- [Expanding Responses](https://docs.stripe.com/api/expanding_objects)
- [OutboundPayment
objects](https://docs.stripe.com/api/treasury/outbound_payments/object)
- [SetupIntent requests in test
mode](https://docs.stripe.com/treasury/moving-money/working-with-bankaccount-objects#setupintents)
- [webhooks](https://docs.stripe.com/webhooks)
- [test post
endpoint](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_post)
- [test fail
endpoint](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_fail)
- [test return
endpoint](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_return)
- [test update
endpoint](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_update)