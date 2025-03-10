# Automatic invoice advancement

## Learn how Stripe Invoicing handles automatic advancement and collection.

Unless you explicitly disable it, invoices you create in the
[Dashboard](https://dashboard.stripe.com/invoices) automatically finalize when
they leave the draft state. However, invoices you create with the API won’t
automatically finalize. You must turn on automatic collection by setting the
[auto_advance](https://docs.stripe.com/api/invoices/update#update_invoice-auto_advance)
property on the invoice to `true`. You must also configure a webhook endpoint to
receive their associated events. When you set `auto_advance` to `false`, you’re
responsible for transitioning the invoice between statuses. Learn more about
[webhook endpoints and finalizing
invoices](https://docs.stripe.com/billing/subscriptions/webhooks#understand).

#### Note

When you turn on automatic collection, Stripe does everything to drive the
invoice towards payment—including automatically finalizing draft invoices after
one hour. During this wait period, the invoice shows a **Scheduled** status.

## Update automatic advancement

You can toggle the `auto_advance` property on `draft` and `open` invoices.
Automatic advancement and collection never occur on invoices that are marked
`uncollectible`, `void`, or `paid`. For these invoices, `auto_advance` is always
set to `false`:

```
curl https://api.stripe.com/v1/invoices/id \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d auto_advance=false
```

## Pause automatic advancement

In some cases, you might want to stop Stripe from automatically advancing your
invoices toward collection. For example, if you want to:

- Use your own business logic to manage the lifecycle of an invoice.
- Decide if and when to send invoice emails on a per-invoice basis.

In both of these cases, use the `auto_advance` property to disable the automatic
advancement and collection behavior.

## Automatic advancement feature comparison

When you set `auto_advance` to `false`, Stripe disables most of the automatic
features for Invoicing—leaving collection up to you. The following table
outlines some key changes in the behavior of automatic collection, depending on
whether `auto_advance` is set to `true` or `false`:

FeatureTrueFalseFinalize drafts to open (after [approximately
1-hour](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle))Emailing
invoices Attempting paymentsRetries (email and charge) Invoice reminder emails
3D Secure reminder emails Email receipts [Stripe
Automation](https://docs.stripe.com/billing/automations)
#### Legend

- = Can be enabled depending on your settings.
- = Configurable in your settings.
- = Not enabled. The invoice isn’t automatically transitioned.

## Links

- [Dashboard](https://dashboard.stripe.com/invoices)
-
[auto_advance](https://docs.stripe.com/api/invoices/update#update_invoice-auto_advance)
- [webhook endpoints and finalizing
invoices](https://docs.stripe.com/billing/subscriptions/webhooks#understand)
- [approximately
1-hour](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)
- [Stripe Automation](https://docs.stripe.com/billing/automations)