# About the Billing APIs

## Understand how the Billing API objects work together.

[Subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
automatically create [Invoices](https://docs.stripe.com/api/invoices) and
[Payment Intents](https://docs.stripe.com/payments/payment-intents) for you.
They have the following parts:

- A [Product](https://docs.stripe.com/api/products) to model what is being sold.
- A [Price](https://docs.stripe.com/api/prices) to determine the interval and
amount to charge.
- A [Customer](https://docs.stripe.com/api/customers) to store the [Payment
Methods](https://docs.stripe.com/api/payment_methods) used to make each
recurring payment.
hide sample
argumentsid`sub_1234`status`active`latest_invoice`in_1234`default_payment_method`pm_1234`customer`cus_1234`items.data.price`price_1234`hide
sample argumentsid`in_1234`currency`usd`status`open`hide sample
argumentsid`pm_1234`type`card`card[brand]`visa`hide sample
argumentsid`cus_1234`name`Jenny Rosen`email`jennyrosen@example.com`hide sample
argumentsid`price_1234`product`prod_1234`type`recurring`hide sample
argumentsid`prod_1234`activetruename`Widget, blue`default_price`price_1234`hide
sample
argumentsid`pi_1234`amount1000customer`cus_1234`invoice`in_1234`status`processing`A
diagram illustrating common billing objects and their relationships
## API object definitions

Resource Definition[Customer](https://docs.stripe.com/api/customers)Represents a
customer who purchases a subscription. Use the Customer object associated with a
subscription to make and track recurring charges and to manage the products that
they subscribe
to.[Entitlement](https://docs.stripe.com/api/entitlements/active-entitlement)Represents
a customer’s access to a feature included in a service product that they
subscribe to. When you create a subscription for a customer’s recurring purchase
of a product, an active entitlement is automatically created for each feature
associated with that product. When a customer accesses your services, use their
active entitlements to enable the features included in their
subscription.[Feature](https://docs.stripe.com/api/entitlements/feature)Represents
a function or ability that your customers can access when they subscribe to a
service product. You can include features in a product by creating
ProductFeatures.[Invoice](https://docs.stripe.com/api/invoices)A statement of
amounts a customer owes that tracks payment statuses from draft through paid or
otherwise finalized. Subscriptions automatically generate
invoices.[PaymentIntent](https://docs.stripe.com/api/payment_intents)A way to
build dynamic payment flows. A PaymentIntent tracks the lifecycle of a customer
checkout flow and triggers additional authentication steps when required by
regulatory mandates, custom Radar fraud rules, or redirect-based payment
methods. Invoices automatically create
PaymentIntents.[PaymentMethod](https://docs.stripe.com/api/payment_methods)A
customer’s payment instruments that they use to pay for your products. For
example, you can store a credit card on a Customer object and use it to make
recurring payments for that customer. Typically used with the Payment Intents or
Setup Intents APIs.[Price](https://docs.stripe.com/api/prices)Defines the unit
price, currency, and billing cycle for a
product.[Product](https://docs.stripe.com/api/products)A good or service that
your business sells. A service product can include one or more
features.[ProductFeature](https://docs.stripe.com/api/product-feature)Represents
a single feature’s inclusion in a single product. Each product is associated
with a ProductFeature for each feature that it includes, and each feature is
associated with a ProductFeature for each product that includes
it.[Subscription](https://docs.stripe.com/api/subscriptions)Represents a
customer’s scheduled recurring purchase of a product. Use a subscription to
collect payments and provide repeated delivery of or continuous access to a
product.
Here’s an example of how products, features, and entitlements work together.
Imagine that you want to set up a subscription service that offers two tiers: a
standard product with basic functionality, and an advanced product that adds
extended functionality.

- You create two features: `basic_features` and `extended_features`.
- You create two products: `standard_product` and `advanced_product`.
- For the standard product, you create one ProductFeature that associates
`basic_features` with `standard_product`.
- For the advanced product, you create two ProductFeatures: one that associates
`basic_features` with `advanced_product` and one that associates
`extended_features` with `advanced_product`.

A customer, `first_customer`, subscribes to the standard product. When you
create the subscription, Stripe automatically creates an Entitlement that
associates `first_customer` with `basic_features`.

Another customer, `second_customer`, subscribes to the advanced product. When
you create the Subscription, Stripe automatically creates two Entitlements: one
that associates `second_customer` with `basic_features`, and one that associates
`second_customer` with `extended_features`.

You can determine which features to provision for a customer by [retrieving
their active entitlements or listening to the Active Entitlement Summary
event](https://docs.stripe.com/billing/entitlements#entitlements). You don’t
have to retrieve their subscriptions, products, and features.

## Links

- [Subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Invoices](https://docs.stripe.com/api/invoices)
- [Payment Intents](https://docs.stripe.com/payments/payment-intents)
- [Product](https://docs.stripe.com/api/products)
- [Price](https://docs.stripe.com/api/prices)
- [Customer](https://docs.stripe.com/api/customers)
- [Payment Methods](https://docs.stripe.com/api/payment_methods)
- [Subscription object](https://docs.stripe.com/api/subscriptions/object)
- [Invoice object](https://docs.stripe.com/api/invoices/object)
- [PaymentMethod object](https://docs.stripe.com/api/payment_methods/object)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [Entitlement](https://docs.stripe.com/api/entitlements/active-entitlement)
- [Feature](https://docs.stripe.com/api/entitlements/feature)
- [ProductFeature](https://docs.stripe.com/api/product-feature)
- [Subscription](https://docs.stripe.com/api/subscriptions)
- [retrieving their active entitlements or listening to the Active Entitlement
Summary event](https://docs.stripe.com/billing/entitlements#entitlements)