# Review actionable accounts

## View connected accounts with open risk, onboarding, and compliance requirements.

The [Accounts to review
page](https://dashboard.stripe.com/connect/accounts_to_review) in your Dashboard
helps you monitor the risk and onboarding status of all of your connected
accounts. From there, you can:

- **Proactively monitor your accounts**: Monitor the status of your accounts
with any open risk, onboarding, or verification requirements. View any risk or
onboarding restrictions that impact your accounts or that will impact them in
the future.
- **Identify the exact requirements needed**: Understand an account status
quickly, without needing to look through webhook logs. View clear instructions
on how to resolve open requirements and take action.
- **Export a list of accounts**: Download a CSV list of accounts, including
remediation links that your accounts with open requirements can use to submit
information and resolve issues.

## View all accounts

The [Accounts to review
page](https://dashboard.stripe.com/connect/accounts_to_review) in your Dashboard
provides a list of all your connected accounts with open risk, verification, and
onboarding requirements.

![The Accounts to review page showing connected accounts that need
action.](https://b.stripecdn.com/docs-statics-srv/assets/accounts-to-review-listview.ae6f4ea186508bdeefa80870c7972208.png)

To view the accounts in a particular status, select the corresponding tab:

TabDescriptionActions requiredActive accounts with open risk, onboarding, or
verification requirements from Stripe or from your platform.In reviewActive
accounts that Stripe is reviewing submitted information for or is conducting an
account review of, regardless of whether any account capabilities are
restricted.RejectedAll accounts that have been rejected by Stripe or by your
platform.
In the **Actions required** and **In review** tabs, you can toggle the
**Restrictions** column between restrictions and information needed by clicking
the gear in its heading.

#### Note

Stripe puts some verifications on hold for accounts that haven’t had activity in
the last 540 days. [Learn more about reviewing inactive
accounts](https://support.stripe.com/questions/2023-2024-us-verification-requirements-updates-for-custom-platforms-reviewing-connected-accounts#reviewing-inactive-accounts).

Within each tab, you can customize the filters to narrow the list of connected
accounts that are most relevant to you. You can filter by:

- Payments capability status
- Payouts capability status
- Issuing capability status
- Account status
- Volume
- Information needed
- Last payout date
- Connected date
- Due date

You can see all accounts in the currently selected status by removing the
default filters.

![A tooltip showing additional filters on the Accounts to review page, including
Payments capability status and Payouts capability
status.](https://b.stripecdn.com/docs-statics-srv/assets/filters.3caca1f55c1754eae084095ca98d333e.png)

You can sort the accounts list by total volume, due date, or connected date. In
the **Rejected** tab, you can also sort by accounts with any ongoing appeals.

#### Note

The **Total volume** column displays “Unavailable” for connected accounts with
Stripe Dashboard access where you don’t have [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
enabled. Filtering by volume always excludes them. You can identify these
accounts by filtering the list by platform controls.

Depending on a connected account’s configuration, you can take action on it in
the **Action required** list or **In review** list by clicking the account’s
overflow menu . You can take the following actions:

- View **Actions required** list on the Account details page.
- Reject the account.
- Pause or resume payouts for the account.
- Pause or resume payments for the account.
- Generate a [remediation
link](https://docs.stripe.com/connect/dashboard/remediation-links) that the
account can use to take required actions.

![A dropdown menu showing the ability to reject the connected account, pause
payouts, pause payments, view required actions, or generate a remediation
link](https://b.stripecdn.com/docs-statics-srv/assets/available-actions.1434b91974aa8acd2b5d3531fd747d8d.png)

## Filter for accounts requiring additional information on business model review

To enable Stripe’s services, your business must comply with Stripe’s [Terms of
Service regarding supported business types, products, and
industries](https://stripe.com/legal/restricted-businesses). Stripe might
require additional information to determine if your business is supported. If
so, that requirement appears in the **Actions required** section of the
connected account detail page.

![A connected account's Actions required list showing a TOS
request](https://b.stripecdn.com/docs-statics-srv/assets/cactus-actions-required.0d2aa5213b0c3f26ed7fc257e82c1643.png)

To filter for accounts requiring additional information for business model
review:

- Navigate to **Accounts to review**.
- Select **More filters**, then **Information needed**.
- In the **Filter by information needed** search box, type **verification**.
- Select the following items, then click **Apply**.- Additional info request
(Verification)
- Rejection appeal (Verification)
- URL (verification)

![A filter to return accounts requiring information for business model
review](https://b.stripecdn.com/docs-statics-srv/assets/verification-filter.f485460099b037652c3a39d615427d59.png)

## Export a list of accounts

You can download a CSV list of all accounts in the current view by clicking
**Export** in the top-right corner of the page. It opens a dialog that lets you
select the fields to include:

- Account ID
- Business name
- Representative email
- Account status
- Earliest due date
- Connected date
- Last activity
- Payment capability status
- Payout capability status
- Issuing capability status
- Treasury (Evolve) capability status
- Treasury (Fifth-third) capability status
- Verification requirement
- Information needed
- Remediation link
- Total volume (USD) (in minor units)
- Last payout date

You can import the list into another system or use it to [send remediation links
to your connected
accounts](https://docs.stripe.com/connect/dashboard/remediation-links). A
connected account can use a remediation link to submit information for open
requirements.

## Use Stripe Sigma to identify accounts with open requirements

If you use [Stripe Sigma](https://docs.stripe.com/stripe-data), it can identify
accounts that have open `requirements` or `future_requirements`. For information
about querying for Connect information with Sigma, see [Query Connect
data](https://docs.stripe.com/stripe-data/query-connect-data).

## Review individual accounts

To investigate the open requirements for an account on the **Accounts to
review** page, click the account. That opens the Account details page with an
[Actions
required](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#actions-required)
list at the top, where you can identify specific requirements and take action.
This list doesn’t appear if there aren’t any actionable requirements on the
account.

## Review and appeal unsupported connected accounts

If Stripe can’t support your connected account or requires more information, you
can review or submit an appeal from the Dashboard.

- To find a specific connected account,
[search](https://docs.stripe.com/dashboard/search) in the Dashboard or view a
[list of accounts](https://dashboard.stripe.com/connect/accounts/overview) on
the **Accounts to review** page.
- Click the row on the **Actions required** list tagged as **Supportability**
and labeled **Pending account closure** to enter the requirement details page.
- Depending on the exact information required, you can do one or more of the
following with the update button:- Send a [remediation
link](https://docs.stripe.com/connect/dashboard/remediation-links) to your
connected account so they can submit the information.
- Submit the information yourself on behalf of your connected account.
- If you choose to submit the information on behalf of your connected account,
complete the **Appeal your Stripe account closure form**.

## Links

- [Accounts to review
page](https://dashboard.stripe.com/connect/accounts_to_review)
- [Learn more about reviewing inactive
accounts](https://support.stripe.com/questions/2023-2024-us-verification-requirements-updates-for-custom-platforms-reviewing-connected-accounts#reviewing-inactive-accounts)
- [platform
controls](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [remediation
link](https://docs.stripe.com/connect/dashboard/remediation-links)
- [Terms of Service regarding supported business types, products, and
industries](https://stripe.com/legal/restricted-businesses)
- [Stripe Sigma](https://docs.stripe.com/stripe-data)
- [Query Connect data](https://docs.stripe.com/stripe-data/query-connect-data)
- [Actions
required](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#actions-required)
- [search](https://docs.stripe.com/dashboard/search)
- [list of accounts](https://dashboard.stripe.com/connect/accounts/overview)