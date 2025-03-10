# Design an integration

## Choose a reader and platform and see how they work together.

Country:AustraliaAustriaBelgiumCanadaCzech
RepublicDenmarkGermanyFinlandFranceIrelandItalyLuxembourgMalaysiaNetherlandsNew
ZealandNorwayPolandPortugalSingaporeSpainSwedenSwitzerlandUnited KingdomUnited
StatesReader:Stripe Reader S700WisePOS EReader M2Architecture:JavaScript SDKiOS
SDKAndroid SDKServer-drivenReact Native SDK
## S700 reader

- All-in-one, Android-based smart reader that can run your custom POS
- For handheld or countertop use; optional dock available for mounted or
countertop use cases
- Contactless, chip, and swipe payments

## Use it in a server-driven integration

- Write your point-of-sale app for any device.
- Access Stripe features using the Stripe API.
- Communicate with the reader using Stripe and your server.

### Limitations

Server-driven integration doesn’t support:

- [Bluetooth
readers](https://docs.stripe.com/terminal/features/mail-telephone-orders/overview)
- [Collect payments while
offline](https://docs.stripe.com/terminal/features/operate-offline/overview?reader-type=internet)

If you don’t write code, you can [find a Stripe partner who supports
Terminal](https://stripe.com/partners/directory?p=Terminal).

## Architecture

In a server-driven integration, your POS device connects to your server. Your
server then makes [Stripe API](https://docs.stripe.com/api) calls, and Stripe
updates the reader and returns the result.

The structure of the integration looks like this:

![Server-driven integration
architecture](https://b.stripecdn.com/docs-statics-srv/assets/server-driven-smart-reader.b78805eff2f4081c889aebbef6d8a3e3.png)

You can build a working example of an integration like this using the [Terminal
Quickstart](https://docs.stripe.com/terminal/quickstart).

## Organize readers and locations

Before you connect a reader to a Terminal integration, you must create one or
more [Locations](https://docs.stripe.com/api/terminal/locations), either [in the
Dashboard](https://dashboard.stripe.com/terminal/locations) or [using the
API](https://docs.stripe.com/terminal/fleet/locations-and-zones#create-locations-and-zones).
When you [connect to your
reader](https://docs.stripe.com/terminal/payments/connect-reader), specify one
of those locations.

Locations represent physical places where your readers operate. Stripe needs
location information to process payments correctly and keep your reader up to
date. If your business requires you to move your readers frequently, your
locations can use addresses that represent a primary place of business.

## Prototyping

When you first begin writing your application, you can test it with a simulated
reader and simulated cards. The [Terminal
Quickstart](https://docs.stripe.com/terminal/quickstart) demonstrates an app at
this stage of development.

When you’re ready to work with actual hardware,

- [Order a reader and physical test
cards](https://dashboard.stripe.com/terminal/shop).
- [Connect to the reader over the
internet](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet).
- [Test your logic with the test
cards](https://docs.stripe.com/terminal/references/testing#physical-test-cards).

## Next steps

- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration) to
start writing code.
- See the [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart) for
a full code example.
- [Order readers, accessories, and test
cards](https://dashboard.stripe.com/terminal/shop) when you’re ready to work
with physical hardware.

## Links

-
[Pricing](https://docs.stripe.com/terminal/fleet/order-and-return-readers#pricing)
- [Reader
instructions](https://docs.stripe.com/terminal/readers/stripe-reader-s700)
- [Product sheet](https://stripe.com/s700/manual)
- [Order readers and accessories](https://dashboard.stripe.com/terminal/shop)
- [Bluetooth
readers](https://docs.stripe.com/terminal/features/mail-telephone-orders/overview)
- [Collect payments while
offline](https://docs.stripe.com/terminal/features/operate-offline/overview?reader-type=internet)
- [find a Stripe partner who supports
Terminal](https://stripe.com/partners/directory?p=Terminal)
- [Stripe API](https://docs.stripe.com/api)
- [Terminal Quickstart](https://docs.stripe.com/terminal/quickstart)
- [Locations](https://docs.stripe.com/api/terminal/locations)
- [in the Dashboard](https://dashboard.stripe.com/terminal/locations)
- [using the
API](https://docs.stripe.com/terminal/fleet/locations-and-zones#create-locations-and-zones)
- [connect to your
reader](https://docs.stripe.com/terminal/payments/connect-reader)
- [Connect to the reader over the
internet](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet)
- [Test your logic with the test
cards](https://docs.stripe.com/terminal/references/testing#physical-test-cards)
- [Set up your
integration](https://docs.stripe.com/terminal/payments/setup-integration)