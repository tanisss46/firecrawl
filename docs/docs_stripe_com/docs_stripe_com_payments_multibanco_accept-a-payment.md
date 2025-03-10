# Accept a Multibanco payment

## Learn how to accept the Multibanco payment method.

WebMobileStripe-hosted pageDirect API
#### Caution

Stripe automatically presents your customers payment method options by
evaluating their currency, payment method restrictions, and other parameters. We
recommend that you configure your payment methods from the Stripe Dashboard
using the instructions in [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted).

If you want to continue manually configuring the payment methods you present to
your customers with Checkout, use this guide. Otherwise, [migrate to the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods).

Multibanco is a voucher-based payment method in Portugal. If your business is
based in Europe or the United States, you can accept Multibanco payments from
customers in Portugal using the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents).

To complete a transaction, customers receive a voucher that includes Multibanco
entity and reference numbers. Customers use these voucher details to make a
payment outside your checkout flow through online banking or from an ATM.

Payment confirmation might be delayed by several days due to the initiation of a
bank transfer when a customer pays for a Multibanco voucher. Bank transfers can
encounter delays, particularly over weekends, contributing to the delay in
payment confirmation.

[Determine
compatibility](https://docs.stripe.com/payments/multibanco/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
Multibanco:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency (EUR).
- You can only use one-time line items (recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans are
not supported).
[Accept a
payment](https://docs.stripe.com/payments/multibanco/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Enable Multibanco by making the following updates to your card payment
integration.

### Enable Multibanco as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `multibanco` to the list of `payment_method_types`.
- Make sure all your `line_items` use the `eur` currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'multibanco'],
 line_items: [{
 price_data: {
 currency: 'usd',
 # To accept `multibanco`, all line items must have currency: eur
 currency: 'eur',
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

### Redirect to Stripe-hosted voucher page

#### Note

Unlike card payments, the customer won’t be redirected to the
[success_url](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-success_url)
with a Multibanco payment.

After submitting the Checkout form successfully, the customer is redirected to
the `hosted_voucher_url`. The customer can reference the hosted page’s payment
instructions for details on how to complete their payment. You can view the page
on both desktop and mobile platforms, and it’s also printable.

Stripe sends a
[payment_intent.requires_action](https://docs.stripe.com/api/events/types#event_types-payment_intent.requires_action)
event when a Multibanco voucher is created successfully. If you need to send an
email with the voucher’s payment instructions link, locate the PaymentIntent at
`data.object` on the `requires_action` event, and extract the
`hosted_voucher_url` at
[next_action.multibanco_display_details.hosted_voucher_url](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-multibanco_display_details-hosted_voucher_url)
on the PaymentIntent.

### Fulfill your orders

Because Multibanco is a [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method, you need to use a method such as
[webhooks](https://docs.stripe.com/webhooks) to monitor the payment status and
handle order fulfillment. Learn more about [setting up webhooks and fulfilling
orders](https://docs.stripe.com/checkout/fulfillment).

The following events are sent when the payment status changes:

Event nameDescriptionNext
steps[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)The
customer has successfully submitted the Checkout form. Stripe has generated a
Multibanco voucher.Wait for the customer to pay the Multibanco
voucher.[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)The
customer has successfully paid the Multibanco voucher. The `PaymentIntent`
transitions to `succeeded`.Fulfill the goods or services that the customer
purchased.[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)The
Multibanco voucher has expired, or the payment has failed for some other reason.
The `PaymentIntent` returns to a status of `requires_payment_method`.Contact the
customer by email and request that they place a new order.[OptionalSend
automated payment instruction
emails](https://docs.stripe.com/payments/multibanco/accept-a-payment#instruction-emails)[OptionalCustomize
voucher
appearance](https://docs.stripe.com/payments/multibanco/accept-a-payment#customize-voucher-appearance)[Test
your
integration](https://docs.stripe.com/payments/multibanco/accept-a-payment#test-the-integration)
When testing your Checkout integration, select Multibanco as the payment method,
then click **Pay**. Provide the following email patterns in the Checkout form to
test different scenarios:

EmailDescription
`{any_prefix}@{any_domain}`

Simulates a Multibanco voucher that a customer pays. The
`payment_intent.succeeded` webhook arrives after about 3 minutes.

Example: jenny@example.com

`{any_prefix}succeed_immediately@{any_domain}`

Simulates a Multibanco voucher that a customer pays immediately. The
`payment_intent.succeeded` webhook arrives within several seconds.

Example: succeed_immediately@example.com

`{any_prefix}expire_immediately@{any_domain}`

Simulates a Multibanco voucher that expires immediately. The
`payment_intent.payment_failed` webhook arrives within several seconds.

Example: expire_immediately@example.com

`{any_prefix}expire_with_delay@{any_domain}`

Simulates a Multibanco voucher that expires before a customer pays. The
`payment_intent.payment_failed` webhook arrives after about 3 minutes.

Example: expire_with_delay@example.com

`{any_prefix}fill_never@{any_domain}`

Simulates a Multibanco voucher that never succeeds. The
`payment_intent.payment_failed` webhook arrives after 11 days, which mimics
behavior in live mode. Learn about Multibanco
[expiration](https://docs.stripe.com/payments/multibanco/accept-a-payment#expiration).

Example: fill_never@example.com

## Expiration

Multibanco vouchers expire at the `expires_at` UNIX timestamp in
[next_action.multibanco_display_details.expires_at](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-multibanco_display_details-expires_at),
which is 7 days after you create the voucher. Customers can’t pay a Multibanco
voucher after it expires. After expiration, the PaymentIntent’s status
transitions from `requires_action` to `processing`, and Stripe sends a
[payment_intent.processing](https://docs.stripe.com/api/events/types#event_types-payment_intent.processing)
event.

The PaymentIntent remains in the `processing` status for a maximum buffer period
of 4 days to allow for potential completed payment notification delays caused by
bank-transfer delays. If the Multibanco payment doesn’t complete within the
buffer period, the PaymentIntent’s status transitions to
`requires_payment_method` and Stripe sends a
[payment_intent.payment_failed](https://docs.stripe.com/api/events/types#event_types-payment_intent.payment_failed)
event. If you receive the customer’s funds after the buffer period, Stripe
automatically initiates a refund process for the mispaid amount.

## Cancelation

You can cancel Multibanco vouchers using [Cancel a
PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel). After
cancelation, Stripe sends a
[payment_intent.canceled](https://docs.stripe.com/api/events/types#event_types-payment_intent.canceled)
event.

If a customer’s funds are received for a canceled Multibanco voucher, Stripe
automatically initiates a refund process for the mispaid amount.

#### Note

Canceling a pending payment invalidates the original voucher instructions. When
you cancel a pending Multibanco payment, inform your customer.

When you successfully reconfirm a PaymentIntent in status `requires_action`,
Stripe creates new voucher instructions and a new `hosted_voucher_url`. You must
provide them to your customer.

## Refunds

Learn about Multibanco
[refunds](https://docs.stripe.com/payments/multibanco#refunds).

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [migrate to the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Prices](https://docs.stripe.com/api/prices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
-
[success_url](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-success_url)
-
[payment_intent.requires_action](https://docs.stripe.com/api/events/types#event_types-payment_intent.requires_action)
-
[next_action.multibanco_display_details.hosted_voucher_url](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-multibanco_display_details-hosted_voucher_url)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
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
[expiration](https://docs.stripe.com/payments/multibanco/accept-a-payment#expiration)
-
[next_action.multibanco_display_details.expires_at](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-multibanco_display_details-expires_at)
-
[payment_intent.processing](https://docs.stripe.com/api/events/types#event_types-payment_intent.processing)
-
[payment_intent.payment_failed](https://docs.stripe.com/api/events/types#event_types-payment_intent.payment_failed)
- [Cancel a PaymentIntent](https://docs.stripe.com/api/payment_intents/cancel)
-
[payment_intent.canceled](https://docs.stripe.com/api/events/types#event_types-payment_intent.canceled)
- [refunds](https://docs.stripe.com/payments/multibanco#refunds)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)