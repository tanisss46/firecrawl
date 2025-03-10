# Revenue Recognition transaction overrides

## Learn how to make manual corrections to your Revenue Recognition reports.

#### Warning

Stripe will soon deprecate the transaction override feature. Use the [data
import feature](https://docs.stripe.com/revenue-recognition/data-import)
instead.

It’s possible for the information on a transaction to become inaccurate for
revenue recognition purposes. This can happen for a number of reasons, such as
human error or evolving terms of a sale. The transaction override feature allows
you to make corrections, regardless of when you created the transaction.

## Creating a transaction override

You can find the transaction overrides section at the bottom of the Revenue
Recognition page.

![Add transaction override
modal](https://b.stripecdn.com/docs-statics-srv/assets/transaction-override-add-modal.8d198b30d4dc9c1a53fa374d4d647550.png)

[Enter ID of the transaction model to
override](https://docs.stripe.com/revenue-recognition/overrides#model)
To get started, enter the `id` of the transaction to override. Stripe supports
overrides on the following transaction models:

Transaction modelRestrictions[Invoices](https://docs.stripe.com/api/invoices)To
override line-item-level details, use the [data import
feature](https://docs.stripe.com/revenue-recognition/data-import).[Charges](https://docs.stripe.com/api/charges)You
can’t override charges that are [associated with an
invoice](https://docs.stripe.com/api/charges/object#charge_object-invoice).
Instead, override the invoice itself.
You can find the `id` of a transaction in the Dashboard or using the API. If the
transaction occurred in a previous month, you can also find it in the following
report downloads when formatted by
[invoice](https://docs.stripe.com/api/invoices):

- Invoice Statement
- Debits and credits
- Corrections
[Choose the override
type](https://docs.stripe.com/revenue-recognition/overrides#override)
The following override types are available:

Override Type DescriptionRecognition period start and end datesThe start date
and end dates correspond to when the service started and ended. The revenue of
this transaction is recognized within this period. Start and end dates can have
the same value, in which case revenue is recognized all at once. Read more about
[how transaction overrides
work](https://docs.stripe.com/revenue-recognition/overrides#how-transaction-overrides-work)
below.Transaction exclusionExcluding a transaction removes all records of it
from revenue recognition. This only works for invoices that are either
[voided](https://docs.stripe.com/invoicing/overview#void) or [manually marked as
paid](https://docs.stripe.com/invoicing/overview#paid), and have no customer
balance applied to them.
## How transaction overrides work

You can create transaction overrides for transactions that occurred in both past
accounting periods and in the current accounting period. If the transaction
occurred in a past accounting period, corrections are implemented prospectively
at the end of the current accounting period. You can view these corrections in
the reports for the current period after it closes.

If the overridden transaction occurred in the current accounting period, it’s
not reflected as a correction in the current period. Instead, it’s recognized
using the new attributes from the override.

Creating a transaction override doesn’t alter the attributes of the transaction
model being overridden.

You can make changes to a transaction override by deleting the override and
creating a new one. If you delete an override that impacts transactions in
closed [accounting
periods](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control),
the first open accounting period will reflect the effect of the deletion. If the
deleted override impacts transactions in open accounting periods, the effect
applies directly to those accounting periods.

#### Note

If you have any feedback on how we can improve transaction overrides to better
suit your accounting needs, visit https://support.stripe.com/.

## Links

- [data import feature](https://docs.stripe.com/revenue-recognition/data-import)
- [Invoices](https://docs.stripe.com/api/invoices)
- [Charges](https://docs.stripe.com/api/charges)
- [associated with an
invoice](https://docs.stripe.com/api/charges/object#charge_object-invoice)
- [how transaction overrides
work](https://docs.stripe.com/revenue-recognition/overrides#how-transaction-overrides-work)
- [voided](https://docs.stripe.com/invoicing/overview#void)
- [manually marked as paid](https://docs.stripe.com/invoicing/overview#paid)
- [accounting
periods](https://docs.stripe.com/revenue-recognition/revenue-settings/accounting-period-control)