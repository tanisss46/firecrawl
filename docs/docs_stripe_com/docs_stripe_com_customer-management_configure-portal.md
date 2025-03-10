# Configure the customer portal

## Configure settings for the self-serve customer portal in the Dashboard.

After setting up your customer portal, configure its settings [in your
Dashboard](https://dashboard.stripe.com/test/settings/billing/portal). If you
haven’t set up your customer portal, see the [customer portal
guide](https://docs.stripe.com/customer-management).

## Configure subscription management

Configure how to manage subscriptions in your customer portal integration.

OptionDescriptionDefaultSwitch plan Let your customer switch between
subscription plans. This option is best when you have a good-better-best pricing
model.OffUpdate quantities Let your customer increase or decrease the quantity
of a subscription. This functionality is best when you have a seat-based pricing
model.OffProrate subscription updates If customers can change their plan or
quantity, optionally credit back customers for time remaining in the billing
cycle. You can apply a
[proration](https://docs.stripe.com/billing/subscriptions/prorations)
immediately or at the end of the billing period.OffManage downgrades PreviewIf
customers can change their plan or quantity, optionally schedule the change to
occur at the end of the billing period. If enabled, the customer portal
automatically creates and attaches a subscription schedule to the subscription.
When using this feature, be sure to follow [best
practices](https://docs.stripe.com/billing/subscriptions/subscription-schedules#subscription-schedule-sub-updates)
to prevent unexpected subscription overwrites.Update immediatelyUse promotion
codes If customers can change their plan or quantity, optionally allow customers
to apply [promotion
codes](https://docs.stripe.com/billing/subscriptions/coupons) when updating
subscriptions.Off
## Cancellation management

Configure your portal to allow cancellations, collect cancellation reasons, and
offer retention coupons.

OptionDescriptionDefaultCancel subscription Let your customer cancel their
subscription. After canceling, customers can still renew subscriptions until the
billing period ends.OnCancellation reason Enable the Cancel subscription option
to capture a cancellation reason when your customer cancels their subscription
on the customer portal.OnRetention coupons Offer coupons to customers before
they cancel their subscriptions. You can use coupons as part of your churn
reduction strategy.Off
## Customer billing configurations

Dictate what information your customers can manage.

OptionDescriptionDefault
**Billing information**

Capture critical customer, shipping, and tax information from your customer for
payment methods and to display on an invoice.

NameDescriptionDefault statusNameLet the customer change their name.OnEmail
addressLet the customer change their email address. Note: This functionality
isn’t available in the no-code customer portalOnBilling addressLet the customer
update their billing address.OnPhone numberLet the customer update their phone
numberOnShipping addressLet the customer update their shipping addressOffTax
IDLet the customer update their tax IDOff
On

Payment methodsLet your customer update their payment method
information.OnPromotion codesLet your customer enter promotion codes on your
customer portal instance when upgrading their plan. Go to the
[Coupons](https://docs.stripe.com/billing/subscriptions/coupons) documentation
to learn more about coupons, promotion codes, and discounts.Off
## Customize the portal

Use these configuration settings to customize your customer portal instance.

NameDescriptionRequired?HeadlineEnter an introductory text that the customer
portal displays to your customers. You can only add one headline for each
customer portal configuration. If you don’t enter anything, the customer portal
displays this default text: “{{YOUR_BUSINESS_NAME}} partners with Stripe for
simplified billing.”YesTerms of service linkEnter a link to your terms of
service. The customer portal shows this to your customers whenever they change a
subscription or add a payment method. If you don’t enter anything, the customer
portal uses the terms of service set in [public account
details](https://dashboard.stripe.com/settings/public) instead.NoDefault
Redirect linkEnter a link to redirect customers when they exit the customer
portal. If you don’t enter anything, the customer portal doesn’t display “Return
to {{YOUR_BUSINESS_NAME}}”.NoCustom domainSet a custom domain from which to
serve the customer portal. To learn more, read the [Checkout
guide](https://docs.stripe.com/payments/checkout/custom-domains) about custom
domains. You can only set one custom domain per account.NoBusiness nameSet the
name of your business in the [Public business
information](https://dashboard.stripe.com/settings/public) section of the Stripe
Dashboard. The customer portal displays this name to your customer.Yes
## Invoice history configurations

NameDescriptionDefault statusInvoice history visibleDetermine whether invoice
history is visible to customers using your customer portal.On
## Email settings configurations

#### Caution

Email settings are applied to all emails sent from Stripe to your customers.
Make sure that any changes you make are appropriate for all your Stripe use
cases.

Configure which emails Stripe sends to your customers. You can also configure a
custom domain to use for the emails. You can configure all of this in the [email
settings](https://dashboard.stripe.com/settings/emails) of the Dashboard.

## Customize branding

To customize the look and feel of the customer portal, go to the [branding
settings](https://dashboard.stripe.com/account/branding) of the Dashboard. You
can customize the following items:

- Your logo and icon
- Background color
- Button color
- Font
- Shapes

### Branding with Connect

If you maintain a platform with Connect, the customer portal uses the brand
settings of the connected account under these circumstances:

- The platform uses direct charges
- The platform uses destination charges with `on_behalf_of`

For all other connected accounts, you can configure the brand settings with the
[Accounts](https://docs.stripe.com/api/accounts/object#account_object-settings-branding)
API.

## Links

- [in your Dashboard](https://dashboard.stripe.com/test/settings/billing/portal)
- [customer portal guide](https://docs.stripe.com/customer-management)
- [proration](https://docs.stripe.com/billing/subscriptions/prorations)
- [best
practices](https://docs.stripe.com/billing/subscriptions/subscription-schedules#subscription-schedule-sub-updates)
- [promotion codes](https://docs.stripe.com/billing/subscriptions/coupons)
- [public account details](https://dashboard.stripe.com/settings/public)
- [Checkout guide](https://docs.stripe.com/payments/checkout/custom-domains)
- [email settings](https://dashboard.stripe.com/settings/emails)
- [branding settings](https://dashboard.stripe.com/account/branding)
-
[Accounts](https://docs.stripe.com/api/accounts/object#account_object-settings-branding)