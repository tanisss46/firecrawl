# Customize checkout behavior

## Customize the behavior of the checkout process to increase conversion and revenue.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
## Customize the Submit button

To better align Checkout with your business model, configure the copy displayed
on the Checkout submit button for one-time purchases.

Define a `submit_type` on your session. In this example (for a 5 USD donation),
your customized Checkout submit button would read **Donate $5.00**. See the [API
reference](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-submit_type)
for a complete list of `submit_type` options.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d submit_type=donate \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

## Localization and supported languages

By default, Checkout detects the locale of the customer’s browser and displays a
translated version of the page in their language, if Stripe [supports
it](https://support.stripe.com/questions/supported-languages-for-stripe-checkout).
You can override the browser locale for Checkout by passing the `locale`
[parameter](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-locale)
when you create a Checkout Session.

Checkout also uses the locale to format numbers and currencies. For example,
when selling a product whose price is set in EUR with the locale set to `auto`,
a browser configured to use (`en`) would display €25.00 while one
configured for German (`de`) would display 25,00 €.

## Autofill payment details with Link

You can automatically use Link (Stripe’s one-click checkout) in your prebuilt
Checkout page. To learn more, see [Link with
Checkout](https://docs.stripe.com/payments/link/checkout-link).

## Filter card brands

You can specify which card brands you want to block from your customers in the
Checkout Session.

To block specific card brands, you can include the `brands_blocked` parameter
when creating a Checkout Session. Pass an array with any of the following card
brand values:

- `visa`
- `mastercard`
- `american_express`
- `discover_global_network`

The `discover_global_network` value encompasses all of the cards that are part
of the Discover Global Network, including Discover, Diners, JCB, UnionPay, and
Elo.

The following code example initializes the Checkout Session with the
`brands_blocked` parameter set to `['american_express']`, which prevents
customers from using American Express cards.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 --data-urlencode return_url="https://example.com/return" \
-d
"payment_method_options[card][restrictions][brands_blocked][0]"=american_express
```

If a customer enters an unsupported card number in Checkout, an error message
notifies them that their card brand isn’t accepted.

![Card brand filtering on
Checkout](https://b.stripecdn.com/docs-statics-srv/assets/card-brand-filtering-on-form.e3a1bab1800020eefd977e093863d208.png)

An error surfaces informing the customer that you don’t accept Visa (or whatever
card brand you have blocked).

Additionally, Link also disables saved cards for returning users if the saved
card is blocked.

![Card brand filtering on Checkout with
Link](https://b.stripecdn.com/docs-statics-srv/assets/card-brand-filtering-link.eb5ed48829c0b18a59dadf2a77cd6a66.png)

If a Link user’s saved card is blocked, it is disabled.

Checkout also filters cards in Apple and Google Pay wallets, customer’s [saved
payment methods](https://docs.stripe.com/payments/checkout/save-during-payment),
and [networks from co-badged
cards](https://docs.stripe.com/co-badged-cards-compliance).

## Links

- [API
reference](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-submit_type)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [supports
it](https://support.stripe.com/questions/supported-languages-for-stripe-checkout)
-
[parameter](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-locale)
- [Link with Checkout](https://docs.stripe.com/payments/link/checkout-link)
- [https://example.com/return](https://example.com/return)
- [saved payment
methods](https://docs.stripe.com/payments/checkout/save-during-payment)
- [networks from co-badged
cards](https://docs.stripe.com/co-badged-cards-compliance)