# Set up a subscription with PayPal

## Learn how to create and charge for a subscription with PayPal.

#### Caution

To start accepting PayPal subscriptions on Stripe, you need to [enable PayPal
recurring
payments](https://docs.stripe.com/payments/paypal/set-up-future-payments?platform=web#enable-recurring-payments-support-from-stripe-dashboard)
from the Dashboard.

Use this guide to set up a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) using
[PayPal](https://docs.stripe.com/payments/paypal) as a payment method.

[Create a product and
priceDashboard](https://docs.stripe.com/billing/subscriptions/paypal#create-product-plan-code)
[Products](https://docs.stripe.com/api/products) represent the item or service
you’re selling. [Prices](https://docs.stripe.com/api/prices) define how much and
how frequently you charge for a product. This includes how much the product
costs, what currency you accept, and whether it’s a one-time or recurring
charge. If you only have a few products and prices, create and manage them in
the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15
EUR monthly subscription. To model this:

- Navigate to the [Add a
product](https://dashboard.stripe.com/test/products/create) page.
- Enter a **Name** for the product.
- Enter **15** for the price.
- Select **EUR** as the currency.
- Click **Save product**.

After you create the product and the price, record the price ID so you can use
it in subsequent steps. The pricing page displays the ID and it looks similar to
this: `price_G0FvDp6vZvdwRZ`.

[Create or retrieve a Customer before
setupServer-side](https://docs.stripe.com/billing/subscriptions/paypal#web-create-a-customer)
To reuse a PayPal payment method for future payments, attach it to a
[Customer](https://docs.stripe.com/api/customers).

Create a Customer object when a customer creates an account on your business.
Associating the ID of the Customer object with your own internal representation
of a customer lets you retrieve and use the stored payment method details later.
If the customer hasn’t created an account, you can still create a Customer
object now and associate it with your internal representation of the customer’s
account later.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Create a
SetupIntentServer-side](https://docs.stripe.com/billing/subscriptions/paypal#web-create-setup-intent)
A [SetupIntent](https://docs.stripe.com/api/setup_intents) is an object that
represents your intent and tracks the steps to set up your customer’s payment
method for future payments.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents) on your server
with
[payment_method_types](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_types)
set to `paypal` and specify the
[Customer](https://docs.stripe.com/api/customers)’s
[id](https://docs.stripe.com/api/customers/object#customer_object-id).

```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "payment_method_types[]"=paypal \
 -d "payment_method_data[type]"=paypal
```

The SetupIntent object contains a
[client_secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret),
a unique key that you need to pass to Stripe on the client side to redirect your
buyer to PayPal and authorize the mandate.

[Redirect your
customerClient-side](https://docs.stripe.com/billing/subscriptions/paypal#web-confirm-setup-intent)
When a customer attempts to set up their PayPal account for future payments, we
recommend you use [Stripe.js](https://docs.stripe.com/js) to confirm the
SetupIntent. Stripe.js is our foundational JavaScript library for building
payment flows. It will automatically handle complexities like the redirect
described below, and enables you to easily extend your integration to other
payment methods in the future.

Include the Stripe.js script on your checkout page by adding it to the head of
your HTML file.

```
<head>
 <title>Checkout</title>
 <script src="https://js.stripe.com/v3/"></script>
</head>
```

Create an instance of Stripe.js with the following JavaScript on your checkout
page.

```
// Set your publishable key. Remember to change this to your live publishable
key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx',
 {}
);
```

To confirm the setup on the client side, pass the client secret of the
SetupIntent object that you created in Step 3.

The client secret is different from your API keys that authenticate Stripe API
requests. It should still be handled carefully because it can complete the
charge. Do not log it, embed it in URLs, or expose it to anyone but the
customer.

### Confirm PayPal Setup

To authorize you to use their PayPal account for future payments, your customer
will be redirected to a PayPal billing agreement page, which they will need to
approve before being redirected back to your website. Use
[stripe.confirmPayPalSetup](https://docs.stripe.com/js/setup_intents/confirm_paypal_setup)
to handle the redirect away from your page and to complete the setup. Add a
`return_url` to this function to indicate where Stripe should redirect the user
to after they approve the billing agreement on PayPal’s website.

```
// Redirects away from the client
const {error} = await stripe.confirmPayPalSetup(
 '{{SETUP_INTENT_CLIENT_SECRET}}',
 {
 return_url: 'https://example.com/setup/complete',
 mandate_data: {
 customer_acceptance: {
 type: 'online',
 online: {
 infer_from_client: true
 }
 }
 },
 }
);

if (error) {
 // Inform the customer that there was an error.
}
```

You can find the Payment Method owner’s email, payer ID, and Billing Agreement
ID on the resulting [Mandate](https://docs.stripe.com/api/mandates/) under the
[payment_method_details](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-paypal)
property. You can also find the buyer’s email and payer ID in the
[paypal](https://docs.stripe.com/api/payment_methods/object#payment_method_object-paypal)
property on the [PaymentMethod](https://docs.stripe.com/api/payment_methods).

FieldValue`verified_email`The email address of the payer on their PayPal
account.`payer_id`A unique ID of the payer’s PayPal
account.`billing_agreement_id`The PayPal Billing Agreement ID (BAID). This is an
ID generated by PayPal which represents the mandate between the business and the
customer.[Monitor
webhooksServer-side](https://docs.stripe.com/billing/subscriptions/paypal#web-monitor-webhooks)
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

[Create the
subscriptionServer-side](https://docs.stripe.com/billing/subscriptions/paypal#create-subscription-code)
Create a [subscription](https://docs.stripe.com/api/subscriptions) with the
price and customer:

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer=cus_Gk0uVzT2M4xOKD \
 -d default_payment_method=pm_1F0c9v2eZvKYlo2CJDeTrB4n \
 -d "items[0][price]"=price_F52b2UdntfQsfR \
 -d "expand[0]"="latest_invoice.payment_intent" \
 -d off_session=true
```

Creating subscriptions automatically charges customers because the [default
payment
method](https://docs.stripe.com/api/customers/create#create_customer-invoice_settings-default_payment_method)
is set. After a successful payment, the status in the [Stripe
Dashboard](https://dashboard.stripe.com/test/subscriptions) changes to
**Active**. The price you created earlier determines subsequent billings.

[Manage subscription
statusClient-side](https://docs.stripe.com/billing/subscriptions/paypal#manage-sub-status)
If the initial payment succeeds, the state of the subscription is `active` and
no further action is needed. When payments fail, the status is changed to the
**Subscription status** configured in your [automatic collection
settings](https://docs.stripe.com/invoicing/automatic-collection). Notify the
customer on failure and [charge them with a different payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method).

[Update a
subscriptionServer-side](https://docs.stripe.com/billing/subscriptions/paypal#update-subscription)
When you update a subscription, you need to specify `off_session=true`.
Otherwise, any new payment requires a user redirection to PayPal for
confirmation. For example, if you want to change the quantity of an item
included in the subscription you can use:

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer=cus_Gk0uVzT2M4xOKD \
 -d default_payment_method=pm_1F0c9v2eZvKYlo2CJDeTrB4n \
 -d "items[0][price]"=price_F52b2UdntfQsfR \
 -d "items[0][quantity]"=2 \
 -d off_session=true
```

[Test the
integration](https://docs.stripe.com/billing/subscriptions/paypal#test-integration)
Test your PayPal integration with your [test API
keys](https://docs.stripe.com/keys#test-live-modes) by viewing the redirect
page. You can test the successful payment case by authenticating the payment on
the redirect page. The PaymentIntent will transition from `requires_action` to
`succeeded`.

To test the case where the user fails to authenticate, use your test API keys
and view the redirect page. On the redirect page, click **Fail test payment**.
The PaymentIntent will transition from `requires_action` to
`requires_payment_method`.

[OptionalSetting the billing
cycle](https://docs.stripe.com/billing/subscriptions/paypal#billing-cycle)[OptionalSubscription
trials](https://docs.stripe.com/billing/subscriptions/paypal#trial-periods)[OptionalRemove
a saved PayPal
account](https://docs.stripe.com/billing/subscriptions/paypal#payment-method-detatch)

## Links

- [enable PayPal recurring
payments](https://docs.stripe.com/payments/paypal/set-up-future-payments?platform=web#enable-recurring-payments-support-from-stripe-dashboard)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [Add a product](https://dashboard.stripe.com/test/products/create)
- [Customer](https://docs.stripe.com/api/customers)
- [SetupIntent](https://docs.stripe.com/api/setup_intents)
-
[payment_method_types](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_types)
- [id](https://docs.stripe.com/api/customers/object#customer_object-id)
-
[client_secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret)
- [Stripe.js](https://docs.stripe.com/js)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[stripe.confirmPayPalSetup](https://docs.stripe.com/js/setup_intents/confirm_paypal_setup)
- [Mandate](https://docs.stripe.com/api/mandates/)
-
[payment_method_details](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-paypal)
-
[paypal](https://docs.stripe.com/api/payment_methods/object#payment_method_object-paypal)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
-
[webhooks](https://docs.stripe.com/payments/payment-intents/verifying-status#webhooks)
-
[setup_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-setup_intent.succeeded)
- [webhook](https://docs.stripe.com/webhooks)
-
[setup_intent.setup_failed](https://docs.stripe.com/api/events/types#event_types-setup_intent.setup_failed)
-
[mandate.updated](https://docs.stripe.com/api/events/types#event_types-mandate.updated)
- [subscription](https://docs.stripe.com/api/subscriptions)
- [default payment
method](https://docs.stripe.com/api/customers/create#create_customer-invoice_settings-default_payment_method)
- [Stripe Dashboard](https://dashboard.stripe.com/test/subscriptions)
- [automatic collection
settings](https://docs.stripe.com/invoicing/automatic-collection)
- [charge them with a different payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method)
- [test API keys](https://docs.stripe.com/keys#test-live-modes)