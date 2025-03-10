# Migrate to Stripe iOS SDK 24

## Migrate your Swift and Objective-C apps to our latest iOS SDK major version.

From SDK 20From SDK 21From SDK 22From SDK 23
### PaymentSheet

PaymentSheet displays payment methods in either a vertical or horizontal layout.
Prior to this major version, PaymentSheet defaulted to a horizontal layout. Now,
Stripe optimizes the layout automatically. To set a specific layout instead, set
the `PaymentSheet.Configuration.paymentMethodLayout` property to either
`.horizontal` or `.vertical`.

!

This example code sets the layout back to horizontal, the previous default.

```
var configuration = PaymentSheet.Configuration()
configuration.paymentMethodLayout = .horizontal
```

### Basic integration

We no longer support our legacy Basic Integration for collecting credit card and
wallet payments.

If your app relies on any of the following APIs, it uses the Basic Integration.
Migrate to the Mobile Payment Element, by following this [migration
guide](https://docs.stripe.com/payments/mobile/migrating-to-mobile-payment-element-from-basic-integration).

- `STPCustomerContext`
- `STPPaymentContext`
- `STPPaymentOptionsViewController`
- `STPAddCardViewController`
- `STPShippingAddressViewController`

## Links

- [migration
guide](https://docs.stripe.com/payments/mobile/migrating-to-mobile-payment-element-from-basic-integration)