# Create a payment link

## Create a custom payment page without code.

Use the [Stripe Dashboard](https://dashboard.stripe.com/payment-links/create) to
create a payment link that you can
[share](https://docs.stripe.com/payment-links/share) with your customers. Stripe
redirects customers who open this link to a Stripe-hosted payment page.

## Get started

Before you begin, decide what pricing model works best for you:

- **Products or subscriptions**: Best for e-commerce or SaaS where you’re
selling products for a fixed price.
- **Customers choose what to pay**: Best for donations, tipping, or
pay-what-you-want. This pricing model currently doesn’t support recurring
payments or recurring donations. Learn more about the requirements for
[accepting tips or
donations](https://support.stripe.com/questions/requirements-for-accepting-tips-or-donations).
Products or subscriptionsCustomers choose what to pay
To let your customers choose what to pay, create a payment link by completing
the following steps:

- In the Dashboard, open the [Payment
Links](https://dashboard.stripe.com/payment-links/create/customer-chooses-pricing)
page and click **New** (or click the plus sign () and select **Payment link**).
- Fill out the payment details.
- (Optional) Set a preset amount.
- (Optional) Set minimum and maximum payment amounts. By default, the maximum
payment amount is 10,000.00 USD. [Contact support](https://support.stripe.com/)
to increase this limit.
- Click **Create link**.

## Payment Links on mobile

If you’re creating a product or subscription, use the [Stripe Dashboard iOS
app](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-mobile-app-docs-plinks&mt=8)
to create a payment link on your mobile device. In the app, go to **Payments** >
**Payment Links** to create a payment link (or click the create icon () and
select **Payment link**). The iOS app doesn’t currently support creating links
where your customers choose how much to pay.

## Configure payment methods

With [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods),
Stripe displays the most relevant and compatible payment methods to your
customers, including Apple Pay and Google Pay. Stripe enables certain payment
methods for you by default. We might also enable additional payment methods
after notifying you. Use the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods) to enable or
disable payment methods at any time. Learn more about [supported payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support)
and [different types of payment
methods](https://stripe.com/guides/payment-methods-guide).

You can review what payment methods your customers see in the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods/review) by
entering a transaction ID or setting an order amount and currency.

## See also

- [Share a payment link](https://docs.stripe.com/payment-links/share)
- [Track a payment link](https://docs.stripe.com/payment-links/url-parameters)

## Links

- [Stripe Dashboard](https://dashboard.stripe.com/payment-links/create)
- [share](https://docs.stripe.com/payment-links/share)
- [30
languages](https://support.stripe.com/questions/supported-languages-for-stripe-checkout-and-payment-links)
- [20 payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options#payment-method-product-support)
- [accepting tips or
donations](https://support.stripe.com/questions/requirements-for-accepting-tips-or-donations)
- [Payment
Links](https://dashboard.stripe.com/payment-links/create/customer-chooses-pricing)
- [Contact support](https://support.stripe.com/)
- [Stripe Dashboard iOS
app](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-mobile-app-docs-plinks&mt=8)
- [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [supported payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [different types of payment
methods](https://stripe.com/guides/payment-methods-guide)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods/review)
- [Track a payment link](https://docs.stripe.com/payment-links/url-parameters)