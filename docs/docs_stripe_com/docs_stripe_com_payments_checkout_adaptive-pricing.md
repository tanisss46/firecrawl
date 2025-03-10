# Adaptive Pricing

## Let customers pay in their local currency with Adaptive Pricing to increase international revenue.

Stripe-hosted pageEmbedded formEmbedded componentsPrivate preview
Adaptive Pricing lets your customers pay in their local currency in more than
[150
countries](https://docs.stripe.com/payments/checkout/adaptive-pricing#supported-currencies).
With Adaptive Pricing, Stripe automatically calculates the localized price and
handles all currency conversion. The presentment currency is inferred from the
buyer’s public IP address. Enabling Adaptive Pricing can increase conversion
rates from global buyers and increase international revenue.

Use Adaptive Pricing to:

- Display pricing in local currencies based on location
- Calculate prices in real-time using an exchange rate guaranteed for 24 hours
- Unlock payment methods that require local currency
- Facilitate your compliance when presenting supported currencies

![A customer in France views a price localized from USD to
EUR](https://b.stripecdn.com/docs-statics-srv/assets/adaptive_pricing.7955669ffbb4f3ddeaca083e186eeb99.png)

### Integration effort

Low code
### Fees

View information on [fees and our
FAQ](https://support.stripe.com/questions/adaptive-pricing).

[Enable Adaptive
PricingDashboard](https://docs.stripe.com/payments/checkout/adaptive-pricing#enable-adaptive-pricing)
Enable Adaptive Pricing in your [payment
settings](https://dashboard.stripe.com/settings/adaptive-pricing) in the
Dashboard. You can enable Adaptive Pricing in a sandbox and live mode. Disabling
Adaptive Pricing doesn’t affect Checkout Sessions that have already been
converted.

Adaptive Pricing works with Checkout, Payment Links, pricing tables, and local
payment methods.

[Configure local payment
methodsDashboard](https://docs.stripe.com/payments/checkout/adaptive-pricing#configure-local-payment-methods)
You can configure which payment methods you accept in your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). Adaptive
Pricing can increase the usage of local payment methods by ensuring customers
have the option to pay in their currency and with payment methods most relevant
to them. As an example, 70% of all e-commerce transactions in the Netherlands
use iDEAL, but it only works with EUR. Adaptive Pricing enables the following
payment methods:

- Alipay
- Bancontact
- BLIK
- Canadian pre-authorized debit
- EPS
- iDEAL
- Link
- PayPal
- P24
- SEPA Debit
- Sofort
- Swish
- WeChat Pay
[Event destinations and
reportingServer-side](https://docs.stripe.com/payments/checkout/adaptive-pricing#event-destinations-reporting)
Enabling Adaptive Pricing can affect some parts of your integration, such as
event destinations and reporting. Review your integration to make sure any
[event
destinations](https://docs.stripe.com/payments/checkout/adaptive-pricing#event-destinations-reporting)
can handle PaymentIntent objects with local currencies.

- Use the
[currency_conversion](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-currency_conversion)
hash on the Checkout Session object to determine what your customer would have
paid in the default currency.
- Use the [BalanceTransactions
API](https://docs.stripe.com/api/balance_transactions) to determine how much you
receive after fees.

Depending on the user-selected currency, both the Checkout Session and the
underlying PaymentIntent objects update automatically to reflect the selected
currency and amount. After a user pays in local currency, the Checkout Session
object’s currency and total amount is in local currency and contains a
`currency_conversion` hash to reflect what the user would have paid in the
default currency. Learn more about what’s [deposited in your account after
fees](https://docs.stripe.com/api/balance_transactions).

The
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
event contains a `currency_conversion` hash that includes the `amount_total` and
`amount_subtotal` in the `source_currency`. The amounts reflect what your
customer would have paid in the source currency.

```
{
 "id": '{{EVENT_ID}}',
 "object": "event",
 "type": "checkout.session.completed",
 "data": {
 "object": {
 "id": '{{SESSION_ID}}',
 "object": "checkout.session",
 "currency": "cad",
 "amount_total": 2055,
 "amount_subtotal": 2055,
 "currency_conversion": {
 "amount_subtotal": 1500,
 "amount_total": 1500,
 "source_currency": "usd",
 "fx_rate": "1.37"
 }
 }
 }
}
```

[Testing](https://docs.stripe.com/payments/checkout/adaptive-pricing#testing)
To test local currency presentment for Checkout, Payment Links, and the [pricing
table](https://docs.stripe.com/payments/checkout/pricing-table), pass in a
location-formatted customer email that includes a suffix in a `+location_XX`
format in the local part of the email. `XX` must be a valid [two-letter ISO
country code](https://www.nationsonline.org/oneworld/country_code_list.htm).

For example, to test currency presentment for a customer in France, pass in an
email like `test+location_FR@example.com`.

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
 -d "line_items[0][price]"="{{PRICE_ID}}" \
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

## Supported currencies

Businesses in supported regions can automatically convert prices to the local
currencies of their customers in the following markets:

### North America

### South America

### Europe

### Asia

### Oceania

### Africa

## Restrictions

Adaptive Pricing doesn’t currently work with Connect or Elements with the
Payment Intents API.

Additionally, Adaptive Pricing requires the [currency for your
prices](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-currency)
to be the same as your default settlement currency. Prices automatically convert
during checkout. This applies to
[prices](https://docs.stripe.com/products-prices/manage-prices#prices-create)
you create and reference with a price ID and prices you create inline with
[price_data](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price_data)
when you create a Checkout Session.

Adaptive Pricing doesn’t apply for Checkout Sessions that:

- Contain explicitly defined [manual currency
prices](https://docs.stripe.com/payments/checkout/manual-currency-prices).
- Are in `subscription` mode.
- Use Connect parameters like `application_fee_amount`, `on_behalf_of`, and
`transfer_data`.
- Use
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
as `manual`.
- Set the
[currency](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-currency)
value on creation.
- Use [custom
amounts](https://docs.stripe.com/payments/checkout/pay-what-you-want).
- Present the customer a local currency that is also configured as a [settlement
currency](https://docs.stripe.com/payouts#supported-accounts-and-settlement-currencies).
For example, suppose an account settles in both `EUR` and `GBP`. If they price
in `EUR`, customers with local currency `GBP` don’t see Adaptive Pricing.
Customers with a local currency other than `EUR` or `GBP`, such as `JPY`, see
Adaptive Pricing.

Checkout Sessions that aren’t supported by Adaptive Pricing present prices in
the original currency that you’ve set your prices in.

## Pricing

- You pay 0
- Your buyers pay 2-4

You (the business) don’t directly pay any additional fees for Adaptive Pricing,
as all such fees are paid for by your customers. Stripe applies a conversion fee
of between 2-4% to the exchange rate you present to your customers, increasing
their purchase price by a corresponding amount. The fee applied is determined by
Stripe and varies for the purposes of increasing customer conversion. Stripe
typically charges a fee of 4% for orders under 500 USD, 3% for 500–1,500 USD,
and 2% for orders over 1,500 USD. For detailed information about current Stripe
fees, see our [pricing page](https://stripe.com/pricing).

## Exchange rate

Stripe uses the mid-market exchange rate and applies a fee to guarantee the rate
for the duration of the Checkout Session (up to 24 hours) through settlement. If
the exchange rate changes by more than 5% in that time, Stripe might use the
updated exchange rate to calculate your payout.

Learn more about how Stripe handles [currency
conversions](https://docs.stripe.com/currencies/conversions) and [Adaptive
Pricing
fees](https://support.stripe.com/questions/adaptive-pricing#:~:text=Adaptive%20Pricing%20is%20a%20Checkout,latest%20Stripe%2Dprovided%20exchange%20rates).

## Refunds

Stripe pays out refunds in the currency your customer pays in using the latest
Stripe-provided exchange rate. This means that you might pay more or less to
cover the refund depending on how the exchange rate changes.

### Example refund

We ignore Stripe fees in this example for simplicity. Suppose:

- You’re a US business that uses Checkout to sell a product for 100 USD and have
activated Adaptive Pricing.
- A customer in Canada views your Checkout page, sees the localized price of 137
CAD at an exchange rate of 1.37 CAD per 1 USD, and completes the purchase.
- Stripe processes the payment, converting the 137 CAD to 100 USD to pay you in
your settlement currency.
- Later, when the exchange rate has changed to 1.40 CAD per 1 USD, you issue a
full refund to the customer.
- Stripe deducts 97.86 USD from your account, exchanging it at 1.40 CAD per 1
USD to pay out the 137 CAD refund.

Learn more about how Stripe helps you manage
[refunds](https://docs.stripe.com/refunds).

## See also

- [Adaptive Pricing FAQ](https://support.stripe.com/questions/adaptive-pricing)

## Links

- [fees and our FAQ](https://support.stripe.com/questions/adaptive-pricing)
- [payment settings](https://dashboard.stripe.com/settings/adaptive-pricing)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
-
[currency_conversion](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-currency_conversion)
- [BalanceTransactions API](https://docs.stripe.com/api/balance_transactions)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
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
- [currency for your
prices](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-currency)
- [prices](https://docs.stripe.com/products-prices/manage-prices#prices-create)
-
[price_data](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price_data)
- [manual currency
prices](https://docs.stripe.com/payments/checkout/manual-currency-prices)
-
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
-
[currency](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-currency)
- [custom amounts](https://docs.stripe.com/payments/checkout/pay-what-you-want)
- [settlement
currency](https://docs.stripe.com/payouts#supported-accounts-and-settlement-currencies)
- [pricing page](https://stripe.com/pricing)
- [currency conversions](https://docs.stripe.com/currencies/conversions)
- [Adaptive Pricing
fees](https://support.stripe.com/questions/adaptive-pricing#:~:text=Adaptive%20Pricing%20is%20a%20Checkout,latest%20Stripe%2Dprovided%20exchange%20rates)
- [refunds](https://docs.stripe.com/refunds)