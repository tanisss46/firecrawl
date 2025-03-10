# Limit customers to one subscription

## Direct customers to manage their subscription when they already have one.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
You can redirect customers that already have an active subscription to the
[customer portal](https://docs.stripe.com/billing/subscriptions/customer-portal)
or your website to manage their subscription. This redirection works with
[Checkout](https://docs.stripe.com/payments/checkout) (including the [pricing
table](https://docs.stripe.com/payments/checkout/pricing-table)) and Payment
Links.

Stripe uses either the [Customer
object](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer)
(if you provide it in the Checkout Session) or the email address to detect if a
customer already has an active subscription.

![Manage
subscription](https://b.stripecdn.com/docs-statics-srv/assets/manage-subscription.47036dfee120d3651fc3819c8b7abfbb.png)

## Direct your customers to the customer portal or your website

Customer portalYour website- [Activate the no-code customer
portal](https://docs.stripe.com/customer-management/activate-no-code-customer-portal)
to allow your customers to log in and manage their subscriptions. You need to
keep the login link for the customer portal enabled to keep this feature
enabled. Disabling the login link disables this feature, which means that
customers can create multiple subscriptions.
- Enable redirecting your customers to the customer portal in your [Checkout and
Payment Links
settings](https://dashboard.stripe.com/settings/checkout#subscriptions).

![Subscription
settings](https://b.stripecdn.com/docs-statics-srv/assets/subscription-settings.28f8c4efc7a1ca0efceeee8ebeae4786.png)

## Active subscription statuses

Active subscriptions have the following [four
statuses](https://docs.stripe.com/api/subscriptions/object#subscription_object-status):

- `Active`
- `PastDue`
- `Unpaid`
- `Paused`

## Links

- [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [pricing table](https://docs.stripe.com/payments/checkout/pricing-table)
- [Customer
object](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer)
- [Activate the no-code customer
portal](https://docs.stripe.com/customer-management/activate-no-code-customer-portal)
- [Checkout and Payment Links
settings](https://dashboard.stripe.com/settings/checkout#subscriptions)
- [four
statuses](https://docs.stripe.com/api/subscriptions/object#subscription_object-status)