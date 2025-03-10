# Issuing watchlist

## Learn about the Issuing watchlist process and best practices.

Stripe automatically screens Issuing users against US and international
sanctions lists. For Issuing, we screen all relevant data. Screening can occur
based on events such as:

- Onboarding
- Updates to sanction lists
- Creation or update of cardholders

If automated screening flags a user, Stripe opens a manual review for them. Our
team reviews any flagged cardholders, and updates information about these
cardholders within 24 hours. During the review, this process might impact your
business, and all cards decline authorizations with the
`cardholder_verification_required` reason.

## Integrating with watchlist events

Make sure your integration listens to the
[issuing_cardholder.updated](https://docs.stripe.com/api/events/types#event_types-issuing_cardholder.updated)
[webhook](https://docs.stripe.com/webhooks) events. This is how we notify you
when an interesting event occurs.

- When a user creates or updates a cardholder, Stripe updates the
[requirements.disabled_reason](https://docs.stripe.com/api/#issuing_cardholder_object-requirements-disabled_reason)
to `under_review`. This notifies the user that a screening is underway.

```
"requirements": {
 "disabled_reason": "under_review",
 "past_due": []
}
```
- In most cases, we clear the cardholder in a few seconds through our automated
review system.

```
"requirements": {
 "disabled_reason": null,
 "past_due": []
}
```
- If a cardholder might be on a prohibited persons or companies list, we update
the
[requirements.disabled_reason](https://docs.stripe.com/api/#issuing_cardholder_object-requirements-disabled_reason)
to `listed`. The `past_due` field contains information you need to provide
before the cardholder can approve authorizations.

```
"requirements": {
 "disabled_reason": "listed",
 "past_due": [
 "individual.dob.day",
 "individual.dob.month",
 "individual.dob.year"
 ]
}
```

In the Dashboard under [Issuing](https://dashboard.stripe.com/issuing/overview)
> [Cardholders](https://dashboard.stripe.com/issuing/cardholders), a banner
appears at the top of the page reflecting the information in the
[requirements.disabled_reason](https://docs.stripe.com/api/#issuing_cardholder_object-requirements-disabled_reason)
attribute noted above.

!

Stripe also sends an email notification to you to provide more information to
expedite the verification process. Its a good practice, to monitor the email
that you have on file with Stripe.

!
- Stripe might reject the Cardholder if the user is on a third-party prohibited
persons or companies list (such as a financial services provider or a government
entity). We update the
[requirements.disabled_reason](https://docs.stripe.com/api/#issuing_cardholder_object-requirements-disabled_reason)
to `rejected.listed`. Additionally, the
[status](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-status)
will be `blocked`.

```
"requirements": {
 "disabled_reason": "rejected.listed",
 "past_due": []
},
"status": "blocked",
"type": "individual"
```

## Best practices

- Provide the date of birth when creating cardholders. When our systems raise
reviews on Issuing Cardholders without a date of birth, analysts must contact
the Issuing platform or the cardholder to obtain this information.
- For Issuing cardholders, you can order an optional physical card. Be aware
that we only ship a physical card after completing the watchlist screening
process at onboarding and determining that it doesn’t hit the watchlist.

## See also

- [Issuing: Watchlist reviews
support](https://support.stripe.com/questions/issuing-watchlist-reviews)

## Links

-
[issuing_cardholder.updated](https://docs.stripe.com/api/events/types#event_types-issuing_cardholder.updated)
- [webhook](https://docs.stripe.com/webhooks)
-
[requirements.disabled_reason](https://docs.stripe.com/api/#issuing_cardholder_object-requirements-disabled_reason)
- [Issuing](https://dashboard.stripe.com/issuing/overview)
- [Cardholders](https://dashboard.stripe.com/issuing/cardholders)
-
[status](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-status)
- [Issuing: Watchlist reviews
support](https://support.stripe.com/questions/issuing-watchlist-reviews)