# Create subscriptions

## Set up recurring payments by offering subscriptions to your service.

Subscriptions represent what your customer is paying for and how much and how
often you’re charging them for the product. You can subscribe customers manually
through the Dashboard. You can also let them sign up through your website or a
[Payment
Link](https://docs.stripe.com/payment-links/create?pricing-model=standard).

This page shows you how to manually create and edit a subscription in your
Stripe Dashboard.

## Create a subscription

To create a subscription:

- In the Stripe Dashboard, go to the
[subscriptions](https://dashboard.stripe.com/test/subscriptions) page.
- Click **+Create subscription**.
- Find or add a customer.
- Enter the pricing and product information. You can add multiple products.
- Set the start and end date of the subscription.
- Set the starting date for the billing cycle. This defines when the next
invoice is generated. Depending on your settings, the saved payment method on
file might also be charged automatically on the billing cycle date. Learn more
about the [billing cycle
date](https://docs.stripe.com/billing/subscriptions/billing-cycle).
- (Optional) Add the default tax behavior, a coupon, a free trial, or metadata.
- (Optional) Enable [revenue
recovery](https://docs.stripe.com/billing/revenue-recovery) features in the
Dashboard, which can help you reduce and recover failed subscription payments.
You can automatically retry failed payments, build custom automations, configure
customer emails, and so on.

### Advanced options

## Edit a subscription

To edit a subscription:

- Go to the [subscriptions](https://dashboard.stripe.com/test/subscriptions)
page.
- Find the subscription you want to modify, click the overflow menu (), then
click **Update subscription**. You can also click the pencil icon () next to the
subscription name. From this menu, you can also:

- **Cancel the subscription**. In the modal that opens, select the date to
cancel the subscription—immediately, at the end of the current period, or on a
custom date. You can also select the option to refund the last payment for this
subscription and create a [credit
note](https://docs.stripe.com/invoicing/dashboard/credit-notes) for your
records.
- **Pause payment collection**. In the modal that opens, select the duration of
the pause—indefinite or ending on a custom date—and how invoices should behave
during the pause.
- **Share payment update link**. In the modal that opens, you can share a link
with the customer to update their payment details. For more information, see
[Share payment update
link](https://docs.stripe.com/billing/subscriptions/update-payment-method).
- Make your changes to the subscription.
- Click **Update subscription**.

## Delete a subscription

You can’t delete a subscription. But you can cancel it or pause payment
collection. See [editing a
subscription](https://docs.stripe.com/no-code/subscriptions#edit-susbscription)
for those details.

## Subscriptions on mobile

Use the [Stripe Dashboard mobile app](https://docs.stripe.com/dashboard/mobile)
to create or manage subscriptions on your mobile device. (Currently only
available on
[iOS](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-docs-subscriptions-nc&mt=8)
only.)

- Go to the **Customers** tab.
- Select a customer.
- Tap the plus sign (**+**) in the subscription row. Alternatively, tap the
overflow menu (), and select **Create subscription**.

You can only select existing products with a recurring price.

### Cancel a subscription from the mobile app

- Go to **Payments > Subscriptions**.
- Select an active subscription.
- Tap **Cancel Subscription** in the action bar.

Currently, you can’t pause subscriptions using the app.

## Links

- [Stripe Billing pricing](https://stripe.com/billing/pricing)
- [Payment
Link](https://docs.stripe.com/payment-links/create?pricing-model=standard)
- [subscriptions](https://dashboard.stripe.com/test/subscriptions)
- [billing cycle
date](https://docs.stripe.com/billing/subscriptions/billing-cycle)
- [revenue recovery](https://docs.stripe.com/billing/revenue-recovery)
- [credit note](https://docs.stripe.com/invoicing/dashboard/credit-notes)
- [Share payment update
link](https://docs.stripe.com/billing/subscriptions/update-payment-method)
- [Stripe Dashboard mobile app](https://docs.stripe.com/dashboard/mobile)
-
[iOS](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-docs-subscriptions-nc&mt=8)