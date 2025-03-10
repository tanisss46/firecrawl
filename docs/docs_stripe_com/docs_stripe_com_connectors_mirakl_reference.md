# Mirakl reference

## Default settings for Miraki connector events.

## Scheduled jobs

### Onboarding

```
php bin/console connector:sync:onboarding -q 2>&1
```

- Default setting: every minute.
- Recommended setting: as often as possible.
- Description: fetch newly created Mirakl shops and add the onboarding link to
their Mirakl back office.
- Documentation: [Onboarding
workflow](https://docs.stripe.com/connectors/mirakl/onboarding-sellers).

### Payment validation

```
php bin/console connector:validate:pending-debit -q 2>&1
```

- Default setting: every 5 minutes.
- Recommended setting: < 1 hour.
- Description: fetch newly accepted Mirakl orders, validate the payment on
Mirakl, and capture it on Stripe.
- Documentation: [Payment validation
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-validation).

### Payment split

```
php bin/console connector:dispatch:process-transfer -q 2>&1
```

- Default setting: every 5 minutes.
- Recommended setting: < 1 hour.
- Description: fetch newly debited Mirakl orders and create Stripe Transfers
from the operator to the seller.
- Documentation: [Payment split
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-split).

### Payment refund

```
php bin/console connector:dispatch:process-refund -q 2>&1
```

- Default setting: every 5 minutes.
- Recommended setting: < 1 hour.
- Description: fetch pending Mirakl refunds, create the refund on Stripe,
validate it on Mirakl, and reverse the initial transfer.
- Documentation: [Payment refund
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-refund).

### Payout

```
php bin/console connector:dispatch:process-payout -q 2>&1
```

- Default setting: every day at 1am.
- Recommended setting: synchronized with your Mirakl billing cycles.
- Description: fetch newly created Mirakl
[invoices](https://docs.stripe.com/api/invoices) and create Stripe Transfers and
[Payouts](https://docs.stripe.com/payouts).
- Documentation: [Payouts
workflow](https://docs.stripe.com/connectors/mirakl/payouts#seller-settlement).

### Alerting

```
php bin/console connector:notify:failed-operation -q 2>&1
```

- Default setting: every day at 8am.
- Recommended setting: according to your preference.
- Description: if
[enabled](https://docs.stripe.com/connectors/mirakl/configuration#alerting),
send an email with all the failed transfers, refunds, and payouts.

## Notification

If [enabled](https://docs.stripe.com/connectors/mirakl/configuration#alerting),
the connector sends server to server notifications in the following events.

#### Note

If your endpoint is unreachable or returns an error, an email is sent to your
`TECHNICAL_ALERT_EMAIL`.

### Account updated

A Stripe connected account was updated by the seller or Stripe.

```
{
 "type": "account.updated",
 "payload": {
 "miraklShopId": 2000,
 "stripeUserId": "acct_1032D82eZvKYlo2C"
 }
}
```

### Transfer failed

A transfer failed during the [payment split
job](https://docs.stripe.com/connectors/mirakl/reference#payment-split) or the
[payout job](https://docs.stripe.com/connectors/mirakl/reference#payout).

```
{
 "type": "transfer.failed",
 "payload": {
 "internalId": 5,
 "miraklId": 123,
 "type": "TRANSFER_ORDER",
 "stripeAccountId": "acct_1032D82eZvKYlo2C",
 "miraklShopId": 2003,
 "transferId": null,
 "transactionId": null,
 "amount": 3400,
 "status": "TRANSFER_FAILED",
 "failedReason": "Reason message",
 "currency": "EUR"
 }
}
```

### Refund failed

A refund failed during the [payment refund
job](https://docs.stripe.com/connectors/mirakl/reference#payment-refund) job.

```
{
 "type": "refund.failed",
 "payload": {
 "internalId": 5,
 "miraklOrderId": "order_refunded_5",
 "miraklRefundId": "1100",
 "stripeRefundId": null,
 "stripeReversalId": "trr_10",
 "amount": 3400,
 "status": "REFUND_FAILED",
 "failedReason": "Reason message",
 "currency": "EUR"
 }
}
```

### Payout failed

A payout failed during the [payout
job](https://docs.stripe.com/connectors/mirakl/reference#payout).

```
{
 "type": "payout.failed",
 "payload": {
 "internalId": 12,
 "amount": 2300,
 "currency": "EUR",
 "miraklInvoiceId": 2000,
 "stripePayoutId": null,
 "status": "PAYOUT_FAILED",
 "failedReason": "Reason message",
 }
}
```

## Links

- [Onboarding
workflow](https://docs.stripe.com/connectors/mirakl/onboarding-sellers)
- [Payment validation
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-validation)
- [Payment split
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-split)
- [Payment refund
workflow](https://docs.stripe.com/connectors/mirakl/payments#payment-refund)
- [invoices](https://docs.stripe.com/api/invoices)
- [Payouts](https://docs.stripe.com/payouts)
- [Payouts
workflow](https://docs.stripe.com/connectors/mirakl/payouts#seller-settlement)
- [enabled](https://docs.stripe.com/connectors/mirakl/configuration#alerting)