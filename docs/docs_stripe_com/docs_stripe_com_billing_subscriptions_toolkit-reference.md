# Toolkit CSV reference

## Follow best practices to successfully migrate your subscriptions using the no-code Billing migration toolkit.

Use this guide to help you specify your CSV file in the Billing migration
toolkit. In the following examples, all timestamps are in Unix EPOCH format. We
also provide test customer and price IDs that you can use while in test mode.

## CSV prerequisites

Before you create or download a CSV file, make sure you know the following:

Customer objectAll customers must have a default [payment method attached to
them](https://docs.stripe.com/api/payment_methods/attach). Without a default
payment method, future subscription payments will fail. If you don’t have a
default payment method set for your customers after migrating their data, you
have two options:- Obtain the user’s consent or rely on their past payment
behavior to determine the default payment method on a per-customer basis.
- Use this [provided
script](https://gist.github.com/bsears90/c3f36bfe379dfd13cae749824c5b45ae) to
attach the latest payment method to your customers and make it the default
method.
Automatic taxIf you use Stripe Tax (where you set automatic tax to true), all
customers must have either [addresses or postal
codes](https://docs.stripe.com/tax/customer-locations) (or †both) per country.
Stripe needs this information to calculate taxes for the given
subscriptions.[collection_method](https://docs.stripe.com/api/subscriptions/create#create_subscription-collection_method)If
you’re using the `send_invoice` payment method for your subscriptions:- Add
email addresses to the required customers.
- Add the
[days_until_due](https://docs.stripe.com/api/subscriptions/create#create_subscription-days_until_due)
parameter in the migration CSV file to state the validity of
[invoices](https://docs.stripe.com/api/invoices) for each customer.
Dates- To ensure accurate timing, pay special attention to timezones when you
create epoch date-time formats for your migration CSV file.
- For the toolkit, set the
[start_date](https://docs.stripe.com/api/subscriptions/object#subscription_object-start_date)
with a buffer of at least 24 hours in advance from the CSV upload time. We
create a [subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
so that you get this buffer time to confirm and verify accuracy. When the start
date begins, the subscription changes from scheduled start to live state.
Coupons- If the subscription schedule or subscription has [billing cycle
anchor](https://docs.stripe.com/billing/subscriptions/billing-cycle) in the
future and `proration_behavior` [set
to](https://docs.stripe.com/billing/subscriptions/prorations#disable-prorations)`none`,
updating these objects unsets the coupon. Re-apply the coupon if you make any
updates to the subscription schedule or subscription.
- To migrate a subscription with ongoing `discount_behavior`:- Set a future
phase that removes the coupon at the correct date instead of waiting for an
expiration.
- Create a coupon for each subscription, with the duration being different on
each one so they all expire correctly.
Stripe to Stripe migrationUsers can migrate subscriptions within Stripe
accounts. You must input Customer IDs and Price IDs (and both Coupon IDs and Tax
IDs, if using them) into the template associated with your destination Stripe
account, and not your source Stripe account. The migration tool generates an
error if you input IDs associated with your source account.
## Migration use-cases

You can apply the following migration use cases to your own migration, if
applicable:

- [Migrate subscriptions with various pricing
models](https://docs.stripe.com/billing/subscriptions/toolkit-reference#various-pricing)
- [Migrate subscriptions with different types of payment collection
methods](https://docs.stripe.com/billing/subscriptions/toolkit-reference#payment-collection)
- [Migrate subscriptions at different stages of the subscription
cycle](https://docs.stripe.com/billing/subscriptions/toolkit-reference#subscription-stage)
- [Migrate subscriptions with
taxes](https://docs.stripe.com/billing/subscriptions/toolkit-reference#subscription-taxes)
- [Migrate subscriptions with
discounts](https://docs.stripe.com/billing/subscriptions/toolkit-reference#subscription-discounts)
- [Migrate subscriptions within Stripe
accounts](https://docs.stripe.com/billing/subscriptions/toolkit-reference#within-Stripe-accounts)
- [Migrate subscriptions with multiple
phases](https://docs.stripe.com/billing/subscriptions/toolkit-reference#multiple-phases)

You can combine any Stripe-provided CSV template
([Basic](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#basic),
[Multi-price
items](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#multi-price),
[Ad-hoc
pricing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#ad-hoc))
with any of the examples below as needed.

### Migrate subscriptions with various pricing models

You can migrate subscriptions with flat-rate pricing, such as a basic plan at
100 USD per month or an advanced plan at 200 USD per month. These subscriptions
can have one or more line items.

**Example 1 (Basic)**: Migrate a basic 100 USD monthly subscription with a
quantity of 2, starting on January 1, 2024. The subscription is charged
automatically using the default payment method.

ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx12subscription_1nonecharge_automatically
**Example 2 (Multi-price items)**: Migrate the following subscriptions starting
on January 1, 2024, to be charged automatically using the default payment
method:

- A basic 100 USD monthly subscription with a quantity of 2
- An advanced 200 USD monthly subscription with a quantity of 1
ATTRIBUTEcustomer (required)start_date (required)items.0.price
(required)items.0.quantityitems.1.priceitems.1.quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx11price_xxx2subscription_1nonecharge_automatically
**Example 3 (Basic)**: Migrate the following subscription starting on January 1,
2024, to be charged automatically using the default payment method:

- A basic 100 USD monthly subscription with a quantity of 2
- An ad-hoc invoice add-on fee of 20 USD
ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx12subscription_1nonecharge_automatically50prod_xxx1usd
You can also migrate subscriptions with ad-hoc pricing, in cases where you don’t
have fixed pricing amounts.

**Example 4 (Ad-hoc pricing)**: Migrate the following subscription starting on
January 1, 2024, to be charged automatically using the default payment method:

- A 153 USD ad-hoc monthly subscription with a quantity of 1
ATTRIBUTEcustomer (required)start_date (required)adhoc_items.0.amount
(required)adhoc_items.0.productadhoc_items.0.intervaladhoc_items.0.currencyadhoc_items.0.quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx1prod_xxx11subscription_1nonecharge_automatically
### Migrate subscriptions with different types of payment collection methods

You can collect payment for the migrated subscriptions either automatically with
the default saved payment method or by sending an invoice that the customer can
pay by the due date.

**Example 1 (Basic)**: Migrate a yearly 500 USD subscription with a quantity of
1, starting on January 1, 2024, to be charged automatically using the default
payment method.

ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx11subscription_1nonecharge_automatically
**Example 2 (Basic)**: Migrate a yearly 500 USD subscription with a quantity of
1, starting on January 1, 2024. This subscription is billed using an invoice
sent to the customer, with a 30-day due date.

ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx11subscription_1nonesend_invoice30
### Migrate subscriptions at different stages of subscription cycle

**Example 1 (Basic): Migrate a subscription that’s due for renewal**. For
example, migrate a 100 USD monthly subscription with a renewal date of January
1, 2024. The subscription renews on the 1st of every month.

- Set the `start_date` to the current renewal date, so the subscription is
charged immediately.
- Set the `billing_cycle_anchor` to the next renewal cycle date.
- Set `proration_behavior` to `none`.
ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx1subscription_11706745600nonecharge_automatically
**Example 2 (Basic): Migrate a paid subscription that’s in the middle of a
billing cycle**. For example, migrate a 100 USD monthly subscription with an
original start date of December 25. The migration date is January 1, and the
subscription renews on the 25th of every month.

- Set `backdate_start_date` to the original start date of the subscription.
- Set `billing_cycle_anchor` to the upcoming renewal date.
- Set `start_date` to the migration date.
- Set `proration_behavior` to `none` to avoid charging the customer again and
keep the subscription in a scheduled state until the next billing cycle.
ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx1subscription_11706140800nonecharge_automatically1703462400
**Example 3 (Basic): Migrate subscriptions with trials**. For example, migrate a
basic 100 USD monthly subscription starting on January 1, 2024. The subscription
is under a trial until January 31, 2024. After the trial ends, the subscription
is charged automatically using the default payment method.

ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx11subscription_11706659200nonecharge_automatically1703462400
**Example 4 (Basic): Migrate past-due subscriptions**. For example, migrate a
100 USD monthly subscription with a last cycle start date of December 25, which
hasn’t been paid. Migrate this mid-cycle starting January 1, with a renewal date
on the 25th of each month. This creates a prorated invoice from January 1 to
January 25 that Stripe can attempt to collect payment for.

To migrate subscriptions that are in an active cycle but haven’t been paid in
the previous system, set `proration_behavior` to `create_prorations` to
immediately create an invoice and collect payment. This also enters the
subscription into Stripe’s dunning flow, if the payment is still unpaid.

ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx11subscription_11706140800create_prorationscharge_automatically1703462400
**Example 5: Migrate subscriptions that need to be canceled at the end of the
cycle**. After migration, you can choose whether or not to charge these
subscriptions, based on the migration timing (mid-cycle or at renewal).

They’re canceled at the end of that period. For example, migrate a basic 100 USD
monthly subscription starting on January 1, 2024. This subscription is
automatically canceled on January 31, 2024.

ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx11subscription_11706140800nonecharge_automatically1703462400TRUE
### Migrate subscriptions with taxes

**Example 1 (Basic)**: Migrate subscriptions to automatically calculate tax by
enabling Stripe Tax. For example, migrate a 100 USD monthly subscription
starting January 1, 2024, with Stripe Tax enabled to calculate the tax
automatically.

The migration toolkit validates if you enabled Stripe Tax in advance, and if
customers provided the required fields to calculate tax automatically. Make sure
your customers provide the necessary information before migration.

ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx11subscription_1TRUEnonecharge_automatically
**Example 2 (Basic)**: Migrate subscriptions and calculate tax using [manual tax
rates](https://dashboard.stripe.com/test/tax-rates). For example, to migrate a
basic $100 monthly subscription starting on January 1, 2024, with 10% tax
created using manual tax rates:

- Create a 10% manual tax rate in the
[Dashboard](https://dashboard.stripe.com/test/tax-rates) (**Product catalog** >
**Coupons**).
- Use the tax rate ID in the migration CSV template.
ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxx11704067200price_xxx11subscription_1FALSE1706140800nonecharge_automaticallytxr_xxx1
**Example 3 (Basic)**: If you use an external tax provider, such as Avalara or
Vertex:

For migrated subscriptions where tax is already calculated, leave both
`automatic_tax` and `default_tax_rate` blank in the CSV.

After the subscriptions are migrated and live, they automatically follow the tax
integration workflows you set up for new subscriptions in your Billing
integration.

### Migrate subscriptions with discounts

Currently, the migration toolkit supports only one coupon per subscription.

**Example 1 (Basic)**: You can migrate subscriptions with discounts that are
applied after migration. For example, to migrate a $100 monthly subscription
starting January 1, 2024, with a 10% forever discount:

- Create a 10% coupon in the
[Dashboard](https://dashboard.stripe.com/test/tax-rates) (**Product catalog** >
**Coupons**).
- Use the coupon name in the migration CSV file.
ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.third_party_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endadd_invoice_items.0.amountadd_invoice_items.0.productadd_invoice_items.0.currencyFIELDcus_xxxx11704067200price_xxx11subscription_1sample_couponnonecharge_automatically
### Migrate subscriptions within Stripe accounts

The steps to migrate subscriptions from one Stripe account to another are the
same as when migrating from a third-party system. Use the [Billing migration
toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)
to migrate subscriptions. You’ll need to export the subscription data for your
CSV file from your old Stripe account.

**Example 1 (Basic)**: To create a migration CSV for a Stripe-to-Stripe
migration:

- Export the subscriptions from the old Stripe account using the Dashboard.
- Use the following CSV example as a reference to map fields between the old and
new Stripe accounts.
ATTRIBUTEcustomer (required)start_date (required)price
(required)quantitymetadata.old_Stripe_sub_idautomatic_taxbilling_cycle_anchorcoupontrial_endproration_behaviorcollection_methoddefault_tax_ratebackdate_start_datedays_until_duecancel_at_period_endFIELDExport
field: Customer ID (from previous account export)Export field: Current Period
End UTC (from previous account export)Respective price id in the new
accountExport field: Quantity (from previous account export)Export field: id
(from previous account export)TRUE if using Stripe tax in new account, else
FALSEFuture billing date in new accountRespective coupon in the new account, if
anyRespective trial in the new account, if any`create_prorations` in case of
prorated invoice, else `none``charge_automatically` or `send_invoice`Respective
tax rate in the new account, if anyExport field: Start Date UTC (from previous
account export)Specify if using `send_invoice` as collection methodSpecify if a
subscription is due to be canceled at period end
### Migrate subscriptions with multiple phases

The migration toolkit doesn’t support adding multiple phases directly to a
subscription. We recommend the following approach:

- Use the migration toolkit to migrate the initial phase of the subscription.
- After the migration, add the additional phases to the migrated subscription
schedules. To do so, call the
[update](https://docs.stripe.com/api/subscription_schedules/update) endpoint or
use the Stripe [Subscriptions](https://dashboard.stripe.com/test/subscriptions)
Dashboard.
- Adjust the `start_date` of the migration to allow enough time between the
scheduled and live status changes. This allows you to make the phase updates
before the subscriptions go live.

## Full CSV specification

AttributeTypeDescription`customer` (required)Stripe Customer IDThe identifier of
the customer to create the subscription for.`start_date` (required)Timestamp in
epoch UNIX formatDetermines when to create the subscription. You must provide a
value that’s 24 hours (or greater) into the future. In test mode, you can set
this to 1 hour in the future.`price` (required)Stripe Price IDMust be a
recurring price. If migrating multiple items, use `items.x.{price, quantity}`
format instead. Ad-hoc prices are also supported with `adhoc_items.x.{amount,
interval, product, currency}`.`quantity`NumberDetermines quantity of a
subscription. By default, each subscription is for one product, but Stripe
allows you to subscribe a customer to multiple quantities of an
item.`items.x.price` (required)Stripe Price IDThe ID of the price object. Must
be a recurring price.`items.x.quantity`NumberDetermines quantity of a
subscription. By default, each subscription is for one product, but Stripe
allows you to subscribe a customer to multiple quantities of an
item.`adhoc_items.x.amount` (required)IntegerA positive integer in cents (or 0
for a free price). For more information, see [Create a
subscription](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data).`adhoc_items.x.product`
(required)Stripe Product IDThe identifier of the product that belongs with the
ad-hoc price.`adhoc_items.x.interval` (required)`day`, `week`, `month` or
`year`The billing frequency.`adhoc_items.x.currency` (required)StringA
three-letter ISO currency code, in lowercase, for a [supported
currency](https://docs.stripe.com/currencies).`adhoc_items.x.quantity`NumberDetermines
quantity of a subscription. By default, each subscription is for one product,
but Stripe allows you to subscribe a customer to multiple quantities of an
item.`metadata_source`StringIf you’re doing a Stripe-to-Stripe migration, enter
`internal:Stripe`.`metadata_*`StringAttach these key-value pairs to an object.
This is useful for storing additional information about the object in a
structured format.`automatic_tax`BooleanSpecify `true` to use automatic tax
settings by Stripe Tax.`coupon`Stripe Coupon IDThe identifier of the coupon to
apply to this subscription.`currency`StringThree-letter [ISO currency
code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a
[supported currency](https://docs.stripe.com/currencies). Used for currency
selection with multi-currency prices.`trial_end`TimestampSets the phase to
trialing from the start date to the `trial_end` date. You must specify a value
that’s before the cycle/phase end date, and you can’t combine it with the
trial.`proration_behavior``create_prorations` or `none`Determines if the
subscription creates prorations after migration. The default value is
`create_prorations`.`collection_method``charge_automatically` or
`send_invoice`When charging automatically, Stripe attempts to pay the underlying
subscription at the end of each billing cycle using the default source attached
to the customer. The default value is `charge_automatically`. When sending an
invoice, Stripe emails your customer an invoice with payment instructions, and
marks the subscription as active. If using `send_invoice`, you must set
`days_until_due`.`default_tax_rate`Stripe Tax IDSets the subscription’s
`default_tax_rates`. This also determines the invoice’s `default_tax_rates` for
any invoices issued by the subscription during this phase. This value is
incompatible with `automatic_tax`.`backdate_start_date`Timestamp in epoch UNIX
formatDetermines the `start_date` of the created subscription, which must occur
in the past. If set, you must specify `none` for the `proration_behavior`. Doing
so prevents the creation of a prorated invoice for the time between
`backdate_start_date` and actual `start_date`. For more details, see [backdating
no
charge](https://docs.stripe.com/billing/subscriptions/backdating#backdating-no-charge).`billing_cycle_anchor`TimestampDetermines
the future dates of when to bill the subscription to the
customer.`days_until_due`IntegerThe number of days from when the invoice is
created until it’s due. This is required and valid only for invoices with
`collection_method` set to `send_invoice`.`cancel_at_period_end`BooleanSpecify
`true` to cancel a subscription at the end of the period.
## See also

- [Import subscriptions with
toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)

## Links

- [payment method attached to
them](https://docs.stripe.com/api/payment_methods/attach)
- [provided
script](https://gist.github.com/bsears90/c3f36bfe379dfd13cae749824c5b45ae)
- [addresses or postal codes](https://docs.stripe.com/tax/customer-locations)
-
[collection_method](https://docs.stripe.com/api/subscriptions/create#create_subscription-collection_method)
-
[days_until_due](https://docs.stripe.com/api/subscriptions/create#create_subscription-days_until_due)
- [invoices](https://docs.stripe.com/api/invoices)
-
[start_date](https://docs.stripe.com/api/subscriptions/object#subscription_object-start_date)
- [subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
- [billing cycle
anchor](https://docs.stripe.com/billing/subscriptions/billing-cycle)
- [set
to](https://docs.stripe.com/billing/subscriptions/prorations#disable-prorations)
- [Migrate subscriptions with various pricing
models](https://docs.stripe.com/billing/subscriptions/toolkit-reference#various-pricing)
- [Migrate subscriptions with different types of payment collection
methods](https://docs.stripe.com/billing/subscriptions/toolkit-reference#payment-collection)
- [Migrate subscriptions at different stages of the subscription
cycle](https://docs.stripe.com/billing/subscriptions/toolkit-reference#subscription-stage)
- [Migrate subscriptions with
taxes](https://docs.stripe.com/billing/subscriptions/toolkit-reference#subscription-taxes)
- [Migrate subscriptions with
discounts](https://docs.stripe.com/billing/subscriptions/toolkit-reference#subscription-discounts)
- [Migrate subscriptions within Stripe
accounts](https://docs.stripe.com/billing/subscriptions/toolkit-reference#within-Stripe-accounts)
- [Migrate subscriptions with multiple
phases](https://docs.stripe.com/billing/subscriptions/toolkit-reference#multiple-phases)
-
[Basic](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#basic)
- [Multi-price
items](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#multi-price)
- [Ad-hoc
pricing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#ad-hoc)
- [manual tax rates](https://dashboard.stripe.com/test/tax-rates)
- [Billing migration
toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)
- [update](https://docs.stripe.com/api/subscription_schedules/update)
- [Subscriptions](https://dashboard.stripe.com/test/subscriptions)
- [Create a
subscription](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data)
- [supported currency](https://docs.stripe.com/currencies)
- [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)
- [backdating no
charge](https://docs.stripe.com/billing/subscriptions/backdating#backdating-no-charge)