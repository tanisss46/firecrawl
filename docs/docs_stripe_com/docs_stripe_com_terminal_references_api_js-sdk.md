# JavaScript API reference

## Use our API reference to navigate the Stripe Terminal JavaScript SDK.

## API methods

-
[StripeTerminal.create()](https://docs.stripe.com/terminal/references/api/js-sdk#stripeterminal-create)
-
[discoverReaders()](https://docs.stripe.com/terminal/references/api/js-sdk#discover-readers)
-
[connectReader()](https://docs.stripe.com/terminal/references/api/js-sdk#connect-reader)
-
[disconnectReader()](https://docs.stripe.com/terminal/references/api/js-sdk#disconnect)
-
[getConnectionStatus()](https://docs.stripe.com/terminal/references/api/js-sdk#get-connection-status)
-
[getPaymentStatus()](https://docs.stripe.com/terminal/references/api/js-sdk#get-payment-status)
-
[clearCachedCredentials()](https://docs.stripe.com/terminal/references/api/js-sdk#clear-cached-credentials)
-
[collectPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk#collect-payment-method)
-
[cancelCollectPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk#cancel-collect-payment-method)
-
[processPayment()](https://docs.stripe.com/terminal/references/api/js-sdk#process-payment)
-
[collectSetupIntentPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk#collect-setup-intent-payment-method)
-
[cancelCollectSetupIntentPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk#cancel-collect-setup-intent-payment-method)
-
[confirmSetupIntent()](https://docs.stripe.com/terminal/references/api/js-sdk#confirm-setup-intent)
-
[readReusableCard()](https://docs.stripe.com/terminal/references/api/js-sdk#read-reusable-card)
-
[cancelReadReusableCard()](https://docs.stripe.com/terminal/references/api/js-sdk#cancel-read-reusable-card)
-
[setReaderDisplay()](https://docs.stripe.com/terminal/references/api/js-sdk#set-reader-display)
-
[clearReaderDisplay()](https://docs.stripe.com/terminal/references/api/js-sdk#clear-reader-display)
-
[setSimulatorConfiguration()](https://docs.stripe.com/terminal/references/api/js-sdk#stripeterminal-setsimulatorconfig)
-
[getSimulatorConfiguration()](https://docs.stripe.com/terminal/references/api/js-sdk#stripeterminal-getsimulatorconfig)
-
[collectRefundPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk#stripeterminal-collectrefundpaymentmethod)
-
[processRefund()](https://docs.stripe.com/terminal/references/api/js-sdk#stripeterminal-processrefund)
-
[cancelCollectRefundPaymentMethod()](https://docs.stripe.com/terminal/references/api/js-sdk#stripeterminal-cancelcollectrefundpaymentmethod)
-
[collectInputs()](https://docs.stripe.com/terminal/references/api/js-sdk#collect-inputs)
-
[cancelCollectInputs()](https://docs.stripe.com/terminal/references/api/js-sdk#cancel-collect-inputs)

### StripeTerminal.create([options])

Creates an instance of `StripeTerminal` with the given options:

Option DescriptiononFetchConnectionTokenAn event handler that [fetches a
connection
token](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=js#connection-token)
from your backend.onUnexpectedReaderDisconnectAn event handler called when a
reader disconnects from your app.onConnectionStatusChange optionalAn event
handler called when the SDK’s ConnectionStatus changes.onPaymentStatusChange
optionalAn event handler called when the SDK’s PaymentStatus
changes.readerBehavior optionalAn object that sets the behavior on the reader
throughout the lifecycle of the SDK. See below for readerBehavior configuration
options.
### Reader Behavior Configuration

Today, there is only one behavior configuration option:

Behavior Description
**allowCustomerCancel**

A Boolean that determines whether the customer can cancel `collectPaymentMethod`
from the reader’s interface. Defaults to `false`.

**Note:** This property isn’t broadly available, and we’re not accepting users
at this time.

### discoverReaders([options])

Begins discovering readers with the given options:

Option Descriptionsimulated optionalA Boolean value indicating whether to
discover a [simulated
reader](https://docs.stripe.com/terminal/references/testing#simulated-reader).
If left empty, this value defaults to `false`.
**location** optional

Return only readers assigned to the given `location`. This parameter is ignored
when discovering a simulated reader.

For more information on using locations to filter discovered readers, see
[Manage locations](https://docs.stripe.com/terminal/fleet/locations-and-zones).

Returns a `Promise` that resolves to an object with the following fields:

- `discoveredReaders`: A list of discovered
[Reader](https://docs.stripe.com/api/terminal/readers/object) objects, if the
command succeeded.
- `error`: An
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors), if the
command failed.

#### Note

Before you can discover the Verifone P400 in your application, you must
[register](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet#register-reader)
the reader to your account.

### connectReader(reader, connectOptions)

Attempts to
[connect](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet#connect-reader)
to the given reader with the given options:

Option Descriptionfail_if_in_use optionalA Boolean value indicating that the
connection fails if the reader is currently connected to a Terminal SDK. If left
empty, this value defaults to `false`.
Returns a `Promise` that resolves to an object with the following fields:

- `reader`: The connected
[Reader](https://docs.stripe.com/api/terminal/readers/object), if the command
succeeded.
- `error`: An
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors), if the
command failed.

#### Note

Don’t cache the `Reader` object in your application. Connecting to a stale
`Reader` can fail if the reader’s IP address has changed.

### disconnectReader()

Disconnects from the connected reader.

### getConnectionStatus()

Returns the current connection status.

ConnectionStatus can be one of `connecting`, `connected`, or `not_connected`.

### getPaymentStatus()

Returns the reader’s payment status.

PaymentStatus can be one of `not_ready`, `ready`, `waiting_for_input`, or
`processing`.

### clearCachedCredentials()

Clears the current
[ConnectionToken](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=js#connection-token),
and any other cached credentials.

Use this method to switch accounts in your application (for example, to switch
between live and test Stripe API keys on your backend). To switch accounts,
follow these steps:

- If a reader is connected, call `disconnectReader`.
- Configure your `onFetchConnectionToken` handler to return connection tokens
for the new account.
- Call `clearCachedCredentials`.
- Reconnect to a reader. The SDK requests a new connection token from your
`onFetchConnectionToken` handler.

### collectPaymentMethod(request, options)

Begins [collecting a payment
method](https://docs.stripe.com/terminal/payments/collect-card-payment#collect-payment)
for a PaymentIntent. This method takes one required parameter, `request`:

- `request`: The `clientSecret` field from a `PaymentIntent` object created on
your backend. Learn how to [create a PaymentIntent and pass its client
secret](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements#web-create-intent).
- `options`: An object containing additional payment parameters.
Option Description
**config_override** optional

An object that allows you to specify configuration overrides per transaction.
This object defaults to null.

`skip_tipping`

- Optional, defaults to false. If true, the reader skips the tipping screen.

`tipping`

- An object that allows you to specify tipping-related options per transaction.
It’s described below.

`update_payment_intent`

- A Boolean, when paired with `payment_intent_id`, instructs the call to update
the `PaymentIntent` and return the attached `PaymentMethod` with card details.

`enable_customer_cancellation`

- Optional, defaults to false. If true, Android-based smart readers show a
cancel button.

`allow_redisplay`

- Required if `setup_future_usage` is set; otherwise, it defaults to
`unspecified`. An enum value indicating whether future checkout flows can show
this payment method to its customer.

`moto`

- Optional, defaults to false. If true, Android-based smart readers start
collection for a [mail order or telephone
order](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments)
transaction.

```
{
 update_payment_intent: boolean,
 payment_intent_id: string,
 enable_customer_cancellation: boolean,
 skip_tipping: boolean,
 tipping: object,
 allow_redisplay: string,
 moto: boolean,
}
```

The following option is available for the `tipping` object:

Option Description
**eligible_amount** optional

A number that allows you to specify the amount of a transaction that
percentage-based tips are calculated against. Set this value to 0 or higher.

If it’s equal to 0, tipping is skipped regardless of the value of
`skip_tipping`.

If it’s equal to the PaymentIntent amount, the parameter is ignored and the tip
is calculated based on the specified amount.

```
{
 eligible_amount: number,
}
```

Returns a `Promise` that resolves to an object with the following fields:

- `paymentIntent`: The updated [PaymentIntent
object](https://docs.stripe.com/api/payment_intents/object), if the command
succeeded.
- `error`: An
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors), if the
command failed.

For more information on collecting payments, see our [Collecting
Payments](https://docs.stripe.com/terminal/payments/collect-card-payment) guide.

### cancelCollectPaymentMethod()

Cancels an outstanding
[collectPaymentMethod](https://docs.stripe.com/terminal/references/api/js-sdk#collect-payment-method)
command.

Returns a `Promise` that resolves to an empty object when command has been
successfully canceled. If cancellation fails, the `Promise` resolves to an
object with an
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors)

### processPayment(paymentIntent, options)

[Processes](https://docs.stripe.com/terminal/payments/collect-card-payment#process-payment)
a payment after a payment method has been
[collected](https://docs.stripe.com/terminal/payments/collect-card-payment#collect-payment).

This method takes one required parameter, `paymentIntent`:

- `paymentIntent`: A `PaymentIntent` object obtained from a successful call to
`collectPaymentMethod`.
- `options`: An object containing additional payment parameters.
Option Description
**config_override** optional

An object that allows you to specify configuration overrides per transaction.
This object defaults to null.

`return_url`

- The URL to redirect your customer back to after they authenticate or cancel
their payment on the payment method’s app or site. We only use this parameter
for redirect-based payment methods. The default is null.

```
{
 return_url: string,
}
```

Returns a `Promise` that resolves to an object with the following fields:

- `paymentIntent`: The confirmed [PaymentIntent
object](https://docs.stripe.com/api/payment_intents/object), if the command
succeeded.
- `error`: An
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors), if the
command failed. For more information, see [Handling processing
failures](https://docs.stripe.com/terminal/payments/collect-card-payment#handling-failures).

### collectSetupIntentPaymentMethod(clientSecret, allowRedisplay, config)

Begins [collecting a payment method for online
reuse](https://docs.stripe.com/terminal/features/saving-cards/overview) for a
[SetupIntent](https://docs.stripe.com/api/setup_intents/object).

The method takes two required parameters:

- `clientSecret`: The `clientSecret` field from a `SetupIntent` object created
on your backend.
- `allowRedisplay`: An enum value indicating whether future checkout flows can
show this payment method to its customer.
- `config`: an optional object containing collection configuration.
Option Description
**enable_customer_cancellation**

Optional, defaults to false.

If true, Android-based smart readers show a cancel button.

**moto**

Optional, defaults to false.

If true, Android-based smart readers start saving a [mail order or telephone
order](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly)
card.

Returns a `Promise` that resolves to an object with the following fields:

- `setupIntent`: The updated [SetupIntent
object](https://docs.stripe.com/api/setup_intents/object), if the command
succeeded.
- `error`: An
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors), if the
command failed.

For more information on saving cards, see our [Saving cards for online
payments](https://docs.stripe.com/terminal/features/saving-cards/overview)
guide.

### cancelCollectSetupIntentPaymentMethod()

Cancels an outstanding
[collectSetupIntentPaymentMethod](https://docs.stripe.com/terminal/references/api/js-sdk#collect-setup-intent-payment-method)
command.

Returns a `Promise` that resolves to an empty object when the command has been
successfully canceled. If cancellation fails, the `Promise` resolves to an
object with an
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors)

### confirmSetupIntent(setupIntent)

[Confirms](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly#submit-payment-method)
a SetupIntent after a payment method has been
[collected](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly#collect-payment-method).

This method takes a single parameter, a `SetupIntent` object obtained from a
successful call to `collectSetupIntentPaymentMethod`.

Returns a `Promise` that resolves to an object with the following fields:

- `setupIntent`: The confirmed [SetupIntent
object](https://docs.stripe.com/api/setup_intents/object), if the command
succeeded.
- `error`: An
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors), if the
command failed.

### readReusableCard()

Reads a card for [online
reuse](https://docs.stripe.com/terminal/features/saving-cards/overview).

Online payments initiated from Terminal do *not* benefit from the [lower
pricing](https://stripe.com/terminal#pricing) and liability shift given to
[standard Terminal
payments](https://docs.stripe.com/terminal/payments/collect-card-payment). Most
integrations do *not* need to use `readReusableCard`. To only collect an
in-person payment from a customer, use the [standard
flow](https://docs.stripe.com/terminal/payments/collect-card-payment).

Returns a `Promise` that resolves to an object with the following fields:

- `payment_method`: The [PaymentMethod
object](https://docs.stripe.com/api/payment_methods/object), if the command
succeeded.
- `error`: An
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors), if the
command failed.

#### Note

Currently, you can’t use Stripe Terminal to save contactless cards and mobile
wallets (for example, Apple Pay, Google Pay) for later reuse.

### cancelReadReusableCard()

Cancels an outstanding
[readReusableCard](https://docs.stripe.com/terminal/references/api/js-sdk#read-reusable-card)
command.

Returns a `Promise` that resolves to an empty object when the command has been
successfully canceled. If cancellation fails, the `Promise` resolves to an
object with an
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors).

### setReaderDisplay(displayInfo)

Updates the reader display with [cart
details](https://docs.stripe.com/terminal/features/display).

This method takes a `DisplayInfo` object as input.

```
{
 type: 'cart',
 cart: {
 line_items: [
 {
 description: string,
 amount: number,
 quantity: number,
 },
 ],
 tax: number,
 total: number,
 currency: string,
 }
}
```

Returns a `Promise` that resolves to an empty object if the command succeeds. If
the command fails, the `Promise` resolves to an object with an
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors).

### clearReaderDisplay()

If the reader is displaying cart details set with `setReaderDisplay`, this
method clears the screen and resets it to the splash screen.

Returns a `Promise` that resolves to an empty object if the command succeeds. If
the command fails, the `Promise` resolves to an object with an
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors).

### setSimulatorConfiguration(configuration)

Sets the configuration object for the [simulated card
reader](https://docs.stripe.com/terminal/references/testing#simulated-reader).

This method only takes effect when connected to the simulated reader; it
performs no action otherwise.

The simulated reader will follow the specified configuration only until
`processPayment` is complete. At that point, the simulated reader will revert to
its default behavior.

Note that this method overwrites any currently active configuration object; to
add specific key-value pairs to the object, make sure to use a combination of
this method and `getSimulatorConfiguration`.

The configuration options available are:

FieldValuesDescriptiontestCardNumberRefer to the [Simulated test
cards](https://docs.stripe.com/terminal/references/testing#simulated-test-cards)
list.Configures the simulated reader to use a test card number as the payment
method presented by the user. Use it to test different scenarios in your
integration, such as payments with different card brands or processing errors
like a declined charge.testPaymentMethodRefer to the [Simulated test
cards](https://docs.stripe.com/terminal/references/testing#simulated-test-cards)
list.Serves the same purpose as `testCardNumber`, but relies on test payment
methods instead.tipAmountAny amount or null.Configures the simulated reader to
simulate an on-reader tip amount selected by the customer.paymentMethodType
deprecated- `card_present` (default)
- `interac_present`
Determine the type of payment method created by the simulated reader when
`collectPaymentMethod` is called.
### getSimulatorConfiguration()

Returns the currently active configuration object.

The Stripe Terminal JavaScript SDK may overwrite this value as necessary,
including (but not limited to) resetting the value after processPayment is
complete, and removing unknown key-value pairs.

### collectRefundPaymentMethod(charge_id, amount, currency, options, config)

Begins collecting a payment method to be refunded. The method takes two required
parameters:

- `charge_id`, the ID of the charge that will be refunded.
- `amount`: a number that represents the amount, in cents, that will be refunded
from the charge. This number must be less than or equal to the amount that was
charged in the original payment.
- `currency`: Three-letter [ISO code for the
currency](https://docs.stripe.com/currencies), in lowercase. Must be a
[supported currency](https://docs.stripe.com/currencies).
- `options`: an optional object containing additional refund parameters.
Option Description
**refund_application_fee**

Optional, defaults to false. Connect only.

Boolean indicating whether the application fee should be refunded when refunding
this charge. If a full charge refund is given, the full application fee will be
refunded. Otherwise, the application fee will be refunded in an amount
proportional to the amount of the charge refunded.

An application fee can be refunded only by the application that created the
charge.

**reverse_transfer**

Optional, defaults to false. Connect only.

Boolean indicating whether the transfer should be reversed when refunding this
charge. The transfer will be reversed proportionally to the amount being
refunded (either the entire or partial amount).

A transfer can be reversed only by the application that created the charge.

- `config`: an optional object containing collection configuration.
Option Description
**enable_customer_cancellation**

Optional, defaults to false.

If true, Android-based smart readers show a cancel button.

Returns a `Promise` that resolves to either:

- an empty object if the payment method collection was successful, or
- an object with an
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors) field if
there was an error while collecting the refund payment method.

### processRefund()

Processes an in-progress refund. This method can only be successfully called
after `collectRefundPaymentMethod` has returned successfully.

Returns a `Promise` that resolves to either:

- a refund object if the refund was successful, or
- an object with an
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors) field if
there was an error while processing the refund.

### cancelCollectRefundPaymentMethod()

Cancels an outstanding `collectRefundPaymentMethod` command.

Returns a `Promise` that resolves to an empty object if the cancellation was
successful. If the cancellation fails, the `Promise` resolves to an object with
an `error` field.

### collectInputs(collectInputsParameters)

#### Note

To request access to the Collect Inputs beta, email us at
[stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com).

Start displaying forms and collecting information from customers using [collect
inputs](https://docs.stripe.com/terminal/features/collect-inputs).

This method takes a `ICollectInputsParameters` object as input.

Returns a `Promise` that resolves to the collected results if the command
succeeds. If the command fails, the `Promise` resolves to an object with an
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors).

### cancelCollectInputs()

#### Note

To request access to the Collect Inputs beta, email us at
[stripe-terminal-betas@stripe.com](mailto:stripe-terminal-betas@stripe.com).

Cancels an outstanding `collectInputs` command.

Returns a `Promise` that resolves to an empty object if the cancellation
succeeds. If the command fails, the `Promise` resolves to an object with an
[error](https://docs.stripe.com/terminal/references/api/js-sdk#errors).

## Errors

Errors returned by the JavaScript SDK include an error `code`, as well as a
human-readable `message`.

For methods involving a PaymentIntent like
[processPayment](https://docs.stripe.com/terminal/payments/collect-card-payment#handling-failures),
the error may also include a `payment_intent` object.

#### Error codes

CodeDescription`no_established_connection`The command failed because no reader
is
connected.`no_active_collect_payment_method_attempt``cancelCollectPaymentMethod`
can only be called when `collectPaymentMethod` is in
progress.`no_active_read_reusable_card_attempt``cancelCollectReusableCard` can
only be called when `readReusableCard` is in progress.`canceled`The command was
canceled.`cancelable_already_completed`Cancellation failed because the operation
has already completed.`cancelable_already_canceled`Cancellation failed because
the operation has already been canceled.`network_error`An unknown error occurred
when communicating with the server or reader over the network. Refer to the
error message for more information.`network_timeout`The request timed out when
communicating with the server or reader over the network. Make sure both your
device and the reader are connected to the network with stable
connections.`already_connected``connectReader` failed because a reader is
already connected.`failed_fetch_connection_token`Failed to fetch a connection
token. Make sure your connection token handler returns a promise that resolves
to the connection token.`discovery_too_many_readers``discoverReaders` returned
too many readers. Use
[Locations](https://docs.stripe.com/terminal/fleet/locations-and-zones) to
filter discovered readers by location.`invalid_reader_version`The reader is
running an unsupported software version. Please allow the reader to update and
try again.`reader_error`The reader returned an error while processing the
request. Refer to the error message for more
information.`command_already_in_progress`The action can’t be performed, because
an in-progress action is preventing it.
## Changelog

If you’re using an earlier version of the JavaScript SDK (before June 7, 2019),
update to the latest release by changing the URL of the script your integration
includes.

```
<script src="https://js.stripe.com/terminal/v1/"></script>
```

For more information on migrating from the Stripe Terminal beta, see the
[Terminal Beta Migration
Guide](https://docs.stripe.com/terminal/references/sdk-migration-guide).

#### v1

- Renamed `confirmPaymentIntent` to `processPayment`.
- Renamed the values for PaymentStatus. PaymentStatus can be one of `not_ready`,
`ready`, `waiting_for_input`, or `processing`.
- Removed card details from the response to `collectPaymentMethod`, previously
available in `response.paymentIntent.payment_method.card_payment`.
- Receipt information is now located in the
`payment_intent.charges[0].payment_method_details.card_present` hash.
- Changed the API for discovering a simulated reader to `discoverReaders({
simulated: true })`.
- Renamed `readSource` to `readReusableCard`. A successful call to
`readReusableCard` returns a
[PaymentMethod](https://docs.stripe.com/api/payment_methods) instead of a
Source. Payment Methods must be used with PaymentIntents. For more information,
see the [Payment Methods API](https://docs.stripe.com/payments/payment-methods)
overview.
- Changed the response of `connectReader` to `{ reader: Reader }`, removing the
wrapper `Connection` object.
- Removed the `startReaderDiscovery` and `stopReaderDiscovery` methods. To
repeatedly discover readers, you can use the JavaScript `setInterval` method.
- Renamed `clearConnectionToken` to `clearCachedCredentials`.

## Links

- [fetches a connection
token](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=js#connection-token)
- [simulated
reader](https://docs.stripe.com/terminal/references/testing#simulated-reader)
- [Manage locations](https://docs.stripe.com/terminal/fleet/locations-and-zones)
- [Reader](https://docs.stripe.com/api/terminal/readers/object)
- [error](https://docs.stripe.com/terminal/references/api/js-sdk#errors)
-
[register](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet#register-reader)
-
[connect](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet#connect-reader)
- [collecting a payment
method](https://docs.stripe.com/terminal/payments/collect-card-payment#collect-payment)
- [create a PaymentIntent and pass its client
secret](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=elements#web-create-intent)
- [mail order or telephone
order](https://docs.stripe.com/terminal/features/mail-telephone-orders/payments)
- [PaymentIntent object](https://docs.stripe.com/api/payment_intents/object)
- [Collecting
Payments](https://docs.stripe.com/terminal/payments/collect-card-payment)
-
[collectPaymentMethod](https://docs.stripe.com/terminal/references/api/js-sdk#collect-payment-method)
-
[Processes](https://docs.stripe.com/terminal/payments/collect-card-payment#process-payment)
- [Handling processing
failures](https://docs.stripe.com/terminal/payments/collect-card-payment#handling-failures)
- [collecting a payment method for online
reuse](https://docs.stripe.com/terminal/features/saving-cards/overview)
- [SetupIntent](https://docs.stripe.com/api/setup_intents/object)
- [mail order or telephone
order](https://docs.stripe.com/terminal/features/mail-telephone-orders/save-directly)
-
[Confirms](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly#submit-payment-method)
-
[collected](https://docs.stripe.com/terminal/features/saving-cards/save-cards-directly#collect-payment-method)
- [lower pricing](https://stripe.com/terminal#pricing)
- [PaymentMethod object](https://docs.stripe.com/api/payment_methods/object)
-
[readReusableCard](https://docs.stripe.com/terminal/references/api/js-sdk#read-reusable-card)
- [cart details](https://docs.stripe.com/terminal/features/display)
- [Simulated test
cards](https://docs.stripe.com/terminal/references/testing#simulated-test-cards)
- [ISO code for the currency](https://docs.stripe.com/currencies)
- [collect inputs](https://docs.stripe.com/terminal/features/collect-inputs)
- [https://js.stripe.com/terminal/v1/](https://js.stripe.com/terminal/v1/)
- [Terminal Beta Migration
Guide](https://docs.stripe.com/terminal/references/sdk-migration-guide)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [Payment Methods API](https://docs.stripe.com/payments/payment-methods)