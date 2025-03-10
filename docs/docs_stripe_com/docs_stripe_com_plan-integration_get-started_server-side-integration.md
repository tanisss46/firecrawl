# Server-side integration

## Set up your Stripe back-end integration.

To set up an optimal backend integration, you must authenticate to Stripe, learn
API request best practices, and appropriately configure your webhooks.

## Authenticate to Stripe

Stripe provides authentication through API key. It’s also possible to create
[restricted access keys](https://docs.stripe.com/keys#limit-access) to further
control access to specific resources. You can use the [secret and publishable
API keys](https://docs.stripe.com/keys#obtain-api-keys) to create tokens, but
need secret keys for any server-side authentication.

Here’s an example API call:

```
curl https://api.stripe.com/v1/balance \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

## API request best practices

Stripe recommends adding an [idempotency
key](https://docs.stripe.com/api/idempotent_requests) to all POST requests. Make
sure that the key is unique, such as a universally unique identifier (UUID) or a
combination of customer ID and order ID. These keys allow you to safely retry
requests if you encounter a network error.

### Customer objects: storing payment details

To store and reuse
[PaymentMethods](https://docs.stripe.com/api/payment_methods), you must attach
them to [Customer objects](https://docs.stripe.com/payments/save-and-reuse).

After attaching the PaymentMethod to a Customer, store the [Customer
ID](https://docs.stripe.com/api/customers/object#customer_object-id) and
[PaymentMethod
ID](https://docs.stripe.com/api/payment_methods/object#payment_method_object-id)
in your system to use it for payments in the future. Because one Customer object
can have a [list of multiple payment
methods](https://docs.stripe.com/api/payment_methods/list), you must specify
both the Customer ID and the PaymentMethod ID when creating a charge later on.

Here’s an example creating a Customer and attaching a PaymentMethod:

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Jenny Rosen" \
 --data-urlencode email="jenny.rosen@stripe.com" \
 -d payment_method={PAYMENT_METHOD_ID}
```

### Refunds

Refunds are managed using the [Refunds](https://docs.stripe.com/api/refunds) API
and can be made for full or partial amounts. To refund a transaction with
Stripe, you’ll need either the PaymentIntent ID or the Charge ID for the
transaction you need to refund.

Refunds use your *available* Stripe balance, and can’t use your pending balance.
If your available balance doesn’t have sufficient funds to cover the amount of
the refund, Stripe debits the remaining amount from your bank account. You can
issue partial refunds, full refunds, and more than one refund against a charge,
but you can’t refund a total greater than the original charge amount.

You can issue refunds using the [API](https://docs.stripe.com/api) or the
[Dashboard](https://dashboard.stripe.com/test/dashboard). You can’t cancel a
refund after you issue it. It takes [5-10 business
days](https://support.stripe.com/questions/customer-refund-processing-time) for
the refund to appear on the customer’s statement. If a customer is curious about
the status of their refund, you can [provide the
ARN](https://support.stripe.com/questions/acquirer-reference-number-(arn)-for-refunds)
so that they can inquire about the refund with their bank.

Here’s an example refund for a PaymentIntent:

```
curl https://api.stripe.com/v1/refunds \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent={PAYMENT_INTENT_ID}
```

Here’s a partial refund example with an amount specified:

```
curl https://api.stripe.com/v1/refunds \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent={PAYMENT_INTENT_ID} \
 -d amount=1000
```

### Disputes and chargebacks

Your business is responsible for managing [disputes (also known as
chargebacks)](https://docs.stripe.com/disputes). We recommend that you actively
monitor disputes and collect and submit evidence to support the validity of
charges where appropriate. We hold disputed funds and deduct them from your
Stripe balance pending a decision. We return the funds if you win the dispute.

You can monitor disputes in two ways:

- Use the Stripe Dashboard and email notifications that you can configure in
your [Dashboard profile](https://dashboard.stripe.com/settings/user).
- You can fully automate the dispute response and evidence submission through
the [Disputes](https://docs.stripe.com/api/disputes) API.

## Configure webhooks

You can use [webhooks](https://docs.stripe.com/webhooks) to capture events that
occur on your account (such as payouts to your bank account, refunds, payments,
and so on). They’re helpful when handling Stripe
[events](https://docs.stripe.com/api/events) that occur asynchronously, or for
those that you want to trigger additional actions for.

!

See our recommended webhook for each type:

WEBHOOK TYPERECOMMENDED WEBHOOKSCHARGES- `charge.succeeded`
- `charge.failed`
- `charge.refunded`
REFUNDS- `refund.created`
- `refund.failed`
PAYOUTS- `payout.created`
- `payout.paid`
- `payout.failed`
PAYMENT INTENTS- `payment_intent.succeeded`
- `payment_intent.payment_failed`
- `payment_intent.canceled`
DISPUTES- `radar.early_fraud_warning.created`
- `charge.dispute.created`
- `charge.dispute.closed`

Use the following resources to set up your webhooks and validate that they’ve
been configured correctly:

- [Webhooks](https://docs.stripe.com/webhooks)
- [Check the webhook signatures](https://docs.stripe.com/webhooks#verify-events)
- [Types of events](https://docs.stripe.com/api/events/types)
- [Best practices for using
webhooks](https://docs.stripe.com/webhooks#best-practices)
- [Check your webhook
configurations](https://dashboard.stripe.com/account/webhooks)

## Links

- [restricted access keys](https://docs.stripe.com/keys#limit-access)
- [secret and publishable API
keys](https://docs.stripe.com/keys#obtain-api-keys)
- [idempotency key](https://docs.stripe.com/api/idempotent_requests)
- [PaymentMethods](https://docs.stripe.com/api/payment_methods)
- [Customer objects](https://docs.stripe.com/payments/save-and-reuse)
- [Customer ID](https://docs.stripe.com/api/customers/object#customer_object-id)
- [PaymentMethod
ID](https://docs.stripe.com/api/payment_methods/object#payment_method_object-id)
- [list of multiple payment
methods](https://docs.stripe.com/api/payment_methods/list)
- [Refunds](https://docs.stripe.com/api/refunds)
- [API](https://docs.stripe.com/api)
- [Dashboard](https://dashboard.stripe.com/test/dashboard)
- [5-10 business
days](https://support.stripe.com/questions/customer-refund-processing-time)
- [provide the
ARN](https://support.stripe.com/questions/acquirer-reference-number-(arn)-for-refunds)
- [disputes (also known as chargebacks)](https://docs.stripe.com/disputes)
- [Dashboard profile](https://dashboard.stripe.com/settings/user)
- [Disputes](https://docs.stripe.com/api/disputes)
- [webhooks](https://docs.stripe.com/webhooks)
- [events](https://docs.stripe.com/api/events)
- [Check the webhook signatures](https://docs.stripe.com/webhooks#verify-events)
- [Types of events](https://docs.stripe.com/api/events/types)
- [Best practices for using
webhooks](https://docs.stripe.com/webhooks#best-practices)
- [Check your webhook
configurations](https://dashboard.stripe.com/account/webhooks)