# Supports domain registration for Amazon Pay

## What’s new

Adds an `amazon_pay` property to the [Payment Method
Domain](https://docs.stripe.com/api/payment_method_domains) resource.

When you [retrieve a payment method
domain](https://docs.stripe.com/api/payment_method_domains/retrieve), the
`amazon_pay` property reflects the domain activation status for Amazon Pay.

## Impact

To use Amazon Pay with [Elements](https://docs.stripe.com/payments/elements) or
[Checkout’s embeddable payment
form](https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=embedded-form),
you must register every web domain that will show the payment method, including
top-level domains and subdomains. After you register a domain, you can use that
domain with any other payment methods that you enable in the future.

You can now register your domain using the [Payment Method Domain
API](https://docs.stripe.com/payments/payment-methods/pmd-registration).

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointsamazon_payAdded[PaymentMethodDomain](https://docs.stripe.com/api/payment_method_domains/object)
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-10-28.acacia`
- Upgrade the API version used for [webhook
endpoints](https://docs.stripe.com/webhooks/versioning).
- [Test your integration](https://docs.stripe.com/testing) against the new
version.
- If you use Connect, [test your Connect
integration](https://docs.stripe.com/connect/testing).
- In Workbench, [perform the
upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade). You can [roll
back the version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades).

## Related changes

- [Adds a metadata field to the Vault and Forward
API](https://docs.stripe.com/changelog/acacia/2024-10-28/forwarding-api-metadata-field)
- [Adds Polish PLN currency support to Terminal tipping
configuration](https://docs.stripe.com/changelog/acacia/2024-10-28/terminal-tipping-pln)

## Links

- [Payment Method Domain](https://docs.stripe.com/api/payment_method_domains)
- [retrieve a payment method
domain](https://docs.stripe.com/api/payment_method_domains/retrieve)
- [Elements](https://docs.stripe.com/payments/elements)
- [Checkout’s embeddable payment
form](https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=embedded-form)
- [Payment Method Domain
API](https://docs.stripe.com/payments/payment-methods/pmd-registration)
-
[PaymentMethodDomain](https://docs.stripe.com/api/payment_method_domains/object)
- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
- [API requests](https://docs.stripe.com/api/versioning)
- [webhook endpoints](https://docs.stripe.com/webhooks/versioning)
- [Test your integration](https://docs.stripe.com/testing)
- [test your Connect integration](https://docs.stripe.com/connect/testing)
- [perform the upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade)
- [roll back the
version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
- [Stripe API upgrades](https://docs.stripe.com/upgrades)
- [Adds a metadata field to the Vault and Forward
API](https://docs.stripe.com/changelog/acacia/2024-10-28/forwarding-api-metadata-field)
- [Adds Polish PLN currency support to Terminal tipping
configuration](https://docs.stripe.com/changelog/acacia/2024-10-28/terminal-tipping-pln)