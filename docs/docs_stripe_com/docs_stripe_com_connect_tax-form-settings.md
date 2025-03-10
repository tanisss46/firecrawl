# Configure tax form settings

## Learn about the settings you can configure for the 1099 forms you send to connected accounts.

#### Getting your 1099 Forms

If you work for a platform that pays you via Stripe and want to learn about your
1099 forms and how to get them, see [1099 tax
forms](https://support.stripe.com/express/topics/1099-tax-forms) on the Stripe
Support site.

Use the [Stripe
Dashboard](https://dashboard.stripe.com/settings/connect/tax-reporting/1099-forms)
to configure the settings for the 1099 forms you send to connected accounts. You
can change almost all tax settings for forms you haven’t filed yet. For example,
if you initially set your tax form to report non-employee compensation using
1099-NEC and later determine you need to report payment transactions using
1099-K, you can change the default form type and automatically update all forms.

If a user with the administrator role configured the tax form default settings
in the onboarding flow for 1099 tax reporting, you can assign the [Tax
Analyst](https://docs.stripe.com/get-started/account/teams) role to a team
member on your account to allow that person full access to features in the [Tax
reporting](https://dashboard.stripe.com/connect/taxes/forms) view.

## Common settings

These settings apply to all tax forms.

Default form typeSets the default type of 1099 form to use to report
compensation or payment transactions. If you need to deliver multiple form
types, you can [change the type of 1099
form](https://docs.stripe.com/connect/modify-tax-forms?method=csv#change-the-type-of-1099-form)
for an account.Payer tax identityUses the platform account’s information (legal
business name and tax identification number) by default. You can change your
payer tax identity if, for example, you want the legal entity on the 1099 form
to differ from the legal entity associated with your Stripe account.Payer
addressUses the platform account’s information by default. This address displays
on the 1099-NEC or 1099-MISC form as the Payer’s address and on the 1099-K form
as the Filer’s address.Payer phone numberUses the platform account’s information
by default. This phone number displays on tax forms as the Payer’s or Filer’s
phone number.Payer state registrationsAdd corresponding state tax registration
or withholding ID when it is required for the states in which you’ll file.
## Delivery method settings

Configure settings for how to deliver your 1099 forms to payees. These settings
apply to all 1099 form types.

Delivery strategyConfigures the default delivery strategy to use, either smart
delivery settings or customize delivery settings.E-deliverySpecifies whether to
e-deliver forms using an interface built by Stripe, including [Stripe Embedded
Components](https://docs.stripe.com/connect/get-started-connect-embedded-components),
the [Stripe Express
Dashboard](https://docs.stripe.com/connect/express-dashboard), and the [Stripe
Dashboard](https://docs.stripe.com/connect/stripe-dashboard). If enabled, all
accounts with a viable email address receive an email when their 1099 form is
available, except in [some rare
situations](https://docs.stripe.com/connect/express-dashboard-taxes#which-accounts-get-access-to-e-delivery).
If an account has given e-delivery consent, they can access their form
immediately. If delivery is through the Stripe Express Dashboard and the
connected previously didn’t have access to it, they must claim their Stripe
Express account before they can access their form.Postal deliverySpecifies
whether to deliver printed copies of 1099 forms via postal mail using the
platform’s US return mailing address.
**Postal Delivery Options**

Disable Postal DeliveryConnected accounts don’t receive tax forms by postal
mail.Optional Postal DeliveryStripe sends printed tax forms through postal mail
to every connected account that hasn’t consented to e-delivery at the time of
filing, or is ineligible to receive e-delivery. If you enabled e-delivery
through an interface built by Stripe, connected accounts can also request a
paper copy of their tax form through their respective interface.Postal
deliveryAll connected accounts receive tax forms by postal mail.
## 1099-K settings

Configure these settings for the
[1099-K](https://support.stripe.com/questions/intro-to-1099-k-tax-forms-for-platforms-and-marketplaces)
forms you send to connected accounts.

Default calculation methodConfigures the default [calculation
method](https://docs.stripe.com/connect/calculation-methods) to use, either
payments that include fees or payments that exclude fees.Filer typeSpecifies if
the platform account is a payment settlement entity (PSE) or an electronic
payment facilitator (EPF).Payment settlement entityAppears if the filer type is
EPF. If so, you must specify the name and phone number for the PSE.Transactions
reportedConfigures the type of transaction that’s processed.
## 1099-MISC settings

Configure these settings for the
[1099-MISC](https://support.stripe.com/questions/intro-to-1099-misc-tax-forms-for-platforms-and-marketplaces)
forms you send to connected accounts.

Payments boxPayment amounts are reported in the specified box on the 1099-MISC
form. For example, choose 3 Other income to display the amount in box number 3.
You can use CSV import to override this box for specific tax forms.Default
calculation methodConfigures the default [calculation
method](https://docs.stripe.com/connect/calculation-methods) to use. You can
choose between payments that include fees, payments that exclude fees, or
payouts only.
## 1099-NEC settings

Configure these settings for your
[1099-NEC](https://support.stripe.com/questions/intro-to-1099-nec-tax-forms-for-platforms-and-marketplaces)
forms.

Default calculation methodConfigures the default [calculation
method](https://docs.stripe.com/connect/calculation-methods) to use. You can
choose between payments that include fees, payments that exclude fees, or
payouts only.

## Links

- [1099 tax forms](https://support.stripe.com/express/topics/1099-tax-forms)
- [Stripe
Dashboard](https://dashboard.stripe.com/settings/connect/tax-reporting/1099-forms)
- [Tax Analyst](https://docs.stripe.com/get-started/account/teams)
- [Tax reporting](https://dashboard.stripe.com/connect/taxes/forms)
- [change the type of 1099
form](https://docs.stripe.com/connect/modify-tax-forms?method=csv#change-the-type-of-1099-form)
- [Stripe Embedded
Components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Stripe Express Dashboard](https://docs.stripe.com/connect/express-dashboard)
- [Stripe Dashboard](https://docs.stripe.com/connect/stripe-dashboard)
- [some rare
situations](https://docs.stripe.com/connect/express-dashboard-taxes#which-accounts-get-access-to-e-delivery)
-
[1099-K](https://support.stripe.com/questions/intro-to-1099-k-tax-forms-for-platforms-and-marketplaces)
- [calculation method](https://docs.stripe.com/connect/calculation-methods)
-
[1099-MISC](https://support.stripe.com/questions/intro-to-1099-misc-tax-forms-for-platforms-and-marketplaces)
-
[1099-NEC](https://support.stripe.com/questions/intro-to-1099-nec-tax-forms-for-platforms-and-marketplaces)