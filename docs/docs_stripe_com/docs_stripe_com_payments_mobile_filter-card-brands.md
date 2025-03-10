# Filter card brands

## Choose which card brands to accept

iOSAndroidReact Native
Use the Stripe [Mobile Payment
Element](https://docs.stripe.com/payments/elements/mobile-payment-element) to
control which card brands you accept. Card brand filtering lets you specify
allowed or disallowed card brands for:

- The credit card form in the Mobile Payment Element
- The cards buyers can use with Google Pay.

When you configure the Mobile Payment Element, you can specify one of two
options:

- `allowed`: Accept only the card brands you specify.
- `disallowed`: Accept all card brands except those you specify.

For either of these options, pass an array with any of the following card brand
values as defined on `PaymentSheet.CardBrandAcceptance.BrandCategory`:

- `Visa`
- `Mastercard`
- `Amex`
- `Discover`

#### Note

The `Discover` value encompasses all of the cards that are part of the Discover
Global Network, including Discover, Diners Club, JCB, UnionPay, and Elo.

This guide demonstrates how to use card brand filtering to only accept card
payments from Visa and Mastercard branded cards.

## Before you begin

- [Create a Stripe account](https://dashboard.stripe.com/register) or [sign
in](https://dashboard.stripe.com/login).
- Follow the steps in [Accept in-app
payments](https://docs.stripe.com/payments/mobile/accept-payment) to integrate
with the Mobile Payment Element.
[Filter card
brands](https://docs.stripe.com/payments/mobile/filter-card-brands#card-brand-filtering-android)
When you create your `PaymentSheet.Configuration` object, specify the card
brands you want to allow or disallow using the `cardBrandAcceptance` property.
This example shows how to allow only Visa and Mastercard:

```
import com.stripe.android.paymentsheet.PaymentSheet

class CheckoutActivity : AppCompatActivity() {

 private fun onPayClicked(
 paymentSheet: PaymentSheet,
 paymentIntentClientSecret: String,
 ) {
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName =
"Example, Inc.")
 .cardBrandAcceptance(
 PaymentSheet.CardBrandAcceptance.allowed(
 listOf(
 PaymentSheet.CardBrandAcceptance.BrandCategory.Visa,
 PaymentSheet.CardBrandAcceptance.BrandCategory.Mastercard
 )
 )
 )
 .build()

 // Present Payment Sheet
paymentSheet.presentWithPaymentIntent(paymentIntentClientSecret, configuration)
 }
}
```

[Test your
integration](https://docs.stripe.com/payments/mobile/filter-card-brands#testing-android)
Stripe provides a set of [test card
numbers](https://docs.stripe.com/testing#cards) that you can use to test your
checkout flow and verify that the Mobile Payment Element accepts or blocks your
desired card brands.

![The Mobile Payment Element when a card brand is
disallowed](https://b.stripecdn.com/docs-statics-srv/assets/filter-card-brands-android.fb9f9a9aa83ea4848db35adbaca08e7a.png)

## Links

- [Mobile Payment
Element](https://docs.stripe.com/payments/elements/mobile-payment-element)
- [Create a Stripe account](https://dashboard.stripe.com/register)
- [sign in](https://dashboard.stripe.com/login)
- [Accept in-app
payments](https://docs.stripe.com/payments/mobile/accept-payment)
- [test card numbers](https://docs.stripe.com/testing#cards)