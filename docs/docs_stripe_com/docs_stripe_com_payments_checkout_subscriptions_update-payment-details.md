# Update payment details

## Learn how to update the payment method used for future invoices.

Use the following steps to create a Checkout page that collects your customer’s
payment details and returns a Payment Method. Then use the Stripe REST APIs to
update the payment method used for future
[invoices](https://docs.stripe.com/api/invoices).

#### Note

This guide uses Checkout to update subscription payment methods. You can instead
implement the [Billing customer
portal](https://docs.stripe.com/customer-management) to provide a Stripe-hosted
dashboard for your customers to manage their subscriptions and billing details.

[Set up
StripeServer-side](https://docs.stripe.com/payments/checkout/subscriptions/update-payment-details#web-setup)
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

[Create a Checkout
SessionServer-side](https://docs.stripe.com/payments/checkout/subscriptions/update-payment-details#create-checkout-session)
To create a setup mode Session, use the `mode` parameter with a value of `setup`
when creating the Session. See the [Checkout Session API
reference](https://docs.stripe.com/api/checkout/sessions/create) for a complete
list of parameters that you can use for Session creation.

Append the `{CHECKOUT_SESSION_ID}` template variable to the `success_url` to get
access to the Session ID after your customer successfully completes a Checkout
Session.

Finally, use the
[setup_intent_data.metadata](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-setup_intent_data-metadata)
dictionary to pass your customer’s existing Stripe `subscription_id` to the
Checkout Session. Note that there other ways to pass this data to your server,
but we’ll use metadata for this guide.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="card" \
 -d "mode"="setup" \
 -d "customer"="cus_FOsk5sbh3ZQpAU" \
 -d "setup_intent_data[metadata][subscription_id]"="sub_8epEF0PuRhmltU" \
-d "success_url"="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"
\
 -d "cancel_url"="https://example.com/cancel"
```

[Redirect to
CheckoutClient-side](https://docs.stripe.com/payments/checkout/subscriptions/update-payment-details#redirect-checkout)
Checkout relies on [Stripe.js](https://docs.stripe.com/payments/elements),
Stripe’s foundational JavaScript library for building payment flows.

HTML + JSReact
To get started, include the following script tag on your website—always load it
directly from **https://js.stripe.com**. You can’t include it in a bundle or
host it yourself. See [Stripe samples](https://github.com/stripe-samples) for
examples.

```
npm install @stripe/stripe-js
```

Next, create an instance of the [Stripe
object](https://docs.stripe.com/js#stripe-function) by providing your
publishable [API key](https://docs.stripe.com/keys) as the first parameter:

```
import {loadStripe} from '@stripe/stripe-js';

const stripe = await loadStripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
```

To use Checkout on your website, you must add a snippet of code that includes
the Session `id` from the [previous
step](https://docs.stripe.com/payments/checkout/subscriptions/update-payment-details#create-checkout-session).
When your customer is ready to save or update their payment method, call
[redirectToCheckout](https://docs.stripe.com/js#stripe-redirect-to-checkout) and
provide the Session `id` as a parameter.

```
const checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', () => {
 stripe.redirectToCheckout({
 // Make the id field from the Checkout Session creation API response
 // available to this file, so you can provide it as argument here
 // instead of the {{CHECKOUT_SESSION_ID}} placeholder.
 sessionId: '{{CHECKOUT_SESSION_ID}}'
 })
 // If `redirectToCheckout` fails due to a browser or network
 // error, display the localized error message to your customer
 // using `error.message`.
});
```

This code is typically invoked from an event handler that triggers in response
to an action taken by your customer, such as clicking on a payment button.

[Retrieve the Checkout
SessionServer-side](https://docs.stripe.com/payments/checkout/subscriptions/update-payment-details#retrieve-checkout-session)
After a customer successfully completes their Checkout Session, you need to
retrieve the Session object. There are two ways to do this:

- **Asynchronously**: Handle `checkout.session.completed`
[webhooks](https://docs.stripe.com/webhooks), which contain a Session object.
Learn more about [setting up webhooks](https://docs.stripe.com/webhooks).
- **Synchronously**: Obtain the Session ID from the `success_url` when a user
redirects back to your site. Use the Session ID to
[retrieve](https://docs.stripe.com/api/checkout/sessions/retrieve) the Session
object.

```
curl
https://api.stripe.com/v1/checkout/sessions/cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

The right choice depends on your tolerance for dropoff, as customers may not
always reach the `success_url` after a successful payment. It’s possible for
them close their browser tab before the redirect occurs. Handling webhooks
prevents your integration from being susceptible to this form of dropoff.

After you have retrieved the Session object, get the value of the `setup_intent`
key, which is the ID for the SetupIntent created during the Checkout Session. A
[SetupIntent](https://docs.stripe.com/payments/setup-intents) is an object used
to set up the customer’s bank account information for future payments.

Example `checkout.session.completed` payload:

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
 "client_reference_id": null,
 "customer": "cus_FOsk5sbh3ZQpAU",
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

Note the `setup_intent` ID for the next step.

[Retrieve the
SetupIntentServer-side](https://docs.stripe.com/payments/checkout/subscriptions/update-payment-details#retrieve-setup-intent)
Using the `setup_intent` ID, retrieve the SetupIntent object using the
[/v1/setup_intents/:id](https://docs.stripe.com/api/setup_intents/retrieve)
endpoint.

```
curl https://api.stripe.com/v1/setup_intents/seti_1EzVO3HssDVaQm2PJjXHmLlM \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

Example response:

```
{
 "id": "seti_1EzVO3HssDVaQm2PJjXHmLlM",
 "object": "setup_intent",
 "application": null,
 "cancellation_reason": null,
 "client_secret": null,
 "created": 1561420781,
 "customer": "cus_FOsk5sbh3ZQpAU",
 "description": null,
 "last_setup_error": null,
 "livemode": false,
 "metadata": {
 "subscription_id": "sub_8epEF0PuRhmltU"
 },
 "next_action": null,
 "on_behalf_of": null,
 "payment_method": "pm_1F0c9v2eZvKYlo2CJDeTrB4n",
 "payment_method_types": [
 "card"
 ],
 "status": "succeeded",
 "usage": "off_session"
}
```

Note the `customer` ID, `subscription_id`, and `payment_method` ID for the next
steps.

#### Note

If you’re requesting this information synchronously from the Stripe API (as
opposed to handling webhooks), you can combine the previous step with this step
by [expanding](https://docs.stripe.com/api/expanding_objects) the SetupIntent
object in the request to the /v1/checkout/session endpoint. Doing this prevents
you from having to make two network requests to access the newly created
PaymentMethod ID.

[Set a default payment
methodServer-side](https://docs.stripe.com/payments/checkout/subscriptions/update-payment-details#set-default-payment-method)
There are two ways to ensure that a payment method is used for future invoices:

- Set it as the Customer’s `invoice_settings.default_payment_method`
- Set it as the Subscription’s `default_payment_method`

Setting `invoice_settings.default_payment_method` on the Customer will cause all
future invoices for that customer to be paid with the specified payment method.

Setting `default_payment_method` on the Subscription will cause all future
invoices for that subscription to be paid with the specified payment method,
overriding any `invoice_settings.default_payment_method` set on the associated
Customer.

### Set invoice_settings.default_payment_method on the Customer

Using the customer ID and the PaymentMethod ID you retrieved, set the
`invoice_settings.default_payment_method` for the Customer using the
[/v1/customers/:id](https://docs.stripe.com/api/customers/update) endpoint.

```
curl https://api.stripe.com/v1/customers/cus_FOsk5sbh3ZQpAU \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "invoice_settings[default_payment_method]"=pm_1F0c9v2eZvKYlo2CJDeTrB4n
```

All future invoices for this customer will now charge the new PaymentMethod
created with the setup mode Checkout Session.

### Set default_payment_method on the Subscription

Using the subscription ID and the PaymentMethod ID you retrieved, set the
`default_payment_method` for the subscription using the
[/v1/subscriptions/:id](https://docs.stripe.com/api/subscriptions/update)
endpoint.

```
curl https://api.stripe.com/v1/subscriptions/sub_8epEF0PuRhmltU \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X "POST" \
 -d "default_payment_method"="pm_1F0c9v2eZvKYlo2CJDeTrB4n"
```

All future invoices for this subscription will now charge the new PaymentMethod
created with the setup mode Checkout Session, overriding any
`invoice_settings.default_payment_method` set on the associated Customer.

## See also

Congrats! You can now set a default payment method for future invoices. When
testing your integration with your test API key, you can use a [test card
number](https://docs.stripe.com/testing#cards) to ensure that it works
correctly.

- [Test Cards](https://docs.stripe.com/testing#cards)

## Links

- [invoices](https://docs.stripe.com/api/invoices)
- [Billing customer portal](https://docs.stripe.com/customer-management)
- [Register now](https://dashboard.stripe.com/register)
- [Checkout Session API
reference](https://docs.stripe.com/api/checkout/sessions/create)
-
[setup_intent_data.metadata](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-setup_intent_data-metadata)
-
[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})
- [https://example.com/cancel](https://example.com/cancel)
- [Stripe.js](https://docs.stripe.com/payments/elements)
- [Stripe samples](https://github.com/stripe-samples)
- [Stripe object](https://docs.stripe.com/js#stripe-function)
- [API key](https://docs.stripe.com/keys)
- [redirectToCheckout](https://docs.stripe.com/js#stripe-redirect-to-checkout)
- [webhooks](https://docs.stripe.com/webhooks)
- [retrieve](https://docs.stripe.com/api/checkout/sessions/retrieve)
- [SetupIntent](https://docs.stripe.com/payments/setup-intents)
- [https://example.com/success](https://example.com/success)
- [/v1/setup_intents/:id](https://docs.stripe.com/api/setup_intents/retrieve)
- [expanding](https://docs.stripe.com/api/expanding_objects)
- [/v1/customers/:id](https://docs.stripe.com/api/customers/update)
- [/v1/subscriptions/:id](https://docs.stripe.com/api/subscriptions/update)
- [test card number](https://docs.stripe.com/testing#cards)