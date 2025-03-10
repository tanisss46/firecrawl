# Sources and customersDeprecated

## Learn how to attach and manage sources with Customer objects.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently handle any local payment methods using the Sources
API, you must [migrate them to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

While we don’t plan to remove support for card payments, we recommend replacing
any use of the Sources API with the [PaymentMethods
API](https://docs.stripe.com/api/payment_methods), which provides access to our
latest features and payment method types.

A [Source](https://docs.stripe.com/api#sources) object can be either [single-use
or reusable](https://docs.stripe.com/sources#single-use-or-reusable), as
indicated by its `usage` parameter. While sources can be charged directly,
*reusable* sources should always be attached to a
[Customer](https://docs.stripe.com/api#customers) object for later reuse.
Attaching reusable sources to `Customer` objects allows you to present your
customers with a list of reusable payment methods that they have previously used
with your app or website.

## Reusable sources

Certain payment methods (for example, [SEPA Direct
Debit](https://docs.stripe.com/sources/sepa-debit)) support reusable sources, so
that you can create additional payments without your customer’s needing to
complete the payment process again. A source that you can reuse has its `usage`
parameter set to `reusable`.

You must [attach](https://docs.stripe.com/api#attach_source) a reusable source
to a `Customer` object before making a charge request. If you charge a reusable
source without first attaching it, the source is consumed (its status changes
from `chargeable` to `consumed`). Consumed sources cannot be used for further
payments.

### Attaching a source to a new Customer object

You can create a `Customer` object and attach a source in one API call. This is
useful if this is the first time you’re seeing this customer.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode email="paying.user@example.com" \
 -d source=src_18eYalAHEMiOZZp1l9ZTjSU0
```

The source becomes the `Customer` object’s [default
source](https://docs.stripe.com/api#customer_object-default_source), since this
is the customer’s first and only payment method. The default source is
automatically selected if you make a charge request using the `customer`
parameter without specifying a `source`.

### Attaching a Source to an existing Customer object

When you [update](https://docs.stripe.com/api#update_customer) a `Customer`
object that has a default source, this automatically detaches the existing
source, and adds the provided source as the new default. To add a source without
replacing the existing default, use the
[attach](https://docs.stripe.com/api#attach_source) method, as shown below.

```
curl https://api.stripe.com/v1/customers/cus_AFGbOSiITuJVDs/sources \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "source"="src_18eYalAHEMiOZZp1l9ZTjSU0"
```

Here, because a default source might already exist for the `Customer` object,
the newly attached source does not become the default source. However, you can
change the default source by updating the `Customer` object and specifying the
source as a value for `default_source`.

```
curl https://api.stripe.com/v1/customers/cus_AFGbOSiITuJVDs \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d default_source=src_18eYalAHEMiOZZp1l9ZTjSU0
```

### Charging an attached source

You must specify both the `Customer` object and the source when making a charge
request.

```
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount="1099" \
 -d currency="eur" \
 -d customer=cus_AFGbOSiITuJVDs \
 -d source=src_18eYalAHEMiOZZp1l9ZTjSU0
```

If you attempt to charge a `Customer` object without specifying a source, Stripe
uses the customer’s default source.

### Detaching a source

If you need to remove a source from a particular `Customer` object, you can
[detach the source](https://docs.stripe.com/api#detach_source). Doing so changes
the source’s status to `consumed`, so it cannot be used once detached.

## Single-use sources

Single-use sources must be created each time a customer makes a payment, and
cannot be reused. For that reason, we do not recommend that you permanently
attach them to customers.

If you want to associate a payment with a particular `Customer` object, you can
include a `customer` parameter when making a charge request with a source, even
if the source is not attached.

```
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount="1099" \
 -d currency="eur" \
 -d customer=cus_AFGbOSiITuJVDs \
 -d source=src_18eYalAHEMiOZZp1l9ZTjSU0
```

The resulting `Charge` object references both the `Customer` and `Source`
objects, even if they’re not directly related to one another.

## See also

- [Supported payment methods on Sources](https://docs.stripe.com/sources)
- [Best practices for using
Sources](https://docs.stripe.com/sources/best-practices)
- [Cloning saved payment
methods](https://docs.stripe.com/connect/cloning-customers-across-accounts)
- [Sources API reference](https://docs.stripe.com/api#sources)

## Links

- [migrate them to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [PaymentMethods API](https://docs.stripe.com/api/payment_methods)
- [Source](https://docs.stripe.com/api#sources)
- [single-use or
reusable](https://docs.stripe.com/sources#single-use-or-reusable)
- [Customer](https://docs.stripe.com/api#customers)
- [SEPA Direct Debit](https://docs.stripe.com/sources/sepa-debit)
- [attach](https://docs.stripe.com/api#attach_source)
- [default source](https://docs.stripe.com/api#customer_object-default_source)
- [update](https://docs.stripe.com/api#update_customer)
- [detach the source](https://docs.stripe.com/api#detach_source)
- [Supported payment methods on Sources](https://docs.stripe.com/sources)
- [Best practices for using
Sources](https://docs.stripe.com/sources/best-practices)
- [Cloning saved payment
methods](https://docs.stripe.com/connect/cloning-customers-across-accounts)