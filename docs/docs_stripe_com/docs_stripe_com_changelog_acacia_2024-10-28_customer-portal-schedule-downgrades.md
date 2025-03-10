# Adds scheduled subscription downgrades in the customer portal

## What’s new

You can now configure the customer portal so that subscription downgrades occur
at the end of the billing cycle, rather than immediately.

You can [manage downgrades in the
Dashboard](https://docs.stripe.com/customer-management/configure-portal#downgrades)
or by using the
[schedule_at_period_end](https://docs.stripe.com/api/customer_portal/configurations/create#create_portal_configuration-features-subscription_update-schedule_at_period_end)
when you [create a portal
configuration](https://docs.stripe.com/api/customer_portal/configurations/create)
through the API.

## Impact

Previously, customers on higher cost plans that allocated credits that switched
to a lower cost plans would be given access to the remaining credits on the
higher cost plan. This change makes it possible for downgrades to occur at the
end of a billing cycle, preventing the credit issue.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsschedule_at_period_endAdded[BillingPortal.Configuration#create.features.subscription_update](https://docs.stripe.com/api/customer_portal/configurations/create#create_portal_configuration-features-subscription_update)[BillingPortal.Configuration#update.features.subscription_update](https://docs.stripe.com/api/customer_portal/configurations/update#update_portal_configuration-features-subscription_update)[BillingPortal.Configuration.features.subscription_update](https://docs.stripe.com/api/customer_portal/configurations/object#portal_configuration_object-features-subscription_update)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-10-28.acacia`
- Upgrade the API version used for [webhook
endpoints](https://docs.stripe.com/webhooks/versioning).
- [Test your integration](https://docs.stripe.com/testing) against the new
version.
- If you use Connect, [test your Connect
integration](https://docs.stripe.com/connect/testing).
- In Workbench, [perform the
upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade). You can [roll
back the version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades).

## Links

- [manage downgrades in the
Dashboard](https://docs.stripe.com/customer-management/configure-portal#downgrades)
-
[schedule_at_period_end](https://docs.stripe.com/api/customer_portal/configurations/create#create_portal_configuration-features-subscription_update-schedule_at_period_end)
- [create a portal
configuration](https://docs.stripe.com/api/customer_portal/configurations/create)
-
[BillingPortal.Configuration#create.features.subscription_update](https://docs.stripe.com/api/customer_portal/configurations/create#create_portal_configuration-features-subscription_update)
-
[BillingPortal.Configuration#update.features.subscription_update](https://docs.stripe.com/api/customer_portal/configurations/update#update_portal_configuration-features-subscription_update)
-
[BillingPortal.Configuration.features.subscription_update](https://docs.stripe.com/api/customer_portal/configurations/object#portal_configuration_object-features-subscription_update)
- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
- [API requests](https://docs.stripe.com/api/versioning)
- [webhook endpoints](https://docs.stripe.com/webhooks/versioning)
- [Test your integration](https://docs.stripe.com/testing)
- [test your Connect integration](https://docs.stripe.com/connect/testing)
- [perform the upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade)
- [roll back the
version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
- [Stripe API upgrades](https://docs.stripe.com/upgrades)