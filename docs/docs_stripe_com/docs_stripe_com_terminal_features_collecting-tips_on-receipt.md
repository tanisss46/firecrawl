# Collect on-receipt tips

## Learn how to allow customers to add tips to receipts.

Available in: 
Some business types allow customers to add a tip to a transaction after
authorizing the card. This is most common for businesses in the dining and
hospitality space (for example, a restaurant or bar), where a customer can add a
tip onto the receipt.

In the US, after you confirm a
[PaymentIntent](https://docs.stripe.com/api/payment_intents), you can collect a
tip by capturing more than the authorized amount. This is known as over-capture.
After you capture the PaymentIntent, your customer sees the full captured amount
reflected on their statement.

To collect a tip, you must create and confirm a PaymentIntent following the
steps outlined in [collecting in-person
payments](https://docs.stripe.com/terminal/payments/collect-card-payment). You
can verify that a given PaymentIntent is eligible for over-capture by accessing
[overcapture_supported](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-overcapture_supported).

Next, [capture](https://docs.stripe.com/api/payment_intents/capture) more than
the authorized amount by providing an
[amount_to_capture](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture)
that’s equal to the sum of the confirmed PaymentIntent and tip amount.

```
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount_to_capture=1800
```

Over-capturing updates the PaymentIntent
[amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount)
to reflect the new total, inclusive of the tip. This doesn’t result in an
additional authorization, so your customer won’t see any immediate updates on
their credit card statement. To see the original amount authorized, use the
[amount_authorized](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-amount_authorized)
field in the PaymentIntent’s underlying
[Charge](https://docs.stripe.com/api/charges) object.

## Limits

You can over-capture up to 50% of the PaymentIntent’s authorized `amount`, or 50
USD, whichever is greater. For example, if your PaymentIntent’s authorized
`amount` is 40 USD, you can capture up to 90 USD; if your PaymentIntent’s
`amount` is 100 USD, you can capture up to 150 USD.

If you need to capture more than these limits allow, there are two options:

- If your MCC is eligible, you can use [incremental
authorization](https://docs.stripe.com/terminal/features/incremental-authorizations)
to increase the PaymentIntent’s `amount`.
- You can create a new PaymentIntent to capture the tip amount using the
[generated_card](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-payment_method-card-generated_from-payment_method_details-card_present-generated_card)
payment method from the first PaymentIntent.

## Availability

On-receipt tipping is available for United States businesses with eligible
merchant category codes (MCCs), for payments using Visa, Mastercard, Discover,
and American Express card brands.

Businesses in the following categories are eligible to collect tips using
over-capture:

- Taxicabs and limousines
- Eating places and restaurants
- Drinking places (alcoholic beverages)
- Fast food restaurants
- Beauty and barber shops
- Health and beauty spas

#### Merchant category codes (MCCs)

If you’re not sure about the eligibility of your merchant category, you can
contact [support](https://support.stripe.com/contact). If you’re a
[Connect](https://docs.stripe.com/connect) user, [set the merchant category
codes](https://docs.stripe.com/connect/setting-mcc) for your connected accounts
to match their businesses.

## Links

- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [collecting in-person
payments](https://docs.stripe.com/terminal/payments/collect-card-payment)
-
[overcapture_supported](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-overcapture_supported)
- [capture](https://docs.stripe.com/api/payment_intents/capture)
-
[amount_to_capture](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture)
-
[amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount)
-
[amount_authorized](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-amount_authorized)
- [Charge](https://docs.stripe.com/api/charges)
- [incremental
authorization](https://docs.stripe.com/terminal/features/incremental-authorizations)
-
[generated_card](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-payment_method-card-generated_from-payment_method_details-card_present-generated_card)
- [support](https://support.stripe.com/contact)
- [Connect](https://docs.stripe.com/connect)
- [set the merchant category codes](https://docs.stripe.com/connect/setting-mcc)