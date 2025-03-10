# Export account activity to QuickBooks

## Download an export of your Stripe account data suitable for import into your desktop QuickBooks.

In addition to the CSV-formatted
[reports](https://docs.stripe.com/stripe-reports) that are available for export
in the Dashboard, information about payments, refunds, fees, and
[payouts](https://docs.stripe.com/payouts) is also available in a [QuickBooks
Desktop](http://quickbooks.intuit.com/)-compatible IIF file. You can download
this within the Dashboard’s [Legacy exports
settings](https://dashboard.stripe.com/account/legacy_exports).

You can also use [Accounting Stripe
Apps](https://marketplace.stripe.com/categories/accounting) to automate your
bookkeeping, keep your financial data updated, and eliminate the need for manual
data entry.

## QuickBooks accounts

The exported IIF file creates the following nine accounts in QuickBooks, if they
don’t already exist. All of the Stripe-created accounts are prefaced by
**Stripe** to make them easy to locate and identify.

NameTypeDescriptionStripe AccountBankAll charges, refunds, and payoutsStripe
Checking AccountBankRepresents your actual bank account to which Stripe sends
payoutsStripe Payment Processing FeesExpenseProcessing fees for all
chargesStripe ReturnsIncomeAll refundsStripe SalesIncomeAll charges minus
processing feesStripe Third-Party AccountTax-Related ExpenseEvery transfer to a
third-partyStripe Other FeesExpenseAdjustmentsStripe Processing Fees
AdjExpenseAdjustmentsStripe Other IncomeIncomeAdjustments
If these accounts already exist but are of a different type than what you see in
the exports file, QuickBooks presents an error about being unable to change the
account type. If this occurs edit the conflicting accounts to have the same type
as the IIF file.

#### Note

Always back up your QuickBooks data before importing new information.

## Date format and timezones

The IIF file formats the date as MM/DD/YYYY. QuickBooks uses the same date
format as your operating system. If this differs from the exported file, you can
temporarily change your operating system’s date format:

- Set the date format in your operating system to MM/DD/YYYY.
- Import the QuickBooks IIF file.
- Change your operating system’s date format back to your preferred style.

Your account’s [timezone setting](https://dashboard.stripe.com/settings/account)
is used for the date range of the IIF export.

## Merging QuickBooks accounts

You may want to merge one or more of these created accounts with an existing
QuickBooks account. In particular, you may want to merge the **Stripe Checking
Account**, which represents the bank where your Stripe payouts are sent, with
your actual banking account in QuickBooks:

- Select **Lists > Chart of Accounts** to view all of your accounts.
- Make sure both accounts being merged are on the same level (that is, both can
be sub-accounts or both can be primary level accounts).
- Select the account you are no longer going to use (for example, **Stripe
Checking Account**).
- Click **Account > Edit Account** at the bottom of the **Chart of Accounts**
window.
- Change the name of this account to exactly match the name of the other account
(the one you’ll be keeping).
- Click **Save**.

You’re then prompted about merging the account with an existing one. Click
**Yes** to proceed with the merge, **No** to cancel. The records in the renamed
account will be merged into the retained account. Accounts need to be re-merged
after each new import.

## Considerations for Connect platforms with Custom accounts

Platform owners with Custom accounts can view the Dashboard of connected Stripe
accounts. From the connected account’s Dashboard, export an IIF file in the same
way as a normal Stripe account.

[Connect](https://docs.stripe.com/connect) platforms creating charges on behalf
of connected accounts that need to generate 1099s for Custom accounts must
declare the correct tax-line mapping of the **Stripe Third-Party Account**. This
expense account is given an initial tax-line mapping of 1099-MISC: Nonemployee
compensation.

For QuickBooks to use **Stripe Third-Party Account** data for the generation of
1099s, you must first enable this feature within QuickBooks’ preferences.

- Select **Preferences > Tax: 1099 > Company Preferences** within QuickBooks.
- Click on the link in **If you want to map your accounts to boxes on Form
1099-MISC, click here**.
- In the resulting QuickBooks 1099 Wizard, select **Stripe Third-Party Account**
under **Accounts used for 1099**.
- Under **Apply payments to this 1099 box** for **Stripe Third-Party Account**,
select **Box 7: Nonemployee compensation**.

## Links

- [third-party accounting
integrations](https://stripe.partners/?f_category=accounting)
- [reports](https://docs.stripe.com/stripe-reports)
- [payouts](https://docs.stripe.com/payouts)
- [QuickBooks Desktop](http://quickbooks.intuit.com/)
- [Legacy exports settings](https://dashboard.stripe.com/account/legacy_exports)
- [Accounting Stripe Apps](https://marketplace.stripe.com/categories/accounting)
- [timezone setting](https://dashboard.stripe.com/settings/account)
- [Connect](https://docs.stripe.com/connect)