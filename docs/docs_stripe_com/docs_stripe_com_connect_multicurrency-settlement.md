# Multi-currency settlement for Connect platforms and marketplaces

## Offer your connected accounts the ability to accept, settle and pay out funds in multiple currencies.

Available in: 
Multi-currency settlement allows your connected accounts to maintain balances
and make payouts in currencies other than their primary currency. Connected
accounts can hold and payout funds in up to 18 supported currencies needed to
pay suppliers, process refunds, and so on, without having to convert funds.

## Enable multi-currency settlement

Enable multi-currency settlement for your conneted accounts in the [Connect
payouts settings page](https://dashboard.stripe.com/settings/connect/payouts) of
the Dashboard. Your account must be in a supported region to access these
settings.

After you enable multi-currency settlement, your users can access all
[currencies that are supported in their
region](https://docs.stripe.com/payouts/multicurrency-settlement#multicurrency-settlement-fees).

#### Note

Connected accounts must be in the same region as your platform to use
multi-currency settlement. For example, both you and your connected account
could be in Australia, or, if you’re in Europe, your connected account could be
in any European country.

If you no longer want your connected accounts to use multi-currency settlement:

- Disable it with the same settings in the Dashboard to prevent connected
accounts from beginning to use it. This doesn’t disable it for connected
accounts that are already using multi-currency settlement.
- Remove any multi-currency external accounts using the [Delete external bank
accounts API](https://docs.stripe.com/api/external_account_bank_accounts/delete)
to disable multi-currency settlement for connected accounts already using it.

## Add external accounts

After you enable multi-currency settlement, your connected accounts can start
using it by adding a new settlement currency external account.

DashboardAPI
Your connected account can add an external account anywhere they can update
their payout methods, including Dashboard and Onboarding interfaces. See
[Connect account types](https://docs.stripe.com/connect/accounts) to learn which
interfaces are available for your connected account. For instance, if your
connected account has access to the Express Dashboard, you can send them a
[Login Link](https://docs.stripe.com/api/account/create_login_link) to update
their payout methods.

After your connected account has an external account in a non-primary currency,
charges presented in that currency accrue towards that currency’s balance. Your
connected accounts can pay out their multi-currency balances in the same way as
a primary currency balance. However, some supported currencies are subject to a
payout minimum and fee, as described in the following section.

To learn more about processing charges in multiple currencies with Connect, see
[Working with multiple currencies](https://docs.stripe.com/connect/currencies).

## Pricing

When funds settle to your connected account in a currency other than the primary
currency of your Stripe account country, Stripe applies [processing
fees](https://docs.stripe.com/currencies/settlement-fees) in that currency.

Stripe charges platforms a 1% payout fee for multi-currency settlement depending
on the combination of currency and bank account country, with a minimum fee. In
your Dashboard and reporting, this fee might appear as an *alternative currency
payout* fee. See our [full list of
fees](https://docs.stripe.com/payouts/multicurrency-settlement#multicurrency-settlement-fees).

Stripe deducts your connected accounts’ multi-currency settlement fees from your
platform balance in the non-primary currency. For example, if your connected
account pays out funds in USD, we charge the fee to your platform balance in USD
when possible. If your platform account doesn’t support the currency, Stripe
converts the fee to your default currency and deducts it from your primary
currency’s balance. See [conversion on Stripe
fees](https://docs.stripe.com/currencies/conversions#conversion-stripe-fees) for
more details.

## Request early access

Use the following form to request updates on preview features as we expand
multi-currency settlement features and regional support.

## Interested in getting early access to new multi-currency settlement features?

Enter your email address below and our team will contact you when we're ready to
provide access.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

- [configure multi-currency
settlement](https://docs.stripe.com/payouts/multicurrency-settlement)
- [configured with
properties](https://docs.stripe.com/connect/update-to-typeless-connect)
- [Connect payouts settings
page](https://dashboard.stripe.com/settings/connect/payouts)
- [currencies that are supported in their
region](https://docs.stripe.com/payouts/multicurrency-settlement#multicurrency-settlement-fees)
- [Delete external bank accounts
API](https://docs.stripe.com/api/external_account_bank_accounts/delete)
- [Connect account types](https://docs.stripe.com/connect/accounts)
- [Login Link](https://docs.stripe.com/api/account/create_login_link)
- [Working with multiple currencies](https://docs.stripe.com/connect/currencies)
- [processing fees](https://docs.stripe.com/currencies/settlement-fees)
- [conversion on Stripe
fees](https://docs.stripe.com/currencies/conversions#conversion-stripe-fees)
- [privacy policy](https://stripe.com/privacy)