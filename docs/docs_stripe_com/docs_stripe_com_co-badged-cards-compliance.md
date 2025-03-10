# Co-badged cards compliance

## Learn about EU regulations requiring customer choice for co-badged cards.

#### Does this regulation apply to me?

[Regulation (EU)
2015/751](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32015R0751)
applies to all businesses in the EEA that can process Cartes Bancaires. [Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fco-badged-cards-compliance)
and return to this section to view if co-badged card regulation applies to you.

**Applicable in:**

AustriaBelgiumBulgariaCroatiaCyprusCzech
RepublicDenmarkEstoniaFinlandFranceGermanyGreeceHungaryIcelandIrelandItalyLatviaLiechtensteinLithuaniaLuxembourgMaltaNetherlandsNorwayPolandPortugalRomaniaSlovakiaSloveniaSpainSweden
## Regulatory requirements

[Regulation (EU)
2015/751](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32015R0751)
requires businesses in the European Economic Area (EEA) to honor customers’ card
brand choice for co-badged cards (for example, [Cartes
Bancaires](https://docs.stripe.com/payments/cartes-bancaires) cards co-badged
with Visa). In practice, this means you must enable cardholders to select a
preferred card brand within your checkout form in accordance with these
guidelines:

- **Display the available card networks in your checkout form:** All available
card networks must be clearly identified during the checkout process. The visual
quality, clarity, and size of the brand logos must be consistent, and it should
be clear to cardholders how to select a card network.
- **Abide by the cardholder’s preferred card network:** Where the cardholder
chooses their preferred card network, you must use it when confirming a payment
or storing card details for future use. If the cardholder doesn’t make a choice,
you can choose your card network for the transaction.
- **Allow updates to the preferred card network:** You must present cardholders
updating their payment methods that are saved for future use with the option to
change their preferred card network when they’re updating their payment details.
For example, you can provide a customer portal for managing saved payment
methods.

## When regulation applies

Cartes Bancaires co-badged cards are the only Stripe-supported cards that fall
under this regulation. As a result, [Regulation (EU)
2015/751](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32015R0751)
applies to businesses that:

- Are in the EEA
- Can process Cartes Bancaires

#### Connect users

In Connect integrations, the merchant of record on a transaction is the business
we use to determine if co-badged regulation applies. Depending on the Connect
integration, this can either be the Platform or the Connected account.

Businesses that meet the above criteria are required to present customers with a
choice of card network for all transactions that can processed with [Cartes
Bancaires](https://docs.stripe.com/payments/cartes-bancaires). A transaction is
eligible for Cartes Bancaires if:

- The business can process Cartes Bancaires
- The currency is EUR
- The payment method is a co-badged Cartes Bancaires card

#### Using test mode

Cartes Bancaires is always enabled in test mode. As a result, you might see the
network selector on Stripe-hosted UIs in test mode even if you don’t enable
Cartes Bancaires. This allows you to preview how Stripe-hosted UIs might handle
co-badged cards if Cartes Bancaires was enabled.

## Integration guides

Stripe-hosted UIs, such as
[Checkout](https://docs.stripe.com/payments/checkout), [Payment
Links](https://docs.stripe.com/payment-links), and
[Elements](https://docs.stripe.com/payments/elements), will automatically
display a network selector when you meet the [applicability
criteria](https://docs.stripe.com/co-badged-cards-compliance#when-reglation-applies)
above, if configured according to the following guides. You can migrate to a
Stripe-hosted UI to use these features.

For other integrations, you’re fully responsible for making sure your
integration complies with the regulation requirements.

Checkout and Payment LinksWeb ElementsMobile ElementsCustom integration
[Stripe Checkout](https://stripe.com/checkout) supports customer card brand
choice by default. Customers who enter a co-badged card in Checkout can select
their option for customer card brand choice:

![The card input with a co-badged card in Stripe
Checkout](https://b.stripecdn.com/docs-statics-srv/assets/checkout-card-brand-choice-full-page.9cf891dfb55abcdc9ae9046ea15bc054.png)

Card input with a co-badged card

## Identifying network used to process a charge

The charge object associated with a successful payment contains a `network`
field indicating which card network the payment was processed on:

```
{
 "id": "ch_1Ff52K2eZvKYlo2CWe10i0s7",
 "object": "charge",
 ...
 "payment_method_details": {
 "card": {
 "brand": "visa",
 ...
 "network": "cartes_bancaires",
 },
 "type": "card"
 }
}
```

## Testing

You can use the following co-badged cards to test your integration:

Card numbersTokensPaymentMethodsNumberBrandCVCDate4000002500001001Cartes
Bancaires or VisaAny 3 digitsAny future date5555552500001001Cartes Bancaires or
MastercardAny 3 digitsAny future date

## Links

- [Regulation (EU)
2015/751](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32015R0751)
- [Sign
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fco-badged-cards-compliance)
- [Cartes Bancaires](https://docs.stripe.com/payments/cartes-bancaires)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Elements](https://docs.stripe.com/payments/elements)
- [Stripe Checkout](https://stripe.com/checkout)