# Create virtual cards

## Create a cardholder and issue a virtual card.

You can use the [Dashboard](https://dashboard.stripe.com/issuing/cards) or the
[Create a card](https://docs.stripe.com/api/issuing/cards) endpoint to issue
virtual cards to cardholders. Cardholders can use virtual cards immediately
after you create them.

## Create a cardholder

You can use the [Dashboard](https://dashboard.stripe.com/issuing/cardholders) or
the [Cardholders API](https://docs.stripe.com/api/issuing/cardholders) to create
a cardholder.

DashboardAPI- Visit the **Cardholders** tab in the Issuing Dashboard.
- Click **Create cardholder**.
- Select cardholder type: individual or company. The full set of valid
characters for both cardholder name and business name are alphanumeric
characters and `/ -&:().'`. There’s a 24 character limit.
- Add a billing address.
- If you’re creating a company card, add the tax ID number.
- Add contact information, which is required for certain features like digital
wallets.
- Click **Create cardholder**.

### Individual type cardholder requirements

When you select the individual cardholder type, you must add the cardholder’s
legal first and last name. Consider providing the [date of
birth](https://docs.stripe.com/api/issuing/cardholders/create#create_issuing_cardholder-individual-dob),
which may help reduce [watchlist
reviews](https://support.stripe.com/questions/issuing-watchlist-reviews).

If you issue cards to individuals for programs backed by Cross River Bank, you
must record acceptance of the [Cross River Bank Authorized User
Terms](https://stripe.com/legal/issuing/crb-authorized-user-terms) before
[activating](https://docs.stripe.com/issuing/cards/physical/issue-cards?testing-method=without-code#activate-the-card)
a card for that cardholder. See the [Required Agreements for Issuing and
Treasury](https://docs.stripe.com/issuing/compliance-us) for more information
about which agreements you must present to account holders and cardholders.

### Company type cardholder requirements

When you add a company name, ensure that it has a minimum of two words, for
example: Stripe Inc.

## Create a card

You can use the [Dashboard](https://dashboard.stripe.com/issuing/cards) to
create a new card.

- Visit the **Cards** tab in the Issuing Dashboard.
- Click **Create card**.
- Search for the cardholder you created in [Create a
cardholder](https://docs.stripe.com/issuing/cards/virtual/issue-cards#create-cardholder).
- Select **Virtual** for the type.
- Select **Activate card**.
- Click **Create**.

## Activate the card

For [authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
to be approved on a card, its `status` must be set to `active`. Past-due
[requirements](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-requirements-past_due)
block card activation.

### Activate on creation

You can activate the card when creating it using the Dashboard or the API. In
the Dashboard, when creating a card, click **Activate card**. Using the API, set
`status` to `active` when using the [create
card](https://docs.stripe.com/api/#create_issuing_card) endpoint.

### Activate after creation

Alternatively, after creating an inactive card, you can activate it using the
Dashboard or the API. To activate it using the Dashboard, select the card you
want to activate, then click **Activate card**. To activate it using the API,
use the [update card](https://docs.stripe.com/api#update_issuing_card) endpoint
to set its `status` to `active`.

```
curl https://api.stripe.com/v1/issuing/cards/ic_1Cm3paIyNTgGDVfzBqq1uqxR \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d status=active
```

### Re-activate after blocking

In some cases, multiple incorrect PIN attempts on a transaction deactivates a
card, preventing further authorizations. To reactivate the card, use the
Dashboard or the [update card](https://docs.stripe.com/api#update_issuing_card)
API to set the card’s `status` to `active`.

## Links

- [Dashboard](https://dashboard.stripe.com/issuing/cards)
- [Create a card](https://docs.stripe.com/api/issuing/cards)
- [Dashboard](https://dashboard.stripe.com/issuing/cardholders)
- [Cardholders API](https://docs.stripe.com/api/issuing/cardholders)
- [date of
birth](https://docs.stripe.com/api/issuing/cardholders/create#create_issuing_cardholder-individual-dob)
- [watchlist
reviews](https://support.stripe.com/questions/issuing-watchlist-reviews)
- [Cross River Bank Authorized User
Terms](https://stripe.com/legal/issuing/crb-authorized-user-terms)
-
[activating](https://docs.stripe.com/issuing/cards/physical/issue-cards?testing-method=without-code#activate-the-card)
- [Required Agreements for Issuing and
Treasury](https://docs.stripe.com/issuing/compliance-us)
- [authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
-
[requirements](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-requirements-past_due)
- [create card](https://docs.stripe.com/api/#create_issuing_card)
- [update card](https://docs.stripe.com/api#update_issuing_card)