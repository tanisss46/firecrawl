# Expanding responses

## Learn how to reduce the number of requests you make to the Stripe API by expanding objects in responses.

This guide describes how to request additional properties from the API. You will
learn to modify your requests to include:

- properties from related objects
- properties from distantly related objects
- additional properties on all objects in a list
- properties that aren’t included by default in a response

## How it works

The Stripe API is organized into resources represented by objects with state,
configuration, and contextual properties. These objects all have unique IDs that
you can use to retrieve, update, and delete them. The API also uses these IDs to
link related objects together. A [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/object), for example,
links to a [Customer](https://docs.stripe.com/api/customers/object) by the
[Customer
ID](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer).

```
{
 "id": "cs_test_KdjLtDPfAjT1gq374DMZ3rHmZ9OoSlGRhyz8yTypH76KpN4JXkQpD2G0",
 "object": "checkout.session",
 ...
 "customer": "cus_HQmikpKnGHkNwW",
 ...
}
```

In cases where you need information from a linked object, you can retrieve the
linked object in a new call using its ID. However, this approach requires two
API requests to access just one value. If you need information from multiple
linked objects, each would also require separate requests, which all adds to the
latency and complexity of your application.

The API has an Expand feature that allows you to retrieve linked objects in a
single call, effectively replacing the object ID with all its properties and
values. For example, say you wanted to access details on a customer tied to a
given Checkout Session. You would retrieve the Checkout Session and pass the
`customer` property to the `expand` array, which tells Stripe to include the
entire Customer object in the response:

```
curl -G https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=customer
```

Which returns the Checkout Session with the full Customer object instead of its
ID:

```
{
 "id": "cs_test_KdjLtDPfAjT1gq374DMZ3rHmZ9OoSlGRhyz8yTypH76KpN4JXkQpD2G0",
 "object": "checkout.session",
 ...
 "customer": {
 "id": "cus_HQmikpKnGHkNwW",
 "object": "customer",
 ...
 "metadata": {
 "user_id": "user_xyz"
 },
 ...
 }
}
```

#### Note

Not all properties can be expanded. The API reference marks expandable
properties with the “Expandable” label.

## Expanding multiple properties

To expand multiple properties in one call, add additional items to the expand
array. For example, if you want to expand both the
[customer](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer)
and the
[payment_intent](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_intent)
for a given Checkout Session, you would pass `expand` an array with both the
`customer` and `payment_intent` strings:

```
curl -G https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=customer \
 -d "expand[]"=payment_intent
```

## Expanding multiple levels

If the value you want is nested deeply across multiple linked resources, you can
reach it by recursively expanding using dot notation. For instance, if you
needed to know the type of payment method that was used for a given Checkout
Session, you would first retrieve the Checkout Session’s payment intent, then
retrieve the payment intent’s linked payment method to get its type. With
`expand`, you can do this in one call:

```
curl -G https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"="payment_intent.payment_method"
```

Which returns the Checkout Session with the full
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object) and
[PaymentMethod](https://docs.stripe.com/api/payment_methods/object) objects
instead of their IDs:

```
{
 "id": "cs_test_KdjLtDPfAjT1gq374DMZ3rHmZ9OoSlGRhyz8yTypH76KpN4JXkQpD2G0",
 "object": "checkout.session",
 ...
 "mode": "payment",
 "payment_intent": {
 "id": "pi_1GkXXDLHughnNhxyLlsnvUuY",
 "object": "payment_intent",
 "amount": 100,
 ...
 "charges": {...},
"client_secret": "pi_1GkXXDLHughnNhxyLlsnvUuY_secret_oLbwpm0ME0ieJ9Aykz2SwKzj5",
 ...
 "payment_method": {
 "id": "pm_1GkXXuLHughnNhxy8xpAdGtf",
 "object": "payment_method",
 "billing_details": {...},
 "card": {...},
```

See all 49 lines
#### Note

Expansions have a maximum depth of four levels. Meaning that an `expand` string
can contain no more than four properties:
`property1.property2.property3.property4`.

## Expanding properties in lists

When the API returns a list of objects, you can use the `data` keyword to expand
a given property on each object in that list. For example, say you need
information about the payment methods used by one of your customers. To get this
information, you would [list the customer’s
PaymentIntents](https://docs.stripe.com/api/payment_intents/list#list_payment_intents-customer),
which returns an object with the following structure:

```
{
 "object": "list",
 "data": [
 {
 "id": "pi_1GrvBKLHughnNhxy6N28q8gt",
 "object": "payment_intent",
 "amount": 1000,
 ...
 "payment_method": "pm_1GrvBxLHughnNhxyJjtBtHcc",
 ...
 },
```

See all 23 lines
#### Note

All lists returned in the API have the above structure, where the `data`
property contains the array of objects being listed. You can use the `data`
keyword in any position in an expand string to move the expand cursor into the
list.

Rather than looping through each payment intent in the list and retrieving the
linked payment methods in separate calls, you can expand all the payment methods
at once using the `data` keyword:

```
curl -G https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "expand[]"="data.payment_method"
```

The list then includes the full payment method object on each payment intent:

```
{
 "object": "list",
 "data": [
 {
 "id": "pi_1GrvBKLHughnNhxy6N28q8gt",
 "object": "payment_intent",
 "amount": 1000,
 ...
 "payment_method": {
 "id": "pm_1GrvBxLHughnNhxyJjtBtHcc",
 "object": "payment_method",
 "billing_details": {...},
 "card": {
 "brand": "visa",
 ...
```

See all 65 lines
#### Note

Expanding responses has performance implications. To keep requests fast, try to
limit many nested expansions on list requests.

## Using expansion to request includable properties

In some cases, resources have properties that aren’t included by default. One
example is the Checkout Session’s
[line_items](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-line_items)
property, which is only included in responses if requested using the `expand`
parameter, for example:

```
curl -G https://api.stripe.com/v1/checkout/sessions/{{SESSION_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=line_items
```

#### Note

Like other expandable properties, the API reference marks properties that are
includable with the “Expandable” label.

## Using expansion with webhooks

You can’t receive [webhook](https://docs.stripe.com/webhooks) events with
properties auto-expanded. Objects sent in events are always in their minimal
form. To access nested values in expandable properties, you must retrieve the
object in a separate call within your webhook handler.

## Links

- [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object)
- [Customer](https://docs.stripe.com/api/customers/object)
- [Customer
ID](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer)
-
[payment_intent](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-payment_intent)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods/object)
- [list the customer’s
PaymentIntents](https://docs.stripe.com/api/payment_intents/list#list_payment_intents-customer)
-
[line_items](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-line_items)
- [webhook](https://docs.stripe.com/webhooks)