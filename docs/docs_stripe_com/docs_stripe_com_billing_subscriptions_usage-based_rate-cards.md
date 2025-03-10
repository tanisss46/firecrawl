# Launch usage-based pricing models with rate cardsPrivate preview

## Charge customers complex pricing models with rate cards and subscriptions.

You can use rate cards to offer complex pay-as-you-go pricing models, like:

- **Large number of usage-based prices**: Model hundreds of pay-as-you-go
usage-based prices and group them into a single rate card. Each price references
a dedicated meter to track customer usage.
- **Subscribe customers to the rate card**: Subscribe customers to a rate card
with many prices in it using a single API call that references the rate card ID.
- **Launch new rates instantly**: Add new prices for new features to existing
rate cards and start reporting usage
[events](https://docs.stripe.com/api/v2/billing-meter). This lets existing
customers use the new feature immediately.

## Before you begin

Rate cards are currently in [private
preview](https://docs.stripe.com/release-phases) and could change in shape and
integration path before they’re generally available to all Stripe users.

## Join our private preview for rate cards

If you're interested in early access to the rate cards private preview, please
register your interest below.

Collect EmailSubmitRead our [privacy policy](https://stripe.com/privacy).
### Limitations

- Rate cards only support usage-based pricing. Additional support for licensed
pricing models is planned.
- You can only create rate cards for v2 subscriptions.
- Invoices are limited to 250 line items. Subscriptions with more than 250 line
items generate multiple invoices.

## Get started

To get started with rate cards:

- [Create a rate
card](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#create-card),
which represents a grouping for all of your usage-based prices.
- [Add prices to the rate
card](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#add-prices).
- [Set up billing cadence for the
customer](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#set-up-cadence)
to define how to invoice your customers on a recurring basis.
- [Subscribe the customer to the rate
card](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#subscribe-customer)
by passing in the rate card and the billing cadence.
- [Start recording customer
usage](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#record-usage)
of your product, then send usage events to Stripe. The customer gets invoiced on
each cadence.
- [Launch new
rates](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#launch-rates)
for new products to existing customers by adding the new price to the rate card.

## How rate cards work

The following diagram shows core concepts of charging a customer based on usage
consumption with rate cards:

Customer

Meter event

Rate Card subscription

Invoice

Rate Card

Price (multiple)

Customer action generatesSubscribeGeneratesRate usage (price x quantity)Rate
with priceHas oneHas many[Create a rate
card](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#create-card)
Provide an internal name, currency, pricing service interval, and tax behavior
to create a rate card. The service interval specifies the rate at which a
customer accumulates fees. The billing interval, defined by the [billing
cadence](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#set-up-cadence),
determines when the customer is invoiced.

```
curl -X POST https://api.stripe.com/v2/billing/rate_cards \
 -H "Authorization: Bearer {{YOUR_API_KEY}}" \
 -H "Stripe-Version: 2025-02-24.acacia" \
 --json '{
 "internal_name": "PAYGO rate card",
 "currency": "usd",
 "tax_behavior": "exclusive",
 "service_interval": "month",
 "service_interval_count": 1
 }'
```

After you submit the rate card request, Stripe returns the active rate card
object. You can’t subscribe new customers to an inactive rate card.

```
{
 "id": "rcd_test_61RVeJCo447E9aFii16RMt7iESSQdRfzhYKc3x1HkXDM",
 "object": "billing.rate_card",
 "active": true,
 "created": "2024-11-17T21:49:50.000Z",
 "currency": "usd",
 "internal_name": "PAYGO rate card",
 "metadata": {},
 "service_interval": "month",
 "service_interval_count": 1,
 "latest_version": "rcdv_123",
 "live_version": "rcdv_123", // defaults to first version created
 "tax_behavior": "exclusive"
}
```

[Add prices to the rate
card](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#add-prices)
After you create a rate card, create your usage-based
[Price](https://docs.stripe.com/api/prices/create), and add each price to the
rate card.

- `recurring.usage_type` must be `metered`.
- `recurring.meter` must reference a [Meter
object](https://docs.stripe.com/api/billing/meter/create) to record usage
events.
- `tax_behavior` must match your rate card’s `tax_behavior`.
- `recurring.interval` must match the `service_interval` of the rate card.

Add each of your [Prices](https://docs.stripe.com/api/prices) to the rate card
by using the following API request:

```
curl -X POST
https://api.stripe.com/v2/billing/rate_cards/rcd_test_61RVeJCo447E9aFii16RMt7iESSQdRfzhYKc3x1HkXDM/rates
\
 -H "Authorization: Bearer {{YOUR_API_KEY}}" \
 -H "Stripe-Version: 2025-02-24.acacia" \
 --json {"price":"{{PRICE_ID}}"}
```

#### Price IDs v1

The Rate Cards API won’t accept [Price IDs
v1](https://docs.stripe.com/api/prices/create) after this private preview
becomes [generally available](https://docs.stripe.com/release-phases). At that
time, this request will require passing the price data directly. Rate card
behavior will not change.

[Set up billing cadence for the
customer](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#set-up-cadence)
Before subscribing your customer to the rate card, define when and how often to
create invoices for the customer by creating a billing cadence. When an invoice
is created, the customer’s default payment method is automatically charged.

To create a billing cadence, [create a Customer
object](https://docs.stripe.com/api/customers/create). To test your integration
and advance time, you can [create a test
clock](https://docs.stripe.com/api/test_clocks/create) and attach it to the
customer.

The Payer resource represents the entity who pays for each invoice (not
necessarily the customer who uses the usage-based rates). To create a payer for
the customer, make the following request:

```
curl -X POST https://api.stripe.com/v2/billing/payers \
 -H "Authorization: Bearer {{YOUR_API_KEY}}" \
 -H "Stripe-Version: 2025-02-24.acacia" \
 --json {"customer":"{{CUSTOMER_ID}}"}
```

After you create a payer, create a billing cadence for them. The `billing_cycle`
defines when and how often you automatically bill the payer. When creating a
billing cadence, set the exact day and time for invoicing using the following
API request:

```
curl -X POST https://api.stripe.com/v2/billing/cadences \
 -H "Authorization: Bearer {{YOUR_API_KEY}}" \
 -H "Stripe-Version: 2025-02-24.acacia" \
 --json '{
 "payer": "{{PAYER_ID}}",
 "billing_cycle": {
 "type": "month",
 "interval_count": 1,
 "month": {
 "day_of_month": 20
 }
 }
 }'
```

[Subscribe the customer to the rate
card](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#subscribe-customer)
Subscribe your customer to the rate card by passing the rate card and billing
cadence in the following request. You can optionally pass a specific version of
a rate card when subscribing a customer. If you don’t specify a version, the
subscription applies the rate card’s live version.

```
curl -X POST https://api.stripe.com/v2/billing/rate_card_subscriptions \
 -H "Authorization: Bearer {{YOUR_API_KEY}}" \
 -H "Stripe-Version: 2025-02-24.acacia" \
 --json '{
 "rate_card": "rcd_A",
 "billing_cadence": "bc_1"
 }'
```

[Record customer
usage](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#record-usage)
Use [meter events](https://docs.stripe.com/api/billing/meter-event) to [record
customer
usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage)
for your meter. At the end of the billing period, Stripe bills the reported
usage to the customer.

To test usage-based billing, send meter events through the Stripe Dashboard or
API. When using the API, specify the customer ID and usage value in the
`payload`.

#### Poll meter events before advancing test clocks

After sending meter events, wait for [meter event
aggregation](https://docs.stripe.com/api/billing/meter-event-summary) to
complete before advancing your test clock. Poll the meter event summary endpoint
to confirm your usage has been processed, then advance the test clock to
generate invoices based on the billing cadence.

```
curl https://api.stripe.com/v1/billing/meter_events \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d event_name=alpaca_ai_tokens \
 -d "payload[stripe_customer_id]"={{CUSTOMER_ID}} \
 -d "payload[value]"=25
```

[Launch new
rates](https://docs.stripe.com/billing/subscriptions/usage-based/rate-cards#launch-rates)
If you launch a new feature that charges a new fee based on usage, you can
[create a new Price](https://docs.stripe.com/api/prices/create) and add that
price to your rate card. After adding a new price to the rate card, all existing
customers subscribed to that rate card can start using the feature. To send
meter events without updating their rate card subscription, add your new
[Price](https://docs.stripe.com/api/prices) to the rate card:

```
curl -X POST https://api.stripe.com/v2/billing/rate_cards/rc_1234/rates \
 -H "Authorization: Bearer {{YOUR_API_KEY}}" \
 -H "Stripe-Version: 2025-02-24.acacia" \
 --json {"price":"PRICE_ID"}
```

## Links

- [events](https://docs.stripe.com/api/v2/billing-meter)
- [private preview](https://docs.stripe.com/release-phases)
- [privacy policy](https://stripe.com/privacy)
- [Price](https://docs.stripe.com/api/prices/create)
- [Meter object](https://docs.stripe.com/api/billing/meter/create)
- [Prices](https://docs.stripe.com/api/prices)
- [create a Customer object](https://docs.stripe.com/api/customers/create)
- [create a test clock](https://docs.stripe.com/api/test_clocks/create)
- [meter events](https://docs.stripe.com/api/billing/meter-event)
- [record customer
usage](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage)
- [meter event
aggregation](https://docs.stripe.com/api/billing/meter-event-summary)