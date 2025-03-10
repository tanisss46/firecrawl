# Link in the Express Checkout Element

## Let customers check out faster with Link and the Express Checkout Element.

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

![Add Link to the Express Checkout
Element](https://b.stripecdn.com/docs-statics-srv/assets/link-in-express-checkout-element.67be6745e5a37c1c09074b0f43763cff.png)

Add Link to the Express Checkout Element

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

## See also

- [Stripe Web Elements](https://docs.stripe.com/payments/elements)
- [Link Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element)
- [Address Element](https://docs.stripe.com/elements/address-element)

## Links

- [Link](https://docs.stripe.com/payments/link)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Google Pay](https://docs.stripe.com/google-pay)
- [PayPal](https://docs.stripe.com/payments/paypal)
- [Amazon Pay](https://docs.stripe.com/payments/amazon-pay)
- [creates](https://docs.stripe.com/js/element/express_checkout_element)
- [mounts](https://docs.stripe.com/js/element/mount)
- [Stripe Web Elements](https://docs.stripe.com/payments/elements)
- [Link Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element)
- [Address Element](https://docs.stripe.com/elements/address-element)