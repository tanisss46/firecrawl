# Build a new Treasury integration with Fifth Third BankPublic preview

## Get started with Stripe Treasury.

This guide describes how to get started with Stripe Treasury using Fifth Third
Bank.

## Before you integrate

### Test mode

You can request access to use test mode immediately. Test mode operates
independently of any specific bank partner.

Before you create financial accounts in live mode for your Treasury integration,
we recommend that you create test financial accounts in test mode. Test mode
financial accounts can’t receive or send real money, and don’t generate a live
account with real routing and account information, but are otherwise identical
in configuration and functionality.

If you create an `Account` object in test mode and want to bypass onboarding
requirements to test functionality, use `POST
/v1/accounts/{{CONNECTED_ACCOUNT_ID}}` to [provide test
values](https://docs.stripe.com/connect/testing-verification) that fulfill all
the requirements.

### Complete compliance reviews and update disclosures

To access Fifth Third in live mode, you must first submit evidence of the
following to Stripe’s compliance team for approval:

- Any live or planned UX, or marketing that names a bank partner
- Any mentions of FDIC pass-through insurance eligibility
- UX including user balances with disclosures, bank statements, and transaction
history

You must send previews of your planned updates using the [Compliance Intake
Form](https://form.asana.com/?k=8K51UWmWhttehNFD5qBLdg&d=974470123217835). After
Stripe’s compliance team completes the review, we’ll grant you access to Fifth
Third in live mode. Then, you can publish your approved disclosures.

You must follow all of the Treasury [compliance
guidelines](https://docs.stripe.com/treasury/compliance), including [regulatory
receipts](https://docs.stripe.com/treasury/moving-money/regulatory-receipts),
[complaints](https://docs.stripe.com/treasury/handling-complaints), and
[marketing guidelines](https://docs.stripe.com/treasury/marketing-treasury).

### Bank partner disclosures

You must include proper disclosures that funds are held with Fifth Third Bank.
You must include disclosures on marketing assets, landing pages, other websites,
dashboards, social media posts, or any other interface that references Stripe
Treasury.

Make sure that your disclosure reads: “[*Company Name*] partners with Stripe
Payments Company for money transmission services and account services with funds
held at Fifth Third Bank, Member FDIC.”

### FDIC pass-through insurance eligibility disclosures

In any place you reference FDIC pass-through insurance eligibility, you must
accompany that text with the approved disclosure language from Fifth Third Bank:

“Stripe Treasury Accounts are eligible for FDIC pass-through deposit insurance
if they meet certain requirements. The accounts are eligible only to the extent
passthrough insurance is permitted by the rules and regulations of the FDIC, and
if the requirements for pass-through insurance are satisfied. The FDIC insurance
applies up to 250,000 USD per depositor, per financial institution, for deposits
held in the same ownership capacity.”

### Viewing multiple balances

If you plan to allow connected accounts to store multiple balances, you must
display balances separately within any dashboard user interface or servicing
communications disclosing balances.

## Feature availability on Fifth Third Bank

The following Treasury features are available when integrating with Fifth Third
Bank.

CategoryFeatureOnboard and store funds with Fifth Third Bank [Onboard connected
accounts](https://docs.stripe.com/treasury/account-management/connected-accounts)
compliantly[Create financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
at Fifth Third Bank that are eligible for FDIC pass-through insurance[Close
financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts#close-a-financialaccount)
with Fifth Third using the APIFinancial accounts come with a Stripe
FinancialAccount IDFinancial accounts can request an externally addressable
account number and routing number
([financial_addresses.aba](https://docs.stripe.com/treasury/account-management/financial-account-features#available-features)),
enabling them to receive external credits and debitsOriginate Transactions for
the financial account Connected account can move funds
([OutboundTransfer](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-transfers))
from the Fifth Third financial account to other financial accounts (Evolve or
Fifth Third Bank) using the Stripe networkConnected accounts can originate
credits
([OutboundTransfer](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-transfers)
or
[OutboundPayment](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments))
out from the financial account using standard or
[same-day](https://docs.stripe.com/treasury/account-management/financial-account-features#same-day-ach)
ACH or wireConnected accounts can originate debits
([InboundTransfer](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/inbound-transfers))
that draw funds from accounts they own into the financial account using standard
or
[same-day](https://docs.stripe.com/treasury/account-management/financial-account-features#same-day-ach)
ACH (self-to-self)Remote deposit capture for check deposit (beta)Payouts from
Stripe Payments You or your connected accounts can acquire funds using Stripe
Payments, then create
[Payouts](https://docs.stripe.com/treasury/moving-money/payouts) into the Fifth
Third financial account (others-to-self)You or your connected accounts can
create [instant
payouts](https://docs.stripe.com/treasury/moving-money/payouts#manual-payout-speeds)
to access pending fundsReceive Transactions into the financial account Financial
accounts can receive credits
([ReceivedCredit](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/received-credits))
using ACH or wireFinancial accounts can receive debits
([ReceivedDebit](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/received-debits))
using ACH, and can create returns
([DebitReversal](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/debit-reversals))Fund
Issuing cards
[Issuing](https://docs.stripe.com/treasury/account-management/issuing-cards)
cards can be funded by the Fifth Third financial accountAn existing Issuing card
can be updated to point to a different financial account
Accounts that have migrated to Fifth Third don’t yet support
[CreditReversals](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/credit-reversals).
When that feature becomes available, we’ll notify you.

If you request a [financial account
Feature](https://docs.stripe.com/treasury/account-management/financial-account-features)
that hasn’t been released for Fifth Third Bank, Stripe returns the following
error: “You cannot request `{feature}` on a financial account with bank
`fifth_third`”.

#### Note

The roadmap above outlines our general product direction and current priorities
for informational purposes only. It’s not a commitment to deliver any material,
code, or functionality, and you shouldn’t rely on it when making purchasing
decisions. The development, release, and timing of any features or functionality
described for Stripe’s products remain at Stripe’s sole discretion.

## Get started with Treasury

You can use the existing [Treasury
documentation](https://docs.stripe.com/treasury) to guide your integration. You
can use the same APIs with your Fifth Third financial account. Below is a list
of expected differences with Fifth Third Bank.

- You receive a [platform financial
account](https://docs.stripe.com/treasury/account-management/platform-financial-account)
at Fifth Third Bank.
- Outbound transfers sent using wire or ACH from a Fifth Third financial account
have later cutoff times than today’s transfers sent with Evolve.
EvolveFifth Third BankWires4:00pm ET5:00pm ETACH7:00pm ET8:30pm ETSame-day
ACH12:00pm ET1:00pm ET- Stripe Payouts sent from the payments balance will
arrive into a Fifth Third financial account faster than today’s payouts into an
external bank account or an Evolve financial account.
External payouts and payouts to Evolve financial accountsPayouts to Fifth Third
financial accountsStandard manual payoutSettled funds arrive in approximately 1
day. Acquired funds arrive approximately 2–3 days after pay-in capture.
Available during business hours only.Settled funds arrive within 2 hours.
Acquired funds arrive approximately 1-2 days after pay-in capture. Available at
any time, including weekends and holidays.Instant manual payoutWithin 1
hourWithin 1 hourStandard automatic payout schedule (`delay_days=2`)Settled
funds arrive approximately 2–3 days after pay-in capture. Available on business
days only.Settled funds arrive approximately 1–2 days after pay-in capture.
Available on business days only.Accelerated automatic payout schedule
(`delay_days=1`)Settled funds arrive approximately 1 day after pay-in capture.
Available on business days only.Settled funds arrive approximately 1 day after
pay-in capture. Available on business days only.
There might be additional [near-term
differences](https://docs.stripe.com/treasury/fifth-third-get-started#feature-availability-on-fifth-third)
while we build Fifth Third Bank to parity with Evolve. For example.

- Received debits: For now, you can only receive debits up to 500,000 USD per
transaction. If an external party originates a debit for an amount exceeding
500,000 USD, Stripe originates a return with the R29 ACH return code. You won’t
see any impact to your balance, and the received debit won’t appear in your
transaction list. When we remove this limit, we’ll notify all platforms that
have gone live with Fifth Third and receive debits.
- DebitReversals and CreditReversals: You must create a DebitReversal within 24
hours; we’ll extend this window in the coming months.

## Links

- [provide test values](https://docs.stripe.com/connect/testing-verification)
- [Compliance Intake
Form](https://form.asana.com/?k=8K51UWmWhttehNFD5qBLdg&d=974470123217835)
- [compliance guidelines](https://docs.stripe.com/treasury/compliance)
- [regulatory
receipts](https://docs.stripe.com/treasury/moving-money/regulatory-receipts)
- [complaints](https://docs.stripe.com/treasury/handling-complaints)
- [marketing guidelines](https://docs.stripe.com/treasury/marketing-treasury)
- [Onboard connected
accounts](https://docs.stripe.com/treasury/account-management/connected-accounts)
- [Create financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
- [Close financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts#close-a-financialaccount)
-
[financial_addresses.aba](https://docs.stripe.com/treasury/account-management/financial-account-features#available-features)
-
[OutboundTransfer](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-transfers)
-
[OutboundPayment](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments)
-
[same-day](https://docs.stripe.com/treasury/account-management/financial-account-features#same-day-ach)
-
[InboundTransfer](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/inbound-transfers)
- [Payouts](https://docs.stripe.com/treasury/moving-money/payouts)
- [instant
payouts](https://docs.stripe.com/treasury/moving-money/payouts#manual-payout-speeds)
-
[ReceivedCredit](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/received-credits)
-
[ReceivedDebit](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/received-debits)
-
[DebitReversal](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/debit-reversals)
- [Issuing](https://docs.stripe.com/treasury/account-management/issuing-cards)
-
[CreditReversals](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/credit-reversals)
- [financial account
Feature](https://docs.stripe.com/treasury/account-management/financial-account-features)
- [Treasury documentation](https://docs.stripe.com/treasury)
- [platform financial
account](https://docs.stripe.com/treasury/account-management/platform-financial-account)