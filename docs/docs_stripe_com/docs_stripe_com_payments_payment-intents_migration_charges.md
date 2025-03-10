# Charges versus Payment Intents APIs

## Learn about the differences between Stripe's two core payment APIs and when to use them.

## Understanding the Stripe payment APIs

There are three ways to accept payments on Stripe today:

- Stripe Checkout
- Charges API
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)

[Stripe Checkout](https://docs.stripe.com/payments/checkout) is a prebuilt
payment page that you can redirect your customer to for simple purchases and
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating). It
provides many features, such as Apple Pay, Google Pay, internationalization, and
form validation.

The [Charges](https://docs.stripe.com/api/charges) and [Payment
Intents](https://docs.stripe.com/api/payment_intents) APIs let you build custom
payment flows and experiences.

The Payment Intents API is the unifying API for all Stripe products and payment
methods. While we are not deprecating Charges, new features are only available
with the Payment Intents API.

For a full feature comparison, see the table below:

Charges APIPayment Intents APIUsed by businesses with customers primarily in the
US / Canada who want a simple way to accept cards.Required for businesses that
accept multiple payment methods and cards requiring authentication (for example,
due to [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) in
Europe).Works on Web, iOS, and Android.Works on Web, iOS, and Android. Can also
be used to accept in-store payments with Terminal.Supports cards and all payment
methods on the [Sources API](https://docs.stripe.com/sources).Supports cards,
cards requiring 3DS, iDEAL, SEPA, and [many other payment
methods](https://docs.stripe.com/payments/payment-methods/overview).Is not SCA
ready[Is SCA ready](https://docs.stripe.com/strong-customer-authentication)
## Migrating code that reads from charges

If you have an application with multiple payment flows and incrementally
migrating each one from the Charges API to the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents), you should first update
any code that reads from the [Charge](https://docs.stripe.com/api/charges)
object. To help with this, the charge object has two additional properties,
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)
and
[billing_details](https://docs.stripe.com/api/charges/object#charge_object-billing_details),
which provide a consistent interface for reading the details of the payment
method used for the charge.

These fields are available on all API versions and on charge objects created
with both the Charges API and the Payment Intents API.

The following table shows commonly used properties on a charge and how the same
information can be accessed using the additional properties:

Cards and bank accountsSourcesDescriptionBeforeAfterDetails about the payment
method used to create a charge`charge.source``charge.payment_method_details`ID
of the payment method used for the
charge`charge.source.id``charge.payment_method`Type of payment method
used`charge.source.object` (for example, `card` or
`bank_account`)`charge.payment_method_details.type`Billing information for the
charge (for example, billing postal
code)`charge.source.address_zip``charge.billing_details.address.postal_code`Name
of the cardholder`charge.source.name``charge.billing_details.name`Last 4 digits
of the card
used`charge.source.last4``charge.payment_method_details.card.last4`Fingerprint
of the
card`charge.source.fingerprint``charge.payment_method_details.card.fingerprint`CVC
verification status for the
charge`charge.source.cvc_check``charge.payment_method_details.card.checks.cvc_check`Card
brand values`charge.source.brand` can be one of: `American Express`, `Diners
Club`, `Discover`, `JCB`, `MasterCard`, `UnionPay`,
`Visa``charge.payment_method_details.card.brand` can be one of: `amex`,
`diners`, `discover`, `jcb`, `mastercard`, `unionpay`, `visa`Google Pay enum
value`charge.source.tokenization_method` is `android_pay``card.wallet.type`
within `charge.payment_method_details` is `google_pay`
## See also

- [Migrate to Payment
Intents](https://docs.stripe.com/payments/payment-intents/migration)

## Links

- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Charges](https://docs.stripe.com/api/charges)
- [Payment Intents](https://docs.stripe.com/api/payment_intents)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [Sources API](https://docs.stripe.com/sources)
- [many other payment
methods](https://docs.stripe.com/payments/payment-methods/overview)
-
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)
-
[billing_details](https://docs.stripe.com/api/charges/object#charge_object-billing_details)
- [Migrate to Payment
Intents](https://docs.stripe.com/payments/payment-intents/migration)