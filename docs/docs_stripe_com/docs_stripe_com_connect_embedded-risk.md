# Embedded Stripe Managed Risk

## Embed Stripe risk management features into your own website.

With [Stripe Managed
Risk](https://docs.stripe.com/connect/risk-management/managed-risk), we provide
an end-to-end business risk management solution and your platform isn’t liable
for your connected accounts’ negative balances. For connected accounts without
access to a Stripe-hosted dashboard, Stripe Managed Risk requires that your
website includes the following embedded components:

- Account onboarding
- Account management
- Notification banner

Through those embedded components, Stripe provides:

- Ongoing monitoring and detection of connected accounts’ credit, fraud, and
supportability risk
- Risk interventions to ensure business supportability and prevent losses
- Co-branded emails and embedded notifications to inform businesses of
interventions
- Embedded forms to respond to and remediate interventions
- Stripe risk operations to review merchant information and make risk decisions
- Stripe liability for connected account negative balances

## Risk interventions

With Stripe Managed Risk, Stripe takes the following actions throughout a
connected account’s operations:

- Verifies the information collected during onboarding
- Evaluates ongoing fraud risk
- Monitors compliance

When Stripe detects elevated risk or non-compliance, we raise a risk review or
apply a risk intervention, which is an action taken to mitigate losses, such as:

- Pausing payouts or charges
- Holding reserves
- Prohibiting the account from using payment processing services

While some high-priority interventions have consequences that take effect
immediately, most interventions notify connected accounts with a deadline to
respond before their business is disrupted. Connected accounts are responsible
for promptly reviewing and responding to interventions.

## Emails

When Stripe raises a risk intervention, we email the connected account to notify
them of the issue. The email provides high-level guidance on:

- What the business must do to resolve the issue
- By when the business must address the issue
- Consequences to the business if no action is taken

Risk intervention emails might include links to more information about a
particular topic, such as restricted business lists or how card brand monitoring
programs work. Emails might also include links to details about activity on the
connected account, like disputed payments or reserve balances.

Emails sent to fully embedded connected accounts include:

- Co-branding
- A primary button that takes users to the embedded notification banner (as
configured in your Connect
[Emails](https://dashboard.stripe.com/settings/connect/emails))
- Links leading to the co-branded support site (see Support) and your embedded
components

The following example shows a fully embedded risk intervention email:

![Sample risk intervention email from the Furever
demo.](https://b.stripecdn.com/docs-statics-srv/assets/embedded-managed-risk-email.0084c37ff7da0310d58aabebd565d2e5.png)

## Notification banner

In addition to notifying connected accounts about risk interventions through
email, Stripe also renders alerts via the [notification banner
component](https://docs.stripe.com/connect/supported-embedded-components/notification-banner).
The notification banner only appears when there are active notifications.

The notification banner provides high level guidance on:

- What the business must do to resolve the issue
- By when the business must address the issue
- Consequences to the business if no action is taken

![Sample embedded risk notification banner from the Furever
demo.](https://b.stripecdn.com/docs-statics-srv/assets/embedded-managed-risk-notif.c24e386e68a8a56ded5eefb122049842.png)

In the example above, the banner shows a single notification requiring action
within 2 days to continue taking payments and receiving payouts. The banner’s
headline states whether the intervention affects payments, payouts, or both.

The banner can also have multiple notifications to help connected accounts
quickly address all open issues.

![Sample of multiple embedded risk notifications in the
banner.](https://b.stripecdn.com/docs-statics-srv/assets/embedded-managed-risk-notif-multiple.9c9218df9607342367840d9d35656cab.png)

Multiple notifications in the embedded notification banner

The notification’s due date indicator shows how much time is remaining and
becomes red to indicate overdue requirements that the connected account must
address urgently to avoid consequences.

![Sample past due embedded risk
notification.](https://b.stripecdn.com/docs-statics-srv/assets/embedded-managed-risk-notif-pastdue.98fa5f8c10d84861178fbbb51392d8be.png)

Notification for a past due risk intervention

After the connected account responds, the notification updates to indicate that
no action is required.

![Sample embedded risk in-review
notification.](https://b.stripecdn.com/docs-statics-srv/assets/embedded-managed-risk-notif-inreview.7d990f036474fc4d0a630867e202ee13.png)

Notification for an in-review risk intervention

When all notifications are in review the banner automatically collapses and can
be expanded to see more details.

![embedded-managed-risk-notif-collapse](https://b.stripecdn.com/docs-statics-srv/assets/embedded-managed-risk-notif-collapse.99b06a09be12ecd64d30c8116b930f3c.png)

Collapsed notification banner

The banner informs your connected account when Stripe suspends their operation
and provides a means for contacting support to appeal.

![embedded-managed-risk-notif-reject](https://b.stripecdn.com/docs-statics-srv/assets/embedded-managed-risk-notif-reject.94843e428028f640d3ea79f8bac8822c.png)

Notification of unsupportable business

## Responding to interventions

Notifications in the [notification
banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner)
include a button that the account user can click to respond directly in a modal
window. In the following example, the notification prompts the user to complete
an identity verification.

![embedded-managed-risk-remediation-ID](https://b.stripecdn.com/docs-statics-srv/assets/embedded-managed-risk-remediation-ID.e518cff147ff3ef2d8c7fa3b6d7455f5.png)

Embedded identity verification

Connected accounts must authenticate with Stripe to resolve risk interventions
in the modal window.

Some interventions might request additional information about the business or
its operations, which the user can provide and submit directly from within the
modal, as shown in the following example.

![embedded-managed-risk-remediation-form](https://b.stripecdn.com/docs-statics-srv/assets/embedded-managed-risk-remediation-form.121ec16bc88310db4db00d5ca5ef2dcb.png)

Embedded form to respond to risk intervention

Most intervention emails include a button directing users to the notification
banner where they can respond directly. In rare cases, the email might direct
the user to respond by replying to the email.

## Support for risk issues

If a connected account needs help with a risk issue, they can:

- Contact Stripe’s risk specialist team using the **Contact support** link at
the bottom of the response modal.
- Reply to any risk email to create a support request.

The forms provided through the intervention notifications are the fastest
resolution for risk issues because they minimize the back-and-forth nature of
email communication.

## Links

- [Stripe Managed
Risk](https://docs.stripe.com/connect/risk-management/managed-risk)
- [Emails](https://dashboard.stripe.com/settings/connect/emails)
- [notification banner
component](https://docs.stripe.com/connect/supported-embedded-components/notification-banner)