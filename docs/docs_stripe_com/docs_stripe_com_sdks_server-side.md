# Introduction to server-side SDKs

## Learn how to install and use the Stripe server-side SDKs.

The Stripe server-side SDKs reduce the amount of work required to use our REST
APIs. Stripe-maintained SDKs are available for Ruby, PHP, Java, Python, Node,
.NET and Go. [Community libraries](https://docs.stripe.com/sdks/community) are
also available for other server languages.

## Installation and setup

Select your language in the language selector below, then follow the
instructions to install the SDK.

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

After completing the installation, you need to initialize Stripe:

```
require 'stripe'
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
```

## Send API requests

You can manipulate objects with the Stripe API in six primary ways: create,
update, delete, retrieve, list, and search. The following examples show each of
the six ways using the `Customer` object:

CreateUpdateDeleteRetrieveListSearch
Create a customer named John Doe.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="John Doe"
```

API requests can contain different types of parameters. For example, here’s how
to create a customer with a `name` (a string), `address` (an object), and
`preferred_locales` (a list):

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="John Doe" \
 -d "address[country]"=US \
 -d "address[city]"="San Fransisco" \
 -d "preferred_locales[]"=EN \
 -d "preferred_locales[]"=FR
```

When updating an object, you can clear some of its properties. For dynamically
typed languages, send an empty string. For strongly typed languages, use
specific constants. For example, here’s how to clear the `name` (a string) and
`metadata` (a hash of key-value pairs) of a customer:

```
customer = Stripe::Customer.update('{{CUSTOMER_ID}}', {
 name: '',
 metadata: '',
})
```

This example clears all metadata, but you can also clear individual keys. Learn
more about managing metadata in our [metadata
guide](https://docs.stripe.com/metadata).

## Access the API response

Every time you make an API request, Stripe sends you back a response.

If you create, retrieve, or update an object, you get back the object itself:

```
{
 "id": "pi_001",
 "object": "payment_intent",
 "amount": 1099,
 "currency": "usd",
 /* ... */
}
```

Use a variable to access the properties of that object:

```
paymentIntent = Stripe::PaymentIntent.retrieve('{{PAYMENT_INTENT_ID}}')
puts paymentIntent.amount
```

When listing or searching for objects, you get back a `List` object containing a
`data` array with the objects requested:

```
{
 "object": "list",
 "data": [
 {
 "id": "pi_003",
 "object": "payment_intent",
 "amount": 4200,
 "currency": "usd",
 /* ... */
 },
 {
 "id": "pi_002",
 "object": "payment_intent",
 "amount": 2100,
 "currency": "usd",
 "payment_method_types": [ "link" ],
 /* ... */
 }
 ],
 "has_more": true,
 "url": "/v1/payment_intents"
}
```

Use a loop on the `data` array to access the properties of each object:

```
paymentIntentList = Stripe::PaymentIntent.list({ limit: 3 })
for pi in paymentIntentList.data do
 puts pi.amount
end
```

You could also use
[auto-pagination](https://docs.stripe.com/api/pagination/auto) to iterate over
all the results.

## Expanding responses

Some properties are expandable or includable, meaning you can return them by
using the `expand` parameter. For example:

- Retrieve a PaymentIntent and expand its associated PaymentMethod.
```
curl -G https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=payment_method
```
- Retrieve a Checkout Session and include the `line_items` property.
```
curl -G https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=line_items
```

Learn more about [expanding responses](https://docs.stripe.com/expand).

## Retrieve the request ID

Each API request has a unique request ID (`req_xxx`) associated with it. You can
use it to inspect the request in the Dashboard to see the parameters Stripe
received, or to share it with Stripe support when you need to resolve an issue.

You can find the IDs in your [Dashboard
logs](https://dashboard.stripe.com/test/workbench/logs), or directly with code
like this:

```
customer = Stripe::Customer.create({ name: 'John Doe', })
puts customer.last_response.request_id
```

## Set additional request options

When sending API requests, you can set additional request options to:

- [Set a specific API version](https://docs.stripe.com/sdks/set-version).
- [Make requests on your connected
accounts](https://docs.stripe.com/connect/authentication).
- [Provide idempotency keys](https://docs.stripe.com/api/idempotent_requests).

## Error handling

Each server SDK interprets error responses from the Stripe API as exception
types, so you don’t need to parse the response status yourself. Use error
handling conventions appropriate for each language to handle those errors.

```
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
```

Learn more about [error handling](https://docs.stripe.com/error-handling).

## Private preview features

Stripe regularly launches private preview features that introduce new properties
or parameters that aren’t immediately public. Dynamically-typed SDKs (PHP, Node,
Ruby, Python) automatically support these. For strongly-typed SDKs (Java, .NET,
Go), use the code below, unless they’re supported in a beta release.

Send undocumented parameters:

```
CustomerCreateParams params =
 CustomerCreateParams.builder()
 .setEmail("jenny.rosen@example.com")
 .putExtraParam("secret_feature_enabled", "true")
 .build();

client.customers().create(params);
```

Access undocumented fields:

```
final Customer customer = client.customers().retrieve("cus_1234");
Boolean featureEnabled = customer.getRawJsonObject()
 .getAsJsonPrimitive("secret_feature_enabled")
 .getAsBoolean();
```

## Source code

The source code for each of our server SDKs is available on GitHub:

LanguageRepositoryRuby[stripe-ruby](https://github.com/stripe/stripe-ruby)PHP[stripe-php](https://github.com/stripe/stripe-php)Java[stripe-Java](https://github.com/stripe/stripe-java)Node[stripe-node](https://github.com/stripe/stripe-node)Python[stripe-python](https://github.com/stripe/stripe-python).NET[stripe-dotnet](https://github.com/stripe/stripe-dotnet)Go[stripe-go](https://github.com/stripe/stripe-go)
## Client and service patterns

For some SDKs, we’ve introduced a client and service pattern that changes the
way you perform operations. This new service-based pattern allows you to create
mocks without static methods and enables multiple client instances to operate
simultaneously with distinct configuration.

If you’re comparing code targeting older versions of these libraries with
resource-based patterns, the calls might look different.

SDKClient/Services releaseTransition guide`stripe-php`7.33.0[GitHub
Wiki](https://github.com/stripe/stripe-php/wiki/Migration-to-StripeClient-and-services-in-7.33.0)`stripe-python`8.0.0[GitHub
Wiki](https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v8-(StripeClient))
## Beta versions

We offer beta SDKs that are identifiable by the `beta` or `b` filename suffix,
such as `5.1.0-beta.3` or `5.1.0b3`. They give you access to products and
features in development, and allow you to share feedback with us before their
general availability.

Access the beta SDK releases through the `readme.md` file of the respective
GitHub repository.

## Links

- [Community libraries](https://docs.stripe.com/sdks/community)
- [metadata guide](https://docs.stripe.com/metadata)
- [auto-pagination](https://docs.stripe.com/api/pagination/auto)
- [expanding responses](https://docs.stripe.com/expand)
- [Dashboard logs](https://dashboard.stripe.com/test/workbench/logs)
- [Set a specific API version](https://docs.stripe.com/sdks/set-version)
- [Make requests on your connected
accounts](https://docs.stripe.com/connect/authentication)
- [Provide idempotency keys](https://docs.stripe.com/api/idempotent_requests)
- [error handling](https://docs.stripe.com/error-handling)
- [stripe-ruby](https://github.com/stripe/stripe-ruby)
- [stripe-php](https://github.com/stripe/stripe-php)
- [stripe-Java](https://github.com/stripe/stripe-java)
- [stripe-node](https://github.com/stripe/stripe-node)
- [stripe-python](https://github.com/stripe/stripe-python)
- [stripe-dotnet](https://github.com/stripe/stripe-dotnet)
- [stripe-go](https://github.com/stripe/stripe-go)
- [GitHub
Wiki](https://github.com/stripe/stripe-php/wiki/Migration-to-StripeClient-and-services-in-7.33.0)
- [GitHub
Wiki](https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v8-(StripeClient))