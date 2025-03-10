# Account management

## Show account details and allow them to be edited.

Account management renders a UI component for connected accounts to view and
manage their account details. Connected accounts can view and edit account
information such as personal or business information, public information, and
bank accounts they use for payouts.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
## Requirements collection options

When a connected account has outstanding
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements),
embedded account management prompts the connected account to update their
information. You can control the collection of `currently_due` or
`eventually_due` requirements, and whether to include [future
requirements](https://docs.stripe.com/connect/handle-verification-updates),
using the `collectionOptions` attribute.

## The details submitted attribute

The account management component renders only for accounts where the
[details_submitted](https://docs.stripe.com/api/accounts/object#account_object-details_submitted)
attribute is `true`. If an account hasn’t gone through onboarding, the account
management component fails to render. In this scenario, we recommend using the
[account
onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
component.

## Displayed fields

The [fields](https://docs.stripe.com/connect/required-verification-information)
that the account management component displays depend on how you configured the
connected account—specifically on the connected account country, business type,
capabilities and service agreement type. This works similarly to how the
[onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
only collects the information that’s required for how the connected account is
configured.

## External account collection

Use the
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_management-features-external_account_collection)
feature to control whether the component collects external account information.
This parameter is enabled by default, and only platforms responsible for
collecting updated information when requirements are due or change (including
Custom accounts) can disable it. When `external_account_collection` is enabled,
[user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
is required. You can opt out of Stripe user authentication with the
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_management-features-disable_stripe_user_authentication)
parameter.

## Disable Stripe user authentication

Use the
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_management-features-disable_stripe_user_authentication)
feature to control whether the component requires Stripe user authentication.
The default value is the opposite of the
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_management-features-external_account_collection)
value. For example, if you don’t set `external_account_collection`, it defaults
to true and `disable_stripe_user_authentication` defaults to false. This value
can only be true for accounts where `controller.requirement_collection` is
`application`.

We recommend implementing 2FA or equivalent security measures as a [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs).
For account configurations that support this feature, such as Custom accounts,
you assume liability for connected accounts if they can’t pay back [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability).

### Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable account
management by specifying `account_management` in the `components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[account_management][enabled]"=true \
-d "components[account_management][features][external_account_collection]"=true
```

### Render the account management component

```
// Include this element in your HTML
const accountManagement = stripeConnectInstance.create('account-management');
container.appendChild(accountManagement);

// Optional:
// accountManagement.setCollectionOptions({
// fields: 'eventually_due',
// futureRequirements: 'include',
// })
```

HTML + JSReactMethodTypeDescriptionDefault`setCollectionOptions``{ fields:
'currently_due' | 'eventually_due', future_requirements: 'omit' | 'include'
}`Customizes collecting `currently_due` or `eventually_due` requirements and
controls whether to include [future
requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements).
Specifying `eventually_due` collects both `eventually_due` and `currently_due`
requirements.`{fields: 'currently_due', futureRequirements: 'omit'}`

## Links

- [furever.dev](https://furever.dev)
-
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
- [future
requirements](https://docs.stripe.com/connect/handle-verification-updates)
-
[details_submitted](https://docs.stripe.com/api/accounts/object#account_object-details_submitted)
- [account
onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
- [fields](https://docs.stripe.com/connect/required-verification-information)
-
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_management-features-external_account_collection)
- [user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
-
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_management-features-disable_stripe_user_authentication)
- [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs)
- [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [future
requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements)