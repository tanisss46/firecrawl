# Tax rates and IDs

## Assign tax rates to draft invoices for automatic tax calculation.

If you’re looking for automated tax calculation where you don’t need to define
the rates, use [Stripe Tax](https://docs.stripe.com/tax).

After you [create a tax rate](https://docs.stripe.com/billing/taxes/tax-rates),
you can assign it:

- On individual [invoice](https://docs.stripe.com/api/invoices) items.
- On the entire subtotal of the invoice.

#### Note

Stripe recommends that you assign a tax rate on individual invoice items.

## Set tax rates on individual items

You can set tax rates on individual items using the
[Dashboard](https://dashboard.stripe.com/invoices/create) or
[API](https://docs.stripe.com/api/tax_rates). You can add up to five tax rates
to each line item.

DashboardAPI
If you’re creating an invoice through the Dashboard, assign tax rates to
individual line items.

## Set default tax rates for the entire invoice

If you sell one type of product, or have simple tax needs, you can set a default
tax rate on the invoice. Default tax rates apply to all invoice line items. For
more complex use cases, you can also set an item-level tax rate that overrides
the default tax rate. You can add up to five default tax rates to each invoice.

DashboardAPI
If you’re creating an invoice through the Dashboard, you can assign a default
tax rate after you add an item.

## Links

- [Stripe Tax](https://docs.stripe.com/tax)
- [create a tax rate](https://docs.stripe.com/billing/taxes/tax-rates)
- [invoice](https://docs.stripe.com/api/invoices)
- [Dashboard](https://dashboard.stripe.com/invoices/create)
- [API](https://docs.stripe.com/api/tax_rates)