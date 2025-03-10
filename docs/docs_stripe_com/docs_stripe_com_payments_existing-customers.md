# Payments for existing customers

## Learn how to charge an existing payment method while a customer is on-session.

Stripe-hosted pageEmbedded formCustom flowDirect API
A Checkout Session allows buyers to enter their payment details. If the buyer is
an existing customer, you can configure the Checkout Session to prefill the
details with one of the customer’s [saved
cards](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=stripe-hosted).

![Checkout with one saved
card](https://b.stripecdn.com/docs-statics-srv/assets/saved-card.59d38df89f7892ff0a3669779ec30f0b.png)

[Create a Checkout
SessionClient-sideServer-side](https://docs.stripe.com/payments/existing-customers#create-checkout-session)
Add a checkout button to your website that calls a server-side endpoint to
create a Checkout Session.

```
<html>
 <head>
 <title>Checkout</title>
 </head>
 <body>
 <form action="/create-checkout-session" method="POST">
 <button type="submit">Checkout</button>
 </form>
 </body>
</html>
```

Checkout supports reusing existing Customer objects with the `customer`
[parameter](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer).
When reusing existing customers, all objects created by Checkout, such as
Payment Intents and Subscriptions, are associated with that Customer object.

Append the `{CHECKOUT_SESSION_ID}` template variable to the `success_url` to get
access to the Session ID after your customer successfully completes a Checkout
Session. After creating the Checkout Session, redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d customer={{CUSTOMER_ID}} \
--data-urlencode
success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"
```

[OptionalDisplay additional saved payment
methodsServer-side](https://docs.stripe.com/payments/existing-customers#display-additional-saved-payment-methods)[Prefill
fields on payment
page](https://docs.stripe.com/payments/existing-customers#prefill-payment-fields)
If all the following conditions are true, Checkout prefills the **email**,
**name**, **card**, and **billing address** fields on the payment page using
details from the customer’s saved card:

- Checkout is in `payment` or `subscription` mode; `setup` mode doesn’t support
prefilling fields.
- The customer has a saved card. Checkout only supports prefilling card payment
methods.
- The saved card has `allow_redisplay` set to `always` or you adjusted the
[default display
setting](https://docs.stripe.com/payments/existing-customers#display-additional-saved-payment-methods).
- The payment method includes
[billing_details](https://docs.stripe.com/api/payment_methods/object#payment_method_object-billing_details)
required by the Checkout Session’s
[billing_address_collection](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-billing_address_collection)
value:- `auto` requires values for `email`, `name`, and `address[country]`. US,
CA, and GB billing addresses also require `address[postal_code]`.
- `required` requires values for `email`, `name`, and all `address` fields.

If your customer has multiple saved cards, Checkout prefills details from the
card matching the following prioritization:

- In `payment` mode, Stripe prefills the fields using the customer’s the newest
saved card.
- In `subscription` mode, Stripe prefills the customer’s default payment method
if it’s a card. Otherwise Stripe prefills the newest saved card.

When Checkout is [collecting a shipping
address](https://docs.stripe.com/payments/collect-addresses), Checkout prefills
shipping address fields if the customer’s
[shipping.address](https://docs.stripe.com/api/customers/object#customer_object-shipping-address)
meets the Checkout Session’s [supported
countries](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_address_collection-allowed_countries).

#### Prefill timeout

The prefilled payment method displays for 30 minutes following Checkout Session
creation. After it expires, loading the same Checkout Session doesn’t prefill
the payment method anymore for security reasons.

[Handle post-payment
eventsServer-side](https://docs.stripe.com/payments/existing-customers#post-payment)
Stripe sends a
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
event when a customer completes a Checkout Session payment. Use the [Dashboard
webhook tool](https://dashboard.stripe.com/webhooks) or follow the [webhook
guide](https://docs.stripe.com/webhooks/quickstart) to receive and handle these
events, which might trigger you to:

- Send an order confirmation email to your customer.
- Log the sale in a database.
- Start a shipping workflow.

Listen for these events rather than waiting for your customer to be redirected
back to your website. Triggering fulfillment only from your Checkout landing
page is unreliable. Setting up your integration to listen for asynchronous
events allows you to accept [different types of payment
methods](https://stripe.com/payments/payment-methods-guide) with a single
integration.

Learn more in our [fulfillment guide for
Checkout](https://docs.stripe.com/checkout/fulfillment).

Handle the following events when collecting payments with the Checkout:

EventDescriptionAction[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)Sent
when a customer successfully completes a Checkout Session.Send the customer an
order confirmation and fulfill their
order.[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)Sent
when a payment made with a delayed payment method, such as ACH direct debt,
succeeds.Send the customer an order confirmation and fulfill their
order.[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)Sent
when a payment made with a delayed payment method, such as ACH direct debt,
fails.Notify the customer of the failure and bring them back on-session to
attempt payment again.

## Links

- [saved
cards](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=stripe-hosted)
-
[parameter](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
-
[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})
-
[billing_details](https://docs.stripe.com/api/payment_methods/object#payment_method_object-billing_details)
-
[billing_address_collection](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-billing_address_collection)
- [collecting a shipping
address](https://docs.stripe.com/payments/collect-addresses)
-
[shipping.address](https://docs.stripe.com/api/customers/object#customer_object-shipping-address)
- [supported
countries](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_address_collection-allowed_countries)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [Dashboard webhook tool](https://dashboard.stripe.com/webhooks)
- [webhook guide](https://docs.stripe.com/webhooks/quickstart)
- [different types of payment
methods](https://stripe.com/payments/payment-methods-guide)
- [fulfillment guide for Checkout](https://docs.stripe.com/checkout/fulfillment)
-
[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)
-
[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)