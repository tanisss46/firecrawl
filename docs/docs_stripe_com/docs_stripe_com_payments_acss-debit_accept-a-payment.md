# Accept a Canadian pre-authorized debit payment

## Build a custom payment form or use Stripe Checkout to accept payments with pre-authorized debit in Canada.

Stripe-hosted pageAdvanced integration
#### Caution

Stripe automatically presents your customers payment method options by
evaluating their currency, payment method restrictions, and other parameters. We
recommend that you configure your payment methods from the Stripe Dashboard
using the instructions in [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted).

If you want to continue manually configuring the payment methods you present to
your customers with Checkout, use this guide. Otherwise, update your integration
to [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods).

Accepting Canadian pre-authorized debit (PAD) payments on your website consists
of creating an object to track a payment, collecting payment method information
and mandate acknowledgement, submitting the payment to Stripe for processing and
verifying your customer’s bank account.

With Checkout, you can create a Checkout Session with `acss_debit` as a payment
method type to track and handle the states of the payment until the payment
completes.

#### Note

Pre-authorized debit in Canada is a **delayed notification payment method**,
which means that funds are not immediately available after payment. A payment
typically takes **5 business days** to arrive in your account.

[Determine
compatibility](https://docs.stripe.com/payments/acss-debit/accept-a-payment#compatibility)
To support Canadian pre-authorized debit payments, a Checkout Session must
satisfy all of the following conditions:

- You can only use one-time line items
([subscriptions](https://docs.stripe.com/billing/subscriptions/creating) are not
yet supported in Checkout).
- [Prices](https://docs.stripe.com/api/prices) for all line items must be
expressed in Canadian or US dollars (currency code `cad` or `usd`).
- Prices for all line items must be in the same currency. If you have line items
in different currencies, create separate Checkout Sessions for each currency.

### Presentment currency

Most bank accounts in Canada hold Canadian dollars (CAD), with a small number of
accounts in other currencies, including US dollars (USD). It is possible to
accept PAD payments in either CAD or USD, but choosing the correct currency for
your customer is important to avoid payment failures.

Unlike many card-based payment methods, you might not be able to successfully
debit a CAD account in USD or debit a USD account in CAD. Most often, attempting
to do so results in a delayed payment failure that takes up to five business
days.

To avoid these failures, it is safest to take PAD payments in CAD unless you are
confident your customer’s account accepts USD debits.

[Accept a
payment](https://docs.stripe.com/payments/acss-debit/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

This guides you through enabling Canadian pre-authorized debit and shows the
differences between accepting a card payment and using this payment method.

### Enable Canadian pre-authorized debit as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `acss_debit` to the list of `payment_method_types`.
- Make sure all your `line_items` use the `cad` currency.
- Specify additional
[payment_method_options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-acss_debit)
parameters to describe your transaction. Learn more below.

Payments must specify a [payment
schedule](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-acss_debit-mandate_options-payment_schedule)
for customers to authorize when checking out. See [PAD
Mandates](https://docs.stripe.com/payments/acss-debit#mandates) for details on
how to choose the right mandate options for your business:

ParameterValueRequired?`payment_method_options[acss_debit][mandate_options][payment_schedule]`The
mandate payment schedule. Accepted values are `interval`, `sporadic`, or
`combined`. See the [PAD
Mandates](https://docs.stripe.com/payments/acss-debit#mandates) overview to help
you select the right schedule for your
business.Yes`payment_method_options[acss_debit][mandate_options][interval_description]`Text
description of the payment schedule. See the [PAD
Mandates](https://docs.stripe.com/payments/acss-debit#mandates) overview to help
you construct the right interval description for your business.Required if
`payment_schedule` value is `interval` or
`combined``payment_method_options[acss_debit][mandate_options][transaction_type]`The
type of the mandate you’re creating, either `personal` (if your customer is an
individual) or `business` (if your customer is a business).Yes
### Create a Checkout session

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['acss_debit'],

 # or you can take multiple payment methods with
 # payment_method_types: ['card', 'acss_debit', ...]
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `acss_debit`, all line items must have currency: cad, usd
 currency: 'cad',
 product_data: {
 name: 'T-shirt',
 },
 unit_amount: 2000,
 },
 quantity: 1,
 }],
 payment_method_options: {
 acss_debit: {
 mandate_options: {
 payment_schedule: 'interval',
 interval_description: 'On ',
 transaction_type: 'personal',
 }
 }
 },
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
})
```

During the Checkout session, the customer is presented with a UI modal that
handles bank account details collection and instant verification with an
optional fallback to verification using micro-deposits. In the uncommon case
that the customer opts for micro-deposit verification, Stripe automatically
sends two small deposits to the provided bank account which take 1-2 business
days to appear on the customer’s online bank statement. When the deposits are
expected to arrive, the customer receives an email with a link to confirm these
amounts and verify the bank account with Stripe. Once completed, the payment
begins processing.

### Fulfill your orders

After accepting a payment, learn how to [fulfill
orders](https://docs.stripe.com/checkout/fulfillment).

[Test your
integration](https://docs.stripe.com/payments/acss-debit/accept-a-payment#test-integration)
### Receive micro-deposit verification email

In order to receive the micro-deposit verification email in test mode after
collecting the bank account details and accepting a mandate, provide an email in
the `payment_method[billing_details][email]` field in the form of
`{any_prefix}+test_email@{any_domain}` when confirming the payment method
details.

### Test account numbers

Stripe provides several test account numbers you can use to make sure your
integration for manually-entered bank accounts is ready for production. All test
accounts that automatically succeed or fail the payment must be verified using
the test micro-deposit amounts below before they can be completed.

Institution NumberTransit NumberAccount
NumberScenario`000``11000``000123456789`Succeeds the payment immediately after
micro-deposits are verified.`000``11000``900123456789`Succeeds the payment with
a three-minute delay after micro-deposits are
verified.`000``11000``000222222227`Fails the payment immediately after
micro-deposits are verified.`000``11000``900222222227`Fails the payment with a
three-minute delay after micro-deposits are
verified.`000``11000``000666666661`Fails to send verification
micro-deposits.`000``11000``000777777771`Fails the payment due to the payment
amount causing the account to exceed its weekly payment volume
limit.`000``11000``000888888881`Fails the payment due to the payment amount
exceeding the account’s transaction limit.
To mimic successful or failed bank account verifications in test mode, use these
meaningful amounts for micro-deposits:

Micro-deposit ValuesScenario`32` and `45`Successfully verifies the account.Any
other number combinationsFails account verification.[Handle refunds and
disputes](https://docs.stripe.com/payments/acss-debit/accept-a-payment#refunds-and-disputes)
The refund period for Canadian pre-authorized debit is up to 180 days after the
original payment.

Customers can dispute a payment through their bank up to 90 calendar days after
the original payment and there is no appeals process.

Learn more about [Canadian pre-authorized debit
disputes](https://docs.stripe.com/payments/acss-debit#disputed-payments).

## Additional considerations

### Microdeposit verification failure

When a bank account is pending verification with micro-deposits, it is possible
for the customer to fail to verify for two reasons:

- The micro-deposits failed to send to the customer’s bank account (usually
indicates a closed/unavailable bank account or incorrect bank account number).
- The customer made three failed verification for the account. Exceeding this
limit means the bank account can no longer be verified or reused.
- The customer failed to verify the bank account within 10 days.

If the bank account fails verification for one of these reasons, you can [handle
the checkout.session.async_payment_failed
event](https://docs.stripe.com/api/events/types?event_types-invoice.payment_succeeded=#event_types-checkout.session.async_payment_failed)
to contact the customer about placing a new order.

[OptionalInstant only
verificationServer-side](https://docs.stripe.com/payments/acss-debit/accept-a-payment#checkout-instant-only)[OptionalMicro-deposit
only
verificationServer-side](https://docs.stripe.com/payments/acss-debit/accept-a-payment#checkout-microdeposit-only)[OptionalConfigure
customer debit
dateServer-side](https://docs.stripe.com/payments/acss-debit/accept-a-payment#web-target-date)
## See also

- [More about pre-authorized debit in
Canada](https://docs.stripe.com/payments/acss-debit)
- [Managing mandates](https://docs.stripe.com/payments/acss-debit#mandates)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Prices](https://docs.stripe.com/api/prices)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[payment_method_options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-acss_debit)
- [payment
schedule](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-acss_debit-mandate_options-payment_schedule)
- [PAD Mandates](https://docs.stripe.com/payments/acss-debit#mandates)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [Canadian pre-authorized debit
disputes](https://docs.stripe.com/payments/acss-debit#disputed-payments)
- [handle the checkout.session.async_payment_failed
event](https://docs.stripe.com/api/events/types?event_types-invoice.payment_succeeded=#event_types-checkout.session.async_payment_failed)
- [More about pre-authorized debit in
Canada](https://docs.stripe.com/payments/acss-debit)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)