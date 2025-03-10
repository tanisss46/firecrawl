# Test Stripe Invoicing

## Learn how to test your Invoicing integration.

Use these common scenarios to test your invoicing integration before taking it
live.

## Test webhook notifications

Stripe triggers event notifications when an
[invoice’s](https://docs.stripe.com/api/invoices) [status
changes](https://docs.stripe.com/invoicing/integration/workflow-transitions#status-transitions-endpoints).
After you set up the Stripe CLI and link to your Stripe account, you can test
webhooks by:

- Triggering event notifications with the [Stripe
CLI](https://docs.stripe.com/stripe-cli). See a complete list of [invoice event
types](https://docs.stripe.com/api/events/types#event_types-invoice.created).
- Using the Dashboard to [create
invoices](https://dashboard.stripe.com/test/invoices/create) in [test
mode](https://docs.stripe.com/test-mode).

You can add an endpoint and see its received events by going to
[Webhooks](https://dashboard.stripe.com/test/webhooks) in the Dashboard.

### Test events with fake data

By using the Stripe CLI to trigger events, you can see event notifications on
your server as they come in. This means that you can check your webhook
integration directly without complicating factors such as network tunnels or
firewalls. When you use the Stripe CLI, the event your webhook receives contains
fake data that doesn’t correlate to invoice information.

### Test events with real data

The most reliable way to test webhook notifications is to create test invoices
for existing customers and handle the corresponding events.

## Test payment failures

To trigger payment failures for invoices, you can use the test credit card
numbers in [Declined
payments](https://docs.stripe.com/testing#declined-payments). If you want to
simulate a declined payment for a card that’s been successfully attached to a
customer, use **4000 0000 0000 0341** as their default payment method.

Depending on your [retry
settings](https://docs.stripe.com/invoicing/automatic-collection), you might
have to wait a day or more to see the first retry attempt. To see what happens
for a successful retry, you can use this waiting period to update the customer’s
payment method to a working test card.

## Test payments that require 3D Secure

Use the [4000 0027 6000 3184](https://docs.stripe.com/testing#regulatory-cards)
card to simulate 3D Secure triggering for invoices. When Stripe triggers a 3D
Secure authentication, you can test authenticating or failing the payment
attempt in the 3DS dialog that opens. If the payment is authenticated
successfully, the invoice is paid. When a payment attempt fails, the
authentication attempt is unsuccessful and the invoice remains `open`.

## Test bank transfer payments

To test manual payments on invoices through bank transfers:

- Create a testmode invoice with the collection method set to `send_invoice` and
`payment_settings[payment_method_types]` array set to `[customer_balance]`.
- Find the invoice in the Dashboard and click **Send**. This generates a unique
virtual bank account number for your customer.
- Retrieve your customer’s unique virtual bank account number using the
[Customer Balance Funding Instructions
API)(/docs/payments/customer-balance/funding-instructions#create-funding-instructions).
You can also find your customer’s virtual banking details in the Hosted Invoice
Page and PDF.

## Test customer tax ID verification

Use these magic tax IDs to trigger certain verification conditions in test mode.
The tax ID type must be either the EU VAT Number or Australian Business Number
(ABN).

NumberType`000000000`Successful verification`111111111`Unsuccessful
verification`222222222`Verification remains pending indefinitely

## Links

- [testing page](https://docs.stripe.com/testing)
- [Testing Stripe Billing](https://docs.stripe.com/billing/testing)
- [invoice’s](https://docs.stripe.com/api/invoices)
- [status
changes](https://docs.stripe.com/invoicing/integration/workflow-transitions#status-transitions-endpoints)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [invoice event
types](https://docs.stripe.com/api/events/types#event_types-invoice.created)
- [create invoices](https://dashboard.stripe.com/test/invoices/create)
- [test mode](https://docs.stripe.com/test-mode)
- [Webhooks](https://dashboard.stripe.com/test/webhooks)
- [Declined payments](https://docs.stripe.com/testing#declined-payments)
- [retry settings](https://docs.stripe.com/invoicing/automatic-collection)
- [4000 0027 6000 3184](https://docs.stripe.com/testing#regulatory-cards)