# Use the Stripe Connector for Adobe Commerce (Magento 2)

## Learn how to install, upgrade, and uninstall the Stripe Connector for Adobe Commerce (Magento 2).

#### Caution

We recommend that you test the module before installing it in your production
environment. If you experience an installation issue, see
[Troubleshooting](https://docs.stripe.com/connectors/adobe-commerce/payments/troubleshooting).

## Install the module

From the Marketplace (recommended)From the raw package- Place an order for the
module through the [Adobe
Marketplace](https://marketplace.magento.com/stripe-stripe-payments.html).
- Open a terminal and run the following command in your Adobe Commerce
directory:

```
composer require stripe/stripe-payments
```

At this stage, you might have to submit your username and password. Provide your
[Adobe Commerce authentication
keys](https://devdocs.magento.com/guides/v2.3/install-gde/prereq/connect-auth.html).
You can accept to save your credentials when prompted by Composer. If you’ve
saved your keys and see the error `Invalid Credentials`, update your keys in
`~/.composer/auth.json` or delete this file and run the command again.

- Set up the module by running the following commands:

```
php bin/magento setup:upgrade
php bin/magento cache:flush
php bin/magento cache:clean
```
- If you run Adobe Commerce in production mode, you must also compile and deploy
the module’s static files.

```
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
```

## Upgrade the module

Before you upgrade:

- Back up your files and database.
- Start with your test environment.
- Keep a copy of any customization you made to the module’s original code.
- Check out the
[CHANGELOG](https://github.com/stripe/stripe-magento2-releases/blob/master/CHANGELOG.md).

Patch releases (x.x.Y) are backward compatible and require no extra development
on your side after you upgrade. Minor and major releases might add new features
or change code in a backwards incompatible way. If you customized the module’s
code, you’ll need to port these customizations after upgrading and resolve any
potential conflict.

From the MarketplaceFrom the raw package
Run the following commands:

```
composer remove stripe/stripe-payments
composer require stripe/stripe-payments
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
php bin/magento cache:clean
```

## Uninstall the module

Before you uninstall:

- Backup your files and database.
- Keep a copy of any customization you made to the module’s original code in
case you need to reinstall it later.
From the MarketplaceFrom the raw package
Run the following commands:

```
composer remove stripe/stripe-payments
php bin/magento setup:upgrade
php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy
php bin/magento cache:clean
```

## Lifecycle policy

The latest version of the module supports the following versions of Adobe
Commerce:

ReleaseSupportAdobe Commerce 2.0 - 2.3.6No longer supported, the last compatible
version is `stripe/stripe-payments:2.9.5`.Adobe Commerce 2.3.7 - 2.4.xCurrently
supported, see below for our own lifecycle policy.
For `stripe/stripe-payments:4.1.*` and later, we provide new features, bug
fixes, and security patches. Older versions are deprecated. Stripe recommends
that you upgrade as soon as you can. All releases are available in the Adobe
Marketplace and in the
[stripe-magento2-releases](https://github.com/stripe/stripe-magento2-releases)
GitHub repository.

## See also

- [Configuring the Stripe Connector for Adobe
Commerce](https://docs.stripe.com/connectors/adobe-commerce/payments/configuration)
- [Using the Adobe Commerce admin
panel](https://docs.stripe.com/connectors/adobe-commerce/payments/admin)
-
[Troubleshooting](https://docs.stripe.com/connectors/adobe-commerce/payments/troubleshooting)

## Links

-
[Troubleshooting](https://docs.stripe.com/connectors/adobe-commerce/payments/troubleshooting)
- [Adobe
Marketplace](https://marketplace.magento.com/stripe-stripe-payments.html)
- [Adobe Commerce authentication
keys](https://devdocs.magento.com/guides/v2.3/install-gde/prereq/connect-auth.html)
-
[CHANGELOG](https://github.com/stripe/stripe-magento2-releases/blob/master/CHANGELOG.md)
- [stripe-magento2-releases](https://github.com/stripe/stripe-magento2-releases)
- [Configuring the Stripe Connector for Adobe
Commerce](https://docs.stripe.com/connectors/adobe-commerce/payments/configuration)
- [Using the Adobe Commerce admin
panel](https://docs.stripe.com/connectors/adobe-commerce/payments/admin)