# Subscription invoices

## Learn how to manage subscription invoices.

[Invoices](https://docs.stripe.com/api/invoices) are core resources in Stripe,
representing the amount a customer owes. Stripe generates an invoice for every
period in a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) billing
cycle period. You can also manually generate invoices through the Dashboard or
API for off-cycle or one-time payments. Read the guides to learn more about the
lifecycle for [standalone
invoices](https://docs.stripe.com/invoicing/overview#invoice-lifecycle) and
[subscription-generated
invoices](https://docs.stripe.com/billing/subscriptions/overview#invoice-lifecycle).

## Subscription invoice lifecycle

The following sections describe how Stripe handles an invoice throughout a
subscription lifecycle.

### New subscription invoices

When you subscribe a customer, Stripe:

- Creates an invoice.
-
[Finalizes](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
the invoice.

If the payment succeeds on a subscription’s first invoice or the invoice doesn’t
require payment, the invoice transitions to
[status=paid](https://docs.stripe.com/api/invoices/object#invoice_object-status),
and the subscription becomes active.

Until the payment succeeds, the invoice
[status](https://docs.stripe.com/api/invoices/object#invoice_object-status)
remains `open` and
[auto_advance](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection#toggle-auto-advance)
remains `false`. The subscription
[status](https://docs.stripe.com/api/subscriptions/object#subscription_object-status)
remains `incomplete`. Learn how to resolve payment failures for new subscription
invoices that [require a payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method).

In some cases, upgrading or downgrading the subscription also creates a new
invoice. We turn off
[auto_advance](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection#toggle-auto-advance)
for these invoices from the outset.

With a finalized invoice, you can’t add invoice items or make other
modifications that affect the amount due. However, you can still add invoice
items to the customer. The added items apply to the next invoice.

### Subscription renewal invoices

When subscriptions renew, Stripe:

- Creates an invoice.
- Leaves the invoice in a `draft` state for about an hour.
- Attempts to finalize and pay the invoice with the default payment method.
- Changes the invoice status to `paid` if payment succeeds.

When Stripe creates an invoice, you receive an `invoice.created` event at your
configured [webhook
endpoint](https://docs.stripe.com/billing/subscriptions/webhooks). In this case,
the attribute of the invoice
[status](https://docs.stripe.com/api/invoices/object#invoice_object-status) is
`draft`, which means that its invoice items are open for modification.

### Collect payment

When an invoice is due, Stripe tries to collect payment by either [automatically
charging](https://docs.stripe.com/invoicing/automatic-charging) the [payment
method](https://docs.stripe.com/payments/payment-methods/integration-options) on
file, or [emailing the
invoice](https://docs.stripe.com/invoicing/integration#accept-invoice-payment)
to customers.

#### Retry payments

Stripe offers several options for dealing with [failed
payments](https://docs.stripe.com/invoicing/automatic-collection), including
machine-learning powered [Smart
Retries](https://docs.stripe.com/invoicing/automatic-collection#smart-retries).

## Manage subscription invoices

DashboardAPI
The following sections describe how to perform basic actions on invoices in the
Dashboard. For more options around using invoices, see [Managing
invoices](https://docs.stripe.com/invoicing/dashboard/manage-invoices).

### Create an invoice

Stripe automatically creates an invoice for subscriptions at the end of each
billing cycle.

Learn how to [create a one-off
invoice](https://docs.stripe.com/invoicing/dashboard#create-invoice).

Stripe finalizes and sends the invoice in 1 hour. Before the invoice is
finalized, you can edit it. Read more about making changes in the [Invoice
details
page](https://docs.stripe.com/invoicing/dashboard/manage-invoices#invoice-details-page).

### Preview upcoming invoices

The [Retrieve an invoice](https://docs.stripe.com/api#retrieve_invoice) API
provides a mechanism for viewing an existing invoice. Stripe also provides an
endpoint for [retrieving an upcoming
invoice](https://docs.stripe.com/api#upcoming_invoice). This preview reflects
the base price, pending invoice items, discounts, and any existing customer
credit balance.

When fetching the preview, you can also model what the invoice would look like
if you changed the subscription in one of these ways:

- Swapping the underlying price.
- Altering the quantity.
- Applying a trial period.
- Adding a coupon.

## Update the first invoice of a subscription

How you edit the first invoice of a subscription depends on the setting for the
customer’s payment method for the subscription. If unsure, you can check the
payment method setting using the API or the Dashboard.

To check subscription payment method using the API, check the value of
[collection_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method)
on the `Subscriptions` object for the customer. A value of `send_invoice` means
Stripe emails the customer their invoice. A value of `charge_automatically`
means Stripe charges the customer on your behalf using their default payment
method.

To check subscription payment method in the Dashboard, open the [Subscriptions
page](https://dashboard.stripe.com/subscriptions). Then, click the subscription
you want to check to open it’s detailed view. In the **Subscription details**
section, the **Billing method** field value defines the payment method: **Charge
default payment method** or **Send invoice**.

Send invoiceCharge default payment method
For customers that receive invoices, you have a one hour period after creation
before Stripe finalizes the subscription. Within this timeframe you can make
necessary changes to the subscription, like changing amount or line items,
adding a description or metadata, and so on.

After the initial hour, you can no longer make updates. Stripe emails the
invoice to the customer to collect subscription payment.

## Customize invoices

You can customize invoices in several ways, including:

- [Add extra items to a future
invoice](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items)
- [Increase the frequency of
invoices](https://docs.stripe.com/billing/invoices/subscription#pending-items-frequently)
- [Add items to a customer’s first
invoice](https://docs.stripe.com/billing/invoices/subscription#first-invoice-extra)
- [Add items to a draft subscription
invoice](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items)
- [Generate an invoice outside of the subscription
cycle](https://docs.stripe.com/billing/invoices/subscription#generating-invoices)
- [Pause a subscription invoice for
review](https://docs.stripe.com/billing/invoices/subscription#holding-review)
- [Issue a subscription invoice with configurable item
prices](https://docs.stripe.com/billing/invoices/subscription#invoice-item-prices)

### Add extra invoice items to a future invoice

You can add up to 250 invoice items to an invoice. To [add extra invoice
items](https://docs.stripe.com/api/invoiceitems/create) to the next invoice in
the cycle:

```
curl https://api.stripe.com/v1/invoiceitems \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d price=price_CBb6IXqvTLXp3f \
 -d customer=cus_4fdAW5ftNQow1a
```

These one-off items are added to the next invoice created for this customer. To
make sure this is added to a specific subscription, use the optional
`subscription` parameter to apply it to that subscription.

#### Invoice pending items more frequently

Other than [changing the billing
cycle](https://docs.stripe.com/billing/subscriptions/billing-cycle), there are a
few ways to invoice these items without adjusting the normal subscription cycle:

- Create a [one-off invoice](https://docs.stripe.com/invoicing/dashboard) for
the customer.
- Charge a subscription whenever the amount due reaches a
[threshold](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#billing-thresholds).
- Use
[pending_invoice_item_interval](https://docs.stripe.com/api/subscriptions/object#subscription_object-pending_invoice_item_interval)
to specify an interval for how often to bill for any pending invoice items. This
is equivalent to having Stripe create a [one-off
invoice](https://docs.stripe.com/invoicing/dashboard) for the subscription on a
recurring basis.

### Add an extra charge on a subscription’s first invoice

Include a one-time charge to the first subscription invoice using
`add_invoice_items`:

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{RECURRING_PRICE_ID}} \
 -d "add_invoice_items[0][price]"={{PRICE_ID}} \
 -d payment_behavior=default_incomplete
```

#### Caution

If you’re using [Checkout](https://docs.stripe.com/payments/checkout) to create
subscriptions, add extra charges by specifying
[line_items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
with the [client and server
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions).

### Add invoice items to a draft subscription invoice

When a subscription renews and creates an invoice, Stripe sends the
`invoice.created` [webhook](https://docs.stripe.com/webhooks) event. Stripe
[waits approximately one
hour](https://docs.stripe.com/billing/subscriptions/webhooks#understand) before
finalizing the invoice and attempting payment, or sending an email.

During that delay, the invoice is a
[draft](https://docs.stripe.com/api/invoices/object#invoice_object-status) and
is editable. You can [create invoice
items](https://docs.stripe.com/api/invoiceitems/create) on that invoice. Make
sure to provide the
[invoice](https://docs.stripe.com/api/invoiceitems/create#create_invoiceitem-invoice)
parameter when you create these invoice items. Otherwise, they’re added as
pending items and are included in the next subscription period.

These invoice items behave slightly differently than invoice items automatically
generated by Stripe:

- Pending invoice items are always charged when the billing period ends for any
canceled subscription. Canceling a customer’s subscription prevents them from
being billed again *if no invoice items exist*.
- Pending invoice items aren’t prorated when a customer’s subscription changes.

If pending invoice items remain after a subscription cancels, Stripe generates
an invoice and attempts to bill the customer for them at the end of the next
billing period. These invoice items are (similarly) not prorated when a
subscription changes.

#### Manage pending invoice items

You can see a customer’s pending invoice items by navigating to the [Customers
page](https://dashboard.stripe.com/customers), and clicking on their name. If
the customer has a pending invoice item, it appears under **Pending invoice
items**. An invoice item appears as pending if it’s not attached to any invoice.

Under **Pending invoice items**, you can also choose to create a new invoice
item, or instantly invoice everything listed. When you click **Invoice now**, a
dialog appears that lets you select whether to charge the default source or
email the invoice to the customer. Additionally, the dialog gives you the option
to calculate tax automatically.

### Generate an invoice for subscription items outside the billing cycle

You can invoice pending invoice items outside of the regular billing cycle by
[generating a one-off invoice](https://docs.stripe.com/invoicing/dashboard).
Generating a one-off invoice pulls in any pending invoice items that would have
been added to the regularly scheduled invoice.

#### Caution

When you manually generate an invoice, Stripe does not apply the [tax
rates](https://docs.stripe.com/billing/taxes) you may have established on the
subscription. If taxes should apply, you must explicitly [add the tax
rates](https://docs.stripe.com/invoicing/taxes/tax-rates) to the invoice.

### Pause a subscription invoice for review

Rather than automatically attempting payment at the end of a billing period, you
can pause the invoice for review or corrections. To pause an invoice:

- Pause automatic collection within one hour of receiving the `invoice.created`
event. You can do this by setting `auto_advance=false` in the API, or by going
to [Subscriptions and
emails](https://dashboard.stripe.com/settings/billing/automatic) in the
Dashboard. Locate the pause payment section, and click **Set up** to make
changes. This feature prevents Stripe from automatically attempting payment from
your customer for the invoice amount, and from emailing the invoice.
- Review the invoice.
- After you’re ready to charge the customer, resume automatic collection. You
can this by either setting
[auto_advance=true](https://docs.stripe.com/api/invoices/update#update_invoice-auto_advance),
or by updating the pause payment options in the Dashboard.

### Issue a subscription invoice with configurable item prices

You can issue invoices with line item prices that exclude inclusive tax.
Tax-exclusive prices are only shown in the invoice PDF. That means, when using
inclusive tax, the Hosted Invoice Page and invoice emails show tax-inclusive
prices. You can define the settings for net prices in the Dashboard or API.

- **Include inclusive tax**—The invoice PDF displays line item prices including
the inclusive tax. (This is the default.)
- **Exclude tax**—The invoice PDF displays line item prices excluding tax.

#### Order precedence

If you set a default for line item prices at the customer level, it takes
precedence over account-level settings.

## Subscription metadata

After a subscription creates an invoice, it includes the subscription’s
`metadata` in the following ways:

- The invoice’s
[subscription_details.metadata](https://docs.stripe.com/api/invoices/object#invoice_object-subscription_details-metadata)
attribute always contains the subscription’s `metadata` at the time of invoice
creation, even if the subscription `metadata` is later modified.
- The
[metadata](https://docs.stripe.com/api/invoice/line_item#invoice_line_item_object-metadata)
attribute of [invoice line
items](https://docs.stripe.com/api/invoices/line_item) with
[type=“subscription”](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-type)
reflects the most recent subscription `metadata` at the time of retrieving the
invoice, meaning it might differ from the `metadata` at the time of invoice
creation.
- Invoice line items with
[type=“invoiceitem”](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-type)
don’t contain the subscription’s `metadata`.

When you modify a subscription invoice line item’s `metadata` directly, either
with the [invoice line update](https://docs.stripe.com/api/invoices/update_line)
or the [bulk invoice line
update](https://docs.stripe.com/invoicing/bulk-update-line-item) endpoint, the
update request declares the invoice line item `metadata`. Any “inherited”
Subscription `metadata` isn’t preserved implicitly.

[Subscription item
metadata](https://docs.stripe.com/api/subscriptions/object#subscription_object-items-data-metadata)
isn’t automatically propagated to any other Stripe objects.

## Links

- [Invoices](https://docs.stripe.com/api/invoices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [standalone
invoices](https://docs.stripe.com/invoicing/overview#invoice-lifecycle)
- [subscription-generated
invoices](https://docs.stripe.com/billing/subscriptions/overview#invoice-lifecycle)
-
[Finalizes](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
-
[status=paid](https://docs.stripe.com/api/invoices/object#invoice_object-status)
-
[auto_advance](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection#toggle-auto-advance)
-
[status](https://docs.stripe.com/api/subscriptions/object#subscription_object-status)
- [require a payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method)
- [webhook endpoint](https://docs.stripe.com/billing/subscriptions/webhooks)
- [automatically charging](https://docs.stripe.com/invoicing/automatic-charging)
- [payment
method](https://docs.stripe.com/payments/payment-methods/integration-options)
- [emailing the
invoice](https://docs.stripe.com/invoicing/integration#accept-invoice-payment)
- [failed payments](https://docs.stripe.com/invoicing/automatic-collection)
- [Smart
Retries](https://docs.stripe.com/invoicing/automatic-collection#smart-retries)
- [Managing
invoices](https://docs.stripe.com/invoicing/dashboard/manage-invoices)
- [create a one-off
invoice](https://docs.stripe.com/invoicing/dashboard#create-invoice)
- [Invoice details
page](https://docs.stripe.com/invoicing/dashboard/manage-invoices#invoice-details-page)
- [Retrieve an invoice](https://docs.stripe.com/api#retrieve_invoice)
- [retrieving an upcoming invoice](https://docs.stripe.com/api#upcoming_invoice)
-
[collection_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method)
- [Subscriptions page](https://dashboard.stripe.com/subscriptions)
- [add extra invoice items](https://docs.stripe.com/api/invoiceitems/create)
- [changing the billing
cycle](https://docs.stripe.com/billing/subscriptions/billing-cycle)
- [one-off invoice](https://docs.stripe.com/invoicing/dashboard)
-
[threshold](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#billing-thresholds)
-
[pending_invoice_item_interval](https://docs.stripe.com/api/subscriptions/object#subscription_object-pending_invoice_item_interval)
- [Checkout](https://docs.stripe.com/payments/checkout)
-
[line_items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
- [client and server
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [webhook](https://docs.stripe.com/webhooks)
- [waits approximately one
hour](https://docs.stripe.com/billing/subscriptions/webhooks#understand)
-
[invoice](https://docs.stripe.com/api/invoiceitems/create#create_invoiceitem-invoice)
- [Customers page](https://dashboard.stripe.com/customers)
- [tax rates](https://docs.stripe.com/billing/taxes)
- [add the tax rates](https://docs.stripe.com/invoicing/taxes/tax-rates)
- [Subscriptions and
emails](https://dashboard.stripe.com/settings/billing/automatic)
-
[auto_advance=true](https://docs.stripe.com/api/invoices/update#update_invoice-auto_advance)
-
[subscription_details.metadata](https://docs.stripe.com/api/invoices/object#invoice_object-subscription_details-metadata)
-
[metadata](https://docs.stripe.com/api/invoice/line_item#invoice_line_item_object-metadata)
- [invoice line items](https://docs.stripe.com/api/invoices/line_item)
-
[type=“subscription”](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-type)
- [invoice line update](https://docs.stripe.com/api/invoices/update_line)
- [bulk invoice line
update](https://docs.stripe.com/invoicing/bulk-update-line-item)
- [Subscription item
metadata](https://docs.stripe.com/api/subscriptions/object#subscription_object-items-data-metadata)