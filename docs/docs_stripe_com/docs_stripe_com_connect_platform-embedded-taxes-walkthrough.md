# 1099 Tax Reporting embedded components walkthrough

## Manage 1099 Tax forms for connected accounts using embedded components.

This page outlines an example of the typical product flow that your connected
accounts can encounter when you, as the platform, have implemented Connect
embedded components. This is useful for you and your support teams to understand
the overall user journey of your connected accounts. If you have any questions,
[contact Stripe Support](https://support.stripe.com/).

#### Note

Tax reporting features are not currently visible in the embedded components. You
can access them later during Tax Season 2024, ahead of relevant milestones as
noted below. This page gives a preview of the user experience.

## Connect embedded components

You can give your connected accounts access to components for managing tax
information and receiving 1099s electronically, all embedded within your
platform. To do this,
[integrate](https://docs.stripe.com/connect/deliver-tax-forms#file-deliver-embedded)
and [configure](https://docs.stripe.com/connect/embedded-comms) Connect embedded
components and enable e-delivery.

Stripe can send pre-filing confirmation emails to collect tax information and
paperless delivery consent directly from your connected accounts. We’ll email
your eligible connected accounts starting the week of November 4. You can select
this option when you configure your [tax form
settings](https://dashboard.stripe.com/settings/connect/tax_forms).

## 1099 tax reporting lifecycle

The following sections describe what the process looks like after Connect
embedded components are set up and e-delivery is enabled.

### Your connected account receives a pre-filing confirmation email from Stripe

Your connected account receives an email from Stripe asking them to confirm
their tax information and update their delivery preferences. The subject line
reads ‘Get your [Platform_Name] 2024 tax forms faster by enabling e-delivery.’

![Stripe Express Tax form email from
Stripe.](https://b.stripecdn.com/docs-statics-srv/assets/tax-reporting-prever-email-2024.3a2bddb9602387c7cf916aa9b9829a45.png)

Pre-filing confirmation email from Stripe

### Your connected account is directed to your platform

During pre-filing confirmation, your connected account is directed to the
[Account Management embedded
component](https://docs.stripe.com/connect/supported-embedded-components/account-management),
where they can confirm their account information and agree to paperless delivery
of their 1099 tax form. They can also edit information other than tax
information in the Account Management component.

![The Account Management embedded
component](https://b.stripecdn.com/docs-statics-srv/assets/embedded-paperless-consent.a38f74c68db322c2143e76aa055349c0.png)

The Account Management embedded component

Your accounts could get blocked if you’ve applied 1099 capabilities and the
connected account updates their value to a name and TIN combination that doesn’t
match against IRS records. Similarly, if Stripe is unable to complete KYC
requirements on them based on the information they provided, their account
payouts are blocked until they correct their information.

### Connected account owners agree to paperless delivery

When your connected account edits their tax form delivery method, they can agree
to paperless delivery.

![The dialog to select the option of paperless delivery of tax
forms](https://b.stripecdn.com/docs-statics-srv/assets/embedded-select-edelivery-option.0d6a7bf8fcae3ca9c2615512a64a47bf.png)

The dialog to consent to paperless delivery of tax forms.

![The dialog to consent to paperless delivery of tax
forms](https://b.stripecdn.com/docs-statics-srv/assets/embedded-edelivery-consent.646bb83a2fa6c412b5dc0bffca36e845.png)

Currently, connected accounts can’t request a paper copy in addition to the
e-delivery of the tax form.

### Your connected account receives the e-delivery email from Stripe

After you file 1099 tax forms in your platform’s Stripe Dashboard, your
connected account receives an email from Stripe to view their tax form
electronically. The subject line reads “Your [Platform_Name] 1099 tax form is
ready.”

![The 1099 electronic delivery email to
users](https://b.stripecdn.com/docs-statics-srv/assets/tax-reporting-edelivery-email-2024.8e2ee57ace01f94b25d9d97068a0f8e1.png)

### Connected accounts download their tax forms

#### Note

Past forms will be visible ahead of 1099 tax form filing in January 2025, and
new forms will appear after they’re filed.

Your connected account can download their form after your platform makes it
available through the [Documents Embedded
Component](https://docs.stripe.com/connect/supported-embedded-components/documents).
Tax invoices and other documents are also available through this component.

![Documents embedded component where payees can download their 1099 tax
forms](https://b.stripecdn.com/docs-statics-srv/assets/tax-documents-component-example.817d1d651866b54a159fdbef3d751c29.png)

The Documents embedded component where payees can download their 1099 tax forms.

Most connected accounts are prompted to enter the last four digits of the TIN on
their 1099 tax form before being able to download a copy of the form.

## Links

- [contact Stripe Support](https://support.stripe.com/)
-
[integrate](https://docs.stripe.com/connect/deliver-tax-forms#file-deliver-embedded)
- [configure](https://docs.stripe.com/connect/embedded-comms)
- [tax form settings](https://dashboard.stripe.com/settings/connect/tax_forms)
- [Account Management embedded
component](https://docs.stripe.com/connect/supported-embedded-components/account-management)
- [Documents Embedded
Component](https://docs.stripe.com/connect/supported-embedded-components/documents)