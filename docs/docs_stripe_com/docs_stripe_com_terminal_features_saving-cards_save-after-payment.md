# Save card details after payment

## Take an in-person payment and save card details to use later, when the cardholder is not physically present.

You can use Stripe Terminal to save payment details from an in-store card
purchase. A successful `card_present` payment returns a reusable `card`
PaymentMethod in the `generated_card` attribute. There are several use cases:

- A gym customer pays in person for an initial session and a membership
subscription. The transaction sets up a `generated_card` to use for future
automatic membership renewals.
- A customer at a clothing store provides their email address when making a
purchase at the checkout counter. The transaction creates a customer record and
an associated saved `generated_card`. That allows the customer to log into the
store’s website later and place an order using the same card.

The initial, in-person payment benefits from liability shift and, in certain
markets, [lower pricing](https://stripe.com/terminal#pricing) for standard
Terminal payments. However, subsequent payments using the `generated_card` are
card-not-present online transactions, without the liability shift.

#### Note

[Digital wallet payments](https://docs.stripe.com/payments/wallets) such as
Apple Pay or Google Pay can’t be saved and don’t create a `generated_card`.
However, for businesses in [certain
verticals](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment#saving-digital-wallets),
Stripe offers a limited private beta feature that allows you to save digital
wallet payment methods. To request access, contact
[stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com).

Server-drivenJavaScriptiOSAndroidReact Native[Create a
customer](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment#create-customer)
To set a card up for future payments, you must attach it to a
[Customer](https://docs.stripe.com/api/customers). Create a Customer object when
your customer creates an account with your business. Customer objects allow for
reusing payment methods and tracking across multiple payments.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Jenny Rosen" \
 --data-urlencode email="jennyrosen@example.com"
```

Successful creation returns the
[Customer](https://docs.stripe.com/api/customers/object) object. You can inspect
the object for the customer `id` and store the value in your database for later
retrieval.

You can find these customers in the
[Customers](https://dashboard.stripe.com/customers) page in the Dashboard.

[Create a
PaymentIntent](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment#create-paymentintent)
Request a `generated_card` when you create a PaymentIntent by specifying a value
for
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
If you intend to only reuse the payment method when the customer is present in
the checkout flow, use `on_session`. Otherwise, use `off_session`.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "setup_future_usage"="off_session" \
 -d "customer"="{{CUSTOMER_ID}}" \
 -d "amount"=1000 \
 -d "currency"="usd" \
 -d "payment_method_types[]"="card_present"
```

#### Note

Visa, Mastercard, American Express, Discover, and co-branded eftpos cards are
supported as `card_present` payment methods that can be saved as type `card`.

[Collect and process a payment
method](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment#collect-payment-method)
When the customer is ready to pay and has [consented to their card details being
saved](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment#compliance),
pass
[allow_redisplay](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
as `always` or `limited` into the `process_payment_intent` or
`collect_payment_method`Preview call. The value indicates the degree to which a
payment method can be shown in a customer checkout flow.

```
curl
https://api.stripe.com/v1/terminal/readers/{{READER_ID}}/process_payment_intent
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent={{PAYMENT_INTENT_ID}} \
 -d "process_config[allow_redisplay]"=always
```

```
curl
https://api.stripe.com/v1/terminal/readers/{{READER_ID}}/collect_payment_method
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent={{PAYMENT_INTENT_ID}} \
 -d "collect_config[allow_redisplay]"=always
```

If you use the `collect_payment_method` flow, which allows access to useful data
like card brand and funding from the PaymentMethod before confirming it, you
must also separately confirm the PaymentIntent.

```
curl
https://api.stripe.com/v1/terminal/readers/{{READER_ID}}/confirm_payment_intent
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent={{PAYMENT_INTENT_ID}}
```

[Access the
generated_card](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment#access-generated-card)
A successful payment with a card that supports future use returns a
PaymentIntent in the `requires_capture` or `succeeded` state, with a
[generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
attribute containing the reusable PaymentMethod. If you passed the customer ID
into the PaymentIntent creation call, the reusable PaymentMethod is
automatically attached to the [Customer](https://docs.stripe.com/api/customers)
object. Otherwise, you can [manually attach
it](https://docs.stripe.com/api/payment_methods/attach) in a separate call.

Always verify that the
[PaymentIntent.latest_charge](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge)
contains a `generated_card` value. Digital wallet payments might not create a
generated card. If that happens, and you require a reusable payment method, you
have two options:

- Prompt the cardholder to save a different card using the flow to [save a card
without taking a
payment](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly).
- Refund the in-person payment, indicate that the transaction failed, and
instruct the cardholder to use a different card.

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

- [lower pricing](https://stripe.com/terminal#pricing)
- [Digital wallet payments](https://docs.stripe.com/payments/wallets)
- [certain
verticals](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment#saving-digital-wallets)
- [Customer](https://docs.stripe.com/api/customers)
- [Customer](https://docs.stripe.com/api/customers/object)
- [Customers](https://dashboard.stripe.com/customers)
- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create)
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
-
[process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent)
-
[collect_payment_method](https://docs.stripe.com/api/terminal/readers/collect_payment_method)
- [consented to their card details being
saved](https://docs.stripe.com/terminal/features/saving-cards/save-after-payment#compliance)
-
[allow_redisplay](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay)
-
[confirm_payment_intent](https://docs.stripe.com/api/terminal/readers/confirm_payment_intent)
-
[generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card)
- [manually attach it](https://docs.stripe.com/api/payment_methods/attach)
-
[PaymentIntent.latest_charge](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge)
- [save a card without taking a
payment](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly)
-
[off_session](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-off_session)