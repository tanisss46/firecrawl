# Save cards using MOTO

## Save mail order and telephone order (MOTO) card details for future payment.

#### Note

MOTO payments are a gated feature. To request access, contact [Stripe
support](https://support.stripe.com/). After we enable the feature, you must
activate it by disconnecting from and reconnecting to your readers.

You can save MOTO card details only in the following countries:

AustraliaCanadaNew ZealandSingaporeUnited
StatesServer-driveniOSAndroidJavaScript
MOTO SetupIntents allow you to enter the card information on the reader and save
the payment details without charging the card.

To do this with a server-driven integration, you must:

- [Create or retrieve a
Customer](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly#create-customer).
- [Create a
SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly#create-setup-intent).
- [Process the
SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly#process-setupintent).
- [Verify the reader
state](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly#verify-reader-state).
- [Use the
PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly#use-payment-method).

![MOTO saving card
screenshots](https://b.stripecdn.com/docs-statics-srv/assets/moto-save-card-light.e745c8d7833fd8290aa7827c57139c6a.png)

Saving a card with MOTO flow

[Create or retrieve a
Customer](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly#create-customer)
To charge a card saved with Stripe, you must attach it to a
[Customer](https://docs.stripe.com/api/customers).

When you include a customer in your
[SetupIntent](https://docs.stripe.com/api/setup_intents) before confirming,
Stripe automatically attaches the generated card payment method to the provided
[Customer](https://docs.stripe.com/api/customers) object that you
create/retrieve.

Include the following code on your server to create a new `Customer`:

```
curl https://api.stripe.com/v1/customers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -X "POST"
```

[Create a
SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly#create-setup-intent)
A [SetupIntent](https://docs.stripe.com/api/setup_intents) is an object that
represents your intent to set up a customer’s payment method for future
payments. The SetupIntent tracks the steps of this setup process. The
[payment_method_types](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_types)
must include `card`.

```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "payment_method_types[]"=card
```

[Process the
SetupIntent](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly#process-setup-intent)
After you create the SetupIntent, use
[process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)
to process the payment, setting
[process_config[moto]](https://docs.stripe.com/api/terminal/readers/process_setup_intent#process_setup_intent-process_config)
to `true`. If the customer provides the required form of agreement or consent,
set the `customer_consent_collected` Boolean to true.

```
curl
https://api.stripe.com/v1/terminal/readers/{{READER_ID}}/process_setup_intent \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d setup_intent={{SETUP_INTENT_ID}} \
 -d "process_config[moto]"=true \
 -d customer_consent_collected=true
```

The
[process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)
request is asynchronous. After the request, the reader prompts you to enter the
cardholder’s card number, CVC, expiration date, and postal code. You can then
confirm the cardholder’s details to submit the card details for authorization.

[Verify the reader
state](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly#verify-reader-state)
Your application must follow the instructions for [verifying the reader
state](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&reader=wpe#verify-reader)
to confirm a successful (approved) SetupIntent.

[Use the
PaymentMethod](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly#use-payment-method)
You can now charge the saved PaymentMethod associated with the `Customer` using
a
[PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method).

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

- [Stripe support](https://support.stripe.com/)
- [Customer](https://docs.stripe.com/api/customers)
- [SetupIntent](https://docs.stripe.com/api/setup_intents)
- [Create a SetupIntent](https://docs.stripe.com/api/setup_intents/create)
-
[payment_method_types](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_types)
-
[process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)
-
[process_config[moto]](https://docs.stripe.com/api/terminal/readers/process_setup_intent#process_setup_intent-process_config)
- [verifying the reader
state](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&reader=wpe#verify-reader)
-
[PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method)