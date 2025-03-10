# Split tax forms

## Split your tax forms for your connected accounts after a change of ownership occurs during the tax year.

Splitting a 1099 tax form means that you distribute the amount initially
reported on a single 1099 form across two 1099 forms. You can split a 1099 form
after a change of ownership occurs during the tax year for the legal entity
receiving the form. Splitting a 1099 form assigns a portion of the reported
amount to the legal entity before the change and assigns the remaining amount to
the legal entity after the change.

Changes to the legal entity of your connected accounts may include these
examples:

- Change of ownership—The owner of the connected account sells the business to a
new entity.
- Change of legal entity type—The owner of the connected account changes the
business type from individual to company, and wants to file for both entities.
- Change of Tax Identification Number (TIN)—A sole proprietorship that uses the
individual’s social security number (SSN) as the business TIN changes it to an
employer identification number (EIN), and wants to file for both entities.

#### Note

Changing the TIN doesn’t necessarily require a split (for example, if the change
was due to an oversight). You’ll need to determine whether changing the TIN
requires a split, an [update](https://docs.stripe.com/connect/modify-tax-forms),
or a [correction](https://docs.stripe.com/connect/correct-tax-forms). Work with
your tax advisor to ensure you understand the split requirements specific to
your business.

## Create a split

You can split a tax form beginning January 4th of the year following that form’s
tax year. For example, you can split a 2024 tax form starting January 4th, 2025.
To create a split, select the form in the
[Dashboard](https://dashboard.stripe.com/connect/taxes/forms) and then click
**Split** from the menu on the detail pane. You can filter by the account ID to
identify the form of the connected account you want to create a split for.

#### Note

You can’t split a form after you manually edit the numerical data. To split one
of these forms, you must revert the numerical data on the form to the
Stripe-supplied values by clicking **Undo edits** on the **Totals** section. If
the split forms are drafts, you can then
[update](https://docs.stripe.com/connect/modify-tax-forms) the draft form prior
to filing. If you have already filed the original form, you can then update form
totals on the split forms with a
[correction](https://docs.stripe.com/connect/correct-tax-forms).

![Click Split from the menu on the detail
pane](https://b.stripecdn.com/docs-statics-srv/assets/split-menu.8cd4a2d5b6f4ca57d77c36b0f1617bdb.png)

In the **Split 1099 tax form**, provide the date of the legal entity change and
then click **Split**.

![Provide date of legal entity change on Split 1099 tax
form](https://b.stripecdn.com/docs-statics-srv/assets/split-tax-form.46d061fd477e72d8b0dc0c672d2f624e.png)

You’ll see two forms for the connected account:

- Form one includes the amounts from January 1 to the day before the specified
split date.
- Form two includes the amounts from the specified split date to December 31.

If the legal entity is the same on both forms, they’re marked `Needs Attention`.
To correct this, you can [update the
form](https://docs.stripe.com/connect/modify-tax-forms) to replace the values
for relevant payees.

#### Note

You have to update the identity information on the forms (name, address, TIN)
correctly, so that it isn’t the same as what it was before the split. You are
responsible for marking the right identity information on each of the split
forms.

After you update the form so that the payee information is different for each
form, the form status changes to `Ready`. Click **File** to send both forms to
the IRS.

#### Note

Split forms can only be delivered using postal mail. Paperless deliveries using
the Express app is not currently supported.

## Links

- [update](https://docs.stripe.com/connect/modify-tax-forms)
- [correction](https://docs.stripe.com/connect/correct-tax-forms)
- [Dashboard](https://dashboard.stripe.com/connect/taxes/forms)