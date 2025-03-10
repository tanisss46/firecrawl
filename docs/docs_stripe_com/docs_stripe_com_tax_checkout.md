# Automatically collect tax on Checkout sessions

## Learn how to automatically calculate taxes in Checkout.

Stripe Tax automatically calculates the taxes on all purchases and
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
accumulated during a Checkout session. If you haven’t integrated with Checkout,
you must complete the integration using the [Accept a Payment
guide](https://docs.stripe.com/checkout/quickstart).

## Get started with a video demo

This short video shows to how to enable automatic tax collection when using
hosted integrations like Stripe Checkout.

[Activate Stripe Tax](https://docs.stripe.com/tax/checkout#activate)
[Log in](https://dashboard.stripe.com/settings/tax) or [sign
up](https://dashboard.stripe.com/register) for Stripe to activate Stripe Tax.

[Update your products and prices
(optional)](https://docs.stripe.com/tax/checkout#product-and-price-setup)
Stripe Tax uses information stored on
[products](https://docs.stripe.com/api/products) and
[prices](https://docs.stripe.com/api/prices) to calculate tax, such as [tax
code](https://docs.stripe.com/api/products/object#product_object-tax_code) and
[tax
behavior](https://docs.stripe.com/api/prices/object#price_object-tax_behavior).
If you don’t explicitly specify these configurations, Stripe Tax will use the
default tax code selected in [Tax
Settings](https://dashboard.stripe.com/settings/tax).

For more information, see [Specify product tax codes and tax
behaviour](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior).

[Create a Checkout Session](https://docs.stripe.com/tax/checkout#create-session)
After updating your products and prices, you’re ready to start calculating tax
on your Checkout sessions. You can create sessions for one time and recurring
purchases.

A customer’s tax rates come from their location, which Checkout assesses from
the customer’s address. The address that Checkout uses to calculate taxes
depends on whether the customer is new or existing, and whether you collect
shipping addresses during the Checkout Session:

New CustomerExisting CustomerCollect a billing address onlyCheckout calculates
taxes based on the customer’s billing address entered into the Checkout
SessionIf the customer has a previously saved shipping address, Checkout
calculates taxes based on that address. Otherwise, you can calculate taxes based
on billing address entered during Checkout (by specifying
[customer_update[address]=auto](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_update-address))
or the billing address saved to the customer (the default behavior).Collect a
shipping addressCheckout calculates taxes based on the customer’s shipping
address entered into the Checkout SessionCheckout calculates taxes based on the
customer’s shipping address entered into the Checkout Session. Existing
addresses on the customer won’t apply in this case.
#### Note

If you wish to ensure that Google Pay is offered as a payment method while using
Stripe Tax in Checkout, you must require collecting a shipping address. Apple
Pay with Stripe Tax displays only when the customer’s browser supports Apple Pay
version 12.

[Calculating tax for new
customers](https://docs.stripe.com/tax/checkout#new-customers)
If you don’t pass in an existing customer when creating a Checkout session,
Checkout creates a new customer and automatically saves billing address and
shipping information. For tax collection purposes, Checkout uses billing and
shipping addresses to determine the customer’s location.

Checkout uses the shipping address entered during the session to determine the
customer’s location for calculating tax. If you don’t collect shipping
information, Checkout uses the billing address.

Stripe-hosted pageEmbedded form
```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=2 \
 -d "automatic_tax[enabled]"=true \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

## Calculate tax for existing customers

To calculate tax on Checkout sessions created for existing customers, you can
set the `automatic_tax[enabled]` parameter to `true` when creating the session.
You can either base tax calculations on the customer’s existing addresses or new
addresses collected during the session:

### Use the existing addresses on the customer for taxes

If you’ve already collected the addresses of existing customers, you can base
tax calculations on those addresses rather than the addresses collected during
checkout:

- **The customer address that Checkout uses for taxes**: If available, Checkout
uses the customer’s saved [shipping
address](https://docs.stripe.com/api/customers/object#customer_object-shipping-address)
to calculate taxes. Otherwise, Checkout uses the customer’s saved [billing
address](https://docs.stripe.com/api/customers/object#customer_object-address)
to calculate taxes.
- **Customer address requirements**: When using existing addresses for taxes,
the customer must either have a valid [shipping
address](https://docs.stripe.com/api/customers/object#customer_object-shipping-address)
or [billing
address](https://docs.stripe.com/api/customers/object#customer_object-address)
saved. You can see whether or not a customer’s saved addresses are valid by
checking the customer’s
[customer.tax.automatic_tax](https://docs.stripe.com/api/customers/object#customer_object-tax-automatic_tax)
property. If the property is `supported` or `not_collecting`, it means the
customer’s saved addresses are valid, and you can enable Stripe Tax on Checkout
sessions for that customer.
Stripe-hosted pageEmbedded form
```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=2 \
 -d "automatic_tax[enabled]"=true \
 -d customer={{CUSTOMER_ID}} \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

### Use the addresses collected during Checkout for taxes

You can configure Checkout to save new billing or shipping addresses to a
customer. In this case, Checkout calculates tax using the address entered during
checkout.

- **The address that Checkout uses for taxes**: If you [collect shipping
addresses](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_address_collection),
Checkout uses the shipping address entered during the session to calculate
taxes. Otherwise, Checkout uses the billing address entered during the session
to calculate taxes.
- **Where Checkout saves the addresses collected during checkout**: If you
[collect shipping
addresses](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_address_collection),
Checkout saves the shipping address entered during the session to the customer’s
[customer.shipping.address](https://docs.stripe.com/api/customers/object#customer_object-shipping-address)
property. Otherwise, Checkout saves the billing address entered during the
session to the customer’s
[customer.address](https://docs.stripe.com/api/customers/object#customer_object-address)
property. In both cases, the address used for taxes overrides any existing
addresses.

If you collect shipping addresses with Checkout, set the
`customer_update[shipping]` property to `auto` so that you copy the shipping
information from Checkout to the customer.

Stripe-hosted pageEmbedded form
```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=2 \
 -d "automatic_tax[enabled]"=true \
 -d customer={{CUSTOMER_ID}} \
 -d "customer_update[shipping]"=auto \
 -d "shipping_address_collection[allowed_countries][0]"=US \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

If you don’t collect shipping addresses with Checkout, and you want to use
billing addresses entered during checkout for taxes, you must save the billing
address to the customer. Set the `customer_update[address]` property to `auto`
so that you copy the newly-entered address onto the provided customer.

Stripe-hosted pageEmbedded form
```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=2 \
 -d "automatic_tax[enabled]"=true \
 -d customer={{CUSTOMER_ID}} \
 -d "customer_update[address]"=auto \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

## Check the response

To inspect the results of the latest tax calculation, you can read the tax
amount calculated by Checkout from the
[total_details.amount_tax](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-total_details)
on the Checkout Session resource. Additionally, the tax outcome for each payment
is available when [viewing a
payment](https://dashboard.stripe.com/test/payments) in the Dashboard.

## See also

- [Determining customer
locations](https://docs.stripe.com/tax/customer-locations)
- [Checkout and tax IDs](https://docs.stripe.com/tax/checkout/tax-ids)
- [Reporting and filing](https://docs.stripe.com/tax/reports)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)
- [Calculate tax in your custom checkout
flow](https://docs.stripe.com/tax/custom)

## Links

- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Accept a Payment guide](https://docs.stripe.com/checkout/quickstart)
- [Log in](https://dashboard.stripe.com/settings/tax)
- [sign up](https://dashboard.stripe.com/register)
- [products](https://docs.stripe.com/api/products)
- [prices](https://docs.stripe.com/api/prices)
- [tax
code](https://docs.stripe.com/api/products/object#product_object-tax_code)
- [tax
behavior](https://docs.stripe.com/api/prices/object#price_object-tax_behavior)
- [Specify product tax codes and tax
behaviour](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
-
[customer_update[address]=auto](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer_update-address)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [shipping
address](https://docs.stripe.com/api/customers/object#customer_object-shipping-address)
- [billing
address](https://docs.stripe.com/api/customers/object#customer_object-address)
-
[customer.tax.automatic_tax](https://docs.stripe.com/api/customers/object#customer_object-tax-automatic_tax)
- [collect shipping
addresses](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-shipping_address_collection)
-
[total_details.amount_tax](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-total_details)
- [viewing a payment](https://dashboard.stripe.com/test/payments)
- [Determining customer
locations](https://docs.stripe.com/tax/customer-locations)
- [Checkout and tax IDs](https://docs.stripe.com/tax/checkout/tax-ids)
- [Reporting and filing](https://docs.stripe.com/tax/reports)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)
- [Calculate tax in your custom checkout
flow](https://docs.stripe.com/tax/custom)