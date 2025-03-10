# Payment Method Configurations API

## Learn how to use the Configurations API to give connected account owners more control over the payment methods they offer.

Use the Payment Method Configurations API to allow your connected account owners
to opt in or opt out of a payment method through your own settings page. You can
view which payment methods are enabled for connected accounts, market payment
methods, and set display preferences for relevant payment types.

You can either build your own payment method settings UI with the API or use the
embedded payment method settings component.

#### Private preview

The **embedded payment method settings component** allows connected accounts to
configure the payment methods they offer at checkout without the need to access
the Stripe Dashboard. [Request
access](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings#request-access)
and learn how to [integrate with Payment Method
Configurations](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings#integration).

[Set the platform level default
state](https://docs.stripe.com/connect/payment-method-configurations#section-1)
In the Stripe Dashboard, set the platform-level default for individual payment
methods in the [Manage payment methods for your connected
accounts](https://dashboard.stripe.com/test/settings/payment_methods/connected_accounts)
page to edit the default-enabled payment methods.

In the [Dashboard](https://dashboard.stripe.com/login), click the gear icon in
the top-right corner to open the **Product settings** page. Click the **Payment
methods** link in the **Payments** section.

![Settings option in the
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/settings-api-dashboard.01bd465492acb49ada30fdda9e9f5d08.png)

![Payment methods under Payments
settings](https://b.stripecdn.com/docs-statics-srv/assets/settings-api-payment-methods.7824d81ee28dd2775b73d556da33d82a.png)

As a platform, you can set payment method preferences for your platform and for
your connected accounts. The settings for **Your account** apply to your direct
payment traffic. For example, if you charge your users a monthly fee to use your
platform through your own checkout page, use the **Your Account** settings to
manage those payments.

The settings for **Your connected accounts** enable you to manage the payment
methods that the connected accounts on your platform can accept.

To set the default state for all connected accounts on your platform, click the
**Edit settings** link under **Your connected accounts**.

![Payment methods settings for your account and connected
accounts](https://b.stripecdn.com/docs-statics-srv/assets/settings-api-connected-accounts.ba46dc06c0684b481667e91cf4e3fcfd.png)

For each payment method, use the dropdown to select the desired setting:

- **Off by default** connected accounts can turn the payment method on or off.
The default is off.
- **Blocked** turns the payment method off for all connected accounts. Connected
account owners can’t opt in.
- **On by default** connected accounts can turn the payment method on or off.
The default is on.

#### Note

By default, Stripe enables a few commonly used payment methods such as Cards,
Apple Pay, and Google Pay.

![Configure settings for each payment
method](https://b.stripecdn.com/docs-statics-srv/assets/settings-api-wallets.956b27fd0756e064d433aaa5999130fe.png)

[Determine availability and display preference for connected
accounts](https://docs.stripe.com/connect/payment-method-configurations#section-2)
Use the Payment Method Configurations API with the connected account ID to read
the current state of a payment method for a specific connected account. If the
connected account has more than one configuration you can filter the results by
your application’s `client_id`, located in your [Connect
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/oauth).

#### Working with multiple payment method configurations

If you’ve created additional payment method configurations for a connected
account, you can identify the original configuration by the `is_default`
property. Stripe uses the default configuration for payments if you don’t [pass
a configuration
ID](https://docs.stripe.com/connect/multiple-payment-method-configurations#use-payment-method-configuration)
into your checkout flow. For more information about `is_default` and other
properties of payment method configurations, see the [API
reference](https://docs.stripe.com/api/payment_method_configurations/object#payment_method_configuration_object-is_default).

```
curl -G https://api.stripe.com/v1/payment_method_configurations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d application={{CLIENT_APPLICATION_ID}}
```

```
{
 "object": "list",
 "data": [
 {
 "id": "{{PAYMENT_METHOD_CONFIGURATION_ID}}",
 "object": "payment_method_configuration",
 "name": "Default",
 "active": true,
 "is_default": true,
 "livemode": false,
 "application": "{{CLIENT_APPLICATION_ID}}",
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

You can use the available field to know whether or not a buyer sees this payment
method at checkout time. If available is `true`, that payment method’s
capability is active and `display_preference` is on. If available is `false`,
that payment method either doesn’t have an active capability or the
`display_preference` value is off and buyers won’t see this payment method at
checkout time. To simplify your integration and take advantage of other
features, use dynamic payment methods at checkout time which automatically reads
this parameter and shows the right payment methods to buyers.
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

[Update display_preference when a connected account edits their
settings](https://docs.stripe.com/connect/payment-method-configurations#section-3)
When a connected account owner takes action to turn on or off a payment method,
you can update the `display_preference` `preference` attribute. This stores the
connected account owner’s preference for that payment method and is used to
determine whether the payment method is shown to buyers.

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
 "name": "Default",
 "active": true,
 "is_default": true,
 "livemode": false,
 "application": "{{CLIENT_APPLICATION_ID}}",
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

[Display available payment methods on
checkout](https://docs.stripe.com/connect/payment-method-configurations#section-4)
You can manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the return of eligible payment methods based on factors such as the
transaction’s amount, currency, and payment flow. This shows buyers in your
checkout flow only the payment methods where `available` is `true`.

If you want to pre-fetch the available payment methods for a connected account
before you render your checkout page, call the Payment Method Configurations API
to get the list of payment methods. Use those with `available` set to `true`.

[Support Card type payment
methods](https://docs.stripe.com/connect/payment-method-configurations#section-5)
Some payment methods, such as Apple Pay and Link, aren’t included as separate
payment method types on a PaymentIntent and are confirmed only when supplying
`card`. With the Payment Method Configurations API, you can let connected
account owners opt in or opt out of these specific payment methods and prevent
them from showing up in the UI.

[Market payment methods to your connected account
owners](https://docs.stripe.com/connect/payment-method-configurations#section-6)
Use targeted marketing messaging to encourage connected account owners to opt in
to specific payment methods they’re eligible for but haven’t yet opted in to.

Call the GET method to retrieve the status of the payment method configuration
to determine when to promote a payment method. You can determine if a connected
account owner has interacted with your configuration before by reading the
`display_preference` value. If the `display_preference` `preference` is `none`,
the connected account owner hasn’t changed the default configuration. If the
`preference` value is `on` or `off`, the connected account owner has interacted
with the configuration and you can choose whether to suppress the marketing
message.

## See also

- [Connect integration guide](https://docs.stripe.com/connect/charges)
- [Multiple payment method
configurations](https://docs.stripe.com/connect/multiple-payment-method-configurations)
- [Adding payment method
capabilities](https://docs.stripe.com/connect/payment-methods)

## Links

- [Request
access](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings#request-access)
- [integrate with Payment Method
Configurations](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings#integration)
- [Manage payment methods for your connected
accounts](https://dashboard.stripe.com/test/settings/payment_methods/connected_accounts)
- [Dashboard](https://dashboard.stripe.com/login)
- [Connect
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/oauth)
- [pass a configuration
ID](https://docs.stripe.com/connect/multiple-payment-method-configurations#use-payment-method-configuration)
- [API
reference](https://docs.stripe.com/api/payment_method_configurations/object#payment_method_configuration_object-is_default)
- [capability](https://docs.stripe.com/api/capabilities/object)
- [Check country
support](https://docs.stripe.com/payments/payment-methods/integration-options)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Connect integration guide](https://docs.stripe.com/connect/charges)
- [Multiple payment method
configurations](https://docs.stripe.com/connect/multiple-payment-method-configurations)
- [Adding payment method
capabilities](https://docs.stripe.com/connect/payment-methods)