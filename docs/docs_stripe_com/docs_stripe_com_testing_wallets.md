# Test Apple and Google wallet rendering

## Compare your integration against working demo integrations to identify possible rendering issues.

The following demo shows different Stripe payment integrations with Apple Pay
and Google Pay set up. Use the demo to visually compare how these wallets
display in the demo integrations and your own integration.

- If the Apple Pay and Google Pay payment options appear as expected and in both
the demo and your integration, they’re configured correctly.
- If you have a valid wallet, but you don’t see it as a payment method option in
the demo, [adjust your device and browser
setup](https://docs.stripe.com/testing/wallets#device-requirements) until Apple
Pay and Google Pay appear as expected.
- If you see your wallet displayed in the demos but not in your own integration,
[check your
integration](https://docs.stripe.com/testing/wallets#integration-requirements).
Payment ElementExpress Checkout ElementCheckout SessionsPayment Request
ButtonLegacyThis demo only displays Google Pay or Apple Pay if you have an
active card with either wallet.
For this integration path, Stripe.js detects and supports the following wallets
based on the state of your device.

```
{  applePay: false  googlePay: false}
```

## Check your device and browser setup

If you can’t see your expected wallet in the demos, your device or browser might
not meet the following Apple Pay or Google Pay conditions.

- The wallet must have at least one card.
- You must use a compatible [Apple Pay
device](https://support.apple.com/en-us/102896) and [Google Pay
device](https://developers.google.com/pay/issuers/overview/supported-devices#compatibility_requirements).
- You must use a [supported
version](https://docs.stripe.com/js/appendix/supported_browsers) of a [supported
browser](https://docs.stripe.com/stripe-js/elements/payment-request-button?client=html#testing)
for the wallet you’re testing.
#### Note

This integration relies on the [Payment Request
API](https://developer.mozilla.org/en-US/docs/Web/API/Payment_Request_API),
which Android WebViews doesn’t support.
- Allow applicable browsers to access your wallet.- Chrome: **Settings** >
**Autofill and passwords** > **Payment methods** > **Allow sites to check if you
have payment methods saved**
- Safari: **Settings** > **Advanced** > **Allow websites to check for Apple Pay
and Apple card**
- Don’t use a Chrome incognito window or Safari private window.
- Confirm you’re operating from a supported [Apple Pay
region](https://support.apple.com/en-us/102775) and [Google Pay
region](https://support.google.com/wallet/answer/12060037?sjid=7404612469520417090-NA#zippy=%2Cuse-google-wallet-for-payments).
- Stripe doesn’t display Apple Pay or Google Pay for IP addresses in India.
- For Apple Pay, confirm your device supports [biometric
authentication](https://support.apple.com/en-us/102626#:~:text=iPhone%20or%20.iPad,on%20all%20devices.).

## Check your integration

If you see the expected wallet payment methods in the demo payment forms, but
they don’t display in your own integration, the following checkpoints might
resolve the issue.

### Register your domains

Check your [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_method_domains) to
confirm your domain registrations. You must [register every domain and
sub-domain](https://docs.stripe.com/payments/payment-methods/pmd-registration?dashboard-or-api=dashboard#register-your-domain)
separately for each environment, including live mode and each
[sandbox](https://docs.stripe.com/sandboxes).

Connect users must also consider the funds flow configuration (direct or
destination charge) for correct [domain
registration](https://docs.stripe.com/payments/payment-methods/pmd-registration?dashboard-or-api=dashboard#register-your-domain-while-using-connect).

### (Apple Pay) Register all domains when using iframes

To see Apple Pay in an integration using iframes you must:

- Make sure the iframe and top-level site domains match if you support
pre-Safari 17 browser versions.
- Set the `allow="payment"` attribute on the iframe.
- Register both the iframe domain and top-level domain of the site, if they’re
different (supported by Safari 17 or later).

### Enable wallets for your integration

- Enable supported wallets in your [Payment Method
Configurations](https://dashboard.stripe.com/test/settings/payment_methods) to
make sure [Dynamic Payment
Methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
can render them.
- To manually specify wallet payment methods, include `payment_method_types=
['card']` when:- [Creating the payment
intent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
- [Initializing
Elements](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodTypes)
from your client to collect payment details [before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred).

## Links

- [Apple Pay device](https://support.apple.com/en-us/102896)
- [Google Pay
device](https://developers.google.com/pay/issuers/overview/supported-devices#compatibility_requirements)
- [supported version](https://docs.stripe.com/js/appendix/supported_browsers)
- [supported
browser](https://docs.stripe.com/stripe-js/elements/payment-request-button?client=html#testing)
- [Payment Request
API](https://developer.mozilla.org/en-US/docs/Web/API/Payment_Request_API)
- [Apple Pay region](https://support.apple.com/en-us/102775)
- [Google Pay
region](https://support.google.com/wallet/answer/12060037?sjid=7404612469520417090-NA#zippy=%2Cuse-google-wallet-for-payments)
- [biometric
authentication](https://support.apple.com/en-us/102626#:~:text=iPhone%20or%20.iPad,on%20all%20devices.)
- [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_method_domains)
- [register every domain and
sub-domain](https://docs.stripe.com/payments/payment-methods/pmd-registration?dashboard-or-api=dashboard#register-your-domain)
- [sandbox](https://docs.stripe.com/sandboxes)
- [domain
registration](https://docs.stripe.com/payments/payment-methods/pmd-registration?dashboard-or-api=dashboard#register-your-domain-while-using-connect)
- [Payment Method
Configurations](https://dashboard.stripe.com/test/settings/payment_methods)
- [Dynamic Payment
Methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Creating the payment
intent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
- [Initializing
Elements](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-paymentMethodTypes)
- [before creating an
Intent](https://docs.stripe.com/payments/accept-a-payment-deferred)