# Revenue Recognition Data Freshness

## Understand when data becomes available to Revenue Recognition for different use cases.

## Overview

You can access Revenue Recognition product data through:

- Product Dashboard for report downloads and charts
- Sigma
- Reporting API
- Data Pipeline for syncing Sigma tables with a custom data warehouse

This guide helps you interpret how soon completed activities might appear in
each source.

#### Note

All load times listed in this guide are estimates. Actual load times might vary.

## Availability of new transaction data

For the Dashboard, Sigma, and Reporting API, new transaction data appears within
approximately 3-4 hours after transaction completion. For example, ledger
entries for an invoice finalized at 10:00 AM UTC on January 1, 2025 become
available in reports as soon as 01:00 PM UTC the same day.

You can use the Data Pipeline to sync Revenue Recognition data with a custom
data warehouse once every 6 hours. Ledger entries for new transactions appear in
SDP within 8-9 hours.

The availability periods described above apply to the following use cases:

- New activity inside Stripe like charges, invoices, or refunds
- Manual data imports to Revenue Recognition
- Exclusions uploaded to ignore certain transactions

## Exceptions

The following table lists use cases that don’t fall within the availability
periods described above.

Use caseData freshnessLegacy metered subscription’s unbilled usage
estimatesEstimates include usage submitted as of 24 hours agoMobile app store
data imports24 hours after data connector importEstimation of FX Loss for
Customer Balance transactions.Reports reflect these with a 24-hour delay.Changes
to Revenue Recognition rules or chart of account mappingHistorical data reflects
changes within 24 hoursRe-opening an accounting period for
correctionsReprocessed entries reflect changes within 24 hours
## Where to find Data freshness timestamp by interface

InterfaceData freshness valueStripe dashboard (charts and reports)Check the
overview page for data freshness timestamp.Reporting APIRefer to [Reports Data
availability](https://docs.stripe.com/reports/api#data-availability).SigmaCheck
the `data_load_time` column in `revenue_recognition_debits_and_credits`.Stripe
Data PipelineLook at the `data_load_times` table shared in the warehouse.

## Links

- [Reports Data
availability](https://docs.stripe.com/reports/api#data-availability)