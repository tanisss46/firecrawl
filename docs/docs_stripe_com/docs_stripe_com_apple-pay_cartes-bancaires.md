# Cartes Bancaires with Apple Pay

## Learn how to integrate Cartes Bancaires with Apple Pay.

#### Note

Stripe only supports EUR payments for Cartes Bancaires with Apple Pay.

Use this guide to enable the [Cartes
Bancaires](https://docs.stripe.com/payments/cartes-bancaires) payment method in
your Apple Pay integration.

iOSWeb
## Before you begin

To avoid issues with failed payments, take the following steps:

- Add Cartes Bancaires to your list of enabled networks only if the transaction
is in Euros.
- Only enable Cartes Bancaires with Apple Pay if you support charges through
Cartes Bancaires.
- If you’re a platform using the
[on_behalf_of](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-on_behalf_of)
parameter, make sure that the `on_behalf_of` account supports Cartes Bancaires
charges. Check an account’s eligibility using the [Capabilities
API](https://docs.stripe.com/api/capabilities).
[Set up Stripe](https://docs.stripe.com/apple-pay/cartes-bancaires#ios-setup)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

[Accept Apple
Pay](https://docs.stripe.com/apple-pay/cartes-bancaires#ios-accept-apple-pay)
Follow the [Apple Pay guide](https://docs.stripe.com/apple-pay?platform=ios) to
start accepting Apple Pay.

[Add Cartes Bancaires as an enabled
network](https://docs.stripe.com/apple-pay/cartes-bancaires#ios-add-cartes-bancaires-to-enabled-networks)
When your app starts, configure the SDK with Cartes Bancaires as an enabled
Apple Pay network.

```
StripeAPI.additionalEnabledApplePayNetworks = [.cartesBancaires]
```

[Test Apple
Pay](https://docs.stripe.com/apple-pay/cartes-bancaires#ios-test-apple-pay)
Apple Pay Wallet can’t save Stripe test card information. Instead, Stripe
recognizes when you’re using your test API keys and provides a successful test
card token for you to use. This allows you to make test payments using a live
card without any charges being applied.

Make sure you test using a Cartes Bancaires card obtained from one of the [Apple
Pay participating banks](https://support.apple.com/en-us/109516).

## Links

- [Cartes Bancaires](https://docs.stripe.com/payments/cartes-bancaires)
-
[on_behalf_of](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-on_behalf_of)
- [Capabilities API](https://docs.stripe.com/api/capabilities)
- [Register now](https://dashboard.stripe.com/register)
- [Apple Pay guide](https://docs.stripe.com/apple-pay?platform=ios)
- [Apple Pay participating banks](https://support.apple.com/en-us/109516)