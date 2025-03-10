# Add a cancellation page to the customer portal

## Allow your customers to cancel their subscriptions in the customer portal.

In the customer portal, you can let your customers cancel their subscriptions.
This option is enabled by default.

You can also enable other options to:

- [Collect a cancellation
reason](https://docs.stripe.com/customer-management/cancellation-page#collect-cancellation-reason)
- [Deflect
cancellations](https://docs.stripe.com/customer-management/cancellation-page#cancellation-deflection)

Configure these options in the [customer portal
settings](https://dashboard.stripe.com/settings/billing/portal) page of the
Stripe Dashboard.

You can also create a [customized deep link
workfow](https://docs.stripe.com/customer-management/portal-deep-links) for
cancellations.

## Collect a cancellation reason

After a customer cancels their subscription, you can collect a reason for their
cancellation. In the customer portal settings, you can select the reasons that
your customers see from the following list.

- It’s too expensive
- I need more features
- I found an alternative
- I no longer need it
- Customer service was less than expected
- Ease of use was less than expected
- Quality was less than expected
- Other reason

If a customer selects **Other reason**, they can optionally enter additional
free text.

### Finding cancellation reasons

You can find the cancellation reasons that users select in the following places:

- **Billing** > **Subscriptions** > subscription details page
- [Stripe Sigma](https://dashboard.stripe.com/sigma/queries)- Learn how to [get
started with
Sigma](https://docs.stripe.com/stripe-data/access-data-in-dashboard) and how to
[use templates to query Billing
data](https://docs.stripe.com/stripe-data/query-billing-data).
- The `subscription.updated` webhook- Learn more about [subscription webhook
events](https://docs.stripe.com/billing/subscriptions/webhooks#events).

## Deflect cancellations in the customer portal

When a customer cancels their subscription in the customer portal, you can
attempt to deflect the cancellation by offering a retention coupon.

To set up a retention coupon to deflect cancellations:

- Go to the **Settings** > **customer portal**
[page](https://dashboard.stripe.com/settings/billing/portal).
- Expand the Cancellations section.
- Select a coupon in the drop-down under **Retention Coupon**.

If you don’t have a coupon already, you can build one inline. [Learn more about
coupons](https://docs.stripe.com/billing/subscriptions/coupons).

## Links

- [customer portal
settings](https://dashboard.stripe.com/settings/billing/portal)
- [customized deep link
workfow](https://docs.stripe.com/customer-management/portal-deep-links)
- [Stripe Sigma](https://dashboard.stripe.com/sigma/queries)
- [get started with
Sigma](https://docs.stripe.com/stripe-data/access-data-in-dashboard)
- [use templates to query Billing
data](https://docs.stripe.com/stripe-data/query-billing-data)
- [subscription webhook
events](https://docs.stripe.com/billing/subscriptions/webhooks#events)
- [Learn more about
coupons](https://docs.stripe.com/billing/subscriptions/coupons)