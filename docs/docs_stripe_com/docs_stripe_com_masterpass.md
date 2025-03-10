# Masterpass guideDeprecated

## Accept payments via Masterpass in your existing Stripe integration.

#### Warning

Mastercard plans to deprecate Masterpass in favor of [Secure Remote
Commerce](https://docs.stripe.com/secure-remote-commerce), which delivers
unified online checkout supporting a number of card brands. Stripe doesn’t
support new Masterpass integrations and existing integrations must migrate to
Secure Remote Commerce as soon as possible.

Masterpass is a third-party service that stores payment and shipping information
for its users in order to streamline the checkout process. Instead of entering
payment information on your checkout page, users can click the Masterpass button
instead. Your Stripe integration receives a unique transaction ID that it can
use to create a charge against the payment information stored in the user’s
Masterpass account.

## Integrating the Masterpass button

To get started, generate your Masterpass **Checkout ID** in the
[Dashboard](https://dashboard.stripe.com/account/payments/settings) and
configure your sandbox and production callback URLs.

To use Masterpass on your website, add the following script tag to your HTML
document:

SandboxProduction
```
<script type="text/javascript"
src="https://sandbox.masterpass.com/integration/merchant.js"></script>
```

To display the Masterpass button, use the following image:

```
<img id="mpbutton"
src="https://static.masterpass.com/dyn/img/btn/global/mp_chk_btn_147x034px.svg"/>
```

Attach a click handler to the image and use it to invoke the
`masterpass.checkout` function with the desired parameters:

```
let button = document.getElementById("mpbutton");

button.addEventListener("click", ev =>
 masterpass.checkout({
 checkoutId: "{MASTERPASS_CHECKOUT_ID}",
 allowedCardTypes: ["master", "amex", "visa"],
 amount: "10.00",
 currency: "USD",
 cartId: "{UNIQUE_ID}",
 callbackUrl: "{CALLBACK_URL}"
 }));
```

The `masterpass.checkout` function requires the following parameters:

ParameterDescription`checkoutId`The Checkout ID for your Masterpass project,
copied from the
[Dashboard](https://dashboard.stripe.com/account/payments/settings)`allowedCardTypes`A
list of the Masterpass-compatible payment providers that you want to
support`amount`The amount of the transaction, expressed in decimal
format`currency`The currency in which to perform the transaction`cartId`A unique
string that you generate to identify the purchase`callbackUrl`(Optional)
Overrides the default `callbackUrl` configured when activating Masterpass.
For more details about the `masterpass.checkout` function and the parameters
that it accepts,
[refer](https://developer.mastercard.com/documentation/masterpass-merchant-integration-v7/7#standard-checkout1)
to Mastercard’s documentation.

## Completing the payment

When the user clicks the Masterpass button on your checkout page, it takes them
to the Masterpass website where they can select an existing payment method from
their account or input a new one. When the user completes the process,
Masterpass redirects them to the callback URL that you configured when
activating Masterpass, or the specified callback URL when invoking
`masterpass.checkout` function. It appends an `oauth_verifier` URL query
parameter that your application can use to complete the transaction.

In the route handler for the redirect destination, extract the URL query
parameter and use it to
[confirm](https://docs.stripe.com/api/payment_intents/confirm) the
[PaymentIntent](https://docs.stripe.com/api/payment_intents) that you have
created at the beginning of the checkout flow. See [accept a
payment](https://docs.stripe.com/payments/accept-a-payment) to learn how to
manage your checkout flow using Payment Intents.

The following code example demonstrates how to confirm a PaymentIntent with
Masterpass in Node.js with the Express framework:

```
app.get('/callback', async (req, res) => {
// retrieve the PaymentIntent ID created at the beginning of the checkout flow.
 const payment_intent_id = '{{PAYMENT_INTENT_ID}}';

const payment_intent = await stripe.paymentIntents.confirm(payment_intent_id, {
 amount: 1000,
 currency: 'usd',
 payment_method_data: {
 type: 'card',
 card: {
 masterpass: {
 cart_id: '{{UNIQUE_ID}}',
 transaction_id: req.query.oauth_verifier,
 },
 },
 },
 });

 res.send('<h1>Charge succeeded</h1>');
});
```

Use the Masterpass sandbox environment while testing, and the Masterpass
production environment in Stripe’s live mode. When creating the source, be sure
to use the same unique value for the `cart_id` property that you used on your
checkout page.

## Testing Masterpass

To test your Masterpass integration against Mastercard’s sandbox, create a new
Masterpass user account during the checkout process on your website. Configure
the account to use one of the [test
cards](https://developer.mastercard.com/page/masterpass-sandbox-testing-guidelines#new-web-experience)
from the Masterpass documentation. Complete the checkout process as normal,
selecting the test card as your Masterpass payment method. If everything works
correctly, Masterpass redirects you back to your application, which creates the
charge as expected.

## Links

- [Secure Remote Commerce](https://docs.stripe.com/secure-remote-commerce)
- [implementation requirements](https://developer.mastercard.com)
- [Operating
Rules](https://masterpass.com/assets/pdf/masterpassoperatingrules.pdf)
- [Dashboard](https://dashboard.stripe.com/account/payments/settings)
-
[https://sandbox.masterpass.com/integration/merchant.js](https://sandbox.masterpass.com/integration/merchant.js)
-
[https://static.masterpass.com/dyn/img/btn/global/mp_chk_btn_147x034px.svg](https://static.masterpass.com/dyn/img/btn/global/mp_chk_btn_147x034px.svg)
-
[refer](https://developer.mastercard.com/documentation/masterpass-merchant-integration-v7/7#standard-checkout1)
- [confirm](https://docs.stripe.com/api/payment_intents/confirm)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [accept a payment](https://docs.stripe.com/payments/accept-a-payment)
- [test
cards](https://developer.mastercard.com/page/masterpass-sandbox-testing-guidelines#new-web-experience)