# Payment methodsPublic preview

## Learn about which payment methods your customers use most frequently.

Navigate to **Payments** > **Analytics** > [Payment
Methods](https://dashboard.stripe.com/payment-methods) in the Stripe Dashboard
to see how frequently your customers use alternative payment methods (such as
[Link](https://docs.stripe.com/payments/link) or [Buy now, pay
later](https://docs.stripe.com/payments/buy-now-pay-later)) compared to card
payments. If you want to view analytics specifically for card payments, see
[Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance).

#### Public preview

[Payments analytics](https://dashboard.stripe.com/acceptance) is in public
preview. If you’re not part of the public preview, you can still access these
analytics by navigating to **Reporting** > **Reports** > **Payment methods** in
the Dashboard. If you want access to the public preview, you can [join the
waitlist](https://docs.stripe.com/payments/analytics).

## Configure your data set

Use filters to control all of the metrics, charts, and tables on this page.

### Specify payment method

This page displays metrics, charts, and tables specific to a single payment
method. The `Payment methods` filter is set to the payment method with the
highest payment volume in the last four weeks by default.

![Payment methods
filter](https://b.stripecdn.com/docs-statics-srv/assets/filter.d4766f7b745d5444a09de91a2935beea.png)

Payment methods filter

To change the payment method, select the payment method you want from the list.
You only see payment methods with previous payment activity. You can view which
payment methods you’ve configured in
[Settings](https://dashboard.stripe.com/settings/payment_methods).

### Specify currency

When you don’t apply a currency filter, all payments are shown and converted to
your default settlement currency, regardless of whether the original payment was
in a different currency. If you apply a currency filter, you only see data for
payments made in the selected currency. To change the currency, click
**Currency** , and select the currency you want from the list.

### Specify Connect

By default, metrics include charge activity for all of your connected accounts.
Use the `Connected accounts` filter if you want to exclude data from your
connected accounts. Data from [Standard connected
accounts](https://docs.stripe.com/connect/accounts#standard-accounts) is only
visible if you enable [Platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts).

## Download data

To download these analytics, click **Download** at the top of each chart. The
CSV file you download matches any filters you selected, or matches your defaults
if you apply no filters.

## Key metrics

These metrics include all payments that were accepted for the selected payment
method. You can view both the number of accepted payments and payment volume for
your selected period. These metrics don’t currently support data related to
failed, pending, or blocked payments.

## Average order value

The average order value (AOV) is the average amount a customer spends per
accepted payment. This chart can help you identify which specific payment
methods drive incremental spend by your customers. For example, [Buy Now Pay
Later](https://docs.stripe.com/payments/buy-now-pay-later) methods might
encourage higher spending by allowing customers to pay over time. Tracking AOV
over time might also help reveal trends in customer spending behavior. To
calculate the AOV, divide the total revenue for a given period (day, week,
month, and so on) by the total number of accepted payments in the same period.

## Payment method share

Payment method share refers to the distribution of different payment methods
used by customers within a given time period (such as a day, week, or month).
This metric helps you understand the frequency that your customers choose
certain payment methods. Tracking the share over time allows you to analyze
shifts in customer preferences between payment methods. Stripe calculates
payment method share in two ways:

- **Share of payments**: The total number of accepted payments made using the
payment method, divided by the total number of accepted payments in the same
period.
- **Share of volume**: The total amount of accepted payment volume processed
using the payment method, divided by the total accepted payment volume in the
same period.

## See also

- [Glossary](https://docs.stripe.com/payments/analytics/glossary)
- [Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance)
- [Authentication
analytics](https://docs.stripe.com/payments/analytics/authentication)

## Links

- [Payment Methods](https://dashboard.stripe.com/payment-methods)
- [Link](https://docs.stripe.com/payments/link)
- [Buy now, pay later](https://docs.stripe.com/payments/buy-now-pay-later)
- [Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance)
- [Payments analytics](https://dashboard.stripe.com/acceptance)
- [join the waitlist](https://docs.stripe.com/payments/analytics)
- [Settings](https://dashboard.stripe.com/settings/payment_methods)
- [Standard connected
accounts](https://docs.stripe.com/connect/accounts#standard-accounts)
- [Platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [Glossary](https://docs.stripe.com/payments/analytics/glossary)
- [Authentication
analytics](https://docs.stripe.com/payments/analytics/authentication)