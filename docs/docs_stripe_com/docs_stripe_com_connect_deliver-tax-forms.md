# Deliver your 1099 tax forms

## Learn about 1099 form delivery requirements and how to deliver your tax forms, including e-delivery and postal delivery.

#### Getting your 1099 Forms

If you work for a platform that pays you via Stripe and want to learn about your
1099 forms and how to get them, see [1099 tax
forms](https://support.stripe.com/express/topics/1099-tax-forms) on the Stripe
Support site.

Revenue authorities (such as the IRS) typically require that you deliver a copy
of the tax form to the payee, in addition to [filing the tax
form](https://docs.stripe.com/connect/file-tax-forms). Per IRS recommendations,
the tax form you deliver is a “ B” with the payee taxpayer identification
number (TIN) redacted to the last four digits.

The IRS requires you to provide tax forms to payees using postal mail unless
you’ve obtained consent from the payee to only deliver the forms electronically.
If you don’t obtain consent for e-delivery, you can still e-deliver as long as
you also mail the copy of the tax form to the payee. For more information, see
the IRS [Requirements for Furnishing Information Returns
Electronically](https://www.irs.gov/government-entities/federal-state-local-governments/requirements-for-furnishing-form-1099-g-electronically).

You must deliver tax forms by the first business day on or after January 31. For
postal delivery, tax forms must be postmarked by this date.

Tax forms are always delivered to payees the first time they’re filed with a
revenue authority. This includes e-filing with the IRS as well as states. If a
tax form is both e-filed with the IRS and to a state, it’s only delivered on the
first of these events.

## Delivery options

There are three options for delivering tax forms:

- **E-delivery with a Stripe-built product:** Use a Stripe-hosted Dashboard
(Stripe Express Dashboard) or Stripe Embedded Components to collect e-delivery
consent and deliver tax forms.
- **E-delivery with Tax Forms API** Preview: Use the Tax Forms API to directly
control and manage the entire e-delivery flow.
- **Postal delivery:** Use Stripe to send tax forms using postal delivery.

## E-delivery with interfaces built by Stripe

Your connected accounts can access their e-delivered tax forms through an
interface built by Stripe. If you implemented Stripe Embedded Components, the
link directs your connected account to the Embedded Component. Otherwise, they
can access the tax forms through the interface that they typically use for
non-tax reporting interactions. For instance:

- If a connected account views their payments through the Stripe Express
Dashboard, their 1099 forms are e-delivered there. If you handle the complete
onboarding and management process for your connected accounts and did not
configure Embedded Components for tax reporting, the Express Dashboard is
accessible.

Despite your platform’s eligibility, some connected accounts might not qualify
for e-delivery through an interface built by Stripe. The following connected
accounts aren’t eligible for e-delivery:

- Multi-user accounts
- Vendors without a Stripe account
- Users who have multiple accounts on your platform with the same email address
To view a full list of the types of connected accounts that aren’t eligible for
e-delivery through an interface built by Stripe, see [Which accounts get access
to
e-delivery](https://docs.stripe.com/connect/express-dashboard-taxes#which-accounts-get-access-to-e-delivery).

Connected account users must provide e-delivery consent to view and download
their forms online. The e-delivery consent is applicable to all future
electronic deliveries. Enable postal delivery to make sure that eligible
accounts receive their tax forms. Consult your tax advisors if you want to
completely opt out of paper delivery.

### Prerequisites for using tax form e-delivery

Make sure that the email address is available and current for the connected
accounts on your platform where you own the user experience. You can confirm
that an email address for an account is available. Use the following command to
view the email address for a connected account:

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode email="jennyrosen@gmail.com"
```

### Turn on e-delivery

To turn on e-delivery for your account, open the [Tax forms
settings](https://dashboard.stripe.com/settings/connect/tax_forms) page in the
Dashboard, then choose **Optimize for e-delivery** in the **Delivery settings**
section.

Additionally, you can select the **Have Stripe collect tax information
automatically** option to have Stripe email your connected accounts and ask them
to update their tax information and delivery preferences. Learn more about
[e-delivery for connected
accounts](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough).

### File and deliver 1099 forms with a Stripe-hosted Dashboard

Stripe-hosted Dashboards are surfaces where eligible Connect platforms can
deliver 1099s to their users.

- **Express Dashboard:** Only connected accounts who have access to the Express
Dashboard for non-tax reporting purposes and connected accounts where you own
the full onboarding and management process can have their 1099 forms delivered
to this Dashboard.

Toward the end of January, when you click **File**, your finalized tax forms are
automatically sent out to your connected accounts. They receive another email
notifying them that their tax forms are ready, with a link to download the forms
directly from the **Tax Forms** tab in the Stripe-hosted Dashboard. If a
connected account user later consents to e-delivery, it applies only to future
years because paper forms were already sent for the current year.

![Connect tax forms page showing forms that are ready to download in the Express
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/connect-tax-form-ready-download.45cd97db253255d3fd8878606e74050c.png)

The Connect tax forms page in the Express Dashboard

### File and deliver 1099 forms with Stripe Embedded Components

If your connected accounts currently interact with Stripe Embedded Components or
you own the full onboarding and management process for your connected accounts,
you can deliver 1099 forms with Stripe Embedded Components.

You need to implement the [Documents
component](https://docs.stripe.com/connect/supported-embedded-components/documents)
for your Connected Account to access their 1099 Tax Forms. You should also
implement the [Account management
component](https://docs.stripe.com/connect/supported-embedded-components/account-management)
to collect paperless delivery consent, and allow your connected accounts to make
any necessary edits to their account information.

#### Note

E-delivery consent appears only if the connected account has a populated email
address. For connected accounts where you’re responsible for requirement
collection, including [custom
accounts](https://docs.stripe.com/connect/custom-accounts), Stripe doesn’t set
the `email` field. You can update the connected account’s email address in the
[Dashboard](https://docs.stripe.com/connect/express-dashboard-taxes#how-do-i-update-the-email-address).

## E-delivery with Tax Forms API

#### Private preview

The Tax Forms API is available in limited preview. We are no longer adding users
to the preview for the 2024 tax season.

You can use the Tax Forms API to deliver forms to your users directly. With the
API, you build and brand the e-delivery flow in your platform and Stripe doesn’t
interact with your users directly. You also need to manage the collection of
e-delivery consent, how your users access the e-delivered forms, and any user
identity changes or corrections that go through your platform.

We’ll use a fictitious account StripeDelivers, a delivery platform to walk
through the API.

### Getting started

Stripe recommends disabling e-delivery and outreach from Stripe — otherwise your
users will also have their e-delivered forms accessible through the Stripe
Express Dashboard.

### Collect paperless delivery consent

Per [IRS
requirements](https://www.irs.gov/government-entities/federal-state-local-governments/requirements-for-furnishing-form-1099-g-electronically),
a StripeDelivers account holder who wants to receive tax correspondence
electronically instead of by mail must opt out of receiving postal mail. When an
account holder provides or revokes consent, the app sends a `POST` request to
update the connected account’s tax form settings. If an account holder provides
consent, Stripe doesn’t mail a copy of their 1099-K form unless you require
postal mailing for all accounts in your [delivery
settings](https://docs.stripe.com/connect/tax-form-settings#delivery-method-settings).

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "settings[tax_forms][consented_to_paperless_delivery]"=true
```

### Retrieving tax forms

StripeDelivers wants to create a view of a connected account’s filed 1099-K tax
forms in their platform’s app, to satisfy the platform’s IRS tax reporting
requirement and inform the account holder of their taxable income.

The developer needs to upload each 1099-K to the platform’s servers to make them
available to the view. The app sends a `GET` request for a list of tax forms
from Stripe’s Tax Forms API on each user request.

```
curl -G https://api.stripe.com/v1/tax/forms \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; retrieve_tax_forms_beta=v1;" \
 -d type=us_1099_k \
 -d "payee[account]"={{CONNECTED_ACCOUNT_ID}}
```

When a user requests a PDF version of the form, the app sends a `GET` request to
Stripe’s Files API, caches it, and returns it in the response.

```
curl https://files.stripe.com/v1/tax/forms/taxform_123/pdf \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2022-11-15; retrieve_tax_forms_beta=v1;" \
 -o "/tmp/tmp.pdf"
```

### Notifications

#### Note

To receive `tax.form.updated` webhooks, you need to create a webhook endpoint
with the Tax Forms API beta `Stripe-Version` header.

StripeDelivers wants to notify an account by email when a form is accepted by
the IRS. When StripeDelivers receives a `tax.form.updated` webhook and
determines that the form has moved to `accepted`, it sends an email to the user
with a download link.

## Postal delivery

If you want to mail your tax forms, you must file by January 22, 2025 to
guarantee the tax forms are postmarked by January 31, 2025. You must also
provide a valid US return address to comply with USPS guidelines.

You can use postal delivery for any deliverable address, including PO boxes. For
compliance reasons, Stripe doesn’t allow you to set a PO box as the address for
a connected account; however, you can use [Tax form
editor](https://docs.stripe.com/connect/modify-tax-forms?method=dashboard) or
[CSV
import](https://docs.stripe.com/connect/modify-tax-forms?method=csv#import-tax-forms)
to modify the address on the tax form.

You may have connected accounts that are only eligible for state filing and not
with the IRS. When you use Stripe to file your forms with the IRS and states,
Forms 1099 for the state are mailed to these connected accounts after you finish
filing.

If you use CSV import to override the default delivery method, this also affects
the state mailing. For example, if you set **postal_delivery** to `false`,
Stripe doesn’t mail the 1099 form to the connected account for state reporting.

## Links

- [1099 tax forms](https://support.stripe.com/express/topics/1099-tax-forms)
- [filing the tax form](https://docs.stripe.com/connect/file-tax-forms)
- [Requirements for Furnishing Information Returns
Electronically](https://www.irs.gov/government-entities/federal-state-local-governments/requirements-for-furnishing-form-1099-g-electronically)
- [Which accounts get access to
e-delivery](https://docs.stripe.com/connect/express-dashboard-taxes#which-accounts-get-access-to-e-delivery)
- [Tax forms settings](https://dashboard.stripe.com/settings/connect/tax_forms)
- [e-delivery for connected
accounts](https://docs.stripe.com/connect/platform-express-dashboard-taxes-walkthrough)
- [Documents
component](https://docs.stripe.com/connect/supported-embedded-components/documents)
- [Account management
component](https://docs.stripe.com/connect/supported-embedded-components/account-management)
- [custom accounts](https://docs.stripe.com/connect/custom-accounts)
-
[Dashboard](https://docs.stripe.com/connect/express-dashboard-taxes#how-do-i-update-the-email-address)
- [delivery
settings](https://docs.stripe.com/connect/tax-form-settings#delivery-method-settings)
- [Tax form
editor](https://docs.stripe.com/connect/modify-tax-forms?method=dashboard)
- [CSV
import](https://docs.stripe.com/connect/modify-tax-forms?method=csv#import-tax-forms)