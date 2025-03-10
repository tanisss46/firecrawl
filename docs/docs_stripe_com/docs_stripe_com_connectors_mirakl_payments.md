# Payments using the Mirakl connector

## Accept payments using Stripe processing on Mirakl.

We categorize [payment
methods](https://docs.stripe.com/payments/payment-methods/overview) into seven
families. Each family has similar features, a single integration, and common
checkout experiences.

You can use one of our [existing connectors](https://docs.stripe.com/connectors)
or [build your own integration](https://docs.stripe.com/payments) to accept
payments.

#### Note

When implementing payments, don’t use any of the
[Connect](https://docs.stripe.com/connect) charge types. The connector takes
care of [splitting the
funds](https://docs.stripe.com/connectors/mirakl/payments#payment-split) based
on your Mirakl orders.

## Payment creation

Choose the payment method families according to the order workflow most adapted
to your use case.

FamilyPay on acceptance Pay on delivery Pay on due date
[Cards](https://docs.stripe.com/payments/accept-a-payment)[Bank
debits](https://docs.stripe.com/payments/bank-debits)[Bank
redirects](https://docs.stripe.com/payments/bank-redirects)[Credit
transfers](https://docs.stripe.com/payments/sources/credit-transfers)[Buy now,
pay
later](https://docs.stripe.com/payments/buy-now-pay-later)[Vouchers](https://docs.stripe.com/payments/vouchers)[Wallets](https://docs.stripe.com/payments/wallets)
Below are some additional guidelines for adapting your payment integration to
your workflows.

### Pay on acceptance

For cards, set the value of
[capture_method](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
option to `manual` when completing the PaymentIntent to authorize only. The
connector [captures the funds
automatically](https://docs.stripe.com/connectors/mirakl/payments#payment-validation)
as soon as all sellers have accepted or refused their respective orders. The
orders must be accepted or refused within 7 days, the validity period of an
authorization.

Because the payment confirmation is immediate for bank redirects, wallets and
buy now, pay later, we recommend setting up your orders to be accepted
automatically and using refunds when sellers can’t fulfill their order.

### Pay on delivery

For cards, you can authorize only during checkout if you have business rules in
place to capture the payment within 7 days. Otherwise, [save the
card](https://docs.stripe.com/payments/save-and-reuse) at checkout and authorize
later.

For bank debits, you can save the bank account at checkout and initiate the
payment after the seller accepts their order.

### Pay on due date

You can use Stripe Billing to [send an
invoice](https://docs.stripe.com/invoicing/dashboard) to your customers who can
then pay using our [hosted invoice
page](https://docs.stripe.com/invoicing/hosted-invoice-page).

## Payment validation

To handle the payment validation of your Mirakl orders, you can rely on the
built-in job or call the
[PA01](https://help.mirakl.net/help/api-doc/operator/mmp.html#PA01) API yourself
if you have specific needs such as offering coupons.

To enable the built-in job, you have to first map the Mirakl order with the
successful Charge by updating the metadata:

```
curl https://api.stripe.com/v1/charges/ch_1Hmloy2eZvKYlo2C2Tx3W00V \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "metadata[mirakl_commercial_order_id]"=123
```

The workflow starts when a seller accepts their logistic order.

- The [payment validation
job](https://docs.stripe.com/connectors/mirakl/reference#payment-validation)
fetches newly accepted Mirakl orders.
- The connector validates the payment in Mirakl.
- For cards, the payment is captured when all the logistic orders are accepted
or refused.

!

## Payment split

The workflow starts when the payment is validated on Mirakl and captured on
Stripe.

- The [payment split
job](https://docs.stripe.com/connectors/mirakl/reference#payment-split) fetches
newly validated Mirakl orders.
- The connector transfers the order amount to the seller after deducting your
commission.

!

## Payment refund

The workflow starts when you request a refund on a Mirakl order.

- The [payment refund
job](https://docs.stripe.com/connectors/mirakl/reference#payment-refund) fetches
newly refunded Mirakl orders.
- The connector creates a refund on Stripe, validates the refund on Mirakl, and
then reverses the transfer used to split the payment.

!

## See also

- [Integration
steps](https://docs.stripe.com/connectors/mirakl#integration-steps).

## Links

- [payment methods](https://docs.stripe.com/payments/payment-methods/overview)
- [existing connectors](https://docs.stripe.com/connectors)
- [build your own integration](https://docs.stripe.com/payments)
- [Connect](https://docs.stripe.com/connect)
- [Cards](https://docs.stripe.com/payments/accept-a-payment)
- [Bank debits](https://docs.stripe.com/payments/bank-debits)
- [Bank redirects](https://docs.stripe.com/payments/bank-redirects)
- [Credit transfers](https://docs.stripe.com/payments/sources/credit-transfers)
- [Buy now, pay later](https://docs.stripe.com/payments/buy-now-pay-later)
- [Vouchers](https://docs.stripe.com/payments/vouchers)
- [Wallets](https://docs.stripe.com/payments/wallets)
-
[capture_method](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
- [save the card](https://docs.stripe.com/payments/save-and-reuse)
- [send an invoice](https://docs.stripe.com/invoicing/dashboard)
- [hosted invoice page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [PA01](https://help.mirakl.net/help/api-doc/operator/mmp.html#PA01)
- [payment validation
job](https://docs.stripe.com/connectors/mirakl/reference#payment-validation)
- [payment split
job](https://docs.stripe.com/connectors/mirakl/reference#payment-split)
- [payment refund
job](https://docs.stripe.com/connectors/mirakl/reference#payment-refund)
- [Integration
steps](https://docs.stripe.com/connectors/mirakl#integration-steps)