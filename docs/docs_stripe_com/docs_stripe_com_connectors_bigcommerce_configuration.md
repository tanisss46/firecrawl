# Configure the connector

## Configure the Stripe Tax Connector for BigCommerce.

After you [install](https://docs.stripe.com/connectors/bigcommerce/installation)
the Stripe Tax Connector for BigCommerce, you can configure your tax settings.

[Configure your Stripe Tax
settings](https://docs.stripe.com/connectors/bigcommerce/configuration#configure-stripe-tax)
Complete steps 1 to 4 in the [Stripe Tax setup
guide](https://docs.stripe.com/tax/set-up). You can skip step 5 because you
don’t need to enable tax in your Stripe integration or use the Stripe Tax API.

In the [Stripe Dashboard](https://dashboard.stripe.com/), do the following:

- Set your origin address.
- Select your preset tax code.
- Select whether or not prices include tax by default.
- Add registrations.
[Configure your BigCommerce store to use the Stripe Tax
app](https://docs.stripe.com/connectors/bigcommerce/configuration#configure-bigcommerce)
Next, configure BigCommerce to set up Stripe Tax as a tax service.

- In your BigCommerce dashboard, go to **Settings** > **Tax**.
- Under **Configured tax services**, click **Edit** next to Stripe.
- Click **Test Connection** to verify that your app is correctly installed.
[Set up the origin
address](https://docs.stripe.com/connectors/bigcommerce/configuration#setup-origin-address)
In your BigCommerce dashboard, go to **Settings** > **Shipping** > **Edit**. Set
your shipping origin address, if you haven’t already.

You must update the shipping origin address in both Stripe and BigCommerce
dashboards. This information doesn’t sync automatically.

[Configure the countries to use Stripe
Tax](https://docs.stripe.com/connectors/bigcommerce/configuration#configure-country-list)
In your BigCommerce dashboard, update the **Provider targeting** to choose the
[countries](https://docs.stripe.com/tax/supported-countries) where you want to
use Stripe Tax.

[Set the provider
options](https://docs.stripe.com/connectors/bigcommerce/configuration#set-provider-options)
In your BigCommerce dashboard, under **Provider Options**, select **Please
submit my order data so that I can use solution tax reporting and returns
features**.

[OptionalSet up tax
codes](https://docs.stripe.com/connectors/bigcommerce/configuration#set-up-tax-codes)[Configure
the tax treatment for your
store](https://docs.stripe.com/connectors/bigcommerce/configuration#configure-tax-treatment)
In your BigCommerce dashboard, go to **Settings** > **Tax** > **Store tax
settings**. Click **Edit** and then set the **Prices entered with tax** to one
of the following:

- **Yes, I will enter prices inclusive of tax**
- **No, I will enter prices exclusive of tax**

The value that you configure in the BigCommerce dashboard takes precedence over
the value configured in the Stripe Dashboard. These values don’t sync
automatically between Stripe and BigCommerce.

[OptionalConfigure the tax code for each of your
products](https://docs.stripe.com/connectors/bigcommerce/configuration#configure-tax-code-for-products)[OptionalConfigure
the tax exemption status for your
customers](https://docs.stripe.com/connectors/bigcommerce/configuration#configure-customer-tax-exemptions)[OptionalLimitations](https://docs.stripe.com/connectors/bigcommerce/configuration#limitations)[OptionalRefund
taxes](https://docs.stripe.com/connectors/bigcommerce/configuration#refund-taxes)
## See also

- [Install the Stripe Tax Connector for
BigCommerce](https://docs.stripe.com/connectors/bigcommerce/installation)
- [Test and troubleshoot the Stripe Tax Connector for
BigCommerce](https://docs.stripe.com/connectors/bigcommerce/troubleshooting)

## Links

- [install](https://docs.stripe.com/connectors/bigcommerce/installation)
- [Stripe Tax setup guide](https://docs.stripe.com/tax/set-up)
- [Stripe Dashboard](https://dashboard.stripe.com/)
- [countries](https://docs.stripe.com/tax/supported-countries)
- [Test and troubleshoot the Stripe Tax Connector for
BigCommerce](https://docs.stripe.com/connectors/bigcommerce/troubleshooting)