# Tax for software platforms

## Learn how to enable Stripe Tax for your connected accounts, and collect tax when the connected account is liable for paying the tax.

Stripe Tax enables businesses to calculate, collect, and report indirect taxes
in over [50 countries](https://docs.stripe.com/tax/supported-countries), across
hundreds of product categories. As a platform, you can use Stripe tax to offer
pre-integrated tax compliance to your connected accounts.

Use this guide if your connected accounts are responsible for collecting,
filing, and reporting taxes.

- [Set up your connected accounts for
tax](https://docs.stripe.com/tax/tax-for-platforms#check-set-up)
- (Optional) [Assign tax codes to the product
catalog](https://docs.stripe.com/tax/tax-for-platforms#assign-product-tax-codes)
- [Integrate tax calculation and
collection](https://docs.stripe.com/tax/tax-for-platforms#enable-tax-collection)
- [Access Stripe Tax
Reports](https://docs.stripe.com/tax/tax-for-platforms#access-reports)
[Set up your connected accounts for
tax](https://docs.stripe.com/tax/tax-for-platforms#set-up)
As a platform, you must make sure that a connected account has their [tax
settings and registrations set up](https://docs.stripe.com/tax/set-up) before
enabling tax calculations. This can be achieved by:

### Connected account using the Stripe Dashboard

### Creating a tax interface within your platform

### Using Connect embedded components within your platform

Your platform must then check whether connected accounts have configured Stripe
Tax to enable tax calculations.

#### Note

[Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ftax-for-platforms)
to check if your connected accounts are ready to use Stripe Tax.

On the Dashboard, you can [filter the accounts that are ready to use Stripe
Tax](https://dashboard.stripe.com/connect/accounts/overview?connected_merchant%5Btax_settings_status%5D=active).
You can also export the accounts from the [connected account overview
page](https://dashboard.stripe.com/connect/accounts/overview) with the following
Stripe Tax-related columns:

- **Tax Settings Status**: the value `active` indicates that the account is
ready to use Stripe Tax. The value `pending` indicates that some required fields
are
[missing](https://docs.stripe.com/api/tax/settings/object#tax_settings_object-status_details-pending-missing_fields).
- **Tax Threshold Status**: the value `exceeded` indicates that the account’s
calculated sales or transactions are over the location’s threshold, and the
business likely needs to register for tax. For more information, see [Monitor
your obligations](https://docs.stripe.com/tax/monitoring).
- **Tax Registration Status**: the value `active` indicates that the account has
at least one active [tax registration](https://docs.stripe.com/tax/registering).

You can also check whether an account has configured Stripe Tax by [using the
Tax Settings API](https://docs.stripe.com/tax/settings-api#checking-settings).

[Assign tax codes to the product
catalogOptional](https://docs.stripe.com/tax/tax-for-platforms#assign-product-tax-codes)
To calculate taxes, Stripe Tax requires classifying products into their tax
codes. One way to do this is to [supply a preset tax code for each connected
account](https://docs.stripe.com/tax/settings-api#updating-settings), which is
probably sufficient if your connected accounts typically sell a single category
of items.

However, you might offer your users more control by allowing them to map Tax
Codes to each product. You can retrieve a list of [supported product tax
codes](https://docs.stripe.com/tax/tax-codes) from the Stripe [Tax Code
API](https://docs.stripe.com/api/tax_codes). You can also allow a subset of this
list if your connected accounts only sell specific types of products.

[Integrate tax calculation and
collection](https://docs.stripe.com/tax/tax-for-platforms#enable-tax-collection)
You need to integrate with Stripe Tax to calculate taxes as part of your
checkout flow.

### Payment Links

### Payment Links for one-time payments

### Payment Links for subscriptions

### Checkout

### Checkout Sessions for one-time payments

### Checkout Sessions for subscriptions

### Billing

### Subscriptions

### Invoicing

### Custom flows using the Stripe Tax API

### Payment Intents

### Off-Stripe payments

After you implement it, Stripe automatically starts collecting tax in
jurisdictions where the user has an active registration.

#### Note

Independent of the integration, your connected account receives a credit for the
collected tax amount by default.

[Access Stripe Tax
Reports](https://docs.stripe.com/tax/tax-for-platforms#access-reports)
Your connected accounts can use [Stripe Tax
reports](https://docs.stripe.com/tax/reports) to help them correctly file and
remit tax.

### Connected account use the Stripe Dashboard

### Use the Stripe API

## See also

- [Calculate tax in your custom checkout
flow](https://docs.stripe.com/tax/custom)

## Links

- [50 countries](https://docs.stripe.com/tax/supported-countries)
- [tax settings and registrations set up](https://docs.stripe.com/tax/set-up)
- [Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ftax-for-platforms)
- [filter the accounts that are ready to use Stripe
Tax](https://dashboard.stripe.com/connect/accounts/overview?connected_merchant%5Btax_settings_status%5D=active)
- [connected account overview
page](https://dashboard.stripe.com/connect/accounts/overview)
-
[missing](https://docs.stripe.com/api/tax/settings/object#tax_settings_object-status_details-pending-missing_fields)
- [Monitor your obligations](https://docs.stripe.com/tax/monitoring)
- [tax registration](https://docs.stripe.com/tax/registering)
- [using the Tax Settings
API](https://docs.stripe.com/tax/settings-api#checking-settings)
- [supply a preset tax code for each connected
account](https://docs.stripe.com/tax/settings-api#updating-settings)
- [supported product tax codes](https://docs.stripe.com/tax/tax-codes)
- [Tax Code API](https://docs.stripe.com/api/tax_codes)
- [Stripe Tax reports](https://docs.stripe.com/tax/reports)
- [Calculate tax in your custom checkout
flow](https://docs.stripe.com/tax/custom)