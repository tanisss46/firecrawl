# How Checkout works

## Learn how to use Checkout to collect payments on your website.

Checkout is a low-code payment integration that creates a customizable form for
collecting payments.

Checkout’s built-in features allow you to reduce your development time. It
supports 40+ payment methods, including
[Link](https://docs.stripe.com/payments/link), which lets your customers save
their payment method for faster checkout. You can accept payments by embedding
Checkout directly into your website, redirecting customers to a Stripe-hosted
payment page, or creating a customized checkout page with [Stripe
Elements](https://docs.stripe.com/payments/elements). Checkout supports payments
for both [one-time purchases](https://docs.stripe.com/payments/online-payments)
and [subscriptions](https://docs.stripe.com/subscriptions).

You can also customize Checkout and access additional functionality with the
[Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions) and the
Stripe Dashboard. For a complete list of features, see its [built-in and
customizable
features](https://docs.stripe.com/payments/checkout/how-checkout-works#features).

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
## Checkout lifecycle

- When customers are ready to complete their purchase, your application creates
a new Checkout Session.
- The Checkout Session provides a URL that redirects customers to a
Stripe-hosted payment page.
- Customers enter their payment details on the payment page and complete the
transaction.
- After the transaction, a [webhook](https://docs.stripe.com/webhooks) [fulfills
the order](https://docs.stripe.com/checkout/fulfillment) using the
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
event.

Client

Server

Stripe API

Stripe Checkout

Send order information

Create Checkout Session

Return Checkout Session

checkout.session.created
Redirect customer to `url` from Checkout Session

Customer completes payment

Customer returns to your application

Handle fulfillment

checkout.session.completedA diagram of a Stripe-hosted page integration's
lifecycle
## Low-code integration

Checkout requires minimal coding and is the best choice for most integrations
because of its prebuilt functionalities and customization options. You can
integrate Checkout by creating a Checkout Session and collecting customer
payment details. Collect payments by redirecting customers to a [Stripe-hosted
payment
page](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted).

[Compare
Checkout](https://docs.stripe.com/payments/online-payments#compare-features-and-availability)
to other Stripe payment options to determine the best one for you. Checkout
displays a payment form to collect customer payment information, validates
cards, handles errors, and so on.

## Built-in and customizable features

Stripe Checkout has the following built-in and customizable features:

### Built-in features

- Support for digital wallets and Link
- Responsive mobile design
- SCA-ready
- CAPTCHAs
- PCI compliance
- Card validation
- Error messaging
- [Adjustable
quantities](https://docs.stripe.com/payments/checkout/adjustable-quantity)
- [Automatic tax collection](https://docs.stripe.com/tax/checkout)
- International language support
- [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing)

### Customizable features

- [Collect taxes](https://docs.stripe.com/payments/checkout/taxes)
- [Custom branding with colors, buttons, and
font](https://docs.stripe.com/payments/checkout/customization)
- [Cross-sells](https://docs.stripe.com/payments/checkout/cross-sells)
- [Global payment
methods](https://docs.stripe.com/payments/dashboard-payment-methods)
- [Subscription upsells](https://docs.stripe.com/payments/checkout/upsells)
- [Custom domains](https://docs.stripe.com/payments/checkout/custom-domains)
(Stripe-hosted page only)
- [Email receipts](https://docs.stripe.com/receipts)
- [Apply discounts](https://docs.stripe.com/payments/checkout/discounts)
- [Custom success
page](https://docs.stripe.com/payments/checkout/custom-success-page)
- [Recover abandoned
carts](https://docs.stripe.com/payments/checkout/abandoned-carts)
- [Autofill payment details with
Link](https://docs.stripe.com/payments/checkout/customization/behavior#link)
- [Collect Tax IDs](https://docs.stripe.com/tax/checkout/tax-ids)
- [Collect shipping
information](https://docs.stripe.com/payments/collect-addresses?payment-ui=checkout)
- [Collect phone
numbers](https://docs.stripe.com/payments/checkout/phone-numbers)
- [Set the subscription billing cycle
date](https://docs.stripe.com/payments/checkout/billing-cycle)

### Custom branding

You can set fonts, colors, icons, and field styles for your Stripe-hosted
Checkout page using the [Branding
settings](https://dashboard.stripe.com/settings/branding/checkout) in the
Dashboard. For more information, see [Customize your
integration](https://docs.stripe.com/payments/checkout/customization).

### Custom domains

If you use Stripe’s [custom domain
feature](https://docs.stripe.com/payments/checkout/custom-domains), you can
serve Stripe-hosted Checkout pages on a subdomain of your custom domain. Custom
domains are a paid feature. For information, see [Pricing and
fees](https://stripe.com/pricing).

## Checkout Session

The Checkout Session is a programmatic representation of what your customers see
on the checkout page. After creating a Checkout Session, redirect your customers
to the Session’s URL to complete the purchase. When customers complete their
purchase, you can [fulfill their
orders](https://docs.stripe.com/checkout/fulfillment) by configuring an [event
destination](https://docs.stripe.com/event-destinations) to process Checkout
Session events. This code snippet from the [quickstart
guide](https://docs.stripe.com/checkout/quickstart) is an example of how to
create a Checkout Session in your application.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success"
```

### One-time and recurring payments

Allow customers to make one-time payments or subscribe to a product or service
by setting the
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
parameter in a Checkout Session.

ModePurchase typePaymentOne-time
purchases[Subscription](https://docs.stripe.com/billing/subscriptions/overview)-
Recurring purchases
- Mixed cart: Recurring purchases with one-time purchases

### Mixed cart

Create a mixed cart in Checkout that lets your customers purchase Subscription
items and one-time purchase items at the same time. To create a mixed cart, set
the `mode` parameter to `subscription` and include the Price IDs, or
`price_data`, for each line_item in the
[line_items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
array. Price IDs come from Price objects created using the Stripe Dashboard or
API and allow you to store information about your product catalog in Stripe.

You can also use
[price_data](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price_data)
to reference information from an external database where you’re hosting price
and product details without storing product catalog information on Stripe. For
more information, see [Build a subscriptions
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions).

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{RECURRING_PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "line_items[1][price]"={{ONE_TIME_PRICE_ID}} \
 -d "line_items[1][quantity]"=1 \
 -d mode=subscription \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

### Payment methods

You can view, enable, and disable different payment methods in the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) at any time.
Stripe enables certain payment methods for you by default. We might also enable
additional payment methods after notifying you. View our [complete list of
payment methods](https://docs.stripe.com/payments/payment-methods/overview).

### Save payment details and default payment methods

You can [save payment details for future
use](https://docs.stripe.com/payments/save-and-reuse) by sending an API
parameter when you create a Session. Options to save payment details include:

- **Single payment**: If your Checkout Session uses `payment` mode, set the
[payment_intent_data.setup_future_usage](https://docs.stripe.com/payments/payment-intents#future-usage)
parameter.
- **Subscription payment**: If your Checkout Session uses `subscription` mode,
Stripe saves the payment method by default.
- [Multiple saved payment
methods](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=checkout#save-payment-method-details):
If a customer has multiple payment methods saved, you can store a default
payment method to the Customer object’s
[default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
field. However, these payment methods don’t appear for return purchases in
Checkout.

### Guest customers

The `Customer` object represents a customer of your business, and it helps
tracking subscriptions and payments that belong to the same customer. Checkout
Sessions that don’t create Customers are associated with [guest
customers](https://docs.stripe.com/payments/checkout/guest-customers) instead.

## Complete a transaction

To automate business flows after a transaction has occurred, register an [event
destination](https://docs.stripe.com/event-destinations) and build a [webhook
endpoint handler](https://docs.stripe.com/webhooks/quickstart). Consider the
following events and automations to enable:

- Process the
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
event to fullfill orders when a customer completes their purchase.
- Process the
[checkout.session.expired](https://docs.stripe.com/api/events/types#event_types-checkout.session.expired)
event to return items to your inventory or send users a cart
[abandonment](https://docs.stripe.com/payments/checkout/abandoned-carts) email
when they don’t make a purchase and their cart expires.

## See also

- [Checkout quickstart](https://docs.stripe.com/checkout/quickstart)
- [Fulfill your orders](https://docs.stripe.com/checkout/fulfillment)
- [Collect taxes in Checkout](https://docs.stripe.com/payments/checkout/taxes)
- [Manage limited inventory with
Checkout](https://docs.stripe.com/payments/checkout/managing-limited-inventory)
- [Automatically convert to local currencies with Adaptive
Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing)

## Links

- [Link](https://docs.stripe.com/payments/link)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [one-time purchases](https://docs.stripe.com/payments/online-payments)
- [subscriptions](https://docs.stripe.com/subscriptions)
- [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions)
- [built-in and customizable
features](https://docs.stripe.com/payments/checkout/how-checkout-works#features)
- [webhook](https://docs.stripe.com/webhooks)
- [fulfills the order](https://docs.stripe.com/checkout/fulfillment)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [Stripe-hosted payment
page](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [Compare
Checkout](https://docs.stripe.com/payments/online-payments#compare-features-and-availability)
- [Adjustable
quantities](https://docs.stripe.com/payments/checkout/adjustable-quantity)
- [Automatic tax collection](https://docs.stripe.com/tax/checkout)
- [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing)
- [Collect taxes](https://docs.stripe.com/payments/checkout/taxes)
- [Custom branding with colors, buttons, and
font](https://docs.stripe.com/payments/checkout/customization)
- [Cross-sells](https://docs.stripe.com/payments/checkout/cross-sells)
- [Global payment
methods](https://docs.stripe.com/payments/dashboard-payment-methods)
- [Subscription upsells](https://docs.stripe.com/payments/checkout/upsells)
- [Custom domains](https://docs.stripe.com/payments/checkout/custom-domains)
- [Email receipts](https://docs.stripe.com/receipts)
- [Apply discounts](https://docs.stripe.com/payments/checkout/discounts)
- [Custom success
page](https://docs.stripe.com/payments/checkout/custom-success-page)
- [Recover abandoned
carts](https://docs.stripe.com/payments/checkout/abandoned-carts)
- [Autofill payment details with
Link](https://docs.stripe.com/payments/checkout/customization/behavior#link)
- [Collect Tax IDs](https://docs.stripe.com/tax/checkout/tax-ids)
- [Collect shipping
information](https://docs.stripe.com/payments/collect-addresses?payment-ui=checkout)
- [Collect phone
numbers](https://docs.stripe.com/payments/checkout/phone-numbers)
- [Set the subscription billing cycle
date](https://docs.stripe.com/payments/checkout/billing-cycle)
- [Branding settings](https://dashboard.stripe.com/settings/branding/checkout)
- [Pricing and fees](https://stripe.com/pricing)
- [event destination](https://docs.stripe.com/event-destinations)
- [quickstart guide](https://docs.stripe.com/checkout/quickstart)
- [https://example.com/success](https://example.com/success)
-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
- [Subscription](https://docs.stripe.com/billing/subscriptions/overview)
-
[line_items](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items)
-
[price_data](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-line_items-price_data)
- [Build a subscriptions
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [complete list of payment
methods](https://docs.stripe.com/payments/payment-methods/overview)
- [save payment details for future
use](https://docs.stripe.com/payments/save-and-reuse)
-
[payment_intent_data.setup_future_usage](https://docs.stripe.com/payments/payment-intents#future-usage)
- [Multiple saved payment
methods](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=checkout#save-payment-method-details)
-
[default_payment_method](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)
- [guest customers](https://docs.stripe.com/payments/checkout/guest-customers)
- [webhook endpoint handler](https://docs.stripe.com/webhooks/quickstart)
-
[checkout.session.expired](https://docs.stripe.com/api/events/types#event_types-checkout.session.expired)
- [Manage limited inventory with
Checkout](https://docs.stripe.com/payments/checkout/managing-limited-inventory)