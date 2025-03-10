# Remediate missing tax information

## Learn how to find and correct forms with missing information.

Stripe automatically identifies forms that are above the IRS or state filing
thresholds. In addition to the totals, a 1099 form also needs to have the name,
address, and TIN of the connected account on the form to be ready for filing.

If a form is above the threshold (has a filing obligation) and has the **name**,
**address**, and **TIN** on the form, Stripe labels the form `Ready`:

![Ready
label.](https://b.stripecdn.com/docs-statics-srv/assets/identity_1.7c55d26b4ecfd38740e2de9acd0ff5b3.png)

If you need to file a form but the form is missing this key information, Stripe
labels the form `Needs attention`:

![Needs attention
label.](https://b.stripecdn.com/docs-statics-srv/assets/identity_2.c7b46cd05ee19f79cc1f7a4c19a205f5.png)

Refer to the [Get started with tax
reporting](https://docs.stripe.com/connect/get-started-tax-reporting#understand-tax-form-status)
guide to learn more about tax form statuses.

The following information describes how to track what forms have `Needs
attention` status, why they have that status, and what to do to get their status
to `Ready`.

## Identity forms in that need attention

The **Needs attention** tab lists all forms with a `Needs attention` status.

![Needs attention
tab.](https://b.stripecdn.com/docs-statics-srv/assets/identity_3.0ec06ddc52465f44465ff9c5a22057b0.png)

#### Note

Some forms that appear to be below the federal filing threshold can also appear
as `Ready` or `Needs attention` due to Grouped TINs or state filing thresholds.
[Learn
more](https://docs.stripe.com/connect/file-tax-forms#below-threshold-forms)

The **Payee details** section lists the missing data that causes the form to
have a `Needs attention` status:

![Payee details
section.](https://b.stripecdn.com/docs-statics-srv/assets/identity_4.bd8c5d5254cb44977f15b2f84d494a14.png)

Refer to the [Required verification information for
taxes](https://docs.stripe.com/connect/required-verification-information-taxes)
guide for information on what information is needed for each form.

The reasons a form might have a `Needs attention` status include:

- **Missing address:** The *line1*, *city*, *state,* or *postal code* is
missing.
- **Missing TIN:** The TIN is missing.
- **Mismatched TIN:** The name and TIN are present on the form, but failed
Stripe’s TIN verification with the IRS as they didn’t match IRS records. [Learn
more about Tax form TIN
status](https://docs.stripe.com/connect/get-started-tax-reporting#understand-tax-form-tin-status).
- **Missing name:** The name is missing from the account. This reason is rare.

Use the filter to retrieve forms based on the reason for the `Needs attention`
status:

![Filter forms by
status](https://b.stripecdn.com/docs-statics-srv/assets/identity_5.9cd7b0b5fff7639007ae9e507504d00f.png)

## Remediation options

There are several ways to fix forms that need attention.

## Scenario A: You’re able to retrieve the data

These are your options if you already have this data or able to retrieve it
outside of Stripe.

- **Option 1 Recommended:** If you already have this data in your internal
systems, or have a way to reach out to your connected account owners to collect
this information directly, use the [Accounts
API](https://docs.stripe.com/api/accounts/update) to send that data to Stripe.
Make sure these required
[fields](https://docs.stripe.com/connect/required-verification-information-taxes)
are present on the Accounts API. After you send the data to Stripe, it appears
in the tax form within 24-36 hours, and the form automatically transitions from
`Needs attention` to `Ready`.
- **Option 2:** Use [CSV
imports](https://docs.stripe.com/connect/modify-tax-forms?method=csv) to get
this data into the current year’s tax forms. If the CSV process imports all of
the required information, the tax form automatically transitions from `Needs
attention` to `Ready`. Importing these details using CSV only updates this
information on the tax form, and doesn’t update the source of truth within
Stripe. As a result, the connected account details view doesn’t show these
updates.
- **Option 3**: If you need to update only a few forms, you can choose to
directly modify the forms in the Dashboard using the [Tax Form
Editor](https://docs.stripe.com/connect/modify-tax-forms?method=dashboard).

## Scenario B: You want Stripe to help get the data

These are your options if you don’t have the required information and you want
Stripe to help you obtain this data. Stripe recommends using both options to for
the best chance of collecting all the information for filing.

- **Option 1:** If you enable e-delivery through an interface built by Stripe,
connected account owners eligible for IRS filing receive emails from Stripe
requesting confirmation of their tax information and to update their delivery
preferences through that interface. If you implemented Connect embedded
components, the email directs them to the embedded component. Otherwise, it
directs them to the [Stripe Express
Dashboard](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough).
Connected account owners can then view and edit their personal details,
including name, address, and TIN.

![Tax form confirm information
email.](https://b.stripecdn.com/docs-statics-srv/assets/tax-form-confirm-information-email-2023.8868bb92bbd3f2fd5fa0e2fe319c11ab.png)

![Confirm
information.](https://b.stripecdn.com/docs-statics-srv/assets/identity_7.1801e85e31759f80b4e3ffd7fe974778.png)
- **Option 2:** Use Stripe Onboarding to collect missing details

- Add the 1099 capability on your accounts
[programmatically](https://docs.stripe.com/connect/account-capabilities#tax-reporting)
or
[one-by-one](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#updating-capabilities)
using the Connect Dashboard. By adding the 1099 capability, you make name,
address, and TIN a requirement on all your connected accounts. If your connected
accounts have more than 600 USD in lifetime volume and don’t have name, address,
and verified TIN on file, payouts are paused until Stripe has that information.-
There’s another feature in private preview called Additional Verifications that
allows platforms to add TIN and address requirements on their connected
accounts, along with flexibility on when to disable payouts. Reach out to your
account manager to learn more.
- You can route your user to a Stripe surface to complete their requirements.-
For accounts with access to the Express Dashboard or embedded components where
Stripe owns the requirement collection, Stripe automatically detects when there
are `currently_due` requirements (such as address or TIN) on the account and
sends the connected account owner an email.
- For other accounts without access to a Stripe Dashboard, including Custom
accounts, create [account
links](https://docs.stripe.com/api/account_links/create) and route your users to
Stripe onboarding for Custom accounts.

![Verify your personal
details.](https://b.stripecdn.com/docs-statics-srv/assets/identity_8.1dc79629776f61a43b06d68a583d6aa4.png)

## Links

- [Get started with tax
reporting](https://docs.stripe.com/connect/get-started-tax-reporting#understand-tax-form-status)
- [Learn
more](https://docs.stripe.com/connect/file-tax-forms#below-threshold-forms)
- [Required verification information for
taxes](https://docs.stripe.com/connect/required-verification-information-taxes)
- [Learn more about Tax form TIN
status](https://docs.stripe.com/connect/get-started-tax-reporting#understand-tax-form-tin-status)
- [Accounts API](https://docs.stripe.com/api/accounts/update)
- [CSV imports](https://docs.stripe.com/connect/modify-tax-forms?method=csv)
- [Tax Form
Editor](https://docs.stripe.com/connect/modify-tax-forms?method=dashboard)
- [Stripe Express
Dashboard](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough)
-
[programmatically](https://docs.stripe.com/connect/account-capabilities#tax-reporting)
-
[one-by-one](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#updating-capabilities)
- [account links](https://docs.stripe.com/api/account_links/create)