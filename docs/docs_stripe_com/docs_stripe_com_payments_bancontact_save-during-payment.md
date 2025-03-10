# Save bank details during a Bancontact payment

## Learn how to save your customer's IBAN bank details from a Bancontact payment.

#### Caution

We recommend that you follow the [Save payment details during
payment](https://docs.stripe.com/payments/save-during-payment) guide. If you’ve
already integrated with Elements, see the [Payment Element migration
guide](https://docs.stripe.com/payments/payment-element/migration).

Bancontact is a popular [single
use](https://docs.stripe.com/payments/payment-methods#usage) payment method in
Belgium where customers are required to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. [Customers](https://docs.stripe.com/api/customers) pay with
Bancontact by redirecting from your website, authorizing the payment, then
returning to your website where you get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

You can use Bancontact to save your customer’s
[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number) bank
details into a [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
[PaymentMethod](https://docs.stripe.com/api/payment_methods). You can then use
the SEPA Direct Debit PaymentMethod to [accept
payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment) or [set
up a subscription](https://docs.stripe.com/billing/subscriptions/sepa-debit).
This reduces friction for your customer as they don’t have to enter their IBAN
again. You also receive their verified name and validated IBAN.

#### Caution

To use Bancontact to set up SEPA Direct Debit payments, you must activate SEPA
Direct Debit in the
[Dashboard](https://dashboard.stripe.com/account/payments/settings). You must
also comply with the [Bancontact Terms of
Service](https://stripe.com/bancontact/legal) and [SEPA Direct Debit Terms of
Service](https://stripe.com/sepa-direct-debit/legal).

WebiOSAndroidReact Native
Accepting Bancontact payments consists of creating a
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object) object to
track a payment, collecting payment method details and mandate acknowledgement,
and submitting the payment to Stripe for processing. Stripe uses the
PaymentIntent to track and handle all the states of the payment until the
payment completes. Use the ID of the SEPA Direct Debit
[PaymentMethod](https://docs.stripe.com/api/payment_methods) collected from your
initial Bancontact PaymentIntent to create future payments.

[Set up
StripeServer-side](https://docs.stripe.com/payments/bancontact/save-during-payment#web-set-up-stripe)
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

[Create a
CustomerServer-side](https://docs.stripe.com/payments/bancontact/save-during-payment#web-create-customer)
Create a [Customer](https://docs.stripe.com/api/customers) when they create an
account with your business and associate it with your internal representation of
their account. This enables you to retrieve and use their saved payment method
details later.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Create a
PaymentIntentServer-side](https://docs.stripe.com/payments/bancontact/save-during-payment#web-create-payment-intent)
Create a `PaymentIntent` on your server and specify the `amount` to collect, the
`eur` currency, the customer ID, and off_session as an argument for [setup
future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
If you have an existing [Payment
Intents](https://docs.stripe.com/payments/payment-intents) integration, add
`bancontact` to the list of [payment method
types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types).

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=eur \
 -d "payment_method_types[]"=bancontact \
 -d customer={{CUSTOMER_ID}} \
 -d setup_future_usage=off_session
```

### Retrieve the client secret

The PaymentIntent includes a [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
that the client side uses to securely complete the payment process. You can use
different approaches to pass the client secret to the client side.

Single-page applicationServer-side rendering
Retrieve the client secret from an endpoint on your server, using the browser’s
`fetch` function. This approach is best if your client side is a single-page
application, particularly one built with a modern frontend framework like React.
Create the server endpoint that serves the client secret:

```
get '/secret' do
 intent = # ... Create or retrieve the PaymentIntent
 {client_secret: intent.client_secret}.to_json
end
```

And then fetch the client secret with JavaScript on the client side:

```
(async () => {
 const response = await fetch('/secret');
 const {client_secret: clientSecret} = await response.json();
 // Render the form using the clientSecret
})();
```

[Collect payment method details and mandate
acknowledgementClient-side](https://docs.stripe.com/payments/bancontact/save-during-payment#web-collect-payment-method-details)
Create a payment form on your client to collect the required billing details
from the customer.

HTML + JSReact
​​To process SEPA Direct Debit payments, you must collect a mandate agreement
from your customer. Display the following standard authorization text for your
customer to implicitly sign the mandate.

Replace *Rocket Rides* with your company name.

deenesfifritnlAuthorization text template
By providing your payment information and confirming this payment, you authorise
(A) and Stripe, our payment service provider, to send instructions to your bank
to debit your account and (B) your bank to debit your account in accordance with
those instructions. As part of your rights, you are entitled to a refund from
your bank under the terms and conditions of your agreement with your bank. A
refund must be claimed within 8 weeks starting from the date on which your
account was debited. Your rights are explained in a statement that you can
obtain from your bank. You agree to receive notifications for future debits up
to 2 days before they occur.

​​Setting up a payment method or confirming a PaymentIntent creates the accepted
mandate. As the customer has implicitly signed the mandate, you must communicate
these terms in your form or through email.

FieldValue`name`The full name (first and last) of the customer.`email`The
customer’s email.
```
<form id="payment-form">
 <div class="form-row">
 <label for="name">
 Name
 </label>
 <input id="name" name="name" required>
 </div>

 <div class="form-row">
 <label for="email">
 Email
 </label>
 <input id="email" name="email" required>
 </div>

 <button id="submit-button">Pay with Bancontact</button>

 <!-- Display mandate acceptance text. -->
 <div id="mandate-acceptance">
 By providing your payment information and confirming this payment, you
 authorise (A) Rocket Rides and Stripe, our payment service provider, to
 send instructions to your bank to debit your account and (B) your bank to
 debit your account in accordance with those instructions. As part of your
 rights, you are entitled to a refund from your bank under the terms and
 conditions of your agreement with your bank. A refund must be claimed
 within 8 weeks starting from the date on which your account was debited.
 Your rights are explained in a statement that you can obtain from your
 bank. You agree to receive notifications for future debits up to 2 days
 before they occur.
 </div>
 <!-- Used to display form errors. -->
 <div id="error-message" role="alert"></div>
</form>
```

[Submit the payment to
StripeClient-side](https://docs.stripe.com/payments/bancontact/save-during-payment#web-submit-payment)
Create a payment on the client side with the [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
of the PaymentIntent. The client secret is different from your API keys that
authenticate Stripe API requests. It should be handled carefully because it can
complete the charge. Do not log it, embed it in URLs, or expose it to anyone but
the customer.

HTML + JSReact
Call
[stripe.confirmBancontactPayment](https://docs.stripe.com/js/payment_intents/confirm_bancontact_payment)
to redirect your customer to Bancontact’s website or app to complete the
payment. Include a
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
to redirect your customer after they complete the payment. You must also provide
the customer’s full name and email in `billing_details`.

```
var stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
var accountholderName = document.getElementById('name');
var accountholderEmail = document.getElementById('email');

// Redirects away from the client
const {error} = await stripe.confirmBancontactPayment(
 '{{PAYMENT_INTENT_CLIENT_SECRET}}',
 {
 payment_method: {
 billing_details: {
 name: accountholderName.value,
 email: accountholderEmail.value,
 },
 },
 return_url: 'https://example.com/checkout/complete',
 }
);

if (error) {
 // Inform the customer that there was an error.
}
```

When your customer submits a payment, Stripe redirects them to the `return_url`
and includes the following URL query parameters. The return page can use them to
get the status of the PaymentIntent so it can display the payment status to the
customer.

When you specify the `return_url`, you can also append your own query parameters
for use on the return page.

ParameterDescription`payment_intent`The unique identifier for the
`PaymentIntent`.`payment_intent_client_secret`The [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
of the `PaymentIntent` object.
When the customer is redirected back to your site, you can use the
`payment_intent_client_secret` to query for the PaymentIntent and display the
transaction status to your customer.

[Charge the SEPA Direct Debit PaymentMethod
later](https://docs.stripe.com/payments/bancontact/save-during-payment#web-charge-sepa-pm)
When you need to charge your customer again, create a new PaymentIntent. Find
the ID of the SEPA Direct Debit payment method by
[retrieving](https://docs.stripe.com/api/payment_intents/retrieve) the previous
PaymentIntent and [expanding](https://docs.stripe.com/api/expanding_objects) the
`latest_charge` field where you will find the `generated_sepa_debit` ID inside
of `payment_method_details`.

```
curl -G https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=latest_charge
```

The SEPA Direct Debit payment method ID is the `generated_sepa_debit` ID under
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-ideal)
in the response.

```
{
 "latest_charge": {
 "payment_method_details": {
 "bancontact": {
 "bank_code": "VAPE",
 "bank_name": "VAN DE PUT & CO",
 "bics": "VAPEBE22",
 "iban_last4": "7061",
 "generated_sepa_debit": "pm_1GrddXGf98efjktuBIi3ag7aJQ",
 "preferred_language": "en",
 "verified_name": "Jenny Rosen"
 },
 "type": "bancontact"
 },
 },
 "payment_method_options": {
 "bancontact": {}
```

See all 32 lines
Create a PaymentIntent with the SEPA Direct Debit and Customer IDs.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "payment_method_types[]"=sepa_debit \
 -d amount=1099 \
 -d currency=eur \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{SEPA_DEBIT_PAYMENT_METHOD_ID}} \
 -d confirm=true
```

[Test your
integration](https://docs.stripe.com/payments/bancontact/save-during-payment#test-your-integration)EmailPaymentMethod
Set `payment_method.billing_details.email` to one of the following values to
test the PaymentIntent status transitions. You can include your own custom text
at the beginning of the email address followed by an underscore. For example,
`test_1_generatedSepaDebitIntentsFail@example.com` results in a SEPA Direct
Debit PaymentMethod that always fails when used with a PaymentIntent.

Email AddressDescription`generatedSepaDebitIntentsSucceed@example.com`The
PaymentIntent status transitions from `processing` to
`succeeded`.`generatedSepaDebitIntentsSucceedDelayed@example.com`The
PaymentIntent status transitions from `processing` to `succeeded` after at least
three minutes.`generatedSepaDebitIntentsFail@example.com`The PaymentIntent
status transitions from `processing` to
`requires_payment_method`.`generatedSepaDebitIntentsFailDelayed@example.com`The
PaymentIntent status transitions from `processing` to `requires_payment_method`
after at least three
minutes.`generatedSepaDebitIntentsSucceedDisputed@example.com`The PaymentIntent
status transitions from `processing` to `succeeded`, but a dispute is created
immediately.[OptionalHandle post-payment
events](https://docs.stripe.com/payments/bancontact/save-during-payment#web-fulfillment)[OptionalHandle
the Bancontact redirect
manually](https://docs.stripe.com/payments/bancontact/save-during-payment#web-handle-redirect)
## See also

- [Accept a SEPA Direct Debit
payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [Set up a subscription with SEPA Direct Debit in the
EU](https://docs.stripe.com/billing/subscriptions/sepa-debit)

## Links

- [Save payment details during
payment](https://docs.stripe.com/payments/save-during-payment)
- [Payment Element migration
guide](https://docs.stripe.com/payments/payment-element/migration)
- [accepting SEPA Direct Debit
payments](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Customers](https://docs.stripe.com/api/customers)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [set up a
subscription](https://docs.stripe.com/billing/subscriptions/sepa-debit)
- [Dashboard](https://dashboard.stripe.com/account/payments/settings)
- [Bancontact Terms of Service](https://stripe.com/bancontact/legal)
- [SEPA Direct Debit Terms of
Service](https://stripe.com/sepa-direct-debit/legal)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [Register now](https://dashboard.stripe.com/register)
- [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
- [Payment Intents](https://docs.stripe.com/payments/payment-intents)
- [payment method
types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
-
[stripe.confirmBancontactPayment](https://docs.stripe.com/js/payment_intents/confirm_bancontact_payment)
-
[return_url](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-return_url)
- [retrieving](https://docs.stripe.com/api/payment_intents/retrieve)
- [expanding](https://docs.stripe.com/api/expanding_objects)
-
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-ideal)