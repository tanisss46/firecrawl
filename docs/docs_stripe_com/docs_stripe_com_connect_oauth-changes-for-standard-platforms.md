# OAuth changes for platform-controlled Standard accounts

## Learn about the changes Stripe has made to OAuth for Connect.

We’ve updated OAuth to isolate platforms’ processing activity on
platform-controlled Standard accounts. Platforms using OAuth with `read_write`
scope can’t connect to Standard accounts that are controlled by another
platform. Prior to June 2021, multiple platforms could connect to the same
Standard account.

This change ensures that in the rare case that a
[Connect](https://docs.stripe.com/connect) user with access to the Stripe
Dashboard interacts with two platforms, each platform’s activity is kept
distinct in separate Standard accounts.

When a user of a Standard account controlled by another platform connects to
your platform, the Connect onboarding flow directs them to create a separate
Standard account to use with your platform. The new account automatically
connects to your platform.

If you registered your Connect application as an [Extension
integration](https://docs.stripe.com/building-extensions), it can still connect
to accounts that are connected to another platform. Extensions need to connect
to existing Standard accounts that might also be connected to another Platform
or Extension. Only Extensions can use `read_only`, which ensures that platforms
can’t read other applications’ data.

However, if you previously selected `Platform` for your Connect application and
you now need Extension functionality, you must [contact
us](https://support.stripe.com/contact/email?topic=connect) to modify your
integration selection. You can find your selection in the [Connect
Settings](https://dashboard.stripe.com/settings/connect/platform-profile) under
**Availability**.

## Links

- [configured with
properties](https://docs.stripe.com/connect/update-to-typeless-connect)
- [platform
controls](https://docs.stripe.com/connect/platform-controls-for-standard-accounts)
- [Connect](https://docs.stripe.com/connect)
- [Extension integration](https://docs.stripe.com/building-extensions)
- [contact us](https://support.stripe.com/contact/email?topic=connect)
- [Connect
Settings](https://dashboard.stripe.com/settings/connect/platform-profile)