# Complex pricing rule conditions

## Create pricing rule conditions based on complex data sources.

Most pricing rules are based on simple logical conditions, such as segmenting
pricing by payment method. You can also write rule conditions based on complex
variables, such as your custom metadata values. This guide explains the
additional steps required for these cases.

## Payment Metadata

As a platform, you can add [custom
metadata](https://docs.stripe.com/api/metadata) to payments and reference it in
your pricing rules. First, add a metadata key-value pair to your
[PaymentIntent](https://docs.stripe.com/api/payment_intents) or
[Charge](https://docs.stripe.com/api/charges). Then, create pricing rules
referencing this metadata value.

Pricing rule conditions based on payment metadata observe the following
behavior:

- Pricing rule conditions can evaluate metadata defined in both PaymentIntents
and Charges.
- A rule condition can only evaluate one key-value pair from the metadata
parameter.
- If you include multiple metadata key-value conditions, the pricing tool only
evaluates the first key-value condition.
- The pricing tool only evaluates metadata that’s available before payment is
captured. Make sure you apply any updates before this point for accurate fee
calculation.
- Use the API to update metadata in the
[PaymentIntent](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-metadata)
or [Charge](https://docs.stripe.com/api/charges/update#update_charge-metadata).
The pricing tool can’t evaluate updates made through the Dashboard.

## See also

[Complete list of supported pricing rule
conditions](https://docs.stripe.com/connect/platform-pricing-tools/pricing-schemes#supported-rule-conditions-by-payment-type)

## Links

- [custom metadata](https://docs.stripe.com/api/metadata)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [Charge](https://docs.stripe.com/api/charges)
-
[PaymentIntent](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-metadata)
- [Charge](https://docs.stripe.com/api/charges/update#update_charge-metadata)
- [Complete list of supported pricing rule
conditions](https://docs.stripe.com/connect/platform-pricing-tools/pricing-schemes#supported-rule-conditions-by-payment-type)