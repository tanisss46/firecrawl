# Migrating to the Payment Intents API

#### Interested in using Stripe Billing, Tax, discounts, shipping, or currency conversion?

We’re developing a Payment Element integration that manages subscriptions, tax,
discounts, shipping, and currency conversion. Read the [Build a checkout
page](https://docs.stripe.com/checkout/custom/quickstart) guide to learn more.

Learn how to migrate your existing cards and Charges API integration.

Migrating your payment flow can be daunting. It is safe to incrementally adopt
the Payment Intents API and use it in parallel with the Charges API. To this
end, you can split up the migration into the following steps:

- [Update your API version and your client
library](https://docs.stripe.com/payments/payment-intents/migration#api-version).
- If applicable, [migrate code that reads from Charge
properties](https://docs.stripe.com/payments/payment-intents/migration/charges)
so that you have a consistent read path between charges created by the Charges
API and charges created by the Payment Intents API. This ensures a read-side
integration that works for both your old and new payments integrations.
- Migrate your existing Charges API integration on
[Web](https://docs.stripe.com/payments/payment-intents/migration#web),
[iOS](https://docs.stripe.com/payments/accept-a-payment?platform=ios), and
[Android](https://docs.stripe.com/payments/accept-a-payment?platform=android) to
use the Payment Intents API.
- Migrate your integration that [saves cards on Customer
objects](https://docs.stripe.com/payments/payment-intents/migration#saved-cards).
- [Test with regulatory test
cards](https://docs.stripe.com/testing#regulatory-cards) to ensure your upgraded
integration handles authentication correctly.

## Update your API version and your client library

While the Payment Intents API works on all API versions, we recommend that you
[upgrade to the latest API
version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api). If you
decide to use an API version older than
[2019-02-11](https://docs.stripe.com/upgrades#2019-02-11), note the following
two changes as you go through the code examples:

- `requires_source` has been renamed to `requires_payment_method`
- `requires_source_action` has been renamed to `requires_action`

In addition, if you use one of our [SDKs](https://docs.stripe.com/sdks), upgrade
to the latest version of the library in order to use the Payment Intents API.

## Migrate your one-time payment flows

ElementsPayment Request ButtonLegacy CheckoutStripe.js v2
An integration built with Stripe.js & Elements consists of the following steps:

- Register your intent to collect payment on the server side
- Collect payment details on the client side
- Initiate creation of the payment
- Fulfill the customer’s order on the server side

### Step 1: Register intent to collect payment on the server side

[Create a PaymentIntent](https://docs.stripe.com/payments/payment-intents) on
your server and make it [accessible on the client
side](https://docs.stripe.com/payments/payment-intents#passing-to-client).

curlRubyPythonPHPJavaNodeGo.NETBeforeAfter
Not possible before

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=1099 \
 -d "currency"="usd"
```

### Step 2: Collect payment details on the client side

Use the
[confirmCardPayment](https://docs.stripe.com/js#stripe-confirm-card-payment)
function, which collects the payment information and submits it directly to
Stripe.

JavaScriptJavascript (ESNext)BeforeAfter
```
stripe.createToken(
 cardElement
).then(function(token) {
 // Send token to server
});
```

```
stripe.confirmCardPayment(
 INTENT_SECRET_FROM_STEP_1,
 {
 payment_method: {card: cardElement}
 }
).then(function(result) {
 if (result.error) {
 // Display error.message in your UI.
 } else {
 // The payment has succeeded
 // Display a success message
 }
});
```

### Step 3: Initiate creation of the payment

In your existing integration, the final step is using tokenized payment
information to create a charge on your server. This is no longer necessary, as
the `confirmCardPayment` function—called in the previous step—initiates creation
of the charge.

curlRubyPythonPHPJavaNodeGo.NETBeforeAfter
```
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "source"="{{FROM_PREVIOUS_STEP}}" \
 -d "amount"=1099 \
 -d "currency"="usd"
```

Completed in previous step

### Step 4: Fulfill the customer’s order

With automatic confirmation, the charge is created for you asynchronously based
on customer action on the client side, so you must [monitor
webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status) to
determine when the payment completes successfully. To perform steps like order
fulfillment after a customer’s payment is successful, implement support for
webhooks and monitor the `payment_intent.succeeded` event.

BeforeAfter
If charge succeeds, fulfill.

Subscribe to the `payment_intent.succeeded` webhook and fulfill in the webhook
handler.

Now that you have migrated, use the test cards in the following section to
verify your upgraded integration handles 3D Secure authentication.

## Migrate your integration that saves cards on Customer objects

Saving cards in checkout flowSaving cards outside checkout flowPaying with saved
cards
A Payment Intents API integration that collects card information in the checkout
flow consists of the following steps:

- Register your intent to collect payment on the server side
- Collect payment details on the client side
- Initiate creation of the payment
- Fulfill the customer’s order on the server side

### Step 1: Register intent to collect payment on the server side

[Create a PaymentIntent](https://docs.stripe.com/payments/payment-intents) on
your server. Set
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
to `off_session` if you primarily intend to charge users when they’re outside of
your application, or `on_session` if you plan to charge them in the application.
If you plan to use the card for both on and off session payments use
`off_session`. Providing the `setup_future_usage` parameter along with a
Customer ID will save the resulting PaymentMethod to that Customer after the
PaymentIntent has been confirmed and any required actions from the customer are
complete. Next, make the PaymentIntent [accessible on the client
side](https://docs.stripe.com/payments/payment-intents#passing-to-client).

curlRubyPythonPHPJavaNodeGo.NETBeforeAfter
Not possible before

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "setup_future_usage"="off_session" \
 -d "amount"=1099 \
 -d "currency"="usd"
```

### Step 2: Collect payment details on the client side

Use the
[confirmCardPayment](https://docs.stripe.com/js#stripe-confirm-card-payment)
function, which collects the payment information and submits it directly to
Stripe.

JavaScriptJavascript (ESNext)BeforeAfter
```
stripe.createToken(
// or stripe.createSource
 cardElement
).then(function(token) {
 // Send token to server
});
```

```
stripe.confirmCardPayment(
 '{{INTENT_SECRET_FROM_STEP_1}}',
 {
 payment_method: {card: cardElement},
 }
).then(function(result) {
 if (result.error) {
 // Display error.message in your UI.
 } else {
 // The payment has succeeded
 // Display a success message
 }
});
```

Finally, attach the payment method (`paymentIntent.payment_method`) to the
customer.

curlRubyPythonPHPJavaNodeGo.NETBeforeAfter
```
curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}}/sources \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "source"="{{TOKEN_OR_SOURCE}}"
```

```
curl https://api.stripe.com/v1/payment_method/{{PAYMENT_METHOD_ID}}/attach \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer"="{{CUSTOMER_ID}}"
```

### Step 3: Initiate creation of the payment

In your existing integration, the final step is using tokenized payment
information to create a charge on your server. This is no longer necessary, as
the `confirmCardPayment` function—called in the previous step—initiates creation
of the charge.

curlRubyPythonPHPJavaNodeGo.NETBeforeAfter
```
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "source"="{{FROM_PREVIOUS_STEP}}" \
 -d "customer"="{{CUSTOMER_ID}}" \
 -d "amount"=1099 \
 -d "currency"="usd"
```

Completed in previous step

### Step 4: Fulfill the customer’s order

With automatic confirmation, the charge is created for you asynchronously based
on customer action on the client side, so you must [monitor
webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status) to
determine when the payment completes successfully. To perform steps like order
fulfillment after a customer’s payment is successful, implement support for
webhooks and monitor the `payment_intent.succeeded` event.

BeforeAfter
If charge succeeds, fulfill.

Subscribe to the `payment_intent.succeeded` webhook and fulfill in the webhook
handler.

Now that you have migrated, use the test cards in the following section to
verify your upgraded integration handles 3D Secure authentication.

## Access saved payment methods

To display the customer’s previously saved Cards, Sources, and PaymentMethods,
[list the payment methods](https://docs.stripe.com/api/payment_methods/list)
instead of reading the
[sources](https://docs.stripe.com/api/customers/object#customer_object-sources)
property of the customer object. This is required because new PaymentMethods
added to a customer will not be duplicated in the sources property of the
customer object.

curlRubyPythonPHPJavaNodeGo.NETBeforeAfter
```
customer.sources
```

```
curl
https://api.stripe.com/v1/payment_methods?customer={{CUSTOMER_ID}}&type=card \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

## Test the integration

It’s important to thoroughly test your integration to make sure you’re correctly
handling cards that require additional authentication and cards that don’t. Use
these card numbers in a [sandbox](https://docs.stripe.com/keys#test-live-modes)
with any expiration date in the future and any three digit CVC code to validate
your integration when authentication is required and when it’s not required.

NumberAuthenticationDescription4000002500003155Required on setup or first
transactionThis test card requires authentication for [one-time
payments](https://docs.stripe.com/payments/accept-a-payment?platform=web).
However, if you set up this card using the [Setup Intents
API](https://docs.stripe.com/payments/save-and-reuse) and use the saved card for
subsequent payments, no further authentication is
needed.4000002760003184RequiredThis test card requires authentication on all
transactions.4000008260003178RequiredThis test card requires authentication, but
payments will be declined with an `insufficient_funds` failure code after
successful authentication.4000000000003055SupportedThis test card supports
authentication via 3D Secure 2, but does not require it. Payments using this
card do not require additional authentication in a sandbox unless your [sandbox
Radar
rules](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
request authentication.
Use these cards in your application or the [payments
demo](https://stripe-payments-demo.appspot.com/) to see the different behavior.

## See also

- [Payment Intents on
iOS](https://docs.stripe.com/payments/accept-a-payment?platform=ios)
- [Payment Intents on
Android](https://docs.stripe.com/payments/accept-a-payment?platform=android)

## Links

- [Build a checkout page](https://docs.stripe.com/checkout/custom/quickstart)
- [migrate code that reads from Charge
properties](https://docs.stripe.com/payments/payment-intents/migration/charges)
- [iOS](https://docs.stripe.com/payments/accept-a-payment?platform=ios)
- [Android](https://docs.stripe.com/payments/accept-a-payment?platform=android)
- [Test with regulatory test
cards](https://docs.stripe.com/testing#regulatory-cards)
- [upgrade to the latest API
version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api)
- [2019-02-11](https://docs.stripe.com/upgrades#2019-02-11)
- [SDKs](https://docs.stripe.com/sdks)
- [Create a PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [accessible on the client
side](https://docs.stripe.com/payments/payment-intents#passing-to-client)
- [confirmCardPayment](https://docs.stripe.com/js#stripe-confirm-card-payment)
- [monitor
webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status)
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
- [list the payment methods](https://docs.stripe.com/api/payment_methods/list)
-
[sources](https://docs.stripe.com/api/customers/object#customer_object-sources)
- [sandbox](https://docs.stripe.com/keys#test-live-modes)
- [one-time
payments](https://docs.stripe.com/payments/accept-a-payment?platform=web)
- [Setup Intents API](https://docs.stripe.com/payments/save-and-reuse)
- [sandbox Radar
rules](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
- [payments demo](https://stripe-payments-demo.appspot.com)