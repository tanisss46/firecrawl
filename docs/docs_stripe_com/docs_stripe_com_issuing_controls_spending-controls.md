# Issuing spending controls

## Learn how to use Issuing to set rules on cards and cardholders to control spending.

You can use spending controls to block [merchant
categories](https://docs.stripe.com/issuing/categories) (for example, bakeries),
[countries](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-country),
or [merchant
IDs](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-network_id),
and to set spending limits such as 100 USD per authorization or 3000 USD per
month. You can apply them to both
[Cards](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-spending_controls)
and
[Cardholders](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-spending_controls)
either by setting their `spending_controls` fields when you create them or by
updating them later.

The `spending_controls` object has the following structure:

Field TypeDescription`allowed_categories` arrayList of
[categories](https://docs.stripe.com/issuing/categories) of authorizations to
allow. All other categories will be blocked.`blocked_categories` arrayList of
[categories](https://docs.stripe.com/issuing/categories) of authorizations to
decline. All other categories will be allowed.`spending_limits` arrayList of
[objects](https://docs.stripe.com/issuing/controls/spending-controls#spending-limits)
that specify amount-based rules.`allowed_merchant_countries` arrayList of
merchant
[countries](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-country)
to allow authorizations from. Authorizations from all other countries are
blocked.`blocked_merchant_countries` arrayList of merchant
[countries](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-country)
to block authorizations from. Authorizations from all other countries are
allowed.
Spending controls run before [real-time
authorizations](https://docs.stripe.com/issuing/controls/real-time-authorizations)
and can decline a purchase before the `issuing_authorization.request` is sent,
resulting in a declined `issuing_authorization.created` event.

#### Note

Merchant ID spend controls are currently limited to beta users. You must be an
Issuing customer to join the beta. To request access to the beta, Contact Stripe
for more information.

## Spending limits

Spending limit rules limit the total amount of spending for categories over
intervals of time.

The `spending_limits` field within `spending_controls` is a list of objects that
have the following structure:

FieldTypeDescription`amount`integerMaximum spend, in the currency of the card.
Amounts in other currencies are converted to the card’s currency when evaluating
this control. This amount is in the card’s currency and in the [smallest
currency
unit](https://docs.stripe.com/currencies#zero-decimal).`interval`enumTime
interval that the amount applies to. See the [Card
spending_controls](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-spending_controls-spending_limits-interval)
for the possible values. All date-based intervals start at midnight
UTC.`categories`array (optional)List of
[categories](https://docs.stripe.com/issuing/categories) this limit applies to.
Omitting this field will apply the limit to all categories.
#### Note

If you don’t set `spending_limits`, a default spending limit is applied to the
newly created card in the amount of 500 USD per day. [Contact
Support](https://support.stripe.com/contact/login) to disable this behavior.

#### Note

In addition to the `spending_limits` configured on card, a default spending
limit in the amount of 10000 USD is also applied to each authorization. This
isn’t configurable. [Contact Support](https://support.stripe.com/contact/login)
to disable this behavior.

A card’s spending limits apply across any cards it replaces (that is, its
[replacement_for](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-replacement_for)
card and *that* card’s
[replacement_for](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-replacement_for)
card, up the chain). A cardholder’s spending limits apply across all of their
cards.

Each spending limit only applies to its own categories. Spending limits alone do
not block categories and should be used with either `allowed_categories` or
`blocked_categories` to restrict spending to specific business types.

If a cardholder has overlapping spending limits (for example, 100 USD per
authorization and 50 USD per authorization for their card), the most restrictive
spending control applies.

Additional tips and fees can be [posted at a later
time](https://docs.stripe.com/issuing/purchases/transactions?issuing-capture-type=over_capture),
causing a spending limit to be exceeded.

## Examples

The following examples demonstrate different uses of spending controls for cards
and cardholders.

APIDashboard
### Limit a cardholder's monthly spend across all of their cards

### Limit the spend and allowed categories for a cardholder

### Limit a cardholder's weekly spend for specific categories

## Links

- [merchant categories](https://docs.stripe.com/issuing/categories)
-
[countries](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-country)
- [merchant
IDs](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-network_id)
-
[Cards](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-spending_controls)
-
[Cardholders](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-spending_controls)
-
[objects](https://docs.stripe.com/issuing/controls/spending-controls#spending-limits)
- [real-time
authorizations](https://docs.stripe.com/issuing/controls/real-time-authorizations)
- [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal)
- [Card
spending_controls](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-spending_controls-spending_limits-interval)
- [Contact Support](https://support.stripe.com/contact/login)
-
[replacement_for](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-replacement_for)
- [posted at a later
time](https://docs.stripe.com/issuing/purchases/transactions?issuing-capture-type=over_capture)