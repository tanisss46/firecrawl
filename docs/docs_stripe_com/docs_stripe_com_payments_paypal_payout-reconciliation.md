# PayPal payout reconciliation

## Learn how to reconcile payments made through PayPal, a common payment method in Europe.

Reconciliation is the process of matching and verifying payments that have been
received and processed with the corresponding PayPal orders. It only applies to
customers receiving their funds on PayPal, and not on Stripe. Stripe
automatically
[reconciles](https://docs.stripe.com/reports/payout-reconciliation) PayPal
transactions before the payout, whereas this can’t be done if transactions
settle outside of Stripe’s platform. When transactions settle outside of
Stripe’s platform, you’ll use PayPal reporting available on your PayPal account
or with sFTP for reconciliation.

Stripe provides two ways of supporting PayPal transaction reconciliation:

- (Recommended) Using the
[reference](https://docs.stripe.com/payments/paypal/payout-reconciliation#use-reference)
field. This is the preferred option if you have a businesses-generated order or
invoice ID, which you can put in the reference field. After the payment is made
and processed, `my_order_id` appears as `Invoice ID` in the PayPal settlement
report.
- Using the
[transaction_id](https://docs.stripe.com/payments/paypal/payout-reconciliation#use-transaction-id)
from the
[Charge](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-paypal-transaction_id)
object. When the payment is processed, `paypal_capture_id` appears as
`Transaction ID` in the PayPal settlement report. This is recommended only if
you don’t have a business-generated order ID.

## Use Reference

Use the
[reference](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-paypal-reference)
field to populate your own reference for an order on a PayPal payment. One
example of this is an Order ID from PayPal. This reference is visible to the
buyer and also in the [settlement
report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/)
on your PayPal account. To reconcile funds using a `reference`, you can include
it as part of the
[payment_method_options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-paypal)
parameter when creating a PaymentIntent. You can use this `reference` to match
payments made through Stripe with corresponding transactions in the [PayPal
settlement
report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/).
Any subsequent transactions derived from the original Payment transaction, such
as refunds and disputes, are associated with the given `reference`.

The following code sample shows the creation of a PaymentIntent with the
`reference` set in `payment_method_options`:

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=eur \
 -d "payment_method_types[]"=paypal \
 -d "payment_method_options[paypal][reference]"=my_order_id
```

After the payment is made and processed, `my_order_id` is reflected as Invoice
ID in the [PayPal settlement
report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/).

## Use the Charge object’s transaction ID

The
[transaction_id](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-paypal-transaction_id)
field contains the ID used by PayPal to identify a transaction. To reconcile
funds using a `transaction_id`, retrieve the `transaction_id` from the
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-paypal)
field in the Charge object. The `transaction_id` is present only if the payment
has been captured. It’s used to match payments made through Stripe with
corresponding transactions in the [PayPal settlement
report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/).

For example, here’s how you can retrieve the `transaction_id` from the Charge
object:

```
{
 "amount": 1099,
 "amount_captured": 1099,
 "payment_method_details": {
 "paypal": {
 "transaction_id": "paypal_capture_id",
 "payer_id": "ZA889USQQDD37",
 "payer_email": "jenny@example.com",
 "payer_name": "Jenny Rosen"
 },
 "type": "paypal"
 },
 "balance_transaction": "txn_3MrOPxGsnWT9WMaQ19vg30v3",
 "billing_details": {
 "address": {
 "city": "Co. Kerry",
 "country": "IE",
 "line1": "Skellig Michael",
 "line2": "Great Skellig",
 "postal_code": "12345",
```

See all 52 lines
When the payment is processed, `paypal_capture_id` is appears as `Transaction
ID` in the [PayPal settlement
report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/).

## Access your PayPal reports

You can download your PayPal Settlement Report and other reports from
paypal.com, or you can enable sFTP reporting by contacting PayPal.

The Settlement Report provides an end-to-end view of all balance-impacting
transactions within a 24-hour period. This report is used to reconcile money
moving events in a PayPal account with monies that are moved to a linked bank
account.

To access the Settlement report:

- [Log in](https://www.paypal.com/signin) to your PayPal business account.
- Under **Activity**, select **All Reports**.
- Select **Transactions > Settlement**.

Read more about [PayPal reports and how to download
them](https://www.paypal.com/us/cshelp/article/how-do-i-view-and-download-statements-and-reports-help145).

## Links

- [reconciles](https://docs.stripe.com/reports/payout-reconciliation)
-
[Charge](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-paypal-transaction_id)
-
[reference](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-paypal-reference)
- [settlement
report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/)
-
[payment_method_options](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-paypal)
-
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-paypal)
- [Log in](https://www.paypal.com/signin)
- [PayPal reports and how to download
them](https://www.paypal.com/us/cshelp/article/how-do-i-view-and-download-statements-and-reports-help145)