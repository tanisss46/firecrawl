# Multibanco payments with SourcesDeprecated

## Use Sources to accept payments using Multibanco, the most popular payment method in Portugal.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently integrate with Multibanco using the Sources API, you
must [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

For information about integrating Multibanco with the current APIs, see
[Multibanco payments](https://docs.stripe.com/payments/multibanco).

Stripe users in Europe and the United States can accept Multibanco payments from
customers in Portugal using [Sources](https://docs.stripe.com/sources)—a single
integration path for creating payments using any supported method.

During the payment process, a [Source](https://docs.stripe.com/api#sources)
object is created and your customer is either redirected to the Multibanco
website, your website, or a Multibanco ATM to send the funds. After completing
this, your integration uses the source to make a charge request and complete the
payment.

Multibanco is a
[push](https://docs.stripe.com/sources#pull-or-push-of-funds)-based,
[single-use](https://docs.stripe.com/sources#single-use-or-reusable) and
[synchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
method of payment. This means your customer takes action to send the amount to
you through a
[receiver](https://docs.stripe.com/sources#flow-for-customer-action). The
pushing of funds may take as little as a few minutes or at most seven days,
since your customer must do this outside of your checkout flow. Once the funds
have been received the amount is immediately available to be charged. Upon
charge, there is immediate confirmation about the success or failure of a
payment.

[Create a Source
object](https://docs.stripe.com/sources/multibanco#create-source)
A `Source` object is either created client-side using
[Stripe.js](https://docs.stripe.com/payments/elements) or server-side using the
[Source creation endpoint](https://docs.stripe.com/api#create_source), with the
following parameters:

ParameterValue`type`multibanco`amount`A positive integer in the [smallest
currency unit](https://docs.stripe.com/currencies#zero-decimal) representing the
amount to charge the customer (for example, 1099 for a 10.99 EUR
payment).`currency`eur (Multibanco must always use
Euros)`redirect[return_url]`The URL the customer should be redirected to after
the authorization process.`owner[email]`The full email address of the customer.
To create a source with [Stripe.js](https://docs.stripe.com/payments/elements),
first include the library within your website and set your [publishable API
key](https://dashboard.stripe.com/apikeys). Once included, use the following
`createSource` method to create a source client-side:

```
stripe.createSource({
 type: 'multibanco',
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
details for the method of payment used. Information specific to Multibanco is
provided within the `multibanco` subhash.

```
{
 "id": "src_16xhynE8WzK49JbAs9M21jaR",
 "object": "source",
 "amount": 1099,
 "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
 "created": 1445277809,
 "currency": "eur",
 "flow": "receiver",
 "livemode": true,
 "owner": {
```

See all 41 lines
### Source creation in mobile applications

If you’re building an iOS or Android app, you can implement sources using our
mobile SDKs. Refer to our sources documentation for
[iOS](https://docs.stripe.com/mobile/ios/sources) or
[Android](https://docs.stripe.com/mobile/android/sources) to learn more.

[Have the customer send the
funds](https://docs.stripe.com/sources/multibanco#customer-action)
When creating a source, its status is initially set to `pending` and cannot yet
be used to make a charge request. To pay with Multibanco, your customers will
need to initiate a transfer of funds from their bank account using reference and
entity numbers provided by you and either their computer, phone, or local ATM.

Portuguese merchants will often display these details within their checkout flow
after the customer has confirmed their purchase and by including them in an
order confirmation email.

You may also redirect your customer to a Multibanco-hosted page that will
display these details for you, by using the URL provided within
the`redirect[url]` attribute of the `Source` object. Multibanco then redirects
them back to the URL provided as a value of `redirect[return_url]`, regardless
of whether funds have been sent or not.

When the customer does send funds, the `Source` object’s status will transition
to `chargeable`, allowing you to charge the source and complete the transaction.
If you don’t do this, the status will transition to `canceled` after six hours.

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

To integrate Multibanco within a mobile application, provide your application
URI scheme as the `redirect[return_url]` value. By doing so, your customers are
returned to your app after completing authorization. Refer to our Sources
documentation for [iOS](https://docs.stripe.com/mobile/ios/sources) or
[Android](https://docs.stripe.com/mobile/android/sources) to learn more.

### Testing the redirect and payment

When creating a `Source` object using your test API keys, the test payment is
fulfilled with a three second delay. Use one of the following test email
addresses when you need to test Multibanco payments under different conditions.

EmailDescription`{any_prefix}+fill_never@{any_domain}`Funds are never sent to
the receiver address.`{any_prefix}+fill_now@{any_domain}`The next time that the
receiver is retrieved after creation, it has received the full amount.
The URL returned in the `redirect[url]` field of takes you to a sample payment
page. Returning from this page takes you to the URL specified in
`redirect[return_url]`.

[Charge the Source](https://docs.stripe.com/sources/multibanco#charge-request)
Once the customer has pushed the funds, the source’s `status` transitions to
`chargeable` and it can be used to make a charge request. This transition
happens asynchronously and may occur after the customer was redirected back to
your website.

It may take minutes, hours, or days for a customer to send the funds after
following and returning from the redirect.

For this reason it is essential that your integration rely on
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

Multibanco Sources are
[single-use](https://docs.stripe.com/sources#single-use-or-reusable) and cannot
be used for recurring or additional payments. Refer to our [Sources &
Customers](https://docs.stripe.com/sources/customers) guide for more information
on how single-use Sources interact with
[Customers](https://docs.stripe.com/api/customers).

[Confirm that the charge has
succeeded](https://docs.stripe.com/sources/multibanco#charge-confirmation)
Since Multibanco is a
[synchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
payment method and the customer has already sent funds, unless there is an
unexpected error, the [Charge](https://docs.stripe.com/api#charge_object) will
immediately succeed.

You will also receive the following webhook event as the charge is created:

EventDescription`charge.succeeded`The charge succeeded and the payment is
complete.
We recommend that you rely on the `charge.succeeded` webhook event to notify
your customer that the payment process has been completed and their order is
confirmed. Please refer to our [best
practices](https://docs.stripe.com/sources/best-practices) for more details on
how to best integrate payment methods using webhooks.

### Disputed payments

The risk of fraud or unrecognized payments is extremely low with Multibanco as
the customer has to push funds from their bank account. As such, there is no
dispute process that can result in a chargeback and funds withdrawn from your
Stripe account.

### Mispayments

As a customer can make a payment at any time directly through the ATM, it is
possible, although unlikely, for a customer to supply funds to a canceled or
expired source. In these cases, Stripe automatically initiates the refund
process for the mispaid amount as described above.

### Refunds

Payments made with Multibanco can only be submitted for refund within 180 days
from the date of the original charge. After 180 days, it is no longer possible
to refund the charge.

Multibanco payments can be refunded through either the
[Dashboard](https://dashboard.stripe.com/test/payments) or
[API](https://docs.stripe.com/api#create_refund). Multibanco does not itself
provide any facility for refunds, and so Stripe handles this by creating an IBAN
credit transfer. We contact the customer at the email address provided during
source creation, and a credit is sent to the customer once they’ve supplied
their account information. No interaction from the merchant is required beyond
the initial refund request.

Some users may want to manage the collection of the refund IBAN details
themselves. Multibanco refunds require the customer’s IBAN number, account
holder name, and the full address including street, city, country, and postal
code. Please [contact us](https://support.stripe.com/email) to learn more about
this option.

### Sources expiration

A `chargeable` Multibanco source must be charged within six hours of becoming
`chargeable`. If it is not, its status is automatically transitioned to
`canceled` and your integration receives a `source.canceled` webhook event. Once
a chargeable source is canceled, the customer’s authenticated Multibanco payment
is refunded automatically—no money is moved into your account. For this reason,
make sure the order is canceled on your end and the customer is notified when
you receive the `source.canceled` event.

Additionally, `pending` sources are canceled after seven days if they’re not
used to receive funds. This ensures that all sources eventually transition out
of their `pending` state to the `canceled` state if they’re not used.

## See also

- [Other supported payment methods](https://docs.stripe.com/sources)
- [Sources API reference](https://docs.stripe.com/api#sources)
- [Best practices](https://docs.stripe.com/sources/best-practices)

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [Multibanco payments](https://docs.stripe.com/payments/multibanco)
- [Dashboard](https://dashboard.stripe.com/account/payments/settings)
- [Multibanco Terms of Service](https://stripe.com/multibanco/legal)
- [Sources](https://docs.stripe.com/sources)
- [Source](https://docs.stripe.com/api#sources)
- [push](https://docs.stripe.com/sources#pull-or-push-of-funds)
- [single-use](https://docs.stripe.com/sources#single-use-or-reusable)
-
[synchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
- [receiver](https://docs.stripe.com/sources#flow-for-customer-action)
- [Stripe.js](https://docs.stripe.com/payments/elements)
- [Source creation endpoint](https://docs.stripe.com/api#create_source)
- [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal)
- [publishable API key](https://dashboard.stripe.com/apikeys)
- [iOS](https://docs.stripe.com/mobile/ios/sources)
- [Android](https://docs.stripe.com/mobile/android/sources)
- [webhooks](https://docs.stripe.com/webhooks)
- [best practices](https://docs.stripe.com/sources/best-practices)
- [Sources & Customers](https://docs.stripe.com/sources/customers)
- [Customers](https://docs.stripe.com/api/customers)
- [Charge](https://docs.stripe.com/api#charge_object)
- [Dashboard](https://dashboard.stripe.com/test/payments)
- [API](https://docs.stripe.com/api#create_refund)
- [contact us](https://support.stripe.com/email)