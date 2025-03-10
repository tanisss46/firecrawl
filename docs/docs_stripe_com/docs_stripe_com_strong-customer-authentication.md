# Strong Customer Authentication readiness

## Learn how the Strong Customer Authentication regulation affects your business and how to update your integration to support it.

[Strong Customer Authentication
(SCA)](https://stripe.com/guides/strong-customer-authentication), a rule in
effect as of September 14, 2019, as part of PSD2 regulation in Europe, requires
changes to how your European customers authenticate online payments. Card
payments require you to use [3D
Secure](https://docs.stripe.com/payments/3d-secure) to meet SCA requirements.
Your customers’ banks might decline transactions that don’t follow the new
authentication guidelines.

To support SCA, you should:

- Determine if SCA impacts your business
- Decide which one of the SCA-ready products is right for your business
- Make changes now to avoid declined payments

#### Caution

If you use a third-party plugin, platform, or extension partner from the
[Partners gallery](https://stripe.partners/), contact your Stripe partner to see
if you need to make any changes to support SCA. Contact
[Support](https://support.stripe.com/contact) if you have any questions. You can
also see the [frequently asked
questions](https://docs.stripe.com/strong-customer-authentication/sca-enforcement)
for information on SCA enforcement.

## Impacted businesses and payments

Update your Stripe integration for SCA if all of the following apply:

- Your business is based in the [European Economic
Area](https://en.wikipedia.org/wiki/European_Economic_Area) or you [create
payments on behalf of connected accounts based in the
EEA](https://docs.stripe.com/strong-customer-authentication/connect-platforms)
- You serve customers in the EEA
- You accept cards (credit or debit)

While some low-risk transactions (based on the volume of fraud rates associated
with the payment provider or bank) don’t require authentication, banks can
choose to not honor these exemptions and request that the customer complete
authentication. Even if you’re primarily processing low-risk transactions,
update your integration so your customers can complete authentication when
requested by the bank. Stripe’s [new products and
APIs](https://docs.stripe.com/strong-customer-authentication#preparing) help you
claim these exemptions and maximize conversion by only requesting authentication
when absolutely necessary. Learn more about [SCA
exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication).

## SCA-ready products and APIs

Whether you collect one-time payments or save cards for later reuse, Stripe
provides prebuilt and customizable products to help you meet SCA requirements.

Integrations that aren’t SCA-ready, like those using the legacy [Charges
API](https://docs.stripe.com/payments/charges-api), might see high rates of
declines from banks that enforce SCA.

### One-time payments

Accept card payments with the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents) and
[Checkout](https://docs.stripe.com/payments/checkout), a prebuilt, Stripe-hosted
checkout flow that automatically handles SCA requirements for you. Checkout is
customizable and lets you accept payments for one-time purchases and
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating) on your
website.

- [Migrating to the Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration)
- [Use a prebuilt checkout
page](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Build a custom payment
flow](https://docs.stripe.com/payments/accept-a-payment?integration=elements)

### Reusing cards

Save a card for later reuse with the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents) and the [Setup Intents
API](https://docs.stripe.com/api/setup_intents). You can also use
[Checkout](https://docs.stripe.com/payments/checkout) to automatically handle
SCA requirements, or use [Billing](https://docs.stripe.com/billing) to handle
SCA for subscription models.

- [Use a prebuilt checkout
page](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
- [Build a custom flow to save card
details](https://docs.stripe.com/payments/save-and-reuse)
- [Use Billing for subscription
models](https://docs.stripe.com/billing/migration/strong-customer-authentication)

## SCA migration

You might need to update your integration to support SCA. For more details about
changes you might need to make, see [Migrating to the Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration) and [SCA
migration guide for
Billing](https://docs.stripe.com/billing/migration/strong-customer-authentication).

For specific product recommendations based on common business scenarios, check
out the [SCA payment flows](https://stripe.com/guides/sca-payment-flows) guide.

## Links

- [Watch the SCA
video](https://stripe.com/payments/strong-customer-authentication)
- [See SCA payment scenarios](https://stripe.com/guides/sca-payment-flows)
- [View the webinar](https://go.stripe.global/sca-webinar.html)
- [Strong Customer Authentication
(SCA)](https://stripe.com/guides/strong-customer-authentication)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [Partners gallery](https://stripe.partners)
- [Support](https://support.stripe.com/contact)
- [frequently asked
questions](https://docs.stripe.com/strong-customer-authentication/sca-enforcement)
- [European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)
- [create payments on behalf of connected accounts based in the
EEA](https://docs.stripe.com/strong-customer-authentication/connect-platforms)
- [SCA
exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)
- [Charges API](https://docs.stripe.com/payments/charges-api)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Migrating to the Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration)
- [Use a prebuilt checkout
page](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Build a custom payment
flow](https://docs.stripe.com/payments/accept-a-payment?integration=elements)
- [Setup Intents API](https://docs.stripe.com/api/setup_intents)
- [Billing](https://docs.stripe.com/billing)
- [Use a prebuilt checkout
page](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
- [Build a custom flow to save card
details](https://docs.stripe.com/payments/save-and-reuse)
- [Use Billing for subscription
models](https://docs.stripe.com/billing/migration/strong-customer-authentication)