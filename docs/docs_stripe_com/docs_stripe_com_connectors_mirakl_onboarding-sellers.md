# Onboarding sellers

## Set up your sellers as Stripe connected accounts.

You can use [Express](https://docs.stripe.com/connect/express-accounts) or
[Custom](https://docs.stripe.com/connect/custom-accounts) accounts with the
[transfers](https://docs.stripe.com/connect/account-capabilities#transfers)
capability to onboard your sellers.

[Standard accounts](https://docs.stripe.com/connect/standard-accounts) aren’t
supported.

## Seller account initiation

The workflow starts when you create a new shop. If you invite the seller via
email, the workflow starts when they submit the initial Mirakl form.

- The [onboarding
job](https://docs.stripe.com/connectors/mirakl/reference#onboarding) fetches
newly created Mirakl shops.
- The connector adds an onboarding link to each shop.
- The seller finds the link in their Mirakl back office under **My Account**.
- They complete their KYC/KYB on Stripe.
- The seller is redirected to the `REDIRECT_ONBOARDING` URL.

Stripe then performs verification, asking for more information when needed. To
handle this, see the
[communication](https://docs.stripe.com/connectors/mirakl/onboarding-sellers#communication)
guidelines.

### Initiate the onboarding outside of Mirakl

You can build your own onboarding flow and then use the following API request to
map the Stripe account with the Mirakl shop:

```
curl \
	-X POST "https://connector-url/api/mappings" \
	-H "accept: application/json" \
	-H "X-AUTH-TOKEN: $OPERATOR_PASSWORD" \
	-H "Content-Type: application/json" \
	-d "{ \"miraklShopId\": 123, \"stripeUserId\": \"acct_1032D82eZvKYlo2C\"}"
```

## Seller account update

The workflow starts with the seller intending to update their information on
Stripe.

- The seller finds the link in their Mirakl back office under **My Account**.
- They update their information on Stripe.
- The shop custom field is updated with a fresh login link to their [Express
dashboard](https://docs.stripe.com/connect/express-dashboard).
- The KYC status is updated on Mirakl.

The last two steps are also performed when accounts are updated by the connector
during the [account initiation
workflow](https://docs.stripe.com/connectors/mirakl/onboarding-sellers#account-initiation-workflow)
or when accounts are updated by Stripe, for example, a new document needs to be
provided. You can receive a notification when that happens, see the [Account
updated](https://docs.stripe.com/connectors/mirakl/reference#account-updated)
notification.

Stripe then performs verification, asking for more information when needed. To
handle this, see the
[communication](https://docs.stripe.com/connectors/mirakl/onboarding-sellers#communication)
guidelines.

!

## Communication

You can customize the visual appearance of the Stripe form with your brand’s
name, color, and icon in your [Connect settings
page](https://dashboard.stripe.com/account/applications/settings).

Be sure to tell your sellers about the link available in their Mirakl account
settings and the need to complete the onboarding on Stripe to receive their
payouts. For example, you could customize some of the email templates sent to
your sellers by Mirakl under **Settings** > **Notifications**.

If we require more information from your sellers, we’ll email them directly for
Express accounts. You must inform the sellers yourself if you decided to use
Custom accounts.

#### Note

In test environments, no emails are sent.

## See also

- [Integration
steps](https://docs.stripe.com/connectors/mirakl#integration-steps).

## Links

- [Express](https://docs.stripe.com/connect/express-accounts)
- [Custom](https://docs.stripe.com/connect/custom-accounts)
- [transfers](https://docs.stripe.com/connect/account-capabilities#transfers)
- [Standard accounts](https://docs.stripe.com/connect/standard-accounts)
- [onboarding
job](https://docs.stripe.com/connectors/mirakl/reference#onboarding)
- [Express dashboard](https://docs.stripe.com/connect/express-dashboard)
- [Account
updated](https://docs.stripe.com/connectors/mirakl/reference#account-updated)
- [Connect settings
page](https://dashboard.stripe.com/account/applications/settings)
- [Integration
steps](https://docs.stripe.com/connectors/mirakl#integration-steps)