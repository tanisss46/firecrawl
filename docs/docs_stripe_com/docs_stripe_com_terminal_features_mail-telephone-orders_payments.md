# Process MOTO payments

## Process mail order and telephone order (MOTO) payments.

#### Note

MOTO payments are a gated feature. To request access, contact [Stripe
support](https://support.stripe.com/). After we enable the feature, you must
activate it by disconnecting from and reconnecting to your readers.

Server-driveniOSAndroidJavaScript
To process MOTO payments with a server-driven integration, you must:

- [Create a
PaymentIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments#create-payment-intent).
- [Process the
payment](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments#process-payment).
- [Verify the reader
state](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments#verify-reader-state).
- [Capture the
payment](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments#capture-payment).

#### Note

If you’re displaying cart details using the
[setReaderDisplay](https://docs.stripe.com/terminal/features/display) method,
you must reset the reader’s display from a line item interface to the splash
screen before collecting a MOTO payment.

![MOTO payment collection
screenshots](https://b.stripecdn.com/docs-statics-srv/assets/moto-payment-light.4990e358c1ac4d6e4c61d3d180e97e41.png)

MOTO payment collection flow

[Create a
PaymentIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments#create-payment-intent)
To begin collecting a MOTO payment, you must create a
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) with
[payment_method_types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
that includes `card`.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d capture_method=automatic \
 -d amount=1000
```

[Process the
payment](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments#process-payment)
After you create a `PaymentIntent`, use
[process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent)
to process the payment, setting
[process_config[moto]](https://docs.stripe.com/api/terminal/readers/process_payment_intent#process_payment_intent-process_config)
to `true`.

```
curl
https://api.stripe.com/v1/terminal/readers/{{READER_ID}}/process_payment_intent
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent={{PAYMENT_INTENT_ID}} \
 -d "process_config[moto]"=true
```

The
[process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent)
request is asynchronous. After the request, the reader prompts you to enter the
cardholder’s card number, CVC, expiration date, and postal code. You can then
confirm the cardholder’s details to submit the payment for authorization.

[Verify the reader
state](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments#verify-reader-state)
Your application must follow the instructions for [verifying the reader
state](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&reader=wpe#verify-reader)
to confirm a successful (approved) payment.

[Capture the
payment](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments#capture-payment)
You must call
[capture](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#capture-payment)
to complete the payment if the `PaymentIntent` has a status of
`requires_capture`.

## Links

- [Stripe support](https://support.stripe.com/)
- [setReaderDisplay](https://docs.stripe.com/terminal/features/display)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
-
[payment_method_types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
-
[process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent)
-
[process_config[moto]](https://docs.stripe.com/api/terminal/readers/process_payment_intent#process_payment_intent-process_config)
- [verifying the reader
state](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&reader=wpe#verify-reader)
-
[capture](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#capture-payment)