# Connect account types

## Learn about older connected account configurations.

When using [Connect](https://docs.stripe.com/connect), you create a [connected
account](https://docs.stripe.com/connect) for each business or individual that
signs up to access your platform’s services. You can configure your platform and
connected accounts to fit your business model, distributing specific
responsibilities between your platform, Stripe, and your connected accounts.

If you’re setting up a new Connect platform, see [Design an
integration](https://docs.stripe.com/connect/design-an-integration) to learn
about configuring connected accounts. The information on this page applies only
to less flexible connected account types, which are mainly used by existing
platforms.

#### Note

If your existing connected accounts are configured as a type, you can still
[migrate your platform to support new connected accounts that are configured
without
types](https://docs.stripe.com/connect/migrate-to-controller-properties). During
and after migration, your platform can continue to support your existing
connected accounts without interruption.

Connect supports the following account types:

- [Standard](https://docs.stripe.com/connect/standard-accounts)
- [Express](https://docs.stripe.com/connect/express-accounts)
- [Custom](https://docs.stripe.com/connect/custom-accounts)

## Choose an account type

You must consider several factors when choosing an account type. Integration
effort and connected account user experience are especially important because
they can affect engineering resource expenditure and conversion rates. After you
create a connected account, you can’t change its type.

Stripe recommends that you [use controller
properties](https://docs.stripe.com/connect/migrate-to-controller-properties)
instead of account types. If you want to use account types, we recommend Express
or Standard connected accounts because they require less integration effort. For
more control over your connected accounts, consider using Custom connected
accounts. To learn which account type we recommend for your business, refer to
your [platform profile](https://dashboard.stripe.com/connect/settings/profile).

There’s an additional cost for using Express or Custom connected accounts.

Standard Express Custom Integration effortLowestLowSignificantly
higherIntegration methodAPI or OAuthAPIAPIFraud and dispute liabilityConnected
accountPlatformPlatformPlatform can specify payout timing?Yes, with [Platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)YesYesOnboardingStripeStripePlatform
or StripeIdentity information gatheringStripeStripePlatform or StripeConnected
account can access the Dashboard?Yes, full DashboardYes, Express
DashboardNoConnected account support provided byPlatform and StripePlatform and
StripePlatformAutomatic updates for new compliance requirementsYesSupport
new countries without integration changesYesIdeal for platformsWith
experienced online businesses as connected accountsAny typeWith significant
engineering resources to dedicate to a fully white-labeled experience
With Standard connected accounts, the connected account is responsible for fraud
and disputes when using [direct
charges](https://docs.stripe.com/connect/charges#types), but that can vary when
using [destination charges](https://docs.stripe.com/connect/charges#types).

## Express connected accounts

With *Express* connected accounts, Stripe handles the onboarding and identity
verification processes. The platform has the ability to specify [charge
types](https://docs.stripe.com/connect/charges) and set the connected account’s
[payout settings](https://docs.stripe.com/connect/payouts-connected-accounts)
programmatically. The platform is responsible for handling disputes and refunds,
which is similar to a Custom connected account.

Although your connected account has interactions with Stripe, they primarily
interact with your platform, particularly for the core payment processing
functionality. For Express connected account holders, Stripe provides an Express
Dashboard (a lighter version of the Dashboard) that allows them to manage their
personal information and see [payouts](https://docs.stripe.com/payouts) to their
bank.

Use Express connected accounts when you:

- Want to get started quickly (letting Stripe handle account onboarding,
management, and identity verification)
- Want to use [destination
charges](https://docs.stripe.com/connect/destination-charges) or [separate
charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- Want significant control over interactions with your connected accounts

Examples of platforms that use Express connected accounts include, but are not
limited to: a [home-rental
marketplace](https://docs.stripe.com/connect/collect-then-transfer-guide) like
Airbnb, or a ride-hailing service like Lyft.

Global compliance requirements do evolve and change over time. With Express,
Stripe proactively collects information when requirements change. For best
practices on how to communicate to your connected accounts when that happens,
visit the [guide for Express
accounts](https://support.stripe.com/questions/best-practices-for-connect-platforms-communicating-updates-to-verification-requirements-with-standard-or-express-connected-accounts).

### Express connected account availability

Select one of the available countries when you create an Express connected
account. You can’t change the country later.

Some countries are available only when using [cross-border
payouts](https://docs.stripe.com/connect/cross-border-payouts).

To know when Express connected accounts are available in your country, [contact
Stripe](mailto:connect@stripe.com).

AlbaniaAntigua &
BarbudaArgentinaArmeniaAustraliaAustriaBahamasBahrainBelgiumBeninBoliviaBosnia &
HerzegovinaBotswanaBruneiBulgariaCambodiaCanadaChileColombiaCosta RicaCôte
d’IvoireCyprusCzech RepublicDenmarkDominican RepublicEcuadorEgyptEl
SalvadorEstoniaEthiopiaFinlandFranceGambiaGermanyGhanaGreeceGuatemalaGuyanaHong
KongHungaryIcelandIrelandIsraelItalyJamaicaJapanJordanKenyaKuwaitLatviaLithuaniaLuxembourgMacao
SAR
ChinaMadagascarMaltaMauritiusMexicoMoldovaMonacoMongoliaMoroccoNamibiaNetherlandsNew
ZealandNigeriaNorth
MacedoniaNorwayOmanPakistanPanamaParaguayPeruPhilippinesPolandPortugalQatarRomaniaRwandaSaudi
ArabiaSenegalSerbiaSingaporeSlovakiaSloveniaSouth AfricaSouth KoreaSpainSri
LankaSt. LuciaSwedenSwitzerlandTaiwanTanzaniaThailandTrinidad &
TobagoTunisiaTurkeyUnited Arab EmiratesUnited KingdomUnited
StatesUruguayUzbekistanVietnam
## Standard connected accounts

A *Standard* connected account is a conventional Stripe account where the
connected account has a direct relationship with Stripe, is able to log in to
the [Dashboard](https://dashboard.stripe.com/), and can process charges on their
own.

Use Standard connected accounts when you:

- Want to get started quickly and don’t need a lot of control over interactions
with your connected accounts
- Want to use [direct charges](https://docs.stripe.com/connect/direct-charges)
- Have connected accounts that are familiar with running online businesses or
that already have a Stripe account
- Prefer that Stripe handles direct communication with the connected account for
account issues (for example, to request more information for identity
verification purposes)

Some examples of platforms that use Standard connected accounts are [store
builders](https://docs.stripe.com/connect/enable-payment-acceptance-guide) like
Shopify, and Software as a Service (SaaS) platforms such as an online invoicing
and payment service.

Global compliance requirements do evolve and change over time. With Standard
connected accounts, Stripe proactively collects information when requirements
change. For best practices on how to communicate to your connected accounts when
that happens, visit the [guide for Standard
accounts](https://support.stripe.com/questions/best-practices-for-connect-platforms-communicating-updates-to-verification-requirements-with-standard-or-express-connected-accounts).

#### Country can't be changed

After you create a Standard connected account, you can’t change its country.

## Custom connected accounts

A *Custom* connected account is almost completely invisible to the account
holder. You—the platform—are responsible for all interactions with your
connected accounts, including collecting any information Stripe needs. You have
the ability to change all of the account’s
[settings](https://docs.stripe.com/connect/updating-service-agreements),
including the payout [bank or debit card
account](https://docs.stripe.com/connect/payouts-connected-accounts),
programmatically.

Custom connected account holders don’t have access to the Dashboard, and Stripe
doesn’t contact them directly.

Use Custom connected accounts when you:

- Want complete control over interactions with your connected accounts
- Can build the significant infrastructure required to collect connected account
information, deploy a custom dashboard, and handle support
- Want to handle all communication with your connected accounts, involving no
direct contact between them and Stripe

Creating and managing Custom connected accounts requires a larger integration
effort than the other account types. To learn more, see [Using Connect with
Custom accounts](https://docs.stripe.com/connect/custom-accounts).

Global compliance requirements do evolve and change over time. For best
practices on how to communicate to your connected accounts when requirements
change, see the [guide for Custom
accounts](https://support.stripe.com/questions/best-practices-for-connect-platforms-communicating-updates-to-verification-requirements-with-custom-connected-accounts).

If you decide to use Custom connected accounts, Stripe recommends that you use
[Connect Onboarding for Custom
accounts](https://docs.stripe.com/connect/custom/hosted-onboarding) to collect
onboarding and verification information from your connected accounts. That
decreases your integration effort and eliminates the need to update your
onboarding form when requirements change.

### Custom connected account availability

Select one of the available countries when you create a Custom connected
account. You can’t change the country later.

Some countries are available only when using [cross-border
payouts](https://docs.stripe.com/connect/cross-border-payouts).

To request notification when Custom connected accounts are available in your
country, [contact Stripe](mailto:connect@stripe.com).

AlbaniaAntigua &
BarbudaArgentinaArmeniaAustraliaAustriaBahamasBahrainBelgiumBeninBoliviaBosnia &
HerzegovinaBotswanaBruneiBulgariaCambodiaCanadaChileColombiaCosta RicaCôte
d’IvoireCyprusCzech RepublicDenmarkDominican RepublicEcuadorEgyptEl
SalvadorEstoniaEthiopiaFinlandFranceGambiaGermanyGhanaGreeceGuatemalaGuyanaHong
KongHungaryIcelandIrelandIsraelItalyJamaicaJapanJordanKenyaKuwaitLatviaLithuaniaLuxembourgMacao
SAR
ChinaMadagascarMaltaMauritiusMexicoMoldovaMonacoMongoliaMoroccoNamibiaNetherlandsNew
ZealandNigeriaNorth
MacedoniaNorwayOmanPakistanPanamaParaguayPeruPhilippinesPolandPortugalQatarRomaniaRwandaSaudi
ArabiaSenegalSerbiaSingaporeSlovakiaSloveniaSouth AfricaSouth KoreaSpainSri
LankaSt. LuciaSwedenSwitzerlandTaiwanTanzaniaThailandTrinidad &
TobagoTunisiaTurkeyUnited Arab EmiratesUnited KingdomUnited
StatesUruguayUzbekistanVietnam
## See also

- [Express connected accounts](https://docs.stripe.com/connect/express-accounts)
- [Standard connected
accounts](https://docs.stripe.com/connect/standard-accounts)
- [Custom connected accounts](https://docs.stripe.com/connect/custom-accounts)
- [Account capabilities](https://docs.stripe.com/connect/account-capabilities)

## Links

- [Connect](https://docs.stripe.com/connect)
- [Design an integration](https://docs.stripe.com/connect/design-an-integration)
- [migrate your platform to support new connected accounts that are configured
without types](https://docs.stripe.com/connect/migrate-to-controller-properties)
- [Standard](https://docs.stripe.com/connect/standard-accounts)
- [Express](https://docs.stripe.com/connect/express-accounts)
- [Custom](https://docs.stripe.com/connect/custom-accounts)
- [Extensions](https://docs.stripe.com/building-extensions)
- [platform profile](https://dashboard.stripe.com/connect/settings/profile)
- [Platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [direct charges](https://docs.stripe.com/connect/charges#types)
- [charge types](https://docs.stripe.com/connect/charges)
- [payout settings](https://docs.stripe.com/connect/payouts-connected-accounts)
- [payouts](https://docs.stripe.com/payouts)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [home-rental
marketplace](https://docs.stripe.com/connect/collect-then-transfer-guide)
- [guide for Express
accounts](https://support.stripe.com/questions/best-practices-for-connect-platforms-communicating-updates-to-verification-requirements-with-standard-or-express-connected-accounts)
- [cross-border payouts](https://docs.stripe.com/connect/cross-border-payouts)
- [Dashboard](https://dashboard.stripe.com/)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [store
builders](https://docs.stripe.com/connect/enable-payment-acceptance-guide)
- [settings](https://docs.stripe.com/connect/updating-service-agreements)
- [guide for Custom
accounts](https://support.stripe.com/questions/best-practices-for-connect-platforms-communicating-updates-to-verification-requirements-with-custom-connected-accounts)
- [Connect Onboarding for Custom
accounts](https://docs.stripe.com/connect/custom/hosted-onboarding)
- [Account capabilities](https://docs.stripe.com/connect/account-capabilities)