# Connect platforms using the Sources APIDeprecated

## Considerations for Stripe Connect platforms adding support for new payment methods using the Sources API.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently handle any local payment methods using the Sources
API, you must [migrate them to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

While we don’t plan to remove support for card payments, we recommend replacing
any use of the Sources API with the [PaymentMethods
API](https://docs.stripe.com/api/payment_methods), which provides access to our
latest features and payment method types.

[Connect](https://docs.stripe.com/connect) platform owners can make use of
additional payment methods supported with Sources. To learn more about creating
payments for connected users, and which approach is best for you, refer to our
Connect [payments and fees
documentation](https://docs.stripe.com/connect/charges).

## Creating destination charges

If you opt for [destination
charges](https://docs.stripe.com/connect/destination-charges), you should create
Sources on your platform directly and create Charges using the appropriate
destination parameter. [Customers](https://docs.stripe.com/api/customers) are
charged by your platform, which then transfers the necessary amount to the
destination account.

With destination charges that use cards, your platform name appears on statement
descriptors and the charge is attributed to the connected account. With
destination charges that use alternative payment methods (APMs), your platform
name appears on statement descriptors but the charge is attributed to your
platform.

## Creating direct charges

If you opt for direct charges, you will need to make sure that the connected
account is onboarded on the payment method you intend to use (see below). Direct
charges require creating sources on connected accounts. You can do so by passing
`source.stripeAccount` with a value of a connected account’s ID when using
Stripe.js.

```
// Set the connected Stripe Account on which the source should be created
var stripe = Stripe(
 'pk_test_TYooMQauvdEDq54NiTphI7jx',
 {stripeAccount: "{{CONNECTED_STRIPE_ACCOUNT_ID}}"},
);

stripe.createSource({
 type: 'ideal',
 amount: 1099,
 currency: 'eur',
 owner: {
 name: 'Jenny Rosen',
 },
 redirect: {
 return_url: 'https://shop.example.com/crtA6B28E1',
 },
}).then(function(result) {
 // handle result.error or result.source
});
```

If you’re creating sources server-side, you can make use of [authentication
using the Stripe-Account
header](https://docs.stripe.com/connect/authentication#stripe-account-header)
with any of our supported libraries.

### Cloning card Sources

Card Sources (because they’re not intrinsically tied to your platform as they do
not require any authentication
[flow](https://docs.stripe.com/sources#flow-for-customer-action)) can be created
on your platform and then cloned to a connected account to create direct charges
there.

Once you created a card Source and attached it to a Customer (see [Sources and
Customers](https://docs.stripe.com/sources/customers) for more details on how
these two objects interact), you can clone that card Source on a connected
account using the connected account’s ID as the `Stripe-Account` header:

```
curl https://api.stripe.com/v1/sources \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer"="cus_AFGbOSiITuJVDs" \
 -d "original_source"="src_19YP2AAHEMiOZZp1Di4rt1K6" \
 -d "usage"="reusable" \
 -H "Stripe-Account: {{CONNECTED_STRIPE_ACCOUNT_ID}}"
```

Card Sources are generally `reusable`. However, when cloning them, you can
override the usage to constrain how the connected account uses them. You do so
by specifying the `usage` as `single_use` when cloning the Source.

If you are creating reusable card Sources on your connected account, you should
make sure to attach them to Customers before charging them. Please refer to
[Sources and Customers](https://docs.stripe.com/sources/customers) for more
details on how to attach and manage Sources on Customers.

## See also

- [Supported Payment Methods](https://docs.stripe.com/sources)
- [Sources API reference](https://docs.stripe.com/api#sources)
- [Best Practices Using Sources](https://docs.stripe.com/sources/best-practices)

## Links

- [migrate them to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [PaymentMethods API](https://docs.stripe.com/api/payment_methods)
- [Connect](https://docs.stripe.com/connect)
- [payments and fees documentation](https://docs.stripe.com/connect/charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [Customers](https://docs.stripe.com/api/customers)
- [authentication using the Stripe-Account
header](https://docs.stripe.com/connect/authentication#stripe-account-header)
- [flow](https://docs.stripe.com/sources#flow-for-customer-action)
- [Sources and Customers](https://docs.stripe.com/sources/customers)
- [Supported Payment Methods](https://docs.stripe.com/sources)
- [Sources API reference](https://docs.stripe.com/api#sources)
- [Best Practices Using Sources](https://docs.stripe.com/sources/best-practices)