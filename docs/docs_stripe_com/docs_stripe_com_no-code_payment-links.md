# Create Payment Links

## Quickly accept payments for goods, services, subscriptions, tips, or donations.

[Payment Links](https://docs.stripe.com/payment-links) are a simple way for
customers to pay you when you sell online. Create one link that you can share
with everyone.

## Create a payment link

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

## Share payment links

Use the Dashboard to copy your payment link, and share it online. Click the copy
icon next to an existing link on the [Payment
Links](https://dashboard.stripe.com/payment-links) page, or go to the payment
link’s details page. You can share your payment link multiple times and anywhere
online, including:

- Emails
- Text messages
- Social media platforms

### Generate a QR code

You can create a QR code for a payment link in the Dashboard. Choose an existing
link from the **Payment Links** page, or [create a new
link](https://dashboard.stripe.com/payment-links/create) and then click **QR
code**. or download a PNG image of the QR code.

The QR code doesn’t expire. If you deactivate the underlying payment link, the
QR code redirects to an expiration page.

### Embed a button on your site

Turn your payment link into an embeddable buy button to sell a product or
subscription from your website. Select an existing link from the **Payment
Links** page or create a new link and then click **Buy button**. the code
and paste it into your website. To learn more on how to embed and customize a
button, see [Create a buy
button](https://docs.stripe.com/payment-links/buy-button).

### Deactivate a link

You can use the Dashboard to deactivate a payment link. Click the overflow menu
() to the right of the desired payment link, and then **Deactivate**. After you
deactivate a link, customers are no longer able to make a purchase using it. You
can choose to reactivate the payment link at any time. You can also use the
[API](https://docs.stripe.com/payment-links/api#deactivate-link) to deactivate a
payment link.

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

## Links

- [Payment Links](https://docs.stripe.com/payment-links)
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
- [Payment Links](https://dashboard.stripe.com/payment-links)
- [create a new link](https://dashboard.stripe.com/payment-links/create)
- [Create a buy button](https://docs.stripe.com/payment-links/buy-button)
- [API](https://docs.stripe.com/payment-links/api#deactivate-link)
- [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [supported payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [different types of payment
methods](https://stripe.com/guides/payment-methods-guide)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods/review)