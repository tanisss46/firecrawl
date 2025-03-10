# Accept an Afterpay or Clearpay payment

## Learn how to accept Afterpay (also known as Clearpay in the UK), a payment method in the US, CA, UK, AU, and NZ.

WebMobileStripe-hosted pageDirect API
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

Afterpay is a [single
use](https://docs.stripe.com/payments/payment-methods#usage), [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method that requires customers to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. Customers are redirected to the Afterpay site, where they agree
to the terms of an installment plan. When the customer accepts the terms,
Afterpay guarantees that the funds are available to the customer and transfers
the funds to your Stripe account. The customer repays Afterpay directly over
time.

#### Note

Before you start the integration, make sure your account is eligible for
Afterpay by navigating to your [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

[Determine
compatibility](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
Afterpay payments:

- You can only use one-time line items (recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans are
not supported).
- You must express [Prices](https://docs.stripe.com/api/prices) in your domestic
currency.
[Accept a
payment](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
Checkout integration.

Use this guide to learn how to enable Afterpay—it shows the differences between
accepting a card payment and using Afterpay.

### Enable Afterpay as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `afterpay_clearpay` to the list of `payment_method_types`.
- Make sure all your `line_items` use your domestic currency.
- We recommend collecting shipping addresses by adding your country to
`shipping_address_collection[allowed_countries]`. If you don’t want to collect
shipping addresses with Checkout, you can also provide the shipping address
using `payment_intent_data[shipping]`. Doing so helps with loan acceptance
rates.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'afterpay_clearpay'],
 line_items: [{
 price_data: {
 currency: 'usd',
 product_data: {
 name: 'T-shirt',
 },
# Make sure the total amount fits within Afterpay transaction amount limits:
# https://stripe.com/docs/payments/afterpay-clearpay#collection-schedule
 unit_amount: 2000,
 },
 quantity: 1,
 }],
 shipping_address_collection: {
 # Shipping address is optional but recommended to pass in
# Specify which shipping countries Checkout should provide as options for
shipping locations
 allowed_countries: ['AU', 'CA', 'GB', 'NZ', 'US'],
 },
# If you already have the shipping address, provide it in payment_intent_data:
 # payment_intent_data: {
 # shipping: {
 # name: 'Jenny Rosen',
 # address: {
 # line1: '1234 Main Street',
 # city: 'San Francisco',
 # state: 'CA',
 # country: 'US',
 # postal_code: '94111',
 # },
 # },
 # },
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
 })
```

### Fulfill your orders

[Use a method such as
webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status#webhooks)
to handle order fulfillment, instead of relying on your customer to return to
the payment status page.

The following events are sent when the payment status changes:

Event NameDescriptionNext
steps[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)The
customer successfully authorized the payment by submitting the Checkout
form.Wait for the payment to succeed or
fail.[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)The
customer’s payment succeeded. The `PaymentIntent` transitions to
`succeeded`.Fulfill the goods or services that the customer
purchased.[payment_intent.payment_failed](https://docs.stripe.com/api/events/types#event_types-payment_intent.payment_failed)The
customer’s payment was declined, or failed for some other reason. The
`PaymentIntent` returns to the `requires_payment_method` status.Email the
customer to request that they place a new order.
Learn more about [fulfilling
orders](https://docs.stripe.com/checkout/fulfillment).

[Test your
integration](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment#test-integration)
When testing your Checkout integration, select Afterpay as the payment method
and click the **Pay** button.

Test your Afterpay integration with your test API keys by viewing the redirect
page. You can test the successful payment case by authenticating the payment on
the redirect page. The PaymentIntent will transition from `requires_action` to
`succeeded`.

To test the case where the user fails to authenticate, use your test API keys
and view the redirect page. On the redirect page, click **Fail test payment**.
The PaymentIntent will transition from `requires_action` to
`requires_payment_method`.

For [manual
capture](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment#manual-capture)
PaymentIntents in testmode, the uncaptured PaymentIntent will auto-expire 10
minutes after successful authorization.

## Failed payments

Afterpay takes into account multiple factors when deciding to accept or decline
a transaction (for example, length of time buyer has been using Afterpay,
outstanding amount customer has to repay, value of the current order).

You should always present additional payment options such as `card` in your
checkout flow, as Afterpay payments have a higher rate of decline than many
payment methods. In these cases, the
[PaymentMethod](https://docs.stripe.com/api/payment_methods/object) is detached
and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
object’s status automatically transitions to `requires_payment_method`.

For an Afterpay
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object) with a
status of `requires_action`, customers need to complete the payment within 3
hours after you redirect them to the Afterpay site (this doesn’t apply to
declined payments). If they take no action within 3 hours, the
[PaymentMethod](https://docs.stripe.com/api/payment_methods/object) detaches and
the object status for the
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
automatically transitions to `requires_payment_method`.

In these cases, inform your customer to try again with a different payment
option presented in your checkout flow.

## Error codes

These are the common error codes and corresponding recommended actions:

Error codeRecommended action`payment_intent_payment_attempt_failed`A generic
failure indicating the Afterpay checkout failed. This can also be a decline
which does not appear as a decline error
code.`payment_method_provider_decline`Afterpay declined the customer’s payment.
As a next step, the customer needs to contact Afterpay for more
information.`payment_intent_payment_attempt_expired`The customer never completed
the payment on Afterpay’s checkout page, and the payment session has expired.
Stripe automatically expires Payment Intents that are not successfully
authorized 3 hours after initial checkout
creation.`payment_method_not_available`Afterpay experienced a service related
error and is unable to complete the request. Retry at a later
time.`amount_too_small`Enter an amount within Afterpay’s [default transactions
limits](https://docs.stripe.com/payments/afterpay-clearpay#collection-schedule)
for the country.`amount_too_large`Enter an amount within Afterpay’s [default
transactions
limits](https://docs.stripe.com/payments/afterpay-clearpay#collection-schedule)
for the country.
## See also

- [More about Afterpay](https://docs.stripe.com/payments/afterpay-clearpay)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Prices](https://docs.stripe.com/api/prices)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[https://stripe.com/docs/payments/afterpay-clearpay#collection-schedule](https://stripe.com/docs/payments/afterpay-clearpay#collection-schedule)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [Use a method such as
webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status#webhooks)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
-
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
-
[payment_intent.payment_failed](https://docs.stripe.com/api/events/types#event_types-payment_intent.payment_failed)
- [fulfilling orders](https://docs.stripe.com/checkout/fulfillment)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods/object)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [default transactions
limits](https://docs.stripe.com/payments/afterpay-clearpay#collection-schedule)
- [More about Afterpay](https://docs.stripe.com/payments/afterpay-clearpay)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)