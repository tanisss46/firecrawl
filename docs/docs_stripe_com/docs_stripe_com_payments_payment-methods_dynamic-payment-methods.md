# Dynamic payment methods

## Simplify your payment methods code by dynamically ordering and displaying payment methods.

Dynamic payment methods is part of the [default Stripe
integration](https://stripe.com/blog/dynamic-payment-methods) and enables you to
configure payment methods settings from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods)—no code
required. When you use dynamic payment methods in a [Payment
Element](https://docs.stripe.com/payments/payment-element) or
[Checkout](https://docs.stripe.com/payments/checkout) integration, Stripe
handles the logic for dynamically displaying the most relevant eligible payment
methods to each customer to maximize conversion. Dynamic payment methods also
unlocks [customization
features](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods#customization-features)
to help you customize and experiment with payment methods.

Use dynamic payment methods to:

- Turn on and manage most payment methods in the Dashboard
- Eliminate the need to specify eligibility requirements for individual payment
methods
- Dynamically order eligible payment methods to maximize conversion based on
factors such as customer device, location, and local currency
- Set rules when payment methods are shown to buyers
- Run A/B Tests for new payment methods before rolling them out to buyers

## Integration options

Use
[Checkout](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
or [Payment
Element](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements)
with dynamic payment methods to have Stripe handle the logic for displaying
eligible payment methods in your frontend for each transaction. If you have a
platform account, follow our [Connect
integration](https://docs.stripe.com/connect/dynamic-payment-methods).

### Migrate to dynamic payment methods

## Dashboard-based customization features

Access the following features with dynamic payment methods to control how and
when payment methods render.

FeatureDescription[Payment method
rules](https://docs.stripe.com/payments/payment-method-rules)Customize how you
display payment methods by setting targeting parameters based on amount or the
buyer’s location.[A/B test payment
methods](https://docs.stripe.com/payments/a-b-testing)Turn on payment methods
for a percentage of traffic, run an experiment, and see the resulting impact on
conversion rate, average order value, and shift in volume from other payment
methods.[Payment method
configurations](https://docs.stripe.com/payments/payment-method-configurations)Create
different sets of payment methods for different checkout scenarios using complex
logic, such as only showing specific payment methods for one-time purchases and
another set for recurring purchases.[Embed the Payment methods settings
component](https://docs.stripe.com/connect/embed-payment-method-settings)Embed a
payment method settings page directly into your website to allow your users to
manage their payment methods.
## How dynamic payment methods work

Review this section to understand the criteria that Stripe uses to automatically
determine eligible payment methods. If a specific payment method isn’t appearing
in your payment flow, one or more of these criteria might not be met.

Stripe applies all these criteria when creating the payment, except for the
customer’s country, which applies when the customer goes to the payment page.

### Dashboard settings

View the available payment methods in your [Stripe
Dashboard](https://dashboard.stripe.com/test/settings/payment_methods). Only
payment methods that you enabled can be shown to your customers.

If a payment method isn’t listed in your Dashboard settings, it’s either not
supported by Stripe or not supported in the country where your account is
registered. For example, PayNow is only available to Stripe accounts in
Singapore.

Learn more about [country
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#country-currency-support).

#### Note

When using Stripe Connect with Direct Charges or `on_behalf_of`, the settings of
the connected account determines the available payment methods. You can
configure them in your [connect
settings](https://dashboard.stripe.com/test/settings/payment_methods/connected_accounts).

### Product support

Several Stripe products allow you to charge customers, such as Checkout Sessions
and Payment Element. Not all payment methods are available in all products. For
example, Bacs Direct Debit isn’t available in the Mobile Payment Element. Some
payment methods, such as Swish, don’t support recurring payments.

Learn more about [product
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support).

### Presentment currency

Stripe supports over [135 presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies), but most
payment methods only support a subset of these. For example, ACH Direct Debit is
only available for payments in USD currency.

Learn more about [currency
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#country-currency-support).

### Charge amount

On top of the general [minimum and maximum
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
Stripe supports, some payment methods have their own minimum and maximum. For
example, SEPA Direct Debit is only available for payments below 10,000 EUR.

#### Note

The final amount, including tax and discounts, is the amount used to determine
available payment methods.

To learn more, go to the a payment method’s overview page.

### API support

Some payment methods, such as TWINT, can’t be set up for future usage. When you
set `setup_future_usage`, some payment methods are automatically filtered out.

Similarly, some payment methods, such as iDEAL, don’t support [manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method).
When you set `capture_method: manual`, some payment methods are automatically
filtered out.

Learn more about [API
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#additional-api-supportability).

### Customer’s country

A customer’s country impacts which payment methods are available on the payment
page, because most payment methods are available in a predefined number of
countries. For example, BLIK is only available for customers in Poland.

Learn more about [country
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#country-currency-support).

### Other considerations

The following features can also impact the availability of some payment methods:

- [Payment method
configuration](https://docs.stripe.com/payments/payment-method-configurations),
to customize the payment method shown.
- [Payment method rules](https://docs.stripe.com/payments/payment-method-rules),
to show or hide a payment method based on conditions, such as the amount and
currencies.
- [A/B testing](https://docs.stripe.com/payments/a-b-testing), to temporarily
show or hide a payment method to see its impact on conversion rates.

## Links

- [default Stripe integration](https://stripe.com/blog/dynamic-payment-methods)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [customization
features](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods#customization-features)
-
[Checkout](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [Payment
Element](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements)
- [Connect integration](https://docs.stripe.com/connect/dynamic-payment-methods)
- [Payment method rules](https://docs.stripe.com/payments/payment-method-rules)
- [A/B test payment methods](https://docs.stripe.com/payments/a-b-testing)
- [Payment method
configurations](https://docs.stripe.com/payments/payment-method-configurations)
- [Embed the Payment methods settings
component](https://docs.stripe.com/connect/embed-payment-method-settings)
- [different criteria](https://docs.stripe.com/testing/wallets)
- [Stripe Dashboard](https://dashboard.stripe.com/test/settings/payment_methods)
- [country
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#country-currency-support)
- [connect
settings](https://dashboard.stripe.com/test/settings/payment_methods/connected_accounts)
- [product
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support)
- [135 presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies)
- [minimum and maximum
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
- [manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [API
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#additional-api-supportability)