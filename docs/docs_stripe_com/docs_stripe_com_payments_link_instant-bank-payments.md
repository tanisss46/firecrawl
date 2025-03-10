# Instant Bank Payments

## Accept low cost bank payments with instant confirmation.

Available in: 
Instant Bank Payments let your customers pay with a US bank account using Link.
Unlike [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit),
Instant Bank Payments deliver instant confirmation and faster settlement,
protection from common ACH failures, and accelerated checkout.

Instant Bank Payments are automatically enabled when you turn on
[Link](https://docs.stripe.com/payments/link), subject to
[eligibility](https://docs.stripe.com/payments/link/instant-bank-payments#eligibility)
requirements. Go to your [payment method
settings](https://dashboard.stripe.com/settings/payment_methods) to manage Link
in your payment integrations. Not all businesses or transactions are eligible
for Instant Bank Payments.

For information about how your payment integration affects Link, see [Link in
different payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations).

## Payment flow

At checkout, the Instant Bank Payment flow depends on whether the customer has a
Link account.

### Flow for new Link customers

![Payment
page](https://b.stripecdn.com/docs-statics-srv/assets/bank-tab.f68600e3dfe858e077d044c193e249c4.png)

Under **Payment details**, they select **Bank**, then search for and select
their bank.

![Link agreement
page](https://b.stripecdn.com/docs-statics-srv/assets/consent.706738ec6793f218792313c32a2c08de.png)

They click **Agree and continue**.

![Link login or sign up
page](https://b.stripecdn.com/docs-statics-srv/assets/sign-up.1fac9f2a7f8ce0b02d6a00af60373dab.png)

They enter their email and click **Continue with Link**.

![Bank login
page](https://b.stripecdn.com/docs-statics-srv/assets/oauth.c007a2dbaa3206e732d4dd0b6c374af0.png)

They enter their bank login credentials and click **Submit**.

![Link success
page](https://b.stripecdn.com/docs-statics-srv/assets/success.cb45bc1cb44c0f1d8f8d8156497d5d64.png)

They click **Back to Powdur**.

The customer then returns to the payment details page and continues with their
new Link account.

### Flow for existing Link customers

When a customer with a Link account encounters Link at checkout, they have the
option to pay with their saved bank account.

![Payment
page](https://b.stripecdn.com/docs-statics-srv/assets/bank-tab.f68600e3dfe858e077d044c193e249c4.png)

Under **Payment details**, they select **Bank**, then search for and select
their bank.

![Link Welcome Back
page](https://b.stripecdn.com/docs-statics-srv/assets/returning.db06671ab9ed4b881e90398d52654d9a.png)

They enter their email and click **Continue with Link**.

![2FA confirmation
page](https://b.stripecdn.com/docs-statics-srv/assets/otp.16c215fdabb2443944f785b063cd4536.png)

They enter their 2FA confirmation code.

![Link select account
page](https://b.stripecdn.com/docs-statics-srv/assets/saved.b60f46f0013d166a37868d6b6ea3e011.png)

They select their saved bank account and click **Connect account**.

![Link success
page](https://b.stripecdn.com/docs-statics-srv/assets/success.cb45bc1cb44c0f1d8f8d8156497d5d64.png)

They click **Back to Powdur**.

The customer then completes the transaction.

## Timing and guaranteed settlement

Confirmation of Instant Bank Payments is immediate, and authorized payments
settle to your Stripe balance on the same timeline as card payments. Stripe
guarantees that authorized payments settle to your account unless the customer
initiates a dispute with their bank.

![2 day settlement
timeline](https://b.stripecdn.com/docs-statics-srv/assets/settlement-timing.be2862d8a51f4d6c1cc339371c7bc0d2.png)

Instant Bank Payments are subject to two types of returns:

- **Bank-initiated ACH returns**: Stripe still guarantees settlement and doesn’t
debit any funds from your balance.
- **Customer-initiated disputes**: When your customer initiates a dispute with
their bank, Stripe debits your balance for the payment amount and dispute fee.
To respond and provide supporting text and images, follow the same [guided
process in your Stripe Dashboard](https://docs.stripe.com/disputes/responding)
as for cardholder disputes.

## Availability of Instant Bank Payments

Instant Bank Payments are built into Link for users in the US. For eligible
transactions, your customers see Instant Bank Payments as a payment option.

To learn about using Link with dynamic payment methods and other integrations,
see [Link payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations).
The following payment integrations support Instant Bank Payments:

- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Payment Element](https://docs.stripe.com/payments/elements)
- [Mobile Payment
Element](https://docs.stripe.com/payments/accept-a-payment?platform=ios&mobile-ui=payment-element)

### Eligibility

Some businesses and transactions aren’t eligible for Instant Bank Payments. In a
given session, Instant Bank Payments appear as a payment option only when
certain risk criteria are met. Some examples include:

- **Two-step authentication**: You must enable [two-step
authentication](https://support.stripe.com/questions/enable-two-step-authentication)
on your Stripe account.
- **Onboarding criteria**: You must satisfy certain onboarding criteria,
including, but not limited to, being a US business and having a history of
Stripe usage.
- **Transaction limits**: Eligible transactions must be below an amount
dynamically set by our risk systems. By default, Instant Bank Payments are
presented only for transactions under $500.
- **ACH Direct Debit**: If you have enabled ACH Direct Debit for a transaction,
then Link doesn’t present Instant Bank Payments as a payment option.

### Interaction with ACH Direct Debit

You can’t present both [ACH Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit) and Instant Bank
Payments as payment options for the same transaction. If you enable both ACH
Direct Debit and Instant Bank Payments, ACH Direct Debit takes precedence at
checkout:

- When creating a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_types),
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_types),
or
[SetupIntent](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_types),
if you explicitly offer ACH Direct Debit by including `us_bank_account` in
`payment_method_types`, Link never presents Instant Bank Payments as a payment
option.
- When using [dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods),
for any transaction that’s eligible for ACH Direct Debit, Link doesn’t present
Instant Bank Payments as a payment option. However, you can restrict ACH Direct
Debit eligibility by configuring a [payment method
rule](https://docs.stripe.com/payments/payment-method-rules). For all
transactions that don’t meet the ACH rule criteria but that are eligible for
Instant Bank Payments, Link presents Instant Bank Payments as a payment option.

We recommend ACH Direct Debit for businesses that don’t immediately fulfill
goods and services, and that can wait up to 4 business days to confirm a
payment.

## Testing

Stripe provides a set of test institutions and bank accounts to simulate various
success and failure scenarios.

### Simulate successful bank account connection

- **Payment Success**: Simulates a successful bank account connection and an
authorized payment.
- **Success (Later Disputed)**: Simulates a successful bank account connection
and an authorized payment, then generates a customer-initiated dispute. You can
view the dispute in the Dashboard.
- **Payment Blocked**: Simulates a successful bank account connection and a
payment that Stripe declines due to elevated risk.

### Simulate failed bank account connection

- **Down Bank (Scheduled)**: The institution’s login API is unavailable for a
known time period that the institution communicated to Stripe.
- **Down Bank (Unscheduled)**: The institution’s login API is unavailable
without any information about the downtime communicated to Stripe.
- **Down Bank (Error)**: Stripe is experiencing an unknown error communicating
with the institution.

## See also

- [Link with Checkout](https://docs.stripe.com/payments/link/checkout-link)
- [Link with Elements](https://docs.stripe.com/payments/link/elements-link)
- [Link with Invoicing](https://docs.stripe.com/payments/link/invoicing)

## Links

- [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit)
- [Link](https://docs.stripe.com/payments/link)
- [payment method
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Link in different payment
integrations](https://docs.stripe.com/payments/link/link-payment-integrations)
- [guided process in your Stripe
Dashboard](https://docs.stripe.com/disputes/responding)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Payment Element](https://docs.stripe.com/payments/elements)
- [Mobile Payment
Element](https://docs.stripe.com/payments/accept-a-payment?platform=ios&mobile-ui=payment-element)
- [two-step
authentication](https://support.stripe.com/questions/enable-two-step-authentication)
- [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_method_types)
-
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_types)
-
[SetupIntent](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_types)
- [dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [payment method rule](https://docs.stripe.com/payments/payment-method-rules)
- [Link with Checkout](https://docs.stripe.com/payments/link/checkout-link)
- [Link with Elements](https://docs.stripe.com/payments/link/elements-link)
- [Link with Invoicing](https://docs.stripe.com/payments/link/invoicing)