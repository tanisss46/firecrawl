# Configure the connector

## Configure the Stripe Tax Connector for WooCommerce.

After you [install](https://docs.stripe.com/connectors/woocommerce/installation)
the Stripe Tax Connector for WooCommerce, you can connect it to your Stripe
account and configure your tax settings.

If you previously configured these tax settings in the [Stripe
Dashboard](https://dashboard.stripe.com/test/settings/tax), the values populate
automatically in the Stripe Tax connector. When you edit the values in the
connector, the changes automatically update in the Stripe Dashboard in live
mode. Test mode isn’t supported for the WooCommerce connector.

If your menu varies from the steps below, refer to the WordPress instructions to
[use a plugin](https://wordpress.com/support/plugins/use-your-plugins/).

[Connect your Stripe
account](https://docs.stripe.com/connectors/woocommerce/configuration#connect-stripe-account)
On your website’s dashboard, navigate to **WooCommerce** > **Settings**. On the
**Stripe Tax** tab, click **Connect with Stripe** to log in to your Stripe
account or create a new one.

After successful authentication, navigate back to the Stripe Tax settings to
continue with the configuration steps.

[Configure your sales tax
settings](https://docs.stripe.com/connectors/woocommerce/configuration#configure-tax-settings)
On the **Stripe Tax** tab, under **Configure your sales tax settings**, complete
the following:

- Enter your head office address, which is your company’s legal address.
- Choose your default [product tax code](https://docs.stripe.com/tax/tax-codes),
which allows Stripe to calculate the tax rate for categories of products.
- Click **Save changes**.

On the **Tax** tab, you can decide if the prices you set for your products are
inclusive or exclusive of tax.

[Manage tax
registrations](https://docs.stripe.com/connectors/woocommerce/configuration#tax-registrations)
Tax isn’t applied [until you add
registrations](https://docs.stripe.com/tax/zero-tax#situations-where-stripe-calculates-zero-tax)
for jurisdictions where you need to collect tax. Our [monitoring
tool](https://docs.stripe.com/tax/monitoring) can help you understand where you
might be registered or need to register.

If you’re already registered in certain jurisdictions and want to start
collecting tax immediately, you can add those registrations to your
configuration. You can only add tax registrations for [supported countries and
registration
types](https://docs.stripe.com/tax/supported-countries#supported-countries).
Some jurisdictions might require additional information.

### Add tax registration

On the **Stripe Tax** tab, under **Tax registrations**, click **Add new**.
Choose the jurisdiction from the dropdown, then click **Save changes**.

### Delete tax registration

To delete a registration, hover over the registration, then click **End
immediately**. To delete multiple registrations, select them from the list, then
click **End immediately** from the **Bulk actions** dropdown.

[OptionalConfigure product tax codes and customer tax
settings](https://docs.stripe.com/connectors/woocommerce/configuration#configure-product-tax-code)[Collect
taxes](https://docs.stripe.com/connectors/woocommerce/configuration#collect-taxes)
To start collecting taxes:

- On the **WooCommerce** > **General** tab, select **Enable tax rates and
calculations**, then click **Save changes**. This setting enables rate
configuration and tax calculation during the checkout process.
- On the **WooCommerce** > **Stripe Tax** tab, select **Enable Stripe Tax**,
then click **Save changes**. This setting enables automatic tax calculation and
collection on all transactions.

After selecting a product from your WooCommerce store, you can enter an address
on the Checkout page to automatically calculate tax based on the address. Test
the tax behavior using the addresses where you registered, as well as the store
address.

Certain product tax codes, such as [most
services](https://docs.stripe.com/tax/tax-codes?type=services), are taxed at
origin (your head office address). Scenarios also exist where [zero
tax](https://docs.stripe.com/tax/zero-tax) is calculated.

[View tax
reports](https://docs.stripe.com/connectors/woocommerce/configuration#tax-reports)
After you start collecting taxes, the Stripe Tax connector sends the
transactions to Stripe Tax. You can then access tax reports and exports in the
[Stripe Dashboard](https://dashboard.stripe.com/tax/registrations).

Learn more about the types of [tax reports](https://docs.stripe.com/tax/reports)
available in Stripe Tax.

[OptionalSet up custom tax
rates](https://docs.stripe.com/connectors/woocommerce/configuration#configure-tax-customizations)[OptionalRefund
taxes](https://docs.stripe.com/connectors/woocommerce/configuration#refund-taxes)
## See also

- [Install the
connector](https://docs.stripe.com/connectors/woocommerce/installation)
- [Test and troubleshoot the
connector](https://docs.stripe.com/connectors/woocommerce/troubleshooting)

## Links

- [install](https://docs.stripe.com/connectors/woocommerce/installation)
- [Stripe Dashboard](https://dashboard.stripe.com/test/settings/tax)
- [use a plugin](https://wordpress.com/support/plugins/use-your-plugins/)
- [product tax code](https://docs.stripe.com/tax/tax-codes)
- [until you add
registrations](https://docs.stripe.com/tax/zero-tax#situations-where-stripe-calculates-zero-tax)
- [monitoring tool](https://docs.stripe.com/tax/monitoring)
- [supported countries and registration
types](https://docs.stripe.com/tax/supported-countries#supported-countries)
- [most services](https://docs.stripe.com/tax/tax-codes?type=services)
- [zero tax](https://docs.stripe.com/tax/zero-tax)
- [Stripe Dashboard](https://dashboard.stripe.com/tax/registrations)
- [tax reports](https://docs.stripe.com/tax/reports)
- [Test and troubleshoot the
connector](https://docs.stripe.com/connectors/woocommerce/troubleshooting)