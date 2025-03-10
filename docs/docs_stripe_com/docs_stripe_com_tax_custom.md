# Tax API for Sales Tax, GST, and VAT

## Use Stripe Tax APIs to implement tax calculations in your custom integration.

#### Note

This guide describes how to integrate Stripe Tax with a custom payment flow,
such as [PaymentIntents](https://docs.stripe.com/api/payment_intents). You can
also integrate Stripe Tax with [Payment
Links](https://docs.stripe.com/tax/payment-links),
[Checkout](https://docs.stripe.com/tax/checkout),
[Billing](https://docs.stripe.com/tax/subscriptions) and
[Invoicing](https://docs.stripe.com/tax/invoicing) with no or low code setups.

Stripe Tax APIs enable you to calculate tax in custom payment flows. After your
customer completes their payment, record the transaction so it appears in Stripe
Tax reporting. The examples in this guide use Stripe payments APIs, but you can
use the Tax API with any payment processor, or multiple payment processors.

Client

Server

Stripe

Preview order summary

Calculate tax with API

Total amount and tax breakdown

Adjust total amount and display tax information

Submit payment

Record transaction with API

Request a refund

Record a partial or full refund with API

Report for filing taxes with all recorded transactions and refunds

A diagram providing a high level overview of the tax api integration outlined in
this doc
## Get started with a video demo

This short video walks through a Stripe Tax API integration that uses
PaymentIntents and the Payment Element.

[Add registrations](https://docs.stripe.com/tax/custom#add-registrations)
Stripe Tax only calculates tax in jurisdictions where you’re registered to
collect tax and requires you to [add your
registrations](https://docs.stripe.com/tax/registering#add-a-registration) in
the Dashboard.

[OptionalCollect customer
addressClient-side](https://docs.stripe.com/tax/custom#collect-address)[Calculate
taxServer-side](https://docs.stripe.com/tax/custom#calculate-tax)
You choose when and how often to [calculate
tax](https://docs.stripe.com/api/tax/calculations/create). For example, you can:

- Show a tax estimate [based on your customer’s IP
address](https://docs.stripe.com/tax/custom#ip-address) when they enter your
checkout flow
- Recalculate tax as your customer types their billing or shipping address
- Calculate the final tax amount to collect when your customer finishes typing
their address

Stripe [charges a fee](https://stripe.com/tax/pricing) per tax calculation API
call. You can throttle tax calculation API calls to manage your costs.

The examples below show how to calculate tax in a variety of scenarios. Stripe
Tax only calculates tax in jurisdictions where you’re registered to collect tax
and requires you to [add your
registrations](https://docs.stripe.com/tax/registering#add-a-registration) in
the Dashboard.

Example:United States: tax-exclusive itemUnited States: multiple items with
shippingUnited States: item with quantityEurope: tax-inclusive itemEurope:
multiple items with shippingShip-from address
This example calculates tax for a US shipping address. The line item has a price
of 10 USD and uses your account’s [preset tax
code](https://docs.stripe.com/tax/set-up#preset-tax-code).

```
curl https://api.stripe.com/v1/tax/calculations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d currency=usd \
 -d "line_items[0][amount]"=1000 \
 -d "line_items[0][reference]"=L1 \
 -d "customer_details[address][line1]"="920 5th Ave" \
 -d "customer_details[address][city]"=Seattle \
 -d "customer_details[address][state]"=WA \
 -d "customer_details[address][postal_code]"=98104 \
 -d "customer_details[address][country]"=US \
 -d "customer_details[address_source]"=shipping
```

The [calculation response](https://docs.stripe.com/api/tax/calculations/object)
contains amounts you can display to your customer, and use to take payment:

AttributeDescription[amount_total](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-amount_total)The
grand total after calculating tax. Use this to set the PaymentIntent
[amount](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-amount)
to charge your
customer.[tax_amount_exclusive](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-tax_amount_exclusive)The
amount of tax added on top of your line item amounts and shipping cost. This tax
amount increases the `amount_total`. Use this to show your customer the amount
of tax added to the transaction
subtotal.[tax_amount_inclusive](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-tax_amount_inclusive)The
amount of tax that’s included in your line item amounts and shipping cost (if
using tax-inclusive pricing). This tax amount does not increase the
`amount_total`. Use this to show your customer the tax included in the total
they’re
paying.[tax_breakdown](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-tax_breakdown)A
list of tax amounts broken out by country or state tax rate. Use this to show
your customer the specific taxes you’re collecting.
### Handling customer location errors

The calculation returns the `customer_tax_location_invalid` error code if your
customer’s address is invalid or isn’t precise enough to calculate tax:

```
{
 "error": {
"doc_url": "https://docs.stripe.com/error-codes#customer-tax-location-invalid",
 "code": "customer_tax_location_invalid",
"message": "We could not determine the customer's tax location based on the
provided customer address.",
 "param": "customer_details[address]",
 "type": "invalid_request_error"
 }
}
```

When you receive this error, prompt your customer to check the address they’ve
entered and fix any typos.

[Create tax
transactionServer-side](https://docs.stripe.com/tax/custom#tax-transaction)
Creating a tax transaction records the tax you’ve collected from your customer,
so that later you can [download exports and generate
reports](https://docs.stripe.com/tax/reports) to help with filing your taxes.
You can [create a
transaction](https://docs.stripe.com/api/tax/transactions/create_from_calculation)
from a calculation until the
[expires_at](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-expires_at)
timestamp, 90 days after it’s created. Attempting to use it after this time
returns an error.

#### Note

The transaction is considered effective on the date when create_from_calculation
is called, and tax amounts won’t be recalculated.

When creating a tax transaction, you must provide a unique `reference` for the
tax transaction and each line item. The references appear in tax exports to help
you reconcile the tax you collected with the orders in your system.

For example, a tax transaction with reference `pi_123456789`, line item
references `L1` and `L2`, and a shipping cost, looks like this in the itemized
tax exports:

IDline_item_idtypecurrencytransaction_date…pi_123456789L1externalusd2023-02-23
17:01:16…pi_123456789L2externalusd2023-02-23
17:01:16…pi_123456789shippingexternalusd2023-02-23 17:01:16…
When your customer pays, use the calculation ID to record the tax collected. Two
ways to do this are:

- If your server has an endpoint where your customer submits their order, you
can create the tax transaction after the order is successfully submitted.
- Listen for the
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
webhook event. Retrieve the calculation ID from the PaymentIntent `metadata`.

The example below creates a transaction and uses the PaymentIntent ID as the
unique reference:

```
curl https://api.stripe.com/v1/tax/transactions/create_from_calculation \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d calculation={{TAX_CALCULATION}} \
 -d reference={{PAYMENT_INTENT_ID}} \
 -d "expand[]"=line_items
```

Store the [tax transaction
ID](https://docs.stripe.com/api/tax/transactions/object#tax_transaction_object-id)
so that later you can record refunds. You can store the transaction ID in your
database or in the PaymentIntent’s metadata:

```
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "metadata[tax_transaction]"={{TAX_TRANSACTION}}
```

[Record refundsServer-side](https://docs.stripe.com/tax/custom#reversals)
After creating a tax transaction to record a sale to your customer, you might
need to record refunds. These are also represented as tax transactions, with
`type=reversal`. Reversal transactions offset an earlier transaction by having
amounts with opposite signs. For example, a transaction that recorded a sale for
50 USD might later have a full reversal of -50 USD.

When you issue a refund (using Stripe or outside of Stripe) you need to create a
reversal tax transaction with a unique `reference`. Common strategies include:

- Append a suffix to the original reference. For example, if the original
transaction has reference `pi_123456789`, then create the reversal transaction
with reference `pi_123456789-refund`.
- Use the ID of the [Stripe refund](https://docs.stripe.com/api/refunds/object)
or a refund ID from your system. For example, `re_3MoslRBUZ691iUZ41bsYVkOg` or
`myRefund_456`.

Choose the approach that works best for how you reconcile your customer orders
with your [tax exports](https://docs.stripe.com/tax/reports).

### Fully refund a sale

When you fully refund a sale in your system, create a reversal transaction with
`mode=full`.

In the example below, `tax_1MEFAAI6rIcR421eB1YOzACZ` is the tax transaction
recording the sale to your customer:

```
curl https://api.stripe.com/v1/tax/transactions/create_reversal \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=full \
 -d original_transaction=tax_1MEFAAI6rIcR421eB1YOzACZ \
 -d reference=pi_123456789-cancel \
 -d "expand[]"=line_items
```

This returns the full reversal transaction that’s created:

```
{
 "id": "tax_1MEFtXI6rIcR421e0KTGXvCK",
 "object": "tax.transaction",
 "created": 1670866467,
 "currency": "eur",
 "customer": null,
 "customer_details": {
 "address": {
 "city": null,
 "country": "IE",
```

See all 73 lines
Fully reversing a transaction doesn’t affect previous partial reversals. When
you record a full reversal, make sure you [fully
reverse](https://docs.stripe.com/tax/custom#reversals-void-refund) any previous
partial reversals for the same transaction to avoid duplicate refunds.

### Partially refund a sale

After [issuing a refund](https://docs.stripe.com/api/refunds/create) to your
customer, create a reversal tax transaction with `mode=partial`. This allows you
to record a partial refund by providing the line item amounts refunded. You can
create up to 30 partial reversals for each sale. Reversing more than the amount
of tax you collected returns an error.

The example below records a refund of only the first line item in the original
transaction:

```
curl https://api.stripe.com/v1/tax/transactions/create_reversal \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=partial \
 -d original_transaction=tax_1MEFAAI6rIcR421eB1YOzACZ \
 -d reference=pi_123456789-refund_1 \
 -d "line_items[0][original_line_item]"=tax_li_MyBXPByrSUwm6r \
 -d "line_items[0][reference]"=L1 \
 -d "line_items[0][amount]"=-4999 \
 -d "line_items[0][amount_tax]"=-1150 \
 -d "metadata[refund]"={{REFUND_ID}} \
--data-urlencode "metadata[refund_reason]"="Refunded line 1 of pi_123456789
(customer was unhappy)" \
 -d "expand[0]"=line_items
```

This returns the partial reversal transaction that’s created:

```
{
 "id": "tax_1MEFACI6rIcR421eHrjXCSmD",
 "object": "tax.transaction",
 "created": 1670863656,
 "currency": "eur",
 ...
 "line_items": {
 "object": "list",
 "data": [
 {
```

See all 44 lines
For each line item reversed you need to provide the `amount` and `amount_tax`
reversed. The `amount` is tax-inclusive if the original calculation line item
was tax-inclusive.

How `amount` and `amount_tax` are determined depends on your situation:

- If your transactions always have a single line item, use [full
reversals](https://docs.stripe.com/tax/custom#reversals-full) instead.
- If you always refund entire line items, use the original transaction line item
`amount` and `amount_tax`, but with negative signs.
- If you refund parts of line items, you need to calculate the amounts refunded.
For example, for a sale transaction with `amount=5000` and `amount_tax=500`,
after refunding half the line item you’d create a partial reversal with line
item `amount=-2500` and `amount_tax=-250`.

### Partially refund a sale by a flat amount

Alternatively, you can create a reversal with `mode=partial` by specifying a
flat after-tax amount to refund. The amount distributes across each line item
and shipping cost proportionally, depending on the remaining amount left to
refund on each.

In the example below, the transaction has two line items: one 10 USD item and
one 20 USD item, both taxed at 10%. The total amount of the transaction is 33.00
USD. A refund for a flat 16.50 USD is recorded:

```
curl https://api.stripe.com/v1/tax/transactions/create_reversal \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=partial \
 -d original_transaction=tax_1NVcKqBUZ691iUZ4xMZtcGYt \
 -d reference=pi_234567890-refund_1 \
 -d flat_amount=-1650 \
 -d "metadata[refund]"={{REFUND_ID}} \
--data-urlencode "metadata[refund_reason]"="Refunded $16.50 of pi_234567890
(customer was unhappy)" \
 -d "expand[]"=line_items
```

This returns the partial reversal transaction that’s created:

```
{
 "id": "tax_1NVcQYBUZ691iUZ4SBPukGa6",
 "object": "tax.transaction",
 "created": 1689780994,
 "currency": "usd",
 ...
 "line_items": {
 "object": "list",
 "data": [
 {
```

See all 61 lines
For each line item and shipping cost in the original transaction, the refunded
amounts and tax are calculated as follows:

- First, we calculate the total remaining funds in the transaction available to
refund. Because this transaction hasn’t had any other reversals recorded, the
total amount is 33.00 USD.
- Next, we calculate the total amount to refund for each line item. We base this
calculation on the proportion of the item’s total available amount to refund
versus the total remaining amount of the transaction. For example, the 10 USD
item, which has 11.00 USD total remaining to refund, represents 33.33% of the
transaction’s remaining total, so the total amount to refund is `-16.50 USD *
33.33% = -5.50 USD`.
- Finally, the total amount to refund is divided between `amount` and
`amount_tax`. We also do this proportionally, depending on how much tax is
available to refund in the line item compared to the total funds left to refund.
Using the 10 USD item example, tax (1.00 USD) represents 9.09% of the total
remaining to refund (11.00 USD), so the `amount_tax` is `-5.50 USD * 9.09% =
-0.50 USD`.

The flat amount distributes according to what’s *left* to refund in the
transaction, not what was originally recorded. Consider this example: instead of
recording a refund for a flat 16.50 USD, you first record a partial reversal for
the total amount of the 10 USD item:

```
curl https://api.stripe.com/v1/tax/transactions/create_reversal \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=partial \
 -d original_transaction=tax_1NVcKqBUZ691iUZ4xMZtcGYt \
 -d reference=pi_234567890-refund_1 \
 -d "line_items[0][original_line_item]"=tax_li_OICmRXkFuWr8Df \
 -d "line_items[0][reference]"=partial_refund_l1 \
 -d "line_items[0][amount]"=-1000 \
 -d "line_items[0][amount_tax]"=-100 \
 -d "metadata[refund]"={{REFUND_ID}} \
--data-urlencode "metadata[refund_reason]"="Refunded line 1 of pi_234567890
(customer was unhappy)" \
 -d "expand[0]"=line_items
```

After this, you record a 16.50 USD flat amount reversal:

```
curl https://api.stripe.com/v1/tax/transactions/create_reversal \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=partial \
 -d original_transaction=tax_1NVcKqBUZ691iUZ4xMZtcGYt \
 -d reference=pi_234567890-refund_2 \
 -d flat_amount=-1650 \
 -d "metadata[refund]"={{REFUND_ID}} \
--data-urlencode "metadata[refund_reason]"="Refunded $16.50 of pi_234567890
(customer was still unhappy)" \
 -d "expand[]"=line_items
```

This returns the partial reversal transaction:

```
{
 "id": "tax_1NVxFIBUZ691iUZ4saOIloxB",
 "object": "tax.transaction",
 "created": 1689861020,
 "currency": "usd",
 ...
 "line_items": {
 "object": "list",
 "data": [
 {
```

See all 58 lines
Because the total amount remaining in the transaction is now 22.00 USD and the
10 USD item is completely refunded, the 16.50 USD distributes entirely to the 20
USD item. The 16.50 USD then distributes, using the logic from step 3, into
`amount = -15.00 USD` and `amount_tax = -1.50 USD`. Meanwhile, the 10 USD item
in the transaction records a refund of 0 USD.

### Undo a partial refund

Tax transactions are immutable but you can cancel out a partial refund by
creating a [full
reversal](https://docs.stripe.com/api/tax/transactions/create_reversal#tax_transaction_create_reversal-mode)
of it.

You might need to do this when:

- The payment [refund fails](https://docs.stripe.com/refunds#failed-refunds) and
you haven’t provided the good or service to your customer
- The wrong order is refunded or the wrong amounts are refunded
- The original sale is fully refunded and the partial refunds are no longer
valid

In the example below, `tax_1MEFACI6rIcR421eHrjXCSmD` is the transaction
representing the partial refund:

```
curl https://api.stripe.com/v1/tax/transactions/create_reversal \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=full \
 -d original_transaction=tax_1MEFACI6rIcR421eHrjXCSmD \
 -d reference=pi_123456789-refund_1-cancel \
-d "metadata[refund_reason]"="User called to cancel because they picked the
wrong item" \
 -d "expand[]"=line_items
```

This returns the full reversal transaction that’s created:

```
{
 "id": "tax_1MEFADI6rIcR421e94fNTOCK",
 "object": "tax.transaction",
 "created": 1670863657,
 "currency": "eur",
 ...
 "line_items": {
 "object": "list",
 "data": [
 {
```

See all 43 lines[Testing](https://docs.stripe.com/tax/custom#testing)
The response structure in [test mode](https://docs.stripe.com/test-mode) is
identical to live mode, so that you can confirm your integration is working
correctly before going live.

#### Warning

We don’t guarantee test mode calculations return up-to-date taxation results.

You are limited to 1,000 test mode tax calculations per day. Contact [Stripe
support](https://support.stripe.com/contact) if you need a higher limit.

[View tax transactions in the
Dashboard](https://docs.stripe.com/tax/custom#view-recorded-transactions)
You can view all tax transactions for your account on the [Tax
Transactions](https://dashboard.stripe.com/test/tax/transactions) page in the
Dashboard. Click an individual transaction to see a detailed breakdown of
calculated tax by jurisdiction, and by the individual products included in the
transaction.

#### Note

This page only includes *transactions* and not *calculations*. If you expect a
calculation to be visible but can’t find it on this page, check that you’ve
successfully [created a tax
transaction](https://docs.stripe.com/tax/custom#tax-transaction) from the
calculation.

[OptionalIntegration
examples](https://docs.stripe.com/tax/custom#integration-examples)[OptionalCalculate
tax on shipping
costsServer-side](https://docs.stripe.com/tax/custom#shipping-costs)[OptionalEstimate
taxes with an IP
addressServer-side](https://docs.stripe.com/tax/custom#ip-address)[OptionalCollect
customer tax
IDsServer-side](https://docs.stripe.com/tax/custom#tax-ids)[OptionalTax-inclusive
pricingServer-side](https://docs.stripe.com/tax/custom#inclusive-pricing)[OptionalUse
an existing Product
objectServer-side](https://docs.stripe.com/tax/custom#existing-product)[OptionalUse
an existing Customer
objectServer-side](https://docs.stripe.com/tax/custom#existing-customer)[OptionalOverride
customer
taxabilityServer-side](https://docs.stripe.com/tax/custom#taxability-override)[OptionalSpecify
a ship-from
locationServer-side](https://docs.stripe.com/tax/custom#ship_from)[OptionalCalculate
the retail delivery
feeServer-side](https://docs.stripe.com/tax/custom#retail_delivery_fee)[OptionalDetailed
line item tax
breakdownsServer-side](https://docs.stripe.com/tax/custom#tax-breakdowns)
## See also

- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)

## Links

- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
- [Payment Links](https://docs.stripe.com/tax/payment-links)
- [Checkout](https://docs.stripe.com/tax/checkout)
- [Billing](https://docs.stripe.com/tax/subscriptions)
- [Invoicing](https://docs.stripe.com/tax/invoicing)
- [add your
registrations](https://docs.stripe.com/tax/registering#add-a-registration)
- [calculate tax](https://docs.stripe.com/api/tax/calculations/create)
- [charges a fee](https://stripe.com/tax/pricing)
- [preset tax code](https://docs.stripe.com/tax/set-up#preset-tax-code)
- [calculation response](https://docs.stripe.com/api/tax/calculations/object)
-
[amount_total](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-amount_total)
-
[amount](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-amount)
-
[tax_amount_exclusive](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-tax_amount_exclusive)
-
[tax_amount_inclusive](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-tax_amount_inclusive)
-
[tax_breakdown](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-tax_breakdown)
-
[https://docs.stripe.com/error-codes#customer-tax-location-invalid](https://docs.stripe.com/error-codes#customer-tax-location-invalid)
- [download exports and generate reports](https://docs.stripe.com/tax/reports)
- [create a
transaction](https://docs.stripe.com/api/tax/transactions/create_from_calculation)
-
[expires_at](https://docs.stripe.com/api/tax/calculations/object#tax_calculation_object-expires_at)
-
[payment_intent.succeeded](https://docs.stripe.com/api/events/types#event_types-payment_intent.succeeded)
- [tax transaction
ID](https://docs.stripe.com/api/tax/transactions/object#tax_transaction_object-id)
- [Stripe refund](https://docs.stripe.com/api/refunds/object)
- [issuing a refund](https://docs.stripe.com/api/refunds/create)
- [full
reversal](https://docs.stripe.com/api/tax/transactions/create_reversal#tax_transaction_create_reversal-mode)
- [refund fails](https://docs.stripe.com/refunds#failed-refunds)
- [test mode](https://docs.stripe.com/test-mode)
- [Stripe support](https://support.stripe.com/contact)
- [Tax Transactions](https://dashboard.stripe.com/test/tax/transactions)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)