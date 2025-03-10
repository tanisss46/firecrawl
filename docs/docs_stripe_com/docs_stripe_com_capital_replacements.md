# ReplacementsPrivate preview

## Learn how to handle financing offer replacements.

#### Private preview

Financing offer replacements aren’t enabled by default. After updating your
integration to support replacements, you must [contact
us](mailto:capital-review@stripe.com) to enable them.

The Capital financing application provides connected account users the option of
linking third-party data to receive updated offer terms, such as a higher loan
amount. Financing offer replacements give a platform visibility into its users’
offer history.

Without replacements, when an account receives an offer with new terms, Stripe
updates the existing
[FinancingOffer](https://docs.stripe.com/api/capital/connect_financing_object).
The platform can’t access any record of previous offers.

With replacements enabled, Stripe instead creates a `FinancingOffer` object
representing the new offer. The platform can access both the existing and new
offers.

The following example illustrates how a user might receive a replacement offer:

- Stripe creates an undelivered financing offer for the user with a maximum loan
amount of $5,000.
- Your platform sends the user an offer email and marks the offer as delivered.
- The user navigates to the Capital financing application and links their bank
account.
- Stripe determines the user is eligible for a new maximum loan amount of
$10,000.
- Stripe replaces the user’s original $5,000 offer with a new $10,000 offer.

This guide covers how to handle offer replacements. It assumes you’ve completed
[the API set-up guide](https://docs.stripe.com/capital/api-integration).

[Create a delivered offer in test
mode](https://docs.stripe.com/capital/replacements#create-delivered-offer)
From the [Dashboard](https://dashboard.stripe.com/test/connect/capital), create
a new financing offer with status delivered in test mode.

[Replace the offer](https://docs.stripe.com/capital/replacements#replace-offer)
Click the overflow menu () next to the delivered offer, and select **Replace
offer**.

#### Note

**Replace offer** only appears for offers that have never been replaced before
and have status undelivered or delivered.

Click **Replace** at the bottom of the modal to replace the offer.

Stripe sends the `capital.financing_offer.replacement_created` webhook after a
replacement [financing
offer](https://docs.stripe.com/api/capital/connect_financing_object) is created.
The body of the webhook contains details about the replacement financing offer.

```
{
 "type": "capital.financing_offer.replacement_created",
 "data": {
 "object": {
 "id": "financingoffer_xyz456",
 "object": "capital.financing_offer",
 "account": "acct_efg678",
 "status": "delivered",
 "financing_type": "flex_loan",
 "offered_terms": {
 "currency": "usd",
 "advance_amount": 100000,
 "fee_amount": 10000,
 "withhold_rate": 0.15,
 },
 "replacement_for": "financingoffer_abc123",
 ...
 }
 }
}
```

Notice that the replacement offer has status delivered. When a user receives a
replacement offer, it becomes their current active offer.

Update your [webhook](https://docs.stripe.com/webhooks) integration to handle
the `capital.financing_offer.replacement_created` webhook. If your internal data
models store the user’s active financing offer ID, make sure you update the ID
to the user’s replacement offer.

[Retrieve the replaced
offer](https://docs.stripe.com/capital/replacements#retrieve-replaced-offer)
After replacing the offer, you’re redirected to a page with details about the
replacement offer. The events table contains an event **Account acct_egg678 has
a replacement financing offer for financingoffer_abc123**, providing a reference
to the user’s original offer ID.

[Retrieve](https://docs.stripe.com/api/capital/financing_offers/retrieve#retrieve_financing_offer)
`financingoffer_abc123`. Notice that it has status replaced, and the
`replacement` attribute has value `financingoffer_xyz456`, indicating that
`financingoffer_xyz456` replaced `financingoffer_abc123`.

```
{
 "id": "financingoffer_abc123",
 "object": "capital.financing_offer",
 "status": "replaced",
 "replacement": "financingoffer_xyz456",
 ...
}
```

Replaced is a terminal state. If the user accepts their replacement offer, all
future offer state transitions affect the replacement offer.

## Links

- [FinancingOffer](https://docs.stripe.com/api/capital/connect_financing_object)
- [the API set-up guide](https://docs.stripe.com/capital/api-integration)
- [Dashboard](https://dashboard.stripe.com/test/connect/capital)
- [webhook](https://docs.stripe.com/webhooks)
-
[Retrieve](https://docs.stripe.com/api/capital/financing_offers/retrieve#retrieve_financing_offer)