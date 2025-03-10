# Set up payment method rules

## Learn how to set up payment method rules for the Stripe Connector for NetSuite.

The Stripe Connector for NetSuite supports using [payment method
rules](https://docs.stripe.com/payments/payment-method-rules) to set the
following conditions on payment methods:

- Hide or show a payment method if the order amount is over or under a certain
amount
- Hide or show a payment method for buyers in certain countries or using certain
currencies

These rules control the payment methods shown on the [invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/overview)
page.

You can use payment method rules for most payment methods, with the exception of
[cards](https://docs.stripe.com/payments/cards). You can turn off cards, which
also turns off [wallets](https://docs.stripe.com/payments/wallets).

## Configure rules for your payment methods

- In your Stripe Dashboard, go to **Settings** > **Payments**.
- On the [Payment
methods](https://dashboard.stripe.com/test/settings/payment_methods) tab, use
the dropdown to locate your NetSuite configuration.
- Under **Stripe Connector for NetSuite configurations**, click **Default**.
- Click the overflow menu () for the payment method that you want to configure a
rule for.
- Create your custom rule, for example, by setting the minimum and maximum
amounts for the transaction limit. When finished, click **Save rules**.

## See also

- [NetSuite invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/overview)
- [Install the NetSuite connector invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation)

## Links

- [payment method rules](https://docs.stripe.com/payments/payment-method-rules)
- [invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/overview)
- [cards](https://docs.stripe.com/payments/cards)
- [wallets](https://docs.stripe.com/payments/wallets)
- [Payment methods](https://dashboard.stripe.com/test/settings/payment_methods)
- [Install the NetSuite connector invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation)