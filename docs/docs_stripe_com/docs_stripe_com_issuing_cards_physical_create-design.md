# Create a design

## Create and name your bundle design.

To create and name your design in the Issuing Dashboard or API before issuing
cards to your cardholders, go directly to the
[Designs](https://dashboard.stripe.com/test/issuing/personalization-designs) tab
and click on **New design**. The standard option is always available, while the
custom option becomes available after you order a custom bundle.

DashboardAPI
## Use a standard bundle

- Visit the [Designs
tab](https://dashboard.stripe.com/test/issuing/personalization-designs) in the
Issuing Dashboard.

![Personalization
designs](https://b.stripecdn.com/docs-statics-srv/assets/card-issuing-designs-tab.8005cf6843cfad8a17067f2cb7eef4e3.png)
- Click **New design** on the upper right and select the **Standard** physical
bundle type.
- Select a white or black card.

![Choose a physical
bundle](https://b.stripecdn.com/docs-statics-srv/assets/choose-physical-bundle.b72ce7b9da304477e2c8ef84993a5599.png)
- Upload your card logo. The logo must be in .PNG format, with a legible size of
1000px by 200px. It must be a binary image containing a black logo on a white
background with no grayscale.
- Set your carrier text.

![Custom carrier
letter](https://b.stripecdn.com/docs-statics-srv/assets/customize-carrier-letter.de2468a680e90b169109fd1c95e1db8d.png)
- Review the design summary and set a name used to specify the physical bundle
when [issuing cards](https://docs.stripe.com/issuing/cards/physical/issue-cards)
to your cardholders.
- Click **Submit** to send your [design for
review](https://docs.stripe.com/issuing/cards/physical/create-design#design-review).

## Use a custom bundle

- Visit the [Designs
tab](https://dashboard.stripe.com/test/issuing/personalization-designs) in the
Issuing Dashboard.

![Personalization
designs](https://b.stripecdn.com/docs-statics-srv/assets/card-issuing-designs-tab.8005cf6843cfad8a17067f2cb7eef4e3.png)
- Click **New design** on the upper right and select the **Custom** physical
bundle type.
- Select the custom bundle from the drop-down list. Stripe enables visibility of
the bundle in the Dashboard after the order has been manufactured and made live.
See [Order a custom
bundle](https://docs.stripe.com/issuing/cards/physical/order-custom-bundle) for
more details.

- If you’ve chosen to add an additional logo during
[personalization](https://docs.stripe.com/issuing/cards/choose-bundle#manufacturing-personalization),
you’re prompted to upload your card logo next. Ensure the logo is in .PNG
format, with a legible size of 1000px by 200px. It must be a binary image
containing a black logo on a white background with no grayscale.
- If you’ve chosen the standard carrier, you’re prompted to upload your carrier
text next.

![Custom physical
bundle](https://b.stripecdn.com/docs-statics-srv/assets/custom-physical-bundle.a5d0bb3b3206c19d3aba48e3d18f859f.png)
- Review design summary and set a personalization design name. The
personalization design name is used to specify the physical bundle when [issuing
cards](https://docs.stripe.com/issuing/cards/physical/issue-cards) to your
cardholders.

![Custom design
summary](https://b.stripecdn.com/docs-statics-srv/assets/custom-design-summary.feda6552ffa73fc575d217cf45b03008.png)
- Click **Submit** to send your design for review. This is only applicable when
an additional logo is added on the card or text is added on the standard
carriers.

## Design review

Stripe reviews all logos and carrier text to make sure they comply with the
guidelines set by our partner networks. We approve almost all designs, but we
might reject yours if it contains:

- The name of another legal entity.
- A reference to a different network (for example, Mastercard if you’re issuing
on Visa).
- The name of a geographic location.
- A reference to non-fiat currency (for example, cryptocurrency).
- Advertising or promotional language.
- Inappropriate text or imagery.

## Design rejection

If Stripe rejects your design, we notify you by email within 2 business days and
ask you to resubmit an updated design. When Stripe approves your design, we
submit any cards that you issued using the design to the vendor. To issue cards
with your newly created personalization design, see [Issue
cards](https://docs.stripe.com/issuing/cards/physical/issue-cards).

## Links

- [Designs](https://dashboard.stripe.com/test/issuing/personalization-designs)
- [issuing cards](https://docs.stripe.com/issuing/cards/physical/issue-cards)
- [Order a custom
bundle](https://docs.stripe.com/issuing/cards/physical/order-custom-bundle)
-
[personalization](https://docs.stripe.com/issuing/cards/choose-bundle#manufacturing-personalization)