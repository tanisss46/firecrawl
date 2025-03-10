# Set up a subscription with pre-authorized debit in Canada

## Learn how to create and charge for a subscription with Canadian pre-authorized debits.

#### Note

Subscription mode in [Checkout](https://docs.stripe.com/payments/checkout) isn’t
yet supported. To learn about early access when this feature is available,
[contact
us](mailto:payment-methods-feedback@stripe.com?subject=PADs%20Subscription%20Mode%20User%20Interest)
to join the waitlist.

[Create a product and
priceDashboard](https://docs.stripe.com/billing/subscriptions/acss-debit#create-product-plan-code)
[Products](https://docs.stripe.com/api/products) represent the item or service
you’re selling. [Prices](https://docs.stripe.com/api/prices) define how much and
how frequently you charge for a product. This includes how much the product
costs, what currency you accept, and whether it’s a one-time or recurring
charge. If you only have a few products and prices, create and manage them in
the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15
CAD monthly subscription. To model this:

- Navigate to the [Add a
product](https://dashboard.stripe.com/test/products/create) page.
- Enter a **Name** for the product.
- Enter **15** for the price.
- Select **CAD** as the currency.
- Click **Save product**.

After you create the product and the price, record the price ID so you can use
it in subsequent steps. The pricing page displays the ID and it looks similar to
this: `price_G0FvDp6vZvdwRZ`.

[Create the
subscriptionServer-side](https://docs.stripe.com/billing/subscriptions/acss-debit#create-subscription)
#### Note

To create a subscription with a free trial period, see [Subscription
trials](https://docs.stripe.com/billing/subscriptions/acss-debit#trial-periods).

Create a [subscription](https://docs.stripe.com/api/subscriptions) with the
price and customer with status `incomplete` by providing the
[payment_behavior](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)
parameter with the value of `default_incomplete`.

```
curl https://api.stripe.com/v1/subscriptions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer"="{{CUSTOMER_ID}}" \
 -d "items[0][price]"="price_F52b2UdntfQsfR" \
 -d "payment_behavior"="default_incomplete" \
 -d "payment_settings[payment_method_types][]"="acss_debit" \
 -d "expand[0]"="latest_invoice.payment_intent"
```

Included in the response is the
[subscription](https://docs.stripe.com/billing/subscriptions/creating)’s first
[PaymentIntent](https://docs.stripe.com/payments/payment-intents), containing
the [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret),
which is used on the client side to securely complete the payment process
instead of passing the entire PaymentIntent object. Return the `client_secret`
to the frontend to complete payment.

[Collect payment method details and mandate
acknowledgmentClient-side](https://docs.stripe.com/billing/subscriptions/acss-debit#collect-payment-and-mandate)
To use Canadian pre-authorized debits, you must obtain authorization from your
customer for one-time and recurring debits using a pre-authorized debit
agreement (see [PAD
Mandates](https://docs.stripe.com/payments/acss-debit#mandates)). The
[Mandate](https://docs.stripe.com/api/mandates) object records this agreement
and authorization.

Stripe automatically configures subscription and
[invoice](https://docs.stripe.com/api/invoices) mandates for you. The customer
only needs to acknowledge the mandate terms once, subsequent subscription
charges will succeed without further intervention.

When a customer clicks to pay with Canadian pre-authorized debit, we recommend
you use Stripe.js to submit the payment to Stripe.
[Stripe.js](https://docs.stripe.com/payments/elements) is our foundational
JavaScript library for building payment flows. It will automatically handle
integration complexities, and enables you to easily extend your integration to
other payment methods in the future.

Include the Stripe.js script on your checkout page by adding it to the `head` of
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
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
```

Rather than sending the entire PaymentIntent object to the client, use its
[client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
from the previous step. This is different from your API keys that authenticate
Stripe API requests.

The client secret should still be handled carefully because it can complete the
charge. Do not log it, embed it in URLs, or expose it to anyone but the
customer.

Use
[stripe.confirmAcssDebitPayment](https://docs.stripe.com/js/payment_intents/confirm_acss_debit_payment)
to collect bank account details and verification, confirm the mandate, and
complete the payment when the user submits the form. Including the customer’s
email address and the account holder’s name in the `billing_details` property of
the `payment_method` parameter is required to create a PAD payment method.

```
const form = document.getElementById('payment-form');
const accountholderName = document.getElementById('accountholder-name');
const email = document.getElementById('email');
const submitButton = document.getElementById('submit-button');
const clientSecret = submitButton.dataset.secret;

form.addEventListener('submit', async (event) => {
 event.preventDefault();

 const {paymentIntent, error} = await stripe.confirmAcssDebitPayment(
 clientSecret,
 {
 payment_method: {
 billing_details: {
 name: accountholderName.value,
 email: email.value,
 },
 },
 }
 );

 if (error) {
 // Inform the customer that there was an error.
 console.log(error.message);
 } else {
 // Handle next step based on PaymentIntent's status.
 console.log("PaymentIntent ID: " + paymentIntent.id);
 console.log("PaymentIntent status: " + paymentIntent.status);
 }
});
```

Stripe.js then loads an on-page modal UI that handles bank account details
collection and verification, presents a hosted mandate agreement and collects
authorization.

#### Note

`stripe.confirmAcssDebitPayment` may take several seconds to complete. During
that time, disable your form from being resubmitted and show a waiting indicator
like a spinner. If you receive an error, show it to the customer, re-enable the
form, and hide the waiting indicator.

If the customer completes instant verification, the subscription automatically
becomes `active`. Otherwise, consult the following section to handle
micro-deposit verification while the subscription remains `incomplete`.

[Verify bank account with
micro-depositsClient-side](https://docs.stripe.com/billing/subscriptions/acss-debit#verify-with-microdeposits)
#### Note

[Customers](https://docs.stripe.com/api/customers) have 10 days to successfully
verify micro-deposits for a subscription, instead of 23 hours normally given in
the [subscription
lifecycle](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle).
However, this expiration can’t be later than the [billing cycle
date](https://docs.stripe.com/billing/subscriptions/acss-debit#billing-cycle).

Not all customers can verify the bank account instantly. This step only applies
if your customer has elected to opt out of the instant verification flow in the
previous step.

In this case, Stripe automatically sends two micro-deposits to the customer’s
bank account. These deposits take 1–2 business days to appear on the customer’s
online statement and have statement descriptors that include `ACCTVERIFY`.

The result of the `stripe.confirmAcssDebitPayment` method call in the previous
step is a PaymentIntent in the `requires_action` state. The PaymentIntent
contains a `next_action` field that contains some useful information for
completing the verification.

Stripe notifies your customer at the [billing
email](https://docs.stripe.com/api/payment_methods/object#payment_method_object-billing_details-email)
when the deposits are expected to arrive. The email includes a link to a
Stripe-hosted verification page where they can confirm the amounts of the
deposits and complete verification.

There is a limit of three failed verification attempts. If this limit is
exceeded, the bank account can no longer be verified. In addition, there is a
timeout for micro-deposit verifications of 10 days. If micro-deposits are not
verified in that time, the PaymentIntent reverts to requiring new payment method
details. Clear messaging about what these micro-deposits are and how you use
them can help your customers avoid verification issues.

### Optional: Custom email and verification page

If you choose to send [custom email
notifications](https://docs.stripe.com/payments/acss-debit#mandate-and-debit-notification-emails),
you have to email your customer instead. To do this, you can use the
`verify_with_microdeposits[hosted_verification_url]` URL in the `next_action`
object to direct your customer to complete the verification process.

If you are sending custom emails and don’t want to use the Stripe hosted
verification page, you can create a form on your site for your customers to
relay these amounts to you and verify the bank account using
[Stripe.js](https://docs.stripe.com/js/payment_intents/verify_microdeposits_for_payment).

```
stripe.verifyMicrodepositsForPayment(clientSecret, {
 amounts: [32, 45],
});
```

[Set the default payment
methodServer](https://docs.stripe.com/billing/subscriptions/acss-debit#default-payment-method)
You now have an active
[subscription](https://docs.stripe.com/billing/subscriptions/creating) belonging
to a customer with a payment method, but this payment method isn’t automatically
used for future payments. To automatically bill this payment method in the
future, use a [webhook](https://docs.stripe.com/webhooks) consumer to listen to
the `invoice.payment_succeeded` event for new subscriptions and set the default
payment method.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

if event.type == 'invoice.payment_succeeded'
 invoice = event.data.object
 if invoice['billing_reason'] == 'subscription_create'
 subscription_id = invoice['subscription']
 payment_intent_id = invoice['payment_intent']

 # Retrieve the payment intent used to pay the subscription
 payment_intent = Stripe::PaymentIntent.retrieve(payment_intent_id)

 # Set the default payment method
 Stripe::Subscription.update(
 subscription_id,
 default_payment_method: payment_intent.payment_method
 )
 end
end
```

[Manage subscription
statusClient-side](https://docs.stripe.com/billing/subscriptions/acss-debit#manage-sub-status)
Assuming the initial payment succeeds, the state of the subscription is `active`
and requires no further action. When payments fail, the status changes to the
**Subscription status** configured in your [automatic collection
settings](https://docs.stripe.com/invoicing/automatic-collection). Notify the
customer upon failure and [charge them with a different payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method).

#### Note

Canadian pre-authorized debit payments are never automatically retried, even if
you have a [retry
schedule](https://docs.stripe.com/invoicing/automatic-collection) configured for
other payment methods.

[Test your
integration](https://docs.stripe.com/billing/subscriptions/acss-debit#test-integration)
### Receive micro-deposit verification email

In order to receive the micro-deposit verification email in test mode after
collecting the bank account details and accepting a mandate, provide an email in
the `payment_method[billing_details][email]` field in the form of
`{any_prefix}+test_email@{any_domain}` when confirming the payment method
details.

### Test account numbers

Stripe provides several test account numbers you can use to make sure your
integration for manually-entered bank accounts is ready for production. All test
accounts that automatically succeed or fail the payment must be verified using
the test micro-deposit amounts below before they can be completed.

Institution NumberTransit NumberAccount
NumberScenario`000``11000``000123456789`Succeeds the payment immediately after
micro-deposits are verified.`000``11000``900123456789`Succeeds the payment with
a three-minute delay after micro-deposits are
verified.`000``11000``000222222227`Fails the payment immediately after
micro-deposits are verified.`000``11000``900222222227`Fails the payment with a
three-minute delay after micro-deposits are
verified.`000``11000``000666666661`Fails to send verification
micro-deposits.`000``11000``000777777771`Fails the payment due to the payment
amount causing the account to exceed its weekly payment volume
limit.`000``11000``000888888881`Fails the payment due to the payment amount
exceeding the account’s transaction limit.
To mimic successful or failed bank account verifications in test mode, use these
meaningful amounts for micro-deposits:

Micro-deposit ValuesScenario`32` and `45`Successfully verifies the account.Any
other number combinationsFails account verification.[OptionalSetting the billing
cycle](https://docs.stripe.com/billing/subscriptions/acss-debit#billing-cycle)[OptionalSubscription
trials](https://docs.stripe.com/billing/subscriptions/acss-debit#trial-periods)[OptionalSaving
payment method details for future
use](https://docs.stripe.com/billing/subscriptions/acss-debit#save-payment-method-for-future-subscriptions)

## Links

- [Checkout](https://docs.stripe.com/payments/checkout)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [Add a product](https://dashboard.stripe.com/test/products/create)
- [subscription](https://docs.stripe.com/api/subscriptions)
-
[payment_behavior](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [PAD Mandates](https://docs.stripe.com/payments/acss-debit#mandates)
- [Mandate](https://docs.stripe.com/api/mandates)
- [invoice](https://docs.stripe.com/api/invoices)
- [Stripe.js](https://docs.stripe.com/payments/elements)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[stripe.confirmAcssDebitPayment](https://docs.stripe.com/js/payment_intents/confirm_acss_debit_payment)
- [Customers](https://docs.stripe.com/api/customers)
- [subscription
lifecycle](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)
- [billing
email](https://docs.stripe.com/api/payment_methods/object#payment_method_object-billing_details-email)
- [custom email
notifications](https://docs.stripe.com/payments/acss-debit#mandate-and-debit-notification-emails)
-
[Stripe.js](https://docs.stripe.com/js/payment_intents/verify_microdeposits_for_payment)
- [webhook](https://docs.stripe.com/webhooks)
- [automatic collection
settings](https://docs.stripe.com/invoicing/automatic-collection)
- [charge them with a different payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method)