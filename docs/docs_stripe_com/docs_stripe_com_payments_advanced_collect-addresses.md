# Collect physical addresses and phone numbers

## Learn how to collect addresses and phone numbers during one-time payment flows.

To collect complete addresses for billing or shipping, use the [Address
Element](https://docs.stripe.com/elements/address-element). You might need to
[collect a full billing address to calculate
taxes](https://docs.stripe.com/tax/custom#collect-address), for example. The
[Payment Element](https://docs.stripe.com/payments/payment-element) only
collects the billing address details required to complete the payment, but you
can configure it to collect other billing details.

Other reasons you might want to use the Address Element:

- To collect customer [phone
numbers](https://docs.stripe.com/js/elements_object/create_address_element#address_element_create-options-fields-phone)
- To enable
[autocomplete](https://docs.stripe.com/js/elements_object/create_address_element#address_element_create-options-autocomplete)
- To prefill billing information in the Payment Element by passing in a shipping
address

Stripe combines the collected address information and the payment method to
create a [PaymentIntent](https://docs.stripe.com/payments/payment-intents).

## Create an Address Element

When you create an Address Element, you specify either a `shipping` or `billing`
mode . The [Address Element
mode](https://docs.stripe.com/js/elements_object/create_address_element#address_element_create-options-mode)
determines whether the shipping or billing addressed is passed to confirm the
PaymentIntent.

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

## See also

- [Use the
address](https://docs.stripe.com/elements/address-element?platform=web#use-an-address)
- [Set up autofill with
Link](https://docs.stripe.com/elements/address-element?platform=web#autofill-with-link)
- [Customize the form’s
appearance](https://docs.stripe.com/elements/address-element?platform=web#appearance)

## Links

- [Address Element](https://docs.stripe.com/elements/address-element)
- [collect a full billing address to calculate
taxes](https://docs.stripe.com/tax/custom#collect-address)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [phone
numbers](https://docs.stripe.com/js/elements_object/create_address_element#address_element_create-options-fields-phone)
-
[autocomplete](https://docs.stripe.com/js/elements_object/create_address_element#address_element_create-options-autocomplete)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [Address Element
mode](https://docs.stripe.com/js/elements_object/create_address_element#address_element_create-options-mode)
- [View full
sample](https://github.com/stripe-samples/accept-a-payment/tree/main/payment-element)
- [Use the
address](https://docs.stripe.com/elements/address-element?platform=web#use-an-address)
- [Set up autofill with
Link](https://docs.stripe.com/elements/address-element?platform=web#autofill-with-link)
- [Customize the form’s
appearance](https://docs.stripe.com/elements/address-element?platform=web#appearance)