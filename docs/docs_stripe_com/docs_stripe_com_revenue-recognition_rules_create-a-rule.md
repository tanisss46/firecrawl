# Create a rule

## Learn how to create a rule.

You can create and manage Revenue Recognition rules from the Stripe Dashboard.
To create a rule, click **Add rule** from the [Rules
page](https://dashboard.stripe.com/revenue-recognition/rules).

A rule consists of the following key components:

- Name
- Apply to
- Revenue treatment and allocation
- Effective period

![Create a
rule](https://b.stripecdn.com/docs-statics-srv/assets/add-rule.26297e9f9ea8ffc213a94784cba9ea27.png)

## Conditions (“Apply to”)

A set of conditions specifies which transactions (for example, charges,
[invoice](https://docs.stripe.com/api/invoices) line items) that a rule applies
to.

#### Caution

A transaction fulfills the condition requirement when all the conditions are
true.

## Effective period

An effective period specifies the time period that a rule applies to.

For an invoice line item, if the finalization time for the invoice falls within
the specified effective period, the invoice line item fulfills the effective
period requirement.

For a charge, if the balance transaction that it corresponds to has a creation
time that falls within the specified effective period, the charge fulfills the
effective period requirement.

#### Caution

For a rule to apply to a transaction, the transaction must fulfill both the
effective period and condition requirements. When you update the effective
period, the rule retroactively applies to previous accounting periods. If the
previous periods are closed, changes are reflected in the first open accounting
period. You can avoid corrections by re-opening previous periods.

## Treatments

When a transaction fulfills both the effective period and condition requirement,
a set of defined treatments are applied.

A treatment consists of its type and the allocation percentage.

The allocation percentage specifies how much of the amount the type of treatment
applies to.

The type of treatment specifies how to treat the amount. Here are the treatment
types that we support:

- Defer and recognize revenue at a specified time (applicable to charges only)
- Categorize the amount as passthrough fees
- Categorize the amount as tax
- Exclude the amount
- Amortize the amount over a specified period (applicable to charges only)
- Amortize the amount over the service period for an invoice line item
(applicable to invoice line items only)

## See also

- [Examples](https://docs.stripe.com/revenue-recognition/rules/examples)

## Links

- [Rules page](https://dashboard.stripe.com/revenue-recognition/rules)
- [invoice](https://docs.stripe.com/api/invoices)
- [Examples](https://docs.stripe.com/revenue-recognition/rules/examples)