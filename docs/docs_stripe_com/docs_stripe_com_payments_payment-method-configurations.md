# Payment method configurations

## Create different sets of payment methods to display to customers based on specific checkout scenarios.

Payment method configurations allows [dynamic payment
method](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
users to display different sets of payment methods to customers for specific
checkout scenarios.

You can create a configuration to:

- Display a unique set of payment methods for certain products
- Enable a set of payment methods for your one-time payment checkout flow and a
different set of payment methods for your subscription checkout flow
- Connect Offer connected accounts access to additional payment methods for a
different subscription fee

After you create a payment method configuration, you can toggle each payment
method on or off for a given scenario directly in Dashboard—no code required.
Then at checkout, select which configuration you want to use. Stripe ranks the
payment methods that are enabled within that configuration to optimize for
conversion.

## Before you begin

- You must use either the Stripe [Payment
Element](https://docs.stripe.com/payments/payment-element) or
[Checkout](https://docs.stripe.com/payments/checkout).
- You must use [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
to enable additional payment methods from the Stripe Dashboard, which won’t
require any code changes.- To set up dynamic payment methods for direct users,
see the [payment method
integration](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
guide.
- Connect To set up dynamic payment methods for Connect platforms, see
[Upgrading to dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods).
[Create a payment method
configuration](https://docs.stripe.com/payments/payment-method-configurations#create-payment-method-configuration)
By default, you have one payment method configuration called **Default Config**.
You can create additional payment method configurations using both the Stripe
Dashboard and the API.

DashboardAPI- In your Dashboard, go to [Payment methods
settings](https://dashboard.stripe.com/test/settings/payment_methods).
- In the **Configuration Management** section, click the overflow menu (), then
select **Create a configuration**.
- Give your new configuration a name.
- Click **Save configuration**.

![Payment method configuration
page](https://b.stripecdn.com/docs-statics-srv/assets/payment-method-configurations.a766550ad4dd95854a7a9b9f178e1d45.png)

The page displays your new configuration. All payment methods are initially
disabled by default.

To switch between configurations, use the **Select configuration** dropdown near
the top of the page.

[Enable payment
methods](https://docs.stripe.com/payments/payment-method-configurations#enable-payment-methods)
In the Dashboard, open the configuration and turn on the payment methods that
you want to make available to buyers when using that configuration. A buyer sees
only payment methods that are turned on and compatible with the payment location
and currency.

#### Note

Some payment methods don’t show edit controls until you expand them.

[Display available payment methods in
checkout](https://docs.stripe.com/payments/payment-method-configurations#section-4)
 the `configuration ID` in the Dashboard from the configuration you want to
use in your checkout flow.

If you’re using the [deferred intent creation integration
path](https://docs.stripe.com/payments/accept-a-payment-deferred), pass the
`payment_method_configuration` ID when you create your Payment Element
component. The Payment Element automatically pulls the payment methods
associated with that configuration and ranks them to best convert buyers.

WebiOSAndroid
```
const options = {
 mode: 'payment',
 amount: 1099,
 currency: 'usd',
 payment_method_configuration: 'pmc_234'
}
```

If you aren’t using a Payment Element, pass the `payment_method_configuration`
ID when you [create a Checkout
session](https://docs.stripe.com/api/checkout/sessions/create).

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d currency=usd \
 -d payment_method_configuration=pmc_234
```

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn
individual payment methods on or off in the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout,
Stripe evaluates the currency and any restrictions, then dynamically presents
the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or
set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). By default,
Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe
filters them out even when they’re enabled. We filter Google Pay if you [enable
automatic tax](https://docs.stripe.com/tax/checkout) without collecting a
shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple
Pay or Google Pay. Stripe handles these payments the same way as other card
payments.

[Create a PaymentIntent with the
configuration](https://docs.stripe.com/payments/payment-method-configurations#create-payment-intent)
Create a PaymentIntent on your server using the payment method configuration.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d "automatic_payment_methods[enabled]"=true \
 -d payment_method_configuration=pmc_123
```

In the latest version of the API, the `automatic_payment_methods` parameter is
optional because it’s enabled by default.

## Links

- [dynamic payment
method](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Upgrading to dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods)
- [Payment methods
settings](https://dashboard.stripe.com/test/settings/payment_methods)
- [deferred intent creation integration
path](https://docs.stripe.com/payments/accept-a-payment-deferred)
- [create a Checkout
session](https://docs.stripe.com/api/checkout/sessions/create)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [enable automatic tax](https://docs.stripe.com/tax/checkout)