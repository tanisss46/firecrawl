# What's new for tax year 2023

## Learn about new features available for Connect platforms and marketplaces filing 1099s with Stripe.

For tax year 2023, Stripe is introducing features that help Connect platforms
efficiently and accurately meet their 1099 tax reporting obligations for
[Custom](https://docs.stripe.com/connect/custom-accounts) and
[Express](https://docs.stripe.com/connect/express-accounts) US-based accounts.
The 2023 tax year features help platforms comply with their 1099 tax reporting
obligations at scale.

#### Note

Stripe delivers 1099 forms to Standard accounts through the Stripe Dashboard.

## Early access to editable tax forms

Starting in August, you can access preliminary 2023 tax forms and associated tax
reporting features directly from your Stripe Connect Dashboard. Your team needs
either Administrator or Tax analyst [user
permissions](https://docs.stripe.com/get-started/account/teams) to get started.

Along with early access to tax forms, you can start editing tax forms right
away, as opposed to waiting to make edits in January. You can do so for
individual tax forms or in bulk by importing a CSV file.

## Improved state ID collection

In our platform onboarding flow for tax year 2023, we clarified the strict ID
requirements for filing in two states: Delaware and Pennsylvania. If you intend
to file in either of these states, include your state IDs during this step to
prevent possible rejection of your filings.

## Create and update tax forms

Stripe provides several features to help you [create and update tax
forms](https://docs.stripe.com/connect/modify-tax-forms).

### Deltas

Importing tax forms using **Delta** allows you to add to (or subtract from) the
values on the initial tax form totals from Stripe. This lets you report just the
totals of transactions that happened outside of Stripe. You don’t need to sum
the values from Stripe with external values—instead, you only need to provide
the delta amounts and Stripe does the rest. This is particularly useful if you
have multiple payout mechanisms or reimbursements on Stripe connected accounts
for activity that happened outside of Stripe.

![Add deltas to a tax form through CSV
imports](https://b.stripecdn.com/docs-statics-srv/assets/deltas-tax-form-2023.1955229634d237c2dded771a26dede66.png)

### Zero dollar tax forms

Platforms can generate tax forms for a Stripe account ID, even when it hasn’t
received any payouts in 2023. If your connected account doesn’t already have a
tax form, performing **Update** imports (to override form values supplied by
Stripe) or **Delta** imports (to make incremental changes to form values
supplied by Stripe) automatically creates the form.

![Update a tax form through CSV
imports](https://b.stripecdn.com/docs-statics-srv/assets/update-tax-form-2023.3ee26a28748bfa00607ba5db863ec3dc.png)

### Standalone tax forms

You can create standalone tax forms for accounts that might not be a connected
account (for example, accounts from a different provider). You can create them
seamlessly by using a **Create** import with a CSV file containing the data of
the form you want to generate. You must include all columns except for `form_id`
and `stripe_account_id`. E-delivery isn’t available for standalone forms (only
postal mailing is allowed for delivery).

![Create a tax form through CSV
imports](https://b.stripecdn.com/docs-statics-srv/assets/create-tax-form-2023.57be1986e99960197e157a73bb2a89aa.png)

### Increased CSV import and export speed

If you’re using CSV imports to create or modify tax forms, we’ve increased the
speed of CSV imports and exports by up to *10 times* the speed of previous
years.

## Improved splitting and grouping of forms

You can use pre-filing splits and improved TIN aggregation to reduce the amount
of overhead for filing taxes.

### Pre-filing splits

You can now [split tax forms](https://docs.stripe.com/connect/split-tax-forms)
to handle account ownership changes before filing the forms. Splitting a 1099
tax form means that you distribute the amount initially reported on a single
1099 form across two 1099 forms. Previously, you could only split tax forms
post-filing, meaning you might have needed to file the wrong tax forms and then
correct them. Now, after January 1, you can do so before filing from the 1099
Dashboard.

![Pre-filing
splits](https://b.stripecdn.com/docs-statics-srv/assets/pre-file-spits-2023.c93202c5520f7be4de8a00cfff2cc264.png)

### Improved TIN aggregation of tax forms

Forms that share the same TIN get their totals aggregated to determine filing
eligibility at all times, even when the platform updates the tax form totals or
identity data. When there are multiple forms with the same TIN, we aggregate the
totals from each form with a maximum of 100 other forms. However, if forms of
different types share the same TIN, we might not aggregate them. In these cases,
check your filing eligibility and apply an override if necessary. To simplify
finding other forms grouped with a particular form, use the **Forms grouped
with** filter.

![Form aggregation
filter](https://b.stripecdn.com/docs-statics-srv/assets/form-agg-filter-2023.a13264f451ac25e0b6ebee27a6915306.png)

## Form Delivery Improvements

You can use the Dashboard to track delivery status and Stripe outreach emails,
and to address missing emails.

### Delivery status visibility

You can now view both postal delivery and e-delivery statuses directly in the
1099 Dashboard. You can also
[filter](https://docs.stripe.com/connect/get-started-tax-reporting#view-and-filter-tax-forms)
for both statuses. Previously, we only showed a combined delivery status, which
reported the best result between the e-delivery and postal delivery status. With
the combined status, if one of the forms was successfully delivered (but not the
other) it showed a status of `delivered`. In other words, if e-delivery was
successful and postal delivery was unsuccessful, the combined status was
`delivered`. Going forward, you can track the individual status for each of the
forms you deliver.

![New dashboard statuses and filters for delivery and
outreach](https://b.stripecdn.com/docs-statics-srv/assets/new-statuses-2023.25eb0f5aecc794bef2ac9ada37c0b05d.png)

### Tracking Stripe outreach

If your platform opts for e-delivery through Stripe Express and enables the
collection of tax information in advance using 1099 tax form settings, Stripe
sends emails to the connected accounts on behalf of platforms. We do this to
confirm their tax information and provide e-delivery consent through Stripe
Express. You can now track the status of that outreach directly in the 1099
Dashboard, and use the `Pre-filing confirmation status` filter. The status is
either `ineligible`, `queued`, `sent`, or `not sent`.

### Addressing missing emails

[For e-delivery with Stripe
Express](https://docs.stripe.com/connect/deliver-tax-forms#e-delivery-with-stripe-express),
the connected account owner must be able to receive the email from Stripe
inviting them to create their account. Stripe can’t electronically deliver the
forms without the email address for the account. If you’ve opted in to paper
delivery, we send paper forms (assuming we have a valid delivery address). You
can now filter for any accounts with missing emails and add them to allow
e-delivery. Any emails added by the following methods will result in updating
the email on the connected account, which will carry over each year.

- Use the
[Update](https://docs.stripe.com/api/accounts/update#update_account-email) API.
- Use the CSV import functionality on the [Emails
page](https://dashboard.stripe.com/settings/connect/emails) in the Dashboard.
New
- Edit the email addresses in the *Payee Details* section in the 1099 dashboard.
New

You can no longer update email addresses using the email_address field in a CSV
import directly into the 1099 product. Changes made using this method don’t
carry over each year.

### Send Stripe pre-filing confirmation invites

Platforms who enable e-delivery can choose to have Stripe collect identity
information and paperless delivery consent directly from their connected
accounts through pre-filing confirmation. This email invites your user to Stripe
Express. If you need to send a one-off pre-filing confirmation email (for
example, your user didn’t receive one since they had the wrong email on file),
you can now do it from the 1099 dashboard. [Learn
more](https://docs.stripe.com/connect/express-dashboard-taxes#my-connected-account-did-not-receive-a-pre-filing-confirmation-email)
about how to resolve issues related to your user not receiving a pre-filing
confirmation email.

### Reset account claim attempts

Connected accounts must claim their Stripe accounts to view the Tax Center in
the Express dashboard. To authorize the claim, Stripe asks the user a series of
questions to verify their identity. For security reasons, if the user fails to
correctly answer the verification questions too many times, Stripe locks their
account. You can now see the status in the 1099 dashboard, and you can reset
your user’s claim attempts directly in the 1099 Dashboard. [Learn
more](https://docs.stripe.com/connect/express-dashboard-taxes#my-connected-account-was-locked-out-of-their-stripe-express-account-for-failing-the-verification-process.-how-can-i-resolve-this-issue)
about how you can use these new features to self-resolve account claim issues.

## Links

- [Custom](https://docs.stripe.com/connect/custom-accounts)
- [Express](https://docs.stripe.com/connect/express-accounts)
- [user permissions](https://docs.stripe.com/get-started/account/teams)
- [create and update tax
forms](https://docs.stripe.com/connect/modify-tax-forms)
- [split tax forms](https://docs.stripe.com/connect/split-tax-forms)
-
[filter](https://docs.stripe.com/connect/get-started-tax-reporting#view-and-filter-tax-forms)
- [For e-delivery with Stripe
Express](https://docs.stripe.com/connect/deliver-tax-forms#e-delivery-with-stripe-express)
- [Update](https://docs.stripe.com/api/accounts/update#update_account-email)
- [Emails page](https://dashboard.stripe.com/settings/connect/emails)
- [Learn
more](https://docs.stripe.com/connect/express-dashboard-taxes#my-connected-account-did-not-receive-a-pre-filing-confirmation-email)
- [Learn
more](https://docs.stripe.com/connect/express-dashboard-taxes#my-connected-account-was-locked-out-of-their-stripe-express-account-for-failing-the-verification-process.-how-can-i-resolve-this-issue)