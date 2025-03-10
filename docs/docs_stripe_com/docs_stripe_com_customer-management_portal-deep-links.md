# Deep links in the customer portal

## Design streamlined customer flows with the customer portal API.

With the [customer portal](https://docs.stripe.com/customer-management), you can
provide subscription and payment method management to your customers without
building it yourself. If you want to streamline customer actions and further
customize workflows between your own app and Stripe, you can create a customer
portal
[flow](https://docs.stripe.com/api/customer_portal/session#portal_session_object-flow).

## Customer portal flows

A *flow* is a customizable deep link into the customer portal. Portal flows
allow you to:

- Deep link directly to the page with the specified action for your customer to
complete. al components to access the rest of the customer portal are
hidden so the customer can focus on the single action.
- Customize the redirect behavior after the customer completes the
action—redirect them immediately to your own URL, to a hosted confirmation page,
or back to the portal homepage.
- Personalize the flow with unique options like prefilled promotion codes or
custom messages.

### Flow types

A flow’s
[type](https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-flow_data-type)
defines what single flow or action your customer will complete. Below are the
currently available flow types:

Flow typeDescriptionExample`payment_method_update`Use `payment_method_update` to
let your customer add a new payment method. The payment method is set as the
`customer.invoice_settings.default_payment_method`.

![Example of payment method update
flow](https://b.stripecdn.com/docs-statics-srv/assets/payment_method_update.6f92b4642ce28020952f263360c83014.png)

Payment method update flow

`subscription_cancel`

Use `subscription_cancel` to let your customer cancel a specific subscription.

You can customize whether the subscription cancels immediately or at the end of
the period by updating your portal configuration through the
[API](https://docs.stripe.com/api/customer_portal/configuration#portal_configuration_object-features-subscription_cancel-mode)
or the [Dashboard](https://dashboard.stripe.com/test/settings/billing/portal).

![Example of subscription cancel
flow](https://b.stripecdn.com/docs-statics-srv/assets/subscription_cancel.6943958d0358b97241a1f4d2703d3bfb.png)

Subscription cancel flow

`subscription_update`

Use `subscription_update` to let your customer select different update options
such as upgrading or downgrading to another plan or updating the current plan
quantity.

You can customize the available plans by updating your portal configuration
through the
[API](https://docs.stripe.com/api/customer_portal/configuration#portal_configuration_object-features-subscription_update-products)
or the [Dashboard](https://dashboard.stripe.com/test/settings/billing/portal).

![Example of subscription update
flow](https://b.stripecdn.com/docs-statics-srv/assets/subscription_update.8426206cdf98ba10d04680b782644b67.png)

Subscription update flow

`subscription_update_confirm`

Use `subscription_update_confirm` to let your customer confirm a specific update
to their subscription.

You can use this option when you have your own pricing page but want to offload
the work of displaying update details such as upcoming invoice and prorations,
handling payment failures, or handling [3D Secure
authentication](https://docs.stripe.com/payments/3d-secure).

You can also specify a coupon or promotion code to apply on the subscription
update. You could use this for promotional campaigns when you offer a discount
for switching to another plan.

![Example of subscription update confirm
flow](https://b.stripecdn.com/docs-statics-srv/assets/subscription_update_confirm.5a06b658cc8a15971fdfae54fc7708da.png)

Subscription update confirm flow

[Create a
flow](https://docs.stripe.com/customer-management/portal-deep-links#create-a-flow)
#### Note

Customer portal flows are an extension to the [customer portal
API](https://docs.stripe.com/api/customer_portal/sessions/create). First follow
the general guide to [integrate the customer portal with the
API](https://docs.stripe.com/customer-management/integrate-customer-portal)
before using this guide.

To create a flow, specify
[flow_data](https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-flow_data)
when you create a portal session.

Set the
[type](https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-flow_data-type)
of flow you want your customer to complete. Depending on the flow `type`, you
might need to pass in additional data such as a subscription ID.

Below are examples on how to set up each flow type.

Payment method updateSubscription cancelSubscription updateSubscription update
confirm
```
curl https://api.stripe.com/v1/billing_portal/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 --data-urlencode return_url="https://example.com/account/overview" \
 -d "flow_data[type]"=payment_method_update
```

The portal session `url` for the response now deep links into the flow you
created. Use that URL to redirect customers to the portal flow from your site.

[Customize after completion
behavior](https://docs.stripe.com/customer-management/portal-deep-links#customize-after-completion)
After your customer successfully completes the flow, they see a localized
confirmation page that shows the details of their completed update. You can
customize the confirmation message on this page, redirect to a URL of your
choice, or redirect them back to the customer portal homepage where their full
account details are visible.

To customize this behavior, set
[after_completion](https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-flow_data-after_completion)
on `flow_data`.

The following example lets your customer cancel their subscription, and redirect
back to your own site afterwards:

```
curl https://api.stripe.com/v1/billing_portal/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 --data-urlencode return_url="https://example.com/account/overview" \
 -d "flow_data[type]"=subscription_cancel \
 -d "flow_data[subscription_cancel][subscription]"={{SUBSCRIPTION_ID}} \
 -d "flow_data[after_completion][type]"=redirect \
--data-urlencode
"flow_data[after_completion][redirect][return_url]"="https://example.com/account/subscription_canceled"
```

#### Note

The top level `return_url` is a link back to your website that the customer can
click at any time (if they decide not to cancel, for example). The
`flow_data[after_completion][redirect][return_url]` is a link back to your
website after a customer successfully cancels their subscription.

## Links

- [customer portal](https://docs.stripe.com/customer-management)
-
[flow](https://docs.stripe.com/api/customer_portal/session#portal_session_object-flow)
-
[type](https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-flow_data-type)
-
[API](https://docs.stripe.com/api/customer_portal/configuration#portal_configuration_object-features-subscription_cancel-mode)
- [Dashboard](https://dashboard.stripe.com/test/settings/billing/portal)
-
[API](https://docs.stripe.com/api/customer_portal/configuration#portal_configuration_object-features-subscription_update-products)
- [3D Secure authentication](https://docs.stripe.com/payments/3d-secure)
- [customer portal
API](https://docs.stripe.com/api/customer_portal/sessions/create)
- [integrate the customer portal with the
API](https://docs.stripe.com/customer-management/integrate-customer-portal)
-
[flow_data](https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-flow_data)
- [https://example.com/account/overview](https://example.com/account/overview)
-
[after_completion](https://docs.stripe.com/api/customer_portal/sessions/create#create_portal_session-flow_data-after_completion)
-
[https://example.com/account/subscription_canceled](https://example.com/account/subscription_canceled)