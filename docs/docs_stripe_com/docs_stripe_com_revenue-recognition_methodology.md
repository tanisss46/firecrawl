# Revenue Recognition methodology

## Learn how Revenue Recognition works within Stripe.

Revenue Recognition is integrated with other Stripe objects to provide
intelligent default settings for how to recognize revenue.

Revenue Recognition automatically calculates all transactions that happen within
Stripe down to the millisecond, including subscriptions, invoices, one-time
payments, refunds, disputes, and so on.

## Chart of accounts

Stripe built Revenue Recognition on top of a double-entry accounting ledger that
tracks debits and credits resulting from your business activity.

To get the most out of Revenue Recognition, it helps to understand the default
chart of accounts and the debits and credits that impact those accounts.

Income statement accountsBalance sheet accountsAccount Debit or Credit type
Description RevenueRevenue (credit)Recognizable portion of finalized invoices,
prorated invoice items, and metered billing that count towards revenue during
the month. For example, if an invoice line item is for 90 USD with 10 USD in
taxes, the total invoice is 100 USD, but the recognizable portion is only 90
USD.RefundsContra revenue (debit)Portion of the refunded amount previously
recognized. For example, if you issue a 120 USD refund on an annual subscription
during the second month, 20 USD for the first 2 months is contra revenue. The
remaining 100 USD is adjusted and reflected in your deferred revenue balance in
the balance sheet.DisputesContra revenue (debit)Portion of the disputed amount
previously recognized. For example, if there’s a 120 USD dispute on an annual
subscription during the second month, 20 USD for the first 2 months is contra
revenue. The remaining 100 USD is adjusted and reflected in your deferred
revenue balance in the balance sheet.Credit notesContra revenue (debit)Portion
of the credit note amount previously recognized. For example, if there’s a 120
USD credit note on an annual subscription during the second month, 20 USD for
the first 2 months is contra revenue. The remaining 100 USD is adjusted and
reflected in your deferred revenue balance in the balance sheet.Bad debtContra
revenue (debit)Previously recognized revenue from invoices that have been marked
as uncollectible.VoidsContra revenue (debit)Previously recognized revenue from
invoices that have been voided.Unbilled voidsContra revenue (debit)Previously
recognized revenue from prorated invoice items that have been deleted. These
items are sometimes deleted when they generate unbilled accounts receivable and
revenue.TransferContra revenue (debit)Previously recognized revenue from
separate transfers.DiscountsContra revenue (debit)Recognized revenue from
invoices that received discounts. Revenue Recognition discount as contra revenue
support is currently in private beta.Customer balance adjustmentsExpense
(debit)Expenses incurred due to manual adjustments to a customer credit balance
or exclusion associated with post-paid credit notes on customer balance.External
customer balance adjustmentsExpense (debit)Expenses incurred due to exclusion
associated with post-paid credit notes on external customer
balance.UnderpaymentsExpense (debit)Expenses incurred due to transfers that
underpay an invoice, as used by the [customer credit
balance](https://docs.stripe.com/invoicing/bank-transfer#underpayments) payment
method or [Sources](https://docs.stripe.com/sources/customers).FeesExpenses
(debit)Expenses incurred due to Stripe fees.RecoverablesGains (credit)Recovered
funds that aren’t attributable to revenue. For example, if you have a 120 USD
dispute on an annual subscription during the second month, 20 USD for the first
2 months is contra revenue and the remaining 100 USD is adjusted from the
deferred revenue balance. If you win the dispute and 120 USD is returned to you,
20 USD is reflected as revenue and the remaining 100 USD is reflected as
recoverables.ExclusionGains (credit)Excluded funds that aren’t attributable to
revenue. To exclude transactions, set up [exclusion
rules](https://docs.stripe.com/revenue-recognition/rules/create-a-rule#treatments)
or use [exclusion
import](https://docs.stripe.com/revenue-recognition/data-import#exclusion-import).Fx
lossLoss (debit)Total loss due to foreign currency exchange rates.Other lossLoss
(debit)The portion of contra revenue that exceeds the total invoice represents
an overcompensation in cash to the customer. For example, if a 100 USD invoice
is partially refunded by 80 USD and then disputed for an additional 80 USD, 60
USD will be categorized as “Other loss.”Connect transfer lossLoss (debit)Total
loss due to destination charge refund, and the transfer reversal will reverse
the ConnectTransferLoss account.
## Data modeling for Revenue Recognition

See the following descriptions of how Revenue Recognition handles common Stripe
resources to learn how Revenue Recognition uses data modeling.

### Subscriptions and Invoicing

Subscriptions and Invoices are higher level resources that contain detailed
information about each transaction.

Subscriptions create invoices on each cycle, with each subscription item
corresponding to an invoice line item. The period of each line item is
automatically populated with the period of the subscription item.

Revenue Recognition treats each invoice line item as its own performance
obligation. When the invoice finalizes, the total recognizable amount is
deferred and subsequently amortized evenly over the period of each invoice line
item.

If a period isn’t set on an invoice line item, the amount on that invoice line
item is recognized entirely when the invoice is finalized. Use the [Data Import
feature](https://docs.stripe.com/revenue-recognition/data-import) to configure
your invoice data, or set
[rules](https://docs.stripe.com/revenue-recognition/rules) to customize when and
how invoice line items are recognized.

For more details and examples regarding how Revenue Recognition handles
subscriptions and invoices with specific scenarios involving upgrades,
downgrades, discounts, taxes, and so on, review the [Subscriptions and
Invoicing](https://docs.stripe.com/revenue-recognition/methodology/subscriptions-and-invoicing)
page.

### One-time payments

One-time payments created in the Dashboard or through the
[Charges](https://docs.stripe.com/api/charges) and
[PaymentIntents](https://docs.stripe.com/api/payment_intents) APIs don’t contain
as much information as invoices.

Because no service period or fulfillment information exists for them, by
default, one-time payments are recognized immediately when the payment occurs.

[Import data](https://docs.stripe.com/revenue-recognition/data-import) to add a
service period or split a payment into different revenue recognition schedules.
This allows you to customize revenue treatment behavior and configure rules such
as payment amount, description, and customer email.

For more details and examples on how Revenue Recognition handles one-time
payments, review the [One-time
payments](https://docs.stripe.com/revenue-recognition/methodology/one-time-payments)
page.

### Refunds and disputes

Revenue Recognition handles refunds and disputes by generating contra revenue to
offset already recognized revenue.

For transactions with both already-recognized and deferred revenue, the
recognized portion is added to either the refunds or disputes contra revenue
account, which cancels out the deferred revenue.

For more details and examples on how Revenue Recognition handles refunds and
disputes, review the [Refunds and
Disputes](https://docs.stripe.com/revenue-recognition/methodology/refunds-and-disputes)
page.

### External transactions

You can track revenue collected outside of Stripe using invoices. Configure the
invoice as you would any other, and then mark the invoice as paid either
directly in the Dashboard, or through the `paid_out_of_band` option in the API.

Invoices marked as paid outside of Stripe contribute not to the cash account,
but rather to the external asset account.

#### Caution

If you’d like to consolidate your financial data from outside Stripe onto
Revenue Recognition, review the [Data
import](https://docs.stripe.com/revenue-recognition/data-import) page.

### Multi-currency

If your business handles transactions in multiple currencies, accurately
recognizing revenue can be complicated.

Revenue Recognition processes transactions and generates journal entries based
on your account’s settlement currencies. Transactions with presentment
currencies that aren’t supported as settlement currencies are automatically
converted to your account’s default settlement currency.

For payments and paid invoices, we use the exchange rate for the actual money
movement (that is, reflected on the balance transaction). If you incur a time
delay between issuing a bill (for example, an invoice) and it getting paid, the
difference in amounts because of changing exchange rates between the two times
is added to the FxLoss account.

For more details and examples on how Revenue Recognition handles multiple
currencies, review the
[Multi-currency](https://docs.stripe.com/revenue-recognition/methodology/multi-currency)
page.

### Data availability

Revenue Recognition computes your data twice daily, at 0:00am UTC and at 12:00pm
UTC.

The data processed at 0:00am UTC encompasses account activity from the prior
day’s 12:00pm to that day’s 11:59pm UTC. The 12:00pm UTC update covers activity
from 0:00am to 11:59am UTC of the same day.

It can take up to 24 hours to process the data. Users in time zones far from UTC
might notice slight delays in reports because late-day activity in PST
corresponds to early hours of the following day in UTC.

As an example, you might have account activity occurring on August 1, 2023, from
0:00 am to 11:59 am UTC. You can expect to see this activity reflected in the
Revenue Recognition reports by August 4, 2023, at 12:00 pm UTC. Similarly, you
can access reports for activity from 12:00 pm to 11:59 pm UTC on August 1, 2023
by August 5, 2023, at 0:00 am UTC.

## Journal entries

Every billing activity in Stripe generates a set of journal entries. A journal
entry is a record of a transaction. Each journal entry consists of a debit and a
credit account. For example, an entry which finalizes an invoice would debit
AccountsReceivable and credit DeferredRevenue. Paying an invoice would debit
Cash and credit AccountsReceivable.

These entries can occur in asset, liability, equity, expense, or revenue
accounts. You can learn more about the definitions of each account that will
appear in a journal entry under our [Chart of
accounts](https://docs.stripe.com/revenue-recognition/methodology#chart-of-accounts)
section.

The table below shows the applicable billing activities for common journal
entries. You can export journal entries to CSV using the debits and credits
report, which you can find in the [Reports tab in the
Dashboard](https://dashboard.stripe.com/revenue-recognition). In addition, there
are options to download debits and credits reports by the event type, which
provide a brief description of the recorded event, which can help you understand
the nature of each journal entry.

#### Caution

The following table isn’t the complete set of entries. We’ll be periodically
updating the entries. If there’s a specific entry that you require assistance
with, please [create a
ticket](https://support.stripe.com/contact/email?topic=financial_reports) on our
support page.

Debit Credit Definition Accounts receivableDeferred revenueInvoice being
finalizedUnbilled accounts receivableUnbilled invoice item being
invoicedPassthrough feesFinalize an invoice with passthrough feesTax
liabilityFinalize an invoice with taxBad debtAccounts receivableMark an invoice
as uncollectiblePending cashMark an invoice with a pending ACH as
uncollectibleRecoverablesMark an invoice which is partially paid with customer
balance as uncollectibleCashAccounts receivableInvoice is paidCustomer
balancePaying for a negative customer balanceExclusionCash is excludedPending
cashACH paying invoice is confirmedRecoverablesWinning a dispute for amounts
that were previously adjusted from deferred revenue balanceConnect transfer
lossCashLoss from a transferCredit notesAccounts receivablePrepaid credit note
is issued on an unpaid invoiceCustomer balancePost paid credit note credits
customer balanceExternal customer balancePost paid credit note credits external
customer balanceCustomer balanceCustomer balance adjustmentsReduce the amount
owned by the customerCustomer balance adjustmentsCustomer balanceIncrease the
amount owned by the customerDeferred revenueCashCaused by Refunds and
DisputesRevenueRevenue is recognizedExternal assetAccounts receivableMark an
invoice as paid outside of StripeRefundsCashRefundTax liabilityCustomer
balanceCredit note on an invoice with tax, and it credits customer
balanceExternal customer balanceCredit note on an invoice with tax, and it
credits external customer balanceUnbilled accounts receivableRevenueRevenue
recognized on unbilled invoice itemUnbilled voidsUnbilled accounts
receivableUnbilled invoice item is deletedVoidsAccounts receivableVoid an
invoiceBad debtVoid an uncollectible invoiceCustomer balanceVoid an invoice
partially paid with customer balance
The activities above are all based on positive amounts. It is important to note
that these billing activities can be reversed. These reverse activities occur
when activities are triggered on negative invoice line item amounts.

## Negative Line Item

A negative line item occurs when the value of the line item becomes higher than
the amount it is paid for. This occurs typically during a subscription downgrade
or upgrade when the product tier changes.

Here is an example of journal entries which contains a negative line item caused
by a downgrade:

- On April 1, the invoice is generated for a monthly subscription worth 90 USD
and the customer pays for it.
- On April 21, the customer requests a downgrade of their service to a 30 USD
subscription. This results in 2 unbilled line items for the remaining time of
the subscription.- il_1 is for the remaining time on new plan worth 10 USD
- il_2 is for the remaining time of old plan worth -30 USD
- On May 1, the invoice is generated containing the line items generated by the
downgrade as well for the new line item, il_3, representing the month of May.
The customer pays for the invoice on the same day.
- On May 4, the customer requests a full refund on the invoice for May,
resulting in full refunds on the line item created by the downgrade as well as
the new line item for May. We process the refund.
Date Debit Credit Amount Line Item 2022-04-21Unbilled accounts
receivableRevenue10 USDil_1RevenueUnbilled accounts receivable30
USDil_22022-05-01Accounts receivableDeferred revenue30 USDil_3CashAccounts
receivable30 USDil_3Deferred revenueRevenue30 USDil_3Accounts receivableUnbilled
accounts receivable10 USDil_1CashAccounts receivable10 USDil_1Unbilled accounts
receivableAccounts receivable30 USDil_2Accounts receivableCash30
USDil_22022-05-04RefundsCash10 USDil_1CashRefunds30 USDil_2RevenueCash30 USDil_3

## Links

- [customer credit
balance](https://docs.stripe.com/invoicing/bank-transfer#underpayments)
- [Sources](https://docs.stripe.com/sources/customers)
- [exclusion
rules](https://docs.stripe.com/revenue-recognition/rules/create-a-rule#treatments)
- [exclusion
import](https://docs.stripe.com/revenue-recognition/data-import#exclusion-import)
- [Data Import feature](https://docs.stripe.com/revenue-recognition/data-import)
- [rules](https://docs.stripe.com/revenue-recognition/rules)
- [Subscriptions and
Invoicing](https://docs.stripe.com/revenue-recognition/methodology/subscriptions-and-invoicing)
- [Charges](https://docs.stripe.com/api/charges)
- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
- [One-time
payments](https://docs.stripe.com/revenue-recognition/methodology/one-time-payments)
- [Refunds and
Disputes](https://docs.stripe.com/revenue-recognition/methodology/refunds-and-disputes)
-
[Multi-currency](https://docs.stripe.com/revenue-recognition/methodology/multi-currency)
- [Chart of
accounts](https://docs.stripe.com/revenue-recognition/methodology#chart-of-accounts)
- [Reports tab in the
Dashboard](https://dashboard.stripe.com/revenue-recognition)
- [create a
ticket](https://support.stripe.com/contact/email?topic=financial_reports)