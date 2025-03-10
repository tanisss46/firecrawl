# Troubleshoot the connector

## Test and troubleshoot the features of the Stripe Tax Connector for BigCommerce.

To troubleshoot the Stripe Tax Connector for BigCommerce, add a product to the
shopping cart and then start the checkout process.

If you don’t see a tax amount displayed, do the following:

- Verify that you installed and connected the Stripe Tax app correctly. Follow
the
[installation](https://docs.stripe.com/connectors/bigcommerce/installation#install-bigcommerce-stripe-app)
steps again.
- Verify that the customer you added is in a market configured in the [Provider
targeting tax
setting](https://docs.stripe.com/connectors/bigcommerce/configuration#configure-country-list).
- Verify that the customer’s address is located in one of the registered
locations. Many businesses miss or skip this step.
- Verify your [tax
registrations](https://dashboard.stripe.com/tax/registrations) in the Stripe
Dashboard.
- Verify that the customer isn’t
[tax-exempt](https://docs.stripe.com/connectors/bigcommerce/configuration#configure-customer-tax-exemptions).
- Verify where your tax is calculated. Some product tax codes might use the
seller’s address instead of the shipping address for tax calculations. Check the
[Dashboard logs](https://dashboard.stripe.com/logs?path=/v1/tax/calculations) to
determine the exact location where your taxes are applied.(Recommended) Select a
product tax code with a description that closely matches your product. This is
important because incorrect tax calculations often occur when selecting a
general product tax code instead of a specific one. For example, selecting
`General - Services` when a more specific category applies can result in taxes
calculated based on the seller’s location. Selecting the most accurate tax code
ensures taxes are calculated correctly.

For more information about why Stripe Tax applies zero tax to some calculations,
see [Zero tax amounts](https://docs.stripe.com/tax/zero-tax).

If you’re still experiencing issues after following these troubleshooting steps,
you can [contact us](mailto:stripe-tax-bigc-support@stripe.com).

## See also

- [Testing Stripe Tax](https://docs.stripe.com/tax/testing)
- [Install the Stripe Tax Connector for
BigCommerce](https://docs.stripe.com/connectors/bigcommerce/installation)
- [Configure the Stripe Tax Connector for
BigCommerce](https://docs.stripe.com/connectors/bigcommerce/configuration)
- [BigCommerce - Automatic Tax
Setup](https://support.bigcommerce.com/s/article/Automatic-Tax-Setup)

## Links

-
[installation](https://docs.stripe.com/connectors/bigcommerce/installation#install-bigcommerce-stripe-app)
- [Provider targeting tax
setting](https://docs.stripe.com/connectors/bigcommerce/configuration#configure-country-list)
- [tax registrations](https://dashboard.stripe.com/tax/registrations)
-
[tax-exempt](https://docs.stripe.com/connectors/bigcommerce/configuration#configure-customer-tax-exemptions)
- [Dashboard logs](https://dashboard.stripe.com/logs?path=/v1/tax/calculations)
- [Zero tax amounts](https://docs.stripe.com/tax/zero-tax)
- [Testing Stripe Tax](https://docs.stripe.com/tax/testing)
- [Install the Stripe Tax Connector for
BigCommerce](https://docs.stripe.com/connectors/bigcommerce/installation)
- [Configure the Stripe Tax Connector for
BigCommerce](https://docs.stripe.com/connectors/bigcommerce/configuration)
- [BigCommerce - Automatic Tax
Setup](https://support.bigcommerce.com/s/article/Automatic-Tax-Setup)