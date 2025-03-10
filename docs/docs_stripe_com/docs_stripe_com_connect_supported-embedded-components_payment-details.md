# Payment details

## Show details of a given payment and allow users to manage disputes and perform refunds.

This component is a subset of `payments`, which provides the detail overlay of a
given payment. The UI rendered by the payment details component is equivalent to
the overlay that the `payments` component renders when the user clicks on a
payment row.

Use the `payment-details` component to invoke the payment details overlay
without the need to inline the entirety of the `payments` list in your website.
This allows you to invoke the payment detail overlay from your existing UI (for
example, your payments list) and integrate with our detail view to enable your
customers to view payment details, issue refunds, and manage disputed payments.

By default, the embedded components offer limited information for destination
charges and separate charges and transfers. They don’t provide access to
customer information, payment methods, and some charge amount details. The
[destination_on_behalf_of_charge_management](https://docs.stripe.com/connect/supported-embedded-components/payment-details#allow-your-connected-accounts-to-manage-destination-charges)
feature allows a connected account to see additional information with
destination charges, as well as perform refunds and manage disputes.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable payment
details by specifying `payment_details` in the `components` parameter. You can
turn on or off an individual feature of the payment details component by
specifying the `features` parameter under `payment_details`:

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[payment_details][enabled]"=true \
 -d "components[payment_details][features][refund_management]"=true \
 -d "components[payment_details][features][dispute_management]"=true \
 -d "components[payment_details][features][capture_payments]"=true \
-d
"components[payment_details][features][destination_on_behalf_of_charge_management]"=false
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the payment details component in the frontend:

```
// Include this element in your HTML
const paymentDetails = stripeConnectInstance.create('payment-details');
paymentDetails.setPayment('{{PAYMENT_INTENT_OR_CHARGE_ID}}');
// use setOnClose to set a callback function to close payment-details
paymentDetails.setOnClose(() => {
 paymentDetails.remove();
});
container.appendChild(paymentDetails);
```

#### Note

For [destination charges](https://docs.stripe.com/connect/destination-charges)
and [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers), the
PaymentIntent doesn’t exist on the connected account. Instead, pass the
associated charge ID that belongs to the connected account.

The payment details component shows different information and supports different
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

## Supported parameters

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescription`setPayment``string`The ID of the payment,
charge, or PaymentIntent that displays in the overlay. This should be an ID of
the payment, charge, or PaymentIntent on the connected account. If this
attribute isn’t defined, the embedded component renders nothing. To obtain this
ID, query the [charges API](https://docs.stripe.com/api/charges) or use a
payment ID that you’ve created or stored in your
integration.required`setOnClose``() => void`We send this event when the user
closes the overlay.
To enable the dismiss behavior of this component, listen to the `close` event by
calling `setOnClose`.

## Links

-
[destination_on_behalf_of_charge_management](https://docs.stripe.com/connect/supported-embedded-components/payment-details#allow-your-connected-accounts-to-manage-destination-charges)
- [furever.dev](https://furever.dev)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
-
[on_behalf_of](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-on_behalf_of)
- [participate directly in handling their
disputes](https://docs.stripe.com/connect/supported-embedded-components/payments#dispute-management-for-destination-charges)
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
- [charges API](https://docs.stripe.com/api/charges)