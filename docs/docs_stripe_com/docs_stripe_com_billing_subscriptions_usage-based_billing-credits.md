# Billing creditsPublic preview

## Learn how to use billing credits for prepaid or promotional usage-based products or services.

Use credit grants to offer billing credits to your customers in your business
workflows, such as the following:

- **Prepayment**: Grant billing credits to your customers that they can use to
pay for usage-based products or services, such as memberships, pay-as-you-go
plans, subscriptions, or specific products or services.
- **Promotional offering**: Grant billing credits for free to your customers as
a promotional offering. Businesses often offer a limited amount of promotional
credits, and typically with an expiration date.

The following diagram shows how billing credits work with usage-based billing:

Customer
Credit grant

Invoice

Meter events

has (multiple)applies togeneratesaggregated (meter) and rated (price)
## Use cases for billing credits

Refer to the following guidance for using billing credits.

**Approved uses**

- You can issue billing credits to your customers either for free or for a fee.
- Your customers can use billing credits to pay for memberships, pay-as-you-go
plans, subscriptions, or specific products or services that you offer.

**Prohibited uses**

- You can’t issue billing credits as gift cards or gift certificates. Also, you
can’t allow your customers to spend billing credits on, or exchange billing
credits for, gift cards or gift certificates.
- You can’t offer billing credits as stored value to your customers. That means
you can’t grant any billing credits that aren’t intended for spending on
memberships, pay-as-you-go plans, subscriptions, or specific products or
services that you offer.
- You can’t allow your customers to use billing credits for payments to third
parties. For example, you can’t allow them to apply billing credits to purchases
on the website or platform of another business.
- You can’t link billing credits to digital wallets, or allow your customers to
do so. For example, you can’t allow your customers to add billing credits to a
digital wallet, such as Apple Pay or Google Pay.

## Credit grants

