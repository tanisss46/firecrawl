# Connected accounts, cardholders, and cards

## Learn how to create and manage cardholders and cards with Stripe Connect.

Connected accounts represent business entities. Cardholders represent
individuals associated with those business entities. One connected account can
have multiple cardholders. For example, a connected account for a small business
might have multiple cardholders for the owner and its employees. After you
create a cardholder, you issue them a virtual or physical card.

PlatformConnected account
Cardholder

Card

Card

Card

Connected account cardholders and cards
## Create cardholders

To create a
[Cardholder](https://docs.stripe.com/api/issuing/cardholders/object), use the
[Cardholders API](https://docs.stripe.com/api/issuing/cardholders/create) and
provide the required information. Using [digital
wallets](https://docs.stripe.com/issuing/cards/digital-wallets) requires a valid
phone number and email address, but they’re optional for physical cards.

#### Note

As a Connect platform, you make API calls on behalf of your connected accounts
by including a `Stripe-Account` header and the connected account’s account ID.

FieldParameterDescriptionBilling information`billing`Cardholder’s billing
address (typically the primary business address)Type`type`Whether the cardholder
is a ‘company’ or ‘individual’. See [Choose a cardholder
type](https://docs.stripe.com/issuing/other/choose-cardholder) for
guidance.Phone number`phone_number`Required if using digital
walletsEmail`email`Email address of the cardholder. Required if using digital
wallets
```
curl https://api.stripe.com/v1/issuing/cardholders \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d name="Jenny Rosen" \
 --data-urlencode email="jenny.rosen@example.com" \
 --data-urlencode phone_number="+18008675309" \
 -d status=active \
 -d type=individual \
 -d "individual[first_name]"=Jenny \
 -d "individual[last_name]"=Rosen \
 -d "individual[dob][day]"=1 \
 -d "individual[dob][month]"=11 \
 -d "individual[dob][year]"=1981 \
 -d "billing[address][line1]"="510 Townsend Street" \
 -d "billing[address][city]"="San Francsico" \
 -d "billing[address][state]"=CA \
 -d "billing[address][postal_code]"=94111 \
 -d "billing[address][country]"=US
```

Stripe returns a Cardholder object that contains the information you provided
and sends the `issuing_cardholder.created`
[webhook](https://docs.stripe.com/webhooks) event.

Stripe must screen cardholder identity information in accordance with legal and
regulatory guidelines. This can block authorizations based on cardholder
attributes. Learn more about [watchlist
reviews](https://support.stripe.com/questions/issuing-watchlist-reviews).

After you create a `Cardholder`, call the [Cardholder
update](https://docs.stripe.com/api/issuing/cardholders/update) endpoint with
the parameters that you need to change. A successful call returns an updated
`Cardholder` object.

Cardholders have a default `active`
[status](https://docs.stripe.com/api/issuing/cardholders/update#update_issuing_cardholder-status),
which means that any cards attached to the cardholder can approve
authorizations. You can change the `status` to `inactive` by updating the
cardholder. An inactive status on a Cardholder means all authorizations will be
declined for any attached cards with a reason of `cardholder_inactive`.

## Create cards

After you create a `Cardholder`, issue them a card with the [Cards
API](https://docs.stripe.com/api/issuing/cards/create).

A [Card](https://docs.stripe.com/api/issuing/cards/object) object represents a
[physical card](https://docs.stripe.com/issuing/cards/physical) or [virtual
card](https://docs.stripe.com/issuing/cards/virtual). Creating a physical card
requires a shipping address, and you can provide [additional
arguments](https://docs.stripe.com/issuing/cards/physical) to specify shipment
packaging and delivery service.

Cardholder`cardholder`Cardholder’s IDCurrency`currency`Three-letter ISO currency
code, in lowercase. Supported currencies are `usd` in the US, `gbp` in the UK,
and `eur` in euro area counties.Type`type`Can be `physical` or `virtual`
The following call is an example of issuing a virtual card attached to the
specified Cardholder:

```
curl https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d cardholder=ich_1234 \
 -d currency=usd \
 -d type=virtual
```

Stripe returns a `Card` object upon creation and sends the
`issuing_card.created` [webhook](https://docs.stripe.com/webhooks) event.

## Activate cards

Cards must be activated before
[authorizations](https://docs.stripe.com/issuing/purchases/authorizations) are
approved.

If you don’t specify a status when you create the card, the card has the default
status of `inactive`. A card remains `inactive` until the status is changed with
the [Card update](https://docs.stripe.com/api/issuing/cards/update) endpoint.

To activate a card:

```
curl https://api.stripe.com/v1/issuing/cards/{{CARD_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d status=active
```

## Deactivating cards

You can deactivate cards by setting the `status` to `inactive` with [Card
update](https://docs.stripe.com/api/issuing/cards/update) endpoint. This means
you can’t approve any *new* authorizations for the card. You can still approve
authorizations that were opened on the card before the status was set to
`inactive`. To approve any new authorizations, you need to change the status of
the card to `active`.

```
curl https://api.stripe.com/v1/issuing/cards/{{CARD_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d status=inactive
```

Learn more about [Managing
authorizations](https://docs.stripe.com/issuing/purchases/authorizations).

## Cancel cards

You can cancel a card by changing the status to `canceled` with the [Card
update](https://docs.stripe.com/api/issuing/cards/update) endpoint. The canceled
status is terminal and you can’t revert it. You can’t approve new authorizations
for a card with a `canceled` status. You can still approve authorizations that
were opened on the card before the status was set to `canceled`.

```
curl https://api.stripe.com/v1/issuing/cards/{{CARD_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d status=canceled
```

### Listing Cardholders

Find cardholders associated with a connected account by making a [Cardholders
API](https://docs.stripe.com/api/issuing/cards/list) GET request and passing the
specific `Stripe-Account` into the header.

```
curl https://api.stripe.com/v1/issuing/cardholders \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

If successful, the response contains a list of cardholders:

```
{
 "object": "list",
 "data": [
 {
 "id": "ich_1234a",
 "object": "issuing.cardholder",
 "billing": {
 "address": {
 "city": "San Francisco",
 "country": "US",
 "line1": "510 Townsend Street",
 "line2": null,
 "postal_code": "94111",
 "state": "CA"
 }
 },
 "company": null,
 "created": 1657144326,
 "email": "jenny.rosen@example.com",
 "individual": null,
 "livemode": false,
 "metadata": {},
 "name": "Jenny Rosen",
 "phone_number": "+18008675309",
 "requirements": {
 "disabled_reason": null,
 "past_due": []
 },
 "spending_controls": {
 "allowed_categories": [],
 "blocked_categories": [],
 "spending_limits": [],
 "spending_limits_currency": null
 },
 "status": "active",
 "type": "individual"
 },
 {
 "id": "ich_1234b",
 "object": "issuing.cardholder",
 "billing": {
 "address": {
 "city": "San Francisco",
 "country": "US",
 "line1": "510 Townsend Street",
 "line2": null,
 "postal_code": "94111",
 "state": "CA"
 }
 },
 "company": null,
 "created": 1656537695,
 "email": "jenny.rosen@example.com",
 "individual": null,
 "livemode": false,
 "metadata": {},
 "name": "Jenny Rosen",
 "phone_number": "+18008675309",
 "requirements": {
 "disabled_reason": null,
 "past_due": []
 },
 "spending_controls": {
 "allowed_categories": [],
 "blocked_categories": [],
 "spending_limits": [],
 "spending_limits_currency": null
 },
 "status": "active",
 "type": "individual"
 }
 ],
 "has_more": false,
 "url": "/v1/issuing/cardholders"
}
```

## Listing cards

You can also see a list of cards created on a connected account by making a
[Cards API](https://docs.stripe.com/api/issuing/cards/list) GET request and
passing the specific `Stripe-Account` into the header.

```
curl https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

If successful, you receive a list of cards:

```
{
 "object": "list",
 "data": [
 {
 "id": "ic_1234a",
 "object": "issuing.card",
 "brand": "Visa",
 "cancellation_reason": null,
 "cardholder": {
 "id": "ich_1234a",
 "object": "issuing.cardholder",
 "billing": {
 "address": {
 "city": "San Francisco",
 "country": "US",
 "line1": "510 Townsend Street",
 "line2": null,
 "postal_code": "94111",
 "state": "CA"
 }
 },
 "company": null,
 "created": 1656537695,
 "email": "jenny.rosen@example.com",
 "individual": null,
 "livemode": false,
 "metadata": {},
 "name": "Jenny Rosen",
 "phone_number": "+18008675309",
 "requirements": {
 "disabled_reason": null,
 "past_due": []
 },
 "spending_controls": {
 "allowed_categories": [],
 "blocked_categories": [],
 "spending_limits": [],
 "spending_limits_currency": null
 },
 "status": "active",
 "type": "individual"
 },
 "created": 1656537950,
 "currency": "usd",
 "exp_month": 5,
 "exp_year": 2025,
 "last4": "0021",
 "livemode": false,
 "metadata": {},
 "pin": null,
 "replaced_by": null,
 "replacement_for": null,
 "replacement_reason": null,
 "shipping": null,
 "spending_controls": {
 "allowed_categories": [
 "car_rental_agencies"
 ],
 "blocked_categories": null,
 "spending_limits": [
 {
 "amount": 8000,
 "categories": [],
 "interval": "per_authorization"
 }
 ],
 "spending_limits_currency": "usd"
 },
 "status": "active",
 "type": "virtual",
 "wallets": {
 "apple_pay": {
 "eligible": true,
 "ineligible_reason": null
 },
 "google_pay": {
 "eligible": true,
 "ineligible_reason": null
 },
 "primary_account_identifier": null
 }
 },
 {
 "id": "ic_1234b",
 "object": "issuing.card",
 "brand": "Visa",
 "cancellation_reason": null,
 "cardholder": {
 "id": "ich_1234a",
 "object": "issuing.cardholder",
 "billing": {
 "address": {
 "city": "San Francisco",
 "country": "US",
 "line1": "510 Townsend Street",
 "line2": null,
 "postal_code": "94111",
 "state": "CA"
 }
 },
 "company": null,
 "created": 1656537695,
 "email": "jenny.rosen@example.com",
 "individual": null,
 "livemode": false,
 "metadata": {},
 "name": "Jenny Rosen",
 "phone_number": "+18008675309",
 "requirements": {
 "disabled_reason": null,
 "past_due": []
 },
 "spending_controls": {
 "allowed_categories": [],
 "blocked_categories": [],
 "spending_limits": [],
 "spending_limits_currency": null
 },
 "status": "active",
 "type": "individual"
 },
 "created": 1656537947,
 "currency": "usd",
 "exp_month": 5,
 "exp_year": 2025,
 "last4": "0013",
 "livemode": false,
 "metadata": {},
 "pin": null,
 "replaced_by": null,
 "replacement_for": null,
 "replacement_reason": null,
 "shipping": null,
 "spending_controls": {
 "allowed_categories": null,
 "blocked_categories": null,
 "spending_limits": [
 {
 "amount": 50000,
 "categories": [],
 "interval": "daily"
 }
 ],
 "spending_limits_currency": "usd"
 },
 "status": "active",
 "type": "virtual",
 "wallets": {
 "apple_pay": {
 "eligible": true,
 "ineligible_reason": null
 },
 "google_pay": {
 "eligible": true,
 "ineligible_reason": null
 },
 "primary_account_identifier": null
 }
 }
 ],
 "has_more": false,
 "url": "/v1/issuing/cards"
}
```

You can see a list of cards associated with a specific cardholder by including
the `cardholder` parameter on your [Cards
API](https://docs.stripe.com/api/issuing/cards/list) GET request. Pass the
specific `Stripe-Account` into the header and the cardholder ID into the
`cardholder` parameter.

```
curl -G https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d cardholder=ich_1234a
```

## Links

- [Cardholder](https://docs.stripe.com/api/issuing/cardholders/object)
- [Cardholders API](https://docs.stripe.com/api/issuing/cardholders/create)
- [digital wallets](https://docs.stripe.com/issuing/cards/digital-wallets)
- [Choose a cardholder
type](https://docs.stripe.com/issuing/other/choose-cardholder)
- [webhook](https://docs.stripe.com/webhooks)
- [watchlist
reviews](https://support.stripe.com/questions/issuing-watchlist-reviews)
- [Cardholder update](https://docs.stripe.com/api/issuing/cardholders/update)
-
[status](https://docs.stripe.com/api/issuing/cardholders/update#update_issuing_cardholder-status)
- [Cards API](https://docs.stripe.com/api/issuing/cards/create)
- [Card](https://docs.stripe.com/api/issuing/cards/object)
- [physical card](https://docs.stripe.com/issuing/cards/physical)
- [virtual card](https://docs.stripe.com/issuing/cards/virtual)
- [authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
- [Card update](https://docs.stripe.com/api/issuing/cards/update)
- [Cardholders API](https://docs.stripe.com/api/issuing/cards/list)