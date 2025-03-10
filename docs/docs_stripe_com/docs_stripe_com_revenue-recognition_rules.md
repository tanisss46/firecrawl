# Revenue Recognition rules

## Customize rules to handle revenue treatments to your business.

Configure [Revenue Recognition
rules](https://dashboard.stripe.com/revenue-recognition/rules) to define revenue
treatments specific to your business.

Stripe Revenue Recognition allows you to configure custom rules to handle
revenue treatments specific to your business needs. For example, you can
configure a rule to:

- **Categorize** an [invoice](https://docs.stripe.com/api/invoices) line item as
a tax or fee
- **Book** a transaction amount or invoice line item as a passthrough fee
- **Exclude** transactions from specific customers or test invoices
- **Amortize** revenue over a specified time period relative to payment or
invoice finalization date
- **Recognize** revenue after a specific time period to model a future
fulfillment schedule
- **Allocate** multiple revenue treatments to a single transaction amount

Rules are typically applied to reports within 24 hours. Rules that have
successfully been applied in the latest report have an `active` status. Rules
that haven’t remain in a `processing` status.

## Default rules

Stripe Revenue Recognition provides a set of default rules to model the
[methodology](https://docs.stripe.com/revenue-recognition/methodology) for
handling common Stripe resources.

- For invoice line items with service periods, the line item amount amortizes
evenly over its service period. If a period isn’t set on an invoice line item,
the amount is recognized entirely when the invoice finalizes.
- Other payments not made through an invoice are recognized immediately upon
payment if no service period or fulfillment information exists, or by the
[imported](https://docs.stripe.com/revenue-recognition/data-import) service
period or fulfillment data.

![Default
rules](https://b.stripecdn.com/docs-statics-srv/assets/default-rules.1cdaa035a358fec4294971ba23bddaa1.png)

## Custom rules

Custom rules override Stripe’s default revenue treatment behaviors where
applicable and you can add or modify them on the Stripe Dashboard.

You can apply rules to:

- [Products](https://docs.stripe.com/api/products)
- [Customers](https://docs.stripe.com/api/customers)
- [Invoice line items](https://docs.stripe.com/api/invoices/line_item)
- [Other payments](https://docs.stripe.com/api/charges) (that is, payments that
aren’t associated with invoices)

See how to [create a rule and define revenue
treatments](https://docs.stripe.com/revenue-recognition/rules/create-a-rule).
You can also explore sample rules on tax treatment, pass-through fees,
exclusion, and custom time periods.

## Rule ordering and hierarchy

Each transaction can only have one rule applied to it when processing revenue
reports. In situations where a single transaction fits the “Apply-to” criteria
for multiple rules, rule hierarchy determines which rule to apply to the
transaction. The higher a rule is ranked on the list, the higher the priority
it’s assigned.

You can rearrange the order of the rules by clicking **Change rule order** as
shown below:

![Rules](https://b.stripecdn.com/docs-statics-srv/assets/rules.076bd00821d7a78ec4d541afe8c9b669.png)

After clicking **Change rule order**, you can reorder the rules to adjust their
priorities.

![Rule
order](https://b.stripecdn.com/docs-statics-srv/assets/rule-order.6232b5130188f7e9b253d7f9d197e3f0.png)

## Best practices for effectively maintaining your rules

As your business grows, it’s important to make sure you regularly maintain your
rules to ensure the accuracy of your revenue reports. The following are some
best practices to keep rules correct for your Revenue Recognition reports.

**Know when to create a rule**

When applied correctly, Stripe’s default rules and revenue treatment methodology
for handling
[subscription](https://docs.stripe.com/billing/subscriptions/creating) events
accurately recognize and defer revenue for businesses who require more control
over their unique use.

**Regularly monitor rules to ensure they’re up-to-date**

Billing models, customer types and edge cases can regularly change, and you
should evolve your rules accordingly. To make sure that revenue treatments
remain predictable, periodically check your rules so they’re up-to-date in terms
of hierarchy and effective period.

**Check if your accounting period is open or closed when new rules are applied**

If the effective period for a new rule overlaps with a closed accounting period,
it generates corrections if the rules are retroactively applied to transactions
from past (closed) accounting periods. If you want to avoid this, reopen your
books by opening your accounting period prior to adding the rule.

## See also

- [Create a
rule](https://docs.stripe.com/revenue-recognition/rules/create-a-rule)
- [Examples](https://docs.stripe.com/revenue-recognition/rules/examples)

## Links

- [Revenue Recognition
rules](https://dashboard.stripe.com/revenue-recognition/rules)
- [invoice](https://docs.stripe.com/api/invoices)
- [methodology](https://docs.stripe.com/revenue-recognition/methodology)
- [imported](https://docs.stripe.com/revenue-recognition/data-import)
- [Products](https://docs.stripe.com/api/products)
- [Customers](https://docs.stripe.com/api/customers)
- [Invoice line items](https://docs.stripe.com/api/invoices/line_item)
- [Other payments](https://docs.stripe.com/api/charges)
- [create a rule and define revenue
treatments](https://docs.stripe.com/revenue-recognition/rules/create-a-rule)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Examples](https://docs.stripe.com/revenue-recognition/rules/examples)