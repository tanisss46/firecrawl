# Billing collection methods

## Configure your preferred method to collect on invoices and subscriptions.

You can set your preferred payment collection method when creating
[invoices](https://docs.stripe.com/api/invoices) and
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating) using
either the Dashboard or API.

## Automatic charging versus manual payments

The collection method determines how Stripe processes the payment for both
products. To collect payments for invoices and subscriptions, you can select
from these methods:

- Automatic charging
- Manual payments

#### Note

Manual payment methods, such as wire transfers, have more rigorous tracking and
reconciliation processes, which [enterprise
clients](https://docs.stripe.com/billing/collection-method#enterprise-clients-wire-transfers)
often require for high transaction volumes. Some payment methods, such as [bank
transfers](https://docs.stripe.com/invoicing/bank-transfer), only support
`send_invoice` and can’t be charged automatically.

### Set a collection method for an invoice

To set a collection method for an invoice through the Invoicing API, use the
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
attribute.

- `charge_automatically`: Lets you automatically charge a customer’s default
payment method to pay invoices.
- `send_invoice`: Sends an invoice for manual payment. Unlike automatic charging
which requires immediate payment, you can give the customer an adjustable
payment window. You can use the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page) and set up [email
notifications and
reminders](https://docs.stripe.com/invoicing/send-email#customer-emails) to
facilitate payment.

### Set a collection method for a subscription

To set a collection method for a subscription through the Subscriptions API, use
the
[collection_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method)
attribute. If you change the collection method for a subscription, only
subsequently created subscription invoices use the new collection method.

- `charge_automatically`: Tells Stripe to automatically charge your customer’s
default payment method to pay the invoice generated for each subscription
period.
- `send_invoice`: Generates an invoice for each billing period, and requires
manual payment. Unlike automatic charging which requires immediate payment, you
can give the customer an adjustable payment window.

#### Automatic charge for free trials without payment method

You can create a free trial for subscription without collecting payment method
from your customers and still set the
[collection_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method)
attribute as `charge_automatically`. During the trial period, customers can [add
their payment details using the Customer
portal](https://docs.stripe.com/billing/subscriptions/trials#use-the-customer-portal-to-collect-payment).
Once the trial ends, customer’s default payment method will be automatically
charged. You can also configure your subscription to pause/cancel if the trial
ends without a payment method. Learn more about [creating free trials without
collecting payment
method.](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment)

## Collection methods and failed payments

Depending on the collection method, failed payments generate different
[subscription
statuses](https://docs.stripe.com/api/subscriptions/object#subscription_object-status)
and [invoice
statuses](https://docs.stripe.com/api/invoices/object#invoice_object-status).

### Failed subscription payments

Creating a subscription with a
[payment_behavior](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)
of `allow_incomplete`, and the `collection_method` set to
`charge_automatically`, immediately attempts payment and marks the subscription
`status` as `incomplete` if the initial payment attempt doesn’t succeed.

Passing a `payment_behavior` of `default_incomplete` will always initialize
subscriptions with an `incomplete` status if the first invoice requires payment.
The resulting PaymentIntent must be confirmed in a separate request in order to
attempt payment.

For both `allow_incomplete` and `default_incomplete`, the subscription becomes
`active` after the first invoice is paid. Subscriptions that do not require
payment upon creation (like those that are trialing) will immediately have a
status of `active`. If the first invoice remains unpaid after 23 hours, the
subscription is set to `incomplete_expired`. This status is final and
irreversible, voiding the open invoice and preventing future invoices.

#### Failed incomplete subscriptions

When a subscription has a status of `incomplete`, you can only update attributes
that won’t result in the creation of an invoice or invoice item, such as its
[metadata](https://docs.stripe.com/api/subscriptions/object#subscription_object-metadata),
[save_default_payment_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-save_default_payment_method),
and
[description](https://docs.stripe.com/api/subscriptions/object#subscription_object-description).

If a payment to renew the subscription fails when you’ve set it to charge
automatically, the subscription transitions to `past_due` and Stripe may mark it
as `canceled` or `unpaid` (depending on your [subscriptions
settings](https://dashboard.stripe.com/settings/billing/automatic)) after Stripe
exhausts all payment retry attempts.

On the other hand, if the subscription’s `collection_method` is set to
`send_invoice`, it becomes `past_due` when its invoice remains unpaid by the due
date. If the customer still hasn’t paid the invoice after you extend the
deadline, Stripe may mark the subscription as `canceled` or `unpaid`, which
again depends on your subscription settings.

When a subscription has a status of `unpaid`, Stripe creates future invoices but
leaves them as drafts. In this case, you have the option to
[resend](https://docs.stripe.com/api/invoices/send) the `past due` invoice and
any created draft invoices to collect payment. Use this feature if you’re trying
to collect payment for unpaid months (such as when you continue to provide the
goods or services related to an unpaid subscription) or leave them closed and
unpaid when you stop providing goods or services.

### Failed invoicing payments

Invoices not associated with subscriptions that have their `collection_method`
set to `charge_automatically` and
[auto-advancement](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
disabled, remain `open` if an initial payment attempt fails. Because
auto-advancement is disabled, Stripe doesn’t automatically close the invoices,
retry them, or transition them to a different status. Learn more about [failed
payment
notifications](https://docs.stripe.com/invoicing/automatic-collection#failed-payment-notifications)
and [managing invoices sent to
customers](https://docs.stripe.com/invoicing/automatic-collection#manage-invoices-sent-customers).

If
[auto-advancement](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
is enabled for the invoice, Stripe may automatically mark the invoice as
`uncollectible` (depending on your [invoice status
settings](https://dashboard.stripe.com/settings/billing/automatic)) after Stripe
exhausts all payment retry attempts.

When the collection method is set to `send_invoice`, the invoice requires manual
payment. If the invoice remains unpaid past the due date, the status becomes
`past_due`, indicating an overdue invoice. If you extend the payment deadline
and the customer still hasn’t paid, you can leave the invoice as `past_due` or
transition it to `uncollectible` or `void`.

## Enterprise clients and wire transfers

For enterprise clients, manual payment methods, such as wire transfers, offer
some advantages. These payment methods often involve more rigorous tracking and
reconciliation processes compared to automated methods, which is crucial for
enterprises that deal with high transaction volumes. By setting the
`collection_method` to `send_invoice`, you can generate clear and
well-documented invoices that enterprise clients can pay using wire transfers—a
commonly preferred payment method for this type of client.

## See also

- [Automatic collection](https://docs.stripe.com/invoicing/automatic-collection)
- [Automatic charging](https://docs.stripe.com/invoicing/automatic-charging)
- [Subscription invoices](https://docs.stripe.com/billing/invoices/subscription)
- [Status transitions and
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions)

## Links

- [invoices](https://docs.stripe.com/api/invoices)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [bank transfers](https://docs.stripe.com/invoicing/bank-transfer)
-
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [email notifications and
reminders](https://docs.stripe.com/invoicing/send-email#customer-emails)
-
[collection_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method)
- [add their payment details using the Customer
portal](https://docs.stripe.com/billing/subscriptions/trials#use-the-customer-portal-to-collect-payment)
- [creating free trials without collecting payment
method.](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment)
- [subscription
statuses](https://docs.stripe.com/api/subscriptions/object#subscription_object-status)
- [invoice
statuses](https://docs.stripe.com/api/invoices/object#invoice_object-status)
-
[payment_behavior](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)
-
[metadata](https://docs.stripe.com/api/subscriptions/object#subscription_object-metadata)
-
[save_default_payment_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-save_default_payment_method)
-
[description](https://docs.stripe.com/api/subscriptions/object#subscription_object-description)
- [subscriptions
settings](https://dashboard.stripe.com/settings/billing/automatic)
- [resend](https://docs.stripe.com/api/invoices/send)
-
[auto-advancement](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
- [failed payment
notifications](https://docs.stripe.com/invoicing/automatic-collection#failed-payment-notifications)
- [managing invoices sent to
customers](https://docs.stripe.com/invoicing/automatic-collection#manage-invoices-sent-customers)
- [Automatic collection](https://docs.stripe.com/invoicing/automatic-collection)
- [Automatic charging](https://docs.stripe.com/invoicing/automatic-charging)
- [Subscription invoices](https://docs.stripe.com/billing/invoices/subscription)
- [Status transitions and
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions)