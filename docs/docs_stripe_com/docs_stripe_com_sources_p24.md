# Przelewy24 payments with SourcesDeprecated

## Use Sources to accept payments using Przelewy24, the most popular payment method in Poland.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently integrate with Przelewy24 using the Sources API, you
must [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

For information about integrating Przelewy24 with the current APIs, see
[Przelewy24 payments](https://docs.stripe.com/payments/p24).

Stripe users in Europe and the United States can accept
[Przelewy24](https://www.przelewy24.pl/) payments from customers in Poland using
[Sources](https://docs.stripe.com/sources).

During the payment process, a [Source](https://docs.stripe.com/api#sources)
object is created and your customer is redirected to their bank’s website or
mobile application to authorize the payment. After completing this, your
integration uses the source to make a charge request and complete the payment.

Przelewy24 is a
[push](https://docs.stripe.com/sources#pull-or-push-of-funds)-based,
[single-use](https://docs.stripe.com/sources#single-use-or-reusable) and
[synchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
method of payment. This means your customer takes action to send the amount to
you through a
[redirect](https://docs.stripe.com/sources#flow-for-customer-action) and there
is immediate confirmation about the success or failure of a payment.

[Create a Source object](https://docs.stripe.com/sources/p24#create-source)
A `Source` object is either created client-side using
[Stripe.js](https://docs.stripe.com/payments/elements) or server-side using the
[Source creation endpoint](https://docs.stripe.com/api#create_source), with the
following parameters:

ParameterValue`type`p24`amount`A positive integer in the [smallest currency
unit](https://docs.stripe.com/currencies#zero-decimal) representing the amount
to charge the customer (for example, 1099 for a 10.99 EUR payment).`currency`eur
or pln (Przelewy24 payments must be in either Euros or Polish
Zloty).`owner[name]` (optional)The name of the account holder.`owner[email]`The
email address of the account holder.`redirect[return_url]`The URL the customer
should be redirected to after the authorization process.`statement_descriptor`
(optional)A custom statement descriptor for the payment.
To create a source with [Stripe.js](https://docs.stripe.com/payments/elements),
first include the library within your website and set your [publishable API
key](https://dashboard.stripe.com/apikeys). Once included, use the following
`createSource` method to create a source client-side:

```
stripe.createSource({
 type: 'p24',
 amount: 1099,
 currency: 'eur',
 owner: {
 name: 'Jenny Rosen',
 email: 'jenny.rosen@example.com',
 },
 redirect: {
 return_url: '__TOKEN_PLACEHOLDER_0__',
 },
}).then(function(result) {
 // handle result.error or result.source
});
```

Using either method, Stripe returns a `Source` object containing the relevant
details for the method of payment used. Information specific to Przelewy24 is
provided within the `p24` subhash.

```
{
 "id": "src_16xhynE8WzK49JbAs9M21jaR",
 "object": "source",
 "amount": 1099,
 "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
 "created": 1445277809,
 "currency": "eur",
 "flow": "redirect",
 "livemode": true,
 "owner": {
```

See all 32 lines
### Source creation in mobile applications

If you’re building an iOS or Android app, you can implement sources using our
mobile SDKs. Refer to our sources documentation for
[iOS](https://docs.stripe.com/mobile/ios/sources) or
[Android](https://docs.stripe.com/mobile/android/sources) to learn more.

### Statement descriptors with Przelewy24

Przelewy24 lets you provide a custom [statement
descriptor](https://docs.stripe.com/get-started/account/activate#public-business-information)
before the customer is redirected to authenticate the payment. It can be
specified by providing `statement_descriptor` when creating a source.

Additionally, when the customer approves the payment, a unique reference will be
stored on the Source under `p24[reference]`. You can share this reference with
your customer to help locate payments.

Providing a custom statement descriptor within a subsequent charge request has
no effect.

### Error codes

Source creation for Przelewy24 payments may return any of the following errors:

ErrorDescription`payment_method_not_available`The payment method is currently
not available. You should invite your customer to fallback to another payment
method to proceed.`processing_error`An unexpected error occurred preventing us
from creating the source. The source creation should be
retried.`invalid_owner_email`The owner email address is invalid. It must be a
valid email address.`invalid_currency`The currency is not supported for
Przelewy24. It must either be `'eur'` or `'pln'`.[Have the customer authorize
the payment](https://docs.stripe.com/sources/p24#customer-action)
When creating a source, its status is initially set to `pending` and cannot yet
be used to make a charge request. Your customer must authorize a Przelewy24
payment to make the source chargeable. To allow your customer to authorize the
payment, redirect them to the URL provided within the`redirect[url]` attribute
of the `Source` object.

After the authorization process, your customer is redirected back to the URL
provided as a value of `redirect[return_url]`. This happens regardless of
whether authorization was successful or not. If the customer has authorized the
payment, the `Source` object’s status is updated to `chargeable` and it is ready
to use in a charge request. If your customer declines the payment, the status
transitions to `failed`.

Stripe populates the `redirect[return_url]` with the following GET parameters
when returning your customer to your website:

- `source`: a string representing the original ID of the `Source` object
- `livemode`: indicates if this is a live payment, either `true` or `false`
- `client_secret`: used to confirm that the returning customer is the same one
who triggered the creation of the source (source IDs are not considered secret)

You may include any other GET parameters you may need when specifying
`redirect[return_url]`. Do not use the above as parameter names yourself as
these would be overridden with the values we populate.

### Mobile applications

To integrate Przelewy24 within a mobile application, provide your application
URI scheme as the `redirect[return_url]` value. By doing so, your customers are
returned to your app after completing authorization. Refer to our Sources
documentation for [iOS](https://docs.stripe.com/mobile/ios/sources) or
[Android](https://docs.stripe.com/mobile/android/sources) to learn more.

If you are integrating without using our mobile SDKs, the redirect URL must be
opened using the device’s native browser. The use of in-app web views and
containers can prevent your customer from completing authentication—resulting in
a lower conversion rate.

### Testing the redirect process

When creating a `Source` object using your test API keys, you can follow the URL
returned in the `redirect[url]` field. This leads to a Stripe page that displays
information about the API request, and where you can either authorize or cancel
the payment. Authorizing the payment redirects you to the URL specified in
`redirect[return_url]`.

Alternatively, to accelerate testing, use the following value for
`owner[email]`, where `xxx_` is any prefix of your choice (these patterns are
significant only in testmode):

Email AddressEffect`xxx_chargeable@example.com`The source will be created as
`pending`, but automatically transition to `chargeable` within seconds of its
creation.[Charge the Source](https://docs.stripe.com/sources/p24#charge-request)
Once the customer has authenticated the payment, the source’s `status`
transitions to `chargeable` and it can be used to make a charge request. This
transition happens asynchronously and may occur after the customer was
redirected back to your website.

Some customers using Przelewy24 assume that the order process is complete once
they have authenticated the payment and received confirmation from their bank.
This results in customers who close their browser instead of following the
redirect and returning to your app or website.

For these reasons it is essential that your integration rely on
[webhooks](https://docs.stripe.com/webhooks) to determine when the source
becomes chargeable in order to create a charge. Please refer to our [best
practices](https://docs.stripe.com/sources/best-practices) for more details on
how to best integrate payment methods using webhooks.

### Webhooks

The following webhook events are sent to notify you about changes to the
source’s status:

EventDescription`source.chargeable`A `Source` object becomes `chargeable` after
a customer has authenticated and verified a payment.`source.failed`A `Source`
object failed to become chargeable as your customer declined to authenticate the
payment.`source.canceled`A `Source` object expired and cannot be used to create
a charge.
### Make a charge request using the source

Once the source is chargeable, from your `source.chargeable` webhook handler,
you can make a charge request using the source ID as the value for the `source`
parameter to complete the payment.

```
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount="1099" \
 -d currency="eur" \
 -d source=src_18eYalAHEMiOZZp1l9ZTjSU0
```

Przelewy24 Sources are
[single-use](https://docs.stripe.com/sources#single-use-or-reusable) and cannot
be used for recurring or additional payments. Refer to our [Sources &
Customers](https://docs.stripe.com/sources/customers) guide for more information
on how single-use Sources interact with
[Customers](https://docs.stripe.com/api/customers).

[Confirm that the charge has
succeeded](https://docs.stripe.com/sources/p24#charge-confirmation)
Since Przelewy24 is a
[synchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
payment method and the customer has already authenticated the payment as part of
the redirect, unless there is an unexpected error, the
[Charge](https://docs.stripe.com/api#charge_object) will immediately succeed.

EventDescription`charge.succeeded`The charge succeeded and the payment is
complete.
We recommend that you rely on the `charge.succeeded` webhook event to notify
your customer that the payment process has been completed and their order is
confirmed. Please refer to our [best
practices](https://docs.stripe.com/sources/best-practices) for more details on
how to best integrate payment methods using webhooks.

### Disputed payments

The risk of fraud or unrecognized payments is extremely low with Przelewy24 as
the customer must authenticate the payment with their bank. As such, there is no
dispute process that can result in a chargeback and funds withdrawn from your
Stripe account.

### Refunds

Payments made with Przelewy24 can only be submitted for refund within 180 days
from the date of the original charge. After 180 days, it is no longer possible
to refund the charge.

### Sources expiration

A `chargeable` Przelewy24 source must be charged within six hours of becoming
`chargeable`. If it is not, its status is automatically transitioned to
`canceled` and your integration receives a `source.canceled` webhook event. Once
a chargeable source is canceled, the customer’s authenticated Przelewy24 payment
is refunded automatically—no money is moved into your account. For this reason,
make sure the order is canceled on your end and the customer is notified when
you receive the `source.canceled` event.

Additionally, `pending` sources are canceled after 1 hour if they aren’t used to
authenticate a payment to make sure that all sources transition out of their
`pending` state to the `canceled` state if they aren’t used.

## See also

- [Other supported payment methods](https://docs.stripe.com/sources)
- [Sources API reference](https://docs.stripe.com/api#sources)
- [Best practices](https://docs.stripe.com/sources/best-practices)

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [Przelewy24 payments](https://docs.stripe.com/payments/p24)
- [Dashboard](https://dashboard.stripe.com/account/payments/settings)
- [Przelewy24](https://www.przelewy24.pl)
- [Sources](https://docs.stripe.com/sources)
- [Source](https://docs.stripe.com/api#sources)
- [push](https://docs.stripe.com/sources#pull-or-push-of-funds)
- [single-use](https://docs.stripe.com/sources#single-use-or-reusable)
-
[synchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
- [redirect](https://docs.stripe.com/sources#flow-for-customer-action)
- [Stripe.js](https://docs.stripe.com/payments/elements)
- [Source creation endpoint](https://docs.stripe.com/api#create_source)
- [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal)
- [publishable API key](https://dashboard.stripe.com/apikeys)
- [iOS](https://docs.stripe.com/mobile/ios/sources)
- [Android](https://docs.stripe.com/mobile/android/sources)
- [statement
descriptor](https://docs.stripe.com/get-started/account/activate#public-business-information)
- [webhooks](https://docs.stripe.com/webhooks)
- [best practices](https://docs.stripe.com/sources/best-practices)
- [Sources & Customers](https://docs.stripe.com/sources/customers)
- [Customers](https://docs.stripe.com/api/customers)
- [Charge](https://docs.stripe.com/api#charge_object)