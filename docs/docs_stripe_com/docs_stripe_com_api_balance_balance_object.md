# [API Reference](https://docs.stripe.com/api)

The Stripe API is organized around
[REST](http://en.wikipedia.org/wiki/Representational_State_Transfer). Our API
has predictable resource-oriented URLs, accepts
[form-encoded](https://en.wikipedia.org/wiki/POST_(HTTP)#Use_for_submitting_web_forms)
request bodies, returns [JSON-encoded](http://www.json.org/) responses, and uses
standard HTTP response codes, authentication, and verbs.

You can use the Stripe API in test mode, which doesn’t affect your live data or
interact with the banking networks. The API key you use to
[authenticate](https://docs.stripe.com/api/authentication) the request
determines whether the request is live mode or test mode.

The Stripe API doesn’t support bulk updates. You can work on only one object per
request.

The Stripe API differs for every account as we release new
[versions](https://docs.stripe.com/api/versioning) and tailor functionality.
[Log
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fapi%2Fbalance%2Fbalance_object)
to see docs with your test key and data.

## Just getting started?

Check out our [development
quickstart](https://docs.stripe.com/development/quickstart) guide.

## Not a developer?

Use Stripe’s [no-code options](https://docs.stripe.com/payments/no-code) or apps
from [our partners](https://stripe.partners/) to get started with Stripe and to
do more with your Stripe account—no code required.

Base URL
```
https://api.stripe.com
```

Client LibrariesRubyPythonPHPJavaNode.jsGo.NET
By default, the Stripe API Docs demonstrate using curl to interact with the API
over HTTP. Select one of our official [client
libraries](https://docs.stripe.com/libraries) to see examples in code.

# [Authentication](https://docs.stripe.com/api/authentication)

The Stripe API uses [API keys](https://docs.stripe.com/keys) to authenticate
requests. You can view and manage your API keys in [the Stripe
Dashboard](https://dashboard.stripe.com/login?redirect=/apikeys).

Test mode secret keys have the prefix `sk_test_` and live mode secret keys have
the prefix `sk_live_`. Alternatively, you can use [restricted API
keys](https://docs.stripe.com/keys#limit-access) for granular permissions.

Your API keys carry many privileges, so be sure to keep them secure! Do not
share your secret API keys in publicly accessible areas such as GitHub,
client-side code, and so forth.

All API requests must be made over
[HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). Calls made over plain HTTP
will fail. API requests without authentication will also fail.

Authenticated RequestServer-side languageStripe
CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/charges \ -u
sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:# The colon
prevents curl from asking for a password.
```

Your API Key
A sample test API key is included in all the examples here, so you can test any
example right away. Do not submit any personally identifiable information in
requests made with this key.

To test requests using your account, replace the sample API key with your actual
API key or [sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fapi%2Fbalance%2Fbalance_object).

# [Connected Accounts](https://docs.stripe.com/api/connected-accounts)

To act as connected accounts, clients can issue requests using the
`Stripe-Account` special header. Make sure that this header contains a Stripe
account ID, which usually starts with the `acct_` prefix.

The value is set per-request as shown in the adjacent code sample. Methods on
the returned object reuse the same account ID.

- Related guide: [Making API calls for connected
accounts](https://docs.stripe.com/connect/authentication)
Per-Request AccountServer-side languageStripe
CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/charges/ch_3LmjFA2eZvKYlo2C09TLIsrw \ -u
sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2: \ -H
"Stripe-Account: acct_1032D82eZvKYlo2C" \ -G
```

# [Errors](https://docs.stripe.com/api/errors)

Stripe uses conventional HTTP response codes to indicate the success or failure
of an API request. In general: Codes in the `2xx` range indicate success. Codes
in the `4xx` range indicate an error that failed given the information provided
(e.g., a required parameter was omitted, a charge failed, etc.). Codes in the
`5xx` range indicate an error with Stripe’s servers (these are rare).

Some `4xx` errors that could be handled programmatically (e.g., a card is
[declined](https://docs.stripe.com/declines)) include an [error
code](https://docs.stripe.com/error-codes) that briefly explains the error
reported.

### Attributes

- #### codenullable string

For some errors that could be handled programmatically, a short string
indicating the [error code](https://docs.stripe.com/error-codes) reported.
- #### decline_codenullable string

For card errors resulting from a card issuer decline, a short string indicating
the [card issuer’s reason for the
decline](https://docs.stripe.com/declines#issuer-declines) if they provide one.
- #### messagenullable string

A human-readable message providing more details about the error. For card
errors, these messages can be shown to your users.
- #### paramnullable string

If the error is parameter-specific, the parameter related to the error. For
example, you can use this to display a message near the correct form field.
- #### payment_intentnullable object

The [PaymentIntent object](https://docs.stripe.com/api/payment_intents/object)
for errors returned on a request involving a PaymentIntent.
- #### typeenum

The type of error returned. One of `api_error`, `card_error`,
`idempotency_error`, or `invalid_request_error`

Possible enum
values`api_error``card_error``idempotency_error``invalid_request_error`

### MoreExpand all

- #### advice_codenullable string
- #### chargenullable string
- #### doc_urlnullable string
- #### network_advice_codenullable string
- #### network_decline_codenullable string
- #### payment_methodnullable object
- #### payment_method_typenullable string
- #### request_log_urlnullable string
- #### setup_intentnullable object
- #### sourcenullable object
HTTP Status Code Summary200OKEverything worked as expected.400Bad RequestThe
request was unacceptable, often due to missing a required
parameter.401UnauthorizedNo valid API key provided.402Request FailedThe
parameters were valid but the request failed.403ForbiddenThe API key doesn’t
have permissions to perform the request.404Not FoundThe requested resource
doesn’t exist.409ConflictThe request conflicts with another request (perhaps due
to using the same idempotent key).429Too Many RequestsToo many requests hit the
API too quickly. We recommend an exponential backoff of your requests.500, 502,
503, 504Server ErrorsSomething went wrong on Stripe’s end. (These are
rare.)Error Types`api_error`API errors cover any other type of problem (e.g., a
temporary problem with Stripe’s servers), and are extremely
uncommon.`card_error`Card errors are the most common type of error you should
expect to handle. They result when the user enters a card that can’t be charged
for some reason.`idempotency_error`Idempotency errors occur when an
`Idempotency-Key` is re-used on a request that does not match the first
request’s API endpoint and parameters.`invalid_request_error`Invalid request
errors arise when your request has invalid parameters.
# [Handling errors](https://docs.stripe.com/api/errors/handling)

Our Client libraries raise exceptions for many reasons, such as a failed charge,
invalid parameters, authentication errors, and network unavailability. We
recommend writing code that gracefully handles all possible API exceptions.

- Related guide: [Error Handling](https://docs.stripe.com/error-handling)
Server-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
# Select a client library to see examples of# handling different kinds of errors.
```

# [Expanding Responses](https://docs.stripe.com/api/expanding_objects)

Many objects allow you to request additional information as an expanded response
by using the `expand` request parameter. This parameter is available on all API
requests, and applies to the response of that request only. You can expand
responses in two ways.

In many cases, an object contains the ID of a related object in its response
properties. For example, a `Charge` might have an associated Customer ID. You
can expand these objects in line with the expand request parameter. The
`expandable` label in this documentation indicates ID fields that you can expand
into objects.

Some available fields aren’t included in the responses by default, such as the
`number` and `cvc` fields for the Issuing Card object. You can request these
fields as an expanded response by using the `expand` request parameter.

You can expand recursively by specifying nested fields after a dot (`.`). For
example, requesting `invoice.subscription` on a charge expands the `invoice`
property into a full Invoice object, then expands the `subscription` property on
that invoice into a full Subscription object.

You can use the `expand` parameter on any endpoint that returns expandable
fields, including list, create, and update endpoints.

Expansions on list requests start with the `data` property. For example, you can
expand `data.customers` on a request to list charges and associated customers.
Performing deep expansions on numerous list requests might result in slower
processing times.

Expansions have a maximum depth of four levels (for example, the deepest
expansion allowed when listing charges is
`data.invoice.subscription.default_source`).

You can expand multiple objects at the same time by identifying multiple items
in the `expand` array.

- Related guide: [Expanding responses](https://docs.stripe.com/expand)
- Related video: [Expand](https://www.youtube.com/watch?v=m8Vj_CEWyQc)
Server-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/charges/ch_3LmzzQ2eZvKYlo2C0XjzUzJV \ -u
sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2: \ -d
"expand[]"=customer \ -d "expand[]"="invoice.subscription" \ -G
```

Response
```
{ "id": "ch_3LmzzQ2eZvKYlo2C0XjzUzJV", "object": "charge", "customer": { "id":
"cu_14HOpH2eZvKYlo2CxXIM7Pb2", "object": "customer", // ... }, "invoice": {
"id": "in_1LmzzQ2eZvKYlo2CpyWn8szu", "object": "invoice", "subscription": {
"id": "su_1LmzoG2eZvKYlo2Cpw6S7dAq", "object": "subscription", // ... }, // ...
}, // ...}
```

# [Idempotent requests](https://docs.stripe.com/api/idempotent_requests)

The API supports [idempotency](https://en.wikipedia.org/wiki/Idempotence) for
safely retrying requests without accidentally performing the same operation
twice. When creating or updating an object, use an idempotency key. Then, if a
connection error occurs, you can safely repeat the request without risk of
creating a second object or performing the update twice.

To perform an idempotent request, provide an additional `IdempotencyKey` element
to the request options.

Stripe’s idempotency works by saving the resulting status code and body of the
first request made for any given idempotency key, regardless of whether it
succeeds or fails. Subsequent requests with the same key return the same result,
including `500` errors.

A client generates an idempotency key, which is a unique key that the server
uses to recognize subsequent retries of the same request. How you create unique
keys is up to you, but we suggest using V4 UUIDs, or another random string with
enough entropy to avoid collisions. Idempotency keys are up to 255 characters
long.

You can remove keys from the system automatically after they’re at least 24
hours old. We generate a new request if a key is reused after the original is
pruned. The idempotency layer compares incoming parameters to those of the
original request and errors if they’re the same to prevent accidental misuse.

We save results only after the execution of an endpoint begins. If incoming
parameters fail validation, or the request conflicts with another request that’s
executing concurrently, we don’t save the idempotent result because no API
endpoint initiates the execution. You can retry these requests. Learn more about
when you can [retry idempotent
requests](https://docs.stripe.com/error-low-level#idempotency).

All `POST` requests accept idempotency keys. Don’t send idempotency keys in
`GET` and `DELETE` requests because it has no effect. These requests are
idempotent by definition.

Server-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/customers \ -u
sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2: \ -H
"Idempotency-Key: KG5LxwFBepaKHyUD" \ -d description="My First Test Customer
(created for API docs at https://docs.stripe.com/api)"
```

# [Metadata](https://docs.stripe.com/api/metadata)

Updateable Stripe objects—including
[Account](https://docs.stripe.com/api/accounts),
[Charge](https://docs.stripe.com/api/charges),
[Customer](https://docs.stripe.com/api/customers),
[PaymentIntent](https://docs.stripe.com/api/payment_intents),
[Refund](https://docs.stripe.com/api/refunds),
[Subscription](https://docs.stripe.com/api/subscriptions), and
[Transfer](https://docs.stripe.com/api/transfers) have a `metadata` parameter.
You can use this parameter to attach key-value data to these Stripe objects.

You can specify up to 50 keys, with key names up to 40 characters long and
values up to 500 characters long. Keys and values are stored as strings and can
contain any characters with one exception: you can’t use square brackets ([ and
]) in keys.

You can use metadata to store additional, structured information on an object.
For example, you could store your user’s full name and corresponding unique
identifier from your system on a Stripe
[Customer](https://docs.stripe.com/api/customers) object. Stripe doesn’t use
metadata—for example, we don’t use it to authorize or decline a charge and it
won’t be seen by your users unless you choose to show it to them.

Some of the objects listed above also support a `description` parameter. You can
use the `description` parameter to annotate a charge-for example, a
human-readable description such as `2 shirts for test@example.com`. Unlike
`metadata`, `description` is a single string, which your users might see (for
example, in email receipts Stripe sends on your behalf).

Don’t store any sensitive information (bank account numbers, card details, and
so on) as metadata or in the `description` parameter.

- Related guide: [Metadata](https://docs.stripe.com/metadata)

## Sample metadata use cases

- **Link IDs**: Attach your system’s unique IDs to a Stripe object to simplify
lookups. For example, add your order number to a charge, your user ID to a
customer or recipient, or a unique receipt number to a transfer.
- **Refund papertrails**: Store information about the reason for a refund and
the individual responsible for its creation.
- **Customer details**: Annotate a customer by storing an internal ID for your
future use.
POST /v1/customersServer-side languageStripe
CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/customers \ -u
"sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \ -d
"metadata[order_id]"=6735
```

```
{ "id": "cus_123456789", "object": "customer", "address": { "city": "city",
"country": "US", "line1": "line 1", "line2": "line 2", "postal_code": "90210",
"state": "CA" }, "balance": 0, "created": 1483565364, "currency": null,
"default_source": null, "delinquent": false, "description": null, "discount":
null, "email": null, "invoice_prefix": "C11F7E1", "invoice_settings": {
"custom_fields": null, "default_payment_method": null, "footer": null,
"rendering_options": null }, "livemode": false, "metadata": { "order_id": "6735"
}, "name": null, "next_invoice_sequence": 1, "phone": null, "preferred_locales":
[], "shipping": null, "tax_exempt": "none"}
```

# [Pagination](https://docs.stripe.com/api/pagination)

All top-level API resources have support for bulk fetches through “list” API
methods. For example, you can [list
charges](https://docs.stripe.com/api/charges/list), [list
customers](https://docs.stripe.com/api/customers/list), and [list
invoices](https://docs.stripe.com/api/invoices/list). These list API methods
share a common structure and accept, at a minimum, the following three
parameters: `limit`, `starting_after`, and `ending_before`.

Stripe’s list API methods use cursor-based pagination through the
`starting_after` and `ending_before` parameters. Both parameters accept an
existing object ID value (see below) and return objects in reverse chronological
order. The `ending_before` parameter returns objects listed before the named
object. The `starting_after` parameter returns objects listed after the named
object. These parameters are mutually exclusive. You can use either the
`starting_after` or `ending_before` parameter, but not both simultaneously.

Our client libraries offer [auto-pagination
helpers](https://docs.stripe.com/api/pagination/auto) to traverse all pages of a
list.

### Parameters

- #### limitoptional, default is 10

This specifies a limit on the number of objects to return, ranging between 1 and
100.
- #### starting_afteroptional object ID

A cursor to use in pagination. `starting_after` is an object ID that defines
your place in the list. For example, if you make a list request and receive 100
objects, ending with `obj_foo`, your subsequent call can include
`starting_after=obj_foo` to fetch the next page of the list.
- #### ending_beforeoptional object ID

A cursor to use in pagination. `ending_before` is an object ID that defines your
place in the list. For example, if you make a list request and receive 100
objects, starting with `obj_bar`, your subsequent call can include
`ending_before=obj_bar` to fetch the previous page of the list.

### List Response Format

- #### objectstring, value is "list"

A string that provides a description of the object type that returns.
- #### dataarray

An array containing the actual response elements, paginated by any request
parameters.
- #### has_moreboolean

Whether or not there are more elements available after this set. If `false`,
this set comprises the end of the list.
- #### urlurl

The URL for accessing this list.
Response
```
{ "object": "list", "url": "/v1/customers", "has_more": false, "data": [ { "id":
"cus_4QFJOjw2pOmAGJ", "object": "customer", "address": null, "balance": 0,
"created": 1405641735, "currency": "usd", "default_source":
"card_14HOpG2eZvKYlo2Cz4u5AJG5", "delinquent": false, "description": "New
customer", "discount": null, "email": null, "invoice_prefix": "7D11B54",
"invoice_settings": { "custom_fields": null, "default_payment_method": null,
"footer": null, "rendering_options": null }, "livemode": false, "metadata": {
"order_id": "6735" }, "name": "cus_4QFJOjw2pOmAGJ", "next_invoice_sequence": 25,
"phone": null, "preferred_locales": [], "shipping": null, "tax_exempt": "none",
"test_clock": null }, ]}
```

# [Search](https://docs.stripe.com/api/pagination/search)

Some top-level API resource have support for retrieval via “search” API methods.
For example, you can [search
charges](https://docs.stripe.com/api/charges/search), [search
customers](https://docs.stripe.com/api/customers/search), and [search
subscriptions](https://docs.stripe.com/api/subscriptions/search).

Stripe’s search API methods utilize cursor-based pagination via the `page`
request parameter and `next_page` response parameter. For example, if you make a
search request and receive `"next_page": "pagination_key"` in the response, your
subsequent call can include `page=pagination_key` to fetch the next page of
results.

Our client libraries offer
[auto-pagination](https://docs.stripe.com/api/pagination/auto) helpers to easily
traverse all pages of a search result.

### Search request format

- #### queryrequired

The search query string. See [search query
language](https://docs.stripe.com/search#search-query-language).
- #### limitoptional

A limit on the number of objects returned. Limit can range between 1 and 100,
and the default is 10.
- #### pageoptional

A cursor for pagination across multiple pages of results. Don’t include this
parameter on the first call. Use the `next_page` value returned in a previous
response to request subsequent results.

### Search response format

- #### objectstring, value is "search_result"

A string describing the object type returned.
- #### urlstring

The URL for accessing this list.
- #### has_moreboolean

Whether or not there are more elements available after this set. If `false`,
this set comprises the end of the list.
- #### dataarray

An array containing the actual response elements, paginated by any request
parameters.
- #### next_pagestring

A cursor for use in pagination. If `has_more` is true, you can pass the value of
`next_page` to a subsequent call to fetch the next page of results.
- #### total_countoptional positive integer or zero

The total number of objects that match the query, only accurate up to 10,000.
This field isn’t included by default. To include it in the response,
[expand](https://docs.stripe.com/api/expanding_objects) the `total_count` field.
Response
```
{ "object": "search_result", "url": "/v1/customers/search", "has_more": false,
"data": [ { "id": "cus_4QFJOjw2pOmAGJ", "object": "customer", "address": null,
"balance": 0, "created": 1405641735, "currency": "usd", "default_source":
"card_14HOpG2eZvKYlo2Cz4u5AJG5", "delinquent": false, "description":
"someone@example.com for Coderwall", "discount": null, "email": null,
"invoice_prefix": "7D11B54", "invoice_settings": { "custom_fields": null,
"default_payment_method": null, "footer": null, "rendering_options": null },
"livemode": false, "metadata": { "foo": "bar" }, "name": "fakename",
"next_invoice_sequence": 25, "phone": null, "preferred_locales": [], "shipping":
null, "tax_exempt": "none", "test_clock": null } ]}
```

# [Auto-pagination](https://docs.stripe.com/api/pagination/auto)

Our libraries support auto-pagination. This feature allows you to easily iterate
through large lists of resources without having to manually perform the requests
to fetch subsequent pages.

Server-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
# The auto-pagination feature is specific to Stripe's# libraries and cannot be used directly with curl.
```

# [Request IDs](https://docs.stripe.com/api/request_ids)

Each API request has an associated request identifier. You can find this value
in the response headers, under `Request-Id`. You can also find request
identifiers in the URLs of individual request logs in your
[Dashboard](https://dashboard.stripe.com/logs).

To expedite the resolution process, provide the request identifier when you
contact us about a specific request.

Server-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/customers \ -u
sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2: \ -D "-" \ -X
POST
```

# [Versioning](https://docs.stripe.com/api/versioning)

Each major release, such as [Acacia](https://docs.stripe.com/changelog/acacia),
includes changes that aren’t
[backward-compatible](https://docs.stripe.com/upgrades#what-changes-does-stripe-consider-to-be-backward-compatible)
with previous releases. Upgrading to a new major release can require updates to
existing code. Each monthly release includes only backward-compatible changes,
and uses the same name as the last major release. You can safely upgrade to a
new monthly release without breaking any existing code. The current version is
2025-02-24.acacia. For information on all API versions, view our [API
changelog](https://docs.stripe.com/changelog).

You can upgrade your API version in
[Workbench](https://dashboard.stripe.com/workbench). As a precaution, use API
versioning to test a new API version before committing to an upgrade.

Server-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/charges \ -u
sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2: \ -H
"Stripe-Version: 2025-02-24.acacia"
```

# [Balance](https://docs.stripe.com/api/balance)

This is an object representing your Stripe balance. You can retrieve it to see
the balance currently on your Stripe account.

You can also retrieve the balance history, which contains a list of
[transactions](https://docs.stripe.com/reporting/balance-transaction-types) that
contributed to the balance (charges, payouts, and so forth).

The available and pending amounts for each currency are broken down further by
payment source types.

Related guide: [Understanding Connect account
balances](https://docs.stripe.com/connect/account-balances)

Endpoints[GET/v1/balance](https://docs.stripe.com/api/balance/balance_retrieve)
# [The Balance object](https://docs.stripe.com/api/balance/balance_object)

### Attributes

- #### availablearray of objects

Available funds that you can transfer or pay out automatically by Stripe or
explicitly through the [Transfers
API](https://docs.stripe.com/api/balance/balance_object#transfers) or [Payouts
API](https://docs.stripe.com/api/balance/balance_object#payouts). You can find
the available balance for each currency and payment type in the `source_types`
property.

Show child attributes
- #### pendingarray of objects

Funds that aren’t available in the balance yet. You can find the pending balance
for each currency and each payment type in the `source_types` property.

Show child attributes

### More attributesExpand all

- #### objectstring
- #### connect_reservednullable array of objectsConnect only
- #### instant_availablenullable array of objects
- #### issuingnullable object
- #### livemodeboolean
The Balance object
```
{ "object": "balance", "available": [ { "amount": 666670, "currency": "usd",
"source_types": { "card": 666670 } } ], "connect_reserved": [ { "amount": 0,
"currency": "usd" } ], "livemode": false, "pending": [ { "amount": 61414,
"currency": "usd", "source_types": { "card": 61414 } } ]}
```

# [Retrieve balance](https://docs.stripe.com/api/balance/balance_retrieve)

Retrieves the current account balance, based on the authentication that was used
to make the request. For a sample request, see [Accounting for negative
balances](https://docs.stripe.com/connect/account-balances#accounting-for-negative-balances).

### Parameters

No parameters.

### Returns

Returns a balance object for the account that was authenticated in the request.

GET /v1/balanceServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/balance \ -u
"sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

Response
```
{ "object": "balance", "available": [ { "amount": 666670, "currency": "usd",
"source_types": { "card": 666670 } } ], "connect_reserved": [ { "amount": 0,
"currency": "usd" } ], "livemode": false, "pending": [ { "amount": 61414,
"currency": "usd", "source_types": { "card": 61414 } } ]}
```

# [Balance Transactions](https://docs.stripe.com/api/balance_transactions)

Balance transactions represent funds moving through your Stripe account. Stripe
creates them for every type of transaction that enters or leaves your Stripe
account balance.

Related guide: [Balance transaction
types](https://docs.stripe.com/reports/balance-transaction-types)

Endpoints[GET/v1/balance_transactions/:id](https://docs.stripe.com/api/balance_transactions/retrieve)[GET/v1/balance_transactions](https://docs.stripe.com/api/balance_transactions/list)
Show

# [Charges](https://docs.stripe.com/api/charges)

The `Charge` object represents a single attempt to move money into your Stripe
account. PaymentIntent confirmation is the most common way to create Charges,
but transferring money to a different Stripe account through Connect also
creates Charges. Some legacy payment flows create Charges directly, which is not
recommended for new integrations.

Endpoints[POST/v1/charges](https://docs.stripe.com/api/charges/create)[POST/v1/charges/:id](https://docs.stripe.com/api/charges/update)[GET/v1/charges/:id](https://docs.stripe.com/api/charges/retrieve)[GET/v1/charges](https://docs.stripe.com/api/charges/list)[POST/v1/charges/:id/capture](https://docs.stripe.com/api/charges/capture)[GET/v1/charges/search](https://docs.stripe.com/api/charges/search)
Show

# [Customers](https://docs.stripe.com/api/customers)

This object represents a customer of your business. Use it to [create recurring
charges](https://docs.stripe.com/invoicing/customer), [save
payment](https://docs.stripe.com/payments/save-during-payment) and contact
information, and track payments that belong to the same customer.

Endpoints[POST/v1/customers](https://docs.stripe.com/api/customers/create)[POST/v1/customers/:id](https://docs.stripe.com/api/customers/update)[GET/v1/customers/:id](https://docs.stripe.com/api/customers/retrieve)[GET/v1/customers](https://docs.stripe.com/api/customers/list)[DELETE/v1/customers/:id](https://docs.stripe.com/api/customers/delete)[GET/v1/customers/search](https://docs.stripe.com/api/customers/search)
Show

# [Customer Session](https://docs.stripe.com/api/customer_sessions)

A Customer Session allows you to grant Stripe’s frontend SDKs (like Stripe.js)
client-side access control over a Customer.

Related guides: [Customer Session with the Payment
Element](https://docs.stripe.com/payments/accept-a-payment-deferred?platform=web&type=payment#save-payment-methods),
[Customer Session with the Pricing
Table](https://docs.stripe.com/payments/checkout/pricing-table#customer-session),
[Customer Session with the Buy
Button](https://docs.stripe.com/payment-links/buy-button#pass-an-existing-customer).

Endpoints[POST/v1/customer_sessions](https://docs.stripe.com/api/customer_sessions/create)
Show

# [Disputes](https://docs.stripe.com/api/disputes)

A dispute occurs when a customer questions your charge with their card issuer.
When this happens, you have the opportunity to respond to the dispute with
evidence that shows that the charge is legitimate.

Related guide: [Disputes and fraud](https://docs.stripe.com/disputes)

Endpoints[POST/v1/disputes/:id](https://docs.stripe.com/api/disputes/update)[GET/v1/disputes/:id](https://docs.stripe.com/api/disputes/retrieve)[GET/v1/disputes](https://docs.stripe.com/api/disputes/list)[POST/v1/disputes/:id/close](https://docs.stripe.com/api/disputes/close)
Show

# [Events](https://docs.stripe.com/api/events)

Events are our way of letting you know when something interesting happens in
your account. When an interesting event occurs, we create a new `Event` object.
For example, when a charge succeeds, we create a `charge.succeeded` event, and
when an invoice payment attempt fails, we create an `invoice.payment_failed`
event. Certain API requests might create multiple events. For example, if you
create a new subscription for a customer, you receive both a
`customer.subscription.created` event and a `charge.succeeded` event.

Events occur when the state of another API resource changes. The event’s data
field embeds the resource’s state at the time of the change. For example, a
`charge.succeeded` event contains a charge, and an `invoice.payment_failed`
event contains an invoice.

As with other API resources, you can use endpoints to retrieve an [individual
event](https://docs.stripe.com/api/balance/balance_object#retrieve_event) or a
[list of events](https://docs.stripe.com/api/balance/balance_object#list_events)
from the API. We also have a separate
[webhooks](http://en.wikipedia.org/wiki/Webhook) system for sending the `Event`
objects directly to an endpoint on your server. You can manage webhooks in your
[account settings](https://dashboard.stripe.com/account/webhooks). Learn how to
[listen for events](https://docs.stripe.com/webhooks) so that your integration
can automatically trigger reactions.

When using [Connect](https://docs.stripe.com/connect), you can also receive
event notifications that occur in connected accounts. For these events, there’s
an additional `account` attribute in the received `Event` object.

We only guarantee access to events through the [Retrieve Event
API](https://docs.stripe.com/api/balance/balance_object#retrieve_event) for 30
days.

Endpoints[GET/v1/events/:id](https://docs.stripe.com/api/events/retrieve)[GET/v1/events](https://docs.stripe.com/api/events/list)
Show

# [Events](https://docs.stripe.com/api/v2/core/events) v2

[Learn more about calling API v2
endpoints.](https://docs.stripe.com/api-v2-overview)
Events are generated to keep you informed of activity in your business account.
APIs in the /v2 namespace generate [thin
events](https://docs.stripe.com/event-destinations#benefits-of-thin-events)
which have small, unversioned payloads that include a reference to the ID of the
object that has changed. The Events v2 API returns these new thin events.
[Retrieve the event
object](https://docs.stripe.com/event-destinations#fetch-data) for additional
data about the event. Use the related object ID in the event payload to [fetch
the API
resource](https://docs.stripe.com/event-destinations#retrieve-the-object-associated-with-thin-events)
of the object associated with the event. Comparatively, events generated by most
API v1 include a versioned snapshot of an API object in their payload.

Endpoints[GET/v2/core/events/:id](https://docs.stripe.com/api/v2/core/events/retrieve)[GET/v2/core/events](https://docs.stripe.com/api/v2/core/events/list)
Show

# [Event Destinations](https://docs.stripe.com/api/v2/core/event_destinations) v2

[Learn more about calling API v2
endpoints.](https://docs.stripe.com/api-v2-overview)
Set up an event destination to receive events from Stripe across multiple
destination types, including [webhook
endpoints](https://docs.stripe.com/webhooks) and [Amazon
EventBridge](https://docs.stripe.com/event-destinations/eventbridge). Event
destinations support receiving [thin
events](https://docs.stripe.com/api/v2/events) and [snapshot
events](https://docs.stripe.com/api/events).

Endpoints[POST/v2/core/event_destinations](https://docs.stripe.com/api/v2/core/event_destinations/create)[POST/v2/core/event_destinations/:id](https://docs.stripe.com/api/v2/core/event_destinations/update)[GET/v2/core/event_destinations/:id](https://docs.stripe.com/api/v2/core/event_destinations/retrieve)[GET/v2/core/event_destinations](https://docs.stripe.com/api/v2/core/event_destinations/list)[DELETE/v2/core/event_destinations/:id](https://docs.stripe.com/api/v2/core/event_destinations/delete)[POST/v2/core/event_destinations/:id/disable](https://docs.stripe.com/api/v2/core/event_destinations/disable)[POST/v2/core/event_destinations/:id/enable](https://docs.stripe.com/api/v2/core/event_destinations/enable)[POST/v2/core/event_destinations/:id/ping](https://docs.stripe.com/api/v2/core/event_destinations/ping)
Show

# [Files](https://docs.stripe.com/api/files)

This object represents files hosted on Stripe’s servers. You can upload files
with the [create
file](https://docs.stripe.com/api/balance/balance_object#create_file) request
(for example, when uploading dispute evidence). Stripe also creates files
independently (for example, the results of a [Sigma scheduled
query](https://docs.stripe.com/api/balance/balance_object#scheduled_queries)).

Related guide: [File upload guide](https://docs.stripe.com/file-upload)

Endpoints[POST/v1/files](https://docs.stripe.com/api/files/create)[GET/v1/files/:id](https://docs.stripe.com/api/files/retrieve)[GET/v1/files](https://docs.stripe.com/api/files/list)
Show

# [File Links](https://docs.stripe.com/api/file_links)

To share the contents of a `File` object with non-Stripe users, you can create a
`FileLink`. `FileLink`s contain a URL that you can use to retrieve the contents
of the file without authentication.

Endpoints[POST/v1/file_links](https://docs.stripe.com/api/file_links/create)[POST/v1/file_links/:id](https://docs.stripe.com/api/file_links/update)[GET/v1/file_links/:id](https://docs.stripe.com/api/file_links/retrieve)[GET/v1/file_links](https://docs.stripe.com/api/file_links/list)
Show

# [Mandates](https://docs.stripe.com/api/mandates)

A Mandate is a record of the permission that your customer gives you to debit
their payment method.

Endpoints[GET/v1/mandates/:id](https://docs.stripe.com/api/mandates/retrieve)
Show

# [Payment Intents](https://docs.stripe.com/api/payment_intents)

A PaymentIntent guides you through the process of collecting a payment from your
customer. We recommend that you create exactly one PaymentIntent for each order
or customer session in your system. You can reference the PaymentIntent later to
see the history of payment attempts for a particular session.

A PaymentIntent transitions through [multiple
statuses](https://docs.stripe.com/payments/intents#intent-statuses) throughout
its lifetime as it interfaces with Stripe.js to perform authentication flows and
ultimately creates at most one successful charge.

Related guide: [Payment Intents
API](https://docs.stripe.com/payments/payment-intents)

Endpoints[POST/v1/payment_intents](https://docs.stripe.com/api/payment_intents/create)[POST/v1/payment_intents/:id](https://docs.stripe.com/api/payment_intents/update)[GET/v1/payment_intents/:id](https://docs.stripe.com/api/payment_intents/retrieve)[GET/v1/payment_intents](https://docs.stripe.com/api/payment_intents/list)[POST/v1/payment_intents/:id/cancel](https://docs.stripe.com/api/payment_intents/cancel)[POST/v1/payment_intents/:id/capture](https://docs.stripe.com/api/payment_intents/capture)[POST/v1/payment_intents/:id/confirm](https://docs.stripe.com/api/payment_intents/confirm)[POST/v1/payment_intents/:id/increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization)[POST/v1/payment_intents/:id/apply_customer_balance](https://docs.stripe.com/api/payment_intents/apply_customer_balance)[GET/v1/payment_intents/search](https://docs.stripe.com/api/payment_intents/search)[POST/v1/payment_intents/:id/verify_microdeposits](https://docs.stripe.com/api/payment_intents/verify_microdeposits)
Show

# [Setup Intents](https://docs.stripe.com/api/setup_intents)

A SetupIntent guides you through the process of setting up and saving a
customer’s payment credentials for future payments. For example, you can use a
SetupIntent to set up and save your customer’s card without immediately
collecting a payment. Later, you can use
[PaymentIntents](https://docs.stripe.com/api/balance/balance_object#payment_intents)
to drive the payment flow.

Create a SetupIntent when you’re ready to collect your customer’s payment
credentials. Don’t maintain long-lived, unconfirmed SetupIntents because they
might not be valid. The SetupIntent transitions through multiple
[statuses](https://docs.stripe.com/payments/intents#intent-statuses) as it
guides you through the setup process.

Successful SetupIntents result in payment credentials that are optimized for
future payments. For example, cardholders in [certain
regions](https://stripe.com/guides/strong-customer-authentication) might need to
be run through [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) during
payment method collection to streamline later [off-session
payments](https://docs.stripe.com/payments/setup-intents). If you use the
SetupIntent with a
[Customer](https://docs.stripe.com/api/balance/balance_object#setup_intent_object-customer),
it automatically attaches the resulting payment method to that Customer after
successful setup. We recommend using SetupIntents or
[setup_future_usage](https://docs.stripe.com/api/balance/balance_object#payment_intent_object-setup_future_usage)
on PaymentIntents to save payment methods to prevent saving invalid or
unoptimized payment methods.

By using SetupIntents, you can reduce friction for your customers, even as
regulations change over time.

Related guide: [Setup Intents
API](https://docs.stripe.com/payments/setup-intents)

Endpoints[POST/v1/setup_intents](https://docs.stripe.com/api/setup_intents/create)[POST/v1/setup_intents/:id](https://docs.stripe.com/api/setup_intents/update)[GET/v1/setup_intents/:id](https://docs.stripe.com/api/setup_intents/retrieve)[GET/v1/setup_intents](https://docs.stripe.com/api/setup_intents/list)[POST/v1/setup_intents/:id/cancel](https://docs.stripe.com/api/setup_intents/cancel)[POST/v1/setup_intents/:id/confirm](https://docs.stripe.com/api/setup_intents/confirm)[POST/v1/setup_intents/:id/verify_microdeposits](https://docs.stripe.com/api/setup_intents/verify_microdeposits)
Show

# [Setup Attempts](https://docs.stripe.com/api/setup_attempts)

A SetupAttempt describes one attempted confirmation of a SetupIntent, whether
that confirmation is successful or unsuccessful. You can use SetupAttempts to
inspect details of a specific attempt at setting up a payment method using a
SetupIntent.

Endpoints[GET/v1/setup_attempts](https://docs.stripe.com/api/setup_attempts/list)
Show

# [Payouts](https://docs.stripe.com/api/payouts)

A `Payout` object is created when you receive funds from Stripe, or when you
initiate a payout to either a bank account or debit card of a [connected Stripe
account](https://docs.stripe.com/connect/bank-debit-card-payouts). You can
retrieve individual payouts, and list all payouts. Payouts are made on [varying
schedules](https://docs.stripe.com/connect/manage-payout-schedule), depending on
your country and industry.

Related guide: [Receiving payouts](https://docs.stripe.com/payouts)

Endpoints[POST/v1/payouts](https://docs.stripe.com/api/payouts/create)[POST/v1/payouts/:id](https://docs.stripe.com/api/payouts/update)[GET/v1/payouts/:id](https://docs.stripe.com/api/payouts/retrieve)[GET/v1/payouts](https://docs.stripe.com/api/payouts/list)[POST/v1/payouts/:id/cancel](https://docs.stripe.com/api/payouts/cancel)[POST/v1/payouts/:id/reverse](https://docs.stripe.com/api/payouts/reverse)
Show

# [Refunds](https://docs.stripe.com/api/refunds)

Refund objects allow you to refund a previously created charge that isn’t
refunded yet. Funds are refunded to the credit or debit card that’s initially
charged.

Related guide: [Refunds](https://docs.stripe.com/refunds)

Endpoints[POST/v1/refunds](https://docs.stripe.com/api/refunds/create)[POST/v1/refunds/:id](https://docs.stripe.com/api/refunds/update)[GET/v1/refunds/:id](https://docs.stripe.com/api/refunds/retrieve)[GET/v1/refunds](https://docs.stripe.com/api/refunds/list)[POST/v1/refunds/:id/cancel](https://docs.stripe.com/api/refunds/cancel)
Show

# [Confirmation Token](https://docs.stripe.com/api/confirmation_tokens)

ConfirmationTokens help transport client side data collected by Stripe JS over
to your server for confirming a PaymentIntent or SetupIntent. If the
confirmation is successful, values present on the ConfirmationToken are written
onto the Intent.

To learn more about how to use ConfirmationToken, visit the related guides:

- [Finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server)
- [Build two-step
confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation).

Endpoints[GET/v1/confirmation_tokens/:id](https://docs.stripe.com/api/confirmation_tokens/retrieve)[POST/v1/test_helpers/confirmation_tokens](https://docs.stripe.com/api/confirmation_tokens/test_create)
Show

# [Tokens](https://docs.stripe.com/api/tokens)

Tokenization is the process Stripe uses to collect sensitive card or bank
account details, or personally identifiable information (PII), directly from
your customers in a secure manner. A token representing this information is
returned to your server to use. Use our [recommended payments
integrations](https://docs.stripe.com/payments) to perform this process on the
client-side. This guarantees that no sensitive card data touches your server,
and allows your integration to operate in a PCI-compliant way.

If you can’t use client-side tokenization, you can also create tokens using the
API with either your publishable or secret API key. If your integration uses
this method, you’re responsible for any PCI compliance that it might require,
and you must keep your secret API key safe. Unlike with client-side
tokenization, your customer’s information isn’t sent directly to Stripe, so we
can’t determine how it’s handled or stored.

You can’t store or use tokens more than once. To store card or bank account
information for later use, create
[Customer](https://docs.stripe.com/api#customers) objects or [External
accounts](https://docs.stripe.com/api#external_accounts).
[Radar](https://docs.stripe.com/radar), our integrated solution for automatic
fraud protection, performs best with integrations that use client-side
tokenization.

Endpoints[POST/v1/tokens](https://docs.stripe.com/api/tokens/create_account)[POST/v1/tokens](https://docs.stripe.com/api/tokens/create_bank_account)[POST/v1/tokens](https://docs.stripe.com/api/tokens/create_card)[POST/v1/tokens](https://docs.stripe.com/api/tokens/create_cvc_update)[POST/v1/tokens](https://docs.stripe.com/api/tokens/create_person)[POST/v1/tokens](https://docs.stripe.com/api/tokens/create_pii)[GET/v1/tokens/:id](https://docs.stripe.com/api/tokens/retrieve)
Show

# [Payment Methods](https://docs.stripe.com/api/payment_methods)

PaymentMethod objects represent your customer’s payment instruments. You can use
them with [PaymentIntents](https://docs.stripe.com/payments/payment-intents) to
collect payments or save them to Customer objects to store instrument details
for future payments.

Related guides: [Payment
Methods](https://docs.stripe.com/payments/payment-methods) and [More Payment
Scenarios](https://docs.stripe.com/payments/more-payment-scenarios).

Endpoints[POST/v1/payment_methods](https://docs.stripe.com/api/payment_methods/create)[POST/v1/payment_methods/:id](https://docs.stripe.com/api/payment_methods/update)[GET/v1/customers/:id/payment_methods/:id](https://docs.stripe.com/api/payment_methods/customer)[GET/v1/payment_methods/:id](https://docs.stripe.com/api/payment_methods/retrieve)[GET/v1/customers/:id/payment_methods](https://docs.stripe.com/api/payment_methods/customer_list)[GET/v1/payment_methods](https://docs.stripe.com/api/payment_methods/list)[POST/v1/payment_methods/:id/attach](https://docs.stripe.com/api/payment_methods/attach)[POST/v1/payment_methods/:id/detach](https://docs.stripe.com/api/payment_methods/detach)
Show

# [Payment Method Configurations](https://docs.stripe.com/api/payment_method_configurations)

PaymentMethodConfigurations control which payment methods are displayed to your
customers when you don’t explicitly specify payment method types. You can have
multiple configurations with different sets of payment methods for different
scenarios.

There are two types of PaymentMethodConfigurations. Which is used depends on the
[charge type](https://docs.stripe.com/connect/charges):

**Direct** configurations apply to payments created on your account, including
Connect destination charges, Connect separate charges and transfers, and
payments not involving Connect.

**Child** configurations apply to payments created on your connected accounts
using direct charges, and charges with the on_behalf_of parameter.

Child configurations have a `parent` that sets default values and controls which
settings connected accounts may override. You can specify a parent ID at payment
time, and Stripe will automatically resolve the connected account’s associated
child configuration. Parent configurations are [managed in the
dashboard](https://dashboard.stripe.com/settings/payment_methods/connected_accounts)
and are not available in this API.

Related guides:

- [Payment Method Configurations
API](https://docs.stripe.com/connect/payment-method-configurations)
- [Multiple configurations on dynamic payment
methods](https://docs.stripe.com/payments/multiple-payment-method-configs)
- [Multiple configurations for your Connect
accounts](https://docs.stripe.com/connect/multiple-payment-method-configurations)

Endpoints[POST/v1/payment_method_configurations](https://docs.stripe.com/api/payment_method_configurations/create)[POST/v1/payment_method_configurations/:id](https://docs.stripe.com/api/payment_method_configurations/update)[GET/v1/payment_method_configurations/:id](https://docs.stripe.com/api/payment_method_configurations/retrieve)[GET/v1/payment_method_configurations](https://docs.stripe.com/api/payment_method_configurations/list)
Show

# [Payment Method Domains](https://docs.stripe.com/api/payment_method_domains)

A payment method domain represents a web domain that you have registered with
Stripe. Stripe Elements use registered payment method domains to control where
certain payment methods are shown.

Related guide: [Payment method
domains](https://docs.stripe.com/payments/payment-methods/pmd-registration).

Endpoints[POST/v1/payment_method_domains](https://docs.stripe.com/api/payment_method_domains/create)[POST/v1/payment_method_domains/:id](https://docs.stripe.com/api/payment_method_domains/update)[GET/v1/payment_method_domains/:id](https://docs.stripe.com/api/payment_method_domains/retrieve)[GET/v1/payment_method_domains](https://docs.stripe.com/api/payment_method_domains/list)[POST/v1/payment_method_domains/:id/validate](https://docs.stripe.com/api/payment_method_domains/validate)
Show

# [Bank Accounts](https://docs.stripe.com/api/customer_bank_accounts)

These bank accounts are payment methods on `Customer` objects.

On the other hand [External
Accounts](https://docs.stripe.com/api#external_accounts) are transfer
destinations on `Account` objects for connected accounts. They can be bank
accounts or debit cards as well, and are documented in the links above.

Related guide: [Bank debits and
transfers](https://docs.stripe.com/payments/bank-debits-transfers)

Endpoints[POST/v1/customers/:id/sources](https://docs.stripe.com/api/customer_bank_accounts/create)[POST/v1/customers/:id/sources/:id](https://docs.stripe.com/api/customer_bank_accounts/update)[GET/v1/customers/:id/bank_accounts/:id](https://docs.stripe.com/api/customer_bank_accounts/retrieve)[GET/v1/customers/:id/bank_accounts](https://docs.stripe.com/api/customer_bank_accounts/list)[DELETE/v1/customers/:id/sources/:id](https://docs.stripe.com/api/customer_bank_accounts/delete)[POST/v1/customers/:id/sources/:id/verify](https://docs.stripe.com/api/customer_bank_accounts/verify)
Show

# [Cash Balance](https://docs.stripe.com/api/cash_balance)

A customer’s `Cash balance` represents real funds. Customers can add funds to
their cash balance by sending a bank transfer. These funds can be used for
payment and can eventually be paid out to your bank account.

Endpoints[POST/v1/customers/:id/cash_balance](https://docs.stripe.com/api/cash_balance/update)[GET/v1/customers/:id/cash_balance](https://docs.stripe.com/api/cash_balance/retrieve)
Show

# [Cash Balance Transaction](https://docs.stripe.com/api/cash_balance_transactions)

Customers with certain payments enabled have a cash balance, representing funds
that were paid by the customer to a merchant, but have not yet been allocated to
a payment. Cash Balance Transactions represent when funds are moved into or out
of this balance. This includes funding by the customer, allocation to payments,
and refunds to the customer.

Endpoints[GET/v1/customers/:id/cash_balance_transactions/:id](https://docs.stripe.com/api/cash_balance_transactions/retrieve)[GET/v1/customers/:id/cash_balance_transactions](https://docs.stripe.com/api/cash_balance_transactions/list)[POST/v1/test_helpers/customers/:id/fund_cash_balance](https://docs.stripe.com/api/cash_balance_transactions/fund_cash_balance)
Show

# [Cards](https://docs.stripe.com/api/cards)

You can store multiple cards on a customer in order to charge the customer
later. You can also store multiple debit cards on a recipient in order to
transfer to those cards later.

Related guide: [Card payments with
Sources](https://docs.stripe.com/sources/cards)

Endpoints[POST/v1/customers/:id/sources](https://docs.stripe.com/api/cards/create)[POST/v1/customers/:id/sources/:id](https://docs.stripe.com/api/cards/update)[GET/v1/customers/:id/cards/:id](https://docs.stripe.com/api/cards/retrieve)[GET/v1/customers/:id/cards](https://docs.stripe.com/api/cards/list)[DELETE/v1/customers/:id/sources/:id](https://docs.stripe.com/api/cards/delete)
Show

# [Sources](https://docs.stripe.com/api/sources) Deprecated

`Source` objects allow you to accept a variety of payment methods. They
represent a customer’s payment instrument, and can be used with the Stripe API
just like a `Card` object: once chargeable, they can be charged, or can be
attached to customers.

Stripe doesn’t recommend using the deprecated [Sources
API](https://docs.stripe.com/api/sources). We recommend that you adopt the
[PaymentMethods API](https://docs.stripe.com/api/payment_methods). This newer
API provides access to our latest features and payment method types.

Related guides: [Sources API](https://docs.stripe.com/sources) and [Sources &
Customers](https://docs.stripe.com/sources/customers).

Endpoints[POST/v1/sources](https://docs.stripe.com/api/sources/create)[POST/v1/sources/:id](https://docs.stripe.com/api/sources/update)[GET/v1/sources/:id](https://docs.stripe.com/api/sources/retrieve)[POST/v1/customers/:id/sources](https://docs.stripe.com/api/sources/attach)[DELETE/v1/customers/:id/sources/:id](https://docs.stripe.com/api/sources/detach)
Show

# [Products](https://docs.stripe.com/api/products)

Products describe the specific goods or services you offer to your customers.
For example, you might offer a Standard and Premium version of your goods or
service; each version would be a separate Product. They can be used in
conjunction with
[Prices](https://docs.stripe.com/api/balance/balance_object#prices) to configure
pricing in Payment Links, Checkout, and Subscriptions.

Related guides: [Set up a
subscription](https://docs.stripe.com/billing/subscriptions/set-up-subscription),
[share a Payment Link](https://docs.stripe.com/payment-links), [accept payments
with
Checkout](https://docs.stripe.com/payments/accept-a-payment#create-product-prices-upfront),
and more about [Products and
Prices](https://docs.stripe.com/products-prices/overview)

Endpoints[POST/v1/products](https://docs.stripe.com/api/products/create)[POST/v1/products/:id](https://docs.stripe.com/api/products/update)[GET/v1/products/:id](https://docs.stripe.com/api/products/retrieve)[GET/v1/products](https://docs.stripe.com/api/products/list)[DELETE/v1/products/:id](https://docs.stripe.com/api/products/delete)[GET/v1/products/search](https://docs.stripe.com/api/products/search)
Show

# [Prices](https://docs.stripe.com/api/prices)

Prices define the unit cost, currency, and (optional) billing cycle for both
recurring and one-time purchases of products.
[Products](https://docs.stripe.com/api/balance/balance_object#products) help you
track inventory or provisioning, and prices help you track payment terms.
Different physical goods or levels of service should be represented by products,
and pricing options should be represented by prices. This approach lets you
change prices without having to change your provisioning scheme.

For example, you might have a single “gold” product that has prices for
$10/month, $100/year, and €9 once.

Related guides: [Set up a
subscription](https://docs.stripe.com/billing/subscriptions/set-up-subscription),
[create an invoice](https://docs.stripe.com/billing/invoices/create), and more
about [products and prices](https://docs.stripe.com/products-prices/overview).

Endpoints[POST/v1/prices](https://docs.stripe.com/api/prices/create)[POST/v1/prices/:id](https://docs.stripe.com/api/prices/update)[GET/v1/prices/:id](https://docs.stripe.com/api/prices/retrieve)[GET/v1/prices](https://docs.stripe.com/api/prices/list)[GET/v1/prices/search](https://docs.stripe.com/api/prices/search)
Show

# [Coupons](https://docs.stripe.com/api/coupons)

A coupon contains information about a percent-off or amount-off discount you
might want to apply to a customer. Coupons may be applied to
[subscriptions](https://docs.stripe.com/api/balance/balance_object#subscriptions),
[invoices](https://docs.stripe.com/api/balance/balance_object#invoices),
[checkout sessions](https://docs.stripe.com/api/checkout/sessions),
[quotes](https://docs.stripe.com/api/balance/balance_object#quotes), and more.
Coupons do not work with conventional one-off
[charges](https://docs.stripe.com/api/balance/balance_object#create_charge) or
[payment intents](https://docs.stripe.com/api/payment_intents).

Endpoints[POST/v1/coupons](https://docs.stripe.com/api/coupons/create)[POST/v1/coupons/:id](https://docs.stripe.com/api/coupons/update)[GET/v1/coupons/:id](https://docs.stripe.com/api/coupons/retrieve)[GET/v1/coupons](https://docs.stripe.com/api/coupons/list)[DELETE/v1/coupons/:id](https://docs.stripe.com/api/coupons/delete)
Show

# [Promotion Code](https://docs.stripe.com/api/promotion_codes)

A Promotion Code represents a customer-redeemable code for a
[coupon](https://docs.stripe.com/api/balance/balance_object#coupons). It can be
used to create multiple codes for a single coupon.

Endpoints[POST/v1/promotion_codes](https://docs.stripe.com/api/promotion_codes/create)[POST/v1/promotion_codes/:id](https://docs.stripe.com/api/promotion_codes/update)[GET/v1/promotion_codes/:id](https://docs.stripe.com/api/promotion_codes/retrieve)[GET/v1/promotion_codes](https://docs.stripe.com/api/promotion_codes/list)
Show

# [Discounts](https://docs.stripe.com/api/discounts)

A discount represents the actual application of a
[coupon](https://docs.stripe.com/api/balance/balance_object#coupons) or
[promotion
code](https://docs.stripe.com/api/balance/balance_object#promotion_codes). It
contains information about when the discount began, when it will end, and what
it is applied to.

Related guide: [Applying discounts to
subscriptions](https://docs.stripe.com/billing/subscriptions/discounts)

Endpoints[DELETE/v1/customers/:id/discount](https://docs.stripe.com/api/discounts/delete)[DELETE/v1/subscriptions/:id/discount](https://docs.stripe.com/api/discounts/subscription_delete)
Show

# [Tax Code](https://docs.stripe.com/api/tax_codes)

[Tax codes](https://stripe.com/docs/tax/tax-categories) classify goods and
services for tax purposes.

Endpoints[GET/v1/tax_codes/:id](https://docs.stripe.com/api/tax_codes/retrieve)[GET/v1/tax_codes](https://docs.stripe.com/api/tax_codes/list)
Show

# [Tax Rate](https://docs.stripe.com/api/tax_rates)

Tax rates can be applied to
[invoices](https://docs.stripe.com/invoicing/taxes/tax-rates),
[subscriptions](https://docs.stripe.com/billing/taxes/tax-rates) and [Checkout
Sessions](https://docs.stripe.com/payments/checkout/use-manual-tax-rates) to
collect tax.

Related guide: [Tax rates](https://docs.stripe.com/billing/taxes/tax-rates)

Endpoints[POST/v1/tax_rates](https://docs.stripe.com/api/tax_rates/create)[POST/v1/tax_rates/:id](https://docs.stripe.com/api/tax_rates/update)[GET/v1/tax_rates/:id](https://docs.stripe.com/api/tax_rates/retrieve)[GET/v1/tax_rates](https://docs.stripe.com/api/tax_rates/list)
Show

# [Shipping Rates](https://docs.stripe.com/api/shipping_rates)

Shipping rates describe the price of shipping presented to your customers and
applied to a purchase. For more information, see [Charge for
shipping](https://docs.stripe.com/payments/during-payment/charge-shipping).

Endpoints[POST/v1/shipping_rates](https://docs.stripe.com/api/shipping_rates/create)[POST/v1/shipping_rates/:id](https://docs.stripe.com/api/shipping_rates/update)[GET/v1/shipping_rates/:id](https://docs.stripe.com/api/shipping_rates/retrieve)[GET/v1/shipping_rates](https://docs.stripe.com/api/shipping_rates/list)
Show

# [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)

A Checkout Session represents your customer’s session as they pay for one-time
purchases or subscriptions through
[Checkout](https://docs.stripe.com/payments/checkout) or [Payment
Links](https://docs.stripe.com/payments/payment-links). We recommend creating a
new Session each time your customer attempts to pay.

Once payment is successful, the Checkout Session will contain a reference to the
[Customer](https://docs.stripe.com/api/customers), and either the successful
[PaymentIntent](https://docs.stripe.com/api/payment_intents) or an active
[Subscription](https://docs.stripe.com/api/subscriptions).

You can create a Checkout Session on your server and redirect to its URL to
begin Checkout.

Related guide: [Checkout
quickstart](https://docs.stripe.com/checkout/quickstart)

Endpoints[POST/v1/checkout/sessions](https://docs.stripe.com/api/checkout/sessions/create)[POST/v1/checkout/sessions/:id](https://docs.stripe.com/api/checkout/sessions/update)[GET/v1/checkout/sessions/:id](https://docs.stripe.com/api/checkout/sessions/retrieve)[GET/v1/checkout/sessions/:id/line_items](https://docs.stripe.com/api/checkout/sessions/line_items)[GET/v1/checkout/sessions](https://docs.stripe.com/api/checkout/sessions/list)[POST/v1/checkout/sessions/:id/expire](https://docs.stripe.com/api/checkout/sessions/expire)
Show

# [Payment Link](https://docs.stripe.com/api/payment-link)

A payment link is a shareable URL that will take your customers to a hosted
payment page. A payment link can be shared and used multiple times.

When a customer opens a payment link it will open a new [checkout
session](https://docs.stripe.com/api/checkout/sessions) to render the payment
page. You can use [checkout session
events](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
to track payments through payment links.

Related guide: [Payment Links API](https://docs.stripe.com/payment-links)

Endpoints[POST/v1/payment_links](https://docs.stripe.com/api/payment-link/create)[POST/v1/payment_links/:id](https://docs.stripe.com/api/payment-link/update)[GET/v1/payment_links/:id/line_items](https://docs.stripe.com/api/payment-link/retrieve-line-items)[GET/v1/payment_links/:id](https://docs.stripe.com/api/payment-link/retrieve)[GET/v1/payment_links](https://docs.stripe.com/api/payment-link/list)
Show

# [Credit Note](https://docs.stripe.com/api/credit_notes)

Issue a credit note to adjust an invoice’s amount after the invoice is
finalized.

Related guide: [Credit
notes](https://docs.stripe.com/billing/invoices/credit-notes)

Endpoints[POST/v1/credit_notes](https://docs.stripe.com/api/credit_notes/create)[POST/v1/credit_notes/:id](https://docs.stripe.com/api/credit_notes/update)[GET/v1/credit_notes/:id/lines](https://docs.stripe.com/api/credit_notes/lines)[GET/v1/credit_notes/preview/lines](https://docs.stripe.com/api/credit_notes/preview_lines)[GET/v1/credit_notes/:id](https://docs.stripe.com/api/credit_notes/retrieve)[GET/v1/credit_notes](https://docs.stripe.com/api/credit_notes/list)[GET/v1/credit_notes/preview](https://docs.stripe.com/api/credit_notes/preview)[POST/v1/credit_notes/:id/void](https://docs.stripe.com/api/credit_notes/void)
Show

# [Customer Balance Transaction](https://docs.stripe.com/api/customer_balance_transactions)

Each customer has a
[Balance](https://docs.stripe.com/api/customers/object#customer_object-balance)
value, which denotes a debit or credit that’s automatically applied to their
next invoice upon finalization. You may modify the value directly by using the
[update customer API](https://docs.stripe.com/api/customers/update), or by
creating a Customer Balance Transaction, which increments or decrements the
customer’s `balance` by the specified `amount`.

Related guide: [Customer
balance](https://docs.stripe.com/billing/customer/balance)

Endpoints[POST/v1/customers/:id/balance_transactions](https://docs.stripe.com/api/customer_balance_transactions/create)[POST/v1/customers/:id/balance_transactions/:id](https://docs.stripe.com/api/customer_balance_transactions/update)[GET/v1/customers/:id/balance_transactions/:id](https://docs.stripe.com/api/customer_balance_transactions/retrieve)[GET/v1/customers/:id/balance_transactions](https://docs.stripe.com/api/customer_balance_transactions/list)
Show

# [Customer Portal Session](https://docs.stripe.com/api/customer_portal/sessions)

The Billing customer portal is a Stripe-hosted UI for subscription and billing
management.

A portal configuration describes the functionality and features that you want to
provide to your customers through the portal.

A portal session describes the instantiation of the customer portal for a
particular customer. By visiting the session’s URL, the customer can manage
their subscriptions and billing details. For security reasons, sessions are
short-lived and will expire if the customer does not visit the URL. Create
sessions on-demand when customers intend to manage their subscriptions and
billing details.

Related guide: [Customer
management](https://docs.stripe.com/customer-management)

Endpoints[POST/v1/billing_portal/sessions](https://docs.stripe.com/api/customer_portal/sessions/create)
Show

# [Customer Portal Configuration](https://docs.stripe.com/api/customer_portal/configurations)

A portal configuration describes the functionality and behavior of a portal
session.

Endpoints[POST/v1/billing_portal/configurations](https://docs.stripe.com/api/customer_portal/configurations/create)[POST/v1/billing_portal/configurations/:id](https://docs.stripe.com/api/customer_portal/configurations/update)[GET/v1/billing_portal/configurations/:id](https://docs.stripe.com/api/customer_portal/configurations/retrieve)[GET/v1/billing_portal/configurations](https://docs.stripe.com/api/customer_portal/configurations/list)
Show

# [Invoices](https://docs.stripe.com/api/invoices)

Invoices are statements of amounts owed by a customer, and are either generated
one-off, or generated periodically from a subscription.

They contain [invoice
items](https://docs.stripe.com/api/balance/balance_object#invoiceitems), and
proration adjustments that may be caused by subscription upgrades/downgrades (if
necessary).

If your invoice is configured to be billed through automatic charges, Stripe
automatically finalizes your invoice and attempts payment. Note that finalizing
the invoice, [when
automatic](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection),
does not happen immediately as the invoice is created. Stripe waits until one
hour after the last webhook was successfully sent (or the last webhook timed out
after failing). If you (and the platforms you may have connected to) have no
webhooks configured, Stripe waits one hour after creation to finalize the
invoice.

If your invoice is configured to be billed by sending an email, then based on
your [email settings](https://dashboard.stripe.com/account/billing/automatic),
Stripe will email the invoice to your customer and await payment. These emails
can contain a link to a hosted page to pay the invoice.

Stripe applies any customer credit on the account before determining the amount
due for the invoice (i.e., the amount that will be actually charged). If the
amount due for the invoice is less than Stripe’s [minimum allowed charge per
currency](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts),
the invoice is automatically marked paid, and we add the amount due to the
customer’s credit balance which is applied to the next invoice.

More details on the customer’s credit balance are
[here](https://docs.stripe.com/billing/customer/balance).

Related guide: [Send invoices to
customers](https://docs.stripe.com/billing/invoices/sending)

Endpoints[POST/v1/invoices](https://docs.stripe.com/api/invoices/create)[POST/v1/invoices/create_preview](https://docs.stripe.com/api/invoices/create_preview)[POST/v1/invoices/:id](https://docs.stripe.com/api/invoices/update)[GET/v1/invoices/:id](https://docs.stripe.com/api/invoices/retrieve)[GET/v1/invoices/upcoming](https://docs.stripe.com/api/invoices/upcoming)[GET/v1/invoices](https://docs.stripe.com/api/invoices/list)[DELETE/v1/invoices/:id](https://docs.stripe.com/api/invoices/delete)[POST/v1/invoices/:id/finalize](https://docs.stripe.com/api/invoices/finalize)[POST/v1/invoices/:id/mark_uncollectible](https://docs.stripe.com/api/invoices/mark_uncollectible)[POST/v1/invoices/:id/pay](https://docs.stripe.com/api/invoices/pay)[GET/v1/invoices/search](https://docs.stripe.com/api/invoices/search)[POST/v1/invoices/:id/send](https://docs.stripe.com/api/invoices/send)[POST/v1/invoices/:id/void](https://docs.stripe.com/api/invoices/void)
Show

# [Invoice Items](https://docs.stripe.com/api/invoiceitems)

Invoice Items represent the component lines of an
[invoice](https://docs.stripe.com/api/invoices). An invoice item is added to an
invoice by creating or updating it with an `invoice` field, at which point it
will be included as [an invoice line
item](https://docs.stripe.com/api/invoices/line_item) within
[invoice.lines](https://docs.stripe.com/api/invoices/object#invoice_object-lines).

Invoice Items can be created before you are ready to actually send the invoice.
This can be particularly useful when combined with a
[subscription](https://docs.stripe.com/api/subscriptions). Sometimes you want to
add a charge or credit to a customer, but actually charge or credit the
customer’s card only at the end of a regular billing cycle. This is useful for
combining several charges (to minimize per-transaction fees), or for having
Stripe tabulate your usage-based billing totals.

Related guides: [Integrate with the Invoicing
API](https://docs.stripe.com/invoicing/integration), [Subscription
Invoices](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items).

Endpoints[POST/v1/invoiceitems](https://docs.stripe.com/api/invoiceitems/create)[POST/v1/invoiceitems/:id](https://docs.stripe.com/api/invoiceitems/update)[GET/v1/invoiceitems/:id](https://docs.stripe.com/api/invoiceitems/retrieve)[GET/v1/invoiceitems](https://docs.stripe.com/api/invoiceitems/list)[DELETE/v1/invoiceitems/:id](https://docs.stripe.com/api/invoiceitems/delete)
Show

# [Invoice Line Item](https://docs.stripe.com/api/invoice-line-item)

Invoice Line Items represent the individual lines within an
[invoice](https://docs.stripe.com/api/invoices) and only exist within the
context of an invoice.

Each line item is backed by either an [invoice
item](https://docs.stripe.com/api/invoiceitems) or a [subscription
item](https://docs.stripe.com/api/subscription_items).

Endpoints[POST/v1/invoices/:id/lines/:id](https://docs.stripe.com/api/invoice-line-item/update)[GET/v1/invoices/:id/lines](https://docs.stripe.com/api/invoice-line-item/retrieve)[GET/v1/invoices/upcoming/lines](https://docs.stripe.com/api/invoice-line-item/invoices/upcoming/lines/retrieve)[POST/v1/invoices/:id/add_lines](https://docs.stripe.com/api/invoice-line-item/bulk)[POST/v1/invoices/:id/remove_lines](https://docs.stripe.com/api/invoice-line-item/invoices/remove-lines/bulk)[POST/v1/invoices/:id/update_lines](https://docs.stripe.com/api/invoice-line-item/invoices/update-lines/bulk)
Show

# [Invoice Rendering Templates](https://docs.stripe.com/api/invoice-rendering-template)

Invoice Rendering Templates are used to configure how invoices are rendered on
surfaces like the PDF. Invoice Rendering Templates can be created from within
the Dashboard, and they can be used over the API when creating invoices.

Endpoints[GET/v1/invoice_rendering_templates/:id](https://docs.stripe.com/api/invoice-rendering-template/retrieve)[GET/v1/invoice_rendering_templates](https://docs.stripe.com/api/invoice-rendering-template/list)[POST/v1/invoice_rendering_templates/:id/archive](https://docs.stripe.com/api/invoice-rendering-template/archive)[POST/v1/invoice_rendering_templates/:id/unarchive](https://docs.stripe.com/api/invoice-rendering-template/unarchive)
Show

# [Alerts](https://docs.stripe.com/api/billing/alert)

A billing alert is a resource that notifies you when a certain usage threshold
on a meter is crossed. For example, you might create a billing alert to notify
you when a certain user made 100 API requests.

Endpoints[POST/v1/billing/alerts](https://docs.stripe.com/api/billing/alert/create)[GET/v1/billing/alerts/:id](https://docs.stripe.com/api/billing/alert/retrieve)[GET/v1/billing/alerts](https://docs.stripe.com/api/billing/alert/list)[POST/v1/billing/alerts/:id/activate](https://docs.stripe.com/api/billing/alert/activate)[POST/v1/billing/alerts/:id/archive](https://docs.stripe.com/api/billing/alert/archive)[POST/v1/billing/alerts/:id/deactivate](https://docs.stripe.com/api/billing/alert/deactivate)
Show

# [Meters](https://docs.stripe.com/api/billing/meter)

Meters specify how to aggregate meter events over a billing period. Meter events
represent the actions that customers take in your system. Meters attach to
prices and form the basis of the bill.

Related guide: [Usage based
billing](https://docs.stripe.com/billing/subscriptions/usage-based)

Endpoints[POST/v1/billing/meters](https://docs.stripe.com/api/billing/meter/create)[POST/v1/billing/meters/:id](https://docs.stripe.com/api/billing/meter/update)[GET/v1/billing/meters/:id](https://docs.stripe.com/api/billing/meter/retrieve)[GET/v1/billing/meters](https://docs.stripe.com/api/billing/meter/list)[POST/v1/billing/meters/:id/deactivate](https://docs.stripe.com/api/billing/meter/deactivate)[POST/v1/billing/meters/:id/reactivate](https://docs.stripe.com/api/billing/meter/reactivate)
Show

# [Meter Events](https://docs.stripe.com/api/billing/meter-event)

Meter events represent actions that customers take in your system. You can use
meter events to bill a customer based on their usage. Meter events are
associated with billing meters, which define both the contents of the event’s
payload and how to aggregate those events.

Endpoints[POST/v1/billing/meter_events](https://docs.stripe.com/api/billing/meter-event/create)
Show

# [Meter Events](https://docs.stripe.com/api/v2/billing-meter) v2

[Learn more about calling API v2
endpoints.](https://docs.stripe.com/api-v2-overview)
Meter events are used to report customer usage of your product or service. Meter
events are associated with billing meters, which define the shape of the event’s
payload and how those events are aggregated. Meter events are processed
asynchronously, so they may not be immediately reflected in aggregates or on
upcoming invoices.

Endpoints[POST/v2/billing/meter_events](https://docs.stripe.com/api/v2/billing/meter-event/create)
Show

# [Meter Event Adjustment](https://docs.stripe.com/api/billing/meter-event-adjustment)

A billing meter event adjustment is a resource that allows you to cancel a meter
event. For example, you might create a billing meter event adjustment to cancel
a meter event that was created in error or attached to the wrong customer.

Endpoints[POST/v1/billing/meter_event_adjustments](https://docs.stripe.com/api/billing/meter-event-adjustment/create)
Show

# [Meter Event Adjustment](https://docs.stripe.com/api/v2/billing-meter-adjustment) v2

[Learn more about calling API v2
endpoints.](https://docs.stripe.com/api-v2-overview)
A billing meter event adjustment is a resource that allows you to cancel a meter
event. For example, you might create a billing meter event adjustment to cancel
a meter event that was created in error or attached to the wrong customer.

Endpoints[POST/v2/billing/meter_event_adjustments](https://docs.stripe.com/api/v2/billing/meter-event-adjustments/create)
Show

# [Meter Event Stream](https://docs.stripe.com/api/v2/billing-meter-stream) v2

[Learn more about calling API v2
endpoints.](https://docs.stripe.com/api-v2-overview)
You can send a higher-throughput of meter events using meter event streams. For
this flow, you must first create a meter event session, which will provide you
with a session token. You can then create meter events through the meter event
stream endpoint, using the session token for authentication. The session tokens
are short-lived and you will need to create a new meter event session when the
token expires.

Endpoints[POST/v2/billing/meter_event_session](https://docs.stripe.com/api/v2/billing/meter-event-stream/session/create)[POST/v2/billing/meter_event_stream](https://docs.stripe.com/api/v2/billing/meter-event-stream/create)
Show

# [Meter Event Summary](https://docs.stripe.com/api/billing/meter-event-summary)

A billing meter event summary represents an aggregated view of a customer’s
billing meter events within a specified timeframe. It indicates how much usage
was accrued by a customer for that period.

Note: Meters events are aggregated asynchronously so the meter event summaries
provide an eventually consistent view of the reported usage.

Endpoints[GET/v1/billing/meters/:id/event_summaries](https://docs.stripe.com/api/billing/meter-event-summary/list)
Show

# [Credit Grant](https://docs.stripe.com/api/billing/credit-grant)

A credit grant is an API resource that documents the allocation of some billing
credits to a customer.

Related guide: [Billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)

Endpoints[POST/v1/billing/credit_grants](https://docs.stripe.com/api/billing/credit-grant/create)[POST/v1/billing/credit_grants/:id](https://docs.stripe.com/api/billing/credit-grant/update)[GET/v1/billing/credit_grants/:id](https://docs.stripe.com/api/billing/credit-grant/retrieve)[GET/v1/billing/credit_grants](https://docs.stripe.com/api/billing/credit-grant/list)[POST/v1/billing/credit_grants/:id/expire](https://docs.stripe.com/api/billing/credit-grant/expire)[POST/v1/billing/credit_grants/:id/void](https://docs.stripe.com/api/billing/credit-grant/void)
Show

# [Credit Balance Summary](https://docs.stripe.com/api/billing/credit-balance-summary)

Indicates the billing credit balance for billing credits granted to a customer.

Endpoints[GET/v1/billing/credit_balance_summary](https://docs.stripe.com/api/billing/credit-balance-summary/retrieve)
Show

# [Credit Balance Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction)

A credit balance transaction is a resource representing a transaction (either a
credit or a debit) against an existing credit grant.

Endpoints[GET/v1/billing/credit_balance_transactions/:id](https://docs.stripe.com/api/billing/credit-balance-transaction/retrieve)[GET/v1/billing/credit_balance_transactions](https://docs.stripe.com/api/billing/credit-balance-transaction/list)
Show

# [Plans](https://docs.stripe.com/api/plans)

You can now model subscriptions more flexibly using the [Prices
API](https://docs.stripe.com/api/balance/balance_object#prices). It replaces the
Plans API and is backwards compatible to simplify your migration.

Plans define the base price, currency, and billing cycle for recurring purchases
of products.
[Products](https://docs.stripe.com/api/balance/balance_object#products) help you
track inventory or provisioning, and plans help you track pricing. Different
physical goods or levels of service should be represented by products, and
pricing options should be represented by plans. This approach lets you change
prices without having to change your provisioning scheme.

For example, you might have a single “gold” product that has plans for
$10/month, $100/year, €9/month, and €90/year.

Related guides: [Set up a
subscription](https://docs.stripe.com/billing/subscriptions/set-up-subscription)
and more about [products and
prices](https://docs.stripe.com/products-prices/overview).

Endpoints[POST/v1/plans](https://docs.stripe.com/api/plans/create)[POST/v1/plans/:id](https://docs.stripe.com/api/plans/update)[GET/v1/plans/:id](https://docs.stripe.com/api/plans/retrieve)[GET/v1/plans](https://docs.stripe.com/api/plans/list)[DELETE/v1/plans/:id](https://docs.stripe.com/api/plans/delete)
Show

# [Quote](https://docs.stripe.com/api/quotes)

A Quote is a way to model prices that you’d like to provide to a customer. Once
accepted, it will automatically create an invoice, subscription or subscription
schedule.

Endpoints[POST/v1/quotes](https://docs.stripe.com/api/quotes/create)[POST/v1/quotes/:id](https://docs.stripe.com/api/quotes/update)[GET/v1/quotes/:id/line_items](https://docs.stripe.com/api/quotes/line_items/list)[GET/v1/quotes/:id/computed_upfront_line_items](https://docs.stripe.com/api/quotes/line_items/upfront/list)[GET/v1/quotes/:id](https://docs.stripe.com/api/quotes/retrieve)[GET/v1/quotes](https://docs.stripe.com/api/quotes/list)[POST/v1/quotes/:id/accept](https://docs.stripe.com/api/quotes/accept)[POST/v1/quotes/:id/cancel](https://docs.stripe.com/api/quotes/cancel)[GET/v1/quotes/:id/pdf](https://docs.stripe.com/api/quotes/pdf)[POST/v1/quotes/:id/finalize](https://docs.stripe.com/api/quotes/finalize)
Show

# [Subscriptions](https://docs.stripe.com/api/subscriptions)

Subscriptions allow you to charge a customer on a recurring basis.

Related guide: [Creating
subscriptions](https://docs.stripe.com/billing/subscriptions/creating)

Endpoints[POST/v1/subscriptions](https://docs.stripe.com/api/subscriptions/create)[POST/v1/subscriptions/:id](https://docs.stripe.com/api/subscriptions/update)[GET/v1/subscriptions/:id](https://docs.stripe.com/api/subscriptions/retrieve)[GET/v1/subscriptions](https://docs.stripe.com/api/subscriptions/list)[DELETE/v1/subscriptions/:id](https://docs.stripe.com/api/subscriptions/cancel)[POST/v1/subscriptions/:id/resume](https://docs.stripe.com/api/subscriptions/resume)[GET/v1/subscriptions/search](https://docs.stripe.com/api/subscriptions/search)
Show

# [Subscription Items](https://docs.stripe.com/api/subscription_items)

Subscription items allow you to create customer subscriptions with more than one
plan, making it easy to represent complex billing relationships.

Endpoints[POST/v1/subscription_items](https://docs.stripe.com/api/subscription_items/create)[POST/v1/subscription_items/:id](https://docs.stripe.com/api/subscription_items/update)[GET/v1/subscription_items/:id](https://docs.stripe.com/api/subscription_items/retrieve)[GET/v1/subscription_items](https://docs.stripe.com/api/subscription_items/list)[DELETE/v1/subscription_items/:id](https://docs.stripe.com/api/subscription_items/delete)
Show

# [Subscription Schedule](https://docs.stripe.com/api/subscription_schedules)

A subscription schedule allows you to create and manage the lifecycle of a
subscription by predefining expected changes.

Related guide: [Subscription
schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules)

Endpoints[POST/v1/subscription_schedules](https://docs.stripe.com/api/subscription_schedules/create)[POST/v1/subscription_schedules/:id](https://docs.stripe.com/api/subscription_schedules/update)[GET/v1/subscription_schedules/:id](https://docs.stripe.com/api/subscription_schedules/retrieve)[GET/v1/subscription_schedules](https://docs.stripe.com/api/subscription_schedules/list)[POST/v1/subscription_schedules/:id/cancel](https://docs.stripe.com/api/subscription_schedules/cancel)[POST/v1/subscription_schedules/:id/release](https://docs.stripe.com/api/subscription_schedules/release)
Show

# [Tax IDs](https://docs.stripe.com/api/tax_ids)

You can add one or multiple tax IDs to a
[customer](https://docs.stripe.com/api/customers) or account. Customer and
account tax IDs get displayed on related invoices and credit notes.

Related guides: [Customer tax identification
numbers](https://docs.stripe.com/billing/taxes/tax-ids), [Account tax
IDs](https://docs.stripe.com/invoicing/connect#account-tax-ids)

Endpoints[POST/v1/customers/:id/tax_ids](https://docs.stripe.com/api/tax_ids/customer_create)[POST/v1/tax_ids](https://docs.stripe.com/api/tax_ids/create)[GET/v1/customers/:id/tax_ids/:id](https://docs.stripe.com/api/tax_ids/customer_retrieve)[GET/v1/tax_ids/:id](https://docs.stripe.com/api/tax_ids/retrieve)[GET/v1/customers/:id/tax_ids](https://docs.stripe.com/api/tax_ids/customer_list)[GET/v1/tax_ids](https://docs.stripe.com/api/tax_ids/list)[DELETE/v1/customers/:id/tax_ids/:id](https://docs.stripe.com/api/tax_ids/customer_delete)[DELETE/v1/tax_ids/:id](https://docs.stripe.com/api/tax_ids/delete)
Show

# [Test Clocks](https://docs.stripe.com/api/test_clocks) Test helper

A test clock enables deterministic control over objects in testmode. With a test
clock, you can create objects at a frozen time in the past or future, and
advance to a specific future time to observe webhooks and state changes. After
the clock advances, you can either validate the current state of your scenario
(and test your assumptions), change the current state of your scenario (and test
more complex scenarios), or keep advancing forward in time.

Endpoints[POST/v1/test_helpers/test_clocks](https://docs.stripe.com/api/test_clocks/create)[GET/v1/test_helpers/test_clocks/:id](https://docs.stripe.com/api/test_clocks/retrieve)[GET/v1/test_helpers/test_clocks](https://docs.stripe.com/api/test_clocks/list)[DELETE/v1/test_helpers/test_clocks/:id](https://docs.stripe.com/api/test_clocks/delete)[POST/v1/test_helpers/test_clocks/:id/advance](https://docs.stripe.com/api/test_clocks/advance)
Show

# [Usage Records](https://docs.stripe.com/api/usage_records)

Usage records allow you to report customer usage and metrics to Stripe for
metered billing of subscription prices.

Related guide: [Metered
billing](https://docs.stripe.com/billing/subscriptions/metered-billing)

This is our legacy usage-based billing API. See the [updated usage-based billing
docs](https://docs.stripe.com/billing/subscriptions/usage-based).

Endpoints[POST/v1/subscription_items/:id/usage_records](https://docs.stripe.com/api/usage_records/create)
Show

# [Usage Record Summary](https://docs.stripe.com/api/usage-record-summary)

A usage record summary represents an aggregated view of how much usage was
accrued for a subscription item within a subscription billing period.

Endpoints[GET/v1/subscription_items/:id/usage_record_summaries](https://docs.stripe.com/api/usage-record-summary/list)
Show

# [Financing Offer](https://docs.stripe.com/api/capital/financing_offers) Preview feature

This is an object representing an offer of financing from Stripe Capital to a
Connect subaccount.

Endpoints[GET/v1/capital/financing_offers/:id](https://docs.stripe.com/api/capital/financing_offers/retrieve)[GET/v1/capital/financing_offers](https://docs.stripe.com/api/capital/financing_offers/list)[POST/v1/capital/financing_offers/:id/mark_delivered](https://docs.stripe.com/api/capital/financing_offers/mark_delivered)
Show

# [Financing Summary](https://docs.stripe.com/api/capital/financing_summary) Preview feature

A financing object describes an account’s current financing state. Used by
Connect platforms to read the state of Capital offered to their connected
accounts.

Endpoints[GET/v1/capital/financing_summary](https://docs.stripe.com/api/capital/financing_summary/retrieve)
Show

# [Accounts](https://docs.stripe.com/api/accounts)

This is an object representing a Stripe account. You can retrieve it to see
properties on the account like its current requirements or if the account is
enabled to make live charges or receive payouts.

For accounts where
[controller.requirement_collection](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
is `application`, which includes Custom accounts, the properties below are
always returned.

For accounts where
[controller.requirement_collection](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
is `stripe`, which includes Standard and Express accounts, some properties are
only returned until you create an [Account
Link](https://docs.stripe.com/api/account_links) or [Account
Session](https://docs.stripe.com/api/account_sessions) to start Connect
Onboarding. Learn about the [differences between
accounts](https://docs.stripe.com/connect/accounts).

Endpoints[POST/v1/accounts](https://docs.stripe.com/api/accounts/create)[POST/v1/accounts/:id](https://docs.stripe.com/api/accounts/update)[GET/v1/accounts/:id](https://docs.stripe.com/api/accounts/retrieve)[GET/v1/accounts](https://docs.stripe.com/api/accounts/list)[DELETE/v1/accounts/:id](https://docs.stripe.com/api/accounts/delete)[POST/v1/accounts/:id/reject](https://docs.stripe.com/api/account/reject)
Show

# [Login Links](https://docs.stripe.com/api/accounts/login_link)

Login Links are single-use URLs for a connected account to access the Express
Dashboard. The connected account’s
[account.controller.stripe_dashboard.type](https://docs.stripe.com/api/accounts/object#account_object-controller-stripe_dashboard-type)
must be `express` to have access to the Express Dashboard.

Endpoints[POST/v1/accounts/:id/login_links](https://docs.stripe.com/api/accounts/login_link/create)
Show

# [Account Links](https://docs.stripe.com/api/account_links)

Account Links are the means by which a Connect platform grants a connected
account permission to access Stripe-hosted applications, such as Connect
Onboarding.

Related guide: [Connect
Onboarding](https://docs.stripe.com/connect/custom/hosted-onboarding)

Endpoints[POST/v1/account_links](https://docs.stripe.com/api/account_links/create)
Show

# [Account Session](https://docs.stripe.com/api/account_sessions)

An AccountSession allows a Connect platform to grant access to a connected
account in Connect embedded components.

We recommend that you create an AccountSession each time you need to display an
embedded component to your user. Do not save AccountSessions to your database as
they expire relatively quickly, and cannot be used more than once.

Related guide: [Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)

Endpoints[POST/v1/account_sessions](https://docs.stripe.com/api/account_sessions/create)
Show

# [Application Fees](https://docs.stripe.com/api/application_fees)

When you collect a transaction fee on top of a charge made for your user (using
[Connect](https://docs.stripe.com/connect)), an `Application Fee` object is
created in your account. You can list, retrieve, and refund application fees.

Related guide: [Collecting application
fees](https://docs.stripe.com/connect/direct-charges#collect-fees)

Endpoints[GET/v1/application_fees/:id](https://docs.stripe.com/api/application_fees/retrieve)[GET/v1/application_fees](https://docs.stripe.com/api/application_fees/list)
Show

# [Application Fee Refunds](https://docs.stripe.com/api/fee_refunds)

`Application Fee Refund` objects allow you to refund an application fee that has
previously been created but not yet refunded. Funds will be refunded to the
Stripe account from which the fee was originally collected.

Related guide: [Refunding application
fees](https://docs.stripe.com/connect/destination-charges#refunding-app-fee)

Endpoints[POST/v1/application_fees/:id/refunds](https://docs.stripe.com/api/fee_refunds/create)[POST/v1/application_fees/:id/refunds/:id](https://docs.stripe.com/api/fee_refunds/update)[GET/v1/application_fees/:id/refunds/:id](https://docs.stripe.com/api/fee_refunds/retrieve)[GET/v1/application_fees/:id/refunds](https://docs.stripe.com/api/fee_refunds/list)
Show

# [Capabilities](https://docs.stripe.com/api/capabilities)

This is an object representing a capability for a Stripe account.

Related guide: [Account
capabilities](https://docs.stripe.com/connect/account-capabilities)

Endpoints[POST/v1/accounts/:id/capabilities/:id](https://docs.stripe.com/api/capabilities/update)[GET/v1/accounts/:id/capabilities/:id](https://docs.stripe.com/api/capabilities/retrieve)[GET/v1/accounts/:id/capabilities](https://docs.stripe.com/api/capabilities/list)
Show

# [Country Specs](https://docs.stripe.com/api/country_specs)

Stripe needs to collect certain pieces of information about each account
created. These requirements can differ depending on the account’s country. The
Country Specs API makes these rules available to your integration.

You can also view the information from this API call as [an online
guide](https://docs.stripe.com/connect/required-verification-information).

Endpoints[GET/v1/country_specs/:id](https://docs.stripe.com/api/country_specs/retrieve)[GET/v1/country_specs](https://docs.stripe.com/api/country_specs/list)
Show

# [External Bank Accounts](https://docs.stripe.com/api/external_accounts)

External bank accounts are financial accounts associated with a Stripe
platform’s connected accounts for the purpose of transferring funds to or from
the connected account’s Stripe balance.

Endpoints[POST/v1/accounts/:id/external_accounts](https://docs.stripe.com/api/external_account_bank_accounts/create)[POST/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_bank_accounts/update)[GET/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_bank_accounts/retrieve)[GET/v1/accounts/:id/external_accounts](https://docs.stripe.com/api/external_account_bank_accounts/list)[DELETE/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_bank_accounts/delete)
Show

# [External Account Cards](https://docs.stripe.com/api/external_account_cards)

External account cards are debit cards associated with a Stripe platform’s
connected accounts for the purpose of transferring funds to or from the
connected accounts Stripe balance.

Endpoints[POST/v1/accounts/:id/external_accounts](https://docs.stripe.com/api/external_account_cards/create)[POST/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_cards/update)[GET/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_cards/retrieve)[GET/v1/accounts/:id/external_accounts](https://docs.stripe.com/api/external_account_cards/list)[DELETE/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_cards/delete)
Show

# [Person](https://docs.stripe.com/api/persons)

This is an object representing a person associated with a Stripe account.

A platform cannot access a person for an account where
[account.controller.requirement_collection](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
is `stripe`, which includes Standard and Express accounts, after creating an
Account Link or Account Session to start Connect onboarding.

See the [Standard onboarding](https://docs.stripe.com/connect/standard-accounts)
or [Express onboarding](https://docs.stripe.com/connect/express-accounts)
documentation for information about prefilling information and account
onboarding steps. Learn more about [handling identity verification with the
API](https://docs.stripe.com/connect/handling-api-verification#person-information).

Endpoints[POST/v1/accounts/:id/persons](https://docs.stripe.com/api/persons/create)[POST/v1/accounts/:id/persons/:id](https://docs.stripe.com/api/persons/update)[GET/v1/accounts/:id/persons/:id](https://docs.stripe.com/api/persons/retrieve)[GET/v1/accounts/:id/persons](https://docs.stripe.com/api/persons/list)[DELETE/v1/accounts/:id/persons/:id](https://docs.stripe.com/api/persons/delete)
Show

# [Top-ups](https://docs.stripe.com/api/topups)

To top up your Stripe balance, you create a top-up object. You can retrieve
individual top-ups, as well as list all top-ups. Top-ups are identified by a
unique, random ID.

Related guide: [Topping up your platform
account](https://docs.stripe.com/connect/top-ups)

Endpoints[POST/v1/topups](https://docs.stripe.com/api/topups/create)[POST/v1/topups/:id](https://docs.stripe.com/api/topups/update)[GET/v1/topups/:id](https://docs.stripe.com/api/topups/retrieve)[GET/v1/topups](https://docs.stripe.com/api/topups/list)[POST/v1/topups/:id/cancel](https://docs.stripe.com/api/topups/cancel)
Show

# [Transfers](https://docs.stripe.com/api/transfers)

A `Transfer` object is created when you move funds between Stripe accounts as
part of Connect.

Before April 6, 2017, transfers also represented movement of funds from a Stripe
account to a card or bank account. This behavior has since been split out into a
[Payout](https://docs.stripe.com/api/balance/balance_object#payout_object)
object, with corresponding payout endpoints. For more information, read about
the [transfer/payout split](https://docs.stripe.com/transfer-payout-split).

Related guide: [Creating separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)

Endpoints[POST/v1/transfers](https://docs.stripe.com/api/transfers/create)[POST/v1/transfers/:id](https://docs.stripe.com/api/transfers/update)[GET/v1/transfers/:id](https://docs.stripe.com/api/transfers/retrieve)[GET/v1/transfers](https://docs.stripe.com/api/transfers/list)
Show

# [Transfer Reversals](https://docs.stripe.com/api/transfer_reversals)

[Stripe Connect](https://docs.stripe.com/connect) platforms can reverse
transfers made to a connected account, either entirely or partially, and can
also specify whether to refund any related application fees. Transfer reversals
add to the platform’s balance and subtract from the destination account’s
balance.

Reversing a transfer that was made for a [destination
charge](https://docs.stripe.com/connect/destination-charges) is allowed only up
to the amount of the charge. It is possible to reverse a
[transfer_group](https://docs.stripe.com/connect/separate-charges-and-transfers#transfer-options)
transfer only if the destination account has enough balance to cover the
reversal.

Related guide: [Reverse
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers#reverse-transfers)

Endpoints[POST/v1/transfers/:id/reversals](https://docs.stripe.com/api/transfer_reversals/create)[POST/v1/transfers/:id/reversals/:id](https://docs.stripe.com/api/transfer_reversals/update)[GET/v1/transfers/:id/reversals/:id](https://docs.stripe.com/api/transfer_reversals/retrieve)[GET/v1/transfers/:id/reversals](https://docs.stripe.com/api/transfer_reversals/list)
Show

# [Secrets](https://docs.stripe.com/api/secret_management)

Secret Store is an API that allows Stripe Apps developers to securely persist
secrets for use by UI Extensions and app backends.

The primary resource in Secret Store is a `secret`. Other apps can’t view
secrets created by an app. Additionally, secrets are scoped to provide further
permission control.

All Dashboard users and the app backend share `account` scoped secrets. Use the
`account` scope for secrets that don’t change per-user, like a third-party API
key.

A `user` scoped secret is accessible by the app backend and one specific
Dashboard user. Use the `user` scope for per-user secrets like per-user OAuth
tokens, where different users might have different permissions.

Related guide: [Store data between page
reloads](https://docs.stripe.com/stripe-apps/store-auth-data-custom-objects)

Endpoints[GET/v1/apps/secrets](https://docs.stripe.com/api/apps/secret_store/list)[POST/v1/apps/secrets/delete](https://docs.stripe.com/api/apps/secret_store/delete)[GET/v1/apps/secrets/find](https://docs.stripe.com/api/apps/secret_store/find)[POST/v1/apps/secrets](https://docs.stripe.com/api/apps/secret_store/set)
Show

# [Early Fraud Warning](https://docs.stripe.com/api/radar/early_fraud_warnings)

An early fraud warning indicates that the card issuer has notified us that a
charge may be fraudulent.

Related guide: [Early fraud
warnings](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)

Endpoints[GET/v1/radar/early_fraud_warnings/:id](https://docs.stripe.com/api/radar/early_fraud_warnings/retrieve)[GET/v1/radar/early_fraud_warnings](https://docs.stripe.com/api/radar/early_fraud_warnings/list)
Show

# [Reviews](https://docs.stripe.com/api/radar/reviews)

Reviews can be used to supplement automated fraud detection with human
expertise.

Learn more about [Radar](https://docs.stripe.com/radar) and reviewing payments
[here](https://docs.stripe.com/radar/reviews).

Endpoints[GET/v1/reviews/:id](https://docs.stripe.com/api/radar/reviews/retrieve)[GET/v1/reviews](https://docs.stripe.com/api/radar/reviews/list)[POST/v1/reviews/:id/approve](https://docs.stripe.com/api/radar/reviews/approve)
Show

# [Value Lists](https://docs.stripe.com/api/radar/value_lists)

Value lists allow you to group values together which can then be referenced in
rules.

Related guide: [Default Stripe
lists](https://docs.stripe.com/radar/lists#managing-list-items)

Endpoints[POST/v1/radar/value_lists](https://docs.stripe.com/api/radar/value_lists/create)[POST/v1/radar/value_lists/:id](https://docs.stripe.com/api/radar/value_lists/update)[GET/v1/radar/value_lists/:id](https://docs.stripe.com/api/radar/value_lists/retrieve)[GET/v1/radar/value_lists](https://docs.stripe.com/api/radar/value_lists/list)[DELETE/v1/radar/value_lists/:id](https://docs.stripe.com/api/radar/value_lists/delete)
Show

# [Value List Items](https://docs.stripe.com/api/radar/value_list_items)

Value list items allow you to add specific values to a given Radar value list,
which can then be used in rules.

Related guide: [Managing list
items](https://docs.stripe.com/radar/lists#managing-list-items)

Endpoints[POST/v1/radar/value_list_items](https://docs.stripe.com/api/radar/value_list_items/create)[GET/v1/radar/value_list_items/:id](https://docs.stripe.com/api/radar/value_list_items/retrieve)[GET/v1/radar/value_list_items](https://docs.stripe.com/api/radar/value_list_items/list)[DELETE/v1/radar/value_list_items/:id](https://docs.stripe.com/api/radar/value_list_items/delete)
Show

# [Authorizations](https://docs.stripe.com/api/issuing/authorizations)

When an [issued card](https://docs.stripe.com/issuing) is used to make a
purchase, an Issuing `Authorization` object is created.
[Authorizations](https://docs.stripe.com/issuing/purchases/authorizations) must
be approved for the purchase to be completed successfully.

Related guide: [Issued card
authorizations](https://docs.stripe.com/issuing/purchases/authorizations)

Endpoints[POST/v1/issuing/authorizations/:id](https://docs.stripe.com/api/issuing/authorizations/update)[GET/v1/issuing/authorizations/:id](https://docs.stripe.com/api/issuing/authorizations/retrieve)[GET/v1/issuing/authorizations](https://docs.stripe.com/api/issuing/authorizations/list)[POST/v1/issuing/authorizations/:id/approve](https://docs.stripe.com/api/issuing/authorizations/approve)[POST/v1/issuing/authorizations/:id/decline](https://docs.stripe.com/api/issuing/authorizations/decline)[POST/v1/test_helpers/issuing/authorizations](https://docs.stripe.com/api/issuing/authorizations/test_mode_create)[POST/v1/test_helpers/issuing/authorizations/:id/capture](https://docs.stripe.com/api/issuing/authorizations/test_mode_capture)[POST/v1/test_helpers/issuing/authorizations/:id/expire](https://docs.stripe.com/api/issuing/authorizations/test_mode_expire)[POST/v1/test_helpers/issuing/authorizations/:id/finalize_amount](https://docs.stripe.com/api/issuing/authorizations/test_mode_finalize_amount)[POST/v1/test_helpers/issuing/authorizations/:id/increment](https://docs.stripe.com/api/issuing/authorizations/test_mode_increment)[POST/v1/test_helpers/issuing/authorizations/:id/fraud_challenges/respond](https://docs.stripe.com/api/issuing/authorizations/respond_to_fraud_challenges)[POST/v1/test_helpers/issuing/authorizations/:id/reverse](https://docs.stripe.com/api/issuing/authorizations/test_mode_reverse)
Show

# [Cardholders](https://docs.stripe.com/api/issuing/cardholders)

An Issuing `Cardholder` object represents an individual or business entity who
is [issued](https://docs.stripe.com/issuing) cards.

Related guide: [How to create a
cardholder](https://docs.stripe.com/issuing/cards/virtual/issue-cards#create-cardholder)

Endpoints[POST/v1/issuing/cardholders](https://docs.stripe.com/api/issuing/cardholders/create)[POST/v1/issuing/cardholders/:id](https://docs.stripe.com/api/issuing/cardholders/update)[GET/v1/issuing/cardholders/:id](https://docs.stripe.com/api/issuing/cardholders/retrieve)[GET/v1/issuing/cardholders](https://docs.stripe.com/api/issuing/cardholders/list)
Show

# [Cards](https://docs.stripe.com/api/issuing/cards)

You can [create physical or virtual cards](https://docs.stripe.com/issuing) that
are issued to cardholders.

Endpoints[POST/v1/issuing/cards](https://docs.stripe.com/api/issuing/cards/create)[POST/v1/issuing/cards/:id](https://docs.stripe.com/api/issuing/cards/update)[GET/v1/issuing/cards/:id](https://docs.stripe.com/api/issuing/cards/retrieve)[GET/v1/issuing/cards](https://docs.stripe.com/api/issuing/cards/list)[POST/v1/test_helpers/issuing/cards/:id/shipping/deliver](https://docs.stripe.com/api/issuing/cards/test_mode_deliver)[POST/v1/test_helpers/issuing/cards/:id/shipping/fail](https://docs.stripe.com/api/issuing/cards/test_mode_fail)[POST/v1/test_helpers/issuing/cards/:id/shipping/return](https://docs.stripe.com/api/issuing/cards/test_mode_return)[POST/v1/test_helpers/issuing/cards/:id/shipping/ship](https://docs.stripe.com/api/issuing/cards/test_mode_ship)[POST/v1/test_helpers/issuing/cards/:id/shipping/submit](https://docs.stripe.com/api/issuing/cards/test_mode_submit)
Show

# [Disputes](https://docs.stripe.com/api/issuing/disputes)

As a [card issuer](https://docs.stripe.com/issuing), you can dispute
transactions that the cardholder does not recognize, suspects to be fraudulent,
or has other issues with.

Related guide: [Issuing
disputes](https://docs.stripe.com/issuing/purchases/disputes)

Endpoints[POST/v1/issuing/disputes](https://docs.stripe.com/api/issuing/disputes/create)[POST/v1/issuing/disputes/:id](https://docs.stripe.com/api/issuing/disputes/update)[GET/v1/issuing/disputes/:id](https://docs.stripe.com/api/issuing/disputes/retrieve)[GET/v1/issuing/disputes](https://docs.stripe.com/api/issuing/disputes/list)[POST/v1/issuing/disputes/:id/submit](https://docs.stripe.com/api/issuing/dispute/submit)
Show

# [Funding Instructions](https://docs.stripe.com/api/issuing/funding_instructions)

Funding Instructions contain reusable bank account and routing information. Push
funds to these addresses via bank transfer to [top up Issuing
Balances](https://docs.stripe.com/issuing/funding/balance).

Endpoints[POST/v1/issuing/funding_instructions](https://docs.stripe.com/api/issuing/funding_instructions/create)[GET/v1/issuing/funding_instructions](https://docs.stripe.com/api/issuing/funding_instructions/list)[POST/v1/test_helpers/issuing/fund_balance](https://docs.stripe.com/api/issuing/funding_instructions/fund)
Show

# [Personalization Designs](https://docs.stripe.com/api/issuing/personalization_designs)

A Personalization Design is a logical grouping of a Physical Bundle, card logo,
and carrier text that represents a product line.

Endpoints[POST/v1/issuing/personalization_designs](https://docs.stripe.com/api/issuing/personalization_designs/create)[POST/v1/issuing/personalization_designs/:id](https://docs.stripe.com/api/issuing/personalization_designs/update)[GET/v1/issuing/personalization_designs/:id](https://docs.stripe.com/api/issuing/personalization_designs/retrieve)[GET/v1/issuing/personalization_designs](https://docs.stripe.com/api/issuing/personalization_designs/list)[POST/v1/test_helpers/issuing/personalization_designs/:id/activate](https://docs.stripe.com/api/issuing/personalization_designs/activate_testmode)[POST/v1/test_helpers/issuing/personalization_designs/:id/deactivate](https://docs.stripe.com/api/issuing/personalization_designs/deactivate_testmode)[POST/v1/test_helpers/issuing/personalization_designs/:id/reject](https://docs.stripe.com/api/issuing/personalization_designs/reject_testmode)
Show

# [Physical Bundles](https://docs.stripe.com/api/issuing/physical_bundles)

A Physical Bundle represents the bundle of physical items - card stock, carrier
letter, and envelope - that is shipped to a cardholder when you create a
physical card.

Endpoints[GET/v1/issuing/physical_bundles/:id](https://docs.stripe.com/api/issuing/physical_bundles/retrieve)[GET/v1/issuing/physical_bundles](https://docs.stripe.com/api/issuing/physical_bundles/list)
Show

# [Tokens](https://docs.stripe.com/api/issuing/tokens) Preview feature

An issuing token object is created when an issued card is added to a digital
wallet. As a [card issuer](https://docs.stripe.com/issuing), you can [view and
manage these tokens](https://docs.stripe.com/issuing/controls/token-management)
through Stripe.

Endpoints[POST/v1/issuing/tokens/:id](https://docs.stripe.com/api/issuing/tokens/update)[GET/v1/issuing/tokens/:id](https://docs.stripe.com/api/issuing/tokens/retrieve)[GET/v1/issuing/tokens](https://docs.stripe.com/api/issuing/tokens/list)
Show

# [Transactions](https://docs.stripe.com/api/issuing/transactions)

Any use of an [issued card](https://docs.stripe.com/issuing) that results in
funds entering or leaving your Stripe account, such as a completed purchase or
refund, is represented by an Issuing `Transaction` object.

Related guide: [Issued card
transactions](https://docs.stripe.com/issuing/purchases/transactions)

Endpoints[POST/v1/issuing/transactions/:id](https://docs.stripe.com/api/issuing/transactions/update)[GET/v1/issuing/transactions/:id](https://docs.stripe.com/api/issuing/transactions/retrieve)[GET/v1/issuing/transactions](https://docs.stripe.com/api/issuing/transactions/list)[POST/v1/test_helpers/issuing/transactions/create_force_capture](https://docs.stripe.com/api/issuing/transactions/test_mode_create_force_capture)[POST/v1/test_helpers/issuing/transactions/create_unlinked_refund](https://docs.stripe.com/api/issuing/transactions/test_mode_create_unlinked_refund)[POST/v1/test_helpers/issuing/transactions/:id/refund](https://docs.stripe.com/api/issuing/transactions/test_mode_refund)
Show

# [Connection Token](https://docs.stripe.com/api/terminal/connection_tokens)

A Connection Token is used by the Stripe Terminal SDK to connect to a reader.

Related guide: [Fleet
management](https://docs.stripe.com/terminal/fleet/locations)

Endpoints[POST/v1/terminal/connection_tokens](https://docs.stripe.com/api/terminal/connection_tokens/create)
Show

# [Location](https://docs.stripe.com/api/terminal/locations)

A Location represents a grouping of readers.

Related guide: [Fleet
management](https://docs.stripe.com/terminal/fleet/locations)

Endpoints[POST/v1/terminal/locations](https://docs.stripe.com/api/terminal/locations/create)[POST/v1/terminal/locations/:id](https://docs.stripe.com/api/terminal/locations/update)[GET/v1/terminal/locations/:id](https://docs.stripe.com/api/terminal/locations/retrieve)[GET/v1/terminal/locations](https://docs.stripe.com/api/terminal/locations/list)[DELETE/v1/terminal/locations/:id](https://docs.stripe.com/api/terminal/locations/delete)
Show

# [Reader](https://docs.stripe.com/api/terminal/readers)

A Reader represents a physical device for accepting payment details.

Related guide: [Connecting to a
reader](https://docs.stripe.com/terminal/payments/connect-reader)

Endpoints[POST/v1/terminal/readers](https://docs.stripe.com/api/terminal/readers/create)[POST/v1/terminal/readers/:id](https://docs.stripe.com/api/terminal/readers/update)[GET/v1/terminal/readers/:id](https://docs.stripe.com/api/terminal/readers/retrieve)[GET/v1/terminal/readers](https://docs.stripe.com/api/terminal/readers/list)[DELETE/v1/terminal/readers/:id](https://docs.stripe.com/api/terminal/readers/delete)[POST/v1/terminal/readers/:id/cancel_action](https://docs.stripe.com/api/terminal/readers/cancel_action)[POST/v1/terminal/readers/:id/collect_inputs](https://docs.stripe.com/api/terminal/readers/collect_inputs)[POST/v1/terminal/readers/:id/confirm_payment_intent](https://docs.stripe.com/api/terminal/readers/confirm_payment_intent)[POST/v1/terminal/readers/:id/collect_payment_method](https://docs.stripe.com/api/terminal/readers/collect_payment_method)[POST/v1/terminal/readers/:id/process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent)[POST/v1/terminal/readers/:id/process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)[POST/v1/terminal/readers/:id/refund_payment](https://docs.stripe.com/api/terminal/readers/refund_payment)[POST/v1/terminal/readers/:id/set_reader_display](https://docs.stripe.com/api/terminal/readers/set_reader_display)[POST/v1/test_helpers/terminal/readers/:id/present_payment_method](https://docs.stripe.com/api/terminal/readers/present_payment_method)
Show

# [Terminal Hardware Order](https://docs.stripe.com/api/terminal/hardware_orders) Preview feature

A TerminalHardwareOrder represents an order for Terminal hardware, containing
information such as the price, shipping information and the items ordered.

Endpoints[POST/v1/terminal/hardware_orders](https://docs.stripe.com/api/terminal/hardware_orders/create)[GET/v1/terminal/hardware_orders/:id](https://docs.stripe.com/api/terminal/hardware_orders/retrieve)[GET/v1/terminal/hardware_orders](https://docs.stripe.com/api/terminal/hardware_orders/list)[POST/v1/terminal/hardware_orders/:id/cancel](https://docs.stripe.com/api/terminal/hardware_orders/cancel)[GET/v1/terminal/hardware_orders/preview](https://docs.stripe.com/api/terminal/hardware_orders/preview)[POST/v1/test_helpers/terminal/hardware_orders/:id/mark_ready_to_ship](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_mark_ready_to_ship)[POST/v1/test_helpers/terminal/hardware_orders/:id/deliver](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_deliver)[POST/v1/test_helpers/terminal/hardware_orders/:id/ship](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_ship)[POST/v1/test_helpers/terminal/hardware_orders/:id/mark_undeliverable](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_mark_undeliverable)
Show

# [Terminal Hardware Order Device](https://docs.stripe.com/api/terminal/hardware_order_devices) Preview feature

A TerminalHardwareOrderDevice represents a device from a Terminal Hardware
Order. A device is a single-quantity hardware item with a serial number.

Endpoints[GET/v1/terminal/hardware_order_devices/:id](https://docs.stripe.com/api/terminal/hardware_order_devices/retrieve)[GET/v1/terminal/hardware_order_devices](https://docs.stripe.com/api/terminal/hardware_order_devices/list)[POST/v1/test_helpers/terminal/hardware_order_devices/create_devices_for_order](https://docs.stripe.com/api/terminal/hardware_order_devices/test_mode_create_devices_for_order)
Show

# [Terminal Hardware Product](https://docs.stripe.com/api/terminal/hardware_products) Preview feature

A TerminalHardwareProduct is a category of hardware devices that are generally
similar, but may have variations depending on the country it’s shipped to.

TerminalHardwareSKUs represent variations within the same Product (for example,
a country specific device). For example, WisePOS E is a TerminalHardwareProduct
and a WisePOS E - US and WisePOS E - UK are TerminalHardwareSKUs.

Endpoints[GET/v1/terminal/hardware_products/:id](https://docs.stripe.com/api/terminal/hardware_products/retrieve)[GET/v1/terminal/hardware_products](https://docs.stripe.com/api/terminal/hardware_products/list)
Show

# [Terminal Hardware SKU](https://docs.stripe.com/api/terminal/hardware_skus) Preview feature

A TerminalHardwareSKU represents a SKU for Terminal hardware. A SKU is a
representation of a product available for purchase, containing information such
as the name, price, and images.

Endpoints[GET/v1/terminal/hardware_skus/:id](https://docs.stripe.com/api/terminal/hardware_skus/retrieve)[GET/v1/terminal/hardware_skus](https://docs.stripe.com/api/terminal/hardware_skus/list)
Show

# [Terminal Hardware Shipping Method](https://docs.stripe.com/api/terminal/hardware_shipping_methods) Preview feature

A TerminalHardwareShipping represents a Shipping Method for Terminal hardware. A
Shipping Method is a country-specific representation of a way to ship hardware,
containing information such as the country, name, and expected delivery date.

Endpoints[GET/v1/terminal/hardware_shipping_methods/:id](https://docs.stripe.com/api/terminal/hardware_shipping_methods/retrieve)[GET/v1/terminal/hardware_shipping_methods](https://docs.stripe.com/api/terminal/hardware_shipping_methods/list)
Show

# [Configuration](https://docs.stripe.com/api/terminal/configuration)

A Configurations object represents how features should be configured for
terminal readers.

Endpoints[POST/v1/terminal/configurations](https://docs.stripe.com/api/terminal/configuration/create)[POST/v1/terminal/configurations/:id](https://docs.stripe.com/api/terminal/configuration/update)[GET/v1/terminal/configurations/:id](https://docs.stripe.com/api/terminal/configuration/retrieve)[GET/v1/terminal/configurations](https://docs.stripe.com/api/terminal/configuration/list)[DELETE/v1/terminal/configurations/:id](https://docs.stripe.com/api/terminal/configuration/delete)
Show

# [Financial Accounts](https://docs.stripe.com/api/treasury/financial_accounts)

Stripe Treasury provides users with a container for money called a
FinancialAccount that is separate from their Payments balance. FinancialAccounts
serve as the source and destination of Treasury’s money movement APIs.

Endpoints[POST/v1/treasury/financial_accounts](https://docs.stripe.com/api/treasury/financial_accounts/create)[POST/v1/treasury/financial_accounts/:id](https://docs.stripe.com/api/treasury/financial_accounts/update)[GET/v1/treasury/financial_accounts/:id](https://docs.stripe.com/api/treasury/financial_accounts/retrieve)[GET/v1/treasury/financial_accounts](https://docs.stripe.com/api/treasury/financial_accounts/list)
Show

# [Financial Account Features](https://docs.stripe.com/api/treasury/financial_account_features)

Encodes whether a FinancialAccount has access to a particular Feature, with a
`status` enum and associated `status_details`. Stripe or the platform can
control Features via the requested field.

Endpoints[POST/v1/treasury/financial_accounts/:id/features](https://docs.stripe.com/api/treasury/financial_account_features/update)[GET/v1/treasury/financial_accounts/:id/features](https://docs.stripe.com/api/treasury/financial_account_features/retrieve)
Show

# [Transactions](https://docs.stripe.com/api/treasury/transactions)

Transactions represent changes to a
[FinancialAccount’s](https://docs.stripe.com/api/balance/balance_object#financial_accounts)
balance.

Endpoints[GET/v1/treasury/transactions/:id](https://docs.stripe.com/api/treasury/transactions/retrieve)[GET/v1/treasury/transactions](https://docs.stripe.com/api/treasury/transactions/list)
Show

# [Transaction Entries](https://docs.stripe.com/api/treasury/transaction_entries)

TransactionEntries represent individual units of money movements within a single
[Transaction](https://docs.stripe.com/api/balance/balance_object#transactions).

Endpoints[GET/v1/treasury/transaction_entries/:id](https://docs.stripe.com/api/treasury/transaction_entries/retrieve)[GET/v1/treasury/transaction_entries](https://docs.stripe.com/api/treasury/transaction_entries/list)
Show

# [Outbound Transfers](https://docs.stripe.com/api/treasury/outbound_transfers)

Use
[OutboundTransfers](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-transfers)
to transfer funds from a
[FinancialAccount](https://docs.stripe.com/api/balance/balance_object#financial_accounts)
to a PaymentMethod belonging to the same entity. To send funds to a different
party, use
[OutboundPayments](https://docs.stripe.com/api/balance/balance_object#outbound_payments)
instead. You can send funds over ACH rails or through a domestic wire transfer
to a user’s own external bank account.

Simulate OutboundTransfer state changes with the
`/v1/test_helpers/treasury/outbound_transfers` endpoints. These methods can only
be called on test mode objects.

Related guide: [Moving money with Treasury using OutboundTransfer
objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-transfers)

Endpoints[POST/v1/treasury/outbound_transfers](https://docs.stripe.com/api/treasury/outbound_transfers/create)[GET/v1/treasury/outbound_transfers/:id](https://docs.stripe.com/api/treasury/outbound_transfers/retrieve)[GET/v1/treasury/outbound_transfers](https://docs.stripe.com/api/treasury/outbound_transfers/list)[POST/v1/treasury/outbound_transfers/:id/cancel](https://docs.stripe.com/api/treasury/outbound_transfers/cancel)[POST/v1/test_helpers/treasury/outbound_transfers/:id/fail](https://docs.stripe.com/api/treasury/outbound_transfers/test_mode_fail)[POST/v1/test_helpers/treasury/outbound_transfers/:id/post](https://docs.stripe.com/api/treasury/outbound_transfers/test_mode_post)[POST/v1/test_helpers/treasury/outbound_transfers/:id/return](https://docs.stripe.com/api/treasury/outbound_transfers/test_mode_return)[POST/v1/test_helpers/treasury/outbound_transfers/:id](https://docs.stripe.com/api/treasury/outbound_transfers/test_mode_update)
Show

# [Outbound Payments](https://docs.stripe.com/api/treasury/outbound_payments)

Use
[OutboundPayments](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-payments)
to send funds to another party’s external bank account or
[FinancialAccount](https://docs.stripe.com/api/balance/balance_object#financial_accounts).
To send money to an account belonging to the same user, use an
[OutboundTransfer](https://docs.stripe.com/api/balance/balance_object#outbound_transfers).

Simulate OutboundPayment state changes with the
`/v1/test_helpers/treasury/outbound_payments` endpoints. These methods can only
be called on test mode objects.

Related guide: [Moving money with Treasury using OutboundPayment
objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-payments)

Endpoints[POST/v1/treasury/outbound_payments](https://docs.stripe.com/api/treasury/outbound_payments/create)[GET/v1/treasury/outbound_payments/:id](https://docs.stripe.com/api/treasury/outbound_payments/retrieve)[GET/v1/treasury/outbound_payments](https://docs.stripe.com/api/treasury/outbound_payments/list)[POST/v1/treasury/outbound_payments/:id/cancel](https://docs.stripe.com/api/treasury/outbound_payments/cancel)[POST/v1/test_helpers/treasury/outbound_payments/:id/fail](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_fail)[POST/v1/test_helpers/treasury/outbound_payments/:id/post](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_post)[POST/v1/test_helpers/treasury/outbound_payments/:id/return](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_return)[POST/v1/test_helpers/treasury/outbound_payments/:id](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_update)
Show

# [Inbound Transfers](https://docs.stripe.com/api/treasury/inbound_transfers)

Use
[InboundTransfers](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers)
to add funds to your
[FinancialAccount](https://docs.stripe.com/api/balance/balance_object#financial_accounts)
via a PaymentMethod that is owned by you. The funds will be transferred via an
ACH debit.

Related guide: [Moving money with Treasury using InboundTransfer
objects](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers)

Endpoints[POST/v1/treasury/inbound_transfers](https://docs.stripe.com/api/treasury/inbound_transfers/create)[GET/v1/treasury/inbound_transfers/:id](https://docs.stripe.com/api/treasury/inbound_transfers/retrieve)[GET/v1/treasury/inbound_transfers](https://docs.stripe.com/api/treasury/inbound_transfers/list)[POST/v1/treasury/inbound_transfers/:id/cancel](https://docs.stripe.com/api/treasury/inbound_transfers/cancel)[POST/v1/test_helpers/treasury/inbound_transfers/:id/fail](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_fail)[POST/v1/test_helpers/treasury/inbound_transfers/:id/return](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_return)[POST/v1/test_helpers/treasury/inbound_transfers/:id/succeed](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_succeed)
Show

# [Received Credits](https://docs.stripe.com/api/treasury/received_credits)

ReceivedCredits represent funds sent to a
[FinancialAccount](https://docs.stripe.com/api/balance/balance_object#financial_accounts)
(for example, via ACH or wire). These money movements are not initiated from the
FinancialAccount.

Endpoints[GET/v1/treasury/received_credits/:id](https://docs.stripe.com/api/treasury/received_credits/retrieve)[GET/v1/treasury/received_credits](https://docs.stripe.com/api/treasury/received_credits/list)[POST/v1/test_helpers/treasury/received_credits](https://docs.stripe.com/api/treasury/received_credits/test_mode_create)
Show

# [Received Debits](https://docs.stripe.com/api/treasury/received_debits)

ReceivedDebits represent funds pulled from a
[FinancialAccount](https://docs.stripe.com/api/balance/balance_object#financial_accounts).
These are not initiated from the FinancialAccount.

Endpoints[GET/v1/treasury/received_debits/:id](https://docs.stripe.com/api/treasury/received_debits/retrieve)[GET/v1/treasury/received_debits](https://docs.stripe.com/api/treasury/received_debits/list)[POST/v1/test_helpers/treasury/received_debits](https://docs.stripe.com/api/treasury/received_debits/test_mode_create)
Show

# [Credit Reversals](https://docs.stripe.com/api/treasury/credit_reversals)

You can reverse some
[ReceivedCredits](https://docs.stripe.com/api/balance/balance_object#received_credits)
depending on their network and source flow. Reversing a ReceivedCredit leads to
the creation of a new object known as a CreditReversal.

Endpoints[POST/v1/treasury/credit_reversals](https://docs.stripe.com/api/treasury/credit_reversals/create)[GET/v1/treasury/credit_reversals/:id](https://docs.stripe.com/api/treasury/credit_reversals/retrieve)[GET/v1/treasury/credit_reversals](https://docs.stripe.com/api/treasury/credit_reversals/list)
Show

# [Debit Reversals](https://docs.stripe.com/api/treasury/debit_reversals)

You can reverse some
[ReceivedDebits](https://docs.stripe.com/api/balance/balance_object#received_debits)
depending on their network and source flow. Reversing a ReceivedDebit leads to
the creation of a new object known as a DebitReversal.

Endpoints[POST/v1/treasury/debit_reversals](https://docs.stripe.com/api/treasury/debit_reversals/create)[GET/v1/treasury/debit_reversals/:id](https://docs.stripe.com/api/treasury/debit_reversals/retrieve)[GET/v1/treasury/debit_reversals](https://docs.stripe.com/api/treasury/debit_reversals/list)
Show

# [Feature](https://docs.stripe.com/api/entitlements/feature)

A feature represents a monetizable ability or functionality in your system.
Features can be assigned to products, and when those products are purchased,
Stripe will create an entitlement to the feature for the purchasing customer.

Endpoints[POST/v1/entitlements/features](https://docs.stripe.com/api/entitlements/feature/create)[GET/v1/entitlements/features](https://docs.stripe.com/api/entitlements/feature/list)[POST/v1/entitlements/features/:id](https://docs.stripe.com/api/entitlements/feature/updates)
Show

# [Product Feature](https://docs.stripe.com/api/product-feature)

A product_feature represents an attachment between a feature and a product. When
a product is purchased that has a feature attached, Stripe will create an
entitlement to the feature for the purchasing customer.

Endpoints[GET/v1/products/:id/features](https://docs.stripe.com/api/product-feature/list)[POST/v1/products/:id/features](https://docs.stripe.com/api/product-feature/attach)[DELETE/v1/products/:id/features/:id](https://docs.stripe.com/api/product-feature/remove)
Show

# [Active Entitlement](https://docs.stripe.com/api/entitlements/active-entitlement)

An active entitlement describes access to a feature for a customer.

Endpoints[GET/v1/entitlements/active_entitlements/:id](https://docs.stripe.com/api/entitlements/active-entitlement/retrieve)[GET/v1/entitlements/active_entitlements](https://docs.stripe.com/api/entitlements/active-entitlement/list)
Show

# [Scheduled Queries](https://docs.stripe.com/api/sigma/scheduled_queries)

If you have [scheduled a Sigma
query](https://docs.stripe.com/sigma/scheduled-queries), you’ll receive a
`sigma.scheduled_query_run.created` webhook each time the query runs. The
webhook contains a `ScheduledQueryRun` object, which you can use to retrieve the
query results.

Endpoints[GET/v1/sigma/scheduled_query_runs/:id](https://docs.stripe.com/api/sigma/scheduled_queries/retrieve)[GET/v1/sigma/scheduled_query_runs](https://docs.stripe.com/api/sigma/scheduled_queries/list)
Show

# [Report Runs](https://docs.stripe.com/api/reporting/report_run)

The Report Run object represents an instance of a report type generated with
specific run parameters. Once the object is created, Stripe begins processing
the report. When the report has finished running, it will give you a reference
to a file where you can retrieve your results. For an overview, see [API Access
to Reports](https://docs.stripe.com/reporting/statements/api).

Note that certain report types can only be run based on your live-mode data (not
test-mode data), and will error when queried without a [live-mode API
key](https://docs.stripe.com/keys#test-live-modes).

Endpoints[POST/v1/reporting/report_runs](https://docs.stripe.com/api/reporting/report_run/create)[GET/v1/reporting/report_runs/:id](https://docs.stripe.com/api/reporting/report_run/retrieve)[GET/v1/reporting/report_runs](https://docs.stripe.com/api/reporting/report_run/list)
Show

# [Report Types](https://docs.stripe.com/api/reporting/report_type)

The Report Type resource corresponds to a particular type of report, such as the
“Activity summary” or “Itemized payouts” reports. These objects are identified
by an ID belonging to a set of enumerated values. See [API Access to Reports
documentation](https://docs.stripe.com/reporting/statements/api) for those
Report Type IDs, along with required and optional parameters.

Note that certain report types can only be run based on your live-mode data (not
test-mode data), and will error when queried without a [live-mode API
key](https://docs.stripe.com/keys#test-live-modes).

Endpoints[GET/v1/reporting/report_types/:id](https://docs.stripe.com/api/reporting/report_type/retrieve)[GET/v1/reporting/report_types](https://docs.stripe.com/api/reporting/report_type/list)
Show

# [Accounts](https://docs.stripe.com/api/financial_connections/accounts)

A Financial Connections Account represents an account that exists outside of
Stripe, to which you have been granted some degree of access.

Endpoints[GET/v1/financial_connections/accounts/:id](https://docs.stripe.com/api/financial_connections/accounts/retrieve)[GET/v1/financial_connections/accounts](https://docs.stripe.com/api/financial_connections/accounts/list)[POST/v1/financial_connections/accounts/:id/disconnect](https://docs.stripe.com/api/financial_connections/accounts/disconnect)[POST/v1/financial_connections/accounts/:id/refresh](https://docs.stripe.com/api/financial_connections/accounts/refresh)[POST/v1/financial_connections/accounts/:id/subscribe](https://docs.stripe.com/api/financial_connections/accounts/subscribe)[POST/v1/financial_connections/accounts/:id/unsubscribe](https://docs.stripe.com/api/financial_connections/accounts/unsubscribe)
Show

# [Account Owner](https://docs.stripe.com/api/financial_connections/ownership)

Describes an owner of an account.

Endpoints[GET/v1/financial_connections/accounts/:id/owners](https://docs.stripe.com/api/financial_connections/ownership/list)
Show

# [Session](https://docs.stripe.com/api/financial_connections/sessions)

A Financial Connections Session is the secure way to programmatically launch the
client-side Stripe.js modal that lets your users link their accounts.

Endpoints[POST/v1/financial_connections/sessions](https://docs.stripe.com/api/financial_connections/sessions/create)[GET/v1/financial_connections/sessions/:id](https://docs.stripe.com/api/financial_connections/sessions/retrieve)
Show

# [Transactions](https://docs.stripe.com/api/financial_connections/transactions)

A Transaction represents a real transaction that affects a Financial Connections
Account balance.

Endpoints[GET/v1/financial_connections/transactions/:id](https://docs.stripe.com/api/financial-connections/transaction/retrieve)[GET/v1/financial_connections/transactions](https://docs.stripe.com/api/financial_connections/transactions/list)
Show

# [Tax Calculations](https://docs.stripe.com/api/tax/calculations)

A Tax Calculation allows you to calculate the tax to collect from your customer.

Related guide: [Calculate tax in your custom payment
flow](https://docs.stripe.com/tax/custom)

Endpoints[POST/v1/tax/calculations](https://docs.stripe.com/api/tax/calculations/create)[GET/v1/tax/calculations/:id/line_items](https://docs.stripe.com/api/tax/calculations/line_items)[GET/v1/tax/calculations/:id](https://docs.stripe.com/api/tax/calculations/retrieve)
Show

# [Tax Registrations](https://docs.stripe.com/api/tax/registrations)

A Tax `Registration` lets us know that your business is registered to collect
tax on payments within a region, enabling you to [automatically collect
tax](https://docs.stripe.com/tax).

Stripe doesn’t register on your behalf with the relevant authorities when you
create a Tax `Registration` object. For more information on how to register to
collect tax, see [our guide](https://docs.stripe.com/tax/registering).

Related guide: [Using the Registrations
API](https://docs.stripe.com/tax/registrations-api)

Endpoints[POST/v1/tax/registrations](https://docs.stripe.com/api/tax/registrations/create)[POST/v1/tax/registrations/:id](https://docs.stripe.com/api/tax/registrations/update)[GET/v1/tax/registrations/:id](https://docs.stripe.com/api/tax/registrations/retrieve)[GET/v1/tax/registrations](https://docs.stripe.com/api/tax/registrations/all)
Show

# [Tax Transactions](https://docs.stripe.com/api/tax/transactions)

A Tax Transaction records the tax collected from or refunded to your customer.

Related guide: [Calculate tax in your custom payment
flow](https://docs.stripe.com/tax/custom#tax-transaction)

Endpoints[POST/v1/tax/transactions/create_reversal](https://docs.stripe.com/api/tax/transactions/create_reversal)[POST/v1/tax/transactions/create_from_calculation](https://docs.stripe.com/api/tax/transactions/create_from_calculation)[GET/v1/tax/transactions/:id/line_items](https://docs.stripe.com/api/tax/transactions/line_items)[GET/v1/tax/transactions/:id](https://docs.stripe.com/api/tax/transactions/retrieve)
Show

# [Tax Settings](https://docs.stripe.com/api/tax/settings)

You can use Tax `Settings` to manage configurations used by Stripe Tax
calculations.

Related guide: [Using the Settings
API](https://docs.stripe.com/tax/settings-api)

Endpoints[POST/v1/tax/settings](https://docs.stripe.com/api/tax/settings/update)[GET/v1/tax/settings](https://docs.stripe.com/api/tax/settings/retrieve)
Show

# [Verification Session](https://docs.stripe.com/api/identity/verification_sessions)

A VerificationSession guides you through the process of collecting and verifying
the identities of your users. It contains details about the type of
verification, such as what [verification
check](https://docs.stripe.com/identity/verification-checks) to perform. Only
create one VerificationSession for each verification in your system.

A VerificationSession transitions through [multiple
statuses](https://docs.stripe.com/identity/how-sessions-work) throughout its
lifetime as it progresses through the verification flow. The VerificationSession
contains the user’s verified data after verification checks are complete.

Related guide: [The Verification Sessions
API](https://docs.stripe.com/identity/verification-sessions)

Endpoints[POST/v1/identity/verification_sessions](https://docs.stripe.com/api/identity/verification_sessions/create)[POST/v1/identity/verification_sessions/:id](https://docs.stripe.com/api/identity/verification_sessions/update)[GET/v1/identity/verification_sessions/:id](https://docs.stripe.com/api/identity/verification_sessions/retrieve)[GET/v1/identity/verification_sessions](https://docs.stripe.com/api/identity/verification_sessions/list)[POST/v1/identity/verification_sessions/:id/cancel](https://docs.stripe.com/api/identity/verification_sessions/cancel)[POST/v1/identity/verification_sessions/:id/redact](https://docs.stripe.com/api/identity/verification_sessions/redact)
Show

# [Verification Report](https://docs.stripe.com/api/identity/verification_reports)

A VerificationReport is the result of an attempt to collect and verify data from
a user. The collection of verification checks performed is determined from the
`type` and `options` parameters used. You can find the result of each
verification check performed in the appropriate sub-resource: `document`,
`id_number`, `selfie`.

Each VerificationReport contains a copy of any data collected by the user as
well as reference IDs which can be used to access collected images through the
[FileUpload](https://docs.stripe.com/api/files) API. To configure and create
VerificationReports, use the
[VerificationSession](https://docs.stripe.com/api/identity/verification_sessions)
API.

Related guide: [Accessing verification
results](https://docs.stripe.com/identity/verification-sessions#results).

Endpoints[GET/v1/identity/verification_reports/:id](https://docs.stripe.com/api/identity/verification_reports/retrieve)[GET/v1/identity/verification_reports](https://docs.stripe.com/api/identity/verification_reports/list)
Show

# [Crypto Onramp Session](https://docs.stripe.com/api/crypto/onramp_sessions)

A Crypto Onramp Session represents your customer’s session as they purchase
cryptocurrency through Stripe. Once payment is successful, Stripe will fulfill
the delivery of cryptocurrency to your user’s wallet and contain a reference to
the crypto transaction ID.

You can create an onramp session on your server and embed the widget on your
frontend. Alternatively, you can redirect your users to the standalone hosted
onramp.

Related guide: [Integrate the
onramp](https://docs.stripe.com/crypto/integrate-the-onramp)

Endpoints[POST/v1/crypto/onramp_sessions](https://docs.stripe.com/api/crypto/onramp_sessions/create)[GET/v1/crypto/onramp_sessions/:id](https://docs.stripe.com/api/crypto/onramp_sessions/retrieve)[GET/v1/crypto/onramp_sessions](https://docs.stripe.com/api/crypto/onramp_sessions/list)
Show

# [Crypto Onramp Quotes](https://docs.stripe.com/api/crypto/onramp_quotes)

Crypto Onramp Quotes are estimated quotes for onramp conversions into all the
different cryptocurrencies on different networks. The Quotes API allows you to
display quotes in your product UI before directing the user to the onramp
widget.

Related guide: [Quotes API](https://docs.stripe.com/crypto/quotes-api)

Endpoints[GET/v1/crypto/onramp/quotes](https://docs.stripe.com/api/crypto/onramp_quotes/retrieve)
Show

# [Climate Order](https://docs.stripe.com/api/climate/order)

Orders represent your intent to purchase a particular Climate product. When you
create an order, the payment is deducted from your merchant balance.

Endpoints[POST/v1/climate/orders](https://docs.stripe.com/api/climate/order/create)[POST/v1/climate/orders/:id](https://docs.stripe.com/api/climate/order/update)[GET/v1/climate/orders/:id](https://docs.stripe.com/api/climate/order/retrieve)[GET/v1/climate/orders](https://docs.stripe.com/api/climate/order/list)[POST/v1/climate/orders/:id/cancel](https://docs.stripe.com/api/climate/order/cancel)
Show

# [Climate Product](https://docs.stripe.com/api/climate/product)

A Climate product represents a type of carbon removal unit available for
reservation. You can retrieve it to see the current price and availability.

Endpoints[GET/v1/climate/products/:id](https://docs.stripe.com/api/climate/product/retrieve)[GET/v1/climate/products](https://docs.stripe.com/api/climate/product/list)
Show

# [Climate Supplier](https://docs.stripe.com/api/climate/supplier)

A supplier of carbon removal.

Endpoints[GET/v1/climate/suppliers/:id](https://docs.stripe.com/api/climate/supplier/retrieve)[GET/v1/climate/suppliers](https://docs.stripe.com/api/climate/supplier/list)
Show

# [Forwarding Request](https://docs.stripe.com/api/forwarding/request)

Instructs Stripe to make a request on your behalf using the destination URL. The
destination URL is activated by Stripe at the time of onboarding. Stripe
verifies requests with your credentials provided during onboarding, and injects
card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication
credentials and card numbers, before storing the request and response data in
the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the
same key result in only one outbound request. The Stripe idempotency key
provided should be unique and different from any idempotency keys provided on
the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out
according to Stripe’s limits.

Related guide: [Forward card details to third-party API
endpoints](https://docs.stripe.com/payments/forwarding).

Endpoints[POST/v1/forwarding/requests](https://docs.stripe.com/api/forwarding/forwarding_requests/create)[GET/v1/forwarding/requests/:id](https://docs.stripe.com/api/forwarding/forwarding_requests/retrieve)[GET/v1/forwarding/requests](https://docs.stripe.com/api/forwarding/forwarding_requests/list)
Show

# [Webhook Endpoints](https://docs.stripe.com/api/webhook_endpoints)

You can configure [webhook endpoints](https://docs.stripe.com/webhooks/) via the
API to be notified about events that happen in your Stripe account or connected
accounts.

Most users configure webhooks from [the
dashboard](https://dashboard.stripe.com/webhooks), which provides a user
interface for registering and testing your webhook endpoints.

Related guide: [Setting up webhooks](https://docs.stripe.com/webhooks/configure)

Endpoints[POST/v1/webhook_endpoints](https://docs.stripe.com/api/webhook_endpoints/create)[POST/v1/webhook_endpoints/:id](https://docs.stripe.com/api/webhook_endpoints/update)[GET/v1/webhook_endpoints/:id](https://docs.stripe.com/api/webhook_endpoints/retrieve)[GET/v1/webhook_endpoints](https://docs.stripe.com/api/webhook_endpoints/list)[DELETE/v1/webhook_endpoints/:id](https://docs.stripe.com/api/webhook_endpoints/delete)
Show

## Links

- [API Reference](https://docs.stripe.com/api)
- [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer)
-
[form-encoded](https://en.wikipedia.org/wiki/POST_(HTTP)#Use_for_submitting_web_forms)
- [JSON-encoded](http://www.json.org/)
- [authenticate](https://docs.stripe.com/api/authentication)
- [versions](https://docs.stripe.com/api/versioning)
- [Log
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fapi%2Fbalance%2Fbalance_object)
- [development quickstart](https://docs.stripe.com/development/quickstart)
- [no-code options](https://docs.stripe.com/payments/no-code)
- [our partners](https://stripe.partners/)
- [client libraries](https://docs.stripe.com/libraries)
- [API keys](https://docs.stripe.com/keys)
- [the Stripe Dashboard](https://dashboard.stripe.com/login?redirect=/apikeys)
- [restricted API keys](https://docs.stripe.com/keys#limit-access)
- [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure)
- [Connected Accounts](https://docs.stripe.com/api/connected-accounts)
- [Making API calls for connected
accounts](https://docs.stripe.com/connect/authentication)
- [Errors](https://docs.stripe.com/api/errors)
- [declined](https://docs.stripe.com/declines)
- [error code](https://docs.stripe.com/error-codes)
- [card issuer’s reason for the
decline](https://docs.stripe.com/declines#issuer-declines)
- [PaymentIntent object](https://docs.stripe.com/api/payment_intents/object)
- [Handling errors](https://docs.stripe.com/api/errors/handling)
- [Error Handling](https://docs.stripe.com/error-handling)
- [Expanding Responses](https://docs.stripe.com/api/expanding_objects)
- [Expanding responses](https://docs.stripe.com/expand)
- [Expand](https://www.youtube.com/watch?v=m8Vj_CEWyQc)
- [Idempotent requests](https://docs.stripe.com/api/idempotent_requests)
- [idempotency](https://en.wikipedia.org/wiki/Idempotence)
- [retry idempotent
requests](https://docs.stripe.com/error-low-level#idempotency)
- [Metadata](https://docs.stripe.com/api/metadata)
- [Account](https://docs.stripe.com/api/accounts)
- [Charge](https://docs.stripe.com/api/charges)
- [Customer](https://docs.stripe.com/api/customers)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [Refund](https://docs.stripe.com/api/refunds)
- [Subscription](https://docs.stripe.com/api/subscriptions)
- [Transfer](https://docs.stripe.com/api/transfers)
- [Metadata](https://docs.stripe.com/metadata)
- [Pagination](https://docs.stripe.com/api/pagination)
- [list charges](https://docs.stripe.com/api/charges/list)
- [list customers](https://docs.stripe.com/api/customers/list)
- [list invoices](https://docs.stripe.com/api/invoices/list)
- [auto-pagination helpers](https://docs.stripe.com/api/pagination/auto)
- [Search](https://docs.stripe.com/api/pagination/search)
- [search charges](https://docs.stripe.com/api/charges/search)
- [search customers](https://docs.stripe.com/api/customers/search)
- [search subscriptions](https://docs.stripe.com/api/subscriptions/search)
- [search query language](https://docs.stripe.com/search#search-query-language)
- [Request IDs](https://docs.stripe.com/api/request_ids)
- [Dashboard](https://dashboard.stripe.com/logs)
- [Acacia](https://docs.stripe.com/changelog/acacia)
-
[backward-compatible](https://docs.stripe.com/upgrades#what-changes-does-stripe-consider-to-be-backward-compatible)
- [API changelog](https://docs.stripe.com/changelog)
- [Workbench](https://dashboard.stripe.com/workbench)
- [Balance](https://docs.stripe.com/api/balance)
- [transactions](https://docs.stripe.com/reporting/balance-transaction-types)
- [Understanding Connect account
balances](https://docs.stripe.com/connect/account-balances)
- [GET/v1/balance](https://docs.stripe.com/api/balance/balance_retrieve)
- [The Balance object](https://docs.stripe.com/api/balance/balance_object)
- [Accounting for negative
balances](https://docs.stripe.com/connect/account-balances#accounting-for-negative-balances)
- [Balance Transactions](https://docs.stripe.com/api/balance_transactions)
- [Balance transaction
types](https://docs.stripe.com/reports/balance-transaction-types)
-
[GET/v1/balance_transactions/:id](https://docs.stripe.com/api/balance_transactions/retrieve)
-
[GET/v1/balance_transactions](https://docs.stripe.com/api/balance_transactions/list)
- [POST/v1/charges](https://docs.stripe.com/api/charges/create)
- [POST/v1/charges/:id](https://docs.stripe.com/api/charges/update)
- [GET/v1/charges/:id](https://docs.stripe.com/api/charges/retrieve)
- [POST/v1/charges/:id/capture](https://docs.stripe.com/api/charges/capture)
- [create recurring charges](https://docs.stripe.com/invoicing/customer)
- [save payment](https://docs.stripe.com/payments/save-during-payment)
- [POST/v1/customers](https://docs.stripe.com/api/customers/create)
- [POST/v1/customers/:id](https://docs.stripe.com/api/customers/update)
- [GET/v1/customers/:id](https://docs.stripe.com/api/customers/retrieve)
- [DELETE/v1/customers/:id](https://docs.stripe.com/api/customers/delete)
- [Customer Session](https://docs.stripe.com/api/customer_sessions)
- [Customer Session with the Payment
Element](https://docs.stripe.com/payments/accept-a-payment-deferred?platform=web&type=payment#save-payment-methods)
- [Customer Session with the Pricing
Table](https://docs.stripe.com/payments/checkout/pricing-table#customer-session)
- [Customer Session with the Buy
Button](https://docs.stripe.com/payment-links/buy-button#pass-an-existing-customer)
-
[POST/v1/customer_sessions](https://docs.stripe.com/api/customer_sessions/create)
- [Disputes](https://docs.stripe.com/api/disputes)
- [Disputes and fraud](https://docs.stripe.com/disputes)
- [POST/v1/disputes/:id](https://docs.stripe.com/api/disputes/update)
- [GET/v1/disputes/:id](https://docs.stripe.com/api/disputes/retrieve)
- [GET/v1/disputes](https://docs.stripe.com/api/disputes/list)
- [POST/v1/disputes/:id/close](https://docs.stripe.com/api/disputes/close)
- [Events](https://docs.stripe.com/api/events)
- [webhooks](http://en.wikipedia.org/wiki/Webhook)
- [account settings](https://dashboard.stripe.com/account/webhooks)
- [listen for events](https://docs.stripe.com/webhooks)
- [Connect](https://docs.stripe.com/connect)
- [GET/v1/events/:id](https://docs.stripe.com/api/events/retrieve)
- [GET/v1/events](https://docs.stripe.com/api/events/list)
- [Events](https://docs.stripe.com/api/v2/core/events)
- [Learn more about calling API v2
endpoints.](https://docs.stripe.com/api-v2-overview)
- [thin
events](https://docs.stripe.com/event-destinations#benefits-of-thin-events)
- [Retrieve the event
object](https://docs.stripe.com/event-destinations#fetch-data)
- [fetch the API
resource](https://docs.stripe.com/event-destinations#retrieve-the-object-associated-with-thin-events)
- [GET/v2/core/events/:id](https://docs.stripe.com/api/v2/core/events/retrieve)
- [GET/v2/core/events](https://docs.stripe.com/api/v2/core/events/list)
- [Event Destinations](https://docs.stripe.com/api/v2/core/event_destinations)
- [Amazon EventBridge](https://docs.stripe.com/event-destinations/eventbridge)
- [thin events](https://docs.stripe.com/api/v2/events)
-
[POST/v2/core/event_destinations](https://docs.stripe.com/api/v2/core/event_destinations/create)
-
[POST/v2/core/event_destinations/:id](https://docs.stripe.com/api/v2/core/event_destinations/update)
-
[GET/v2/core/event_destinations/:id](https://docs.stripe.com/api/v2/core/event_destinations/retrieve)
-
[GET/v2/core/event_destinations](https://docs.stripe.com/api/v2/core/event_destinations/list)
-
[DELETE/v2/core/event_destinations/:id](https://docs.stripe.com/api/v2/core/event_destinations/delete)
-
[POST/v2/core/event_destinations/:id/disable](https://docs.stripe.com/api/v2/core/event_destinations/disable)
-
[POST/v2/core/event_destinations/:id/enable](https://docs.stripe.com/api/v2/core/event_destinations/enable)
-
[POST/v2/core/event_destinations/:id/ping](https://docs.stripe.com/api/v2/core/event_destinations/ping)
- [Files](https://docs.stripe.com/api/files)
- [File upload guide](https://docs.stripe.com/file-upload)
- [POST/v1/files](https://docs.stripe.com/api/files/create)
- [GET/v1/files/:id](https://docs.stripe.com/api/files/retrieve)
- [GET/v1/files](https://docs.stripe.com/api/files/list)
- [File Links](https://docs.stripe.com/api/file_links)
- [POST/v1/file_links](https://docs.stripe.com/api/file_links/create)
- [POST/v1/file_links/:id](https://docs.stripe.com/api/file_links/update)
- [GET/v1/file_links/:id](https://docs.stripe.com/api/file_links/retrieve)
- [GET/v1/file_links](https://docs.stripe.com/api/file_links/list)
- [Mandates](https://docs.stripe.com/api/mandates)
- [GET/v1/mandates/:id](https://docs.stripe.com/api/mandates/retrieve)
- [multiple statuses](https://docs.stripe.com/payments/intents#intent-statuses)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [POST/v1/payment_intents](https://docs.stripe.com/api/payment_intents/create)
-
[POST/v1/payment_intents/:id](https://docs.stripe.com/api/payment_intents/update)
-
[GET/v1/payment_intents/:id](https://docs.stripe.com/api/payment_intents/retrieve)
- [GET/v1/payment_intents](https://docs.stripe.com/api/payment_intents/list)
-
[POST/v1/payment_intents/:id/cancel](https://docs.stripe.com/api/payment_intents/cancel)
-
[POST/v1/payment_intents/:id/capture](https://docs.stripe.com/api/payment_intents/capture)
-
[POST/v1/payment_intents/:id/confirm](https://docs.stripe.com/api/payment_intents/confirm)
-
[POST/v1/payment_intents/:id/increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization)
-
[POST/v1/payment_intents/:id/apply_customer_balance](https://docs.stripe.com/api/payment_intents/apply_customer_balance)
-
[GET/v1/payment_intents/search](https://docs.stripe.com/api/payment_intents/search)
-
[POST/v1/payment_intents/:id/verify_microdeposits](https://docs.stripe.com/api/payment_intents/verify_microdeposits)
- [Setup Intents](https://docs.stripe.com/api/setup_intents)
- [certain regions](https://stripe.com/guides/strong-customer-authentication)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [off-session payments](https://docs.stripe.com/payments/setup-intents)
- [POST/v1/setup_intents](https://docs.stripe.com/api/setup_intents/create)
- [POST/v1/setup_intents/:id](https://docs.stripe.com/api/setup_intents/update)
- [GET/v1/setup_intents/:id](https://docs.stripe.com/api/setup_intents/retrieve)
- [GET/v1/setup_intents](https://docs.stripe.com/api/setup_intents/list)
-
[POST/v1/setup_intents/:id/cancel](https://docs.stripe.com/api/setup_intents/cancel)
-
[POST/v1/setup_intents/:id/confirm](https://docs.stripe.com/api/setup_intents/confirm)
-
[POST/v1/setup_intents/:id/verify_microdeposits](https://docs.stripe.com/api/setup_intents/verify_microdeposits)
- [Setup Attempts](https://docs.stripe.com/api/setup_attempts)
- [GET/v1/setup_attempts](https://docs.stripe.com/api/setup_attempts/list)
- [Payouts](https://docs.stripe.com/api/payouts)
- [connected Stripe
account](https://docs.stripe.com/connect/bank-debit-card-payouts)
- [varying schedules](https://docs.stripe.com/connect/manage-payout-schedule)
- [Receiving payouts](https://docs.stripe.com/payouts)
- [POST/v1/payouts](https://docs.stripe.com/api/payouts/create)
- [POST/v1/payouts/:id](https://docs.stripe.com/api/payouts/update)
- [GET/v1/payouts/:id](https://docs.stripe.com/api/payouts/retrieve)
- [GET/v1/payouts](https://docs.stripe.com/api/payouts/list)
- [POST/v1/payouts/:id/cancel](https://docs.stripe.com/api/payouts/cancel)
- [POST/v1/payouts/:id/reverse](https://docs.stripe.com/api/payouts/reverse)
- [Refunds](https://docs.stripe.com/refunds)
- [POST/v1/refunds](https://docs.stripe.com/api/refunds/create)
- [POST/v1/refunds/:id](https://docs.stripe.com/api/refunds/update)
- [GET/v1/refunds/:id](https://docs.stripe.com/api/refunds/retrieve)
- [GET/v1/refunds](https://docs.stripe.com/api/refunds/list)
- [POST/v1/refunds/:id/cancel](https://docs.stripe.com/api/refunds/cancel)
- [Confirmation Token](https://docs.stripe.com/api/confirmation_tokens)
- [Finalize payments on the
server](https://docs.stripe.com/payments/finalize-payments-on-the-server)
- [Build two-step
confirmation](https://docs.stripe.com/payments/build-a-two-step-confirmation)
-
[GET/v1/confirmation_tokens/:id](https://docs.stripe.com/api/confirmation_tokens/retrieve)
-
[POST/v1/test_helpers/confirmation_tokens](https://docs.stripe.com/api/confirmation_tokens/test_create)
- [Tokens](https://docs.stripe.com/api/tokens)
- [recommended payments integrations](https://docs.stripe.com/payments)
- [Customer](https://docs.stripe.com/api#customers)
- [External accounts](https://docs.stripe.com/api#external_accounts)
- [Radar](https://docs.stripe.com/radar)
- [POST/v1/tokens](https://docs.stripe.com/api/tokens/create_account)
- [POST/v1/tokens](https://docs.stripe.com/api/tokens/create_bank_account)
- [POST/v1/tokens](https://docs.stripe.com/api/tokens/create_card)
- [POST/v1/tokens](https://docs.stripe.com/api/tokens/create_cvc_update)
- [POST/v1/tokens](https://docs.stripe.com/api/tokens/create_person)
- [POST/v1/tokens](https://docs.stripe.com/api/tokens/create_pii)
- [GET/v1/tokens/:id](https://docs.stripe.com/api/tokens/retrieve)
- [Payment Methods](https://docs.stripe.com/api/payment_methods)
- [Payment Methods](https://docs.stripe.com/payments/payment-methods)
- [More Payment
Scenarios](https://docs.stripe.com/payments/more-payment-scenarios)
- [POST/v1/payment_methods](https://docs.stripe.com/api/payment_methods/create)
-
[POST/v1/payment_methods/:id](https://docs.stripe.com/api/payment_methods/update)
-
[GET/v1/customers/:id/payment_methods/:id](https://docs.stripe.com/api/payment_methods/customer)
-
[GET/v1/payment_methods/:id](https://docs.stripe.com/api/payment_methods/retrieve)
-
[GET/v1/customers/:id/payment_methods](https://docs.stripe.com/api/payment_methods/customer_list)
- [GET/v1/payment_methods](https://docs.stripe.com/api/payment_methods/list)
-
[POST/v1/payment_methods/:id/attach](https://docs.stripe.com/api/payment_methods/attach)
-
[POST/v1/payment_methods/:id/detach](https://docs.stripe.com/api/payment_methods/detach)
- [Payment Method
Configurations](https://docs.stripe.com/api/payment_method_configurations)
- [charge type](https://docs.stripe.com/connect/charges)
- [managed in the
dashboard](https://dashboard.stripe.com/settings/payment_methods/connected_accounts)
- [Payment Method Configurations
API](https://docs.stripe.com/connect/payment-method-configurations)
- [Multiple configurations on dynamic payment
methods](https://docs.stripe.com/payments/multiple-payment-method-configs)
- [Multiple configurations for your Connect
accounts](https://docs.stripe.com/connect/multiple-payment-method-configurations)
-
[POST/v1/payment_method_configurations](https://docs.stripe.com/api/payment_method_configurations/create)
-
[POST/v1/payment_method_configurations/:id](https://docs.stripe.com/api/payment_method_configurations/update)
-
[GET/v1/payment_method_configurations/:id](https://docs.stripe.com/api/payment_method_configurations/retrieve)
-
[GET/v1/payment_method_configurations](https://docs.stripe.com/api/payment_method_configurations/list)
- [Payment Method Domains](https://docs.stripe.com/api/payment_method_domains)
- [Payment method
domains](https://docs.stripe.com/payments/payment-methods/pmd-registration)
-
[POST/v1/payment_method_domains](https://docs.stripe.com/api/payment_method_domains/create)
-
[POST/v1/payment_method_domains/:id](https://docs.stripe.com/api/payment_method_domains/update)
-
[GET/v1/payment_method_domains/:id](https://docs.stripe.com/api/payment_method_domains/retrieve)
-
[GET/v1/payment_method_domains](https://docs.stripe.com/api/payment_method_domains/list)
-
[POST/v1/payment_method_domains/:id/validate](https://docs.stripe.com/api/payment_method_domains/validate)
- [Bank Accounts](https://docs.stripe.com/api/customer_bank_accounts)
- [Bank debits and
transfers](https://docs.stripe.com/payments/bank-debits-transfers)
-
[POST/v1/customers/:id/sources](https://docs.stripe.com/api/customer_bank_accounts/create)
-
[POST/v1/customers/:id/sources/:id](https://docs.stripe.com/api/customer_bank_accounts/update)
-
[GET/v1/customers/:id/bank_accounts/:id](https://docs.stripe.com/api/customer_bank_accounts/retrieve)
-
[GET/v1/customers/:id/bank_accounts](https://docs.stripe.com/api/customer_bank_accounts/list)
-
[DELETE/v1/customers/:id/sources/:id](https://docs.stripe.com/api/customer_bank_accounts/delete)
-
[POST/v1/customers/:id/sources/:id/verify](https://docs.stripe.com/api/customer_bank_accounts/verify)
- [Cash Balance](https://docs.stripe.com/api/cash_balance)
-
[POST/v1/customers/:id/cash_balance](https://docs.stripe.com/api/cash_balance/update)
-
[GET/v1/customers/:id/cash_balance](https://docs.stripe.com/api/cash_balance/retrieve)
- [Cash Balance
Transaction](https://docs.stripe.com/api/cash_balance_transactions)
-
[GET/v1/customers/:id/cash_balance_transactions/:id](https://docs.stripe.com/api/cash_balance_transactions/retrieve)
-
[GET/v1/customers/:id/cash_balance_transactions](https://docs.stripe.com/api/cash_balance_transactions/list)
-
[POST/v1/test_helpers/customers/:id/fund_cash_balance](https://docs.stripe.com/api/cash_balance_transactions/fund_cash_balance)
- [Cards](https://docs.stripe.com/api/cards)
- [Card payments with Sources](https://docs.stripe.com/sources/cards)
- [POST/v1/customers/:id/sources](https://docs.stripe.com/api/cards/create)
- [POST/v1/customers/:id/sources/:id](https://docs.stripe.com/api/cards/update)
- [GET/v1/customers/:id/cards/:id](https://docs.stripe.com/api/cards/retrieve)
- [GET/v1/customers/:id/cards](https://docs.stripe.com/api/cards/list)
-
[DELETE/v1/customers/:id/sources/:id](https://docs.stripe.com/api/cards/delete)
- [Sources](https://docs.stripe.com/api/sources)
- [Sources API](https://docs.stripe.com/sources)
- [Sources & Customers](https://docs.stripe.com/sources/customers)
- [POST/v1/sources](https://docs.stripe.com/api/sources/create)
- [POST/v1/sources/:id](https://docs.stripe.com/api/sources/update)
- [GET/v1/sources/:id](https://docs.stripe.com/api/sources/retrieve)
- [POST/v1/customers/:id/sources](https://docs.stripe.com/api/sources/attach)
-
[DELETE/v1/customers/:id/sources/:id](https://docs.stripe.com/api/sources/detach)
- [Products](https://docs.stripe.com/api/products)
- [Set up a
subscription](https://docs.stripe.com/billing/subscriptions/set-up-subscription)
- [share a Payment Link](https://docs.stripe.com/payment-links)
- [accept payments with
Checkout](https://docs.stripe.com/payments/accept-a-payment#create-product-prices-upfront)
- [Products and Prices](https://docs.stripe.com/products-prices/overview)
- [POST/v1/products](https://docs.stripe.com/api/products/create)
- [POST/v1/products/:id](https://docs.stripe.com/api/products/update)
- [GET/v1/products/:id](https://docs.stripe.com/api/products/retrieve)
- [GET/v1/products](https://docs.stripe.com/api/products/list)
- [DELETE/v1/products/:id](https://docs.stripe.com/api/products/delete)
- [GET/v1/products/search](https://docs.stripe.com/api/products/search)
- [Prices](https://docs.stripe.com/api/prices)
- [create an invoice](https://docs.stripe.com/billing/invoices/create)
- [POST/v1/prices](https://docs.stripe.com/api/prices/create)
- [POST/v1/prices/:id](https://docs.stripe.com/api/prices/update)
- [GET/v1/prices/:id](https://docs.stripe.com/api/prices/retrieve)
- [GET/v1/prices](https://docs.stripe.com/api/prices/list)
- [GET/v1/prices/search](https://docs.stripe.com/api/prices/search)
- [Coupons](https://docs.stripe.com/api/coupons)
- [checkout sessions](https://docs.stripe.com/api/checkout/sessions)
- [POST/v1/coupons](https://docs.stripe.com/api/coupons/create)
- [POST/v1/coupons/:id](https://docs.stripe.com/api/coupons/update)
- [GET/v1/coupons/:id](https://docs.stripe.com/api/coupons/retrieve)
- [GET/v1/coupons](https://docs.stripe.com/api/coupons/list)
- [DELETE/v1/coupons/:id](https://docs.stripe.com/api/coupons/delete)
- [Promotion Code](https://docs.stripe.com/api/promotion_codes)
- [POST/v1/promotion_codes](https://docs.stripe.com/api/promotion_codes/create)
-
[POST/v1/promotion_codes/:id](https://docs.stripe.com/api/promotion_codes/update)
-
[GET/v1/promotion_codes/:id](https://docs.stripe.com/api/promotion_codes/retrieve)
- [GET/v1/promotion_codes](https://docs.stripe.com/api/promotion_codes/list)
- [Discounts](https://docs.stripe.com/api/discounts)
- [Applying discounts to
subscriptions](https://docs.stripe.com/billing/subscriptions/discounts)
-
[DELETE/v1/customers/:id/discount](https://docs.stripe.com/api/discounts/delete)
-
[DELETE/v1/subscriptions/:id/discount](https://docs.stripe.com/api/discounts/subscription_delete)
- [Tax Code](https://docs.stripe.com/api/tax_codes)
- [Tax codes](https://stripe.com/docs/tax/tax-categories)
- [GET/v1/tax_codes/:id](https://docs.stripe.com/api/tax_codes/retrieve)
- [GET/v1/tax_codes](https://docs.stripe.com/api/tax_codes/list)
- [Tax Rate](https://docs.stripe.com/api/tax_rates)
- [invoices](https://docs.stripe.com/invoicing/taxes/tax-rates)
- [subscriptions](https://docs.stripe.com/billing/taxes/tax-rates)
- [Checkout
Sessions](https://docs.stripe.com/payments/checkout/use-manual-tax-rates)
- [POST/v1/tax_rates](https://docs.stripe.com/api/tax_rates/create)
- [POST/v1/tax_rates/:id](https://docs.stripe.com/api/tax_rates/update)
- [GET/v1/tax_rates/:id](https://docs.stripe.com/api/tax_rates/retrieve)
- [GET/v1/tax_rates](https://docs.stripe.com/api/tax_rates/list)
- [Shipping Rates](https://docs.stripe.com/api/shipping_rates)
- [Charge for
shipping](https://docs.stripe.com/payments/during-payment/charge-shipping)
- [POST/v1/shipping_rates](https://docs.stripe.com/api/shipping_rates/create)
-
[POST/v1/shipping_rates/:id](https://docs.stripe.com/api/shipping_rates/update)
-
[GET/v1/shipping_rates/:id](https://docs.stripe.com/api/shipping_rates/retrieve)
- [GET/v1/shipping_rates](https://docs.stripe.com/api/shipping_rates/list)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payments/payment-links)
- [Checkout quickstart](https://docs.stripe.com/checkout/quickstart)
-
[POST/v1/checkout/sessions](https://docs.stripe.com/api/checkout/sessions/create)
-
[POST/v1/checkout/sessions/:id](https://docs.stripe.com/api/checkout/sessions/update)
-
[GET/v1/checkout/sessions/:id](https://docs.stripe.com/api/checkout/sessions/retrieve)
-
[GET/v1/checkout/sessions/:id/line_items](https://docs.stripe.com/api/checkout/sessions/line_items)
- [GET/v1/checkout/sessions](https://docs.stripe.com/api/checkout/sessions/list)
-
[POST/v1/checkout/sessions/:id/expire](https://docs.stripe.com/api/checkout/sessions/expire)
- [Payment Link](https://docs.stripe.com/api/payment-link)
- [checkout session
events](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [POST/v1/payment_links](https://docs.stripe.com/api/payment-link/create)
- [POST/v1/payment_links/:id](https://docs.stripe.com/api/payment-link/update)
-
[GET/v1/payment_links/:id/line_items](https://docs.stripe.com/api/payment-link/retrieve-line-items)
- [GET/v1/payment_links/:id](https://docs.stripe.com/api/payment-link/retrieve)
- [GET/v1/payment_links](https://docs.stripe.com/api/payment-link/list)
- [Credit Note](https://docs.stripe.com/api/credit_notes)
- [Credit notes](https://docs.stripe.com/billing/invoices/credit-notes)
- [POST/v1/credit_notes](https://docs.stripe.com/api/credit_notes/create)
- [POST/v1/credit_notes/:id](https://docs.stripe.com/api/credit_notes/update)
-
[GET/v1/credit_notes/:id/lines](https://docs.stripe.com/api/credit_notes/lines)
-
[GET/v1/credit_notes/preview/lines](https://docs.stripe.com/api/credit_notes/preview_lines)
- [GET/v1/credit_notes/:id](https://docs.stripe.com/api/credit_notes/retrieve)
- [GET/v1/credit_notes](https://docs.stripe.com/api/credit_notes/list)
-
[GET/v1/credit_notes/preview](https://docs.stripe.com/api/credit_notes/preview)
- [POST/v1/credit_notes/:id/void](https://docs.stripe.com/api/credit_notes/void)
- [Customer Balance
Transaction](https://docs.stripe.com/api/customer_balance_transactions)
-
[Balance](https://docs.stripe.com/api/customers/object#customer_object-balance)
- [Customer balance](https://docs.stripe.com/billing/customer/balance)
-
[POST/v1/customers/:id/balance_transactions](https://docs.stripe.com/api/customer_balance_transactions/create)
-
[POST/v1/customers/:id/balance_transactions/:id](https://docs.stripe.com/api/customer_balance_transactions/update)
-
[GET/v1/customers/:id/balance_transactions/:id](https://docs.stripe.com/api/customer_balance_transactions/retrieve)
-
[GET/v1/customers/:id/balance_transactions](https://docs.stripe.com/api/customer_balance_transactions/list)
- [Customer Portal
Session](https://docs.stripe.com/api/customer_portal/sessions)
- [Customer management](https://docs.stripe.com/customer-management)
-
[POST/v1/billing_portal/sessions](https://docs.stripe.com/api/customer_portal/sessions/create)
- [Customer Portal
Configuration](https://docs.stripe.com/api/customer_portal/configurations)
-
[POST/v1/billing_portal/configurations](https://docs.stripe.com/api/customer_portal/configurations/create)
-
[POST/v1/billing_portal/configurations/:id](https://docs.stripe.com/api/customer_portal/configurations/update)
-
[GET/v1/billing_portal/configurations/:id](https://docs.stripe.com/api/customer_portal/configurations/retrieve)
-
[GET/v1/billing_portal/configurations](https://docs.stripe.com/api/customer_portal/configurations/list)
- [Invoices](https://docs.stripe.com/api/invoices)
- [when
automatic](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
- [email settings](https://dashboard.stripe.com/account/billing/automatic)
- [minimum allowed charge per
currency](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)
- [Send invoices to customers](https://docs.stripe.com/billing/invoices/sending)
- [POST/v1/invoices](https://docs.stripe.com/api/invoices/create)
-
[POST/v1/invoices/create_preview](https://docs.stripe.com/api/invoices/create_preview)
- [POST/v1/invoices/:id](https://docs.stripe.com/api/invoices/update)
- [GET/v1/invoices/:id](https://docs.stripe.com/api/invoices/retrieve)
- [GET/v1/invoices/upcoming](https://docs.stripe.com/api/invoices/upcoming)
- [DELETE/v1/invoices/:id](https://docs.stripe.com/api/invoices/delete)
- [POST/v1/invoices/:id/finalize](https://docs.stripe.com/api/invoices/finalize)
-
[POST/v1/invoices/:id/mark_uncollectible](https://docs.stripe.com/api/invoices/mark_uncollectible)
- [POST/v1/invoices/:id/pay](https://docs.stripe.com/api/invoices/pay)
- [GET/v1/invoices/search](https://docs.stripe.com/api/invoices/search)
- [POST/v1/invoices/:id/send](https://docs.stripe.com/api/invoices/send)
- [POST/v1/invoices/:id/void](https://docs.stripe.com/api/invoices/void)
- [Invoice Items](https://docs.stripe.com/api/invoiceitems)
- [an invoice line item](https://docs.stripe.com/api/invoices/line_item)
-
[invoice.lines](https://docs.stripe.com/api/invoices/object#invoice_object-lines)
- [Integrate with the Invoicing
API](https://docs.stripe.com/invoicing/integration)
- [Subscription
Invoices](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items)
- [POST/v1/invoiceitems](https://docs.stripe.com/api/invoiceitems/create)
- [POST/v1/invoiceitems/:id](https://docs.stripe.com/api/invoiceitems/update)
- [GET/v1/invoiceitems/:id](https://docs.stripe.com/api/invoiceitems/retrieve)
- [GET/v1/invoiceitems](https://docs.stripe.com/api/invoiceitems/list)
- [DELETE/v1/invoiceitems/:id](https://docs.stripe.com/api/invoiceitems/delete)
- [Invoice Line Item](https://docs.stripe.com/api/invoice-line-item)
- [subscription item](https://docs.stripe.com/api/subscription_items)
-
[POST/v1/invoices/:id/lines/:id](https://docs.stripe.com/api/invoice-line-item/update)
-
[GET/v1/invoices/:id/lines](https://docs.stripe.com/api/invoice-line-item/retrieve)
-
[GET/v1/invoices/upcoming/lines](https://docs.stripe.com/api/invoice-line-item/invoices/upcoming/lines/retrieve)
-
[POST/v1/invoices/:id/add_lines](https://docs.stripe.com/api/invoice-line-item/bulk)
-
[POST/v1/invoices/:id/remove_lines](https://docs.stripe.com/api/invoice-line-item/invoices/remove-lines/bulk)
-
[POST/v1/invoices/:id/update_lines](https://docs.stripe.com/api/invoice-line-item/invoices/update-lines/bulk)
- [Invoice Rendering
Templates](https://docs.stripe.com/api/invoice-rendering-template)
-
[GET/v1/invoice_rendering_templates/:id](https://docs.stripe.com/api/invoice-rendering-template/retrieve)
-
[GET/v1/invoice_rendering_templates](https://docs.stripe.com/api/invoice-rendering-template/list)
-
[POST/v1/invoice_rendering_templates/:id/archive](https://docs.stripe.com/api/invoice-rendering-template/archive)
-
[POST/v1/invoice_rendering_templates/:id/unarchive](https://docs.stripe.com/api/invoice-rendering-template/unarchive)
- [Alerts](https://docs.stripe.com/api/billing/alert)
- [POST/v1/billing/alerts](https://docs.stripe.com/api/billing/alert/create)
-
[GET/v1/billing/alerts/:id](https://docs.stripe.com/api/billing/alert/retrieve)
- [GET/v1/billing/alerts](https://docs.stripe.com/api/billing/alert/list)
-
[POST/v1/billing/alerts/:id/activate](https://docs.stripe.com/api/billing/alert/activate)
-
[POST/v1/billing/alerts/:id/archive](https://docs.stripe.com/api/billing/alert/archive)
-
[POST/v1/billing/alerts/:id/deactivate](https://docs.stripe.com/api/billing/alert/deactivate)
- [Meters](https://docs.stripe.com/api/billing/meter)
- [Usage based
billing](https://docs.stripe.com/billing/subscriptions/usage-based)
- [POST/v1/billing/meters](https://docs.stripe.com/api/billing/meter/create)
- [POST/v1/billing/meters/:id](https://docs.stripe.com/api/billing/meter/update)
-
[GET/v1/billing/meters/:id](https://docs.stripe.com/api/billing/meter/retrieve)
- [GET/v1/billing/meters](https://docs.stripe.com/api/billing/meter/list)
-
[POST/v1/billing/meters/:id/deactivate](https://docs.stripe.com/api/billing/meter/deactivate)
-
[POST/v1/billing/meters/:id/reactivate](https://docs.stripe.com/api/billing/meter/reactivate)
- [Meter Events](https://docs.stripe.com/api/billing/meter-event)
-
[POST/v1/billing/meter_events](https://docs.stripe.com/api/billing/meter-event/create)
- [Meter Events](https://docs.stripe.com/api/v2/billing-meter)
-
[POST/v2/billing/meter_events](https://docs.stripe.com/api/v2/billing/meter-event/create)
- [Meter Event
Adjustment](https://docs.stripe.com/api/billing/meter-event-adjustment)
-
[POST/v1/billing/meter_event_adjustments](https://docs.stripe.com/api/billing/meter-event-adjustment/create)
- [Meter Event
Adjustment](https://docs.stripe.com/api/v2/billing-meter-adjustment)
-
[POST/v2/billing/meter_event_adjustments](https://docs.stripe.com/api/v2/billing/meter-event-adjustments/create)
- [Meter Event Stream](https://docs.stripe.com/api/v2/billing-meter-stream)
-
[POST/v2/billing/meter_event_session](https://docs.stripe.com/api/v2/billing/meter-event-stream/session/create)
-
[POST/v2/billing/meter_event_stream](https://docs.stripe.com/api/v2/billing/meter-event-stream/create)
- [Meter Event Summary](https://docs.stripe.com/api/billing/meter-event-summary)
-
[GET/v1/billing/meters/:id/event_summaries](https://docs.stripe.com/api/billing/meter-event-summary/list)
- [Credit Grant](https://docs.stripe.com/api/billing/credit-grant)
- [Billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
-
[POST/v1/billing/credit_grants](https://docs.stripe.com/api/billing/credit-grant/create)
-
[POST/v1/billing/credit_grants/:id](https://docs.stripe.com/api/billing/credit-grant/update)
-
[GET/v1/billing/credit_grants/:id](https://docs.stripe.com/api/billing/credit-grant/retrieve)
-
[GET/v1/billing/credit_grants](https://docs.stripe.com/api/billing/credit-grant/list)
-
[POST/v1/billing/credit_grants/:id/expire](https://docs.stripe.com/api/billing/credit-grant/expire)
-
[POST/v1/billing/credit_grants/:id/void](https://docs.stripe.com/api/billing/credit-grant/void)
- [Credit Balance
Summary](https://docs.stripe.com/api/billing/credit-balance-summary)
-
[GET/v1/billing/credit_balance_summary](https://docs.stripe.com/api/billing/credit-balance-summary/retrieve)
- [Credit Balance
Transaction](https://docs.stripe.com/api/billing/credit-balance-transaction)
-
[GET/v1/billing/credit_balance_transactions/:id](https://docs.stripe.com/api/billing/credit-balance-transaction/retrieve)
-
[GET/v1/billing/credit_balance_transactions](https://docs.stripe.com/api/billing/credit-balance-transaction/list)
- [Plans](https://docs.stripe.com/api/plans)
- [POST/v1/plans](https://docs.stripe.com/api/plans/create)
- [POST/v1/plans/:id](https://docs.stripe.com/api/plans/update)
- [GET/v1/plans/:id](https://docs.stripe.com/api/plans/retrieve)
- [GET/v1/plans](https://docs.stripe.com/api/plans/list)
- [DELETE/v1/plans/:id](https://docs.stripe.com/api/plans/delete)
- [Quote](https://docs.stripe.com/api/quotes)
- [POST/v1/quotes](https://docs.stripe.com/api/quotes/create)
- [POST/v1/quotes/:id](https://docs.stripe.com/api/quotes/update)
-
[GET/v1/quotes/:id/line_items](https://docs.stripe.com/api/quotes/line_items/list)
-
[GET/v1/quotes/:id/computed_upfront_line_items](https://docs.stripe.com/api/quotes/line_items/upfront/list)
- [GET/v1/quotes/:id](https://docs.stripe.com/api/quotes/retrieve)
- [GET/v1/quotes](https://docs.stripe.com/api/quotes/list)
- [POST/v1/quotes/:id/accept](https://docs.stripe.com/api/quotes/accept)
- [POST/v1/quotes/:id/cancel](https://docs.stripe.com/api/quotes/cancel)
- [GET/v1/quotes/:id/pdf](https://docs.stripe.com/api/quotes/pdf)
- [POST/v1/quotes/:id/finalize](https://docs.stripe.com/api/quotes/finalize)
- [Creating
subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [POST/v1/subscriptions](https://docs.stripe.com/api/subscriptions/create)
- [POST/v1/subscriptions/:id](https://docs.stripe.com/api/subscriptions/update)
- [GET/v1/subscriptions/:id](https://docs.stripe.com/api/subscriptions/retrieve)
- [GET/v1/subscriptions](https://docs.stripe.com/api/subscriptions/list)
-
[DELETE/v1/subscriptions/:id](https://docs.stripe.com/api/subscriptions/cancel)
-
[POST/v1/subscriptions/:id/resume](https://docs.stripe.com/api/subscriptions/resume)
-
[POST/v1/subscription_items](https://docs.stripe.com/api/subscription_items/create)
-
[POST/v1/subscription_items/:id](https://docs.stripe.com/api/subscription_items/update)
-
[GET/v1/subscription_items/:id](https://docs.stripe.com/api/subscription_items/retrieve)
-
[GET/v1/subscription_items](https://docs.stripe.com/api/subscription_items/list)
-
[DELETE/v1/subscription_items/:id](https://docs.stripe.com/api/subscription_items/delete)
- [Subscription Schedule](https://docs.stripe.com/api/subscription_schedules)
- [Subscription
schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
-
[POST/v1/subscription_schedules](https://docs.stripe.com/api/subscription_schedules/create)
-
[POST/v1/subscription_schedules/:id](https://docs.stripe.com/api/subscription_schedules/update)
-
[GET/v1/subscription_schedules/:id](https://docs.stripe.com/api/subscription_schedules/retrieve)
-
[GET/v1/subscription_schedules](https://docs.stripe.com/api/subscription_schedules/list)
-
[POST/v1/subscription_schedules/:id/cancel](https://docs.stripe.com/api/subscription_schedules/cancel)
-
[POST/v1/subscription_schedules/:id/release](https://docs.stripe.com/api/subscription_schedules/release)
- [Tax IDs](https://docs.stripe.com/api/tax_ids)
- [Customer tax identification
numbers](https://docs.stripe.com/billing/taxes/tax-ids)
- [Account tax IDs](https://docs.stripe.com/invoicing/connect#account-tax-ids)
-
[POST/v1/customers/:id/tax_ids](https://docs.stripe.com/api/tax_ids/customer_create)
- [POST/v1/tax_ids](https://docs.stripe.com/api/tax_ids/create)
-
[GET/v1/customers/:id/tax_ids/:id](https://docs.stripe.com/api/tax_ids/customer_retrieve)
- [GET/v1/tax_ids/:id](https://docs.stripe.com/api/tax_ids/retrieve)
-
[GET/v1/customers/:id/tax_ids](https://docs.stripe.com/api/tax_ids/customer_list)
- [GET/v1/tax_ids](https://docs.stripe.com/api/tax_ids/list)
-
[DELETE/v1/customers/:id/tax_ids/:id](https://docs.stripe.com/api/tax_ids/customer_delete)
- [DELETE/v1/tax_ids/:id](https://docs.stripe.com/api/tax_ids/delete)
- [Test Clocks](https://docs.stripe.com/api/test_clocks)
-
[POST/v1/test_helpers/test_clocks](https://docs.stripe.com/api/test_clocks/create)
-
[GET/v1/test_helpers/test_clocks/:id](https://docs.stripe.com/api/test_clocks/retrieve)
-
[GET/v1/test_helpers/test_clocks](https://docs.stripe.com/api/test_clocks/list)
-
[DELETE/v1/test_helpers/test_clocks/:id](https://docs.stripe.com/api/test_clocks/delete)
-
[POST/v1/test_helpers/test_clocks/:id/advance](https://docs.stripe.com/api/test_clocks/advance)
- [Usage Records](https://docs.stripe.com/api/usage_records)
- [Metered
billing](https://docs.stripe.com/billing/subscriptions/metered-billing)
-
[POST/v1/subscription_items/:id/usage_records](https://docs.stripe.com/api/usage_records/create)
- [Usage Record Summary](https://docs.stripe.com/api/usage-record-summary)
-
[GET/v1/subscription_items/:id/usage_record_summaries](https://docs.stripe.com/api/usage-record-summary/list)
- [Financing Offer](https://docs.stripe.com/api/capital/financing_offers)
-
[GET/v1/capital/financing_offers/:id](https://docs.stripe.com/api/capital/financing_offers/retrieve)
-
[GET/v1/capital/financing_offers](https://docs.stripe.com/api/capital/financing_offers/list)
-
[POST/v1/capital/financing_offers/:id/mark_delivered](https://docs.stripe.com/api/capital/financing_offers/mark_delivered)
- [Financing Summary](https://docs.stripe.com/api/capital/financing_summary)
-
[GET/v1/capital/financing_summary](https://docs.stripe.com/api/capital/financing_summary/retrieve)
-
[controller.requirement_collection](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
- [Account Link](https://docs.stripe.com/api/account_links)
- [Account Session](https://docs.stripe.com/api/account_sessions)
- [differences between accounts](https://docs.stripe.com/connect/accounts)
- [POST/v1/accounts](https://docs.stripe.com/api/accounts/create)
- [POST/v1/accounts/:id](https://docs.stripe.com/api/accounts/update)
- [GET/v1/accounts/:id](https://docs.stripe.com/api/accounts/retrieve)
- [GET/v1/accounts](https://docs.stripe.com/api/accounts/list)
- [DELETE/v1/accounts/:id](https://docs.stripe.com/api/accounts/delete)
- [POST/v1/accounts/:id/reject](https://docs.stripe.com/api/account/reject)
- [Login Links](https://docs.stripe.com/api/accounts/login_link)
-
[account.controller.stripe_dashboard.type](https://docs.stripe.com/api/accounts/object#account_object-controller-stripe_dashboard-type)
-
[POST/v1/accounts/:id/login_links](https://docs.stripe.com/api/accounts/login_link/create)
- [Connect Onboarding](https://docs.stripe.com/connect/custom/hosted-onboarding)
- [POST/v1/account_links](https://docs.stripe.com/api/account_links/create)
- [Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
-
[POST/v1/account_sessions](https://docs.stripe.com/api/account_sessions/create)
- [Application Fees](https://docs.stripe.com/api/application_fees)
- [Collecting application
fees](https://docs.stripe.com/connect/direct-charges#collect-fees)
-
[GET/v1/application_fees/:id](https://docs.stripe.com/api/application_fees/retrieve)
- [GET/v1/application_fees](https://docs.stripe.com/api/application_fees/list)
- [Application Fee Refunds](https://docs.stripe.com/api/fee_refunds)
- [Refunding application
fees](https://docs.stripe.com/connect/destination-charges#refunding-app-fee)
-
[POST/v1/application_fees/:id/refunds](https://docs.stripe.com/api/fee_refunds/create)
-
[POST/v1/application_fees/:id/refunds/:id](https://docs.stripe.com/api/fee_refunds/update)
-
[GET/v1/application_fees/:id/refunds/:id](https://docs.stripe.com/api/fee_refunds/retrieve)
-
[GET/v1/application_fees/:id/refunds](https://docs.stripe.com/api/fee_refunds/list)
- [Capabilities](https://docs.stripe.com/api/capabilities)
- [Account capabilities](https://docs.stripe.com/connect/account-capabilities)
-
[POST/v1/accounts/:id/capabilities/:id](https://docs.stripe.com/api/capabilities/update)
-
[GET/v1/accounts/:id/capabilities/:id](https://docs.stripe.com/api/capabilities/retrieve)
-
[GET/v1/accounts/:id/capabilities](https://docs.stripe.com/api/capabilities/list)
- [Country Specs](https://docs.stripe.com/api/country_specs)
- [an online
guide](https://docs.stripe.com/connect/required-verification-information)
- [GET/v1/country_specs/:id](https://docs.stripe.com/api/country_specs/retrieve)
- [GET/v1/country_specs](https://docs.stripe.com/api/country_specs/list)
- [External Bank Accounts](https://docs.stripe.com/api/external_accounts)
-
[POST/v1/accounts/:id/external_accounts](https://docs.stripe.com/api/external_account_bank_accounts/create)
-
[POST/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_bank_accounts/update)
-
[GET/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_bank_accounts/retrieve)
-
[GET/v1/accounts/:id/external_accounts](https://docs.stripe.com/api/external_account_bank_accounts/list)
-
[DELETE/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_bank_accounts/delete)
- [External Account Cards](https://docs.stripe.com/api/external_account_cards)
-
[POST/v1/accounts/:id/external_accounts](https://docs.stripe.com/api/external_account_cards/create)
-
[POST/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_cards/update)
-
[GET/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_cards/retrieve)
-
[GET/v1/accounts/:id/external_accounts](https://docs.stripe.com/api/external_account_cards/list)
-
[DELETE/v1/accounts/:id/external_accounts/:id](https://docs.stripe.com/api/external_account_cards/delete)
- [Person](https://docs.stripe.com/api/persons)
- [Standard onboarding](https://docs.stripe.com/connect/standard-accounts)
- [Express onboarding](https://docs.stripe.com/connect/express-accounts)
- [handling identity verification with the
API](https://docs.stripe.com/connect/handling-api-verification#person-information)
- [POST/v1/accounts/:id/persons](https://docs.stripe.com/api/persons/create)
- [POST/v1/accounts/:id/persons/:id](https://docs.stripe.com/api/persons/update)
-
[GET/v1/accounts/:id/persons/:id](https://docs.stripe.com/api/persons/retrieve)
- [GET/v1/accounts/:id/persons](https://docs.stripe.com/api/persons/list)
-
[DELETE/v1/accounts/:id/persons/:id](https://docs.stripe.com/api/persons/delete)
- [Top-ups](https://docs.stripe.com/api/topups)
- [Topping up your platform account](https://docs.stripe.com/connect/top-ups)
- [POST/v1/topups](https://docs.stripe.com/api/topups/create)
- [POST/v1/topups/:id](https://docs.stripe.com/api/topups/update)
- [GET/v1/topups/:id](https://docs.stripe.com/api/topups/retrieve)
- [GET/v1/topups](https://docs.stripe.com/api/topups/list)
- [POST/v1/topups/:id/cancel](https://docs.stripe.com/api/topups/cancel)
- [transfer/payout split](https://docs.stripe.com/transfer-payout-split)
- [Creating separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [POST/v1/transfers](https://docs.stripe.com/api/transfers/create)
- [POST/v1/transfers/:id](https://docs.stripe.com/api/transfers/update)
- [GET/v1/transfers/:id](https://docs.stripe.com/api/transfers/retrieve)
- [GET/v1/transfers](https://docs.stripe.com/api/transfers/list)
- [Transfer Reversals](https://docs.stripe.com/api/transfer_reversals)
- [destination charge](https://docs.stripe.com/connect/destination-charges)
-
[transfer_group](https://docs.stripe.com/connect/separate-charges-and-transfers#transfer-options)
- [Reverse
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers#reverse-transfers)
-
[POST/v1/transfers/:id/reversals](https://docs.stripe.com/api/transfer_reversals/create)
-
[POST/v1/transfers/:id/reversals/:id](https://docs.stripe.com/api/transfer_reversals/update)
-
[GET/v1/transfers/:id/reversals/:id](https://docs.stripe.com/api/transfer_reversals/retrieve)
-
[GET/v1/transfers/:id/reversals](https://docs.stripe.com/api/transfer_reversals/list)
- [Secrets](https://docs.stripe.com/api/secret_management)
- [Store data between page
reloads](https://docs.stripe.com/stripe-apps/store-auth-data-custom-objects)
- [GET/v1/apps/secrets](https://docs.stripe.com/api/apps/secret_store/list)
-
[POST/v1/apps/secrets/delete](https://docs.stripe.com/api/apps/secret_store/delete)
- [GET/v1/apps/secrets/find](https://docs.stripe.com/api/apps/secret_store/find)
- [POST/v1/apps/secrets](https://docs.stripe.com/api/apps/secret_store/set)
- [Early Fraud Warning](https://docs.stripe.com/api/radar/early_fraud_warnings)
- [Early fraud
warnings](https://docs.stripe.com/disputes/measuring#early-fraud-warnings)
-
[GET/v1/radar/early_fraud_warnings/:id](https://docs.stripe.com/api/radar/early_fraud_warnings/retrieve)
-
[GET/v1/radar/early_fraud_warnings](https://docs.stripe.com/api/radar/early_fraud_warnings/list)
- [Reviews](https://docs.stripe.com/api/radar/reviews)
- [here](https://docs.stripe.com/radar/reviews)
- [GET/v1/reviews/:id](https://docs.stripe.com/api/radar/reviews/retrieve)
- [GET/v1/reviews](https://docs.stripe.com/api/radar/reviews/list)
-
[POST/v1/reviews/:id/approve](https://docs.stripe.com/api/radar/reviews/approve)
- [Value Lists](https://docs.stripe.com/api/radar/value_lists)
- [Default Stripe
lists](https://docs.stripe.com/radar/lists#managing-list-items)
-
[POST/v1/radar/value_lists](https://docs.stripe.com/api/radar/value_lists/create)
-
[POST/v1/radar/value_lists/:id](https://docs.stripe.com/api/radar/value_lists/update)
-
[GET/v1/radar/value_lists/:id](https://docs.stripe.com/api/radar/value_lists/retrieve)
- [GET/v1/radar/value_lists](https://docs.stripe.com/api/radar/value_lists/list)
-
[DELETE/v1/radar/value_lists/:id](https://docs.stripe.com/api/radar/value_lists/delete)
- [Value List Items](https://docs.stripe.com/api/radar/value_list_items)
-
[POST/v1/radar/value_list_items](https://docs.stripe.com/api/radar/value_list_items/create)
-
[GET/v1/radar/value_list_items/:id](https://docs.stripe.com/api/radar/value_list_items/retrieve)
-
[GET/v1/radar/value_list_items](https://docs.stripe.com/api/radar/value_list_items/list)
-
[DELETE/v1/radar/value_list_items/:id](https://docs.stripe.com/api/radar/value_list_items/delete)
- [Authorizations](https://docs.stripe.com/api/issuing/authorizations)
- [issued card](https://docs.stripe.com/issuing)
- [Authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
-
[POST/v1/issuing/authorizations/:id](https://docs.stripe.com/api/issuing/authorizations/update)
-
[GET/v1/issuing/authorizations/:id](https://docs.stripe.com/api/issuing/authorizations/retrieve)
-
[GET/v1/issuing/authorizations](https://docs.stripe.com/api/issuing/authorizations/list)
-
[POST/v1/issuing/authorizations/:id/approve](https://docs.stripe.com/api/issuing/authorizations/approve)
-
[POST/v1/issuing/authorizations/:id/decline](https://docs.stripe.com/api/issuing/authorizations/decline)
-
[POST/v1/test_helpers/issuing/authorizations](https://docs.stripe.com/api/issuing/authorizations/test_mode_create)
-
[POST/v1/test_helpers/issuing/authorizations/:id/capture](https://docs.stripe.com/api/issuing/authorizations/test_mode_capture)
-
[POST/v1/test_helpers/issuing/authorizations/:id/expire](https://docs.stripe.com/api/issuing/authorizations/test_mode_expire)
-
[POST/v1/test_helpers/issuing/authorizations/:id/finalize_amount](https://docs.stripe.com/api/issuing/authorizations/test_mode_finalize_amount)
-
[POST/v1/test_helpers/issuing/authorizations/:id/increment](https://docs.stripe.com/api/issuing/authorizations/test_mode_increment)
-
[POST/v1/test_helpers/issuing/authorizations/:id/fraud_challenges/respond](https://docs.stripe.com/api/issuing/authorizations/respond_to_fraud_challenges)
-
[POST/v1/test_helpers/issuing/authorizations/:id/reverse](https://docs.stripe.com/api/issuing/authorizations/test_mode_reverse)
- [Cardholders](https://docs.stripe.com/api/issuing/cardholders)
- [How to create a
cardholder](https://docs.stripe.com/issuing/cards/virtual/issue-cards#create-cardholder)
-
[POST/v1/issuing/cardholders](https://docs.stripe.com/api/issuing/cardholders/create)
-
[POST/v1/issuing/cardholders/:id](https://docs.stripe.com/api/issuing/cardholders/update)
-
[GET/v1/issuing/cardholders/:id](https://docs.stripe.com/api/issuing/cardholders/retrieve)
-
[GET/v1/issuing/cardholders](https://docs.stripe.com/api/issuing/cardholders/list)
- [Cards](https://docs.stripe.com/api/issuing/cards)
- [POST/v1/issuing/cards](https://docs.stripe.com/api/issuing/cards/create)
- [POST/v1/issuing/cards/:id](https://docs.stripe.com/api/issuing/cards/update)
- [GET/v1/issuing/cards/:id](https://docs.stripe.com/api/issuing/cards/retrieve)
- [GET/v1/issuing/cards](https://docs.stripe.com/api/issuing/cards/list)
-
[POST/v1/test_helpers/issuing/cards/:id/shipping/deliver](https://docs.stripe.com/api/issuing/cards/test_mode_deliver)
-
[POST/v1/test_helpers/issuing/cards/:id/shipping/fail](https://docs.stripe.com/api/issuing/cards/test_mode_fail)
-
[POST/v1/test_helpers/issuing/cards/:id/shipping/return](https://docs.stripe.com/api/issuing/cards/test_mode_return)
-
[POST/v1/test_helpers/issuing/cards/:id/shipping/ship](https://docs.stripe.com/api/issuing/cards/test_mode_ship)
-
[POST/v1/test_helpers/issuing/cards/:id/shipping/submit](https://docs.stripe.com/api/issuing/cards/test_mode_submit)
- [Disputes](https://docs.stripe.com/api/issuing/disputes)
- [Issuing disputes](https://docs.stripe.com/issuing/purchases/disputes)
-
[POST/v1/issuing/disputes](https://docs.stripe.com/api/issuing/disputes/create)
-
[POST/v1/issuing/disputes/:id](https://docs.stripe.com/api/issuing/disputes/update)
-
[GET/v1/issuing/disputes/:id](https://docs.stripe.com/api/issuing/disputes/retrieve)
- [GET/v1/issuing/disputes](https://docs.stripe.com/api/issuing/disputes/list)
-
[POST/v1/issuing/disputes/:id/submit](https://docs.stripe.com/api/issuing/dispute/submit)
- [Funding
Instructions](https://docs.stripe.com/api/issuing/funding_instructions)
- [top up Issuing Balances](https://docs.stripe.com/issuing/funding/balance)
-
[POST/v1/issuing/funding_instructions](https://docs.stripe.com/api/issuing/funding_instructions/create)
-
[GET/v1/issuing/funding_instructions](https://docs.stripe.com/api/issuing/funding_instructions/list)
-
[POST/v1/test_helpers/issuing/fund_balance](https://docs.stripe.com/api/issuing/funding_instructions/fund)
- [Personalization
Designs](https://docs.stripe.com/api/issuing/personalization_designs)
-
[POST/v1/issuing/personalization_designs](https://docs.stripe.com/api/issuing/personalization_designs/create)
-
[POST/v1/issuing/personalization_designs/:id](https://docs.stripe.com/api/issuing/personalization_designs/update)
-
[GET/v1/issuing/personalization_designs/:id](https://docs.stripe.com/api/issuing/personalization_designs/retrieve)
-
[GET/v1/issuing/personalization_designs](https://docs.stripe.com/api/issuing/personalization_designs/list)
-
[POST/v1/test_helpers/issuing/personalization_designs/:id/activate](https://docs.stripe.com/api/issuing/personalization_designs/activate_testmode)
-
[POST/v1/test_helpers/issuing/personalization_designs/:id/deactivate](https://docs.stripe.com/api/issuing/personalization_designs/deactivate_testmode)
-
[POST/v1/test_helpers/issuing/personalization_designs/:id/reject](https://docs.stripe.com/api/issuing/personalization_designs/reject_testmode)
- [Physical Bundles](https://docs.stripe.com/api/issuing/physical_bundles)
-
[GET/v1/issuing/physical_bundles/:id](https://docs.stripe.com/api/issuing/physical_bundles/retrieve)
-
[GET/v1/issuing/physical_bundles](https://docs.stripe.com/api/issuing/physical_bundles/list)
- [Tokens](https://docs.stripe.com/api/issuing/tokens)
- [view and manage these
tokens](https://docs.stripe.com/issuing/controls/token-management)
-
[POST/v1/issuing/tokens/:id](https://docs.stripe.com/api/issuing/tokens/update)
-
[GET/v1/issuing/tokens/:id](https://docs.stripe.com/api/issuing/tokens/retrieve)
- [GET/v1/issuing/tokens](https://docs.stripe.com/api/issuing/tokens/list)
- [Transactions](https://docs.stripe.com/api/issuing/transactions)
- [Issued card
transactions](https://docs.stripe.com/issuing/purchases/transactions)
-
[POST/v1/issuing/transactions/:id](https://docs.stripe.com/api/issuing/transactions/update)
-
[GET/v1/issuing/transactions/:id](https://docs.stripe.com/api/issuing/transactions/retrieve)
-
[GET/v1/issuing/transactions](https://docs.stripe.com/api/issuing/transactions/list)
-
[POST/v1/test_helpers/issuing/transactions/create_force_capture](https://docs.stripe.com/api/issuing/transactions/test_mode_create_force_capture)
-
[POST/v1/test_helpers/issuing/transactions/create_unlinked_refund](https://docs.stripe.com/api/issuing/transactions/test_mode_create_unlinked_refund)
-
[POST/v1/test_helpers/issuing/transactions/:id/refund](https://docs.stripe.com/api/issuing/transactions/test_mode_refund)
- [Connection Token](https://docs.stripe.com/api/terminal/connection_tokens)
- [Fleet management](https://docs.stripe.com/terminal/fleet/locations)
-
[POST/v1/terminal/connection_tokens](https://docs.stripe.com/api/terminal/connection_tokens/create)
- [Location](https://docs.stripe.com/api/terminal/locations)
-
[POST/v1/terminal/locations](https://docs.stripe.com/api/terminal/locations/create)
-
[POST/v1/terminal/locations/:id](https://docs.stripe.com/api/terminal/locations/update)
-
[GET/v1/terminal/locations/:id](https://docs.stripe.com/api/terminal/locations/retrieve)
-
[GET/v1/terminal/locations](https://docs.stripe.com/api/terminal/locations/list)
-
[DELETE/v1/terminal/locations/:id](https://docs.stripe.com/api/terminal/locations/delete)
- [Reader](https://docs.stripe.com/api/terminal/readers)
- [Connecting to a
reader](https://docs.stripe.com/terminal/payments/connect-reader)
-
[POST/v1/terminal/readers](https://docs.stripe.com/api/terminal/readers/create)
-
[POST/v1/terminal/readers/:id](https://docs.stripe.com/api/terminal/readers/update)
-
[GET/v1/terminal/readers/:id](https://docs.stripe.com/api/terminal/readers/retrieve)
- [GET/v1/terminal/readers](https://docs.stripe.com/api/terminal/readers/list)
-
[DELETE/v1/terminal/readers/:id](https://docs.stripe.com/api/terminal/readers/delete)
-
[POST/v1/terminal/readers/:id/cancel_action](https://docs.stripe.com/api/terminal/readers/cancel_action)
-
[POST/v1/terminal/readers/:id/collect_inputs](https://docs.stripe.com/api/terminal/readers/collect_inputs)
-
[POST/v1/terminal/readers/:id/confirm_payment_intent](https://docs.stripe.com/api/terminal/readers/confirm_payment_intent)
-
[POST/v1/terminal/readers/:id/collect_payment_method](https://docs.stripe.com/api/terminal/readers/collect_payment_method)
-
[POST/v1/terminal/readers/:id/process_payment_intent](https://docs.stripe.com/api/terminal/readers/process_payment_intent)
-
[POST/v1/terminal/readers/:id/process_setup_intent](https://docs.stripe.com/api/terminal/readers/process_setup_intent)
-
[POST/v1/terminal/readers/:id/refund_payment](https://docs.stripe.com/api/terminal/readers/refund_payment)
-
[POST/v1/terminal/readers/:id/set_reader_display](https://docs.stripe.com/api/terminal/readers/set_reader_display)
-
[POST/v1/test_helpers/terminal/readers/:id/present_payment_method](https://docs.stripe.com/api/terminal/readers/present_payment_method)
- [Terminal Hardware
Order](https://docs.stripe.com/api/terminal/hardware_orders)
-
[POST/v1/terminal/hardware_orders](https://docs.stripe.com/api/terminal/hardware_orders/create)
-
[GET/v1/terminal/hardware_orders/:id](https://docs.stripe.com/api/terminal/hardware_orders/retrieve)
-
[GET/v1/terminal/hardware_orders](https://docs.stripe.com/api/terminal/hardware_orders/list)
-
[POST/v1/terminal/hardware_orders/:id/cancel](https://docs.stripe.com/api/terminal/hardware_orders/cancel)
-
[GET/v1/terminal/hardware_orders/preview](https://docs.stripe.com/api/terminal/hardware_orders/preview)
-
[POST/v1/test_helpers/terminal/hardware_orders/:id/mark_ready_to_ship](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_mark_ready_to_ship)
-
[POST/v1/test_helpers/terminal/hardware_orders/:id/deliver](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_deliver)
-
[POST/v1/test_helpers/terminal/hardware_orders/:id/ship](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_ship)
-
[POST/v1/test_helpers/terminal/hardware_orders/:id/mark_undeliverable](https://docs.stripe.com/api/terminal/hardware_orders/test_mode_mark_undeliverable)
- [Terminal Hardware Order
Device](https://docs.stripe.com/api/terminal/hardware_order_devices)
-
[GET/v1/terminal/hardware_order_devices/:id](https://docs.stripe.com/api/terminal/hardware_order_devices/retrieve)
-
[GET/v1/terminal/hardware_order_devices](https://docs.stripe.com/api/terminal/hardware_order_devices/list)
-
[POST/v1/test_helpers/terminal/hardware_order_devices/create_devices_for_order](https://docs.stripe.com/api/terminal/hardware_order_devices/test_mode_create_devices_for_order)
- [Terminal Hardware
Product](https://docs.stripe.com/api/terminal/hardware_products)
-
[GET/v1/terminal/hardware_products/:id](https://docs.stripe.com/api/terminal/hardware_products/retrieve)
-
[GET/v1/terminal/hardware_products](https://docs.stripe.com/api/terminal/hardware_products/list)
- [Terminal Hardware SKU](https://docs.stripe.com/api/terminal/hardware_skus)
-
[GET/v1/terminal/hardware_skus/:id](https://docs.stripe.com/api/terminal/hardware_skus/retrieve)
-
[GET/v1/terminal/hardware_skus](https://docs.stripe.com/api/terminal/hardware_skus/list)
- [Terminal Hardware Shipping
Method](https://docs.stripe.com/api/terminal/hardware_shipping_methods)
-
[GET/v1/terminal/hardware_shipping_methods/:id](https://docs.stripe.com/api/terminal/hardware_shipping_methods/retrieve)
-
[GET/v1/terminal/hardware_shipping_methods](https://docs.stripe.com/api/terminal/hardware_shipping_methods/list)
- [Configuration](https://docs.stripe.com/api/terminal/configuration)
-
[POST/v1/terminal/configurations](https://docs.stripe.com/api/terminal/configuration/create)
-
[POST/v1/terminal/configurations/:id](https://docs.stripe.com/api/terminal/configuration/update)
-
[GET/v1/terminal/configurations/:id](https://docs.stripe.com/api/terminal/configuration/retrieve)
-
[GET/v1/terminal/configurations](https://docs.stripe.com/api/terminal/configuration/list)
-
[DELETE/v1/terminal/configurations/:id](https://docs.stripe.com/api/terminal/configuration/delete)
- [Financial Accounts](https://docs.stripe.com/api/treasury/financial_accounts)
-
[POST/v1/treasury/financial_accounts](https://docs.stripe.com/api/treasury/financial_accounts/create)
-
[POST/v1/treasury/financial_accounts/:id](https://docs.stripe.com/api/treasury/financial_accounts/update)
-
[GET/v1/treasury/financial_accounts/:id](https://docs.stripe.com/api/treasury/financial_accounts/retrieve)
-
[GET/v1/treasury/financial_accounts](https://docs.stripe.com/api/treasury/financial_accounts/list)
- [Financial Account
Features](https://docs.stripe.com/api/treasury/financial_account_features)
-
[POST/v1/treasury/financial_accounts/:id/features](https://docs.stripe.com/api/treasury/financial_account_features/update)
-
[GET/v1/treasury/financial_accounts/:id/features](https://docs.stripe.com/api/treasury/financial_account_features/retrieve)
- [Transactions](https://docs.stripe.com/api/treasury/transactions)
-
[GET/v1/treasury/transactions/:id](https://docs.stripe.com/api/treasury/transactions/retrieve)
-
[GET/v1/treasury/transactions](https://docs.stripe.com/api/treasury/transactions/list)
- [Transaction
Entries](https://docs.stripe.com/api/treasury/transaction_entries)
-
[GET/v1/treasury/transaction_entries/:id](https://docs.stripe.com/api/treasury/transaction_entries/retrieve)
-
[GET/v1/treasury/transaction_entries](https://docs.stripe.com/api/treasury/transaction_entries/list)
- [Outbound Transfers](https://docs.stripe.com/api/treasury/outbound_transfers)
-
[OutboundTransfers](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-transfers)
-
[POST/v1/treasury/outbound_transfers](https://docs.stripe.com/api/treasury/outbound_transfers/create)
-
[GET/v1/treasury/outbound_transfers/:id](https://docs.stripe.com/api/treasury/outbound_transfers/retrieve)
-
[GET/v1/treasury/outbound_transfers](https://docs.stripe.com/api/treasury/outbound_transfers/list)
-
[POST/v1/treasury/outbound_transfers/:id/cancel](https://docs.stripe.com/api/treasury/outbound_transfers/cancel)
-
[POST/v1/test_helpers/treasury/outbound_transfers/:id/fail](https://docs.stripe.com/api/treasury/outbound_transfers/test_mode_fail)
-
[POST/v1/test_helpers/treasury/outbound_transfers/:id/post](https://docs.stripe.com/api/treasury/outbound_transfers/test_mode_post)
-
[POST/v1/test_helpers/treasury/outbound_transfers/:id/return](https://docs.stripe.com/api/treasury/outbound_transfers/test_mode_return)
-
[POST/v1/test_helpers/treasury/outbound_transfers/:id](https://docs.stripe.com/api/treasury/outbound_transfers/test_mode_update)
- [Outbound Payments](https://docs.stripe.com/api/treasury/outbound_payments)
-
[OutboundPayments](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/out-of/outbound-payments)
-
[POST/v1/treasury/outbound_payments](https://docs.stripe.com/api/treasury/outbound_payments/create)
-
[GET/v1/treasury/outbound_payments/:id](https://docs.stripe.com/api/treasury/outbound_payments/retrieve)
-
[GET/v1/treasury/outbound_payments](https://docs.stripe.com/api/treasury/outbound_payments/list)
-
[POST/v1/treasury/outbound_payments/:id/cancel](https://docs.stripe.com/api/treasury/outbound_payments/cancel)
-
[POST/v1/test_helpers/treasury/outbound_payments/:id/fail](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_fail)
-
[POST/v1/test_helpers/treasury/outbound_payments/:id/post](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_post)
-
[POST/v1/test_helpers/treasury/outbound_payments/:id/return](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_return)
-
[POST/v1/test_helpers/treasury/outbound_payments/:id](https://docs.stripe.com/api/treasury/outbound_payments/test_mode_update)
- [Inbound Transfers](https://docs.stripe.com/api/treasury/inbound_transfers)
-
[InboundTransfers](https://docs.stripe.com/docs/treasury/moving-money/financial-accounts/into/inbound-transfers)
-
[POST/v1/treasury/inbound_transfers](https://docs.stripe.com/api/treasury/inbound_transfers/create)
-
[GET/v1/treasury/inbound_transfers/:id](https://docs.stripe.com/api/treasury/inbound_transfers/retrieve)
-
[GET/v1/treasury/inbound_transfers](https://docs.stripe.com/api/treasury/inbound_transfers/list)
-
[POST/v1/treasury/inbound_transfers/:id/cancel](https://docs.stripe.com/api/treasury/inbound_transfers/cancel)
-
[POST/v1/test_helpers/treasury/inbound_transfers/:id/fail](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_fail)
-
[POST/v1/test_helpers/treasury/inbound_transfers/:id/return](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_return)
-
[POST/v1/test_helpers/treasury/inbound_transfers/:id/succeed](https://docs.stripe.com/api/treasury/inbound_transfers/test_mode_succeed)
- [Received Credits](https://docs.stripe.com/api/treasury/received_credits)
-
[GET/v1/treasury/received_credits/:id](https://docs.stripe.com/api/treasury/received_credits/retrieve)
-
[GET/v1/treasury/received_credits](https://docs.stripe.com/api/treasury/received_credits/list)
-
[POST/v1/test_helpers/treasury/received_credits](https://docs.stripe.com/api/treasury/received_credits/test_mode_create)
- [Received Debits](https://docs.stripe.com/api/treasury/received_debits)
-
[GET/v1/treasury/received_debits/:id](https://docs.stripe.com/api/treasury/received_debits/retrieve)
-
[GET/v1/treasury/received_debits](https://docs.stripe.com/api/treasury/received_debits/list)
-
[POST/v1/test_helpers/treasury/received_debits](https://docs.stripe.com/api/treasury/received_debits/test_mode_create)
- [Credit Reversals](https://docs.stripe.com/api/treasury/credit_reversals)
-
[POST/v1/treasury/credit_reversals](https://docs.stripe.com/api/treasury/credit_reversals/create)
-
[GET/v1/treasury/credit_reversals/:id](https://docs.stripe.com/api/treasury/credit_reversals/retrieve)
-
[GET/v1/treasury/credit_reversals](https://docs.stripe.com/api/treasury/credit_reversals/list)
- [Debit Reversals](https://docs.stripe.com/api/treasury/debit_reversals)
-
[POST/v1/treasury/debit_reversals](https://docs.stripe.com/api/treasury/debit_reversals/create)
-
[GET/v1/treasury/debit_reversals/:id](https://docs.stripe.com/api/treasury/debit_reversals/retrieve)
-
[GET/v1/treasury/debit_reversals](https://docs.stripe.com/api/treasury/debit_reversals/list)
- [Feature](https://docs.stripe.com/api/entitlements/feature)
-
[POST/v1/entitlements/features](https://docs.stripe.com/api/entitlements/feature/create)
-
[GET/v1/entitlements/features](https://docs.stripe.com/api/entitlements/feature/list)
-
[POST/v1/entitlements/features/:id](https://docs.stripe.com/api/entitlements/feature/updates)
- [Product Feature](https://docs.stripe.com/api/product-feature)
-
[GET/v1/products/:id/features](https://docs.stripe.com/api/product-feature/list)
-
[POST/v1/products/:id/features](https://docs.stripe.com/api/product-feature/attach)
-
[DELETE/v1/products/:id/features/:id](https://docs.stripe.com/api/product-feature/remove)
- [Active
Entitlement](https://docs.stripe.com/api/entitlements/active-entitlement)
-
[GET/v1/entitlements/active_entitlements/:id](https://docs.stripe.com/api/entitlements/active-entitlement/retrieve)
-
[GET/v1/entitlements/active_entitlements](https://docs.stripe.com/api/entitlements/active-entitlement/list)
- [Scheduled Queries](https://docs.stripe.com/api/sigma/scheduled_queries)
- [scheduled a Sigma query](https://docs.stripe.com/sigma/scheduled-queries)
-
[GET/v1/sigma/scheduled_query_runs/:id](https://docs.stripe.com/api/sigma/scheduled_queries/retrieve)
-
[GET/v1/sigma/scheduled_query_runs](https://docs.stripe.com/api/sigma/scheduled_queries/list)
- [Report Runs](https://docs.stripe.com/api/reporting/report_run)
- [API Access to Reports](https://docs.stripe.com/reporting/statements/api)
- [live-mode API key](https://docs.stripe.com/keys#test-live-modes)
-
[POST/v1/reporting/report_runs](https://docs.stripe.com/api/reporting/report_run/create)
-
[GET/v1/reporting/report_runs/:id](https://docs.stripe.com/api/reporting/report_run/retrieve)
-
[GET/v1/reporting/report_runs](https://docs.stripe.com/api/reporting/report_run/list)
- [Report Types](https://docs.stripe.com/api/reporting/report_type)
-
[GET/v1/reporting/report_types/:id](https://docs.stripe.com/api/reporting/report_type/retrieve)
-
[GET/v1/reporting/report_types](https://docs.stripe.com/api/reporting/report_type/list)
- [Accounts](https://docs.stripe.com/api/financial_connections/accounts)
-
[GET/v1/financial_connections/accounts/:id](https://docs.stripe.com/api/financial_connections/accounts/retrieve)
-
[GET/v1/financial_connections/accounts](https://docs.stripe.com/api/financial_connections/accounts/list)
-
[POST/v1/financial_connections/accounts/:id/disconnect](https://docs.stripe.com/api/financial_connections/accounts/disconnect)
-
[POST/v1/financial_connections/accounts/:id/refresh](https://docs.stripe.com/api/financial_connections/accounts/refresh)
-
[POST/v1/financial_connections/accounts/:id/subscribe](https://docs.stripe.com/api/financial_connections/accounts/subscribe)
-
[POST/v1/financial_connections/accounts/:id/unsubscribe](https://docs.stripe.com/api/financial_connections/accounts/unsubscribe)
- [Account Owner](https://docs.stripe.com/api/financial_connections/ownership)
-
[GET/v1/financial_connections/accounts/:id/owners](https://docs.stripe.com/api/financial_connections/ownership/list)
- [Session](https://docs.stripe.com/api/financial_connections/sessions)
-
[POST/v1/financial_connections/sessions](https://docs.stripe.com/api/financial_connections/sessions/create)
-
[GET/v1/financial_connections/sessions/:id](https://docs.stripe.com/api/financial_connections/sessions/retrieve)
- [Transactions](https://docs.stripe.com/api/financial_connections/transactions)
-
[GET/v1/financial_connections/transactions/:id](https://docs.stripe.com/api/financial-connections/transaction/retrieve)
-
[GET/v1/financial_connections/transactions](https://docs.stripe.com/api/financial_connections/transactions/list)
- [Tax Calculations](https://docs.stripe.com/api/tax/calculations)
- [Calculate tax in your custom payment
flow](https://docs.stripe.com/tax/custom)
-
[POST/v1/tax/calculations](https://docs.stripe.com/api/tax/calculations/create)
-
[GET/v1/tax/calculations/:id/line_items](https://docs.stripe.com/api/tax/calculations/line_items)
-
[GET/v1/tax/calculations/:id](https://docs.stripe.com/api/tax/calculations/retrieve)
- [Tax Registrations](https://docs.stripe.com/api/tax/registrations)
- [automatically collect tax](https://docs.stripe.com/tax)
- [our guide](https://docs.stripe.com/tax/registering)
- [Using the Registrations API](https://docs.stripe.com/tax/registrations-api)
-
[POST/v1/tax/registrations](https://docs.stripe.com/api/tax/registrations/create)
-
[POST/v1/tax/registrations/:id](https://docs.stripe.com/api/tax/registrations/update)
-
[GET/v1/tax/registrations/:id](https://docs.stripe.com/api/tax/registrations/retrieve)
- [GET/v1/tax/registrations](https://docs.stripe.com/api/tax/registrations/all)
- [Tax Transactions](https://docs.stripe.com/api/tax/transactions)
- [Calculate tax in your custom payment
flow](https://docs.stripe.com/tax/custom#tax-transaction)
-
[POST/v1/tax/transactions/create_reversal](https://docs.stripe.com/api/tax/transactions/create_reversal)
-
[POST/v1/tax/transactions/create_from_calculation](https://docs.stripe.com/api/tax/transactions/create_from_calculation)
-
[GET/v1/tax/transactions/:id/line_items](https://docs.stripe.com/api/tax/transactions/line_items)
-
[GET/v1/tax/transactions/:id](https://docs.stripe.com/api/tax/transactions/retrieve)
- [Tax Settings](https://docs.stripe.com/api/tax/settings)
- [Using the Settings API](https://docs.stripe.com/tax/settings-api)
- [POST/v1/tax/settings](https://docs.stripe.com/api/tax/settings/update)
- [GET/v1/tax/settings](https://docs.stripe.com/api/tax/settings/retrieve)
- [Verification
Session](https://docs.stripe.com/api/identity/verification_sessions)
- [verification check](https://docs.stripe.com/identity/verification-checks)
- [multiple statuses](https://docs.stripe.com/identity/how-sessions-work)
- [The Verification Sessions
API](https://docs.stripe.com/identity/verification-sessions)
-
[POST/v1/identity/verification_sessions](https://docs.stripe.com/api/identity/verification_sessions/create)
-
[POST/v1/identity/verification_sessions/:id](https://docs.stripe.com/api/identity/verification_sessions/update)
-
[GET/v1/identity/verification_sessions/:id](https://docs.stripe.com/api/identity/verification_sessions/retrieve)
-
[GET/v1/identity/verification_sessions](https://docs.stripe.com/api/identity/verification_sessions/list)
-
[POST/v1/identity/verification_sessions/:id/cancel](https://docs.stripe.com/api/identity/verification_sessions/cancel)
-
[POST/v1/identity/verification_sessions/:id/redact](https://docs.stripe.com/api/identity/verification_sessions/redact)
- [Verification
Report](https://docs.stripe.com/api/identity/verification_reports)
- [Accessing verification
results](https://docs.stripe.com/identity/verification-sessions#results)
-
[GET/v1/identity/verification_reports/:id](https://docs.stripe.com/api/identity/verification_reports/retrieve)
-
[GET/v1/identity/verification_reports](https://docs.stripe.com/api/identity/verification_reports/list)
- [Crypto Onramp Session](https://docs.stripe.com/api/crypto/onramp_sessions)
- [Integrate the onramp](https://docs.stripe.com/crypto/integrate-the-onramp)
-
[POST/v1/crypto/onramp_sessions](https://docs.stripe.com/api/crypto/onramp_sessions/create)
-
[GET/v1/crypto/onramp_sessions/:id](https://docs.stripe.com/api/crypto/onramp_sessions/retrieve)
-
[GET/v1/crypto/onramp_sessions](https://docs.stripe.com/api/crypto/onramp_sessions/list)
- [Crypto Onramp Quotes](https://docs.stripe.com/api/crypto/onramp_quotes)
- [Quotes API](https://docs.stripe.com/crypto/quotes-api)
-
[GET/v1/crypto/onramp/quotes](https://docs.stripe.com/api/crypto/onramp_quotes/retrieve)
- [Climate Order](https://docs.stripe.com/api/climate/order)
- [POST/v1/climate/orders](https://docs.stripe.com/api/climate/order/create)
- [POST/v1/climate/orders/:id](https://docs.stripe.com/api/climate/order/update)
-
[GET/v1/climate/orders/:id](https://docs.stripe.com/api/climate/order/retrieve)
- [GET/v1/climate/orders](https://docs.stripe.com/api/climate/order/list)
-
[POST/v1/climate/orders/:id/cancel](https://docs.stripe.com/api/climate/order/cancel)
- [Climate Product](https://docs.stripe.com/api/climate/product)
-
[GET/v1/climate/products/:id](https://docs.stripe.com/api/climate/product/retrieve)
- [GET/v1/climate/products](https://docs.stripe.com/api/climate/product/list)
- [Climate Supplier](https://docs.stripe.com/api/climate/supplier)
-
[GET/v1/climate/suppliers/:id](https://docs.stripe.com/api/climate/supplier/retrieve)
- [GET/v1/climate/suppliers](https://docs.stripe.com/api/climate/supplier/list)
- [Forwarding Request](https://docs.stripe.com/api/forwarding/request)
- [Forward card details to third-party API
endpoints](https://docs.stripe.com/payments/forwarding)
-
[POST/v1/forwarding/requests](https://docs.stripe.com/api/forwarding/forwarding_requests/create)
-
[GET/v1/forwarding/requests/:id](https://docs.stripe.com/api/forwarding/forwarding_requests/retrieve)
-
[GET/v1/forwarding/requests](https://docs.stripe.com/api/forwarding/forwarding_requests/list)
- [Webhook Endpoints](https://docs.stripe.com/api/webhook_endpoints)
- [webhook endpoints](https://docs.stripe.com/webhooks/)
- [the dashboard](https://dashboard.stripe.com/webhooks)
- [Setting up webhooks](https://docs.stripe.com/webhooks/configure)
-
[POST/v1/webhook_endpoints](https://docs.stripe.com/api/webhook_endpoints/create)
-
[POST/v1/webhook_endpoints/:id](https://docs.stripe.com/api/webhook_endpoints/update)
-
[GET/v1/webhook_endpoints/:id](https://docs.stripe.com/api/webhook_endpoints/retrieve)
- [GET/v1/webhook_endpoints](https://docs.stripe.com/api/webhook_endpoints/list)
-
[DELETE/v1/webhook_endpoints/:id](https://docs.stripe.com/api/webhook_endpoints/delete)