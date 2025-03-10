# Automatic reconciliation

## Let Stripe handle the cash reconciliation for credit transfer payment methods.

#### Warning

This page covers the Sources-based implementation of credit transfers. We
deprecated the Sources API and plan to remove support for local payment methods.
If you currently integrate with Credit Transfers, you must [migrate to the
Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning). We’ll send
email communication with more information about this end of support.

​​Businesses often use credit transfer payments for large deals or new business
relationships. Credit transfer payments can generate a lot of manual work for
your team. Stripe facilitates this process by accepting transfers that pay open
invoices.

For each of your customers, Stripe auto-generates a US virtual bank account
number that can be paid in USD with ACH credit or wires. When your customer sees
an invoice with this virtual bank account, they can send payment to it. ​​Stripe
automatically reconciles the payment with the virtual bank account and the
invoice. Stripe then marks the invoice as paid.

### Transfers versus debits

Using automatic reconciliation means that you don’t need to expose your
sensitive bank account details to users or manually reconcile open invoices with
your bank. With auto-reconciliation for invoices, Stripe can:

- Match incoming payments with invoice amounts.
- Manage overpayment or underpayment, when the amount paid doesn’t match the
invoice.
- Reduce the number of API calls required to transfer funds into Stripe.
- Manage payment retries on open invoices.

## Pay an invoice

If a customer doesn’t have an
[ach_credit_transfer](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-ach_credit_transfer)
subhash, Stripe creates one for every invoice. All invoices include instructions
on where to send payment. Also, each customer has a unique payment address
that’s shared across their invoices. With the `ach_credit_transfer` subhash,
customers can transfer funds through either the US ACH system or domestic wire,
and include an invoice number in the memo field.

#### Note

​​ACH credit transfers only support USD.

