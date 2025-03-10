# Tour of the API

## See how Stripe API objects fit together and learn best practices for combining them.

The Stripe APIs are powerful and flexible if you know how to use them. This tour
of the API covers key information to help you understand the APIs more deeply:

- The core concepts we use across the APIs
- The path a successful payment takes
- The objects that play a role and how to determine when they’re needed
- Common patterns and best practices for using those objects together

Understanding these patterns helps you move beyond the pre-written code in
Stripe tutorials. You can migrate old integrations to use more modern patterns,
combine simple patterns in novel ways, and plan for future growth.

## Core concepts

### Everything is an object

Everything in your Stripe account is an object, whether you create it with the
API or not. Your balance corresponds to a
[Balance](https://docs.stripe.com/api/balance) object, you track customers with
[Customer](https://docs.stripe.com/api/customers) objects, you store payment
details in [PaymentMethod](https://docs.stripe.com/api/payment_methods) objects,
and so on.

Even low-code and no-code integrations produce these objects. So do actions you
perform in the Dashboard. For instance, when you manually create a customer in
the Dashboard, it still creates a Customer object.

### Objects have lives

Stripe integrations handle complicated processes.

The API uses a single object to track each process. You create the object at the
start of the process, and after every step you can check its `status` to see
what needs to happen next—This is sometimes referred to as a *state machine*.

For instance, while completing a payment, a customer might try several payment
methods. If one payment method fails, a `status` of `requires_payment_method`
lets you know to prompt the customer for another.

### An integration is made out of cooperating objects

To accept a payment, a system needs to create several core objects and manage
them through several states.

Your Stripe integration is a system that handles this creation and management by
communicating with Stripe.

Some integrations do a lot more than that: track customers, manage
subscriptions, etc. But their core payment functionality still comes from the
same objects and steps, with more objects added around that core.

## Payment objects

Stripe uses a variety of related objects to facilitate payments. Before you can
build an integration that suits your specific needs, you must familiarize
yourself with how these objects work together.

Check out this video for an overview of payment object roles and capabilities.

To learn more about Stripe’s payment integration options, see the following
guides:

- [Payment Links](https://docs.stripe.com/payment-links)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Subscriptions](https://docs.stripe.com/billing)
- [Invoicing](https://docs.stripe.com/invoicing)
- [Payment Intents](https://docs.stripe.com/payments/payment-intents)

## The path to a payment

In a modern Stripe integration, every payment uses an object called a
[PaymentIntent](https://docs.stripe.com/api/payment_intents). As its name
suggests, it represents your *intent* to collect a payment. This object tracks
the steps you go through along the way to fulfilling that intent.

For instance, suppose a customer clicks a **Check out** button with a 100 USD
item in their cart. They haven’t bought it yet, and they might never buy it
(maybe at some point they abandon the payment flow, or their card issuer
declines the payment). But clicking **Check out** indicates their *intent* to
buy—and you intend to help them. At that point, an integration creates a
`PaymentIntent` object in the amount of 100 USD to track the rest of the
process.

The `PaymentIntent`’s path to success goes through [several
statuses](https://docs.stripe.com/payments/paymentintents/lifecycle)—here’s a
simplified version:

`requires_payment_method`

`requires_confirmation`

`processing`

`succeeded`

`canceled`

retryShows the status of a PaymentIntent changing from requires_payment_method
to requires_confirmation to processing which either ends in a state of succeeded
or canceled
### Payment methods

A PaymentIntent starts with the status `requires_payment_method`. To move it
forward, Stripe needs details about the customer’s payment method—either a card
number or credentials for some other payment system.

An integration represents these details using an API object called a
[PaymentMethod](https://docs.stripe.com/api/payment_methods). In some
integrations, you write the code that creates that object and attaches it to the
PaymentIntent. In others, Stripe gathers the details and does the work for you.
You can also create and save a payment method for use with future PaymentIntents
[using the Setup Intents API](https://docs.stripe.com/payments/setup-intents).

### Confirmation

The next status is `requires_confirmation`. In an interactive payment flow, the
customer must confirm that they intend to pay—and that they intend to do it
using the method they provided. In a one-time online payment, this usually
happens when they click the **Pay** button.

When the customer clicks **Pay** or otherwise confirms their intent, an
integration notifies Stripe with an API call. In some integrations, you write
the code that makes this call. Stripe provides drop-in UI elements, called
[Stripe Elements](https://docs.stripe.com/payments/elements), to enable this
while still providing flexibility to build a custom integration. In other
integrations, like a [Stripe
Checkout](https://docs.stripe.com/payments/checkout) or [Payment
Links](https://docs.stripe.com/payment-links) integration, Stripe makes the call
and handles the next steps. There are many ways to integrate Stripe and combine
different objects to handle your use case. [Learn more about integration options
for online payments.](https://docs.stripe.com/payments/online-payments)

In most cases a [Charge](https://docs.stripe.com/api/charges) will be created
when a PaymentIntent is confirmed to represent that specific attempt to move
money. The Charge might succeed or fail. If it fails the payment can be retried
by confirming the PaymentIntent again, usually with new payment details.
Allowing retries immediately, without the need to create a new PaymentIntent,
tends to increase conversion rates.

### Processing and success

The intent’s state is now `processing`, and at this point Stripe attempts to
process the payment.

Stripe always does this part for you—and it can have several steps. (For credit
cards, these steps are part of [how cards
work](https://docs.stripe.com/payments/cards/overview).) As we work through the
steps, we update the intent’s state with the outcome: either `succeeded` or back
to `requires_payment_method` if it fails.

When we’re done, one last object comes into play: the
[Event](https://docs.stripe.com/api/events). We use `Event` objects to represent
activity. In this case, the activity might be “the charge succeeded” or “the
charge failed.” In some integrations, you write custom code to respond to events
using [webhook endpoints](https://docs.stripe.com/webhooks). In others, such as
[Checkout](https://docs.stripe.com/payments/checkout) or [Payment
Links](https://docs.stripe.com/payment-links) integrations, Stripe listens for
the event and provides a pre-written response.

## Links

- [Balance](https://docs.stripe.com/api/balance)
- [Customer](https://docs.stripe.com/api/customers)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Subscriptions](https://docs.stripe.com/billing)
- [Invoicing](https://docs.stripe.com/invoicing)
- [Payment Intents](https://docs.stripe.com/payments/payment-intents)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [several statuses](https://docs.stripe.com/payments/paymentintents/lifecycle)
- [using the Setup Intents API](https://docs.stripe.com/payments/setup-intents)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [Learn more about integration options for online
payments.](https://docs.stripe.com/payments/online-payments)
- [Charge](https://docs.stripe.com/api/charges)
- [how cards work](https://docs.stripe.com/payments/cards/overview)
- [Event](https://docs.stripe.com/api/events)
- [webhook endpoints](https://docs.stripe.com/webhooks)