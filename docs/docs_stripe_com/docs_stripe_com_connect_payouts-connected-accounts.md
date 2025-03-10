# Payouts to connected accounts

## Manage payouts and external accounts for your platform's connected accounts.

By default, any [charge](https://docs.stripe.com/connect/charges) you make on
behalf of a connected account accumulates in the connected account’s
[balance](https://docs.stripe.com/connect/account-balances) and is paid out on a
daily rolling basis. Depending on the configuration of your connected accounts,
your platform can manage their payouts as follows:

- Schedule [the frequency of automatic
payouts](https://docs.stripe.com/connect/manage-payout-schedule)
- Perform [manual payouts](https://docs.stripe.com/connect/manual-payouts)
- Settle funds [instantly](https://docs.stripe.com/connect/instant-payouts)
- When using [destination
charges](https://docs.stripe.com/connect/destination-charges) or [separate
charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers),
retain funds in your platform balance

#### Note

In versions of Connect earlier than 2018, payouts were known as bank transfers
and used the deprecated `transfers` API. For information about bank transfers,
see the legacy [Transfers](https://docs.stripe.com/connect/legacy-transfers)
documentation.

## Payout management configurations

For connected accounts with access to the full Stripe Dashboard or Express
Dashboard, the account holder manages their external
[payout](https://docs.stripe.com/payouts) accounts (bank accounts and debit
cards), but the platform can schedule payouts. To schedule payouts for an
account that has access to the full Stripe Dashboard, the platform must
configure [Platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
for the account.

For connected accounts without access to a Stripe-hosted Dashboard, the platform
manages their external payout accounts and can schedule their payouts.

## Supported settlement currencies

To see which currencies you can use to settle funds in a particular country,
select that country from the following dropdown.

#### Note

For a list of supported presentment currencies, see the
[currencies](https://docs.stripe.com/currencies#presentment-currencies)
documentation.

Viewing supported settlement currencies for Stripe accounts in:Albania
(AL)Algeria (DZ)Angola (AO)Antigua & Barbuda (AG)Argentina (AR)Armenia
(AM)Australia (AU)Austria (AT)Azerbaijan (AZ)Bahamas (BS)Bahrain (BH)Bangladesh
(BD)Belgium (BE)Benin (BJ)Bhutan (BT)Bolivia (BO)Bosnia & Herzegovina
(BA)Botswana (BW)Brazil (BR)Brunei (BN)Bulgaria (BG)Cambodia (KH)Canada
(CA)Chile (CL)Colombia (CO)Costa Rica (CR)Côte d’Ivoire (CI)Croatia (HR)Cyprus
(CY)Czech Republic (CZ)Denmark (DK)Dominican Republic (DO)Ecuador (EC)Egypt
(EG)El Salvador (SV)Estonia (EE)Ethiopia (ET)Finland (FI)France (FR)Gabon
(GA)Gambia (GM)Germany (DE)Ghana (GH)Gibraltar (GI)Greece (GR)Guatemala
(GT)Guyana (GY)Hong Kong (HK)Hungary (HU)Iceland (IS)India (IN)Indonesia
(ID)Ireland (IE)Israel (IL)Italy (IT)Jamaica (JM)Japan (JP)Jordan (JO)Kazakhstan
(KZ)Kenya (KE)Kuwait (KW)Laos (LA)Latvia (LV)Liechtenstein (LI)Lithuania
(LT)Luxembourg (LU)Macao SAR China (MO)Madagascar (MG)Malaysia (MY)Malta
(MT)Mauritius (MU)Mexico (MX)Moldova (MD)Monaco (MC)Mongolia (MN)Morocco
(MA)Mozambique (MZ)Namibia (NA)Netherlands (NL)New Zealand (NZ)Niger (NE)Nigeria
(NG)North Macedonia (MK)Norway (NO)Oman (OM)Pakistan (PK)Panama (PA)Paraguay
(PY)Peru (PE)Philippines (PH)Poland (PL)Portugal (PT)Qatar (QA)Romania
(RO)Rwanda (RW)San Marino (SM)Saudi Arabia (SA)Senegal (SN)Serbia (RS)Singapore
(SG)Slovakia (SK)Slovenia (SI)South Africa (ZA)South Korea (KR)Spain (ES)Sri
Lanka (LK)St. Lucia (LC)Sweden (SE)Switzerland (CH)Taiwan (TW)Tanzania
(TZ)Thailand (TH)Trinidad & Tobago (TT)Tunisia (TN)Turkey (TR)United Arab
Emirates (AE)United Kingdom (GB)United States (US)Uruguay (UY)Uzbekistan
(UZ)Vietnam (VN)Accounts created in United States and that are under the [full
service agreement](https://docs.stripe.com/connect/service-agreement-types#full)
can receive payouts in the following settlement currencies.Settlement
currencyCan be paid out to banks in these countriesUSDUnited States
Platforms can also enable their connected accounts to settle funds and pay out
to banks in certain non-primary currencies, or pay out to non-domestic bank
accounts in the local currency. In some cases, Stripe charges a fee. For more
information, see [multi-currency settlement for Connect marketplaces and
platforms](https://docs.stripe.com/connect/multicurrency-settlement).

### Use webhooks with payouts

You can track all payout activity on connected accounts with webhooks by
creating an [event destination](https://docs.stripe.com/event-destinations) and
listening for these events:

- `payout.created`
- `payout.updated`
- `payout.paid`
- `payout.failed`

For most payouts, event notifications occur over a series of days. Instant
payouts typically send `payout.paid` within 30 minutes.

When a payout can’t be completed, a `payout.failed` event occurs. The event’s
`failure_code` property indicates the reason. A failed payout also disables the
external account involved in that payout, triggering an
`account.external_account.updated` event. No payouts can be made to that
external account until the platform updates the connected account’s external
accounts.

## Links

- [charge](https://docs.stripe.com/connect/charges)
- [balance](https://docs.stripe.com/connect/account-balances)
- [the frequency of automatic
payouts](https://docs.stripe.com/connect/manage-payout-schedule)
- [manual payouts](https://docs.stripe.com/connect/manual-payouts)
- [instantly](https://docs.stripe.com/connect/instant-payouts)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Transfers](https://docs.stripe.com/connect/legacy-transfers)
- [payout](https://docs.stripe.com/payouts)
- [Platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [currencies](https://docs.stripe.com/currencies#presentment-currencies)
- [full service
agreement](https://docs.stripe.com/connect/service-agreement-types#full)
- [multi-currency settlement for Connect marketplaces and
platforms](https://docs.stripe.com/connect/multicurrency-settlement)
- [event destination](https://docs.stripe.com/event-destinations)