# Authorization signalsDeprecated

## Make informed, real-time decisions with authorization signals.

We provide a set of signals at authorization that you can use to make informed
decisions.

## Verification data

For every authorization that takes place, we compare the values provided during
checkout with the ones on file. We notify you if we detect a mismatch on:

- CVV2 (or security code)
- Card expiration date
- Billing address
- Billing zip code
- PIN number (when entered)

### Identify fraudulent activity

Identifying a mismatch between the card details on file and those entered at
checkout might help you identify fraudulent activity. For example:

- A mismatch between the billing postal code and the one provided at checkout
might represent a card that’s been stolen by a fraudulent actor who’s unaware of
the cardholder’s postal code and attempts to use the card to make a purchase.
- A mismatch between the CVV2 on file and the one entered at checkout might
represent a fraudulent actor cycling through card numbers to find one that
works, without knowledge of the CVV associated with it.

### Reject authorizations

Depending on your risk tolerance and the characteristics of the authorization,
such as whether it’s in person or online, you can reject authorizations if any
mismatches are identified in the verification data values.

## Fraud disputability assessment

Stripe’s fraud disputability assessment evaluates whether an authorization can
be disputed in the event of fraud.

### Make informed decisions based on authorization disputability

Knowing whether or not you can dispute an authorization in the event of fraud at
the time of authorization allows you to make informed decisions. For example,
consider an authorization that is otherwise classified as “medium risk”:

- If you know that you can dispute the authorization if fraud occurs, you can
approve it
- If you know that you can’t dispute the authorization (if fraud occurs), you
can decline it or only approve a lower amount than what’s requested

Stripe assesses disputability likelihood by comparing the characteristics of the
authorization (such as whether 3DS was used or if the card was present with a
chip). We make this assessment against network rules for disputes to proactively
determine what would happen in the event of a dispute.

### Determine the likelihood a dispute can be filed

To determine the disputability likelihood of an authorization in the event of
fraud, examine the
[fraud_disputability_likelihood](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-fraud_disputability_likelihood)
field on the `Authorization` object. This field populates with various enums
that inform you about whether you can dispute the authorization. We label every
authorization as `very_likely`, `neutral`, or `very_unlikely`, or `unknown`:

- When authorizations receive a score of `very_likely`, it’s highly probable
that disputes filed based on these authorizations are accepted by the card
network. The card network rarely rejects `very_likely` authorization disputes.
When they do, it’s typically due to exceptional circumstances. These
circumstances might include a card filing a fraud dispute for the second time or
exceeding the allowable number of disputes for a card within a specific
timeframe defined by Visa.
- When authorizations receive a score of `very_unlikely`, disputes are almost
always automatically rejected by the card network.
- When authorizations receive a score of `neutral`, Stripe assesses that the
dispute outcome depends on various factors. Historically, these disputes are
more likely to be accepted by the card network. However, this behavior might
change at any given point.

Learn more about [fraud disputability
likelihood](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-fraud_disputability_likelihood).

## High-risk business alerts

Use webhook notifications to receive detailed risk assessments of the acquiring
business involved in an authorization.

### Make informed decisions based on risk level

If you have data on the risk level of a business and the likelihood of a
dispute, you can make more informed decisions about which authorizations you
approve or reject. To make this assessment, Stripe evaluates all of the
acquiring transaction activity for a business on Stripe Issuing, including data
such as its historical dispute rate.

### Determine the risk level

To determine the risk level, examine the
[risk_assessment.merchant_dispute_risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-merchant_risk)
hash field on the `Authorization` object. The following example demonstrates how
to use each value.

### Example responses

A low (normal) risk transaction:

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

A high-risk transaction:

```
{
 "id": "iauth_1CmMk2IyNTgGDVfzFKlCm0gU",
 "object": "issuing.authorization",
 // ...
 "risk_assessment": {
 "merchant_dispute_risk": {
 "risk_level": "high",
 "dispute_rate": 47
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
may have been compromised during the attack.

### Make informed decisions based on card testing risk

Stripe automatically intervenes in the most obvious card testing scenarios. We
offer a balanced approach in medium-risk situations to avoid being overly
conservative. These cases require careful consideration of various factors,
including the authorization and cardholder details. As a result, we recommend
the careful evaluation of all relevant considerations before making a decision
on whether to block an authorization.

We assess card testing risk by, among other things, evaluating the frequency and
intensity of “card does not exist” declines associated with a specific bank
identification number (BIN) or merchant. These declines are the most definitive
significant indicator because they often exhibit a noticeable increase in speed
and frequency compared to regular card declines.

### Determine card testing risk

To determine card testing risk, examine the
[risk_assessment.card_testing_risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk)
field on the `Authorization` object. The following example demonstrates how to
use each value. We also provide the following fields:

- `invalid_account_number_decline_rate_past_hour`: Stripe calculates and returns
this value when a decline contains a non-existent PAN.
- `invalid_credentials_decline_rate_past_hour`: Stripe calculates and returns
this value on declines where the PAN exists (or existed in the past), but other
verifications such as the CVV, expiration, and postal code are failing.

#### Example responses

A low risk transaction:

```
{
 "id": "iauth_1CmMk2IyNTgGDVfzFKlCm0gU",
 "object": "issuing.authorization",
 // ...
 "risk_assessment": {
 "card_testing_risk": {
 "invalid_account_number_decline_rate_past_hour": 5,
 "invalid_credentials_decline_rate_past_hour": 3
 }
 }
}

```

A high-risk transaction:

```
{
 "id": "iauth_1CmMk2IyNTgGDVfzFKlCm0gU",
 "object": "issuing.authorization",
 // ...
 "risk_assessment": {
 "card_testing_risk": {
 "invalid_account_number_decline_rate_past_hour": 79,
 "invalid_credentials_decline_rate_past_hour": 83
 }
 }
}

```

Learn more about [card testing
risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk).

## Recommended settings

To get started, enable the following settings that align with your business
needs. While these settings might not be customized to your business model,
geography, or cardholder behavior, you can use them as a source of directional
guidance when using Stripe’s tools. Contact us for support in adjusting these
thresholds.

Optimize for approval rateBalance approval rate and fraud preventionOptimize for
fraud preventionVerification dataBlock on `mismatch` valueBlock on `mismatch`
valueBlock on `mismatch` and `not_provided` valuesFraud disputability
likelihoodNo actionBlock on `very_unlikely` value if fraud is suspectedBlock on
`very_unlikely` value if fraud is suspectedHigh risk merchant alertsBlock on
`high` value if fraud is suspectedBlock on `high` valueBlock on `high` valueCard
testing riskNo actionBlock on `high` value if fraud is suspectedBlock on
`elevated` and `high` values if fraud is suspected
Authorization signals are currently limited to beta users. You must be an
Issuing customer to join the beta. To request access to the beta, log in to your
Stripe account and refresh the page. [Contact
Stripe](https://stripe.com/contact/sales) for more information.

## Links

-
[fraud_disputability_likelihood](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-fraud_disputability_likelihood)
-
[risk_assessment.merchant_dispute_risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-merchant_risk)
- [merchant dispute
risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-merchant_dispute_risk)
-
[risk_assessment.card_testing_risk](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk)
- [Contact Stripe](https://stripe.com/contact/sales)