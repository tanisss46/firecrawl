# Moving money with Treasury using InboundTransfer objects

## Learn how to transfer money from another account you own into a Treasury financial account.

Inbound transfers move money from an external US bank account into a financial
account using the ACH network. These transfers are initiated with
[InboundTransfer](https://docs.stripe.com/api/treasury/inbound_transfers)
objects.

Inbound transfers take 2-4 business days to complete unless you’re using the
same-day ACH capability. For more information, see the [Money movement
timelines](https://docs.stripe.com/treasury/money-movement/timelines#inboundtransfer-transactions)
guide.

#### Note

You can use inbound transfers to move funds from a financial account owner’s
bank account. To accept funds from an external party into a financial account,
use an [ACH
Debit](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment) into
the Payments balance, followed by a [payout to the financial
account](https://docs.stripe.com/treasury/moving-money/payouts).

## Create an InboundTransfer

Use `POST /v1/treasury/inbound_transfers` to create an `InboundTransfer` object,
which represents pull-based transfers from an external account that you own into
your financial account. In other words, you create an `InboundTransfer` to move
funds into your financial account by debiting your external US bank account. You
must include the following parameters with your request:

- `amount`: The amount in cents to be transferred into the financial account.
- `currency`: Three-letter ISO currency code (`usd` is currently the only
supported value).
- `financial_account`: The ID of the financial account receiving the transfer.
- `origin_payment_method`: The source of funds for the inbound transfer. You
must first set up the account-attached payment method for inbound flows and
verify the bank account using a
[SetupIntent](https://docs.stripe.com/api/setup_intents). Alternatively, you can
use an existing
[BankAccount](https://docs.stripe.com/api/customer_bank_accounts) previously set
up as a verified
[ExternalAccount](https://docs.stripe.com/api/external_accounts). Whether you
use a payment method or a bank account, you need the [account owner’s
permission](https://docs.stripe.com/treasury/moving-money/working-with-bankaccount-objects)
to debit the funds from the account.

The following JSON shows the data you can include in the body of your request.

```
{
// The source PaymentMethod or BankAccount. Funds are pulled from this account.
 "origin_payment_method": "{{PAYMENT_METHOD_ID}}" | "{{BANK_ACCOUNT_ID}}",
 // The destination FinancialAccount. Funds arrive in this account.
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
 // The amount to debit. 10.00 USD in this case.
 "amount": 1000,
 "currency": "usd",
 // An optional, internal description for the InboundTransfer.
 "description": "Funds for vendor payment payment_234281",
 // An optional descriptor for the InboundTransfer to send
 // to the network with the debit request. Max 10 characters
 "statement_descriptor": "payment_1",
 // Stripe does not support updating InboundTransfers after creation.
 // You can only set metadata at creation time.
 "metadata": null | {{Hash}}
}
```

The following request transfers 200 USD using an account-attached payment method
into the financial account with the provided ID. The `Stripe-Account` header
value identifies the Stripe account that owns both the financial account and the
payment method.

```
curl https://api.stripe.com/v1/treasury/inbound_transfers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d origin_payment_method={{PAYMENT_METHOD_ID}} \
 -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
 -d amount=20000 \
 -d currency=usd \
 -d description="Funds for repair" \
 -d statement_descriptor="Invoice 12"
```

If successful, the response provides the `InboundTransfer` object. The object
includes a `hosted_regulatory_receipt_url` that provides access to details of
the transaction for the account holder on your platform.

```
{
 "id": "{{INBOUND_TRANSFER_ID}}",
 "object": "inbound_transfer",
 "amount": 20000,
 "created": 1648071297,
 "currency": "usd",
 "description": "Funds for repair",
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
"hosted_regulatory_receipt_url":
"https://payments.stripe.com/regulatory-receipt/{{IBT_URL}}",
 "linked_flows": null,
 "livemode": false,
 "metadata": {},
 "origin_payment_method": "{{PAYMENT_METHOD_ID}}",
 ...
 "statement_descriptor": "Invoice 12",
 "status": "processing",
 ...
}
```

#### Warning

In rare cases, Stripe might cancel an InboundTransfer request due to various
risk factors. In these scenarios, the API request errors with response code 402.
The error message provides additional detail on the risk factors that led to the
intervention.

### Same-day ACH

#### Private preview

Same-day ACH is currently in preview with limited availability, subject to
Stripe review and approval. To request access, email
[treasury-support@stripe.com](mailto:treasury-support@stripe.com).

If you don’t have access, API calls that include same-day ACH features or
parameters return an error.

Using same-day ACH enables funds to arrive in the originating financial account
within the same business day if the `InboundTransfer` call successfully
completes before the [cutoff
time](https://docs.stripe.com/treasury/money-movement/timelines#evolve-bank-and-trust--inbound).
To use same-day ACH, set the
`origin_payment_method_options.us_bank_account.ach.submission` parameter to
`same_day`.

#### Note

The fast settlement of same-day ACH inbound transfers can expose your platform
to greater financial risk than from standard ACH inbound transfers. For example,
a connected account can initiate an inbound transfer that gets returned due to
insufficient funds in the source account. Same-day settlement leaves more time
to potentially withdraw the funds from the financial account before they’re
returned. If the connected account withdraws the funds, and then the return
causes a negative balance in the financial account, [your platform is
responsible](https://docs.stripe.com/treasury/account-management/working-with-balances-and-transactions#overdrafts).

## Retrieve an InboundTransfer

Use `GET /v1/treasury/inbound_transfers/{{INBOUND_TRANSFER_ID}}` to retrieve the
`InboundTransfer` object with the associated ID.

The following JSON shows the data you can include in the body of your request.
Some of the parameters in the response have additional details that are only
returned when you add them as values to the `expand[]` parameter. The fields
that you can expand have an “Expandable” comment in the following response
example. See [Expanding
Responses](https://docs.stripe.com/api/expanding_objects) to learn more about
expanding object responses.

```
{
 "id": "{{INBOUND_TRANSFER_ID}}",
 "object": "inbound_transfer",
 "livemode": false,
 "created": "{{Timestamp}}",
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}", // Expandable
 "amount": 1000,
 "currency": "usd",
// The only current valid PaymentMethod type for InboundTransfers is
us_bank_account
 "origin_payment_method": "{{PAYMENT_METHOD_ID}}",
```

See all 52 lines
The following request retrieves the `InboundTransfer` with the `id` value of
`{{INBOUND_TRANSFER_ID}}`. Including `transaction` in the `expand[]` array of
the body returns the relevant expanded information.

```
curl -G
https://api.stripe.com/v1/treasury/inbound_transfers/{{INBOUND_TRANSFER_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "expand[]"=financial_account
```

If successful, the response returns the `InboundTransfer` object with the
expanded information.

```
{
 "id": "{{INBOUND_TRANSFER_ID}}",
 "object": "inbound_transfer",
 "amount": 20000,
 "created": 1648071297,
 "currency": "usd",
 "description": "Inbound transfer",
 "failure_details": null,
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}",
"hosted_regulatory_receipt_url":
"https://payments.stripe.com/regulatory-receipt/{{INBOUND_TRANSFER_ID}}",
```

See all 78 lines
## List InboundTransfers

Use `GET /v1/treasury/inbound_transfers` to retrieve all the `InboundTransfers`
for the financial account with the associated ID. You can filter the list with
the standard list parameters or by `status`.

```
{
 // Standard list parameters
 "limit", "starting_after", "ending_before",
 // Filter by status
 "status": "processing" | "succeeded" | "failed",
 // Filter by FinancialAccount (Required)
 "financial_account": "{{FINANCIAL_ACCOUNT_ID}}", // Required
}

```

The following request retrieves all the inbound transfers with a status of
`succeeded` for the financial account with ID `{{FINANCIAL_ACCOUNT_ID}}`, which
is attached to the connected account with ID `{{CONNECTED_ACCOUNT_ID}}`.

```
curl -G https://api.stripe.com/v1/treasury/inbound_transfers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
 -d status=succeeded
```

## Manually review InboundTransfers

You can reduce the risk of inbound transfers by delaying when they’re submitted
to our banking partners or by holding funds for an extended period. These holds
can provide you with additional time to review potentially suspicious activity.
You can [request access](https://support.stripe.com/contact) to the
`inbound_transfers.ach.platform_review` feature to make financial accounts with
this feature enabled receive all inbound transfers with a
`requires_confirmation` status.

Below is an example of setting this feature on a new financial account. You can
also add other features.

```
curl https://api.stripe.com/v1/treasury/financial_accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "supported_currencies[]"=usd \
 -d "inbound_transfers[ach][requested]"=true \
 -d "inbound_transfers[ach][platform_review][requested]"=true
```

Below is an example of setting this feature on an existing financial account.

```
curl https://api.stripe.com/v1/treasury/financial_accounts/fa_xxx/features \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "supported_currencies[]"=usd \
 -d "inbound_transfers[ach][requested]"=true \
 -d "inbound_transfers[ach][platform_review][requested]"=true
```

Typically, we automatically send inbound transfers to the bank upon creation.
However, inbound transfers with a `requires_confirmation` status require
explicit user confirmation through the
`/v1/treasury/inbound_transfers/{id}/confirm` endpoint before we can submit the
transfers to our banking partners. You can review the inbound transfer details
and risk signals before confirming or canceling the transfer. You have 5
business days to confirm or cancel inbound transfers in the
`requires_confirmation` state. After 5 business days, the inbound transfer is
automatically canceled. For example, you have until the following Friday to
confirm an inbound transfer with the `requires_confirmation` state that’s
created on a Friday (assuming no US holidays).

Use the `funds_availability_delay` parameter with the `confirm` endpoint to
specify the delay (in seconds) to hold the funds before releasing them to the
intended financial account. This allows you to use the additional delay to
manually review a transfer. You can also use this field to hold funds past the
ACH return window, so the originating bank can’t recall funds after they’re
spent. For extra security, set `funds_availability_delay` to 432,000, which
releases funds beyond the return window.

Below is an example of calling the `confirm` endpoint without an availability
delay.

```
curl -X POST
https://api.stripe.com/v1/treasury/inbound_transfers/ibt_xxx/confirm \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

Below is an example of calling the `confirm` endpoint with an availability
delay.

```
curl https://api.stripe.com/v1/treasury/inbound_transfers/ibt_xxx/confirm \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d funds_availability_delay=432000
```

## InboundTransfer states

The following table describes each status and what the possible transition
states are.

STATUSDESCRIPTIONTRANSITIONS TO STATE`processing`The `InboundTransfer` creation
succeeded. Stripe instructs movement of funds on the network.`failed`,
`canceled`, `succeeded`, `requires_confirmation``requires_confirmation`The
`InboundTransfer` is created in an holding state. Stripe hasn’t initiated the
movement of funds on the network and the user has to explicitly confirm their
intent to trigger this inbound transfer using the
`/v1/treasury/inbound_transfers/:ID/confirm` endpoint.`processing`,
`canceled``failed` (terminal)The `InboundTransfer` failed to confirm. No
transaction was created, and the `payment_method` hasn’t been
debited.N/A`canceled` (terminal)The `InboundTransfer` was canceled prior to
submission to the network. Stripe voids the transaction and no funds are moved
from the external bank account.N/A`succeeded` (terminal)The `InboundTransfer`
succeeded and funds have landed in the account. A Transaction has been created.
InboundTransfers can be returned after succeeding if the external account pulls
back their funds, which is represented by a linked ReceivedDebit.N/A
## Test InboundTransfers

To test your integration end-to-end, use the [SetupIntents requests in test
mode](https://docs.stripe.com/api/setup_intents) to create a `PaymentMethod`,
then pass that `PaymentMethod` into an `InboundTransfer` creation request. Valid
`PaymentMethods` result in succeeded `InboundTransfers`, while invalid
`PaymentMethods` (for example, of unsupported types, containing an unverified
bank account, or not set up for inbound flows) throw the same errors as in live
mode.

## Test InboundTransfer states

Stripe also provides a set of test `PaymentMethod` tokens you can use to trigger
specific state transitions:

PAYMENT_METHOD VALUERESULT`pm_usBankAccount``InboundTransfer` that transitions
from `processing` to `succeeded`.`pm_usBankAccount_processing``InboundTransfer`
that remains in the `processing`
state.`pm_usBankAccount_internalFailure``InboundTransfer` that transitions from
`processing` to `failed`.
To test various edge cases more quickly, `PaymentMethod` tokens simulate
specific failure types:

PAYMENT_METHOD VALUERESULT`pm_usBankAccount_noAccount``InboundTransfer` that
transitions to failed with `failure_details.code=
"no_account"`.`pm_usBankAccount_accountClosed``InboundTransfer` that transitions
to `failed` with `failure_details.code=
"account_closed"`.`pm_usBankAccount_invalidAccountNumber``InboundTransfer` that
transitions to failed with `failure_details.code=
"invalid_account_number"`.`pm_usBankAccount_insufficientFunds``InboundTransfer`
that transitions to failed with `failure_details.code=
"insufficient_funds"`.`pm_usBankAccount_debitNotAuthorized``InboundTransfer`
that transitions to failed with `failure_details.code=
"debit_not_authorized"`.`pm_usBankAccount_dispute``InboundTransfer` that
transitions from `processing` to `succeeded` and is later disputed.
`inbound_transfer.returned` becomes `true`, and a linked `ReceivedDebit` is
created.
In all cases, the `InboundTransfer` response begins in the `processing` state.
You receive [webhooks](https://docs.stripe.com/webhooks) for each relevant state
transition, and fetching the `InboundTransfer` after creation returns the
expected state.

## InboundTransfer test helper endpoints

Stripe also provides endpoints that enable you to test `InboundTransfers` in
different states. Create an `InboundTransfer`, then:

- Use the [test succeed
endpoint](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_succeed)
to move the transfer with the associated ID directly into the `succeeded` state.

`POST
/v1/test_helpers/treasury/inbound_transfers/{{INBOUND_TRANSFER_ID}}/succeed`
- Use the [test fail
endpoint](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_fail)
to move the transfer with the associated ID directly into the `failed` state.

`POST /v1/test_helpers/treasury/inbound_transfers/{{INBOUND_TRANSFER_ID}}/fail`

These endpoints are particularly useful when testing error scenarios, such as
returns, which would otherwise require action from the external account the
InboundTransfer was pulling funds from.

Include the optional `failure_details.code` parameter in the body to indicate
why the transfer failed. If you don’t provide it, the transfer fails with the
default `could_not_process` failure code.

```
{
 "failure_details": {
 "code": "account_closed" |
 "account_frozen" |
 "bank_account_restricted" |
 "bank_ownership_changed" |
 "could_not_process" | // Generic fallback code
 "invalid_account_number" |
 "incorrect_account_holder_name" |
 "invalid_currency" |
 "no_account"
 }
}
```

Treasury also provides a `return` endpoint to simulate an InboundTransfer that
succeeds, but is later returned.

Use the [test return
endpoint](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_return)
to initiate the simulated return on the `InboundTransfer` with the associated
ID.

`POST
/v1/test_helpers/treasury/inbound_transfers/{{INBOUND_TRANSFER_ID}}/return`

All test endpoints trigger [webhooks](https://docs.stripe.com/webhooks) for each
relevant state transition, and fetching the `InboundTransfer` after transition
returns the expected state.

## InboundTransfer webhooks

Stripe emits the following `InboundTransfer` events to your
[webhook](https://docs.stripe.com/webhooks) endpoint:

- `treasury.inbound_transfer.created` on `InboundTransfer` creation.
- `treasury.inbound_transfer.{{new_status}}` when an `InboundTransfer` changes
status. Available status value options include:-
`treasury.inbound_transfer.succeeded`
- `treasury.inbound_transfer.failed`

## Links

- [InboundTransfer](https://docs.stripe.com/api/treasury/inbound_transfers)
- [Money movement
timelines](https://docs.stripe.com/treasury/money-movement/timelines#inboundtransfer-transactions)
- [ACH
Debit](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment)
- [payout to the financial
account](https://docs.stripe.com/treasury/moving-money/payouts)
- [SetupIntent](https://docs.stripe.com/api/setup_intents)
- [BankAccount](https://docs.stripe.com/api/customer_bank_accounts)
- [ExternalAccount](https://docs.stripe.com/api/external_accounts)
- [account owner’s
permission](https://docs.stripe.com/treasury/moving-money/working-with-bankaccount-objects)
- [cutoff
time](https://docs.stripe.com/treasury/money-movement/timelines#evolve-bank-and-trust--inbound)
- [your platform is
responsible](https://docs.stripe.com/treasury/account-management/working-with-balances-and-transactions#overdrafts)
- [Expanding Responses](https://docs.stripe.com/api/expanding_objects)
- [request access](https://support.stripe.com/contact)
- [webhooks](https://docs.stripe.com/webhooks)
- [test succeed
endpoint](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_succeed)
- [test fail
endpoint](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_fail)
- [test return
endpoint](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_return)