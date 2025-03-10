# Tap to Pay in the Dashboard mobile app

## Use the Stripe Dashboard mobile app to accept in-person, contactless payments.

Process in-person, contactless payments using only your phone with [Tap to
Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay) with
Stripe Terminal. You don’t need to buy any hardware or write any code. To get
started accepting payments with Tap to Pay, download the Stripe Dashboard mobile
app on
[iOS](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-mobile-app-ttp-doc-page&mt=8)
or
[Android](https://play.google.com/store/apps/details?id=com.stripe.android.dashboard)
and log in with your Stripe account.

## Before you begin

Before you start setting up Tap to Pay, make sure that you meet the requirements
below and operate in a supported country.

If you’re new to Stripe, [set up and activate a new
account](https://dashboard.stripe.com/register/) before downloading the
Dashboard mobile app.

Good forIn-person payments without your own app or terminalPricing[Pay-as-you-go
for Terminal and Tap to Pay](https://stripe.com/pricing)Compatible
withContactless cards (Visa, MC, Amex, Discover) and NFC mobile wallets (Apple
Pay, Google Pay, Samsung Pay)
**Download the app**

The Stripe Dashboard app is available in the App Store and Google Play:

- [Download the iOS app from the App
Store](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-mobile-app-ttp-doc-page&mt=8)
- [Download Android app on Google
Play](https://play.google.com/store/apps/details?id=com.stripe.android.dashboard)
Requirements- [Stripe account](https://docs.stripe.com/get-started/account)
- Stripe
[iOS](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-mobile-app-ttp-doc-page&mt=8)
or
[Android](https://play.google.com/store/apps/details?id=com.stripe.android.dashboard)
Dashboard app
- Location permissions enabled
- **iOS:** iPhone XS or later. The device must have a passcode set and be signed
into iCloud. Reference [country
availability](https://docs.stripe.com/no-code/tap-to-pay#ios-availability) for
OS requirements.
- **Android:** A [supported Android
device](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=android#supported-devices)
Supported countries
The Stripe Dashboard app is available on iOS and Android in the following
countries.

### iOS country availability

#### Note

Tap to Pay on iOS isn’t available in Puerto Rico.

##### iOS 16.7+

AustraliaUnited KingdomUnited States
##### iOS 17.0+

FranceItalyNetherlands
##### iOS 17.4+

AustriaCanadaCzech RepublicGermanyIrelandNew ZealandSweden
### Android country availability

AustraliaAustriaBelgiumCanadaCzech
RepublicDenmarkFinlandFranceGermanyIrelandItalyLuxembourgMalaysiaNetherlandsNew
ZealandNorwayPolandPortugalSingaporeSpainSwedenSwitzerlandUnited KingdomUnited
States
## Accept a Tap to Pay contactless payment

#### Enable NFC

Before accepting Tap to Pay contactless payments, you must enable NFC on your
mobile device.

- Open your Stripe Dashboard mobile app.
- Tap the add symbol () from any tab.
- Select **Charge a card or send an invoice**.
- Enter the amount to charge.
- Select **Tap to Pay** as your payment acceptance option.
- When the Tap to Pay symbol appears, prompt your customer to tap their card to
the device by following the instructions on screen.
- The payment confirmation page signals successful completion of the
transaction.

## Other ways to accept in-person payments

If you’re unable to accept a Tap to Pay payment in the Dashboard app, you have
other options:

- **Manually charge a card**: Open the Stripe Dashboard app, click the add
symbol () from any tab, and select **Charge a card or send an invoice**. Then,
enter your customer’s card information manually.
- **iOS only: Generate a QR code**: Create a [payment
link](https://docs.stripe.com/no-code/payment-links) and have your customer scan
the QR code to pay. You can also [share a payment
link](https://docs.stripe.com/payment-links/share) through text, email, and
other channels.

#### For developers

If you’re looking to build Tap to Pay functionality into your mobile app, see
the [Tap to Pay integration
guide](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay).

## Charge limits

Maximum and minimum limits on charge amounts apply when accepting payments. For
more information on limits, see [Minimum and maximum charge
amounts](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts).

## Links

- [Tap to
Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay)
-
[iOS](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-mobile-app-ttp-doc-page&mt=8)
-
[Android](https://play.google.com/store/apps/details?id=com.stripe.android.dashboard)
- [set up and activate a new account](https://dashboard.stripe.com/register/)
- [Pay-as-you-go for Terminal and Tap to Pay](https://stripe.com/pricing)
- [Stripe account](https://docs.stripe.com/get-started/account)
- [supported Android
device](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay?platform=android#supported-devices)
- [payment link](https://docs.stripe.com/no-code/payment-links)
- [share a payment link](https://docs.stripe.com/payment-links/share)
- [Minimum and maximum charge
amounts](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts)