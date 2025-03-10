# Set up your integration

## Set up a Stripe Terminal SDK or server-driven integration to accept in-person payments.

Server-drivenJavaScriptiOSAndroidReact NativeApps on Devices
Server-driven integrations use the Stripe API instead of a Terminal SDK to
connect to [WisePOS E or Stripe Reader S700 smart
readers](https://docs.stripe.com/terminal/smart-readers) and collect in-person
payments. This allows you to:

- Use Terminal even if your infrastructure doesn’t support iOS, Android, or
JavaScript SDKs
- Build a Terminal integration that’s powered by your custom middleware or
cloud-based infrastructure
- Integrate any device including a .NET-based point of sale to Terminal
- Improve reader network connections using an internet connection instead of the
local area network
- Make curl requests to prototype an integration

Server-driven integration doesn’t support:

- [Stripe Terminal mobile
readers](https://docs.stripe.com/terminal/mobile-readers)
- [Collect card payments while
offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments)

You can start your server-driven integration with the following components:

- **Your point of sale application**: The operator-facing UI that employees see
when creating a transaction.
- **Your backend infrastructure**: Mediates requests from your point of sale
application and makes requests to the Stripe API during the transaction.
- **The Stripe API**: Receives requests and forwards them to a smart reader,
such as the [BBPOS WisePOS E
reader](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e)
or [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700). Stripe also
sends [webhooks](https://docs.stripe.com/webhooks) to your backend
infrastructure with the payment status.
- **A BBPOS WisePOS E reader, Stripe Reader S700, or simulated reader**: Prompts
the cardholder for payment and communicates with Stripe and our financial
infrastructure to process the payment. You can create a simulated reader if you
don’t yet have a physical reader.

![Server-driven integration
architecture](https://b.stripecdn.com/docs-statics-srv/assets/server-driven-integration-architecture.a8499c1169a540cef98c9dd539f99a61.png)

## See also

- [Connect to a
reader](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=server-driven&reader-type=internet)

## Links

- [WisePOS E or Stripe Reader S700 smart
readers](https://docs.stripe.com/terminal/smart-readers)
- [Stripe Terminal mobile
readers](https://docs.stripe.com/terminal/mobile-readers)
- [Collect card payments while
offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments)
- [BBPOS WisePOS E
reader](https://docs.stripe.com/terminal/payments/setup-reader/bbpos-wisepos-e)
- [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700)
- [webhooks](https://docs.stripe.com/webhooks)
- [Connect to a
reader](https://docs.stripe.com/terminal/payments/connect-reader?terminal-sdk-platform=server-driven&reader-type=internet)