A [Credit Grant](https://docs.stripe.com/api/billing/credit-grant) tracks a set
of prepaid or promotional billing credits allocated to a customer. Credit grants
have the following states:

StateDescriptionPendingThe
[available_balance](https://docs.stripe.com/api/billing/credit-balance-summary/object#billing_credit_balance_summary_object-balances-available_balance)
on the credit grant isn’t yet available for use.GrantedThe credit grant is
eligible for use based on the
[effective_at](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-effective_at)
timestamp, which must occur in the future. If you don’t set this field, the
credit grant is effective immediately.DepletedThe balance on the credit grant is
fully used.ExpiredYou can immediately
[expire](https://docs.stripe.com/api/billing/credit-grant/expire) any remaining
credits on a credit grant, or you can specify an expiration time for the credit
grant using the
[expires_at](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-expires_at)
field. Credits won’t expire unless you set this field.VoidedYou can only
[void](https://docs.stripe.com/api/billing/credit-grant/void) credit grants that
you haven’t applied to an invoice, either partially or completely. You can’t
apply voided credit grants to future invoices, but you can expire any remaining
credits.
## Credit grant eligibility

You can apply credit grants to invoices if all of the following are true:

- The invoice’s
[period_end](https://docs.stripe.com/api/invoices/object#invoice_object-period_end)
is on or after the credit grant’s
[effective_at](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-effective_at)
time.
- The invoice’s `period_end` occurs before the credit grant’s
[expires_at](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-expires_at)
time, if set.
- The credit grant has an available balance when the invoice finalizes.
- The credit grant’s currency matches the invoice currency.

You can only apply credit grants to subscription items that use
[metered](https://docs.stripe.com/api/prices/object#price_object-recurring-usage_type)
prices and report usage through
[Meters](https://docs.stripe.com/api/billing/meter).

You can’t apply credit grants to:

- One-off invoices that weren’t created by a subscription.
- One-time invoice items which are added to a subscription’s upcoming invoice,
such as an initial setup fee.
- [Line items](https://docs.stripe.com/api/invoices/object#invoice_object-lines)
on subscription invoices that use
[licensed](https://docs.stripe.com/api/prices/object#price_object-recurring-usage_type)
prices.
- [Line items](https://docs.stripe.com/api/invoices/object#invoice_object-lines)
on subscription invoices that use
[metered](https://docs.stripe.com/api/prices/object#price_object-recurring-usage_type)
prices but report usage through legacy [Usage
Records](https://docs.stripe.com/api/usage_records).

## Apply credit grants

You can apply credit grants to
[subscription](https://docs.stripe.com/api/invoices/object#invoice_object-subscription)
line items that link to a [meter
price](https://docs.stripe.com/api/prices/object#price_object-recurring-meter).
Credit grants apply to invoices after discounts, but before taxes and the
[invoice_credit_balance](https://docs.stripe.com/api/customers/object#customer_object-invoice_credit_balance).

### Price-level applicability

When creating a credit grant, you can configure the [applicability
scope](https://docs.stripe.com/api/billing/credit-grant/create#create_billing_credit_grant-applicability_config-scope-price_type)
to specify a list of metered prices to which a credit grant can apply. If the
price on a subscription item matches one of the credit grant’s applicable
prices, then the credit grant could apply to that item.

### Multiple invoices or line items

If you can apply a credit grant to multiple invoices, the credit applies first
to the invoice that finalizes first. Because subscription invoices finalize
independently as soon as they’re eligible, we can’t guarantee the finalization
order.

If you can apply a credit grant to multiple
[lines](https://docs.stripe.com/api/invoices/object#invoice_object-lines) on the
same invoice, the credit applies to the lines in the order they appear on the
invoice.

### Multiple credit grants

If you can apply multiple credit grants to an invoice or line item, they’re
prioritized as follows:

- **Priority**: Credit grants with higher
[priority](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-priority)
(lower number indicates a higher priority) apply first.
- **Expiration date**: Credit grants with earlier
[expires_at](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-expires_at)
timestamps apply first.
- **Category**: Credit grants with the `promotional` category apply first.
- **Effective date**: Credit grants with earlier
[effective_at](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-effective_at)
timestamps apply first.
- **Created date**: Credit grants with earlier
[created](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-created)
timestamps apply first.

### Upcoming, draft, or finalized invoices

Credits apply to invoices only at the time of
[finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized).
If you apply credits to an
[upcoming](https://docs.stripe.com/api/invoices/upcoming) or
[draft](https://docs.stripe.com/invoicing/overview#draft) invoice, those credits
might change if a finalized invoice uses them first.

**Example 1**: At the end of a cycle, the same set of credits appear on both a
draft invoice and an upcoming invoice. When finalized, the draft invoice uses
the credits. The upcoming invoice adjusts to accurately reflect any remaining
credits from the credit grant.

**Example 2**: A customer has multiple active subscriptions and the same set of
credits appear on an upcoming invoice for all of the subscriptions. If there
aren’t enough credits to apply to all the subscriptions when the invoices
finalize, only some invoices receive the credits. If you use [billing
thresholds](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#billing-thresholds),
they might trigger later than expected because of the credits that apply to
multiple upcoming invoices.

## Credit balance summaries and transactions

The [Credit Balance
Summary](https://docs.stripe.com/api/billing/credit-balance-summary) shows the
following for a customer:

- **Ledger balance**: The balance amount reflects the billing credit balance
after recording all relevant account ledger transactions. A credit grant is
backed by an immutable, append-only ledger.
- **Available balance**: The billing credit balance available for the customer
to use. This amount is equal to the ledger balance less any expired credits or
unrecorded transactions.

A [Credit Balance
Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction)
includes the credits and debits that impact a credit grant. For example, you
might see a credit transaction for initial funding of the credit grant, or a
debit transaction for a credit grant on an invoice.

## Void invoices and issue credit notes

The following is true if you void invoices and issue credit notes:

- [Voiding an invoice](https://docs.stripe.com/api/invoices/void) with credits
applied reinstates the applied balance to the credit grant. If the credit grant
is past the expiration date, the reinstated credits expire immediately.
- Issuing a [Credit Note](https://docs.stripe.com/api/credit_notes/object)
doesn’t refund credit grants applied to an invoice. To restore those billing
credits, you must create a new credit grant.

## Links

- [Credit Grant](https://docs.stripe.com/api/billing/credit-grant)
-
[available_balance](https://docs.stripe.com/api/billing/credit-balance-summary/object#billing_credit_balance_summary_object-balances-available_balance)
-
[effective_at](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-effective_at)
- [expire](https://docs.stripe.com/api/billing/credit-grant/expire)
-
[expires_at](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-expires_at)
- [void](https://docs.stripe.com/api/billing/credit-grant/void)
-
[period_end](https://docs.stripe.com/api/invoices/object#invoice_object-period_end)
-
[metered](https://docs.stripe.com/api/prices/object#price_object-recurring-usage_type)
- [Meters](https://docs.stripe.com/api/billing/meter)
- [Line items](https://docs.stripe.com/api/invoices/object#invoice_object-lines)
- [Usage Records](https://docs.stripe.com/api/usage_records)
-
[subscription](https://docs.stripe.com/api/invoices/object#invoice_object-subscription)
- [meter
price](https://docs.stripe.com/api/prices/object#price_object-recurring-meter)
-
[invoice_credit_balance](https://docs.stripe.com/api/customers/object#customer_object-invoice_credit_balance)
- [applicability
scope](https://docs.stripe.com/api/billing/credit-grant/create#create_billing_credit_grant-applicability_config-scope-price_type)
-
[priority](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-priority)
-
[created](https://docs.stripe.com/api/billing/credit-grant/object#billing_credit_grant_object-created)
-
[finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
- [upcoming](https://docs.stripe.com/api/invoices/upcoming)
- [draft](https://docs.stripe.com/invoicing/overview#draft)
- [billing
thresholds](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#billing-thresholds)
- [Credit Balance
Summary](https://docs.stripe.com/api/billing/credit-balance-summary)
- [Credit Balance
Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction)
- [Voiding an invoice](https://docs.stripe.com/api/invoices/void)
- [Credit Note](https://docs.stripe.com/api/credit_notes/object)