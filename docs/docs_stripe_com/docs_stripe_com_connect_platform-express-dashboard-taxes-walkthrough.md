# 1099 Tax Reporting Express Dashboard walkthrough

## Learn how to manage 1099 tax forms for connected accounts that use the Express Dashboard.

The images in this section describe an example of the product flow that
connected accounts can encounter when using the Express Dashboard. We provide
these images to help give you and your support teams an idea of the overall user
experience. If you have any questions, contact Stripe Support.

[The Stripe Express
Dashboard](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough#express-dashboard)
For your connected accounts not using Connect embedded components, enabling
e-delivery for tax year 2024 gives them access to the Stripe Express Tax Forms
page. That page is a prebuilt web and mobile dashboard for managing their tax
information and receiving their 1099s electronically.

As you configure your [tax form
settings](https://dashboard.stripe.com/settings/connect/tax_forms), you can also
choose to have Stripe send pre-filing confirmation emails to collect tax
information and paperless delivery consent directly from your connected
accounts. We’ll email your eligible connected accounts starting the week of
November 4.

![Stripe Express dashboard for connected account
taxes](https://b.stripecdn.com/docs-statics-srv/assets/stripe-express-tax-dashboard-2023.4fc699b9b7f560443aacd25b89d14a59.png)

The Stripe Express Dashboard where payees can grant e-delivery consent, download
their 1099 tax forms, and update their tax information.

![Stripe Express dashboard for connected
accounts](https://b.stripecdn.com/docs-statics-srv/assets/stripe-express-dashboard.75de9515d0222275afb3c67a4d6117c4.png)

Connected accounts can also use the Express Dashboard to view their available
balance, see upcoming payouts, and track their earnings in real time.

#### Note

To prevent accounts that don’t normally access the Express Dashboard from using
it, or if you don’t want Stripe to email your connected accounts, select postal
delivery and disable electronic delivery in your [tax form
settings](https://dashboard.stripe.com/settings/connect/tax_forms).

[Your connected account receives an email from
Stripe](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough#receive-email)
Your connected account receives an email from Stripe asking them to confirm
their tax information and update their delivery preferences. The subject line
reads ‘Get your [Platform_Name] 2024 tax forms faster by enabling e-delivery.’
The following image displays the content of the email.

![Stripe Express Tax form email from
Stripe.](https://b.stripecdn.com/docs-statics-srv/assets/tax-reporting-prever-email-2024.3a2bddb9602387c7cf916aa9b9829a45.png)

Pre-filing confirmation email from Stripe

[Connected Accounts are prompted to claim their account on Stripe
Express](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough#verify-info)
For connected accounts without existing access to the Express Dashboard,
clicking the **Get Started** button in Stripe’s email takes them to this screen.

For connected accounts that can access the Express Dashboard but aren’t logged
in, the button opens a login screen. Authenticated accounts with Express
Dashboard access proceed directly to the next step.

![The Stripe Express page to create an
account.](https://b.stripecdn.com/docs-statics-srv/assets/tax-create-stripe-express-account.7bfe7be3830ecb6ca313cadfa256e758.png)

The Stripe Express page to create an account

[Connected account owners with existing accounts are presented with phone number
verification](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough#two-factor)
This screen requests a code sent to the phone number associated with the
connected account.

![Stripe Express account two-factor authentication
dialog.](https://b.stripecdn.com/docs-statics-srv/assets/tax-verify-phone.a6b5b1e2455c322950902d1355324d4d.png)

The Stripe Express account phone number verification dialog.

[After passing phone number verification, accounts new to Express are asked to
verify their
identity](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough#verify-identity)
This step applies only to connected accounts that claimed Express Dashboard
access in the earlier step and haven’t onboarded to Stripe Express. Other
accounts proceed to the next step.

Stripe provides the connected account with prompts to verify their identity by
providing details matching their account information. If, after a few attempts,
they’re unable to enter matching details, we prompt them to confirm their
details with you, the platform. The error message reads “One of the fields
didn’t match the information we received from [Platform_Name]. You can try
again, or check that your information with [Platform_Name] is up to date.”

![Stripe Express account Verify your identity
dialog](https://b.stripecdn.com/docs-statics-srv/assets/tax-verify-identity.7f5df7551dfbb1801cdde12ed9c0dd36.png)

The Stripe Express account **Verify your identity** dialog.

[After verifying their identity, connected accounts are taken to the Tax forms
page of Stripe
Express](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough#tax-forms-page)
After the connected account’s details are verified, they’re taken to the **Tax
forms** page in Stripe Express where they can confirm their tax information they
have on file for their account and agree to paperless delivery of their 1099 tax
form.

![The Tax forms page of the Express
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-page.0430a010ebfa14b6c8914a90376e7a49.png)

The Tax forms page of the Express Dashboard.

They’re prompted to confirm tax information but can choose to skip temporarily
if they want to leave their information as is. Your accounts could get blocked
if you’ve applied 1099 capabilities and the connected account updates their
value to a name and TIN combination that doesn’t match against IRS records. If
the connected account is verified and then changes their name or TIN, they’re
asked to re-sign a new Stripe Terms Of Service Agreement. Similarly, if Stripe
is unable to complete KYC requirements on them based on the information they
provided, their account payouts are blocked until they log back in to Stripe
Express and correct their information.

![The dialog displayed to connected accounts to confirm their
information.](https://b.stripecdn.com/docs-statics-srv/assets/tax-confirm-information.1801e85e31759f80b4e3ffd7fe974778.png)

The dialog displayed to users to confirm their information.

[Connected account owners agree to paperless
delivery](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough#for-delivery)
After the tax information is confirmed, Stripe prompts the connected account to
agree to paperless delivery.

![The dialog to consent to paperless delivery of tax
forms](https://b.stripecdn.com/docs-statics-srv/assets/tax-consent-edelivery.603807401bba412dd0c3bc383d5abd52.png)

The dialog to consent to paperless delivery of tax forms.

If you’ve enabled optional postal delivery, after agreeing to paperless delivery
consent, your connected accounts can choose to request a paper copy in addition
to the e-delivery of the tax form.

![The dialog to optionally request a paper copy of tax
forms](https://b.stripecdn.com/docs-statics-srv/assets/stripe-express-tax-postal-delivery-option.9fe97c25a15822fbe4713b2c281ec96a.png)

[Your connected account receives an email from
Stripe](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough#email-from-stripe)
After filing 1099 tax forms in your Stripe dashboard, your connected account
receives an email from Stripe to view their tax form electronically. The subject
line reads ‘Your [Platform_Name] 1099 tax form is ready.’ The following image
displays the content of the email.

![The 1099 electronic delivery email to
users](https://b.stripecdn.com/docs-statics-srv/assets/tax-reporting-edelivery-email-2024.8e2ee57ace01f94b25d9d97068a0f8e1.png)

[Connected account owners can download their tax
forms](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough#display-tax-forms-page)
After a connected account agrees to the e-delivery terms, they can download
their form when your platform makes it available.

![Stripe Express dashboard where payees can download their 1099 tax
forms](https://b.stripecdn.com/docs-statics-srv/assets/stripe-express-tax-dashboard.78c8723a939c34a01e17ae807ffa31d2.png)

The dashboard where payees can download their 1099 tax forms.

Most connected account owners are prompted to enter the last four digits of the
TIN on their 1099 tax form before being able to download a copy of the form.
Downloads aren’t available for 24 hours after an update has been made to any
personal identity information including name, address, business type, or TIN.

![The dialog to verify your SSN information to securely access tax
forms.](https://b.stripecdn.com/docs-statics-srv/assets/tax-forms-secure-access.5d000d31ccbd402d50cb3a2731dce4f2.png)

#### Caution

Connected accounts that do not agree to paperless delivery are unable to
download their 1099 tax forms and resolve the call to action in their dashboard.
Turn on paper delivery in your Stripe [Tax form
settings](https://dashboard.stripe.com/settings/connect/tax_forms) to make sure
that recipients who don’t consent to e-delivery still receive paper forms.

## Links

- [tax form settings](https://dashboard.stripe.com/settings/connect/tax_forms)