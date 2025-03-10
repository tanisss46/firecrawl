# Bulk issuance

## Ship cards in bulk to one location.

Stripe supports bulk issuance, allowing you to order a large number of physical
cards and have them shipped to a single destination.

Before you place a bulk shipment, you must verify PCI compliance throughout the
supply chain. The recipient of a bulk issuance must meet all applicable PCI
certification requirements. For certain specific issuing use cases, Stripe can
grant an exception that allows your business to receive its own bulk shipments.
Check with your account team to confirm the recipient adheres to the appropriate
PCI standards necessary for card possession.

## Bulk card issuance

Stripe groups all cards with the same shipping destination that are placed on
the same day into one bulk shipment.

- There’s no limit to the quantity of cards.
- If the quantity exceeds a few thousand, the shipment is split across multiple
boxes.
- There is a maximum of 2,000 cards per box.
- Each box has its own tracking number.
- The bulk cost reflected in the [pricing
table](https://docs.stripe.com/issuing/cards/physical/ship-cards#select-service-type)
is per box.

Select bulk issuance for a card:

- **Create a bulk-issued card:** Set the
[shipping.type](https://docs.stripe.com/api/issuing/cards/create#create_issuing_card-shipping-type)
property to `bulk` in [Create
card](https://docs.stripe.com/api/issuing/cards/create) call.
- **Track bulk shipments:** Upon shipment of each box, Stripe updates the
tracking number on the corresponding [Card
object](https://docs.stripe.com/api/issuing/cards/object). You can listen for
the
[issuing_card.updated](https://docs.stripe.com/api/events/types#event_types-issuing_card.updated)
webhook to receive notifications when the tracking numbers are assigned.

## Links

- [pricing
table](https://docs.stripe.com/issuing/cards/physical/ship-cards#select-service-type)
-
[shipping.type](https://docs.stripe.com/api/issuing/cards/create#create_issuing_card-shipping-type)
- [Create card](https://docs.stripe.com/api/issuing/cards/create)
- [Card object](https://docs.stripe.com/api/issuing/cards/object)
-
[issuing_card.updated](https://docs.stripe.com/api/events/types#event_types-issuing_card.updated)