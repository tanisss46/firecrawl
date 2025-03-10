# Multi-currency settlement

## Accept, settle and pay out funds in multiple currencies.

Available in: 
Stripe automatically converts all incoming funds into the default currency of
your home country. With multi-currency settlement, you can configure your
account to accrue balances and get paid out in additional currencies without
incurring foreign exchange fees.

## Enable multi-currency settlement

To configure your account to receive settlement and pay out in multiple
currencies, configure the currencies and bank accounts in your
[Dashboard](https://dashboard.stripe.com/account/payouts).

![Bank accounts and currencies settings in the
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/bank-accounts-and-currencies-page.cd3a7a8bf6a23667bb5f45f2bf7e19c4.png)

### Configure settlement currencies

In your Payout Settings, click **Manage Currencies** to select the settlement
currencies you want to receive funds in. Balances accrue in each currency for
payments you accept in that currency.

### Attach bank accounts to receive payouts in local currencies

You must provide a separate supported bank account for each settlement currency
you configure to receive payouts in that currency. You must match the currency
of the bank account to the settlement currency. After you provide the
corresponding bank accounts, Stripe directs payouts from your multi-currency
balances to their respective bank accounts in the matching currency.

### Configure payout settings

After you meet a currency’s [minimum payout
amount](https://docs.stripe.com/payouts/multicurrency-settlement#multicurrency-settlement-fees),
payouts follow your configured [payout
schedule](https://docs.stripe.com/connect/manage-payout-schedule), whether
manual or automatic. You can’t pay out until your balance for the currency meets
the minimum payout amount.

## Fees and minimum payout amounts for multi-currency settlement

Viewing supported settlement currencies for Stripe accounts in:Australia
(AU)Austria (AT)Belgium (BE)Bulgaria (BG)Croatia (HR)Cyprus (CY)Czech Republic
(CZ)Denmark (DK)Estonia (EE)Finland (FI)France (FR)Germany (DE)Gibraltar
(GI)Greece (GR)Hong Kong (HK)Hungary (HU)Ireland (IE)Italy (IT)Latvia
(LV)Liechtenstein (LI)Lithuania (LT)Luxembourg (LU)Malta (MT)Netherlands
(NL)Norway (NO)Poland (PL)Portugal (PT)Romania (RO)Singapore (SG)Slovakia
(SK)Slovenia (SI)Spain (ES)Sweden (SE)Switzerland (CH)United Arab Emirates
(AE)United Kingdom (GB)United States (US)Accounts created in United States can
receive payouts in the following non-local settlement currencies.Payouts in
these currencies to bank accounts in the US are currently in beta. [Please reach
out to us](https://support.stripe.com/) if you are interested in this
feature.Settlement currencyCan be paid out to banks in these countriesMinimum
manual payout amountMinimum auto payout amountPricingCADCanada$300.00 CAD$300.00
CAD1% or minimum fee of $3.00 cadEURAustria, Belgium, Bulgaria, Croatia, Cyprus,
Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece,
Hungary, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta,
Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain,
Sweden, Switzerland, United Kingdom€200.00 EUR€200.00 EUR1% or minimum fee of
€2.00 eurGBPAustria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic,
Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hungary, Ireland,
Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway,
Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland,
United Kingdom£200.00 GBP£200.00 GBP1% or minimum fee of £2.00 gbp
If your business is based in a currently ineligible country for multi-currency
settlement, [contact support](https://support.stripe.com/) to help us with
expansion planning.

## See also

- [Supported currencies](https://docs.stripe.com/currencies)
- [Currency conversions](https://docs.stripe.com/currencies/conversions)

## Links

- [Connect Docs](https://docs.stripe.com/connect/multicurrency-settlement)
- [Dashboard](https://dashboard.stripe.com/account/payouts)
- [payout schedule](https://docs.stripe.com/connect/manage-payout-schedule)
- [Please reach out to us](https://support.stripe.com/)
- [Supported currencies](https://docs.stripe.com/currencies)
- [Currency conversions](https://docs.stripe.com/currencies/conversions)