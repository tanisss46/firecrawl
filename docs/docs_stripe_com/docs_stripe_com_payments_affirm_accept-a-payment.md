# Accept an Affirm payment

## Learn how to accept Affirm, a buy now and pay later payment method.

Stripe-hosted pageDirect API
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

Affirm is a [single
use](https://docs.stripe.com/payments/payment-methods#usage), [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method that requires customers to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. Customers are redirected to the Affirm site, where they agree to
the terms of an installment plan. When the customer accepts the terms, funds are
guaranteed and transferred to your Stripe account. The customer repays Affirm
directly over time.

#### Note

Before you start the integration, make sure your account is eligible for Affirm
by navigating to your [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

[Determine
compatibility](https://docs.stripe.com/payments/affirm/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
Affirm payments:

- You can only use one-time line items. Affirm doesn’t support recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans.
- Express all [Prices](https://docs.stripe.com/api/prices) in your domestic
currency.
[Accept a
payment](https://docs.stripe.com/payments/affirm/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
Checkout integration.

Use this guide to learn how to enable Affirm—it shows the differences between
accepting a card payment and using Affirm.

### Enable Affirm as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `affirm` to the list of `payment_method_types`.
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
 payment_method_types: ['card', 'affirm'],
 line_items: [{
 price_data: {
 currency: 'usd',
 product_data: {
 name: 'T-shirt',
 },
# Make sure the total amount fits within Affirm's transaction amount limits
 unit_amount: 5000,
 },
 quantity: 1,
 }],
 shipping_address_collection: {
 # Shipping address is optional but recommended to pass in
# Specify which shipping countries Checkout should provide as options for
shipping locations
 allowed_countries: ['CA', 'US'],
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
integration](https://docs.stripe.com/payments/affirm/accept-a-payment#test-integration)
When testing your Checkout integration, select Affirm as the payment method and
click the **Pay** button.

Test your Affirm integration with your test API keys by viewing the redirect
page. You can test the successful payment case by authenticating the payment on
the redirect page. The PaymentIntent transitions from `requires_action` to
`succeeded`.

To test the case where the user fails to authenticate, use your test API keys
and view the redirect page. On the redirect page, close the Affirm modal window
and verify that payment failed. The PaymentIntent transitions from
`requires_action` to `requires_payment_method`.

When redirected to the Affirm sandbox, Affirm may ask for the last four digits
of your SSN. Affirm suggests using `'0000'` or `'5678'`.

For [manual
capture](https://docs.stripe.com/payments/affirm/accept-a-payment#manual-capture)
PaymentIntents in testmode, the uncaptured PaymentIntent auto-expires 10 minutes
after successful authorization.

## Failed payments

Affirm takes into account multiple factors when deciding to accept or decline a
transaction (for example, the length of time buyer has used Affirm, the
outstanding amount the customer has to repay, and the value of the current
order).

Always present additional payment options such as `card` in your checkout flow,
as Affirm payments have a higher rate of decline than many payment methods. In
these cases, the
[PaymentMethod](https://docs.stripe.com/api/payment_methods/object) is detached
and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
object’s status automatically transitions to `requires_payment_method`.

Other than a payment being declined, for an Affirm
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object) with a
status of `requires_action`, customers need to complete the payment within 12
hours after you redirect them to the Affirm site. If the customer takes no
action within 12 hours, the
[PaymentMethod](https://docs.stripe.com/api/payment_methods/object) is detached
and the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
object’s status automatically transitions to `requires_payment_method`.

In these cases, inform your customer to try again with a different payment
option presented in your checkout flow.

## Error codes

These are the common error codes and corresponding recommended actions:

Error codeRecommended action`payment_intent_payment_attempt_failed`A generic
failure indicating the Affirm checkout failed. Additional information may be
available in the charge outcome reason.`payment_method_provider_decline`Affirm
declined the customer’s payment. As a next step, the customer needs to contact
Affirm for more information.`payment_intent_payment_attempt_expired`The customer
never completed the payment on Affirm’s checkout page, and the payment session
has expired. Stripe automatically expires PaymentIntents that are not
successfully authorized 12 hours after initial checkout
creation.`payment_method_not_available`Affirm experienced a service related
error and is unable to complete the request. Retry at a later
time.`amount_too_small`Enter an amount within Affirm’s [default transactions
limits](https://docs.stripe.com/payments/affirm#payment-options).`amount_too_large`Enter
an amount within Affirm’s [default transactions
limits](https://docs.stripe.com/payments/affirm#payment-options).
Some errors might have additional insight included in the charge outcome reason:

Outcome ReasonWhat this means`generic_decline`The default outcome reason for a
payment error. This usually indicates that the partner declined the payment (for
example, because of insufficient funds), the bank issuer declined the charge,
the transaction included a high-risk purchase, or a similar reason. Stripe may
not always receive a decline reason for these
cases.`affirm_checkout_canceled`Either the customer has explicitly canceled the
Affirm checkout or Affirm has rejected the customer’s loan eligibility. Stripe
can’t distinguish the difference between these two types of events.

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
limits](https://docs.stripe.com/payments/affirm#payment-options)