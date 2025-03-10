# Integrate the customer portal with the API

## Learn how to integrate the customer portal using the Stripe API.

## Get started

With the customer portal, you can provide subscription, billing, and invoicing
management to your customers without building it yourself. After you configure
and integrate the portal, customers redirect to a co-branded dashboard where
they can manage their account based on the functionality you configured.

To integrate your application with the customer portal:

-
[Configure](https://docs.stripe.com/customer-management/integrate-customer-portal#configure)
the portal’s features and user interface (UI). You can do this in the Dashboard.
- [Implement a
redirect](https://docs.stripe.com/customer-management/integrate-customer-portal#redirect)
to integrate the portal with your application.
- [Listen to
webhooks](https://docs.stripe.com/customer-management/integrate-customer-portal#webhooks)
to receive updates to customers’ subscriptions and payment methods.
- [Go
live](https://docs.stripe.com/customer-management/integrate-customer-portal#go-live)
to use the portal in your production environment.

Or clone one of our sample projects:

- [Firebase](https://github.com/stripe-samples/firebase-subscription-payments)
- [Netlify
Identity](https://github.com/stripe-samples/netlify-stripe-subscriptions)
- [Ruby on
Rails](https://github.com/stripe-samples/developer-office-hours/tree/master/2020-06-29-customer-portal).

You can optionally
[customize](https://docs.stripe.com/customer-management/integrate-customer-portal#customize)
portal sessions to enable different features for different customers.

[Configure the
portal](https://docs.stripe.com/customer-management/integrate-customer-portal#configure)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register/).

Before you integrate the customer portal, configure its functionality and
branding in the Dashboard to define what your users can do with the portal. Its
features depend on your product and price catalog, so there are different
settings for live and test modes.

#### Common mistake

If you’re using the customer portal with Stripe Connect, make sure you configure
the customer portal for the platform, not a connected account.

If you want to create multiple portal configurations for different sets of
customers—or if you’re a [Connect](https://docs.stripe.com/connect) platform and
would like to manage configurations for your connected accounts—you can do that
by using the [API](https://docs.stripe.com/api/customer_portal/configuration):

```
curl https://api.stripe.com/v1/billing_portal/configurations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "features[invoice_history][enabled]"=true
```

### Set a product catalog

If you allow customers to upgrade, downgrade, or change the quantities of their
subscriptions, you must also set a product catalog. This includes the products
and prices that your customers can upgrade or downgrade to, as well as the
subscriptions they can update quantities on. See the
[guide](https://docs.stripe.com/products-prices/getting-started#create-product)
for more details about creating products and prices. If you’re using the
customer portal only for invoicing, you don’t need to set a product catalog.

The portal displays the following attributes of your product catalog:

- **Product name and description**—these attributes are editable in the
Dashboard and API.
- **Quantity restrictions per product**—these attributes are editable in the
Dashboard.
- **Price amount, currency, and billing interval**—these attributes are
immutable and you can only set them when you create them in the Dashboard and
API.

### Enable tax ID collection

If you use [Stripe Tax](https://docs.stripe.com/tax) to automatically collect
taxes for subscriptions or invoices, you can let customers set and update their
tax IDs in the customer portal. Stripe Billing adds the tax IDs to the
customers’ [invoices](https://docs.stripe.com/api/invoices). To enable this, go
to the [Customer portal
settings](https://dashboard.stripe.com/settings/billing/portal) and toggle on
**Tax ID**. For more information, see how customer tax IDs work with
[subscriptions](https://docs.stripe.com/billing/customer/tax-ids) and
[invoices](https://docs.stripe.com/invoicing/taxes/account-tax-ids).

Learn how to [set up Stripe Tax](https://docs.stripe.com/tax/set-up), [collect
taxes for recurring
payments](https://docs.stripe.com/billing/taxes/collect-taxes), [collect taxes
in your custom payment
flows](https://docs.stripe.com/tax/custom#existing-customer) and [set tax rates
for line items and invoices](https://docs.stripe.com/tax/invoicing).

### Preview and test

As you configure your settings, you can preview the portal by clicking
**Preview**. This launches a read-only version of the portal that lets you see
how your customers could manage their subscriptions and billing details.

After saving your settings, you can launch the portal and test it by using a
customer in test mode. Navigate to a customer in the Dashboard, click
**Actions**, and then select **Open customer portal**.

Previewing the portal as a read-only version is only available when your
Dashboard is in test mode. If you’re unable to preview and test the portal,
check your settings to make sure that your configuration is saved in test mode.
For previewing and testing to work, you also need to have edit permissions in
the Dashboard.

[Implement a redirect on your
siteClient-sideServer-side](https://docs.stripe.com/customer-management/integrate-customer-portal#redirect)
A portal session is the entry point into the customer portal. It provides a
unique, temporary link to the portal. When a customer wants to manage their
billing or invoicing, create a new portal session and redirect them to the
session’s `url`.

On your site, add a button that customers can click to enter the portal. Use a
POST request to create a portal session:

```
<form method="POST" action="/create-customer-portal-session">
 <button type="submit">Manage billing</button>
</form>
```

Next, add an endpoint that creates a portal session and redirects your
customers. Make sure to authenticate customers on your site before creating
sessions for them. To [create a
session](https://docs.stripe.com/api/customer_portal/sessions/create), you need
the customer’s ID and a `return_url`, which is required if a default return URL
isn’t set in the Dashboard configuration.

When you create a portal session, Stripe returns the `portal session object`,
which contains the session’s [short-lived
URL](https://docs.stripe.com/api/customer_portal/session?lang=curl#portal_session_object-url)
that your customers use to access the customer portal.

```
curl https://api.stripe.com/v1/billing_portal/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 --data-urlencode return_url="https://example.com/account"
```

[Listen to
webhooksServer-side](https://docs.stripe.com/customer-management/integrate-customer-portal#webhooks)
When subscriptions are upgraded, downgraded, or canceled, you need to make sure
that customers receive only the products or services they’re actively subscribed
to. Stripe sends notifications of these changes to your integration using
[webhooks](https://docs.stripe.com/webhooks). In the `Event` object, look at the
ID for the subscription or the customer to determine which customer the event
applies to.

Stripe also sends notifications if an invoice is paid to your integration using
[webhooks](https://docs.stripe.com/webhooks). In the `Event` object, look at the
ID for the invoice or the customer to determine which customer the event applies
to.

If you haven’t set up a webhook endpoint with Stripe before, you can use
Stripe’s [webhooks documentation](https://docs.stripe.com/webhooks) to get
started, and then listen for the events described below.

EventDescription

[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)

Listen to this to monitor subscription upgrades and downgrades. For upgrades,
check the `subscription.items.data[0].price` attribute in the subscription
object to find the price the customer is subscribed to. Then, grant access to
the new product. For downgrades, check the same attribute and adjust or revoke
access as needed.

When a customer uses the portal to upgrade or downgrade a subscription with a
[trial](https://docs.stripe.com/billing/subscriptions/trials), the
subscription’s trial ends immediately when switching to the new price.

[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)Listen
to this to monitor updates to the subscription quantity. When you receive this
event, check the `subscription.items.data[0].quantity` attribute to find the
quantity the customer is subscribed to. Then, grant access to the new quantity.

[customer.subscription.deleted](https://docs.stripe.com/api/events/types#event_types-customer.subscription.deleted)

Listen to this to monitor subscription cancellations. When you receive this
event, revoke the customer’s access to the product. If you configure the portal
to cancel subscriptions at the end of a billing period, listen to the
[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)
event to be notified of cancellations before they occur. If
`cancel_at_period_end` is `true`, the subscription is canceled at the end of its
billing period.

If a customer changes their mind, they can reactivate their subscription prior
to the end of the billing period. When they do this, a
[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)
event is sent. Check that `cancel_at_period_end` is `false` to confirm that they
reactivated their subscription.

[payment_method.attached](https://docs.stripe.com/api/events/types#event_types-payment_method.attached)Occurs
when a customer adds a payment
method.[payment_method.detached](https://docs.stripe.com/api/events/types#event_types-payment_method.detached)Occurs
when a customer removes a payment
method.[customer.updated](https://docs.stripe.com/api/events/types#event_types-customer.updated)Check
the `invoice_settings.default_payment_method` attribute to find the payment
method that a customer selected as the new default. If you have subscriptions
that override the customer-level default payment method, customers can remove
this override. Check the subscription’s `default_payment_method` attribute when
you receive this event to see if the override was removed. Use this webhook to
update any relevant information in your database. All updates must be treated as
billing information changes only. Don’t use the customer billing email address
as a login
credential.[customer.tax_id.created](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.created)Occurs
when customers manage their tax IDs. Stripe can validate some types of tax IDs.
Learn more in the [tax IDs
guide](https://docs.stripe.com/billing/customer/tax-ids).[customer.tax_id.deleted](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.deleted)Occurs
when customers manage their tax IDs. Stripe can validate some types of tax IDs.
Learn more in the [tax IDs
guide](https://docs.stripe.com/billing/customer/tax-ids).[customer.tax_id.updated](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.updated)Listen
to this to get validation updates about customer tax IDs. Learn more in the [tax
IDs
guide](https://docs.stripe.com/billing/customer/tax-ids).[billing_portal.configuration.created](https://docs.stripe.com/api/events/types#event_types-billing_portal.configuration.created)Occurs
when a configuration is
created.[billing_portal.configuration.updated](https://docs.stripe.com/api/events/types#event_types-billing_portal.configuration.updated)Occurs
when a configuration is
updated.[billing_portal.session.created](https://docs.stripe.com/api/events/types#event_types-billing_portal.session.created)Occurs
when a portal session is created.[Go
live](https://docs.stripe.com/customer-management/integrate-customer-portal#go-live)
Make sure to test the portal before enabling it in production. When you’re ready
to go live:

When you create a portal session, Stripe returns the `portal session` object,
which contains the session’s [short-lived
URL](https://docs.stripe.com/api/customer_portal/session?lang=curl#portal_session_object-url)
that your customers must use to access the customer portal. You can also create
one shareable link for each configuration of the portal with the
[login_page](https://docs.stripe.com/api/customer_portal/configuration#portal_configuration_object-login_page)
parameter.

- Turn off **View test data** in the Dashboard.
- [Configure](https://dashboard.stripe.com/settings/billing/portal) the portal
in live mode.
- Add your [webhooks](https://dashboard.stripe.com/webhooks) in live mode.

Stripe maintains two distinct sets of portal configurations: one for live mode
and one for test mode. To help you validate your integration, making changes in
one mode does not affect your configuration in the other.

[OptionalDeep link to specific
pages](https://docs.stripe.com/customer-management/integrate-customer-portal#deep-links)[OptionalCustomize
a portal
sessionServer-side](https://docs.stripe.com/customer-management/integrate-customer-portal#customize)[OptionalCustomize
branding](https://docs.stripe.com/customer-management/integrate-customer-portal#branding)

## Links

- [Firebase](https://github.com/stripe-samples/firebase-subscription-payments)
- [Netlify
Identity](https://github.com/stripe-samples/netlify-stripe-subscriptions)
- [Ruby on
Rails](https://github.com/stripe-samples/developer-office-hours/tree/master/2020-06-29-customer-portal)
- [Register now](https://dashboard.stripe.com/register/)
- [Connect](https://docs.stripe.com/connect)
- [API](https://docs.stripe.com/api/customer_portal/configuration)
-
[guide](https://docs.stripe.com/products-prices/getting-started#create-product)
- [Stripe Tax](https://docs.stripe.com/tax)
- [invoices](https://docs.stripe.com/api/invoices)
- [Customer portal
settings](https://dashboard.stripe.com/settings/billing/portal)
- [subscriptions](https://docs.stripe.com/billing/customer/tax-ids)
- [invoices](https://docs.stripe.com/invoicing/taxes/account-tax-ids)
- [set up Stripe Tax](https://docs.stripe.com/tax/set-up)
- [collect taxes for recurring
payments](https://docs.stripe.com/billing/taxes/collect-taxes)
- [collect taxes in your custom payment
flows](https://docs.stripe.com/tax/custom#existing-customer)
- [set tax rates for line items and
invoices](https://docs.stripe.com/tax/invoicing)
- [create a
session](https://docs.stripe.com/api/customer_portal/sessions/create)
- [short-lived
URL](https://docs.stripe.com/api/customer_portal/session?lang=curl#portal_session_object-url)
- [webhooks](https://docs.stripe.com/webhooks)
-
[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)
- [trial](https://docs.stripe.com/billing/subscriptions/trials)
-
[customer.subscription.deleted](https://docs.stripe.com/api/events/types#event_types-customer.subscription.deleted)
-
[payment_method.attached](https://docs.stripe.com/api/events/types#event_types-payment_method.attached)
-
[payment_method.detached](https://docs.stripe.com/api/events/types#event_types-payment_method.detached)
-
[customer.updated](https://docs.stripe.com/api/events/types#event_types-customer.updated)
-
[customer.tax_id.created](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.created)
-
[customer.tax_id.deleted](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.deleted)
-
[customer.tax_id.updated](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.updated)
-
[billing_portal.configuration.created](https://docs.stripe.com/api/events/types#event_types-billing_portal.configuration.created)
-
[billing_portal.configuration.updated](https://docs.stripe.com/api/events/types#event_types-billing_portal.configuration.updated)
-
[billing_portal.session.created](https://docs.stripe.com/api/events/types#event_types-billing_portal.session.created)
-
[login_page](https://docs.stripe.com/api/customer_portal/configuration#portal_configuration_object-login_page)
- [webhooks](https://dashboard.stripe.com/webhooks)