# Accept meses sin intereses card payments

## Learn how to accept credit card payments using meses sin intereses across a variety of Stripe products.

Installments (meses sin intereses) is a feature of consumer credit cards in
Mexico that allows customers to split purchases over multiple billing
statements. You receive payment as if it were a normal one-time charge, with
fees deducted, and the customer’s bank handles collecting the money over time.

Some restrictions apply to which transactions and cards can use installments.
Review the [compatibility
requirements](https://docs.stripe.com/payments/mx-installments#requirements).

Accepting an installment payment incurs [an additional
fee](https://docs.stripe.com/payments/mx-installments#fees) to the standard
credit card transaction fee.

You can enable installments across a variety of Stripe products. Choose the
instructions below matching your implementation.

Payment Element support for meses sin intereses is in private preview. To get
access, contact [Stripe support](https://support.stripe.com/?contact=true).

Stripe-hosted pageDirect APIInvoicesNo code
## Installments on Stripe Checkout

[Checkout](https://docs.stripe.com/payments/checkout) creates a secure,
Stripe-hosted payment page that lets you collect payments quickly. It works
across devices and can help increase your conversion. Checkout provides a
low-code way to get started accepting payments.

Your customers use Checkout to pay with cards (with or without installments) and
other payment methods that support Checkout.

[Review Checkout
documentation](https://docs.stripe.com/payments/meses-sin-intereses/accept-a-payment#integrate)
Stripe Checkout allows you to collect installment payments. For information
about setting up Checkout, see the
[quickstart](https://docs.stripe.com/checkout/quickstart).

[Create a new Checkout
session](https://docs.stripe.com/payments/meses-sin-intereses/accept-a-payment#create-new-session)
Create a new Checkout session with installments enabled as shown in the example
below. You need to substitute your own price object.

#### Note

Installments only works with `payment` mode, not `setup` or `subscription` mode.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=3 \
 -d mode=payment \
 -d "payment_method_options[card][installments][enabled]"=true
```

[Redirect to
Checkout](https://docs.stripe.com/payments/meses-sin-intereses/accept-a-payment#redirect)
After creating the session, redirect your customer to the URL for the Checkout
page returned in the CheckoutSession.

## See also

- [Checkout integration guide](https://docs.stripe.com/checkout/quickstart)
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)
- [Payment Intents](https://docs.stripe.com/api/payment_intents/object)

## Custom settings

You can customize your installments configuration using the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) payment
methods settings page.

You can find the option to enable or disable installments in your [payment
methods settings page](https://dashboard.stripe.com/settings/payment_methods).
This setting allows you to enable installments for no-code payment methods,
including Payment Links and Checkout.

Separately, on the payment methods settings page, you can also configure the
specific monthly plans you want to offer and the minimum and maximum transaction
amounts for each plan. These plan configurations apply to all of your existing
installments integrations.

## Test the integration

You can use the following cards to test your integration:

NumberDescription40000048400000083, 6, 9, 12, 18, and 24 month installment plans
available4242424242424242No installment plans available.

## Links

- [compatibility
requirements](https://docs.stripe.com/payments/mx-installments#requirements)
- [an additional fee](https://docs.stripe.com/payments/mx-installments#fees)
- [Stripe support](https://support.stripe.com/?contact=true)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [quickstart](https://docs.stripe.com/checkout/quickstart)
- [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions)
- [Payment Intents](https://docs.stripe.com/api/payment_intents/object)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)