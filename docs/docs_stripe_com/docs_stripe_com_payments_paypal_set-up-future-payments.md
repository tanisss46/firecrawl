# Set up future PayPal payments

## Learn how to save PayPal details and charge your customers later.

## Enable recurring payments support from the Stripe Dashboard

You can request access to the recurring payments directly from the Stripe
Dashboard. To do that, go to the [Payment Methods
Settings](https://dashboard.stripe.com/settings/payment_methods) page, find
PayPal and click **Enable** next to the Recurring Payments section. You’ll see
the **pending** status. It usually takes up to 5 business days to get access to
the recurring payments for PayPal. When access is granted, you’ll see recurring
payments on your [PayPal
settings](https://dashboard.stripe.com/settings/payment_methods) page. For test
mode, recurring payments are enabled by default.

WebMobileStripe-hosted pageDirect API
Use [Stripe Checkout](https://docs.stripe.com/payments/checkout) to collect
PayPal payment details in advance, and determine the final amount or payment
date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a
subscription](https://docs.stripe.com/billing/subscriptions/trials)
[Set up
StripeServer-side](https://docs.stripe.com/payments/paypal/set-up-future-payments#set-up-stripe)
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

[Create or retrieve a Customer before
setupServer-side](https://docs.stripe.com/payments/paypal/set-up-future-payments#create-customer)
To reuse a PayPal payment method for future payments, it must be attached to a
[Customer](https://docs.stripe.com/api/customers).

You should create a Customer object when your customer creates an account on
your business. Associating the ID of the Customer object with your own internal
representation of a customer will enable you to retrieve and use the stored
payment method details later. If your customer hasn’t created an account, you
can still create a Customer object now and associate it with your internal
representation of the customer’s account later.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Create a Checkout
SessionClient-sideServer-side](https://docs.stripe.com/payments/paypal/set-up-future-payments#create-checkout-session)
Before you can accept PayPal payments, your customer must authorize you to use
their PayPal account for future payments through Stripe Checkout.

Add a checkout button to your website that calls a server-side endpoint to
create a [Checkout Session](https://docs.stripe.com/api/checkout/sessions).

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

Create a Checkout Session in `setup` mode to collect the required information.
After creating the Checkout Session, redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="paypal" \
 -d mode=setup \
 -d customer={{CUSTOMER_ID}} \
-d success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
 -d cancel_url="https://example.com/cancel"
```

When your customer provides their payment method details, they’re redirected to
the `success_url`, a page on your website that informs them that their payment
method was saved successfully. Make the Session ID available on your success
page by including the `{CHECKOUT_SESSION_ID}` template variable in the
`success_url` as in the above example.

When your customer clicks on your logo in a Checkout Session without providing
their payment method details, Checkout redirects them back to your website by
navigating to the `cancel_url`. This is usually the page on your website that
the customer viewed prior to redirecting to Stripe Checkout.

#### Caution

Don’t rely on the redirect to the `success_url` alone for detecting payment
initiation, as:

- Malicious users could directly access the `success_url` without paying and
gain access to your goods or services.
- Customers may not always reach the `success_url` after a successful
payment—they might close their browser tab before the redirect occurs.
[Retrieve the payment
methodServer-side](https://docs.stripe.com/payments/paypal/set-up-future-payments#retrieve-payment-method)
After a customer submits their payment details, retrieve the
[PaymentMethod](https://docs.stripe.com/payments/payment-methods) object. A
[PaymentMethod](https://docs.stripe.com/api/payment_methods) stores the
customer’s PayPal account information for future payments. You can retrieve the
PaymentMethod synchronously using the `success_url` or asynchronously using
[webhooks](https://docs.stripe.com/webhooks).

The decision to retrieve the PaymentMethod synchronously or asynchronously
depends on your tolerance for dropoff, as customers might not always reach the
`success_url` after a successful payment (for example, it’s possible for them to
close their browser tab before the redirect occurs). Using webhooks prevents
your integration from experiencing this form of dropoff.

WebhooksSuccess URL
Handle `checkout.session.completed` webhooks, which contain a Session object. To
learn more, see [setting up webhooks](https://docs.stripe.com/webhooks). The
following example is a `checkout.session.completed` response.

```
{
 "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",
 "object": "event",
 "api_version": "2019-03-14",
 "created": 1561420781,
 "data": {
 "object": {
 "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",
 "object": "checkout.session",
 "billing_address_collection": null,
 "cancel_url": "https://example.com/cancel",
 "client_reference_id": null,
 "customer": null,
 "customer_email": null,
 "display_items": [],
 "mode": "setup",
 "setup_intent": "seti_1EzVO3HssDVaQm2PJjXHmLlM",
 "submit_type": null,
 "subscription": null,
 "success_url": "https://example.com/success"
 }
 },
 "livemode": false,
 "pending_webhooks": 1,
 "request": {
 "id": null,
 "idempotency_key": null
 },
 "type": "checkout.session.completed"
}
```

Note the value of the `setup_intent` key, which is the ID for the SetupIntent
created with the Checkout Session. A
[SetupIntent](https://docs.stripe.com/payments/setup-intents) is an object used
to set up the customer’s PayPal account information for future payments.
[Retrieve](https://docs.stripe.com/api/setup_intents/retrieve) the SetupIntent
object with the ID.

```
curl https://api.stripe.com/v1/setup_intents/seti_1EzVO3HssDVaQm2PJjXHmLlM \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Handle post-setup
eventsServer-side](https://docs.stripe.com/payments/paypal/set-up-future-payments#handle-post-setup-events)
Use a method such as
[webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status#webhooks)
to confirm the billing agreement was authorized successfully by your customer,
instead of relying on your customer to return to the payment status page. When a
customer successfully authorizes the billing agreement, the SetupIntent emits
the
[setup_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-setup_intent.succeeded)
[webhook](https://docs.stripe.com/webhooks) event. If a customer doesn’t
successfully authorize the billing agreement, the SetupIntent will emit the
[setup_intent.setup_failed](https://docs.stripe.com/api/events/types#event_types-setup_intent.setup_failed)
webhook event and returns to a status of `requires_payment_method`. When a
customer revokes the billing agreement from their PayPal account, the
[mandate.updated](https://docs.stripe.com/api/events/types#event_types-mandate.updated)
is emitted.

[Test the
integration](https://docs.stripe.com/payments/paypal/set-up-future-payments#testing)
Test your PayPal integration with your [test API
keys](https://docs.stripe.com/keys#test-live-modes) by viewing the redirect
page. You can test the successful payment case by authenticating the payment on
the redirect page. The PaymentIntent will transition from `requires_action` to
`succeeded`.

To test the case where the user fails to authenticate, use your test API keys
and view the redirect page. On the redirect page, click **Fail test payment**.
The PaymentIntent will transition from `requires_action` to
`requires_payment_method`.

[Use the payment method for future
paymentsServer-side](https://docs.stripe.com/payments/paypal/set-up-future-payments#charge-later)
When you’re ready to charge your customer off-session, use the
[Customer](https://docs.stripe.com/api/customers) and
[PaymentMethod](https://docs.stripe.com/api/payment_methods) IDs to create a
[PaymentIntent](https://docs.stripe.com/api/payment_intents).

To find a `paypal` instrument to charge,
[list](https://docs.stripe.com/api/payment_methods/list) the PaymentMethods
associated with your Customer.

```
curl -G https://api.stripe.com/v1/payment_methods \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d type=paypal
```

When you have the Customer and PaymentMethod IDs, create a PaymentIntent with
the amount and currency of the payment. Set a few other parameters to make the
off-session payment:

- Set
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
to `true` to indicate that the customer is not in your checkout flow during this
payment attempt. This causes the PaymentIntent to throw an error if
authentication is required.
- Set the value of the PaymentIntent’s
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
property to `true`, which causes confirmation to occur immediately when the
PaymentIntent is created.
- Set
[payment_method](https://docs.stripe.com/api#create_payment_intent-payment_method)
to the ID of the PaymentMethod and
[customer](https://docs.stripe.com/api#create_payment_intent-customer) to the ID
of the Customer.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=eur \
 -d customer={{CUSTOMER_ID}} \
 -d "payment_method_types[]"=paypal \
 -d payment_method={{PAYMENT_METHOD_ID}} \
 -d off_session=true \
 -d confirm=true
```

[User-initiated payment method
cancellationServer-side](https://docs.stripe.com/payments/paypal/set-up-future-payments#web-user-initiated-payment-method-cancellation)
A customer can cancel the subscription (Billing Agreement) through their PayPal
account. When they do so, Stripe emits a
[mandate.updated](https://docs.stripe.com/api/events/types#event_types-mandate.updated)
webhook. All subsequent Payment Intents using the saved Payment Method will fail
until you change to a Payment Method with active mandates. When payments fail
for Subscriptions, the status changes to the Subscription status configured in
your [automatic collection
settings](https://docs.stripe.com/invoicing/automatic-collection). Notify the
customer of failure and [charge them with a different payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method).

[OptionalRemove a saved PayPal
accountServer-side](https://docs.stripe.com/payments/paypal/set-up-future-payments#payment-method-detatch)

## Links

- [Payment Methods
Settings](https://dashboard.stripe.com/settings/payment_methods)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Start a free trial for a
subscription](https://docs.stripe.com/billing/subscriptions/trials)
- [Register now](https://dashboard.stripe.com/register)
- [Customer](https://docs.stripe.com/api/customers)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
-
[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})
- [https://example.com/cancel](https://example.com/cancel)
- [PaymentMethod](https://docs.stripe.com/payments/payment-methods)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [webhooks](https://docs.stripe.com/webhooks)
- [https://example.com/success](https://example.com/success)
- [SetupIntent](https://docs.stripe.com/payments/setup-intents)
- [Retrieve](https://docs.stripe.com/api/setup_intents/retrieve)
-
[webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status#webhooks)
-
[setup_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-setup_intent.succeeded)
-
[setup_intent.setup_failed](https://docs.stripe.com/api/events/types#event_types-setup_intent.setup_failed)
-
[mandate.updated](https://docs.stripe.com/api/events/types#event_types-mandate.updated)
- [test API keys](https://docs.stripe.com/keys#test-live-modes)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [list](https://docs.stripe.com/api/payment_methods/list)
-
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
-
[confirm](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm)
-
[payment_method](https://docs.stripe.com/api#create_payment_intent-payment_method)
- [customer](https://docs.stripe.com/api#create_payment_intent-customer)
- [automatic collection
settings](https://docs.stripe.com/invoicing/automatic-collection)
- [charge them with a different payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method)