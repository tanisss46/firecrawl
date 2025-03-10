# Fraud challenges

## Learn about fraud challenges, an additional layer of verification for authorizations.

Turn on fraud challenges to:

- Minimize accidental blocks on transactions that appear fraudulent, but are in
fact legitimate
- Conduct additional verification on authorizations Stripe deems high risk
- Conduct additional verification on authorizations you determine require it

Fraud challenges allow your cardholders to retry non-fraudulent transactions
that would otherwise be blocked by fraud controls. When fraud challenges are
enabled and a transaction is declined for fraud, Stripe sends the cardholder an
SMS message. They can verify whether the transaction was fraudulent by replying
to the message. All cardholders with an associated phone number can use fraud
challenges.

## Before you begin

- Make sure you’re collecting [phone
numbers](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-phone_number)
for your cardholders
- Enable fraud challenges in your [card issuing
settings](https://dashboard.stripe.com/settings/issuing/authorizations)

## High-risk transactions

Stripe blocks transactions above a certain risk level. The risk level of a
transaction is determined by the network you’re using. High-risk authorizations
are identified by a value of `suspected_fraud` in the
[request_history.reason](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)
field, and won’t trigger [issuing.authorization_request
webhooks](https://docs.stripe.com/issuing/controls/real-time-authorizations)
when declined.

## Fraud challenge flow

Stripe starts sending fraud challenges on high-risk authorizations as soon as
you enable the feature in your [card issuing
settings](https://dashboard.stripe.com/settings/issuing/authorizations).

You can see fraud challenge activity with the [Authorizations
API](https://docs.stripe.com/api/issuing/authorizations). Declined
authorizations that were fraud-challenged have a value in the
[fraud_challenges](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-fraud_challenges)
field. Subsequent authorizations that the cardholder verifies as genuine have a
value of `true` in the
[verified_by_fraud_challenge](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-verified_by_fraud_challenge)
field.

The following shows an example of a fraud-challenged and declined authorization:

```
{
 "id": "iauth_1CmMk2IyNTgGDVfzFKlCm0gU",
 "object": "issuing_authorization",
 "approved": false,
 ...
 "fraud_challenges": [{
 "channel": "sms",
 "status": "pending"
 }]
}
```

This example shows a subsequent authorization that has been verified by the
cardholder:

```
{
 "id": "iauth_1CmMk28Jx923VfJJwMCejmX",
 "object": "issuing_authorization",
 "approved": true,
 ...
 "verified_by_fraud_challenge": true
}
```

#### Note

Verified, genuine authorizations trigger `issuing_authorization.request`
webhooks. If you use [real-time
authorization](https://docs.stripe.com/issuing/controls/real-time-authorizations),
consider `verified_by_fraud_challenge` when deciding whether to approve an
authorization. If your cardholder has explicitly confirmed a transaction as
genuine, we recommend that you don’t apply any of your own risk controls.

To use fraud challenges, make sure that:

- The phone number associated with your cardholder is valid and correct
- Existing transaction decline logic in any `issuing_authorization.request`
webhook handler doesn’t conflict with fraud challenges

### Cardholder flow

Your cardholders might receive a challenge and contact your company’s customer
service to learn more. Make sure your internal teams are prepared to answer
questions that they might receive from your customers about these challenges.

When a cardholder receives a fraud challenge, they can override the declined
transaction by verifying that the suspicious transaction is legitimate and
initiated by them. Fraud challenges are only available to cardholders with an
associated [phone
number](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-phone_number).

The cardholder verifies the override with a one-time SMS prompt with the
following language:

Did you attempt a *[amount]* transaction at *[merchant]*? Reply YES if you did,
or NO if not. Reply STOP to opt out

If the cardholder replies “YES,” they receive the following:

Thanks, please wait a moment and try again.

To complete the purchase, the cardholder needs to initiate the transaction a
second time. After retrying, they won’t receive the SMS prompt, and Stripe won’t
block the transaction for being high-risk. If the cardholder instead replies
“NO," they receive the following:

This transaction was declined. We recommend you cancel your card and request a
new one. Review your account for other suspicious transactions.

Cardholders can reply “STOP” to opt out of fraud challenges, and “START” to opt
back in again.

## Fraud challenges for Connect platforms

If you use [Connect](https://docs.stripe.com/issuing/connect) with Stripe
Issuing, turning on fraud challenges enables it for all cardholders across all
connected accounts.

## Availability

Fraud challenges are only available to cardholders with phone numbers in the
following countries. Attempts to send fraud challenges to other phone numbers,
or to cardholders who are physically outside of these countries, won’t be
delivered.

- United Kingdom (+44)
- United States (+1)

Fraud challenges that can’t be delivered because of an unsupported country code
have a
[status](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-fraud_challenges-status)
of `undeliverable`.

## Testing

Stripe doesn’t send fraud challenge text messages to cardholders in test mode.
To help you integrate with fraud challenges, we provide helper APIs for
simulating a fraud challenge flow, including sending and responding to a
challenge.

[Challenge a high-risk test mode
authorization](https://docs.stripe.com/issuing/controls/fraud-challenges#high-risk-test)
Use helper APIs to [create a test mode
authorization](https://docs.stripe.com/api/issuing/authorizations/test_mode_create).
The risk level of the authorization you create is controllable: you can create a
high-risk authorization by overriding the default risk assessment with a high
fraud risk level.

```
curl https://api.stripe.com/v1/test_helpers/issuing/authorizations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=2300 \
 -d card={{CARD_ID}} \
 -d "risk_assessment[fraud_risk][risk_level]"=high \
 -d "risk_assessment[fraud_risk][fraud_score]"=95
```

This authorization would be declined, with a `reason` of `suspected_fraud` in
its
[request_history](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history).
If fraud challenges are turned on, then a fraud challenge is created for this
high-risk test mode authorization. See [Before you
begin](https://docs.stripe.com/issuing/controls/fraud-challenges#prerequisites)
for the steps required to turn on fraud challenges.

Alternatively, you can test fraud challenges by issuing a challenge yourself. To
induce a fraud challenge in test mode, create a test mode authorization without
a risk assessment override, and then respond to an
`issuing_authorization.request` webhook. This method doesn’t require fraud
challenges to be turned on in your Issuing settings. Learn how to [trigger fraud
challenges
yourself](https://docs.stripe.com/issuing/controls/fraud-challenges#define-your-own-logic)
in webhook responses.

[Simulate a response to the fraud
challenge](https://docs.stripe.com/issuing/controls/fraud-challenges#simulate-response)
After inducing a test mode fraud challenge, you can simulate a cardholder’s
response using another helper API. Call the [test mode fraud challenge
response](https://docs.stripe.com/api/issuing/authorization/respond) method,
passing the ID of the authorization you created in step 1, and a `confirmed`
parameter.

Provide `confirmed=true` to simulate the cardholder responding “yes, I made this
transaction, and it isn’t fraudulent.” Provide `confirmed=false` to simulate a
response of “no, I did not make this transaction, it is fraudulent.”

```
curl
https://api.stripe.com/v1/test_helpers/issuing/authorizations/{{AUTHORIZATION_ID}}/fraud_challenges/respond
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d confirmed=true
```

[Try the high-risk authorization
again](https://docs.stripe.com/issuing/controls/fraud-challenges#retry-authorization)
If you simulated a response of “yes, I made this transaction”
(`confirmed=true`), you can try the high-risk test mode authorization again.
This time, the authorization won’t be declined because you simulated a scenario
where the cardholder has indicated that the original, declined transaction is
actually legitimate.

```
curl https://api.stripe.com/v1/test_helpers/issuing/authorizations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=2300 \
 -d card={{CARD_ID}} \
 -d "risk_assessment[fraud_risk][risk_level]"=high \
 -d "risk_assessment[fraud_risk][fraud_score]"=95
```

This new authorization won’t be declined for `suspected_fraud`, and is approved.
It might also be declined for other reasons (such as an insufficient test mode
balance), look at the authorization’s
[request_history](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history)
to learn more.

Additionally, this new authorization’s
[verified_by_fraud_challenge](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-verified_by_fraud_challenge)
field will be `true`. This indicates that the cardholder has previously
completed a fraud challenge for a similar authorization (as simulated in step
2).

## Links

- [phone
numbers](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-phone_number)
- [card issuing
settings](https://dashboard.stripe.com/settings/issuing/authorizations)
-
[request_history.reason](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)
- [issuing.authorization_request
webhooks](https://docs.stripe.com/issuing/controls/real-time-authorizations)
- [Authorizations API](https://docs.stripe.com/api/issuing/authorizations)
-
[fraud_challenges](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-fraud_challenges)
-
[verified_by_fraud_challenge](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-verified_by_fraud_challenge)
- [Connect](https://docs.stripe.com/issuing/connect)
-
[status](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-fraud_challenges-status)
- [create a test mode
authorization](https://docs.stripe.com/api/issuing/authorizations/test_mode_create)
-
[request_history](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history)
- [test mode fraud challenge
response](https://docs.stripe.com/api/issuing/authorization/respond)