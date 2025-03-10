# Collect and save cards for online payments

## Use your Stripe Terminal integration to collect and save card details for online reuse.

Use Stripe Terminal to collect and save [payment
methods](https://docs.stripe.com/api/payment_methods) (excluding [mobile
wallets](https://docs.stripe.com/payments/wallets)) for online reuse. Use an
in-person card to initiate an online
[subscription](https://docs.stripe.com/billing/subscriptions/creating) using
[Billing](https://docs.stripe.com/billing), save payment details to a customer’s
online account, or defer payment.

## Collect and save reusable card details

You can collect reusable card details and save them for online use with
Terminal:

- [Directly, without charging the
card](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly)
- [After
payment](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment)

## Create a reusable PaymentMethod

When you create a PaymentIntent or SetupIntent with a card-present payment
method, you can’t save the PaymentMethod directly. However, in most cases,
Stripe can create a reusable `generated_card` PaymentMethod using the card
information. It represents the same payment method and can be reused for online
payments.

## Charge a saved card

You can charge customers at a later date using card details that were saved
during an earlier transaction.

To charge a saved card for future purchases, [create and confirm a
PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method)
with the saved payment method.

To [save a card from a Terminal
PaymentIntent](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment),
attach the `generated_card` PaymentMethod to a Customer. This allows you to
reuse it without having to collect payment details again. If you attach a
PaymentMethod to a PaymentIntent without also attaching the PaymentMethod to a
Customer, you won’t be able to reuse the Payment Method in future transactions.

## Charge customers outside the checkout flow

If the customer isn’t in your checkout flow when you charge the customer, set
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
to `true`. This causes the PaymentIntent to throw an error if customer
authentication is required.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="card" \
 -d "amount"=1099 \
 -d "currency"="usd" \
 -d "customer"="{{CUSTOMER_ID}}" \
 -d "payment_method"="{{PAYMENT_METHOD_ID}}"
```

When charging a saved card, you can’t use the
[confirmPaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment#confirm-payment)
method. Payments with generated cards are online payments and can’t be processed
with Terminal SDK methods.

## Track customer behavior with card fingerprints

Use the Stripe API to recognize repeat customers across online and retail
channels by correlating transactions by the same card. Like `card` payment
methods, each `card_present` payment method has a
[fingerprint](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-fingerprint)
attribute that uniquely identifies a particular card number. Cards from [mobile
wallets](https://docs.stripe.com/payments/wallets) (for example, Apple Pay or
Google Pay) don’t share a fingerprint with cards used online.

Starting with [API version
2018-01-23](https://docs.stripe.com/upgrades#2018-01-23), Connect platforms see
a fingerprint on `card_present` and `card` PaymentMethods that’s uniform across
all connected accounts. You can use this fingerprint to look up a specific
card’s charges in a connected account.

## Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. For example, the
European Data Protection Board has issued guidance regarding saving payment
details. These requirements generally apply if you want to save your customer’s
payment method for future use, such as presenting a customer’s payment method to
them in the checkout flow for a future purchase or charging them when they’re
not actively using your website or app.

Add terms to your website or app that state how you plan to save payment method
details and allow customers to opt in. If you plan to charge the customer while
they’re offline, then at a minimum, make sure that your terms also cover the
following:

- The customer’s agreement to your initiating a payment or a series of payments
on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for instance, whether
charges are for scheduled installment or subscription payments, or for
unscheduled top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a
subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

When you save a payment method, it can only be used for the specific usage that
you included in your terms. If you want to charge customers when they’re offline
and also save the customer’s payment method to present to them as a saved
payment method for future purchases, you must explicitly collect consent from
the customer. One way to do so is with a “Save my payment method for future use”
checkbox.

## Links

- [payment methods](https://docs.stripe.com/api/payment_methods)
- [mobile wallets](https://docs.stripe.com/payments/wallets)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Billing](https://docs.stripe.com/billing)
- [Directly, without charging the
card](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly)
- [After
payment](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment)
- [create and confirm a
PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method)
-
[off_session](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-off_session)
-
[confirmPaymentIntent](https://docs.stripe.com/terminal/payments/collect-card-payment#confirm-payment)
-
[fingerprint](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-fingerprint)
- [API version 2018-01-23](https://docs.stripe.com/upgrades#2018-01-23)