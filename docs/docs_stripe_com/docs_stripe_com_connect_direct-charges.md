# Create direct charges

## Create charges directly on the connected account and collect fees.

Create *direct charges* when customers transact directly with a connected
account, often unaware of your platform’s existence. With direct charges:

- The payment appears as a charge on the connected account, not your platform’s
account.
- The connected account’s balance increases with every charge.
- Your account balance increases with application fees from every charge.

This charge type is best suited for platforms providing software as a service.
For example, Shopify provides tools for building online storefronts, and
Thinkific enables educators to sell online courses.

#### Note

We recommend using direct charges for connected accounts that have access to the
full Stripe Dashboard.

WebiOSAndroidReact NativeStripe-hosted pageEmbedded formCustom flow
Redirect to a Stripe-hosted payment page using [Stripe
Checkout](https://docs.stripe.com/payments/checkout). See how this integration
[compares to Stripe’s other integration
types](https://docs.stripe.com/payments/online-payments#compare-features-and-availability).

### Integration effort

Low code
### Integration type

Redirect to Stripe-hosted payment page

### UI customization

Limited customization
[Try it out](https://checkout.stripe.dev/)

First, [register](https://dashboard.stripe.com/register) for a Stripe account.

Use our official libraries to access the Stripe API from your application:

```
# Available as a gem
sudo gem install stripe
```

```
# If you use bundler, you can add this line to your Gemfile
gem 'stripe'
```

[Create a Checkout
SessionClient-sideServer-side](https://docs.stripe.com/connect/direct-charges#create-checkout-session)
A [Checkout Session](https://docs.stripe.com/api/checkout/sessions) controls
what your customer sees in the payment form such as line items, the order
amount, and currency. Add a checkout button to your website that calls a
server-side endpoint to create a Checkout Session.

```
<html>
 <head>
 <title>Checkout</title>
 </head>
 <body>
 <form action="/create-checkout-session" method="POST">
 <button type="submit">Checkout</button>
 </form>
 </body>
</html>
```

On your server, create a Checkout Session and redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][unit_amount]"=1000 \
 -d "line_items[0][quantity]"=1 \
 -d "payment_intent_data[application_fee_amount]"=123 \
 -d mode=payment \
--data-urlencode
success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"
```

- `line_items` - This attribute represents items that your customer is
purchasing and shows up in the Stripe-hosted checkout page.
- `payment_intent_data[application_fee_amount]` - This attribute specifies the
amount your platform deducts from the transaction as an application fee. After
the payment is processed on the connected account, the `application_fee_amount`
is transferred to the platform. See [collect
fees](https://docs.stripe.com/connect/direct-charges#collect-fees) for more
information.
- `success_url` - Stripe redirects the customer to the success URL after they
complete a payment and replaces the `{CHECKOUT_SESSION_ID}` string with the
Checkout Session ID. Use this to retrieve the Checkout Session and inspect the
status to decide what to show your customer. You can also append your own query
parameters, which persist through the redirect process. See [customize redirect
behavior with a Stripe-hosted
page](https://docs.stripe.com/payments/checkout/custom-success-page) for more
information.
- `Stripe-Account` - This header indicates a direct charge for your connected
account. The connected account’s
[branding](https://docs.stripe.com/connect/direct-charges#branding) is used in
Checkout, which allows their customers to feel like they’re interacting directly
with the connected account instead of your platform.

Charges that you create directly on the connected account are reported only on
that account. These charges aren’t shown in your platform’s Dashboard or
exports. Direct charges are included in reports and Sigma for connected accounts
that your platform controls. You can always retrieve this information using the
Stripe API.

[Handle post-payment
eventsServer-side](https://docs.stripe.com/connect/direct-charges#handle-post-payment-events)
Stripe sends a
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
event when the payment completes. [Use a webhook to receive these
events](https://docs.stripe.com/webhooks/quickstart) and run actions, like
sending an order confirmation email to your customer, logging the sale in a
database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On
the client, the customer could close the browser window or quit the app before
the callback executes. Some payment methods also take 2-14 days for payment
confirmation. Setting up your integration to listen for asynchronous events
enables you to accept multiple [payment
methods](https://stripe.com/payments/payment-methods-guide) with a single
integration.

Stripe recommends handling all of the following events when collecting payments
with Checkout:

EventDescriptionNext
steps[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)The
customer has successfully authorized the payment by submitting the Checkout
form.Wait for the payment to succeed or
fail.[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)The
customer’s payment succeeded.Fulfill the purchased goods or
services.[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)The
payment was declined, or failed for some other reason.Contact the customer
through email and request that they place a new order.
These events all include the [Checkout
Session](https://docs.stripe.com/api/checkout/sessions) object. After the
payment succeeds, the underlying
[PaymentIntent](https://docs.stripe.com/payments/payment-intents)
[status](https://docs.stripe.com/payments/paymentintents/lifecycle) changes from
`processing` to `succeeded` or a failure status.

[Test the
integration](https://docs.stripe.com/connect/direct-charges#test-the-integration)CardsWalletsBank
redirectsBank debitsVouchersCard numberScenarioHow to test4242424242424242The
card payment succeeds and doesn’t require authentication.Fill out the credit
card form using the credit card number with any expiration, CVC, and postal
code.4000002500003155The card payment requires
[authentication](https://docs.stripe.com/strong-customer-authentication).Fill
out the credit card form using the credit card number with any expiration, CVC,
and postal code.4000000000009995The card is declined with a decline code like
`insufficient_funds`.Fill out the credit card form using the credit card number
with any expiration, CVC, and postal code.6205500000000000004The UnionPay card
has a variable length of 13-19 digits.Fill out the credit card form using the
credit card number with any expiration, CVC, and postal code.
See [Testing](https://docs.stripe.com/testing) for additional information to
test your integration.

[OptionalEnable additional payment
methods](https://docs.stripe.com/connect/direct-charges#enable-payment-methods)
## Collect fees

Your platform can take an application fee with the following limitations:

- The value of `application_fee_amount` must be positive and less than the
amount of the charge. The application fee collected is capped at the amount of
the charge.
- There are no additional Stripe fees on the application fee itself.
- In line with Brazilian regulatory and compliance requirements, platforms based
outside of Brazil, with Brazilian connected accounts cannot collect application
fees through Stripe.
- The currency of `application_fee_amount` depends upon a few [multiple
currency](https://docs.stripe.com/connect/currencies) factors.

The resulting charge’s [balance
transaction](https://docs.stripe.com/api#balance_transaction_retrieve) includes
a detailed fee breakdown of both the Stripe and application fees. To provide a
better reporting experience, an [Application
Fee](https://docs.stripe.com/api/application_fees/object) is created after the
fee is collected. Use the `amount` property on the application fee object for
reporting. You can then access these objects with the [Application
Fees](https://docs.stripe.com/api/application_fees/list) endpoint.

Earned application fees are added to your available account balance on the same
schedule as funds from regular Stripe charges. Application fees are viewable in
the [Collected fees](https://dashboard.stripe.com/connect/application_fees)
section of the Dashboard.

#### Caution

Application fees for direct charges are created asynchronously by default. If
you expand the `application_fee` object in a charge creation request, the
application fee is created synchronously as part of that request. Only expand
the `application_fee` object if you absolutely have to, because it increases the
latency of the request.

To access the application fee objects for application fees that are created
asynchronously, listen for the
[application_fee.created](https://docs.stripe.com/api/events/types#event_types-application_fee.created)
webhook event.

### Flow of funds with fees

When you specify an application fee on a charge, the fee amount is transferred
to your platform’s Stripe account. When processing a charge directly on the
connected account, the charge amount—less the Stripe fees and application fee—is
deposited into the connected account.

For example, if you make a charge of 10 USD with a 1.23 USD application fee
(like in the previous example), 1.23 USD is transferred to your platform
account. 8.18 USD (10 USD - 0.59 USD - 1.23 USD) is netted in the connected
account (assuming standard US Stripe fees).

![Flow of funds for a charge with an application
fee](https://b.stripecdn.com/docs-statics-srv/assets/direct_charges_flow.ac943c1635c3c66d1ee5e0020c453744.png)

If you process payments in multiple currencies, read [how currencies are
handled](https://docs.stripe.com/connect/currencies) in Connect.

## Customize branding

Your platform and connected accounts can use the [Branding
settings](https://dashboard.stripe.com/account/branding) in the Dashboard to
customize branding on the payments page. For direct charges, Checkout uses the
brand settings of the connected account.

You can also use the API to
[update](https://docs.stripe.com/api/accounts/update#update_account-settings-branding)
branding settings:

- `icon` - Displayed next to the business name in the header of the Checkout
page.
- `logo` - Used in place of the icon and business name in the header of the
Checkout page.
- `primary_color` - Used as the background color on the Checkout page.
- `secondary_color` - Used as the button color on the Checkout page.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "settings[branding][icon]"={{FILE_ID}} \
 -d "settings[branding][logo]"={{FILE_ID}} \
 --data-urlencode "settings[branding][primary_color]"="#663399" \
 --data-urlencode "settings[branding][secondary_color]"="#4BB543"
```

## Issue refunds

Just as platforms can create charges on connected accounts, they can also create
refunds of charges on connected accounts. [Create a
refund](https://docs.stripe.com/api#create_refund) using your platform’s secret
key while
[authenticated](https://docs.stripe.com/connect/authentication#stripe-account-header)
as the connected account.

Application fees are not automatically refunded when issuing a refund. Your
platform must explicitly refund the application fee or the connected account—the
account on which the charge was created—loses that amount. You can refund an
application fee by passing a `refund_application_fee` value of **true** in the
refund request:

```
curl https://api.stripe.com/v1/refunds \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d charge={{CHARGE_ID}} \
 -d refund_application_fee=true
```

By default, the entire charge is refunded, but you can create a partial refund
by setting an `amount` value as a positive integer. If the refund results in the
entire charge being refunded, the entire application fee is refunded. Otherwise,
a proportional amount of the application fee is refunded. Alternatively, you can
provide a `refund_application_fee` value of **false** and [refund the
application fee](https://docs.stripe.com/api#create_fee_refund) separately.

## See also

- [Working with multiple currencies](https://docs.stripe.com/connect/currencies)
- [Statement descriptors with
Connect](https://docs.stripe.com/connect/statement-descriptors)

## Links

- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [compares to Stripe’s other integration
types](https://docs.stripe.com/payments/online-payments#compare-features-and-availability)
- [register](https://dashboard.stripe.com/register)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
-
[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})
- [customize redirect behavior with a Stripe-hosted
page](https://docs.stripe.com/payments/checkout/custom-success-page)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [Use a webhook to receive these
events](https://docs.stripe.com/webhooks/quickstart)
- [payment methods](https://stripe.com/payments/payment-methods-guide)
-
[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)
-
[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [status](https://docs.stripe.com/payments/paymentintents/lifecycle)
- [authentication](https://docs.stripe.com/strong-customer-authentication)
- [Testing](https://docs.stripe.com/testing)
- [multiple currency](https://docs.stripe.com/connect/currencies)
- [balance
transaction](https://docs.stripe.com/api#balance_transaction_retrieve)
- [Application Fee](https://docs.stripe.com/api/application_fees/object)
- [Application Fees](https://docs.stripe.com/api/application_fees/list)
- [Collected fees](https://dashboard.stripe.com/connect/application_fees)
-
[application_fee.created](https://docs.stripe.com/api/events/types#event_types-application_fee.created)
- [Branding settings](https://dashboard.stripe.com/account/branding)
-
[update](https://docs.stripe.com/api/accounts/update#update_account-settings-branding)
- [Create a refund](https://docs.stripe.com/api#create_refund)
-
[authenticated](https://docs.stripe.com/connect/authentication#stripe-account-header)
- [refund the application fee](https://docs.stripe.com/api#create_fee_refund)
- [Statement descriptors with
Connect](https://docs.stripe.com/connect/statement-descriptors)