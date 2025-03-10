# Address Element

## Use the Address Element to collect complete billing and shipping addresses.

The Address Element is an embeddable UI component for accepting complete
addresses. Use it to collect shipping addresses, or when you need a complete
billing address, such as for tax purposes.

ThemeDefaultSizeDesktopCustomer LocationUnited StatesPhone
numberAutocompleteContactsOptionDescriptionThemeUse the dropdown to choose a
theme or customize the theme with the [Elements Appearance
API](https://docs.stripe.com/elements/appearance-api).Desktop and mobile sizeUse
the dropdown to set the max pixel width of the parent element that the Address
Element is mounted to. You can set it to 750px (Desktop) or 320px
(Mobile).Customer locationUse the dropdown to choose a location for accepting
complete addresses. Changing the location localizes the UI language and displays
locally relevant payment methods.Phone numberEnable this option to allow phone
number collection when the address form is expanded or using a
contact.AutocompleteEnable this option to decrease checkout time, reduce
validation errors, and increase checkout conversion with built-in address
autocomplete. Stripe supports 236 regional address formats, including
right-to-left address formats.ContactsEnable this option to add a new address or
change an existing address or phone number.
## Start with examples

To see the Address Element in action, start with one of these examples:

[Collect customer addressesCode and instructions for saving an address using the
Address
Element.](https://docs.stripe.com/elements/address-element/collect-addresses?platform=react-native)[Clone
a sample app on GitHubHTML · React](https://github.com/stripe-samples/link)
## Create an Address Element

When you create an Address Element, specify whether to use it in shipping or
billing mode.

Shipping modeBilling mode
In shipping mode, the element does two things:

- Collect a shipping address.
- Offer the customer the option to use it as a billing address too.

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const appearance = { /* appearance */ };
const options = { mode: 'shipping' };
const elements = stripe.elements({ clientSecret, appearance });
const addressElement = elements.create('address', options);
addressElement.mount('#address-element');
```

### Use Address Element with other elements

You can collect both shipping and billing addresses by using multiple Address
Elements, one of each mode, on your page.

If you need to collect both shipping and billing addresses and only want to use
one Address Element, use the Address Element in Shipping mode and use the
[Payment Element](https://docs.stripe.com/payments/payment-element) to collect
only the necessary billing address details.

When you use the Address Element with other elements, you can expect some
automatic behavior when confirming the PaymentIntent or SetupIntent. The Address
Element validates completeness upon confirming the PaymentIntent or SetupIntent
and then displays errors for each field if there are any validation errors.

## Use an address

The Address Element automatically works with the
[Payment](https://docs.stripe.com/payments/payment-element) or Express Checkout
Element. When a customer provides an address and a payment method, Stripe
combines them into a single
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) with the
address in the correct field.

### Automatic behavior

The element’s default behavior depends on its mode.

Shipping modeBilling mode
In shipping mode, the address is stored in these fields:

- It appears in the
[shipping](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-shipping)
field.
- If the customer indicates it is also the billing address, it also appears in
the
[billing_details](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_data-billing_details)
field.

To enable combining information, create all elements from the same `Elements`
object, as in this example:

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const appearance = { /* appearance */ };
const options = { mode: 'shipping' };
const paymentElementOptions = { layout: 'accordion'};
const elements = stripe.elements({ clientSecret });
const addressElement = elements.create('address', options);
const paymentElement = elements.create('payment', paymentElementOptions);
addressElement.mount('#address-element');
paymentElement.mount('#payment-element');
```

### Custom behavior

Normally, the Address Element’s default behavior is enough. But in a complex
payment flow, you might need to write custom responses to the customer’s input.
For information, see [Listen for address
input](https://docs.stripe.com/elements/address-element/collect-addresses).

## Autocomplete

The Address Element can autocomplete addresses for 25 countries. If your
customer selects a supported country for their address, then they see the
autocomplete options. These are the supported countries for autocomplete:

AustraliaBelgiumBrazilCanadaFranceGermanyIndiaIrelandItalyJapanMalaysiaMexicoNetherlandsNorwayPhilippinesPolandRussiaSingaporeSouth
AfricaSpainSwedenSwitzerlandTurkeyUnited KingdomUnited States
If you use the Address Element and the Payment Element together, Stripe enables
autocomplete with no configuration required. This is done using a
Stripe-provided Google Maps API key.

#### Note

By using autocomplete, you agree to comply with the [Google Maps Platform
Acceptable Use Policy](https://cloud.google.com/maps-platform/terms/aup). If you
violate this policy, we might disable autocomplete, or take any other action as
necessary.

If you use the Address Element alone, you must use your own [Google Maps API
Places Library
key](https://developers.google.com/maps/documentation/javascript/places), which
is managed separately from your Stripe account. Pass the key in the
[autocomplete.apiKey](https://docs.stripe.com/js/elements_object/create_address_element#address_element_create-options-autocomplete-apiKey)
option.

## Autofill with Link

[Link](https://docs.stripe.com/payments/link) saves and autofills payment and
shipping information for the options you’ve enabled. For example, if the Link
customer has a saved phone number, Stripe autofills the phone number only if
phone number collection is enabled. When a returning Link customer
authenticates, Stripe autofills their shipping information in the Address
element.

![Create a payment form using multiple
Elements](https://b.stripecdn.com/docs-statics-srv/assets/link-with-elements.f60af275f69b6e6e73c766d1f9928457.png)

Create a payment form using multiple Elements

To enable autofill, create all elements from the same `Elements` object, as in
this example:

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const appearance = { /* appearance */ };
const options = { mode: 'shipping' };
const paymentElementOptions = { layout: 'accordion'};
const elements = stripe.elements({ clientSecret });
const linkAuthElement = elements.create('linkAuthentication');
const addressElement = elements.create('address', options);
const paymentElement = elements.create('payment', paymentElementOptions);
linkAuthElement.mount('#link-auth-element');
addressElement.mount('#address-element');
paymentElement.mount('#payment-element');
```

## Appearance

You can use the Appearance API to control the style of all elements. Choose a
theme or update specific details.

![Examples of light and dark modes for the address
element.](https://b.stripecdn.com/docs-statics-srv/assets/address_appearance_example.c7884ea763b05e5881d65ed2b2afadbc.png)

For instance, choose the “flat” theme and override the primary text color.

```
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const appearance = {
 theme: 'flat',
 variables: { colorPrimaryText: '#262626' }
};
```

See all 10 lines
See the [Appearance API](https://docs.stripe.com/elements/appearance-api)
documentation for a full list of themes and variables.

## Links

- [Elements Appearance API](https://docs.stripe.com/elements/appearance-api)
- [Collect customer addressesCode and instructions for saving an address using
the Address
Element.](https://docs.stripe.com/elements/address-element/collect-addresses?platform=react-native)
- [Clone a sample app on GitHubHTML ·
React](https://github.com/stripe-samples/link)
- [View full
sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
-
[shipping](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-shipping)
-
[billing_details](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_data-billing_details)
- [Listen for address
input](https://docs.stripe.com/elements/address-element/collect-addresses)
- [Google Maps Platform Acceptable Use
Policy](https://cloud.google.com/maps-platform/terms/aup)
- [Google Maps API Places Library
key](https://developers.google.com/maps/documentation/javascript/places)
-
[autocomplete.apiKey](https://docs.stripe.com/js/elements_object/create_address_element#address_element_create-options-autocomplete-apiKey)
- [Link](https://docs.stripe.com/payments/link)
- [View full
sample](https://github.com/stripe-samples/link/blob/main/client/html/index.js)