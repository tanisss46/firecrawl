# Automate payment retries

## Automatically retry failed payments and reduce involuntary churn.

Although payments can fail for a number of reasons, many of them are
recoverable. You can automatically retry failed payments with Stripe, without
writing code.

Configure the settings in the **Retries** tab of the [Revenue
recovery](https://dashboard.stripe.com/revenue_recovery/retries) Dashboard.

Stripe doesn’t retry payments for:

- Failures where the issuer provided a non-retryable [decline
code](https://docs.stripe.com/billing/revenue-recovery/smart-retries#non-retryable-decline-codes).
- Unavailable payment methods
- Detached connected accounts (Connect only)

Stripe recommends using Smart Retries, but you can also create a custom retry
schedule.

## Payment method ordering

Stripe uses the first payment instrument from this ordered list in retries:

-
[subscription.default_payment_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
-
[subscription.default_source](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_source)
-
[customer.invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
-
[customer.default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source)

When you update payment methods after a failed payment attempt, update the field
where the previous payment failed. For example, if a subscription has a
`default_payment_method`, but you only update
`customer.invoice_settings.default_payment_method`, Stripe continues to retry on
the subscription’s `default_payment_method`.

## Smart Retries

Using machine learning, Smart Retries chooses the best times to retry failed
payment attempts to increase the chance of successfully paying an invoice. The
machine learning system behind Smart Retries uses time-dependent, dynamic
signals, such as:

- The number of different devices that have presented a given payment method in
the last *N* hours.
- The best time to pay (payments made for debit cards in certain countries might
be slightly more successful at 12:01 AM in local time zones).

Based on a combination of these factors, Stripe intelligently assesses when to
retry payments. We continuously learn from new purchaser behaviors and
transactions, which provide for a more targeted approach over traditional
rules-based payment retry logic.

Smart Retries reattempts the charge according to your specifications for the
number of retries and the maximum duration. You can also use
[automations](https://docs.stripe.com/billing/automations) to create different
retry policies for different customer segments.

You can override this behavior by [disabling Smart
Retries](https://dashboard.stripe.com/revenue_recovery/retries) and defining
your own custom retry rules. When you enable dunning, the
[next_payment_attempt](https://docs.stripe.com/api/invoices/object#invoice_object-next_payment_attempt)
attribute indicates when the next collection attempt will be.

## ACH Debit retries

[Enable ACH Debit
retries](https://dashboard.stripe.com/revenue_recovery/retries) to have Stripe
automatically retry failed ACH Debit payments caused by insufficient funds.
Stripe retries the failed ACH Debit a maximum of two times over a 14 day period.

You can turn on retries for recurring subscription invoices, one-off invoices,
or both types of invoice.

Before retrying, make sure you’ve [obtained
authorization](https://docs.stripe.com/payments/ach-direct-debit#mandates) from
your customer to retry a debit on their bank account.

## Webhook events

For both Smart Retries and custom retry schedules, Stripe reattempts the charge
according to your specified schedule. Use the `invoice.payment_failed`
[webhook](https://docs.stripe.com/webhooks) to receive subscription payment
failure events and retry attempt updates.

The
[attempt_count](https://docs.stripe.com/api/invoices/object#invoice_object-next_payment_attempt)
attribute on the `invoice.payment_failed` webhook indicates how many attempts
have been made so far. If a failure returns a non-retryable return code, we
can’t retry invoice payment without a new payment method. Retries continue to be
scheduled, and
[attempt_count](https://docs.stripe.com/api/invoices/object#invoice_object-next_payment_attempt)
continues to increment, but retries only execute after detecting a new payment
method. Unexecuted retries don’t create a new
[Charge](https://docs.stripe.com/api/charges).

The
[next_payment_attempt](https://docs.stripe.com/api/invoices/object#invoice_object-next_payment_attempt)
attribute on the invoice indicates the date when Stripe will attempt the next
collection. For [automations](https://docs.stripe.com/billing/automations)
users,
[next_payment_attempt](https://docs.stripe.com/api/invoices/object#invoice_object-next_payment_attempt)
is no longer set in `invoice.payment_failed` webhooks but is set in
`invoice.updated` webhooks.

### Non-retryable decline codes

If the card issuer returns the payment with a subset of [decline
codes](https://docs.stripe.com/declines/codes) considered as non-retryable, then
Stripe can’t automatically retry the payment. These codes are one of the
following:

- `incorrect_number`
- `lost_card`
- `pickup_card`
- `stolen_card`
- `revocation_of_authorization`
- `revocation_of_all_authorizations`
- `authentication_required`
- `highest_risk_level`

For these failures, the scheduled retries continue but the payment only executes
if you obtain a new payment method.

## Links

- [Revenue recovery](https://dashboard.stripe.com/revenue_recovery/retries)
- [decline
code](https://docs.stripe.com/billing/revenue-recovery/smart-retries#non-retryable-decline-codes)
-
[subscription.default_payment_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
-
[subscription.default_source](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_source)
-
[customer.invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
-
[customer.default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source)
- [automations](https://docs.stripe.com/billing/automations)
-
[next_payment_attempt](https://docs.stripe.com/api/invoices/object#invoice_object-next_payment_attempt)
- [obtained
authorization](https://docs.stripe.com/payments/ach-direct-debit#mandates)
- [webhook](https://docs.stripe.com/webhooks)
- [Charge](https://docs.stripe.com/api/charges)
- [decline codes](https://docs.stripe.com/declines/codes)