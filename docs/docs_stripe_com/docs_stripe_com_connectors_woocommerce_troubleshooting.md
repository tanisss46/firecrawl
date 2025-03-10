# Troubleshoot the connector

## Test and troubleshoot the features for the Stripe Tax Connector for WooCommerce.

If you encounter any issues while using the Stripe Tax Connector for
WooCommerce, you can use the information below to test tax calculation or
identify and resolve issues.

## Test tax calculation

You can test how the Stripe Tax Connector for WooCommerce calculates tax for
your products by manually creating an order or through your checkout flow.

### Example 1: Manual order creation

To calculate and add tax to a manually created order:

- On your website’s dashboard, navigate to **WooCommerce** > **Orders**.
- On the **Orders** page, click **Add new order**.
- Add your customer and order information, then click **Recalculate**.

If you don’t see tax added, you might not have a
[registration](https://docs.stripe.com/connectors/woocommerce/configuration#tax-registrations)
in the customer’s jurisdiction.

### Example 2: Checkout page

To test how the connector calculates and adds tax on the checkout page:

- View your shop as a customer.
- Add a taxable product to your cart.
- Enter an address in a jurisdiction where you have an active
[registration](https://docs.stripe.com/connectors/woocommerce/configuration#tax-registrations).

The appropriate tax automatically calculates on the checkout page.

## Taxes applied to orders

Taxes apply only if your customer is located in a jurisdiction where you have a
registration, and your product is taxable in that jurisdiction.

If taxes aren’t applying to orders, make sure the customer is in a jurisdiction
where you have an active registration, and that you’ve properly set up and
enabled the connector:

- Verify that the Stripe Tax Connector for WooCommerce is [configured and
connected](https://docs.stripe.com/connectors/woocommerce/configuration#connect-stripe-account)
to your Stripe account.
- Verify that tax is enabled in the Dashboard, as follows:- On the **General**
tab, select **Enable taxes**.
- On the **Tax** tab, select **Automated taxes**.
- On the **Stripe Tax** tab, select **Enable tax collection**.

If taxes still aren’t applying to orders, the product might not be taxable for
your customer in that jurisdiction, even if you’re registered. Check the [API
responses](https://dashboard.stripe.com/workbench/logs) for more details about
why the tax rate is zero.

## Multiple taxes

When you create an order, you might see multiples of the same tax amount. This
isn’t an error. Occasionally multiple taxes exist with the same name and same
amount that apply to a single line item.

You can choose to display a single total tax amount to your customers. To do so,
navigate to **Settings** > **Tax** in your WooCommerce app, and select **As a
single total** for **Display tax totals**.

## Transactions in Stripe reports

If you can’t see transactions in your Stripe reports, make sure your
[Dashboard](https://dashboard.stripe.com/dashboard) isn’t in Test mode.

After your customer completes their purchase and the connector records the
transaction, you can expect a delay of a few minutes before the transaction
appears in the Stripe reports in your Dashboard.

## See also

- [Install the
connector](https://docs.stripe.com/connectors/woocommerce/installation)
- [Configure the
connector](https://docs.stripe.com/connectors/woocommerce/configuration)

## Links

-
[registration](https://docs.stripe.com/connectors/woocommerce/configuration#tax-registrations)
- [configured and
connected](https://docs.stripe.com/connectors/woocommerce/configuration#connect-stripe-account)
- [API responses](https://dashboard.stripe.com/workbench/logs)
- [Dashboard](https://dashboard.stripe.com/dashboard)
- [Install the
connector](https://docs.stripe.com/connectors/woocommerce/installation)
- [Configure the
connector](https://docs.stripe.com/connectors/woocommerce/configuration)