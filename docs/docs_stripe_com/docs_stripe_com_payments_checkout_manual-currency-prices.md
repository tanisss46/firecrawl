# Manual currency prices

## Present local currencies to customers with manual currency prices.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
Stripe supports manually defining prices in different currencies when creating
[products](https://docs.stripe.com/products-prices/overview#get-started).
However, Stripe recommends leveraging [Adaptive
Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing) instead of
manual currency prices to reduce currency exchange rate fluctuation risk and to
automatically enable support for 50+ local currencies.

Use manual currency prices over Adaptive Pricing when:

- Adaptive Pricing isn’t yet
[supported](https://docs.stripe.com/payments/checkout/adaptive-pricing#restrictions)
for your business or Checkout configuration (reach out to
[adaptive-pricing-beta@stripe.com](mailto:adaptive-pricing-beta@stripe.com) to
inquire about the preview).
- You’re supporting a region where you’re comfortable taking on fluctuations in
the currency’s exchange rate.

Manually defined multi-currency prices override Adaptive Pricing for those
currencies, even if it’s enabled.

[Create a multi-currency
priceDashboardServer-side](https://docs.stripe.com/payments/checkout/manual-currency-prices#add-multiple-currencies-to-a-price)DashboardAPI-
Navigate to a product in the
[Dashboard](https://dashboard.stripe.com/products?active=true).
- Click **+Add another price** to create a new price.
- Fill in the price and select a currency. This first currency is the price’s
default currency. Make sure all of your prices have the same default currency.
- Click **+Add a price by currency** to search and select from supported
currencies, adding them to your price.
- Use the multi-currency price you created by passing its ID into [line
items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price)
when you create a Checkout Session.
[Create a Checkout
SessionServer-side](https://docs.stripe.com/payments/checkout/manual-currency-prices#create-checkout-session)
Create a Checkout Session using the multi-currency price:

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success"
```

[TestingServer-sideClient-side](https://docs.stripe.com/payments/checkout/manual-currency-prices#testing)
To test local currency presentment for Checkout, Payment Links, and the [pricing
table](https://docs.stripe.com/payments/checkout/pricing-table), pass in a
location-formatted customer email that includes a suffix in a `+location_XX`
format in the local part of the email. `XX` must be a valid [two-letter ISO
country code](https://www.nationsonline.org/oneworld/country_code_list.htm).

For example, to test currency presentment for a customer in France, pass in an
email such as `test+location_FR@example.com`.

When you visit the URL for a Checkout Session, Payment Link, or pricing table
created with a location-formatted email, you see the same currency as a customer
does in the specified country.

### Testing Checkout

When you create a Checkout Session, pass the location-formatted email as
[customer_email](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_email)
to simulate Checkout from a particular country.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 -d success_url="https://example.com/success" \
 --data-urlencode customer_email="test+location_FR@example.com"
```

You can also create a [Customer](https://docs.stripe.com/api/customers/create)
and specify their email that contains the `+location_XX` suffix. Stripe test
cards work as usual.

When it’s possible to present the customer’s local currency in Checkout, the
[Checkout Session](https://docs.stripe.com/api/checkout/sessions/object) object
changes. Fields like `currency`, `payment_method_types`, and `amount_total`
reflect the local currency and price.

### Testing Payment Links

For Payment Links, pass the location-formatted email as the `prefilled_email`
[URL
parameter](https://docs.stripe.com/payment-links/customize#customize-checkout-with-url-parameters)
to test currency presentment for customers in different countries.

### Testing Pricing table

For the pricing table, pass the location-formatted email as the
[customer-email](https://docs.stripe.com/payments/checkout/pricing-table#customer-email)
attribute to test currency presentment for customers in different countries.

[OptionalSpecify a
currencyServer-side](https://docs.stripe.com/payments/checkout/manual-currency-prices#specify-currency)
## Local payment methods

The Checkout Session presents customers with popular payment methods compatible
with their local currencies. For example, for customers located in the
Netherlands, the Checkout Session converts prices to EUR and also present
popular Dutch payment methods like iDEAL.

You can configure which payment methods you accept in your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

## Pricing tables

Manual currency prices also work with [pricing
tables](https://docs.stripe.com/payments/checkout/pricing-table). To render
local currencies to customers viewing your pricing table, all of the pricing
table’s Prices must include the customer’s local currency in their
`currency_options`. They must also include a `tax_behavior` for the given
currency if you’re using Stripe Tax.

## Supported integrations

Checkout automatically presents the local currency to customers if all of the
following are true:

- The Checkout Session’s prices, shipping rates, and discounts have the relevant
currency in their `currency_options`.
- If a price on the Checkout Session has an upsell, the upsell’s price has the
relevant currency in its `currency_options`.
- For a Checkout Session using Stripe Tax, the `tax_behavior` on the Checkout
Session is specified for the relevant currency for all of the Checkout Session’s
prices, shipping rates, and discounts.
- You didn’t specify a currency during Checkout Session creation.

If Checkout can’t localize the currency because the relevant currency option or
`tax_behavior` is missing, the Session presents to the customer in the default
currency. The default currency must be the same across all prices, shipping
rates, and discounts.

### Restrictions

Price localization isn’t available for Checkout Sessions that:

- Use manual tax rates.
- Use `payment_intent_data.application_fee_amount` or
`payment_intent_data.transfer_data.amount`.

## Fees

Stripe’s standard transaction fees apply to automatically converted
transactions:

- Cards or payment methods fee
- International cards or payment methods fee (if applicable)
- Currency conversion fee

See the [pricing page](https://stripe.com/pricing) for more details about these
fees.

## Links

- [products](https://docs.stripe.com/products-prices/overview#get-started)
- [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing)
-
[supported](https://docs.stripe.com/payments/checkout/adaptive-pricing#restrictions)
- [Dashboard](https://dashboard.stripe.com/products?active=true)
- [line
items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price)
- [https://example.com/success](https://example.com/success)
- [pricing table](https://docs.stripe.com/payments/checkout/pricing-table)
- [two-letter ISO country
code](https://www.nationsonline.org/oneworld/country_code_list.htm)
-
[customer_email](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_email)
- [Customer](https://docs.stripe.com/api/customers/create)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object)
- [URL
parameter](https://docs.stripe.com/payment-links/customize#customize-checkout-with-url-parameters)
-
[customer-email](https://docs.stripe.com/payments/checkout/pricing-table#customer-email)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [pricing page](https://stripe.com/pricing)