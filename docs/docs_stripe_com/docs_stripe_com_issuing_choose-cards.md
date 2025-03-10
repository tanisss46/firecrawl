# Choose which type of card to issue

## Decide on physical or virtual cards for your cardholders.

Stripe offers several options for the types of cards that can be issued to
cardholders. This page describes these options at a high level, including
tradeoffs and use cases for each.

You can issue multiple card types simultaneously for your card program and can
also transition to different options as your business needs change. For example,
if you wanted to create a custom card, you could issue an instant physical card
while you’re working with the Stripe team to manufacture your custom design. The
following options aren’t mutually exclusive.

Virtual cardsPhysical cardsOverviewCards with no physical representation, but
which include all the card information required for digital transactions. [Read
more about virtual cards](https://docs.stripe.com/issuing/cards/virtual).Cards
that can be physically personalized and shipped to cardholders. [Read more about
physical cards](https://docs.stripe.com/issuing/cards/physical).Best forVirtual
cards are best for use cases where card transactions are expected to be
completely digitized, or if you plan to use your card to complete a backend
process, such as fulfilling a customer’s order with a third party. Examples of
use cases that would benefit from virtual cards would be B2B payments (a
business is paying a supplier for a good or service) or buy now, pay later
payments (a business is paying a merchant).Physical cards are best when you
expect to support a high degree of in-person point-of-sale transactions and you
don’t want to rely on digital wallets alone. Use cases such as fleet or
contractor purchases or expense management often require physical cards.
**Customization**

Not applicable for virtual cards.

Physical cards have two customization options:

- Standard cards-black or white templated cards that you can personalize with
your business name or logo and instantly send to cardholders. These are best if
you want to prioritize speed-to-market, if basic branding is sufficient for your
cardholders, or if you need to issue only a few cards.
- Custom cards-you can fully customize cards to best feature your branding
goals. These are best if your physical card is a core identifier of your
business or if you want to build brand affinity with your cardholders. However,
custom cards are subject to minimum orders of 2,500 cards and require
significant planning and investment.

For more on the types of physical cards available, see [Physical
cards](https://docs.stripe.com/issuing/cards/physical).

**Creating cards**

Virtual cards can be created using the Dashboard or API. Once created, cards are
immediately generated and available for use.

You can create physical cards using the Dashboard or API. After they’re created,
cards are printed and shipped out within a few days. From there, time of
delivery to the cardholder depends on the shipping speed you choose. See
[Shipping your cards](https://docs.stripe.com/issuing/cards/physical/ship-cards)
for more details.

*Note: Custom cards must be manufactured, tested, and stocked in inventory
before they can be printed out and shipped. Lead times and prices will vary
depending on the level of customization. See Stripe Support for more details.*

**Cost**

Virtual cards are 0.10 USD each in the US, 0.10 GBP in the UK and 0,10 EUR in
the EU.

Standard cards are 3.50 USD each in the US, 3.50 GBP in the UK, and 3,50 EUR in
the EU. Shipping costs apply for each region.

Custom card prices depend on the level of customization of your card design. See
[Stripe Support](https://support.stripe.com/topics/issuing) for more details.

Digital Wallet support[Digital
wallets](https://docs.stripe.com/issuing/cards/digital-wallets) support all of
our card types. A cardholder can add a representation of your virtual or
physical card to their digital wallet for Apple Pay, Google Pay, or Samsung Pay.
Because of market variations, the lead times for digital wallets vary depending
on region and might require partnering with Stripe. See [Stripe
Support](https://support.stripe.com/topics/issuing) for more details.

## Links

- [Read more about virtual cards](https://docs.stripe.com/issuing/cards/virtual)
- [Read more about physical
cards](https://docs.stripe.com/issuing/cards/physical)
- [Shipping your
cards](https://docs.stripe.com/issuing/cards/physical/ship-cards)
- [Stripe Support](https://support.stripe.com/topics/issuing)
- [Digital wallets](https://docs.stripe.com/issuing/cards/digital-wallets)