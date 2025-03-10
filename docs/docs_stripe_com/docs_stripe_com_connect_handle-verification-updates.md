# Handle verification updates

## Help your connected accounts maintain compliance with changing verification requirements.

Before your connected accounts can accept payments and send payouts, you must
fulfill what are typically called Know Your Customer (KYC) requirements. To do
so, you must collect [certain information about your connected
accounts](https://docs.stripe.com/connect/required-verification-information) and
send it to Stripe for verification.

Stripe frequently updates KYC requirements, often due to changes implemented by
financial regulators, card networks, and other financial institutions.

#### Get risk requirements with the API

As part of a current preview, you can handle current and upcoming risk-related
account issues with the
[account.requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
attribute. To learn more about how to participate in the preview, submit your
email.

These updates might require you to take the following actions:

- Modify your onboarding flow to account for the changed requirements.
- Collect updated information from affected connected accounts and handle
verification responses.
- [Handle risk-related
requirements](https://docs.stripe.com/connect/handling-api-verification) by
notifying connected accounts of identified issues so you can guide them to
resolve through Stripe interfaces.

When [upcoming requirements
updates](https://support.stripe.com/user/questions/onboarding-requirements-updates)
affect your connected accounts, we’ll notify you.

If you use embedded or Stripe-hosted onboarding, you can proactively collect
information to fulfill [future
requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements).
For embedded onboarding, include the `collectionOptions` attribute in the
[embedded onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding).
For Stripe-hosted onboarding, specify the `collection_options` parameter when
[creating account
links](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options).

### API version considerations

In [API version 2023-10-16](https://docs.stripe.com/upgrades#2023-10-16) and
later, the `account` object’s
[requirements.errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors)
array specifies the latest verification error types in the `code` attribute. We
recommend upgrading to API version 2023-10-16 and using `requirements.errors`.

If you can’t update to version 2023-10-16, earlier versions of the
`requirements.errors` array include a `detailed_code` field to return
verification errors that weren’t compatible with the `code` attribute. The
`detailed_code` attribute doesn’t appear in the API reference.

If you’re using account or remediation links to collect new requirements, set
the [API version to 2021-09-07](https://docs.stripe.com/sdks/set-version) or
later.

If you’re receiving `account.updated` events. Set the webhooks [API version to
2021-09-07](https://docs.stripe.com/upgrades#2021-09-07) or later.

## Modify your onboarding flow

### Onboarding flow options

When requirements change, we update Stripe-hosted and embedded onboarding flows
to reflect the changes. However, if you use a custom API-based onboarding flow,
you must update it to handle any changed requirements.

Regardless of the onboarding flow type, you must address requirements changes
for your existing connected accounts.

Onboarding Flow TypeDescriptionUpdate
Responsibility[API-based](https://docs.stripe.com/connect/custom/onboarding#api-based-onboarding)You
build custom flows using Stripe APIs for your connected accounts. Your
integration must meet all of Stripe’s onboarding requirements.You’re responsible
for identifying requirements changes and updating your flows to handle
them.[Embedded](https://docs.stripe.com/connect/custom/onboarding#embedded-onboarding)
new(Recommended method) Your connected accounts interact with a [highly
themeable](https://docs.stripe.com/connect/customize-connect-embedded-components)
and
[customizable](https://docs.stripe.com/connect/embedded-onboarding#customize-policies-shown-to-your-users)
UI in an embedded component without leaving your application.You don’t have to
update your onboarding flow when requirements change. Stripe automatically
updates embedded onboarding components
accordingly.[Stripe-hosted](https://docs.stripe.com/connect/custom/onboarding#stripe-hosted-onboarding)Your
application redirects your connected accounts to Stripe to complete the
onboarding process in a co-branded interface.You don’t have to update your
onboarding flow when requirements change. Stripe automatically updates hosted
onboarding accordingly.
If you use embedded components or Stripe-hosted onboarding, requirements changes
don’t require you to update your onboarding flow. Skip to the section on
[collecting updated
information](https://docs.stripe.com/connect/handle-verification-updates#collect-updated-information-from-affected-users).

If you use a custom API-based onboarding flow, handle updated requirements by
following these steps or by replacing your onboarding flow with embedded
components or Stripe-hosted onboarding.

#### Note

You can’t use the API to respond to Stripe risk reviews. You can enable your
connected accounts to respond using embedded components, Stripe-hosted
onboarding, or remediation links. You can also use the Dashboard to respond to
risk reviews on behalf of your connected accounts.

### Modify your API-based onboarding flow

#### 1. Preview updated verification requirements

When verification requirements change, you must collect updated information by
[a certain
date](https://support.stripe.com/user/questions/onboarding-requirements-updates).
Otherwise, connected accounts won’t be able to use the capabilities you request
(for example, `card_payments`). See details about the [information you need to
collect](https://docs.stripe.com/connect/required-verification-information)
based on an account’s region, capabilities requested, and other factors.

You can avoid disruption of your connected accounts’ capabilities by planning
the collection of updated information before the `current_deadline`. To preview
information about upcoming requirements changes, look at the Account object’s
[future_requirements
hash](https://docs.stripe.com/api/accounts/object#account_object-future_requirements).

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 "object": "account",
 "future_requirements": {
 "current_deadline": 1656608400,
 "currently_due": [
 "company.tax_id"
 ],
 "disabled_reason": null,
 "errors": [],
 "eventually_due": [
 "company.tax_id"
 ],
 "past_due": [],
 "pending_verification": []
 },
 ...
}
```

#### Note

If you use [Stripe Data](https://docs.stripe.com/stripe-data), you can retrieve
the `future_requirements` hash using [a Sigma
query](https://docs.stripe.com/stripe-data/query-connect-data#account-requirements).

#### 2. Add required fields to your onboarding flow

When you’ve identified the updated information you need to collect, add
corresponding fields to your onboarding flow and update your connected accounts
using the Accounts API.

To avoid disruption to your connected accounts, have your onboarding flow
address all requirements listed in the Account object’s
[future_requirements.currently_due](https://docs.stripe.com/api/accounts/object#account_object-future_requirements-currently_due)
list.

You can also prepare for requirements that will apply when an account reaches
their thresholds by considering the
[future_requirements.eventually_due](https://docs.stripe.com/api/accounts/object#account_object-future_requirements-eventually_due)
list.

#### 3. Test your updated onboarding flow

To simulate future verification requirements, create a test account using the
Accounts API with `enforce_future_requirements` in the email field. That
populates the account’s `requirements` hash with all known future verification
requirements.

With controller propertiesWith account type
```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[fees][payer]"=application \
 -d "controller[losses][payments]"=application \
 -d "controller[requirement_collection]"=application \
 -d country=US \
 -d business_type=individual \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true \
 --data-urlencode email="jenny.rosen+enforce_future_requirements@example.com"
```

To verify that your updated onboarding flow fulfills the account requirements,
onboard the test account and check its `requirements` hash. If your flow covers
all the requirements, the
[currently_due](https://docs.stripe.com/api/accounts/object#account_object-requirements-currently_due)
list is empty.

#### 4. Listen for account status changes to enable functionality

Detect account status changes by listening to the `account.updated` event. After
an account has gone through your onboarding flow, inspect the `currently_due`
and `pending_verification` lists in the account’s `requirements` hash. When both
are empty, and `requirements.disabled_reason` is null, you can enable
functionality for the account. When `payouts_enabled` is true, the account can
receive payouts. When `charges_enabled` is true, unlock payments for the
account.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 "object": "account",
 "charges_enabled": true,
 "payouts_enabled": true,
 "requirements": {
 "alternatives": [],
 "current_deadline": null,
 "currently_due": [],
 "disabled_reason": null,
 "errors": [],
 "eventually_due": [],
 "past_due": [],
 "pending_verification": []
 },
 ...
}
```

## Collect updated information from accounts with outstanding requirements

You can collect updated information from your connected accounts using embedded
components, Stripe-hosted onboarding, or the Stripe API. We recommend either
integrating embedded components or directing your connected accounts to
[Stripe-hosted onboarding using Account
Links](https://docs.stripe.com/connect/custom/hosted-onboarding).

In all cases, follow these steps:

### 1. Adjust your integration to handle new verification responses

When Stripe receives updated information about your connected accounts, it takes
time to verify the associated account fields. Until we complete verification,
assume that any related functionality remains disabled. To detect field
verification updates, listen for
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
events and inspect them for [verification
errors](https://docs.stripe.com/connect/handling-api-verification#validation-and-verification-errors).
If you don’t resolve an error before its deadline, it disables requested
capabilities for affected accounts.

A disabled capability’s `requirements` hash contains a
[disabled_reason](https://docs.stripe.com/api/capabilities/object#capability_object-requirements-disabled_reason)
that you can use to determine the action you must take. To investigate or to
provide required information, use the [Accounts to review
tab](https://docs.stripe.com/connect/dashboard/review-actionable-accounts) in
your Connect Dashboard.

### 2. Identify accounts with outstanding requirements

In your Connect Dashboard, select [Accounts to
review](https://dashboard.stripe.com/connect/accounts_to_review). It displays a
list of connected accounts with current or future outstanding requirements. You
can filter the list by account issue and status.

You can also see what information each connected account must provide, and the
deadline, in the account object’s
[future_requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements)
hash or by using a [Sigma
query](https://docs.stripe.com/stripe-data/query-connect-data).

### 3. Prepare for enforcement of updated requirements

On the enforcement date for an account (`future_requirements.current_deadline`),
the contents of the `future_requirements` hash move to the `requirements` hash
and Stripe generates an
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
event. Because this enforcement can cause more accounts to require review, use
the enforcement date as a reminder to check the [Accounts to review
tab](https://docs.stripe.com/connect/dashboard/review-actionable-accounts) in
your Connect Dashboard.

### 4. Send connected accounts to the information collection flow

If any account has
[currently_due](https://docs.stripe.com/api/accounts/object#account_object-requirements-currently_due)
requirements or [verification
errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors),
you must address them by the requirements
[current_deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline).
At that deadline, the requirements in the `requirements.currently_due` array are
added to the `requirements.past_due` array and any associated capabilities
become disabled until you provide the information and resolve the errors.

Future requirements can immediately affect an account’s capabilities when they
become current requirements. Make sure to address all requirements before their
deadlines, even if they’re still in `future_requirements`.

When your accounts have `requirements` that are `currently_due`, direct your
accounts to address any issues according to your onboarding flow or with
remediation links:

- **API-based onboarding:** Use your [custom onboarding
flow](https://docs.stripe.com/connect/custom/onboarding#api-based-onboarding),
optionally collecting `future_requirements` as well.
- **Embedded onboarding:** Render the [embedded onboarding
component](https://docs.stripe.com/connect/custom/onboarding#embedded-onboarding)
for affected accounts.
- **Stripe-hosted onboarding:** Use the [Account Links
API](https://docs.stripe.com/api/account_links) to generate a single-use link to
[Stripe-hosted
onboarding](https://docs.stripe.com/connect/custom/onboarding#stripe-hosted-onboarding).
Send your connected accounts to this link from your application.
- **Remediation links:** Use the Dashboard to generate [remediation
links](https://docs.stripe.com/connect/dashboard/remediation-links) that your
connected accounts can use to provide required information.

## See also

- [Handling verification with the
API](https://docs.stripe.com/connect/handling-api-verification)
- [Required verification
information](https://docs.stripe.com/connect/required-verification-information)
- [Testing Connect](https://docs.stripe.com/connect/testing)
- [Testing account identity
verification](https://docs.stripe.com/connect/testing-verification)

## Links

- [certain information about your connected
accounts](https://docs.stripe.com/connect/required-verification-information)
-
[account.requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
- [Handle risk-related
requirements](https://docs.stripe.com/connect/handling-api-verification)
- [upcoming requirements
updates](https://support.stripe.com/user/questions/onboarding-requirements-updates)
- [future
requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements)
- [embedded onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
- [creating account
links](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options)
- [API version 2023-10-16](https://docs.stripe.com/upgrades#2023-10-16)
-
[requirements.errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors)
- [API version to 2021-09-07](https://docs.stripe.com/sdks/set-version)
- [API version to 2021-09-07](https://docs.stripe.com/upgrades#2021-09-07)
-
[API-based](https://docs.stripe.com/connect/custom/onboarding#api-based-onboarding)
-
[Embedded](https://docs.stripe.com/connect/custom/onboarding#embedded-onboarding)
- [highly
themeable](https://docs.stripe.com/connect/customize-connect-embedded-components)
-
[customizable](https://docs.stripe.com/connect/embedded-onboarding#customize-policies-shown-to-your-users)
-
[Stripe-hosted](https://docs.stripe.com/connect/custom/onboarding#stripe-hosted-onboarding)
- [Stripe Data](https://docs.stripe.com/stripe-data)
- [a Sigma
query](https://docs.stripe.com/stripe-data/query-connect-data#account-requirements)
-
[future_requirements.currently_due](https://docs.stripe.com/api/accounts/object#account_object-future_requirements-currently_due)
-
[future_requirements.eventually_due](https://docs.stripe.com/api/accounts/object#account_object-future_requirements-eventually_due)
-
[currently_due](https://docs.stripe.com/api/accounts/object#account_object-requirements-currently_due)
- [Stripe-hosted onboarding using Account
Links](https://docs.stripe.com/connect/custom/hosted-onboarding)
-
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
- [verification
errors](https://docs.stripe.com/connect/handling-api-verification#validation-and-verification-errors)
-
[disabled_reason](https://docs.stripe.com/api/capabilities/object#capability_object-requirements-disabled_reason)
- [Accounts to review
tab](https://docs.stripe.com/connect/dashboard/review-actionable-accounts)
- [Accounts to review](https://dashboard.stripe.com/connect/accounts_to_review)
- [Sigma query](https://docs.stripe.com/stripe-data/query-connect-data)
-
[current_deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline)
- [Account Links API](https://docs.stripe.com/api/account_links)
- [remediation
links](https://docs.stripe.com/connect/dashboard/remediation-links)
- [Testing Connect](https://docs.stripe.com/connect/testing)
- [Testing account identity
verification](https://docs.stripe.com/connect/testing-verification)