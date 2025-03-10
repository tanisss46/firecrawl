# How invoicing works

## Learn about the stages of the invoice lifecycle.

Invoices provide an itemized list of goods and services rendered, which includes
the cost, quantity, and taxes. You can send invoices to customers to collect
payment or you can create an invoice and automatically charge a customer’s saved
payment method.
[Subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
automatically generate invoices for each billing cycle. Learn more about the
[invoice lifecycle for
subscriptions](https://docs.stripe.com/billing/subscriptions/overview#invoice-lifecycle).

When you create an invoice, you can select an existing
[customer](https://docs.stripe.com/invoicing/customer) and
[product](https://docs.stripe.com/invoicing/products-prices) or create and save
new ones. You can also create one-time products that only exist on the current
invoice.

You can use both the [Dashboard](https://docs.stripe.com/invoicing/dashboard)
and the [API](https://docs.stripe.com/api/invoices) to create, edit, and manage
invoices.

## Invoice lifecycle

After they’re created manually or as part of a subscription, invoices move
through a series of statuses as they’re created and processed. Stripe calls this
the automatic collection workflow.

The basic lifecycle for invoices looks like this:

- A newly created invoice has `draft` status.
- Stripe [finalizes an
invoice](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
when it’s ready to be paid by changing its status to `open`. You can no longer
change most details of a finalized invoice.
- Stripe can wait for the customer to pay the invoice or automatically attempt
to pay it using the customer’s default payment method.- If payment succeeds,
Stripe updates the invoice status to `paid`.
- If payment fails, the invoice remains `open`.
- Optionally, you can change the status of an unpaid invoice to `void` or
`uncollectible`.

You can [configure Stripe to send customer
emails](https://docs.stripe.com/invoicing/send-email) at different stages of the
invoice lifecycle, such as when it finalizes an invoice or when automatic
payment fails.

## Invoice statuses

Invoices can have one of five statuses. The actions you can take on an invoice
depend on its status.

StatusDescriptionPossible
Actions[draft](https://docs.stripe.com/invoicing/overview#draft)The invoice
isn’t ready to use. All invoices start in `draft` status.- Edit any part of the
invoice.
- When the invoice is ready to use, finalize it by changing its status to
`open`.
- If the invoice isn’t associated with a subscription,
[delete](https://docs.stripe.com/invoicing/overview#deleted) it.
[open](https://docs.stripe.com/invoicing/overview#open)The invoice is finalized
and awaiting payment.- Send the invoice to a customer for payment.
- Change [only some elements of the
invoice](https://docs.stripe.com/invoicing/invoice-edits). To make more
substantive changes, create a new invoice and void the old one.
- Change the invoice’s status to `paid`, `void`, or `uncollectible`.
[paid](https://docs.stripe.com/invoicing/overview#paid)This invoice is paid.- No
further actions.
[void](https://docs.stripe.com/invoicing/overview#void)This invoice is
canceled.- No further actions.
[uncollectible](https://docs.stripe.com/invoicing/overview#uncollectible)The
customer is unlikely to pay the invoice. Normally, you treat it as bad debt in
your accounting process.- Change the invoice’s status to `void` or `paid`.

### Draft invoices

You can update almost any details of a `draft` invoice. You can also delete it,
unless it’s associated with a subscription. When a `draft` invoice is ready to
send for payment, you finalize it by changing its status to `open`.

You can delete a `draft` invoice. You can’t recover a deleted invoice.

DashboardAPI- Go to the [Invoices
page](https://dashboard.stripe.com/test/invoices).
- Click the overflow menu () next to the invoice.
- Click **Delete draft**.

### Open invoices

The invoice has been finalized and is awaiting customer payment. If its amount
due is less than the [minimum chargeable
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts),
it automatically transitions to `paid` status and Stripe debits the amount from
the [customer’s credit
balance](https://docs.stripe.com/billing/customer/balance).

In the Dashboard, invoices in `open` status can display a different badge, such
as `Past due` or `Retrying`. In some scenarios, you can hover over the badge to
view an explanatory tooltip.

If an open non-subscription invoice is waiting for a payment that’s initiated
but still pending, it shows the `Pending` badge in the list of invoices.
However, its details page shows the `Open` badge.

You can update only a few elements of an open invoice, such as the memo or
metadata. To make more substantive changes, you must [revise the
invoice](https://docs.stripe.com/invoicing/invoice-edits) by replacing it with a
new one.

You can’t delete a finalized invoice. To cancel it, change its status to `void`.

### Paid invoices

The customer has paid the invoice. This status is terminal, which means that the
invoice’s status can never change.

DashboardAPI
To attempt a payment through the Dashboard, open the [Invoice details
page](https://docs.stripe.com/invoicing/dashboard/manage-invoices#invoice-details-page)
and click **Charge customer**.

#### Out of band invoices

If a customer pays an invoice out of band (outside of Stripe), you can manually
change the [status](https://docs.stripe.com/invoicing/overview#invoice-statuses)
to `paid` through the Dashboard or API.

DashboardAPI
You can manually mark an open invoice as paid in the Dashboard. On the invoice
details page, click the overflow menu () and select **Change invoice status**.
In the **Change invoice status** dialog, select **Paid**.

### Void invoices

Voiding an invoice is conceptually similar to deleting or canceling it. However,
voiding an invoice maintains a paper trail, which allows you to look up the
invoice by number. Voided invoices are treated as zero-value for reporting
purposes, and aren’t payable. This status is terminal, which means that the
invoice’s status can never change.

After you void an invoice, the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page) is still
accessible, and displays a message indicating that the invoice has been voided.
You can only void an invoice in `open` or `uncollectible` status.

#### Note

Consult with local regulations to determine whether and how an invoice might be
amended, canceled, or voided in the jurisdiction you’re doing business in. You
might need to [issue another
invoice](https://docs.stripe.com/invoicing/integration#create-invoice-code) or
[credit
note](https://docs.stripe.com/invoicing/integration/programmatic-credit-notes)
instead. Stripe recommends that you consult with your legal counsel for advice
specific to your business.

DashboardAPI
To void an invoice from the Dashboard:

- Go to the **Invoice details** page.
- Click the overflow menu () and select **Change invoice status**.
- In the resulting dialog, select **Void**.

### Uncollectible invoices

Sometimes your customers can’t pay their outstanding bills. For example, assume
that you provide 1,000 USD worth of services to your customer, but they’ve since
declared bankruptcy and have no assets to pay the invoice.

As a result, you decide to write off the invoice as unlikely to be paid. In this
case, you can update the status of the invoice to be `uncollectible`. This
allows you to track the amount owed for reporting purposes as part of your bad
debt accounting process.

DashboardAPI
You can mark an open invoice as uncollectible in the Dashboard. On the invoice
details page, click the overflow menu () and select **Change invoice status**.
In the **Change invoice status** dialog, select **Uncollectible**.

## See also

- [Use the Dashboard](https://docs.stripe.com/invoicing/dashboard)
- [Integrate with the API](https://docs.stripe.com/invoicing/integration)
- [Status transitions and
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions)

## Links

- [Subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [invoice lifecycle for
subscriptions](https://docs.stripe.com/billing/subscriptions/overview#invoice-lifecycle)
- [customer](https://docs.stripe.com/invoicing/customer)
- [product](https://docs.stripe.com/invoicing/products-prices)
- [Dashboard](https://docs.stripe.com/invoicing/dashboard)
- [API](https://docs.stripe.com/api/invoices)
- [finalizes an
invoice](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
- [configure Stripe to send customer
emails](https://docs.stripe.com/invoicing/send-email)
- [only some elements of the
invoice](https://docs.stripe.com/invoicing/invoice-edits)
- [Invoices page](https://dashboard.stripe.com/test/invoices)
- [minimum chargeable
amount](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
- [customer’s credit balance](https://docs.stripe.com/billing/customer/balance)
- [Invoice details
page](https://docs.stripe.com/invoicing/dashboard/manage-invoices#invoice-details-page)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [issue another
invoice](https://docs.stripe.com/invoicing/integration#create-invoice-code)
- [credit
note](https://docs.stripe.com/invoicing/integration/programmatic-credit-notes)
- [Integrate with the API](https://docs.stripe.com/invoicing/integration)
- [Status transitions and
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions)