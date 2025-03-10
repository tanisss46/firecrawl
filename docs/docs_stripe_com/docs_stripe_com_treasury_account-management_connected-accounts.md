# Working with connected accounts in Treasury

## Request the Treasury capability and collect onboarding requirements for your connected accounts.

To use Stripe Treasury, your platform must have a Stripe
[Connect](https://docs.stripe.com/connect) integration. Stripe Connect enables a
platform to provide connected accounts to sellers and service providers. For an
overview of how connected accounts fit into the Stripe Treasury account
structure, see the [Stripe Treasury accounts
structure](https://docs.stripe.com/treasury/account-management/treasury-accounts-structure)
guide.

Treasury only supports connected accounts that don’t use a Stripe-hosted
dashboard and where your platform is responsible for requirements collection and
loss liability, including Custom connected accounts. Learn how to [create
connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
that work with Treasury.

#### Private preview

Enabling Treasury on non-custom connected accounts is a new feature. Email
[treasury-support@stripe.com](mailto:treasury-support@stripe.com) to request
access.

As a platform with connected accounts, you’re responsible for maintaining a
minimum API version, communicating terms of service updates to your connected
accounts, handling information requests from them, and providing them with
support. Because your platform is ultimately responsible for the losses your
connected accounts incur, you’re also responsible for vetting them for fraud. To
learn more, read the [Treasury fraud
guide](https://docs.stripe.com/treasury/examples/fraud-guide).

Connected accounts require specific capabilities enabled on the account to use
features of Treasury. Different features require different capabilities, which
might require additional information about your connected account owners. The
`treasury` capability, for example, is a requirement on connected accounts for
Treasury access. When you request `treasury` for an account, additional fields
become required for that connected account before the account can use Treasury.

Before you create connected accounts in live mode for your Treasury integration,
we recommend you first create test connected accounts in [test
mode](https://docs.stripe.com/test-mode). Test mode connected accounts can’t
receive or send real money and can’t be used in live mode, but are otherwise
identical in configuration and functionality.

## Checking current connected account types

If your platform already has a Connect integration with connected accounts but
are unsure of their type, you can use the Dashboard or API to retrieve this
information.

DashboardAPI request
Navigate to the [Connected accounts
page](https://dashboard.stripe.com/test/connect/accounts/overview) in the
Dashboard. We list your connected accounts in a table format.

![Table of connected
accounts](https://b.stripecdn.com/docs-statics-srv/assets/account-dashboard.f7c91e5c9e06a1ca68102ed2cbaaa8ce.png)

Connected accounts

To find the account features, select an account in the table to open the
detailed view, then click **Profile** > **Account information**.

![Account details section of the dashboard displaying one account of type
Custom.](https://b.stripecdn.com/docs-statics-srv/assets/account-information.22a76ce6f2d50771ebd78a0f21020fb3.png)

Account information

## Create a new connected account with the treasury capability

#### Note

This guide demonstrates how to create a new connected account using the Stripe
API for Treasury and isn’t exhaustive. For complete documentation on creating a
connected account, including through hosted onboarding, see the [Connect
integration
guide](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct).

Use `POST /v1/accounts` to create a new connected account. Request the following
capabilities for the account, which are required to use Stripe Treasury:

- `transfers` (required for all connected accounts)
- `treasury`

#### Note

You can update the account later to request these capabilities if you don’t do
so when creating the account.

If you want to issue cards with Stripe Issuing to your connected account, you
must request the `card_issuing` capability, as well. See the [Working with
Stripe Issuing
cards](https://docs.stripe.com/treasury/account-management/issuing-cards) guide
for more information.

If you want to use ACH to transfer funds to or from an external account, you
must also request the `us_bank_account_ach_payments` capability.

With all the previous options included, the request resembles the following:

```
const account = await stripe.accounts.create({
 country: 'US',
 email: email,
 capabilities: {
 transfers: {requested: true},
 treasury: {requested: true},
 card_issuing: {requested: true},
 },
 controller: {
 dashboard: {type: "none"},
 losses: {payments: "application"},
 requirement_collection: "application",
 fees: {payer: "application"}
 },
});
```

If successful, the response you receive confirms the connected account and
requested `capabilities`.

```
{
 "id": "acct_1234",
 "object": "account",
 "capabilities": {
"card_issuing": "inactive", // Should be requested only for Stripe Issuing
users.
 "treasury": "inactive",
 "us_bank_account_ach_payments": "inactive"
 },
 ...
}
```

To learn more about connected account capabilities, see the [Account
capabilities](https://docs.stripe.com/connect/account-capabilities) guide for
Connect.

## Update a connected account to include the treasury capability

If you already have a connected account with `card_payments` enabled, use `POST
/v1/accounts/{{CONNECTED_ACCOUNT_ID}}` to update the account with the associated
ID with a request for the `treasury` capability. The following request updates a
connected account with a request for the `treasury` capability, and includes the
optional capabilities of `card_issuing` and `us_bank_account_ach_payments`:

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "capabilities[treasury][requested]"=true \
 -d "capabilities[card_issuing][requested]"=true \
 -d "capabilities[us_bank_account_ach_payments][requested]"=true
```

Use `POST /v1/accounts/{{CONNECTED_ACCOUNT_ID}}` to update connected account
capabilities for connected accounts that already have a `FinancialAccount`
assigned. See [Working with financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
or the [FinancialAccount
object](https://docs.stripe.com/api/treasury/financial_accounts/object) API
documentation for more information.

## Onboard the connected account

After you create an account, you must onboard the seller or service provider to
the account for ownership. The
[Account](https://docs.stripe.com/api/accounts/object#account_object-requirements-currently_due)
object that represents the connected account has a `requirements` hash that
contains `currently_due` [identity
verification](https://docs.stripe.com/connect/handling-api-verification)
requirements. The seller or service provider on your platform must provide the
details itemized in the `requirements` hash to enable charges and
[payouts](https://docs.stripe.com/payouts) on their connected account and enable
all requested features of their financial account.

You have two options for onboarding connected account owners to Treasury:
[hosted
onboarding](https://docs.stripe.com/treasury/account-management/connected-accounts#using-hosted-onboarding)
and [custom
onboarding](https://docs.stripe.com/treasury/account-management/connected-accounts#using-custom-onboarding).
We recommend hosted onboarding.

If you create an `Account` object in test mode and want to bypass onboarding
requirements to test functionality, use `POST
/v1/accounts/{{CONNECTED_ACCOUNT_ID}}` to [provide test
values](https://docs.stripe.com/connect/testing-verification) that fulfill all
the requirements. The following request uses a previously created connected
account to apply the required account details.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "tos_acceptance[date]"=1547923073 \
 -d "tos_acceptance[ip]"="172.18.80.19" \
 -d "settings[treasury][tos_acceptance][date]"=1547923073 \
 -d "settings[treasury][tos_acceptance][ip]"="172.18.80.19" \
 -d "business_profile[mcc]"=5045 \
 --data-urlencode "business_profile[url]"="https://bestcookieco.com" \
 -d "company[address][city]"=Schenectady \
 -d "company[address][line1]"="123 State St" \
 -d "company[address][postal_code]"=12345 \
 -d "company[address][state]"=NY \
 -d "company[tax_id]"=000000000 \
 -d "company[name]"="The Best Cookie Co" \
 -d "company[phone]"=8888675309 \
 -d "individual[first_name]"=Jenny \
 -d "individual[last_name]"=Rosen
```

### Using hosted onboarding

Use Connect Onboarding to efficiently collect required information. That
offloads the verification complexity from your platform to Stripe and collects
the terms of the service agreement. Alternatively, you can write your own API
requests for initial integration, but must monitor for changes to compliance
requirements to keep your onboarding workflow current. Learn how to [create
connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
that work with Treasury.

Before you can use Connect Onboarding, you must provide the name, color, and
icon of your brand in the **Branding** section of your [Connect settings
page](https://dashboard.stripe.com/test/settings/connect). Doing so customizes
the visual appearance of the form that sellers and service providers interact
with when onboarding to your platform.

To take advantage of Connect Onboarding, use `POST /v1/account_links` to create
an `AccountLink` to provide to the seller or service provider who’s going to
take ownership of the connected account:

#### Warning

For security, don’t email, text, or otherwise send account link URLs directly to
your user. Instead, redirect the authenticated user to the account link URL from
within your platform’s application.

```
curl https://api.stripe.com/v1/account_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 --data-urlencode refresh_url="https://example.com/reauth" \
 --data-urlencode return_url="https://example.com/return" \
 -d type=account_onboarding
```

The response you receive includes the URL to provide to your user.

```
{
 "object": "account_link",
 "created": 1612927106,
 "expires_at": 1612927406,
 "url": "https://connect.stripe.com/setup/s/iCtLfmYb2tEU"
}
```

### Using custom onboarding

If you prefer to build custom onboarding for your users, use `POST
/v1/accounts/{{CONNECTED_ACCOUNT_ID}}` and `POST
/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/persons/{{PERSON_ID}}` to update the
relevant `Account` and `Person` objects with the required information.

You must also confirm that the connected account owner has read and agreed to
the [Stripe Treasury
Agreement](https://stripe.com/treasury-connect-account/legal). See [Handling
verification with the
API](https://docs.stripe.com/connect/handling-api-verification) for additional
details on fulfilling onboarding requirements.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "company[name]"=Homebox \
 -d "company[address][line1]"="123 Market St." \
 -d "company[address][city]"="San Francisco" \
 -d "company[address][state]"=CA \
 -d "company[address][postal_code]"=94107 \
 -d "company[address][country]"=US
```

### Requirements

The fields in the following table are required for Treasury users.

Entity typeAt onboardingIndividual, Sole proprietorshipEntity details:- Business
names (customer facing and legal)
- Legal entity type
- Business address
- Business phone number
- Product or service description
- Industry or Merchant category code
- Tax ID Number (SSN, ITIN, or EIN)
- Treasury TOS acceptance
- Stripe TOS acceptance
Owner details:- Legal name
- Date of birth
- Email address
- Residential address
- Full SSN, or ID document scan for non-US persons or if SSN can’t be verified
- Title
- Phone number
Companies (LLCs, corporations, non-profits, partnerships, and so on)Entity
details:- Business names (customer facing and legal)
- Legal entity type
- Business address
- Business phone number
- Product or service description
- Industry or Merchant category code
- Tax ID Number (EIN)
- Treasury TOS acceptance
- Stripe TOS acceptance
Owner/representative details:- Legal name
- Date of birth
- Email address
- Residential address
- Phone number
- Title
- Percent ownership of company
- Full SSN, or ID document scan for non-US persons or if SSN can’t be verified

### Completion

The connected account onboarding process is complete when you receive an
`account.updated` [webhook](https://docs.stripe.com/webhooks) confirming the
following fields on your connected account:

```
{
 "object": {
 "object": "account",
 "id": "acct_1234",
 "capabilities": {
 "treasury": "active",
"card_issuing": "active", // Only appears if requesting the `card_issuing`
capability.
"us_bank_account_ach_payments": "active", // Only appears if requesting the
`us_bank_account_ach_payments` capability.
 },
 ...
 }
}

```

Account onboarding latency when your platform’s bank partner is Evolve Bank &
Trust is less than 5 minutes.

### Updates to requirements

To adapt to changes in financial regulations, Stripe must occasionally update
information collection requirements for Treasury. The
`requirements.eventually_due` array on the `Account` object captures the updated
information required by these regulation changes. Learn more about the
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
hash.

## Links

- [Connect](https://docs.stripe.com/connect)
- [Stripe Treasury accounts
structure](https://docs.stripe.com/treasury/account-management/treasury-accounts-structure)
- [create connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
- [Treasury fraud guide](https://docs.stripe.com/treasury/examples/fraud-guide)
- [test mode](https://docs.stripe.com/test-mode)
- [Connected accounts
page](https://dashboard.stripe.com/test/connect/accounts/overview)
- [Working with Stripe Issuing
cards](https://docs.stripe.com/treasury/account-management/issuing-cards)
- [Account capabilities](https://docs.stripe.com/connect/account-capabilities)
- [Working with financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
- [FinancialAccount
object](https://docs.stripe.com/api/treasury/financial_accounts/object)
-
[Account](https://docs.stripe.com/api/accounts/object#account_object-requirements-currently_due)
- [identity
verification](https://docs.stripe.com/connect/handling-api-verification)
- [payouts](https://docs.stripe.com/payouts)
- [hosted
onboarding](https://docs.stripe.com/treasury/account-management/connected-accounts#using-hosted-onboarding)
- [custom
onboarding](https://docs.stripe.com/treasury/account-management/connected-accounts#using-custom-onboarding)
- [provide test values](https://docs.stripe.com/connect/testing-verification)
- [https://bestcookieco.com](https://bestcookieco.com)
- [Connect settings page](https://dashboard.stripe.com/test/settings/connect)
- [https://example.com/reauth](https://example.com/reauth)
- [https://example.com/return](https://example.com/return)
-
[https://connect.stripe.com/setup/s/iCtLfmYb2tEU](https://connect.stripe.com/setup/s/iCtLfmYb2tEU)
- [Stripe Treasury Agreement](https://stripe.com/treasury-connect-account/legal)
- [webhook](https://docs.stripe.com/webhooks)
-
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)