# Remediation link process walkthrough

## Learn how to use remediation links to collect verification information from your connected accounts.

Remediation links allow platform users to collect verification information from
their existing connected accounts. You generate account-specific remediation
links in the Dashboard, then send them to connected accounts through any
communication channels, such as email, chat, in-app notifications, or support
interactions. When a connected account clicks a remediation link, it takes them
to a Stripe-hosted page where they can provide updated information directly to
Stripe.

#### Note

If your connected accounts access Stripe-hosted Dashboards or an interface built
with Connect embedded components, use remediation links to address updated
requirements. Otherwise, configure your integration to address updated
requirements [using account
links](https://docs.stripe.com/connect/handle-verification-updates#collect-updated-information-from-affected-users).

Remediation links are active for 90 days, and an account can access the same
link multiple times. Before generating a link, make sure that it goes to the
right individual by verifying that the account owner is set correctly. If a link
expires, you can generate a new one.

Only the following [user
roles](https://docs.stripe.com/get-started/account/teams/roles) have permission
to generate remediation links:

- Administrator
- Connect Onboarding Analyst
- Developer
- Data Migration Specialist
- Support Associate
- Support Specialist

#### Note

You can only generate remediation links in the Dashboard, not using the API. To
use the API to direct connected accounts to onboarding, create [Account
links](https://docs.stripe.com/connect/custom/onboarding?verification=hosted#stripe-hosted-onboarding),
which are temporary and can only be used once.

The page that a remediation link opens depends on the account’s configuration:

Connected account has access to: Remediation link opens:A Stripe embedded
onboarding component and embedded notification bannerA platform website page
that contains the notification banner; configured in the [platform
Dashboard](https://dashboard.stripe.com/settings/connect/site-links)The full
Stripe Dashboard and no embedded onboarding or notification banner (including
Standard accounts)The Account Status page in the Stripe DashboardThe Express
Dashboard and no embedded onboarding or notification banner (including Express
accounts)The Stripe Express onboarding flowNo Stripe Dashboard and no embedded
onboarding or notification banner (including Custom accounts)Stripe-hosted
onboarding; the account holder must create a Stripe account and verify their
information as the primary account owner or representative
This page walks through the process of generating and sending remediation links
and describes the experience of a connected account when they use a link.

[Generate remediation
links](https://docs.stripe.com/connect/dashboard/remediation-links#generate-remediation-links)
You can generate a remediation link for an individual account or export a list
of remediation links for multiple accounts.

## Generate a link for an individual account

An account might have requirements that you can generate links for. For such
accounts, go to the **Actions required** list in the **Activity** section of the
Account details page. Click an issue to go to the details page for that
requirement.

!

Actions required list

Possible remediation paths, if available, appear as a button or dropdown menu.
Generate the link by clicking **Request from account**.

!

Request information from the connected account

!

The remediation link appears in a dialog.

## Export links for multiple accounts

On the **Accounts to review** page of your Dashboard, filter the view to include
the accounts that you want to generate remediation links for, then click
**Export**. In the export dialog, select **Remediation link** and any other
desired fields, then export the list of accounts.

![Export a list of
accounts](https://b.stripecdn.com/docs-statics-srv/assets/bulk-export-A2R.56ffa4d9f3eb55c08a1eb71ed46f0904.png)

Export a list of accounts

#### Note

If a Remediation Link couldn’t be generated, we don’t have enough information to
verify the account. Make sure that the account data in Stripe includes a primary
account representative, with their full name and date of birth, and an external
payout account.

[Send remediation links to connected
accounts](https://docs.stripe.com/connect/dashboard/remediation-links#send-remediation-links)
You can send remediation links by any communication channel. Because they direct
accounts to a Stripe-hosted page, we recommend that when you send a link, you
inform the account that you partner with Stripe for payments. That explains why
your link takes them to a Stripe-hosted page.

Here’s an example of an email that a platform might use to send a remediation
link:

![Example of a remediation link
email](https://b.stripecdn.com/docs-statics-srv/assets/email-action-required.15e5878a481c6a8726e15965bdfaffe1.png)

Remediation link email

[Understand what a connected account sees when they click a remediation
link](https://docs.stripe.com/connect/dashboard/remediation-links#understand-what-account-sees)
The following example scenarios help you and your support team understand
remediation links from the perspective of a connected account. Select the
Dashboard that’s applicable to your connected accounts.

#### Note

The screenshots are representative examples that might not match the actual
screens presented to your connected accounts.

Embedded componentsFull Stripe DashboardExpress DashboardNo Stripe Dashboard
For connected accounts that used hosted onboarding and have access to the
Notification banner embedded component, remediation links point to the platform
website page that hosts the notification banner. The banner includes information
and links for the connected account to address any open issues.

#### Note

If the platform’s Connect settings don’t include the URL of the Notification
banner component, a remediation link takes the connected account to hosted
onboarding. The behavior is the same as it is for other accounts that don’t have
Stripe Dashboard access.

- **The account reviews the notification banner**

Clicking the link opens the page containing the notification banner. In some
cases, the account [might need to log
in](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components).

The notification banner displays any outstanding tasks.

#### Note

The notification banner appears only if there are outstanding tasks or other
notifications.

![The embedded notification
banner](https://b.stripecdn.com/docs-statics-srv/assets/remediation-furever-banner.dec6fe3e17b4bcf0ded7a9dcbdaa6267.png)

Embedded notification banner

- **The account addresses open tasks**

The account can address a task by clicking the button in the notification. In
this example, clicking **Add information** opens a dialog where they can enter
the required information.

![An information collection
dialog](https://b.stripecdn.com/docs-statics-srv/assets/remediation-furever-dialog.c2f68feec130e92f09cdd5b675fe430d.png)

Information collection dialog

[Handle an unverified account
owner](https://docs.stripe.com/connect/dashboard/remediation-links#verification-failure)
If a connected account owner fails to verify their identity, we tell them to
contact their platform.

![The page shown when a connected account fails to verify their
identity](https://b.stripecdn.com/docs-statics-srv/assets/custom-hosted-form-failure.e25c0e547e804a1a3851be7b2155f5e1.png)

Identity verification failure

If verification fails, verify that the account information is correct and
complete. Then, reset the remediation link through the banner at the top of the
connected account details page.

![The verification failure
banner](https://b.stripecdn.com/docs-statics-srv/assets/remediation-account-security-failure.ed976c409d500dc55f8bfe80ca04ceb3.png)

Verification failure banner

Failure reason Platform actionThe account owner or representative has entered
the wrong information four times.The banner at the top of the connected account
details page requires you to acknowledge a security check before you can reset
the link. Acknowledging the check allows you to reset the link four more times.A
person not listed as the account representative is trying to enter account
information.Update the account representative’s name, date of birth, and last 4
digits of the SSN, and ask them to try the link again. To instead let the
representative update their information directly, use the API to create and
share an [account
link](https://docs.stripe.com/connect/custom/onboarding?verification=hosted#stripe-hosted-onboarding).We
don’t have enough account information (such as the bank account number or last
four digits of the SSN).Add more account details, including date of birth and
last 4 digits of the SSN, then ask the connected account to try the link again.
To instead let the representative update their information directly, use the API
to create and share an [account
link](https://docs.stripe.com/connect/custom/onboarding?verification=hosted#stripe-hosted-onboarding).

## Links

- [using account
links](https://docs.stripe.com/connect/handle-verification-updates#collect-updated-information-from-affected-users)
- [user roles](https://docs.stripe.com/get-started/account/teams/roles)
- [Account
links](https://docs.stripe.com/connect/custom/onboarding?verification=hosted#stripe-hosted-onboarding)
- [platform Dashboard](https://dashboard.stripe.com/settings/connect/site-links)
- [might need to log
in](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)