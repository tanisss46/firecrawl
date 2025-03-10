# Choose a calculation method

## Learn about the calculation methods for reporting charges and payouts.

The Stripe 1099 tax reporting product allows platforms to select a calculation
method, depending on the type of 1099 form they must file. While these
calculation methods reflect the most common reporting scenarios, you can import
CSV files and edit the amount on each 1099 form to better match the
requirements.

#### Note

Stripe recommends that you consult a tax advisor to determine your tax filing
and reporting requirements.

Available calculation method1099-K1099-MISC1099-NECPayments including
feesYesYesYesPayments excluding feesYesYesYesPayouts onlyYesYes
## Payments including fees

This payment calculation method includes all charges and transfers *including*
any fees related to each transaction. Such fees might be:

- Stripe processing and foreign currency conversion fees
- Platform fees

For Form 1099-K, the IRS requires reporting [gross reportable
amounts](https://www.irs.gov/instructions/i1099k#idm140262090779520) without any
adjustments. It’s the taxpayer’s responsibility to determine their taxable
income by taking into account their business expenses and deductions.

Depending on your business, you may determine this payment calculation method is
also appropriate for the amounts on their Forms 1099-MISC or 1099-NEC.

#### Note

Refunded charges aren’t deducted when using this calculation method.

### Example 1

On December 31, 2020, a customer buys flowers for 100 USD from an online flower
shop. The flower shop is a connected account and the [destination
charge](https://docs.stripe.com/connect/destination-charges#flow-of-funds-app-fee)
uses the platform’s API key. The charge authorization and capture time are the
same since partial authorization wasn’t specified. The platform retains a 2 USD
platform fee and a 3.20 USD Stripe fee nets directly out of the connected
account’s charge.

On January 2, 2021, the issuing bank settles the money to Stripe. On January 7,
2021, a [payout](https://docs.stripe.com/payouts) occurs from the connected
account’s Stripe balance to their bank account, and includes the proceeds from
this sale. With this method, the platform can report 100 USD on their 1099 form
for 2021, and no amount for 2020.

DescriptionAmountCustomer charged100 USDIncrease in connected account’s Stripe
balance94.80 USDIncrease in platform account’s Stripe balance2 USDAmount
reported with this method100 USD
Assume the same conditions, but a [direct
charge](https://docs.stripe.com/connect/direct-charges#flow-of-funds-with-fees)
uses the connected account’s API key. With this method, the platform can report
the same 100 USD on their 1099 form for 2021.

### Example 2

Assume the same conditions as Example 1, but the connected account issues a
refund the same day as the charge because they’re unable to fulfill the order.
Ignore any potential Stripe fees for refunds.

DescriptionAmountCustomer charged100 USDCustomer refunded100 USDNet change in
connected account’s Stripe balance0 USDNet change in platform account’s Stripe
balance0 USDAmount reported with this method100 USD
With this method, the platform can report the same 100 USD on their 1099 form
for 2021, and no amount for 2020.

## Payments excluding fees

This payment calculation method includes all charges and transfers *excluding*
any fees related to each transaction. Such fees might be:

- Stripe processing and foreign currency conversion fees
- Platform fees

This method is useful if the platform wants to remove their fee from the amount
reported for the connected account.

For example, in the [destination
charge](https://docs.stripe.com/connect/destination-charges#flow-of-funds-app-fee)
flow, the application fee is attributed to the connected account, but a platform
might pass the application fee to the end customer to pay the platform. Those
funds aren’t necessarily attributable or even known to the connected account.
While platforms acknowledge that gross amounts should be reported to their
connected accounts on the Form 1099-K, they might think the gross amount to
report should be payments excluding fees.

For Form 1099-K, the IRS requires reporting gross amounts for all reportable
transactions, without any adjustments for refunds, fees, credits, cash
equivalents, or discounts. Because platforms use
[Connect](https://docs.stripe.com/connect) differently, we recommend working
with a tax advisor to determine if this method is right for you based on the
1099 form you want to file.

Depending on your business, you may determine this payment calculation method is
also appropriate for the amounts on their Forms 1099-MISC or 1099-NEC.

#### Note

Stripe doesn’t deduct refunded charges when using this calculation method.

### Example

On December 31, 2020, a customer buys flowers for 100 USD from an online flower
shop. The flower shop is a connected account and the [destination
charge](https://docs.stripe.com/connect/destination-charges#flow-of-funds-app-fee)
uses the platform’s API key. The destination charge specifies an amount of 100
USD and a `transfer_data[amount]` of 94.80 USD. The charge authorization and
capture time are the same since partial authorization wasn’t specified. The
platform retains a 2 USD platform fee and a 3.20 USD Stripe fee nets directly
out of the connected account’s charge.

On January 2, 2021, the issuing bank settles the money to Stripe. On January 7,
2021, a payout occurs from the connected account’s Stripe balance to their bank
account, and includes the proceeds from this sale. With this method, the
platform can report 94.80 USD on their 1099 form for 2021, and no amount for
2020.

DescriptionAmountCustomer charged100 USDIncrease in connected account’s Stripe
balance94.80 USDIncrease in platform account’s Stripe balance2 USDAmount
reported with this method94.80 USD
Assume the same conditions, but the [destination
charge](https://docs.stripe.com/connect/destination-charges#flow-of-funds-app-fee)
specifies an amount of 100 USD and an `application_fee_amount` of 5.20 USD. The
Stripe fee is deducted on the platform’s account from the 5.20 USD. With this
method, the platform can report the same 94.80 USD on their 1099 form for 2021.

Assume the same conditions, but a [direct
charge](https://docs.stripe.com/connect/direct-charges#flow-of-funds-with-fees)
uses the connected account’s API key. The direct charge specifies an amount of
100 USD and an `application_fee_amount` of 5.20 USD. With this method, the
platform can report the same 94.80 USD on their 1099 form for 2021.

## Payouts only

The payouts only method lets you report only the amount that was paid out to the
connected account’s bank account, minus any payout reversals. The amount may
also include payments that aren’t related to a specific charge transaction. This
calculation method takes into consideration `payouts` and not `charges`.

Because platforms use Connect differently, we recommend working with a tax
advisor to determine if this method is right for you based on the 1099 form you
want to file.

### Example

On December 31, 2020, a customer buys flowers for 100 USD from an online flower
shop. The flower shop is a connected account and the [destination
charge](https://docs.stripe.com/connect/destination-charges#flow-of-funds-app-fee)
uses the platform’s API key. The charge authorization and capture time are the
same since partial authorization wasn’t specified. The platform retains a 2 USD
platform fee and a 3.20 USD Stripe fee nets directly out of the connected
account’s charge.

On January 2, 2021, the issuing bank settles the money to Stripe. On January 7,
2021, a payout of 94.80 USD occurs from the connected account’s Stripe balance
to their bank account, and includes the proceeds from this sale. With this
method, the platform can report 94.80 USD on their 1099 form for 2021, and no
amount for 2020.

DescriptionAmountCustomer charged100 USDIncrease in connected account’s Stripe
balance94.80 USDIncrease in platform account’s Stripe balance2 USDAmount
reported with this method (2020)0 USDAmount reported with this method
(2021)94.80 USD
Assume the same conditions, but a [direct
charge](https://docs.stripe.com/connect/direct-charges#flow-of-funds-with-fees)
uses the connected account’s API key. On January 7, 2021, a payout of 94.80 USD
occurs from the connected account’s Stripe balance to their bank account, and
includes the proceeds from this sale. With this method, the platform can report
the same 94.80 USD on their 1099 form for 2021.

## Additional calculation method topics

The following sections discuss calculation method topics that might be
applicable to your platform.

### Transactions included in calculations for the account

The inclusion of transactions in the Form 1099 calculations for the forms you
will issue depends on the connected account’s `controller.fees.payer` property.

- Transactions on accounts where `controller.fees.payer` = `application_custom`
or `application_express` are included in the calculations.
- Transactions on accounts where `controller.fees.payer` = `application` could
be included if the application fees for those transactions are paid to the
platform. Otherwise, the transactions could be included in a Stripe-issued 1099.
- Transactions on accounts where `controller.fees.payer` = `account` won’t be
included, but instead could be included in a Stripe-issued 1099 to the account.

### Timing and recognition of transactions

Stripe uses the [available_on
date](https://docs.stripe.com/api/balance_transactions/object#balance_transaction_object-available_on)
of the balance transaction associated with the payment to determine which tax
year the transaction belongs to. The `available_on` date represents the date the
funds become available in the Stripe account. We believe this approach best
matches the IRS’s instructions.

### Card not present payments

IRS Form 1099-K box “1b” reports the volume of “card not present” payments.
Stripe classifies a payment as “card present” or “card not present” based on the
[PaymentMethod
type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
associated with that payment. The following PaymentMethod `type` values are
“card present”. All others are “card not present”:

- `card_present`
- `interac_present`

### Tax form totals

We recommend that platforms audit Stripe transactions that have contributed to a
form’s totals by [exporting the transaction
log](https://docs.stripe.com/connect/calculation-methods#export-transaction-logs).

Account transactions performed outside of Stripe aren’t included in form totals.
To include non-Stripe transactions, platforms must manually adjust the form box
amounts before filing.

Transactions created with the [Transfers
API](https://docs.stripe.com/api/transfers) to credit connected accounts (for
example, handling dispute reversals and refund failures) are included in 1099-K
form totals. Debits from connected accounts are excluded. To remove these credit
transfers from the form, platforms must manually adjust the form box amounts
before filing.

### Separate charges and transfers

Stripe derives the reportable amount for a separate charge and transfer from the
transfer, not the charge.

Additionally, you must use the [source_transaction
parameter](https://docs.stripe.com/api/transfers/object#transfer_object-source_transaction)
to associate a charge with a transfer from your platform to a connected
account—Stripe classifies any transfers without this parameter as “card not
present” transactions.

If you initially created a separate charge and transfer with a link from the
transfer to the charge and later updated the `Charge` object to include the
transfer, we treat it like a destination charge in calculations. The gross
amount on your draft form might change if you’ve opted to include fees, as we’ll
now include the charge in our considerations.

### Foreign exchange rate conversions

Stripe’s 1099 calculation methods convert non-USD transactions to USD using the
market exchange rate from the day the transaction is created. This method might
yield a different value than the Stripe Dashboard shows because we compute that
value using an intra-day exchange rate adjusted for Stripe’s foreign exchange
fee.

### Cancelled asynchronous payments

If a user cancels an asynchronous payment (for example, ACH debit) that would’ve
otherwise been successful before the payment completes, that payment might still
be included in the results of the “payments including fees” and “payments
excluding fees” methods.

## Export transaction logs

For tax year 2022 and later, you can use the [Stripe
Dashboard](https://dashboard.stripe.com/connect/taxes/forms) to export the
transaction log of each 1099 form. A transaction log lists the Stripe
transactions that have contributed to a form’s total. This log allows you to
audit transaction discrepancies and answer questions from your connected
accounts about which transactions Stripe includes in their tax forms.

After you export the transaction log, the sum of its **Calculation Amount**
column reflects the form total that you see on the 1099. For each transaction,
we show the applicable **merchant_id**, **balance_transaction_id**,
**charge_id**, and **transfer_id** along with the calculation amount relevant to
that transaction. The calculation amount is dependent on the type of calculation
method you choose. The 1099-K form transaction logs list
**card_not_present_volume** and **transaction_count** to match the values on the
form.

#### Note

Transaction logs only contain Stripe transactions. [Manual
updates](https://docs.stripe.com/connect/modify-tax-forms) through CSV imports
or the Dashboard’s Tax form editor won’t be included in the transaction log.

To export the transaction log of a tax form:

- Navigate to the [Tax
reporting](https://dashboard.stripe.com/connect/taxes/forms) page in the
Dashboard.
- Select the checkbox next to the tax form.
- Click the overflow menu () at the top-right of the tax form and select
**Export transaction log**.
- Specify the date range and rows that you want to export. Use the default
export settings to capture all the details of the entire year. The transaction
log file downloads in your browser. Keep the email notification option selected
if you want to receive an email containing a link to download your transaction
log.

The transaction log file downloads after Stripe finishes the export process. If
you exported with the email notification option selected, Stripe also sends you
an email from `notification@stripe.com` with a link to download your transaction
log.

## Links

- [gross reportable
amounts](https://www.irs.gov/instructions/i1099k#idm140262090779520)
- [destination
charge](https://docs.stripe.com/connect/destination-charges#flow-of-funds-app-fee)
- [payout](https://docs.stripe.com/payouts)
- [direct
charge](https://docs.stripe.com/connect/direct-charges#flow-of-funds-with-fees)
- [Connect](https://docs.stripe.com/connect)
- [available_on
date](https://docs.stripe.com/api/balance_transactions/object#balance_transaction_object-available_on)
- [PaymentMethod
type](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
- [exporting the transaction
log](https://docs.stripe.com/connect/calculation-methods#export-transaction-logs)
- [Transfers API](https://docs.stripe.com/api/transfers)
- [source_transaction
parameter](https://docs.stripe.com/api/transfers/object#transfer_object-source_transaction)
- [Stripe Dashboard](https://dashboard.stripe.com/connect/taxes/forms)
- [Manual updates](https://docs.stripe.com/connect/modify-tax-forms)