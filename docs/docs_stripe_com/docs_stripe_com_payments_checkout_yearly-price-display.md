# Display yearly prices in monthly terms

## Help customers compare prices by displaying yearly prices in monthly terms.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
You can display annually billed prices as their per month cost equivalent across
Checkout, Payment Links, [pricing
tables](https://docs.stripe.com/payments/checkout/pricing-table), and [buy
buttons](https://docs.stripe.com/payment-links/buy-button). You can manage
pricing display in your [Checkout and Payment Links
settings](https://dashboard.stripe.com/settings/checkout).

## Checkout and Payment Links

When you have pricing set to display `per month`, Checkout shows a label with
the equivalent monthly rate below the yearly total. If the yearly price is an
[upsell](https://docs.stripe.com/payments/checkout/upsells) from a monthly price
and has a lower equivalent monthly rate, the old price displays with a
strikethrough.

![A yearly recurring price with a monthly terms description in
Checkout](https://b.stripecdn.com/docs-statics-srv/assets/checkout-with-upsell.7a3032232b5d4e1905c0f7ced7101ade.png)

## Pricing table

When you have pricing set to display `per month`, the pricing table displays the
equivalent monthly rate of eligible yearly prices followed by the total annual
amount.

![A pricing table with yearly prices displayed in monthly
terms](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table.a1b0b5b830c1ec8233dfc25733947f57.png)

## Buy button

When you have pricing set to display `per month`, the buy button displays the
equivalent monthly rate of eligible yearly prices followed by the total annual
amount.

![A buy button with a yearly price displayed in monthly
terms](https://b.stripecdn.com/docs-statics-srv/assets/buy-button.a7a65d2d935600d581e4885a90585570.png)

## Restrictions

Customers, sessions, and pricing tables with any of the following features
aren’t eligible to display `per month`:

- A combination of recurring and one-time prices
- Prices with recurring intervals that aren’t billed annually
- Prices with free trials or [billing cycle
anchors](https://docs.stripe.com/payments/checkout/billing-cycle)
- [Usage-based
pricing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)

## Links

- [pricing tables](https://docs.stripe.com/payments/checkout/pricing-table)
- [buy buttons](https://docs.stripe.com/payment-links/buy-button)
- [Checkout and Payment Links
settings](https://dashboard.stripe.com/settings/checkout)
- [upsell](https://docs.stripe.com/payments/checkout/upsells)
- [billing cycle
anchors](https://docs.stripe.com/payments/checkout/billing-cycle)
- [Usage-based
pricing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)