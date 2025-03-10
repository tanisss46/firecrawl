# Payout Trace IDs

## Track late or missing payouts with your bank.

The Trace ID is a unique identifier for a payout that our banking partners
create to help you track missing or delayed payouts. If an expected payout
hasn’t landed in your bank account after 10 business days, contact your bank for
an update and provide the Trace ID. The Trace ID is available on the [Stripe
Dashboard](https://dashboard.stripe.com/test/payouts),
[API](https://docs.stripe.com/api/payouts/retrieve),
[Sigma](https://docs.stripe.com/stripe-data) and [Payout Reconciliation
Report](https://docs.stripe.com/reports/payout-reconciliation).

For Connect users, you can provide your connected accounts their payout Trace
IDs by accessing them on the [Stripe
API](https://docs.stripe.com/api/payouts/retrieve). This enables your connected
accounts to self-serve their late or missing payouts without the need for manual
support intervention.

As a result, Connect users can:

- Minimize support requests from your connected accounts relating to late or
missing payouts.
- Improve user satisfaction by letting your connected accounts self-serve their
late or missing payout investigations with their bank.

#### Trace ID Format

The format of the Trace ID is dependent on Stripe’s banking partners and might
not be consistent across payouts.

## Availability

Trace IDs are retrieved from the partner bank up to 10 days after a payout has
been marked as paid. A Trace ID might not be available within this time-frame,
in which case the Trace ID status is marked as pending. If a trace ID can’t be
retrieved after 10 days, the Trace ID is marked as unsupported.

## Dashboard

To access the Trace ID on the Dashboard:

- Navigate to your [payouts](https://dashboard.stripe.com/test/payouts).
- Click the payout that you want to investigate.
- You can find the Trace ID under the *Details* section.

## API

You can find the API specifications on the Stripe API docs.

The `trace_id` contains two sub-fields: `value` and `status`:

- `value`: The Trace ID string that is retrieved from our banking partners when
a payout is paid.
- `status`: The current status of the Trace ID as it is being retrieved from our
banking partners.
StatusDescription`pending`When a payout is marked as paid, Stripe attempts to
retrieve the Trace ID from the banking partner for up to 10 days. During this
time the `status` becomes `pending`.`supported`When the Trace ID is successfully
retrieved from the banking partner, the `status` becomes `supported`. The
`value` is populated at this time.`unsupported`There are some scenarios where
the Trace ID can’t be provided, such as when the payout is failed or the Trace
ID isn’t supported for the country and currency combination. In these cases the
`status` is `unsupported`.
### Retrieving a Trace ID on the API

```
curl https://api.stripe.com/v1/payouts/po_xxx \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

```
{
 "object": "list",
 "data": [
 {
 "id": "po_xxx",
 "trace_id": {
 "status": "supported",
 "value": "7UF6L35ME6bh3bk3cj51L7o93ky79X5Pb58i5LO1e"
 }
 ...
 }
 ]
}
```

## Sigma

The Trace ID is also accessible using Sigma. The following example query uses
the transfers table to retrieve Trace ID information for the three most recent
payouts:

```
select
 date_format(created, '%m/%d/%Y') as day,
 id,
 trace_id_status,
 trace_id
from transfers
order by day desc
limit 3
```

`day``id``trace_id_status``trace_id`9/9/2024po_NKQiZu88eC4SGG6AoPctuUdypendingnull9/8/2024po_SAqvUY2iqhIpDAPzdidUv2JksupportedqfbjqDXXYy7dpiximwrYxL4T29/6/2024po_GgImpsIO3gDEVOszUVfmjBCHunsupportednull
## Support

Trace IDs are available in all Stripe supported countries except the following
payout destinations:

- Argentina
- Bolivia
- Chile
- Colombia
- Egypt
- Japan
- Philippines
- UK (Instant Payouts)

## Links

- [Stripe Dashboard](https://dashboard.stripe.com/test/payouts)
- [API](https://docs.stripe.com/api/payouts/retrieve)
- [Sigma](https://docs.stripe.com/stripe-data)
- [Payout Reconciliation
Report](https://docs.stripe.com/reports/payout-reconciliation)