# Cross-border payoutsUS only

## Transfer and pay out funds to other countries.

Cross-border [payouts](https://docs.stripe.com/payouts) enable you to pay
sellers, freelancers, content creators, and service providers in their local
currencies. You can transfer funds to connected accounts in other countries with
your existing platform account and charge configuration.

#### Note

Stripe determines whether to enable cross-border payouts based on your platform
profile. If they aren’t enabled and you want to use them, contact [Stripe
Support](https://support.stripe.com/).

## Fund flow restrictions

The following fund flows are generally supported in countries for cross-border
payouts:

- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
without the `on_behalf_of` parameter
- [Top-ups and transfers](https://docs.stripe.com/connect/top-ups)
- [Destination charges](https://docs.stripe.com/connect/destination-charges)

Direct charges and destination charges *with* the `on_behalf_of` parameter
aren’t supported. However, some countries have additional limitations.

For
[India](https://support.stripe.com/questions/stripe-india-support-for-marketplaces),
only the following fund flows are supported:

- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
without the `on_behalf_of` parameter
- Top-up and transfers

## Supported countries

Cross-border payouts enable US platforms using separate charges and transfers,
destination charges, or top-ups to pay out to connected accounts in the
following countries:

AlbaniaAlgeriaPreviewAngolaPreviewAntigua &
BarbudaArgentinaArmeniaAustraliaAustriaAzerbaijanPreviewBahamasBahrainBangladeshPreviewBelgiumBeninBhutanPreviewBoliviaBosnia
& HerzegovinaBotswanaBruneiBulgariaCambodiaCanadaChileColombiaCosta RicaCôte
d’IvoireCroatia*CyprusCzech Republic*DenmarkDominican RepublicEcuadorEgyptEl
SalvadorEstoniaEthiopiaFinlandFranceGabonPreviewGambiaGermanyGhanaGreeceGuatemalaGuyanaHong
KongHungaryIceland*IndiaIndonesiaIrelandIsraelItalyJamaicaJapanJordanKazakhstanPreviewKenyaKuwaitLaosPreviewLatviaLiechtenstein*LithuaniaLuxembourgMacao
SAR
ChinaMadagascarMalaysiaMaltaMauritiusMexicoMoldovaMonacoMongoliaMoroccoMozambiquePreviewNamibiaNetherlandsNew
ZealandNigerPreviewNigeriaNorth
MacedoniaNorwayOmanPakistanPanamaParaguayPeruPhilippinesPolandPortugalQatarRomaniaRwandaSan
MarinoPreviewSaudi ArabiaSenegalSerbiaSingaporeSlovakiaSloveniaSouth AfricaSouth
KoreaSpainSri LankaSt. LuciaSwedenSwitzerland*TaiwanTanzaniaThailandTrinidad &
TobagoTunisiaTurkeyUnited Arab EmiratesUnited KingdomUruguayUzbekistanVietnam-
For connected accounts in countries marked with an asterisk (*), bank accounts
in those countries can only receive payouts in Euros (EUR).
- For connected accounts in countries labeled Preview, Stripe can pause payouts
in order to resolve issues. We don’t provide advance notice of pauses to
platforms or to connected accounts.

Each country has a minimum amount for cross-border payouts, which can differ
from the [minimum amount for regular
payouts](https://docs.stripe.com/payouts#minimum-payout-amounts). Some countries
also have special restrictions or requirements that affect cross-border payouts.
For details about minimum amounts and other requirements, see [Country-specific
considerations for cross-border
payouts](https://docs.stripe.com/connect/cross-border-payouts/special-requirements).

Stripe isn’t responsible for providing direct support for accounts on the
[recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#recipient).
However, the platform can reach out to Stripe for support for these accounts.

## Restrictions and requirements

- The platform must be in the US.
- Funds must come from separate charges and transfers, destination charges
without `on_behalf_of` (OBO), or top-ups.
- The platform must be the business of record. Consequently, [destination
charges with on_behalf_of
(OBO)](https://docs.stripe.com/connect/destination-charges#settlement-merchant)
aren’t supported.
- Connected accounts must onboard under the [recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#recipient).
That means transfers to `recipient` accounts take an extra 24 hours to become
available in the connected account’s balance.
- US connected accounts don’t support cross-border payouts; onboard US connected
accounts using the full [terms of
service](https://docs.stripe.com/connect/service-agreement-types).
- You can’t make cross-border [instant
payouts](https://docs.stripe.com/connect/instant-payouts).

In addition to businesses [prohibited on
Stripe](https://stripe.com/legal/restricted-businesses), you can’t use
cross-border payouts for:

- Crowdfunding
- Donations or fund contributions
- Non-fungible tokens (NFTs) minting and sales

The onboarding specifications for cross-border payouts vary by destination
country. To learn more, see:

- [Required verification
information](https://docs.stripe.com/connect/required-verification-information)
- [Supported settlement
currencies](https://docs.stripe.com/connect/payouts-connected-accounts#supported-settlement)
- [Bank account formats](https://docs.stripe.com/connect/payouts-bank-accounts)

## Get started

**Existing Connect platforms**—[Select the recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#choosing-type)
at account creation.

**New Connect platforms**—Follow one of the guides below that best fits your use
case, and make sure to [specify the recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#choosing-type)
in the account creation step.

- [Collect payments and then pay
out](https://docs.stripe.com/connect/collect-then-transfer-guide)
- [Pay out money](https://docs.stripe.com/connect/add-and-pay-out-guide)

## Links

- [payouts](https://docs.stripe.com/payouts)
- [Stripe Support](https://support.stripe.com/)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Top-ups and transfers](https://docs.stripe.com/connect/top-ups)
- [Destination charges](https://docs.stripe.com/connect/destination-charges)
-
[India](https://support.stripe.com/questions/stripe-india-support-for-marketplaces)
- [minimum amount for regular
payouts](https://docs.stripe.com/payouts#minimum-payout-amounts)
- [Country-specific considerations for cross-border
payouts](https://docs.stripe.com/connect/cross-border-payouts/special-requirements)
- [recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#recipient)
- [destination charges with on_behalf_of
(OBO)](https://docs.stripe.com/connect/destination-charges#settlement-merchant)
- [terms of service](https://docs.stripe.com/connect/service-agreement-types)
- [instant payouts](https://docs.stripe.com/connect/instant-payouts)
- [prohibited on Stripe](https://stripe.com/legal/restricted-businesses)
- [Required verification
information](https://docs.stripe.com/connect/required-verification-information)
- [Supported settlement
currencies](https://docs.stripe.com/connect/payouts-connected-accounts#supported-settlement)
- [Bank account formats](https://docs.stripe.com/connect/payouts-bank-accounts)
- [Select the recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#choosing-type)
- [Collect payments and then pay
out](https://docs.stripe.com/connect/collect-then-transfer-guide)
- [Pay out money](https://docs.stripe.com/connect/add-and-pay-out-guide)