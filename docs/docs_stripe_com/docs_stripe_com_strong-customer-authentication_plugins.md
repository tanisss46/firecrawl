# SCA migration guide for plugins and developer libraries

## Learn how to update your Stripe plugin or developer library to support Strong Customer Authentication (SCA).

#### Note

This [SCA](https://docs.stripe.com/strong-customer-authentication) guide is
designed for developers of Stripe plugins or libraries. If you’re a Stripe user
looking for an SCA-ready plugin, visit [Stripe
Partners](https://stripe.com/partners/sca-ready).

## Do I need to support SCA for my users?

Businesses in the [European Economic
Area](https://en.wikipedia.org/wiki/European_Economic_Area) (EEA) that accept
online payments from customers in the EEA require you to use [3D
Secure](https://docs.stripe.com/payments/3d-secure). Transactions that don’t
follow these authentication guidelines might be declined by a customer’s bank,
as of September 14th, 2019. This additional layer of authentication requires
migrating to SCA-ready solutions like
[Checkout](https://docs.stripe.com/payments/checkout) or [Payment
Intents](https://docs.stripe.com/payments/payment-intents).

[Identify your plugin on our
platform](https://docs.stripe.com/strong-customer-authentication/plugins#identify-plugin)
Plugins and third-party libraries should include identifying information so we
can contact you about future changes or critical updates to the API. Use the
[setAppInfo function](https://docs.stripe.com/building-plugins#setappinfo) to
provide those details in your Stripe integration.

We encourage you to join the [Stripe Partner
Program](https://stripe.com/partner-program?utm_campaign=partnerprogram&utm_source=sca-plugins-guide),
which includes [free
registration](https://stripe.com/partner-program?utm_campaign=partnerprogram&utm_source=sca-plugins-guide&utm_medium=join#stripe-partner-program)
and more resources for developers building plugins. Learn more about [suggested
best practices](https://docs.stripe.com/building-plugins).

[Determine your integration
path](https://docs.stripe.com/strong-customer-authentication/plugins#determine-integration)
For developers of plugins or libraries:

- **Choose Stripe Checkout when possible.** Checkout is a low-code integration
that lets you collect payments using a customizable form. You can embed the
payment form on your website or host it on Stripe. To learn more about this
payment integration option, see [Stripe
Checkout](https://docs.stripe.com/payments/checkout).
- **For more control over your checkout flow, use the Payment Intents and Setup
Intents APIs.** These APIs work with
[Elements](https://docs.stripe.com/payments/elements), Stripe’s customizable UI
components for payment flows, and other Stripe APIs like
[PaymentMethods](https://docs.stripe.com/api/payment_methods),
[Customers](https://docs.stripe.com/api/customers), and
[Connect](https://docs.stripe.com/connect). The [Payment
Intents](https://docs.stripe.com/payments/payment-intents) and [Setup
Intents](https://docs.stripe.com/payments/save-and-reuse) APIs display
authentication flows like 3D Secure 2, save cards to use later, and support SCA.
- **For recurring payments, use Stripe Billing.** Billing is a tool for managing
subscriptions and invoicing. To learn how to update your Billing implementation
to support SCA requirements, see [SCA migration guide for
Billing](https://docs.stripe.com/billing/migration/strong-customer-authentication).
- **Programmatically subscribe your user to webhooks**: You can [register a
webhook endpoint](https://docs.stripe.com/webhooks#register-webhook) for your
account or connected accounts and manage them with the
[Webhooks](https://docs.stripe.com/webhooks) API, simplifying setup for your
users.

If none of these options work for your integration, [let us
know](mailto:plugins+sca@stripe.com).

[Test dynamic
authentication](https://docs.stripe.com/strong-customer-authentication/plugins#test-dynamic-auth)
After you have finished implementing the new integration path, configure your
[Dynamic 3D Secure Radar
rules](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
to test your integration using [3D Secure test
cards](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-cards).
Make sure to test both successful and unsuccessful authentication cases.

[Notify your users and
Stripe](https://docs.stripe.com/strong-customer-authentication/plugins#notify-users)
We recommend releasing an update for your users to let them know your payments
solution is SCA-ready. You can share the [guide to Strong Customer
Authentication](https://stripe.com/guides/strong-customer-authentication) with
your users to help them understand these regulatory changes. When you’ve
released an SCA-ready update, please [let us
know](mailto:plugins+sca@stripe.com) as well.

#### Caution

Provide an SCA-ready update as soon as you’re finished updating. We direct users
to SCA-ready solutions on the [Stripe
Partners](https://stripe.com/partners/sca-ready) page.

## See also

- [Checkout Overview](https://docs.stripe.com/payments/checkout)
- [One-time Payments](https://docs.stripe.com/payments/payment-intents)
- [Saving and Reusing Cards](https://docs.stripe.com/payments/save-and-reuse)
- [Migrating to Payment
Intents](https://docs.stripe.com/payments/payment-intents/migration)

## Links

- [SCA](https://docs.stripe.com/strong-customer-authentication)
- [Stripe Partners](https://stripe.com/partners/sca-ready)
- [European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Intents](https://docs.stripe.com/payments/payment-intents)
- [setAppInfo function](https://docs.stripe.com/building-plugins#setappinfo)
- [Stripe Partner
Program](https://stripe.com/partner-program?utm_campaign=partnerprogram&utm_source=sca-plugins-guide)
- [free
registration](https://stripe.com/partner-program?utm_campaign=partnerprogram&utm_source=sca-plugins-guide&utm_medium=join#stripe-partner-program)
- [suggested best practices](https://docs.stripe.com/building-plugins)
- [Elements](https://docs.stripe.com/payments/elements)
- [PaymentMethods](https://docs.stripe.com/api/payment_methods)
- [Customers](https://docs.stripe.com/api/customers)
- [Connect](https://docs.stripe.com/connect)
- [Setup Intents](https://docs.stripe.com/payments/save-and-reuse)
- [SCA migration guide for
Billing](https://docs.stripe.com/billing/migration/strong-customer-authentication)
- [register a webhook
endpoint](https://docs.stripe.com/webhooks#register-webhook)
- [Webhooks](https://docs.stripe.com/webhooks)
- [Dynamic 3D Secure Radar
rules](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
- [3D Secure test
cards](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-cards)
- [guide to Strong Customer
Authentication](https://stripe.com/guides/strong-customer-authentication)
- [Migrating to Payment
Intents](https://docs.stripe.com/payments/payment-intents/migration)