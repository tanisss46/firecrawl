# Authentication analyticsPublic preview

## Learn how 3D Secure affects your payments success rate for card payments.

Navigate to **Payments** > **Analytics** > **Authentication** in the Dashboard
to see how [3D Secure (3DS)](https://docs.stripe.com/payments/3d-secure) affects
your payments success rate. 3DS is an authentication method for card payments
and aims to help protect businesses from
[liability](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
for fraud. You must set up 3DS to see your authentication analytics. To set up
3DS, see [Authenticate with 3D
Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow).

#### Public preview

[Payments analytics](https://dashboard.stripe.com/acceptance) is in public
preview. If you’re not part of the public preview, you can still access these
analytics by navigating to **Reporting** > **Reports** > **Authentication
analytics** in the Dashboard. If you want access to the public preview, you can
[join the waitlist](https://docs.stripe.com/payments/analytics).

## Configure your data set

Use filters to control all the metrics, charts, and tables on this page.

These metrics and charts exclude:

- 3DS requests that occur during [card
validations](https://docs.stripe.com/disputes/prevention/card-testing)
- Payments made with digital wallets such as Apple Pay and Google pay. These
digital wallets use device-based authentication methods (such as biometrics)
instead of 3DS
- 3DS requests for [Data
Only](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions#data-only)
authentication. Data Only doesn’t lead to 3DS challenges or [liability
shift](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
for your customers.

### Specify currency

The `Currency` filter is set to your settlement currency by default. To change
the currency, click **Currency** , and select the currency you want from the
list.

### Specify data as Raw or Deduplicated

You can also view your data as `Raw` or `Deduplicated`:

- **Raw** (default): Raw data includes all payment attempts, including repeat
attempts to complete a payment. When Stripe calculates the raw rate, we include
all attempts except invalid API requests.
- **Deduplicated**: Deduplicated data only includes the final outcome of payment
attempts that belong to the same payment. For example, Stripe considers a single
customer repeatedly trying and failing a payment as a single attempt.

### Specify Connect

You can view the direct charge activity for all of your connected accounts by
default. Use the **Connected accounts** filter if you want to exclude data from
your connected accounts. Data from [Standard connected
accounts](https://docs.stripe.com/connect/accounts#standard-accounts) is only
visible if you enable [Platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts).

## Download authentication data

To download these analytics, click **Download** at the top of each chart. The
CSV file you download matches any filters you selected and by default displays
your analytics in your settlement currency. To change the currency, click
**Currency** (), and select the currency you want from the list.

## Key metrics

These metrics include all payments where 3D Secure was requested, covering both
successful and unsuccessful authentication attempts.

MetricDefinitionAuthentication ratePercentage of payments where 3DS was
attempted, out of all payments.Authentication success ratePercentage of payments
where 3DS was successfully completed out of all 3DS attempts.Challenge
ratePercentage of payments where the customer receives a challenge out of all
3DS attempts.Challenge success ratePercentage of payments where a 3DS challenge
was successfully completed out of all the payments that require and receive a
challenge from 3DS.
### Calculate authentication rates

The following example explains how Stripe calculates authentication success
rates:

MetricValueTotal payments requests to Stripe100,000Total payments without
3DS60,000Total payments with 3DS requests40,000Total 3Ds requests with challenge
flow20,000Total 3DS requests successful with challenge flow16,000Authentication
rate40% = (40,000 / 100,000)Authentication success rate87.5% = (35,000 /
40,000)Challenge rate50% = (20,000 / 40,000)Challenge success rate80% = (16,000
/ 20,000)
## 3D Secure authentication outcomes

Use this chart to see all the outcomes for payments authentication through 3D
Secure. You can toggle this chart by 3DS requests, share of 3DS requests, and
3DS request volume.

Successful 3DS frictionless flowThis outcome represents payments that
successfully completed 3DS without any additional cardholder input needed,
including payments that were successfully exempted through 3DS.Successful 3DS
challenge flowThis outcome includes payments that successfully authenticated
using 3DS where the customer provided additional input to verify their identity
to the card issuer.Failed 3DS challengeThis outcome represents payments where
the customer abandoned the authentication flow or the payment was rejected by
the customer’s bank.3DS unavailableThis outcome represents situations where the
bank doesn’t support 3DS or the issuing bank returns an error.3DS not
actionedThis outcome refers to instances where the customer didn’t enter the 3DS
flow, or there was an issue with your integration and it didn’t action the
attempt. To troubleshoot, review your [3DS
integration](https://docs.stripe.com/payments/3d-secure/authentication-flow)
## 3D Secure authentication request reasons

Use this chart to see what initiated 3D Secure for your payments to evaluate if
you want to make adjustments to the frequency of when 3DS is requested.

API requestPayments where you requested 3DS through your Stripe integration. 3DS
can be triggered manually using the API. Stripe’s SCA rules run automatically,
regardless of whether or not you manually request 3DS. You can include
additional 3DS prompts but they aren’t required for SCA.Radar requestPayments
that match a Radar rule to request 3DS. The default method to trigger 3DS is
using Radar to dynamically request 3DS based on risk level and other
requirements.Stripe requestStripe requests 3DS because of regulations or
optimizations using our [Authentication
engine](https://stripe.com/payments/authentication). Stripe automatically
attempts to maximize payments success while minimizing fraud.Bank
requestPayments where the customer’s bank requests 3DS with the [soft decline
code](https://docs.stripe.com/declines/codes) `authentication_required`.
## Strong Customer Authentication

Use this chart to see which of your payments were considered in scope of [Strong
Customer Authentication
(SCA)](https://docs.stripe.com/strong-customer-authentication) rules. SCA
requires businesses in Europe and the UK to use 3DS to help prevent fraud for
[customer-initiated](https://docs.stripe.com/payments/cits-and-mits#customer-initiated-transactions-(cit))
online payments.

Stripe might request exemptions on your behalf for qualifying in scope payments
to minimize friction for your users and to increase your payments success rate.
Stripe won’t attempt to request exemptions in cases where you explicitly request
3DS using the API. Exempted payments don’t benefit from [liability
shift](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments).

- This chart is only visible if your business is based in Europe.
- This chart includes payments [within SCA
scope](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions).
- This chart includes payments considered as [SCA
exemptions](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions).
SCA exemptions are considered in scope of SCA rules.
- This chart excludes payments outside of SCA scope, such
[merchant-initiated](https://docs.stripe.com/payments/cits-and-mits#merchant-initiated-transactions-(mit))
payments.
- This chart excludes payments from digital wallets like Apple Pay and Google
Pay because they don’t use 3DS.

## See also

- [Glossary](https://docs.stripe.com/payments/analytics/glossary)
- [Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance)
- [Payment methods
analytics](https://docs.stripe.com/payments/analytics/payment-methods)

## Links

- [Authentication](https://dashboard.stripe.com/authentication)
- [3D Secure (3DS)](https://docs.stripe.com/payments/3d-secure)
-
[liability](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
- [Authenticate with 3D
Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow)
- [Payments analytics](https://dashboard.stripe.com/acceptance)
- [join the waitlist](https://docs.stripe.com/payments/analytics)
- [card validations](https://docs.stripe.com/disputes/prevention/card-testing)
- [Data
Only](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions#data-only)
- [Standard connected
accounts](https://docs.stripe.com/connect/accounts#standard-accounts)
- [Platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [Authentication engine](https://stripe.com/payments/authentication)
- [soft decline code](https://docs.stripe.com/declines/codes)
- [Strong Customer Authentication
(SCA)](https://docs.stripe.com/strong-customer-authentication)
-
[customer-initiated](https://docs.stripe.com/payments/cits-and-mits#customer-initiated-transactions-(cit))
- [within SCA
scope](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions)
-
[merchant-initiated](https://docs.stripe.com/payments/cits-and-mits#merchant-initiated-transactions-(mit))
- [Glossary](https://docs.stripe.com/payments/analytics/glossary)
- [Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance)
- [Payment methods
analytics](https://docs.stripe.com/payments/analytics/payment-methods)