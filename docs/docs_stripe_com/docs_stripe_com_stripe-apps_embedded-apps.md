# Embedded Stripe Apps integration guidePrivate preview

## Use embedded components for Stripe Apps to allow your customers to manage payments data in third party applications.

Customers expect their payments data to be readily available in the tools
they’re already using to complete their business workflows. Embedded components
for Apps allow your customers to use third party applications in Stripe.

With embedded components for Apps, you can embed integrations built for Stripe
into your platform, and allow your customers to use their preferred third party
applications without leaving Stripe. Use prebuilt UI components that sync data
directly with applications such as QuickBooks and Xero.

[Integrate with Connect embedded
components](https://docs.stripe.com/stripe-apps/embedded-apps#integrate-connect-js)
[Set up
Connect.js](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
to enable the ability to add connected account dashboard functionality to your
website.

[Select the app to
integrate](https://docs.stripe.com/stripe-apps/embedded-apps#app-select)
Stripe supports the following app integrations.

App integrationApp ID[QuickBooks Sync by
Acodei](https://docs.stripe.com/stripe-apps/embedded-apps/accounting-integrations#quickbooks-sync-by-acodei)com.example.acodeistripeapp[Xero
sync by
Xero](https://docs.stripe.com/stripe-apps/embedded-apps/accounting-integrations#xero)com.xero.stripeapp[Mailchimp](https://docs.stripe.com/stripe-apps/embedded-apps/marketing-integrations#mailchimp)mailchimp[Set
up app
installation](https://docs.stripe.com/stripe-apps/embedded-apps#app-install)
Render the app install embedded component for your selected app. App
installation grants permission for the third party app to access your users’
Stripe data, creating a connection between your platform, Stripe, and the third
party app. The component has two states: `uninstalled` and `installed`. Listen
to install event triggers to build your custom UX flow or make updates in your
own back end.

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable app
installation and rendering by specifying `app_install`, and `app_viewport` in
the `components` parameter. You must enable the app you want to render by
specifying the `features` parameter under `allowed_apps`.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; embedded_connect_beta=v2;" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[app_install][enabled]"=true \
 -d "components[app_install][features][allowed_apps][]"=APP_ID \
 -d "components[app_viewport][enabled]"=true \
 -d "components[app_viewport][features][allowed_apps][]"=APP_ID
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the App install component in the front end:

```
const appInstall = stripeConnectInstance.create('app-install');
appViewport.setApp('{{APP_ID}}');
container.appInstall(appViewport);
```

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescription`setApp``string`Sets the ID of the App your
connected account can install. See the list of [available
apps](https://docs.stripe.com/stripe-apps/embedded-apps#app-select).
You can configure custom behavior based on the current or updated state of an
install. To do so, set a custom callback function using the following methods:

HTML + JSReactMethodDescriptionVariables`setOnAppInstallStateFetched`Allows
users to specify custom behavior in a callback function on install fetch.-
`response.appId`: The app installed
- `response.state`: The state of the install `INSTALLED | UNINSTALLED`
`setOnAppInstallStateChanged`Allows users to specify custom behavior in a
callback function when the install state has changed.- `response.appId`: The app
installed
- `response.state`: The state of the install `INSTALLED | UNINSTALLED`
[Set up app
settings](https://docs.stripe.com/stripe-apps/embedded-apps#app-viewport)
Render the app viewport embedded component for your selected app to enable core
app functionality, including connection to the app’s software account with
OAuth, onboarding, settings, and configuration for the service and
synchronization states of transactions. Pass the `user_id` (business represented
on your platform) as an optional HTML attribute that third party apps can use to
build a dynamic URL that redirects back to your user dashboard after OAuth.

```
const appViewport = stripeConnectInstance.create('app-viewport');
appViewport.setApp('{{APP_ID}}');
appViewport.setAppData({userId: '{{PLATFORM_USER_ID}}'});
container.appendChild(appViewport);
```

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescription`setApp``string`Sets the ID of the App your
connected account can render. See available apps in the [Embedded Stripe Apps
integration
guide](https://docs.stripe.com/stripe-apps/embedded-apps#app-select).`setAppData``Record<String,
String>`Sets data pertaining to your platform consumed by the App.[Customize for
Connect destination on behalf of
(OBO)](https://docs.stripe.com/stripe-apps/embedded-apps#destination-obo)
Pass required and optional transaction data to your selected app by updating the
destination charge on the connected account using the data standardized data
schema below. You must pass a
[Customer](https://docs.stripe.com/api/customers/object) object to the
destination charge. You have three scenarios that require you to update your
destination charge:

- One-time payment complete
- Recurring payment complete
- Payment refunded
AccountingMarketingField or key nameFormat (standard CSV rules
apply)DescriptionRequired[charges.customer](https://docs.stripe.com/api/charges/object#charge_object-customer)String
(ID)Stripe Customer ID (belonging to the connected account) attached to a
destination `Charge` object. Transactions don’t sync to apps (such as Xero and
QBO) if this field isn’t
present.Required[customer.name](https://docs.stripe.com/api/customers/object#customer_object-name)StringCustomer’s
full
name[customer.email](https://docs.stripe.com/api/customers/object#customer_object-email)StringCustomer’s
email
address[customer.address.<>](https://docs.stripe.com/api/customers/object#customer_object-address)String
(multi-field)Customer’s physical address (can be used for both billing and
shipping)`charges.metadata.[refund_amount]`String (cents integer)Mirroring
[charges.amount_refunded](https://docs.stripe.com/api/charges/object#charge_object-amount_refunded)
in base currency sub-units (‘350’ = 3.50 USD)Required by Quickbooks Online sync
by Acodei`charges.metadata.[refund_reason]`stringReason for the
refund`charges.metadata.[currency_converted]``true` | `false` | `null`Set to
`true` if currency has been converted, for example, if the presentment currency
differs from the settlement currencyRequired by Quickbooks Online sync by Acodei
if using fees_names
metadata`customer.metadata.[platform_customer_ID]`StringCustomer ID as recorded
in the platform’s system*`charges.metadata.[platform_product_ID]`String, CSV
multiple productsProduct IDs as recorded in the platform’s
system`charges.metadata.[platform_product_name]`String, CSV multiple
productsProduct name as recorded in the platform’s
system`charges.metadata.[platform_product_quantity]`String, CSV multiple
productsQuantity of each product corresponding to the ID and name
array`charges.metadata.[platform_product_value]`Integer, CSV multiple
productsThe individual product value (price or cost) corresponding to the
Product ID and name. Base currency sub-units (‘350’ = 3.50
USD)`charges.metadata.[platform_product_tag]`String, CSV multiple
productsProduct tag or category corresponding to the ID and name
array`charges.metadata.[platform_order_ID]`StringOrder ID as recorded in the
platform’s system`charges.metadata.[platform_charge_ID]`StringCharge or
transaction ID as recorded in the platform’s system and visible to the
business`charges.metadata.[fees_names]`String, CSV multiple feesName of fees the
user is paying (expense) of any kind related to the transaction that aren’t
captured in the Charge (for example, credit processing fee or platform fee) If
this field is populated, the charges.application_fee is
ignored.`charges.metadata.[fees_values]`Integer, CSV multiple feesValues of fees
the user is paying (expense) of any kind related to the transaction that aren’t
captured in the charge—for example, the credit processing fee or platform fee.
Base currency sub-units (‘350’ = 350
USD)`charges.metadata.[revenues_names]`String, CSV multiple revenuesFees
(revenues) collected by the business related to this transaction (charge) that
aren’t captured in the charge (for example, a convenience fee or
tips)`charges.metadata.[revenues_values]`Integer, CSV multiple revenuesValues of
fees (revenues) collected by the business related to this transaction (charge).
Base currency sub-units (‘350’ = 3.50
USD)`charges.metadata.[total_tax]`IntegerTotal taxes associated with this
transaction (charge). Base currency sub-units (‘350’ = 3.50
USD)`charges.metadata.[tax_names]`String, CSV multiple taxesTax type names
applied on a transaction allowing for multiple tax types, using an array (for
example ‘GST’ or ‘sales’)`charges.metadata.[tax_rates]`Float, CSV multiples
taxesTax rates applied on a transaction corresponding to specified tax types as
a percentage (for example, ‘3’ or ‘1.5’ corresponds to 3% GST and 1.5% sales
tax)`charges.metadata.[tax_values]`string, CSV multiple taxesTax values applied
on a transaction corresponding to specified tax types. Base currency sub-units
(‘350’ = 3.50 USD)
QuickBooks Sync by Acodei also requires charge updates with refund amounts
written to metadata.

The following code snippet example traverses to the target destination charge
and shows how to update per schema.

- Trace from the Transaction to the destination charge

```
const paymentOnPlatform = await StripeClient.paymentIntents.retrieve(
 "pi_3N6JL7LirQdaQn8E1Lpn7Dui",
);

const latestCharge = await StripeClient.charges.retrieve(
 paymentOnPlatform.latest_charge as string,
);

const transfer = await StripeClient.transfers.retrieve(
 latestCharge.transfer as string,
);

const payment = await StripeClient.charges.retrieve(
 transfer.destination_payment as string,
 undefined,
 {
 stripeAccount: transfer.destination as string,
 },
 );
```

- Create a customer and then update the charge with the relevant customer ID and
metadata. The customer must belong to the connected account and not the platform
for the data to pass, and apps to synchronize.

```
const customer = await StripeClient.customers.create(
 {
 email: `jenny.rosen@example.com`,
 name: "Jenny Rosen",
	 address.city: "Brothers"
	 Address.state: "Oregon"
	 address.country: "USA"
	 address.line1: "27 Fredrick Ave"
	 address.postal_code: "97712"
 	 metadata: {
 	 platform_customer_ID: "K-123456"
	 },
 },
 {
 stripeAccount: accountId,
 },
 );
 const payment = await StripeClient.charges.update(
 id,
 {
 customer: customer.id,
 metadata: {
 product_name: "Creative writing course for PMs",
 platform_product_ID: "P-123456"
 platform_order_ID: "O-123456"
 },
 },
 {
 stripeAccount: accountId,
 },
 );
```

[Direct
charges](https://docs.stripe.com/stripe-apps/embedded-apps#direct-charges)
The embedded integrations accesses all payment, customer, and product data
stored with Stripe. You can pass optional platform-specific data to the App
using the below metadata schema.

Field or key nameFormat (standard CSV rules
apply)Description`customer.metadata.[platform_customer_ID]`stringCustomer ID as
recorded in the platform’s system`payment.metadata.[platform_product_ID]`string,
CSV multiple productsProduct IDs as recorded in the platform’s system, related
to this transaction (if different than the Stripe product
ID)`payment.metadata.[platform_product_name]`string, CSV multiple
productsProduct or service names as recorded in the platforms’ system, related
to this transaction (if different than the Stripe product
name)`payment.metadata.[platform_product_value]`string, CSV multiple productsThe
individual product value (price or cost) corresponding to the ID and name array
(if different than the Stripe product
value)`payment.metadata.[platform_order_ID]`stringOrder ID as recorded in the
platform’s system, related to this transaction
(charge)`payment.metadata.[platform_charge_ID]`stringCharge or transaction ID as
recorded on the platform and visible to the user (if different than the Stripe
payment ID)
## Interested in the preview of embedded components for Apps?

Enter your email address below to provide feedback, request other software
integrations, and request early access to embedded components for Apps.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

- [Set up
Connect.js](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [QuickBooks Sync by
Acodei](https://docs.stripe.com/stripe-apps/embedded-apps/accounting-integrations#quickbooks-sync-by-acodei)
- [Xero sync by
Xero](https://docs.stripe.com/stripe-apps/embedded-apps/accounting-integrations#xero)
-
[Mailchimp](https://docs.stripe.com/stripe-apps/embedded-apps/marketing-integrations#mailchimp)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [available apps](https://docs.stripe.com/stripe-apps/embedded-apps#app-select)
- [Customer](https://docs.stripe.com/api/customers/object)
-
[charges.customer](https://docs.stripe.com/api/charges/object#charge_object-customer)
-
[customer.name](https://docs.stripe.com/api/customers/object#customer_object-name)
-
[customer.email](https://docs.stripe.com/api/customers/object#customer_object-email)
-
[customer.address.<>](https://docs.stripe.com/api/customers/object#customer_object-address)
-
[charges.amount_refunded](https://docs.stripe.com/api/charges/object#charge_object-amount_refunded)
- [privacy policy](https://stripe.com/privacy)