# Set payment methods per-subscription

## Learn how to specify which payment methods are available for a subscription.

The subscription
[payment_settings](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings)
parameter lets you set specific payment methods on individual subscriptions.
This allows more flexibility than a single `default_payment_method` or less
granular customer settings.

To enable payment methods, you first need to activate them in your [account
settings](https://dashboard.stripe.com/settings/payment_methods) in the Stripe
Dashboard.

In some situations, there might be restrictions that prevent certain payment
methods from being used for a subscription. For example, a payment method might
only operate in one currency, or have limitations on the amount that a customer
can pay. Stripe doesn’t automatically select a payment method if limitations
prevent it from being used. Learn more about [payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support).

## Manually select payment methods

You can override the payment methods that a customer can use to pay a
subscription by changing its [payment
settings](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings).

```
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "payment_settings[payment_method_types][]"=card \
 -d "payment_settings[payment_method_types][]"=customer_balance
```

If you configured a default payment method on either the
[Customer](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
or the
[Subscription](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method),
be sure to include it in the list of `payment_method_types`. Otherwise, that
method won’t be used and payment might fail.

## Payment method priority

By default, customers can pay a subscription’s generated
[invoice](https://docs.stripe.com/api/invoices) with any of the enabled payment
methods in your [Invoice default payment method
configuration](https://dashboard.stripe.com/settings/billing/invoice). This
takes precedence over the older
[default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source)
customer setting.

If set, a subscription’s `payment_settings.payment_method_types` takes priority
over default invoice settings, but only for that specific subscription. Payment
method types are passed onto the subscription’s [setup
intent](https://docs.stripe.com/api/setup_intents) and invoices.

You can further specify a subscription’s `default_payment_method`, or the older
`default_source`, to prioritize which payment method is attempted.

## Payment method errors

Payment method errors can prevent a subscription from being created. This can
happen when:

- You manually select a payment method but a restriction, such as supported
currencies, prevents it from being used.
- A payment method isn’t activated for your account

Errors can also occur at time of payment, and Stripe can’t finalize the invoice.
See invoicing [payment method
errors](https://docs.stripe.com/invoicing/payment-methods#payment-method-errors)
for details.

### Payment method options

Some payment methods have additional options that you can set to customize how a
customer pays. See the [payment method
options](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings)
documentation for details.

## Links

-
[payment_settings](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings)
- [account settings](https://dashboard.stripe.com/settings/payment_methods)
- [payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support)
-
[Customer](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
-
[Subscription](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
- [invoice](https://docs.stripe.com/api/invoices)
- [Invoice default payment method
configuration](https://dashboard.stripe.com/settings/billing/invoice)
-
[default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source)
- [setup intent](https://docs.stripe.com/api/setup_intents)
- [payment method
errors](https://docs.stripe.com/invoicing/payment-methods#payment-method-errors)