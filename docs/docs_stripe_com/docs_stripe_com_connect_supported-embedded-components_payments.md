# Payments

## Show a list of payments with export, refund, and dispute capabilities.

Payments renders a transaction list for [direct
charges](https://docs.stripe.com/connect/direct-charges), [destination
charges](https://docs.stripe.com/connect/destination-charges), and [separate
charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) on
the connected account.

By default, the embedded components offer limited information for destination
charges and separate charges and transfers. They don’t provide access to
customer information, payment methods, and some charge amount details. The
[destination_on_behalf_of_charge_management](https://docs.stripe.com/connect/supported-embedded-components/payments#allow-your-connected-accounts-to-manage-destination-charges)
feature allows a connected account to see additional information with
destination charges, as well as perform refunds and manage disputes.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
### Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
payments embedded component by specifying `payments` in the `components`
parameter. You can turn on or off an individual feature of the payments
component by specifying the `features` parameter under `payments`:

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[payments][enabled]"=true \
 -d "components[payments][features][refund_management]"=true \
 -d "components[payments][features][dispute_management]"=true \
 -d "components[payments][features][capture_payments]"=true \
-d
"components[payments][features][destination_on_behalf_of_charge_management]"=false
```

The payments component shows different information and supports different
features for different charge types:

- For direct charges, your connected accounts can view the complete set of
information. They can also manage refunds, manage disputes, and capture payments
if you enable the corresponding features when creating an account session.
- For [destination charges](https://docs.stripe.com/connect/destination-charges)
and [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers), your
connected accounts can only see the transfer object associated with the selected
charge, which contains limited information.
- For destination charges with the
[on_behalf_of](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-on_behalf_of)
attribute, your connected accounts can view the complete set of information when
the `destination_on_behalf_of_charge_management` feature is enabled. When this
feature is turned on, you can also enable refund and disputes management by
enabling the corresponding features.

### Allow your connected accounts to manage destination charges

When you set the `destination_on_behalf_of_charge_management` feature to `true`,
your connected accounts can use the payments component to view and manage
[destination charges](https://docs.stripe.com/connect/destination-charges) that
have the
[on_behalf_of](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-on_behalf_of)
attribute. If you also turn on the `dispute_management` feature, your connected
accounts can [participate directly in handling their
disputes](https://docs.stripe.com/connect/supported-embedded-components/payments#dispute-management-for-destination-charges).

Enabling the `destination_on_behalf_of_charge_management` feature has the
following limitations:

- You can’t filter by charge status or payment methods.
- You can’t export certain data columns.

### Render the payments component

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the payments component in the front end:

```
// Include this element in your HTML
const payments = stripeConnectInstance.create('payments');
container.appendChild(payments);

// Optional: specify filters to apply on load
// payments.setDefaultFilters({
// amount: {greaterThan: 100},
// date: {before: new Date(2024, 0, 1)},
// status: ['partially_refunded', 'refund_pending', 'refunded'],
// paymentMethod: 'card',});
```

HTML +
JSReactMethodTypeDescriptionDefault`setDefaultFilters``PaymentsListDefaultFilters`On
load, show the payments matching the filter criteria. See the possible
[PaymentsListDefaultFilters
properties](https://docs.stripe.com/connect/supported-embedded-components/payments#the-object).none
#### Setting default filters

Setting default filters for the payments list is optional. If set, it applies
any valid filters and ignores invalid filters. If the
`destination_on_behalf_of_charge_management` feature is enabled, then you can’t
filter by status or payment method so it ignores these filters automatically.

You can specify any combination of payment filters of your choice using the
`PaymentsListDefaultFilters` object.

#### The `PaymentsListDefaultFilters` object

If you want to specify default filters, pass a `PaymentsListDefaultFilters`
object into the `setDefaultFilters` setter. The object has the following
properties. All properties are optional.

NameTypeDescriptionExample value`amount``{equals: number} | {greaterThan:
number} | {lessThan: number} | {between: {lowerBound: number, upperBound:
number}}`Filter by the payment amount (to the nearest hundredth).`{greaterThan:
100}``date``{before: Date} | {after: Date} | {between: {start: Date; end: Date}
`Provide `Date` objects to filter by date. It accepts any date format allowed by
a JavaScript `Date` object. Only the year, month, and day are taken into
consideration.`{before: new Date(2024, 0, 1)}`
`status`

`Status[]`

Provide one or more statuses. The valid status options are:

`'blocked' | 'canceled' | 'disputed' | 'early_fraud_warning' | 'failed' |
'incomplete' | 'partially_refunded' | 'pending' | 'refund_pending' | 'refunded'
| 'successful' | 'uncaptured'`

This filter is ignored if the `destination_on_behalf_of_charge_management`
feature is enabled.

`['disputed', 'canceled']`

`paymentMethod`

`PaymentMethod`

The full list of payment methods is available under the type enum for the
[PaymentMethod
object](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type).
To see which payment methods are available to you, check your [payment method
settings](https://dashboard.stripe.com/login?redirect=%2Fsettings%2Fpayment_methods%2Fconnected_accounts%3Fconfig_id%3Dpmc_1KldNkAppfGnVJgHI6jpKIek).

This filter is ignored if the `destination_on_behalf_of_charge_management`
feature is enabled.

`'card'`

## Dispute management for destination charges

For [destination charges](https://docs.stripe.com/connect/destination-charges),
with or without `on_behalf_of`, Stripe debits dispute amounts and fees from your
platform account.

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

When both `dispute_management` and `destination_on_behalf_of_charge_management`
are enabled, the connected accounts can update and modify dispute evidence,
counter disputes, and accept disputes for destination charges with the
`on_behalf_of` attribute set to the connected account.

## Customize the description

If you’re using the
[destination_on_behalf_of_charge_management](https://docs.stripe.com/connect/supported-embedded-components/payments#allow-your-connected-accounts-to-manage-destination-charges)
option, the payment information (including the description) shown for
destination charges with the `on_behalf_of` attribute corresponds to the
original created payment. To display a custom description within the payment
detail view for [destination
charges](https://docs.stripe.com/connect/destination-charges) and [separate
charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) when
this feature is off, follow these steps:

### Destination charges

To update the
[description](https://docs.stripe.com/api/charges/object#charge_object-description)
on a payment object that’s visible to your platform’s users, you need to use the
Stripe API. This applies to all platforms that use [destination
charges](https://docs.stripe.com/connect/destination-charges).

- Find the existing transfer object you created for an account by finding the
latest
[charge](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-charges)
created on the
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object).
- Use the charge object to find the
[transfer](https://docs.stripe.com/api/charges/object#charge_object-transfer)
object associated with the charge.
- Use the transfer object to find the
[destination_payment](https://docs.stripe.com/api/transfers/object#transfer_object-destination_payment)
ID that exists on the transfer.
- Call the [Update Charge](https://docs.stripe.com/api/charges/update) API to
update the
[description](https://docs.stripe.com/api/charges/update#update_charge-description)
on the destination payment using the `destination_payment` ID.

#### Note

The
[destination_payment](https://docs.stripe.com/api/transfers/object#transfer_object-destination_payment)
object belongs to the connected account, so you’ll need to set [the
Stripe-Account header](https://docs.stripe.com/connect/authentication) to the
connected account’s ID to make this call.

```
curl https://api.stripe.com/v1/charges/{{PAYMENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d description="My custom description"
```

This description becomes visible on the charge after you’ve written this field.

Learn more about [creating destination charges on your
platform](https://docs.stripe.com/connect/destination-charges).

### Separate charges and transfers

To update the
[description](https://docs.stripe.com/api/charges/object#charge_object-description)
on a payment object that’s visible to your platform’s users, you need to use the
Stripe API. This applies to platforms that use [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers).

- Use the transfer object to find the
[destination_payment](https://docs.stripe.com/api/transfers/object#transfer_object-destination_payment)
ID that exists on the transfer.
- Call the [Update Charge](https://docs.stripe.com/api/charges/update) API to
update the
[description](https://docs.stripe.com/api/charges/update#update_charge-description)
on the destination payment using the `destination_payment` ID found in the
previous step.

#### Note

The
[destination_payment](https://docs.stripe.com/api/transfers/object#transfer_object-destination_payment)
object belongs to the connected account, so you’ll need to set [the
Stripe-Account header](https://docs.stripe.com/connect/authentication) to the
connected account’s ID to make this call.

```
curl https://api.stripe.com/v1/charges/{{PAYMENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d description="My custom description"
```

This description becomes visible on the charge after you’ve written this field.

Learn more about [creating separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers).

## Links

- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
-
[destination_on_behalf_of_charge_management](https://docs.stripe.com/connect/supported-embedded-components/payments#allow-your-connected-accounts-to-manage-destination-charges)
- [furever.dev](https://furever.dev)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
-
[on_behalf_of](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-on_behalf_of)
- [participate directly in handling their
disputes](https://docs.stripe.com/connect/supported-embedded-components/payments#dispute-management-for-destination-charges)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [PaymentMethod
object](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
- [payment method
settings](https://dashboard.stripe.com/login?redirect=%2Fsettings%2Fpayment_methods%2Fconnected_accounts%3Fconfig_id%3Dpmc_1KldNkAppfGnVJgHI6jpKIek)
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
- [cross-border transfer
restrictions](https://docs.stripe.com/connect/account-capabilities#transfers-cross-border)
-
[description](https://docs.stripe.com/api/charges/object#charge_object-description)
-
[charge](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-charges)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [transfer](https://docs.stripe.com/api/charges/object#charge_object-transfer)
-
[destination_payment](https://docs.stripe.com/api/transfers/object#transfer_object-destination_payment)
- [Update Charge](https://docs.stripe.com/api/charges/update)
-
[description](https://docs.stripe.com/api/charges/update#update_charge-description)
- [the Stripe-Account header](https://docs.stripe.com/connect/authentication)