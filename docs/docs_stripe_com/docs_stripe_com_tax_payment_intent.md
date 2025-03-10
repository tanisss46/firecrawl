# Calculate tax in your custom payment flowsPrivate preview

## Learn how to integrate taxes with the Stripe Tax and Payment Intents APIs.

The Stripe Tax API enables you to calculate tax in your custom payment flows. If
you use the Payment Intents API, Stripe can submit tax transactions in the
payment lifecycle.

Client

Server

Stripe

Calculate tax with API

Total amount and tax breakdown

Adjust total amount and display tax information

Submit payment

Submit payment with Tax Calculation

Record Tax Transaction

Request a refund

Request a refund

Record a Tax Reversal

Report for filing taxes with all recorded transactions and refunds

A diagram providing a high level overview of the tax api integration outlined in
this doc
#### Private preview

This feature is currently in Private preview. Users without preview access can
use the [Tax API](https://docs.stripe.com/tax/custom) to integrate Stripe Tax
with payment intents.

[Calculate tax](https://docs.stripe.com/tax/payment_intent#calculate-tax)
You can integrate the [Tax API](https://docs.stripe.com/tax/custom) with a
PaymentIntent by associating it with a Tax `Calculation` object. Use [calculate
tax](https://docs.stripe.com/api/tax/calculations/create) to get a new Tax
`Calculation` object with information about how much tax to collect.

```
curl https://api.stripe.com/v1/tax/calculations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d currency=usd \
 -d "line_items[0][amount]"=1000 \
 -d "line_items[0][reference]"=L1 \
 -d "line_items[0][tax_code]"=txcd_99999999 \
 -d "customer_details[address][line1]"="920 5th Ave" \
 -d "customer_details[address][city]"=Seattle \
 -d "customer_details[address][state]"=WA \
 -d "customer_details[address][postal_code]"=98104 \
 -d "customer_details[address][country]"=US \
 -d "customer_details[address_source]"=shipping
```

[Link tax calculation to the
PaymentIntent](https://docs.stripe.com/tax/payment_intent#link-calculation-to-payment)
#### Private preview

This feature is currently in Private preview. Users without preview access can
use the [Tax API](https://docs.stripe.com/tax/custom) to integrate Stripe Tax
with payment intents.

When [creating or modifying a
PaymentIntent](https://docs.stripe.com/payments/quickstart), include the Tax
`Calculation` ID and set the `amount` to the `amount_total` of the Tax
[Calculation](https://docs.stripe.com/api/tax/calculations/object) object.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; payment_intent_with_tax_api_beta=v1;" \
 -d amount=1000 \
 -d currency=usd \
 -d "automatic_payment_methods[enabled]"=true \
 -d "async_workflows[inputs][tax][calculation]"={{CALCULATION_ID}}
```

### Supported endpoints

The following endpoints support setting a calculation on a PaymentIntent.

- Create:
[/v1/payment_intents](https://docs.stripe.com/api/payment_intents/create)
- Update:
[/v1/payment_intents/:id](https://docs.stripe.com/api/payment_intents/update)
- Confirm:
[/v1/payment_intents/:id/confirm](https://docs.stripe.com/api/payment_intents/confirm)
- Capture:
[/v1/payment_intents/:id/capture](https://docs.stripe.com/api/payment_intents/capture)

### Limitations

- You can only link new calculations to a PaymentIntent until it transitions to
a `succeeded` state.
- A tax calculation can transition to only one tax `Transaction`. If multiple
PaymentIntents transition to a `succeeded` state with the same linked
calculation, accounting reflects only the first one.

## Resulting Stripe actions

If the PaymentIntent is correctly linked to the Tax `Calculation` object, Stripe
automatically:

- Creates a tax transaction from the calculation after the PaymentIntent
transitions to a `succeeded` state
- Performs a tax reversal of a tax transaction for any refunds (created with API
or Dashboard) for the PaymentIntent
- Creates a tax reversal for a reversal, if a refund has failed
- Includes the total tax information in `PaymentIntent` receipts

Stripe won’t:

- Change the PaymentIntent amount based on the linked tax calculation
- Alter the tax transaction amount based on the PaymentIntent captured amount
- Automatically create a tax reversal for disputes

## Integrate taxes for your Connect platform with the Stripe Tax and Payment Intents APIs

The Payment Intents API works with connected accounts on your Connect platform.
This means that if you calculate tax using a connected account, you can link the
tax calculation to a Payment Intent created using that connected account.

[OptionalRetrieve automatically committed tax
transactions](https://docs.stripe.com/tax/payment_intent#get-transaction-attempts)
## See also

- [Tax API for Sales Tax, GST, and VAT](https://docs.stripe.com/tax/custom)
- [Custom payment flow guide](https://docs.stripe.com/payments/quickstart)
- [Reporting and filing](https://docs.stripe.com/tax/reports)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)

## Links

- [Tax API](https://docs.stripe.com/tax/custom)
- [calculate tax](https://docs.stripe.com/api/tax/calculations/create)
- [creating or modifying a
PaymentIntent](https://docs.stripe.com/payments/quickstart)
- [Calculation](https://docs.stripe.com/api/tax/calculations/object)
- [/v1/payment_intents](https://docs.stripe.com/api/payment_intents/create)
- [/v1/payment_intents/:id](https://docs.stripe.com/api/payment_intents/update)
-
[/v1/payment_intents/:id/confirm](https://docs.stripe.com/api/payment_intents/confirm)
-
[/v1/payment_intents/:id/capture](https://docs.stripe.com/api/payment_intents/capture)
- [Reporting and filing](https://docs.stripe.com/tax/reports)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)