# Create separate charges and transfers

## Create charges on your platform account and transfer funds to multiple connected accounts.

Create *separate charges and transfers* to transfer funds from one payment to
multiple connected accounts, or when a specific user isn’t known at the time of
the payment. The charge on your platform account is decoupled from the transfers
to your connected accounts. With this charge type:

- You create a charge on your platform’s account and also transfer funds to your
connected accounts. The payment appears as a charge on your account and there
are also transfers to connected accounts (amount determined by you), which are
withdrawn from your account balance.
- You can transfer funds to multiple connected accounts.
- Your account balance is debited for the cost of the Stripe fees, refunds, and
chargebacks.

This charge type is most optimal for marketplaces that need to split payments
between multiple parties, such as DoorDash, a restaurant delivery platform.

Stripe supports separate charges and transfers in the following regions:

AustraliaAustriaBelgiumBrazilBulgariaCanadaCroatiaCyprusCzech
RepublicDenmarkEstoniaFinlandFranceGermanyGreeceHungaryIrelandItalyJapanLatviaLiechtensteinLithuaniaLuxembourgMalaysiaMaltaMexicoNetherlandsNew
ZealandNorwayPolandPortugalRomaniaSingaporeSlovakiaSloveniaSpainSwedenSwitzerlandUnited
KingdomUnited States
In most scenarios, your platform and any connected account must be in the same
region. Attempting to transfer funds across a disallowed border returns an
error. For information about cross-region support, see [cross-border
transfers](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border).
You must only use transfers in combination with the permitted use cases for
[charges](https://docs.stripe.com/connect/charges),
[tops-ups](https://docs.stripe.com/connect/top-ups) and
[fees](https://docs.stripe.com/connect/separate-charges-and-transfers#collect-fees).

#### Note

We recommend using separate charges and transfers for connected accounts that
have access to the Express Dashboard or no dashboard access.

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
SessionClient-sideServer-side](https://docs.stripe.com/connect/separate-charges-and-transfers#create-checkout-session)
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

On your server, create a Checkout Session and redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price_data][currency]"=usd \
-d "line_items[0][price_data][product_data][name]"="Restaurant delivery service"
\
 -d "line_items[0][price_data][unit_amount]"=10000 \
 -d "line_items[0][quantity]"=1 \
 -d "payment_intent_data[transfer_group]"=ORDER100 \
 -d mode=payment \
--data-urlencode
success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"
```

- `line_items` - This attribute represents the items the customer is purchasing.
The items are displayed in the Stripe-hosted checkout page.
- `payment_intent_data[transfer_group]` - Use a unique string as the
`transfer_group` to identify objects that are associated with each other. When
Stripe automatically creates a charge for a PaymentIntent with a
`transfer_group` value, it assigns the same value to the charge’s
`transfer_group`.
- `success_url` - Stripe redirects the customer to the success URL after they
complete a payment and replaces the `{CHECKOUT_SESSION_ID}` string with the
Checkout Session ID. Use this to retrieve the Checkout Session and inspect the
status to decide what to show your customer. You can also append your own query
parameters, which persist through the redirect process. See [customize redirect
behavior with a Stripe-hosted
page](https://docs.stripe.com/payments/checkout/custom-success-page) for more
information.
CustomerPlatformConnected accountConnected account
$100 Charge

($70) Transfer

$70 Payment

($20) Transfer

$20 Payment

($3.20) Stripe fees

Stripe
$6.80 net

[Handle post-payment
eventsServer-side](https://docs.stripe.com/connect/separate-charges-and-transfers#handle-post-payment-events)
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

[Create a
TransferServer-side](https://docs.stripe.com/connect/separate-charges-and-transfers#create-transfer)
On your server, send funds from your account to a connected account by creating
a [Transfer](https://docs.stripe.com/api/transfers/create) and specifying the
`transfer_group` used.

```
curl https://api.stripe.com/v1/transfers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=7000 \
 -d currency=usd \
 -d destination={{CONNECTED_ACCOUNT_ID}} \
 -d transfer_group=ORDER100
```

Transfer and charge amounts don’t have to match. You can split a single charge
between multiple transfers or include multiple charges in a single transfer. The
following example creates an additional transfer associated with the same
`transfer_group`.

```
curl https://api.stripe.com/v1/transfers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=2000 \
 -d currency=usd \
 -d destination={{OTHER_CONNECTED_ACCOUNT_ID}} \
 -d transfer_group=ORDER100
```

### Transfer options

You can assign any value to the `transfer_group` string, but it must represent a
single business action. You can also make a transfer with neither an associated
charge nor a `transfer_group`—for example, when you must pay a provider but
there’s no associated customer payment.

#### Note

The `transfer_group` only identifies associated objects. It doesn’t affect any
standard functionality. To prevent a transfer from executing before the funds
from the associated charge are available, use the transfer’s
`source_transaction` attribute.

By default, a transfer request fails when the amount exceeds the platform’s
[available account balance](https://docs.stripe.com/connect/account-balances).
Stripe doesn’t automatically retry failed transfer requests.

You can avoid failed transfer requests for transfers that are associated with
charges. When you specify the associated charge [as the transfer’s
source_transaction](https://docs.stripe.com/connect/separate-charges-and-transfers#transfer-availability),
the transfer request automatically succeeds. However, we don’t execute the
transfer until the funds from that charge are available in the platform account.

#### Note

If you use separate charges and transfers, take that into account when planning
your [payout](https://docs.stripe.com/payouts) schedule. Automatic payouts can
interfere with transfers that don’t have a defined `source_transaction`.

[Test the
integration](https://docs.stripe.com/connect/separate-charges-and-transfers#test-the-integration)CardsWalletsBank
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
methods](https://docs.stripe.com/connect/separate-charges-and-transfers#enable-payment-methods)
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

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price_data][currency]"=usd \
-d "line_items[0][price_data][product_data][name]"="Restaurant delivery service"
\
 -d "line_items[0][price_data][unit_amount]"=10000 \
 -d "line_items[0][quantity]"=1 \
 -d "payment_intent_data[on_behalf_of]"={{CONNECTED_ACCOUNT_ID}} \
 -d "payment_intent_data[transfer_group]"=ORDER100 \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success"
```

## Collect fees

When using separate charges and transfers, the platform can collect fees on a
charge by reducing the amount it transfers to the destination accounts. For
example, consider a restaurant delivery service transaction that involves
payments to the restaurant and to the driver:

- The customer pays a 100 USD charge.
- Stripe collects a 3.20 USD fee and adds the remaining 96.80 USD to the
platform account’s pending balance.
- The platform transfers 70 USD to the restaurant’s connected account and 20 USD
to the driver’s connected account.
- A platform fee of 6.80 USD remains in the platform account.

![How a charge is divided into fees for the platform account and transfers for
the connected
accounts](https://b.stripecdn.com/docs-statics-srv/assets/charges_transfers.c54b814c7e6f88993bf259c8a53f03e8.png)

To learn about processing payments in multiple currencies with Connect, see
[working with multiple currencies](https://docs.stripe.com/connect/currencies).

## Transfer availability

The default behavior is to transfer funds from the platform account’s available
balance. Attempting a transfer that exceeds the available balance fails with an
error. To avoid this problem, when creating a transfer, tie it to an existing
[charge](https://docs.stripe.com/api/charges) by specifying the charge ID as the
`source_transaction` parameter. With a `source_transaction`, the transfer
request returns success regardless of your available balance if the related
charge has not settled yet. However, the funds don’t become available in the
destination account until the funds from the associated charge are available to
transfer from the platform account.

#### Note

If a transfer fails due to insufficient funds in your platform balance, adding
funds doesn’t automatically retry the failed action. After adding funds, you
must repeat any failed transfers or payouts.

If the source charge has a `transfer_group` value, Stripe assigns the same value
to the transfer’s `transfer_group`. If it doesn’t, then Stripe generates a
string in the format `group_` plus the associated PaymentIntent ID, for example:
`group_pi_2NHDDD589O8KAxCG0179Du2s`. It assigns that string as the
`transfer_group` for both the charge and the transfer.

#### Note

You must specify the `source_transaction` when you create a transfer. You can’t
update that attribute later.

```
curl https://api.stripe.com/v1/transfers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=7000 \
 -d currency=usd \
 -d source_transaction={{CHARGE_ID}} \
 -d destination={{CONNECTED_ACCOUNT_ID}}
```

You can get the charge ID from the
[PaymentIntent](https://docs.stripe.com/payments/payment-intents):

- Get the PaymentIntent’s [latest_charge
attribute](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge).
This attribute is the ID of the most recent charge associated with the
PaymentIntent.
- [Request a list of charges](https://docs.stripe.com/api/charges/list),
specifying the `payment_intent` in the request. This method returns full data
for all charges associated with the PaymentIntent.

When using this parameter:

- The amount of the transfer must not exceed the amount of the source charge
- You can create multiple transfers with the same `source_transaction`, as long
as the sum of the transfers doesn’t exceed the source charge
- The transfer takes on the pending status of the associated charge: if the
funds from the charge become available in N days, the payment that the
destination Stripe account receives from the transfer also becomes available in
N days
- Stripe automatically creates a `transfer_group` for you
- The currency of the balance transaction associated with the charge must match
the currency of the transfer

Asynchronous payment methods, like ACH, can fail after a subsequent transfer
request is made. For these payments, avoid using `source_transaction`. Instead,
wait until a
[charge.succeeded](https://docs.stripe.com/api/events/types#event_types-charge.succeeded)
event is triggered before transferring the funds. If you have to use
`source_transaction` with these payments, you must implement functionality to
manage payment failures.

When a payment used as a `source_transaction` fails, funds from your platform’s
account balance are transferred to the connected account to cover the payment.
To recover these funds,
[reverse](https://docs.stripe.com/connect/separate-charges-and-transfers#reverse-transfers)
the transfer associated with the failed `source_transaction`.

## Issue refunds

You can refund charges created on your platform using its secret key. However,
refunding a charge has no impact on any associated transfers. It’s up to your
platform to reconcile any amount owed back to it by reducing subsequent transfer
amounts or by [reversing
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers#reversing-transfers).

```
curl https://api.stripe.com/v1/refunds \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d charge={{CHARGE_ID}}
```

## Reverse transfers

Connect supports the ability to [reverse
transfers](https://docs.stripe.com/api#create_transfer_reversal) made to
connected accounts, either entirely or partially (by setting an `amount` value).
Use transfer reversals only for refunds or disputes related to the charge, or to
correct errors in the transfer.

```
curl https://api.stripe.com/v1/transfers/{{TRANSFER_ID}}/reversals \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=7000
```

Transfer reversals add the specified (or entire) amount back to the platform’s
available balance, reducing the connected account’s available balance
accordingly. It is only possible to reverse a transfer if the connected
account’s available balance is greater than the reversal amount or has
[connected
reserves](https://docs.stripe.com/connect/account-balances#understanding-connected-reserve-balances)
enabled.

If the transfer reversal requires a currency conversion, and the reversal amount
would result in a zero balance after the conversion, it returns an error.

Disabling refunds for a connected account won’t block the ability to process
transfer reversals.

## See also

- [Working with multiple currencies](https://docs.stripe.com/connect/currencies)
- [Statement descriptors with
Connect](https://docs.stripe.com/connect/statement-descriptors)
- [Understanding Connect account
balances](https://docs.stripe.com/connect/account-balances)

## Links

- [cross-border
transfers](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border)
- [charges](https://docs.stripe.com/connect/charges)
- [tops-ups](https://docs.stripe.com/connect/top-ups)
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
- [Transfer](https://docs.stripe.com/api/transfers/create)
- [available account balance](https://docs.stripe.com/connect/account-balances)
- [payout](https://docs.stripe.com/payouts)
- [authentication](https://docs.stripe.com/strong-customer-authentication)
- [Testing](https://docs.stripe.com/testing)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)
-
[delay_days](https://docs.stripe.com/api/accounts/create#create_account-settings-payouts-schedule-delay_days)
-
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments)
- [recipient service
agreement](https://docs.stripe.com/connect/service-agreement-types#recipient)
- [https://example.com/success](https://example.com/success)
- [working with multiple currencies](https://docs.stripe.com/connect/currencies)
- [charge](https://docs.stripe.com/api/charges)
- [latest_charge
attribute](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge)
- [Request a list of charges](https://docs.stripe.com/api/charges/list)
-
[charge.succeeded](https://docs.stripe.com/api/events/types#event_types-charge.succeeded)
-
[reverse](https://docs.stripe.com/connect/separate-charges-and-transfers#reverse-transfers)
- [reverse transfers](https://docs.stripe.com/api#create_transfer_reversal)
- [connected
reserves](https://docs.stripe.com/connect/account-balances#understanding-connected-reserve-balances)
- [Statement descriptors with
Connect](https://docs.stripe.com/connect/statement-descriptors)