# Expands filtering support for Financial Connections Sessions

## What’s new

Expands filtering support for allowable Financial Connections Account categories
in the `Financial Connections.Session` by introducing three new values:
`mortgage`, `line_of_credit`, and `credit_card`. This is in addition to the
previously supported `checking` and `savings` values.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsaccount_subcategoriesAdded[FinancialConnections.Session#create.filters](https://docs.stripe.com/api/financial_connections/sessions/create#financial_connections_create_session-filters)[FinancialConnections.Session.filters](https://docs.stripe.com/api/financial_connections/sessions/object#financial_connections_session_object-filters)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-09-30.acacia`
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

## Related changes

- [Adds support for filtering by account subcategories on Financial
Connections](https://docs.stripe.com/changelog/acacia/2024-09-30/financial-connections-filters)

## Links

-
[FinancialConnections.Session#create.filters](https://docs.stripe.com/api/financial_connections/sessions/create#financial_connections_create_session-filters)
-
[FinancialConnections.Session.filters](https://docs.stripe.com/api/financial_connections/sessions/object#financial_connections_session_object-filters)
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
- [Adds support for filtering by account subcategories on Financial
Connections](https://docs.stripe.com/changelog/acacia/2024-09-30/financial-connections-filters)