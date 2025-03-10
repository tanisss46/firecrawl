# Stripe-hosted onboarding

## Onboard connected accounts by redirecting them to a Stripe-hosted onboarding flow.

Stripe-hosted onboarding handles the collection of business and identity
verification information from connected accounts, requiring minimal effort by
the platform. It’s a web form hosted by Stripe that renders dynamically based on
the capabilities, country, and business type of each connected account.

Stripe-hosted onboarding supports [Legal Entity
Sharing](https://docs.stripe.com/connect/legal-entity-sharing), which allows
owners of multiple Stripe accounts to share business information between them.
When they onboard an account, they can reuse that information from an existing
account instead of resubmitting it.

!

The hosted onboarding form in Stripe’s sample integration, [Rocket
Deliveries](https://rocketdeliveries.io/).

[Customize the onboarding
formDashboard](https://docs.stripe.com/connect/hosted-onboarding#customize-onboarding-form)
Go to the [Connect settings
page](https://dashboard.stripe.com/account/applications/settings) in the
Dashboard to customize the visual appearance of the form with your brand’s name,
color, and icon. Stripe-hosted onboarding requires this information. Stripe also
recommends [collecting bank account
information](https://dashboard.stripe.com/settings/connect/payouts/onboarding)
from your connected accounts as they’re onboarding.

[Create an account and prefill
informationServer-side](https://docs.stripe.com/connect/hosted-onboarding#create-account)
Create a [connected account](https://docs.stripe.com/api/accounts) with the
default
[controller](https://docs.stripe.com/api/accounts/create#create_account-controller)
properties. See [design an
integration](https://docs.stripe.com/connect/design-an-integration) to learn
more about controller properties. Alternatively, you can create a connected
account by specifying an account
[type](https://docs.stripe.com/api/accounts/create#create_account-type).

With controller propertiesWith account type
```
curl -X POST https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

If you know the country for your connected account, you can provide that
information when you create the account. The country defaults to the same
country as your platform if not provided.

To request [capabilities](https://docs.stripe.com/connect/account-capabilities)
for your connected account, you can provide that information when you create the
account. Stripe’s onboarding UIs automatically collect the requirements for
those capabilities. To reduce onboarding effort, request only the capabilities
you need. If you omit capabilities, and your connected account has access to the
full Stripe Dashboard or the Express Dashboard, capabilities are automatically
requested. For accounts with access to the Express dashboard, Stripe-hosted
onboarding uses the [Configuration
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/countries)
to request capabilities based on the account’s country.

If you have information about the account holder (like their name, address, or
other details), you can proactively provide this when you
[create](https://docs.stripe.com/api/accounts/create) or
[update](https://docs.stripe.com/api/accounts/update) the account. Stripe-hosted
onboarding asks the account holder to confirm the pre-filled information before
accepting the [Connect service
agreement](https://docs.stripe.com/connect/service-agreement-types). Providing
more information through the API reduces the number of prompts and enhances the
onboarding flow for your connected account.

Additionally, if you onboard an account without its own website and your
platform provides the account with a URL, prefill the account’s
[business_profile.url](https://docs.stripe.com/api/accounts/create#create_account-business_profile-url).
If the account doesn’t have a URL, you can prefill its
[business_profile.product_description](https://docs.stripe.com/api/accounts/create#create_account-business_profile-product_description)
instead.

When testing your integration, use [test
data](https://docs.stripe.com/connect/testing) to simulate different outcomes
including identity verification, business information verification, payout
failures, and more.

[Determine the information to
collect](https://docs.stripe.com/connect/hosted-onboarding#info-to-collect)
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

[Create an Account
LinkServer-side](https://docs.stripe.com/connect/hosted-onboarding#create-account-link)
Create an [Account Link](https://docs.stripe.com/api/account_links) using the
connected account ID and include a [refresh
URL](https://docs.stripe.com/connect/hosted-onboarding#refresh-url) and a
[return URL](https://docs.stripe.com/connect/hosted-onboarding#return-url).
Stripe redirects the connected account to the refresh URL if the Account Link
URL has already been visited, has expired, or is otherwise invalid. Stripe
redirects connected accounts to the return URL when they have completed or left
the onboarding flow. Additionally, based on the information you need to collect,
pass either `currently_due` or `eventually_due` for `collection_options.fields`.
This example passes `eventually_due` to use upfront onboarding. Set to
`currently_due` for incremental onboarding.

```
curl https://api.stripe.com/v1/account_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 --data-urlencode refresh_url="https://example.com/refresh" \
 --data-urlencode return_url="https://example.com/return" \
 -d type=account_onboarding \
 -d "collection_options[fields]"=eventually_due
```

### Redirect your connected account to the Account Link URL

Redirect the connected account to the Account Link URL to send them to the
onboarding flow. Each Account Link URL can only be used once because it grants
access to the account holder’s personal information. Authenticate the account in
your application before redirecting them to this URL.

[Handle new requirements becoming
dueServer-side](https://docs.stripe.com/connect/hosted-onboarding#handle-new-requirements-becoming-due)
Set up your integration to [listen for
changes](https://docs.stripe.com/connect/handling-api-verification#verification-process)
to account requirements. You can test handling new requirements (and how they
might disable charges and payouts) with the [test mode trigger
cards](https://docs.stripe.com/connect/testing#trigger-cards).

Based on your application’s verification requirements, send the connected
account back through onboarding when it has `currently_due` or `eventually_due`
requirements. Use these signals to determine when it’s necessary to re-initiate
onboarding for a connected account.

You don’t need to worry about determining which requirements are missing.
Onboarding collects the necessary information. For example, if there’s a typo
preventing verification, onboarding prompts the connected account to upload an
identity document (such as a Driver’s License in the United States). If any
information is missing, onboarding requests it.

Stripe notifies you about any [upcoming requirements
updates](https://support.stripe.com/user/questions/onboarding-requirements-updates)
that affect your connected accounts. You can proactively collect this
information by reviewing the [future
requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements)
for your accounts.

### Handle verification errors

Listen to the
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
event. If the account contains any `currently_due` fields when the
`current_deadline` arrives, the corresponding functionality is disabled and
those fields are added to `past_due`.

Let your accounts remediate their verification requirements by directing them to
the Stripe-hosted onboarding form.

[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
event

If `requirements.currently_due` contains fields

Direct account to onboarding in time to finish before
[current_deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline)

No action required

If `requirements.past_due` contains fields

Account possibly disabled; direct it to onboarding

Redirect to the Stripe-hosted onboarding form

YesNo[Handle the connected account returning to your
platformServer-side](https://docs.stripe.com/connect/hosted-onboarding#handle-returning-accounts)
The Account Link requires a `refresh_url` and `return_url` to handle all cases
in which the connected account is redirected back to your platform. It’s
important to implement these correctly to provide the best onboarding flow for
your connected accounts.

#### Note

You can use HTTP for your `refresh_url` and `return_url` while you’re in test
mode (for example, to test locally), but for live mode only HTTPS is accepted.
Be sure you’ve swapped any testing URLs for HTTPS URLs before going live.

### Refresh URL

Your connected account is redirected to the `refresh_url` when:

- The link is expired (a few minutes went by since the link was created).
- The link was already visited (the connected account refreshed the page or
clicked the **back** or **forward** button).
- The link was shared in a third-party application such as a messaging client
that attempts to access the URL to preview it. Many clients automatically visit
links which causes them to become expired.

The `refresh_url` should call a method on your server to create a new [Account
Link](https://docs.stripe.com/api/account_links) with the same parameters and
redirect the connected account to the new Account Link URL.

### Return URL

Stripe redirects the connected account back to this URL when they complete the
onboarding flow or click **Save for later** at any point in the flow. It **does
not** mean that all information has been collected, or that there are no
outstanding requirements on the account. It only means the flow was entered and
exited properly.

No state is passed with this URL. After a connected account is redirected to the
`return_url`, determine if the account has completed onboarding.
[Retrieve](https://docs.stripe.com/api/accounts/retrieve) the account and check
the
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
attribute for outstanding requirements. Or, listen to the `account.updated`
event sent to your webhook endpoint and cache the state of the account in your
application. If the account hasn’t completed onboarding, provide prompts in your
application to allow them to continue onboarding later.

[Handle connected account-initiated
updatesServer-side](https://docs.stripe.com/connect/hosted-onboarding#handle-account-initiated-updates)
Stripe-hosted onboarding also supports connected account-initiated updates to
the information they’ve already provided. Listen to the `account.updated` event
sent to your webhook endpoint to be notified when the account completes
requirements and updates their information.

When you create an Account Link, you can set the `type` to either
`account_onboarding` or `account_update`.

### Account onboarding

Account Links of this type provide a form for inputting outstanding
requirements. Use it when you’re onboarding a new connected account, or when an
existing user has new requirements (such as when a connected account had already
provided enough information, but you requested a new capability that needs
additional info). Send them to this type of Account Link to just collect the new
information you need.

### Account update

Account Links of this type are enabled for accounts where your platform is
responsible for requirement collection. `account_update` links display the
attributes that are already populated on the account object and allows your
connected account to edit previously provided information (for example, they
need to update their address). Provide an option in your application (for
example, “edit my profile” or “update my verification information”) for
connected accounts to make updates themselves.

## Supported browsers

Stripe-hosted onboarding supports:

- The last 20 major versions of Chrome and Firefox
- The last two major versions of Safari and Edge
- The last two major versions of mobile Safari on iOS

Stripe-hosted onboarding is only supported in web browsers and cannot be used in
embedded web views inside mobile or desktop applications.

## Links

- [Legal Entity Sharing](https://docs.stripe.com/connect/legal-entity-sharing)
- [Rocket Deliveries](https://rocketdeliveries.io/)
- [Connect settings
page](https://dashboard.stripe.com/account/applications/settings)
- [collecting bank account
information](https://dashboard.stripe.com/settings/connect/payouts/onboarding)
- [connected account](https://docs.stripe.com/api/accounts)
-
[controller](https://docs.stripe.com/api/accounts/create#create_account-controller)
- [design an integration](https://docs.stripe.com/connect/design-an-integration)
- [type](https://docs.stripe.com/api/accounts/create#create_account-type)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)
- [Configuration
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/countries)
- [create](https://docs.stripe.com/api/accounts/create)
- [update](https://docs.stripe.com/api/accounts/update)
- [Connect service
agreement](https://docs.stripe.com/connect/service-agreement-types)
-
[business_profile.url](https://docs.stripe.com/api/accounts/create#create_account-business_profile-url)
-
[business_profile.product_description](https://docs.stripe.com/api/accounts/create#create_account-business_profile-product_description)
- [test data](https://docs.stripe.com/connect/testing)
- [required
information](https://docs.stripe.com/connect/required-verification-information)
- [future
requirements](https://docs.stripe.com/connect/handle-verification-updates)
-
[collection_options.future_requirements](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options-future_requirements)
- [Account Link](https://docs.stripe.com/api/account_links)
- [https://example.com/refresh](https://example.com/refresh)
- [https://example.com/return](https://example.com/return)
- [listen for
changes](https://docs.stripe.com/connect/handling-api-verification#verification-process)
- [test mode trigger
cards](https://docs.stripe.com/connect/testing#trigger-cards)
- [upcoming requirements
updates](https://support.stripe.com/user/questions/onboarding-requirements-updates)
- [future
requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements)
-
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
-
[current_deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline)
- [Retrieve](https://docs.stripe.com/api/accounts/retrieve)
-
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)