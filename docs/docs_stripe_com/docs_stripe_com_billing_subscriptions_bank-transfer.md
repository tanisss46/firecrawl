# Set up a subscription with bank transfers

## Learn how to create and charge for a subscription with bank transfers.

Use this guide to set up a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) using
[bank transfers](https://docs.stripe.com/payments/bank-transfers) as a payment
method.

[Create a product and
priceDashboardServer-side](https://docs.stripe.com/billing/subscriptions/bank-transfer#create-product-plan-code)
[Products](https://docs.stripe.com/api/products) and
[Prices](https://docs.stripe.com/api/prices) are core resources for
Subscriptions. Create a product and a recurring price by following the steps in
the [product and prices
guide](https://docs.stripe.com/products-prices/getting-started). Save the price
ID—you’ll need it later in this guide.

[Create or retrieve a
customerServer-side](https://docs.stripe.com/billing/subscriptions/bank-transfer#create-customer)
To start, create a [customer](https://docs.stripe.com/api/customers) with a
valid email address, if one doesn’t already exist. The valid email address
ensures that the customer can receive invoices you send to them. Funds from bank
transfers are held in the customer’s [cash
balance](https://docs.stripe.com/payments/customer-balance), so you have to
associate a [Customer](https://docs.stripe.com/api/customers) object with each
bank transfer subscription.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Jenny Rosen" \
 --data-urlencode email="jenny.rosen@example.com"
```

[Create the
subscriptionServer-side](https://docs.stripe.com/billing/subscriptions/bank-transfer#create-subscription)
[Create](https://docs.stripe.com/api/subscriptions/create) the subscription
using the customer ID and price ID from the previous steps.

- Set
[collection_method](https://docs.stripe.com/api/subscriptions/create#create_subscription-collection_method)
to `send_invoice`.
- Set
[days_until_due](https://docs.stripe.com/api/subscriptions/create#create_subscription-days_until_due)
to configure how many days the customer has to pay the
[invoice](https://docs.stripe.com/api/invoices).

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{PRICE_ID}} \
 -d collection_method=send_invoice \
 -d days_until_due=30 \
 -d "payment_settings[payment_method_types][0]"=customer_balance
```

An invoice is sent to the customer when the Subscription is due. The invoice is
marked as paid if the customer has enough funds in their [cash
balance](https://docs.stripe.com/payments/customer-balance). Otherwise, it
contains the necessary information needed for the customer to push funds from
their bank account. This invoice also has a link to the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page). Subsequent
invoices use the price you created in the first step.

Learn more about [bank transfer
invoices](https://docs.stripe.com/invoicing/bank-transfer).

[OptionalCreate a subscription
scheduleServer-side](https://docs.stripe.com/billing/subscriptions/bank-transfer#create-subscription-schedule)[Test
your
integration](https://docs.stripe.com/billing/subscriptions/bank-transfer#test-your-integration)
Use the Stripe Dashboard or CLI to simulate an [inbound transfer of
funds](https://docs.stripe.com/payments/bank-transfers/accept-a-payment#test-your-integration).

As soon as you receive a fund, Stripe performs
[automatic](https://docs.stripe.com/invoicing/bank-transfer#automatic-transfer-reconciliation)
or
[manual](https://docs.stripe.com/invoicing/bank-transfer#manual-reconciliation)
reconciliation of the invoice.

## Links

- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [bank transfers](https://docs.stripe.com/payments/bank-transfers)
- [Products](https://docs.stripe.com/api/products)
- [Prices](https://docs.stripe.com/api/prices)
- [product and prices
guide](https://docs.stripe.com/products-prices/getting-started)
- [customer](https://docs.stripe.com/api/customers)
- [cash balance](https://docs.stripe.com/payments/customer-balance)
- [Create](https://docs.stripe.com/api/subscriptions/create)
-
[collection_method](https://docs.stripe.com/api/subscriptions/create#create_subscription-collection_method)
-
[days_until_due](https://docs.stripe.com/api/subscriptions/create#create_subscription-days_until_due)
- [invoice](https://docs.stripe.com/api/invoices)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [bank transfer invoices](https://docs.stripe.com/invoicing/bank-transfer)
- [inbound transfer of
funds](https://docs.stripe.com/payments/bank-transfers/accept-a-payment#test-your-integration)
-
[automatic](https://docs.stripe.com/invoicing/bank-transfer#automatic-transfer-reconciliation)
-
[manual](https://docs.stripe.com/invoicing/bank-transfer#manual-reconciliation)