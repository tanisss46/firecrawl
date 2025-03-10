# API onboarding

## Build your own onboarding flow using Stripe's APIs.

With API onboarding, you use the [Accounts
API](https://docs.stripe.com/api/accounts) to build an onboarding flow,
reporting functionality, and communication channels for your users. Stripe can
be completely invisible to the account holder. However, your platform is
responsible for all interactions with your accounts and for collecting all the
information needed to verify them.

#### Additional responsibilities

With API onboarding, your custom flow must meet all legal and regulatory
requirements in the regions where you do business. You must also commit
resources to track changes to those requirements and collect updated information
on an ongoing basis, at least once every six months. If you want to implement a
customized onboarding flow, Stripe strongly recommends that you use [embedded
onboarding](https://docs.stripe.com/connect/embedded-onboarding).

Onboard new user

Re-onboard existing user

[Retrieve](https://docs.stripe.com/api/accounts/retrieve) the connected account

Show UI to collect `requirements` from your user

[Create](https://docs.stripe.com/api/accounts/create) a connected account

If `requirements.currently_due` is not empty

Present forms to collect information and validate fields

Update the connected account with the collected information

[Establish
requirements](https://docs.stripe.com/connect/api-onboarding#establish-requirements)
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

[Create forms to collect
informationClient-side](https://docs.stripe.com/connect/api-onboarding#create-forms-to-collect-information)
As a best practice, organize the required parameters into logical groupings or
forms in your onboarding flow. You might wish to encode a mapping between the
Stripe parameters and the logical groupings. Suggested logical groupings for
parameters are shown in the first column of the example requirements table.

After you encode the required parameters into your application, generate UIs for
the parameters corresponding to these requirements. For each parameter, design a
UI form that includes:

- Parameter label, localized to each supported country and language
- Parameter description, localized to each supported country and language
- Parameter input fields with data validation logic and document uploading where
required

It’s important to architect your application logic to account for the
possibility of additional parameters in the future. For example, Stripe might
introduce new parameters, new verifications, or new thresholds that you must
incorporate into your onboarding flows over time.

Changing any of the factors that determine your connected accounts requirements
means you must also adjust your collection forms.
[Country](https://docs.stripe.com/api/accounts/object#account_object-country)
and [service agreement
type](https://docs.stripe.com/api/accounts/object#account_object-tos_acceptance-service_agreement)
are immutable, while
[capabilities](https://docs.stripe.com/api/accounts/object#account_object-capabilities)
and [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
are mutable.

- To change an immutable field such as country or service agreement type, create
a new connected account with the new values. Doing so produces new requirements
for you to incorporate in your collection flows.
- To change a mutable field such as capabilities or business type, update the
connected account. Doing so produces new requirements for you to incorporate in
your collection flows.

### Include Stripe Terms of Service Agreement

Your connected accounts must accept Stripe terms of service before they can be
activated. You can [wrap Stripe terms of service in your own terms of
service](https://docs.stripe.com/connect/updating-service-agreements#adding-stripes-service-agreement-to-your-terms-of-service).

[Create a connected
accountServer-side](https://docs.stripe.com/connect/api-onboarding#create-account)
Create a [connected account](https://docs.stripe.com/api/accounts) where your
platform is liable for negative balances, Stripe collects fees from your
platform account, and your connected accounts don’t have access to a
Stripe-hosted dashboard. Request any capabilities that your connected accounts
need. Include business type and any other information matching your
[requirements](https://docs.stripe.com/connect/api-onboarding#establish-requirements)
if you have it available to prefill.

Alternatively, you can create a connected account with `type` set to `custom`
and desired capabilities.

If you don’t specify the country and service type agreement, they’re assigned
the following default values:

- The `country` defaults to the same country as your platform.
- The service type agreement (`tos_acceptance.service_agreement`) defaults to
`full`.
With controller propertiesWith an account type
```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "controller[losses][payments]"=application \
 -d "controller[fees][payer]"=application \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[requirement_collection]"=application \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true \
 -d business_type=individual \
 -d country=US
```

[Determine the information to
collectServer-side](https://docs.stripe.com/connect/api-onboarding#determine-information-to-collect)
As the platform, you must decide if you want to collect the required information
from your connected accounts upfront or incrementally. Upfront onboarding
collects the `eventually_due` requirements for the account, while incremental
onboarding only collects the `currently_due` requirements.

Upfront onboarding Incremental onboarding Advantages- Entails a single request
for information (normally)
- Creates fewer problems in receiving payouts and maintaining processing ability
- Exposes potential fraudsters or connected accounts who refuse to provide
required information later
- Onboards connected accounts quickly
- Results in higher onboarding rates
Disadvantages- Onboarding connected accounts can take longer
- Some legitimate new connected accounts might turn away due to the amount of
information required before they complete the onboarding process
- Creates a higher likelihood of disrupting business of an ongoing connected
account

To determine whether to use upfront or incremental onboarding, review the
[required
information](https://docs.stripe.com/connect/required-verification-information)
for the countries where your connected accounts are located to understand the
requirements that are eventually due. While Stripe tries to minimize any impact
to connected accounts, requirements might change over time.

For connected accounts where you’re responsible for requirement collection, you
can customize the behavior of [future
requirements](https://docs.stripe.com/connect/handle-verification-updates) using
the `collection_options` parameter. Set
[collection_options.future_requirements](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options-future_requirements)
to `include` to collect the account’s future requirements.

To implement your onboarding strategy, inspect the requirements hash of the
connected account you created. The requirements hash provides a complete list of
parameters you must collect to activate the connected account.

- For incremental onboarding, inspect the `currently_due` field in the
requirements hash and build an onboarding flow that only collects for the listed
parameters.
- For upfront onboarding, inspect the `eventually_due` field in the requirements
hash and build an onboarding flow that collects for all the listed parameters.

```
{
 ...
 "requirements": {
 "alternatives": [],
 "current_deadline": null,
 "currently_due": [
 "business_profile.product_description",
 "business_profile.support_phone",
 "business_profile.url",
 "external_account",
 "tos_acceptance.date",
 "tos_acceptance.ip"
 ],
 "disabled_reason": "requirements.past_due",
 "errors": [],
 "eventually_due": [
 "business_profile.product_description",
 "business_profile.support_phone",
 "business_profile.url",
 "external_account",
 "tos_acceptance.date",
 "tos_acceptance.ip"
 ],
 "past_due": [],
 "pending_verification": []
 },
 ...
}
```

[Handle liveness
requirements](https://docs.stripe.com/connect/api-onboarding#proof-of-liveness)
An account can have one or more Persons with a `proof_of_liveness` requirement.
A `proof_of_liveness` requirement might require collection of an electronic ID
credential such as [MyInfo](https://www.singpass.gov.sg/main/individuals/) in
Singapore, or by using Stripe Identity to collect a document or selfie. We
recommend using Stripe-hosted or embedded onboarding to satisfy all variations
of the `proof_of_liveness` requirement.

HostedEmbedded
[Stripe-hosted onboarding](https://docs.stripe.com/connect/hosted-onboarding)
can complete all variations of `proof_of_liveness` requirements.

[Create an Account
Link](https://docs.stripe.com/connect/hosted-onboarding#create-account-link)
using the connected account ID, and send the account to the `url` returned.

```
curl https://api.stripe.com/v1/account_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 --data-urlencode refresh_url="https://example.com/refresh" \
 --data-urlencode return_url="https://example.com/return" \
 -d type=account_onboarding \
 -d "collection_options[fields]"=currently_due
```

The account receives a prompt to complete the `proof_of_liveness` requirement,
along with any other currently due requirements. Listen to the `account.updated`
event sent to your webhook endpoint to be notified when the account completes
requirements and updates their information. After the account completes the
requirement, the account is redirected to the `return_url` specified.

[Update the connected
accountServer-side](https://docs.stripe.com/connect/api-onboarding#update-the-connected-account)
[Update](https://docs.stripe.com/api/accounts/update) the connected account
object with new information as your user progresses through each step of the
onboarding flow to allow Stripe to validate the information as soon as it’s
added. After Stripe confirms acceptance of our terms of service, any changes to
the connected account triggers reverification. For example, if you change the
connected account’s name and ID number, Stripe reruns verifications.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode "business_profile[url]"="https://furever.dev" \
 -d "tos_acceptance[date]"=1609798905 \
 -d "tos_acceptance[ip]"="8.8.8.8"
```

When updating a connected account, you must handle any [verification
errors](https://docs.stripe.com/connect/api-onboarding#handle-verification-errors)
or [HTTP error codes](https://docs.stripe.com/error-handling).

[Handle verification
errorsServer-side](https://docs.stripe.com/connect/api-onboarding#handle-verification-errors)
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

#### Note

You can’t use the API to respond to Stripe risk reviews. You can enable your
connected accounts to respond using embedded components, Stripe-hosted
onboarding, or remediation links. You can also use the Dashboard to respond to
risk reviews on behalf of your connected accounts.

Listen to the
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
event. If the account contains any `currently_due` fields when the
`current_deadline` arrives, the corresponding functionality is disabled and
those fields are added to `past_due`.

[Create a
form](https://docs.stripe.com/connect/api-onboarding#create-forms-to-collect-information)
with clear instructions that the account can use to correct the information.
Notify the account, then [submit the corrected
information](https://docs.stripe.com/connect/api-onboarding#update-the-connected-account)
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

## Links

- [Accounts API](https://docs.stripe.com/api/accounts)
- [embedded onboarding](https://docs.stripe.com/connect/embedded-onboarding)
- [Retrieve](https://docs.stripe.com/api/accounts/retrieve)
- [Create](https://docs.stripe.com/api/accounts/create)
- [onboarding
requirements](https://docs.stripe.com/connect/required-verification-information)
- [service agreement
type](https://docs.stripe.com/connect/service-agreement-types)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)
- [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
-
[company.structure](https://docs.stripe.com/api/accounts/object#account_object-company-structure)
- [Country](https://docs.stripe.com/api/accounts/object#account_object-country)
- [service agreement
type](https://docs.stripe.com/api/accounts/object#account_object-tos_acceptance-service_agreement)
-
[capabilities](https://docs.stripe.com/api/accounts/object#account_object-capabilities)
- [wrap Stripe terms of service in your own terms of
service](https://docs.stripe.com/connect/updating-service-agreements#adding-stripes-service-agreement-to-your-terms-of-service)
- [future
requirements](https://docs.stripe.com/connect/handle-verification-updates)
-
[collection_options.future_requirements](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options-future_requirements)
- [MyInfo](https://www.singpass.gov.sg/main/individuals/)
- [Stripe-hosted onboarding](https://docs.stripe.com/connect/hosted-onboarding)
- [Create an Account
Link](https://docs.stripe.com/connect/hosted-onboarding#create-account-link)
- [https://example.com/refresh](https://example.com/refresh)
- [https://example.com/return](https://example.com/return)
- [Update](https://docs.stripe.com/api/accounts/update)
- [https://furever.dev](https://furever.dev)
- [HTTP error codes](https://docs.stripe.com/error-handling)
- [Capabilities API](https://docs.stripe.com/api/capabilities/retrieve)
- [events](https://docs.stripe.com/api/events/types#event_types-account.updated)
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
- [dynamically generated
UI](https://docs.stripe.com/connect/custom/onboarding#create-forms-to-collect-information)
- [Update
account](https://docs.stripe.com/connect/custom/onboarding#update-the-connected-account)
- [verification errors and how to handle
them](https://docs.stripe.com/connect/handling-api-verification)
- [Test verification
states](https://docs.stripe.com/connect/testing-verification)