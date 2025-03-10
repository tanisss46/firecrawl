# Trigger webhook events with the Stripe CLI

## Learn how to trigger webhook events in a sandbox.

There are two ways to trigger webhook events in a sandbox:

- Do the actions that lead to the event you want to trigger. For example,
[creating a Customer](https://docs.stripe.com/api/customers/create) with the
Stripe API or in the Stripe Dashboard generates a `customer.created` event.
- Run a command with the Stripe CLI to automatically generate the event.

This guide focuses on the Stripe CLI.

## Trigger events

To see the name of all events supported by the Stripe CLI, run this command.

```
stripe trigger --help
```

To trigger a specific event, run this by replacing `<EVENT>` with the name of
the event.

```
stripe trigger <EVENT>
```

For example, this command triggers the `payment_intent.succeeded` event.

```
stripe trigger payment_intent.succeeded
```

Then, you can view the event in the [events
page](https://dashboard.stripe.com/test/events) of the Stripe Dashboard or by
using the [stripe listen](https://docs.stripe.com/cli/listen) command.

#### Note

Depending on the event that you trigger, the Stripe CLI might generate multiple
related events. For example, when running `stripe trigger price.created`, the
Stripe CLI needs to create a Product to create a Price, so it generates two
events: `product.created` and `price.created`.

## Customize events

To generate events, the Stripe CLI calls the Stripe API with some predefined
parameters. For example, to trigger the `payment_intent.succeeded` event, the
Stripe CLI calls the create PaymentIntent endpoint with the `amount` parameter
set to `2000`. You can change these API parameters with the `override` flag.

```
stripe trigger <EVENT> --override <RESOURCE>:<PROPERTY>=<VALUE>
```

Here are some examples of using overrides.

```
# Set a top-level parameter
stripe trigger customer.created --override customer:name=Bob

# Set a nested parameter
stripe trigger customer.created --override customer:"address[country]"=FR

# Append an element to the end of a list
stripe trigger customer.created --override customer:"preferred_locales[]"=FR

# Replace an element of a list
stripe trigger customer.created --override customer:"preferred_locales[0]"=FR

# Set a parameter inside a list
stripe trigger customer.subscription.created --override
subscription:"items[0][price]"=price_xxx
```

You can also combine multiple overrides on different resources.

```
stripe trigger price.created \
 --override product:name=foo \
 --override price:unit_amount=4200
```

To figure out which resources and parameters you can change, review the relevant
triggers in the [GitHub
repository](https://github.com/stripe/stripe-cli/tree/master/pkg/fixtures/triggers)
of the Stripe CLI.

## Advanced customization of events

If the available events or overrides aren’t sufficient for your use case, you
can write a JSON file describing how to generate an event, and use the CLI to
trigger that event. Read the [API
reference](https://docs.stripe.com/cli/fixtures) to learn more.

## Links

- [creating a Customer](https://docs.stripe.com/api/customers/create)
- [events page](https://dashboard.stripe.com/test/events)
- [stripe listen](https://docs.stripe.com/cli/listen)
- [GitHub
repository](https://github.com/stripe/stripe-cli/tree/master/pkg/fixtures/triggers)
- [API reference](https://docs.stripe.com/cli/fixtures)