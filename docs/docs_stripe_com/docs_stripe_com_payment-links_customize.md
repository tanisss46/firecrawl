# Customize checkout for Payment Links

## Collect additional information, taxes, or update your branding.

When you create a payment link, you can customize the look and feel of a
checkout session for your user. You can also choose what type of customer
information to collect and save for later.

See [After a payment link
payment](https://docs.stripe.com/payment-links/post-payment) for more
information about customizing a session post-payment, such as redirecting the
customer to a branded confirmation page or emailing a receipt.

## Limit the number of times a payment link can be paid

You can limit the amount of times a payment link is paid for. This is helpful,
for example, if you have limited inventory, or only want the links to be used
once. When the payment link reaches the limit, it automatically deactivates and
customers can’t use it to make a purchase. If a customer tries to open the link
after the limit has been reached, they’re shown the default message for
deactivated links or [a message that you can
customize](https://docs.stripe.com/payment-links/customize#custom-deactivated-link-message).

A payment link is considered “paid for” when a checkout session is complete. You
can see the payments for completed checkout sessions in two different ways,
depending on the type of payment link:

- For payment links that include subscriptions (that is, any link that has a
[recurring price](https://docs.stripe.com/products-prices/pricing-models)), go
to **Billing** > **Subscriptions**.
- For all other payment links, go to the payment link’s details page, then
**Payments and analytics** > **Recent payments**.
DashboardAPI
To limit the number of payments using the Dashboard:

- [Create](https://dashboard.stripe.com/payment-links/create) or edit a payment
link.
- Select **Limit the number of payments** and enter the number of payments you
want to allow before the link deactivates.

## Set a custom message for deactivated links

If customers try to open a deactivated payment link, they’re shown a default
message. You can customize this message in the Dashboard or with the API.

DashboardAPI
You can customize the message for a deactivated link in the Dashboard in two
ways:

- When you [create](https://dashboard.stripe.com/payment-links/create) or edit a
payment link, select **Limit the number of payments**. Then select **Change
deactivation message** and add your custom message.
- When you attempt to deactivate a payment link, a modal with a prompt to change
the default deactivation message appears. Use that to update the message.

## Collect customer addresses and phone numbers

You can collect addresses and phone numbers with payment links by adding those
fields to the checkout session.

DashboardAPI
### Collect an address

To collect addresses from your customers:

- [Create](https://dashboard.stripe.com/payment-links/create) or edit a payment
link.

To edit a payment link go to its details page and click the overflow menu ().
- Select **Collect customers’ addresses** in the **Options** section.
- You can collect **Billing addresses only** or you can collect **Billing and
shipping addresses**. Choosing either makes these fields required for customers.
- If you collect shipping addresses:

- You need to select the countries you ship to. These countries appear in the
**Country** dropdown in the **Shipping Address form** in the checkout session.
- You can optionally add shipping rates.

### Collect a phone number

If you need to collect phone numbers to complete the transaction:

- [Create](https://dashboard.stripe.com/payment-links/create) or edit a payment
link.
- Select **Require customers to provide a phone number**.

You can configure Payment Links to always collect a billing address, or always
collect both a billing and a shipping address. When you collect shipping
addresses, you can define the allowed values for shipping countries, and create
one or more shipping rates to include in your link.

You can configure Payment Links to collect a phone number for shipping or
invoicing. Only collect phone numbers if you need them for the transaction. When
choosing this option, the payment page shows a required field to capture your
customer’s phone number.

## Collect business customer tax IDs

To display a customer’s tax ID and legal business name on invoices, enable tax
ID collection on your Payment Links. Learn how to [collect customer tax IDs with
Checkout](https://docs.stripe.com/tax/checkout/tax-ids).

## Collect taxes

Payment Links work with [Stripe Tax](https://stripe.com/tax) to calculate and
collect tax on your payments. Stripe Tax is a paid product that automatically
calculates the tax on your transactions without the need to define the rates and
rules.

Fees only apply after you’ve added at least one location where you’re registered
to calculate and remit tax.

To get started, [activate Stripe
Tax](https://dashboard.stripe.com/setup/tax/activate) in the Dashboard. Learn
how to use [products, prices, tax codes, and tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior) to
automatically calculate tax.

DashboardAPI
To enable automatic tax collection using the Dashboard:

- [Create](https://dashboard.stripe.com/payment-links/create) or edit a payment
link.
- Select **Collect tax automatically**.

To accurately determine tax, Stripe Tax collects the customer’s billing address
(full address for US customers).

## Collect agreement to your terms of service

You can require that your customers accept your terms of service before
completing their purchase. When your terms of service URL is set in your
account’s [Public details](https://dashboard.stripe.com/settings/public), you
have the option to require a terms of service agreement when you create a
payment link in the Dashboard. Enabling this setting requires that your
customers click a checkbox to accept your terms in their checkout page. The
checkout page also links to your Privacy policy when a URL to your Privacy
policy is set your [public
details](https://dashboard.stripe.com/settings/public).

## Add custom fields

#### Caution

Don’t use custom fields to collect personal, protected, or sensitive data, or
information restricted by law.

You can add custom fields on the payment form to collect additional information
from your customers. The information is available after the payment is complete
and is useful for fulfilling the purchase. You can add the following types of
fields.

TypeDescriptionTextCollects freeform text up to 255 characters.Numbers
onlyCollects only numerical values up to 255 digits.DropdownPresents your
customers with a list of options to select from. Payment links created through
the Dashboard support up to 10 options. You can add up to 200 options after you
create a link through the API.- Click **Add custom fields** in the **Options**
section.
- Select a type of field to add.
- Enter a label for the field.
- *(Optional)* Mark your field as required.

Labels for custom fields aren’t translated, but you can use the `locale` [URL
parameter](https://docs.stripe.com/payment-links/customize#customize-checkout-with-url-parameters)
to set the language of your payment link to match the same language as your
labels.

!

After your customer completes the payment, you can view the fields on the
payment details page in the Dashboard.

!

The custom fields are also sent in the
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
[webhook](https://docs.stripe.com/webhooks) upon payment completion.

## Automatically convert prices to local currencies

Enable [Adaptive
Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing) in the
[Stripe
Dashboard](https://dashboard.stripe.com/settings/automatic_currency_conversion)
in either test or live mode to let prices automatically convert to an
international customer’s local currency depending on their location.

Alternatively, you can set pricing manually for each currency using [manual
currency
prices](https://docs.stripe.com/payments/checkout/manual-currency-prices).

## Save payment details for future use

#### Caution

Consult with your legal counsel or compliance team regarding saving and using
payment details. For example, the European Data Protection Board issued
[guidance](https://edpb.europa.eu/system/files/2021-05/recommendations022021_on_storage_of_credit_card_data_en_1.pdf)
regarding the saving of payment details for faster future checkouts.

If you want to save the payment method information to provide returning
customers an optional 1-click payment experience in the future, we recommend
using
[Link](https://docs.stripe.com/payments/checkout/customization/behavior#link).

To save payment details for a customer, select **Save payment details for future
use** in the **Advanced options** section when you [create a Payment
Link](https://dashboard.stripe.com/test/payment-links/create).

## Apply branding

You can customize the look and feel of the payment page in the Stripe Dashboard.
Go to your [branding
settings](https://dashboard.stripe.com/account/branding/checkout) to:

- Upload a logo or icon
- Customize the payment page’s background color, button color, font, and shapes

Learn more about [custom fonts and font
compatibility](https://docs.stripe.com/payments/checkout/customization/appearance#font-compatibility).

## Use your own domain

If you have your own custom domain, you can add it in the Stripe Dashboard.
Instead of Stripe-branded payment links (`buy.stripe.com/`), you can create
links using your own subdomain (`pay.example.com`)

#### Note

Learn more about [custom
domains](https://docs.stripe.com/payments/checkout/custom-domains).

## Set store policies and contact information

You can display your return, refund, and legal policies on the payment page in
addition to your support contact information.

Go to the [Checkout and Payment Links
settings](https://dashboard.stripe.com/settings/checkout) to configure the
information you want to display.

Presenting this information can increase buyer confidence and minimize [cart
abandonment](https://docs.stripe.com/payments/checkout/abandoned-carts).

## Customize checkout with URL parameters

URL parameters allow you to add additional context to your payment page and
streamline checkout. Specify the language that appears during checkout, prefill
an email address or promotional code for your customers, track campaigns, and
streamline reconciliation.

You can configure URL parameters directly from the Stripe Dashboard, and use
them in the query string of your payment link URL. From the [payment links
page](https://dashboard.stripe.com/payment-links), click a specific payment
link, then click the dropdown menu on the **** button to add URL parameters.

Here’s an example link with prefilled email, promotional code, and locale
parameters.

```

https://buy.stripe.com/test_eVa3do41l4Ye6KkcMN?prefilled_email=jenny%40example.com&prefilled_promo_code=20off&locale=de

```

ParameterDescriptionSyntax
`prefilled_email`

Use `prefilled_email` to enter an email address on the payment page
automatically. Your end customer can still edit this field, so the email you
pass in for `prefilled_email` might not be the same email that your customer
uses to complete the payment.

`prefilled_email` must be a valid email address. Invalid values are silently
dropped and your payment page continues to work as expected.

We recommend [encoding](https://en.wikipedia.org/wiki/Percent-encoding) email
addresses that you attach as URL parameters to reduce the risk of them not being
passed through to your payment page.

`prefilled_promo_code`

Use `prefilled_promo_code` to enter a [promotion
code](https://docs.stripe.com/api/promotion_codes) on the payment page
automatically. Your customer can still edit this field, so the promotion code
you pass in for `prefilled_promo_code` might not be the same promotion code that
your customer uses to complete the payment.

You must also [enable promotion
codes](https://docs.stripe.com/payment-links/promotions) on your payment link,
or this parameter has no effect.

`prefilled_promo_code` must be composed of alphanumeric characters and can’t use
any special characters. Promotion codes are case insensitive. Invalid values are
silently dropped, and your payment page continues to work as expected.

`locale`Use `locale` to display your payment link in a specific language for
your customers regardless of their location.View the complete list of all
[supported
languages](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-locale).
You can also use URL parameters to [track payment links and related
campaigns](https://docs.stripe.com/payment-links/url-parameters).

## Limit customers to one subscription

You can redirect customers that already have a subscription to the [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal) or your
website to manage their subscription. Learn more about [limiting customers to
one
subscription](https://docs.stripe.com/payments/checkout/limit-subscriptions).

## Support free trials without collecting payment method details

For Payment Links that you create with a product that includes a free trial, you
can allow customers to sign up for a subscription without providing their
payment method details.

DashboardAPI
To configure trials without payment methods for Payment Links in the Dashboard:

- When you [create](https://dashboard.stripe.com/payment-links/create) or edit a
payment link with a subscription product, select **Include a free trial**. Then
select **Let customers start trial without payment method**.
- Set [subscription email
reminders](https://docs.stripe.com/payments/checkout/free-trials#collect-payment)
to make sure that Stripe prompts your customer to add their payment information
before the trial ends. Otherwise, Stripe pauses the trial.

## Links

- [After a payment link
payment](https://docs.stripe.com/payment-links/post-payment)
- [recurring price](https://docs.stripe.com/products-prices/pricing-models)
- [Create](https://dashboard.stripe.com/payment-links/create)
- [collect customer tax IDs with
Checkout](https://docs.stripe.com/tax/checkout/tax-ids)
- [Stripe Tax](https://stripe.com/tax)
- [activate Stripe Tax](https://dashboard.stripe.com/setup/tax/activate)
- [products, prices, tax codes, and tax
behavior](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
- [Public details](https://dashboard.stripe.com/settings/public)
- [URL
parameter](https://docs.stripe.com/payment-links/customize#customize-checkout-with-url-parameters)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [webhook](https://docs.stripe.com/webhooks)
- [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing)
- [Stripe
Dashboard](https://dashboard.stripe.com/settings/automatic_currency_conversion)
- [manual currency
prices](https://docs.stripe.com/payments/checkout/manual-currency-prices)
-
[guidance](https://edpb.europa.eu/system/files/2021-05/recommendations022021_on_storage_of_credit_card_data_en_1.pdf)
- [Link](https://docs.stripe.com/payments/checkout/customization/behavior#link)
- [create a Payment
Link](https://dashboard.stripe.com/test/payment-links/create)
- [branding settings](https://dashboard.stripe.com/account/branding/checkout)
- [custom fonts and font
compatibility](https://docs.stripe.com/payments/checkout/customization/appearance#font-compatibility)
- [custom domains](https://docs.stripe.com/payments/checkout/custom-domains)
- [Checkout and Payment Links
settings](https://dashboard.stripe.com/settings/checkout)
- [cart abandonment](https://docs.stripe.com/payments/checkout/abandoned-carts)
- [payment links page](https://dashboard.stripe.com/payment-links)
- [encoding](https://en.wikipedia.org/wiki/Percent-encoding)
- [promotion code](https://docs.stripe.com/api/promotion_codes)
- [enable promotion codes](https://docs.stripe.com/payment-links/promotions)
- [supported
languages](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-locale)
- [track payment links and related
campaigns](https://docs.stripe.com/payment-links/url-parameters)
- [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal)
- [limiting customers to one
subscription](https://docs.stripe.com/payments/checkout/limit-subscriptions)
- [subscription email
reminders](https://docs.stripe.com/payments/checkout/free-trials#collect-payment)