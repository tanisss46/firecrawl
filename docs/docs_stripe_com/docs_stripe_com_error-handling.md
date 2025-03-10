# Error handling

## Catch and respond to declines, invalid data, network problems, and more.

RubyPythonPHPJavaNode.jsGo.NET
Stripe offers many kinds of errors. They can reflect external events, like
declined payments and network interruptions, or code problems, like invalid API
calls.

To handle errors, use some or all of the techniques in the table below. No
matter what technique you use, you can follow up with our [recommended responses
for each error type](https://docs.stripe.com/error-handling#error-types).

TechniquePurposeWhen needed[Catch
exceptions](https://docs.stripe.com/error-handling#catch-exceptions)Recover when
an API call can’t continueAlways[Monitor
webhooks](https://docs.stripe.com/error-handling#monitor-webhooks)React to
notifications from StripeSometimes[Get stored information about
failures](https://docs.stripe.com/error-handling#use-stored-information)Investigate
past problems and support other techniquesSometimes
## Catch exceptions

If an immediate problem prevents an API call from continuing, the Stripe Ruby
library raises an exception. It’s a best practice to catch and handle
exceptions.

To catch an exception, use Ruby’s `rescue` keyword. Catch `Stripe::StripeError`
or its subclasses to handle Stripe-specific exceptions only. Each subclass
represents a different kind of exception. When you catch an exception, you can
[use its class to choose a
response](https://docs.stripe.com/error-handling#error-types).

```
require 'stripe'

Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

def example_function(params)
 begin
 Stripe::PaymentIntent.create(params)
 rescue Stripe::CardError => e
 puts "A payment error occurred: #{e.error.message}"
 rescue Stripe::InvalidRequestError => e
 puts "An invalid request occurred."
 rescue Stripe::StripeError => e
 puts "Another problem occurred, maybe unrelated to Stripe."
 else
 puts "No error."
 end
end
```

After setting up exception handling, test it on a variety of data, including
[test cards](https://docs.stripe.com/testing), to simulate different payment
outcomes.

Error to trigger:Invalid requestCard errorNo error
```
example_function(
 # The required parameter currency is missing,
 amount: 2000,
 confirm: true,
 payment_method: 'pm_card_visa',
)
```

```
An invalid request occurred.

```

## Monitor webhooks

Stripe notifies you about many kinds of problems using
[webhooks](https://docs.stripe.com/webhooks). This includes problems that don’t
follow immediately after an API call. For example:

- You lose a dispute.
- A recurring payment fails after months of success.
- Your frontend [confirms](https://docs.stripe.com/api/payment_intents/confirm)
a payment, but goes offline before finding out the payment fails. (The backend
still receives webhook notification, even though it wasn’t the one to make the
API call.)

You don’t need to handle every webhook event type. In fact, some integrations
don’t handle any.

In your webhook handler, start with the basic steps from the [webhook
builder](https://docs.stripe.com/webhooks/quickstart): get an event object and
use the event type to find out what happened. Then, if the event type indicates
an error, follow these extra steps:

- Access
[event.data.object](https://docs.stripe.com/api/events/object#event_object-data-object)
to retrieve the affected object.
- [Use stored
information](https://docs.stripe.com/error-handling#use-stored-information) on
the affected object to gain context, including an error object.
- [Use its type to choose a
response](https://docs.stripe.com/error-handling#error-types).

```
require 'stripe'
require 'sinatra'
post '/webhook' do
 payload = request.body.read
 data = JSON.parse(payload, symbolize_names: true)

 # Get the event object
 event = Stripe::Event.construct_from(data)

 # Use the event type to find out what happened
 case event.type
 when 'payment_intent.payment_failed'

 # Get the object affected
 payment_intent = event.data.object

 # Use stored information to get an error object
 e = payment_intent.last_payment_error

 # Use its type to choose a response
 case e.type
 when 'card_error'
 puts "A payment error occurred: #{e.message}"
 when 'invalid_request'
 puts "An invalid request occurred."
 else
 puts "Another problem occurred, maybe unrelated to Stripe."
 end
 end

 content_type 'application/json'
 {
 status: 'success'
 }.to_json
end
```

To test how your integration responds to webhook events, you can [trigger
webhook events locally](https://docs.stripe.com/webhooks#test-webhook). After
completing the setup steps at that link, trigger a failed payment to see the
resulting error message.

```
stripe trigger payment_intent.payment_failed
```

```
A payment error occurred: Your card was declined.
```

## Get stored information about failures

Many objects store information about failures. That means that if something
already went wrong, you can retrieve the object and examine it to learn more. In
many cases, stored information is in the form of an error object, and you can
[use its type to choose a
response](https://docs.stripe.com/error-handling#error-types).

For instance:

- Retrieve a specific payment intent.
- Check if it experienced a payment error by determining if
[last_payment_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error)
is empty.
- If it did, log the error, including its type and the affected object.

```
require 'stripe'
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

payment_intent = Stripe::PaymentIntent.retrieve('{{PAYMENT_INTENT_ID}}')
e = payment_intent.last_payment_error
if !e.nil?
 puts "PaymentIntent #{payment_intent.id} experienced a #{e.type}."
end
```

Here are common objects that store information about failures.

ObjectAttributeValues[Payment
Intent](https://docs.stripe.com/api/payment_intents)`last_payment_error`[An
error
object](https://docs.stripe.com/error-handling#work-with-error-objects)[Setup
Intent](https://docs.stripe.com/api/setup_intents)`last_setup_error`[An error
object](https://docs.stripe.com/error-handling#work-with-error-objects)[Invoice](https://docs.stripe.com/api/invoices)`last_finalization_error`[An
error
object](https://docs.stripe.com/error-handling#work-with-error-objects)[Setup
Attempt](https://docs.stripe.com/api/setup_attempts)`setup_error`[An error
object](https://docs.stripe.com/error-handling#work-with-error-objects)[Payout](https://docs.stripe.com/api/payouts)`failure_code`[A
payout failure
code](https://docs.stripe.com/api/payouts/failures)[Refund](https://docs.stripe.com/api/refunds)`failure_reason`[A
refund failure
code](https://docs.stripe.com/api/refunds/object#refund_object-failure_reason)
To test code that uses stored information about failures, you often need to
simulate failed transactions. You can often do this using [test
cards](https://docs.stripe.com/testing) or test bank numbers. For example:

- [Simulate a declined
payment](https://docs.stripe.com/testing#declined-payments), for creating failed
Charges, PaymentIntents, SetupIntents, and so on.
- [Simulate a failed
payout](https://docs.stripe.com/connect/testing#account-numbers).
- [Simulate a failed refund](https://docs.stripe.com/testing#refunds).

## Types of error and responses

In the Stripe Ruby library, error objects belong to `stripe.error.StripeError`
and its subclasses. Use the documentation for each class for advice on
responding.

Name
Class

DescriptionPayment error
[Stripe::CardError](https://docs.stripe.com/error-handling#payment-errors)

An error occurred during a payment, involving one of these situations:- [Payment
blocked for suspected
fraud](https://docs.stripe.com/error-handling#payment-blocked)
- [Payment declined by the
issuer](https://docs.stripe.com/error-handling#payment-declined).
- [Other payment
errors](https://docs.stripe.com/error-handling#other-payment-errors).
Invalid request error

[Stripe::InvalidRequestError](https://docs.stripe.com/error-handling#invalid-request-errors)

You made an API call with the wrong parameters, in the wrong state, or in an
invalid way.

Connection error

[Stripe::APIConnectionError](https://docs.stripe.com/error-handling#connection-errors)

There was a network problem between your server and Stripe.API error
[Stripe::APIError](https://docs.stripe.com/error-handling#api-errors)

Something went wrong on Stripe’s end. (These are rare.)Authentication error

[Stripe::AuthenticationError](https://docs.stripe.com/error-handling#authentication-errors)

Stripe can’t authenticate you with the information provided.Idempotency error

[Stripe::IdempotencyError](https://docs.stripe.com/error-handling#idempotency-errors)

You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests)
for something unexpected, like replaying a request but passing different
parameters.Permission error

[Stripe::PermissionError](https://docs.stripe.com/error-handling#permission-errors)

The API key used for this request does not have the necessary permissions.Rate
limit error

[Stripe::RateLimitError](https://docs.stripe.com/error-handling#rate-limit-errors)

You made too many API calls in too short a time.Signature verification error

[Stripe::SignatureVerificationError](https://docs.stripe.com/error-handling#signature-verification-errors)

You’re using [webhook](https://docs.stripe.com/webhooks) [signature
verification](https://docs.stripe.com/webhooks#verify-events) and couldn’t
verify that a webhook event is authentic.
## Payment errors

Payment errors—sometimes called “card errors” for historical reasons—cover a
wide range of common problems. They come in three categories:

- [Payment blocked for suspected
fraud](https://docs.stripe.com/error-handling#payment-blocked)
- [Payment declined by the
issuer](https://docs.stripe.com/error-handling#payment-declined)
- [Other payment
errors](https://docs.stripe.com/error-handling#other-payment-errors)

To distinguish these categories or get more information about how to respond,
consult the [error code](https://docs.stripe.com/error-codes), [decline
code](https://docs.stripe.com/declines/codes), and [charge
outcome](https://docs.stripe.com/api/charges/object#charge_object-outcome).

(To find the charge outcome from an error object, first get the [Payment Intent
that’s involved](https://docs.stripe.com/api/errors#errors-payment_intent) and
the [latest Charge it
created](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge).
See the example below for a demonstration.)

```
require 'stripe'
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

def example_function(params)
 begin
 Stripe::PaymentIntent.create(params)
 rescue Stripe::CardError => e
 charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
 if charge.outcome.type == 'blocked'
 puts 'Payment blocked for suspected fraud.'
 elsif e.code == 'card_declined'
 puts 'Payment declined by the issuer.'
 elsif e.code == 'expired_card'
 puts 'Card expired.'
 else
 puts 'Other card error.'
 end
 end
end
```

Users on API version [2022-08-01](https://docs.stripe.com/upgrades#2022-08-01)
or older:

(To find the charge outcome from an error object, first get the [Payment Intent
that’s involved](https://docs.stripe.com/api/errors#errors-payment_intent) and
the [latest Charge it
created](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-charges-data).
See the example below for a demonstration.)

```
require 'stripe'
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

def example_function(params)
 begin
 Stripe::PaymentIntent.create(params)
 rescue Stripe::CardError => e
 if e.error.payment_intent.charges.data[0].outcome.type == 'blocked'
 puts 'Payment blocked for suspected fraud.'
 elsif e.code == 'card_declined'
 puts 'Payment declined by the issuer.'
 elsif e.code == 'expired_card'
 puts 'Card expired.'
 else
 puts 'Other card error.'
 end
 end
end
```

You can trigger some common kinds of payment error with test cards. Consult
these lists for options:

- [Simulating payments blocked for fraud
risk](https://docs.stripe.com/testing#fraud-prevention)
- [Simulating declined payments and other card
errors](https://docs.stripe.com/testing#declined-payments)

The test code below demonstrates a few possibilities.

Error to trigger:Blocked for suspected fraudDeclined by the issuerCard
expiredOther card error
```
example_function(
 currency: 'usd',
 amount: 2000,
 confirm: true,
 payment_method: 'pm_card_radarBlock',
)
```

```
Payment blocked for suspected fraud.

```

### Payment blocked for suspected fraud

Type
`Stripe::CardError`

Codes
```
charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
charge.outcome.type == 'blocked'
```

Codes
`e.error.payment_intent.charges.data[0].outcome.type == 'blocked'`

ProblemStripe’s fraud prevention system, [Radar](https://docs.stripe.com/radar),
blocked the payment
**Solutions**

This error can occur when your integration is working correctly. Catch it and
prompt the customer for a different payment method.

To block fewer legitimate payments, try these:

- [Optimize your Radar integration](https://docs.stripe.com/radar/integration)
to collect more detailed information.
- Use [Payment Links](https://docs.stripe.com/payment-links),
[Checkout](https://docs.stripe.com/payments/checkout), or [Stripe
Elements](https://docs.stripe.com/payments/elements) for prebuilt optimized form
elements.

[Radar for Fraud Teams](https://docs.stripe.com/radar) customers have these
additional options:

- To exempt a specific payment, add it to your allowlist. Radar for Fraud Teams
- To change your risk tolerance, adjust your [risk
settings](https://docs.stripe.com/radar/risk-settings). Radar for Fraud Teams
- To change the criteria for blocking a payment, use [custom
rules](https://docs.stripe.com/radar/rules). Radar for Fraud Teams

You can test your integration’s settings with [test cards that simulate
fraud](https://docs.stripe.com/radar/testing). If you have custom Radar rules,
follow the testing advice in the [Radar
documentation](https://docs.stripe.com/radar/testing).

### Payment declined by the issuer

Type
`Stripe::CardError`

Codes
`e.error.code == "card_declined"`

ProblemThe card issuer declined the payment.
**Solutions**

This error can occur when your integration is working correctly. It reflects an
action by the issuer, and that action may be legitimate. Use the decline code to
determine what next steps are appropriate. See the [documentation on decline
codes](https://docs.stripe.com/declines/codes) for appropriate responses to each
code.

You can also:

- [Follow recommendations to reduce issuer
declines](https://docs.stripe.com/declines/card#reducing-bank-declines).
- Use [Payment Links](https://docs.stripe.com/payment-links),
[Checkout](https://docs.stripe.com/payments/checkout), or [Stripe
Elements](https://docs.stripe.com/payments/elements) for prebuilt form elements
that implement those recommendations.

Test how your integration handles declines with [test cards that simulate
successful and declined payments](https://docs.stripe.com/radar/testing).

### Other payment errors

Type
`Stripe::CardError`

ProblemAnother payment error occurred.SolutionsThis error can occur when your
integration is working correctly. Use the error code to determine what next
steps are appropriate. See the [documentation on error
codes](https://docs.stripe.com/error-codes) for appropriate responses to each
code.
## Invalid request errors

Type 
`Stripe::InvalidRequestError`

Problem You made an API call with the wrong parameters, in the wrong state, or
in an invalid way.Solutions In most cases, the problem is with the request
itself. Either its parameters are invalid or it can’t be carried out in your
integration’s current state.- Consult the [error code
documentation](https://docs.stripe.com/error-codes) for details on the problem.
- For convenience, you can follow the link at for documentation about the error
code.
- If the error involves a specific parameter, use to determine which one.

## Connection errors

Type
`Stripe::APIConnectionError`

ProblemThere was a network problem between your server and Stripe.
**Solutions**

Treat the result of the API call as indeterminate. That is, don’t assume that it
succeeded or that if failed.

To find out if it succeeded, you can:

- Retrieve the relevant object from Stripe and check its status.
- Listen for webhook notification that the operation succeeded or failed.

To help recover from connection errors, you can:

- When creating or updating an object, use an [idempotency
key](https://docs.stripe.com/api/idempotent_requests). Then, if a connection
error occurs, you can safely repeat the request without risk of creating a
second object or performing the update twice. Repeat the request with the same
idempotency key until you receive a clear success or failure. For advanced
advice on this strategy, see [Low-level error
handling](https://docs.stripe.com/error-low-level#idempotency).
- Turn on [automatic
retries.](https://docs.stripe.com/error-handling#automatic-retries) Then, Stripe
generates idempotency keys for you, and repeats requests for you when it is safe
to do so.

This error can mask others. It’s possible that when the connection error
resolves, some other error becomes apparent. Check for errors in all of these
solutions just as you would in the original request.

## API errors

Type
`Stripe::APIError`

ProblemSomething went wrong on Stripe’s end. (These are rare.)
**Solutions**

Treat the result of the API call as indeterminate. That is, don’t assume that it
succeeded or that it failed.

Rely on [webhooks](https://docs.stripe.com/webhooks) for information about the
outcome. Whenever possible, Stripe fires webhooks for any new objects we create
as we solve a problem.

To set your integration up for maximum robustness in unusual situations, see
[this advanced discussion of server
errors.](https://docs.stripe.com/error-low-level#server-errors)

## Authentication errors

Type
`Stripe::AuthenticationError`

ProblemStripe can’t authenticate you with the information provided.Solutions-
Use the correct [API key](https://docs.stripe.com/keys).
- Make sure you aren’t using a key that you [“rolled” or
revoked](https://docs.stripe.com/keys#rolling-keys).

## Idempotency errors

Type
`Stripe::IdempotencyError`

ProblemYou used an [idempotency
key](https://docs.stripe.com/api/idempotent_requests) for something unexpected,
like replaying a request but passing different parameters.Solutions- After you
use an idempotency key, only reuse it for identical API calls.
- Use idempotency keys under the limit of 255 characters.

## Permission errors

Type
`Stripe::PermissionError`

ProblemThe API key used for this request does not have the necessary
permissions.Solutions- Are you using a [restricted API
key](https://docs.stripe.com/keys#limit-access) for a service it doesn’t have
access to?
- Are you performing an action in the Dashboard while logged in as a [user
role](https://docs.stripe.com/get-started/account/teams/roles) that lacks
permission?

## Rate limit errors

Type
`Stripe::RateLimitError`

ProblemYou made too many API calls in too short a time.Solutions- If a single
API call triggers this error, wait and try it again.
- To handle rate-limiting automatically, retry the API call after a delay, and
increase the delay exponentially if the error continues. See the documentation
on [rate limits](https://docs.stripe.com/rate-limits) for further advice.
- If you anticipate a large increase in traffic and want to request an increased
rate limit, [contact support](https://support.stripe.com/) in advance.

## Signature verification errors

Type
`Stripe::SignatureVerificationError`

ProblemYou’re using [webhook](https://docs.stripe.com/webhooks) [signature
verification](https://docs.stripe.com/webhooks#verify-events) and couldn’t
verify that a webhook event is authentic.
**Solutions**

This error can occur when your integration is working correctly. If you use
webhook signature verification and a third party attempts to send you a fake or
malicious webhook, then verification fails and this error is the result. Catch
it and respond with a `400 Bad Request` status code.

If you receive this error when you shouldn’t—for instance, with webhooks that
you know originate with Stripe—then see the documentation on [checking webhook
signatures](https://docs.stripe.com/webhooks#verify-events) for further advice.
In particular, make sure you’re using the correct endpoint secret. This is
different from your API key.

## Links

- [Low-level exception handling](https://docs.stripe.com/error-low-level)
- [Error](https://docs.stripe.com/api/errors)
- [test cards](https://docs.stripe.com/testing)
- [webhooks](https://docs.stripe.com/webhooks)
- [confirms](https://docs.stripe.com/api/payment_intents/confirm)
- [webhook builder](https://docs.stripe.com/webhooks/quickstart)
-
[event.data.object](https://docs.stripe.com/api/events/object#event_object-data-object)
- [trigger webhook events
locally](https://docs.stripe.com/webhooks#test-webhook)
-
[last_payment_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error)
- [Payment Intent](https://docs.stripe.com/api/payment_intents)
- [Setup Intent](https://docs.stripe.com/api/setup_intents)
- [Invoice](https://docs.stripe.com/api/invoices)
- [Setup Attempt](https://docs.stripe.com/api/setup_attempts)
- [Payout](https://docs.stripe.com/api/payouts)
- [A payout failure code](https://docs.stripe.com/api/payouts/failures)
- [Refund](https://docs.stripe.com/api/refunds)
- [A refund failure
code](https://docs.stripe.com/api/refunds/object#refund_object-failure_reason)
- [Simulate a declined
payment](https://docs.stripe.com/testing#declined-payments)
- [Simulate a failed
payout](https://docs.stripe.com/connect/testing#account-numbers)
- [Simulate a failed refund](https://docs.stripe.com/testing#refunds)
- [idempotency key](https://docs.stripe.com/api/idempotent_requests)
- [signature verification](https://docs.stripe.com/webhooks#verify-events)
- [error code](https://docs.stripe.com/error-codes)
- [decline code](https://docs.stripe.com/declines/codes)
- [charge
outcome](https://docs.stripe.com/api/charges/object#charge_object-outcome)
- [Payment Intent that’s
involved](https://docs.stripe.com/api/errors#errors-payment_intent)
- [latest Charge it
created](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge)
- [2022-08-01](https://docs.stripe.com/upgrades#2022-08-01)
- [latest Charge it
created](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-charges-data)
- [Simulating payments blocked for fraud
risk](https://docs.stripe.com/testing#fraud-prevention)
- [Radar](https://docs.stripe.com/radar)
- [Optimize your Radar integration](https://docs.stripe.com/radar/integration)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [risk settings](https://docs.stripe.com/radar/risk-settings)
- [custom rules](https://docs.stripe.com/radar/rules)
- [test cards that simulate fraud](https://docs.stripe.com/radar/testing)
- [Follow recommendations to reduce issuer
declines](https://docs.stripe.com/declines/card#reducing-bank-declines)
- [Low-level error
handling](https://docs.stripe.com/error-low-level#idempotency)
- [this advanced discussion of server
errors.](https://docs.stripe.com/error-low-level#server-errors)
- [API key](https://docs.stripe.com/keys)
- [“rolled” or revoked](https://docs.stripe.com/keys#rolling-keys)
- [restricted API key](https://docs.stripe.com/keys#limit-access)
- [user role](https://docs.stripe.com/get-started/account/teams/roles)
- [rate limits](https://docs.stripe.com/rate-limits)
- [contact support](https://support.stripe.com/)