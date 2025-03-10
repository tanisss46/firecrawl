# Migrating accounts to Stripe

## Start processing accounts on Stripe without disrupting payments.

Stripe enables you to migrate your existing connected accounts along with your
payment and customer data. Doing so allows you to continue to [collect payments
and pay out](https://docs.stripe.com/connect/collect-then-transfer-guide) or
[enable other businesses to accept payments
directly](https://docs.stripe.com/connect/enable-payment-acceptance-guide). To
successfully bring your existing platform business to Stripe, you need to:

- Create a migration plan and timeline
- Update your integration for connected accounts
- Create and onboard accounts
- Handle outstanding and ongoing requirements
- Migrate payment and customer data to Stripe

## Create a migration plan

A successful migration to Stripe includes a migration plan, a timeline, and KYC
information for connected accounts, as well as payment and customer data.

Connected accounts must onboard to Stripe, which requires sending Stripe Know
Your Customer (KYC) data for each account. Stripe’s requirements can require
collecting additional information from your accounts. Perform an analysis to
understand what data has been collected with your previous provider and what
data Stripe requires. Stripe verifies KYC data before activating connected
accounts. Monitor account verification status using the
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
event or the [Retrieve Account](https://docs.stripe.com/api/account/retrieve)
API. Accounts that fail to verify require action before they’re activated.

Include a hard cutover date for payment data after onboarding accounts to
Stripe. Payment and customer data requires [a PAN
import](https://docs.stripe.com/get-started/data-migrations/pan-import) as part
of the cutover. We recommend that you import accounts in batches.

## Update your integration

Your application can require changes as part of the integration updates to
migrate to Stripe. For example, consider any changes to your connected accounts’
usage of your platform, such as pricing updates. Stripe recommends communicating
any changes to your accounts ahead of time.

### Stripe terms of service agreement

Your connected accounts must accept the Stripe terms of service before they’re
activated.

For accounts where Stripe is responsible for collecting updated information when
requirements are due or change (including Standard and Express accounts), the
account accepts Stripe’s terms of service as part of the onboarding flow.

If your platform is responsible for [collecting updated
information](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
from a connected account (including Custom accounts) when requirements change,
you can [wrap Stripe’s terms of service in your own terms of
service](https://docs.stripe.com/connect/updating-service-agreements#adding-stripes-service-agreement-to-your-terms-of-service).
We recommend placing terms of service acceptance at the end of the onboarding
flow, but you can also have it at the start if that makes more sense for your
business. When creating or updating connected accounts, record acceptance of the
[updated Terms of Service
information](https://docs.stripe.com/api/accounts/update#update_account-tos_acceptance)
to send to Stripe, and communicate that to the accounts.

### Onboard connected accounts to Stripe

Stripe offers different levels of onboarding support for your connected
accounts. Build an onboarding flow for your connected accounts using any of the
following methods:

MethodProsCons[Stripe-hosted
onboarding](https://docs.stripe.com/connect/custom/onboarding#stripe-hosted-onboarding)-
Lowest effort integration
- Stripe-branded with limited platform branding
- Limited control over the flow logic
- Connected accounts redirect to Stripe instead of completing the process
without leaving your site
[Embedded
onboarding](https://docs.stripe.com/connect/custom/onboarding#embedded-onboarding)-
[Highly
themeable](https://docs.stripe.com/connect/customize-connect-embedded-components)
- Limited or no Stripe branding
- Connected accounts remain in the flow of your site
- Low effort integration
- Limited control over the flow logic
[API-based
onboarding](https://docs.stripe.com/connect/custom/onboarding#api-based-onboarding)
- Exercise full control over your own UI
- Expensive and time-consuming to build
- Continuing high maintenance, especially to keep in compliance with changing
global requirements
- Can’t resolve Stripe risk reviews

## Create and onboard accounts

The following is an overview of the process:

[Get requirements for
account](https://docs.stripe.com/connect/required-verification-information)

Collect account data

[Create
account](https://docs.stripe.com/connect/custom/onboarding#create-the-connected-account)

If `requirements.currently_due` isn’t empty

Do you have the information?

Present a [dynamically generated
UI](https://docs.stripe.com/connect/custom/onboarding#create-forms-to-collect-information)
to collect and validate fields

Use a [Stripe
UI](https://docs.stripe.com/connect/custom/onboarding#embedded-onboarding) to
collect and validate fields

[Update the
account](https://docs.stripe.com/connect/custom/onboarding#update-the-connected-account)
with collected fields

Yes
### Establish account requirements

The following factors affect the [onboarding
requirements](https://docs.stripe.com/connect/required-verification-information)
for your connected accounts:

- The origin country of the connected accounts
- The [service agreement
type](https://docs.stripe.com/connect/service-agreement-types) applicable to the
connected accounts
- The [capabilities](https://docs.stripe.com/connect/account-capabilities)
requested for the connected accounts
- The [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
(for example, individual or company) and
[company.structure](https://docs.stripe.com/api/accounts/object#account_object-company-structure)
(for example, public corporation or private partnership)

Use the interactive form to see how changing these factors affects the
requirements.

### Requirements form

### Create the connected account

For each account to be migrated to Stripe, create an associated Account.

StandardExpressCustomController properties
Use the [Create Account](https://docs.stripe.com/api/accounts/create) API to
create a connected account with `controller` set to the desired account
preferences. You can prefill any information, but at a minimum, you must specify
the `controller`. The country of the account defaults to the same country as
your platform, and the account confirms the selection during onboarding.

#### Note

This example includes only some of the fields you can set when creating an
account. For a full list of the fields you can set, such as `address` and
`website_url`, see the [Create Account API
reference](https://docs.stripe.com/api/accounts/create).

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "controller[fees][payer]"=account \
 -d "controller[losses][payments]"=stripe \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[requirement_collection]"=stripe \
 -d country=US \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true
```

If you’ve already collected information for your connected accounts, you can
prefill that information on the `Account` object. You can prefill any account
information, including personal and business information, external account
information, and so on.

Connect Onboarding doesn’t ask for the prefilled information. However, it does
ask the account holder to confirm the prefilled information before accepting the
[Connect service
agreement](https://docs.stripe.com/connect/service-agreement-types).

When testing your integration, prefill account information using [test
data](https://docs.stripe.com/connect/testing).

Successful creation returns the [account
object](https://docs.stripe.com/api/accounts/object). Inspect the object for the
connected account `id` and store the value in your database.

```
{
 ...
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 ...
}
```

After updating Stripe with all existing data, look for any outstanding
requirements. Any outstanding requirements are listed in the `currently_due`
array. All `currently_due` requirements need to be collected from the account
for Stripe to verify the account and activate the account’s capabilities.

```
{
 ...
 "requirements": {
 "alternatives": [],
 "current_deadline": null,
 "currently_due": [
 "business_profile.url",
 "external_account",
 "individual.first_name",
 "individual.last_name",
 "tos_acceptance.date",
 "tos_acceptance.ip"
 ],
 "disabled_reason": "requirements.past_due",
 "errors": [],
```

See all 36 lines
After providing all existing data on an account, direct the account to a Stripe
UI to set up Stripe credentials, confirm the information, and accept the Stripe
terms of service.

### Take new accounts through an onboarding flow

In addition to migrating existing accounts, build a flow for new accounts to
onboard to Stripe. You can also use this onboarding flow to collect missing data
for accounts being migrated.

Review [onboarding options](https://docs.stripe.com/connect/onboarding) to
create your onboarding flow.

## Handle outstanding and ongoing requirements

When the connected account’s data is submitted, Stripe verifies it. This process
might take minutes or hours depending on the nature of the verification
required. During this process, the capabilities you requested have [a pending
status](https://docs.stripe.com/api/accounts/object#account_object-capabilities).

### Review status

You can retrieve the status of your connected account’s capabilities by:

- Inspecting the Account object’s
[capabilities](https://docs.stripe.com/api/accounts/object#account_object-capabilities)
hash for the relevant capability.
- Requesting capabilities directly from the [Capabilities
API](https://docs.stripe.com/api/capabilities/retrieve) and inspecting the
status of the relevant capability.
- Listening for `account.updated`
[events](https://docs.stripe.com/api/events/types#event_types-account.updated)
in your [webhook](https://docs.stripe.com/connect/webhooks) endpoint and
inspecting the `capabilities` hash for the relevant capability.

After verifications are complete, the capability becomes `active` and available
to the connected account. Account verifications run continuously, and if a
future verification fails, a capability can transition out of `active`. Listen
for `account.updated` events to detect changes to capability states.

Confirm that your Connect integration is compliant and operational by checking
that the account’s `charges_enabled` and `payouts_enabled` are both true. You
can use the API or listen for `account.updated` events. For details on other
relevant fields, check the account’s
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
hash. You can’t confirm the integration based on a single value because statuses
can vary depending on the application and related policies.

-
[charges_enabled](https://docs.stripe.com/api/accounts/object#account_object-charges_enabled)
confirms that your full charge path including the charge and transfer works
correctly and evaluates if either `card_payments` or `transfers` capabilities
are active.
-
[payouts_enabled](https://docs.stripe.com/api/accounts/object#account_object-payouts_enabled)
evaluates whether your connected account can pay out to an external account.
Depending on your risk policies, you can allow your connected account to start
transacting without payouts enabled. You [must eventually enable
payouts](https://docs.stripe.com/connect/manage-payout-schedule) to pay your
connected accounts.

You can use the following logic as a starting point for defining a summary
status to display to your connected account.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

def account_state(account)
 reqs = account.requirements

 if reqs.disabled_reason && reqs.disabled_reason.include?("rejected")
 "rejected"
 elsif account.payouts_enabled && account.charges_enabled
 if reqs.pending_verification
 "pending enablement"
 elsif !reqs.disabled_reason && !reqs.currently_due
 if !reqs.eventually_due
 "complete"
 else
 "enabled"
 end
 else
 "restricted"
 end
 elsif !account.payouts_enabled && account.charges_enabled
 "restricted (payouts disabled)"
 elsif !account.charges_enabled && account.payouts_enabled
 "restricted (charges disabled)"
 elsif reqs.past_due
 "restricted (past due)"
 elsif reqs.pending_verification
 "pending (disabled)"
 else
 "restricted"
 end
end

accounts = Stripe::Account.list(limit: 10)

accounts.each do |account|
 puts "#{account.id} has state: #{account_state(account)}"
end
```

### Handle verification errors

Handle verification failures differently depending on your onboarding flow.

#### Note

You can’t use the API to respond to Stripe risk reviews. You can enable your
connected accounts to respond using embedded components, Stripe-hosted
onboarding, or remediation links. You can also use the Dashboard to respond to
risk reviews on behalf of your connected accounts.

APIEmbeddedHosted
Listen to the
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
event. If the account contains any `currently_due` fields when the
`current_deadline` arrives, the corresponding functionality is disabled and
those fields are added to `past_due`.

[Create a
form](https://docs.stripe.com/connect/migrate-to-stripe#create-forms-to-collect-information)
with clear instructions that the account can use to correct the information.
Notify the account, then [submit the corrected
information](https://docs.stripe.com/connect/migrate-to-stripe#update-the-connected-account)
using the Accounts API.

[account.updated
event](https://docs.stripe.com/api/events/types#event_types-account.updated)

If `requirements.currently_due` contains fields

Direct account to onboarding in time to finish before
[current_deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline)

No action required

If `requirements.past_due` contains fields

Account possibly disabled; direct it to onboarding

Present [dynamically generated
UI](https://docs.stripe.com/connect/custom/onboarding#create-forms-to-collect-information)
to collect and validate fields

[Update
account](https://docs.stripe.com/connect/custom/onboarding#update-the-connected-account)
with fields collected

If `requirements.currently_due` contains fields

YesNo
If you plan to create custom flows to handle all your verification errors:

- Review the details regarding all possible [verification errors and how to
handle them](https://docs.stripe.com/connect/handling-api-verification).
- [Test verification
states](https://docs.stripe.com/connect/testing-verification).

## Migrate payment and customer data to Stripe

After your connected accounts are created on Stripe, [request a PAN data
import](https://docs.stripe.com/get-started/data-migrations/pan-import), which
migrates your payment and customer data for use on Stripe.

## See also

- [Choose your onboarding
configuration](https://docs.stripe.com/connect/onboarding)
- [Handling identity verification with the
API](https://docs.stripe.com/connect/handling-api-verification)
- [Testing account identity
verification](https://docs.stripe.com/connect/testing-verification)

## Links

- [collect payments and pay
out](https://docs.stripe.com/connect/collect-then-transfer-guide)
- [enable other businesses to accept payments
directly](https://docs.stripe.com/connect/enable-payment-acceptance-guide)
-
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
- [Retrieve Account](https://docs.stripe.com/api/account/retrieve)
- [a PAN import](https://docs.stripe.com/get-started/data-migrations/pan-import)
- [collecting updated
information](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
- [wrap Stripe’s terms of service in your own terms of
service](https://docs.stripe.com/connect/updating-service-agreements#adding-stripes-service-agreement-to-your-terms-of-service)
- [updated Terms of Service
information](https://docs.stripe.com/api/accounts/update#update_account-tos_acceptance)
- [Stripe-hosted
onboarding](https://docs.stripe.com/connect/custom/onboarding#stripe-hosted-onboarding)
- [Embedded
onboarding](https://docs.stripe.com/connect/custom/onboarding#embedded-onboarding)
- [Highly
themeable](https://docs.stripe.com/connect/customize-connect-embedded-components)
- [API-based
onboarding](https://docs.stripe.com/connect/custom/onboarding#api-based-onboarding)
- [Get requirements for
account](https://docs.stripe.com/connect/required-verification-information)
- [Create
account](https://docs.stripe.com/connect/custom/onboarding#create-the-connected-account)
- [dynamically generated
UI](https://docs.stripe.com/connect/custom/onboarding#create-forms-to-collect-information)
- [Update the
account](https://docs.stripe.com/connect/custom/onboarding#update-the-connected-account)
- [service agreement
type](https://docs.stripe.com/connect/service-agreement-types)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)
- [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
-
[company.structure](https://docs.stripe.com/api/accounts/object#account_object-company-structure)
- [Create Account](https://docs.stripe.com/api/accounts/create)
- [test data](https://docs.stripe.com/connect/testing)
- [account object](https://docs.stripe.com/api/accounts/object)
- [onboarding options](https://docs.stripe.com/connect/onboarding)
- [a pending
status](https://docs.stripe.com/api/accounts/object#account_object-capabilities)
- [Capabilities API](https://docs.stripe.com/api/capabilities/retrieve)
- [webhook](https://docs.stripe.com/connect/webhooks)
-
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
-
[charges_enabled](https://docs.stripe.com/api/accounts/object#account_object-charges_enabled)
-
[payouts_enabled](https://docs.stripe.com/api/accounts/object#account_object-payouts_enabled)
- [must eventually enable
payouts](https://docs.stripe.com/connect/manage-payout-schedule)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[current_deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline)
- [verification errors and how to handle
them](https://docs.stripe.com/connect/handling-api-verification)
- [Test verification
states](https://docs.stripe.com/connect/testing-verification)