# Accept a bank transfer

## Use the Payment Intents API to accept bank transfer payments.

The first time you accept a bank transfer payment from a customer, Stripe
generates a virtual bank account for them, which you can then share with them
directly. All future bank transfer payments from this customer get sent to this
bank account. In some countries, Stripe also provides you with a unique transfer
reference number that your customer should include with each transfer to make it
easier to match the transfer against outstanding payments. Some countries have
limits on the number of virtual bank account numbers that you can create for
free.

You can find an overview of the common steps when accepting a bank transfer
payment in the following sequence diagram:

With InvoicesWithout Invoices
Customer

Server

Stripe

Stripe creates an invoice with bank account information: `POST /v1/invoices`

Invoice sent by email

The customer sends the correct amount of funds by bank transfer

Adds funds to cash balance

Reconciles against outstanding invoices

POST `invoice.paid` webhook

POST `payment_intent.succeeded` webhook

Responds with `200 OK`

Common steps when accepting a bank transfer payment
## Handling underpayments and overpayments

With bank transfer payments, it’s possible that the customer sends you more or
less than the expected payment amount. If the customer sends too little, Stripe
partially funds an open payment intent. Invoices won’t be partially funded and
remain open until incoming funds cover the full invoice amount.

If the customer sends more than the expected amount, Stripe attempts to
reconcile the incoming funds against an open payment and keep the remaining
excess amount in the customer cash balance. You can find more details on how
Stripe handles reconciliation in the [reconciliation
section](https://docs.stripe.com/payments/customer-balance/reconciliation) of
our documentation.

With InvoicesWithout Invoices
When a customer underpays:

Customer

Server

Stripe

POST `cash_balance.funds_available`

Responds with `200 OK`

A customer has sent a bank transfer for less than the expected amount
When a customer overpays:

Customer

Server

Stripe

POST `payment_intent.succeeded`

POST `cash_balance.funds_available`

POST `invoice.paid`

Responds with `200 OK`

A customer has sent a bank transfer for more than the expected amount
## Handling multiple open payments or invoices

You might have multiple open payments or invoices which can be paid with a bank
transfer. In the default setup, Stripe attempts to [automatically
reconcile](https://docs.stripe.com/payments/customer-balance/reconciliation) the
bank transfer by using information like the transfer’s reference code or the
amount transferred.

You can disable automatic reconciliation and [manually
reconcile](https://docs.stripe.com/payments/customer-balance/reconciliation#cash-manual-reconciliation)
payments and invoices yourself. You can override the automatic reconciliation
behavior on a per-customer basis by setting [reconciliation
mode](https://docs.stripe.com/api/customers/create#create_customer-cash_balance-settings-reconciliation_mode)
to manual.

Stripe-hosted pageAdvanced integrationDirect API
#### Caution

Stripe automatically presents your customers payment method options by
evaluating their currency, payment method restrictions, and other parameters. We
recommend that you configure your payment methods from the Stripe Dashboard
using the instructions in [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted).

If you want to continue manually configuring the payment methods you present to
your customers with Checkout, use this guide. Otherwise, update your integration
to [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods).

Bank transfer is a
[single-use](https://docs.stripe.com/payments/payment-methods#usage) payment
method for Checkout where customers pay with a bank transfer using payment
instructions presented. When selecting to pay, the user is redirected to a
hosted page which displays bank transfer instructions and the status of the
transfer payment.

Bank transfer is also a [delayed notification payment
method](https://docs.stripe.com/payments/payment-methods), which means that
funds are not immediately available after payment.

#### Caution

Bank transfers aren’t available on Checkout Sessions that didn’t include an
existing [Customer
object](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer)
as part of the of the session creation request.

[Determine
compatibility](https://docs.stripe.com/payments/bank-transfers/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support Bank
Transfer payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency. If you have line items in different currencies, create separate
Checkout Sessions for each currency.
- You can only use one-time line items (Bank Transfer Checkout Sessions don’t
support recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans).
[Accept a
payment](https://docs.stripe.com/payments/bank-transfers/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Use this guide to enable Bank Transfer.

### Create or retrieve a Customer

You must associate a [Customer](https://docs.stripe.com/api/customers) object to
reconcile each bank transfer payment. If you have an existing Customer object,
you can skip this step. Otherwise, create a new Customer object.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

### Enable Bank Transfer as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Set `customer`
- Add `customer_balance` to the list of `payment_method_types`
- Make sure all your `line_items` use the same currency
USUKEUJPMX
```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][unit_amount]"=2000 \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 -d "payment_method_types[0]"=card \
 -d "payment_method_types[1]"=customer_balance \
 -d "payment_method_options[customer_balance][funding_type]"=bank_transfer \
-d
"payment_method_options[customer_balance][bank_transfer][type]"=us_bank_transfer
\
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/failure"
```

### Redirect to Stripe hosted bank transfer instructions page

#### Note

Unlike card payments, the customer isn’t always redirected to the
[success_url](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-success_url)
with bank transfer payment.

After submit the Checkout form successfully,

- If the customer already has a balance high enough to cover the request amount,
the payment immediately succeeds and the customer is redirected to the
[success_url](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-success_url).
- If the customer balance isn’t high enough to cover the request amount, the
customer is redirected to the
[hosted_instructions_url](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-hosted_instructions_url).
The page has the instructions to guide your customer through completing the
transfer.

Stripe allows customization of customer-facing UIs on the [Branding
Settings](https://dashboard.stripe.com/account/branding) page. The following
brand settings can be applied to the hosted instructions page:

- **Icon**—your brand image and public business name
- **Brand color**—used as the background color

### Fulfill your orders

Because bank transfer is a [delayed notification payment
method](https://docs.stripe.com/payments/payment-methods), you need to use a
method such as [webhooks](https://docs.stripe.com/webhooks) to monitor the
payment status and handle order fulfillment. Learn more about [setting up
webhooks and fulfilling orders](https://docs.stripe.com/checkout/fulfillment).

The following events are sent when the payment status changes:

Event NameDescriptionNext
steps[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)The
customer has successfully submitted the Checkout form and is redirected to
`hosted_instructions_url`.Wait for the customer to make the bank
transfer.[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)The
customer has successfully made the bank transfer. The `PaymentIntent`
transitions to `succeeded`.Fulfill the goods or services that the customer
purchased.[OptionalSend payment instruction
emails](https://docs.stripe.com/payments/bank-transfers/accept-a-payment#instruction-emails)[Test
your
integration](https://docs.stripe.com/payments/bank-transfers/accept-a-payment#checkout-test-your-integration)
You can test your integration by simulating an incoming bank transfer using the
API, Dashboard, or a beta version of the Stripe CLI.

DashboardAPIStripe CLI
To simulate a bank transfer using the Dashboard, navigate to the customer’s page
in the Dashboard. Under **Payment methods**, click **Add** and select **Fund
cash balance (testmode only)**.

## See also

- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [reconciliation
section](https://docs.stripe.com/payments/customer-balance/reconciliation)
- [manually
reconcile](https://docs.stripe.com/payments/customer-balance/reconciliation#cash-manual-reconciliation)
- [reconciliation
mode](https://docs.stripe.com/api/customers/create#create_customer-cash_balance-settings-reconciliation_mode)
- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [delayed notification payment
method](https://docs.stripe.com/payments/payment-methods)
- [Customer
object](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer)
- [Prices](https://docs.stripe.com/api/prices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Customer](https://docs.stripe.com/api/customers)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/failure](https://example.com/failure)
-
[success_url](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-success_url)
-
[hosted_instructions_url](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-hosted_instructions_url)
- [Branding Settings](https://dashboard.stripe.com/account/branding)
- [webhooks](https://docs.stripe.com/webhooks)
- [setting up webhooks and fulfilling
orders](https://docs.stripe.com/checkout/fulfillment)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
-
[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)