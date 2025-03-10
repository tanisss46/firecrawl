# Service agreement types

## A service agreement establishes the relationship between Stripe and the platform's users.

The connected account’s [service agreement
type](https://docs.stripe.com/api/accounts/object#account_object-tos_acceptance)
determines what
[capabilities](https://docs.stripe.com/connect/account-capabilities) the account
has access to, and which service agreement applies to the platform’s users.

## Supported agreement types

Connected accounts can be under one of the following service agreement types:
`full` or `recipient`. After the connected account’s service agreement is
accepted, the type of service agreement can’t be modified.

### Full service agreement

A `full` service agreement creates a service relationship between Stripe and the
connected account holder. Connected accounts under the `full` service agreement
can process card payments and request the
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments)
capability.

For the legal language, see the [Stripe Connected Account
Agreement](https://stripe.com/connect-account/legal/full).

### Recipient service agreement

A `recipient` service agreement clarifies that there is no service relationship
between Stripe and the recipient, and that the recipient’s relationship is with
the platform. Connected accounts under the recipient service agreement can’t
process payments or request the `card_payments` capability.

Transfers to `recipient` accounts take an extra 24 hours to become available in
the connected account’s balance. To learn more about `pending` balances, see the
[account balances](https://docs.stripe.com/connect/account-balances) page.

[Cross-border payouts](https://docs.stripe.com/connect/cross-border-payouts)
only work with accounts under the `recipient` service agreement. You must
explicitly pass in the country code if it differs from the platform country.

Stripe isn’t responsible for providing direct support for accounts on the
`recipient` service agreement. However, the platform can reach out to Stripe for
support for these accounts.

For the legal language, see the [Stripe Recipient
Agreement](https://stripe.com/connect-account/legal/recipient).

## Choosing the agreement type

You can specify the agreement type through the
[Accounts](https://docs.stripe.com/api/accounts) API.

### Accounts API

To choose a `recipient` service agreement when [creating an
account](https://docs.stripe.com/api#create_account), specify the agreement type
with
[tos_acceptance[service_agreement]](https://docs.stripe.com/api/accounts/object#account_object-tos_acceptance):

With controller propertiesWith account type
```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d country=US \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[fees][payer]"=application \
 -d "controller[losses][payments]"=application \
 -d "controller[requirement_collection]"=application \
 -d "capabilities[transfers][requested]"=true \
 -d "tos_acceptance[service_agreement]"=recipient
```

The same principle applies when [updating an
account](https://docs.stripe.com/api#update_account):

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "tos_acceptance[service_agreement]"=recipient
```

#### Caution

Changing the service agreement type fails if the service agreement has already
been accepted; in those cases, create a new account with the desired service
agreement.

### Connect Configuration settings

To choose a `recipient` service agreement for connected accounts with access to
the Express Dashboard, select the **Transfers** option with the **Restricted
Capability Access** icon in the [Configuration
settings](https://dashboard.stripe.com/account/applications/settings/express)
section of the Stripe Dashboard.

You can override the Configuration settings for an individual account by
specifying its capabilities and service agreement type with the Accounts API.

## Accepting the correct agreement

Stripe handles the service agreement acceptance if you use [Stripe-hosted
onboarding](https://docs.stripe.com/connect/hosted-onboarding) or [Embedded
onboarding](https://docs.stripe.com/connect/embedded-onboarding). For [API
onboarding](https://docs.stripe.com/connect/api-onboarding), the platform must
attest that their user has seen and accepted the service agreement. See [service
agreement
acceptance](https://docs.stripe.com/connect/updating-service-agreements#tos-acceptance)
for more information.

## Links

- [service agreement
type](https://docs.stripe.com/api/accounts/object#account_object-tos_acceptance)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)
-
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments)
- [Stripe Connected Account
Agreement](https://stripe.com/connect-account/legal/full)
- [account balances](https://docs.stripe.com/connect/account-balances)
- [Cross-border payouts](https://docs.stripe.com/connect/cross-border-payouts)
- [Stripe Recipient
Agreement](https://stripe.com/connect-account/legal/recipient)
- [Accounts](https://docs.stripe.com/api/accounts)
- [creating an account](https://docs.stripe.com/api#create_account)
- [updating an account](https://docs.stripe.com/api#update_account)
- [Configuration
settings](https://dashboard.stripe.com/account/applications/settings/express)
- [Stripe-hosted onboarding](https://docs.stripe.com/connect/hosted-onboarding)
- [Embedded onboarding](https://docs.stripe.com/connect/embedded-onboarding)
- [API onboarding](https://docs.stripe.com/connect/api-onboarding)
- [service agreement
acceptance](https://docs.stripe.com/connect/updating-service-agreements#tos-acceptance)