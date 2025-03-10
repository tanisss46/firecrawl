# Adds support for disabling Stripe user authentication for certain embedded components

## What’s new

Adds support for `disable_stripe_user_authentication` on several
`AccountSession` components.

## Impact

Previously, when using the Account Sessions API with
`external_account_collection` set to `true` for an embedded component, the
account would be required to authenticate through Stripe before using the
component. Now, for accounts where you’re responsible for collecting
requirements (such as Custom accounts), you can disable Stripe user
authentication by setting the `disable_stripe_user_authentication` feature to
`true`.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsdisable_stripe_user_authenticationAdded[AccountSession#create.components.account_management.features](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_management-features)[AccountSession#create.components.account_onboarding.features](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features)[AccountSession#create.components.balances.features](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-balances-features)
+ 7 more
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

-
[AccountSession#create.components.account_management.features](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_management-features)
-
[AccountSession#create.components.account_onboarding.features](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features)
-
[AccountSession#create.components.balances.features](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-balances-features)
-
[AccountSession#create.components.notification_banner.features](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-notification_banner-features)
-
[AccountSession#create.components.payouts.features](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-payouts-features)
-
[AccountSession.components.account_management.features](https://docs.stripe.com/api/account_sessions/object#account_session_object-components-account_management-features)
-
[AccountSession.components.account_onboarding.features](https://docs.stripe.com/api/account_sessions/object#account_session_object-components-account_onboarding-features)
-
[AccountSession.components.balances.features](https://docs.stripe.com/api/account_sessions/object#account_session_object-components-balances-features)
-
[AccountSession.components.notification_banner.features](https://docs.stripe.com/api/account_sessions/object#account_session_object-components-notification_banner-features)
-
[AccountSession.components.payouts.features](https://docs.stripe.com/api/account_sessions/object#account_session_object-components-payouts-features)
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