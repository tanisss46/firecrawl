# Monthly summary

## Learn about the monthly summary report.

The [monthly summary](https://dashboard.stripe.com/revenue-recognition/)
provides a detailed breakdown of activity for the previous month. You can use
this information to understand how your billing activity affected your revenue
and to book journal entries.

![Monthly summary for July
2020](https://b.stripecdn.com/docs-statics-srv/assets/monthly-summary-v2.ba474e8e2a801fedb0674c40bae653ad.png)

You can see that the net recognized revenue is 171,601 USD and the ending
balance of deferred revenue at the end of July is 310,000 USD.

## Recognized revenue

Items can be broken down into two categories: revenue and contra revenue. The
following table explains each item under recognized revenue:

Item Category Description Revenue from billings this monthRevenueThe recognized
revenue portion from finalized invoice line items and standalone payments
occurring this month. The revenue of a standalone payment is recognized when the
payment occurs.Recognized revenue previously deferredRevenueThe recognized
revenue portion from invoice line items finalized in previous months.Revenue
from metered subscriptions this monthRevenueThe revenue from metered
subscriptions.Revenue from unbilled servicesRevenueThe revenue from unbilled
invoice items.Revenue from platform feesRevenueThe revenue from platform fees.
[Learn how a platform fee impacts
revenue](https://docs.stripe.com/revenue-recognition/connect/destination-charges#revenue-collected-with-application_fee_amount).Less
canceled unbilled invoice itemsContra revenueThe contra revenue originated from
the deleted unbilled invoice items.Less refundsContra revenueThe contra revenue
originated from refunds. This contra revenue offsets previously recognized
revenue. [Learn how a refund impacts
revenue.](https://docs.stripe.com/revenue-recognition/examples/contra#refund)Less
disputesContra revenueThe contra revenue originated from disputes. This contra
revenue offsets previously recognized revenue. [Learn how a dispute impacts
revenue.](https://docs.stripe.com/revenue-recognition/examples/contra#dispute)Less
voided billingsContra revenueThe contra revenue originated from voids. This
contra revenue offsets previously recognized revenue. [Learn how voiding impacts
revenue.](https://docs.stripe.com/revenue-recognition/examples/contra#void)Less
bad debtContra revenueThe contra revenue originated from marking invoices as
uncollectible. This contra revenue offsets previously recognized revenue. [Learn
how marking an invoice as uncollectible impacts
revenue.](https://docs.stripe.com/revenue-recognition/examples/contra#uncollectible)Less
credit notesContra revenueThe contra revenue originated from credit notes. This
contra revenue offsets previously recognized revenue.Less refunds from platform
feesContra revenueThe contra revenue originated from refunding platform fees.
[Learn how a platform fee refund impacts
revenue](https://docs.stripe.com/revenue-recognition/connect/destination-charges#loss-and-contra-revenue-with-issuing-refunds).Less
transferContra revenueThe contra revenue originated from separate transfers.
[Learn how a separate transfer impacts
revenue](https://docs.stripe.com/revenue-recognition/connect/charges-transfers).Net
revenue-
The recognized revenue less the contra revenue.
## Deferred revenue

The deferred revenue section gives the breakdown of what changed in the deferred
revenue balance. The following table lists the items under this section:

Item Description Starting balanceThe ending balance of the deferred revenue from
the previous month.Deferred change from new billings this monthThe deferred
revenue from finalized invoice line items and standalone payments occurring this
month. With the exception of unbilled revenue that was recognized in previous
months (that is, included in “Revenue from unbilled services” in previous
months), every invoice line item and standalone payment books its deferred
revenue regardless of their revenue recognition schedule.Less recognized
revenueThe portion of deferred revenue that was recognized this month.Less
credits issuedThe remaining deferred revenue erased due to refunds, disputes,
voids, uncollectible invoices, and credit notes. [Learn how a refund impacts the
remaining deferred
revenue.](https://docs.stripe.com/revenue-recognition/examples/contra#refund)Ending
balanceThe ending balance of the deferred revenue from this month.
## Finalized invoice example

This example includes only one [invoice](https://docs.stripe.com/api/invoices)
with the following assumptions:

- The invoice finalizes on July 10, 2020.
- The invoice has only one line item whose service period is from July 20, 2020
to September 17, 2020.
- The amount for the invoice line item is 60 USD, out of which 12 USD is
recognized in July and 48 USD is deferred.

The monthly summary for July 2020 would look like this:

Recognized revenueRevenue from billings this month12 USDNet revenue12
USDDeferred revenueStarting balance Jul 1 UTC0 USDDeferred change from new
billings this month60 USDLess recognized revenue-12 USDEnding balance Jul 31
UTC48 USDFuture scheduled billingsStarting balance Jul 1 UTC0 USDEnding balance
Jul 31 UTC0 USD
Continuing on this example, if the invoice is refunded on August 15, 2020, the
monthly summary for August 2020 would look like this:

Recognized revenueLess refunds-12 USDNet revenue-12 USDDeferred revenueStarting
balance Aug 1 UTC48 USDLess credits issued-48 USDEnding balance Aug 31 UTC0
USDFuture scheduled billingsStarting balance Aug 1 UTC0 USDEnding balance Aug 31
UTC0 USD
## Standalone payment example

The revenue of a standalone payment is recognized when the payment occurs. This
example has only one charge with the following assumptions:

- The charge occurs on July 15, 2020.
- The charge’s amount is 17 USD.

The monthly summary for July 2020 would look like this:

Recognized revenueRevenue from billings this month17 USDNet revenue17
USDDeferred revenueStarting balance Jul 1 UTC0 USDDeferred change from new
billings this month17 USDLess recognized revenue17 USDEnding balance Jul 31 UTC0
USDFuture scheduled billingsStarting balance Jul 1 UTC0 USDEnding balance Jul 31
UTC0 USD

## Links

- [monthly summary](https://dashboard.stripe.com/revenue-recognition/)
- [Learn how a platform fee impacts
revenue](https://docs.stripe.com/revenue-recognition/connect/destination-charges#revenue-collected-with-application_fee_amount)
- [Learn how a refund impacts
revenue.](https://docs.stripe.com/revenue-recognition/examples/contra#refund)
- [Learn how a dispute impacts
revenue.](https://docs.stripe.com/revenue-recognition/examples/contra#dispute)
- [Learn how voiding impacts
revenue.](https://docs.stripe.com/revenue-recognition/examples/contra#void)
- [Learn how marking an invoice as uncollectible impacts
revenue.](https://docs.stripe.com/revenue-recognition/examples/contra#uncollectible)
- [Learn how a platform fee refund impacts
revenue](https://docs.stripe.com/revenue-recognition/connect/destination-charges#loss-and-contra-revenue-with-issuing-refunds)
- [Learn how a separate transfer impacts
revenue](https://docs.stripe.com/revenue-recognition/connect/charges-transfers)
- [invoice](https://docs.stripe.com/api/invoices)