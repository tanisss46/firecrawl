# Create pricing groups

## Define separate pricing schemes for different connected account groups.

You can define pricing groups to assign specific pricing schemes to multiple
connected accounts simultaneously. This can save time over manually adding or
updating the same fee override to each connected account individually.

You can create up to 50 groups across all pricing schemes.

## Assign groups to a pricing scheme

You can define up to 50 pricing schemes per product (such as Payments or Instant
Payouts) and apply each to one or more groups of [eligible connected
accounts](https://docs.stripe.com/connect/platform-pricing-tools#eligibility-for-payments).
You can enable only one pricing scheme to a connected account.

To create a new schema and define a pricing group:

- From the Payments tab of the [Platform
pricing](https://dashboard.stripe.com/settings/connect/platform_pricing) page in
your Stripe Dashboard (**Settings** > **Connect** > **Platform pricing**), click
**+ Add scheme**.
- Select **Create a new scheme** or **Start from an existing scheme**.
- Name your scheme.
- Define your scheme with pricing rules, fallback rules and fee modifiers using
the instructions in [create a pricing
scheme](https://docs.stripe.com/connect/platform-pricing-tools/pricing-schemes).
- Assign a group to your scheme.- Type a name and click **+ Add** to create a
new group. After you save the scheme, you can [add accounts to your new
group](https://docs.stripe.com/connect/platform-pricing-tools/pricing-groups#add-accounts-to-groups).
- Alternatively, click **Reassign a group** to choose an existing group, then
click **+ Reassign**
- Click **Save and enable** and review the details of your schema, including its
assigned groups and the number of accounts in each group. Click **Confirm** to
submit the changes.
- Click the overflow menu () of a scheme, then click **Edit** to make changes.

## Add accounts to groups

You can add connected accounts to existing groups using the following methods:

- **CSV import**: Takes effect immediately, but group counts in the UI take a
few minutes to update.
- **API**: Takes effect immediately.

Recent group assignment changes take up to 24 hours to reflect in CSV exports.

### CSV Import

Use the Dashboard to import a CSV file defining the connected accounts to add to
a group.

- the GroupID of the group you want to add accounts to.
- Click the overflow menu () of the group’s pricing scheme, then select **Add
accounts**.
- Download the pre-configured CSV for the group (or create your own).
- Populate the following two columns for each connected account to add.-
**connected_account**: `account id` of a connected account to assign to this
group.
- **account_group**: `group id` of the group to add the account to.
- Click **Upload CSV** and select your completed file.
- Stripe validates the file and returns the number of connected accounts in your
platform *not* included in the file. This helps you make sure you didn’t
unintentionally omit any users.
- Click **Confirm** to complete the import.

### API

Before assigning a connected account into a pricing group, obtain the group ID
(`acctgrp_xxx`) from the Platform Pricing page in your Dashboard.

#### Assign a group to an existing account

- Populate the `groups.payments_pricing` parameter of the [Update an
account](https://docs.stripe.com/api/accounts/update) call with the `ID` of the
group to assign the account to.
- [Expand](https://docs.stripe.com/expand) the `groups` object to request the
`groups` parameter in the response.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "groups[payments_pricing]"=acctgrp_NrikrzNEvHZ4go \
 -d "expand[]"=groups
```

The response returns the connected account object with the expanded `groups`
parameter.

```
{
 // ...
 "groups": {
 "payments_pricing": "acctgrp_NrikrzNEvHZ4go"
 }
}
```

#### Assign a group when creating a new account

- Populate the `groups` parameter of the [Create an
account](https://docs.stripe.com/api/accounts/create) call with the `name` and
`ID` of the group to assign it to the account.

Alternatively, omit the `groups` parameter during account creation to
automatically assign the account to the default group. All eligible connected
accounts without a specific group designation belong to the default group.
- [Expand](https://docs.stripe.com/expand) the `groups` object to request the
`groups` parameter in the response.

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "groups[payments_pricing]"=acctgrp_NrikrzNEvHZ4go \
 -d "expand[]"=groups
```

The response returns the new connected account object with the expanded `groups`
parameter.

```
{
 // ...
 "groups": {
 "payments_pricing": "acctgrp_NrikrzNEvHZ4go"
 }
}
```

#### Retrieve the group of an account

Expand the `groups` parameter in the Accounts lookup call to see the account’s
pricing group. If the `payments_pricing` group has a null value, the connected
account has a [pricing
override](https://docs.stripe.com/connect/platform-pricing-tools/pricing-schemes#override-a-specific-account).

```
curl -G https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=groups
```

The response returns the new connected account object with the expanded `groups`
parameter.

```
{
 // ...
 "groups": {
 "payments_pricing": "acctgrp_NrikrzNEvHZ4go"
 }
}
gated=["groups"]
```

## Unassign a pricing group from a pricing scheme

To disassociate a group and it’s connected accounts from a pricing scheme:

- Click the overflow menu () of the pricing scheme, then select **Edit**.
- In the **Assign groups** section, click the overflow menu () of the intended
group, then select **Unassign**.
- Click **Save and Enable**, then **Confirm**.

This doesn’t delete the pricing group with its associated connected accounts. It
reassigns the pricing group to the default pricing scheme. You can still
[reassign the pricing group to a different
scheme](https://docs.stripe.com/connect/platform-pricing-tools/pricing-groups#assign-groups-to-a-pricing-scheme).

## Delete a pricing group

You can delete a pricing group and reassign its connected accounts to the
pricing group associated with the default pricing scheme. You can only delete a
pricing group from the Dashboard.

#### Caution

Deleting a pricing group that you still reference in your API calls can break
your integration.

- Click the overflow menu () of the pricing scheme, then select **Edit**.
- In the **Assign groups** section, click the overflow menu () of the intended
group, then select **Delete**.
- Click **Save and Enable**, then **Confirm**.

Any connected accounts in a deleted pricing group get reassigned to the pricing
group of the default pricing scheme.

## View accounts assigned to a payments pricing scheme

You can download a CSV list of connected accounts and their assigned groups for
a pricing scheme. From the [Platform
Pricing](https://dashboard.stripe.com/settings/connect/platform_pricing) page of
your Dashboard, click the overflow menu () of the pricing scheme, then select
**Export accounts**.

You can also download a CSV list of all connected accounts and their assigned
schemes by clicking **Export accounts** at the top of the [Platform
Pricing](https://dashboard.stripe.com/settings/connect/platform_pricing) page.

## Links

-
[override](https://docs.stripe.com/connect/platform-pricing-tools/pricing-schemes#override-a-specific-account)
- [eligible connected
accounts](https://docs.stripe.com/connect/platform-pricing-tools#eligibility-for-payments)
- [Platform
pricing](https://dashboard.stripe.com/settings/connect/platform_pricing)
- [create a pricing
scheme](https://docs.stripe.com/connect/platform-pricing-tools/pricing-schemes)
- [Update an account](https://docs.stripe.com/api/accounts/update)
- [Expand](https://docs.stripe.com/expand)
- [Create an account](https://docs.stripe.com/api/accounts/create)