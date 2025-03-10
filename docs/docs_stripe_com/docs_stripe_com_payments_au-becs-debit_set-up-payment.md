# Save Australia BECS Direct Debit details for future payments

## Use the Setup Intents API to save payment method details for future Australia BECS Direct Debit payments.

Advanced integrationiOSAndroidReact Native
Use [Stripe Elements](https://docs.stripe.com/payments/elements), our prebuilt
UI components, to create a payment form that lets you securely collect bank
details without handling the sensitive data. You can use the [Setup Intents
API](https://docs.stripe.com/payments/setup-intents) to collect BECS Direct
Debit payment method details in advance, and determine the final amount or
payment date later. Use it to:

- Save payment methods to a wallet to streamline future purchases
- Collect surcharges after fulfilling a service
- [Start a free trial for a
subscription](https://docs.stripe.com/billing/subscriptions/trials)
[Set up
StripeServer-side](https://docs.stripe.com/payments/au-becs-debit/set-up-payment#web-set-up-stripe)
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

[Create or retrieve a
CustomerServer-side](https://docs.stripe.com/payments/au-becs-debit/set-up-payment#web-create-customer)
To reuse a BECS Direct Debit account for future payments, you must attach it to
a [Customer](https://docs.stripe.com/api/customers).

Create a Customer object when your customer creates an account with your
business. Associating the ID of the Customer object with your own internal
representation of them enables you to retrieve and use the stored payment method
details later.

Create a new Customer or retrieve an existing Customer to associate with this
payment. Include the following code on your server to create a new Customer.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Create a
SetupIntentServer-side](https://docs.stripe.com/payments/au-becs-debit/set-up-payment#web-create-setup-intent)
A [SetupIntent](https://docs.stripe.com/api/setup_intents) is an object that
represents your intent to set up a customer’s payment method for future
payments. The `SetupIntent` will track the steps of this set-up process. For
BECS Direct Debit, this includes collecting a mandate from the customer and
tracking its validity throughout its lifecycle.

Create a [SetupIntent](https://docs.stripe.com/api/setup_intents) on your server
with
[payment_method_types](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_types)
set to `au_becs_debit` and specify the
[Customer](https://docs.stripe.com/api/customers)’s
[id](https://docs.stripe.com/api/customers/object#customer_object-id):

```
curl https://api.stripe.com/v1/setup_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="au_becs_debit" \
 -d "customer"="{{CUSTOMER_ID}}"
```

After creating a `SetupIntent` on your server, you can associate the
`SetupIntent` ID with the current session’s customer in your application’s data
model. Doing so allows you to retrieve the information after you have
successfully collected a payment method.

The returned `SetupIntent` object contains a `client_secret` property. Pass the
client secret to the client-side application to continue with the setup process.

[Collect payment method details and mandate
acknowledgmentClient-side](https://docs.stripe.com/payments/au-becs-debit/set-up-payment#web-collect-payment-method-details)
You’re ready to collect payment information on the client with [Stripe
Elements](https://docs.stripe.com/payments/elements). Elements is a set of
prebuilt UI components for collecting payment details.

A Stripe Element contains an iframe that securely sends the payment information
to Stripe over an HTTPS connection. The checkout page address must also start
with https:// rather than http:// for your integration to work.

You can test your integration without using HTTPS. [Enable
it](https://docs.stripe.com/security/guide#tls) when you’re ready to accept live
payments.

### Set up Stripe Elements

HTML + JSReact
Stripe Elements is automatically available as a feature of Stripe.js. Include
the Stripe.js script on your payment page by adding it to the `head` of your
HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI
compliant. Don’t include the script in a bundle or host a copy of it yourself.

```
<head>
 <title>Payment Setup</title>
 <script src="https://js.stripe.com/v3/"></script>
</head>
```

Create an instance of [Elements](https://docs.stripe.com/js#stripe-elements)
with the following JavaScript on your payment page:

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
const elements = stripe.elements();
```

### Direct Debit Requests

Before you can create a BECS Direct Debit payment, your customer must agree with
the Direct Debit Request Service Agreement. They do so by submitting a completed
Direct Debit Request (DDR). The approval gives you a mandate to debit their
account. The `Mandate` is a record of the permission to debit a payment method.

For online mandate acceptance, you can create a form to collect the necessary
information. Serve the form over
[HTTPS](https://docs.stripe.com/security/guide#tls) and capture the following
information:

InformationDescriptionAccount nameThe full name of the account holderBSB
numberThe Bank-State-Branch number of the bank account (for example,
`123-456`)Account numberThe bank account number (for example, `87654321`)
When collecting a Direct Debit Request, follow our [BECS Direct Debit
Terms](https://stripe.com/au-becs/legal) and as part of your checkout form:

- Display the exact terms of [Stripe’s DDR service
agreement](https://stripe.com/au-becs-dd-service-agreement/legal) either inline
on the form, or on a page linked from the form, and identifying it as the “DDR
service agreement.”
- Make sure the accepted DDR and its accompanying [DDR service
agreement](https://stripe.com/au-becs-dd-service-agreement/legal) can be shared
with your customer at all times, either as a printed or non-changeable
electronic copy (such as email). Stripe hosts this for you.
- Display the following standard authorization text for your customer to accept
the BECS DDR, where you replace *Rocketship Inc* with your company name. Their
acceptance authorizes you to initiate BECS Direct Debit payments from their bank
account.

#### Note

By providing your bank account details, you agree to this Direct Debit Request
and the [Direct Debit Request service
agreement](https://stripe.com/au-becs-dd-service-agreement/legal), and authorize
Stripe Payments Australia Pty Ltd ACN 160 180 343 Direct Debit User ID number
507156 (“Stripe”) to debit your account through the Bulk Electronic Clearing
System (BECS) on behalf of *Rocketship Inc* (the “Merchant”) for any amounts
separately communicated to you by the Merchant. You certify that you’re either
an account holder or an authorized signatory on the account listed above.

The details of the accepted mandate are generated when setting up a
[PaymentMethod](https://docs.stripe.com/payments/payment-methods) or confirming
a `PaymentIntent`. At all times, you should be able to share this mandate—the
accepted DDR and its accompanying DDR service agreement—with your customer,
either in print or as a non-changeable electronic copy (such as email). Stripe
hosts this for you under the `url` property of the `Mandate` object linked to
the `PaymentMethod`.

### Add and configure an Australia Bank Account Element

The Australia Bank Account Element will help you collect and validate both the
BSB number and the account number. It needs a place to live in your payment
form. Create empty DOM nodes (containers) with unique IDs in your payment form.
Additionally, your customer must read and accept the [Direct Debit Request
service agreement](https://stripe.com/au-becs-dd-service-agreement/legal).

```
<form action="/setup" method="post" id="setup-form">
 <div class="form-row inline">
 <div class="col">
 <label for="accountholder-name">
 Name
 </label>
 <input
 id="accountholder-name"
 name="accountholder-name"
 placeholder="John Smith"
 required
 />
 </div>
 <div class="col">
 <label for="email">
 Email Address
 </label>
 <input
 id="email"
 name="email"
 type="email"
 placeholder="john.smith@example.com"
 required
 />
 </div>
 </div>

 <div class="form-row">
 <!--
 Using a label with a for attribute that matches the ID of the
 Element container enables the Element to automatically gain focus
 when the customer clicks on the label.
 -->
 <label for="au-bank-account-element">
 Bank Account
 </label>
 <div id="au-bank-account-element">
 <!-- A Stripe Element will be inserted here. -->
 </div>
 </div>

 <!-- Used to display bank (branch) name associated with the entered BSB -->
 <div id="bank-name"></div>

 <!-- Used to display form errors. -->
 <div id="error-message" role="alert"></div>

 <!-- Display mandate acceptance text. -->
 <div class="col" id="mandate-acceptance">
By providing your bank account details, you agree to this Direct Debit Request
and the <a href="stripe.com/au-becs-dd-service-agreement/legal">Direct Debit
Request service agreement</a>,
 and authorise Stripe Payments Australia Pty Ltd ACN 160 180 343
 Direct Debit User ID number 507156 (“Stripe”) to debit your account
 through the Bulk Electronic Clearing System (BECS) on behalf of
 Rocket Rides (the "Merchant") for any amounts separately
 communicated to you by the Merchant. You certify that you are either
 an account holder or an authorised signatory on the account listed above.
 </div>
 
 <!-- Add the client_secret from the SetupIntent as a data attribute -->
<button id="submit-button" data-secret="{{CLIENT_SECRET}}">Set up BECS Direct
Debit</button>

</form>
```

When the form loads, you can [create an
instance](https://docs.stripe.com/js/elements_object/create_element?type=au_bank_account)
of the Australia Bank Account Element and mount it to the Element container:

```
// Custom styling can be passed to options when creating an Element
const style = {
 base: {
 color: '#32325d',
 fontSize: '16px',
 '::placeholder': {
 color: '#aab7c4'
 },
 ':-webkit-autofill': {
 color: '#32325d',
 },
 },
 invalid: {
 color: '#fa755a',
 iconColor: '#fa755a',
 ':-webkit-autofill': {
 color: '#fa755a',
 },
 }
};

const options = {
 style: style,
 disabled: false,
 hideIcon: false,
 iconStyle: "default", // or "solid"
}

// Create an instance of the auBankAccount Element.
const auBankAccount = elements.create('auBankAccount', options);

// Add an instance of the auBankAccount Element into
// the `au-bank-account-element` <div>.
auBankAccount.mount('#au-bank-account-element');
```

[Submit the payment method details to
StripeClient-side](https://docs.stripe.com/payments/au-becs-debit/set-up-payment#web-submit-payment-method)
Rather than sending the entire `SetupIntent` object to the client, use its
[client
secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret)
from [step
2](https://docs.stripe.com/payments/au-becs-debit/set-up-payment#web-create-setup-intent).
This is different from your API keys that authenticate Stripe API requests.

The client secret should be handled carefully because it can complete the setup.
Do not log it, embed it in URLs, or expose it to anyone but the customer.

HTML + JSReact
Use
[stripe.confirmAuBecsDebitSetup](https://docs.stripe.com/js/setup_intents/confirm_au_becs_debit_setup)
to complete the setup when the user submits the form. A successful setup returns
a `succeeded` value for the SetupIntent’s `status` property. If the setup isn’t
successful, inspect the returned `error` to determine the cause.

As
[customer](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-customer)
was set, the [PaymentMethod](https://docs.stripe.com/api/payment_methods) is
attached to the provided `Customer` object after a successful setup. At this
point, you can associate the ID of the `Customer` object with your internal
representation of a customer. This allows you to use the stored `PaymentMethod`
to collect future payments without prompting for your customer’s payment method
details.

```
const form = document.getElementById('setup-form');
const accountholderName = document.getElementById('accountholder-name');
const email = document.getElementById('email');
const submitButton = document.getElementById('submit-button');
const clientSecret = submitButton.dataset.secret;

form.addEventListener('submit', async (event) => {
 event.preventDefault();
 stripe.confirmAuBecsDebitSetup(
 clientSecret,
 {
 payment_method: {
 au_becs_debit: auBankAccount,
 billing_details: {
 name: accountholderName.value,
 email: email.value
 }
 }
 }
 );
});
```

After successfully confirming the `SetupIntent`, you should share the [mandate
URL](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-au_becs_debit-url)
from the [Mandate object](https://docs.stripe.com/api/mandates) with your
customer. We also recommend including the following details to your customer
when you confirm their mandate has been established:

- an explicit confirmation message that indicates a Direct Debit arrangement has
been set up
- the [business
name](https://docs.stripe.com/payments/au-becs-debit/set-up-payment#statement-descriptors)
that will appear on the customer’s bank statement whenever their account gets
debited
- the payment amount and schedule (if applicable)
- a link to the generated DDR mandate URL

The `Mandate` object’s ID is accessible from the `mandate` on the SetupIntent
object, which is sent as part of the `setup_intent.succeeded` event sent after
confirmation, but can also be [retrieved through the
API](https://docs.stripe.com/api/setup_intents/retrieve).

```
curl https://api.stripe.com/v1/setup_intents/{{SETUP_INTENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=mandate
```

[Test the
integration](https://docs.stripe.com/payments/au-becs-debit/set-up-payment#web-test-integration)
You can test your form using the test BSB number `000-000` and one of the test
account numbers below with your
[confirmAuBecsDebitSetup](https://docs.stripe.com/js/setup_intents/confirm_au_becs_debit_setup)
request.

BSB NumberAccount NumberDescription`000-000``000123456`The PaymentIntent created
with the resulting PaymentMethod transitions from `processing` to `succeeded`.
The mandate status remains `active`.`000-000``900123456`The PaymentIntent
created with the resulting PaymentMethod transitions from `processing` to
`succeeded` (with a three-minute delay). The mandate status remains
`active`.`000-000``111111113`The PaymentIntent created with the resulting
PaymentMethod transitions from `processing` to `requires_payment_method` with an
`account_closed` failure code. The mandate status becomes `inactive` at that
point.`000-000``111111116`The PaymentIntent created with the resulting
PaymentMethod transitions from `processing` to `requires_payment_method` with a
`no_account` failure code. The mandate status becomes `inactive` at that
point.`000-000``222222227`The PaymentIntent created with the resulting
PaymentMethod transitions from `processing` to `requires_payment_method` with a
`refer_to_customer` failure code. The mandate status remains
`active`.`000-000``922222227`The PaymentIntent created with the resulting
PaymentMethod transitions from `processing` to `requires_payment_method` with a
`refer_to_customer` failure code (with a three-minute delay). The mandate status
remains `active`.`000-000``333333335`The PaymentIntent created with the
resulting PaymentMethod transitions from `processing` to
`requires_payment_method` with a `debit_not_authorized` failure code. The
mandate status becomes `inactive` at that point.`000-000``666666660`The
PaymentIntent created with the resulting PaymentMethod transitions from
`processing` to `succeeded`, but a dispute is immediately
created.`000-000``343434343`The PaymentIntent that was created with the
resulting PaymentMethod fails with a `charge_exceeds_source_limit` error due to
the payment amount causing the account to exceed its weekly payment volume
limit.`000-000``121212121`The PaymentIntent that was created with the resulting
PaymentMethod fails with a `charge_exceeds_transaction_limit` error due to the
payment amount exceeding the account’s transaction volume
limit.[OptionalValidate the Australia Bank Account
ElementClient-side](https://docs.stripe.com/payments/au-becs-debit/set-up-payment#web-validate-element)[OptionalAccepting
future
paymentsClient-side](https://docs.stripe.com/payments/au-becs-debit/set-up-payment#web-future-payments)
## See also

- [Accept an Australia BECS Direct Debit
payment](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment)
- [Connect payments](https://docs.stripe.com/connect/charges)

## Links

- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [Setup Intents API](https://docs.stripe.com/payments/setup-intents)
- [Start a free trial for a
subscription](https://docs.stripe.com/billing/subscriptions/trials)
- [Register now](https://dashboard.stripe.com/register)
- [Customer](https://docs.stripe.com/api/customers)
- [SetupIntent](https://docs.stripe.com/api/setup_intents)
-
[payment_method_types](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_types)
- [id](https://docs.stripe.com/api/customers/object#customer_object-id)
- [Enable it](https://docs.stripe.com/security/guide#tls)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [Elements](https://docs.stripe.com/js#stripe-elements)
- [BECS Direct Debit Terms](https://stripe.com/au-becs/legal)
- [Stripe’s DDR service
agreement](https://stripe.com/au-becs-dd-service-agreement/legal)
- [PaymentMethod](https://docs.stripe.com/payments/payment-methods)
- [create an
instance](https://docs.stripe.com/js/elements_object/create_element?type=au_bank_account)
- [client
secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret)
-
[stripe.confirmAuBecsDebitSetup](https://docs.stripe.com/js/setup_intents/confirm_au_becs_debit_setup)
-
[customer](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-customer)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [mandate
URL](https://docs.stripe.com/api/mandates/object#mandate_object-payment_method_details-au_becs_debit-url)
- [Mandate object](https://docs.stripe.com/api/mandates)
- [retrieved through the
API](https://docs.stripe.com/api/setup_intents/retrieve)
- [Accept an Australia BECS Direct Debit
payment](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment)
- [Connect payments](https://docs.stripe.com/connect/charges)