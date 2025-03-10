# Configure the Stripe Connector for Shopware 6

## Learn how to configure the Stripe Connector for Shopware 6.

To use Stripe with [Shopware 6](https://www.shopware.com/en/), you must
[install](https://docs.stripe.com/connectors/shopware6/installation) and then
configure the Stripe connector.

## Configure the connector

Use the Shopware administration panel to configure the connector.

- In the admin panel sidebar, under **Extensions**, select **My extensions**.
- On the **Apps** tab, for the Stripe connector, click the overflow menu () and
select **Open extension**.
- Configure the Stripe Connector for Shopware 6:

- [Connect to Stripe to accept
payments](https://docs.stripe.com/connectors/shopware6/configuration#connect-stripe)
- [Choose your payment
form](https://docs.stripe.com/connectors/shopware6/configuration#payment-form)
- [Customize the payment
form](https://docs.stripe.com/connectors/shopware6/configuration#customize-payment-form)
- [Collect your customer’s postal
code](https://docs.stripe.com/connectors/shopware6/configuration#postal-code)
- [Choose how to capture
funds](https://docs.stripe.com/connectors/shopware6/configuration#capture-funds)

## Connect to Stripe to accept payments

Connect Shopware to your Stripe account to start accepting payments. When you
connect to a new account, you must reactivate your preferred payment methods.

- On the **Stripe Configuration** page, click **Connect with Stripe in Live
Mode**. If you want to test different app functionality without processing live
payments, use **Connect with Stripe in Test Mode**.
- Provide your business information to [create your Stripe
account](https://dashboard.stripe.com/register).
- After you create your Stripe account, log in to your [Stripe
Dashboard](https://dashboard.stripe.com/).
- In the Stripe Dashboard, do the following:

- Under **Settings** > **Payment methods**, select your Shopware account from
the **Select your platform** drop-down.
- Turn on your preferred payment methods individually or by using the **Turn on
all** button.

The payment methods you choose for your Shopware connector are separate from
your [Stripe account payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options).

## Connect multiple channels

You can use separate Stripe accounts to connect to different sales channels.

- For each channel, the **Sales Channels** tab in the Stripe configuration page
displays:- A **Connect with Stripe in Test mode** button
- A **Connect with Stripe in Live mode** button
- The corresponding Stripe account name and Stripe account ID.
- Your main account is connected by default. Uncheck the **Use default account**
checkbox and click **Connect with Stripe […]** to specify the Stripe account for
each sales channel.

## Choose your payment form

Configure the payment form that displays to your customers during checkout.
Under **Payment form settings**, you can choose from the following:

- **Integrated payment form**–The [Payment
Element](https://docs.stripe.com/payments/payment-element) is an embeddable UI
component that lets you accept 25+ payment methods with a single integration.

![Integrated payment form with Payment
Element](https://b.stripecdn.com/docs-statics-srv/assets/connector_payment_form_element.424e5b7d979120ca7615409e62bb86bc.png)

- **Redirect to Stripe**–[Stripe
Checkout](https://docs.stripe.com/payments/checkout) lets you redirect your
customers to a Stripe-hosted, customizable checkout page to finalize payment.

![Stripe-hosted checkout
page](https://b.stripecdn.com/docs-statics-srv/assets/connector_payment_form_checkout.9846147c723ca1610638c755de28ebc9.png)

## Customize the payment form

You can configure the appearance of the integrated payment form in the following
ways:

- Choose a prebuilt theme: **Stripe**, **Night**, **Flat**, or **None**.
- Position the payment form: **On top of the Shopware payment methods**, **At
the bottom of the Shopware payment methods**, or **With the Shopware payment
methods**.
- Use the [Elements Appearance
API](https://docs.stripe.com/elements/appearance-api) to customize individual
aspects of the payment form by editing
`Resources/app/storefront/src/StripePaymentsApp/stripe.appearance.js` in your
local project.

You can customize the look and feel of Checkout (**Redirect to Stripe**) in the
[Dashboard](https://docs.stripe.com/payments/checkout/customization).

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

You can specify how you want to authorize and capture funds.

- **Simultaneous authorization and capture**–The issuing bank confirms that the
cardholder can pay, and then transfers the funds automatically after
confirmation.
- **Separate authorization and capture**–The authorization occurs first, and the
capture occurs later. To capture funds, change the order’s payment status from
`Authorized` to `Paid` or `Partially paid` in the Shopware administration panel.

## See also

- [Overview](https://docs.stripe.com/connectors/shopware6)
- [Install the
connector](https://docs.stripe.com/connectors/shopware6/installation)

## Links

- [Shopware 6](https://www.shopware.com/en/)
- [install](https://docs.stripe.com/connectors/shopware6/installation)
- [Connect to Stripe to accept
payments](https://docs.stripe.com/connectors/shopware6/configuration#connect-stripe)
- [Choose your payment
form](https://docs.stripe.com/connectors/shopware6/configuration#payment-form)
- [Customize the payment
form](https://docs.stripe.com/connectors/shopware6/configuration#customize-payment-form)
- [Collect your customer’s postal
code](https://docs.stripe.com/connectors/shopware6/configuration#postal-code)
- [Choose how to capture
funds](https://docs.stripe.com/connectors/shopware6/configuration#capture-funds)
- [create your Stripe account](https://dashboard.stripe.com/register)
- [Stripe Dashboard](https://dashboard.stripe.com/)
- [Stripe account payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Elements Appearance API](https://docs.stripe.com/elements/appearance-api)
- [Dashboard](https://docs.stripe.com/payments/checkout/customization)
- [Overview](https://docs.stripe.com/connectors/shopware6)