As soon as a customer makes a transfer, Stripe matches the payment to an invoice
by checking for an invoice number in the memo field of the transfer. We fulfill
any invoices that we find a match for. If we can’t find a match, we fulfill the
oldest outstanding invoice of the same amount. If we can’t find any outstanding
invoice that has the same amount, then we’ll fulfill as many outstanding
invoices that can be fulfilled with the transfer amount, starting with the
oldest payable invoice. When an invoice is fulfilled, an `invoice.paid` event
occurs (you can receive this event by using
[webhooks](https://docs.stripe.com/invoicing/integration/workflow-transitions)).

You can inspect the status of any ACH credit transfer by viewing the list of
payment methods for the customer in the
[Dashboard](https://dashboard.stripe.com/customers). You can also see the status
by viewing a customer’s sources in the API:

```
curl https://api.stripe.com/v1/customers/cus_9jWC3097MQwYwF/sources \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

Stripe returns a list of sources attached to that customer. The source `type`
for an ACH credit transfer has a value of `ach_credit_transfer`. In the
following response example, the ACH credit transfer receiver is awaiting payment
from the customer:

```
{
 "object": "list",
 "data": [
 {
 "id": "src_19Q3AILlRB0eXbMt81RVDnM9",
 "object": "source",
 "amount": null,
 "client_secret": "src_client_secret_Z0zPIgnR0BVafiMLaJcxI3HS",
 "created": 1481585102,
 "currency": "usd",
 "customer": "cus_9jWC3097MQwYwF",
 "flow": "receiver",
 "livemode": false,
 "metadata": {},
 "owner": {
 "address": null,
 "email": "jenny.rosen@example.com",
 "name": null,
 "phone": null,
 "verified_address": null,
```

See all 45 lines
Occasionally, customers might want to use payment methods outside of Stripe,
such as paper checks. In these situations, Stripe allows you to keep track of
your invoice’s payment status. After you receive an invoice payment from a
customer outside of Stripe, you can manually mark their invoice as paid:

```
curl https://api.stripe.com/v1/invoices/in_18jwqyLlRB0eXbMtrUQ97YBw/pay \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d paid_out_of_band=true
```

## Handle exceptions

If your customer pays an amount that doesn’t match an invoice amount, the funds
aren’t charged and remain in the `Source​` object. If you want to use these
funds to fulfill your invoice, you have a few options:

- **Overpayment**—If a user sends more funds than the invoice requests, Stripe
automatically marks the invoice as paid, using the funds that match the open
invoice. The remaining funds stay in the `Source` receiver. You can manually
apply these funds to an invoice. If you have multiple matching open invoices,
Stripe applies the funds to the oldest invoice.
- **Underpayment**—In your [Subscription and emails
settings](https://dashboard.stripe.com/settings/billing/automatic), you can
specify rules around underpayment in the **Partial payments** section. You can
specify that within a certain margin of error, Stripe auto-reconciles invoices
and credits the difference.

A typical scenario for underpayment might be that a customer’s bank takes funds
from the total amount sent. For example, ​​if the customer sends 100 USD to pay
their 100 USD invoice, the customer’s bank might take 20 USD, which leaves you
with 80 USD. If this difference (which is usually within 20 USD) is acceptable,
you can ​​minimize manual effort by specifying this margin ahead of time.

For any other exceptions:

- ​If the receiver has enough money to pay your invoice, you can claim those
funds in the Dashboard by clicking the **Charge customer** button on the
invoice, or by calling the [Pay
invoice](https://docs.stripe.com/api#pay_invoice) endpoint and specifying the
ACH credit transfer object as the source.
- ​​If the funds to pay the invoice are insufficient and you don’t forgive the
difference, you can ask your customer to send the remaining amount. You can also
void the old invoice, open a new one for the lesser amount, and immediately
click **Charge customer** on it.

If your customer has an ACH credit transfer source with sufficient funds, or a
credit card or bank account on file, you can use those sources to pay the
invoice by calling the [Pay invoice](https://docs.stripe.com/api#pay_invoice)
endpoint with the source you want to use.

## Refund payments

You can refund ACH credit transfer and check payments through either the
[Dashboard](https://dashboard.stripe.com/payments) or the
[API](https://docs.stripe.com/api#create_refund). However, the customer must
specify the account to return the funds to. Stripe automatically contacts the
customer at the email address provided. As soon as the customer provides us with
their account information, we process the refund automatically.

A refund’s initial status is `pending`. If the refund fails, ​​you receive the
`refund.failed` event, and the status of the refund transitions to `failed`.
This means Stripe can’t process the refund, and you must return the funds to
your customer outside of Stripe. This is rare, but might happen if the refunded
account is frozen. Completed refunds have a `succeeded` status.

## Test payment

If ​​you’re in test mode, you can simulate transferring money into the receiver
by updating the owner email on the source to `amount_XXXX@any_domain.com`, where
`XXXX` is the amount of money you want to simulate transferring. ​​The payment
won’t be associated with the invoice unless Stripe has frozen the invoice from
editing. This happens either one hour after
[webhooks](https://docs.stripe.com/webhooks) have been delivered, or when you’ve
sent the customer an email for the invoice. In the Dashboard, you can
immediately send an email by clicking the invoice’s **Send invoice** button.

```
curl https://api.stripe.com/v1/sources/src_19Q3AILlRB0eXbMt81RVDnM9 \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode "owner[email]"="amount_1000@example.com"
```

A few moments after the update request, you can retrieve the `receiver`
parameter:

```
curl https://api.stripe.com/v1/sources/src_19Q3AILlRB0eXbMt81RVDnM9 \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

If the update request succeeded, the `receiver` attribute shows the funds:

```
{
 "object": "list",
 "data": [
 {
 "id": "src_19Q3AILlRB0eXbMt81RVDnM9",
 "object": "source",
 "amount": null,
 "client_secret": "src_client_secret_Z0zPIgnR0BVafiMLaJcxI3HS",
 "created": 1481585102,
 "currency": "usd",
 "customer": "cus_4fdAW5ftNQow1a",
 "flow": "receiver",
 "livemode": false,
 "metadata": {},
 "owner": {
 "address": null,
 "email": "amount_1000@test.com",
 "name": null,
 "phone": null,
 "verified_address": null,
```

See all 45 lines
In this instance, the customer’s open invoice (of the same amount) transitions
to paid. It has a corresponding payment object that displays the details of the
payment.

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [Billing
plan](https://dashboard.stripe.com/settings/billing/plans?utm_source=docs-reconciliation)
-
[ach_credit_transfer](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-ach_credit_transfer)
- [webhooks](https://docs.stripe.com/invoicing/integration/workflow-transitions)
- [Dashboard](https://dashboard.stripe.com/customers)
- [Subscription and emails
settings](https://dashboard.stripe.com/settings/billing/automatic)
- [Pay invoice](https://docs.stripe.com/api#pay_invoice)
- [Dashboard](https://dashboard.stripe.com/payments)
- [API](https://docs.stripe.com/api#create_refund)
- [webhooks](https://docs.stripe.com/webhooks)