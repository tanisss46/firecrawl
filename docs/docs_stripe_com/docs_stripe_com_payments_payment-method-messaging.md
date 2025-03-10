# Payment Method Messaging Element

## Automatically explain buy now, pay later payment options.

The Payment Method Messaging Element is a UI component for informing a customer
about available buy-now-pay-later plans. It automatically determines the
available plans and conditions, generates a localized description, and displays
it in your form’s theme.

![Prince of Persia
book](https://b.stripecdn.com/docs-statics-srv/assets/c2815bda1cf26cedf5b8603b4667acae.png)

The Making of Prince of Persia: Journals 1985-1993Jordan Mechner$99.00
## Create and mount the Payment Method Messaging Element

HTML + JSReact
Use Stripe Elements to include the [Payment Method
Messaging](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging)
Element on your site.

- Add the Stripe.js script on your page by adding it to the `head` of your HTML
file:

```
<script src="https://js.stripe.com/v3/"></script>
```
- Create a placeholder element in your page where you want to mount the Payment
Method Messaging Element:

```
<div id="payment-method-messaging-element"></div>
```
- On your product, cart, and payment pages, include the following code to create
an instance of Stripe.js ([with
locale](https://docs.stripe.com/js/appendix/supported_locales)) and mount the
Payment Method Messaging Element:

```
// Set your publishable key. Remember to change this to your live publishable
key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
const elements = stripe.elements();
const options = {
 amount: 9900, // $99.00 USD
 currency: 'USD',
 // the country that the end-buyer is in
 countryCode: 'US',
};
const PaymentMessageElement =
 elements.create('paymentMethodMessaging', options);
PaymentMessageElement.mount('#payment-method-messaging-element');
```

#### Caution

If your integration requires you to list payment methods manually, see
[Customize payment
methods](https://docs.stripe.com/payments/payment-method-messaging#customize-payment-methods).

[OptionalUse with Stripe
Connect](https://docs.stripe.com/payments/payment-method-messaging#connect)
## Dynamic display

The element dynamically displays payment plans that the customer is eligible
for. These depend on the customer’s location and currency. They also depend on
the amount of the payment, as in this example:

$0.99$99$1200
Some payment methods offer “pay now” in addition to “pay later” plans. If only a
“pay now” option is available, nothing is shown.

## Customize Payment Methods

If you use [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods),
the Payment Method Messaging Element automatically pulls your payment method
preferences from the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) to dynamically
show the most relevant payment methods to your customers. Alternatively, you can
list payment methods manually using
[paymentMethodTypes](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging#elements_create-options-paymentMethodTypes).
The Payment Method Messaging Element still only displays plans that the customer
is eligible for based on their location, the currency, and the amount of the
payment.

HTML + JSReact
```
// Set your publishable key. Remember to change this to your live publishable
key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
const elements = stripe.elements();
const options = {
 amount: 9900, // $99.00 USD
 currency: 'USD',
 paymentMethodTypes: ['klarna', 'afterpay_clearpay', 'affirm'],
 // the country that the end-buyer is in
 countryCode: 'US',
};
const PaymentMessageElement =
 elements.create('paymentMethodMessaging', options);
PaymentMessageElement.mount('#payment-method-messaging-element');
```

By default, the Payment Method Messaging Element uses a dynamic ordering that
optimizes payment method display for each user. Use the
[paymentMethodOrder](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging#elements_create-options-paymentMethodOrder)
option to set your preferred order.

## Info modal

When the customer selects the info icon (ⓘ), the Payment Method Messaging
Element displays a modal with details about buy now, pay later payment plans.

![The info
modal](https://b.stripecdn.com/docs-statics-srv/assets/pmme-learn-more.eb5802e4d0caeb5469ee11fcfbc26c09.png)

A preview of the info modal

The modal includes:

- A step-by-step overview of how to use a buy now, pay later payment method
- A summary of terms for each available payment plan
- A link to the full terms for each available payment plan

## Supported plans

The Payment Method Messaging Element supports these payment methods and payment
plans:

KlarnaAfterpayAffirm- Pay in 3
- Pay in 4
- Pay in 30 days
- Pay in 60 days
- Financing
- Pay now
- Pay in 4
- Interest-bearing loan installments
- Pay in 4
- 0% interest loan installments
- Interest-bearing loan installments

It supports these values for
[countryCode](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging#elements_create-options-countryCode):
`AT`, `AU`, `BE`, `CA`, `CH`, `CZ`, `DE`, `DK`, `ES`, `FI`, `FR`, `GB`, `GR`,
`IE`, `IT`, `NL`, `NO`, `NZ`, `PL`, `PT`, `RO`, `SE`, `US`.

It supports these values for
[currency](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging#elements_create-options-currency):
`AUD`, `CAD`, `CHF`, `CZK`, `DKK`, `EUR`, `GBP`, `NOK`, `NZD`, `PLN`, `SEK`,
`USD`.

#### Caution

Messaging does not render if the `countryCode` and `currency` combination passed
has no eligible payment plans.

## Appearance

Use the [Appearance API](https://docs.stripe.com/elements/appearance-api) to
customize the font and logo of your messaging. You can select a
[theme](https://docs.stripe.com/elements/appearance-api?platform=web#theme) as
in the example below.

FlatNightStripe
Use [variables](https://docs.stripe.com/elements/appearance-api#variables) and
[rules](https://docs.stripe.com/elements/appearance-api#rules) for additional
customization.

```
const appearance = {
 variables: {
 colorText: 'rgb(84, 51, 255)',
 colorTextSecondary: 'rgb(28, 198, 255)', // info icon color
 fontSizeBase: '16px',
 spacingUnit: '10px',
 fontWeightMedium: 'bolder',
 fontFamily: 'Ideal Sans, system-ui, sans-serif',
 },
 rules: {
 '.PaymentMethodMessaging': {
 textAlign: 'right',
 }
 }
};
```

See all 24 lines
## Disclose Stripe to your customers

Stripe collects information on customer interactions with Elements to provide
services to you, prevent fraud, and improve its services. This includes using
cookies and IP addresses to identify which Elements a customer saw during a
single checkout session. You’re responsible for disclosing and obtaining all
rights and consents necessary for Stripe to use data in these ways. For more
information, visit our [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe).

The Payment Method Messaging Element is a tool that allows you to message
various buy now, pay later payment options to your customers. You’re responsible
for compliance with applicable laws, rules, and regulations regarding the
promotion of buy now, pay later payment options.

## Links

- [Payment Method
Messaging](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [with locale](https://docs.stripe.com/js/appendix/supported_locales)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
-
[paymentMethodTypes](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging#elements_create-options-paymentMethodTypes)
-
[paymentMethodOrder](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging#elements_create-options-paymentMethodOrder)
-
[countryCode](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging#elements_create-options-countryCode)
-
[currency](https://docs.stripe.com/js/elements_object/create_element?type=paymentMethodMessaging#elements_create-options-currency)
- [Appearance API](https://docs.stripe.com/elements/appearance-api)
- [theme](https://docs.stripe.com/elements/appearance-api?platform=web#theme)
- [variables](https://docs.stripe.com/elements/appearance-api#variables)
- [rules](https://docs.stripe.com/elements/appearance-api#rules)
- [privacy
center](https://stripe.com/legal/privacy-center#as-a-business-user-what-notice-do-i-provide-to-my-end-customers-about-stripe)