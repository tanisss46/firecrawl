# Stripe Connector for Shopware 6 Troubleshooting

## Avoid and resolve issues with your Stripe Connector for Shopware 6.

## Webhook failed notifications

The app doesn’t create any webhooks on the client side because all
synchronizations go through our systems. You might still receive **Webhook
failed** emails if you still have an old webhook registered from the previous
Stripe plugin before transitioning to the app. The webhook doesn’t interfere
with the app functionality.

To disable the webhook and stop receiving these emails:

- In the [Dashboard webhooks](https://dashboard.stripe.com/webhooks) page, click
the URL for the old webhook from the list.
- Click the overflow menu () and choose **Delete**.
- Click **Delete webhook**.

## Synchronization issues

Shopware is aware of the following [know
issues](https://developer.shopware.com/docs/guides/plugins/apps/app-base-guide.html#handling-the-migration-of-shops)
related to shop synchronization.

- If a shop migrates to new servers or otherwise changes its URL, the URL you
saved during registration might be invalid, breaking connectivity from the app.
- If a running **PRODUCTION** shop duplicates its entire database to create a
**STAGING** environment, it might result in corrupt data because both
environments have the same `shopId`. You might also receive webhooks from both
shops (prod & staging) that look like they came from the same shop.

You can resolve these issues by reinstalling the Stripe Payments for Shopware 6
App on the **PRODUCTION** environment. This action renews the credentials and
the connection between the Stripe Payments for Shopware 6 App and the Shopware
instance that you have on **PRODUCTION**.

Make sure the other Shopware instances (such as a STAGING or DEV environment)
won’t interfere with the PRODUCTION environment by performing a clean install,
with a fresh database. Don’t duplicate it from the PRODUCTION environment.

If it isn’t possible to use a new database, delete the `core.app.shopId` row
entry from the `system_config table` to reset the configuration for all
installed applications. Then reinstall the Stripe Payments for Shopware 6 App to
establish new IDs and credentials.

To reinstall the Stripe Payments for Shopware 6 App:

- Open your Shopware instance’s Admin page.
- In the left panel, navigate to **Extensions** >> **My Extensions**.
- Find the **Stripe Payments for Shopware 6 App** and click on the overflow menu
() to open the actions dialog. Then select **Uninstall**.
- Click **Uninstall**.
- After the page refreshes, click **Install the App**.

## Links

- [Dashboard webhooks](https://dashboard.stripe.com/webhooks)
- [know
issues](https://developer.shopware.com/docs/guides/plugins/apps/app-base-guide.html#handling-the-migration-of-shops)