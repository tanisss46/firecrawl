# Design an integration

## Learn what choices you need to make before integrating the Payment Element.

Before building your Payment Element integration, choose an integration path
that aligns with your business requirements.

The diagram below provides an overview of the integration guides available when
integrating the Payment Element.

Do you have a multi-page checkout?

Follow the [Build two-step
confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation)
guide

Do you have a dynamic checkout page where the amount might change based customer
inputs?

Do you have additional business logic that needs to run on your server prior to
PaymentIntent or SetupIntent confirmation?

Follow the [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements)
guide

Follow the [Finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server) guide

Follow the [Collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred) guide

The sections below demonstrate the two architectural choices required when
integrating the Payment Element.

[Choose when to create the PaymentIntent or SetupIntent
object](https://docs.stripe.com/payments/payment-element/design-an-integration#when-to-create-intent)
The Payment Element collects payment information from your customer and
populates it onto either a
[PaymentIntent](https://docs.stripe.com/api/payment_intents) or a
[SetupIntent](https://docs.stripe.com/api/setup_intents) object, depending on
whether you’re collecting payment or setting up a payment method for future use.
When a customer enters your checkout, you can either:

- **Create only the Payment Element**: Defer creating and confirming the
PaymentIntent or SetupIntent until the customer submits the payment form by
pressing the **Pay** button. Choose this option if:

- You have a multi-page checkout flow where the page for collecting payment
details comes before the page for payment submission or order summary. Learn how
to [build two-step
confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation).
- You have a dynamic checkout page where the amount can change based on customer
selections, such as changing the items or quantity of items being purchased, or
adding discount codes. By deferring Intent creation until after the customer
presses **Pay**, you eliminate the need to synchronize your Intent with the
changes made on the client. This is necessary because changes to amount affect
the eligibility of certain payment methods. Learn how to [collect payment
details before creating a
PaymentIntent](https://docs.stripe.com/payments/accept-a-payment-deferred) if
you’re confirming the Intent on your client and how to [finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server) if
you’re confirming the Intent on your server.
- **Create both the PaymentIntent/SetupIntent and the Payment Element**: Create
the PaymentIntent or SetupIntent before loading the checkout page and then
create the Payment Element, associating the two by providing the Intent’s
`client_secret` [as a parameter when creating the Elements
object](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-clientSecret).
Choose this option if:

- You have a static checkout page and want to quickly set up your integration.
Learn how to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements).
[Choose where to confirm the PaymentIntent or
SetupIntent](https://docs.stripe.com/payments/payment-element/design-an-integration#where-to-confirm-intent)
Payment information collected by the Payment Element is transferred onto the
PaymentIntent or SetupIntent at confirmation time. When the customer presses
**Pay**, you can either:

- **Confirm the PaymentIntent/SetupIntent on your client**: Code on your client
calls a Stripe SDK, which invokes the API to confirm the Intent. The Stripe SDK
also automatically handles additional next actions that might be required, such
as authenticating with [3D Secure](https://docs.stripe.com/payments/3d-secure),
and also localizes [error](https://docs.stripe.com/api/errors) messages. Choose
this option if:

- You don’t require the additional control of confirming the Intent on your
server, and you prefer the quickest integration.
- **Confirm the PaymentIntent/SetupIntent on your server**: Code on your server
directly invokes the API to confirm the Intent. If next actions are required,
you must handle them either manually or by using a Stripe SDK, e.g.
[stripe.handleNextAction](https://docs.stripe.com/js/payment_intents/handle_next_action).
Choose this option if:

- You have to execute business logic on your server before the confirmation,
such as payment method restrictions or adjusting application fees. After your
business logic runs, immediately confirm the Intent on your server to guarantee
that the client can’t make any changes that could invalidate your business
logic.

## Links

- [Build two-step
confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation)
- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements)
- [Finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server)
- [Collect payment details before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [SetupIntent](https://docs.stripe.com/api/setup_intents)
- [as a parameter when creating the Elements
object](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-clientSecret)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [error](https://docs.stripe.com/api/errors)
-
[stripe.handleNextAction](https://docs.stripe.com/js/payment_intents/handle_next_action)