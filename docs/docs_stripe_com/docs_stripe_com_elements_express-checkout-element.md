# Express Checkout Element

## Show multiple one-click payment buttons with a single component.

![Checkout UX showing Apple Pay, Link, and PayPal
buttons](https://b.stripecdn.com/docs-statics-srv/assets/link-in-express-checkout-element.67be6745e5a37c1c09074b0f43763cff.png)

The Express Checkout Element gives you a single integration for accepting
payments through one-click payment buttons. Supported payment methods include
[Link](https://docs.stripe.com/payments/link), [Apple
Pay](https://docs.stripe.com/apple-pay), [Google
Pay](https://docs.stripe.com/google-pay),
[PayPal](https://docs.stripe.com/payments/paypal), and [Amazon
Pay](https://docs.stripe.com/payments/amazon-pay).

With this integration, you can:

- Dynamically sort payment buttons based on a customer’s location.
- Add payment buttons without any frontend changes.
- Integrate Elements seamlessly by reusing an existing Elements instance to save
time.

#### Klarna on the Express Checkout Element

Klarna on the Express Checkout Element is currently in private preview with
limited availability. Reach out here to request access.

## Try the demo

In the following demo, you can toggle some of the prebuilt options to change the
background color, layout, size, and shipping address collection of the payment
interface. The demo displays Google Pay and Apple Pay only on their available
platforms. Payment Method buttons are only shown in their supported countries.

Merchant CountryUnited StatesBackground ColorLightSizeDesktopMax ColumnsMax
ColumnsMax RowsMax RowsOverflowCollect Shipping AddressThe Express Checkout
Element displays multiple buttons at the same time in the order that maximizes
payment conversion on your page. The demo sets the
[wallets](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-wallets)
parameter to 'always' for all wallets. Google Pay and Apple Pay are displayed
only on their available platforms. Amazon Pay and Paypal are only displayed if
they are available in the selected business country.
If you don’t see the demo, try viewing this page in a [supported
browser](https://docs.stripe.com/elements/express-checkout-element#supported-browsers).

OptionDescriptionMerchant countrySet this using the [publishable
key](https://docs.stripe.com/keys#obtain-api-keys) that you use to [initialize
Stripe.js](https://docs.stripe.com/js/initializing). To change the country, you
must unmount the Express Checkout Element, update the publishable key, then
re-mount the Express Checkout Element.Background colorSet colors using the
[Elements Appearance API](https://docs.stripe.com/elements/appearance-api).
Button themes are inherited from the Appearance API but you can also [define
them directly when you create the
Element](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonTheme).Desktop
and mobile sizeUse the dropdown to set the max pixel width of the parent element
that the Express Checkout Element is mounted to. You can set it to 750px
(Desktop) or 320px (Mobile).Max columns and max rowsSet these values using the
[layout](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-layout)
parameter when you [Create the Express Checkout
Element](https://docs.stripe.com/js/elements_object/create_express_checkout_element).Overflow
menuSet this using the
[layout](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-layout)
parameter when you [Create the Express Checkout
Element](https://docs.stripe.com/js/elements_object/create_express_checkout_element).Collect
shipping addressTo collect shipping information, you must pass options when
[creating](https://docs.stripe.com/js/elements_object/create_express_checkout_element)
the Express Checkout Element. Learn more about [collecting customer details and
displaying line
items](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#handle-create-event).
## Start with a guide

[Add one-click wallets to your checkout pageBuild an integration with the
Express Checkout Element using the Checkout Sessions
API.](https://docs.stripe.com/checkout/one-click-payment-buttons)[Use one-click
wallets in advanced integrationsBuild an integration with the Express Checkout
Element using the Payment Intents
API.](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment)[Migrate
to the Express Checkout ElementMigrate from the Payment Request Button Element
to the web Express Checkout
Element.](https://docs.stripe.com/elements/express-checkout-element/migration)[View
the Stripe.js
reference](https://docs.stripe.com/js/element/express_checkout_element)
## Create an Express Checkout Element

This code [creates](https://docs.stripe.com/js/element/express_checkout_element)
an elements group with an Express Checkout Element and
[mounts](https://docs.stripe.com/js/element/mount) it to the DOM.

```
const appearance = { /* appearance */ }
const options = { /* options */ }
const elements = stripe.elements({
 mode: 'payment',
 amount: 1099,
 currency: 'usd',
 appearance,
})
const expressCheckoutElement = elements.create('expressCheckout', options)
expressCheckoutElement.mount('#express-checkout-element')
```

#### Note

Express Checkout Element dynamically resizes Payment Method buttons to fill
available space, but individual buttons can have different minimum widths
depending on the Payment Method. Be sure to test at different screen sizes,
especially if mounting Express Checkout Element in a narrow container.

## Payment methods

The Express Checkout Element presents one-click payment methods that are active,
supported, and set up.

- Some payment methods [require activation in the
Dashboard](https://dashboard.stripe.com/settings/payment_methods).
- Payment methods are only available when the customer uses a supported browser
and pays in a supported currency.
- Some payment methods require setup actions from the customer. For example, a
customer won’t see a Google Pay button if they don’t have Google Pay set up.

The element sorts payment methods by relevance to your customer.

To control these behaviors, you can [customize the payment
methods](https://docs.stripe.com/elements/express-checkout-element#customize-payment-methods).

## Supported browsers

Certain payment methods work with specific browsers.

Apple Pay Google Pay Link PayPal Amazon Pay Chrome1EdgeFirefoxOperaSafari2Chrome
on iOS 16+Firefox on iOS 16+Edge on iOS 16+
1Other chromium browsers might be supported. For more information, see
[supported browsers](https://docs.stripe.com/js/appendix/supported_browsers).

2When using an iframe, its origin must match the top-level origin (except for
Safari 17+ when specifying `allow="payment"` attribute). Two pages have the same
origin if the protocol, host (full domain name), and port (if specified) are the
same for both pages.

## Layout

By default, when the Express Checkout Element displays multiple buttons, it
arranges the buttons in a grid based on available space, and shows an overflow
menu if necessary.

You can override this default and specify a grid layout yourself with the
[layout](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-layout)
option.

## Text

You can control a button’s text by selecting a
[buttonType](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonType).
Each wallet offers its own types.

LinkApple PayGoogle PayPayPalAmazon Pay
Link only offers one button type, which presents the “Pay with Link” call to
action and the Link logo.

We attempt to detect your customer’s locale and use it to localize the button
text. You can also specify a
[locale](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-locale).

This example code includes the call to action “Buy” or “Buy now” for buttons
that support it. Then, it specifies the locale `de` to get their German
equivalents.

```
const expressCheckoutOptions = {
 buttonType: {
 applePay: 'buy',
 googlePay: 'buy',
 paypal: 'buynow',
 klarna: 'pay',
 }
}
const elements = stripe.elements({
 locale: 'de',
```

See all 19 lines
## Appearance

You can’t fully customize the appearance of Express Checkout Element buttons
because each payment method sets its own logo and brand colors. You can
customize the following options:

- [Button
height](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonHeight)
- Border radius using variables with the
[Appearance](https://docs.stripe.com/elements/appearance-api) API
- [Button
themes](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonTheme)

#### Note

The Apple Pay button automatically resizes when border radius increases beyond a
certain threshold. If modifying the default border radius, make sure to test it
with all active payment methods.

This example code sets up an elements group with a light theme and 36px border
radius, makes buttons 50px tall, and overrides the theme to use the
white-outline version of the Apple Pay button.

```
const appearance = {
 theme: 'stripe',
 variables: {
 borderRadius: '36px',
 }
}
const expressCheckoutOptions = {
 buttonHeight: 50,
 buttonTheme: {
```

See all 23 lines
We support the following themes:

LinkPayPalApple PayGoogle PayAmazon Pay
Link has a single button theme, which is readable on either a light or a dark
background.

## Customize payment methods

You can’t specify which payment methods to display. For example, you can’t force
a Google Pay button to appear if your customer’s device doesn’t support Google
Pay.

But you can customize payment method behavior in various ways, such as:

- You can activate or deactivate payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods).
- You can override Stripe’s default logic of sorting payment methods by
relevance. Use the
[paymentMethodOrder](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-paymentMethodOrder)
option to set your preferred order.
- If there is too little room in the layout, low-relevance payment methods might
appear in an overflow menu. Customize when the menu appears using the
[layout](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-layout)
option.
- To prevent Apple Pay or Google Pay from appearing, set
[paymentMethods.applePay](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-paymentMethods-applePay)
or
[paymentMethods.googlePay](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-paymentMethods-applePay)
to `never`.
- To allow Apple Pay or Google Pay to appear when they’re not set up, set
[paymentMethods.applePay](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-paymentMethods-applePay)
or
[paymentMethods.googlePay](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-paymentMethods-applePay)
to `always`. This still won’t force them to appear on unsupported platforms, or
when the payment is in an unsupported currency.

#### Regional considerationsFinlandSweden

Regulations in
[Finland](https://support.stripe.com/questions/payment-method-legislation-in-finland)
and
[Sweden](https://support.stripe.com/questions/payment-method-legislation-in-sweden)
require you to present debit payment methods first before showing credit payment
methods at checkout in these countries.

## Links

- [Link](https://docs.stripe.com/payments/link)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Google Pay](https://docs.stripe.com/google-pay)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [Amazon Pay](https://docs.stripe.com/payments/amazon-pay)
-
[wallets](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-wallets)
- [publishable key](https://docs.stripe.com/keys#obtain-api-keys)
- [initialize Stripe.js](https://docs.stripe.com/js/initializing)
- [Elements Appearance API](https://docs.stripe.com/elements/appearance-api)
- [define them directly when you create the
Element](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonTheme)
-
[layout](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-layout)
- [Create the Express Checkout
Element](https://docs.stripe.com/js/elements_object/create_express_checkout_element)
- [collecting customer details and displaying line
items](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment#handle-create-event)
- [Add one-click wallets to your checkout pageBuild an integration with the
Express Checkout Element using the Checkout Sessions
API.](https://docs.stripe.com/checkout/one-click-payment-buttons)
- [Use one-click wallets in advanced integrationsBuild an integration with the
Express Checkout Element using the Payment Intents
API.](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment)
- [Migrate to the Express Checkout ElementMigrate from the Payment Request
Button Element to the web Express Checkout
Element.](https://docs.stripe.com/elements/express-checkout-element/migration)
- [View the Stripe.js
reference](https://docs.stripe.com/js/element/express_checkout_element)
- [mounts](https://docs.stripe.com/js/element/mount)
- [require activation in the
Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [supported browsers](https://docs.stripe.com/js/appendix/supported_browsers)
-
[buttonType](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonType)
-
[locale](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-locale)
- [Button
height](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-buttonHeight)
-
[paymentMethodOrder](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-paymentMethodOrder)
-
[paymentMethods.applePay](https://docs.stripe.com/js/elements_object/create_express_checkout_element#express_checkout_element_create-options-paymentMethods-applePay)
-
[Finland](https://support.stripe.com/questions/payment-method-legislation-in-finland)
-
[Sweden](https://support.stripe.com/questions/payment-method-legislation-in-sweden)