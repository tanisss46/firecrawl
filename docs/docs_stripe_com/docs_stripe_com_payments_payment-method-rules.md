# Payment method rules

## Control when payment methods are available to your buyers.

Payment method rules allow you to set conditions on payment methods directly
from the Dashboard without any custom logic or code. Rules allow you to:

- Hide or show a payment method if the order amount is over or under a certain
amount
- Hide or show a payment method for buyers in certain countries or using certain
currencies

## Payment method rules considerations

Non-card payment methods can help offer improved unit economics compared to
cards and they often drive higher AOV and conversion rates.

When you turn on these payment methods, you might want to apply specific
business logic to control when payment methods are available to your buyers.
With payment method rules, you can apply these insights directly in Dashboard—no
code required.

Payment method rules are compatible with Stripe [A/B
Testing](https://docs.stripe.com/payments/a-b-testing). This allows you to run
A/B tests using the targeting criteria you select or test additional criteria.
For example, you can test the impact of only showing a specific payment method
when the price is greater than a certain dollar amount.

#### Note

Payment method rules won’t apply when a Payment Element, Checkout, or Payment
Links integration creates a
[subscription](https://docs.stripe.com/billing/subscriptions/creating). For more
information about subscriptions and invoices, see [How subscriptions
work](https://docs.stripe.com/billing/subscriptions/overview).

## Before you begin

- You must use either the Stripe [Payment
Element](https://docs.stripe.com/payments/payment-element),
[Checkout](https://docs.stripe.com/payments/checkout), or [Payment
Links](https://docs.stripe.com/payment-links).
- You must use [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
to enable additional payment methods from the Stripe Dashboard, which won’t
require any code changes.- To set up dynamic payment methods for direct users,
see the [payment method
integration](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
guide.
- Connect To set up dynamic payment methods for Connect platforms, see
[Upgrading to dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods).
[Set rule
conditions](https://docs.stripe.com/payments/payment-method-rules#set-rule-conditions)-
In your Dashboard, go to [Payment methods
settings](https://dashboard.stripe.com/test/settings/payment_methods).
- In the payment method row, select **Create custom rules**.

![Klarna
Row](https://b.stripecdn.com/docs-statics-srv/assets/pmt-klarna-row.931f50a1bd9a4d872657f0372dead2d8.png)
- Set custom rules (for example, a new minimum of 100 USD for Klarna), then
select **Apply Overrides**. The configured payment method now has a
**Customized** tag. A customized payment method appears only in Checkout or
Payment Element sessions that meet its targeting criteria.

![A checkout page showing
Klarna.](https://b.stripecdn.com/docs-statics-srv/assets/pmt-checkout-klarna-present.fab9fed6ec4dfc1e187b38beb944fc65.png)

Before

![A checkout page with Klarna
hidden.](https://b.stripecdn.com/docs-statics-srv/assets/pmt-checkout-klarna-hidden.e1d585ab6318861be8aa813cdde91fb4.png)

After

## Links

- [A/B Testing](https://docs.stripe.com/payments/a-b-testing)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [How subscriptions
work](https://docs.stripe.com/billing/subscriptions/overview)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Upgrading to dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods)
- [Payment methods
settings](https://dashboard.stripe.com/test/settings/payment_methods)