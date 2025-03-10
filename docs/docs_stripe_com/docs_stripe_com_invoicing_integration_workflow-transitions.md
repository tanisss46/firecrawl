# Status transitions and finalization

## Learn about invoice status transitions and finalization.

The following graphic shows the different ways that an invoice can transition
from status to status:

!

Status transitions and finalization

## Transitions and endpoints

The following table outlines the status transitions and their endpoints. It also
lists the [webhooks](https://docs.stripe.com/webhooks) that are emitted by the
endpoint, and the resulting status for each:

StatusAPI EndpointEmitted WebhookEnd Status`draft`[DELETE
/v1/invoices/:id](https://docs.stripe.com/api/invoices/delete)`invoice.deleted`(Deleted)`draft`[POST
/v1/invoices/:id/finalize](https://docs.stripe.com/api/invoices/finalize)`invoice.finalized``open``open`[POST
/v1/invoices/:id/pay](https://docs.stripe.com/api/invoices/pay)`invoice.paid``paid``open`[POST
/v1/invoices/:id/pay](https://docs.stripe.com/api/invoices/pay)`invoice.payment_failed``open``open`[POST
/v1/invoices/:id/send](https://docs.stripe.com/api/invoices/send)`invoice.sent``open``open`[POST
/v1/invoices/:id/void](https://docs.stripe.com/api/invoices/void)`invoice.voided``void``open`[POST
/v1/invoices/:id/mark_uncollectible](https://docs.stripe.com/api/invoices/mark_uncollectible)`invoice.marked_uncollectible``uncollectible``uncollectible`[POST
/v1/invoices/:id/pay](https://docs.stripe.com/api/invoices/pay)`invoice.paid``paid``uncollectible`[POST
/v1/invoices/:id/pay](https://docs.stripe.com/api/invoices/pay)`invoice.payment_failed``uncollectible``uncollectible`[POST
/v1/invoices/:id/void](https://docs.stripe.com/api/invoices/void)`invoice.voided``void`
## Finalize draft invoices

When you enable [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection),
Stripe automatically finalizes, and begins automatic collection of the
[invoice](https://docs.stripe.com/billing/invoices/subscription). We wait 1 hour
after receiving a successful response to the `invoice.created` event from all
listening webhooks before attempting payment. If we don’t receive a successful
response within 72 hours, we attempt to finalize and send the invoice. [You can
configure a longer grace
period](https://docs.stripe.com/billing/subscriptions/usage-based/configure-grace-period).

Invoices are initially created with `status=draft`, and you can only edit them
while they’re in this state. When an invoice is ready to be paid, finalize it.
Finalizing an invoice sets `status=open` on the invoice. You can manually
finalize an invoice in the
[Dashboard](https://docs.stripe.com/invoicing/dashboard) or by using the
[Finalize](https://docs.stripe.com/api/invoices/finalize) endpoint. If you’ve
configured [webhook](https://docs.stripe.com/webhooks) endpoints, you receive an
`invoice.finalized` event when an invoice finalizes.

```
curl -X POST https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/finalize \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

In live mode, if your webhook endpoint doesn’t [respond
properly](https://docs.stripe.com/webhooks), Stripe continues retrying the
webhook notification for up to 3 days with an exponential back off. In test
mode, we retry three times over a few hours. During that time, we won’t attempt
to charge the customer unless we receive a successful response. We also send you
an email to notify you that the webhook is failing.

This behavior applies to all webhook endpoints defined on your account,
including cases where a [Connect application](https://stripe.com/works-with) or
other third-party service is having trouble handling incoming webhooks.

[You can configure a longer grace
period](https://docs.stripe.com/billing/subscriptions/usage-based/configure-grace-period).

## Post-finalization

Finalizing an invoice does the following:

- It allows the invoice to be paid.
- It ensures that an invoice number is present.
- It makes certain properties
[immutable](https://docs.stripe.com/invoicing/integration/workflow-transitions#immutable)
on the invoice.
- It creates an incomplete payment intent for the invoice.
- It generates a unique URL where someone can pay the invoice, and a link to
download a [PDF of the
invoice](https://docs.stripe.com/api/invoices/object#invoice_object-invoice_pdf).

#### Caution

If an invoice isn’t finalized, you can’t collect payment.

### Finalized invoice restrictions

After you finalize an invoice, you can’t change certain fields that pertain to
the amount and customer. This is to satisfy the common tax-compliance
requirement that finalized invoices be retained—as they were finalized—for a
legally required minimum time period.

In some jurisdictions, editing fields that modify the total amount due on an
invoice could render the invoice invalid. These are typically fields associated
with your account, customer, line items, or taxes. It’s your responsibility to
make sure that the invoices you create comply with all applicable laws.

If you require updates to the invoice amount after it finalizes, use [credit
notes](https://docs.stripe.com/invoicing/dashboard/credit-notes). Credit notes
allow you to modify the invoice amount by specifying an adjustment in money owed
by the customer. You can issue credit notes for any invoice in an `open` or
`paid` status. Finalizing the invoice copies the following customer fields to it
and makes them immutable:

-
[invoice.customer_address](https://docs.stripe.com/api/invoices/object#invoice_object-customer_address)
-
[invoice.customer_email](https://docs.stripe.com/api/invoices/object#invoice_object-customer_email)
-
[invoice.customer_name](https://docs.stripe.com/api/invoices/object#invoice_object-customer_name)
-
[invoice.customer_phone](https://docs.stripe.com/api/invoices/object#invoice_object-customer_phone)
-
[invoice.customer_shipping](https://docs.stripe.com/api/invoices/object#invoice_object-customer_shipping)
-
[invoice.customer_tax_exempt](https://docs.stripe.com/api/invoices/object#invoice_object-customer_tax_exempt)
-
[invoice.customer_tax_ids](https://docs.stripe.com/api/invoices/object#invoice_object-customer_tax_ids)

If you want to change a customer-related property on an invoice:

- Void the current invoice.
- [Duplicate](https://docs.stripe.com/invoicing/dashboard#modify-invoice) the
voided invoice.
- Update the customer information on the new invoice.

### Emails after finalization

By default, Stripe automatically sends invoices when you set
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
to `send_invoice`. Stripe doesn’t email invoices in the following cases:

- When [charged
automatically](https://docs.stripe.com/invoicing/automatic-charging).
- When [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
is turned off for the invoice.
- When the [Email finalized invoices to
customers](https://dashboard.stripe.com/settings/billing/automatic) option is
turned off.

#### Note

If you turn off the **Email finalized invoices to customers** option, automatic
or manual finalization doesn’t send an invoice.

## Asynchronous payments

Some payment methods require customer interaction to complete the payment—for
example, a European card or bank transfer may require [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) (SCA).

Use the invoice’s
[payment_intent](https://docs.stripe.com/api/invoices/object#invoice_object-payment_intent)
parameter to choose how to handle the response from the payment attempt, which
may be either `success` or `requires_action`.

When the status of the PaymentIntent is `requires_action`, you must have your
user complete a [3D Secure
authentication](https://docs.stripe.com/billing/migration/strong-customer-authentication#scenario-4)
to complete the payment.

Instead of building this yourself, you can rely on Stripe to handle it for you.
[Enable reminder
emails](https://dashboard.stripe.com/settings/billing/automatic) in the
Dashboard so that Stripe can automatically send emails to your customers
whenever `requires_action` occurs. These emails include a link to the [Hosted
Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page), where a
customer can perform all of the actions required to pay the invoice. To learn
more about these emails and how to customize them, see [Sending email
reminders](https://docs.stripe.com/invoicing/send-email).

## Links

- [webhooks](https://docs.stripe.com/webhooks)
- [DELETE /v1/invoices/:id](https://docs.stripe.com/api/invoices/delete)
- [POST
/v1/invoices/:id/finalize](https://docs.stripe.com/api/invoices/finalize)
- [POST /v1/invoices/:id/pay](https://docs.stripe.com/api/invoices/pay)
- [POST /v1/invoices/:id/send](https://docs.stripe.com/api/invoices/send)
- [POST /v1/invoices/:id/void](https://docs.stripe.com/api/invoices/void)
- [POST
/v1/invoices/:id/mark_uncollectible](https://docs.stripe.com/api/invoices/mark_uncollectible)
- [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
- [invoice](https://docs.stripe.com/billing/invoices/subscription)
- [You can configure a longer grace
period](https://docs.stripe.com/billing/subscriptions/usage-based/configure-grace-period)
- [Dashboard](https://docs.stripe.com/invoicing/dashboard)
- [Connect application](https://stripe.com/works-with)
- [PDF of the
invoice](https://docs.stripe.com/api/invoices/object#invoice_object-invoice_pdf)
- [credit notes](https://docs.stripe.com/invoicing/dashboard/credit-notes)
-
[invoice.customer_address](https://docs.stripe.com/api/invoices/object#invoice_object-customer_address)
-
[invoice.customer_email](https://docs.stripe.com/api/invoices/object#invoice_object-customer_email)
-
[invoice.customer_name](https://docs.stripe.com/api/invoices/object#invoice_object-customer_name)
-
[invoice.customer_phone](https://docs.stripe.com/api/invoices/object#invoice_object-customer_phone)
-
[invoice.customer_shipping](https://docs.stripe.com/api/invoices/object#invoice_object-customer_shipping)
-
[invoice.customer_tax_exempt](https://docs.stripe.com/api/invoices/object#invoice_object-customer_tax_exempt)
-
[invoice.customer_tax_ids](https://docs.stripe.com/api/invoices/object#invoice_object-customer_tax_ids)
- [Duplicate](https://docs.stripe.com/invoicing/dashboard#modify-invoice)
-
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [charged automatically](https://docs.stripe.com/invoicing/automatic-charging)
- [Email finalized invoices to
customers](https://dashboard.stripe.com/settings/billing/automatic)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [3D Secure
guide](https://docs.stripe.com/payments/3d-secure/authentication-flow#when-to-use-3d-secure)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
-
[payment_intent](https://docs.stripe.com/api/invoices/object#invoice_object-payment_intent)
- [3D Secure
authentication](https://docs.stripe.com/billing/migration/strong-customer-authentication#scenario-4)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Sending email reminders](https://docs.stripe.com/invoicing/send-email)