# Allow customers to update their subscription payment methods

## Give your customers links they can use to update subscription payment details.

The Dashboard provides sharable links that allow customers to update their
payment method for an automatically billed subscription.

#### Common mistake

Shareable links to update a subscription payment method are only available in
certain scenarios, see
[restrictions](https://docs.stripe.com/billing/subscriptions/update-payment-method#restrictions)
below.

## Create and share the link

To share a link, either:

- Go to the **Subscription details** page for the customer’s subscription.
- Click the **Actions** menu.
- Select **Share payment update link**.

Or:

- Find the subscription on [Dashboard >
Customers](https://dashboard.stripe.com/customers) > **Customer details** or
[Dashboard > Billing >
Subscriptions](https://dashboard.stripe.com/subscriptions).
- Click the overflow menu ().
- Select **Share payment update link**.

A modal opens that allows you to:

- Email a link
- a link to directly share with a customer
- Deactivate all existing links for this subscription

These links allow a customer to update their payment method for only the
applicable subscription. The links don’t update other subscriptions or the
customer’s default payment method.

## Restrictions

- The subscription’s status must be `active`, `past_due`, or `trialing`. It
cannot be `unpaid`.
- The subscription’s billing must be `auto` and charge a payment method. It
cannot be `send`.
- This feature only supports updating card payment methods.
- Each link only allows a customer to update their payment details one time.
- If unused, a link expires after 30 days.

## Links

- [Dashboard > Customers](https://dashboard.stripe.com/customers)
- [Dashboard > Billing >
Subscriptions](https://dashboard.stripe.com/subscriptions)