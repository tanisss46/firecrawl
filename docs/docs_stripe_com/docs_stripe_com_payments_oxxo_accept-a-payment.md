# Accept an OXXO payment

## Learn how to accept OXXO, a common payment method in Mexico.

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

OXXO is a [single use](https://docs.stripe.com/payments/payment-methods#usage)
payment method where customers are required to [take additional
steps](https://docs.stripe.com/payments/payment-methods#customer-actions) to
complete their payment. [Customers](https://docs.stripe.com/api/customers) pay
by providing an OXXO voucher with a generated number and cash payment at an OXXO
convenience store.

[Determine
compatibility](https://docs.stripe.com/payments/oxxo/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support OXXO
payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency. If you have line items in different currencies, create separate
Checkout Sessions for each currency.
- You can only use one-time line items (recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans are
not supported).
[Accept a
payment](https://docs.stripe.com/payments/oxxo/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Use this guide to learn how to enable OXXO—it shows the differences between
accepting a card payment and using OXXO.

### Enable OXXO as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `oxxo` to the list of `payment_method_types`
- Make sure all your `line_items` use the `mxn` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'oxxo'],
 # The parameter is optional. The default value of expires_after_days is 3.
 payment_method_options: {
 oxxo: {
 expires_after_days: 2
 }
 },
 line_items: [{
 price_data: {
 # To accept `oxxo`, all line items must have currency: mxn
 currency: 'mxn',
 product_data: {
 name: 'T-shirt',
 },
 unit_amount: 2000,
 },
 quantity: 1,
 }],
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
})
```

### Additional payment method options

You can specify an optional `expires_after_days` parameter in the [payment
method
options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-oxxo-expires_after_days)
for your `Session` that sets the number of calendar days before an OXXO voucher
expires. For example, if you create an OXXO voucher on Monday and you set
`expires_after_days` to 2, the OXXO voucher will expire on Wednesday at 23:59
America/Mexico_City (UTC-6) time. The `expires_after_days` parameter can be set
from 1 to 7 days. The default is 3 days.

### Redirect to Stripe hosted voucher page

After submitting the Checkout form successfully, the customer is redirected to
the `hosted_voucher_url`. The customer can find the barcode or print the OXXO
voucher from the hosted voucher page. You can locate the `hosted_voucher_url` in
[payment_intent.next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-oxxo_display_details-hosted_voucher_url).

Stripe allows customization of customer-facing UIs on the [Branding
Settings](https://dashboard.stripe.com/account/branding) page. The following
brand settings can be applied to the voucher:

- **Icon**—your brand image and public business name
- **Accent color**—used as the color of Print button
- **Brand color**—used as the background color

### Fulfill your orders

Because OXXO is a delayed notification payment method, you need to use a method
such as [webhooks](https://docs.stripe.com/webhooks) to monitor the payment
status and handle order fulfillment. Learn more about [setting up webhooks and
fulfilling orders](https://docs.stripe.com/checkout/fulfillment).

The following events are sent when the payment status changes:

Event NameDescriptionNext steps

[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)

The customer has successfully submitted the Checkout form. Stripe has generated
the OXXO voucher.

You can choose to email the `hosted_voucher_url` to your customer in case they
lose the OXXO voucher.

Wait for the customer to pay the OXXO voucher.

[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)The
customer has successfully paid the OXXO. The `PaymentIntent` transitions to
`succeeded`.Fulfill the goods or services that the customer
purchased.[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)The
OXXO voucher has expired, or the payment has failed for some other reason. The
`PaymentIntent` returns to a status of `requires_payment_method`.Contact the
customer via email and request that they place a new order.[Test your
integration](https://docs.stripe.com/payments/oxxo/accept-a-payment#test-integration)
When testing your Checkout integration, select OXXO as the payment method and
click the **Pay** button.

EmailDescription
`{any_prefix}@{any_domain}`

Simulates an OXXO voucher which a customer pays after 3 minutes and the
`payment_intent.succeeded` webhook arrives after about 3 minutes. In production,
this webhook arrives after 1 business day.

Example: fulano@test.com

`{any_prefix}succeed_immediately@{any_domain}`

Simulates an OXXO voucher which a customer pays immediately and the
`payment_intent.succeeded` webhook arrives within several seconds. In
production, this webhook arrives after 1 business day.

Example: succeed_immediately@test.com

`{any_prefix}expire_immediately@{any_domain}`

Simulates an OXXO voucher which expires before a customer pays and the
`payment_intent.payment_failed` webhook arrives within several seconds.

The `expires_after` field in
[next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-oxxo_display_details-expires_after)
is set to the current time regardless of what the `expires_after_days` parameter
in [payment method
options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-oxxo-expires_after_days)
is set to.

Example: expire_immediately@test.com

`{any_prefix}expire_with_delay@{any_domain}`

Simulates an OXXO voucher which expires before a customer pays and the
`payment_intent.payment_failed` webhook arrives after about 3 minutes.

The `expires_after` field in
[next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-oxxo_display_details-expires_after)
is set to 3 minutes in the future regardless of what the `expires_after_days`
parameter in [payment method
options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-oxxo-expires_after_days)
is set to.

Example: expire_with_delay@test.com

`{any_prefix}fill_never@{any_domain}`

Simulates an OXXO voucher which expires before a customer pays and the
`payment_intent.payment_failed` webhook arrives after 1 business day and 2
calendar days. In production, this webhook arrives at the same time as in
testmode.

Example: fill_never@test.com

[OptionalSend payment instruction
emails](https://docs.stripe.com/payments/oxxo/accept-a-payment#instruction-emails)
## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
- [take additional
steps](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Customers](https://docs.stripe.com/api/customers)
- [Prices](https://docs.stripe.com/api/prices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [payment method
options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-oxxo-expires_after_days)
-
[payment_intent.next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-oxxo_display_details-hosted_voucher_url)
- [Branding Settings](https://dashboard.stripe.com/account/branding)
- [webhooks](https://docs.stripe.com/webhooks)
- [setting up webhooks and fulfilling
orders](https://docs.stripe.com/checkout/fulfillment)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
-
[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)
-
[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)
-
[next_action.oxxo_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-oxxo_display_details-expires_after)
- [payment method
options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-oxxo-expires_after_days)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)