# Onboarding solutions for Custom accounts

## Choose the onboarding method for Custom accounts that suits your business.

Stripe offers several ways to onboard Custom connected accounts. You can choose
the best onboarding method for your business.

#### Note

We recommend using Stripe-hosted onboarding or embedded onboarding components.
Both automatically update to handle changing requirements when they apply to a
connected account. With embedded components, you can [match them to your
branding](https://docs.stripe.com/connect/customize-connect-embedded-components)
and [control which policies and terms are
shown](https://docs.stripe.com/connect/embedded-onboarding#customize-policies-shown-to-your-users).

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

## Stripe hosted onboarding

Stripe hosted onboarding allows you to redirect your user to Stripe to complete
the onboarding process in a co-branded interface. Create an [Account
Link](https://docs.stripe.com/api/account_links) and direct your user to the
hosted onboarding flow. The
[return_url](https://docs.stripe.com/api/account_links/create#create_account_link-return_url)
allows Stripe to return the user to your application and allow you to progress
the connected account accordingly.

To integrate Stripe hosted onboarding, follow our [Stripe hosted onboarding
guide](https://docs.stripe.com/connect/custom/hosted-onboarding).

Onboard new user

[Create Account](https://docs.stripe.com/api/accounts/create)

Re-onboard existing user

Call [Account Retrieve](https://docs.stripe.com/api/accounts/retrieve)

If `requirements.currently_due` is not empty

Redirect to [hosted
onboarding](https://docs.stripe.com/connect/custom/hosted-onboarding)

## Embedded onboarding

Embedded onboarding is a highly themeable onboarding UI with limited Stripe
branding. Connected account users interact with the embedded component without
ever leaving your application. Embedded onboarding uses the [Accounts
API](https://docs.stripe.com/api/accounts) to read the requirements and generate
an onboarding form that is localized for all Stripe-supported countries and has
robust data validation. In addition, embedded onboarding handles all:

- Business types
- Configurations of company representatives
- Verification document uploading
- Identify verification and statuses
- International bank accounts
- Error states

You can integrate embedded onboarding with a few lines of code, whereas
API-based onboarding requires you to construct custom logic. To integrate
embedded onboarding, follow our [embedded components
guide](https://docs.stripe.com/connect/get-started-connect-embedded-components)
and integrate the [Account
onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
embedded component.

Onboard new user

[Create Account](https://docs.stripe.com/api/accounts/create)

Re-onboard existing user

Call [Account Retrieve](https://docs.stripe.com/api/accounts/retrieve)

If `requirements.currently_due` is not empty

Render the [onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)

## API-based onboarding

API-based onboarding involves building out each aspect of your site’s onboarding
user interface to call the corresponding Stripe APIs. Your integration must
satisfy all of Stripe’s onboarding requirements.

Onboard new user

Re-onboard existing user

[Retrieve](https://docs.stripe.com/api/accounts/retrieve) the connected account

Show UI to collect `requirements` from your user

[Create](https://docs.stripe.com/api/accounts/create) a connected account

If `requirements.currently_due` is not empty

Present forms to collect information and validate fields

Update the connected account with the collected information

### Establish Requirements

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

### Create forms to collect information

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

### Create the Connected Account

Use the [Create Account](https://docs.stripe.com/api/accounts/create) API to
create a connected account with country, service type agreement, desired
capabilities, business type, and any other information matching your
[requirements](https://docs.stripe.com/connect/custom/onboarding#establish-requirements).
At a minimum, you must specify `capabilities` and `type`. If you don’t specify
other parameters, they’re assigned the following default values:

- The service type agreement (`tos_acceptance.service_agreement`) defaults to
`full`.
- The `country` defaults to the same country as your platform.

The following code sample creates a Custom connected account with
`card_payments` and `transfers` capabilities under a full service agreement for
an individual.

#### Note

This example includes only some of the fields you can set when creating an
account. For a full list of the fields you can set, such as `address` and
`website_url`, see the [Create Account API
reference](https://docs.stripe.com/api/accounts/create).

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d country=US \
 -d type=custom \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true
```

### Take your account through the onboarding flow

You can enable connected accounts in either of two ways:

- Incremental onboarding strategy: Collect the minimum [required
information](https://docs.stripe.com/connect/custom/onboarding#establish-requirements)
up front and the rest later
- Upfront onboarding strategy: Collect all information up front

The incremental onboarding strategy speeds up initial onboarding but requires
additional information collection later on. The upfront onboarding strategy
minimizes enablement disruption throughout the connected account’s lifecycle at
the expense of a lengthier application process. You can decide which strategy
better suits your use case.

To implement your onboarding strategy, inspect the requirements hash of the
connected account you created. The requirements hash provides a complete list of
parameters you must collect to activate the connected account.

- If you choose the incremental onboarding strategy, inspect the `currently_due`
field in the requirements hash and build an onboarding flow that only collects
for the listed parameters.
- If you choose the upfront onboarding strategy, inspect the `eventually_due`
field in the requirements hash and build an onboarding flow that collects for
all the listed parameters.

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

### Update the connected account

Update the connected account object with new information as it progresses
through your onboarding flow. Perform an [Update
Account](https://docs.stripe.com/api/accounts/update) call, identifying the
connected account by the `id` value you stored earlier.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode "business_profile[url]"="https://furever.dev" \
 -d "tos_acceptance[date]"=1609798905 \
 -d "tos_acceptance[ip]"="8.8.8.8"
```

Stripe validates every update to a connected account. Update the account at each
step in onboarding to allow Stripe to validate information as soon as it’s
added, while your users continue through the onboarding flow. After Stripe
confirms acceptance of our terms of service, any changes to the connected
account trigger reverification. For example, if you change the connected
account’s name and ID number, Stripe reruns verifications.

When updating a connected account, you must handle any [verification
errors](https://docs.stripe.com/connect/custom/onboarding#verification-handling)
or [HTTP error codes](https://docs.stripe.com/error-handling) returned by the
Accounts API.

## Verification handling

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
form](https://docs.stripe.com/connect/custom/onboarding#create-forms-to-collect-information)
with clear instructions that the account can use to correct the information.
Notify the account, then [submit the corrected
information](https://docs.stripe.com/connect/custom/onboarding#update-the-connected-account)
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

## See also

Learn more about working with Custom accounts.

- [Handle verification
updates](https://docs.stripe.com/connect/handle-verification-updates)
- [Updating
Accounts](https://docs.stripe.com/connect/updating-service-agreements)
- [Identity Verification](https://docs.stripe.com/connect/identity-verification)

## Links

- [match them to your
branding](https://docs.stripe.com/connect/customize-connect-embedded-components)
- [control which policies and terms are
shown](https://docs.stripe.com/connect/embedded-onboarding#customize-policies-shown-to-your-users)
- [Stripe-hosted
onboarding](https://docs.stripe.com/connect/custom/onboarding#stripe-hosted-onboarding)
- [Embedded
onboarding](https://docs.stripe.com/connect/custom/onboarding#embedded-onboarding)
- [API-based
onboarding](https://docs.stripe.com/connect/custom/onboarding#api-based-onboarding)
- [Account Link](https://docs.stripe.com/api/account_links)
-
[return_url](https://docs.stripe.com/api/account_links/create#create_account_link-return_url)
- [Stripe hosted onboarding
guide](https://docs.stripe.com/connect/custom/hosted-onboarding)
- [Create Account](https://docs.stripe.com/api/accounts/create)
- [Account Retrieve](https://docs.stripe.com/api/accounts/retrieve)
- [Accounts API](https://docs.stripe.com/api/accounts)
- [embedded components
guide](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Account
onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
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
- [Update Account](https://docs.stripe.com/api/accounts/update)
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
- [Handle verification
updates](https://docs.stripe.com/connect/handle-verification-updates)
- [Updating
Accounts](https://docs.stripe.com/connect/updating-service-agreements)
- [Identity Verification](https://docs.stripe.com/connect/identity-verification)