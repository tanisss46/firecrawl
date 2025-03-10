# Stripe Connector for the Apple App Store

## Manage your revenue recognition in Stripe by importing data from the Apple App Store.

The [Stripe Connector for the Apple App
Store](https://docs.stripe.com/stripe-data/import-external-data/connectors/apple-app-store)
lets you automatically import subscription purchases from the Apple App Store
into [Stripe Revenue Recognition](https://docs.stripe.com/revenue-recognition).

The benefits of using Revenue Recognition for the Apple App Store are:

- **Near real-time availability**: Set up daily, automated imports from the
Apple App Store. This minimizes manual work and reduces corrections at
month-end.
- **Increased accuracy**: Improve recognition accuracy by considering time zone
differences.
- **Improved refund treatment**: Associate refunds with original purchases, and
generate more accurate refund journal entries that adjust deferred revenue
instead of treating refunds as negative line items.
- **Audit by subscribers**: Break down numbers on a per subscriber basis to help
with audits.

## Get started

To import data from the Apple App Store, [set up the Stripe Connector for the
Apple App
Store](https://docs.stripe.com/stripe-data/import-external-data/connectors/apple-app-store).
It can take up to 24 hours for your reports to reflect imported data.

### Backfill historical data

When you onboard, the connector backfills up to 1 year of historical data.

### Handle Apple transactions previously imported through manual data import

If you previously imported data from the Apple App Store using the Revenue
Recognition [data
import](https://docs.stripe.com/revenue-recognition/data-import#general-import)
feature, you want to avoid double-counting Apple revenue upon switching to the
automated connector.

To migrate from manual data imports to the connector,
[delete](https://docs.stripe.com/revenue-recognition/data-import/manage-imported-data#transactions-deletion)
all Apple transactions from the past year that you manually uploaded using data
import CSVs. The connector replaces these transactions with the entries it
generates during import.

#### Note

Because the connector only backfills up to 1 year of historical data, we
recommend keeping your data import CSV uploads for Apple transactions that
occurred more than 1 year ago.

## Examples

### Subscription purchase

A subscriber purchases 1 unit of a News Plan Monthly subscription on December 3.
The subscription is valid for 1 month, which means the service period is
December 3 to January 3. The customer pays 32 USD, but the developer receives 31
USD.

The developer proceeds count toward revenue rather than customer price, because
the customer price also includes taxes and Apple commissions. Revenue is billed
and paid in full on December 3. Stripe recognizes most of the revenue in
December, and a smaller portion in January.

At the end of January, the summary might look like this:

AccountDecemberJanuaryExternal Asset+31Revenue+28+3Deferred Revenue+3-3
### Subscription refund

A subscriber purchases a 3-month subscription on January 2. The service period
is January 2 to April 2. The customer pays 91 USD, but the developer receives 90
USD. On February 1, the customer receives a full refund.

During a full refund:

- The customer receives their money back.
- Recognized revenue is offset by the refunds in a contra revenue account.
- The unused portion of the subscription revenue is cleared from the deferred
revenue.

The refund reduces the external assets balance by 90 USD. The customer received
30 days of service, so you add 30 USD to the external refunds balance. The
remainder of the deferred revenue–60 USD in this example–is also cleared.

At the end of April, the summary might look like this:

AccountDecemberJanuaryRevenue+30Deferred Revenue+60-60External
Asset+90-90External Refunds+30
### Free trial

Stripe doesn’t generate journal entries for free trials.

## Limitations

The most detailed level of reporting that Stripe can provide is audit by
subscriber. We can’t provide an audit by invoice view because the financial
reports from the Apple App Store don’t include invoice IDs.

Stripe also can’t book tax liability and Apple commissions because Apple doesn’t
provide this data.

## Audit numbers

To view account balances for an Apple subscriber:

- Click a number in the [Monthly
summary](https://docs.stripe.com/revenue-recognition/reports/monthly-summary)
section to view a list of customers. Apple subscribers have names that consist
solely of numbers.
- Click any Apple subscriber to enter the audit view.

## Get answers to your questions about the Stripe Connector for the Apple App Store.

Provide your email address below and our team will be in touch.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

- [Stripe Connector for the Apple App
Store](https://docs.stripe.com/stripe-data/import-external-data/connectors/apple-app-store)
- [Stripe Revenue Recognition](https://docs.stripe.com/revenue-recognition)
- [data
import](https://docs.stripe.com/revenue-recognition/data-import#general-import)
-
[delete](https://docs.stripe.com/revenue-recognition/data-import/manage-imported-data#transactions-deletion)
- [Monthly
summary](https://docs.stripe.com/revenue-recognition/reports/monthly-summary)
- [privacy policy](https://stripe.com/privacy)