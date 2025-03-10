# Test your integration with test clocks

## Learn how to move Billing objects through time in test mode.

## Overview

Test clocks help you test your Billing integration and make sure it behaves as
designed. When you use test clocks you simulate the forward movement of time in
[test mode](https://docs.stripe.com/test-mode), which causes Billing resources,
like Subscriptions, to change state and trigger
[webhook](https://docs.stripe.com/webhooks) events. This means that, for
example, you don’t have to wait a year to see how your integration handles a
payment failure for a quarterly or annual renewal.

Here are some other things you can do with test clocks:

- Test complex simulations such as upgrading or changing plans mid-cycle.
- Ensure your integration processes Billing lifecycle webhooks correctly.
- Validate that your app handles trials correctly.
- Build and test multi-phase subscription schedules.

## How to use test clocks

[Simulate subscriptionsLearn how to simulate subscriptions in test
mode.](https://docs.stripe.com/billing/testing/test-clocks/simulate-subscriptions)[API
and advanced usageLearn advanced strategies for using test clocks in the
Dashboard and
API.](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage)

## Links

- [test mode](https://docs.stripe.com/test-mode)
- [webhook](https://docs.stripe.com/webhooks)
- [Simulate subscriptionsLearn how to simulate subscriptions in test
mode.](https://docs.stripe.com/billing/testing/test-clocks/simulate-subscriptions)
- [API and advanced usageLearn advanced strategies for using test clocks in the
Dashboard and
API.](https://docs.stripe.com/billing/testing/test-clocks/api-advanced-usage)