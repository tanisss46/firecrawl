# Configure the Stripe Connector for PrestaShop

## Learn how to configure the Stripe Connector for PrestaShop.

To use Stripe with [PrestaShop](https://www.prestashop.com/en), you must
[install](https://docs.stripe.com/connectors/prestashop/installation) and then
configure the Stripe connector.

## Configure the connector

Use the PrestaShop dashboard to configure the connector.

- Under **Modules**, select **Module Manager**.
- On the **Modules** tab, for the **Stripe payment module**, click
**Configure**.
- Configure the Stripe Connector for PrestaShop:

- [Connect to Stripe to accept
payments](https://docs.stripe.com/connectors/prestashop/configuration#connect-stripe)
- [Choose your payment
form](https://docs.stripe.com/connectors/prestashop/configuration#payment-form)
- [Customize the payment
form](https://docs.stripe.com/connectors/prestashop/configuration#customize-payment-form)
- [Collect your customer’s postal
code](https://docs.stripe.com/connectors/prestashop/configuration#postal-code)
- [Choose how to capture
funds](https://docs.stripe.com/connectors/prestashop/configuration#capture-funds)
- [Save customer payment
methods](https://docs.stripe.com/connectors/prestashop/configuration#payment-methods)
- [Choose when the order is
created](https://docs.stripe.com/connectors/prestashop/configuration#order-creation)

## Install the Stripe PrestaShop Commerce app

Use Stripe Apps to bolster security and simplify the use of distinct restricted
keys for each integration with your Stripe account. The process of installing
the Stripe App and acquiring the newly generated secret and publishable
[keys](https://docs.stripe.com/keys) is essential for your integration with the
PrestaShop Commerce connector. This approach eliminates the need to manually
create your own restricted key or use a secret key. To integrate the PrestaShop
Commerce app and reinforce your account’s security infrastructure:

- Navigate to the [Stripe App Marketplace](https://marketplace.stripe.com/),
then click [Install the PrestaShop Commerce
app](https://marketplace.stripe.com/apps/install/link/com.stripe.PrestaShop.commerce).
- Select the Stripe account where you want to install the app.
- Review and approve the app permissions, install the app in test mode or live
mode, then click **Install**.
- After you install the app, store the keys in a safe place where you won’t lose
them. To help yourself remember where you stored it, you can [leave a note on
the key in the
Dashboard](https://docs.stripe.com/keys#reveal-an-api-secret-key-live-mode).
- Use the newly generated publishable key and secret key to finish the Connector
configuration.
- To manage the app or generate new security keys after installation, navigate
to the application settings page in [test
mode](https://dashboard.stripe.com/test/settings/apps/com.stripe.PrestaShop.commerce)
or [live
mode](https://dashboard.stripe.com/settings/apps/com.stripe.PrestaShop.commerce).

## Connect to Stripe to accept payments

Connect PrestaShop to your Stripe account to start accepting payments.

- On the **Stripe Configure** page, click **Connect with Stripe**.
- Navigate to the **Stripe Configure** page in the PrestaShop Dashboard, then
paste the key from the Stripe PrestaShop app into the appropriate field.

## Choose your payment form

Configure the payment form that displays to your customers during checkout.
Under **Payment form settings**, you can choose from the following:

- **Integrated payment form**–The [Payment
Element](https://docs.stripe.com/payments/payment-element) is an embeddable UI
component that lets you accept 25+ payment methods with a single integration.

![Integrated payment form with Payment
Element](https://b.stripecdn.com/docs-statics-srv/assets/connector_payment_form_element.92e9bda6d112030dee8cd68a9af2a9eb.png)

- **Redirect to Stripe**–[Stripe
Checkout](https://docs.stripe.com/payments/checkout) lets you redirect your
customers to a Stripe-hosted, customizable checkout page to finalize payment.

![Stripe-hosted checkout
page](https://b.stripecdn.com/docs-statics-srv/assets/connector_payment_form_checkout.d40ed334159b3a72be24b0f86bbbb376.png)

## Customize the payment form

- Click the **Integrated payment form** radio button to expose the customization
options.
- Choose a [layout](https://docs.stripe.com/payments/payment-element#layout) for
the **Integrated payment form**:- **Accordion with radio buttons**
- **Accordion without radio buttons**
- **Tabs**
- Choose where to position the payment form:- **On top of the Shopware payment
methods**
- **At the bottom of the Shopware payment methods**
- **With the Shopware payment methods**
- Choose a prebuilt theme that most closely resembles your website:- **Stripe**
- **Flat**
- **Night**
- **None**

You can also [customize the look and feel of
Checkout](https://docs.stripe.com/payments/checkout/customization) (**Redirect
to Stripe**).

## Express Checkout Element

Express Checkout Element allows you to display one-click payment buttons with
Link, Apple Pay, Google Pay, PayPal, and Amazon Pay.

Stripe sorts the payment buttons dynamically based on customer location,
detected environment, and other optimized conversion factors.

On the backoffice, you can customize Express Checkout Element after you check
**Enable Express Checkout**.

- Specify where to display the one-click payment buttons:- On the **Product
Page**
- On the **Shopping Chart Page**

![Express checkout at product
level](https://b.stripecdn.com/docs-statics-srv/assets/express-checkout-product.2e598dada8a10ad85b1478d6327e3c96.png)

![Express checkout at cart
level](https://b.stripecdn.com/docs-statics-srv/assets/express-checkout-cart.5b7dbd005bbdd03688f74b9e63f0fd48.png)
- Choose different button themes and button types for Apple Pay, Google Pay and
PayPal.

Both logged in and guest users can purchase through the Express Checkout
buttons. Guest users will be able to enter their address through the payment
interface.

## Collect your customer’s postal code

You can specify whether or not to collect your customer’s postal code at
checkout using the **Never collect the postal code** field. Stripe recommends
collecting and verifying postal code information, which can help decrease the
card decline rate.

- (Recommended) **Unselect** this field if you want to require a postal code at
checkout. This applies to cards issued in Canada, the United Kingdom, or the
United States.
- **Select** this field if you don’t want to collect a postal code at checkout.

## Choose how to capture funds

You can specify how you want to authorize and capture funds using the **Enable
separate authorization and capture** field.

- **Unselect** this field to use simultaneous authorization and capture. The
issuing bank confirms that the cardholder can pay, and then transfers the funds
automatically after confirmation.
- **Select** this field to use separate authorization and capture. The
authorization occurs first, and the capture occurs later.

You can usually authorize a charge within a 7-day window.

To capture funds, do either of the following:

- In the PrestaShop dashboard, change the order’s payment status from
`Authorized` to the status you specify in the **Catch status** field. For
example, you can use `Shipped` as the catch status. The capture occurs
automatically when the status changes.

If the capture is unsuccessful, the status changes to the specified value in the
**Transition to the following order status if the authorization expires before
being captured** field.
- In the Stripe Dashboard, under **Payments**, select **All payments**. On the
**Uncaptured** tab, select the order and then click **Capture**.

## Save customer payment methods

You can let customers save their payment details for faster checkout on future
purchases by enabling the **Save payment methods at customer level** option. If
not selected, customers can still use Link to save their payment methods
globally.

## Choose when the order is created

You can specify when to create the order during the payment process using the
**Payment Flow** field:

- (Recommended) **Create the order after the payment is initiated**: Creates the
order when the customer clicks the **Place Order** button.
- (Legacy, not recommended) **Create the order after the payment is confirmed**:
Creates the order after Stripe validates the payment.

## Refunds

To refund a payment, you need the Stripe Payment ID for the order.

- In the PrestaShop dashboard, under **Orders**, select **Orders**.
- Find the order you want to refund and copy the **Payment ID** under
**Stripe**.
- To initiate a full or partial refund, do the following:

- Go to the **Refund** tab on the **Stripe payment module**.
- In the **Stripe Payment ID** field, paste the payment ID.
- Select **Full refund** or **Partial refund**. If you want to initiate a
partial refund, you must provide the amount to refund.
- Click **Request Refund**.

## See also

- [Overview](https://docs.stripe.com/connectors/prestashop)
- [Install the
connector](https://docs.stripe.com/connectors/prestashop/installation)

## Links

- [PrestaShop](https://www.prestashop.com/en)
- [install](https://docs.stripe.com/connectors/prestashop/installation)
- [Connect to Stripe to accept
payments](https://docs.stripe.com/connectors/prestashop/configuration#connect-stripe)
- [Choose your payment
form](https://docs.stripe.com/connectors/prestashop/configuration#payment-form)
- [Customize the payment
form](https://docs.stripe.com/connectors/prestashop/configuration#customize-payment-form)
- [Collect your customer’s postal
code](https://docs.stripe.com/connectors/prestashop/configuration#postal-code)
- [Choose how to capture
funds](https://docs.stripe.com/connectors/prestashop/configuration#capture-funds)
- [Save customer payment
methods](https://docs.stripe.com/connectors/prestashop/configuration#payment-methods)
- [Choose when the order is
created](https://docs.stripe.com/connectors/prestashop/configuration#order-creation)
- [keys](https://docs.stripe.com/keys)
- [Stripe App Marketplace](https://marketplace.stripe.com/)
- [Install the PrestaShop Commerce
app](https://marketplace.stripe.com/apps/install/link/com.stripe.PrestaShop.commerce)
- [leave a note on the key in the
Dashboard](https://docs.stripe.com/keys#reveal-an-api-secret-key-live-mode)
- [test
mode](https://dashboard.stripe.com/test/settings/apps/com.stripe.PrestaShop.commerce)
- [live
mode](https://dashboard.stripe.com/settings/apps/com.stripe.PrestaShop.commerce)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [layout](https://docs.stripe.com/payments/payment-element#layout)
- [customize the look and feel of
Checkout](https://docs.stripe.com/payments/checkout/customization)
- [Overview](https://docs.stripe.com/connectors/prestashop)