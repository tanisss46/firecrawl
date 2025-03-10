# Stripe payments with Visa CheckoutDeprecated

## Accept payments via Visa Checkout in your existing Stripe integration.

#### Warning

Visa terminated support for [Visa
Checkout](https://usa.visa.com/pay-with-visa/visa-checkout.html) in favor of
[Secure Remote Commerce](https://docs.stripe.com/secure-remote-commerce), which
delivers unified online checkout supporting multiple of card brands. Stripe
doesn’t support new Visa Checkout integrations and existing Visa Checkout
integrations must migrate to Secure Remote Commerce as soon as possible.

Visa Checkout is a third-party service that stores payment and shipping
information for its users in order to streamline the checkout process. Instead
of entering payment information on your checkout page, users can click the Visa
Checkout button instead. Your Stripe integration receives a unique ID that it
can use to create a charge against the payment information stored in the user’s
Visa Checkout account.

## Integrating the Visa Checkout button

To get started, generate your **Visa Checkout API key** in the
[Dashboard](https://dashboard.stripe.com/account/payments/settings). There are
two keys, a [sandbox](https://docs.stripe.com/sandboxes) key that you can use
while testing, and a production key that works in live mode.

SandboxProduction
To use Visa Checkout on your website, add the following script tag to the end of
your document’s body tag:

```
<script type="text/javascript"
src="https://sandbox-assets.secure.checkout.visa.com/checkout-widget/resources/js/integration/v1/sdk.js"></script>
```

To display the Visa Checkout button, use the following image:

```
<img alt="Visa Checkout" class="v-button" role="button"
src="https://sandbox.secure.checkout.visa.com/wallet-services-web/xo/button.png">
```

To initialize the button, add an `onVisaCheckoutReady` function that invokes
`V.init`:

```
function onVisaCheckoutReady() {
 V.init({
 apikey: '{{VISA_CHECKOUT_ID}}',
 paymentRequest:{
 subtotal: '10.00',
 currencyCode: 'USD'
 },
 settings: {
 displayName: 'My Website'
 }
 });
}
```

The Visa Checkout JavaScript SDK automatically invokes the `onVisaCheckoutReady`
function when it finishes loading. The `paymentRequest` property accepted by
`V.init` requires the following parameters:

ParameterDescription`subtotal`The amount of the transaction, expressed in
decimal format`currencyCode`The currency in which to perform the transaction
By default, American Express, MasterCard, Visa, and Discover card brands are
accepted, all shipping and billing countries are also enabled.

For more details about the `V.init` function and the parameters that it accepts,
[refer](https://developer.visa.com/images2/products/visa_checkout/VisaCheckoutMerchantDocs.zip)
to Visa’s documentation. There are optional `paymentRequest` properties that
support a range of other features, including promotions, discounts, and taxes.
There are also optional `settings` properties that allow you to control the
shipping information options.

## Completing the payment

When the user clicks the Visa Checkout button on your checkout page, it opens a
lightbox where they can select an existing payment method from their account or
input a new one. When the user completes the process, the Visa Checkout
JavaScript SDK in the browser emits a `payment.success` event with a unique ID
that your application can use to complete the transaction.

The following code shows how to handle the `payment.success` event and
[confirm](https://docs.stripe.com/api/payment_intents/confirm) the
[PaymentIntent](https://docs.stripe.com/api/payment_intents) you created at the
beginning of the checkout flow. See [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web) to
learn how to manage your checkout flow using Payment Intents.

```
// PaymentIntent client secret passed from server-side.
// See: https://stripe.com/docs/payments/accept-a-payment?platform=web
// for more information on how to do this.
const clientSecret = '{{CLIENT_SECRET}}';

V.on('payment.success', async (payment) => {
 const intent = await stripe.confirmCardPayment(clientSecret, {
 payment_method: {
 card: {
 visa_checkout: {
 callid: payment.callid,
 },
 },
 },
 });
 // Perform logic for payment completion here
});
```

## Testing Visa Checkout

To test your integration against Visa Checkout’s sandbox, create a new Visa
Checkout user account during the checkout process on your website. Configure the
account to use the test card number **4242 4242 4242 4242**, a random
three-digit CVC number, and any expiration date in the future. Complete the
checkout process as normal. If everything works correctly, Visa Checkout
redirects you back to your application, which creates the charge as expected.

## Links

- [Visa Checkout](https://usa.visa.com/pay-with-visa/visa-checkout.html)
- [Secure Remote Commerce](https://docs.stripe.com/secure-remote-commerce)
- [terms of service](https://stripe.com/visa-checkout/legal)
- [user interface
guidelines](https://developer.visa.com/capabilities/visa_checkout/docs#user_interface_guidelines)
- [Dashboard](https://dashboard.stripe.com/account/payments/settings)
- [sandbox](https://docs.stripe.com/sandboxes)
-
[https://sandbox-assets.secure.checkout.visa.com/checkout-widget/resources/js/integration/v1/sdk.js](https://sandbox-assets.secure.checkout.visa.com/checkout-widget/resources/js/integration/v1/sdk.js)
-
[https://sandbox.secure.checkout.visa.com/wallet-services-web/xo/button.png](https://sandbox.secure.checkout.visa.com/wallet-services-web/xo/button.png)
-
[refer](https://developer.visa.com/images2/products/visa_checkout/VisaCheckoutMerchantDocs.zip)
- [confirm](https://docs.stripe.com/api/payment_intents/confirm)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web)