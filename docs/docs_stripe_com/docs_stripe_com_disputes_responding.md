# Respond to disputes

## Learn how to challenge or accept a dispute.

When an account owner files a dispute against a payment, their bank alerts
Stripe. We then notify you through the following channels:

- Email.
- The Stripe Dashboard.
- A `charge.dispute.created` event (if your integration is set up to receive
events to an [event destination](https://docs.stripe.com/event-destinations)).
- A push notification (if you’ve subscribed).

Each of the dispute notification channels provides a link to the **Dispute**
details page in your Dashboard, where you can learn more about the reason for
the dispute and take appropriate action.

You can see a detailed list of all disputed payments on the [Disputes
tab](https://dashboard.stripe.com/disputes) in the Dashboard. To review or
respond to a dispute, open its details page by selecting it in the list.

When you receive a dispute notification, take action to resolve it before the
deadline. If you don’t respond, you automatically lose the dispute and can’t
retrieve the disputed funds.

[Review the dispute
category](https://docs.stripe.com/disputes/responding#review-reasons)
When you get a dispute, you can see the corresponding category or reason in your
[Dashboard](https://dashboard.stripe.com/disputes) and see the same information
as the `reason` attribute for the [Dispute
object](https://docs.stripe.com/api#dispute_object-reason).

Each dispute category specifies different response requirements and
recommendations to effectively address the cardholder’s root claim. Your first
step is to review our response guidelines for the [dispute
category](https://docs.stripe.com/disputes/categories#dispute-category-types).
This helps you collect the best evidence to counter the dispute claim.

### Inquiries

[Inquiries](https://docs.stripe.com/disputes/how-disputes-work#inquiries) appear
as disputed payments in the Dashboard, but they actually represent a pre-dispute
stage that’s typically issued when an account owner doesn’t recognize a
transaction on their account. Respond in this stage to resolve any questions and
prevent a formal dispute escalation, which saves you time, fees, and your rating
with the card networks.

#### Note

If an inquiry escalates to a chargeback, you must submit another response for
the dispute.

### Fraudulent disputes

To help you navigate fraudulent disputes, Stripe offers Visa CE 3.0 Eligibility
and liability shift.

#### Visa CE 3.0 Eligibility

For fraudulent disputes with the Visa 10.4 (Card absent fraud) code, Stripe
automatically evaluates your transaction history to determine eligibility with
[Visa Compelling Evidence
3.0](https://docs.stripe.com/disputes/categories#visa-ce-30). If your dispute is
eligible, we notify you in the Dashboard and in the dispute email. In these
cases, we encourage [submitting
evidence](https://docs.stripe.com/disputes/responding#respond), because this
eligibility typically translates to a significantly higher likelihood of
overturning the dispute in your favor.

#### Liability shift

For fraudulent disputes that might be covered by the [liability
shift](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
rule, Stripe automatically provides most of the evidence, such as the Electronic
Commerce Indicator (ECI) from [3D
Secure](https://docs.stripe.com/payments/3d-secure).

[Understand the
complaint](https://docs.stripe.com/disputes/responding#understand)
When possible, the **Dispute** details page provides you with a copy of the
bank’s submission to Stripe based on the account owner’s claim. These are actual
documents attached by card networks and can provide additional information about
the disputed transaction, such as a text description from the account owner
describing the specific complaint. When responding to the dispute, make sure to
properly address the issue described in these files.

If the dispute is still open and the bank has provided these files, select
**Review the claim details** under step 1 of the checklist modal in the
Dashboard to view them.

The **Dispute** details page might also provide you with a way to email the
account owner. We recommend contacting them, as it might give you insight to
better understand the complaint and help you decide how to proceed. Be sure to
keep a record of all communication with your customer during this process, as it
provides evidence to submit with your response.

[Accept or challenge the
dispute](https://docs.stripe.com/disputes/responding#decide)
When you have a clear picture of the dispute details, decide whether to accept
or challenge the dispute. If you prefer to handle disputes programmatically,
[use the API](https://docs.stripe.com/disputes/api) to respond to disputes.
Consider the following in your determination:

- Make sure the account owner’s claim is valid. If it’s not, gather the evidence
required to disprove the claim.
- See if you can convince the account owner to withdraw their dispute if you
resolve their complaint amicably. For example, you could offer a store credit or
a replacement item.
- Check to see if the dispute is [CE 3.0
Eligible](https://docs.stripe.com/disputes/responding#visa-ce-30-eligibility).
If it is, consider responding because Stripe provides most of the required
evidence from your transaction history.
- Check to see if the dispute is covered by the [liability
shift](https://docs.stripe.com/disputes/responding#liability-shift) rule. If it
is, consider responding with evidence on top of what Stripe automatically
provides, such as the 3D Secure outcome.

When you’ve decided how to respond, select the corresponding button on the
**Dispute** details page in the Dashboard:

- **Accept dispute**: Submits a response to the issuing bank affirming that you
aren’t contesting the refunded amount.
- **Counter dispute**: Opens a form that guides you through the submission
process, prompts you for evidence relevant to both the dispute and response
type, and allows you to upload supporting files.
[Submit evidence through the
Dashboard](https://docs.stripe.com/disputes/responding#respond)
You have only one opportunity to submit your response. Stripe immediately
forwards your response and all supporting files to the issuing bank. You can’t
edit the response or submit additional files, so make sure you’ve assembled all
your evidence before you submit.

- **Open the dispute response form**: Click **Counter dispute** to open the
Stripe dispute response form.
- **Tell us about the dispute**: In the first page of the form, tell us why you
believe the dispute is in error and the product type of the original purchase.
This information, along with the dispute category, helps Stripe recommend the
most relevant evidence to support your challenge on the next page of the form.
For example, you don’t need to provide shipping details for an online service.
When your integration supports it, Stripe automatically captures the product
type based on the original payment.
- **Assemble your evidence**: The second page of the form has a dynamic set of
sections representing the most relevant details you can provide for your
individual case.

In the **Supporting Files** section, use the File Upload tool to attach evidence
that matches the checklist of evidence types relevant to your dispute type and
counter argument. For each uploaded file, specify which type of evidence it
satisfies. You can only submit one file per type of evidence, so if you have
several files representing one type of evidence, combine them into a single,
multi-page file.

Consider the following guidelines to make sure your supporting files are
effective:

- Consult the evidence recommendations for your specific [dispute
category](https://docs.stripe.com/disputes/categories#dispute-category-types).
- For fraudulent disputes in particular, if your dispute is [Visa CE 3.0
eligible](https://docs.stripe.com/disputes/responding#visa-ce-30-eligibility),
look for the Required for CE 3.0 badge throughout the response form. In most
cases, Stripe pre-populates these fields with the required data from your
transaction history.

- If the field is pre-populated, don’t edit it because you might affect
eligibility.
- If the field is empty, add the requested information, such as the product
description.

If your dispute might be covered by the [liability
shift](https://docs.stripe.com/disputes/responding#liability-shift) rule, we
populate [3D Secure](https://docs.stripe.com/payments/3d-secure) information
such as the Electronic Commerce Indicator (ECI) automatically for you.
- Organize each piece of evidence according to the evidence type it satisfies—be
as succinct as possible.
- Combine items of the same evidence type into a single file.
- Limit your evidence file size to the combined maximum of 4.5 MB.
- Limit your Mastercard evidence file length to the combined maximum of 19
pages.
- Banks evaluating the dispute won’t review any external content, so don’t
include:

- Audio or video files
- Requests to call or email for more information
- Links to click for further information (for example, file downloads or links
to tracking information)
- **Background evidence**: The other sections of the second page vary depending
on the dispute type and your answers on the first page. When your integration
supports it, Stripe automatically captures the data for these sections and
pre-populates both the API evidence object attributes and the form fields in the
Dashboard. If any of these fields aren’t pre-populated, include as much
information as you can before you submit your response. These sections can
include:

- Shipping details
- Refund policy details
- Customer details
- Product details

The more information your integration [collects and passes to
Stripe](https://docs.stripe.com/disputes/prevention/best-practices#collect-information)
when your customer makes a payment, the better your ability to prevent disputes
and fraud from occurring, and challenge them effectively when they do.
- **Submit evidence**: Click the checkbox to acknowledge your understanding that
your response is final. After you submit it, Stripe automatically puts the
evidence you provide into a format accepted by the issuing bank and submits it
for consideration. At this point, you can’t amend what you’ve submitted or
provide any additional information, so make sure to include every relevant
detail.

In some cases, you might have multiple disputes associated with a single
payment. If this occurs, consider responding to each dispute individually.

[Check the dispute status](https://docs.stripe.com/disputes/responding#status)
After you submit a response, the status of the dispute changes to `under
review`. When the issuer informs Stripe of its decision, we inform you of the
outcome by email, in the `charge.dispute.closed` event, and by updating the
dispute status in the Dashboard and the `Dispute` API object to one of the
following:

- `won`: Indicates that the bank decided in your favor and overturned the
dispute. In this case, the issuing bank returns the debited chargeback amount to
Stripe, and Stripe passes this amount back to you. For businesses in Mexico, the
dispute fee might also be returned. Otherwise, the dispute fee isn’t returned.
- `lost`: Indicates that the bank decided in the account owner’s favor and
upheld the dispute. In this case, the refund is permanent and the dispute fee
isn’t returned.

In some cases, the bank provides additional details about the dispute decision.
Select **View issuing bank response** under **Relevant documents** in the
dispute details to view them.

## See also

- [Prevent disputes and fraud](https://docs.stripe.com/disputes/prevention)
- [Dispute monitoring
programs](https://docs.stripe.com/disputes/monitoring-programs)
- [Calculate dispute rates](https://docs.stripe.com/disputes/measuring)

## Links

- [Fraud Stripe Apps](https://marketplace.stripe.com/categories/fraud)
- [event destination](https://docs.stripe.com/event-destinations)
- [Disputes tab](https://dashboard.stripe.com/disputes)
- [Dispute object](https://docs.stripe.com/api#dispute_object-reason)
- [dispute
category](https://docs.stripe.com/disputes/categories#dispute-category-types)
- [Inquiries](https://docs.stripe.com/disputes/how-disputes-work#inquiries)
- [Visa Compelling Evidence
3.0](https://docs.stripe.com/disputes/categories#visa-ce-30)
- [liability
shift](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [use the API](https://docs.stripe.com/disputes/api)
- [collects and passes to
Stripe](https://docs.stripe.com/disputes/prevention/best-practices#collect-information)
- [Prevent disputes and fraud](https://docs.stripe.com/disputes/prevention)
- [Dispute monitoring
programs](https://docs.stripe.com/disputes/monitoring-programs)
- [Calculate dispute rates](https://docs.stripe.com/disputes/measuring)