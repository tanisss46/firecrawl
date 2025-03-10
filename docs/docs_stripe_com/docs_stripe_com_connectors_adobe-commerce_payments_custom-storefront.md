# Build a custom storefront

## Learn how to build a custom storefront that supports Stripe payment features.

Adobe Commerce can operate as a headless commerce platform that’s decoupled from
its storefront. You can use the REST API or GraphQL API to build custom
storefronts, such as progressive web apps (PWA), mobile apps, or frontends based
on React, Vue, or other frameworks.

The Stripe module extends the REST API and GraphQL API by:

- Setting payment method tokens during order placement
- Performing 3D Secure customer authentication
- Managing customers’ saved payment methods

The Stripe module uses the REST API on the checkout page. You can find examples
of how to use the API in the Stripe module directory under the
`resources/examples/` subdirectory. This guide uses the GraphQL API to build a
custom storefront.

[Retrieve initialization
parameters](https://docs.stripe.com/connectors/adobe-commerce/payments/custom-storefront#retrieve-initialization-parameters)
To initialize Stripe.js and the payment form on the front end, you need the
Stripe [publishable API key](https://docs.stripe.com/keys#obtain-api-keys) that
you configured in the admin area. You can retrieve the key and other
initialization parameters using the following GraphQL mutation:

```
query {
getStripeConfiguration {
	apiKey
		locale
		appInfo
		options {
			betas
			apiVersion
		}
	elementsOptions
	}
}

```

[Tokenize a payment method during the checkout
flow](https://docs.stripe.com/connectors/adobe-commerce/payments/custom-storefront#tokenize-payment-method)
You can use the
[PaymentElement](https://docs.stripe.com/payments/payment-element) to collect a
payment method from the customer during checkout. After the customer provides
their payment method details and clicks **Place Order**, you can tokenize the
payment method and use it to place the order. Calling `createPaymentMethod`
[generates a payment method
token](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy?type=payment#create-pm)
from the details provided in the `PaymentElement`.

```
var stripe = Stripe(API_PUBLISHABLE_KEY);

var options = {
 mode: 'payment',
 amount: 1099,
 currency: 'eur'
};

var elements = stripe.elements(options);
var paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');

var placeOrder = function()
{
 elements.submit().then(function()
 {
 stripe.createPaymentMethod({
 elements: elements,
 params: {
 billing_details: {
 name: 'Jenny Rosen'
 }
 }
 }).then(function(result)
 {
 if (result && result.paymentMethod)
 {
 // Success
 }
 });
 });
}

```

[Pass the tokenized payment
method](https://docs.stripe.com/connectors/adobe-commerce/payments/custom-storefront#pass-tokenized-payment-method)
After you obtain a payment method token, you must call `setPaymentMethodOnCart`
to [set the payment
method](https://developer.adobe.com/commerce/webapi/graphql/tutorials/checkout/set-payment-method/#set-payment-method-on-cart)
on the order.

```
mutation {
 setPaymentMethodOnCart(input: {
 cart_id: "CART_ID"
 payment_method: {
 code: "stripe_payments"
 stripe_payments: {
 payment_method: "PAYMENT_METHOD_ID"
 save_payment_method: true
 }
 }
 }) {
 cart {
 selected_payment_method {
 code
 }
 }
 }
}

```

Use the following parameters for `setPaymentMethodOnCart`:

ParameterTypeDescription`payment_method`StringUse this parameter to pass the
tokenized payment method ID. You can also pass saved payment method tokens when
a customer chooses a saved payment method during
checkout.`save_payment_method`BooleanSpecify whether or not to save the payment
method.`cvc_token`StringIf CVC is enabled for saved cards, use this parameter to
pass the CVC token and perform verification.[Place the
order](https://docs.stripe.com/connectors/adobe-commerce/payments/custom-storefront#place-order)
After you set the payment method token, you can use the Adobe Commerce
`placeOrder` mutation to place an order:

```
mutation {
 placeOrder(input: {cart_id: "CART_ID"}) {
 order {
 order_number
 client_secret
 }
 }
}

```

The example above requests a `client_secret`, which isn’t a default `placeOrder`
mutation parameter. The Stripe module adds this parameter for you to use after
the order is placed to finalize details specific to the selected payment method.
You can finalize payment with the `stripe.handleNextAction(client_secret)`
method. Options include performing an inline 3D Secure authentication for cards,
displaying a printable voucher for certain payment methods, or redirecting the
customer externally for authentication.

## Order placement flow

Payment methods of type `card` or `link` that require 3D Secure (3DS) customer
authentication go through the following process:

- The order is placed in `Pending Payment` status.
- The client secret is passed to the front end to perform the authentication.
- After successful authentication, payment is collected client-side, and the
customer is redirected to the order success page.
- A `charge.succeeded` webhook event arrives at your website on the server side.
- The module handles the event and changes the order status from `Payment
Pending` to `processing`.

That procedure is the default for GraphQL, but not for the REST API. With the
REST API, if customer authentication is required, the order placement fails with
an `Authentication Required: client_secret` error. You must authenticate the
payment using the `client_secret`, and the order placement must be attempted
again following successful authentication. This approach’s advantage is that
inventory isn’t held until the payment is successful. To employ this procedure
with GraphQL, edit the module’s `etc/config.xml` file by adding `card` and
`link` under the `<graphql_api>` node:

```
<manual_authentication>
 <rest_api>card,link</rest_api>
 <graphql_api>card,link</graphql_api>
</manual_authentication>

```

## Retrieve saved payment methods

You can use `listStripePaymentMethods` to retrieve a list of saved payment
methods for a customer in an active checkout session.

```
mutation {
 listStripePaymentMethods {
 id
 created
 type
 fingerprint
 label
 icon
 cvc
 brand
 exp_month
 exp_year
 }
}

```

## Save a payment method

You can use `addStripePaymentMethod` to save payment methods to a customer’s
account. The `payment_method` parameter is the tokenized payment method ID. The
tokenization process is similar to the tokenization process during the checkout
flow.

```
mutation {
 addStripePaymentMethod(
 input: {
 payment_method: "PAYMENT_METHOD_ID"
 }
 ) {
 id
 created
 type
 fingerprint
 label
 icon
 cvc
 brand
 exp_month
 exp_year
 }
}

```

## Delete a saved payment method

You can use `deleteStripePaymentMethod` to allow customers to delete saved
payment methods from their account.

For most use cases, we recommend passing a payment method fingerprint, which
deletes all payment methods that match the fingerprint. The
`listStripePaymentMethods` mutation automatically removes duplicates before
returning recently added payment methods that match a specific fingerprint. But
if you only delete a payment method by ID, the results of
`listStripePaymentMethods` might include an older saved payment method with the
same fingerprint.

```
mutation {
 deleteStripePaymentMethod(
 input: {
 payment_method: "paste a payment method ID here"
 fingerprint: null
 }
 )
}

```

## See also

- [SetupIntents API](https://docs.stripe.com/payments/setup-intents)
- [Use the Adobe Commerce admin
panel](https://docs.stripe.com/connectors/adobe-commerce/payments/admin)
-
[Troubleshooting](https://docs.stripe.com/connectors/adobe-commerce/payments/troubleshooting)

## Links

- [publishable API key](https://docs.stripe.com/keys#obtain-api-keys)
- [PaymentElement](https://docs.stripe.com/payments/payment-element)
- [generates a payment method
token](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy?type=payment#create-pm)
- [set the payment
method](https://developer.adobe.com/commerce/webapi/graphql/tutorials/checkout/set-payment-method/#set-payment-method-on-cart)
- [SetupIntents API](https://docs.stripe.com/payments/setup-intents)
- [Use the Adobe Commerce admin
panel](https://docs.stripe.com/connectors/adobe-commerce/payments/admin)
-
[Troubleshooting](https://docs.stripe.com/connectors/adobe-commerce/payments/troubleshooting)