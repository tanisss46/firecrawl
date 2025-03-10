# Compare the Payment Element and Card Element

## Select the right Element for your payment integration.

Previously, each payment method (for example, cards and iDEAL) required
integrating a separate Element. Now, you can use the Payment Element to accept
payments from one or multiple payment methods. Since this also includes cards,
you have the option to integrate the Card Element or the Payment Element to
accept card payments.

For most users, the Payment Element is the best option to process cards. The
integration effort is the same as the Card Element and it supports all the
common payment flows. It also gives you instant access to additional payment
methods, including Google Pay and Apple Pay. Accepting more [payment
methods](https://docs.stripe.com/payments/payment-methods/overview) can help
your business expand its global reach and improve checkout conversion.

If you’re already using the [Card
Element](https://docs.stripe.com/js/element/other_element?type=card) and want to
migrate to the [Payment
Element](https://docs.stripe.com/js/element/payment_element), follow our
[migration guide](https://docs.stripe.com/payments/payment-element/migration).

#### Note

You can have a single line [Card
Element](https://docs.stripe.com/js/element/other_element?type=card) or use
split Elements, such as [Card
Number](https://docs.stripe.com/js/element/other_element?type=cardNumber),
[Expiry](https://docs.stripe.com/js/element/other_element?type=cardExpiry), and
[CVC](https://docs.stripe.com/js/element/other_element?type=cardCvc). When
referring to the Card Element, the information below applies to both styles.

FeaturesPayment ElementCard ElementAccepts card paymentsAccepts card payments
using Wallets (for example, Apple Pay and Google Pay)Accepts payments with other
payment methodsEnables faster checkout with
[Link](https://docs.stripe.com/payments/link)Customizable look and feelHandles
all [Stripe supported card
brands](https://docs.stripe.com/payments/cards#supported-card-brands)Handles [3D
Secure authentication](https://docs.stripe.com/payments/3d-secure)Input
style1SplitSplit and single-line
1Using split input fields is more accessible than using a single line input.

## Advanced scenarios

Advanced scenariosPayment ElementCard Element[Set up future
payments](https://docs.stripe.com/payments/save-and-reuse)[Save payment details
during payment](https://docs.stripe.com/payments/save-during-payment)Updating a
customer’s saved payment details[Place a hold on a payment
method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Credit
card installments](https://docs.stripe.com/payments/mx-installments)Charge a
different [application fee
amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-application_fee_amount)
based on the card brand, country, or payment methodCharging differently based on
the payment method selectedDisplaying a review page after collecting payment
details[Brand choice for cobranded
cards](https://docs.stripe.com/co-badged-cards-compliance)Collecting card
information so that you can run a validation for verification purposes
If you want to use the Card Element, see our guide on [accepting a
payment](https://docs.stripe.com/payments/card-element).

## Links

- [payment methods](https://docs.stripe.com/payments/payment-methods/overview)
- [Card Element](https://docs.stripe.com/js/element/other_element?type=card)
- [Payment Element](https://docs.stripe.com/js/element/payment_element)
- [migration guide](https://docs.stripe.com/payments/payment-element/migration)
- [Card
Number](https://docs.stripe.com/js/element/other_element?type=cardNumber)
- [Expiry](https://docs.stripe.com/js/element/other_element?type=cardExpiry)
- [CVC](https://docs.stripe.com/js/element/other_element?type=cardCvc)
- [Link](https://docs.stripe.com/payments/link)
- [Stripe supported card
brands](https://docs.stripe.com/payments/cards#supported-card-brands)
- [3D Secure authentication](https://docs.stripe.com/payments/3d-secure)
- [Set up future payments](https://docs.stripe.com/payments/save-and-reuse)
- [Save payment details during
payment](https://docs.stripe.com/payments/save-during-payment)
- [Place a hold on a payment
method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [Credit card installments](https://docs.stripe.com/payments/mx-installments)
- [application fee
amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-application_fee_amount)
- [Brand choice for cobranded
cards](https://docs.stripe.com/co-badged-cards-compliance)
- [accepting a payment](https://docs.stripe.com/payments/card-element)