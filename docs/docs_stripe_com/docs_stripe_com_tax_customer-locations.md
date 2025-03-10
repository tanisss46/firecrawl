# Collect customer addresses

## Learn about collecting customer address information to calculate tax.

Stripe Tax requires your customer’s location to automatically calculate tax.
This requirement applies even if you don’t have an active registration. This
guide helps you understand how to collect addresses from your customers.

## Checkout and Payment Links

Checkout handles the collection of customer addresses for you, including those
created by Payment Links.

## Invoicing, Subscriptions, and custom payment integrations

If you don’t use Payment Links or Checkout, you’re responsible for the
collection of customer addresses.

- Collect and set both the
[country](https://docs.stripe.com/api/customers/object#customer_object-address-country)
and the
[postal_code](https://docs.stripe.com/api/customers/object#customer_object-address-postal_code)
fields on your customer objects.
- Use two-letter country codes ([ISO 3166-1
alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
- When [creating](https://docs.stripe.com/api/customers/create) or [updating a
customer](https://docs.stripe.com/api/customers/update), set
[tax[validate_location]=“immediately”](https://docs.stripe.com/api/customers/create#create_customer-tax-validate_location)
to prevent
[customer_tax_location_invalid](https://docs.stripe.com/error-codes#customer-tax-location-invalid)
errors later.
- Listen for [subscription webhook
events](https://docs.stripe.com/billing/subscriptions/webhooks) as most activity
happens asynchronously.

#### Regional considerationsUnited States

In the United States, sales tax rules and rates vary by state, with some states
having hundreds of districts setting their own rates. We recommend collecting a
full address (including
[line1](https://docs.stripe.com/api/customers/object#customer_object-address-line1),
[city](https://docs.stripe.com/api/customers/object#customer_object-address-city),
and
[state](https://docs.stripe.com/api/customers/object#customer_object-address-state))
from your customers in the US.

### Invoice finalization errors

Finalizing invoices with Stripe Tax requires a recognized customer location.
Location details might be missing or invalid if you update or remove a
customer’s default payment method, or if you didn’t provide
`tax[validate_location]="immediately"` when creating or updating a customer.

If we don’t have a recognized customer location, invoices for a subscription
continue to [finalize
automatically](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
but without calculating taxes. This has the following effects:

- The `automatic_tax[enabled]` parameter changes to `false` on the
[subscription](https://docs.stripe.com/api/subscriptions/object#subscription_object-automatic_tax-enabled)
and
[invoice](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax-enabled).
- The `Invoice[automatic_tax][disabled_reason]` parameter changes to
`finalization_requires_location_inputs`.
- The `Subscription[automatic_tax][disabled_reason]` parameter changes to
`requires_location_inputs`.
- If the subscription has a
[schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules),
we set `automatic_tax[enabled]` to `false` on the current phase and in
`default_settings`. We set the `disabled_reason` in both to
`requires_location_inputs`.
- We send `invoice.updated` and `customer.subscription.updated`
[events](https://docs.stripe.com/billing/subscriptions/webhooks#events) to
inform your integration of these changes.- If there’s a schedule, we also send a
`subscription_schedule.updated` webhook.
- The invoice finalizes without calculating or collecting taxes. It won’t
contain any tax amounts.
- We collect payment as usual according to the [collection
method](https://docs.stripe.com/billing/collection-method) for the invoice.

To review subscriptions without automatic tax calculations in your Stripe
Dashboard, visit your Subscriptions page and filter the view by the **Automatic
tax not enabled** option. To reactivate automatic tax for these subscriptions in
the future, make sure you have at least one valid customer location, and
activate automatic tax through the [Stripe Tax
Dashboard](https://dashboard.stripe.com/tax/migrations).

#### Exceptions to automatically disabling tax

Stripe returns an error and leaves the invoice in a `draft` status when
finalizing with the [API](https://docs.stripe.com/api/invoices/finalize) or
Dashboard without a valid customer location. In the API, this returns an HTTP
400 error with a `code` of `customer_tax_location_invalid`.

Similarly, for automatic finalization of standalone invoices without a
subscription, the invoice remains a draft if the customer location isn’t valid.
We send an
[invoice.finalization_failed](https://docs.stripe.com/api/events/types#event_types-invoice.finalization_failed)
event with the invoice
[last_finalization_error[code]](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error-code)
being `customer_tax_location_invalid`.

How you recover from a `customer_tax_location_invalid` error depends on whether
you have or can collect a customer address.

- If you have a customer address or can collect it, update the customer and
finalize the invoice manually.- [Update the
customer](https://docs.stripe.com/api/customers/update) with
[tax[validate_location]=“immediately”](https://docs.stripe.com/api/customers/create#create_customer-tax-validate_location)
to make sure that the new address is valid.
- [Finalize](https://docs.stripe.com/api/invoices/finalize) the invoice.
- If you don’t have a customer address or can’t collect it, disable Stripe Tax
for the invoice and its subscription, and finalize the invoice manually.-
[Update the affected
invoice](https://docs.stripe.com/api/invoices/update#update_invoice-automatic_tax)
with `automatic_tax[enabled]=false`.
- [Update the affected
subscription](https://docs.stripe.com/api/subscriptions/update#update_subscription-automatic_tax-enabled)
with `automatic_tax[enabled]=false`.
- [Finalize the invoice](https://docs.stripe.com/api/invoices/finalize).
[OptionalWhich customer address we
use](https://docs.stripe.com/tax/customer-locations#address-hierarchy)[OptionalMinimal
address
collection](https://docs.stripe.com/tax/customer-locations#supported-formats)[OptionalRegional
considerations](https://docs.stripe.com/tax/customer-locations#region-specific)
## See also

- [Understanding zero tax](https://docs.stripe.com/tax/zero-tax)
- [Available tax codes](https://docs.stripe.com/tax/tax-codes)
- [How tax is calculated](https://docs.stripe.com/tax/calculating)

## Links

-
[country](https://docs.stripe.com/api/customers/object#customer_object-address-country)
-
[postal_code](https://docs.stripe.com/api/customers/object#customer_object-address-postal_code)
- [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
- [creating](https://docs.stripe.com/api/customers/create)
- [updating a customer](https://docs.stripe.com/api/customers/update)
-
[tax[validate_location]=“immediately”](https://docs.stripe.com/api/customers/create#create_customer-tax-validate_location)
-
[customer_tax_location_invalid](https://docs.stripe.com/error-codes#customer-tax-location-invalid)
- [subscription webhook
events](https://docs.stripe.com/billing/subscriptions/webhooks)
-
[line1](https://docs.stripe.com/api/customers/object#customer_object-address-line1)
-
[city](https://docs.stripe.com/api/customers/object#customer_object-address-city)
-
[state](https://docs.stripe.com/api/customers/object#customer_object-address-state)
- [finalize
automatically](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
-
[subscription](https://docs.stripe.com/api/subscriptions/object#subscription_object-automatic_tax-enabled)
-
[invoice](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax-enabled)
-
[schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
- [events](https://docs.stripe.com/billing/subscriptions/webhooks#events)
- [collection method](https://docs.stripe.com/billing/collection-method)
- [Stripe Tax Dashboard](https://dashboard.stripe.com/tax/migrations)
- [API](https://docs.stripe.com/api/invoices/finalize)
-
[invoice.finalization_failed](https://docs.stripe.com/api/events/types#event_types-invoice.finalization_failed)
-
[last_finalization_error[code]](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error-code)
- [Update the affected
invoice](https://docs.stripe.com/api/invoices/update#update_invoice-automatic_tax)
- [Update the affected
subscription](https://docs.stripe.com/api/subscriptions/update#update_subscription-automatic_tax-enabled)
- [Understanding zero tax](https://docs.stripe.com/tax/zero-tax)
- [Available tax codes](https://docs.stripe.com/tax/tax-codes)
- [How tax is calculated](https://docs.stripe.com/tax/calculating)