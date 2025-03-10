# Integrate with the Invoicing API

## Learn how to create and send an invoice with code.

The [Dashboard](https://dashboard.stripe.com/invoices) is the most common way to
[create invoices](https://docs.stripe.com/invoicing/dashboard#create-invoice).
If you’d like to automate invoice creation, you can integrate with the API.
Build a full, working Invoicing integration using our [sample
integration](https://docs.stripe.com/invoicing/integration/quickstart).

#### Note

You don’t need to integrate with the Payments API to integrate with the
Invoicing API.

[Set up Stripe](https://docs.stripe.com/invoicing/integration#setup)
Use our official libraries for access to the Stripe API:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Create a product](https://docs.stripe.com/invoicing/integration#create-product)
To create a product, enter its name:

```
curl https://api.stripe.com/v1/products \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Gold Special"
```

[Create a price](https://docs.stripe.com/invoicing/integration#create-prices)
[Prices](https://docs.stripe.com/api#prices) define how much and how often to
charge for products. This includes how much the product costs, what currency to
use, and the billing interval (when the price is for a subscription). Like
products, if you only have a few prices, it’s preferable to manage them in the
Dashboard. Use the unit amount to express prices in the lowest unit of the
currency—in this case, cents (10 USD is 1,000 cents, so the unit amount is
1000).

#### Note

As an alternative, if you don’t need to create a price for your product, you can
use the
[amount](https://docs.stripe.com/api/invoiceitems/create#create_invoiceitem-amount)
parameter during invoice item creation.

To create a price and assign it to the product, pass the product ID, unit
amount, and currency. In the following example, the price for the “Gold Special”
product is 10 USD:

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d product={{PRODUCT_ID}} \
 -d unit_amount=1000 \
 -d currency=usd
```

[Create a
customer](https://docs.stripe.com/invoicing/integration#create-customer-code)
The [Customer](https://docs.stripe.com/api#customer_object) object represents
the customer purchasing your product. It’s required for creating an invoice. To
create a customer with a `name`, `email`, and `description`, add the following
code replacing the values with your own:

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Jenny Rosen" \
 --data-urlencode email="jenny.rosen@example.com" \
 -d description="My first customer"
```

After you create the customer, store the customer `id` in your database so that
you can use it later. The next step, for example, uses the customer ID to create
an invoice.

#### Note

See [Create a customer](https://docs.stripe.com/api/customers/create) for
additional parameters.

[Create an
invoice](https://docs.stripe.com/invoicing/integration#create-invoice-code)
Set the
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
attribute to `send_invoice`. For Stripe to mark an invoice as past due, you must
add the
[days_until_due](https://docs.stripe.com/api/invoices/create#create_invoice-days_until_due)
parameter. When you send an invoice, Stripe emails the invoice to the customer
with payment instructions.

```
curl https://api.stripe.com/v1/invoices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d collection_method=send_invoice \
 -d days_until_due=30
```

Then, create an invoice item by passing in the customer `id`, product `price`,
and invoice ID `invoice`.

The maximum number of invoice items is 250.

```
curl https://api.stripe.com/v1/invoiceitems \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d price={{PRICE_ID}} \
 -d invoice={{INVOICE_ID}}
```

If you set `auto_advance` to `false`, you can continue to modify the invoice
until you
[finalize](https://docs.stripe.com/invoicing/integration/workflow-transitions)
it. To finalize a draft invoice, use the Dashboard, send it to the customer, or
pay it. You can also use the
[Finalize](https://docs.stripe.com/api/invoices/finalize) API:

#### Note

If you created the invoice in error,
[void](https://docs.stripe.com/invoicing/overview#void) it. You can also mark an
invoice as
[uncollectible](https://docs.stripe.com/invoicing/overview#uncollectible).

```
curl -X POST https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/finalize \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Accept invoice
payment](https://docs.stripe.com/invoicing/integration#accept-invoice-payment)Send
an InvoiceStripe Elements
Send the invoice to the email address associated with the customer. As soon as
the an invoice is sent, Stripe finalizes it. Many jurisdictions consider
finalized invoices a legal document making certain fields unalterable. If you
send invoices that have already been paid, there’s no reference to the payment
in the email.

#### Note

When you send invoices that have already been paid, the email doesn’t reference
the payment. Stripe sends invoices to the email address associated with the
customer.

```
curl -X POST https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/send \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Handle post-payment
events](https://docs.stripe.com/invoicing/integration#handle-payment-events)
Stripe sends an
[invoice.paid](https://docs.stripe.com/api/events/types?event_types-invoice.paid)
event when an invoice payment completes. Listen for this event to ensure
reliable fulfillment. If your integration relies on only a client-side callback,
the customer could lose connection before the callback executes, which would
result in the customer being charged without your server being notified. Setting
up your integration to listen for asynchronous events is also what enables you
to accept [different types of payment
methods](https://stripe.com/payments/payment-methods-guide) with a single
integration.

#### Note

Successful invoice payments trigger both an
[invoice.paid](https://docs.stripe.com/api/events/types?event_types-invoice.paid)
and
[invoice.payment_succeeded](https://docs.stripe.com/api/events/types?event_types-invoice.payment_succeeded)
event. Both event types contain the same invoice data, so it’s only necessary to
listen to one of them to be notified of successful invoice payments. The
difference is that `invoice.payment_succeeded` events are sent for successful
invoice payments, but aren’t sent when you mark an invoice as
[paid_out_of_band](https://docs.stripe.com/api/invoices/pay#pay_invoice-paid_out_of_band).
`invoice.paid` events, on the other hand, are triggered for both successful
payments and out of band payments. Because `invoice.paid` covers both scenarios,
we typically recommend listening to `invoice.paid` rather than
`invoice.payment_succeeded`.

Use the [Dashboard webhook tool](https://dashboard.stripe.com/webhooks) or
follow the [webhook quickstart](https://docs.stripe.com/webhooks/quickstart) to
receive these events and run actions, such as sending an order confirmation
email to your customer, logging the sale in a database, or starting a shipping
workflow.

In addition to handling the `invoice.paid` event, we recommend handling two
other events when collecting payments with the Payment Element:

EventDescriptionAction[payment_intent.processing](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.processing)Sent
when a customer successfully initiated a payment, but the payment has yet to
complete. This event is most commonly sent when a bank debit is initiated. It’s
followed by either a `invoice.paid` or `invoice.payment_failed` event in the
future.Send the customer an order confirmation that indicates their payment is
pending. For digital goods, you might want to fulfill the order before waiting
for payment to
complete.[invoice.payment_failed](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.payment_failed)Sent
when a customer attempted a payment on an invoice, but the payment failed.If a
payment transitioned from `processing` to `payment_failed`, offer the customer
another attempt to pay.[OptionalCustomize an
invoice](https://docs.stripe.com/invoicing/integration#customize-invoices)
## See also

-
[Post-finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#post-finalized)
- [Use incoming webhooks to get real-time
updates](https://docs.stripe.com/webhooks)

## Links

- [Dashboard](https://dashboard.stripe.com/invoices)
- [create invoices](https://docs.stripe.com/invoicing/dashboard#create-invoice)
- [sample integration](https://docs.stripe.com/invoicing/integration/quickstart)
- [Prices](https://docs.stripe.com/api#prices)
-
[amount](https://docs.stripe.com/api/invoiceitems/create#create_invoiceitem-amount)
- [Customer](https://docs.stripe.com/api#customer_object)
- [Create a customer](https://docs.stripe.com/api/customers/create)
-
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
-
[days_until_due](https://docs.stripe.com/api/invoices/create#create_invoice-days_until_due)
- [finalize](https://docs.stripe.com/invoicing/integration/workflow-transitions)
- [Finalize](https://docs.stripe.com/api/invoices/finalize)
- [void](https://docs.stripe.com/invoicing/overview#void)
- [uncollectible](https://docs.stripe.com/invoicing/overview#uncollectible)
-
[invoice.paid](https://docs.stripe.com/api/events/types?event_types-invoice.paid)
- [different types of payment
methods](https://stripe.com/payments/payment-methods-guide)
-
[invoice.payment_succeeded](https://docs.stripe.com/api/events/types?event_types-invoice.payment_succeeded)
-
[paid_out_of_band](https://docs.stripe.com/api/invoices/pay#pay_invoice-paid_out_of_band)
- [Dashboard webhook tool](https://dashboard.stripe.com/webhooks)
- [webhook quickstart](https://docs.stripe.com/webhooks/quickstart)
-
[payment_intent.processing](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.processing)
-
[invoice.payment_failed](https://docs.stripe.com/api/events/types?lang=php#event_types-payment_intent.payment_failed)
-
[Post-finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#post-finalized)
- [Use incoming webhooks to get real-time
updates](https://docs.stripe.com/webhooks)