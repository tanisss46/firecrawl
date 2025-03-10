# Design a multiparty platform

## Design a Terminal integration with your business serving as a central platform.

Stripe Terminal is fully compatible with [Stripe
Connect](https://docs.stripe.com/connect), enabling your platform or marketplace
to accept in-person payments. If you aren’t familiar with Stripe Connect, we
recommend going through the [Connect
overview](https://docs.stripe.com/connect/how-connect-works).

There are two options for integrating Terminal with Connect, depending on [the
account type you choose](https://docs.stripe.com/connect/accounts) for your
platform’s connected accounts. To decide which option best suits your business’s
needs, refer to the following table:

Custom or ExpressStandardWho owns the API resources?PlatformConnected
accountsWho has access to [the Terminal hardware ordering dashboard and
APIs](https://docs.stripe.com/terminal/fleet/order-and-return-readers)?PlatformConnected
accountsWhich [charge types](https://docs.stripe.com/connect/charges#types) can
I use?- [Destination
charges](https://docs.stripe.com/connect/destination-charges)
- [Separate
charges/transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Direct charges](https://docs.stripe.com/connect/direct-charges)

## Express or Custom Connect

In a Connect integration with Express or Custom accounts, all API resources
belong to the platform account. As needed, you can associate Terminal objects
like [Readers](https://docs.stripe.com/api/terminal/readers) and
[Locations](https://docs.stripe.com/api/terminal/locations) with a particular
connected account by including them in the
[metadata](https://docs.stripe.com/api/metadata) object on these resources.

!

When processing payments, you specify the connected account as the destination
for the funds using the `on_behalf_of`, `transfer_data[destination]`, and
`application_fee_amount` parameters. This creates a transfer to the connected
account automatically and establishes the connected account as the merchant of
record.

## Standard Connect

In a Connect integration with Standard accounts, all API resources belong to
individual connected accounts. When making API requests such as for creating
locations, readers, and payments, you pass the connected account ID in the
`Stripe-Account` header. This tells Stripe that the request is effectively being
made by the connected account.

!

When processing payments, you also pass the connected account’s ID in the
`Stripe-Account` header, which creates the charge directly on the connected
account.

## Next steps

- [Build a sample integration](https://docs.stripe.com/terminal/quickstart)

## Links

- [Stripe Connect](https://docs.stripe.com/connect)
- [Connect overview](https://docs.stripe.com/connect/how-connect-works)
- [the account type you choose](https://docs.stripe.com/connect/accounts)
- [the Terminal hardware ordering dashboard and
APIs](https://docs.stripe.com/terminal/fleet/order-and-return-readers)
- [charge types](https://docs.stripe.com/connect/charges#types)
- [Destination charges](https://docs.stripe.com/connect/destination-charges)
- [Separate
charges/transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Direct charges](https://docs.stripe.com/connect/direct-charges)
- [Readers](https://docs.stripe.com/api/terminal/readers)
- [Locations](https://docs.stripe.com/api/terminal/locations)
- [metadata](https://docs.stripe.com/api/metadata)
- [Build a sample integration](https://docs.stripe.com/terminal/quickstart)