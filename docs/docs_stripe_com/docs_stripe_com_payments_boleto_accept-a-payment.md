# Boleto payments

## Learn how to accept Boleto, a common payment method in Brazil.

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

Boleto is a [single use](https://docs.stripe.com/payments/payment-methods#usage)
payment method where customers are required to [take additional
steps](https://docs.stripe.com/payments/payment-methods#customer-actions) to
complete their payment. [Customers](https://docs.stripe.com/api/customers) pay
by using a Boleto voucher with a generated number either in ATMs, banks, bank
portals or authorized agencies.

[Determine
compatibility](https://docs.stripe.com/payments/boleto/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
Boleto payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency. If you have line items in different currencies, create separate
Checkout Sessions for each currency.
- You can only use one-time line items (recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans are
not supported).
[Accept a
payment](https://docs.stripe.com/payments/boleto/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Use this guide to learn how to enable Boleto—it shows the differences between
accepting a card payment and using Boleto.

### Enable Boleto as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `boleto` to the list of `payment_method_types`
- Make sure all your `line_items` use the `brl` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'boleto'],
 # The parameter is optional. The default value of expires_after_days is 3.
 payment_method_options: {
 boleto: {
 expires_after_days: 7
 }
 },
 line_items: [{
 price_data: {
 # To accept `boleto`, all line items must have currency: brl
 currency: 'brl',
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
options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-boleto-expires_after_days)
for your `Session` that sets the number of calendar days before a Boleto voucher
expires. For example, if you create a Boleto voucher on Monday and you set
`expires_after_days` to 2, the Boleto voucher expires on Wednesday at 23:59
America/Sao_Paulo (UTC-3) time. If you set it to 0, the Boleto voucher expires
at the end of the day. The `expires_after_days` parameter can be set from 0 to
60 days. The default is 3 days. You can customize the default expiration days on
your account in the [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)

### Redirect to Stripe hosted voucher page

#### Note

Unlike card payments, the customer won’t be redirected to the
[success_url](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-success_url)
with Boleto payment.

After submitting the Checkout form successfully, the customer is redirected to
the `hosted_voucher_url`. The customer can copy the Boleto number or download
the voucher PDF from the hosted voucher page.

Stripe sends a
[payment_intent.requires_action](https://docs.stripe.com/api/events/types#event_types-payment_intent.requires_action)
event when a Boleto voucher is created successfully. If you need to email your
customers the voucher link, you can locate the `hosted_voucher_url` in
[payment_intent.next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-boleto_display_details-hosted_voucher_url).
Learn more about how to [monitor a PaymentIntent with
webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status#webhooks).

Stripe allows customization of customer-facing UIs on the [Branding
Settings](https://dashboard.stripe.com/account/branding) page. The following
brand settings can be applied to the voucher:

- **Icon**—your brand image and public business name
- **Accent color**—used as the color of the Number button
- **Brand color**—used as the background color

### Fulfill your orders

Because Boleto is a delayed notification payment method, you need to use a
method such as [webhooks](https://docs.stripe.com/webhooks) to monitor the
payment status and handle order fulfillment. Learn more about [setting up
webhooks and fulfilling orders](https://docs.stripe.com/checkout/fulfillment).

The following events are sent when the payment status changes:

Event NameDescriptionNext steps

[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)

The customer has successfully submitted the Checkout form. Stripe has generated
the Boleto voucher.

You can choose to email the `hosted_voucher_url` to your customer in case they
lose the Boleto voucher.

Wait for the customer to pay the Boleto.

[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)The
customer has successfully paid the Boleto. The `PaymentIntent` transitions to
`succeeded`.Fulfill the goods or services that the customer
purchased.[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)The
Boleto voucher has expired, or the payment has failed for some other reason. The
`PaymentIntent` returns to a status of `requires_payment_method`.Contact the
customer via email and request that they place a new order.[Test your
integration](https://docs.stripe.com/payments/boleto/accept-a-payment#test-integration)
When testing your Checkout integration, select Boleto as the payment method and
click the **Pay** button.

EmailDescription
`{any_prefix}@{any_domain}`

Simulates a Boleto voucher which a customer pays after 3 minutes and the
`payment_intent.succeeded` webhook arrives after about 3 minutes. In production,
this webhook arrives 1 business day after a payment.

Example: fulaninho@example.com

`{any_prefix}succeed_immediately@{any_domain}`

Simulates a Boleto voucher which a customer pays immediately and the
`payment_intent.succeeded` webhook arrives within several seconds. In
production, this webhook arrives 1 business day after a payment.

Example: succeed_immediately@example.com

`{any_prefix}expire_immediately@{any_domain}`

Simulates a Boleto voucher which expires before a customer pays and the
`payment_intent.payment_failed` webhook arrives within several seconds.

The `expires_at` field in
[next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-boleto_display_details-expires_at)
is set to the current time regardless of what the `expires_after_days` parameter
in [payment method
options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-boleto-expires_after_days)
is set to.

Example: expire_immediately@example.com

`{any_prefix}expire_with_delay@{any_domain}`

Simulates a Boleto voucher which expires before a customer pays and the
`payment_intent.payment_failed` webhook arrives after about 3 minutes.

The `expires_at` field in
[next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-boleto_display_details-expires_at)
is set to 3 minutes in the future regardless of what the `expires_after_days`
parameter in [payment method
options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-boleto-expires_after_days)
is set to.

Example: expire_with_delay@example.com

`{any_prefix}fill_never@{any_domain}`

Simulates a Boleto voucher which never succeeds; it expires according to the
`expires_at` field in
[next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-boleto_display_details-expires_at)
per the provided parameters in the [payment method
options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-boleto-expires_after_days)
and the `payment_intent.payment_failed` webhook arrives after that.

Example: fill_never@example.com

Tax IDDescription
CPF `000.000.000-00`

CNPJ `00.000.000/0000-00`

In a sandbox, set `tax_id` to these values, so they bypass the tax ID
validation.

[Handle
refunds](https://docs.stripe.com/payments/boleto/accept-a-payment#refunds)
Boleto payments can’t be refunded. Some merchants have created a separate
process to credit their customers who reach out directly.

[Handle
disputes](https://docs.stripe.com/payments/boleto/accept-a-payment#disputes)
Boleto payments can’t be disputed by the customer.

[OptionalSend payment instruction
emails](https://docs.stripe.com/payments/boleto/accept-a-payment#instruction-emails)
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
options](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-boleto-expires_after_days)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
-
[success_url](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-success_url)
-
[payment_intent.requires_action](https://docs.stripe.com/api/events/types#event_types-payment_intent.requires_action)
-
[payment_intent.next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-boleto_display_details-hosted_voucher_url)
- [monitor a PaymentIntent with
webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status#webhooks)
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
[next_action.boleto_display_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-boleto_display_details-expires_at)
- [payment method
options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-boleto-expires_after_days)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)