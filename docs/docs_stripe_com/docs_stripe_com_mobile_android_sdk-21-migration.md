# Migrate to Stripe Android SDK 21

## Migrate your Kotlin apps to our latest Android SDK major version.

From SDK 18From SDK 19From SDK 20
### CollectBankAccountLauncher

[CollectBankAccountLauncher](https://github.com/stripe/stripe-android/blob/f3233f35b2a7ec545042137604a2c5efa71d3151/payments-core/src/main/java/com/stripe/android/payments/bankaccount/CollectBankAccountLauncher.kt)’s
dependency `com.stripe.connections` has been renamed
`com.stripe.financial-connections`.

### PaymentSheet

PaymentSheet displays payment methods in either a vertical or horizontal layout.
Prior to this major version, PaymentSheet defaulted to a horizontal layout. Now,
Stripe optimizes the layout automatically. To set a specific layout instead, set
the `PaymentSheet.Configuration.paymentMethodLayout` property to either
`.horizontal` or `.vertical`.

!

This example code sets the layout back to horizontal, the previous default.

```
PaymentSheet.Configuration.Builder("Example, Inc.")
 .paymentMethodLayout(PaymentSheet.PaymentMethodLayout.Horizontal)
 .build()
)
```

### Basic integration

We no longer support our legacy Basic Integration for collecting credit card and
wallet payments.

If your app relies on any of the following APIs, it uses the Basic Integration.
Migrate to the Mobile Payment Element, by following this [migration
guide](https://docs.stripe.com/payments/mobile/migrating-to-mobile-payment-element-from-basic-integration).

-
[CustomerSession](https://github.com/stripe/stripe-android/blob/f3233f35b2a7ec545042137604a2c5efa71d3151/payments-core/src/main/java/com/stripe/android/CustomerSession.kt)
- `PaymentSession`
- `PaymentMethodsActivity`
- `AddPaymentMethodActivity`
- `PaymentFlowActivity`

## Links

-
[CollectBankAccountLauncher](https://github.com/stripe/stripe-android/blob/f3233f35b2a7ec545042137604a2c5efa71d3151/payments-core/src/main/java/com/stripe/android/payments/bankaccount/CollectBankAccountLauncher.kt)
- [migration
guide](https://docs.stripe.com/payments/mobile/migrating-to-mobile-payment-element-from-basic-integration)
-
[CustomerSession](https://github.com/stripe/stripe-android/blob/f3233f35b2a7ec545042137604a2c5efa71d3151/payments-core/src/main/java/com/stripe/android/CustomerSession.kt)