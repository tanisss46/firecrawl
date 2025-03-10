# Save Bacs Direct Debit bank details

## Learn how to use Checkout to save payment method details for future Bacs Direct Debit payments.

Use [Stripe Checkout](https://docs.stripe.com/payments/checkout) to collect Bacs
Direct Debit payment details in advance, with the final amount or payment date
determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases.
- Collecting surcharges after fulfilling a service.
- [Starting a free trial for a
subscription](https://docs.stripe.com/billing/subscriptions/trials).
[Set up
StripeServer-side](https://docs.stripe.com/payments/bacs-debit/save-bank-details#set-up-stripe)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

Use our official libraries for access to the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Create a
CustomerServer-side](https://docs.stripe.com/payments/bacs-debit/save-bank-details#create-customer)
To reuse a Bacs Direct Debit payment method for future payments, you must attach
it to a [Customer](https://docs.stripe.com/api/customers). Create a Customer
object when someone creates an account with you and associate the ID of the
Customer object with your own internal representation of a customer so you can
use the stored payment method details later. If you have an existing Customer
object, skip this step.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Create a Checkout
SessionClient-sideServer-side](https://docs.stripe.com/payments/bacs-debit/save-bank-details#create-checkout-session)
Before you can accept Direct Debit payments, your customer must provide their
bank account information and give permission to debit their account (also known
as a
[mandate](https://docs.stripe.com/payments/payment-methods/bacs-debit#mandates))
through Stripe Checkout.

Add a checkout button to your website that calls a server-side endpoint to
create a Checkout Session.

```
<html>
 <head>
 <title>Checkout</title>
 </head>
 <body>
 <form action="/create-checkout-session" method="POST">
 <button type="submit">Checkout</button>
 </form>
 </body>
</html>
```

Create a Checkout Session in `setup` mode to collect the required information.
After creating the Checkout Session, redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="bacs_debit" \
 -d mode=setup \
 -d customer={{CUSTOMER_ID}} \
-d success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
 -d cancel_url="https://example.com/cancel"
```

When your customer provides their payment method details, they’re redirected to
the `success_url`, a page on your website that informs them that their payment
method was saved successfully. Make the Session ID available on your success
page by including the `{CHECKOUT_SESSION_ID}` template variable in the
`success_url` as in the above example.

When your customer clicks on your logo in a Checkout Session without providing
their payment method details, Checkout redirects them back to your website by
navigating to the `cancel_url`. This is usually the page on your website that
the customer viewed prior to redirecting to Stripe Checkout.

#### Caution

Don’t rely on the redirect to the `success_url` alone for detecting payment
initiation, as:

- Malicious users could directly access the `success_url` without paying and
gain access to your goods or services.
- Customers may not always reach the `success_url` after a successful
payment—they might close their browser tab before the redirect occurs.

#### Note

The Bacs Direct Debit rules require that customers are sent an email
notification when payment details are collected. By default, these emails are
sent automatically by Stripe. You can also opt to [send your own Bacs
notifications](https://docs.stripe.com/payments/payment-methods/bacs-debit#debit-notifications).

[Retrieve the payment
methodServer-side](https://docs.stripe.com/payments/bacs-debit/save-bank-details#retrieve-payment-method)
After a customer submits their payment details, retrieve the
[PaymentMethod](https://docs.stripe.com/payments/payment-methods) object. A
[PaymentMethod](https://docs.stripe.com/api/payment_methods) stores the
customer’s bank account information for future payments. You can retrieve the
PaymentMethod synchronously using the `success_url` or asynchronously using
[webhooks](https://docs.stripe.com/webhooks).

The decision to retrieve the PaymentMethod synchronously or asynchronously
depends on your tolerance for dropoff, as customers might not always reach the
`success_url` after a successful payment (for example, it’s possible for them to
close their browser tab before the redirect occurs). Using webhooks prevents
your integration from experiencing this form of dropoff.

WebhooksSuccess URL
Handle `checkout.session.completed` webhooks, which contain a Session object. To
learn more, see [setting up webhooks](https://docs.stripe.com/webhooks). The
following example is a `checkout.session.completed` response.

```
{
 "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",
 "object": "event",
 "api_version": "2019-03-14",
 "created": 1561420781,
 "data": {
 "object": {
 "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",
 "object": "checkout.session",
 "billing_address_collection": null,
 "cancel_url": "https://example.com/cancel",
 "client_reference_id": null,
 "customer": null,
 "customer_email": null,
 "display_items": [],
 "mode": "setup",
 "setup_intent": "seti_1EzVO3HssDVaQm2PJjXHmLlM",
 "submit_type": null,
 "subscription": null,
 "success_url": "https://example.com/success"
 }
 },
 "livemode": false,
 "pending_webhooks": 1,
 "request": {
 "id": null,
 "idempotency_key": null
 },
 "type": "checkout.session.completed"
}
```

Note the value of the `setup_intent` key, which is the ID for the SetupIntent
created with the Checkout Session. A
[SetupIntent](https://docs.stripe.com/payments/setup-intents) is an object used
to set up the customer’s bank account information for future payments.
[Retrieve](https://docs.stripe.com/api/setup_intents/retrieve) the SetupIntent
object with the ID.

```
curl https://api.stripe.com/v1/setup_intents/seti_1EzVO3HssDVaQm2PJjXHmLlM \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

[Handle post-setup
eventsServer-side](https://docs.stripe.com/payments/bacs-debit/save-bank-details#handle-post-setup-events)
Once the Checkout Session completes, payment details are submitted to the bank
as a mandate.

The mandate can change at any time after you’ve collected it. This might be the
result of the customer instructing their bank to amend the mandate or because of
a change in the bank itself (for example, the customer changes to a different
one). Stripe sends the following events when the mandate changes:

Event nameDescription Can accept payments?`mandate.updated`Occurs whenever a
mandate is rejected, canceled, or reactivated by the Bacs network. Check
[mandate.status](https://docs.stripe.com/api/mandates/object#mandate_object-status)
to determine if the mandate can continue to be used.Yes, if the new status is
`active``payment_method.automatically_updated`Occurs when a customer’s bank
account details change.Yes
These events are available in the
[Dashboard](https://dashboard.stripe.com/events), but you can set up a
[webhook](https://docs.stripe.com/webhooks) to handle these programatically.

[Test the
integration](https://docs.stripe.com/payments/bacs-debit/save-bank-details#testing)
There are several test bank account numbers you can use in [test
mode](https://docs.stripe.com/keys#test-live-modes) to make sure this
integration is ready.

Sort code Account numberDescription10880000012345The payment succeeds and the
PaymentIntent transitions from `processing` to `succeeded`.10880090012345The
payment succeeds after three minutes and the PaymentIntent transitions from
`processing` to `succeeded`.10880033333335The payment is accepted but then
immediately fails with a `debit_not_authorized` failure code and the
PaymentIntent transitions from `processing` to `requires_payment_method`. The
Mandate becomes `inactive` and the PaymentMethod can not be used
again.10880093333335The payment fails after three minutes with a
`debit_not_authorized` failure code and the PaymentIntent transitions from
`processing` to `requires_payment_method`. The Mandate becomes `inactive` and
the PaymentMethod can not be used again.10880022222227The payment fails with an
`insufficient_funds` failure code and the PaymentIntent transitions from
`processing` to `requires_payment_method`. The Mandate remains `active` and the
PaymentMethod can be used again.10880092222227The payment fails after three
minutes with an `insufficient_funds` failure code and the PaymentIntent
transitions from `processing` to `requires_payment_method`. The Mandate remains
`active` and the PaymentMethod can be used again.10880055555559The payment
succeeds after three minutes and the PaymentIntent transitions from `processing`
to `succeeded`, but a dispute is immediately created.10880000033333Payment
Method creation succeeds, but the Mandate is refused by the customer’s bank and
immediately transitions to inactive.10880000044444The request to set up Bacs
Direct Debit fails immediately due to an invalid account number and the customer
is prompted to update their information before submitting. Payment details are
not collected.10880034343434The payment fails with a
`charge_exceeds_source_limit` failure code due to the payment amount causing the
account to exceed its weekly payment volume limit.10880012121212The payment
fails with a `charge_exceeds_weekly_limit` failure code due to the payment
amount exceeding the account’s transaction volume limit.
You can test using any of the account numbers provided above. However, because
Bacs Direct Debit payments take several days to process, use the test account
numbers that operate on a three-minute delay to better simulate the behavior of
live payments.

#### Note

By default, Stripe automatically sends
[emails](https://docs.stripe.com/payments/payment-methods/bacs-debit#debit-notifications)
to the customer when payment details are initially collected and each time a
debit will be made on their account. These notifications aren’t sent in
testmode.

[Use the payment method for future
paymentsServer-side](https://docs.stripe.com/payments/bacs-debit/save-bank-details#charge-later)
After you set up a [PaymentMethod](https://docs.stripe.com/api/payment_methods),
you can accept future Bacs Direct Debit payments by creating and confirming a
[PaymentIntent](https://docs.stripe.com/payments/payment-intents).

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="bacs_debit" \
 -d payment_method={{PAYMENT_METHOD_ID}} \
 -d customer={{CUSTOMER_ID}} \
 -d confirm=true \
 -d amount=100 \
 -d currency=gbp
```

## Links

- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Starting a free trial for a
subscription](https://docs.stripe.com/billing/subscriptions/trials)
- [Register now](https://dashboard.stripe.com/register)
- [Customer](https://docs.stripe.com/api/customers)
- [contact](https://stripe.com/contact/sales)
-
[mandate](https://docs.stripe.com/payments/payment-methods/bacs-debit#mandates)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
-
[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})
- [https://example.com/cancel](https://example.com/cancel)
- [send your own Bacs
notifications](https://docs.stripe.com/payments/payment-methods/bacs-debit#debit-notifications)
- [PaymentMethod](https://docs.stripe.com/payments/payment-methods)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [webhooks](https://docs.stripe.com/webhooks)
- [https://example.com/success](https://example.com/success)
- [SetupIntent](https://docs.stripe.com/payments/setup-intents)
- [Retrieve](https://docs.stripe.com/api/setup_intents/retrieve)
-
[mandate.status](https://docs.stripe.com/api/mandates/object#mandate_object-status)
- [Dashboard](https://dashboard.stripe.com/events)
- [test mode](https://docs.stripe.com/keys#test-live-modes)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)