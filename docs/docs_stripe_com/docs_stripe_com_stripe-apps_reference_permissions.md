# Permissions reference

## A list of available events and their required permissions.

A Stripe App needs permission to read or write user data. This includes these
situations:

- Accessing Stripe API objects—see [Object
permissions](https://docs.stripe.com/stripe-apps/reference/permissions#object)
- Subscribing to events—see [Event
permissions](https://docs.stripe.com/stripe-apps/reference/permissions#event)

To request permissions, list them in the `permissions` array in your app
manifest file. You can also manage this array from the CLI. Account
administrators that install your app must accept the permissions that you list
before using it.

If your app performs an action it lacks permissions for, Stripe might raise an
[invalid request
error](https://docs.stripe.com/error-handling#invalid-request-errors).

## Manage permissions

You can add a permission to the `permissions` array in your `stripe-app.json`
app manifest file using the following command:

```
stripe apps grant permission "PERMISSION_NAME" "EXPLANATION"
```

Replace:

- `PERMISSION_NAME` with the permission name. You can find permission names for
[objects](https://docs.stripe.com/stripe-apps/reference/permissions#object) and
[events](https://docs.stripe.com/stripe-apps/reference/permissions#event) in the
sections below.
- `EXPLANATION` with an explanation for enabling access. Users see this
explanation when they install your app.

Repeat this step for each permission that you want to add to your application.

For example, after you add the `customer_read` permission, your app manifest
file might look like this:

```
{
 "id": "com.example.app",
 "version": "1.2.3",
 "name": "Example App",
 "icon": "./example_icon_32.png",
 "permissions": [
 {
 "permission": "customer_read",
 "purpose": "Receive access to the customer’s phone number"
 }
 ],
}
```

To remove a permission, you can also use the CLI:

```
stripe apps revoke permission "PERMISSION_NAME"
```

## Object permissions

For each [API object](https://docs.stripe.com/api) your app reads or writes, it
must request at least one of the corresponding permissions.

If you’re [expanding objects](https://docs.stripe.com/expand) in the responses
of your API requests, you must also request at least one corresponding
permission for each API object you expand.

ResourcePermissionDescription
### Account

`connected_account_read`Grants access to read
[Accounts](https://docs.stripe.com/api/accounts)
### Account link

`account_link_write`Grants access to [Account
Links](https://docs.stripe.com/api/account_links)
### Apple Pay Domain

`apple_pay_domain_read`, `apple_pay_domain_write`Grants access to Apple Pay
Domain resources. To use Apple Pay, you need to register your web domains with
Apple. See [domain
registration](https://docs.stripe.com/payments/payment-methods/pmd-registration)
for more information.
### Application Fee

`application_fee_read`, `application_fee_write`Grants access to [Application
Fees](https://docs.stripe.com/api/application_fees)
### Balance

`balance_read`Grants access to [Balance](https://docs.stripe.com/api/balance)
### Balance transaction source

`balance_transaction_source_read`

Grants access to expand the `source` attribute when retrieving [Balance
Transactions](https://docs.stripe.com/api/balance_transactions)

This permission also implies the following permissions: `application_fee_read`,
`balance_read`, `transfer_read`

### Billing clock

`billing_clock_read`, `billing_clock_write`Grants access to [Test
clocks](https://docs.stripe.com/billing/testing/test-clocks)
### Billing meter

`billing_meter_read`, `billing_meter_write`Grants access to [Billing
meters](https://docs.stripe.com/api/billing/meter)
### Charge

`charge_read`, `charge_write`Grants access to
[Charges](https://docs.stripe.com/api/charges)
### Checkout Session

`checkout_session_read`, `checkout_session_write`

Grants access to [Sessions](https://docs.stripe.com/api/checkout/sessions)

This permission also implies the following permissions: `mandate_read`,
`payment_intent_read`, `payment_links_read`, `product_read`,
`setup_intent_read`, `sku_read`

### Configuration

`terminal_configuration_read`, `terminal_configuration_write`Grants access to
[Configurations](https://docs.stripe.com/api/terminal/configuration)
### Confirmation Token

`confirmation_token_read`Grants read access to [Confirmation
Tokens](https://docs.stripe.com/api/confirmation_tokens)
### Confirmation Token (client)

`confirmation_token_client_write`Grants write access to [Confirmation
Tokens](https://docs.stripe.com/api/confirmation_tokens) from the client.
### Connection Token

`terminal_connection_token_write`Grants access to [Connection
Tokens](https://docs.stripe.com/api/terminal/connection_tokens)
### Coupon

`coupon_read`, `coupon_write`Grants access to
[Coupons](https://docs.stripe.com/api/coupons)
### Credit note

`credit_note_read`, `credit_note_write`

Grants access to [Credit Notes](https://docs.stripe.com/api/credit_notes)

This permission also implies the following permissions: `invoice_read`,

### Customer portal

`customer_portal_read`, `customer_portal_write`

Grants access to the [customer
portal](https://docs.stripe.com/api/customer_portal)

If you’re using the customer portal to manage subscriptions or payment methods,
you must also request `elements_write`.

### Customer

`customer_read`, `customer_write`

Grants access to [Customers](https://docs.stripe.com/api/customers)

This permission also implies the following permission: `billing_clock_read`.

### Dispute

`dispute_read`, `dispute_write`Grants access to
[Disputes](https://docs.stripe.com/api/disputes)
### Edit link

`edit_link_write`Grants access to [Login
Links](https://docs.stripe.com/api/account/login_link)
### Elements

`elements_write`Grants access to [Stripe.js
Elements](https://docs.stripe.com/js/elements_object)
### Entitlements

`entitlement_read`Grants access to
[Entitlements](https://docs.stripe.com/billing/entitlements)
### Event

`event_read`Grants access to [Events](https://docs.stripe.com/api/events)
### File

`file_read`, `file_write`Grants access to
[Files](https://docs.stripe.com/api/files)
### Invoice

`invoice_read`, `invoice_write`

Grants access to [Invoices](https://docs.stripe.com/api/invoices)

This permission also implies the following permission: `credit_note_read`

If you’re using the [hosted invoice
page](https://docs.stripe.com/invoicing/hosted-invoice-page) to manage invoices
or payment methods, you must also request `elements_write`.

### Issuing authorization

`issuing_authorization_read`, `issuing_authorization_write`Grants access to
[Authorizations](https://docs.stripe.com/api/issuing/authorizations)
### Issuing card

`issuing_card_read`, `issuing_card_write`Grants access to
[Cards](https://docs.stripe.com/api/issuing/cards)
### Issuing cardholder

`issuing_cardholder_read`, `issuing_cardholder_write`Grants access to
[Cardholders](https://docs.stripe.com/api/issuing/cardholders)
### Issuing dispute

`issuing_dispute_read`, `issuing_dispute_write`Grants access to [Issuing
Disputes](https://docs.stripe.com/api/issuing/disputes)
### Issuing transaction

`issuing_transaction_read, issuing_transaction_write`Grants access to
[Transactions](https://docs.stripe.com/api/issuing/transactions)
### Location

`terminal_location_read`, `terminal_location_write`Grants access to
[Locations](https://docs.stripe.com/api/terminal/locations)
### Mandate

`mandate_read`, `mandate_write`Grants access to
[Mandates](https://docs.stripe.com/api/mandates)
### Order

`order_read`, `order_write`Grants access to
[Orders](https://docs.stripe.com/api/orders_legacy)
### Payment intent

`payment_intent_read`, `payment_intent_write`

Grants access to [PaymentIntents](https://docs.stripe.com/api/payment_intents)

If you’re managing PaymentIntents with [Stripe.js
Elements](https://docs.stripe.com/js/elements_object), you must also request
`elements_write`.

This permission also implies the following permissions: `product_read`,
`sku_read`

### Payment links

`payment_links_read`, `payment_links_write`

Grants access to [Payment Links](https://docs.stripe.com/payment-links)

This permission also implies the following permissions: `mandate_read`,
`product_read`, `sku_read`

### Payment method

`payment_method_read`, `payment_method_write`

Grants access to [PaymentMethods](https://docs.stripe.com/api/payment_methods)

This permission also implies the following permission: `source_read`

### Payout

`payout_read`, `payout_write`Grants access to
[Payouts](https://docs.stripe.com/api/payouts)
### Plan

`plan_read`, `plan_write`Grants access to
[Plans](https://docs.stripe.com/api/plans),
[Prices](https://docs.stripe.com/api/prices), and (implicitly)
[Products](https://docs.stripe.com/api/products)
### Product

`product_read`, `product_write`Grants access to
[Products](https://docs.stripe.com/api/products)
### Promotion Code

`promotion_code_read`, `promotion_code_write`Grants access to [Promotion
Codes](https://docs.stripe.com/api/promotion_codes)
### Quote

`quote_read`, `quote_write`

Grants access to [Quotes](https://docs.stripe.com/api/quotes)

This permission also implies the following permissions: `sku_read`,
`product_read`

### Reader

`terminal_reader_read`, `terminal_reader_write`Grants access to
[Readers](https://docs.stripe.com/api/terminal/readers)
### Report Runs and Report Types

`report_runs_and_report_types_read`Grants read access to [Report
Types](https://docs.stripe.com/api/reporting/report_type) and allows creation of
[Report Runs](https://docs.stripe.com/api/reporting/report_run)
### Review

`review_read`, `review_write`Grants access to
[Reviews](https://docs.stripe.com/api/radar/reviews)
### Secret

`secret_write`Grants access to
[Secrets](https://docs.stripe.com/api/secret_management)
### Setup Intent

`setup_intent_read`, `setup_intent_write`

Grants access to [SetupIntents](https://docs.stripe.com/api/setup_intents)

If you’re managing SetupIntents with [Stripe.js
Elements](https://docs.stripe.com/js/elements_object), you must also request
`elements_write`.

This permission also implies the following permission: `mandate_read`

### Shipping rate

`shipping_rate_read`, `shipping_rate_write`Grants access to [Shipping
Rates](https://docs.stripe.com/api/shipping_rates)
### SKU

`sku_read`, `sku_write`Grants access to [SKUs](https://docs.stripe.com/api/skus)
### Source

`source_read`, `source_write`Grants access to
[Sources](https://docs.stripe.com/api/sources)
### Subscription

`subscription_read`, `subscription_write`Grants access to
[Subscriptions](https://docs.stripe.com/api/subscriptions)
### Tax rate

`tax_rate_read`, `tax_rate_write`Grants access to [Tax
Rates](https://docs.stripe.com/api/tax_rates)
### Tax settings

`tax_settings_read`, `tax_settings_write`,Grants access to [Tax
Settings](https://docs.stripe.com/api/tax/settings)
### Tax transaction

`tax_calculations_and_transactions_read`,
`tax_calculations_and_transactions_write`,Grants access to [Tax Calculations and
Transactions](https://docs.stripe.com/api/tax/transactions)
### Token

`token_read`, `token_write`Grants access to
[Tokens](https://docs.stripe.com/api/tokens)
### Top up

`top_up_read`, `top_up_write`Grants access to
[Top-ups](https://docs.stripe.com/api/topups)
### Transfer

`transfer_read`, `transfer_write`

Grants access to [Transfers](https://docs.stripe.com/api/transfers)

This permission also implies the following permission: `payout_read`,
`payout_write`

### Usage record

`usage_record_read`, `usage_record_write`Grants access to [Usage
Records](https://docs.stripe.com/api/usage_records)
### User Email

`user_email_read`Grants access to user emails
### Webhook

`webhook_read`, `webhook_write`

Grants access to [Webhook
Endpoints](https://docs.stripe.com/api/webhook_endpoints)

For most apps, you don’t need to include`webhook_write`. Instead, set up a
webhook to [listen to events](https://docs.stripe.com/stripe-apps/events) from
your connected accounts. If you still need `webhook_write`, contact [Stripe
Support](https://support.stripe.com/contact/email).

## Event permissions

For each [Event](https://docs.stripe.com/api/events/types) your app subscribes
to, it must request at least one of the corresponding permissions.

EventPermission`file.created``file_read``issuing_personalization_design.activated``issuing_card_read`,`issuing_card_sensitive_read``issuing_personalization_design.deactivated``issuing_card_read`,`issuing_card_sensitive_read``issuing_personalization_design.rejected``issuing_card_read`,`issuing_card_sensitive_read``issuing_personalization_design.updated``issuing_card_read`,`issuing_card_sensitive_read``account.application.authorized``event_read``account.application.deauthorized``event_read``account.external_account.created``connected_account_read``account.external_account.deleted``connected_account_read``account.external_account.updated``connected_account_read``account.updated``connected_account_read``application_fee.created``application_fee_read`,`balance_transaction_source_read``application_fee.refund.updated``application_fee_read`,`balance_transaction_source_read``application_fee.refunded``application_fee_read`,`balance_transaction_source_read``balance.available``balance_read`,`balance_transaction_source_read``billing_portal.configuration.created``checkout_session_read`,`customer_portal_read`,`payment_links_read``billing_portal.configuration.updated``checkout_session_read`,`customer_portal_read`,`payment_links_read``billing_portal.session.created``checkout_session_read`,`customer_portal_read`,`payment_links_read``cash_balance.funds_available``customer_read``charge.captured``charge_read``charge.dispute.closed``dispute_read``charge.dispute.created``dispute_read``charge.dispute.funds_reinstated``dispute_read``charge.dispute.funds_withdrawn``dispute_read``charge.dispute.updated``dispute_read``charge.expired``charge_read``charge.failed``charge_read``charge.pending``charge_read``charge.refund.updated``charge_read``charge.refunded``charge_read``charge.succeeded``charge_read``charge.updated``charge_read``checkout.session.async_payment_failed``checkout_session_read``checkout.session.async_payment_succeeded``checkout_session_read``checkout.session.completed``checkout_session_read``checkout.session.expired``checkout_session_read``coupon.created``coupon_read``coupon.deleted``coupon_read``coupon.updated``coupon_read``credit_note.created``credit_note_read`,`invoice_read`,`quote_read``credit_note.updated``credit_note_read`,`invoice_read`,`quote_read``credit_note.voided``credit_note_read`,`invoice_read`,`quote_read``customer_cash_balance_transaction.created``balance_transaction_source_read`,`customer_read``customer.created``customer_read``customer.deleted``customer_read``customer.discount.created``customer_read``customer.discount.deleted``customer_read``customer.discount.updated``customer_read``entitlements.active_entitlement_summary.updated``entitlement_read``customer.source.created``customer_read``customer.source.deleted``customer_read``customer.source.expiring``customer_read``customer.source.updated``customer_read``customer.subscription.created``quote_read`,`subscription_read``customer.subscription.deleted``quote_read`,`subscription_read``customer.subscription.paused``quote_read`,`subscription_read``customer.subscription.pending_update_applied``quote_read`,`subscription_read``customer.subscription.pending_update_expired``quote_read`,`subscription_read``customer.subscription.resumed``quote_read`,`subscription_read``customer.subscription.trial_will_end``quote_read`,`subscription_read``customer.subscription.updated``quote_read`,`subscription_read``customer.tax_id.created``customer_read``customer.tax_id.deleted``customer_read``customer.tax_id.updated``customer_read``customer.updated``customer_read``invoice.created``credit_note_read`,`invoice_read`,`quote_read``invoice.deleted``credit_note_read`,`invoice_read`,`quote_read``invoice.finalization_failed``credit_note_read`,`invoice_read`,`quote_read``invoice.finalized``credit_note_read`,`invoice_read`,`quote_read``invoice.marked_uncollectible``credit_note_read`,`invoice_read`,`quote_read``invoice.overdue``credit_note_read`,`invoice_read`,`quote_read``invoice.paid``credit_note_read`,`invoice_read`,`quote_read``invoice.payment_action_required``credit_note_read`,`invoice_read`,`quote_read``invoice.payment_failed``credit_note_read`,`invoice_read`,`quote_read``invoice.payment_succeeded``credit_note_read`,`invoice_read`,`quote_read``invoice.sent``credit_note_read`,`invoice_read`,`quote_read``invoice.upcoming``credit_note_read`,`invoice_read`,`quote_read``invoice.updated``credit_note_read`,`invoice_read`,`quote_read``invoice.voided``credit_note_read`,`invoice_read`,`quote_read``invoice.will_be_due``credit_note_read`,`invoice_read`,`quote_read``invoiceitem.created``credit_note_read`,`invoice_read`,`quote_read``invoiceitem.deleted``credit_note_read`,`invoice_read`,`quote_read``mandate.updated``checkout_session_read`,`mandate_read`,`payment_links_read`,`setup_intent_read``payment_intent.amount_capturable_updated``checkout_session_read`,`payment_intent_read``payment_intent.canceled``checkout_session_read`,`payment_intent_read``payment_intent.created``checkout_session_read`,`payment_intent_read``payment_intent.partially_funded``checkout_session_read`,`payment_intent_read``payment_intent.payment_failed``checkout_session_read`,`payment_intent_read``payment_intent.processing``checkout_session_read`,`payment_intent_read``payment_intent.requires_action``checkout_session_read`,`payment_intent_read``payment_intent.succeeded``checkout_session_read`,`payment_intent_read``payment_link.created``payment_links_read``payment_link.updated``payment_links_read``payment_method.attached``payment_method_read``payment_method.automatically_updated``payment_method_read``payment_method.detached``payment_method_read``payment_method.updated``payment_method_read``payout.canceled``balance_transaction_source_read`,`payout_read`,`transfer_read``payout.created``balance_transaction_source_read`,`payout_read`,`transfer_read``payout.failed``balance_transaction_source_read`,`payout_read`,`transfer_read``payout.paid``balance_transaction_source_read`,`payout_read`,`transfer_read``payout.reconciliation_completed``balance_transaction_source_read`,`payout_read`,`transfer_read``payout.updated``balance_transaction_source_read`,`payout_read`,`transfer_read``person.created``connected_account_read``person.deleted``connected_account_read``person.updated``connected_account_read``plan.created``plan_read``plan.deleted``plan_read``plan.updated``plan_read``price.created``plan_read``price.deleted``plan_read``price.updated``plan_read``product.created``checkout_session_read`,`payment_intent_read`,`payment_links_read`,`product_read`,`quote_read``product.deleted``checkout_session_read`,`payment_intent_read`,`payment_links_read`,`product_read`,`quote_read``product.updated``checkout_session_read`,`payment_intent_read`,`payment_links_read`,`product_read`,`quote_read``promotion_code.created``credit_note_read`,`invoice_read`,`promotion_code_read`,`quote_read``promotion_code.updated``credit_note_read`,`invoice_read`,`promotion_code_read`,`quote_read``quote.accepted``quote_read``quote.canceled``quote_read``quote.created``quote_read``quote.finalized``quote_read``radar.early_fraud_warning.created``charge_read``radar.early_fraud_warning.updated``charge_read``refund.created``charge_read``refund.failed``charge_read``refund.updated``charge_read``reporting.report_run.failed``report_runs_and_report_types_read``reporting.report_run.succeeded``report_runs_and_report_types_read``reporting.report_type.updated``report_runs_and_report_types_read``review.closed``review_read``review.opened``review_read``setup_intent.canceled``checkout_session_read`,`setup_intent_read``setup_intent.created``checkout_session_read`,`setup_intent_read``setup_intent.requires_action``checkout_session_read`,`setup_intent_read``setup_intent.setup_failed``checkout_session_read`,`setup_intent_read``setup_intent.succeeded``checkout_session_read`,`setup_intent_read``sigma.scheduled_query_run.created``subscription_schedule.aborted``quote_read`,`subscription_read``subscription_schedule.canceled``quote_read`,`subscription_read``subscription_schedule.completed``quote_read`,`subscription_read``subscription_schedule.created``quote_read`,`subscription_read``subscription_schedule.expiring``quote_read`,`subscription_read``subscription_schedule.released``quote_read`,`subscription_read``subscription_schedule.updated``quote_read`,`subscription_read``tax_rate.created``tax_rate_read``tax_rate.updated``tax_rate_read``tax.settings.updated``tax_settings_read``terminal.reader.action_failed``terminal_reader_read``terminal.reader.action_succeeded``terminal_reader_read``test_helpers.test_clock.advancing``billing_clock_read`,`customer_read``test_helpers.test_clock.created``billing_clock_read`,`customer_read``test_helpers.test_clock.deleted``billing_clock_read`,`customer_read``test_helpers.test_clock.internal_failure``billing_clock_read`,`customer_read``test_helpers.test_clock.ready``billing_clock_read`,`customer_read``topup.canceled``funding_instruction_read`,`top_up_read``topup.created``funding_instruction_read`,`top_up_read``topup.failed``funding_instruction_read`,`top_up_read``topup.reversed``funding_instruction_read`,`top_up_read``topup.succeeded``funding_instruction_read`,`top_up_read``transfer.created``balance_transaction_source_read`,`transfer_read``transfer.reversed``balance_transaction_source_read`,`transfer_read``transfer.updated``balance_transaction_source_read`,`transfer_read`
## See also

- [App manifest
reference](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)

## Links

- [invalid request
error](https://docs.stripe.com/error-handling#invalid-request-errors)
- [API object](https://docs.stripe.com/api)
- [expanding objects](https://docs.stripe.com/expand)
- [Accounts](https://docs.stripe.com/api/accounts)
- [Account Links](https://docs.stripe.com/api/account_links)
- [domain
registration](https://docs.stripe.com/payments/payment-methods/pmd-registration)
- [Application Fees](https://docs.stripe.com/api/application_fees)
- [Balance](https://docs.stripe.com/api/balance)
- [Balance Transactions](https://docs.stripe.com/api/balance_transactions)
- [Test clocks](https://docs.stripe.com/billing/testing/test-clocks)
- [Billing meters](https://docs.stripe.com/api/billing/meter)
- [Charges](https://docs.stripe.com/api/charges)
- [Sessions](https://docs.stripe.com/api/checkout/sessions)
- [Configurations](https://docs.stripe.com/api/terminal/configuration)
- [Confirmation Tokens](https://docs.stripe.com/api/confirmation_tokens)
- [Connection Tokens](https://docs.stripe.com/api/terminal/connection_tokens)
- [Coupons](https://docs.stripe.com/api/coupons)
- [Credit Notes](https://docs.stripe.com/api/credit_notes)
- [customer portal](https://docs.stripe.com/api/customer_portal)
- [Customers](https://docs.stripe.com/api/customers)
- [Disputes](https://docs.stripe.com/api/disputes)
- [Login Links](https://docs.stripe.com/api/account/login_link)
- [Stripe.js Elements](https://docs.stripe.com/js/elements_object)
- [Entitlements](https://docs.stripe.com/billing/entitlements)
- [Events](https://docs.stripe.com/api/events)
- [Files](https://docs.stripe.com/api/files)
- [Invoices](https://docs.stripe.com/api/invoices)
- [hosted invoice page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Authorizations](https://docs.stripe.com/api/issuing/authorizations)
- [Cards](https://docs.stripe.com/api/issuing/cards)
- [Cardholders](https://docs.stripe.com/api/issuing/cardholders)
- [Issuing Disputes](https://docs.stripe.com/api/issuing/disputes)
- [Transactions](https://docs.stripe.com/api/issuing/transactions)
- [Locations](https://docs.stripe.com/api/terminal/locations)
- [Mandates](https://docs.stripe.com/api/mandates)
- [Orders](https://docs.stripe.com/api/orders_legacy)
- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
- [Payment Links](https://docs.stripe.com/payment-links)
- [PaymentMethods](https://docs.stripe.com/api/payment_methods)
- [Payouts](https://docs.stripe.com/api/payouts)
- [Plans](https://docs.stripe.com/api/plans)
- [Prices](https://docs.stripe.com/api/prices)
- [Products](https://docs.stripe.com/api/products)
- [Promotion Codes](https://docs.stripe.com/api/promotion_codes)
- [Quotes](https://docs.stripe.com/api/quotes)
- [Readers](https://docs.stripe.com/api/terminal/readers)
- [Report Types](https://docs.stripe.com/api/reporting/report_type)
- [Report Runs](https://docs.stripe.com/api/reporting/report_run)
- [Reviews](https://docs.stripe.com/api/radar/reviews)
- [Secrets](https://docs.stripe.com/api/secret_management)
- [SetupIntents](https://docs.stripe.com/api/setup_intents)
- [Shipping Rates](https://docs.stripe.com/api/shipping_rates)
- [SKUs](https://docs.stripe.com/api/skus)
- [Sources](https://docs.stripe.com/api/sources)
- [Subscriptions](https://docs.stripe.com/api/subscriptions)
- [Tax Rates](https://docs.stripe.com/api/tax_rates)
- [Tax Settings](https://docs.stripe.com/api/tax/settings)
- [Tax Calculations and
Transactions](https://docs.stripe.com/api/tax/transactions)
- [Tokens](https://docs.stripe.com/api/tokens)
- [Top-ups](https://docs.stripe.com/api/topups)
- [Transfers](https://docs.stripe.com/api/transfers)
- [Usage Records](https://docs.stripe.com/api/usage_records)
- [Webhook Endpoints](https://docs.stripe.com/api/webhook_endpoints)
- [listen to events](https://docs.stripe.com/stripe-apps/events)
- [Stripe Support](https://support.stripe.com/contact/email)
- [Event](https://docs.stripe.com/api/events/types)
- [App manifest
reference](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)