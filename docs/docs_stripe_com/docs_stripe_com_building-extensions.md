# Legacy extensionsDeprecated

## Learn how to build Stripe extensions, and see our Partner Directory for extensions created by our verified partners.

#### Stripe Apps replaces extensions

You can no longer build new Stripe extensions. Stripe Apps replaces extensions
for developing on Stripe. However, existing extensions will continue to work
until 2024. If you already have an extension, we recommend migrating it to
Stripe Apps.

[View the Stripe Apps migration
docs](https://docs.stripe.com/stripe-apps/migrate-extension)

#### Note

You can now automatically send your Stripe data and reports to Snowflake or
Amazon Redshift in a few clicks with Stripe Data Pipeline. [Learn
more](https://stripe.com/data-pipeline).

Stripe’s products and features allow companies to accept online payments, but
offer other reasons to integrate as well. Companies like
[Baremetrics](https://stripe.com/partners/baremetrics) and
[Segment](https://stripe.com/partners/segmentsources) build on top of Stripe to
provide their services to Stripe accounts with a Standard dashboard.

Building an extension on Stripe consists of four steps:

- [Configure OAuth and specify a redirect
URI](https://docs.stripe.com/building-extensions#configure-oauth-redirect).
- [Configure branding
settings](https://docs.stripe.com/building-extensions#configure-branding).
- [Create an OAuth link for your
users](https://docs.stripe.com/building-extensions#create-oauth-link).
- [Use the API on behalf of connected
accounts](https://docs.stripe.com/building-extensions#use-api).

You’re also required to add business details to activate your account, if you
haven’t already.

To get started, visit the [Extensions
page](https://dashboard.stripe.com/test/extensions) located in the Developers
tab of the Stripe dashboard.

[Configure OAuth and specify a redirect
URI](https://docs.stripe.com/building-extensions#configure-oauth-redirect)
You can configure this setting in the **Integration** section of the [Extensions
Settings](https://dashboard.stripe.com/test/settings/extensions) page.

Start your integration by toggling the button to enable onboarding Standard
accounts with OAuth. Extensions shouldn’t use OAuth with Express accounts.

Stripe provides a unique identifier for your extension called a `client_id`. You
set the `redirect_uri` and users are directed to that page after they connect
their accounts. You must specify all redirect URIs in your extension settings.
The development and production versions of these two values help with
[testing](https://docs.stripe.com/connect/testing#using-oauth). Take note of
these values so you can create an OAuth link in the third step.

[Configure branding
settings](https://docs.stripe.com/building-extensions#configure-branding)
You can customize how your business appears to your users in the **Branding**
section of the [Extensions
Settings](https://dashboard.stripe.com/test/settings/extensions) page.

Users see your logo when they link their Stripe accounts to your application.
After they link their accounts, your icon displays in their connected
applications list.

[Create an OAuth link for your
users](https://docs.stripe.com/building-extensions#create-oauth-link)
Stripe offers a standard OAuth 2.0 flow to connect to Stripe accounts. Using the
`client_id` and `redirect_uri` values from step one, you can create an OAuth
link for your users to onboard with. We recommend showing this link with a
**Connect with Stripe** button that sends users to the `authorize_url` endpoint:

```

https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_only
```

Here’s an example of how you can display the above link to your user, along with
the [Connect with Stripe
button](https://d37ugbyn3rpeym.cloudfront.net/docs/connect/Connect-with-Stripe-button.zip):

[Connect
with](https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_write)
After the user clicks the link on your site, we redirect them to a page to allow
or deny the connection to your extension. Stripe’s authorization flow prompts
them to either choose an existing account to connect with your extension, or
create a new one.

After the user connects their existing or newly created account to your
extension, we redirect them back to the URL you set as your extension’s
`redirect_uri` .

At the end of the OAuth workflow, you’re provided with authorization credentials
for the user’s account:

```
{
 ...
 "stripe_user_id": "acct_0123456789",
 ...
}
```

You need to store the `stripe_user_id` so you can identify user accounts.

[Use the API on behalf of connected
accounts](https://docs.stripe.com/building-extensions#use-api)
After users link their Stripe accounts to your application, you can make [API
requests](https://docs.stripe.com/api) on their behalf. To perform API requests,
you need your extension account’s secret key, and a `Stripe-Account` header that
identifies the account that you’re making the request for. All Stripe libraries
support this style of authentication on a per-request basis.

### Fetching stored data

Stored data includes information like charges and customer details. With
`read_only` access, you can make most `GET` requests in Stripe’s API. You can
retrieve a single object (for example, [retrieve a Payment
Intent](https://docs.stripe.com/api/payment_intents/retrieve)) or a list of
objects (for example, [list all Payment
Intents](https://docs.stripe.com/api/payment_intents/list)).

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "created[lte]"=1612048287 \
 -d "limit"=50 \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

While the API performs at a high level, repeatedly fetching large data sets
slows your application’s responsiveness. We recommended storing fetched data on
your side for analysis and reporting.

### Listening for real-time data

In addition to stored data, you can access real-time data via
[webhooks](https://docs.stripe.com/connect/webhooks). After you define an
[extension webhook endpoint in your
account](https://dashboard.stripe.com/account/webhooks), Stripe sends [event
notifications](https://docs.stripe.com/api#events) to your endpoint for every
connected account. The event object’s `account` property identifies the account
where the event occurred.

For example, the event below shows that a customer was created in the
`acct_0123456789` account. Again, we recommend storing this data on your side
for analysis and reporting. By watching events as they occur, your application
can respond faster, and you won’t need to make as many API calls.

```
{
 "id": "evt_",
 "livemode": true,
 "object": "event",
 "type": "customer.created",
 "account": "acct_0123456789",
 "pending_webhooks": 2,
 "created": 1349654313,
 "data": {...}
}
```

## Charging for your application

Your extension’s Stripe account can process its own charges, so you can still
charge for your application with `read_only` access. After customers connect
their Stripe accounts, ask for their payment details and then [create a
subscription](https://docs.stripe.com/api/subscriptions/create) for them in your
Stripe account. Make sure to store the created customer ID with the associated
Stripe account ID, so that you can track which users are paid and active, and
which ones are not.

If you create
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating), you can
also specify an `application_fee_percent` as a fee for your application. This is
charged on top of any Stripe fees. Read the
[Subscriptions](https://docs.stripe.com/connect/subscriptions) documentation to
learn more.

## Disconnected accounts

Users can disconnect their accounts from your integration at any time. When this
happens, Stripe sends an `account.application.deauthorized`
[webhook](https://docs.stripe.com/webhooks). You can use this notification to
trigger cleanup on your end, such as disabling the user’s account on your site
or removing their data.

You can also disconnect accounts from your integration, by making a request to
the [OAuth
deauthorization](https://docs.stripe.com/connect/oauth-reference#post-deauthorize)
endpoint.

## Links

- [View the Stripe Apps migration
docs](https://docs.stripe.com/stripe-apps/migrate-extension)
- [Learn more](https://stripe.com/data-pipeline)
- [Baremetrics](https://stripe.com/partners/baremetrics)
- [Segment](https://stripe.com/partners/segmentsources)
- [Extensions page](https://dashboard.stripe.com/test/extensions)
- [Extensions Settings](https://dashboard.stripe.com/test/settings/extensions)
- [testing](https://docs.stripe.com/connect/testing#using-oauth)
- [Connect OAuth Reference](https://docs.stripe.com/connect/oauth-reference)
- [OAuth 2.0 client](https://oauth.net/2/)
-
[https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_only](https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_only)
- [Connect with Stripe
button](https://d37ugbyn3rpeym.cloudfront.net/docs/connect/Connect-with-Stripe-button.zip)
- [Connect
with](https://connect.stripe.com/oauth/authorize?response_type=code&client_id=ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb&scope=read_write)
- [API requests](https://docs.stripe.com/api)
- [retrieve a Payment
Intent](https://docs.stripe.com/api/payment_intents/retrieve)
- [list all Payment Intents](https://docs.stripe.com/api/payment_intents/list)
- [webhooks](https://docs.stripe.com/connect/webhooks)
- [extension webhook endpoint in your
account](https://dashboard.stripe.com/account/webhooks)
- [event notifications](https://docs.stripe.com/api#events)
- [create a subscription](https://docs.stripe.com/api/subscriptions/create)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Subscriptions](https://docs.stripe.com/connect/subscriptions)
- [webhook](https://docs.stripe.com/webhooks)
- [OAuth
deauthorization](https://docs.stripe.com/connect/oauth-reference#post-deauthorize)