# Pay by Bank payments

## Learn how to accept Pay by Bank payments.

Stripe-hosted pageAdvanced integration
#### Caution

Stripe automatically presents your customers payment method options by
evaluating their currency, payment method restrictions, and other parameters. We
recommend that you configure your payment methods from the Stripe Dashboard
using the instructions in [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted).

If you want to continue manually configuring the payment methods you present to
your customers with Checkout, use this guide. Otherwise, update your integration
to [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods).

Pay by Bank is a [single
use](https://docs.stripe.com/payments/payment-methods#usage) payment method
where customers must
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. Pay by Bank redirects customers from your website, authorizes the
payment, and returns them to your website.

You get [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed.

[Determine
compatibility](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support Pay
by Bank payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency. If you have line items in different currencies, create separate
Checkout Sessions for each currency.
- You can only use one-time line items. Recurring
[subscription](https://docs.stripe.com/billing/subscriptions/creating) plans are
not supported.

Pay by Bank is on our roadmap for Germany in 2025. You can register your
interest in Pay by Bank in Germany in the form below.

## Interested in getting early access to Pay by Bank in Germany?

To learn more or get early access, enter your email address below. We’ll
determine your eligibility and guide you through the onboarding steps.

Collect EmailSign upRead our [privacy
policy](https://stripe.com/privacy).[Accept a
payment](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment#accept-a-payment)
#### Note

This guide builds on the foundational [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
Checkout integration.

Use this guide to learn how to enable Pay by Bank—it shows the differences
between accepting a card payment and using Pay by Bank.

### Enable Pay by Bank as a payment method

To create a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions):

- Add `pay_by_bank` to the list of `payment_method_types`
- Add the necessary [payment method
options](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-pay_by_bank)
fields for `pay_by_bank`
- Make sure all your `line_items` use the `gbp` currency

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "mode"="payment" \
 -d "payment_method_types[]"="card" \
 -d "payment_method_types[]"="pay_by_bank" \
 -d "statement_descriptor"="Business name" \
 -d "line_items[0][price_data][currency]"="gbp" \
 -d "line_items[0][price_data][unit_amount]"=2000 \
 -d "line_items[0][price_data][product_data][name]"="Blue bananas" \
 -d "line_items[0][quantity]"=1 \
 -d "success_url"="https://example.com/success" \
 -d "cancel_url"="https://example.com/cancel"
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill
orders](https://docs.stripe.com/checkout/fulfillment).

[Test your
integration](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment#test-integration)
To test your Checkout integration, select Pay by Bank as the payment method and
click the **Pay** button.

[Handle refunds and
disputes](https://docs.stripe.com/payments/pay-by-bank/accept-a-payment#refunds-and-disputes)
The refund period for Pay by Bank is up to 730 days (2 years) after the original
payment.

There is no dispute process—customers authenticate with their bank.

## See also

- [More about Pay by Bank](https://docs.stripe.com/payments/pay-by-bank)
- [Checkout fulfillment](https://docs.stripe.com/checkout/fulfillment)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Prices](https://docs.stripe.com/api/prices)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [privacy policy](https://stripe.com/privacy)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?ui=stripe-hosted)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [payment method
options](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-pay_by_bank)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [More about Pay by Bank](https://docs.stripe.com/payments/pay-by-bank)
- [Customizing
Checkout](https://docs.stripe.com/payments/checkout/customization)