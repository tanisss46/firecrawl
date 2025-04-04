# Configure an invoice finalization grace period

## Learn how to configure a grace period for finalizing your invoices.

During the configured finalization grace period, you can continue to report
usage for the previous billing period. When the invoice finalizes, Stripe
updates it to reflect the latest quantity for its billing period. Use this
setting if you need to record late arriving usage data in a previous billing
cycle, or you need more time to record usage for a billing period that already
ended.

Configure how long it takes for invoices enabled for automatic collection to
transition from `draft` to
[finalized](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized).
You can set a delay of up to 72 hours (3 days). Don’t specify a value that’s
longer than your subscription period. For example, if your subscription period
is daily, don’t set a grace period greater than or equal to 24 hours.

#### Regional considerations

Invoice finalization requirements vary by region. Consult your legal advisor for
advice specific to your business.

## Configure the default grace period

- Go to the [Invoice settings
page](https://dashboard.stripe.com/test/settings/billing/invoice).
- Under **Invoice finalization grace period**, review the configured
finalization behavior. The default is set to 1 hour for all invoices.
- To change the default behavior for all invoices, do the following:- Click the
overflow menu () in the **Account default** row, and select **Edit**.
- Under **Invoice finalization delay**, specify the duration between invoice
creation and finalization
- Click **Save**.

## Configure rules for the grace period

Rules allow you to set the grace period for specific groups of invoices. If the
conditions on your rules aren’t met, Stripe uses the default behavior.

You can change the order that we apply rules by clicking **Change order**. You
can’t change the order of the default behavior, which is always applied last.
You can revert to the Stripe default behavior by deleting all other rules and
setting the **Invoice finalization delay** to `1 hour`.

For invoices with multiple products that might satisfy more than one rule,
Stripe applies the more conservative grace period. For example, if an invoice
includes one line item for a usage-based product (72 hours) and a simple
subscription product (1 hour), the invoice finalizes after 72 hours.

The first invoice generated by a subscription set to [charge
automatically](https://docs.stripe.com/api/subscriptions/create#create_subscription-collection_method)
finalizes immediately, regardless of the rules you configure.

- On the [Invoice settings
page](https://dashboard.stripe.com/test/settings/billing/invoice), under
**Invoice finalization grace period**, click **Add rule**.
- On the **Create new rule** page, under **Invoice finalization delay**, specify
the duration between invoice creation and finalization.
- Under **Conditions**, do the following to set the grace period:For invoicesDo
the followingGenerated at the end of a subscription periodSelect Invoice is from
a subscription cycle from the dropdown.With usage-based productsSelect Has a
metered price from the dropdown.With usage-based products from a subscription
cycleSelect Has a metered price from the dropdown. Click Add more conditions,
then select Invoice is from a subscription cycle from the dropdown.
- Click **Save**.

## Add usage to draft invoices

By default, newly recorded usage appears on an invoice when it’s finalized, and
not on the draft invoice. You can delay finalization if you need more time to
aggregate and add usage to your draft invoices. To add usage to existing
invoices, they must meet the following conditions:

- The invoice is in a `draft` state.
- The timestamp from the [meters
request](https://docs.stripe.com/billing/subscriptions/usage-based/configure-grace-period#configuring-meter)
is within the subscription period for the invoice.

If the usage timestamp is for any time after the creation time of the draft
invoice, we append the usage to the next invoice.

You can verify added usage on the [Meters
page](https://dashboard.stripe.com/test/meters) in the Dashboard or using the
[Meters API](https://docs.stripe.com/api/billing/meter).

## Links

-
[finalized](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
- [Invoice settings
page](https://dashboard.stripe.com/test/settings/billing/invoice)
- [charge
automatically](https://docs.stripe.com/api/subscriptions/create#create_subscription-collection_method)
- [Meters page](https://dashboard.stripe.com/test/meters)
- [Meters API](https://docs.stripe.com/api/billing/meter)