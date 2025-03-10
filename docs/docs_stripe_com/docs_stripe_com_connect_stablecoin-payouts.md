# Stablecoin payouts for ConnectPrivate preview

## Enable stablecoin payouts on your platform.

#### Private preview

The Stablecoin Payouts feature is currently limited to private preview users. If
you’re interested in trying it out, [email
us](mailto:stablecoin-payouts@stripe.com).

Stablecoin payouts let your platform pay out in stablecoins, starting with USDC.
You can use stablecoin payouts with your existing
[Connect](https://docs.stripe.com/connect) integration to avoid managing
stablecoins yourself. Your platform’s funds can remain in fiat currency, and
Stripe handles converting to stablecoins and paying it out.

## How it works

When you opt in to stablecoin payouts and provide your users access to the
[Express Dashboard](https://docs.stripe.com/connect/express-dashboard), your
users can link a crypto wallet with their account and set their default currency
to USDC. Your users can link a crypto wallet using the Express Dashboard.

When a user links a crypto wallet, they immediately see a new USDC balance on
their connected account. The USDC balance works like any other local currency
balance. You can transfer funds into the balance and the funds are paid out to
their linked crypto wallet instead of their bank account. When you create
[Transfers](https://docs.stripe.com/api/transfers) in USD, they automatically
convert to the preferred currency of your recipients. This simplifies your
integration and enables you to have a unified integration across fiat and
stablecoin payouts.

## Considerations

- **US platform activation**: Your platform must be in the US and activated. You
can activate it by [registering your
platform](https://dashboard.stripe.com/connect/set-up), [activating your
account](https://dashboard.stripe.com/account/onboarding), and [completing the
platform profile](https://dashboard.stripe.com/connect/settings/profile).
- **Individual recipients**: Recipients paid in stablecoins must be individuals
or sole proprietors. Paying companies and non-profits in stablecoins isn’t
currently supported.
- **Express Dashboard access**: To pay an individual in stablecoins, create a
connected account for them with access to the Express Dashboard. They can link a
crypto wallet and choose their preferred currency in this Dashboard.
- **Pay with the Transfers API**: You must use the [Transfers
API](https://docs.stripe.com/api/transfers) within your integration to pay in
stablecoins. Transfers to connected accounts with linked crypto wallets are
converted from fiat to USDC, enabling you to pay in USDC while your platform
balance stays in fiat. If you haven’t built an integration yet, you can pay in
stablecoins using a
[no-code](https://docs.stripe.com/connect/add-and-pay-out-guide?dashboard-or-api?dashboard-or-api=dashboard)
or [programmatic
integration](https://docs.stripe.com/connect/add-and-pay-out-guide?dashboard-or-api?dashboard-or-api=api).

### Supported countries

## Onboarding

Before you can enable Stablecoin Payouts:

- Make sure your Stripe account has been set up as a [Connect
platform](https://dashboard.stripe.com/connect/set-up/welcome).
- [Email us](mailto:stablecoin-payouts@stripe.com) to gain access to this
preview feature. Include your Stripe account ID in the email.
- After you hear back from us, which can take around two business days, request
the feature through the
[Dashboard](https://dashboard.stripe.com/stablecoin-payouts/overview).
- Complete additional account requirements, filling out the due diligence
questionnaire on the [Account status
page](https://dashboard.stripe.com/account/status).
- After we review and approve your information, Stablecoin Payouts becomes
available in your [Payment Method
settings](https://dashboard.stripe.com/settings/connect/payment_methods).

## Links

- [configured with
properties](https://docs.stripe.com/connect/update-to-typeless-connect)
- [Connect](https://docs.stripe.com/connect)
- [Express Dashboard](https://docs.stripe.com/connect/express-dashboard)
- [Transfers](https://docs.stripe.com/api/transfers)
- [registering your platform](https://dashboard.stripe.com/connect/set-up)
- [activating your account](https://dashboard.stripe.com/account/onboarding)
- [completing the platform
profile](https://dashboard.stripe.com/connect/settings/profile)
-
[no-code](https://docs.stripe.com/connect/add-and-pay-out-guide?dashboard-or-api?dashboard-or-api=dashboard)
- [programmatic
integration](https://docs.stripe.com/connect/add-and-pay-out-guide?dashboard-or-api?dashboard-or-api=api)
- [Connect platform](https://dashboard.stripe.com/connect/set-up/welcome)
- [Dashboard](https://dashboard.stripe.com/stablecoin-payouts/overview)
- [Account status page](https://dashboard.stripe.com/account/status)
- [Payment Method
settings](https://dashboard.stripe.com/settings/connect/payment_methods)