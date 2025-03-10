# Legal Entity Sharing

## Streamline connected account onboarding by sharing business information across accounts that belong to the same owner.

Legal Entity Sharing enables a connected account owner to reuse certain business
information, such as their legal company name or business details, during
account onboarding. The information can come from their Stripe user account or
from an existing connected account that they own. They don’t have to resubmit
that information or repeat related Know Your Customer (KYC) processes.

Some shared information remains synchronized between accounts. If the account
owner updates it on one account, the update automatically applies to all shared
accounts.

## Use Case Example

Emma, an artisan jeweler, has been selling her wares through a personal website
that accepts payments using Stripe Checkout. Looking to expand her business, she
discovers an online marketplace called Artisan Market and decides to sign up.
Artisan Market is a Stripe Connect platform.

Because Emma is the sole proprietor for both her website and her new marketplace
venture, they share the same legal entity information. When Emma onboards her
connected account for Artisan Market, Legal Entity Sharing lets her reuse some
of the information she provided when setting up payments for her website. She
doesn’t have to resubmit documentation for that information.

The wider exposure increases Emma’s sales, and she decides to expand by moving
her business from her home studio to a dedicated workshop in a commercial
building. Because Legal Entity Sharing synchronizes company address information
between shared accounts, Emma only needs to update the business address on one
of her accounts. Legal Entity Sharing automatically updates the address on the
other account.

## Availability

Legal Entity Sharing is available for accounts where Stripe is responsible for
collecting requirements (the account’s
[controller.requirement_collection](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
is `stripe`).

For accounts where
[controller.requirement_collection](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
is `platform`, including Custom accounts, the account owner can copy some
existing account information during onboarding. However, sharing doesn’t apply
to future updates. Each account must be updated individually.

If the platform has requested any
[capabilities](https://docs.stripe.com/api/accounts/object#account_object-capabilities)
for the new account, the owner can only share information from accounts in the
same country as the new account. Otherwise, they can share information from any
of their existing accounts.

[Stripe-hosted](https://docs.stripe.com/connect/hosted-onboarding) and
[embedded](https://docs.stripe.com/connect/embedded-onboarding) onboarding flows
support Legal Entity Sharing. However, embedded onboarding flows require [Stripe
user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components?platform=web#user-authentication-in-connect-embedded-components).
If you set
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features-disable_stripe_user_authentication)
to true, your embedded onboarding flow can’t use Legal Entity Sharing.

API based onboarding flows can’t use Legal Entity Sharing.

When a legal entity is shared between accounts, some information is synchronized
between shared accounts. If the account owner changes that information on one
account, the changes automatically apply to all shared accounts. Other
information can be copied from existing accounts during onboarding, but future
updates to it aren’t synchronized.

#### Note

During onboarding, Stripe offers Legal Entity Sharing if the authenticated
account owner has any existing accounts. The owner can select an existing
account to share information with the new account, or they can choose to set up
the new account from scratch. If they set up the new account from scratch, they
can’t share it with existing accounts later. However, they can select it to
share information when onboarding new accounts.

Legal Entity Sharing shares the following information between
[Accounts](https://docs.stripe.com/api/accounts/object), and updates on one
account automatically apply to shared accounts:

-
[business_type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
- [country](https://docs.stripe.com/api/accounts/object#account_object-country)
- [company](https://docs.stripe.com/api/accounts/object#account_object-company)
-
[individual](https://docs.stripe.com/api/accounts/object#account_object-individual)

Legal Entity Sharing copies the following information from an existing account
during onboarding. However, future updates to this information aren’t
automatically copied to shared accounts:

-
[external_accounts](https://docs.stripe.com/api/accounts/object#account_object-external_accounts)
-
[business_profile](https://docs.stripe.com/api/accounts/object#account_object-business_profile)
-
[settings.payments.statement_descriptor](https://docs.stripe.com/api/accounts/object#account_object-settings-payments-statement_descriptor)
-
[settings.card_payments.statement_descriptor_prefix](https://docs.stripe.com/api/accounts/object#account_object-settings-card_payments-statement_descriptor_prefix)
-
[settings.branding](https://docs.stripe.com/api/accounts/object#account_object-settings-branding)

## Manage access

If you don’t want to offer this feature to your connected accounts during
onboarding, you can disable it from your
[Dashboard](https://dashboard.stripe.com/settings/connect/onboarding-options/le-sharing).

Disabling Legal Entity Sharing doesn’t affect existing accounts that already use
the feature. It only hides the feature from new connected accounts.

## Links

-
[controller.requirement_collection](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
-
[capabilities](https://docs.stripe.com/api/accounts/object#account_object-capabilities)
- [Stripe-hosted](https://docs.stripe.com/connect/hosted-onboarding)
- [embedded](https://docs.stripe.com/connect/embedded-onboarding)
- [Stripe user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components?platform=web#user-authentication-in-connect-embedded-components)
-
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features-disable_stripe_user_authentication)
- [Accounts](https://docs.stripe.com/api/accounts/object)
-
[business_type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
- [country](https://docs.stripe.com/api/accounts/object#account_object-country)
- [company](https://docs.stripe.com/api/accounts/object#account_object-company)
-
[individual](https://docs.stripe.com/api/accounts/object#account_object-individual)
-
[external_accounts](https://docs.stripe.com/api/accounts/object#account_object-external_accounts)
-
[business_profile](https://docs.stripe.com/api/accounts/object#account_object-business_profile)
-
[settings.payments.statement_descriptor](https://docs.stripe.com/api/accounts/object#account_object-settings-payments-statement_descriptor)
-
[settings.card_payments.statement_descriptor_prefix](https://docs.stripe.com/api/accounts/object#account_object-settings-card_payments-statement_descriptor_prefix)
-
[settings.branding](https://docs.stripe.com/api/accounts/object#account_object-settings-branding)
-
[Dashboard](https://dashboard.stripe.com/settings/connect/onboarding-options/le-sharing)