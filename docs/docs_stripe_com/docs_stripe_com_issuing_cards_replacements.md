# Replacement cards

## Learn how to replace cards that are expired, damaged, lost, or stolen.

You can replace cards that are expired, damaged, lost, or stolen. The process
differs slightly for each kind of card replacement.

- **Card expired**: The card has reached its expiration date and is no longer
valid.
- **Card damaged**: The cardholder requests a new card for a reason other than
lost or stolen (for example, a physical card’s chip no longer reads properly).
- **Card lost/stolen**: The card is reported lost or stolen and a new card
number, expiry, security code are issued.

Depending on the scenario, the replacement card might have a different card
number, expiry, or security code from the original:

ScenarioNew card numberNew security codeNew expiryCard expiredNoYesYesCard
damagedNoYesYesCard lost/stolenYesYesYes
## Replacements for expired or damaged cards

Physical cards can get damaged, and both physical cards and virtual cards
expire, but you can create replacement cards that have the same card number. The
cardholder can continue to use the original card before the replacement card is
activated, as long as the card isn’t too damaged or already expired. Activating
the replacement card cancels the original card if it isn’t already canceled.

To create a replacement card for an expired or damaged card, create a
[Card](https://docs.stripe.com/api#issuing_card_object) with `replacement_for`
using the expired or damaged `Card` ID and `replacement_reason` set to `expired`
or `damaged`.

```
curl https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d cardholder=ich_1Cm3pZIyNTgGDVfzI83rasFP \
 -d currency=usd \
 -d type=virtual \
 -d replacement_for=ic_1LL8wgLUVt6Jcs5dgLLfwcAE \
 -d replacement_reason=expired
```

## Replacements for lost or stolen cards

Lost or stolen cards get new card numbers for security reasons. We need to
cancel the original cards before we can create the replacement card.

To create a replacement card for a lost or stolen card:

- Cancel the lost or stolen card by using the [update
card](https://docs.stripe.com/api#update_issuing_card) endpoint to set its
`status` to `canceled` and its `cancellation_reason` to `lost` or `stolen`.
- Create a [Card](https://docs.stripe.com/api#issuing_card_object) with
`replacement_for` using the lost or stolen `Card` ID and `replacement_reason`
set to `lost` or `stolen`.

```
curl https://api.stripe.com/v1/issuing/cards/ic_1CoYuRKEl2ztzE5GIEDjQiUI \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d status=canceled \
 -d cancellation_reason=lost
```

```
curl https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d cardholder=ich_1Cm3pZIyNTgGDVfzI83rasFP \
 -d currency=usd \
 -d type=virtual \
 -d replacement_for=ic_1CoYuRKEl2ztzE5GIEDjQiUI \
 -d replacement_reason=lost
```

## All replacements

All replacement cards have renewed expiration dates and new security codes.
Authorizations made on the original cards are migrated to the replacements, but
might still clear on the original cards. Like the originals, replacement cards
must be activated before use.

## Card-on-file updating

For many of our card programs, Stripe automatically updates the card details on
file with acquiring merchants, even when a card is completely reissued. This
feature offers several benefits, including saving your cardholders the hassle of
manually re-entering card details when their cards expire.

### Card expired or damaged

Updating the payment details for a card that has been replaced due to expiration
or damage ensures that recurring payments and stored payment details continue to
function. This enables cardholders to continue making payments when they replace
a card.

### Card lost or stolen

Stripe doesn’t update businesses with the new card number, expiry, and security
code of a replacement card if the old card is marked as being lost or stolen.

## Links

- [Card](https://docs.stripe.com/api#issuing_card_object)
- [update card](https://docs.stripe.com/api#update_issuing_card)