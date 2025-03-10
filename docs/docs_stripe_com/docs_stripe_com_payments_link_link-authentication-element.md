# Explore the Link Authentication Element

## Create a single email input for both email collection and Link authentication.

Create a single email input for both email collection and Link authentication by
adding the [Link Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element)
to your Elements integration. If your customer doesn’t have a Link account, and
they select one of its supported payment methods (credit card, debit card, or US
bank), they’re given the option of signing up.

Alternatively, if your customer already has a Link account, it authenticates
them with a one-time-password, then automatically fills their payment details in
the Payment Element.

![Use the Link Authentication Element as part of your checkout
page](https://b.stripecdn.com/docs-statics-srv/assets/link-authentication-element.a5477f2043e29562f86d6de06f02e6b9.png)

Use the Link Authentication Element as part of your checkout page

## Add the Link Authentication Element

Put the Link Authentication Element at the beginning of the checkout page,
followed by the [Address
Element](https://docs.stripe.com/elements/address-element) (optional), then the
Payment Element. The following code
[creates](https://docs.stripe.com/js/elements_object/create_link_authentication_element)
an instance of the Link Authentication Element and
[mounts](https://docs.stripe.com/js/element/mount) it to the DOM:

HTML + JSReact
```
// Enable the skeleton loader UI for the optimal loading experience.
const loader = 'auto';

// Create an elements group from the Stripe instance passing in the clientSecret
and enabling the loader UI.
const elements = stripe.elements({clientSecret, loader});

// Create an instance of the Link Authentication Element optionally prefilling a
customer's email address.
const linkAuthenticationElement = elements.create("linkAuthentication",
{defaultValues: {email: "foo@bar.com"}});

// Passing in defaultValues is optional, but useful if you want to prefill
customer information to simplify the customer experience.
const paymentElement = elements.create('payment', {
 defaultValues: {
 billingDetails: {
 name: 'John Doe',
 phone: '888-888-8888',
```

See all 22 lines
`linkAuthenticationElement` renders an email address input. When Link matches a
customer email with an existing Link account, it sends the customer a secure,
one-time code to their phone to authenticate. If the customer successfully
authenticates, Stripe displays their Link-saved addresses and payment methods
automatically so they can use them. You also need to [register your
domain](https://docs.stripe.com/payments/payment-methods/pmd-registration).

## See also

- [Stripe Web Elements](https://docs.stripe.com/payments/elements)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Address Element](https://docs.stripe.com/elements/address-element)

## Links

- [pass them directly to the Payment
Element](https://docs.stripe.com/payments/link/payment-element-link?elements=pass-email)
- [Link Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element)
- [Address Element](https://docs.stripe.com/elements/address-element)
-
[creates](https://docs.stripe.com/js/elements_object/create_link_authentication_element)
- [mounts](https://docs.stripe.com/js/element/mount)
- [register your
domain](https://docs.stripe.com/payments/payment-methods/pmd-registration)
- [Stripe Web Elements](https://docs.stripe.com/payments/elements)
- [Payment Element](https://docs.stripe.com/payments/payment-element)