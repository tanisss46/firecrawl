# Manage individual accounts

## Use the Stripe Dashboard to manage connected accounts.

You can use the [Stripe
Dashboard](https://dashboard.stripe.com/connect/accounts/overview) to inspect,
support, and better understand your platform’s [connected
accounts](https://docs.stripe.com/connect/accounts).

## Create accounts

#### Regional considerationsFrance

Platforms in France can’t create connected accounts in the Dashboard. Due to
French regulations, you can only create connected accounts using Stripe-hosted
onboarding.

This feature allows you to onboard connected accounts without writing code and
to test before integrating. The user creating the account must be an
[Administrator or
Developer](https://docs.stripe.com/get-started/account/teams/roles), and the
account must have a completed [platform
profile](https://dashboard.stripe.com/connect/settings/profile).

To create a new account, click the **+ Create** button on the [Connected
accounts](https://dashboard.stripe.com/connect/accounts/overview) page, then
select the account type and country.

For Stripe Dashboard access, select
[Express](https://docs.stripe.com/connect/express-dashboard) or
[Standard](https://docs.stripe.com/connect/stripe-dashboard) to generate a
one-time link for the account holder to complete the onboarding flow. After the
account successfully connects, Stripe notifies you by email. Select
[None](https://docs.stripe.com/connect/get-started-connect-embedded-components)
to create the account immediately, then [complete
onboarding](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#updating-accounts)
it on the Account details page.

![Create an account in the
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/create-account-unified.450b8fb21ed13bcc165baa7db225e157.png)

Create an account in the Dashboard

## Find accounts

To find a specific connected account, you can [search in the
Dashboard](https://docs.stripe.com/dashboard/search) using criteria such as its
name, email, or
[metadata](https://docs.stripe.com/dashboard/search#metadata-searches).
Alternatively, you can [view a list of
accounts](https://docs.stripe.com/connect/dashboard/viewing-all-accounts) on the
[Connected accounts](https://dashboard.stripe.com/connect/accounts/overview)
page and click an account to open its Account details page.

The Activity section at the top of the Account details page can include an
**Actions required** list. If the list appears, then you or the connected
account [must take
action](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#actions-required)
to prevent or remove restrictions on the account’s capabilities. Such
restrictions can result from open onboarding, verification, or risk
requirements.

![Connected account
activity](https://b.stripecdn.com/docs-statics-srv/assets/connected-account-detail-activity-actions-required.1fa550ba2083b188f24dab6ffaf29864.png)

#### Note

Stripe puts some verifications on hold for accounts that haven’t had activity in
the last 540 days. [Learn more about reviewing inactive
accounts](https://support.stripe.com/questions/2023-2024-us-verification-requirements-updates-for-custom-platforms-reviewing-connected-accounts#reviewing-inactive-accounts).

## View the Dashboard as a connected account

![View the Dashboard as a connected
account](https://b.stripecdn.com/docs-statics-srv/assets/view-dashboard-as.cc119a613c37b3d7c0b55750002c5a1b.png)

View the Dashboard as a connected account

To view the Stripe Dashboard from the perspective of the connected account,
click the overflow menu () and select **View Dashboard As**. For connected
accounts that don’t access the full Stripe Dashboard, such as Express and Custom
accounts, you still see the full Stripe Dashboard. In those cases, what you see
isn’t an exact representation of what the connected account sees. This feature
works by passing the connected account ID as the stripe-account-header on
requests made from the Stripe Dashboard, similar to [making API calls on behalf
of connected
accounts](https://docs.stripe.com/connect/authentication#stripe-account-header).

## View and unblock support cases

View support cases your connected accounts have opened with Stripe and help
unblock those cases by providing additional context.

The **Activity** section of a connected account’s details page contains a list
of support cases raised by the connected account.

![Support
cases](https://b.stripecdn.com/docs-statics-srv/assets/connected-account-detail-support-cases.66690b126ed794b0f0c482eb8b6e79b8.png)

You can view support cases from the last 90 days created from any connected
account with access to either the full Stripe Dashboard or Express Dashboard.
Connected accounts with Stripe Dashboard access who have the following
exceptions are not included:

- Connected accounts who are or have been connected to multiple platforms
- Connected accounts who are also platform accounts
- Connected accounts who have opted out of sharing their cases.

Click on any conversation in the **Support Cases** section to open the support
case details page containing the detailed conversation between the connected
account and Stripe.

![Send Stripe Support an
email](https://b.stripecdn.com/docs-statics-srv/assets/stripe-support-email.1d56ea6297510ab80f728b808e613972.png)

You can use the **Send Stripe Support an email** functionality for an existing
support case to privately add any additional context that would help Stripe
resolve the issue. These messages aren’t visible to the connected account.

## Identify and remediate issues with required actions

If the account requires any action to prevent or remove restrictions, the action
appears in the **Actions required** list at the top of the Account details page.
Each list entry corresponds to a
[requirement](https://docs.stripe.com/api/accounts/object#account_object-requirements),
[future_requirement](https://docs.stripe.com/api/accounts/object#account_object-future_requirements),
or information request from Stripe, and displays its due date and any
capabilities it can affect.

![Connected account
activity](https://b.stripecdn.com/docs-statics-srv/assets/connected-account-detail-activity-actions-required.1fa550ba2083b188f24dab6ffaf29864.png)

The Due Date is the [current
deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline)
of the corresponding requirement. The following table describes the action
statuses.

When the list contains multiple actions, it orders them by priority. For
example, a past due requirement appears before a currently due requirement.

RequirementIssue statusInformation request from StripeVarious`requirement` in
`past_due`Past due`requirement` in `currently_due`Currently
due`future_requirement`Future requirement`requirement` in `eventually_due`Due
later
Clicking a requirement opens a requirement detail page with more information
about the requirement, including any errors and possible remediation paths. To
take action, click one of the paths.

Available paths depend on the requirement and the account type. They can include
submitting information on behalf of the account, sending the account a link that
they can use to submit information, or contacting Stripe Support.

### Submit the information

Depending on the issue type, this path opens a dialog or form where you can
enter and submit the required information.

### Send a remediation link

This path generates an account-specific remediation link that you can copy and
send to the account. The link takes them to a page where they can submit the
required information.

For more information about remediation links, see the [remediation link process
walkthrough](https://docs.stripe.com/connect/dashboard/remediation-links).

### Contact Support

To remediate some issues, you must contact Stripe. This path opens a pre-filled
form that you can use to submit a ticket to Stripe Support.

## Update account information

The capabilities of connected accounts change over time depending on their
verification status. If your platform is responsible for [collecting updated
information](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
from a connected account (including Custom accounts) when requirements change,
you can:

- Update its account information, contact information, and business details in
the **Profile** section of the Account details page.
- Update its [payout](https://docs.stripe.com/payouts) schedule in the
**Overview** tab of the Activity section under **Account balances**.

### Change the account representative

You can call the [Accounts API](https://docs.stripe.com/api/accounts/update) to
change the account representative. For more information, see the [required
verification information
page](https://docs.stripe.com/connect/required-verification-information#change-verification-info).

### Managing business owners

You can add, edit, and remove business owners on the Account details page. To
add a new owner, click **+ Add owner**. To edit an existing owner, click the
overflow menu ().

### Update capabilities

You can manage an account’s
[capabilities](https://docs.stripe.com/connect/account-capabilities) by clicking
**Edit** in the **Capabilities** section.

![Manage connected account
capabilities](https://b.stripecdn.com/docs-statics-srv/assets/edit-capabilities.59a5314539722cc15753c851fa2e1fda.png)

Manage connected account capabilities

## Send funds

Funds sent to connected accounts come from your platform’s balance. You can add
additional funds to your balance by clicking **Add to balance** in the
**Balances** section.

To execute the transfer, go to your **Balances** section and click the
**Transfers** tab. Click **New** to open the dialog for sending funds to
connected accounts.

For accounts where your platform is liable for negative balances (including
Custom and Express accounts), you can send money directly to a connected
account’s bank or debit card. To send funds, a user must have at least
[Administrator
privileges](https://docs.stripe.com/get-started/account/teams/roles).

## Pull funds

#### Private preview

Pulling funds is a US-exclusive preview feature. Both the platform’s country and
the connected account’s country must be `US`.

You can pull funds from connected accounts using the **Pull funds** button in
the **Account balances** section.

![Pull funds from a connected
account](https://b.stripecdn.com/docs-statics-srv/assets/pullfunds.91aed365ffb0bcc44510f00fa64d5761.png)

Pull funds from a connected account

For accounts where your platform is liable for negative balances (including
Custom and Express accounts), you can pull money from a connected account’s
Stripe balance directly to your platform balance. Pulling funds is restricted to
users with at least [Administrator
privileges](https://docs.stripe.com/get-started/account/teams/roles).

## Remove accounts

![Remove connected account from
platform](https://b.stripecdn.com/docs-statics-srv/assets/remove_account.2b00800b90522e6b2a46dd8827e1fa7b.png)

Remove a connected account

You can remove and disconnect any connected account with access to the full
Stripe Dashboard from your platform. A removed account no longer appears in your
connected accounts list, and you can’t process payments or make API calls for
it. You also lose any platform-controlled settings on the removed account, and
they aren’t reinstated if the account reconnects later.

Removing an account only disconnects it from your platform. It still functions
as a normal Stripe account.

## Links

- [Stripe Dashboard](https://dashboard.stripe.com/connect/accounts/overview)
- [connected accounts](https://docs.stripe.com/connect/accounts)
- [Administrator or
Developer](https://docs.stripe.com/get-started/account/teams/roles)
- [platform profile](https://dashboard.stripe.com/connect/settings/profile)
- [Express](https://docs.stripe.com/connect/express-dashboard)
- [Standard](https://docs.stripe.com/connect/stripe-dashboard)
-
[None](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [complete
onboarding](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#updating-accounts)
- [search in the Dashboard](https://docs.stripe.com/dashboard/search)
- [metadata](https://docs.stripe.com/dashboard/search#metadata-searches)
- [view a list of
accounts](https://docs.stripe.com/connect/dashboard/viewing-all-accounts)
- [Learn more about reviewing inactive
accounts](https://support.stripe.com/questions/2023-2024-us-verification-requirements-updates-for-custom-platforms-reviewing-connected-accounts#reviewing-inactive-accounts)
- [making API calls on behalf of connected
accounts](https://docs.stripe.com/connect/authentication#stripe-account-header)
-
[requirement](https://docs.stripe.com/api/accounts/object#account_object-requirements)
-
[future_requirement](https://docs.stripe.com/api/accounts/object#account_object-future_requirements)
- [current
deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline)
- [remediation link process
walkthrough](https://docs.stripe.com/connect/dashboard/remediation-links)
- [collecting updated
information](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
- [payout](https://docs.stripe.com/payouts)
- [Accounts API](https://docs.stripe.com/api/accounts/update)
- [required verification information
page](https://docs.stripe.com/connect/required-verification-information#change-verification-info)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)