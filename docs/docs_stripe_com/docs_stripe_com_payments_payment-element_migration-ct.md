# Migrate to Confirmation Tokens

## Finalize payments on the server by using a ConfirmationToken instead of a PaymentMethod.

Use this guide to learn how to finalize payments on the server by using a
[ConfirmationToken](https://docs.stripe.com/api/confirmation_tokens/object)
instead of a [PaymentMethod](https://docs.stripe.com/api/payment_methods) to
send data collected from your client to your server.

A `ConfirmationToken` holds a superset of the data found on a `PaymentMethod`,
such as shipping information, and enables new features as we build them.

[Create the Confirmation
Tokenclient-side](https://docs.stripe.com/payments/payment-element/migration-ct#client-side)
Instead of calling
[stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method_elements),
call
[stripe.createConfirmationToken](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token)
to create a `ConfirmationToken` object. Pass this ConfirmationToken to the
server to confirm the PaymentIntent.

The `stripe.createConfirmationToken` method accepts the same parameters as
`stripe.createPaymentMethod` (through
[params.payment_method_data](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-payment_method_data)),
plus additional
[shipping](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-shipping)
and
[return_url](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-return_url)
parameters.

BeforeAfter
```
// Create the PaymentMethod using the details collected by the Payment Element.
const {error, paymentMethod} = await stripe.createPaymentMethod({
 elements,
 params: {
 billing_details: {
 name: 'Jenny Rosen',
 }
 }
});

if (error) {
// This point is only reached if there's an immediate error when creating the
PaymentMethod.
 // Show the error to your customer (for example, payment details incomplete)
 handleError(error);
 return;
}

// Create and confirm the PaymentIntent
const res = await fetch("/create-confirm-intent", {
 method: "POST",
 headers: {"Content-Type": "application/json"},
 body: JSON.stringify({
 paymentMethodId: paymentMethod.id,
 }),
});
```

```
// Create the ConfirmationToken using the details collected by the Payment
Element and additional shipping information. Provide shipping and return_url if
you don't want to provide it when confirming the intent on the server
const {error, confirmationToken} = await stripe.createConfirmationToken({
 elements,
 params: {
 payment_method_data: {
 billing_details: {
 name: 'Jenny Rosen',
 }
 },
// Remove shipping if you're collecting it using Address Element or don't
require it
 shipping: {
 name: 'Jenny Rosen',
 address: {
 line1: '1234 Main Street',
 city: 'San Francisco',
 state: 'CA',
 country: 'US',
 postal_code: '94111',
 },
 },
 return_url: 'https://example.com/order/123/complete',
 }
});

if (error) {
// This point is only reached if there's an immediate error when creating the
ConfirmationToken.
 // Show the error to your customer (for example, payment details incomplete)
 handleError(error);
 return;
}

// Create and confirm the PaymentIntent
const res = await fetch("/create-confirm-intent", {
 method: "POST",
 headers: {"Content-Type": "application/json"},
 body: JSON.stringify({
 confirmationTokenId: confirmationToken.id,
 }),
});
```

[Create and submit the payment to
Stripeserver-side](https://docs.stripe.com/payments/payment-element/migration-ct#server-side)
You pass the ConfirmationToken to the server to confirm the
[PaymentIntent](https://docs.stripe.com/api/payment_intents), rather than
passing a [PaymentMethod](https://docs.stripe.com/api/payment_methods) as you
did before. The properties stored on the `ConfirmationToken` are applied to the
Intent when its ID is provided to the
[confirmation_token](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirmation_token)
parameter at confirmation time.

#### Note

If you already provide
[shipping](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-shipping)
and
[return_url](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-return_url)
on the ConfirmationToken, you don’t need to provide those fields again when
confirming the PaymentIntent.

BeforeAfter
```
app.post('/create-confirm-intent', async (req, res) => {
 try {
 const intent = await stripe.paymentIntents.create({
 confirm: true,
 amount: 1099,
 currency: 'usd',
// In the latest version of the API, specifying the `automatic_payment_methods`
parameter is optional because Stripe enables its functionality by default.
 automatic_payment_methods: {enabled: true},
 use_stripe_sdk: true,
 // the PaymentMethod ID sent by your client
 payment_method: req.body.paymentMethodId,
 return_url: 'https://example.com/order/123/complete',
 mandate_data: {
 customer_acceptance: {
 type: "online",
 online: {
 ip_address: req.ip,
 user_agent: req.get("user-agent"),
 },
 },
 },
 shipping: {
 name: 'Jenny Rosen',
 address: {
 line1: '1234 Main Street',
 city: 'San Francisco',
 state: 'CA',
 country: 'US',
 postal_code: '94111',
 },
 }
 });
 res.json({
 client_secret: intent.client_secret,
 status: intent.status
 });
 } catch (err) {
 res.json({
 error: err
 })
 }
});
```

```
app.post('/create-confirm-intent', async (req, res) => {
 try {
 const intent = await stripe.paymentIntents.create({
 confirm: true,
 amount: 1099,
 currency: 'usd',
// In the latest version of the API, specifying the `automatic_payment_methods`
parameter is optional because Stripe enables its functionality by default.
 automatic_payment_methods: {enabled: true},
 use_stripe_sdk: true,
// the ConfirmationToken ID sent by your client that already has the shipping,
mandate_data, and return_url data
 confirmation_token: req.body.confirmationTokenId,
 });
 res.json({
 client_secret: intent.client_secret,
 status: intent.status
 });
 } catch (err) {
 res.json({
 error: err
 })
 }
});
```

Any parameters provided directly to the PaymentIntent or SetupIntent at
confirmation time, such as `shipping` override corresponding properties on the
ConfirmationToken.

[OptionalSetting conditional parameters setup_future_usage or capture_method
based on payment
method](https://docs.stripe.com/payments/payment-element/migration-ct#conditional-options)
## See also

- [Design an
integration](https://docs.stripe.com/payments/payment-element/design-an-integration)

## Links

- [ConfirmationToken](https://docs.stripe.com/api/confirmation_tokens/object)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
-
[stripe.createPaymentMethod](https://docs.stripe.com/js/payment_methods/create_payment_method_elements)
-
[stripe.createConfirmationToken](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token)
-
[params.payment_method_data](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-payment_method_data)
-
[shipping](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-shipping)
-
[return_url](https://docs.stripe.com/js/confirmation_tokens/create_confirmation_token#create_confirmation_token-options-params-return_url)
-
[https://example.com/order/123/complete](https://example.com/order/123/complete)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
-
[confirmation_token](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirmation_token)
- [Design an
integration](https://docs.stripe.com/payments/payment-element/design-an-integration)