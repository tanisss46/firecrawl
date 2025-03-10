# Manage connected accounts with the Dashboard

## Learn about using the Stripe Dashboard to find and manage connected accounts.

You can use the Dashboard to inspect, support, and better understand your
platform’s connected accounts. Some common tasks supported by the Dashboard
include:

- [Understand and manage your Connect payments
business](https://docs.stripe.com/connect/dashboard/understand-your-connect-business)
- [View all
accounts](https://docs.stripe.com/connect/dashboard/viewing-all-accounts)
- [Review actionable
accounts](https://docs.stripe.com/connect/dashboard/review-actionable-accounts)
- [Create
accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#creating-accounts)
- [Find individual
accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#finding-accounts)
- [Update account
information](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#updating-accounts)
- [Send funds to
accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#sending-funds)

[Viewing all
accounts](https://docs.stripe.com/connect/dashboard/viewing-all-accounts)
provides a high-level view of your connected accounts. By default, all accounts
are displayed on the [accounts
overview](https://dashboard.stripe.com/connect/accounts/overview) page, but you
can filter by account status, balance, and other attributes. Filtering accounts
is useful because it allows you to:

- View accounts that are restricted or have other issues that you can help
resolve.
- View your largest accounts.
- View accounts based on their status.

The other workflows, like inspecting accounts and sending funds, are actions you
can take on [individual
accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts).
These actions are generally made after you know which accounts need to be
inspected or modified.

Before viewing and making changes to accounts, learn more about the [status
badges](https://docs.stripe.com/connect/dashboard#status-badges) displayed in
the Dashboard.

## Status badges

Status badges provide a quick way to understand the status of an account. You
can hover over the badges to view contextual information, and you can click the
[status
tabs](https://docs.stripe.com/connect/dashboard/viewing-all-accounts#tabs-workflows)
to view accounts grouped by that status. Status badges include:

StatusBadge[Restricted](https://docs.stripe.com/connect/dashboard#restricted)Restricted[Restricted
soon](https://docs.stripe.com/connect/dashboard#restricted-soon)Restricted
soon[Pending](https://docs.stripe.com/connect/dashboard#pending) (enabled or
disabled)Pending or
Pending[Enabled](https://docs.stripe.com/connect/dashboard#enabled)Enabled[Complete](https://docs.stripe.com/connect/dashboard#complete)Complete[Rejected](https://docs.stripe.com/connect/dashboard#rejected)Rejected
### Restricted

**Restricted** means the account has [payouts](https://docs.stripe.com/payouts)
or payments disabled. Additional information usually needs to be collected to
enable these accounts. Hovering over the status badge displays:

- Which capability is disabled (payouts or payments).

If information is required to enable the account, it appears in an **Actions
required** list at the top of the connected account details page.

### Restricted soon

**Restricted soon** means the account has a due date for providing additional
information.

If information is required to enable the account, it appears in an **Actions
required** list at the top of the connected account details page.

### Pending

**Pending** means the account is being reviewed or verified by Stripe. This
occurs when:

- Stripe is verifying the information that was provided, such as an ID document
upload.
- Stripe is performing a watchlist check against a list of prohibited
individuals and businesses.
- Stripe is reviewing the account for suspected fraudulent activity.

Payouts can be enabled or disabled for accounts with a pending status and
requires no action on your part. Stripe automatically updates the account’s
status when the review finishes.

### Enabled

**Enabled** means the account is in good standing, though additional information
might be required if another payment volume
[threshold](https://docs.stripe.com/connect/identity-verification#verification-requirements)
is reached. Hovering over the status badge displays:

- What information Stripe might request in the future.

In the account’s
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
hash, the array `eventually_due` contains at least one requirement, but payments
and payouts are enabled and `current_deadline` is empty.

### Complete

**Complete** means the account provided all the required information and is in
good standing.

In the account’s
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
hash, the array `eventually_due` is empty.

### Rejected

**Rejected** means you (the platform) or Stripe rejected the connected account.
Hovering over the status badge displays:

- Whether the account was rejected by you (the platform), or by Stripe.

Check the **Actions required** list at the top of the connected account details
page to see the reason the account was rejected. In general, accounts are
rejected by Stripe if they’re suspected of fraudulent activity.

## Use Platform Branding for Connected Accounts

As the platform, you can initialize newly created connected accounts with your
platform branding settings. To do so, navigate to **Connect Settings** >
**Branding** and enable ** Platform Branding**. After you enable it, all new
accounts onboarding to your platform receive the same branding settings as your
platform.

Use [Account Update](https://docs.stripe.com/api/accounts/update) to update the
account’s branding after creation.

## See also

- [Viewing all
accounts](https://docs.stripe.com/connect/dashboard/viewing-all-accounts)
- [Managing individual
accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts)

## Links

- [Understand and manage your Connect payments
business](https://docs.stripe.com/connect/dashboard/understand-your-connect-business)
- [View all
accounts](https://docs.stripe.com/connect/dashboard/viewing-all-accounts)
- [Review actionable
accounts](https://docs.stripe.com/connect/dashboard/review-actionable-accounts)
- [Create
accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#creating-accounts)
- [Find individual
accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#finding-accounts)
- [Update account
information](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#updating-accounts)
- [Send funds to
accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#sending-funds)
- [accounts overview](https://dashboard.stripe.com/connect/accounts/overview)
- [individual
accounts](https://docs.stripe.com/connect/dashboard/managing-individual-accounts)
- [status
tabs](https://docs.stripe.com/connect/dashboard/viewing-all-accounts#tabs-workflows)
- [payouts](https://docs.stripe.com/payouts)
-
[threshold](https://docs.stripe.com/connect/identity-verification#verification-requirements)
-
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
- [Account Update](https://docs.stripe.com/api/accounts/update)