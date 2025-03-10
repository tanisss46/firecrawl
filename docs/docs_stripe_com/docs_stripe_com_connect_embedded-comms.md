# Email communications in embedded Connect integrations

## Customize Stripe notifications to your connected accounts in a fully embedded integration.

In an embedded Connect integration, when connected accounts must review
information or take action, Stripe sends email communications directly to them.
Those emails direct your connected accounts to embedded components on your
website to review information or take required action. You must provide Stripe
with the URLs for those components so we can include them in the emails.

You can customize the messages that Stripe sends to match your platform brand,
and you can view an account’s Stripe email history on the account’s details
page.

## Communications that Stripe sends to your connected accounts

We send the following emails to your connected accounts:

- **Account emails** verify an account’s information, such as additions or
changes to an email address, phone number, or bank account.
- **Compliance emails** notify accounts to provide required information. Stripe
often needs to collect further information to maintain compliance with our
financial partners.
- **Risk emails** notify accounts when they’re under a risk review. These emails
often provide instructions on how to submit information to resolve a risk
action; for example, to remove a pause on payouts.
- **Tax emails** (only when Stripe collects Stripe fees directly from connected
accounts) notify users when their tax invoices or 1099s are ready to download.

If you want to send any other payments-related emails to your connected
accounts, you must send them yourself. For example, to send emails for new
disputes, [listen for](https://docs.stripe.com/webhooks) the
`charge.dispute.created` event on a connected account. When that event occurs,
use [the Disputes API](https://docs.stripe.com/api/disputes) to get the details
and email them to the account.

You must [update your Connect settings with the
URLs](https://dashboard.stripe.com/settings/connect/site-links) of your payments
and account workflows so Stripe’s email communications can include links for
your accounts to respond.

## Site links to your website components

Emails sent by Stripe that contain a call to action include a link to perform
that action. For example, if we send an email directing a connected account to
respond to a risk notification, it must include a link to the page where you
embedded your Notification banner component.

Before you can create a live mode Account Session, you must provide the URLs
where you have integrated the embedded components into your website. Configure
the sending email domain and embedded component URLs in the **Site links**
section of [your platform’s Connect
settings](https://dashboard.stripe.com/settings/connect/embedded_ui).

#### Note

Test mode environments use the same URLs as live mode.

For embedded components integrated in your site, select **Yes** and enter the
URL of the page that hosts the component. For any actions not handled by an
embedded component, select **No** and enter the URL of the page on your site
where the account can perform the action. After entering the URLs, test them to
verify that they open the right pages. You can test a link by clicking
**Validate**.

You must set URLs for the following:

- Notification banner
- Account management
- Payments
- Payouts
- Balances
- Documents (when Stripe collects Stripe fees directly from connected accounts)

When sending an email, Stripe automatically appends the connected account ID to
the redirect URL as the `stripe_account_id` parameter. Use that parameter to
identify the account and verify that they’re authenticated. Set up the route on
your server to read the parameters and display the correct embedded component.

## Preview and customize communications

You can customize the co-branded communications that we send to your connected
accounts in your [communication
settings](https://dashboard.stripe.com/settings/connect/communication). To
customize a category of emails, click **Preview and customize**.

### Customize email branding

You can set your Business name, Logo, Icon, Brand color, and Accent color.
Stripe uses these values in the co-branded emails we send to your connected
accounts.

### Customize email domain

By default, emails are sent from a stripe.com address. You can [customize the
domain](https://docs.stripe.com/get-started/account/email-domain), but not the
specific address. We set the address automatically [based on the context of the
message](https://support.stripe.com/questions/custom-email-domain).

### Preview and test emails

When you customize a category of co-branded Stripe emails, you can check their
appearance and test their links in the preview on the right side of the page.
Select a specific email from the **Preview** dropdown list. You can also send
test emails to verify that they’re working correctly by clicking **Send email**.

### View the history of emails sent to connected accounts

You can see the emails that Stripe has sent to your connected accounts on the
account details page under **Emails to this account**. To see the details of an
email, including its exact contents, its To: address, and its status (such as
whether it was delivered successfully or was opened), click it in the list.

## Links

- [listen for](https://docs.stripe.com/webhooks)
- [the Disputes API](https://docs.stripe.com/api/disputes)
- [update your Connect settings with the
URLs](https://dashboard.stripe.com/settings/connect/site-links)
- [your platform’s Connect
settings](https://dashboard.stripe.com/settings/connect/embedded_ui)
- [communication
settings](https://dashboard.stripe.com/settings/connect/communication)
- [customize the
domain](https://docs.stripe.com/get-started/account/email-domain)
- [based on the context of the
message](https://support.stripe.com/questions/custom-email-domain)