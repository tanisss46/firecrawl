# Respond to disputes

## Respond to Klarna disputes using the Dashboard or API.

Learn how take action in response to Klarna inquiry disputes and chargeback
disputes.

## Dispute types

### Inquiry disputes

Almost all Klarna disputes begin as inquiry disputes. The exceptions are
disputes raised because of fraudulent transactions, which escalate immediately
to [chargeback
disputes](https://docs.stripe.com/payments/klarna/disputes#chargeback-disputes).

Inquiry disputes are an opportunity to resolve a customer’s issue before the
dispute escalates to a chargeback and carries a fee. Klarna doesn’t accept
evidence to challenge an inquiry dispute. Contact your customer during the
21-day inquiry period. Listen to the customer’s reason for raising this dispute
to find an amicable resolution within the 21-day period preceding automatic
escalation. For example, a customer you successfully reassure that their
purchased goods are delayed rather than undelivered can withdraw their inquiry
dispute directly with Klarna.

You can also perform one of the following actions:

- Accept the dispute. Confirm the disputed amount with the customer and issue a
refund. Refunding during the inquiry dispute period avoids a dispute fee.
- Allow the dispute to escalate. If you’re unable to resolve the issue within
the 21 days, you can submit evidence to challenge the dispute after it escalates
to a chargeback.

#### Refunds as inquiry disputes

Customers paying with Klarna use inquiry disputes as a means to request refunds
from businesses. If you receive an inquiry dispute with the
[Return](https://docs.stripe.com/disputes/categories?card-network=klarna) Klarna
dispute code, consider this the customer’s request for a refund, rather than a
greater dispute against the payment. As with other inquiry disputes, contact the
customer, understand why they’ve requested the refund, and process it
appropriately.

### Chargeback disputes

If an inquiry dispute remains unresolved after the 21-day timeframe, the dispute
automatically escalates to a chargeback dispute. Stripe withholds the disputed
funds and the associated [dispute
fee](https://stripe.com/pricing/local-payment-methods#klarna) from your account
for this payment until the dispute is resolved.

During the chargeback dispute stage, you can counter disputes by [submitting
evidence](https://docs.stripe.com/payments/klarna/disputes#evidence-submission)
to Klarna, either in the Stripe Dashboard or with the API. Starting from the
chargeback dispute creation date, you have 13 days to submit evidence. If you
choose to counter the dispute by submitting evidence, Klarna will evaluate your
response to decide the outcome of the dispute.

- If you win the dispute, Stripe releases the aforementioned withheld funds to
your account, including the associated [dispute
fee](https://stripe.com/pricing/local-payment-methods#klarna).
- If you lose the dispute, Stripe debits the withheld funds, including the
associated [dispute
fee](https://stripe.com/pricing/local-payment-methods#klarna). Klarna then
returns the disputed amount to the customer.

## Funds flow

### Funds flow for a resolved inquiry dispute

The following diagram shows what happens when you resolve the inquiry dispute
without a chargeback escalation.

Customer

Klarna

Stripe

Merchant

Reports a problem with the order

Opens an inquiry dispute

Notifies inquiry dispute is open

Opens an inquiry dispute

Notifies merchant inquiry is open

webhook
Resolves the dispute in 21 days

Verifies the problem is resolved. Customer confirms, it’s resolved

Closes the inquiry dispute

Notifies inquiry dispute is closed

Closes the inquiry dispute

Notifies the inquiry dispute is closed

webhookYou resolve the inquiry dispute without chargeback escalation
When a chargeback dispute is created, Stripe withholds the disputed funds,
including the dispute fee, until Klarna informs us about the dispute outcome. If
you win the dispute, we immediately release the funds to your account, and don’t
charge a dispute fee.

### Funds flow for a won chargeback dispute

The following diagram shows what happens when you win the chargeback dispute
after escalation.

Customer

Klarna

Stripe

Merchant

Unable to resolve the inquiry dispute in 21 days

Verifies the problem is resolved. Customer confirms, it’s open

Opens a chargeback dispute

Notifies the chargeback dispute is open

Opens a chargeback dispute. Dispute amount and dispute fee is withheld from the
merchant balance

Notifies chargeback dispute is created.

webhook
Counter dispute with evidence or accept dispute in 13 days

Submits the merchant action

Decides merchant won the dispute

Notifies chargeback dispute is lost

Notifies chargeback dispute is won

Marks chargeback dispute is won. Releases the dispute fee and dispute amount to
the merchant balance

Notifies chargeback dispute is won

webhookYou win the chargeback dispute after escalation
When a chargeback dispute is created, Stripe withholds the funds, including the
dispute fee, until Klarna informs us about the dispute outcome. If you lose the
dispute, we release the funds to Klarna and charge the [dispute
fee](https://stripe.com/pricing/local-payment-methods#klarna).

### Funds flow for a lost chargeback dispute

The following diagram depicts what happens when you lose the chargeback dispute
after escalation.

Customer

Klarna

Stripe

Merchant

Unable to resolve the inquiry dispute in 21 days

Verifies the problem is resolved. Customer confirms, it’s open

Opens a chargeback dispute

Notifies the chargeback dispute is open

Opens a chargeback dispute. Dispute amount and dispute fee is withheld from the
merchant balance

Notifies chargeback dispute is created.

webhook
Counter dispute with evidence or accept dispute in 13 days

Submits the merchant action

Decides merchant lost the dispute

Notifies chargeback dispute is won

Notifies chargeback dispute is lost

Marks chargeback dispute is lost. Debits the dispute fee and dispute amount from
the merchant balance

Notifies chargeback dispute is lost

webhookYou lose the chargeback dispute after escalation
## Email-based disputes versus Dashboard and API disputes

Prior to November 15 2023, Stripe only supported disputes for Klarna through
emails directly from Klarna to you. Now, Klarna disputes are managed in the
Stripe Dashboard and with the API. This table highlights key differences between
the old email-based disputes process and the new Dashboard and API process:

Email disputesDashboard and API disputesYou don’t receive notifications from
Klarna and Stripe for inquiry disputes.Stripe notifies you in the Dashboard,
API, and by email when an inquiry is opened.You can submit multiple rounds of
evidence for a chargeback dispute.You can only submit a single round of
structured evidence for a chargeback dispute.You have 14 days to submit counter
evidence from the creation date of the chargeback dispute.You have 13 days to
submit counter evidence from the creation date of the chargeback dispute.Dispute
lifecycle management must be built by you on top of the emails you receive from
Klarna.You can manage the entire dispute life cycle and track the status in a
single place using the Dashboard or API.Stripe doesn’t withhold funds when
Klarna creates a chargeback dispute.Stripe withholds the disputed funds when
Klarna creates a chargeback dispute.
When an inquiry dispute starts off as an email dispute, it persists as an email
dispute, even after onboarding to use the Dashboard or API for new disputes. If
you lose an email dispute, it displays as lost in the Dashboard, you receive a
webhook, and Stripe applies the [dispute
fee](https://stripe.com/pricing/local-payment-methods#klarna).

## Evidence submission

To submit evidence against a chargeback dispute, use either the Dashboard or
API:

DashboardAPI
### Submit evidence

- Navigate to the [Disputes Dashboard](https://dashboard.stripe.com/disputes),
and click the **Needs Response** tab.
- Click the disputed payment. If you want to counter the dispute, click
**Counter dispute**.
- Select the reason why you should win the dispute, and click **Next**.
- Enter and attach all the applicable supporting evidence. The `recommended`
label indicates the best documents for the type of dispute.
- After entering all the evidence, verify the information is correct by
selecting the checkbox.
- Click **Submit Evidence**.

For additional guidance on how to submit evidence, see [Responding to
disputes](https://docs.stripe.com/disputes/responding).

If you fail to submit evidence, Klarna will rule the dispute in favor of the
customer.

[OptionalAccept dispute
loss](https://docs.stripe.com/payments/klarna/disputes#accept-loss)
## Guidelines

Follow these guidelines to submit the most relevant evidence for both Dashboard
and API disputes.

Stripe dispute reasonGuidelinesProduct not received- Attach all the shipping
details, such as the tracking number, carrier, shipped date, and customer
communication.
Credit not processed- If you receive the returned product, attach the date when
the customer initiated the return and any other information related to the
return.
- If the customer confirms that the dispute is for a partial order, share the
customer communication and the return order amount.
- If the return hasn’t been received, share when the customer initiated the
return and make a note that the return hasn’t yet been received.
- If the customer didn’t communicate or failed to reply to your request,
document in the evidence when your team attempted to contact the customer, the
number of attempts made, and the lack of response received.
- If you fully or partially refunded the payment prior to it becoming a
chargeback dispute, attach the refund details.
Fraudulent- Share the shipping policy as an attachment or link to your shipping
policy.
General- If the customer confirms that the price is incorrect, attach all the
supporting documents against the claim, such as order details.
- If you fully or partially refunded the payment prior to it becoming a
chargeback dispute, attach the refund details.
[Create test
disputes](https://docs.stripe.com/payments/klarna/disputes#create-test-disputes)
You can simulate dispute creation in test mode by creating a transaction in test
mode using the following email addresses and phone numbers in the given Klarna
checkout region. A dispute automatically opens on the transaction. You can
submit evidence on the dispute, but you can’t simulate the final dispute outcome
in test mode.

Below, we have specially selected test data for the currently supported customer
countries.

AustraliaAustriaBelgiumCanadaCzechiaDenmarkFinlandFranceGermanyGreeceIrelandItalyNetherlandsNew
ZealandNorwayPolandPortugalRomaniaSpainSwedenSwitzerlandUnited KingdomUnited
StatesStripe dispute reasonKlarna dispute reasonEmailPhone numberCredit not
processedReturn`customer+disputed-return@email.au``+61491574118`Product not
receivedGoods not
received`customer+disputed-goods_not_received@email.au``+61491574632`DuplicateAlready
paid`customer+disputed-already_paid@email.au``+61491575254`Product
unacceptableFaulty
goods`customer+disputed-faulty_goods@email.au``+61491575789`GeneralIncorrect
invoice`customer+disputed-incorrect_invoice@email.au``+61491575789`GeneralHigh
risk
order`customer+disputed-high_risk_order@email.au``+61491576801`FraudulentUnauthorized
purchase`customer+disputed-unauthorized_purchase@email.au``+61491577426`
## Dispute API

A [Dispute object](https://docs.stripe.com/api/issuing/disputes/object) contains
a dispute type and Klarna dispute reason. These parameters are useful for
countering a dispute.

### Type

The [Status](https://docs.stripe.com/api/disputes/object#dispute_object-status)
parameter indicates the dispute type. The following table explains the dispute
status and the state of the dispute.

StatusDispute typeDescription`warning_needs_response`InquiryThe inquiry is open
and the business can issue a refund.`warning_closed`InquiryThe inquiry is
closed.`needs_response`ChargebackThe chargeback is open and the business can
submit evidence.`under_review`ChargebackThe chargeback is open and the evidence
is submitted to Klarna.`lost`ChargebackThe chargeback is closed and the business
lost the dispute.`won`ChargebackThe Chargeback is closed and the business won
the dispute.
### Klarna reason

The Klarna reason is mapped to [Stripe dispute
reason](https://docs.stripe.com/disputes/categories?card-network=klarna) and
displayed in the Dashboard as `Network Reason Code`.

The Stripe reason is available in the Dispute object as
[reason](https://docs.stripe.com/api/disputes/object#dispute_object-reason) and
the Klarna reason is available in
[payment_method_details.klarna.reason_code](https://docs.stripe.com/api/disputes/object#dispute_object-payment_method_details-klarna-reason_code).
The data is available in the API and webhook.

## See also

- [Responding to disputes](https://docs.stripe.com/disputes/responding)
- [Dispute
Categories](https://docs.stripe.com/disputes/categories?card-network=klarna)
- [Dispute evidence
object](https://docs.stripe.com/api/disputes/evidence_object)

## Links

- [chargeback
disputes](https://docs.stripe.com/payments/klarna/disputes#chargeback-disputes)
- [Return](https://docs.stripe.com/disputes/categories?card-network=klarna)
- [dispute fee](https://stripe.com/pricing/local-payment-methods#klarna)
- [submitting
evidence](https://docs.stripe.com/payments/klarna/disputes#evidence-submission)
- [Disputes Dashboard](https://dashboard.stripe.com/disputes)
- [Responding to disputes](https://docs.stripe.com/disputes/responding)
- [Dispute object](https://docs.stripe.com/api/issuing/disputes/object)
- [Status](https://docs.stripe.com/api/disputes/object#dispute_object-status)
- [reason](https://docs.stripe.com/api/disputes/object#dispute_object-reason)
-
[payment_method_details.klarna.reason_code](https://docs.stripe.com/api/disputes/object#dispute_object-payment_method_details-klarna-reason_code)
- [Dispute evidence
object](https://docs.stripe.com/api/disputes/evidence_object)