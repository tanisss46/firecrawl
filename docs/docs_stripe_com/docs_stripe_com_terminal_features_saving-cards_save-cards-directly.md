# Save directly without charging

## Collect details of a present card and save them for online use.

Use [SetupIntents](https://docs.stripe.com/payments/setup-intents) to collect
card details without charging the card. A SetupIntent can’t save a
`card_present` [PaymentMethod](https://docs.stripe.com/api/payment_methods)
directly, but in most cases you can create a reusable `generated_card`
PaymentMethod that represents the same card. From your customer’s perspective,
they’re the same payment method.

You can use [SetupIntents](https://docs.stripe.com/payments/setup-intents) to
collect card details on Visa, Mastercard, American Express, Discover, co-branded
Interac, and co-branded eftpos cards. Single-branded Interac cards and
single-branded eftpos cards aren’t supported.

#### Note

For businesses in [certain
verticals](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment#saving-digital-wallets),
Stripe offers a limited private beta feature that allows you to save digital
wallet payment methods. To request access, contact
[stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com).

Saving cards with Stripe Terminal using SetupIntents requires you to:

- Create or retrieve a [Customer](https://docs.stripe.com/api/customers) object.
- Create a [SetupIntent](https://docs.stripe.com/api/setup_intents) object to
track the process.
- Collect a payment method after collecting the customer’s consent.
- Submit the payment method details to Stripe.

#### Note

As of October 2024, we’ve changed the customer consent model to use the
`allow_redisplay` parameter instead of the legacy `customer_consent_collected`
parameter. If your integration uses `customer_consent_collected`, you must
update it to use `allow_redisplay` before March 31, 2025. For guidance, see the
[changelog
entry](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay).

Server-drivenJavaScriptiOSAndroidReact Native
#### Note

The server-driven-based SetupIntents API is compatible with BBPOS WisePOS E and
Stripe Reader S700.

## Create or retrieve a customer

To charge a card saved with Stripe, you must attach it to a
[Customer](https://docs.stripe.com/api/customers).

When you include a customer in your
[SetupIntent](https://docs.stripe.com/api/setup_intents) before confirming,
Stripe automatically attaches the generated card payment method to the
[Customer](https://docs.stripe.com/api/customers) object you provide.

Include the following code on your server to create a new `Customer`.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

## Create a SetupIntent

#### Note

We recommend providing a [customer
ID](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-customer)
while creating a SetupIntent—doing so attaches the card payment method to the
`Customer` upon successful setup. If you don’t provide a customer ID, you must
attach the payment method in a separate call.

A [SetupIntent](https://docs.stripe.com/api/setup_intents) is an object that
represents your intent to set up a customer’s payment method for future
payments. The SetupIntent tracks the steps of this setup process. For Terminal,
this includes collecting and recording cardholder consent.

You must create the SetupIntent on your server and include `card_present` on the
`payment_method_types` parameter.

The SetupIntent contains a [client
secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret),
which is a key that’s unique to the individual SetupIntent. You must obtain the
[client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
from the SetupIntent on your server and pass it to the client side.

```
# Request
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_26PHem9AhJZvU623DfE1x4sd:" \
 -d "payment_method_types[]"=card

# Response
{
 "id": "seti_1234567890abcdefghijklmn",
 "object": "setup_intent",
"client_secret": "seti_1234567890abcdefghijklmn_secret_5678901234opqrstuvwxyz",
 ... # other SetupIntent fields
}

# Your server endpoint response
{
 "id": "seti_1234567890abcdefghijklmn",
 "client_secret": "seti_1234567890abcdefghijklmn_secret_5678901234opqrstuvwxyz"
}
```

## Collect a payment method for saving cards

After you create a SetupIntent, you need to collect a payment method and collect
customer consent. Pass
[allow_redisplay](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
as `always` or `limited`, indicating the degree to which a payment method can be
shown in a customer checkout flow.

After you create a SetupIntent, you need to collect a payment method and collect
customer consent. If the customer provides the required form of agreement or
consent, set the `customer_consent_collected` Boolean to true.

#### Note

Collect customer consent verbally or with a checkbox in your application. You
must comply with all applicable laws, rules, and regulations in your region.

You must call the
[process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)
endpoint, which handles both collecting and confirming the SetupIntent. If the
customer provides consent, set `allow_redisplay` to either `always` or
`limited`.

```
curl
https://api.stripe.com/v1/terminal/readers/{{READER_ID}}/process_setup_intent \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d setup_intent={{SETUP_INTENT_ID}} \
 -d allow_redisplay=always
```

This method collects encrypted payment method data using the connected card
reader, and associates the encrypted data with the SetupIntent.

#### Caution

Collecting a payment method happens locally and requires no authorization or
updates to the SetupIntent object until the next step.

### Cancel collection

#### Programmatic cancellation

You can cancel collecting a payment method by calling
[cancel_action](https://docs.stripe.com/api/terminal/readers/cancel_action).

## Submit the payment method details to Stripe

Your previous call to
[process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)
handles the confirm for you, so no further action is necessary.

A successful setup returns a `succeeded` value for the SetupIntent’s
[status](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-status)
property, along with a
[SetupAttempt.payment_method_details.card_present.generated_card](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-payment_method_details-card_present-generated_card),
which is a reusable `card` payment method you can use for online payments.

#### Note

The
[SetupIntent.payment_method](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method)
is a `card_present` PaymentMethod that represents the tokenization of the
physically present card and isn’t chargeable online. Future payments use the
generated card instead. From the customer’s perspective, they’re the same
payment method.

The `generated_card` payment method automatically attaches to the customer you
provided during [SetupIntent
creation](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly#create-setupintent).
You can retrieve the `generated_card` payment method by expanding the
SetupIntent’s `latest_attempt` property. Always check for a `generated_card`
value, because for payment methods that don’t allow generated cards, the value
is empty.

```
curl -G https://api.stripe.com/v1/setup_intents/{{SETUP_INTENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=latest_attempt
```

Alternatively, you can retrieve the attached payment method by fetching the list
of payment methods that gets attached to the customer.

```
curl -G https://api.stripe.com/v1/customers/{{CUSTOMER_ID}}/payment_methods \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d type=card
```

If you didn’t provide a customer during SetupIntent creation, you can attach the
`generated_card` to a Customer object in a separate call.

```
curl https://api.stripe.com/v1/payment_methods/{{PAYMENT_METHOD_ID}}/attach \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}}
```

If the setup isn’t successful, inspect the returned error to determine the
cause. For example, failing to collect and notify Stripe of customer consent
results in an error.

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

## Save digital wallets

If your MCC is in one of the following ranges, you might be eligible to
participate in a limited beta for saving digital wallet payment methods. For
more details, contact
[stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com).

- Car Rental Agencies (3351 - 3500)
- Lodging – Hotels, Motels, Resorts (3501 - 3999)
- Steamship and Cruise Lines (4411)
- Boat Rentals and Leasing (4457)
- Lodging - Hotels, Motels, Resorts, Central Reservations Services (Not
Elsewhere Classified) (7011)
- Trailer Parks and Campgrounds (7033)
- Equipment, Tool, Furniture, and Appliance Rental and Leasing (7394)
- Car Rental Agencies (Not Elsewhere Classified) (7512)
- Truck and Utility Trailer Rentals (7513)
- Motor Home and Recreational Vehicle Rentals (7519)

When you save a digital wallet payment method, the `generated_card` has
`allow_redisplay=limited`, because checkout flows are prohibited from presenting
saved digital wallets as a payment option. You can only charge saved digital
wallet payment methods for
[off_session](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-off_session)
payments.

## Links

- [SetupIntents](https://docs.stripe.com/payments/setup-intents)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [certain
verticals](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment#saving-digital-wallets)
- [Customer](https://docs.stripe.com/api/customers)
- [SetupIntent](https://docs.stripe.com/api/setup_intents)
- [changelog
entry](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay)
- [customer
ID](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-customer)
- [Create a SetupIntent](https://docs.stripe.com/api/setup_intents/create)
- [client
secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret)
- [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
-
[process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)
-
[allow_redisplay](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
- [cancel_action](https://docs.stripe.com/api/terminal/readers/cancel_action)
-
[status](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-status)
-
[SetupAttempt.payment_method_details.card_present.generated_card](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-payment_method_details-card_present-generated_card)
-
[SetupIntent.payment_method](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method)
- [SetupIntent
creation](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly#create-setupintent)
-
[off_session](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-off_session)