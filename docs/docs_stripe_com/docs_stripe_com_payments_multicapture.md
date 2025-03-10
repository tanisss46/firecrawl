# Capture a payment multiple times

## Capture a PaymentIntent multiple times, up to the authorized amount.

Stripe-hosted pageEmbedded formAdvanced integration
Multicapture allows you to [capture a
PaymentIntent](https://docs.stripe.com/api/payment_intents/capture) created
during the confirmation step of a
[CheckoutSession](https://docs.stripe.com/api/checkout_sessions) multiple times
for a single transaction, up to the full [amount of the
PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-amount).
You can use it when you have orders with multiple shipments, and want to capture
funds as you fulfill parts of the order.

#### IC+ feature

Multicapture is part of the functionality we offer to users on [IC+
pricing](https://support.stripe.com/questions/understanding-blended-interchange-pricing).
If you’re on blended Stripe pricing and want access to this feature, contact
[Stripe Support](https://support.stripe.com/).

## Availability

When using multicapture, be aware of the following restrictions:

- It only supports online card payments
- It’s only available with Amex, Visa, Discover, Mastercard, and Cartes
Bancaires
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) fund
flows using
[source_transaction](https://docs.stripe.com/api/transfers/create#create_transfer-source_transaction)
aren’t supported
- Stripe allows you to capture up to 50 times for a single
[PaymentIntent](https://docs.stripe.com/api/payment_intents)
-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
is set to `payment` and
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
is set to `manual` on the
[CheckoutSession](https://docs.stripe.com/api/checkout/sessions/)

## Best practices

When sending separate shipments for one order, proactively notify your end
customer with the details of each shipment. Doing so avoids inquiries and
chargebacks from customers because of confusion with seeing multiple
transactions on their bank statement. Use the following best practices when
notifying customers:

- Inform them of the estimated delivery date and transaction amount for each
shipment at the time of checkout, before purchase.
- Notify them upon each shipment, along with the transaction amount.
- Disclose your full refund and cancellation policy.

You can use the
[custom_text](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_text)
field when creating a new
[CheckoutSession](https://docs.stripe.com/api/checkout_sessions) to display
additional text on the checkout page to help meet compliance requirements.

#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when using multicapture. Consult the rules for the card
networks that you want to use this feature with to make sure your sales comply
with all applicable rules, which vary by network. For example, most card
networks restrict multicapture usage to card-not-present transactions for the
sale of goods that ship separately. Certain card networks permit multicapture
for businesses based on their industry (for example, travel), while some don’t
permit multicapture for installment or deposit workflows.

The information provided on this page relating to your compliance with these
requirements is for your general guidance, and isn’t legal, tax, accounting, or
other professional advice. Consult with a professional if you’re unsure about
your obligations.

[Create a Checkout
Session](https://docs.stripe.com/payments/multicapture#create-and-confirm)
Add a checkout button to your website that calls a server-side endpoint to
create a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create).

```
<html>
 <head>
 <title>Buy cool new product</title>
 </head>
 <body>
<!-- Use action="/create-checkout-session.php" if your server is PHP based. -->
 <form action="/create-checkout-session" method="POST">
 <button type="submit">Checkout</button>
 </form>
 </body>
</html>r
```

A Checkout Session is the programmatic representation of what your customer sees
when they’re redirected to the payment form. You can configure it with options
such as:

- [Line
items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
to charge
- Currencies to use

You must populate `success_url` with the URL value of a page on your website
that Checkout returns your customer to after they complete the payment. You can
optionally also provide a `cancel_url` value of a page on your website that
Checkout returns your customer to if they terminate the payment process before
completion.

#### Note

Checkout Sessions expire 24 hours after creation by default.

After creating a Checkout Session, redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

Lastly, set
[request_multicapture](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card-request_multicapture)
as `if_available` to enable the multicapture feature.

```
# This example sets up an endpoint using the Sinatra framework.
# Watch this video to get started: https://youtu.be/8aA9Enb8NVc.

require 'json'
require 'sinatra'
require 'stripe'

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

post '/create-checkout-session' do
 session = Stripe::Checkout::Session.create({
 line_items: [{
 price_data: {
 currency: 'usd',
 product_data: {
 name: 'T-shirt',
 },
 unit_amount: 2000,
 },
 quantity: 1,
 }],
 payment_method_options: {
 card: {
 request_multicapture: 'if_available',
 },
 },
 mode: 'payment',
 # These placeholder URLs will be replaced in a following step.
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
 })

 redirect session.url, 303
end
```

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn
individual payment methods on or off in the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout,
Stripe evaluates the currency and any restrictions, then dynamically presents
the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or
set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). By default,
Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe
filters them out even when they’re enabled. We filter Google Pay if you [enable
automatic tax](https://docs.stripe.com/tax/checkout) without collecting a
shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple
Pay or Google Pay. Stripe handles these payments the same way as other card
payments.

[Capture the
PaymentIntent](https://docs.stripe.com/payments/multicapture#capture-payment-intent)
For a PaymentIntent in a [requires_capture
state](https://docs.stripe.com/payments/paymentintents/lifecycle) where
multicapture is `available`, specifying the optional `final_capture` parameter
to be `false` tells Stripe not to release the remaining uncaptured funds when
calling the capture API. For example, if you confirm a 10 USD payment intent,
capturing 7 USD with `final_capture=false` keeps the remaining 3 USD authorized.

```
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount_to_capture=700 \
 -d final_capture=false \
 -d "expand[]"=latest_charge
```

In the PI capture response, the
[amount_capturable](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_capturable)
and
[amount_received](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_received)
fields update accordingly.

```
// PaymentIntent Response
{
 "id": "pi_ANipwO3zNfjeWODtRPIg",
 "object": "payment_intent",
 "amount": 1000,
 "amount_capturable": 300, // 1000 - 700 = 300
 "amount_received": 700,
 // if latest_charge is expanded
 "latest_charge": {
 "id": "ch_xxx",
 "object": "charge",
 "amount": 1000,
 "amount_captured": 700,
 "amount_refunded": 0,
 ...
 }
 ...
}
```

[Final capture](https://docs.stripe.com/payments/multicapture#final-capture)
The PaymentIntent remains in a `requires_capture` state until you do one of the
following:

- Set `final_capture` to `true`.
- Make a capture without the `final_capture` parameter (because `final_capture`
defaults to `true`).
- The authorization window expires.

At this point, Stripe releases any remaining funds and transitions the
PaymentIntent to a `succeeded` state.

```
curl https://api.stripe.com/v1/payment_intents/pi_xxx/capture \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount_to_capture=200 \
 -d final_capture=true \
 -d "expand[]"=latest_charge
```

In the PI capture response, the
[amount_capturable](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_capturable)
and
[amount_received](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_received)
fields will be updated accordingly.

```
// PaymentIntent Response
{
 "id": "pi_ANipwO3zNfjeWODtRPIg",
 "object": "payment_intent",
 "amount": 1000,
 "amount_capturable": 0, // not 100 due to final_capture=true
 "amount_received": 900, // 700 + 200 = 900
 // if latest_charge is expanded
 "latest_charge": {
 "id": "ch_xxx",
 "object": "charge",
 "amount": 1000,
 "amount_captured": 900,
 "amount_refunded": 0,
 ...
 }
 ...
}
```

Uncaptured PaymentIntents transition to `canceled`, while partially captured
PaymentIntents transition to `succeeded`.

[OptionalRelease uncaptured
funds](https://docs.stripe.com/payments/multicapture#close-payment)
## Test your integration

Use a Stripe test card with any CVC, postal code, and future expiration date to
test multicapture payments.

NumberPayment MethodDescription4242424242424242`pm_card_visa`This test card
supports multicapture.4000002500001001`pm_card_visa_cartesBancaires`Cartes
Bancaires or Visa test card that supports multicapture.
## Refunds

For a PaymentIntent in `requires_capture` state, you can
[refund](https://docs.stripe.com/api/refunds) any number of times up to the
total captured amount minus the total refunded amount, which is the
[amount_received](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_received)—[amount_refunded](https://docs.stripe.com/api/charges/object#charge_object-amount_refunded).
The
[charge.refunded](https://docs.stripe.com/api/charges/object#charge_object-refunded)
field transitions to `true` only when the final capture has been performed and
the entire
[amount_received](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_received)
is refunded.

Stripe doesn’t support partial refunds with
[refund_application_fee=true](https://docs.stripe.com/api/refunds/create#create_refund-refund_application_fee)
or
[reverse_transfer=true](https://docs.stripe.com/api/refunds/create#create_refund-reverse_transfer).
Instead, you can perform partial fee refunds by manually performing partial fee
refunds and transfer reversals using the [application fee
refund](https://docs.stripe.com/api/fee_refunds) and [transfer
reversal](https://docs.stripe.com/api/transfer_reversals) endpoints. After using
the application fee refund or transfer reversal endpoints, Stripe doesn’t
support any further refunds with `refund_application_fee=true` or
`reverse_transfer=true` respectively.

## Connect

Multicapture supports all Connect use cases, with the exception of [Separate
Charges and
Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) with
the
[source_transaction](https://docs.stripe.com/api/transfers/create#create_transfer-source_transaction)
parameter. The
[application_fee_amount](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-application_fee_amount)
and
[transfer_data[amount]](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-transfer_data-amount)
parameters have some additional validations. Consider the following validations
when implementing multicapture with Connect:

- Setting `application_fee_amount` or `transfer_data[amount]` on the first
capture makes it required for all subsequent captures. Each
`application_fee_amount` and `transfer_data[amount]` passed at capture time
overrides the values passed in on PaymentIntent creation, confirmation, and
update.
- Stripe doesn’t support partial refunds on multicapture payments with
refund_application_fee=true or reverse_transfer=true. You can perform partial
fee refunds or transfer reversals using the [application fee
refund](https://docs.stripe.com/api/fee_refunds) and [transfer
reversal](https://docs.stripe.com/api/transfer_reversals) endpoints.

## Webhooks

### Charge updated webhooks

We send a
[charge.updated](https://docs.stripe.com/api/events/types#event_types-charge.updated)
webhook each time you capture a payment.

For example, on the first capture of a destination charge multicapture payment
with an `application_fee_amount`, we update these fields from empty to non-empty
values.

```
// charge.updated
{
 "data": {
 "id": "ch_xxx",
 "object": "charge",
 "amount": 1000,
 "balance_transaction": "txn_xxx", // applicable to all charges
 "transfer": "tr_xxx", // applicable to destination charges only
 "application_fee": "fee_xxx", // applicable to Connect only
 ...
 },
 "previous_attributes": {
 "balance_transaction": null, // applicable to all charges
 "transfer": null, // applicable to destination charges only
 "application_fee": null, // applicable to Connect only
 }
}
```

### payment_intent.amount_capturable_updated

We send
[payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types#event_types-payment_intent.amount_capturable_updated)
on every capture, regardless of `amount_to_capture` and `final_capture` values.

For example, if we capture 1 USD from a PaymentIntent with an amount of 10 USD,
the PaymentIntent’s amount_capturable field updates to 9 USD.

```
// payment_intent.amount_capturable_updated
{
 "data": {
 "id": "pi_xxx",
 "object": "payment_intent",
 "amount": 1000,
 "amount_capturable": 900 // 1000 - 100 = 900
 ...
 },
 "previous_attributes": {
 "amount_capturable": 1000
 }
}
```

### Charge captured events

We send a
[charge.captured](https://docs.stripe.com/api/events/types#event_types-charge.captured)
event for final captures or at the end of the authorization window to reverse
the authorization of the uncaptured amount. The
[captured](https://docs.stripe.com/api/charges/object#charge_object-captured)
field for a charge only becomes `true` after a final capture or authorization
reversal.

For example, if we do a capture with `amount=0` and `final_capture=true`, the
[captured](https://docs.stripe.com/api/charges/object#charge_object-captured)
attribute on the charge changes from false to true.

```
// charge.captured
{
 "data": {
 "id": "ch_xxx",
 "object": "charge",
 "captured": true
 ...
 },
 "previous_attributes": {
 "captured": false
 }
}
```

### Refund webhooks

Multicapture refund webhooks are no different than non-multicapture refund
webhooks.

During each partial refund, we send a
[refund.created](https://docs.stripe.com/api/events/types#event_types-refund.created)
event. For connected accounts, we also send
[application_fee.refunded](https://docs.stripe.com/api/events/types#event_types-application_fee.refunded)
events when we refund application fees and
[transfer.reversed](https://docs.stripe.com/api/events/types#event_types-transfer.reversed)
events when we reverse transfers.

## Links

- [capture a PaymentIntent](https://docs.stripe.com/api/payment_intents/capture)
- [CheckoutSession](https://docs.stripe.com/api/checkout_sessions)
- [amount of the
PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-amount)
- [IC+
pricing](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
- [Stripe Support](https://support.stripe.com/)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
-
[source_transaction](https://docs.stripe.com/api/transfers/create#create_transfer-source_transaction)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
-
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
- [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/)
-
[custom_text](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_text)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create)
- [Line
items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
-
[request_multicapture](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card-request_multicapture)
- [https://youtu.be/8aA9Enb8NVc.](https://youtu.be/8aA9Enb8NVc)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [enable automatic tax](https://docs.stripe.com/tax/checkout)
- [requires_capture
state](https://docs.stripe.com/payments/paymentintents/lifecycle)
-
[amount_capturable](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_capturable)
-
[amount_received](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_received)
- [refund](https://docs.stripe.com/api/refunds)
-
[amount_refunded](https://docs.stripe.com/api/charges/object#charge_object-amount_refunded)
-
[charge.refunded](https://docs.stripe.com/api/charges/object#charge_object-refunded)
-
[refund_application_fee=true](https://docs.stripe.com/api/refunds/create#create_refund-refund_application_fee)
-
[reverse_transfer=true](https://docs.stripe.com/api/refunds/create#create_refund-reverse_transfer)
- [application fee refund](https://docs.stripe.com/api/fee_refunds)
- [transfer reversal](https://docs.stripe.com/api/transfer_reversals)
-
[application_fee_amount](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-application_fee_amount)
-
[transfer_data[amount]](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-transfer_data-amount)
-
[charge.updated](https://docs.stripe.com/api/events/types#event_types-charge.updated)
-
[payment_intent.amount_capturable_updated](https://docs.stripe.com/api/events/types#event_types-payment_intent.amount_capturable_updated)
-
[charge.captured](https://docs.stripe.com/api/events/types#event_types-charge.captured)
- [captured](https://docs.stripe.com/api/charges/object#charge_object-captured)
-
[refund.created](https://docs.stripe.com/api/events/types#event_types-refund.created)
-
[application_fee.refunded](https://docs.stripe.com/api/events/types#event_types-application_fee.refunded)
-
[transfer.reversed](https://docs.stripe.com/api/events/types#event_types-transfer.reversed)