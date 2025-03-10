# Receive payouts

## Set up your bank account to receive payouts.

You receive funds when Stripe (or your platform) makes payouts to your bank
account. Payout availability varies depending on your industry and country of
operation. When you start processing live payments, Stripe typically schedules
your initial payout for 7-14 days after you successfully receive your first
payment. Your first payout might take longer, depending on your industry risk
level and country of operation. Subsequent payouts follow your account’s [payout
schedule](https://docs.stripe.com/payouts#payout-schedule).

You can see a comprehensive list of your payouts and the expected dates of
deposit into your bank account in the
[Dashboard](https://dashboard.stripe.com/test/payouts). If you’re a
[Connect](https://docs.stripe.com/connect) platform, see [Connect
payouts](https://docs.stripe.com/connect/payouts-connected-accounts).

## Add or update your bank account

You can update your account details or add a new bank account using the [Payout
settings](https://dashboard.stripe.com/account/payouts) in the Dashboard. Based
on your bank’s location, Stripe might require different kinds of account details
to activate your bank account. You must match the currency of the bank account
to the currency in your [Payout
settings](https://dashboard.stripe.com/account/payouts). Click **Edit** next to
the applicable bank account to modify the banking information.

Use the following table to see the required bank details for specific countries:

Albania (AL)Algeria (DZ)Angola (AO)Antigua and Barbuda (AG)Argentina (AR)Armenia
(AM)Australia (AU)Austria (AT)Azerbaijan (AZ)Bahamas (BS)Bahrain (BH)Bangladesh
(BD)Belgium (BE)Benin (BJ)Bhutan (BT)Bolivia (BO)Bosnia and Herzegovina
(BA)Botswana (BW)Brazil (BR)Brunei (BN)Bulgaria (BG)Cambodia (KH)Canada
(CA)Chile (CL)Colombia (CO)Costa Rica (CR)Côte d'Ivoire (CI)Croatia (HR)Cyprus
(CY)Czech Republic (CZ)Denmark (DK)Dominican Republic (DO)Ecuador (EC)Egypt
(EG)El Salvador (SV)Estonia (EE)Ethiopia (ET)Finland (FI)France (FR)Gabon
(GA)Gambia (GM)Germany (DE)Ghana (GH)Gibraltar (GI)Greece (GR)Guatemala
(GT)Guyana (GY)Hong Kong (HK)Hungary (HU)Iceland (IS)India (IN)Indonesia
(ID)Ireland (IE)Israel (IL)Italy (IT)Jamaica (JM)Japan (JP)Jordan (JO)Kazakhstan
(KZ)Kenya (KE)Kuwait (KW)Laos (LA)Latvia (LV)Liechtenstein (LI)Lithuania
(LT)Luxembourg (LU)Macau (MO)Madagascar (MG)Malaysia (MY)Malta (MT)Mauritius
(MU)Mexico (MX)Moldova (MD)Monaco (MC)Mongolia (MN)Morocco (MA)Mozambique
(MZ)Namibia (NA)Netherlands (NL)New Zealand (NZ)Niger (NE)Nigeria (NG)North
Macedonia (MK)Norway (NO)Oman (OM)Pakistan (PK)Panama (PA)Paraguay (PY)Peru
(PE)Philippines (PH)Poland (PL)Portugal (PT)Qatar (QA)Romania (RO)Rwanda
(RW)Saint Lucia (LC)Saudi Arabia (SA)San Marino (SM)Senegal (SN)Serbia
(RS)Singapore (SG)Slovakia (SK)Slovenia (SI)South Africa (ZA)South Korea
(KR)Spain (ES)Sri Lanka (LK)Sweden (SE)Switzerland (CH)Taiwan (TW)Tanzania
(TZ)Thailand (TH)Trinidad & Tobago (TT)Tunisia (TN)Türkiye (TR)United Kingdom
(GB)United States (US)United Arab Emirates (AE)Uruguay (UY)Uzbekistan
(UZ)Vietnam (VN)Bank account information Example dataRouting Number111000000 (9
characters)Account numberFormat varies by bank
### Supported bank account types

You have the flexibility to link various types of bank accounts for your Stripe
payouts. Supported options include traditional accounts offered by established
financial institutions, including checking and savings accounts. Additionally,
Stripe lets you use virtual bank accounts such as N26, Revolut, Wise, and
others. If you’re eligible, you can also use a debit card for [instant
payouts](https://docs.stripe.com/payouts#instant-payouts).

#### Note

While Stripe supports non-standard bank accounts, you might see higher payout
failures for these accounts.

### Supported accounts and settlement currencies

In most cases, bank accounts must be located in the country where the settlement
currency is the official currency. For example, SEK bank accounts must be based
in Sweden. Stripe also allows you to settle and pay out to banks in select
additional currencies, or pay out to non-domestic bank accounts in the local
currency, for a fee. Learn more about [presenting and settling in multiple
currencies](https://docs.stripe.com/payouts/multicurrency-settlement).

At times, Stripe supports non-primary currencies that don’t incur a fee. See the
following table for the list of supported free currencies per country:

Viewing supported settlement currencies for Stripe accounts in:Albania
(AL)Algeria (DZ)Angola (AO)Antigua & Barbuda (AG)Argentina (AR)Armenia
(AM)Australia (AU)Austria (AT)Azerbaijan (AZ)Bahamas (BS)Bahrain (BH)Bangladesh
(BD)Belgium (BE)Benin (BJ)Bhutan (BT)Bolivia (BO)Bosnia & Herzegovina
(BA)Botswana (BW)Brazil (BR)Brunei (BN)Bulgaria (BG)Cambodia (KH)Canada
(CA)Chile (CL)Colombia (CO)Costa Rica (CR)Côte d’Ivoire (CI)Croatia (HR)Cyprus
(CY)Czech Republic (CZ)Denmark (DK)Dominican Republic (DO)Ecuador (EC)Egypt
(EG)El Salvador (SV)Estonia (EE)Ethiopia (ET)Finland (FI)France (FR)Gabon
(GA)Gambia (GM)Germany (DE)Ghana (GH)Gibraltar (GI)Greece (GR)Guatemala
(GT)Guyana (GY)Hong Kong (HK)Hungary (HU)India (IN)Indonesia (ID)Ireland
(IE)Israel (IL)Italy (IT)Jamaica (JM)Japan (JP)Jordan (JO)Kazakhstan (KZ)Kenya
(KE)Kuwait (KW)Laos (LA)Latvia (LV)Liechtenstein (LI)Lithuania (LT)Luxembourg
(LU)Macao SAR China (MO)Madagascar (MG)Malaysia (MY)Malta (MT)Mauritius
(MU)Mexico (MX)Moldova (MD)Mongolia (MN)Morocco (MA)Mozambique (MZ)Namibia
(NA)Netherlands (NL)New Zealand (NZ)Niger (NE)Nigeria (NG)North Macedonia
(MK)Norway (NO)Oman (OM)Pakistan (PK)Panama (PA)Paraguay (PY)Peru
(PE)Philippines (PH)Poland (PL)Portugal (PT)Qatar (QA)Romania (RO)Rwanda
(RW)Saudi Arabia (SA)Senegal (SN)Serbia (RS)Singapore (SG)Slovakia (SK)Slovenia
(SI)South Africa (ZA)South Korea (KR)Spain (ES)Sri Lanka (LK)St. Lucia
(LC)Sweden (SE)Switzerland (CH)Taiwan (TW)Tanzania (TZ)Thailand (TH)Trinidad &
Tobago (TT)Tunisia (TN)Turkey (TR)United Arab Emirates (AE)United Kingdom
(GB)United States (US)Uruguay (UY)Uzbekistan (UZ)Vietnam (VN)Settlement
currencyCan be paid out to banks in these countriesUSDUnited States
Acquiring fees, where applicable, are based on the settlement currency. You can
find these acquiring fees listed out by currency on your country’s pricing page.

### Multiple bank accounts for different settlement currencies

In some countries, Stripe users can add extra bank accounts to enable
settlements and payouts in additional currencies. You can add one bank account
per supported settlement currency. If you use multiple bank accounts, you must
select a default settlement currency, which you can change at any time.

Charges that are
[presented](https://docs.stripe.com/currencies#presentment-currencies) in any
enabled settlement currency settle without [currency
conversion](https://docs.stripe.com/currencies/conversions). However, payments
presented in a currency that you haven’t configured an additional bank account
for automatically convert to your default currency.

For example, consider a Stripe user in the United Kingdom who has added both GBP
and USD bank accounts, with GBP selected as the default settlement currency. USD
payments (where USD is the presentment currency) are automatically paid out to
the USD bank account without conversion, whereas payments in all other
currencies are converted into GBP.

You can manage your bank accounts and default settlement currency by visiting
[Bank accounts and scheduling](https://dashboard.stripe.com/account/payouts) in
the Dashboard.

## Payout schedule

Your payout schedule determines when Stripe sends money to your bank account.
You can select your preferred payout schedule during onboarding or update it any
time in the Stripe Dashboard.

### Types of payout schedules

The following payout schedules are available:

- Manual payouts: You choose when to send payouts and how much to transfer.
- Daily payouts: Stripe automatically transfers your available funds every
business day.
- Weekly or monthly payouts: You set a specific day of the week or day of the
month for payouts.
- Monthly adjustments: If your selected payout day doesn’t exist in a given
month (for example, the 31st in a 30-day month), Stripe moves the payout to the
last day of that month.
- Non-business days: Payouts that are scheduled on weekends or holidays arrive
on the next business day.

### How payout timing works

Choosing a payout schedule doesn’t change how long it takes for your pending
balance to become available. It only controls when payouts are sent.

For example, if your account is set to daily payouts with a 3-business-day
[payout speed](https://docs.stripe.com/payouts#payout-speed), Stripe pays out
funds daily from transactions that were captured three business days earlier.

### Country-specific payout restrictions

Some countries have preset payout schedules due to local regulations:

- Brazil and India: Payouts are always automatic and daily.
- Japan: Daily payouts aren’t available. The default schedule is weekly
(Friday).
- Thailand: The default schedule is daily automatic payouts.

These restrictions don’t apply if you’re using [Cross-border
payouts](https://docs.stripe.com/connect/cross-border-payouts).

### Manual payouts

If you turn off automatic payouts in the
[Dashboard](https://dashboard.stripe.com/settings/payouts), you must manually
send funds to your bank account. You can do this either in the Dashboard or by
[creating payouts](https://docs.stripe.com/api#create_payout) using the API.
Manual payouts are available in all regions except Brazil and India, where
payouts are always automatic and daily. In most regions, manual payouts
typically take 1-4 business days to arrive in your bank account after initiating
the manual payout.

If your Stripe account that operates in the United Kingdom has a standard [T+3
payout speed](https://docs.stripe.com/payouts#payout-speed) and you initiate a
manual payout during business hours, the funds typically arrive in your bank
account on the same business day. This same-day payout is limited to 10 same-day
manual payouts per day, with a maximum transaction amount of £1 million each.
All other manual payouts typically arrive within 2 business days in your bank
account.

```
curl https://api.stripe.com/v1/payouts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=5000 \
 -d currency=usd
```

## Payout speed

While payout schedule refers to the cadence your funds are paid out on (for
example, day of the week), payout speed refers to the amount of time it takes
for your funds to become available. The payout speed varies per country and is
typically expressed as T+X days. Some payment processors might start “T” from
their internal settlement time, meaning when the funds land in their bank
accounts.

In Stripe, “T” refers to the transaction time, which indicates the time of the
original payment confirmation or capture, and the counting starts earlier. If
your Stripe account is in a country with a T+3 standard payout speed and you use
a manual payout schedule, your Stripe balance is available for payout within
three business days of capturing a payment. However, if you use a daily
automatic payout schedule with a T+3 speed, Stripe pays out funds daily from
transactions captured 3 business days earlier.

Most banks deposit payouts into your bank account as soon as they receive them,
though some might take a few extra days to make them available. The type of
business and the country you’re in can also affect payout timing.

### Accelerated payout speeds

Stripe offers accelerated payout speeds for users and connected accounts where
Stripe manages credit and fraud risk in Europe, the UK, Mexico, and Canada. With
accelerated payout speeds, funds are available within 3 business days.

Users become eligible for accelerated payout speeds after meeting certain
criteria based on risk and history with Stripe. When you’re eligible, you can
choose to opt in or out of accelerated payout speeds in the Dashboard by
updating your [Payout settings](https://dashboard.stripe.com/settings/payouts).
You remain at the starting 7 calendar day payout speed until you meet the
eligibility criteria. You can [configure
accounts](https://docs.stripe.com/connect/manage-payout-schedule) where you
manage fraud and dispute liability separately. Some high risk industries might
not be eligible.

### Delay behavior per account country

As the platform, you can set
[delay_days](https://docs.stripe.com/connect/manage-payout-schedule#delay_days)
on your connected accounts. The delay applies as a **business day** or
**calendar day** delay based on the country of the connected account. The
following table shows which countries apply the delay by business or calendar
day.

CountryDelay typeAustralia, India, Japan, Malaysia, New Zealand, Thailand,
United Arab Emirates, United StatesBusiness day (Monday - Friday)Brazil1,
Canada, Gibraltar, Hong Kong, Liechtenstein, Mexico, Norway, Singapore2,
Switzerland, United Kingdom, and supported EU countriesCalendar day (Sunday -
Saturday)
1 Delays for Pix, Boleto, debit, and prepaid payouts in Brazil apply in business
days.

2 Delays for PayNow in Singapore apply in business days.

### Payout speed by country

Use the following table to determine your country’s payout speed. The initial
payout speed applies until an account meets eligibility criteria for
[accelerated
payouts](https://docs.stripe.com/payouts#accelerated-payout-speeds).

### Country and payout speed

## Minimum payout amounts

The minimum payout amount depends on the lowest amount we can support with our
banking partners. For example, if you’re located in the US and you have less
than 1 cent (0.01 of 1 dollar) USD in your Stripe account, you must wait until
you accept more payments and increase your balance before you can receive a
payout. If your available account balance is less than the minimum payout
amount, it remains in your Stripe account until your balance increases.

If you’re in a supported country, you can use [multi-currency
settlement](https://docs.stripe.com/payouts/multicurrency-settlement) to send a
payout to your local bank accounts in a foreign currency. For example, a French
user can now receive a USD payout in their French bank account instead of having
to pay for multiple currency exchanges.

Minimum payout amounts are typically one base unit of the local currency. See
the following collapsed table for a list of countries and their minimum payout
amounts:

### Minimum payout amounts per country

### Cross-border minimum payout amounts

[Minimum amounts for cross-border
payouts](https://docs.stripe.com/connect/cross-border-payouts/special-requirements#cbp-minimum-payout-amounts)
are typically one base unit of the recipient account’s local currency, but can
be higher. They don’t necessarily match the minimum amounts for regular payouts.

## Negative payouts

Each payout reflects your available account balance at the time it was created.
In some cases, you might have a negative account balance. For example, if you
receive 100 USD in payments but refund 200 USD of prior payments, your account
balance would be -100 USD. If you don’t receive further payments to balance out
the negative amount, Stripe creates a payout that *debits* your bank account.

Your bank account must support both credit and debit transactions so that Stripe
can perform any required payouts.

## Payout failures

If your bank account can’t receive a payout for any reason, your bank sends the
funds back to us. This returns an error with the [reason for the
failure](https://docs.stripe.com/api/payouts/failures). It can take up to 5
additional business days for your bank to return the payout and inform us that
it failed. If this happens, you’re notified by email and in the
[Dashboard](https://dashboard.stripe.com/test/payouts). To make sure that your
bank account details are correct, you need to re-enter them if a payout fails.
After you re-enter your bank account details, Stripe attempts to perform the
payout again at the next scheduled payout interval.

#### Caution

When a payout fails, it’s possible that its state initially shows as `paid` but
then changes to `failed` (within 5 business days).

Make sure that the bank account information you provide is correct because
Stripe sends the funds using the account information you enter. Therefore, if
you provide incorrect information (for example, a mistyped account number or an
incorrect routing number), Stripe might send payouts to the wrong bank account
and might not be able to recover the funds.

Any fees or losses that you incur due to incorrect information fall under your
responsibility. If your banking details are correct and the payout failure is
for other reasons, contact your bank. After you resolve any issues with your
bank, you can reactivate the payouts by clicking **Resume Payouts**. If you
don’t receive a payout from Stripe after clicking **Resume Payouts**, and
haven’t received a failure notification within a reasonable time frame, please
[contact us](https://support.stripe.com/contact).

## Instant Payouts

With [Instant Payouts](https://docs.stripe.com/payouts/instant-payouts), you can
instantly send funds to a supported debit card or bank account. You can request
Instant Payouts any time, including weekends and holidays, and funds usually
appear in the associated bank account within 30 minutes. New Stripe users aren’t
immediately eligible for Instant Payouts. You can check your
[eligibility](https://docs.stripe.com/payouts/instant-payouts#eligibility-and-daily-volume-limits)
in the
[Dashboard](https://dashboard.stripe.com/payouts/instant_payouts_eligibility).

## Payout fees

Stripe doesn’t charge you a fee to initiate normal payouts. However, most
[non-primary currency
payouts](https://docs.stripe.com/payouts/multicurrency-settlement), where you
pay out money in a currency other than your Stripe account’s local currency, do
incur Stripe fees.

## See also

- [Payout reconciliation
report](https://docs.stripe.com/reports/payout-reconciliation)
- [Financial reports](https://docs.stripe.com/reports/select-a-report)

## Links

- [Payouts FAQ](https://support.stripe.com/questions/payouts-faq)
- [pricing guide](https://www.stripe.com/pricing)
- [Dashboard](https://dashboard.stripe.com/test/payouts)
- [Connect](https://docs.stripe.com/connect)
- [Connect payouts](https://docs.stripe.com/connect/payouts-connected-accounts)
- [Payout settings](https://dashboard.stripe.com/account/payouts)
- [presenting and settling in multiple
currencies](https://docs.stripe.com/payouts/multicurrency-settlement)
- [presented](https://docs.stripe.com/currencies#presentment-currencies)
- [currency conversion](https://docs.stripe.com/currencies/conversions)
- [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)
- [except for Asia-Pacific (APAC)
markets](https://support.stripe.com/questions/default-start-of-day-for-asia-pacific-%28apac%29-payouts)
- [Cross-border payouts](https://docs.stripe.com/connect/cross-border-payouts)
- [Dashboard](https://dashboard.stripe.com/settings/payouts)
- [creating payouts](https://docs.stripe.com/api#create_payout)
- [configure accounts](https://docs.stripe.com/connect/manage-payout-schedule)
-
[delay_days](https://docs.stripe.com/connect/manage-payout-schedule#delay_days)
- [Minimum amounts for cross-border
payouts](https://docs.stripe.com/connect/cross-border-payouts/special-requirements#cbp-minimum-payout-amounts)
- [reason for the failure](https://docs.stripe.com/api/payouts/failures)
- [contact us](https://support.stripe.com/contact)
- [Instant Payouts](https://docs.stripe.com/payouts/instant-payouts)
-
[eligibility](https://docs.stripe.com/payouts/instant-payouts#eligibility-and-daily-volume-limits)
- [Dashboard](https://dashboard.stripe.com/payouts/instant_payouts_eligibility)
- [Payout reconciliation
report](https://docs.stripe.com/reports/payout-reconciliation)
- [Financial reports](https://docs.stripe.com/reports/select-a-report)