# Provide receipts

## Use Stripe to provide your customers with receipts that meet card network rules.

Card network rules and local regulatory requirements are different for in-person
payments. If you accept payments using Stripe Terminal, you must provide
customers with the option to receive a physical or email receipt. Stripe
provides everything you need to start offering receipts with your first
transaction.

Receipts must contain certain fields to comply with card network rules. You can
use Stripe’s [prebuilt email
receipts](https://docs.stripe.com/terminal/features/receipts#prebuilt), or use
receipt data from the Stripe API and your Terminal integration to generate
on-brand [custom
receipts](https://docs.stripe.com/terminal/features/receipts#custom).

## Prebuilt email receipts

Prebuilt email receipts already include all card network-required fields. It’s
the simplest way to set up compliant receipts.

If you have the customer’s email, use the `receipt_email` field when [creating a
PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-receipt_email).
When you provide a `receipt_email`, Stripe automatically emails a compliant
receipt to the customer when
[capturing](https://docs.stripe.com/terminal/payments/collect-card-payment#capture-payment)
the PaymentIntent.

To trigger an automatic email receipt *after* the customer checks out, update
the PaymentIntent’s `receipt_email` with the customer’s email.

For more information about automatic email receipts, see [Email
Receipts](https://docs.stripe.com/receipts).

!

## Custom receipts

You can also customize receipts to include any design and content you want—as
long as you list required information. When you accept in-person payments with
EMV chip cards, card networks require you to include several fields on the
receipts you provide to customers.

The Stripe API allows you to fetch necessary fields for compliance-ready
receipts.

The following fields become available in the PaymentIntent object as soon as the
payment is
[confirmed](https://docs.stripe.com/terminal/payments/collect-card-payment#confirm-payment).

FieldNameRequirement`account_type`Account TypeRequired (Optional in
US)`application_preferred_name`Application
nameRequired`dedicated_file_name`AIDRequired`authorization_response_code`ARCOptional`application_cryptogram`Application
CryptogramOptional`terminal_verification_results`TVROptional`transaction_status_information`TSIOptional
You can access these fields server-side using the Stripe API, or client-side
using the Stripe Terminal SDKs. When using the JavaScript SDK, the PaymentIntent
object matches the [API
object](https://docs.stripe.com/api/payment_intents/object).

Whether you’re emailing or printing your custom receipts for Terminal payments,
be sure to include the **required** fields to meet card network rules. If
provided, you can also access the cardholder’s preferred language (based on the
presented card’s settings), using the `preferred_locales` field on the [Payment
Method](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card_present-preferred_locales)
object.

## Links

- [test API keys](https://docs.stripe.com/keys#test-live-modes)
- [Dashboard](https://dashboard.stripe.com/payments)
-
[receipt_email](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-receipt_email)
- [receiptEmail
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPPaymentIntentParameters.html#/c:objc(cs)SCPPaymentIntentParameters(py)receiptEmail)
- [receiptEmail
(Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-payment-intent-parameters/receipt-email.html)
- [receiptEmail (React
Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#CreatePaymentIntentParams)
- [receiptEmail
(Java)](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.models/-payment-intent-parameters/receipt-email.html)
-
[capturing](https://docs.stripe.com/terminal/payments/collect-card-payment#capture-payment)
- [Email Receipts](https://docs.stripe.com/receipts)
-
[confirmed](https://docs.stripe.com/terminal/payments/collect-card-payment#confirm-payment)
-
[receipt](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-receipt)
- [ReceiptDetails
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPReceiptDetails.html)
- [ReceiptDetails
(Android)](https://stripe.dev/stripe-terminal-android/external/com.stripe.stripeterminal.external.models/-receipt-details/index.html)
- [ReceiptDetails (React
Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/index.html#ReceiptDetails)
- [ReceiptDetails
(Java)](https://stripe.dev/stripe-terminal-java/external/com.stripe.stripeterminal.external.models/-receipt-details/index.html)
- [API object](https://docs.stripe.com/api/payment_intents/object)
- [Payment
Method](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card_present-preferred_locales)