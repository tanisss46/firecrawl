# Acceptance analyticsPublic preview

## Understand what influences card payment acceptance, reasons behind payment failures or declines, and ways to maximize your payment success rate.

On the [Payments analytics](https://dashboard.stripe.com/acceptance) page in the
Stripe Dashboard, you can analyze your payment success rate, authorization rate,
and payments to find out where exactly payments fail, why they fail, and how to
use this information to increase your revenue. To view your analytics, go to
**Payments** > **Analytics** >
[Acceptance](https://dashboard.stripe.com/acceptance).

#### Public preview

[Payments analytics](https://dashboard.stripe.com/acceptance) is in public
preview. If you want access to the public preview, we invite you to [join the
waitlist](https://docs.stripe.com/payments/analytics).

## Understand payment attempts

When your customers attempt to pay, Stripe sends the charge details through the
card networks, like Visa, Mastercard, or China UnionPay. The card networks then
send the requests to the relevant card issuing banks, who either [authorize or
decline](https://docs.stripe.com/declines) the payments.

A payment attempt can fail at multiple stages, even before a payment is sent to
the card network. For example, it might fail 3D Secure authentication (3DS) or
be blocked by [Stripe Radar](https://docs.stripe.com/radar). After the payment
is sent to the card network, issuers can decline it for several reasons, such as
a lack of sufficient funds on the card account or incorrect card information.
Occasionally, issuers incorrectly decline legitimate payments for suspected
fraud.

Payments analytics provides the following data for card payments:

- Payment success and network authorization rate, which you can view as either
raw or deduplicated
- Pivot charts for common dimensions (also available as filters)
- Reasons for failed payments (authentication issue, blocked, or card network
decline reasons)
- The uplift provided by Stripe’s payments optimizations features

## Available data

Data on this page includes attempted and authorized card payments. Authorized
volume figures don’t take into account whether the payments were ultimately
captured. Learn more about the distinction between [authorization and
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method).

## Configure your data set

The filters at the top of the Payments analytics page apply to all metrics,
charts, and tables on the page.

Stripe processes your data daily starting at 12:00 am UTC and ending at 11:59pm
UTC. All data shown is in the UTC time zone.

### Specify currency

The `Currency` filter is set to your settlement currency by default. To change
the currency, click **Currency** , and select the currency you want from the
list.

## Download acceptance data

You can download all of the data used to generate the report. To download these
analytics, click **Download** at the top of each chart.

Downloads provide payments that match the filters at the top of the report. The
download dialog is only set to one currency filter (by default, the currency of
the business).

If you’re a [Sigma
user](https://docs.stripe.com/stripe-data/access-data-in-dashboard), you can
view your data in Sigma, and have access to the specific queries used to
generate each chart.

### Specify Connect

Connect platforms see direct charge activity aggregated across all of their
connected accounts. Use the **Connected accounts** filter at the top of the
report to include connected account data or to exclude it and display only
platform data. Data from Standard accounts is only visible to platforms if
[Platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
are enabled.

## Metrics definitions

You can review your analytics with two metrics: payment success rate or
authorization rate.

### Payment success rate

Payment success rate measures the success of all payment attempts through all
stages of the payment process: 3D Secure authentication, Stripe or Radar blocks,
and card network authorization. It’s the number of charges authorized by the
card network divided by the number of unique payment attempts submitted through
Stripe. We include all payment attempts except [invalid API
calls](https://docs.stripe.com/declines#invalid-api-calls).

### Authorization rate

The network authorization rate measures the success of payment attempts that
reach the card networks. It is the number of payments authorized by the card
issuer divided by the number of unique payment attempts submitted to the card
network for authorization. We don’t include [invalid API
calls](https://docs.stripe.com/declines#invalid-api-calls), payments that fail
3D Secure authentication, and [blocked
payments](https://docs.stripe.com/declines#blocked-payments) in the denominator
because these failures occur before Stripe sends the authorization request to
the issuer.

## Comparison chart

The following table shows which types of payment attempts are included in the
two metrics.

Payment success rateAuthorization rateInvalid API requestsFailed 3D Secure
authentication paymentsBlocked paymentsIssuer declinesAuthorized payments
## Example calculations

The following is an example authorization rate calculation for authorization
rate and payment success rate.

Calculation componentComponent valueTOTAL PAYMENT REQUESTS TO
STRIPE103,000Invalid API requests(3,000)Valid API requests100,000Failed
authentication attempts(1,000)Blocked payment attempts(1,000)Total payment
attempts that reach card network98,000Authorized payments93,000Payment Success
Rate93% = (93,000 / 100,000)Network Authorization Rate94.9% = (93,000 / 98,000)
## Deduplicated versus raw rates

Some payment attempts are repeat attempts of the same unique purchase; for
example, a customer’s original payment attempt is declined because they entered
the wrong CVC and they later resubmit the payment after correcting their error.
We include all attempts except invalid API requests in the calculation. The raw
rate counts all of these attempts to make the same purchase, whereas the
deduplicated rate groups the retried attempts together and calculates the
acceptance rate based on the final outcome.

The following tables shows example calculations using deduplicated rate and raw
rate.

Raw rateDeduplicated rateCalculation stepResultPayment A, Attempt 1FailedPayment
A, Attempt 2FailedPayment A, Attempt 3AuthorizedRaw Rate (Counts all
attempts)33.3% = (1 / 3) (1 authorized attempt / 3 total attempts)
When looking at deduplicated rates, you might see a temporary drop in your
success or authorization rates for the past month if not all payment retries
have been attempted yet.

You can also schedule repeat attempts yourself, a practice known as “dunning,"
which is common for businesses with recurring revenue. If you perform dunning
through [Stripe Billing](https://docs.stripe.com/billing), Stripe highlights the
affected portion of the chart using your Billing settings.

### How Stripe identifies repeat attempts

For payments through [Stripe Invoices](https://docs.stripe.com/api/invoices), we
group attempts on the same Invoice together. For payments with
[Customers](https://docs.stripe.com/api/customers), we group attempts on the
same Customer if they’re attempted close to each other in time and for the same
amount. For all other payments, we group on the same card number for attempts
close to each other in time and for the same amount.

## Key metrics report

This report shows the key metrics for your chosen filters, including the rate,
number of authorized payments, and payment volume that was authorized. The time
series compares the rate to a `previous_period`, which you can customize. By
default, the comparison period starts right before your chosen timeframe and
represents the same length of time.

## Payments report

The Payments report allows you to view card acceptance metrics across several
common acceptance-driving dimensions. Each of the top-level filters has a
corresponding pivot chart. Pairing the filtering capabilities with the pivot
charts in the Payments chart provides a view that lets you monitor how different
groups of payments perform over time. You can switch through each tab to compare
rates, payment count breakdowns (in absolute numbers or as a share of payments),
and payment volumes.

Use all of these tabs to see how changes in the rate relate to changes in
payment counts or volume. You can dig deeper into any trends you want to explore
with Sigma or use the itemized download to filter across available charge
attributes. For example, [card
testing](https://docs.stripe.com/disputes/prevention/card-testing) can lead to a
reduction in the rate and a sudden spike in payment count.

Analyze payments across many options, such as which card brands, countries, or
input methods your customers use to pay.

### Card type

On average, credit success rates are higher than debit success rates, which in
turn are higher than prepaid success rates. This is usually because payments
made with debit and prepaid cards are more likely to be declined for having
insufficient funds to complete the purchases.

### Card country

Card country refers to the country of the card issuer, rather than the physical
location of your customer at the time of payment. On average, domestic success
rates are higher than those on cross-border payments (where the card country and
your business are located in different regions). This pivot may also help you
identify where your customers are based.

### Transaction type

The card networks divide card payments into two types, depending on whether the
customer is participating in the payment flow: [Customer-Initiated Transactions
(CITs) and Merchant-Initiated Transactions
(MITs)](https://docs.stripe.com/payments/cits-and-mits). Card issuers assign
different characteristics and risk profiles to these transaction types, so there
can be varying success rates between the two.

### Input method

Digital wallets such as Apple Pay and Android Pay typically have higher success
rates than normal online card charges because they’re tokenized and
device-authenticated, creating a higher level of trust for the card issuer.

If you use [Stripe Terminal](https://docs.stripe.com/terminal), you might also
see **Card present** as an input method option, which represents in-person
payments. Industry-wide, card present success rates are typically higher than
card not present ones. The physical card must be present at the time of purchase
for in-person payments, so these payments often have lower risk profiles for
card issuers than online payments do.

### Saved card status

You can use previously saved card details to charge customers later. This is
most often used for subscriptions. A saved card is also referred to as a
Credential-on-File (CoF). Success rates are typically higher for saved cards
than non-saved cards.

### Postal code response

Address Verification Service (AVS) is an identity verification tool that allows
businesses to detect and prevent potentially fraudulent credit or debit card
payments by comparing the billing address provided by a customer with the
billing address on-file with the customer’s card issuer, to confirm they match.
Address verification is primarily supported by card issuers in the United
States, Canada, and the United Kingdom.

The following table shows example values for the Postal code response metric.

ValueDefinitionNot sentPostal code was not sent to the card networksPassedPostal
code was sent to the card networks and passed validationFailedPostal code was
sent to the card networks and failed validationUncheckedPostal code was sent to
the card networks but no validation was performed
### CVC response

The [CVC](https://docs.stripe.com/disputes/prevention/verification#cvc-check)
(also referred to as CVV) is the three- or four-digit verification number
printed directly on a card, usually on the signature strip or the front of the
card. When a card payment is submitted to a card network for authorization,
Stripe sends the CVC if it is provided . Similar to AVS, the card issuer checks
the CVC against the information they have on-file for the customer as an
additional verification. If the provided information doesn’t match, the CVC
verification check fails, which may result in a declined payment. A failed CVC
check can indicate the payment is fraudulent, so review it carefully before
fulfilling the order.

The following table shows example values for the CVC response metric.

ValueDefinitionNot sentCVC was not sent to the card networksPassedCVC was sent
to the card networks and passed validationFailedCVC was sent to the card
networks and failed validationUncheckedCVC was sent to the card networks but no
validation was performed
### Network token usage

A [network
token](https://stripe.com/guides/understanding-benefits-of-network-tokens#what-are-network-tokens)
(NT) is a non-sensitive, 16-digit numeric substitute for a “front-of-card”
number also referred to as a primary account number (PAN). When paired with a
cryptogram, a network token can be sent to the card network in the authorization
message instead of a PAN.

Unlike PANs, network tokens are payment credentials that can be dynamically
restricted to specific businesses and channels, reducing the risk and impact of
potential security breaches and intrusions. Businesses also use NTs for
authorization rate uplift; networks contain the latest mapping between NTs and
PANs, so Stripe can continue to use the same NT even if the underlying PAN
changes, and avoid declines on legitimate payment attempts.

### Further analyze “other”

For dimensions with several options, the pivot chart will include an “other”
category to group the low volume data points that aren’t represented on the
chart. For example, you might want to see the full set of card issued countries
in your data. To do so, you can view the data in Sigma or download the data.

## Failed payments

Use this chart to find out why payments failed or declined.

### Before the payment is sent to the card network

The following sections describe failures that occur before the payment is sent
to the card network.

#### Authentication failed

You can request payments
[authentication](https://docs.stripe.com/payments/3d-secure/authentication-flow)
with 3D Secure (3DS) using the API or with a Radar rule. Stripe might also
trigger 3DS to comply with certain regulations, such as [Strong Customer
Authentication (SCA)](https://stripe.com/guides/strong-customer-authentication)
requirements in Europe. The failed authentication payment requests represent
situations where the customer didn’t finish the steps for authentication or
failed the authentication for other reasons. To learn more about authentication
failures, see [Payment analytics](https://docs.stripe.com/payments/analytics).

#### Block payments by reason

Stripe Radar blocks high-risk payments, such as those with mismatched CVC or
postal code values. This automated fraud prevention product evaluates each
payment, without requiring any action from you. The blocked payments represent
the ones blocked by Stripe, obtaining initial authorization from the card issuer
but refrains from charging the card. This precaution helps prevent potential
fraudulent payments that might lead to disputes. See Blocked payments by reason
below for more information about block reasons.

### After the payment is sent to the card network

The following sections describe failures that occur after the payment is sent to
the card network.

#### Issuer declines

When a payment request is submitted to the card issuer, they use automated
systems and models to determine whether to authorize it. If the issuer declines
a payment, Stripe shares the [reason](https://docs.stripe.com/declines/card) the
issuer gave for the decline. In some cases, the issuer provides specific reasons
for the decline with a [decline code](https://docs.stripe.com/declines/codes).
However, many payments are categorized into generic declines (the most common of
which is `do_not_honor`). Card issuers can only discuss the specifics with their
cardholders, not with you or Stripe, for privacy and security.

For most businesses, the most common decline reasons provided for issuer
declined payments fall into a few categories. Below are explanations and
recommended actions to take for some common network decline reasons. To learn
more about the full list of potential reasons why card issuers decline payments,
see [decline codes](https://docs.stripe.com/declines/codes).

- **Insufficient funds**: The account doesn’t have sufficient funds to cover the
payment amount at the time of authorization. Prompt the customer to try a
different payment method, or obtain approval from the customer to retry the
payment at a later date.
- **Do not honor and other generic responses (like Generic decline or Service
not allowed)**: The issuer has chosen not to provide the specific reason for
their decision. Prompt the customer to contact their card issuer for more
information, or to try a different payment method. Retrying the payment yourself
might also be successful.
- **Incorrect number, incorrect CVC, and other incorrect card information
responses**: The customer has entered incorrect card information or card
information that’s no longer valid. Make sure you have [automatic card
updates](https://docs.stripe.com/saving-cards#automatic-card-updates) enabled.
Contact the customer through multiple channels, such as email, text messages, or
in-app notifications to re-enter their payment details or contact their card
issuer if problems persist. Otherwise, try a different payment method.
- **Transaction not allowed**: The issuer has declined the payment for
unspecified reasons, which might be related to the card, or might be
payment-specific. In the latter case, the merchant spend category might not be
allowed on the card for example (such as FSA cards for ineligible items). The
customer should contact their card issuer for more information (retries are
unlikely to be successful until the issuer has been contacted) or try a
different payment method.
- **Lost card or Stolen card**: The customer has reported the card as either
lost or stolen. Retries won’t be successful, and the customer should contact
their card issuer for more information. Don’t report the specific reason to the
customer in case the legitimate cardholder isn’t the one attempting the
purchase.

## Blocked payments chart

Use this chart to learn why some payments were blocked.

### Rule match - Radar

Some payments are blocked because of a rule that you configured in Radar. This
doesn’t include payments that Radar blocked by default because of their risk
score.

### Post authorization rule match - Radar

Some payments are blocked after the card issuer has authorized the payment
because of a configured rule in Radar. Specifically, Radar rules that require a
response from the card issuer, such as ensuring postal code or CVC match what
the card issuer had on-file. This doesn’t include payments that Radar blocked by
default because of their risk score.

### High risk - Radar

Some payments are blocked by Radar by default because of their risk score. Radar
determines this score using machine learning, and you can adjust the minimum
score that it blocks by default. There are some Radar rules that block payments
after they have been authorized.

### Stripe

Some payments are blocked by Stripe for other reasons not included above. For
example, the payment was initiated by a card on deny-lists that are globally
known to be fraudulent, or a payment made from sanctioned countries.
Additionally, Stripe may block payments that are suspected to be connected to
[card testing](https://docs.stripe.com/disputes/prevention/card-testing).

## Payment optimizations chart

Stripe’s [solutions for maximizing authorization
rates](https://stripe.com/guides/optimizing-authorization-rates#how-stripe-can-help)
help prevent legitimate charges from being declined. These features include
Adaptive Acceptance, Card account updater, and Network tokens.

### Adaptive Acceptance

If Stripe receives a decline response from the issuer, machine learning models
immediately evaluate if Stripe should retry the request, and how to adjust the
authorization request to improve the likelihood of acceptance. This retry
request happens in real time before Stripe returns a charge response to you. The
uplift shown in this report is from payments that Adaptive Acceptance
successfully retried after an initial issuer decline.

### Card account updater

Card numbers and expiration dates regularly change, so outdated card information
is a common source of declines for online businesses. Stripe integrates with
major card networks to update saved card payment information automatically to
make sure you have the latest card details. The uplift shown in this report is
from successful payments on cards that were updated within 180 days of the
payment date.

### Network tokens

Network tokens are secure payment credentials that serve as substitutes for card
numbers. Network tokens ensure that you process payments with the most
up-to-date credentials, because they stay current even if the underlying card
data changes. Stripe has built integrations with major card networks to tokenize
your cards, and machine learning models to determine when to use a network token
to provide you the maximum success rate. The uplift shown in this report is from
successful payments run with network tokens that received updates to the
underlying credentials within 180 days of the payment date.

## See also

- [Glossary](https://docs.stripe.com/payments/analytics/glossary)
- [Authentication
analytics](https://docs.stripe.com/payments/analytics/authentication)
- [Payment methods
analytics](https://docs.stripe.com/payments/analytics/payment-methods)

## Links

- [Payments analytics](https://dashboard.stripe.com/acceptance)
- [join the waitlist](https://docs.stripe.com/payments/analytics)
- [authorize or decline](https://docs.stripe.com/declines)
- [Stripe Radar](https://docs.stripe.com/radar)
- [authorization and
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [Sigma user](https://docs.stripe.com/stripe-data/access-data-in-dashboard)
- [Platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [invalid API calls](https://docs.stripe.com/declines#invalid-api-calls)
- [blocked payments](https://docs.stripe.com/declines#blocked-payments)
- [Stripe Billing](https://docs.stripe.com/billing)
- [Stripe Invoices](https://docs.stripe.com/api/invoices)
- [Customers](https://docs.stripe.com/api/customers)
- [card testing](https://docs.stripe.com/disputes/prevention/card-testing)
- [Customer-Initiated Transactions (CITs) and Merchant-Initiated Transactions
(MITs)](https://docs.stripe.com/payments/cits-and-mits)
- [Stripe Terminal](https://docs.stripe.com/terminal)
- [CVC](https://docs.stripe.com/disputes/prevention/verification#cvc-check)
- [network
token](https://stripe.com/guides/understanding-benefits-of-network-tokens#what-are-network-tokens)
-
[authentication](https://docs.stripe.com/payments/3d-secure/authentication-flow)
- [Strong Customer Authentication
(SCA)](https://stripe.com/guides/strong-customer-authentication)
- [reason](https://docs.stripe.com/declines/card)
- [decline code](https://docs.stripe.com/declines/codes)
- [automatic card
updates](https://docs.stripe.com/saving-cards#automatic-card-updates)
- [solutions for maximizing authorization
rates](https://stripe.com/guides/optimizing-authorization-rates#how-stripe-can-help)
- [Glossary](https://docs.stripe.com/payments/analytics/glossary)
- [Authentication
analytics](https://docs.stripe.com/payments/analytics/authentication)
- [Payment methods
analytics](https://docs.stripe.com/payments/analytics/payment-methods)