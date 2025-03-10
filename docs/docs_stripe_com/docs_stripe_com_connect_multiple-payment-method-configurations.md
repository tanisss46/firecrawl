# Multiple configurations for your Connect accounts

## Learn how to allow your connected accounts to display different sets of payment methods to their buyers in different scenarios.

Use this feature if your platform is using [dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods) and supports
setting different types of payment methods for different types of transactions
(for example, subscriptions versus one-time checkout) or for different invoice
amounts (for example, invoices more than a certain dollar amount can be paid
using BNPL).

[Create a new payment method
configurationDashboard](https://docs.stripe.com/connect/multiple-payment-method-configurations#create-payment-method-configuration)
Navigate to the [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods/connected_accounts)
for your connected accounts in the Stripe Dashboard. This is where you control
your platform level “parent” configurations. Your connected accounts receive a
“child” configuration for each parent that they can customize within the
constraints you set below.

You start with one parent configuration by default. To create an additional
configuration, click **Add new configuration**, and give it a name.

![Payment method configuration
page](https://b.stripecdn.com/docs-statics-srv/assets/ppc-dashboard-demo-connect.93d78670fd3582900915ab57e3e219ec.png)

[Set the default state for each payment
methodDashboard](https://docs.stripe.com/connect/multiple-payment-method-configurations#set-payment-method-default-state)
You can apply the default setting for each payment method to your new parent
configuration, and control what customizations your connected accounts can make.
Use the dropdown to select the desired setting:

- **On by default** the payment method is on by default. Connected accounts can
turn it on and off.
- **Off by default** the payment method is off by default. Connected accounts
can turn it on and off.
- **Blocked** turns the payment method off for all connected accounts. Connected
accounts can’t turn it on.

![Configure settings for each payment
method](https://b.stripecdn.com/docs-statics-srv/assets/settings-api-wallets.956b27fd0756e064d433aaa5999130fe.png)

[Allow your connected accounts to customize their payment
methods](https://docs.stripe.com/connect/multiple-payment-method-configurations#allow-payment-method-customization)
Connected accounts with access to the full Stripe Dashboard can turn payment
methods on or off if the payment method has been set to either `On by default`
or `Off by default`. Your connected accounts see the newly created child
configuration in their **Payment methods** settings. Your connected accounts can
use the dropdown menu at the top of the page to choose a configuration to edit.

If you want your connected accounts to customize their **Payment methods**
settings from your platform dashboard instead of the Stripe Dashboard, or if you
have connected accounts who don’t have Stripe Dashboard access, you can
integrate with the Payment Method Configurations API.

Use the Payment Method Configurations API with the connected account ID and
child configuration ID to read the current state of a payment method for a
specific connected account on that configuration.

```
curl
https://api.stripe.com/v1/payment_method_configurations/{{PAYMENT_METHOD_CONFIGURATION_ID}}
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

```
{
 "object": "list",
 "data": [
 {
 "id": "{{PAYMENT_METHOD_CONFIGURATION_ID}}",
 "object": "payment_method_configuration",
 "name": "My Custom Configuration",
 "active": true,
 "is_default": true,
 "livemode": false,
 "parent": "{{PAYMENT_METHOD_CONFIGURATION_ID}}",
 "acss_debit": {
 "available": false,
 "display_preference": {
 "overridable": true,
 "preference": "off",
 "value": "off"
 }
 },
 "affirm": {
 "available": false,
 "display_preference": {
 "overridable": true,
 "preference": "off",
 "value": "off"
 }
 },
 "afterpay_clearpay": {
 "available": false,
 "display_preference": {
 "overridable": true,
 "preference": "off",
 "value": "off"
 }
 },
 ... additional payment methods
 }
 ],
 "has_more": false,
 "url": "/v1/payment_method_configurations"
}
```

If successful, the return list displays each payment method and includes two
parameters outlining availability and display preference.

- `available` is the combination of
[capability](https://docs.stripe.com/api/capabilities/object) value (`active`,
`inactive`, `pending`, or `unrequested`) and `display_preference` value.

You can use the `available` field to know whether or not a buyer sees this
payment method at checkout time. If `available` is `true`, that payment method’s
capability is active and `display_preference` is on. If `available` is `false`,
the payment method either doesn’t have an active capability or the
`display_preference` value is off, and buyers won’t see it at checkout time. To
simplify your integration and take advantage of other features, use payment
methods that you manage from the Dashboard at checkout, which automatically
reads this parameter and shows the right payment methods to buyers.
- `display_preference` has three components: `overridable`, `preference`, and
`value`.

- `overridable` is read-only, and indicates whether the connected account’s
preference can override the default set above.
- `preference` is writable, and stores the connected account’s preference.
- `value` is read-only, and reflects the effective `display_preference` value.

#### Note

Only payment methods that are relevant in the connected account’s country are
shown in the API response and are configurable. [Check country
support](https://docs.stripe.com/payments/payment-methods/integration-options).

When a connected account owner takes action to turn on or off a payment method,
you can update the `display_preference` `preference` attribute. This stores the
connected account owner’s preference for that payment method and is used to
determine whether buyers see the payment method.

```
curl
https://api.stripe.com/v1/payment_method_configurations/{{PAYMENT_METHOD_CONFIGURATION_ID}}
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "affirm[display_preference][preference]"=on
```

```
{
 "id": "{{PAYMENT_METHOD_CONFIGURATION_ID}}",
 "object": "payment_method_configuration",
 "name": "My Custom Configuration",
 "active": true,
 "is_default": true,
 "livemode": false,
 "acss_debit": {
 "available": false,
 "display_preference": {
 "overridable": true,
 "preference": "off",
 "value": "off"
 }
 },
 "affirm": {
 "available": true,
 "display_preference": {
 "overridable": true,
 "preference": "on",
 "value": "on"
 }
 },
 "afterpay_clearpay": {
 "available": false,
 "display_preference": {
 "overridable": true,
 "preference": "off",
 "value": "off"
 }
 },
 ... additional payment methods
}
```

When your connected accounts turn on payment methods with the API, Stripe
intelligently ranks the payment methods based on the buyer’s location, order
size, and other factors to always show the highest converting payment methods
first.

[Use the configuration in your checkout
flow](https://docs.stripe.com/connect/multiple-payment-method-configurations#use-payment-method-configuration)
Pass the parent configuration ID when rendering your checkout flow to use your
new configuration. Stripe automatically looks up the child configuration for the
associated connected account and uses their customized settings.

CheckoutPayment Element
```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d currency=usd \
 -d payment_method_configuration={{PAYMENT_METHOD_CONFIGURATION_ID}}
```

[OptionalApple Pay and Google
Pay](https://docs.stripe.com/connect/multiple-payment-method-configurations#apple-pay-google-pay)

## Links

- [dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods/connected_accounts)
- [capability](https://docs.stripe.com/api/capabilities/object)
- [Check country
support](https://docs.stripe.com/payments/payment-methods/integration-options)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)