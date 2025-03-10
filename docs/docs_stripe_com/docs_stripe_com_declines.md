# Declines

## Learn about payment declines and how to lower your decline rate.

Payments can fail for a variety of reasons, including some that help prevent
fraudulent transactions. Stripe works to reduce decline rates across all
supported payment methods. We work with issuers and networks to improve
acceptance rates, often without affecting your integration.

There are three reasons why a payment might fail:

- [Issuer declines](https://docs.stripe.com/declines#issuer-declines)
- [Blocked payments](https://docs.stripe.com/declines#blocked-payments)
- [Invalid API calls](https://docs.stripe.com/declines#invalid-api-calls)

You need to handle each type of payment failure differently. For every failure,
you can use the [Dashboard](https://dashboard.stripe.com/payments) or API to
review a payment’s details. When using the API, look at the `Charge` object’s
[outcome](https://docs.stripe.com/api/charges/object#charge_object-outcome).
This attribute covers the payment failure type and provides information about
its cause.

Stripe handles non-card payment method declines similarly to card declines.
Stripe sends you a response code that includes information about the decline,
for example, if it’s due to insufficient funds, a lost or stolen card, or
another reason.

## Issuer declines

When your customer’s card issuer receives a charge, their automated systems and
models decide whether to authorize it. These tools analyze signals such as
spending habits, account balance, and card data (expiration date, address
information, and CVC).

If the card issuer declines a payment, Stripe shares with you all of the decline
information we receive. This information is available in the Dashboard and
through the API. When issuers provide specific explanations, such as an
incorrect card number or low funds, these explanations return to Stripe through
[decline codes](https://docs.stripe.com/declines/codes).

## Blocked payments

[Stripe Radar](https://docs.stripe.com/radar) blocks high risk payments, such as
those with mismatched CVC or postal code values. This automated fraud prevention
product evaluates each payment, without requiring any action from you.

![A payment that Radar
declined](https://b.stripecdn.com/docs-statics-srv/assets/payment-high-risk-allow-list.1dd70f2d0e26384f44e8eeeb59eaf533.png)

A payment that Radar declined

When Stripe blocks a payment, it obtains initial authorization from the card
issuer but refrains from charging the card. This precaution helps prevent
potential fraudulent payments that might lead to disputes.

For some card types, customers might see the card issuer’s authorization for the
payment amount on their statement. However, Stripe hasn’t charged this amount or
withdrawn funds. The card issuer typically removes this authorization from the
customer’s statement within a few days.

If a rule you configured blocks a payment you recognize as legitimate, you can
lift the block by locating the payment in the
[Dashboard](https://dashboard.stripe.com/payments) and clicking **Add to allow
list**. This action doesn’t retry the payment. Instead, it overrides all of your
other rules from blocking future payment attempts that match the list attribute.

#### Note

Don’t see the **Add to allow list** button on the payment details page? [Contact
Stripe](https://support.stripe.com/email) to add this feature to your Radar
account.

When using the API, the `outcome` of a blocked payment reflects the type of
payment failure and the reason for it, along with the evaluated risk level.

```
...
outcome: {
 network_decline_code: null,
 network_advice_code: null,
 network_status: "not_sent_to_network",
 reason: "highest_risk_level",
 advice_code: "do_not_try_again",
 risk_level: "highest",
 seller_message: "Stripe blocked this charge as too risky.",
 type: "blocked"
},
...
```

## Invalid API calls

In the API, you might see an invalid API call like the following:

```
curl https://api.stripe.com/v1/charges \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=2000 \
 -d currency=usd \
 -d source=tok_invalid \
 --data-urlencode description="Charge for jenny.rosen@example.com"
```

The invalid API call generates an error response that might look like this:

```
{
 "error": {
 "code": "invalid_number",
 "doc_url": "https://docs.stripe.com/error-codes#invalid-number",
 "message": "Your card number is incorrect.",
 "param": "card[number]",
 "type": "card_error"
 }
}
```

The [outcome](https://docs.stripe.com/api#charge_object-outcome) of a declined
payment includes the type of payment failure and the
[reason](https://docs.stripe.com/api#charge_object-outcome-reason), based on the
card issuer’s decline code. The reason might contain information other than the
issuer’s response code, for example, if a Radar rule evaluation blocked the
charge.

```
...
outcome: {
 network_decline_code: "54",
 network_advice_code: "01",
 network_status: "declined_by_network",
 reason: "expired_card",
 advice_code: "do_not_try_again",
 risk_level: "normal",
 seller_message: "The bank returned the decline code `expired_card`.",
 type: "issuer_declined"
},
...
```

As you develop your Stripe integration, continuously
[test](https://docs.stripe.com/testing) it to identify any potential bugs that
might lead to invalid API calls. Invalid API calls typically don’t result in a
payment appearing in your Dashboard. However, you might see the payment appear
in a few cases.

```
...
outcome: {
 network_decline_code: null,
 network_advice_code: null,
 network_status: "not_sent_to_network",
 type: "invalid"
},
...
```

## See also

- [Card declines](https://docs.stripe.com/declines/card)
- [Test declined
payments](https://docs.stripe.com/testing?testing-method=card-numbers#declined-payments)
- [Refund and cancel payments](https://docs.stripe.com/refunds)

## Links

- [Issuer declines](https://docs.stripe.com/declines#issuer-declines)
- [Blocked payments](https://docs.stripe.com/declines#blocked-payments)
- [Invalid API calls](https://docs.stripe.com/declines#invalid-api-calls)
- [Dashboard](https://dashboard.stripe.com/payments)
- [outcome](https://docs.stripe.com/api/charges/object#charge_object-outcome)
- [decline codes](https://docs.stripe.com/declines/codes)
- [Stripe Radar](https://docs.stripe.com/radar)
- [Contact Stripe](https://support.stripe.com/email)
-
[https://docs.stripe.com/error-codes#invalid-number](https://docs.stripe.com/error-codes#invalid-number)
- [outcome](https://docs.stripe.com/api#charge_object-outcome)
- [reason](https://docs.stripe.com/api#charge_object-outcome-reason)
- [test](https://docs.stripe.com/testing)
- [Card declines](https://docs.stripe.com/declines/card)
- [Test declined
payments](https://docs.stripe.com/testing?testing-method=card-numbers#declined-payments)
- [Refund and cancel payments](https://docs.stripe.com/refunds)