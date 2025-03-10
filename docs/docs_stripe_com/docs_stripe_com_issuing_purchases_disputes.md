# Issuing disputes

## Learn how to use Issuing to dispute transactions.

The purpose of a dispute is to recover funds for captured transactions. Disputes
are often used to correct fraudulent transactions or problems with the quality
or delivery of the product.

Stripe offers a guided Dashboard process and an API to submit disputes and
monitor them through to resolution. This process typically takes between 30 and
90 days. If you only manage occasional disputes, we recommend using the
Dashboard. If you manage a high volume of disputes, we recommend
programmatically managing disputes using the API.

If you think a card has been compromised, [cancel and replace
it](https://docs.stripe.com/issuing/cards/replacements) using the Dashboard or
the API before continuing with the dispute process.

## Considerations before initiating a dispute

### Requirements for fraud disputes

Platforms must allow their connected accounts to submit fraudulent disputes
directly to Stripe through a dashboard that you, as the Platform, make available
using our APIs or embedded components. You can’t restrict their ability to
submit such disputes in any way. After fraud disputes are submitted, Stripe will
review them to determine if the cardholder needs to be reimbursed.

### Non-fraud disputes

Make sure that the cardholder has exhausted other means of resolving the issue.
They must attempt to return any products they received, cancel any ongoing
services, and seek a refund directly from the business. Collect documentation of
these attempts to use as evidence when filing the dispute.

### Blocked dispute submissions

Stripe might block fraud dispute submission if the transaction doesn’t qualify
for fraud protection under local regulations and the account holder has no
dispute rights according to network rules.

#### For platforms

If you’re obligated to submit a dispute and you submit it, you’ve fulfilled your
obligation, regardless of if Stripe blocks the submission.

Card networks might consider a dispute invalid for the following reasons (among
others):

- The transaction is a refund and not a
[capture](https://docs.stripe.com/issuing/purchases/transactions).
- The transaction is a mobile push payment transaction.
- More than 110 days have passed since the business captured the transaction.-
However, if you plan to file an Authorization dispute, this deadline is
shorter:- For Visa, the transaction was captured more than 65 days ago.
- For Mastercard, the transaction was captured more than 80 days ago.

In the Dashboard, the dispute transaction button is only enabled for eligible
transactions. In the API, attempting to dispute an ineligible transaction
results in an error.

## Lifecycle

**Unsubmitted**

**Expired**

**Submitted** (the dispute is sent to the card network)

**Lost**

The business receives the dispute

The business refutes with counter-evidence

Stripe refutes the business’s evidence

The business declines, moves toarbitration with card network

The card network makes a final ruling

**Won**

The business accepts liabilityor doesn’t respond

Evidence in favor ofacquiring business

110 daysSubmitRejected≤ 30 days≤ 30 days≤ 30 days≤ 30 days≤ 30 days≤ 30
daysLifecycle of an Issuing dispute
#### Business terminology

In the above diagram, *business* refers to the *acquiring business*, the
business receiving the payment.

Newly-created disputes begin in an `unsubmitted` status. At this point, you can
update their evidence and metadata. After you’ve added all the required
evidence, you can then submit the dispute. If you don’t submit a dispute within
110 days of the transaction clearing, its status becomes `expired`.

Stripe and card networks process disputes that have a status of `submitted`. As
such, you can’t update dispute evidence, but you can still update their
`metadata`. Submitted disputes enter into a multi-step process defined by card
networks and participating banks. After a dispute is resolved, Stripe
transitions it to either the terminal `won` or `lost` status.

## Creation

Fill out the **Dispute Amount** field to indicate the disputed amount (full or
partial). The field’s initial value is the transaction amount. Submissions that
have empty **Dispute Amount** fields create disputes with the full transaction
amount.

!

Dispute Amount field on the Issuing dispute creation page

DashboardAPI - Issuing-onlyAPI - Issuing with Treasury
Click **Dispute transaction** when viewing an eligible transaction. You’ll be
redirected to a form which requests different information based on the dispute
reason and product type (merchandise, services or digital goods). A dispute is
created the first time you click **Save**. If you click **Submit** without
saving, we create a dispute before submitting it.

After you submit a dispute, you can’t modify the information or resubmit the
dispute.

## Update

DashboardAPI
Use the **Unsubmitted** tab to access disputes that are in progress. The
**Submit before** date indicates when the dispute expires.

!

From the individual dispute page, click **Edit submission** to access the form
where you can update the evidence.

## Submission

DashboardAPI
The **Submit** button on the evidence form is enabled when all required evidence
is present.

#### Caution

Review the evidence thoroughly before you submit, because you can’t modify
dispute information after submitting the dispute.

## Resolution

DashboardAPI
Stripe updates a dispute’s status when we hear back from the card network.

If you win the dispute, its status changes to `won` and we credit your Issuing
balance in the form of an `issuing_dispute` [balance
transaction](https://docs.stripe.com/reports/balance-transaction-types#issuing_related).
This balance transaction is accessible in the Dashboard under [All
transactions](https://dashboard.stripe.com/balance) and on the bottom of the
dispute detail page.

#### Note

If you make a transaction in a currency other than your account’s default
currency (for example, a GBP transaction that your USD card pays), Stripe
refunds the won dispute in the transaction’s original currency.

If you lose the dispute, the dispute’s status changes to `lost` and we don’t
credit any amount to your Issuing balance.

!

Viewing a dispute’s balance transactions in the Dashboard.

Stripe processes disputes according to card network rules. These rules are
updated twice a year. You can review the latest rules on each network’s website:

- **Visa**: [Visa Core Rules and Visa Product and Service
Rules](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf)
- **Mastercard**: [Mastercard
Rules](https://www.mastercard.us/en-us/business/overview/support/rules.html)-
The [Mastercard
Chargeback](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf)
guide is especially useful for understanding Mastercard’s dispute rules.

## Testing

DashboardAPI
Stripe’s test mode allows you to test dispute logic without any live mode
effects. For example, we send webhook events, create [balance
transactions](https://docs.stripe.com/reports/balance-transaction-types), and
update your test mode Issuing balance without moving any funds or changing any
balances in live mode.

Similar to live mode, a test mode dispute transitions to `expired` 110 days
after the transaction is captured.

When submitting a test mode dispute through the Dashboard, you can choose the
dispute’s outcome. Selecting **Won** automatically changes the dispute’s
`explanation` field to `winning_evidence`, and selecting **Lost** automatically
changes the dispute’s **explanation** field to `losing_evidence`.

!

## Webhooks

To be notified of changes to your disputes, you can listen for Issuing dispute
[webhook events](https://docs.stripe.com/webhooks). All Issuing dispute events
contain the updated
[Dispute](https://docs.stripe.com/api/#issuing_dispute_object) object.

Webhook eventsTrigger`issuing_dispute.created`Dispute
created.`issuing_dispute.updated`Dispute
updated.`issuing_dispute.submitted`Dispute
submitted.`issuing_dispute.funds_reinstated`Funds transferred to your Issuing
balance (usually associated with `won` dispute
status).`issuing_dispute.funds_rescinded`Funds deducted from your Issuing
balance (usually associated with a provisional credit
clawback).`issuing_dispute.closed`Dispute transitioned into a `won`, `lost`, or
`expired` status.
## Dispute reasons and evidence

You must submit supporting documentation with a dispute. The quality of this
documentation directly influences your chances of winning and the strongest
disputes have clear, descriptive documentation. All relevant information or
documentation must be included when you first submit the dispute.

The type of documentation required depends on the reason for the dispute.
Because of this, it’s important to choose the correct reason.

Disputes can be submitted with one of these reasons:

- **Canceled**: The cardholder canceled or returned merchandise or canceled
services, and the business didn’t process a credit or void a transaction
receipt.
- **Duplicate**: Covers processing error dispute types, including duplicate
transaction, incorrect amount, paid by other means, and so on.
- **Fraudulent**: The cardholder’s details were compromised and the transaction
wasn’t authorized by them.
- **Merchandise not as described**: The cardholder received the merchandise, but
it didn’t match what was presented at time of purchase, or it was damaged or
defective.
- **Not received**: The cardholder participated in the transaction but didn’t
receive the merchandise or service.
- **No valid authorization**: (API only) The business processed a transaction
without a valid authorization.
- **Service not as described**: The cardholder received the service, but it
didn’t match what was presented at time of purchase.
- **Other**: A dispute scenario that doesn’t clearly qualify as any other
dispute reason. Authorization disputes might have this reason (for example, if
filed through the Dashboard).

In the Dashboard, `Merchandise not as described` and `Service not as described`
are consolidated under `Not as described`.

Each reason requires a different set of evidence:

FraudulentNo valid authorizationNot receivedDuplicateMerchandise not as
describedService not as describedCanceledOtherEvidence DescriptionExplanationA
description of the transaction and why the cardholder is disputing it. You can
also use this field to provide an additional explanation that’s not captured
anywhere else. It’s important for the cardholder to verify that they didn’t
participate in the transaction, and that the transaction wasn’t made by someone
known to the cardholder.Additional documentationRelevant documents such as card
statements or return shipping tracking. The files must be in PDF or JPEG format.
Before submitting the dispute, make sure that all text and images are clear and
large enough to be legible in a black-and-white fax transmission. Encouraging
cardholders to keep their billing address up to date is a key component in the
assessment of fraudulent disputes.
### Fraud disputes

You can dispute a transaction for fraud if the cardholder’s card details were
compromised and they didn’t authorize the transaction.

Before filing a dispute:

- Confirm with the cardholder that they didn’t make the transaction in error,
and that it wasn’t made by someone known to them. Transactions made by a friend
or family member, for example, don’t constitute fraud for dispute purposes.
- Cancel the affected card.

In certain situations, you can lose fraud dispute rights for a transaction:

- **For card-present transactions**: A card network might automatically reject a
fraud dispute because liability defaults to the issuer.
- **For card-not-present transactions**: A card network might automatically
reject a fraud dispute if the cardholder was authenticated during the
transaction. That often happens when [3D
Secure](https://docs.stripe.com/payments/3d-secure) was requested or a secured
payment method like Apple Pay was used.

### Authorization disputes

Each time an acquiring business processes a transaction, they must first request
an authorization from the issuer. If a business captures a payment without a
valid authorization, you can dispute the transaction. The reason you should
choose depends on the method used to submit the dispute:

- **Filing a dispute through the API**: File the dispute under the
`no_valid_authorization` reason.
- **Filing a dispute through the Dashboard**: File the dispute under the `other`
reason and specify in the `explanation` field that the business didn’t get a
valid authorization.

Authorization disputes are distinct from fraud disputes:

- File a fraud dispute when the cardholder didn’t participate in the
transaction. For example, a thief stole their card and used it.
- File an authorization dispute when the business didn’t have a valid
authorization for the transaction. For example, they captured a payment 2 days
after its authorization expired.

A common reason for an authorization dispute is an overcapture. An overcapture
occurs when the captured amount exceeds the authorized amount. When you submit
an authorization dispute for an overcapture, you must adjust the dispute amount
to include only the amount that exceeded the authorization.

#### Note

Some Merchant Category Codes (MCCs) allow overcaptures of certain amounts or
disallow authorization disputes. For details, refer to the current card network
rules for your region.

A card network can reject an authorization dispute if the transaction had a
valid authorization. In the case of an overcapture, it can reject the dispute if
the disputed amount doesn’t take into account the allowed overcapture amount for
the associated MCC.

## Withdrawing

Stripe can only withdraw a dispute within 1 day of its submission to the card
network. If you want to withdraw a dispute, contact [Stripe
Support](https://support.stripe.com/contact) immediately.

## Liability for fraud (platforms in the USA)

Most aspects of Regulation Z don’t apply to business-purpose cards, but
Regulation Z does protect users of business-purpose cards from fraud and other
types of “unauthorized card use," which means the use of a charge card by a
person who doesn’t have the authority to use it. In most cases, an accountholder
can’t be held responsible for unauthorized use of cards linked to their account
unless a reasonable investigation into the fraud is conducted. However, if the
account holder has 10 or more employee authorized users, they might not qualify
for this protection.

When one of your users disputes a transaction because the user believes it was
unauthorized, Stripe sends the dispute to the card network for adjudication (as
with any other type of disputed transaction). Stripe or the card network
determines who must pay for the fraud: you or the business.

If Stripe or the card network determines the business is liable for the fraud,
then neither you nor your user are responsible for the disputed transactions.

If Stripe or the card network determines that you’re liable for the fraud, then
you might be required to pay for the disputed transaction. Stripe performs a
reasonable investigation into the dispute to determine whether fraud actually
occurred or whether the user doesn’t qualify for protection under Regulation Z.
If the investigation uncovers that unauthorized card use actually occurred and
that the user qualifies for protection, then you remain liable for the
unauthorized transactions. Alternatively, if the investigation uncovers that
unauthorized card use didn’t occur or that the user doesn’t qualify for
protection, then we hold the accountholder responsible for the disputed charges.

## Emailing connect accounts

Issuing platforms must send regulated notice emails to connected accounts when a
dispute is submitted, and again when a dispute is won or lost. [Learn more about
regulated
notices](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices).

## Use with Stripe Treasury

Disputes of `ReceivedDebits` on `FinancialAccounts` have a corresponding
[DebitReversal](https://docs.stripe.com/api/treasury/debit_reversals) after the
dispute is submitted.

## Links

- [cancel and replace it](https://docs.stripe.com/issuing/cards/replacements)
- [capture](https://docs.stripe.com/issuing/purchases/transactions)
- [balance
transaction](https://docs.stripe.com/reports/balance-transaction-types#issuing_related)
- [All transactions](https://dashboard.stripe.com/balance)
- [Visa Core Rules and Visa Product and Service
Rules](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf)
- [Mastercard
Rules](https://www.mastercard.us/en-us/business/overview/support/rules.html)
- [Mastercard
Chargeback](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/chargeback-guide.pdf)
- [balance
transactions](https://docs.stripe.com/reports/balance-transaction-types)
- [webhook events](https://docs.stripe.com/webhooks)
- [Dispute](https://docs.stripe.com/api/#issuing_dispute_object)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [Stripe Support](https://support.stripe.com/contact)
- [Learn more about regulated
notices](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices)
- [DebitReversal](https://docs.stripe.com/api/treasury/debit_reversals)