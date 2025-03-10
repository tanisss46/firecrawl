# Advanced fraud tools

## Reduce fraud with Issuing’s advanced tooling.

The Stripe Issuing advanced fraud tools help you identify and prevent
transaction fraud through API signals and tooling. This guide helps you
understand how to use these signals and features to drive down transaction fraud
while minimizing the impact on legitimate transactions.

## Getting started with advanced fraud tooling

Advanced fraud tools provides resources that you can incorporate into decision
making for Issuing authorizations and to prevent unauthorized use. Learn more
about [real time
authorizations](https://docs.stripe.com/issuing/controls/real-time-authorizations).

Using advanced fraud tools allows you to:

- Receive signals assessing several fraud vectors on every authorization,
allowing you to make more informed authorization approval and decline decisions.
- Receive notifications that an issued card has been compromised, allowing you
to proactively cancel and replace high risk cards.
- Trigger SMS-based fraud challenges on any authorization, driving down
fraudulent activity while mitigating the impact to legitimate transaction
activity.

### Use signals for your authorization logic

As a first step, we recommend back-testing your authorization activity and past
transaction fraud against the Stripe API signals to determine the optimal
approve and decline thresholds to set for your portfolio.

When setting thresholds, set them for one of three outcomes, depending on the
needs of your business:

- **Approval rate maximization**: Best if you prefer to approve more
authorizations, even if it means more transaction fraud.
- **Minimize fraud**: Best if you’re trying to keep fraud to a minimum, even if
it means good transactions are more likely to be declined.
- **Balance of approval rate and fraud reduction**: Best if you want a blend of
the previous two options.

In most cases, fraud prevention and approval rate maximization are inversely
related, but you might identify thresholds where you can apply both at the same
time, depending on your portfolio composition. If you’re a new user without much
history to backtest, see our recommended thresholds to start. We recommend
refining these over time based on your fraud outcomes to layer in additional
signals or adjust the thresholds based on performance.

Maximize approval rateBalance approval rate and risk preventionMaximize risk
preventionBlock authorizations with [fraud
score](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-fraud_risk-fraud_score)
above 75Block authorizations with [fraud
score](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-fraud_risk-fraud_score)
above 50Block authorizations with [fraud
score](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-fraud_risk-fraud_score)
above 25
You can also test API behavior by simulating authorizations with specific fraud
signals in test mode through either the Issuing dashboard, or using the API.
Learn more about [test mode](https://docs.stripe.com/test-mode).

To compare your past activity with Stripe API signals, start by identifying
transactions where a fraud dispute was filed, defined as having an
[evidence.reason](https://docs.stripe.com/api/issuing/disputes/object#issuing_dispute_object-evidence-reason)
of `fraudulent`. Then, compare that set of transactions to the set of
transactions flagged by each signal. The amount of overlap between them
indicates how likely a signal is to predict future fraud disputes.

Make sure to analyze a representative sample of recent transactions, but
consider that disputes can take several weeks to report. We recommend looking
only at transactions that occurred within the last 6 months, but not within the
last 60 days.

For example, select a 90-day period ending 60 days ago. Within that period,
compare the set of authorizations scored as
[risk_level](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-fraud_risk-risk_level)
= `high` to the set of transactions that resulted in a fraud dispute. If that
signal flagged 90% of transactions that resulted in a dispute, but only a small
number of transactions that didn’t, then it’s probably a reliable indicator for
you. Alternatively, if that signal flagged only 5% of actually disputed
transactions, then it probably isn’t very reliable for you.

When defining your authorization logic, implement rules that accurately prevent
fraudulent disputes but have limited impact on legitimate authorizations. Aim
for a precision of ~10%, meaning that at least 1 in 10 authorizations declined
by your logic are actually fraudulent.

### Identify and replace compromised cards

Advanced fraud tools notify you through the [Cards
API](https://docs.stripe.com/api/issuing/cards) when Stripe suspects an issued
card has been compromised, making it more likely to drive unauthorized use in
the future. We recommend automatically canceling and reissuing cards when this
occurs. Learn more about [card
replacement](https://docs.stripe.com/issuing/manage-fraud#card-management).

### Send SMS-based fraud challenges in elevated risk scenarios

Even with advanced fraud tools API signals, it might not always be clear whether
to approve or reject an authorization. For example:

- Rejecting a cardholder authorization might leave them without recourse on an
important purchase.
- Cardholders do regularly engage in legitimate spend activity that might look
anomalous (for example, a business trip abroad).
- The authorization looks legitimate but the user is newer to your platform and
requires additional scrutiny.

Fraud challenges allow you to conduct additional verification on authorizations
while mitigating the impact on good card spend. When triggered, fraud challenges
decline an authorization and send an SMS to a cardholder’s phone number and asks
the them to verify they recognize the authorization.

- Unless a fraudulent actor has access to the phone number on file, they won’t
be able to complete this step, stopping the fraud vector.
- If the SMS fraud challenge is successfully delivered, a legitimate cardholder
will be able to complete the prompt, allowing them to retry the authorization
and get through on a second authorization attempt. This reduces the risk that
the cardholder gets stranded at the point of sale, unable to make an important
purchase.

Learn more about [fraud
challenges](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#fraud-challenges).

### Advanced fraud tools feature set

FeatureCategoryDescription[Fraud
challenges](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#fraud-challenges)API
toolingTrigger SMS-based verification of authorizations. Use this to conduct
additional verification of higher risk authorization activity.[Fraud risk
assessment](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#fraud-risk-assessment)Authorization
signalThe Stripe ML model scores the riskiness of every authorization to help
you assess whether to approve or reject it.[Merchant dispute
risk](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#merchant-dispute-risk)Authorization
signalThe dispute risk of the acquiring business on an Issuing authorization,
based on Stripe’s history with the business. The higher the risk value, the more
likely the authorization will result in a dispute. Available at the point of
authorization.[Card testing
risk](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#card-testing-risk)Authorization
signalThe likelihood that the authorization is part of a card testing event. The
higher the risk value, the higher the likelihood that card testing is taking
place. Available at the point of authorization.[Fraud disputability
likelihood](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#fraud-disputability-likelihood)Authorization
signalThe likelihood that an authorization can be disputed in the event of
fraud. If an authorization is likely to be disputable, your odds of recovery in
the event of fraud are higher. Available at the point of
authorization.[Compromised card
alerting](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#compromised-card-alerting)Card
signalThe Stripe assessment of whether card details have been compromised in a
risk event, putting it at increased risk for future unauthorized activity.
## Fraud challenges

Fraud challenges provide you with the ability to request additional, SMS-based
verification in situations you prefer not to outright decline potentially risky
authorizations.

False positive declines can occur in fraud protection. To allow cardholders to
override potential false-positive declines and limit disruption, you can trigger
SMS-based verification.

SMS verification works as an override option to a decline. For cardholders, the
process looks like this:

- Attempt an authorization, but receive a fraud-related decline.
- Successfully complete a fraud challenge by replying to an SMS, sent to the
cardholder’s phone number on file with Stripe.
- Try the authorization again and receive approval.

If you enable fraud challenges, Stripe automatically triggers SMS verification
for authorizations that we consider to be high risk.

If the cardholder successfully completes the verification within 60 minutes, the
business is allow-listed on that card for 7 days. Subsequent authorizations
during that time won’t encounter fraud-related declines.

Learn more about the [fraud challenge
flow](https://docs.stripe.com/issuing/controls/fraud-challenges).

## Authorization signals

During authorization, we provide a comprehensive set of signals that you can use
to make informed approve or decline decisions in real-time webhook responses.

SignalDescription[Fraud risk
assessment](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#fraud-risk-assessment)The
Stripe ML model scores the fraud risk of every authorization to help you assess
whether to approve or reject it.[Merchant dispute
risk](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#merchant-dispute-risk)The
dispute risk of the acquiring business on an Issuing authorization, based on
Stripe’s history with the business. The higher the risk value, the more likely
the authorization results in a dispute. Available at the point of
authorization.[Card testing
risk](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#card-testing-risk)The
likelihood that the authorization is part of a card testing event. The higher
the risk value, the higher the likelihood that card testing is taking place.
Available at the point of authorization.[Fraud disputability
likelihood](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#fraud-disputability-likelihood)The
likelihood that an authorization can be disputed in the event of fraud. If an
authorization is likely to be disputable, your odds of recovery in the event of
fraud are higher. Available at the point of authorization.
## Fraud risk assessment

[Request access](https://support.stripe.com/contact) if you’re interested in our
fraud risk assessment.

## Merchant dispute risk

Receive detailed risk assessments of the acquiring merchant, or seller, involved
in an authorization.

### Make informed decisions based on risk level

If you have data on an acquiring merchant’s risk level and dispute likelihood,
you can make more informed decisions about approving authorizations. Stripe
makes that assessment by evaluating all of the acquiring transaction activity
for a business on Stripe Issuing, including data such as its historical dispute
rate.

[Merchant dispute
risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-merchant_dispute_risk)
provides the dispute rate and risk for a given acquiring merchant across all
Stripe Issuing transaction activity. The higher the value, the more frequently
the merchant’s past authorizations have resulted in a dispute. This value can be
useful when deciding whether to approve the first purchase at a particular
acquiring merchant by one of your cards.

### Determine the risk level

To determine the risk level, examine the [merchant dispute
risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-merchant_dispute_risk)
hash. The following example demonstrates how to use each value.

#### Example responses

A normal risk authorization, where only 5% of past authorizations from this
merchant have resulted in a dispute:

```
{
 "id": "iauth_1CmMk2IyNTgGDVfzFKlCm0gU",
 "object": "issuing.authorization",
 // ...
 "risk_assessment": {
 "merchant_dispute_risk": {
 "risk_level": "normal",
 "dispute_rate": 5
 }
 }
}
```

A high-risk authorization, where 57% of past authorizations from this merchant
have resulted in a dispute:

```
{
 "id": "iauth_1CmMk2IyNTgGDVfzFKlCm0gU",
 "object": "issuing.authorization",
 // ...
 "risk_assessment": {
 "merchant_dispute_risk": {
 "risk_level": "high",
 "dispute_rate": 57
 }
 }
}
```

Learn more about [merchant dispute
risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-merchant_dispute_risk).

## Card testing risk

Card testing is a prevalent form of fraud where fraudulent actors test stolen
card numbers or cycle through primary account numbers (PANs) until they find a
valid one. They use this valid PAN at a business with weak verification
controls. To counteract this, Stripe assesses the likelihood of your involvement
in a card testing attack, takes action on your behalf, and notifies you through
the API about the severity of the incident. Additionally, we assess if any cards
might have been compromised during the attack.

### Make informed decisions based on card testing risk

Stripe automatically intervenes in the most obvious card testing scenarios. We
offer a balanced approach in normal-risk situations to avoid being overly
conservative. These cases require careful consideration of various factors,
including the authorization and cardholder details. As a result, we recommend
the careful evaluation of all relevant considerations before making a decision
on whether to block an authorization.

We assess card testing risk by, among other things, evaluating the frequency and
intensity of “card does not exist” declines associated with a specific bank
identification number (BIN) or business. These declines are the most definitive
significant indicator because they often exhibit a noticeable increase in speed
and frequency compared to regular card declines.

### Determine card testing risk

To determine card testing risk, examine the [card testing
risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk)
hash. The following example demonstrates how to use each value. We also provide
the following fields:

- [Invalid account number decline
rate](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk-invalid_account_number_decline_rate_past_hour):
The percentage of declines because of a card number not existing in the past
hour, taking place at the same business. Higher rates correspond to a greater
probability of card testing activity, meaning fraudulent actors might be
attempting different card number combinations to guess a correct one.
- [Invalid credentials decline
rate](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk-invalid_credentials_decline_rate_past_hour):
The percentage of declines because of incorrect verification data (such as CVV
or expiry) in the past hour, taking place at the same business. Higher rates
correspond to a greater probability of fraudulent actors attempting to use valid
card credentials at businesses with verification requirements. This value
spiking means fraudulent actors likely have a valid PAN but can’t supply valid
verification data.

#### Example responses

A normal risk authorization:

```
{
 "id": "iauth_1CmMk2IyNTgGDVfzFKlCm0gU",
 "object": "issuing.authorization",
 // ...
 "risk_assessment": {
 "card_testing_risk": {
 "risk_level": "normal",
 "invalid_account_number_decline_rate_past_hour": 2,
 "invalid_credentials_decline_rate_past_hour": 1
 }
 }
}
```

A high-risk authorization:

```
{
 "id": "iauth_1CmMk2IyNTgGDVfzFKlCm0gU",
 "object": "issuing.authorization",
 // ...
 "risk_assessment": {
 "card_testing_risk": {
 "risk_level": "highest",
 "invalid_account_number_decline_rate_past_hour": 79,
 "invalid_credentials_decline_rate_past_hour": 83
 }
 }
}
```

Learn more about [card testing
risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk).

## Fraud disputability likelihood

Stripe’s fraud disputability assessment evaluates whether an authorization can
be disputed in the event of fraud.

### Make informed decisions based on authorization disputability

Knowing whether or not you can dispute an authorization in the event of fraud at
the time of authorization allows you to make informed decisions. For example,
consider an authorization that’s otherwise classified as “normal risk”:

- If you know that you can dispute the authorization if fraud occurs, you can
approve it.
- If you know that you can’t dispute the authorization (if fraud occurs), you
can opt to decline it or trigger a fraud challenge for additional verification.

Stripe assesses the disputability likelihood by comparing the characteristics of
the authorization (such as whether 3DS was used or if the card was present with
a chip). We make this assessment against network rules for disputes to
proactively determine what would happen in the event of a dispute.

### Determine the likelihood that a dispute can be filed

To determine the disputability likelihood of an authorization in the event of
fraud, examine the [fraud disputability
likelihood](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-fraud_disputability_likelihood)
field. This field populates with various enums that inform you about whether you
can dispute the authorization. We label every authorization as `very_likely`,
`neutral`, `very_unlikely`, or `unknown`:

- When authorizations receive a score of `very_likely`, it’s highly probable
that disputes filed based on these authorizations are accepted by the card
network. The card network rarely rejects `very_likely` authorization disputes.
When they do, it’s typically because of exceptional circumstances. These
circumstances might include a card filing a fraud dispute for the second time or
exceeding the allowable number of disputes for a card within a specific
timeframe defined by Visa or MasterCard.
- When authorizations receive a score of `very_unlikely`, disputes are almost
always automatically rejected by the card network.
- When authorizations receive a score of `neutral`, Stripe assesses that the
dispute outcome depends on various factors. Historically, these disputes are
more likely to be accepted by the card network. However, this behavior might
change at any given point.

Most issuing activity is classified as `very_likely`, but how often each of
these values populate depends on the composition of your issuing activity. For
example, online authorizations are more likely have `very_likely` values than in
person authorizations. Learn more about [fraud disputability
likelihood](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-fraud_disputability_likelihood).

## Compromised card alerting

Stripe notifies you through the API when we believe a card might have been
compromised. This helps you know when to cancel and reissue a card, file
disputes, or notify a cardholder.

### Prevent subsequent abuse and initiate cardholder communications

Canceling a card suspected to be compromised can help you prevent future
fraudulent use of PANs that have been compromised. You can use these indicators
to initiate communications and a reissuance workflow for cardholders. If Stripe
observes that a card has been compromised in a risk event, we flag the card as
compromised.

### Mitigate risk and take action

When Stripe determines that a card number or PAN has likely been compromised in
one or more of the following risk events, Stripe marks the card as compromised.

- A card testing attack where a successful authorization took place
- The cardholder verified through SMS that they didn’t attempt a past
authorization on the card
- A fraud dispute has been filed on the card in the past
- The PAN was found in a dark web search

When a risk event takes place, we update the [fraud
warning](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-fraud_warning)
hash to notify you. The
[started_at](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-fraud_warning-started_at)
value corresponds to the date that the risk event took place. If a subsequent
risk event takes place, both values update to reflect the most recent event.

If either value is populated, we recommend contacting the cardholder, canceling
the card, and issuing a new one. This mitigates the risk of subsequent
unauthorized use on what a fraudulent actor likely assumes is a valid PAN that
they can make purchases with.

### Using advanced fraud tools through the Stripe Dashboard

If you want to use the authorization signals of advanced fraud tools for fraud
prevention through the Stripe Dashboard, Stripe offers a rules engine. To
request access, please contact Stripe using the contact form at [Stripe
Support](https://support.stripe.com/?contact=true).

## Links

- [real time
authorizations](https://docs.stripe.com/issuing/controls/real-time-authorizations)
- [fraud
score](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-fraud_risk-fraud_score)
- [test mode](https://docs.stripe.com/test-mode)
-
[evidence.reason](https://docs.stripe.com/api/issuing/disputes/object#issuing_dispute_object-evidence-reason)
-
[risk_level](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-fraud_risk-risk_level)
- [Cards API](https://docs.stripe.com/api/issuing/cards)
- [card
replacement](https://docs.stripe.com/issuing/manage-fraud#card-management)
- [fraud
challenges](https://docs.stripe.com/issuing/controls/advanced-fraud-tools#fraud-challenges)
- [fraud challenge
flow](https://docs.stripe.com/issuing/controls/fraud-challenges)
- [Request access](https://support.stripe.com/contact)
- [Merchant dispute
risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-merchant_dispute_risk)
- [card testing
risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk)
- [Invalid account number decline
rate](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk-invalid_account_number_decline_rate_past_hour)
- [Invalid credentials decline
rate](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk-invalid_credentials_decline_rate_past_hour)
- [fraud disputability
likelihood](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-fraud_disputability_likelihood)
- [fraud
warning](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-fraud_warning)
-
[started_at](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-fraud_warning-started_at)
- [Stripe Support](https://support.stripe.com/?contact=true)