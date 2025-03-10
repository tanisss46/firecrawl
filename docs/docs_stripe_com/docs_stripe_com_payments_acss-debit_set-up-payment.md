# Save details for future payments with pre-authorized debit in Canada

## Save payment method details for future Canadian pre-authorized debit payments.

Stripe-hosted pageAdvanced integration
You can use the [Setup Intents
API](https://docs.stripe.com/payments/setup-intents) to collect payment method
details in advance, with the final amount or payment date determined later. This
is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a subscription

#### Note

Pre-authorized debit in Canada is a **delayed notification payment method**,
which means that funds are not immediately available after payment. A payment
typically takes **5 business days** to arrive in your account.

Most bank accounts in Canada hold Canadian dollars (CAD), with a small number of
accounts in other currencies, including US dollars (USD). It is possible to
accept PAD payments in either CAD or USD, but choosing the correct currency for
your customer is important to avoid payment failures.

Unlike many card-based payment methods, you might not be able to successfully
debit a CAD account in USD or debit a USD account in CAD. Most often, attempting
to do so results in a delayed payment failure that takes up to five business
days.

To avoid these failures, it is safest to set up PAD bank accounts in CAD unless
you are confident your customer’s account accepts USD debits.

[Set up
StripeServer-side](https://docs.stripe.com/payments/acss-debit/set-up-payment#checkout-set-up-stripe)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Create or retrieve a
CustomerServer-side](https://docs.stripe.com/payments/acss-debit/set-up-payment#checkout-create-customer)
To reuse a bank account for future payments, it must be attached to a
[Customer](https://docs.stripe.com/api/customers).

Create a Customer object when your customer creates an account with your
business. Associating the ID of the Customer object with your own internal
representation of a customer lets you retrieve and use the stored payment method
details later. If your customer hasn’t created an account, you can still create
a Customer object now and associate it with your internal representation of the
customer’s account later.

Create a new Customer or retrieve an existing Customer to associate with these
payment details. Include the following code on your server to create a new
Customer.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Set up future
payments](https://docs.stripe.com/payments/acss-debit/set-up-payment#setup-a-payment)
#### Note

This guide builds on the foundational [set up future
payments](https://docs.stripe.com/payments/save-and-reuse) Checkout integration.

Use this guide to learn how to enable Canadian Pre-Authorized Debits (PADs)—it
shows the differences between setting up future payments for cards and using
PADs.

### Enable Canadian pre-authorized debit as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

Pre-authorized debit in Canada

- Add `acss_debit` to the list of `payment_method_types`.
- Specify additional
[payment_method_options](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-acss_debit)
parameters to describe your transaction. Learn more below.

Payments must specify a [payment
schedule](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-acss_debit-mandate_options-payment_schedule)
for customers to authorize when checking out. See [PAD
Mandates](https://docs.stripe.com/payments/acss-debit#mandates) for details on
how to choose the right mandate options for your business:

ParameterValueRequired`payment_method_options[acss_debit][currency]`Currency to
use for future payments with this payment method. Must match the customer’s bank
account currency. Accepted values are `cad` or
`usd`.Yes`payment_method_options[acss_debit][mandate_options][payment_schedule]`The
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
 mode: 'setup',
 payment_method_types: ['card'],
 payment_method_types: ['acss_debit'],

 # or you can take multiple payment methods with
 # payment_method_types: ['card', 'acss_debit', ...]
 payment_method_options: {
 acss_debit: {
 currency: 'cad',
 mandate_options: {
 payment_schedule: 'interval',
 interval_description: 'First day of every month',
 transaction_type: 'personal',
 }
 }
 },
 customer: customer.id,
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
})
```

During the Checkout session, the customer is presented with a UI modal that
handles bank account details collection and instant verification with an
optional fallback to verification using microdeposits. If the customer opts for
microdeposit verification, Stripe automatically sends two small deposits to the
provided bank account which take 1-2 business days to appear on the customer’s
online bank statement. When the deposits are expected to arrive, the customer
receives an email with a link to confirm these amounts and verify the bank
account with Stripe. After verification is completed, the payment method is
ready to be used for future payments.

[Test your
integration](https://docs.stripe.com/payments/acss-debit/set-up-payment#checkout-test-integration)
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
other number combinationsFails account verification.[Use the payment
methodServer-side](https://docs.stripe.com/payments/acss-debit/set-up-payment#use-the-payment-method)
After completing the Checkout Session, you can
[collect](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=stripe-hosted#retrieve-checkout-session)
the [PaymentMethod](https://docs.stripe.com/api/payment_methods) ID and a
[Mandate](https://docs.stripe.com/api/mandates) ID. You can use these to
initiate future payments without having to prompt the customer for their bank
account a second time.

#### Warning

Future pre-authorized debit payments must be charged according to the terms of
the existing mandate. Debiting at any time that doesn’t meet the terms of the
mandate could be cause for a payment dispute.

When you’re ready to charge your customer off-session, provide the
`payment_method`, `customer`, and `mandate` IDs when [creating a
PaymentIntent](https://docs.stripe.com/api/payment_intents/create).

[OptionalInstant only
verificationServer-side](https://docs.stripe.com/payments/acss-debit/set-up-payment#checkout-instant-only)[OptionalMicro-deposit
only
verificationServer-side](https://docs.stripe.com/payments/acss-debit/set-up-payment#checkout-microdeposit-only)

## Links

- [Setup Intents API](https://docs.stripe.com/payments/setup-intents)
- [Register now](https://dashboard.stripe.com/register)
- [Customer](https://docs.stripe.com/api/customers)
- [set up future payments](https://docs.stripe.com/payments/save-and-reuse)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[payment_method_options](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-acss_debit)
- [payment
schedule](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-acss_debit-mandate_options-payment_schedule)
- [PAD Mandates](https://docs.stripe.com/payments/acss-debit#mandates)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
-
[collect](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=stripe-hosted#retrieve-checkout-session)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [Mandate](https://docs.stripe.com/api/mandates)
- [creating a PaymentIntent](https://docs.stripe.com/api/payment_intents/create)