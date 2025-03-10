# Create destination charges

## Create charges on your platform account, collect fees, and immediately transfer the remaining funds to your connected accounts.

Create *destination charges* when customers transact with your platform for
products or services provided by your connected accounts and you immediately
transfer funds to your connected accounts. With this charge type:

- You create a charge on your platform’s account.
- You determine whether some or all of those funds are transferred to the
connected account.
- Your account balance is debited for the cost of the Stripe fees, refunds, and
chargebacks.

This charge type is most optimal for marketplaces such as Airbnb, a home rental
marketplace or Lyft, a ridesharing app.

Destination charges are only supported if both your platform and the connected
account are in the same country. For cross-border support, you must specify the
[settlement
merchant](https://docs.stripe.com/connect/destination-charges#settlement-merchant)
to the connected account using the
[on_behalf_of](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-on_behalf_of)
parameter on the Payment Intent or other valid [cross-border
transfers](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border)
scenarios.

#### Note

We recommend using destination charges for connected accounts that have access
to the Express Dashboard or no dashboard access.

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
SessionClient-sideServer-side](https://docs.stripe.com/connect/destination-charges#create-checkout-session)
A [Checkout Session](https://docs.stripe.com/api/checkout/sessions) controls
what your customer sees in the payment form such as line items, the order amount
and currency, and acceptable payment methods. Add a checkout button to your
website that calls a server-side endpoint to create a Checkout Session.

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

DestinationOn behalf of
On your server, create a Checkout Session and redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][unit_amount]"=1000 \
 -d "line_items[0][quantity]"=1 \
 -d "payment_intent_data[application_fee_amount]"=123 \
-d "payment_intent_data[transfer_data][destination]"={{CONNECTED_ACCOUNT_ID}} \
 -d mode=payment \
--data-urlencode
success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"
```

- `payment_intent_data[transfer_data][destination]` - This parameter indicates
that this is a destination charge. A destination charge means the charge is
processed on the platform and then the funds are immediately and automatically
transferred to the connected account’s pending balance.
- `line_items` - This parameter represents the items the customer is purchasing.
The items are displayed in the embedded payment form.
- `success_url` - Stripe redirects the customer to the success URL after they
complete a payment and replaces the `{CHECKOUT_SESSION_ID}` string with the
Checkout Session ID. Use this to retrieve the Checkout Session and inspect the
status to decide what to show your customer. You can also append your own query
parameters, which persist through the redirect process. See [customize redirect
behavior with a Stripe-hosted
page](https://docs.stripe.com/payments/checkout/custom-success-page) for more
information.
- `payment_intent_data[application_fee_amount]` - This parameter specifies the
amount your platform plans to take from the transaction. The full charge amount
is immediately transferred from the platform to the connected account that’s
specified by `transfer_data[destination]` after the charge is captured. The
`application_fee_amount` is then transferred back to the platform, and the
Stripe fee is deducted from the platform’s amount.
CustomerPlatformConnected account
$10 Charge

$10 Transfer

$10 Payment

($1.23) Application fee

$8.77 net

$1.23 Application fee

($0.59) Stripe fees

Stripe
$0.64 net

When processing destination charges, Checkout uses the brand settings of your
platform account. See [customize
branding](https://docs.stripe.com/connect/destination-charges#branding) for more
information.

[Handle post-payment
eventsServer-side](https://docs.stripe.com/connect/destination-charges#handle-post-payment-events)
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
integration](https://docs.stripe.com/connect/destination-charges#test-the-integration)CardsWalletsBank
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
methods](https://docs.stripe.com/connect/destination-charges#enable-payment-methods)
## Collect fees

You can collect fees with either an
[application_fee_amount](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-application_fee_amount)
or
[transfer_data[amount]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-transfer_data-amount).

application_fee_amounttransfer_data[amount]
When creating charges with an `application_fee_amount`, the full charge amount
is immediately transferred from the platform to the `transfer_data[destination]`
account after the charge is captured. The `application_fee_amount` (capped at
the full amount of the charge) is then transferred back to the platform.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][unit_amount]"=1000 \
 -d "line_items[0][quantity]"=1 \
 -d "payment_intent_data[application_fee_amount]"=123 \
-d "payment_intent_data[transfer_data][destination]"={{CONNECTED_ACCOUNT_ID}} \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success"
```

After the application fee is collected, an [Application
Fee](https://docs.stripe.com/api/application_fees/object) object is created. You
can view a list of application fees in the
[Dashboard](https://dashboard.stripe.com/connect/application_fees), with the
[application fees](https://docs.stripe.com/api/application_fees/list), or in
[Sigma](https://docs.stripe.com/stripe-data/access-data-in-dashboard). You can
also use the `amount` property on the application fee object for itemized fee
reporting.

When using an `application_fee_amount`, know that:

- The `application_fee_amount` is capped at the total transaction amount.
- The `application_fee_amount` is always computed in the same currency as the
transaction.
- The application fee settles in the same currency as the connected account’s
settlement currency. For cross-border destination charges, this might [differ
from your platform’s settlement
currency](https://docs.stripe.com/connect/currencies#application-fees-for-destination-charges-and-converting-balances).
- Your platform pays the Stripe fee after the `application_fee_amount` is
transferred to your account.
- No additional Stripe fees are applied to the amount.
- Your platform can use built-in application fee reporting to reconcile [fees
collected](https://dashboard.stripe.com/connect/application_fees).
- In Stripe-hosted dashboards or components such as the [Payment details
component](https://docs.stripe.com/connect/supported-embedded-components/payment-details),
your connected account can view both the total amount and the application fee
amount.

### Flow of funds

With the above code, the full charge amount (10.00 USD) is added to the
connected account’s pending balance. The `application_fee_amount` (1.23 USD) is
subtracted from the charge amount and is transferred to your platform. Stripe
fees (0.59 USD) are subtracted from your platform account’s balance. The
application fee amount minus the Stripe fees (1.23 USD - 0.59 USD = 0.64 USD)
remains in your platform account’s balance.

![Flow of funds for destination
charges](https://b.stripecdn.com/docs-statics-srv/assets/destination_charge_app_fee.c9ef81298155b38f986df02d0efa9167.png)

The `application_fee_amount` becomes available on the platform account’s normal
transfer schedule, just like funds from regular Stripe charges.

## Customize branding

Your platform uses the [branding
settings](https://dashboard.stripe.com/account/branding) in the Dashboard to
customize branding on the payments page. For destination charges, Checkout uses
the branding settings of the platform account. For destination charges with
`on_behalf_of`, Checkout uses the branding settings of the connected account.

Platforms can configure the branding settings of connected accounts using the
[Update
Account](https://docs.stripe.com/api/accounts/update#update_account-settings-branding)
API:

- `icon` - Displayed next to the business name in the header of the Checkout
page.
- `logo`- Used in place of the icon and business name in the header of the
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

## Specify the settlement merchant

The settlement merchant is dependent on the
[capabilities](https://docs.stripe.com/connect/account-capabilities) set on an
account and how a charge is created. The settlement merchant determines whose
information is used to make the charge. This includes the statement descriptor
(either the platform’s or the connected account’s) that’s displayed on the
customer’s credit card or bank statement for that charge.

Specifying the settlement merchant allows you to be more explicit about who to
create charges for. For example, some platforms prefer to be the settlement
merchant because the end customer interacts directly with their platform (such
as on-demand platforms). However, some platforms have connected accounts that
interact directly with end customers instead (such as a storefront on an
e-commerce platform). In these scenarios, it might make more sense for the
connected account to be the settlement merchant.

You can set the `on_behalf_of` parameter to the ID of a connected account to
make that account the settlement merchant for the payment. When using
`on_behalf_of`:

- Charges settle in the connected account’s country and settlement currency.
- The fee structure for the connected account’s country is used.
- The connected account’s statement descriptor is displayed on the customer’s
credit card statement.
- If the connected account is in a different country than the platform, the
connected account’s address and phone number are displayed on the customer’s
credit card statement.
- The number of days that a [pending
balance](https://docs.stripe.com/connect/account-balances) is held before being
paid out depends on the
[delay_days](https://docs.stripe.com/api/accounts/create#create_account-settings-payouts-schedule-delay_days)
setting on the connected account.

If `on_behalf_of` is omitted, the platform is the business of record for the
payment.

#### Caution

The `on_behalf_of` parameter is supported only for connected accounts with a
payments capability such as
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments).
Accounts under the [recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#recipient)
can’t request `card_payments` or other payments capabilities.

## Issue refunds

If you are using the Payment Intents API, refunds should be issued against [the
most recent charge that is
created](https://docs.stripe.com/payments/payment-intents/verifying-status#identifying-charges).

Charges created on the platform account can be refunded using the platform
account’s secret key. When refunding a charge that has a
`transfer_data[destination]`, by default the destination account keeps the funds
that were transferred to it, leaving the platform account to cover the negative
balance from the refund. To pull back the funds from the connected account to
cover the refund, set the `reverse_transfer` parameter to `true` when creating
the refund:

```
curl https://api.stripe.com/v1/refunds \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d charge="{CHARGE_ID}" \
 -d reverse_transfer=true \
```

By default, the entire charge is refunded, but you can create a partial refund
by setting an `amount` value as a positive integer.

If the refund results in the entire charge being refunded, the entire transfer
is reversed. Otherwise, a proportional amount of the transfer is reversed.

### Refund application fees

When refunding a charge with an application fee, by default the platform account
keeps the funds from the application fee. To push the application fee funds back
to the connected account, set the
[refund_application_fee](https://docs.stripe.com/api/refunds/create#create_refund-refund_application_fee)
parameter to `true` when creating the refund:

```
curl https://api.stripe.com/v1/refunds \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d charge="{CHARGE_ID}" \
 -d reverse_transfer=true \
 -d refund_application_fee=true \
```

Note that if you refund the application fee for a destination charge, you must
also reverse the transfer. If the refund results in the entire charge being
refunded, the entire application fee is refunded as well. Otherwise, a
proportional amount of the application fee is refunded.

Alternatively, you can provide a `refund_application_fee` value of **false** and
refund the application fee separately [through the
API](https://docs.stripe.com/api#create_fee_refund).

### Failed refunds

If a refund fails, or you [cancel
it](https://docs.stripe.com/refunds#cancel-refund), the amount of the failed
refund returns to your platform account’s Stripe balance. Create a
[Transfer](https://docs.stripe.com/connect/separate-charges-and-transfers#create-transfer)
to move the funds to the connected account, as needed.

## Handle disputes

For destination charges, with or without `on_behalf_of`, Stripe debits dispute
amounts and fees from your platform account.

We recommend setting up [a webhook](https://docs.stripe.com/webhooks) to listen
to [dispute created
events](https://docs.stripe.com/api/events/types#event_types-charge.dispute.created).
When that happens, you can attempt to recover funds from the connected account
by reversing the transfer through the
[Dashboard](https://dashboard.stripe.com/test/transfers) or by [creating a
transfer reversal](https://docs.stripe.com/api/transfer_reversals/create).

If the connected account has a negative balance, Stripe attempts to [debit its
external
account](https://docs.stripe.com/connect/account-balances#automatically-debit-connected-accounts)
if `debit_negative_balances` is set to `true`.

If you challenge the dispute and win, you can transfer the funds that you
previously reversed back to the connected account. If your platform has an
insufficient balance, the transfer fails. Prevent insufficient balance errors by
[adding funds to your Stripe
balance](https://docs.stripe.com/get-started/account/add-funds).

#### Common mistake

Retransferring a previous reversal is subject to [cross-border transfer
restrictions](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border),
meaning you might have no means to repay your connected account. Instead, wait
to recover disputed cross-border payment transfers for destination charges with
`on_behalf_of` until after a dispute is lost.

## See also

- [Working with multiple currencies](https://docs.stripe.com/connect/currencies)
- [Statement descriptors with
Connect](https://docs.stripe.com/connect/statement-descriptors)

## Links

-
[on_behalf_of](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-on_behalf_of)
- [cross-border
transfers](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border)
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
-
[application_fee_amount](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-application_fee_amount)
-
[transfer_data[amount]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-transfer_data-amount)
- [https://example.com/success](https://example.com/success)
- [Application Fee](https://docs.stripe.com/api/application_fees/object)
- [Dashboard](https://dashboard.stripe.com/connect/application_fees)
- [application fees](https://docs.stripe.com/api/application_fees/list)
- [Sigma](https://docs.stripe.com/stripe-data/access-data-in-dashboard)
- [differ from your platform’s settlement
currency](https://docs.stripe.com/connect/currencies#application-fees-for-destination-charges-and-converting-balances)
- [Payment details
component](https://docs.stripe.com/connect/supported-embedded-components/payment-details)
- [branding settings](https://dashboard.stripe.com/account/branding)
- [Update
Account](https://docs.stripe.com/api/accounts/update#update_account-settings-branding)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)
- [pending balance](https://docs.stripe.com/connect/account-balances)
-
[delay_days](https://docs.stripe.com/api/accounts/create#create_account-settings-payouts-schedule-delay_days)
-
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments)
- [recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#recipient)
- [the most recent charge that is
created](https://docs.stripe.com/payments/payment-intents/verifying-status#identifying-charges)
-
[refund_application_fee](https://docs.stripe.com/api/refunds/create#create_refund-refund_application_fee)
- [through the API](https://docs.stripe.com/api#create_fee_refund)
- [cancel it](https://docs.stripe.com/refunds#cancel-refund)
-
[Transfer](https://docs.stripe.com/connect/separate-charges-and-transfers#create-transfer)
- [a webhook](https://docs.stripe.com/webhooks)
- [dispute created
events](https://docs.stripe.com/api/events/types#event_types-charge.dispute.created)
- [Dashboard](https://dashboard.stripe.com/test/transfers)
- [creating a transfer
reversal](https://docs.stripe.com/api/transfer_reversals/create)
- [debit its external
account](https://docs.stripe.com/connect/account-balances#automatically-debit-connected-accounts)
- [adding funds to your Stripe
balance](https://docs.stripe.com/get-started/account/add-funds)
- [Working with multiple currencies](https://docs.stripe.com/connect/currencies)
- [Statement descriptors with
Connect](https://docs.stripe.com/connect/statement-descriptors)