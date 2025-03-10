# WeChat Pay payments with SourcesDeprecated

## Use Sources to accept payments using WeChat Pay, a popular payment method in China.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently integrate with WeChat Pay using the Sources API, you
must [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

For information about integrating WeChat Pay with the current APIs, see [WeChat
Pay payments](https://docs.stripe.com/payments/wechat-pay).

Stripe users can use [Sources](https://docs.stripe.com/sources)—a single
integration path for creating payments using any supported method—to accept
[WeChat Pay](https://pay.weixin.qq.com/index.php/public/wechatpay) payments from
customers from China.

During the payment process, a [Source](https://docs.stripe.com/api#sources)
object is created and you receive a WeChat Pay URL that is used to authorize the
payment in the WeChat app by scanning a QR code. After completing this, your
integration uses the source to make a charge request and complete the payment.

WeChat Pay is a
[push](https://docs.stripe.com/sources#pull-or-push-of-funds)-based,
[single-use](https://docs.stripe.com/sources#single-use-or-reusable) and
[synchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
method of payment. This means that once your customer takes action to authorize
the charge there is immediate confirmation about the success or failure of a
payment.

[Create a Source
object](https://docs.stripe.com/sources/wechat-pay#create-source)
A `Source` object is either created client-side using
[Stripe.js](https://docs.stripe.com/payments/elements) or server-side using the
[Source creation endpoint](https://docs.stripe.com/api#create_source), with the
following parameters:

ParameterValue`type`wechat`amount`A positive integer in the [smallest currency
unit](https://docs.stripe.com/currencies#zero-decimal) representing the amount
to charge the customer (for example, 1099 for a 10.99 USD payment).`currency`The
currency of the payment. Must be the default currency for your country. Can be
aud, cad, eur, gbp, hkd, jpy, sgd, or usd.`statement_descriptor` (optional)A
custom statement descriptor for the payment.
To create a source with [Stripe.js](https://docs.stripe.com/payments/elements),
first include the library within your website and set your [publishable API
key](https://dashboard.stripe.com/apikeys). Once included, use the following
`createSource` method to create a source client-side:

```
stripe.createSource({
 type: 'wechat',
 amount: 1099,
 currency: 'usd',
}).then(function(result) {
 // handle result.error or result.source
});
```

Using either method, Stripe returns a `Source` object containing the relevant
details for the method of payment used. Information specific to WeChat is
provided within the `wechat` subhash.

```
{
 "id": "src_18eYalAHEMiOZZp1l9ZTjSU0",
 "object": "source",
 "amount": 1099,
 "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
 "created": 1445277809,
 "currency": "usd",
 "flow": "none",
 "livemode": true,
 "metadata": {},
```

See all 27 lines
### Optional: Provide a custom statement descriptor

WeChat Pay can accept a [statement
descriptor](https://support.stripe.com/questions/when-i-charge-a-customer-what-will-they-see-on-their-card-statements)
before the customer is redirected to authorize the payment. By default, your
Stripe account’s statement descriptor is used (you can review this in the
[Dashboard](https://dashboard.stripe.com/settings/public)). You can provide a
custom descriptor by specifying `statement_descriptor` when creating a source.
WeChat statement descriptors support a maximum of 32 characters.

```
stripe.createSource({
 type: 'wechat',
 amount: 1099,
 currency: 'usd',
 statement_descriptor: 'ORDER AT11990',
 owner: {
 name: 'Jenny Rosen',
 },
}).then(function(result) {
 // handle result.error or result.source
});
```

Providing a custom statement descriptor within a subsequent charge request has
no effect.

### Error codes

Source creation for WeChat Pay payments may return any of the following errors:

ErrorDescription`payment_method_not_available`The payment method is currently
not available. You should invite your customer to fallback to another payment
method to proceed.`processing_error`An unexpected error occurred preventing us
from creating the source. The source creation should be retried.[Have the
customer authorize the
payment](https://docs.stripe.com/sources/wechat-pay#customer-action)
When creating a source, its status is initially set to `pending` and cannot yet
be used to make a charge request. Your customer must authorize a WeChat Pay
payment to make the source chargeable.

To do so, you will need to show the customer a QR code created from the URL
provided within `wechat[qr_code_url]`.

After the authorization process, if the customer has authorized the payment, the
`Source` object’s status will transition to `chargeable`; it is then ready to be
used in a charge request. If your customer declines the payment, the status will
transition to `failed`.

To receive notifications of status changes on `Source` objects, your integration
must use [webhooks](https://docs.stripe.com/webhooks).

### Testing

For sources created while testing, the `wechat[qr_code_url]` can be scanned
using any QR Code scanning application rather than WeChat. The URL leads to a
Stripe page that displays information about the API request, and where you can
either authorize or cancel the payment.

[Charge the Source](https://docs.stripe.com/sources/wechat-pay#charge-request)
Once the customer has authorized the payment, the source’s `status` transitions
to `chargeable` and it can be used to make a charge request. This transition
happens asynchronously.

Some customers using WeChat Pay will assume that the order process is complete
once they have authorized the payment and received confirmation on WeChat Pay’s
app. It is essential that your integration rely on
[webhooks](https://docs.stripe.com/webhooks) to determine when the source
becomes chargeable in order to create a charge. See our [best
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
 -d currency="usd" \
 -d source=src_18eYalAHEMiOZZp1l9ZTjSU0
```

WeChat Pay Sources are
[single-use](https://docs.stripe.com/sources#single-use-or-reusable) and cannot
be used for recurring or additional payments. Learn more about using [Sources
with Customer objects](https://docs.stripe.com/sources/customers).

[Confirm that the charge has
succeeded](https://docs.stripe.com/sources/wechat-pay#charge-confirmation)
Since WeChat Pay is a
[synchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
payment method and the customer has already authorized the payment using the
WeChat application, the [Charge](https://docs.stripe.com/api#charge_object) will
immediately succeed unless there’s an unexpected error.

You receive the following webhook event when the charge succeeds:

EventDescription`charge.succeeded`The charge succeeded and the payment is
complete.
Stripe recommends that you rely on the `charge.succeeded` webhook event to
notify your customer that the payment process has been completed and their order
is confirmed. See [best
practices](https://docs.stripe.com/sources/best-practices) for more details on
integrating payment methods using webhooks.

### Disputed payments

If a customer’s WeChat Pay account is used illicitly, WeChat Pay and Stripe
handle the issue internally. In the context of WeChat Pay, payments are only
disputed if the customer has a complaint about the provided goods or service.
Should a dispute occur, a `charge.dispute.created` webhook event is sent, and
Stripe deducts the amount of the dispute from your Stripe balance.

### Refunds

Payments made with WeChat Pay can only be submitted for refund within 180 days
from the date of the original charge. After 180 days, it is no longer possible
to refund the charge.

### Sources expiration

A WeChat Pay source must be charged within six hours of becoming `chargeable`,
or before 23:45 China Standard Time (GMT+8) due to Chinese government
restrictions around settlement. If it is not, its status is automatically
transitioned to `canceled` and your integration receives a `source.canceled`
webhook event. Once a chargeable source is canceled, the customer’s authorized
WeChat Pay payment is refunded automatically—no money is moved into your
account. For this reason, make sure the order is canceled on your end and the
customer is notified when you receive the `source.canceled` event.

Additionally, `pending` sources are canceled after 1 hour if they aren’t used to
authorize a payment to make sure that all sources transition out of their
`pending` state to the `canceled` state if they aren’t used.

## See also

- [Other supported payment methods](https://docs.stripe.com/sources)
- [Sources API reference](https://docs.stripe.com/api#sources)
- [Best practices](https://docs.stripe.com/sources/best-practices)

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [WeChat Pay payments](https://docs.stripe.com/payments/wechat-pay)
- [Sources](https://docs.stripe.com/sources)
- [WeChat Pay](https://pay.weixin.qq.com/index.php/public/wechatpay)
- [Source](https://docs.stripe.com/api#sources)
- [push](https://docs.stripe.com/sources#pull-or-push-of-funds)
- [single-use](https://docs.stripe.com/sources#single-use-or-reusable)
-
[synchronous](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
- [Stripe.js](https://docs.stripe.com/payments/elements)
- [Source creation endpoint](https://docs.stripe.com/api#create_source)
- [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal)
- [publishable API key](https://dashboard.stripe.com/apikeys)
- [statement
descriptor](https://support.stripe.com/questions/when-i-charge-a-customer-what-will-they-see-on-their-card-statements)
- [Dashboard](https://dashboard.stripe.com/settings/public)
- [webhooks](https://docs.stripe.com/webhooks)
- [best practices](https://docs.stripe.com/sources/best-practices)
- [Sources with Customer objects](https://docs.stripe.com/sources/customers)
- [Charge](https://docs.stripe.com/api#charge_object)