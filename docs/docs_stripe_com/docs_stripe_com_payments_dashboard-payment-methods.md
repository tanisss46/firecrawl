# Migrate payment methods to the Dashboard

## Turn on different Checkout payment methods through the Dashboard.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
By changing your integration to pull your payment method preferences from the
Dashboard, Stripe displays all compatible payment methods to your customers when
checking out depending on the chosen currency or any payment method restrictions
like maximum transaction amounts. Stripe also presents the most relevant payment
methods for each customer based on their location and currency used.

The checkout page prioritizes showing payment methods known to increase
conversion for your customer’s location while lower priority payment methods are
hidden beneath an overflow menu. Your customers see multiple payment methods at
checkout that are popular for their location and currency, but they still have
the option to choose a different payment method from the overflow menu.

[Update your
integration](https://docs.stripe.com/payments/dashboard-payment-methods#update)
For existing Stripe Checkout integrations that specify `payment_method_types`,
you must remove this parameter to migrate payment methods preferences to the
Dashboard. After you remove the parameter from your integration, some payment
methods turn on automatically including cards and wallets. The `currency`
parameter restricts the payment methods the customer sees in the Checkout
Session.

#### Warning

Upgrading your integration initially turns off any non-default payment methods
for your integration, like bank redirects. If you added payment methods to your
Checkout integration, you must go to the payment methods settings page in the
Dashboard to turn them back on.

```
Stripe::Checkout::Session.create({
 line_items: [
 {
 price_data: {
 currency: 'eur',
 product_data: {name: 'T-shirt'},
 unit_amount: 2000,
 },
 quantity: 1,
 },
 ],
 mode: 'payment',
# Remove the payment_method_types parameter to manage payment methods in the
Dashboard
 payment_method_types: ['card'],
 return_url: 'https://example.com/return',
 ui_mode: 'embedded',
})
```

[View available payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods#view-dash)
View your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) to see the
payment methods that you currently accept. This list includes the payment
methods turned on by default, like cards. These payment methods cost the same or
less than cards and settle immediately.

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn
individual payment methods on or off in the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout,
Stripe evaluates the currency and any restrictions, then dynamically presents
the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or
set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). By default,
Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe
filters them out even when they’re enabled. We filter Google Pay if you [enable
automatic tax](https://docs.stripe.com/tax/checkout) without collecting a
shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple
Pay or Google Pay. Stripe handles these payments the same way as other card
payments.

[Add or remove payment methods to your
integration](https://docs.stripe.com/payments/dashboard-payment-methods#add-remove)
On the payment methods settings Dashboard page, you can view the available
payment methods and turn on new payment methods for your integration.

You can enable some payment methods just by selecting **Turn on**. However, some
payment methods require additional steps to turn them on. For those cases,
you’ll see a button that says **Set up** or **Review terms**.

To learn more about which payment methods are right for your business, see our
[payment methods guide](https://stripe.com/payments/payment-methods-guide).

[(Recommended) Handle delayed notification payment
methods](https://docs.stripe.com/payments/dashboard-payment-methods#delayed-notifications)
Depending on the type of payment method you integrate, there can be a 2-14 day
delay in payment confirmation. If you set up
[webhooks](https://docs.stripe.com/webhooks) to [automatically
fulfill](https://docs.stripe.com/checkout/fulfillment#create-payment-event-handler)
orders with your Checkout integration, when you add your first delayed
notification payment methods, you might need to update your code.

#### Caution

This step is only required if you plan to use any of the following payment
methods: [Bacs Direct
Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment), [Bank
transfers](https://docs.stripe.com/payments/bank-transfers/accept-a-payment),
[Boleto](https://docs.stripe.com/payments/boleto/accept-a-payment), [Canadian
pre-authorized
debits](https://docs.stripe.com/payments/acss-debit/accept-a-payment),
[Konbini](https://docs.stripe.com/payments/konbini/accept-a-payment),
[OXXO](https://docs.stripe.com/payments/oxxo/accept-a-payment), [Pay by
Bank](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment), [SEPA
Direct Debit](https://docs.stripe.com/payments/sepa-debit/accept-a-payment),
[SOFORT](https://docs.stripe.com/payments/sofort/accept-a-payment), or [ACH
Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment).

When receiving payments with a delayed notification payment method, funds aren’t
immediately available. It can take multiple days for funds to process so you
should delay order fulfillment until the funds are available in your account.
After the payment succeeds, the underlying
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) status changes
from `processing` to `succeeded`.

You’ll need to handle the following Checkout events:

Event NameDescriptionNext
steps[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)The
customer has successfully authorized the debit payment by submitting the
Checkout form.Wait for the payment to succeed or
fail.[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)The
customer’s payment succeeded.Fulfill the purchased goods or
services.[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)The
payment was declined, or failed for some other reason.Contact the customer via
email and request that they place a new order.
These events all include the [Checkout
Session](https://docs.stripe.com/api/checkout/sessions) object.

Update your event handler to fulfill the order:

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

# You can find your endpoint's secret in the output of the `stripe listen`
# command you ran earlier
endpoint_secret = 'whsec_...'

post '/webhook' do
 event = nil

 # Verify webhook signature and extract the event
 # See https://stripe.com/docs/webhooks#verify-events for more information.
 begin
 sig_header = request.env['HTTP_STRIPE_SIGNATURE']
 payload = request.body.read
event = Stripe::Webhook.construct_event(payload, sig_header, endpoint_secret)
 rescue JSON::ParserError => e
 # Invalid payload
 return status 400
 rescue Stripe::SignatureVerificationError => e
 # Invalid signature
 return status 400
 end

 case event['type']
 if event['type'] == 'checkout.session.completed'
 checkout_session = event['data']['object']

 fulfill_order(checkout_session)
 end
 when 'checkout.session.completed'
 checkout_session = event['data']['object']

 # Save an order in your database, marked as 'awaiting payment'
 create_order(checkout_session)

 # Check if the order is already paid (for example, from a card payment)
 #
 # A delayed notification payment will have an `unpaid` status, as
 # you're still waiting for funds to be transferred from the customer's
 # account.
 if checkout_session.payment_status == 'paid'
 fulfill_order(checkout_session)
 end
 when 'checkout.session.async_payment_succeeded'
 checkout_session = event['data']['object']

 # Fulfill the purchase...
 fulfill_order(checkout_session)
 when 'checkout.session.async_payment_failed'
 session = event['data']['object']

 # Send an email to the customer asking them to retry their order
 email_customer_about_failed_payment(checkout_session)
 end

 status 200
end

def fulfill_order(checkout_session)
 # TODO: fill in with your own logic
 puts "Fulfilling order for #{checkout_session.inspect}"
end

def create_order(checkout_session)
 # TODO: fill in with your own logic
 puts "Creating order for #{checkout_session.inspect}"
end

def email_customer_about_failed_payment(checkout_session)
 # TODO: fill in with your own logic
puts "Emailing customer about payment failure for: #{checkout_session.inspect}"
end
```

### Testing

Ensure that `stripe listen` is still running. Go through Checkout as a test
user, like you did in the prior steps. Your event handler should receive a
`checkout.session.completed` event, and you should have successfully handled it.

Now that you’ve completed these steps, you’re ready to go live in production
whenever you decide to do so.

[Test your
integration](https://docs.stripe.com/payments/dashboard-payment-methods#test-your-integration)CardsWalletsBank
redirectsBank debitsVouchersCard numberScenarioHow to test4242424242424242The
card payment succeeds and doesn’t require authentication.Fill out the credit
card form using the credit card number with any expiration, CVC, and postal
code.4000002500003155The card payment requires
[authentication](https://docs.stripe.com/strong-customer-authentication).Fill
out the credit card form using the credit card number with any expiration, CVC,
and postal code.4000000000009995The card is declined with a decline code like
`insufficient_funds`.Fill out the credit card form using the credit card number
with any expiration, CVC, and postal code.6205500000000000004The UnionPay card
has a variable length of 13-19 digits.Fill out the credit card form using the
credit card number with any expiration, CVC, and postal code.
See [Testing](https://docs.stripe.com/testing) for additional information to
test your integration.

## Links

- [https://example.com/return](https://example.com/return)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [enable automatic tax](https://docs.stripe.com/tax/checkout)
- [payment methods guide](https://stripe.com/payments/payment-methods-guide)
- [webhooks](https://docs.stripe.com/webhooks)
- [automatically
fulfill](https://docs.stripe.com/checkout/fulfillment#create-payment-event-handler)
- [Bacs Direct
Debit](https://docs.stripe.com/payments/bacs-debit/accept-a-payment)
- [Bank
transfers](https://docs.stripe.com/payments/bank-transfers/accept-a-payment)
- [Boleto](https://docs.stripe.com/payments/boleto/accept-a-payment)
- [Canadian pre-authorized
debits](https://docs.stripe.com/payments/acss-debit/accept-a-payment)
- [Konbini](https://docs.stripe.com/payments/konbini/accept-a-payment)
- [OXXO](https://docs.stripe.com/payments/oxxo/accept-a-payment)
- [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment)
- [SEPA Direct
Debit](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [SOFORT](https://docs.stripe.com/payments/sofort/accept-a-payment)
- [ACH Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
-
[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)
-
[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events)
- [authentication](https://docs.stripe.com/strong-customer-authentication)
- [Testing](https://docs.stripe.com/testing)