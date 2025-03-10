# File tax forms with states

## Learn about the state requirements for filing 1099 forms.

When you [file](https://docs.stripe.com/connect/file-tax-forms) your 1099 forms
from the [Tax reporting](https://dashboard.stripe.com/connect/taxes/forms) view
in the Dashboard, Stripe submits your forms to the IRS and all qualifying
states. We automatically apply state thresholds when generating 1099 tax forms,
so you can easily determine which forms need state filing based on the addresses
of your connected accounts.

#### Note

Stripe supports e-filing in all states but won’t transmit forms to states on
your behalf that have backup or state withholding amounts. Review [1099 form
requirements by
state](https://docs.stripe.com/connect/tax-forms-state-requirements#check-1099-form-requirements-by-state)
and work with your tax advisor to make sure you understand the tax requirements
specific to your business.

## Prepare to file with the states

Before filing forms in your Dashboard, do the following to make sure forms are
filed correctly with both the IRS and states:

[Choose the tax form type in the
Dashboard](https://docs.stripe.com/connect/tax-forms-state-requirements#choose-form-type)
[Configure your tax forms
settings](https://docs.stripe.com/connect/get-started-tax-reporting#set-tax-form-default-settings)
to choose the tax form type (or types) you’ll file: 1099-K, 1099-NEC, or
1099-MISC. Each state has different requirements for each form type.

[Determine the states where your connected accounts are
based](https://docs.stripe.com/connect/tax-forms-state-requirements#determine-location)
In the [Dashboard](https://dashboard.stripe.com/connect/taxes/forms), you can
either [export](https://docs.stripe.com/connect/modify-tax-forms?method=csv) a
CSV file with state information (reported in the **payee_region** column) or
filter by **Payee state**.

![Filter by payee
state](https://b.stripecdn.com/docs-statics-srv/assets/payee_state.f077495dfbceb3bba62b27c5aee2bb9f.png)

[Determine which states to file
with](https://docs.stripe.com/connect/tax-forms-state-requirements#determine-states)
Some state 1099 filings also require a state tax registration or withholding ID.
Refer to the tables in the [Check 1099 form requirements by
state](https://docs.stripe.com/connect/tax-forms-state-requirements#check-1099-form-requirements-by-state)
section to determine where you might need state online accounts and IDs.

[Add the state tax Registration or withholding
ID](https://docs.stripe.com/connect/tax-forms-state-requirements#add-state-reg)
After you obtain the registration or withholding ID, add the states in which
you’ll file and the corresponding IDs on the [Tax forms
settings](https://dashboard.stripe.com/settings/connect/tax_forms) page. In the
Dashboard, click **Settings**. On **Product settings**, under **Connect**, click
**Tax form settings**.

![Add the state tax registration or withholding ID for each state you'll
file](https://b.stripecdn.com/docs-statics-srv/assets/state_tax_registration_id.b61e81338146c94a3e98ee995cd866ce.png)

Refer to the tables in the [Check 1099 form requirements by
state](https://docs.stripe.com/connect/tax-forms-state-requirements#check-1099-form-requirements-by-state)
section to determine where you might need state online accounts and IDs. If
prompted that some state registration or withholding IDs were missing during
filing, you must add the missing IDs on the Connect [Tax forms
settings](https://dashboard.stripe.com/settings/connect/tax_forms) page, and
then go through the filing flow again. Delaware and Pennsylvania typically
reject state filings if state IDs are missing and a state ID was issued.

## State-by-state breakdown

When you’re ready to [file forms in your
Dashboard](https://docs.stripe.com/connect/file-tax-forms), the forms for IRS
and state reporting agencies will be filed at the same time. To understand the
number of forms being filed in each state, click **Show state-by-state
breakdown** on the **File Federal and state tax forms** window in the filing
flow. This page also indicates whether the state’s registration or withholding
ID is missing or has already been provided. A yellow informational banner
displays at the top of every page in the filing flow if state IDs are missing
from states that are being filed.

![Review filing details page displaying a banner to indicate a missing Tax
ID.](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-review-filing-missing-ID.40d5902778ca845d5190d1679d9f4ee8.png)

## Withholding

Stripe can’t file tax forms with the state authorities if state withholding is
present. If you have forms with state withholding, Stripe won’t file those with
the states but will make the files available as an export and file with the IRS.
Please check the **Exports & Imports** section in the Dashboard for the
downloaded file. Please consult a tax advisor on how/whether to file these forms
with state agencies.

## Check 1099 form requirements by state

Choose the form type to view state filing requirements:

- [1099-K](https://docs.stripe.com/connect/1099-K)
- [1099-NEC](https://docs.stripe.com/connect/1099-NEC)
- [1099-MISC](https://docs.stripe.com/connect/1099-MISC)

## Correct 1099 reports with the states

When you file a correction with the IRS, the state correction is filed at the
same time. To file a
[correction](https://docs.stripe.com/connect/correct-tax-forms) with a state for
a form that was already filed, you must create a correction.

## Frequently asked questions

The following section provides answers to common questions about filing tax
forms through Connect.

### What happens if a connected account needs their form filed in multiple states?

Stripe does not support this at the moment. Stripe only checks eligibility and
files in the state where the connected account’s address is registered.

### When we click “File”, does Stripe file with the IRS and the States at the same time, or do we have the ability to make changes if one has a later deadline?

Stripe files with the IRS and the State right away when you file the submission
and you can’t make changes to that. But platforms are always able to make
“corrections” and then file them and Stripe takes care of processing those
corrections to the IRS and the State.

### How do I know if a particular form will be filed with the state?

We’ve introduced a new State filing status. For more information, see
[Understand tax form
status](https://docs.stripe.com/connect/get-started-tax-reporting#understand-tax-form-status).

### Can I override the filing requirement for State filing without overriding the filing requirement for Federal filing?

No. If you override the filing requirements, it applies to both federal and
state filing.

### Why wasn’t the state filing status overridden when I selected “File even if incomplete”?

When you choose to override the filing status and select **File even if
incomplete**, there are still certain edge cases where your form might still
have a state filing status of `Needs Attention`. This is done to minimize the
risk of rejections from the state. Take note of the following state-specific
rules:

- Pennsylvania: The form must have a non-zero Taxpayer Identification Number
(TIN) and pass a basic address validation check, which requires at least one
digit and one number in the address.
- Illinois: The form must have a non-zero TIN and a valid payee name.
- Oregon: The form must have a non-zero TIN.
- District of Columbia: The form cannot have a TIN with all digits being the
same number.

## Links

- [file](https://docs.stripe.com/connect/file-tax-forms)
- [Tax reporting](https://dashboard.stripe.com/connect/taxes/forms)
- [1099 form requirements by
state](https://docs.stripe.com/connect/tax-forms-state-requirements#check-1099-form-requirements-by-state)
- [Configure your tax forms
settings](https://docs.stripe.com/connect/get-started-tax-reporting#set-tax-form-default-settings)
- [export](https://docs.stripe.com/connect/modify-tax-forms?method=csv)
- [Tax forms settings](https://dashboard.stripe.com/settings/connect/tax_forms)
- [1099-K](https://docs.stripe.com/connect/1099-K)
- [1099-NEC](https://docs.stripe.com/connect/1099-NEC)
- [1099-MISC](https://docs.stripe.com/connect/1099-MISC)
- [correction](https://docs.stripe.com/connect/correct-tax-forms)
- [Understand tax form
status](https://docs.stripe.com/connect/get-started-tax-reporting#understand-tax-form-status)