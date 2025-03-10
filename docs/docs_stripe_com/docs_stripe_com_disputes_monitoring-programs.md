# Dispute and fraud card monitoring programs

## Learn about the monitoring programs operated by the card networks, and what to do if you're placed into one.

#### Upcoming changes to Visa monitoring programs

The [Visa
section](https://docs.stripe.com/disputes/monitoring-programs#visa-programs)
describes Visa’s new monitoring program and corresponding changes to existing
programs.

As part of your financial obligations to the card networks, you must keep
[disputes](https://docs.stripe.com/disputes) (also called chargebacks) and fraud
at acceptable levels. If they exceed the thresholds dictated by a network (for
example,
[Visa](https://docs.stripe.com/disputes/monitoring-programs#visa-programs) or
[Mastercard](https://docs.stripe.com/disputes/monitoring-programs#mastercard-programs)),
the network places you into one of their monitoring programs. As part of a
program, you can incur monthly fines and additional fees until you reduce your
dispute or fraud levels in a sustained way.

Stripe can work with you on a remediation plan to reduce the levels of disputes
or fraud related to your account. We also communicate directly with the networks
and relay information on a monthly basis. Download our [remediation
template](https://d37ugbyn3rpeym.cloudfront.net/docs/files/compliance/monitoring_program_remediation_template.pdf)
to get started.

While monitoring programs are comparatively rare, take them seriously. If you’re
placed into one, you must take immediate action to address the situation.
Failure to comply with the requirements of a program within the specified time
period can result in the network refusing to process further payments to you.
This can put your ability to accept any credit card payments [at
risk](https://docs.stripe.com/disputes/match).

#### Note

This page is a general guide for Stripe users, not a comprehensive reference for
card network monitoring programs. For complete and up to date information about
monitoring programs, see the documentation provided by the networks.

## Understanding disputes and chargebacks

For the purposes of monitoring programs, a dispute or chargeback occurs when
funds move out of an account due to a disputed payment, regardless of the
reason. The terms “dispute” and “chargeback” are interchangeable. The Visa
monitoring program refers to disputes, while the Mastercard and AusPayNet
monitoring programs refer to chargebacks.

Monitoring programs don’t consider refunds when identifying disputes. In some
cases, if you issued a full refund at least 10 days before a dispute, we can ask
to have the dispute removed from the account. The issuer might have missed the
refund and raised the dispute by mistake, but that rarely happens.

Similarly, monitoring programs don’t consider dispute outcomes. If they did,
they’d have to wait for the outcome of every dispute, which can take months,
before including it in their calculations. They’re also more interested in how
successfully you prevent disputes than in whether you win them.

Some disputes where you have no liability don’t appear in your Dashboard or API
responses because Stripe handles them on your behalf. They don’t count toward
your Stripe dispute or fraud rates, and we don’t charge you for them. However,
monitoring programs still include them in their calculations. That can create a
discrepancy between your data and the dispute rates that the networks calculate
for you, especially if you issue a lot of refunds. For example:

- You refunded the payment before the customer submitted the dispute.
- The dispute duplicates a previously resolved dispute.
- The card network created or processed the dispute in error.

In some cases, the data reported to Stripe by the card networks doesn’t match
the data visible in your Dashboard. It can happen because of discrepancies or
formatting issues in your statement descriptors, having multiple Merchant IDs
(MIDs), or double-counted charges. If Stripe updates your MID during a month, it
can affect your Mastercard data. If you think a card network made a calculation
error, contact [Stripe support](https://support.stripe.com/).

The following scenarios don’t count as disputes:

- Unescalated
[inquiries](https://docs.stripe.com/disputes/how-disputes-work#inquiries), where
a card issuer begins an investigation but never returns the disputed payment.
- [Early fraud
warnings](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings)
(EFWs), which are informational messages from card network reports about
suspected fraud. Although they don’t count as disputes, they do count as fraud,
regardless of their outcome, and Visa’s
[VFMP](https://docs.stripe.com/disputes/monitoring-programs#vfmp) program
includes them in its calculations.
- Non-disputed funds that move through a card network’s dispute system. Such
movement can occur as part of Visa’s [Rapid Dispute
Resolution](https://docs.stripe.com/disputes/how-disputes-work#respond-dispute)
program.

## Monitoring program calendars

Visa and Mastercard monitoring programs track activity by month, while the
AusPayNet monitoring program tracks activity by quarter.

Visa and Mastercard programs calculate monthly rates differently. Visa
calculates the ratio of disputes or fraud to the total number of payments in the
same calendar month. Mastercard calculates the ratio of disputes or fraud to the
total number of payments in the previous month. Both networks assign a dispute
or fraud report to the month in which they received it, regardless of when the
original payment occurred.

Visa and Mastercard monitoring programs use specific nomenclature to refer to
their monthly rate calculations:

A “data month” is the month in which a network receives a dispute or fraud
report. Mastercard refers to two different data months, one for disputes and the
other for sales.

A “report month,” “reporting month,” or “identification month” is the month in
which a program identifies a business based on its data meeting a threshold.
It’s usually the month after the data month containing that data.

## Estimate your dispute or fraud rate

If you have [Stripe Sigma](https://stripe.com/sigma) or [Data
Pipeline](https://stripe.com/data-pipeline), you can use it to [track your
estimated dispute or fraud rate for a given monitoring
program](https://docs.stripe.com/stripe-data/query-disputes-and-fraud-data#tracking-monitoring-programs).
We offer [a guide to help you implement a continuous fraud management
process](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)
using those tools.

If you don’t have either of those products, you can manually estimate your
dispute rate. Export your Visa or Mastercard disputes from the **Payments** tab
in your Dashboard and compare them to your payments according to a program’s
formula. Networks count payments by their capture date and disputes by their
creation date. For accounts outside the US, count payments and disputes for a
calendar month. For accounts in the US, there’s a delay between receiving
disputes from our financial partner and reporting them to the card network. To
account for that delay, count payments for a calendar month, and count disputes
from the 5th of that month to the 5th of the following month.

You can also track EFWs using the [Early Fraud
Warnings](https://docs.stripe.com/api/radar/early_fraud_warnings) API. In
addition, when we receive a fraud report for a payment that hasn’t already been
disputed or refunded, we send a notification to the primary email on your
account.

## Visa monitoring programs

Visa evaluates your activity monthly against the thresholds established in their
monitoring programs. If Visa places you in a program, Stripe notifies you. You
have 12 months to meet the thresholds, or Visa can restrict your ability to
accept Visa payments.

### Regional considerations

Except for [VFMP
3DS](https://docs.stripe.com/disputes/monitoring-programs#vfmp3ds), which
applies to US businesses only, Visa enforces its monitoring programs on all
businesses in all Stripe supported countries.

For users in the US, Europe, Canada, Australia, and Brazil, both domestic and
cross-border activity count toward monthly totals. For users outside of those
regions, only cross-border activity is counted.

Visa places individual accounts in its programs, but identifies an account by
the static component of its [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
and its acquiring bank. Because banks often vary by country or region, one
Stripe business might represent multiple monitored accounts to Visa.

- A Stripe business that uses one statement descriptor in Canada and a second
statement descriptor in both Canada and the US qualifies as three accounts to
Visa: one for each descriptor in each country.
- A Stripe business that uses the same statement descriptor in Ireland, France,
and Germany results in only one account because Visa aggregates its EU volume.
- A Stripe business with multiple statement descriptors represents that many
Visa accounts. To aggregate the dispute and fraud rates:- Give each descriptor
the same static prefix.
- If updating existing statement descriptors, ask Stripe to contact Visa and
request that they aggregate your transactions.
- Make the change at the end of a month so it doesn’t affect the rate
calculations for that month.

### VAMP: Visa Acquirer Monitoring Program Effective April 1, 2025

The VAMP program identifies merchants based on:

- VAMP Ratio: (fraud + non-fraud disputes) / total transactions- Fraud is
defined as [early fraud warning
(EFW)](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings)
data sourced from Visa’s TC40 reporting
- Minimum of 1,000 monthly combined fraud and non-fraud disputes
- VAMP Enumeration Ratio: Monthly enumerated transactions / total transactions-
Measures card testing activity
- Minimum of 300,000 enumerated transactions identified

Stripe notifies you if your ratios place you at risk for enrollment. You can
avoid enrollment by reducing your fraud at this time.

VAMP only enrolls accounts it classifies as `Excessive` when their counts and
rates exceed the following thresholds. After the metric falls below the
threshold, VAMP releases the account from the program.

Program Type ThresholdVAMP Ratio- April 1, 2025: 1.5% globally (0.9% in LAC)
- January 1, 2026: 0.9% globally (1.5% in CEMEA)
VAMP Enumeration Ratio20
### VFMP 3DS: Visa Fraud Monitoring Program-3DS (US-only)

VFMP-3DS applies only to US-based users with US-based custom accounts and an
excessive level of fraud on domestic Visa 3D-Secure-authenticated (3DS)
transactions on US-issued cards.

#### Note

By default, Stripe allows all authenticated 3DS payments to go through. You can
adjust your rules to block 3DS payments that are flagged as high risk. You can
also consider other signals that usually apply to normal charges, such as
velocity, transaction size, and CVC/AVS checks.

Visa calculates the fraud level using [early fraud warning
(EFW)](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings)
data sourced from their TC40 reporting. Users are placed into this program if
they meet or exceed the monthly thresholds for both of the following criteria:

- The total USD volume of EFWs for Visa 3DS-authenticated payments (Fraud
Volume)
- The ratio of the USD volume of EFWs for Visa 3DS-authenticated payments to the
USD volume of all captured Visa 3DS-authenticated payments (Fraud Rate)

An EFW belongs to the month in which the TC40 was reported, not the month when
the reported payment was captured. For example, calculations for February
include 3DS-authenticated payments captured in February and EFWs reported in
February for 3DS-authenticated payments, even if the potentially fraudulent
payments were captured in January. The February calculations don’t consider any
payments captured in January.

Early warningStandardFraud volume Fraud rate Fines50,000 USD0.50%None. You have
the opportunity to take action that reduces your fraud level before it exceeds a
threshold where penalties are incurred.
You might not receive an early warning notification if you reach the standard
threshold immediately after reaching the early warning threshold.

### Retiring Visa programs Deprecated as of March 31, 2025

The following guidance relates to the disputes and fraud monitoring programs
Visa enforces until
[VAMP](https://docs.stripe.com/disputes/monitoring-programs#visa-programs)
becomes effective.

#### Early warning notifications

You might receive an early warning notification from Visa if you’re at risk for
being placed in one of its programs. Such notifications give you an opportunity
to preemptively reduce the level of fraud on your account. Early warning
notifications might not occur for accounts that reach a program’s standard or
excessive threshold immediately after meeting its early warning threshold.

#### Remediation

Visa removes you from a program when your level of disputes or fraud drops below
the standard threshold for 3 consecutive months, even if you’re at the excessive
level. If you reach a program’s excessive threshold, excessive penalties apply
until you exit the program entirely. Dropping below the excessive threshold
doesn’t reduce your penalties to the standard level.

#### Note

Dropping below the threshold doesn’t reset your timeline. If you remain below
the threshold for 1 or 2 months, then reach it again, your original timeline
resumes. That means that if 10 months pass without exiting a program, exceeding
the threshold in any month prevents you from exiting before the end of the
timeline.

Monitoring your dispute and fraud levels accurately is important. For example,
Visa counts disputes regardless of whether the dispute was hidden due to a
refund, regardless of liability shift, and regardless of whether you won the
dispute.

As part of the remediation process, Stripe can require you to provide details on
the steps you’re taking and your timeline for implementing them.

#### VDMP: Visa Dispute Monitoring Program

VDMP applies to users with an unusually high level of disputed payments on their
account. Users are placed into this program if they meet or exceed the monthly
thresholds for both of the following criteria:

- The total number of payment disputes (dispute count)
- The ratio of disputed payments to all captured payments ([dispute
rate](https://docs.stripe.com/disputes/measuring#dispute-rate-usage))

A payment dispute belongs to the month in which it’s raised, not the month when
the original payment was captured. For example, calculations for February
include payments captured in February and disputes raised in February, even if
the payments being disputed were captured in January. The February calculations
don’t consider any payments captured in January.

Early WarningStandardExcessiveDispute Count Dispute Rate Fines750.65%None. You
have the opportunity to take action that reduces your dispute level before it
exceeds a threshold where fines are incurred.
You might not receive an early warning notification if you reach the standard or
excessive threshold immediately after reaching the early warning threshold.

#### VFMP: Visa Fraud Monitoring Program

VFMP applies to users with an excessive level of fraud on their account, which
Visa calculates using [early fraud warning
(EFW)](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings)
data sourced from their TC40 reporting. Users are placed into this program if
they meet or exceed the monthly thresholds for both of the following criteria:

- The total USD volume of EFWs (Fraud Volume)
- The ratio of the USD volume of EFWs to the USD volume of all captured payments
(Fraud Rate)

An EFW belongs to the month in which the TC40 was reported, not the month when
the reported payment was captured. For example, calculations for February
include payments captured in February and EFWs reported in February, even if the
potentially fraudulent payments were captured in January. The February
calculations don’t consider any payments captured in January.

Early WarningStandardExcessiveFraud Volume Fraud Rate Fines50,000 USD0.65%None.
You can take action that reduces your fraud level before it incurs penalties.
You might not receive an early warning notification if you reach the standard or
excessive threshold immediately after reaching the early warning threshold.

#### VFMP: Visa Fraud Monitoring Program (digital goods merchants)

The VFMP for digital goods merchants applies to small ticket and digital goods
merchants with excessive levels of fraud on their account. Visa calculates the
fraud level using [early fraud warning
(EFW)](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings)
data sourced from their TC40 reporting. The VFMP for digital goods merchants
applies to businesses with the following MCCs:

- 5735 — Record Stores
- 5815 — Digital Goods Media — Books, Movies, Digital artwork/images, Music
- 5816 — Digital Goods — Games
- 5817 — Digital Goods — Applications (Excludes Games)
- 5818 — Digital Goods — Large Digital Goods Merchant

Users are placed into this program if they meet or exceed the monthly thresholds
for all of the following criteria:

- The total USD volume of EFWs for relevant payments (Fraud volume)
- The total count of EFWs for relevant payments (Fraud count)
- The ratio of the USD volume of EFWs for relevant payments to the USD volume of
all captured relevant payments (Fraud Rate)

An EFW belongs to the month in which the TC40 was reported, not the month when
the reported payment was captured. For example, calculations for February
include relevant payments captured in February and EFWs reported in February for
relevant payments, even if the potentially fraudulent payments were captured in
January. The February calculations don’t consider any payments captured in
January.

Early WarningStandardFraud volume Fraud count Fraud rate Fines15,000
USD1500.45%None. You have the opportunity to take action that reduces your fraud
level before it exceeds a threshold where penalties are incurred.
## Mastercard monitoring programs

Mastercard’s Excessive Chargeback Program (ECP) consists of two levels:
[Excessive Chargeback Merchant
(ECM)](https://docs.stripe.com/disputes/monitoring-programs#ecm) and [High
Excessive Chargeback Merchant
(HECM)](https://docs.stripe.com/disputes/monitoring-programs#hecm), and it
applies to users in all supported countries. The [Excessive Fraud Merchant (EFM)
Compliance Program](https://docs.stripe.com/disputes/monitoring-programs#efm) is
a separate program that applies to users in all supported countries besides
Germany, India, and Switzerland.

If your account exceeds program thresholds, Mastercard places you into that
program and Stripe notifies you. If you exceed both EFM and ECP thresholds,
you’re placed in EFM but not ECP. However, Mastercard tracks both thresholds.
For example, you exceed EFM and ECP thresholds in March and April, but exceed
only ECP thresholds in May. In April, you’re placed in month 2 of EFM and fined
accordingly. In May, you’re placed in month 3 of ECP despite the EFM
identifications taking precedence in prior months.

### Remediation

Mastercard removes you from a program when your chargebacks drop below the
program threshold for 3 consecutive months. If you’re in HECM, and your
chargebacks drop below the HECM threshold but still meet the ECM threshold, you
move to the ECM level.

Monitoring your chargeback and fraud levels accurately is important. For
example, Mastercard counts a chargeback regardless of whether it was hidden due
to a refund, regardless of liability shift, and regardless of its outcome.

As part of the remediation process, Stripe can require you to provide details on
the steps you’re taking and your timeline for implementing them.

### ECP: Mastercard Excessive Chargeback Program

Users are placed into ECP if they meet or exceed the monthly thresholds for both
of the following criteria:

- The total number of payment chargebacks (chargeback count)
- The ratio of the chargeback count for the current month to the total number of
captured payments from the preceding month ([chargeback
rate](https://docs.stripe.com/disputes/measuring#dispute-rate-usage))

A payment chargeback belongs to the month in which it’s raised, not the month
when the original payment was captured. For example, calculations for February
use payments captured in January and chargebacks raised in February, including
chargebacks for payments captured in February.

### ECM: Mastercard Excessive Chargeback Merchant

Dispute Count Chargeback Rate Fines100-2991.5-2.99%Fines begin in month two and
continue at increasing rates in subsequent months. See the timeline below for
details.Number of months above ECM thresholds Fine Issuer recovery assessment10
USDNo21,000 USDNo32,000 USDNo4-65,000 USDYes7-1125,000 USDYes12-1850,000
USDYes19+100,000 USDYes
Issuer recovery assessment applies an additional 5 USD per chargeback fee for
each chargeback over 300 chargebacks. For example, a merchant identified in
month 4 of ECM with 400 disputes is assessed a 5,500 USD fine (5,000 USD +
(400-300) x 5 USD).

### HECM: Mastercard High Excessive Chargeback Merchant

Dispute Count Chargeback Rate Fines300+3%Fines begin in month two and continue
at increasing rates in subsequent months. See the timeline below for
details.Number of months above ECM thresholds Fine Issuer recovery assessment10
USDNo21,000 USDNo32,000 USDNo4-610,000 USDYes7-1150,000 USDYes12-18100,000
USDYes19+200,000 USDYes
Mastercard communicates total fine amounts to merchants through Stripe.

### EFM: Mastercard Excessive Fraud Merchant Compliance Program

Users are placed into EFM if they meet or exceed the monthly thresholds for all
of the following criteria:

- Number of e-commerce Mastercard payments
- The total USD volume of fraud-related chargebacks (net fraud volume) with
dispute reason code 4837 or 4863
- The ratio of the number of fraud-related chargebacks in the current month to
the number of e-commerce transactions in the preceding month (fraud chargeback
rate)
- The percentage of Mastercard payments that use 3-D Secure (3DS)

The fraud chargeback rate uses a similar calculation to the chargeback rate for
ECP, but it considers only fraud-related chargebacks.

EFM applies to users who meet all of the following conditions:

- Minimum of 1,000 e-commerce Mastercard payments
- Net fraud volume is greater than 50,000 USD (15,000 USD for Australia)
- Fraud chargeback rate is greater than 0.50% (0.20% for Australia)
- Total 3DS Mastercard payment count is less than or equal to:- 10% of total
Mastercard payment count (non-regulated countries)
- 50% of total Mastercard payment count (regulated countries)
Number of months above ECM thresholds Fine 10 USD2500 USD31,000 USD4-65,000
USD7-1125,000 USD12-1850,000 USD19+100,000 USD
You can request that Mastercard suspend an assessed fine one time during an open
case. However, only do so if you’re confident that you’ll be below the threshold
to exit the program for the next 3 months. If you request a suspension of fines
and fall below the threshold for 2 months, but exceed it in the following month,
fine assessments continue until you exit the program.

## AusPayNet monitoring programs

The AusPayNet (APN) Card-Not-Present (CNP) fraud mitigation program is designed
to reduce CNP payments fraud within the Australian payment industry (AU-based
users and cardholders only). Where user fraud rates exceed certain defined
thresholds for two consecutive quarters, the APN reserves the option to mandate
[Strong Customer Authentication
(SCA)](https://docs.stripe.com/disputes/monitoring-programs#sca) for all
transactions. Stripe notifies you if your account exceeds program thresholds for
the preceding quarter.

### FMP: APN Fraud Monitoring Program

Users who meet or exceed both the following criteria thresholds are placed into
FMP:

- **Fraud chargeback amount**: Total value (in AUD) of fraudulent chargebacks
received in the quarter is greater than 50,000 AUD.
- **Fraud-to-sales ratio**: The ratio of fraud chargeback amount to sales value
in the quarter is greater than or equal to 0.20

#### Note

APN excludes card-present and 3DS authenticated payment transactions in these
threshold computations.

Number of quarters above FMP thresholds Remediation measures 1You must implement
fraud controls to reduce fraudulent chargebacks. We recommend performing
[SCA](https://docs.stripe.com/disputes/monitoring-programs#sca) on a subset of
CNP transactions that you define as high risk.2You must do one or more of the
following:- Perform risk based SCA (as above)
- Use SCA on all CNP transaction (excluding [SCA exempted
transactions](https://docs.stripe.com/disputes/monitoring-programs#sca-exemptions))
- Introduce more sensitive or effective fraud controls
3You must pass all CNP transactions through to the cardholder’s issuing bank for
SCA. Failure to do so might result in off-boarding.4+You might be off-boarded.
When your CNP transactions fall below the threshold criteria for FMP for one
quarter, APN releases you from the FMP and SCA obligations.

### SCA: Strong Customer Authentication

SCA is an authentication method in which you verify cardholder’s identity using
at least two of the following factors:

- Knowledge factor: something only the cardholder knows, for example a password
- Possession factor: something only the cardholder possess, for example a mobile
phone
- Inherence factor: something the cardholder is, for example fingerprint or
facial recognition

### SCA exemptions

APN exempts the following types of transactions from the SCA requirement:

- Recurring transactions: Series of repeated transactions with SCA applied on
the first charge of the recurring series
- Trusted customer transactions: Transactions where you have previously
identified/authenticated the cardholder and the cardholder uses the same card on
file with matching identifiers
- Wallet transactions: Digital or mobile wallet transactions where the
cardholder identity has been verified and each subsequent transaction is
authorized by the cardholder using biometrics or a passcode

## Best practices for preventing fraud and disputes

Following these guidelines can help you avoid being placed into card network
monitoring programs.

### Prevent identifiable fraud

Consider using separate authorization and capture in combination with review
rules. Issuers are required to report possible fraud for a captured payment,
even if it gets refunded, but aren’t required to report it for a payment
authorization. If you identify and reverse a fraudulent or suspicious payment
authorization before it’s captured, it isn’t reported.

### Prevent disputes for canceled subscriptions

- Offer a quick and easy way to cancel. An in-app cancellation button is often
the best solution, because it doesn’t require the cardholder to wait to confirm
their refund.
- Clearly communicate billing terms up front prior to accepting cardholder
information.
- Require the cardholder to click a button that confirms their agreement to the
billing terms.
- If offering a free or discounted trial, send a reminder before it expires
allowing the cardholder an opportunity to cancel.
- Implement a flexible refund or return policy. For example, if a user cancels
the day after being billed, offer a full or prorated refund.
- Send billing reminders, especially if on a yearly
[subscription](https://docs.stripe.com/billing/subscriptions/creating).
Typically 7 days before a yearly renewal and 2 to 3 days before a monthly
renewal.
- Third party solutions, such as Ethoca and Verifi. These companies work with
certain issuers so that an alert is raised when a chargeback is about to be
initiated, allowing the user an opportunity to refund.

### Prevent disputes for unreceived products

- Clearly communicate shipping times prior to checkout.
- Clearly and quickly communicate any shipping delays and offer an option for
the cardholder to receive a refund if they don’t want to wait.
- Ship items quickly and provide the cardholder with a tracking number when the
item has been shipped.
- For higher value goods, require a signature upon delivery to prevent missing
packages or potential “friendly fraud.”
- Make sure items are well stocked and either indicate when an item is
backordered or remove it from the site.

### Prevent disputes for unacceptable products

- Implement a flexible refund policy and issue them under reasonable
circumstances.
- Clearly describe the items being sold and display accurate images when
possible.
- Reevaluate any products which tend to see higher dispute rates for these
reasons. It’s possible the items could be defective.
- Clearly display the full price of the item, including any taxes, and make sure
to present it to the cardholder before accepting their payment information.

### Prevent friendly fraud disputes

A [friendly
fraud](https://docs.stripe.com/disputes/prevention/fraud-types#friendly-fraud)
dispute occurs when a customer disputes a legitimate charge that they believe to
be fraudulent. The best way to prevent such disputes is to collect as much
information as possible when capturing a payment. For example, clearly
communicate billing terms and shipping times, require the cardholder to agree to
the terms of service, ship only to verified addresses, or require a signature
upon delivery.

### Prevent other types of disputes

Less common disputes, such as `general` or `duplicate`, can indicate things like
an unrecognized statement descriptor or a confusing billing statement. Normally,
such disputes make up a small percentage of the total. However, if you find any
of them to be very common, it could indicate some other issue at the root of the
problem. For example, a large number of `general` disputes can result from
poorly designed receipts that make customers question the amounts they were
charged.

## Links

- [Visa
section](https://docs.stripe.com/disputes/monitoring-programs#visa-programs)
- [prevention guide](https://docs.stripe.com/disputes/prevention)
- [disputes](https://docs.stripe.com/disputes)
- [remediation
template](https://d37ugbyn3rpeym.cloudfront.net/docs/files/compliance/monitoring_program_remediation_template.pdf)
- [at risk](https://docs.stripe.com/disputes/match)
- [Stripe support](https://support.stripe.com/)
- [inquiries](https://docs.stripe.com/disputes/how-disputes-work#inquiries)
- [Early fraud
warnings](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings)
- [VFMP](https://docs.stripe.com/disputes/monitoring-programs#vfmp)
- [Rapid Dispute
Resolution](https://docs.stripe.com/disputes/how-disputes-work#respond-dispute)
- [Stripe Sigma](https://stripe.com/sigma)
- [Data Pipeline](https://stripe.com/data-pipeline)
- [track your estimated dispute or fraud rate for a given monitoring
program](https://docs.stripe.com/stripe-data/query-disputes-and-fraud-data#tracking-monitoring-programs)
- [a guide to help you implement a continuous fraud management
process](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)
- [Early Fraud Warnings](https://docs.stripe.com/api/radar/early_fraud_warnings)
- [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
- [dispute rate](https://docs.stripe.com/disputes/measuring#dispute-rate-usage)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [friendly
fraud](https://docs.stripe.com/disputes/prevention/fraud-types#friendly-fraud)