# RefillsPrivate preview

## Learn how to enable refills for your Capital program.

Refills are additional financing offers sent to customers who have made
substantial repayment progress towards their in-progress loans. If approved,
refill offers pay down the remaining balance on the in-progress loan.

This guide assumes you have completed [the API set-up
guide](https://docs.stripe.com/capital/api-integration).

#### Private preview

Refills aren’t enabled by default for [Capital
API](https://docs.stripe.com/api/capital/financing_offers) platforms. After
you’ve updated your integration to support refills, [contact
us](mailto:capital-review@stripe.com) to enable refill offers for your platform.

## Refill offer lifecycle

- Stripe evaluates active Capital users daily for refill financing eligibility,
just like standard financing offers.
- When a refill offer is created, you receive a
`capital.financing_offer.created` [webhook](https://docs.stripe.com/webhooks)
which contains `"product_type": "refill"` to indicate it’s a refill offer.
- Depending on the `product_type` and `offered_terms.campaign_type` fields, use
approved messaging to communicate the financing offer to the customer.
- The customer accesses the refill application with the same Account Link setup
from the [API set up
guide](https://docs.stripe.com/capital/api-integration#send-offer-email). The
customer can adjust a custom slider up to the max qualified offer amount.

!

Refill application

!

Refill application
- Customers who accept the refill offer are offered a discount, taken as a
percentage on the remaining premium of their existing loan. This discount rate
is exposed as `previous_financing_fee_discount_rate` under `offered_terms`.
- If the customer accepts the refill offer, we send a
`capital.financing_offer.accepted` [webhook](https://docs.stripe.com/webhooks).
The webhook payload contains an `accepted_terms` field containing the amounts
the customer selected. The field `previous_financing_fee_discount_amount` will
be `null` until the previous financing has been fully repaid and we’ve
determined the discount amount.

Example webhook:

```
{
 "type": "capital.financing_offer.accepted",
 "api_version": "2022-02-28",
 "created": 123456789,
 "data": {
 "object": {
 "id": "financingoffer_abcdef123456",
 "object": "capital.financing_offer",
 "account": "acct_abcdef123456",
 "created_at": 123456789,
 "expires_after": 123456789,
 "livemode": true,
 "status": "accepted",
 "accepted_terms": {
 "currency": "usd",
 "advance_amount": 100000,
 "fee_amount": 10000,
 "withhold_rate": 0.15,
 "previous_financing_fee_discount_amount": null
 },
 "financing_type": "flex_loan",
 "offered_terms": {
 "currency": "usd",
 "advance_amount": 100000,
 "fee_amount": 10000,
 "withhold_rate": 0.15,
 "campaign_type": "repeat_user",
 "previous_financing_fee_discount_rate": 0.5
 },
 "product_type": "refill"
 }
 }
}
```
- The new loan will first repay and close out the customer’s active loan. The
customer receives the difference. This new loan payout will send the
`capital.financing_offer.paid_out` webhook, at which point the
`previous_financing_fee_discount_amount` field will be set.
- [Retrieve the financing
summary](https://docs.stripe.com/api/capital/financing_summary) to see the
details of the customer’s `paid_out` financing.

Example response:

```
{
 "object": "capital.financing_summary",
 "details": {
 "currency": "usd",
 "advance_amount": 1000000,
 "fee_amount": 100000,
 "withhold_rate": 0.2,
 "remaining_amount": 0,
 "paid_amount": 0,
 "current_repayment_interval": {
 "due_at": 123456789,
 "remaining_amount": 50,
 "paid_amount": 50
 },
 "repayments_begin_at": 123456789,
 "advance_paid_out_at": 123456789
 }
 }
```
- Details about the refill and original financing are also available on the
financing reporting page.

!

Hosted reporting of original loan

!

Hosted reporting of newly refilled loan

## Links

- [the API set-up guide](https://docs.stripe.com/capital/api-integration)
- [Capital API](https://docs.stripe.com/api/capital/financing_offers)
- [webhook](https://docs.stripe.com/webhooks)
- [API set up
guide](https://docs.stripe.com/capital/api-integration#send-offer-email)
- [Retrieve the financing
summary](https://docs.stripe.com/api/capital/financing_summary)