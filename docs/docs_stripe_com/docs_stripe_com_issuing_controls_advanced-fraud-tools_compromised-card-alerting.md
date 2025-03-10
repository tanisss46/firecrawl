# Compromised card alertingDeprecated

## Cancel and reissue a card, file disputes, or notify a cardholder based on Stripe notifications.

Canceling a card suspected to be compromised can help you prevent future
fraudulent use of PANs that have been compromised. You can use these indicators
to initiate communications and a reissuance workflow for cardholders. If Stripe
observes that a card has been successfully used in a card testing attack, we
flag the card as compromised.

## Mitigate risk and take action

When Stripe observes a successful authorization during a severe card testing
attack (defined as a `risk_assessment.card_testing_risk.risk_level` of
`elevated` or `highest`), the card’s `fraud_warning.type` field will have a
value of `card_testing_exposure`. The `started_at` value corresponds to the date
that the successful authorization in card testing attack took place. This value
won’t update if the card is compromised again in a later attack.

After Stripe sets the `type` field to `card_testing_exposure`, we recommend
contacting the cardholder, canceling the card, and issuing a new one. This
mitigates the risk of subsequent authorizations on what a fraudulent actor
likely assumes is a valid PAN that they can use.

Learn more about [compromised card
alerting](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-fraud_warning)

Compromised card alerting is currently limited to beta users. You must be an
Issuing customer to join the beta. To request access to the beta, log in to your
Stripe account and refresh the page. [Contact
Stripe](https://stripe.com/contact/sales) for more information.

## Links

- [compromised card
alerting](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-fraud_warning)
- [Contact Stripe](https://stripe.com/contact/sales)