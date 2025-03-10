# Data reconciliation with Stripe reports

## Learn how to reconcile Revenue Recognition data with other financial reports.

You can reconcile the cash account from Revenue Recognition and the **Balance
change from activity** report within the same month. Because Revenue Recognition
focuses on revenue-generating activities, you must exclude fees, network costs,
contributions, and financing paydowns from the **Balance change from activity**
report before reconciling. To get the cash amount in Revenue Recognition,
download the balance sheet report in the summary format.

#### Note

The balance sheet report doesn’t take corrections into account. If there were
corrections issued for the month for which you’re attempting to reconcile
reports, you must also consider the Revenue Recognition corrections summary
reports for all subsequent months. Any corrections that would have been booked
to the `original_accounting_period` of the reconciliation month must be factored
into the Revenue Recognition cash amount.

## Example

As an example, the balance sheet report might look like the following, with a
100 USD amount:

accountcurrencynet changeCashusd+100.00Casheur+15.00
To get the cash amount in the **Balance change from activity** report, set the
currency to USD, and the report timezone to UTC.

After downloading the report in the summary format, it might look like the
following:

reporting
categorycurrencygross`charge`usd+140.00`refund`usd-40.00`refund_failure`usd+20.00`partial_capture_reversal`usd-20.00`fee`usd-10.00`network_cost`usd-10.00`contribution`usd-10.00`financing_paydown`usd-10.00`total`usd+60.00
The total gross amount excludes some Stripe fees. After deducting rows for
additional Stripe fees, network costs, contributions, and financing paydowns,
the calculated cash amount is 100 USD.

## Journal entries

The journal entries in the **Debits and credits** report don’t consider fees,
network costs, contributions, and financing paydowns. However, you can use
Stripe fees in your Revenue Recognition reporting to create journal entries for
these items.

#### Note

To enable Stripe fees support in Revenue Recognition, [create a
ticket](https://support.stripe.com/contact/email?topic=financial_reports) on our
support page. When you enable this feature, the journal entries in the **Debits
and credits** report automatically incorporate fees, network costs, and
contributions.

With Stripe fees enabled, you can do the following to reconcile Revenue
Recognition fees with the [Balance change from
activity](https://docs.stripe.com/reports/balance) report:

- Download the **Balance change from activity** report in the summary format.
Make sure you select these columns: **Reporting Category**, **Gross**, and
**Fee**.
- Calculate the total fee by summing the values in these columns:- **Gross**
column: fee, network cost, and contribution
- **Fee** column: total

In the following example, you calculate the total fees: `-1000.00 + -0.50 +
-0.40 + -1.00` to get the sum: `-1001.90`.

reporting categorygrossfee`charge`100.00-4.00`refund`-100.003.00`platform
earning refund`-0.100.00`fee`-1000.000.00`network
cost`-0.500.00`contribution`-0.400.00`total`-1001.00-1.00
If you download the **Debits and credits** report in the summary format, you can
see `1001.90` debited from the Fees expense account and credited to the Cash
account.

debitcreditamountFeesCash1001.90
#### Note

The debits and credits report doesn’t take corrections into account. If there
were corrections issued for the month for which you’re attempting to reconcile
reports, you must also consider the Revenue Recognition corrections summary
reports for all subsequent months. Any corrections that would have been booked
to the `original_accounting_period` of the reconciliation month must be factored
into the Revenue Recognition cash amount.

## Links

- [create a
ticket](https://support.stripe.com/contact/email?topic=financial_reports)
- [Balance change from activity](https://docs.stripe.com/reports/balance)