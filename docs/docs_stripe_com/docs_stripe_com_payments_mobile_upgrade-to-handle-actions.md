# Migrate your basic card integration

## Migrate your mobile app to an integration that can handle bank requests for card authentication.

iOSAndroidReact Native
If you followed the [Card payments without bank
authentication](https://docs.stripe.com/payments/without-card-authentication)
guide, your integration creates payments that decline when a bank asks the
customer to authenticate the purchase.

If you start seeing many failed payments like the one in the Dashboard below or
with an error code of `requires_action_not_handled` in the API, upgrade your
basic integration to handle, rather than decline, these payments.

![Dashboard showing a failed payment that says that this bank required
authentication for this
payment](https://b.stripecdn.com/docs-statics-srv/assets/failed-payment-dashboard.9e22ec31f3c7063665911e26e389c5dc.png)

Use this guide to learn how to upgrade the integration you built in the previous
guide to add server and client code that prompts the customer to authenticate
the payment by displaying a modal.

#### Note

See a [full
sample](https://github.com/stripe-samples/accept-a-payment/tree/master/custom-payment-flow)
of this integration on GitHub.

[Check if the payment requires
authenticationServer-side](https://docs.stripe.com/payments/mobile/upgrade-to-handle-actions#update-server)
Make three changes to the endpoint on your server that creates the
PaymentIntent:

- **Remove** the
[error_on_requires_action](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-error_on_requires_action)
parameter to no longer fail payments that require authentication. Instead, the
PaymentIntent status changes to `requires_action`.
- **Add** the `confirmation_method` parameter to indicate that you want to
explicitly (manually) confirm the payment again on the server after handling
authentication requests.
- **Add** the
[use_stripe_sdk](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-use_stripe_sdk)
parameter to enable your mobile client to handle additional authentication
steps.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount=1099 \
 -d currency=usd \
 -d payment_method_types[]=card \
 -d confirm=true \
 -d error_on_requires_action=true \
 -d payment_method="{{PAYMENT_METHOD_ID}}" \
 -d confirmation_method=manual
```

Then update your “generate response” function to handle the `requires_action`
state instead of erroring:

```
# If the request succeeds, check the
# PaymentIntent's `status` and handle
# its `next_action`.
```

[Ask the customer to
authenticateClient-side](https://docs.stripe.com/payments/mobile/upgrade-to-handle-actions#update-client)
Next, update your Android code to tell Stripe to show a modal if the customer
needs to authenticate.

Use `handleNextActionForPayment` when a PaymentIntent has a status of
`requires_action`. If successful, the PaymentIntent will have a status of
`requires_confirmation` and you need to confirm the PaymentIntent again on your
server to finish the payment.

```
public class CheckoutActivity extends Activity {
 private Stripe stripe;

 @Override
 protected void onCreate(@Nullable Bundle savedInstanceState) {
 super.onCreate(savedInstanceState);
 stripe = new Stripe(this, "pk_test_TYooMQauvdEDq54NiTphI7jx");
 }
 private void handleResponse(@NonNull JSONObject json) throws JSONException {
 if (json.has("error")) {
 // Display the error to the customer
 final String error = json.getString("error");
 } else if (json.has("requiresAction")) {
 final String clientSecret = json.getString("clientSecret");
 stripe.handleNextActionForPayment(this, clientSecret);
 } else {
 // Display success message
 }
 }
 @Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable
Intent data) {
 super.onActivityResult(requestCode, resultCode, data);

 stripe.onPaymentResult(requestCode, data,
 new ApiResultCallback<PaymentIntentResult>() {
 @Override
 public void onSuccess(@NonNull PaymentIntentResult result) {
 switch (result.getOutcome()) {
 case StripeIntentResult.Outcome.SUCCEEDED: {
 // The card action has been handled
// Send the Payment Intent ID to your server and confirm it again
 }
 case StripeIntentResult.Outcome.CANCELED: {
 // Canceled
 }
 case StripeIntentResult.Outcome.TIMEDOUT: {
 // Timed-out
 }
 case StripeIntentResult.Outcome.FAILED: {
 // Failed
 }
 }
 }

 @Override
 public void onError(@NonNull Exception e) {
 // Error encountered
 }
 }
 );
 }
}
```

[Confirm the PaymentIntent
againServer-side](https://docs.stripe.com/payments/mobile/upgrade-to-handle-actions#update-server-second-confirm)
Using the same endpoint you set up earlier, confirm the PaymentIntent again to
finalize the payment and fulfill the order. The payment attempt fails and
transitions back to `requires_payment_method` if it is not confirmed again
within one hour.

```
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X "POST"
```

[Test the
integration](https://docs.stripe.com/payments/mobile/upgrade-to-handle-actions#test-manual)
Use our test cards in a sandbox to verify that your integration was properly
updated. Stripe displays a fake authentication page inside the modal in a
sandbox that lets you simulate a successful or failed authentication attempt. In
live mode the bank controls the UI of what is displayed inside the modal.

NumberDescription4242424242424242Succeeds and immediately processes the
payment.4000000000009995Always fails with a decline code of
`insufficient_funds`.4000002500003155Requires authentication, which in this
integration will fail with a decline code of `authentication_not_handled`.

## Links

- [Card payments without bank
authentication](https://docs.stripe.com/payments/without-card-authentication)
- [full
sample](https://github.com/stripe-samples/accept-a-payment/tree/master/custom-payment-flow)
-
[error_on_requires_action](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-error_on_requires_action)
-
[use_stripe_sdk](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-use_stripe_sdk)