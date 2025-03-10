# Install the Stripe Connector for Shopware 6

## Learn how to install and update the Stripe Connector for Shopware 6.

Use the Stripe Connector for [Shopware 6](https://www.shopware.com/en/) to
integrate [Stripe Elements](https://docs.stripe.com/payments/elements) and
accept more than 25 payment methods with a single integration.

## Install the connector

- On the Shopware backoffice, go to **Extensions** -> **My extensions** ->
**Shopware Account**, fill in your credentials, and click **Login**.
- Go to **Extensions** -> **Store**, and in the search bar enter “Stripe”.
- Click **Stripe** -> **Add extension** -> **Add extension for free**.
- Click **Install extension**.

After the installation finishes, Stripe is available in **My extensions**.

Make sure to test the connector before deploying it to production, because your
environment might differ from other users’ environments.

#### Note

Don’t duplicate your production shop to use it as a staging environment. That
can corrupt the data associated with the original production shop, due to the
Shopware App infrastructure.

## Add Stripe as a payment method

When the installation completes, view the connector on your extensions page in
the Shopware administration panel.

- In the admin panel sidebar, under **Sales Channels**, select your [sales
channel](https://docs.shopware.com/en/shopware-6-en/settings/saleschannel) to
add Stripe as a payment method.
- Under **Payment and shipping**, select **Pay with Stripe** from the **Payment
methods** drop-down.
- *(Optional)* To display Stripe first at checkout, select **Pay with Stripe**
from the **Default payment method** drop-down.
- Click **Save**.

## Update the connector

Use the Shopware administration panel to update the connector when a new version
is available. Under **Extensions**, select **My extensions**. To initialize the
update process, select **Update** on the **Apps** tab for the Stripe connector.

## See also

- [Overview](https://docs.stripe.com/connectors/shopware6)
- [Configure the
connector](https://docs.stripe.com/connectors/shopware6/configuration)

## Links

- [Shopware 6](https://www.shopware.com/en/)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [sales
channel](https://docs.shopware.com/en/shopware-6-en/settings/saleschannel)
- [Overview](https://docs.stripe.com/connectors/shopware6)
- [Configure the
connector](https://docs.stripe.com/connectors/shopware6/configuration)