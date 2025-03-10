# Notification banner

## Show a banner that lists required actions for risk interventions and onboarding requirements.

Renders a notification banner that lists open tasks that can affect a connected
account’s status or capabilities. Tasks can involve risk interventions or
outstanding requirements for account capabilities, such as accepting payments
and payouts. The banner renders only when the connected account must respond to
risk interventions or provide currently due requirements [after initial
onboarding](https://docs.stripe.com/connect/supported-embedded-components/notification-banner#account-onboarding).

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
## Requirements collection options

You can control the collection of `currently_due` or `eventually_due`
requirements and the inclusion of [future
requirements](https://docs.stripe.com/connect/handle-verification-updates) by
using the `collectionOptions` attribute when you integrate the notification
banner component.

## External account collection

Use the
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-notification_banner-features-external_account_collection)
feature to control whether the component collects external account information.
This parameter is enabled by default, and only platforms responsible for
collecting updated information when requirements are due or change (including
Custom accounts) can disable it. When `external_account_collection` is enabled,
[user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
is required. You can opt out of Stripe user authentication with the
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-notification_banner-features-disable_stripe_user_authentication)
parameter.

## Disable Stripe user authentication

Use the
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-notification_banner-features-disable_stripe_user_authentication)
feature to control whether the component requires Stripe user authentication.
The default value is the opposite of the
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-notification_banner-features-external_account_collection)
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
Session](https://docs.stripe.com/api/account_sessions/create), enable
notification banner by specifying `notification_banner` in the `components`
parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[notification_banner][enabled]"=true \
-d "components[notification_banner][features][external_account_collection]"=true
```

### Render the notification banner component

```
// Include this element in your HTML
const notificationBanner = stripeConnectInstance.create('notification-banner');
container.appendChild(notificationBanner);

// Optional:
// notificationBanner.setCollectionOptions({
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
## Configure custom banner behavior

You can configure custom behavior, such as different margins, for when the
banner includes any notifications or when the notifications require any action.
To do so, set a custom callback function using `onNotificationsChange`.

```
// index.html

<h1 id="notification-banner-action-warning"></h1>

<div id="notification-banner-container"></div>

// index.js
const handleNotificationsChange = (response) => {
 const warning = document.getElementById("notification-banner-action-warning");

 if (response.actionRequired > 0) {
// Do something related to required actions, such as adding margins to the
banner container or tracking the current number of notifications.
 warning.style.display = "block";
 warning.textContent =
 "You must resolve the notifications on this page before proceeding.";
 } else if (response.total > 0) {
 // Do something related to notifications that don't require action.
 warning.style.display = "block";
 warning.textContent = "The items below are in review.";
 } else {
 warning.style.display = "none";
 }
};

const container = document.getElementById('notification-banner-container');
const notificationBanner = stripeConnectInstance.create('notification-banner');
notificationBanner.setOnNotificationsChange(handleNotificationsChange);
container.appendChild(notificationBanner);
```

HTML + JSReactMethodDescriptionVariables`setOnNotificationsChange`Allows users
to specify an optional custom behavior in a callback function.-
`response.total`: The total number of notifications in the banner
- `response.actionRequired`: The number of notifications that require user
action

## Testing

To test this component in test mode, specify different [test
inputs](https://docs.stripe.com/connect/testing) for fields that fail
verifications or generate requirements on the account. For example, you can use
the [account management
component](https://docs.stripe.com/connect/supported-embedded-components/account-management)
to enter `address_no_match` in `line1` of an individual’s address to trigger an
address mismatch. In production, it can be difficult to verify that this
component is working as expected because it’s hidden when an account has no
banner items. To validate your integration is working, you can:

- Set a callback using `onNotificationsChange` that verifies `response.total` is
zero
- Confirm the component is being displayed with no content using a [loader start
handler](https://docs.stripe.com/connect/get-started-connect-embedded-components#reacting-to-component-display)

## Account onboarding

Use the notification banner after the account goes through [account
onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
and has
[details_submitted](https://docs.stripe.com/api/accounts/object#account_object-details_submitted).
The banner won’t render any UI if the account is missing `details_submitted`.

## Links

- [after initial
onboarding](https://docs.stripe.com/connect/supported-embedded-components/notification-banner#account-onboarding)
- [furever.dev](https://furever.dev)
- [future
requirements](https://docs.stripe.com/connect/handle-verification-updates)
-
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-notification_banner-features-external_account_collection)
- [user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
-
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-notification_banner-features-disable_stripe_user_authentication)
- [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs)
- [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [future
requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements)
- [test inputs](https://docs.stripe.com/connect/testing)
- [account management
component](https://docs.stripe.com/connect/supported-embedded-components/account-management)
- [loader start
handler](https://docs.stripe.com/connect/get-started-connect-embedded-components#reacting-to-component-display)
- [account
onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
-
[details_submitted](https://docs.stripe.com/api/accounts/object#account_object-details_submitted)