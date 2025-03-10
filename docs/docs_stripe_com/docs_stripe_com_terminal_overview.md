# Accept in-person payments with Terminal

## Learn how Terminal works.

With [Stripe Terminal](https://docs.stripe.com/terminal), you can integrate
Stripe payments into your existing in-person checkout flow or build in-person
payments into your native mobile or web-based application.

Terminal comes with SDKs built for modern development environments, Tap to Pay
on
[iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=ios)
and
[Android](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=android),
[pre-certified readers](https://docs.stripe.com/terminal/payments/setup-reader),
and tools for ordering and managing readers from the Stripe Dashboard. Build a
SaaS platform or marketplace using [Connect](https://docs.stripe.com/connect) or
initiate subscriptions in-store with [Billing](https://docs.stripe.com/billing).

Stripe Terminal is available in the following countries:

### Availability

AustraliaAustriaBelgiumCanadaCzech
RepublicDenmarkFinlandFranceGermanyIrelandItalyLuxembourgMalaysiaNetherlandsNew
ZealandNorwayPortugalSingaporeSpainSwedenSwitzerlandUnited KingdomUnited States
### Available in Preview

Poland
You can only collect payments in your local currency with [supported card
brands](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands).
Stripe Terminal offers pre-certified readers and Tap to Pay, which allows users
to accept in-person contactless payments with a compatible
[iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=ios)
or
[Android](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=android)
device and the Stripe Terminal SDK. Hardware must be shipped to physical
addresses (not PO boxes). If you’re outside the available countries, you can
[request an invite](https://stripe.com/terminal#request-invite) to test
Terminal.

## Features

Use Terminal to take the complexity out of in-person payments:

- **Online compatibility**: Unify your online and in-person payments in a single
system.
- **Flexible SDKs**: Use Terminal’s JavaScript, iOS, Android, or React Native
SDK to integrate your existing point of sale (POS), or build a modern POS
tailored to your business. Use the [server-driven
integration](https://support.stripe.com/questions/terminal-server-driven-integration)
to integrate directly using the Stripe API.
- **Reader choices**: Choose from [different
readers](https://docs.stripe.com/terminal/payments/setup-reader) depending on
your business needs.
- **Connection types**:
[Connect](https://docs.stripe.com/terminal/payments/connect-reader) to your
Terminal reader with Bluetooth, USB (Android with mobile readers only), or
internet, depending on your physical sales environment.
- **Ordering and fleet management from the Stripe Dashboard**: Order
[pre-certified
readers](https://docs.stripe.com/terminal/fleet/order-and-return-readers) and
[monitor your fleet of
readers](https://docs.stripe.com/terminal/fleet/locations-and-zones) from the
Stripe Dashboard.

## How Terminal works

A Stripe Terminal deployment consists of four main components:

- Your web-based, mobile, or desktop application
- Your backend
- A Stripe Terminal reader
- The Stripe Terminal SDK

The SDK facilitates communication between your point of sale application logic,
the firmware running on the reader, and the Stripe API so you can accept
in-person payments in the same way as you accept online payments with Stripe.
The SDK is available for JavaScript, iOS, Android applications. You can develop
desktop applications using a server-driven integration.

!

Stripe Terminal offers a selection of [pre-certified
readers](https://docs.stripe.com/terminal/payments/setup-reader) that accept
payment details (EMV, contactless, and swiped), encrypt sensitive card
information, and return a token to your application (through the Stripe Terminal
SDK) so you can confirm payment.

Stripe Terminal works only with our pre-certified card readers and compatible
Tap to Pay
[iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=ios)
and
[Android](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=android)
devices. This ensures secure transactions by our end-to-end encryption, by
default, and up-to-date readers through our remote management tools.

You can [order readers and
accessories](https://docs.stripe.com/terminal/fleet/order-and-return-readers)
from the Stripe Dashboard and get them shipped to a location of your choice. As
a [Connect](https://docs.stripe.com/connect) platform, you can even enable your
connected accounts to receive readers and accessories at their business
location.

## Use cases

Stripe Terminal is built with developers in mind. Its flexible design supports a
wide range of use cases:

- Extend your online business to the physical world.
- Enable in-person payments for your [Connect](https://docs.stripe.com/connect)
platform, with readers for each connected account.
- Collect payments in-person and use those card details for recurring online
payments with [Billing](https://docs.stripe.com/billing).
- Build a new, customized point of sale application or integrate with your
existing point of sale application, while taking advantage of the Stripe API for
processing payments.

Choose an SDK that works best for you and combine it with a reader that works
best for you. This documentation provides all the information you need to design
your in-person payments solution, order readers and accessories, integrate, and
deploy.

## Scope of integration

The full scope of an integration consists of four major steps.

- Use the [sample integration](https://docs.stripe.com/terminal/quickstart) to
get up and running with an integration quickly.
- [Design your
integration](https://docs.stripe.com/terminal/designing-integration) to create
in-person payments.
- [Integrate the
SDK](https://docs.stripe.com/terminal/payments/setup-integration) in your
application. Use the simulated reader to emulate reader behavior for all the
Terminal flows while building your initial integration.
- [Order](https://docs.stripe.com/terminal/fleet/order-and-return-readers) a
physical reader and test card.

From there, explore the docs to see all you can do with your Terminal
integration. We recommend [testing your
integration](https://docs.stripe.com/terminal/references/testing) and reviewing
the [checklist](https://docs.stripe.com/terminal/references/checklist) before
going live.

## See also

- [Design an
integration](https://docs.stripe.com/terminal/designing-integration)
- [Sample integration](https://docs.stripe.com/terminal/quickstart)
- [Supported card
brands](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands)

## Links

- [no-code POS solutions](https://stripe.partners/?f_category=point-of-sale)
- [Stripe Terminal](https://docs.stripe.com/terminal)
-
[iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=ios)
-
[Android](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=android)
- [pre-certified
readers](https://docs.stripe.com/terminal/payments/setup-reader)
- [Connect](https://docs.stripe.com/connect)
- [Billing](https://docs.stripe.com/billing)
- [supported card
brands](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands)
- [request an invite](https://stripe.com/terminal#request-invite)
- [server-driven
integration](https://support.stripe.com/questions/terminal-server-driven-integration)
- [Connect](https://docs.stripe.com/terminal/payments/connect-reader)
- [pre-certified
readers](https://docs.stripe.com/terminal/fleet/order-and-return-readers)
- [monitor your fleet of
readers](https://docs.stripe.com/terminal/fleet/locations-and-zones)
- [sample integration](https://docs.stripe.com/terminal/quickstart)
- [Design your
integration](https://docs.stripe.com/terminal/designing-integration)
- [Integrate the
SDK](https://docs.stripe.com/terminal/payments/setup-integration)
- [testing your
integration](https://docs.stripe.com/terminal/references/testing)
- [checklist](https://docs.stripe.com/terminal/references/checklist)