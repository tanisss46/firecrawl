# Stripe fiat-to-crypto onrampPublic preview

## Let your users securely purchase crypto directly from your platform or Dapp.

The Stripe fiat-to-crypto onramp lets users securely purchase cryptocurrencies
directly from your platform or decentralized application (Dapp) at checkout. You
can customize and integrate the onramp into your product or service. To access
the onramp API, [submit an onramp
application](https://docs.stripe.com/crypto/onramp#submit-your-application).

Stripe serves as the merchant of record for these onramp transactions and
assumes full liability for all fraud and disputes. We also handle all regulatory
requirements, [know your
customer](https://en.wikipedia.org/wiki/Know_your_customer) (KYC) verifications,
and sanctions screening. Users can save payment methods, KYC data, and wallet
information with Stripe, which reduces the number of steps required when users
return to onramp.

![Stripe's fiat-to-crypto onramp being embedded into a third-party
application](https://b.stripecdn.com/docs-statics-srv/assets/crypto-onramp-overview.c9ec889d4c12403f4b2dbc17600dc640.png)

Stripe’s fiat-to-crypto onramp embedded within a third-party application

## Submit your application

We review most onramp applications within 48 hours. Follow these steps to submit
your application:

- Create or sign in to your Stripe account and submit the [onramp
application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication).
- Complete your [Stripe
application](https://dashboard.stripe.com/account/onboarding).
- After submitting the application, start development using [test
mode](https://docs.stripe.com/test-mode).

We notify you when your application is approved or if we need more information.
You can check your application status anytime by visiting the [onboarding
page](https://dashboard.stripe.com/crypto-onramp/onboarding).

## Integration options

Stripe offers multiple integration options for your application to connect with
the onramp. See the features available for each option to determine the best fit
for your use case.

IntegrationOverviewBest for[Embeddable
onramp](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide)
Recommended- Brand customization
- Supports dark mode
- Full parameter customization, including destination wallet address with the
[Onramp API](https://docs.stripe.com/crypto/onramp/api-reference#api-reference)
Users who want full customization and to embed the onramp widget directly into
their application.[No-code redirect URL
generation](https://docs.stripe.com/crypto/onramp/standalone-onramp-quickstart)-
No code required
- Some customization, including the suggested source or destination amount,
destination currency, and network
- Send users to a Stripe-hosted, standalone onramp at
[crypto.link.com](https://crypto.link.com/)
- Optional Stripe account
Users who don’t want to write any code and have static parameter values.Redirect
URL to [standalone
onramp](https://docs.stripe.com/crypto/onramp/standalone-onramp-guide)1- Some
customization, including the suggested source or destination amount, destination
currency, and network
- Send users to the Stripe-hosted, standalone onramp at
[crypto.link.com](https://crypto.link.com/)
- Optional Stripe account
Users who want light customization and a lightweight frontend integration.Minted
session with redirect URL to [standalone
onramp](https://docs.stripe.com/crypto/onramp/standalone-onramp-guide)1- Brand
customization
- Full parameter customization, including destination wallet address with the
[Onramp API](https://docs.stripe.com/crypto/onramp/api-reference#api-reference)
- Send users to the Stripe-hosted, standalone onramp at
[crypto.link.com](https://crypto.link.com/)
Users who want full customization, but don’t want to host the onramp themselves.
1 The [Stripe-hosted, standalone
onramp](https://docs.stripe.com/crypto/onramp/standalone-onramp-guide) provides
two different integration options with different levels of customization
available.

## Feature set

Stripe’s fiat-to-crypto onramp comes with the following built-in features:

FeatureDetailsCustomizability- Pre-populate transaction parameters
(`wallet_addresses`, source and destination currencies, source and destination
amounts, supported networks)
- Free platform integration—users pay fees
- Real-time quotes, automated KYC, and multi-chain support with very little
coding
- Implement using an embeddable widget, customizable to your brand
- Every session status change generates a webhook
- No platform fraud liability—Stripe handles all disputes
- Returning users can check out faster with
[Link](https://docs.stripe.com/payments/link), Stripe’s consumer account
infrastructure
Payment methodsCredit, debit, Apple Pay, and ACH (US only). All of these payment
methods are eligible for instant crypto delivery after KYC
completion.Currencies- ETH (Ethereum)
- ETH (Base)1
- SOL
- MATIC
- BTC
- AVAX
- XLM1
- USDC (Ethereum)
- USDC (Solana)1
- USDC (Polygon)1
- USDC (Avalanche)1
- USDC (Base)1
- USDC (Stellar)1
Geographic availabilityUS (excluding Hawaii) and EU countries
1XLM, USDC (Stellar), USDC (Avalanche), and USDC (Polygon) aren’t available in
New York. ETH (Base), MATIC, AVAX, USDC (Solana), USDC (Polygon), USDC
(Avalanche), and USDC (Base) aren’t supported in the EU.

## Links

- [know your customer](https://en.wikipedia.org/wiki/Know_your_customer)
- [onramp
application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication)
- [Stripe application](https://dashboard.stripe.com/account/onboarding)
- [test mode](https://docs.stripe.com/test-mode)
- [onboarding page](https://dashboard.stripe.com/crypto-onramp/onboarding)
- [Embeddable
onramp](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide)
- [Onramp
API](https://docs.stripe.com/crypto/onramp/api-reference#api-reference)
- [No-code redirect URL
generation](https://docs.stripe.com/crypto/onramp/standalone-onramp-quickstart)
- [crypto.link.com](https://crypto.link.com)
- [standalone
onramp](https://docs.stripe.com/crypto/onramp/standalone-onramp-guide)
- [Link](https://docs.stripe.com/payments/link)