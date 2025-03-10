# Place an extended hold on an online card payment

## Learn how to use extended authorizations to capture online card payments up to 30 days after authorization.

Stripe-hosted pageEmbedded formAdvanced integration
Extended authorizations have a longer authorization validity period, which
allows you to hold customer funds for longer than standard authorization
validity windows. For most card networks, the default authorization validity
period is 7 days for online payments and 2 days for in-person
[Terminal](https://docs.stripe.com/terminal) payments, whereas extended validity
periods can go up to 30 days depending on the card network. For more information
about authorization validity windows, see [place a hold on a payment
method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method).

## Availability

When you use extended authorizations, there are no regional restrictions.
However, be aware of the following limitations:

- They’re only available with Visa, Mastercard, American Express, and Discover.
- Certain card brands have merchant category restrictions. Refer to the network
availability table below.
- This page describes extended authorizations for online card payments. For
in-person card payments using extended authorizations, refer to the [Terminal
documentation](https://docs.stripe.com/terminal/features/extended-authorizations).
-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
is set to `payment` and
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
is set to `manual` on the
[CheckoutSession](https://docs.stripe.com/api/checkout/sessions/).

#### IC+ Feature

We offer extended authorizations to users on
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
pricing. If you’re on blended Stripe pricing and want access to this feature,
contact us at [support.stripe.com](https://support.stripe.com/).

### Availability by card network and merchant category

Every card network has different rules that determine which payments have
extended authorizations available, and how long they’re valid. The following
table shows the validity windows and transaction types that extended
authorization is available for using Visa, Mastercard, American Express, and
Discover. However, we recommend that you rely on the [capture_before
field](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-capture_before)
to confirm the validity window for any given payment because these rules can
change without prior notice.

Card brand Merchant category Extended authorization validity window 
**Visa**

Hotel, lodging, vehicle rental, and cruise line

All other merchant categories*

30 days**

Mastercard (not including Maestro and Cirrus cards)All merchant categories30
daysAmerican ExpressLodging and vehicle rental30 days***DiscoverAirline, bus
charter/tour, car rental, cruise line, local/suburban commuter, passenger
transportation including ferries, hotel, lodging, and passenger railway30 days
* For other merchant categories, Stripe charges an additional 0.08% fee per
transaction, and the extended window doesn’t apply to transactions with
merchants in US or JP. ** The exact extended authorization window for Visa is 29
days and 18 hours, to allow time for clearing processes.*** Although your
validity window is extended to 30 days, you must capture the authorized funds no
later than the end of your customer’s stay or rental.

### Networks with limited support (beta)

### Recent changes to availability

## Best Practices

Customers see their funds held longer when you use extended authorizations. Use
clear [statement
descriptors](https://docs.stripe.com/get-started/account/statement-descriptors)
to avoid increased disputes from unrecognized payments.

You can use the
[custom_text](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_text)
field when creating a new
[CheckoutSession](https://docs.stripe.com/api/checkout_sessions) to display
additional text on the checkout page to help meet compliance requirements.

#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when using extended authorization. Consult the network
specifications for the card networks that you plan to accept using this feature
with to make sure your sales are compliant with the applicable rules, which vary
by network. For instance, for many networks extended validity windows are only
for cases where you don’t know the final amount that you’ll capture at the time
of authorization.

The information provided on this page relating to your compliance with these
requirements is for your general guidance, and is not legal, tax, accounting, or
other professional advice. Consult with a professional if you’re unsure about
your obligations.

[Create a
CheckoutSession](https://docs.stripe.com/payments/extended-authorization#create-and-confirm)
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
</html>
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

To enable the extended authorization feature, set
[request_extended_authorization](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card-request_extended_authorization)
to `if_available`.

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
 request_extended_authorization: 'if_available',
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

Rely on the [capture_before
field](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-capture_before)
to confirm the validity window for a given payment. The validity window won’t
change after the CheckoutSession is complete. To determine if the authorization
is extended after the CheckoutSession is complete, look at the
[extended_authorization.status
field](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-extended_authorization-status)
on the associated charge.

```
{
 "id": "pi_xxx",
 "object": "payment_intent",
 "amount": 1000,
 "amount_capturable": 1000,
 "amount_received": 0,
 "status": "requires_capture",
 ...
 // if latest_charge is expanded
 "latest_charge": {
 "id": "ch_xxx",
 "object": "charge",
 "payment_method_details": {
 "card": {
 "amount_authorized": 1000,
 "capture_before": 1696524701,
 "extended_authorization": {
 "status": "enabled", // or "disabled"
 }
 }
 }
 ...
 }
 ...
}
```

[Test your
integration](https://docs.stripe.com/payments/extended-authorization#test-your-integration)
Use any of the below Stripe test cards with any CVC and future expiration date
to request extended authorizations while in test mode. If extended
authorizations are available on payments for a given network in test mode,
they’re also available in live mode.

Card brandNumberPayment
methodVisa4242424242424242`pm_card_visa`Mastercard5555555555554444`pm_card_mastercard`Amex378282246310005`pm_card_amex`Discover6011111111111117`pm_card_discover`
## See also

- [Place a hold on a payment
method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)

## Links

- [Terminal](https://docs.stripe.com/terminal)
- [place a hold on a payment
method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [Terminal
documentation](https://docs.stripe.com/terminal/features/extended-authorizations)
-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
-
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
- [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/)
-
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
- [support.stripe.com](https://support.stripe.com/)
- [capture_before
field](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-capture_before)
- [statement
descriptors](https://docs.stripe.com/get-started/account/statement-descriptors)
-
[custom_text](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_text)
- [CheckoutSession](https://docs.stripe.com/api/checkout_sessions)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create)
- [Line
items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
-
[request_extended_authorization](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card-request_extended_authorization)
- [https://youtu.be/8aA9Enb8NVc.](https://youtu.be/8aA9Enb8NVc)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [extended_authorization.status
field](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-extended_authorization-status)