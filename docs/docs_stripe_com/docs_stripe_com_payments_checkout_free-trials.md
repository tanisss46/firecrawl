# Configure free trials

## Delay payments on subscriptions using free trial periods.

Stripe doesn’t set a specific limit on a free trial length. Most businesses use
shorter trials (such as 30 days), but you can set longer periods. However,
consider:

- Keeping payment methods valid for post-trial charges
- Potential impact on conversion rates with longer trials
Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
You can configure a Checkout Session to start a customer’s subscription with a
free trial by passing one of the following parameters:

-
[subscription_data.trial_period_days](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-subscription_data-trial_period_days),
the length (in days) of your free trial.
-
[subscription_data.trial_end](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-subscription_data-trial_end),
a Unix timestamp representing the end of the trial period.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=subscription \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "subscription_data[trial_period_days]"=30
```

## Free trials without collecting a payment method

By default, Checkout Sessions collect a payment method to use after the trial
ends. You can sign customers up for free trials without collecting payment
details by passing
[payment_method_collection=if_required](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_collection).

Choose whether to cancel or pause the subscription if the customer doesn’t
provide a payment method before the trial ends by passing
[trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-subscription_data-trial_settings-end_behavior-missing_payment_method).

- **Cancel subscription**-If the free trial subscription ends without a payment
method, it cancels immediately. You can create another subscription if the
customer decides to subscribe to a paid plan in the future.
- **Pause subscription**-If the free trial subscription ends without a payment
method, it pauses and doesn’t cycle until it’s resumed. When a subscription is
paused, it doesn’t generate invoices (unlike when a subscription’s [payment
collection](https://docs.stripe.com/billing/subscriptions/pause-payment) is
paused). When your customer adds their payment method after the subscription has
paused, you can resume the same subscription. The subscription can remain paused
indefinitely.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=subscription \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "subscription_data[trial_period_days]"=30 \
-d
"subscription_data[trial_settings][end_behavior][missing_payment_method]"=cancel
\
 -d payment_method_collection=if_required
```

### Collect payment details automatically

Before the trial expires, collect payment details from your customer.

Under **Manage free trial messaging** in your [Subscriptions and emails
settings](https://dashboard.stripe.com/settings/billing/automatic), you can
choose to automatically send a reminder email when a customer’s trial is about
to expire.

Next, select the **Link to a Stripe-hosted page** option so the reminder email
contains a link for the customer to add or update their payment details. We
don’t send free trial reminder emails in a sandbox. Learn more about how to [set
up free trial
reminders](https://docs.stripe.com/billing/revenue-recovery/customer-emails#trial-ending-reminders).

You must comply with card network requirements when offering trials. Learn more
about [compliance requirements for trials and
promotions](https://docs.stripe.com/billing/subscriptions/trials#compliance).

### Collect payment details in the Billing customer portal

You can also send the reminder email yourself, and redirect customers to the
Billing customer portal to add their payment details.

First, configure the [Billing customer
portal](https://docs.stripe.com/customer-management) to enable your customers to
manage their subscriptions.

Next, collect billing information from your customers:

- Listen to the `customer.subscription.trial_will_end`
[event](https://docs.stripe.com/api/events/types#event_types-customer.subscription.trial_will_end).
- If the subscription doesn’t have a [default payment
method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method),
get the customer’s email using the [Customers
API](https://docs.stripe.com/api/customers/retrieve) and send them a message
with a link to your site. It’s helpful to embed the customer ID in the email,
for example `https://example.com?...&customer={{CUSTOMER_ID}}`.
- When the customer lands on your site, create a customer portal session using
the customer ID from the previous step.
-
[Redirect](https://docs.stripe.com/customer-management/integrate-customer-portal#redirect)
the customer to the customer portal, where they can update their subscription
with payment details.

Your customers can also [resume their paused
subscription](https://docs.stripe.com/billing/subscriptions/trials#resume-a-paused-subscription)
in the customer portal by selecting **Start subscription**, then adding a
payment method. View [free trial
periods](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment)
to learn how to configure a subscription to pause or cancel when a free trial
ends without a payment method attached.

## Combining trials with usage-based billing

You can use trial periods for subscriptions with [usage-based
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing).
During the trial period, any usage accrued doesn’t count toward the total
charged to the customer at the end of the billing cycle. After the trial period
ends, usage accrues and is billed at the end of the next billing cycle.

### Trials and aggregate usage

If you use the `aggregate_usage`
[parameter](https://docs.stripe.com/api/prices/create#create_price-recurring-aggregate_usage)
and set the behavior to `last_ever`, your customer is billed for the last usage
record if it falls within the trial period, even if the usage occurred during
the trial period.

For example, if you provide file storage you might want to offer a month of free
storage, but then charge for the first month if the customer continues to store
files with your service.

## Links

-
[subscription_data.trial_period_days](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-subscription_data-trial_period_days)
-
[subscription_data.trial_end](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-subscription_data-trial_end)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
-
[payment_method_collection=if_required](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_collection)
-
[trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-subscription_data-trial_settings-end_behavior-missing_payment_method)
- [payment
collection](https://docs.stripe.com/billing/subscriptions/pause-payment)
- [Subscriptions and emails
settings](https://dashboard.stripe.com/settings/billing/automatic)
- [set up free trial
reminders](https://docs.stripe.com/billing/revenue-recovery/customer-emails#trial-ending-reminders)
- [compliance requirements for trials and
promotions](https://docs.stripe.com/billing/subscriptions/trials#compliance)
- [Billing customer portal](https://docs.stripe.com/customer-management)
-
[event](https://docs.stripe.com/api/events/types#event_types-customer.subscription.trial_will_end)
- [default payment
method](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method)
- [Customers API](https://docs.stripe.com/api/customers/retrieve)
-
[Redirect](https://docs.stripe.com/customer-management/integrate-customer-portal#redirect)
- [resume their paused
subscription](https://docs.stripe.com/billing/subscriptions/trials#resume-a-paused-subscription)
- [free trial
periods](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment)
- [usage-based
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
-
[parameter](https://docs.stripe.com/api/prices/create#create_price-recurring-aggregate_usage)