# Risk evaluation

## Access the Stripe Radar risk evaluations in the Dashboard and the API.

At the core of Stripe Radar is an adaptive machine learning system that
evaluates the risk level for each payment in real time. It uses hundreds of
signals about each payment, and taps into data across our network of millions of
businesses, to predict whether a payment is likely to be fraudulent.

Our [machine learning system](https://stripe.com/radar/guide) is flexible and
responsive, continuously learns from new customer purchase patterns and
transaction features, and incorporates feedback from you whenever payments are
indicated as fraudulent.

#### Note

When a business using Stripe sees a card for the first time, there’s a 91%
chance that we’ve seen the card elsewhere on the Stripe network in the past.

## When to use Radar

Radar evaluates risk and runs rules for three different types of Stripe API
objects: [Charges](https://docs.stripe.com/api/charges),
[PaymentIntents](https://docs.stripe.com/api/payment_intents) and
[SetupIntents](https://docs.stripe.com/api/setup_intents). Stripe designed the
Radar rules to take four different actions:

- Request 3DS authentication
- Allow the creation of the object
- Block the creation of the object
- Review the creation of a Charge

The following table illustrates which rules Radar runs for each type of API
object:

Transaction typeRequest 3DS Allow & Block Review Charge✔ ✔ PaymentIntent✔ ✔ ✔
SetupIntent✔ ✔
You can enable Radar for SetupIntents in your [Radar
settings](https://dashboard.stripe.com/test/radar/settings).

## Risk outcomes

The Stripe machine learning models evaluate the likelihood that a payment is
fraudulent. This judgment can take one of five values:

- [High risk](https://docs.stripe.com/radar/risk-evaluation#high-risk)
- [Elevated risk](https://docs.stripe.com/radar/risk-evaluation#elevated-risk)
- [Normal risk](https://docs.stripe.com/radar/risk-evaluation#normal-risk)
- [Not evaluated](https://docs.stripe.com/radar/risk-evaluation#not-evaluated)
- [Unknown risk](https://docs.stripe.com/radar/risk-evaluation#unknown-risk)

Each payment includes information on the *outcome* of our risk evaluation.

Radar for fraud teams users will see a [risk
insights](https://docs.stripe.com/radar/reviews/risk-insights) section on the
payment page that provides more details about why we assigned a payment a
particular risk level and score.

If a card issuer [declines](https://docs.stripe.com/declines) a payment, Stripe
also includes any information we receive from them as part of the outcome.

The outcome for each payment is available when viewing a payment in the
[Dashboard](https://dashboard.stripe.com/) or through the API as part of the
[Outcome](https://docs.stripe.com/api#charge_object-outcome) attribute of the
[Charge](https://docs.stripe.com/api#charge_object) object.

### High risk payments

Stripe reports payments as high risk when we believe they’re likely to be
fraudulent. Payments of this risk level are
[blocked](https://docs.stripe.com/radar/rules#built-in-rules) by default.

On the `Charge` object of a high risk payment, the `risk_level` is set to
`highest`.

```
...
"outcome":
{
 "network_status": "not_sent_to_network",
 "reason": "highest_risk_level",
 "risk_level": "highest",
 "risk_score": 92, // Provided only with Stripe Radar for Fraud Teams
 "seller_message": "Stripe blocked this charge as too risky.",
 "type": "blocked",
}
...
```

If Stripe Radar ever blocks a payment that you know is legitimate, you can
remove the block using the Dashboard. To do this, view the payment in the
Dashboard and click **Add to allow list**. Adding a payment to the allow list
doesn’t retry the payment, but it does prevent Stripe Radar from blocking future
payment attempts with that card or email address.

#### Note

Don’t see **Add to allow list**? [Contact
Stripe](https://support.stripe.com/email) to have this feature added to your
Radar account.

### Elevated risk payments

Elevated risk payments have an increased chance of being fraudulent. Stripe
Radar allows payments of this risk level by default. Stripe Radar for Fraud
Teams automatically places elevated risk payments into your
[review](https://docs.stripe.com/radar/reviews) queue so you can take a closer
look.

On the `Charge` object of an elevated risk payment, the `risk_level` is set to
`elevated`.

```
...
"outcome": {
 "network_status": "approved_by_network",
 "reason": "elevated_risk_level",
 "risk_level": "elevated",
 "risk_score": 56, // Provided only with Stripe Radar for Fraud Teams
"seller_message": "Stripe evaluated this charge as having elevated risk, and
placed it in your manual review queue.",
 "type": "manual_review"
}
...
```

### Normal risk payments

Payments with a normal risk evaluation have fewer characteristics that are
strongly indicative of fraud than payments with elevated or high risk levels.
However, we recommend that you continue to be vigilant when fulfilling these
orders. Payments that have normal risk can still turn out to be fraudulent and
there are other possible [types of
fraud](https://docs.stripe.com/disputes/prevention/identifying-fraud) that can
occur later on in the order process.

On the `Charge` object of a successful payment with normal risk, the
`risk_level` is set to `normal`.

```
...
"outcome":
{
 "network_status": "approved_by_network",
 "reason": null,
 "seller_message": "The charge was authorized.",
 "risk_level": "normal",
 "risk_score": 23, // Provided only with Stripe Radar for Fraud Teams
 "type": "authorized",
}
...
```

### Not evaluated

The Risk level is set to `not_assessed` for non-card payments, card-based
payments predating the public assignment of risk levels, and for payments where
the merchant opts out of Radar fraud risk assessment.

On the `Charge` object of an unevaluated payment, the `risk_level` is set to
`not_assessed`.

```
...
"outcome": {
 "network_status": "approved_by_network",
 "reason": "not_assessed_risk_level",
 "risk_level": "not_assessed",
"seller_message": "Your business has opted out of Radar fraud risk
assessments.",
 "type": "authorized"
}
...
```

### Unknown risk payments

In unusual cases, an error might cause risk evaluation to fail. In this case,
Stripe reports the payment as having unknown risk.

On the `Charge` object of an unknown risk payment, the `risk_level` is set to
`unknown`.

```
...
"outcome": {
 "network_status": "approved_by_network",
 "reason": "unknown_risk_level",
 "risk_level": "unknown",
"seller_message": "Something went wrong while evaluating this payment. Our
engineers have been notified and we’ll look into this as soon as possible.",
 "type": "authorized"
}
...
```

## Searching for a specific risk level in the Dashboard

You can search for payments of a specific risk level using the **risk_level**
search term and the desired risk level. For example, a search for
[risk_level:highest](https://dashboard.stripe.com/test/search?query=risk_level%3Ahighest)
returns a list of all payments with a high risk level. Likewise, a search for
[risk_level:elevated](https://dashboard.stripe.com/test/search?query=risk_level%3Aelevated)
returns a list of all payments with an elevated risk level.

## Feedback on risk evaluations

While we use information across our network to evaluate a payment, you might
have additional information about a payment as a result of a customer
interaction. The Stripe machine learning models respond to feedback you share
with us, and you can help improve our fraud detection algorithms by
[refunding](https://docs.stripe.com/refunds) and reporting payments that you
believe are fraudulent.

Refunding fraudulent payments helps improve our fraud detection algorithms and
the accuracy of our risk evaluations for this payment, and similar ones in the
future.

To refund a payment and mark it as fraudulent, view the payment in the Dashboard
and then:

- Click **Refund**.
- Select **Fraudulent** as the **Reason**.
- Provide a brief explanation.

You can also indicate that a payment is fraudulent when you [create a
refund](https://docs.stripe.com/api#create_refund) using the API by providing
`fraudulent` as the value for `reason`. This adds the email address and card
fingerprint associated with the payment to the default email address and card
fingerprint [block lists](https://docs.stripe.com/radar/lists#default-lists).

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

# If you haven't refunded the charge, you can do so and let Stripe
# know it was fraudulent in one step.
Stripe::Refund.create({
 charge: '{{CHARGE_ID}}',
 reason: 'fraudulent',
})

# If you already refunded the charge (without specifying the
# 'fraudulent' reason), you can still let us know it was fraudulent.
Stripe::Charge.update(
 '{{CHARGE_ID}}',
 {
 fraud_details: {
 user_report: 'fraudulent',
 },
 }
)
```

For a small subset of charges, Stripe modifies the reported risk score so we can
measure the performance of our models and obtain data for subsequent model
development. This allows Stripe to ensure key metrics like false positive rate
and recall remain within desirable ranges, and that model performance continues
to improve.

If you don’t want the protection of the Stripe Radar machine learning models,
you can opt out by [contacting](https://stripe.com/contact) our Support team.

## Links

- [ultimately
responsible](https://stripe.com/us/legal#processing-transactions-disputes)
- [machine learning system](https://stripe.com/radar/guide)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Charges](https://docs.stripe.com/api/charges)
- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
- [SetupIntents](https://docs.stripe.com/api/setup_intents)
- [Radar settings](https://dashboard.stripe.com/test/radar/settings)
- [Risk Settings](https://docs.stripe.com/radar/risk-settings)
- [risk insights](https://docs.stripe.com/radar/reviews/risk-insights)
- [declines](https://docs.stripe.com/declines)
- [Dashboard](https://dashboard.stripe.com/)
- [Outcome](https://docs.stripe.com/api#charge_object-outcome)
- [Charge](https://docs.stripe.com/api#charge_object)
- [blocked](https://docs.stripe.com/radar/rules#built-in-rules)
- [Contact Stripe](https://support.stripe.com/email)
- [review](https://docs.stripe.com/radar/reviews)
- [types of
fraud](https://docs.stripe.com/disputes/prevention/identifying-fraud)
-
[risk_level:highest](https://dashboard.stripe.com/test/search?query=risk_level%3Ahighest)
-
[risk_level:elevated](https://dashboard.stripe.com/test/search?query=risk_level%3Aelevated)
- [refunding](https://docs.stripe.com/refunds)
- [create a refund](https://docs.stripe.com/api#create_refund)
- [block lists](https://docs.stripe.com/radar/lists#default-lists)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [contacting](https://stripe.com/contact)