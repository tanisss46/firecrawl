# Decide between test mode and Sandboxes

## Learn about the differences between test mode and Sandboxes to help choose the most suitable environment for you.

Test mode and Sandboxes are testing environments that simulate creating real
objects without the risk of affecting real transactions or moving actual money.
Understanding when to use each can help you build your testing strategy.

We recommend that you continue using test mode if it meets your requirements;
however, if you benefit from the additional functionality that Sandboxes
provide, you can transition to using Sandboxes to enhance your testing
capabilities.

View the table below to understand the differences and choose the most suitable
environment for your needs.

Test modeSandboxesNumber of environmentsUse one environmentUse up to five
environmentsAccess controlGrant all users with roles the same roles and
access.Exercise granular control over access. Only admins automatically have
access. Invite users to sandboxes only, without access to live
mode.SettingsShare settings between live mode and test mode. You can’t test many
settings independently.Isolate settings completely for each sandbox. 
settings from live mode at creation time, and test independently from your live
integration.Product limitationsYou can’t test
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
pricing in a sandbox.You can’t test
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
pricing or [Issuing](https://docs.stripe.com/issuing), use
[Sigma](https://stripe.com/sigma), or install [Stripe
Apps](https://docs.stripe.com/stripe-apps) in a sandbox.Version supportSupports
V1 onlySupports V1 and V2 (including products such as [Usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based) and [Event
Destinations](https://docs.stripe.com/event-destinations)).Rate limitsKeep the
same between bothKeep the same between bothTest card numbersKeep the same
between bothKeep the same between both
## See also

- [Test mode and use cases](https://docs.stripe.com/test-mode)
- [Sandboxes use cases](https://docs.stripe.com/sandboxes#use-cases)

## Links

-
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
- [Issuing](https://docs.stripe.com/issuing)
- [Sigma](https://stripe.com/sigma)
- [Stripe Apps](https://docs.stripe.com/stripe-apps)
- [Usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based)
- [Event Destinations](https://docs.stripe.com/event-destinations)
- [Test mode and use cases](https://docs.stripe.com/test-mode)
- [Sandboxes use cases](https://docs.stripe.com/sandboxes#use-cases)