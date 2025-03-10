# Alipay payments with Sources

## Use Sources to accept payments using Alipay, a popular payment method in China.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently integrate with Alipay using the Sources API, you must
[migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

For information about integrating Alipay with the current APIs, see [Alipay
payments](https://docs.stripe.com/payments/alipay).

Stripe users can use [Sources](https://docs.stripe.com/sources) to accept
[Alipay](https://alipay.com/) payments from customers from China.

During the payment process, a [Source](https://docs.stripe.com/api#sources)
object is created and your customer is redirected to Alipay for authorization.
After completing this, your integration uses the source to make a charge request
and complete the payment.

Alipay is a [push](https://docs.stripe.com/sources#pull-or-push-of-funds)-based,
[single-use](https://docs.stripe.com/sources#single-use-or-reusable) and
[synchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
method of payment. This means that your customer takes action to authorize the
push of funds through a
[redirect](https://docs.stripe.com/sources#flow-for-customer-action). There is
immediate confirmation about the success or failure of a payment.

[Create a Source object](https://docs.stripe.com/sources/alipay#create-source)
A `Source` object is either created client-side using
[Stripe.js](https://docs.stripe.com/payments/elements) or server-side using the
[Source creation endpoint](https://docs.stripe.com/api#create_source), with the
following parameters:

ParameterValue`type`alipay`currency`cny or the default currency for your
country. Accepted currencies are aud, cad, cny, eur, gbp, hkd, jpy, nzd, sgd, or
usd. Users in Denmark, Norway, Sweden, or Switzerland must use
eur.`redirect[return_url]`The URL the customer should be redirected to after the
authorization process.`amount` A positive integer in the [smallest currency
unit](https://docs.stripe.com/currencies#zero-decimal) representing the amount
to charge the customer (for example, 1099 for a 10.99 USD payment).
To create a source with [Stripe.js](https://docs.stripe.com/payments/elements),
first include the library within your website and set your [publishable API
key](https://dashboard.stripe.com/apikeys). Once included, use the following
`createSource` method to create a source client-side:

```
stripe.createSource({
 type: 'alipay',
 amount: 1099,
 currency: 'usd',
 redirect: {
 return_url: '__TOKEN_PLACEHOLDER_0__',
 },
}).then(function(result) {
 // handle result.error or result.source
});
```

Using either method, Stripe returns a `Source` object containing the relevant
details for the method of payment used. Information specific to Alipay is
provided within the `alipay` subhash.

```
{
 "id": "src_16xhynE8WzK49JbAs9M21jaR",
 "object": "source",
 "amount": 1099,
 "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
 "created": 1445277809,
 "currency": "usd",
 "flow": "redirect",
 "livemode": true,
 "owner": {
```

See all 33 lines
### Error codes

Source creation for Alipay payments may return any of the following errors:

ErrorDescription`payment_method_not_available`The payment method is currently
not available. You should invite your customer to fallback to another payment
method to proceed.`processing_error`An unexpected error occurred preventing us
from creating the source. The source creation should be retried.[Have the
customer complete
authorization](https://docs.stripe.com/sources/alipay#customer-action)
When creating a source, its status is initially set to `pending` and cannot yet
be used to make a charge request. Your customer must authorize an Alipay payment
to make the source chargeable. To allow your customer to authorize the payment,
redirect them to the URL provided within the`redirect[url]` attribute of the
`Source` object.

After the authorization process, your customer is redirected back to the URL
provided as a value of `redirect[return_url]`. This happens regardless of
whether authorization was successful or not. If the customer has authorized the
payment, the `Source` object’s status will transition to `chargeable` when it is
ready to be used in a charge request. If your customer declines the payment, the
status will transition to `failed`.

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

To integrate Alipay within a mobile application, provide your application URI
scheme as the `redirect[return_url]` value. By doing so, your customers are
returned to your app after completing authorization. Direct redirects to the
Alipay app are also supported when using our native SDKs.

For Android sources, the [Alipay
SDK](https://doc.open.alipay.com/doc2/detail.htm?treeId=54&articleId=104509&docType=1)
is required for app-to-app support.

### Testing the redirect process

When creating a `Source` object using your test API keys, you can follow the URL
returned in the `redirect[url]` field. This leads to a Stripe page that displays
information about the API request, and where you can either authorize or cancel
the payment. Authorizing the payment redirects you to the URL specified in
`redirect[return_url]`.

[Charge the Source](https://docs.stripe.com/sources/alipay#charge-request)
Once the customer has authorized the payment, the source’s `status` transitions
to `chargeable` and it can be used to make one charge request. This transition
happens asynchronously and may occur after the customer was redirected back to
your website.

Some customers using Alipay assume that the order process is complete once they
have authorized the payment and received confirmation on Alipay’s site or app.
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
a customer has authorized and verified a payment.`source.failed`A `Source`
object failed to become chargeable as your customer declined to authorize the
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

By default, your account’s [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
appears on customer statements whenever you create an Alipay payment.

### Error codes

Charge creation for Alipay payments may return any of the following errors:

ErrorDescription`insufficient_funds`The Alipay account has insufficient funds to
complete the purchase. The customer should fund their account and try again, or
use an alternative payment method.`invalid_amount`This occurs if the charge
amount is larger than what is supported by Alipay.[Confirm that the charge has
succeeded](https://docs.stripe.com/sources/alipay#charge-confirmation)
Since the customer has already authorized the payment as part of the redirect,
unless there is an unexpected error, the
[Charge](https://docs.stripe.com/api#charge_object) will immediately succeed.

You will also receive the following webhook event as the charge is created:

EventDescription`charge.succeeded`The charge succeeded and the payment is
complete.
We recommend that you rely on the `charge.succeeded` webhook event to notify
your customer that the payment process has been completed and their order is
confirmed. Please refer to our [best
practices](https://docs.stripe.com/sources/best-practices) for more details on
how to best integrate payment methods using webhooks.

## Disputed payments

If a customer’s Alipay account is used illicitly, Alipay and Stripe handle the
issue internally. Alipay payments are disputed only if the customer has a
complaint about the provided goods or service. Should a dispute occur, a
`charge.dispute.created` webhook event is sent to your webhook endpoint, and
Stripe deducts the amount of the dispute from your Stripe balance.

## Refunds

Payments made with Alipay can only be submitted for refund within 90 days from
the date of the original charge. After 90 days, it is no longer possible to
refund the charge.

## Single-use Sources expiration

A single-use Alipay source must be charged within six hours of becoming
`chargeable`, or before 23:45 China Standard Time (GMT+8) due to Chinese
government restrictions around settlement. If it is not, its status is
automatically transitioned to `canceled` and your integration receives a
`source.canceled` webhook event. Once a chargeable source is canceled, the
customer’s authorized Alipay payment is refunded automatically—no money is moved
into your account. For this reason, make sure the order is canceled on your end
and the customer is notified when you receive the `source.canceled` event.

Additionally, `pending` sources are canceled after one hour if they’re not used
to authorize a payment, ensuring that all sources eventually transition out of
their `pending` state to the `canceled` state if they’re not used.

## Settlement currencies

Alipay supports settlement in the default currency of your account. If you have
a bank account in another currency and would like to create Alipay sources in
that currency, please [get in touch](https://support.stripe.com/email). Support
for additional currencies is provided on a case-by-case basis.

## See also

- [Other supported payment methods](https://docs.stripe.com/sources)
- [Sources API reference](https://docs.stripe.com/api#sources)
- [Best practices](https://docs.stripe.com/sources/best-practices)

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [Alipay payments](https://docs.stripe.com/payments/alipay)
- [Sources](https://docs.stripe.com/sources)
- [Alipay](https://alipay.com/)
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
- [Alipay
SDK](https://doc.open.alipay.com/doc2/detail.htm?treeId=54&articleId=104509&docType=1)
- [webhooks](https://docs.stripe.com/webhooks)
- [best practices](https://docs.stripe.com/sources/best-practices)
- [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
- [Charge](https://docs.stripe.com/api#charge_object)
- [get in touch](https://support.stripe.com/email)