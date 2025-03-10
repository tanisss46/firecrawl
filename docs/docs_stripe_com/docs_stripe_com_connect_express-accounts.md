# Using Connect with Express connected accounts

## Express connected accounts enable your platform to manage payout schedules, customize the flow of funds, and control branding. Stripe handles onboarding, account management, and identity verification.

## Express demo

To see the complete Express onboarding flow in action, try the [sample
end-to-end Express integration](https://rocketrides.io/) before you start
building your own. This demo includes an example of a connected account
onboarding experience and account management for Rocket Rides, an on-demand
marketplace.

You can find the demo’s [complete source
code](https://github.com/stripe/stripe-connect-rocketrides) on GitHub.

![Rocket Rides, a demo of Stripe Connect with Express connected
accounts](https://b.stripecdn.com/docs-statics-srv/assets/rocket-rides-new.e01ced22698d7f5d3d1c915f26175dcd.png)

## Before you begin

To create Express connected accounts, you must meet all of these requirements:

- **Minimum API version**: Express connected accounts require API version
2017-05-25 or later.
[Capabilities](https://docs.stripe.com/connect/account-capabilities) require API
version 2019-02-19 or later.
- **Platform in a supported country**: Platforms in Australia, Austria, Belgium,
Brazil, Bulgaria, Canada, Croatia, Cyprus, the Czech Republic, Denmark, Estonia,
Finland, France, Germany, Greece, Hong Kong, Hungary, Ireland, Italy, Japan,
Latvia, Lithuania, Luxembourg, Malta, Mexico, the Netherlands, New Zealand,
Norway, Poland, Portugal, Romania, Singapore, Slovakia, Slovenia, Spain, Sweden,
Switzerland, Thailand, the United Kingdom, and the United States can create
Express accounts for most countries [Stripe
supports](https://stripe.com/global). For information about country-specific
restrictions, or to request notification when Express accounts become available
in your country, [contact us](mailto:connect@stripe.com).
- **Countries that don’t support self-serve**: Due to restrictions that apply
when using Connect in the [United Arab
Emirates](https://support.stripe.com/questions/connect-availability-in-the-uae)
and
[Thailand](https://support.stripe.com/questions/stripe-thailand-support-for-marketplace),
platform users in these countries can’t self-serve Express connected accounts.
To begin onboarding for Express connected accounts in these countries, [contact
us](https://stripe.com/contact/sales).
- **Platforms in the UAE**: Platforms in the UAE can only use Express connected
accounts based in the UAE with the following charge types:
[destination_charges](https://docs.stripe.com/connect/destination-charges) and
[separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers).
Destination charges using the
[on_behalf_of](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-on_behalf_of)
attribute are not yet supported for UAE platforms.
- **Vetting for fraud**: Because your platform is responsible for losses
incurred by Express connected accounts, you must closely examine all accounts
that sign up through your platform for potential fraud. Refer to our [risk
management best practices
guide](https://docs.stripe.com/connect/risk-management/best-practices#fraud) for
more information.
- **Platform profile**: You need to complete your [platform’s
profile](https://dashboard.stripe.com/connect/registration).

## Onboarding Express connected accounts outside of your platform’s country

You can enable onboarding on a per-country basis in the [Connect
Settings](https://dashboard.stripe.com/account/applications/settings) section of
your Dashboard.

The Express account onboarding flow is currently localized in , French,
Spanish, Bulgarian, Simplified Chinese, Traditional Chinese, Czech, Danish,
Dutch, Estonian, Finnish, German, Greek, Hungarian, Indonesian, Italian,
Japanese, Latvian, Lithuanian, Norwegian, Polish, Portuguese, Romanian, Slovak,
Slovenian, Swedish, and Thai.

Keep the following in mind when onboarding accounts globally:

- **International business:** Your platform is responsible for understanding the
implications of doing business internationally, such as tax and financial
reporting.
- **Charge flows:** Be sure to review your options for [creating
charges](https://docs.stripe.com/connect/charges) based on the countries you
intend to operate in.
- **Service agreement type:** Your platform can create connected accounts under
the [recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#recipient) to
enable [cross-border
transfers](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border).
Such accounts have restricted access to capabilities.
[Configure the onboarding
experience](https://docs.stripe.com/connect/express-accounts#configure-onboarding)
Before onboarding your first account, go to the [Connect settings
page](https://dashboard.stripe.com/account/applications/settings) to customize
the visual appearance of the form with your brand’s name, color, and icon.
Connect Onboarding requires this information.

[Create an Express connected account and prefill
information](https://docs.stripe.com/connect/express-accounts#create-account)
Use the [Create Account](https://docs.stripe.com/api/accounts/create) API to
create a connected account with `type` set to `express`. You can prefill any
information, but at a minimum, you must specify the `type`. The country of the
account defaults to the same country as your platform, and the account confirms
the selection during onboarding.

#### Note

This example includes only some of the fields you can set when creating an
account. For a full list of the fields you can set, such as `address` and
`website_url`, see the [Create Account API
reference](https://docs.stripe.com/api/accounts/create).

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d type=express
```

If you know the country and
[capabilities](https://docs.stripe.com/connect/account-capabilities) for your
connected account, you can provide that information when you create the account.
Connect Onboarding then collects the requirements for those capabilities. To
reduce onboarding effort, request only the capabilities you need.

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d country=US \
 -d type=express \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true \
 -d business_type=individual \
 --data-urlencode "business_profile[url]"="https://example.com"
```

If you’ve already collected information for your connected accounts, you can
prefill that information on the `Account` object. You can prefill any account
information, including personal and business information, external account
information, and so on.

Connect Onboarding doesn’t ask for the prefilled information. However, it does
ask the account holder to confirm the prefilled information before accepting the
[Connect service
agreement](https://docs.stripe.com/connect/service-agreement-types).

When you onboard an account without its own website and your platform provides
it with a personal URL, prefill its `business_profile.url`. If the account
doesn’t have a URL, you can prefill its `business_profile.product_description`
instead.

When testing your integration, prefill account information using [test
data](https://docs.stripe.com/connect/testing).

If you omit `capabilities`, Connect Onboarding uses the settings in the
[Configuration
settings](https://dashboard.stripe.com/account/applications/settings/express)
section of the Stripe Dashboard to automatically request capabilities based on
the account’s country.

[Create an account
link](https://docs.stripe.com/connect/express-accounts#create-link)
[Create an Account Link](https://docs.stripe.com/api/account_links/create) with
the following parameters:

- `account` - use the account ID returned by the API from the previous step
- `refresh_url`
- `return_url`
- `type` = `account_onboarding`

```
curl https://api.stripe.com/v1/account_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 --data-urlencode refresh_url="https://example.com/reauth" \
 --data-urlencode return_url="https://example.com/return" \
 -d type=account_onboarding
```

[Redirect your account to the account link
URL](https://docs.stripe.com/connect/express-accounts#redirect-link)
An [Account Link](https://docs.stripe.com/api/account_links/object) contains a
`url`. Redirect the account to this link to send your account into the
onboarding flow. Each [Account Link](https://docs.stripe.com/api/account_links)
URL can only be used once because it grants access to the account holder’s
personal information. Authenticate the account in your application before
redirecting them to this URL.

Before creating the first account link for an Express connected account, prefill
any [Know Your
Customer](https://support.stripe.com/questions/know-your-customer) (KYC)
information. After you create an account link for an Express connected account,
you can’t read or update its KYC information.

#### Security tip

Don’t email, text, or otherwise send account link URLs outside of your platform
application. Instead, provide them to the authenticated account holder within
your application.

[Handle the connected account returning to your
platform](https://docs.stripe.com/connect/express-accounts#return-user)
Connect Onboarding requires you to pass both a `return_url` and `refresh_url` to
handle all cases where the connected account is redirected to your platform.
It’s important that you implement these correctly to provide the best experience
for your connected account.

#### Note

You can use HTTP for your `return_url` and `refresh_url` while in test mode (for
example, to test with localhost), but live mode only accepts HTTPS. Be sure to
swap testing URLs for HTTPS URLs before going live.

#### return_url

Stripe issues a redirect to this URL when the connected account completes the
Connect Onboarding flow. This doesn’t mean that all information has been
collected or that there are no outstanding requirements on the account. This
only means the flow was entered and exited properly.

No state is passed through this URL. After a connected account is redirected to
your `return_url`, check the state of the `details_submitted` parameter on their
account by doing either of the following:

- Listen to `account.updated` events with a [Connect
webhook](https://docs.stripe.com/connect/webhooks).
- [Retrieve](https://docs.stripe.com/api/accounts/retrieve) the account with the
API.

#### refresh_url

Your connected account is redirected to the `refresh_url` in these cases:

- The link is expired (a few minutes passed after the link was created).
- They already visited the URL (they refreshed the page or clicked back or
forward in the browser).
- Your platform can no longer access the account.
- The account has been rejected.

Set up your `refresh_url` to trigger a method on your server to call [Account
Links](https://docs.stripe.com/api/account_links) again with the same
parameters, and redirect the connected account to the Connect Onboarding flow to
create a seamless experience.

[Handle connected accounts that have not completed
onboarding](https://docs.stripe.com/connect/express-accounts#handle-users-not-completed-onboarding)
A connected account that’s redirected to your `return_url` might not have
completed the onboarding process.
[Retrieve](https://docs.stripe.com/api/accounts/retrieve) their account and
check for `charges_enabled`. If the account isn’t fully onboarded, provide UI
prompts to allow them to continue onboarding later. They can complete their
account activation through a new account link (generated by your integration).
You can check the state of the `details_submitted` parameter on their account to
see if they’ve completed the onboarding process.

## See also

- [Express Dashboard](https://docs.stripe.com/connect/express-dashboard)
- [Integrate the Express
Dashboard](https://docs.stripe.com/connect/integrate-express-dashboard)
- [Customize the Express
Dashboard](https://docs.stripe.com/connect/customize-express-dashboard)

## Links

- [sample end-to-end Express integration](https://rocketrides.io/)
- [complete source code](https://github.com/stripe/stripe-connect-rocketrides)
- [Capabilities](https://docs.stripe.com/connect/account-capabilities)
- [Stripe supports](https://stripe.com/global)
- [United Arab
Emirates](https://support.stripe.com/questions/connect-availability-in-the-uae)
-
[Thailand](https://support.stripe.com/questions/stripe-thailand-support-for-marketplace)
- [contact us](https://stripe.com/contact/sales)
- [destination_charges](https://docs.stripe.com/connect/destination-charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
-
[on_behalf_of](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-on_behalf_of)
- [risk management best practices
guide](https://docs.stripe.com/connect/risk-management/best-practices#fraud)
- [platform’s profile](https://dashboard.stripe.com/connect/registration)
- [Connect Settings](https://dashboard.stripe.com/account/applications/settings)
- [creating charges](https://docs.stripe.com/connect/charges)
- [recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#recipient)
- [cross-border
transfers](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border)
- [Create Account](https://docs.stripe.com/api/accounts/create)
- [https://example.com](https://example.com)
- [Connect service
agreement](https://docs.stripe.com/connect/service-agreement-types)
- [test data](https://docs.stripe.com/connect/testing)
- [Configuration
settings](https://dashboard.stripe.com/account/applications/settings/express)
- [Create an Account Link](https://docs.stripe.com/api/account_links/create)
- [https://example.com/reauth](https://example.com/reauth)
- [https://example.com/return](https://example.com/return)
- [Account Link](https://docs.stripe.com/api/account_links/object)
- [Account Link](https://docs.stripe.com/api/account_links)
- [Know Your Customer](https://support.stripe.com/questions/know-your-customer)
- [Connect webhook](https://docs.stripe.com/connect/webhooks)
- [Retrieve](https://docs.stripe.com/api/accounts/retrieve)
- [Express Dashboard](https://docs.stripe.com/connect/express-dashboard)
- [Integrate the Express
Dashboard](https://docs.stripe.com/connect/integrate-express-dashboard)
- [Customize the Express
Dashboard](https://docs.stripe.com/connect/customize-express-dashboard)