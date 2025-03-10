# How subscriptions work

## Manage recurring payments and subscription lifecycles.

With Subscriptions, customers make recurring payments for access to a product.
Subscriptions require you to retain more information about your customers than
one-time purchases because you need to charge them in the future.

## Subscription objects

Use the following core API resources to build and manage subscriptions:

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

![How Stripe objects work in a subscription
lifecycle.](https://b.stripecdn.com/docs-statics-srv/assets/abstractions.c0365799e62eac96eed3e9e746e3b65b.svg)

## Integration example

This section describes our [sample
integration](https://github.com/stripe-samples/subscription-use-cases/tree/master/fixed-price-subscriptions)
on GitHub, which illustrates how to build a subscriptions integration. If you’re
ready to build your own integration, see the [Billing
quickstart](https://docs.stripe.com/billing/quickstart) or [integration
guide](https://docs.stripe.com/billing/subscriptions/build-subscriptions).

### Landing page

On your frontend, the landing page collects the email address first. Your
application might have other customer-specific information you want to collect
like a username or address. Clicking the signup button sends the information
collected on the landing page to your backend. This process creates a customer
and displays the pricing page on your frontend.

### Pricing page

The pricing page displays your subscription options based on the products and
prices you create when you first set up your integration, meaning you don’t need
to create new ones every time customers sign up. Your pricing page displays the
prices you created, and your customers choose the option they want. The [example
on
GitHub](https://github.com/stripe-samples/subscription-use-cases/tree/master/fixed-price-subscriptions)
displays a payment form when a customer selects an option. Learn more about
[products and
prices](https://docs.stripe.com/products-prices/how-products-and-prices-work).

### Payment

The payment form collects a name and card information. Stripe hosts this form if
you use Checkout. It’s one of the key features that allows you to collect
payments and remain PCI compliant. Clicking **Subscribe**:

- Creates a new subscription with your customer and price IDs.
- Generates an invoice for your initial subscription cycle.
- Collects payment details and pays your invoice.
- Sets the payment method as the default payment method for the subscription-a
requirement for subsequent payments.

Make sure to [confirm](https://docs.stripe.com/api/payment_intents/confirm)
payment before [provisioning
access](https://docs.stripe.com/billing/subscriptions/overview#provisioning) for
your customer.

To implement this:

- **Accept payments without code**: If you don’t want to write any code, learn
how to [create a Payment
Link](https://docs.stripe.com/payment-links/create?pricing-model=standard) and
share it with your customers.
- **Build a checkout page**: Use the [Checkout Sessions
API](https://docs.stripe.com/api/checkout/sessions) to accept payments through
[a hosted page](https://docs.stripe.com/checkout/quickstart), [an embedded form
on your site](https://docs.stripe.com/checkout/embedded/quickstart), or [a
customized checkout page built with embedded
components](https://docs.stripe.com/checkout/custom/quickstart).
- **Advanced integration**: Use [Stripe
Elements](https://docs.stripe.com/payments/elements) to [collect payment details
and activate the
subscription](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements#collect-payment)
with the [Payment Element](https://docs.stripe.com/payments/payment-element).

### Provisioning

Use [Entitlements](https://docs.stripe.com/billing/entitlements) to determine
when you can grant or revoke product feature access to your customers.
Alternatively, after a successful payment, you can safely provision the product
for the customer. This generally means:

- Verifying the status of the subscription is `active`.
- Granting the customer access to the products and features they subscribed to.

Learn how to use [event
destinations](https://docs.stripe.com/event-destinations) to:

- [Track active
subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks#active-subscriptions)
- [Handle payment
failures](https://docs.stripe.com/billing/subscriptions/webhooks#payment-failures)
- [Check event
objects](https://docs.stripe.com/event-destinations#events-overview)

## How payments work with subscriptions

To simplify the handling of failed payments and to create subscriptions before
attempting payment:

- Pass
[payment_behavior=default_incomplete](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)
when creating a subscription. If your subscription requires payment, it’s
created with an `incomplete` status, otherwise your subscription immediately
becomes `active`.
- Activate an incomplete subscription by paying the first invoice.
- Pass the payment intent identifier from the invoice to your user interface to
collect payment information and confirm the payment intent. You can use
[Elements](https://docs.stripe.com/js/elements_object), the [Android
SDK](https://stripe.dev/stripe-android/), or the [iOS
SDK](https://stripe.dev/stripe-ios/).

### Payment status

The payment process differs across payment methods and geographical locations.
Payments can also fail initially (for example, a customer might enter the wrong
card number or have insufficient funds), so various payment outcomes are
possible.

A [PaymentIntent](https://docs.stripe.com/payments/payment-intents) tracks the
lifecycle of every payment. Whenever a payment is due for a subscription, Stripe
generates an invoice and a PaymentIntent. The PaymentIntent ID attaches to the
invoice and you can access it from the Invoice and Subscription objects. The
state of the PaymentIntent affects the state of the invoice and the
subscription. Here’s how the different outcomes of a payment map to the
different statuses:

Payment outcomePaymentIntent statusInvoice statusSubscription
statusSuccess`succeeded``paid``active`Fails because of a card
error`requires_payment_method``open``incomplete`Fails because of
authentication`requires_action``open``incomplete`
The following sections explain these statuses and the actions to take for each.

### Payment succeeded

When your payment succeeds, the status of the PaymentIntent is `succeeded`, and
the subscription becomes `active`. For [payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
with longer processing periods, subscriptions are immediately activated. In
these cases, the status of the PaymentIntent may be `processing` for an `active`
subscription until the payment succeeds.

With your subscription now activated, provision access to your product. Read the
guide to learn more about [the subscription
lifecycle](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)
and best practices for provisioning.

ResponseSubscriptionPaymentIntent
```
{
 "id": "sub_1ELI8bClCIKljWvsvK36TXlC",
 "object": "subscription",
 "status": "active",
 ...
 "latest_invoice": {
 "id": "in_EmGqfJMYy3Nt9M",
 "status": "paid",
 ...
 "payment_intent": {
 "status": "succeeded",
 ...
 }
 }
}
```

activesucceeded

![Subscription payment network
flow.](https://b.stripecdn.com/docs-statics-srv/assets/payment-flow-succeeds.ac7343c9ec9a77e6efa1a84c02bb597d.svg)

### Requires payment method

If payment fails because of a [card
error](https://docs.stripe.com/api/errors#errors-card_error), such as a
[decline](https://docs.stripe.com/declines#issuer-declines), the status of the
PaymentIntent is `requires_payment_method` and the subscription is `incomplete`.

ResponseSubscriptionPaymentIntent
```
{
 "id": "sub_1ELI8bClCIKljWvsvK36TXlC",
 "object": "subscription",
 "status": "incomplete",
 ...
 "latest_invoice": {
 "id": "in_EmGqfJMYy3Nt9M",
 "status": "open",
 ...
 "payment_intent": {
 "status": "requires_payment_method",
 ...
 }
 }
}
```

incompleterequires_payment_method
To resolve these scenarios:

- Notify the customer.
- Collect new payment information and [confirm the payment
intent](https://docs.stripe.com/api/payment_intents/confirm).
- Update the [default payment
method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
on the subscription.

Learn how to [handle payment failures for
subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks#payment-failures).

![How to handle subscription payment
failures.](https://b.stripecdn.com/docs-statics-srv/assets/payment-flow-requires-payment-method.8305917aa91650ba7f7e9b6e5999ce32.svg)

### Requires action

Some payment methods require customer authentication with [3D
Secure](https://docs.stripe.com/payments/3d-secure) (3DS) to complete the
payment process. If you use the [Payment Intents
API](https://docs.stripe.com/api/payment_intents), the value of
`latest_invoice.payment_intent.status` is `requires_action` when a customer
needs to authenticate a payment. 3DS completes the authentication process.
Whether a payment method requires authentication depends on your [Radar
rules](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
and the issuing bank for the card.

Regulations in Europe often require 3D Secure. See [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) to
determine whether handling this status is important for your business. If you
have an existing billing integration and want to add support for this flow, also
see the [Billing SCA Migration
guide](https://docs.stripe.com/billing/migration/strong-customer-authentication).

ResponseSubscriptionPaymentIntent
```
{
 "id": "sub_1ELI8bClCIKljWvsvK36TXlC",
 "object": "subscription",
 "status": "incomplete",
 ...
 "latest_invoice": {
 "id": "in_EmGqfJMYy3Nt9M",
 "status": "open",
 ...
 "payment_intent": {
 "status": "requires_action",
 "client_secret": "pi_91_secret_W9",
 "next_action": {
 "type": "use_stripe_sdk",
 ...
 },
 ...
 }
 }
}
```

incompleterequires_action
To handle these scenarios:

- Monitor for the `invoice.payment_action_required` event notification with
[webhook endpoints](https://docs.stripe.com/billing/subscriptions/webhooks).
This indicates that authentication is required.
- Notify your customer that they must authenticate.
- Retrieve the client secret for the payment intent and pass it in a call to
[stripe.ConfirmCardPayment](https://docs.stripe.com/js/payment_intents/confirm_card_payment).
This displays an authentication modal to your customers, attempts payment, then
closes the modal and returns context to your application.
- Monitor the `invoice.paid` event on your event destination to verify that the
payment succeeded. Users can leave your application before
`confirmCardPayment()` finishes. Verifying whether the payment succeeded allows
you to correctly provision your product.

![How to handle subscription payments that require additional action from the
customer.](https://b.stripecdn.com/docs-statics-srv/assets/payment-flow-requires-action.ac57889e9bccdb6ec4f5ea47fba194ec.svg)

### Recurring charges

Stripe handles recurring charges for you automatically. This includes:

- [Automatically
invoicing](https://docs.stripe.com/billing/invoices/subscription#subscription-renewal)
customers and attempting payments when new billing cycles start.
- When payments fail, Stripe retries them using the [Smart
Retries](https://docs.stripe.com/invoicing/automatic-collection#smart-retries)
feature or your custom retry schedule. This automatically re-attempts payment
according to your Dashboard settings when cards are declined. If a failure
returns a non-retryable [decline code](https://docs.stripe.com/declines/codes),
the scheduled retries continue but the payment executes only if you obtain a new
payment method.

You can send a [dunning
email](https://docs.stripe.com/invoicing/integration/send-email) to customers
for overdue payments to increase recovery chances. For payments that require 3D
Secure, you can [configure your billing
settings](https://dashboard.stripe.com/account/billing/automatic) to send a
[hosted link](https://docs.stripe.com/invoicing/hosted-invoice-page) to
customers so they can complete the flow.

#### Handle recurring charge failures

If you don’t want to use Stripe’s tooling to manage failures, you can build your
own. If a payment fails or if it requires customer authentication, the
subscription’s `status` is set to `past_due` and the PaymentIntent status is
either `requires_payment_method` or `requires_action`.

![Objects involved when handling failed or action required subscription
payments.](https://b.stripecdn.com/docs-statics-srv/assets/recurring-charge-failure.0e0ffd1930f8e91c96f21707a49111b6.svg)

To manage these scenarios, set up a [webhook
endpoint](https://docs.stripe.com/webhooks) and listen to the
[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)
event so you’re notified when subscriptions enter a `past_due` state:

```
{
 "id": "sub_E8uXk63MAbZbto",
 "object": "subscription",
 ...
 "status": "past_due",
 "latest_invoice": "in_1EMLu1ClCIKljWvsfTjRFAxa"
}
```

For these subscriptions, you need to get your customers back into your
application to collect a different payment method so they can complete the
payment. You can use an email or a mobile push notification. Stripe provides
built-in reminder emails to handle this case, which you can configure in your
[billing settings](https://dashboard.stripe.com/account/billing/automatic).

When your customer is back in your application, reuse either your [payment
failure
flow](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method)
or [customer action
flow](https://docs.stripe.com/billing/subscriptions/overview#requires-action)
depending on the status of the associated PaymentIntent. After the payment
succeeds, the status of the subscription is `active` and the invoice is `paid`.

### Handle non-payment invoices

Subscriptions that include [free
trials](https://docs.stripe.com/billing/subscriptions/trials), [usage-based
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing),
invoices with coupons, or applied customer credit balances often result in
non-payment invoices. This means you don’t immediately charge your customer when
you create the subscription.

Even though you don’t charge customers for the first invoice, authenticating and
authorizing their card is often beneficial as it can increase the chance that
the first non-zero payment completes successfully. Payments made this way are
known as off-session payments. To manage these scenarios, Stripe created
SetupIntents.

#### Use SetupIntents

You can use SetupIntents to:

- Collect payment information.
- Authenticate your customer’s card to claim
[exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)
later.
- Authorize your customer’s card without charging it.

Authenticating payments allows your customer to grant permissions to charge
their card. [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) requires
this, and [3DS](https://docs.stripe.com/payments/3d-secure) is a common way to
complete it. Collecting payment method information and authorizing it ensures
that you can successfully charge the payment method.

In off-session scenarios, SetupIntents enable you to charge customers for their
first non-zero payment without having to bring them back to your website or app
for authentication. This reduces the friction on your customers.

The `pending_setup_intent` field on a subscription doesn’t cancel automatically
when the subscription ends. Listen for `customer.subscription.deleted` events
and manually [cancel a subscription
SetupIntent](https://docs.stripe.com/api/setup_intents/cancel) if needed.

Stripe automatically creates SetupIntents for subscriptions that don’t require
an initial payment. The authentication and authorization process also completes
at this point, if required. If both succeed or aren’t required, no action is
necessary, and the `subscription.pending_setup_intent` field is `null`. If
either step fails, Stripe recommends using the SetupIntent on your frontend to
resolve the issue while your customer is on-session. The next two sections
explain in detail how to manage scenarios where authentication or authorization
fail.

#### Manage authentication failures Client-side

Authentication failures occur when Stripe is unable to authenticate your
customer with their card issuer. When this happens, the `status` of the
SetupIntent is set to `requires_action`.

![How to handle subscription payment authentication
failures.](https://b.stripecdn.com/docs-statics-srv/assets/authentication_failure.2eaec43cac8c688f0ff3438fbe3b50e4.svg)

To resolve these scenarios, call
[confirmCardSetup](https://docs.stripe.com/js#stripe-confirm-card-setup) on your
frontend so that your customer can complete the authentication flow manually.
The code example below [expands](https://docs.stripe.com/api/expanding_objects)
the `pending_setup_intent` to complete the flow.

```
const {pending_setup_intent} = subscription;

if (pending_setup_intent) {
 const {client_secret, status} = subscription.pending_setup_intent;

 if (status === "requires_action") {
 const {setupIntent, error} = await stripe.confirmCardSetup(client_secret);

 if (error) {
 // Display error.message in your UI.
 } else {
 // The setup has succeeded. Display a success message.
 }
 }
}
```

After completing this flow, authorization executes if it’s required. If
authorization succeeds, or if it’s not required, `pending_setup_intent` is
updated to `null` upon completion.

#### Manage authorization failures Client-side

Payment authorization failures occur when Stripe can’t verify that a card can be
charged. When this happens, the `status` of the SetupIntent is set to
`requires_payment_method`. This generally means that subsequent charges with
that card fail.

![How to handle subscription payment authorization
failures.](https://b.stripecdn.com/docs-statics-srv/assets/authorization_failure.0b6ca4a2e2bbeba11710bf22fb0a5d00.svg)

To resolve these scenarios, [collect a new payment
method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method),
then update the default payment method for your customer or the subscription.
The code example below [expands](https://docs.stripe.com/api/expanding_objects)
the `pending_setup_intent` to complete the flow.

```
const {pending_setup_intent, latest_invoice} = subscription;

if (pending_setup_intent) {
 const {client_secret, status} = subscription.pending_setup_intent;

 if (status === "requires_action") {
 const {setupIntent, error} = await stripe.confirmCardSetup(client_secret);

 if (error) {
 // Display error.message in your UI.
 } else {
 // The setup has succeeded. Display a success message.
 }
 } else if (status === "requires_payment_method") {
 // Collect new payment method
 }
}
```

## The subscription lifecycle

This is what the recommended subscription flow looks like:

- You create the subscription. The `status` of the subscription is `incomplete`
(if you follow the recommended flow—if you create a subscription without
specifying the `payment_behavior`, the default `status` is `active`).
- An invoice is created for the subscription. The `status` of the invoice is
`open`.
- The customer pays the first invoice.
- When the payment succeeds:

- The subscription `status` moves to `active`
- The invoice `status` is set to `paid`
- Stripe sends an `invoice.paid` event to your configured webhook endpoints.
- You provision access to your product. You can confirm whether the invoice has
been paid by:

- Setting up a webhook endpoint or another type of event destination and
listening for the `invoice.paid` event.
- Manually checking the subscription object and looking for
`subscription.status=active`. The `status` becomes `active` when the invoice has
been paid either through an automatic charge or having the customer pay
manually.

The `status` can also become `trialing` if you offer trials that don’t require
payments. When the trial is over, the subscription moves to `active` and the
subscribed customer starts to be charged.

![Subscription creation and expiration
workflow](https://b.stripecdn.com/docs-statics-srv/assets/lifecycle-default-incomplete.a6ba5c1779f0f9b8601166f41bbc6d88.svg)

### Subscription payment behavior

To simplify handling failed payments, create subscriptions with
`payment_behavior` set to
[default_incomplete](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior).
This creates subscriptions with status `incomplete`, which allows you to collect
and confirm payment information in a single user interface. When using
`allow_incomplete` or `error_if_incomplete`, Stripe immediately attempts to pay
the invoice. If the payment fails, the subscription’s status changes to
`incomplete` or the creation fails.

### Successful payments

When your customer successfully pays the invoice, the subscription updates to
`active` and the invoice to `paid`. At this point, you can provision access to
your product.

#### Payment window

Customers have about 23 hours to make a successful payment. The subscription
remains in status `incomplete` and the invoice is `open` during this time. If
your customer pays the invoice, the subscription updates to `active` and the
invoice to `paid`. If they don’t make a payment, the subscription updates to
`incomplete_expired` and the invoice becomes `void`.

This window exists because your customer usually makes the first payment for a
subscription while on-session. If the customer returns to your application after
23 hours, create a new subscription for them.

### Failed payments

The subscription’s status remains `active` as long as automatic payments
succeed. If automatic payment fails, the subscription updates to `past_due` and
Stripe attempts to recover payment based on your [retry
rules](https://dashboard.stripe.com/account/billing/automatic). If payment
recovery fails, you can set the subscription status to `canceled`, `unpaid`, or
leave it `past_due`.

### Unpaid subscriptions

For subscriptions with unpaid invoices, the unpaid invoices remain open but
further payment attempts are paused. The subscription continues to generate
invoices each billing cycle, which remain in the `draft` state. To reactivate
the subscription:

- Collect new payment information if necessary.
- Enable automatic collection by setting [auto
advance](https://docs.stripe.com/api/invoices/update#update_invoice-auto_advance)
to `true` on draft invoices.
- [Finalize](https://docs.stripe.com/api/invoices/finalize) and pay the open
invoices. Paying the most recent non-voided invoice before its due date updates
the subscription status to `active`.

Invoices marked as uncollectable are treated as `paid` when determining
subscription status, even though their
[paid](https://docs.stripe.com/api/invoices/object#invoice_object-paid) property
remains `false`. Stripe ignores voided invoices when determining subscription
status; the most recent non-voided invoice is used instead.

The `status` of an unpaid subscription is based on your [failed payment
settings](https://dashboard.stripe.com/settings/billing/automatic) in the
Dashboard.

### Cancel subscriptions

If you cancel a subscription, it disables creating new invoices and stops
automatic collection of all invoices from the subscription because it sets
`auto_advance` to `false`. It also deletes the subscription and you can no
longer update the subscription or its
[metadata](https://docs.stripe.com/metadata). If your customer wants to
resubscribe, you need to collect new payment information from them and create a
new subscription.

### Voiding an invoice generated by a subscription

If the subscription is `incomplete` and you void the first invoice that’s
generated, the subscription updates to `incomplete_expired`. If you void the
most recent invoice for an active subscription and it’s not the first one, the
following logic is applied to each invoice (from most recent to oldest) until it
meets one of these conditions:

- If the invoice is in a `paid` or `uncollectible` state, the subscription state
is set to `active`.
- If the
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
is set to `charge_automatically` on the invoice and Stripe stopped dunning on
the invoice because of retry limits, the subscription state is set to `canceled`
, `unpaid`, or `past_due` based on your [automatic collection
settings](https://dashboard.stripe.com/settings/billing/automatic).
- If the
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
is set to `send_invoice`, and the invoice is past its due date, the state of the
subscription is set to `past_due`.
- If the invoice is in none of these states, the same steps execute on the next
most recent invoice.

If no invoices match any of the above criteria, the subscription state is set to
`active`.

### Checkout Sessions

For [Stripe Checkout](https://docs.stripe.com/payments/checkout) integrations,
you can’t update the subscription or its invoice if the session’s subscription
is `incomplete`. You can listen to the
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
event to make the update after the session has completed.

You can also [expire the
session](https://docs.stripe.com/api/checkout/sessions/expire) instead if you
want to cancel the session’s subscription, void the subscription invoice, or
mark the invoice as uncollectible.

### Get referral information

You can use [Affiliate and referral Stripe
Apps](https://marketplace.stripe.com/categories/affiliate_and_referrals) to set
up and manage referral and affiliate programs with Stripe, get customer
information, and automate commission adjustments from the Stripe Dashboard.

### Subscription statuses

StatusDescription`trialing`The subscription is currently in a trial period and
you can safely provision your product for your customer. The subscription
transitions automatically to `active` when a customer makes the first
payment.`active`The subscription is in good standing. For `past_due`
subscriptions, paying the latest associated invoice or marking it uncollectible
transitions the subscription to `active`. Note that `active` doesn’t indicate
that all outstanding invoices associated with the subscription have been paid.
You can leave other outstanding invoices open for payment, mark them as
uncollectible, or void them as you see fit.`incomplete`The customer must make a
successful payment within 23 hours to activate the subscription. Or the payment
[requires
action](https://docs.stripe.com/billing/subscriptions/overview#requires-action),
such as customer authentication. Subscriptions can also be `incomplete` if
there’s a pending payment and the PaymentIntent status is
`processing`.`incomplete_expired`The initial payment on the subscription failed
and the customer didn’t make a successful payment within 23 hours of
subscription creation. These subscriptions don’t bill customers. This status
exists so you can track customers that failed to activate their
subscriptions.`past_due`Payment on the latest finalized invoice either failed or
wasn’t attempted. The subscription continues to create invoices. Your
[subscription
settings](https://docs.stripe.com/billing/subscriptions/overview#settings)
determine the subscription’s next state. If the invoice is still unpaid after
all attempted [smart
retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries), you
can configure the subscription to move to `canceled`, `unpaid`, or leave it as
`past_due`. To move the subscription to `active`, pay the most recent invoice
before its due date.`canceled`The subscription was canceled. During
cancellation, automatic collection for all unpaid invoices is disabled
(`auto_advance=false`). This is a terminal state that can’t be
updated.`unpaid`The latest invoice hasn’t been paid but the subscription remains
in place. The latest invoice remains open and invoices continue to generate, but
payments aren’t attempted. Revoke access to your product when the subscription
is `unpaid` because payments were already attempted and retried while
`past_due`. To move the subscription to `active`, pay the most recent invoice
before its due date.`paused`The subscription has ended its trial period without
a default payment method and the
[trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment)
is set to `pause`. Invoices are no longer created for the subscription. After
attaching a default payment method to the customer, you can [resume the
subscription](https://docs.stripe.com/billing/subscriptions/trials#resume-a-paused-subscription).
## Subscription events

[Events](https://docs.stripe.com/api#event_types) are triggered every time a
subscription is created or changed. We send some events immediately when a
subscription is created, while others recur on regular billing intervals. We
recommend listening for events with [webhook
endpoints](https://docs.stripe.com/billing/subscriptions/webhooks).

Make sure that your integration properly handles the events. For example, you
might want to email a customer if a payment fails or revoke a customer’s access
when a subscription is canceled.

The following table describes the most common events related to subscriptions
and, where applicable, suggests actions for handling the events.

EventDescription`customer.created`Sent when a
[Customer](https://docs.stripe.com/api/customers/object) is successfully
created.`customer.subscription.created`Sent when the subscription is created.
The subscription `status` might be `incomplete` if customer authentication is
required to complete the payment or if you set `payment_behavior` to
`default_incomplete`. View [subscription payment
behavior](https://docs.stripe.com/billing/subscriptions/overview#subscription-payment-behavior)
to learn more.`customer.subscription.deleted`Sent when a customer’s subscription
ends.`customer.subscription.paused`Sent when a subscription’s `status` changes
to `paused`. For example, this is sent when a subscription is
[configured](https://docs.stripe.com/api/subscriptions/create#create_subscription-trial_settings-end_behavior-missing_payment_method)
to pause when a [free trial ends without a payment
method](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment).
Invoicing won’t occur until the subscription is
[resumed](https://docs.stripe.com/api/subscriptions/resume). We don’t send this
event if [payment collection is
paused](https://docs.stripe.com/billing/subscriptions/pause-payment) because
invoices continue to be created during that time
period.`customer.subscription.resumed`Sent when a subscription previously in a
`paused` status is resumed. This doesn’t apply when [payment collection is
unpaused](https://docs.stripe.com/billing/subscriptions/pause-payment#unpausing).`customer.subscription.trial_will_end`Sent
three days before the [trial period
ends](https://docs.stripe.com/billing/subscriptions/trials). If the trial is
less than three days, this event is
triggered.`customer.subscription.updated`Sent when a subscription starts or
[changes](https://docs.stripe.com/billing/subscriptions/change). For example,
renewing a subscription, adding a coupon, applying a discount, adding an invoice
item, and changing plans all trigger this
event.`entitlements.active_entitlement_summary.updated`Sent when a customer’s
active entitlements are updated. When you receive this event, you can provision
or de-provision access to your product’s features. Read more about [integrating
with
entitlements](https://docs.stripe.com/billing/entitlements).`invoice.created`Sent
when an invoice is created for a new or renewing subscription. If Stripe fails
to receive a successful response to `invoice.created`, then finalizing all
invoices with [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
is delayed for up to 72 hours. Read more about [finalizing
invoices](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized).-
Respond to the notification by sending a request to the [Finalize an
invoice](https://docs.stripe.com/api/invoices/finalize) API.
`invoice.finalized`Sent when an invoice is successfully finalized and ready to
be paid.- You can send the invoice to the customer. View [invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
to learn more.
- Depending on your settings, we automatically charge the default payment method
or attempt collection. View [emails after
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#emails)
to learn more.
`invoice.finalization_failed`The invoice couldn’t be finalized. Learn how to
[handle invoice finalization
failures](https://docs.stripe.com/tax/customer-locations#finalizing-invoices-with-finalization-failures)
by reading the guide. Learn more about [invoice
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
in the invoices overview guide.- Inspect the Invoice’s
[last_finalization_error](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
to determine the cause of the error.
- If you’re using Stripe Tax, check the Invoice object’s
[automatic_tax](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
field.
- If `automatic_tax[status]=requires_location_inputs`, the invoice can’t be
finalized and payments can’t be collected. Notify your customer and collect the
required [customer location](https://docs.stripe.com/tax/customer-locations).
- If `automatic_tax[status]=failed`, retry the request later.
`invoice.paid`Sent when the invoice is successfully paid. You can provision
access to your product when you receive this event and the subscription `status`
is `active`.`invoice.payment_action_required`Sent when the invoice requires
customer authentication. Learn how to handle the subscription when the invoice
[requires
action](https://docs.stripe.com/billing/subscriptions/overview#requires-action).
`invoice.payment_failed`

A payment for an invoice failed. The PaymentIntent status changes to
`requires_action`. The status of the subscription continues to be `incomplete`
*only* for the subscription’s first invoice. If a payment fails, there are
several possible actions to take:

- Notify the customer. Read about how you can configure [subscription
settings](https://docs.stripe.com/billing/subscriptions/overview#settings) to
enable [Smart
Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries) and
other revenue recovery features.
- If you’re using PaymentIntents, collect new payment information and [confirm
the PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm).
- Update the [default payment
method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
on the subscription.
`invoice.upcoming`Sent a few days prior to the renewal of the subscription. The
number of days is based on the number set for Upcoming renewal events in the
[Dashboard](https://dashboard.stripe.com/settings/billing/automatic). For
existing subscriptions, changing the number of days takes effect on the next
billing period. You can still add [extra invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items),
if needed.`invoice.updated`Sent when a payment succeeds or fails. If payment is
successful the `paid` attribute is set to `true` and the `status` is `paid`. If
payment fails, `paid` is set to `false` and the `status` remains `open`. Payment
failures also trigger a `invoice.payment_failed`
event.`payment_intent.created`Sent when a
[PaymentIntent](https://docs.stripe.com/api/payment_intents) is
created.`payment_intent.succeeded`Sent when a PaymentIntent has successfully
completed payment.`subscription_schedule.aborted`Sent when a subscription
schedule is canceled because payment delinquency terminated the related
subscription.`subscription_schedule.canceled`Sent when a subscription schedule
is canceled, which also cancels any active associated
subscription.`subscription_schedule.completed`Sent when all
[phases](https://docs.stripe.com/billing/subscriptions/subscription-schedules#subscription-schedule-phases)
of a subscription schedule complete.`subscription_schedule.created`Sent when a
new subscription schedule is created.`subscription_schedule.expiring`Sent 7 days
before a subscription schedule is set to
expire.`subscription_schedule.released`Sent when a subscription schedule is
[released](https://docs.stripe.com/api/subscription_schedules/release), or
stopped and disassociated from the subscription, which
remains.`subscription_schedule.updated`Sent when a subscription schedule is
updated.
## Invoice lifecycle

The [invoices overview](https://docs.stripe.com/invoicing/overview) provides a
more detailed explanation of how invoices work, but for invoices generated by
subscriptions, the basic lifecycle looks like this:

- The subscription generates a new invoice in `draft` state.
- About [one
hour](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items)
after creation, the invoice finalizes. You can’t make changes after the invoice
is finalized.
- The status is set to `open` and Stripe automatically attempts to pay it using
the default payment method.
- If payment succeeds, the status updates to `paid`.
- If payment fails, the invoice remains `open` and the subscription becomes
`past_due`.

In this flow, Stripe doesn’t notify your customer about the invoice. Payment is
automatically attempted on the invoice shortly after it’s generated. However, if
[customer emails](https://dashboard.stripe.com/account/emails) are enabled, we
send an email receipt.

## Subscription settings and recovery

Your [subscription
settings](https://dashboard.stripe.com/settings/billing/automatic) determine how
Stripe responds when payments fail or when subscriptions become past due.

### Smart Retries

After creating a subscription, payment failure is the most important event that
can happen. Failures occur for many reasons:

- Lack of a payment method on the customer.
- The payment method is expired.
- The payment is declined.

You can configure Stripe to retry failed payments. [Smart
Retries](https://dashboard.stripe.com/settings/billing/automatic) use Stripe’s
machine learning to pick the optimal time to retry over a configurable time
period up to 2 months after the initial payment fails.

You can also modify the retry schedule with custom rules. You can configure up
to three retries, each with a specific number of days after the previous
attempt.

You can use the
[invoice.payment_failed](https://docs.stripe.com/billing/revenue-recovery/smart-retries#invoice-payment-failed-webhook)
event to monitor subscription payment failure events and retry attempt updates.
After a payment attempt on an invoice, its
[next_payment_attempt](https://docs.stripe.com/api#invoice_object-next_payment_attempt)
value is set using the current subscription settings in your Dashboard.

If recovery fails, the subscription transitions according to your settings. The
options are:

SettingDescriptionCancel the subscriptionThe subscription changes to a
`canceled` state after the maximum number of days defined in the retry
schedule.Mark the subscription as unpaidThe subscription changes to an `unpaid`
state after the maximum number of days defined in the retry schedule. Invoices
continue to be generated and stay in a draft state.Leave the subscription
past-dueThe subscription remains in a `past_due` state after the maximum number
of days defined in the retry schedule. Invoices continue to be generated and
charge customer based on retry settings.
After the final payment attempt, we make no further payment attempts. Changing
your subscription settings only affects future retries.

#### Emails

Stripe can optionally send different emails to customers, using the email
addresses associated with the [Customer](https://docs.stripe.com/api#customers)
object:

- An upcoming renewal reminder at the same time that we send the
`invoice.upcoming` event.
- A failed payment notification prompting customers to update their payment
information. Learn [how to turn on failed payment
notifications](https://docs.stripe.com/billing/revenue-recovery/customer-emails#failed-payment-notifications).
- An expiring card notification when a customer’s `default_source` card is due
to expire.

You can customize the logos and colors your customers see in emails, and our
Hosted Invoice Payment page by changing the [branding
settings](https://dashboard.stripe.com/account/branding) in the Dashboard.

### Manual payment

You can configure the due date for invoices that use the `send_invoice`
[collection
method](https://docs.stripe.com/billing/collection-method#set-collection-method-invoice)
to receive manual payments. You can also configure up to three reminders,
starting at 10 days before the due date and ending at 60 days after.

You can also take additional action on the subscription 30, 60, or 90 days after
an invoice becomes past due. The options are:

SettingDescriptionCancel the subscriptionThe subscription changes to a
`canceled` state after the maximum number of days defined in the retry
schedule.Mark the subscription as unpaidThe subscription changes to an `unpaid`
state after the maximum number of days defined in the retry schedule. Invoices
continue to generate and either stay in a `draft` state or transition to a state
specified in your invoice settings.Leave the subscription past-dueThe
subscription remains in a `past_due` state after the maximum number of days
defined in the retry schedule. Invoices continue to be generated into an `open`
state.
Learn more about [subscription
statuses](https://docs.stripe.com/billing/subscriptions/overview#subscription-statuses).

### Payments requiring 3D Secure

For payments that require 3D Secure, Stripe can send a confirmation email to
your customer at the same time that we send the
`invoice.payment_action_required`. You can also configure sending up to three
reminders, from 1 to 7 days after the payment was initiated.

If a payment is still incomplete after the set number of days, you can choose
to:

SettingDescriptionCancel the subscriptionThe subscription changes to a
`canceled` state after the maximum number of days defined in the retry
schedule.Mark the subscription as unpaidThe subscription changes to an `unpaid`
state after the maximum number of days defined in the retry schedule. Invoices
continue to be generated and stay in a draft state.Leave the subscription
past-dueThe subscription remains in a `past_due` state after the maximum number
of days defined in the retry schedule. Invoices continue to be generated and
charge customer based on retry settings.
### Trials

Card networks require you to inform your customers about their trials. Stripe
can manage this communication for you. In the [Stripe
Dashboard](https://dashboard.stripe.com/settings/billing/automatic), you can
configure the cancellation URL that’s included on both the reminder emails and
on the receipt for the first invoice after a trial ends. You can also configure
the statement descriptor for the first charge after a trial. Learn more about
these requirements and settings on the
[trials](https://docs.stripe.com/billing/subscriptions/trials#compliance) page.

## Change subscriptions

Stripe supports [modifying existing
subscriptions](https://docs.stripe.com/billing/subscriptions/change) without
having to cancel and recreate them. Some of the most significant changes you
might make are [upgrading or
downgrading](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade)
the subscription price, or
[canceling](https://docs.stripe.com/billing/subscriptions/cancel) or [pausing
payment collection
for](https://docs.stripe.com/billing/subscriptions/pause-payment) an active
subscription. Learn more about how to [change existing
subscriptions](https://docs.stripe.com/billing/subscriptions/change).

## Links

- [Customer](https://docs.stripe.com/api/customers)
- [Entitlement](https://docs.stripe.com/api/entitlements/active-entitlement)
- [Feature](https://docs.stripe.com/api/entitlements/feature)
- [Invoice](https://docs.stripe.com/api/invoices)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [Price](https://docs.stripe.com/api/prices)
- [Product](https://docs.stripe.com/api/products)
- [ProductFeature](https://docs.stripe.com/api/product-feature)
- [Subscription](https://docs.stripe.com/api/subscriptions)
- [retrieving their active entitlements or listening to the Active Entitlement
Summary event](https://docs.stripe.com/billing/entitlements#entitlements)
- [sample
integration](https://github.com/stripe-samples/subscription-use-cases/tree/master/fixed-price-subscriptions)
- [Billing quickstart](https://docs.stripe.com/billing/quickstart)
- [integration
guide](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [products and
prices](https://docs.stripe.com/products-prices/how-products-and-prices-work)
- [confirm](https://docs.stripe.com/api/payment_intents/confirm)
- [create a Payment
Link](https://docs.stripe.com/payment-links/create?pricing-model=standard)
- [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions)
- [a hosted page](https://docs.stripe.com/checkout/quickstart)
- [an embedded form on your
site](https://docs.stripe.com/checkout/embedded/quickstart)
- [a customized checkout page built with embedded
components](https://docs.stripe.com/checkout/custom/quickstart)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [collect payment details and activate the
subscription](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=elements#collect-payment)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Entitlements](https://docs.stripe.com/billing/entitlements)
- [event destinations](https://docs.stripe.com/event-destinations)
- [Track active
subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks#active-subscriptions)
- [Handle payment
failures](https://docs.stripe.com/billing/subscriptions/webhooks#payment-failures)
- [Check event
objects](https://docs.stripe.com/event-destinations#events-overview)
-
[payment_behavior=default_incomplete](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)
- [Elements](https://docs.stripe.com/js/elements_object)
- [Android SDK](https://stripe.dev/stripe-android/)
- [iOS SDK](https://stripe.dev/stripe-ios/)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
- [the subscription
lifecycle](https://docs.stripe.com/billing/subscriptions/overview#subscription-lifecycle)
- [card error](https://docs.stripe.com/api/errors#errors-card_error)
- [decline](https://docs.stripe.com/declines#issuer-declines)
- [default payment
method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [Radar
rules](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [Billing SCA Migration
guide](https://docs.stripe.com/billing/migration/strong-customer-authentication)
- [webhook endpoints](https://docs.stripe.com/billing/subscriptions/webhooks)
-
[stripe.ConfirmCardPayment](https://docs.stripe.com/js/payment_intents/confirm_card_payment)
- [Automatically
invoicing](https://docs.stripe.com/billing/invoices/subscription#subscription-renewal)
- [Smart
Retries](https://docs.stripe.com/invoicing/automatic-collection#smart-retries)
- [decline code](https://docs.stripe.com/declines/codes)
- [dunning email](https://docs.stripe.com/invoicing/integration/send-email)
- [configure your billing
settings](https://dashboard.stripe.com/account/billing/automatic)
- [hosted link](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [webhook endpoint](https://docs.stripe.com/webhooks)
-
[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)
- [payment failure
flow](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method)
- [customer action
flow](https://docs.stripe.com/billing/subscriptions/overview#requires-action)
- [free trials](https://docs.stripe.com/billing/subscriptions/trials)
- [usage-based
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
-
[exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)
- [cancel a subscription
SetupIntent](https://docs.stripe.com/api/setup_intents/cancel)
- [confirmCardSetup](https://docs.stripe.com/js#stripe-confirm-card-setup)
- [expands](https://docs.stripe.com/api/expanding_objects)
- [auto
advance](https://docs.stripe.com/api/invoices/update#update_invoice-auto_advance)
- [Finalize](https://docs.stripe.com/api/invoices/finalize)
- [paid](https://docs.stripe.com/api/invoices/object#invoice_object-paid)
- [failed payment
settings](https://dashboard.stripe.com/settings/billing/automatic)
- [metadata](https://docs.stripe.com/metadata)
-
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [expire the session](https://docs.stripe.com/api/checkout/sessions/expire)
- [Affiliate and referral Stripe
Apps](https://marketplace.stripe.com/categories/affiliate_and_referrals)
- [subscription
settings](https://docs.stripe.com/billing/subscriptions/overview#settings)
- [smart
retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries)
-
[trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment)
- [resume the
subscription](https://docs.stripe.com/billing/subscriptions/trials#resume-a-paused-subscription)
- [Events](https://docs.stripe.com/api#event_types)
- [Customer](https://docs.stripe.com/api/customers/object)
- [subscription payment
behavior](https://docs.stripe.com/billing/subscriptions/overview#subscription-payment-behavior)
-
[configured](https://docs.stripe.com/api/subscriptions/create#create_subscription-trial_settings-end_behavior-missing_payment_method)
- [resumed](https://docs.stripe.com/api/subscriptions/resume)
- [payment collection is
paused](https://docs.stripe.com/billing/subscriptions/pause-payment)
- [payment collection is
unpaused](https://docs.stripe.com/billing/subscriptions/pause-payment#unpausing)
- [changes](https://docs.stripe.com/billing/subscriptions/change)
- [automatic
collection](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection)
- [finalizing
invoices](https://docs.stripe.com/invoicing/integration/workflow-transitions#finalized)
- [emails after
finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions#emails)
- [handle invoice finalization
failures](https://docs.stripe.com/tax/customer-locations#finalizing-invoices-with-finalization-failures)
-
[last_finalization_error](https://docs.stripe.com/api/invoices/object#invoice_object-last_finalization_error)
- [customer location](https://docs.stripe.com/tax/customer-locations)
- [extra invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-upcoming-invoice-items)
-
[phases](https://docs.stripe.com/billing/subscriptions/subscription-schedules#subscription-schedule-phases)
- [released](https://docs.stripe.com/api/subscription_schedules/release)
- [invoices overview](https://docs.stripe.com/invoicing/overview)
- [one
hour](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items)
- [customer emails](https://dashboard.stripe.com/account/emails)
-
[invoice.payment_failed](https://docs.stripe.com/billing/revenue-recovery/smart-retries#invoice-payment-failed-webhook)
-
[next_payment_attempt](https://docs.stripe.com/api#invoice_object-next_payment_attempt)
- [Customer](https://docs.stripe.com/api#customers)
- [how to turn on failed payment
notifications](https://docs.stripe.com/billing/revenue-recovery/customer-emails#failed-payment-notifications)
- [branding settings](https://dashboard.stripe.com/account/branding)
- [collection
method](https://docs.stripe.com/billing/collection-method#set-collection-method-invoice)
- [trials](https://docs.stripe.com/billing/subscriptions/trials#compliance)
- [upgrading or
downgrading](https://docs.stripe.com/billing/subscriptions/upgrade-downgrade)
- [canceling](https://docs.stripe.com/billing/subscriptions/cancel)