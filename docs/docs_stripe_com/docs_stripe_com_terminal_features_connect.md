# Use Terminal with Connect

## Integrate Stripe Terminal with your Connect platform.

Stripe Terminal is fully compatible with
[Connect](https://docs.stripe.com/connect), enabling your platform or
marketplace to accept in-person payments.

The way Terminal creates API objects depends on whether you use [direct
charges](https://docs.stripe.com/connect/direct-charges) or [destination
charges](https://docs.stripe.com/connect/destination-charges). If you use direct
charges, all payment-related Terminal API objects belong to connected accounts
while readers might belong to either the connected account or the platform. If
you use destination charges, all Terminal API objects are created on your
platform account. In both cases, use
[Locations](https://docs.stripe.com/api/terminal/locations) to group readers as
you see fit.

#### Note

Terminal Connect Accounts must have the `card_payments` capability to perform
transactions.

## Direct charges

### Connected accounts own readers

With this integration, all API resources belong to the connected account rather
than the platform. The connected account is responsible for the cost of Stripe
fees, refunds, and chargebacks.

In the Dashboard, you can view your Terminal data by logging in as the connected
account.

#### Create locations and readers Server-side

Create Terminal API objects like
[Locations](https://docs.stripe.com/api/terminal/locations) and
[Readers](https://docs.stripe.com/api/terminal/readers) that belong to the same
connected account which owns the payment.

To [create a
Location](https://docs.stripe.com/terminal/fleet/locations-and-zones?dashboard-or-api=dashboard#create-locations-and-zones)
belonging to a connected account, use the `Stripe-Account` header.

```
curl https://api.stripe.com/v1/terminal/locations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d display_name=HQ \
 -d "address[line1]"="1272 Valencia Street" \
 -d "address[city]"="San Francisco" \
 -d "address[state]"=CA \
 -d "address[country]"=US \
 -d "address[postal_code]"=94110
```

Before you can connect your application to a [smart
reader](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet),
you must register the reader to a Stripe account. To register a reader to a
connected account, use the `Stripe-Account` header.

```
curl https://api.stripe.com/v1/terminal/readers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d registration_code={{READER_REGISTRATION_CODE}} \
 --data-urlencode label="Alice's reader" \
 -d location={{LOCATION_ID}}
```

#### Create connection tokens Server-side

#### Note

When using [Connect OAuth](https://docs.stripe.com/connect/oauth-reference)
authentication, the connected account needs to be authorized for live mode and
test mode separately, using the respective application Client ID for each mode.

When creating a
[ConnectionToken](https://docs.stripe.com/api/terminal/connection_tokens) for
the Terminal SDK, set the `Stripe-Account` header to the connected account
accepting payments. You can also provide a `location` parameter to control
access to readers. If you provide a location, the `ConnectionToken` is only
usable with readers assigned to that location. If you don’t provide a location,
the `ConnectionToken` is usable with all readers.

```
curl https://api.stripe.com/v1/terminal/connection_tokens \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d location={{LOCATION_ID}}
```

#### Create PaymentIntents Client-side Server-side

With the iOS, Android, and React Native SDKs, you can create a `PaymentIntent`
on the client or server. The JavaScript SDK only supports server-side creation.

##### Client-side

When creating a `PaymentIntent` client-side for direct charges, you don’t need
to specify any additional parameters for the `PaymentIntent`. Instead, when
creating a `ConnectionToken`, set the `Stripe-Account` header to the connected
account accepting payments. The client SDKs create the `PaymentIntent` on the
same connected account the `ConnectionToken` belongs to. For more information,
see [Create PaymentIntents
Client-side](https://docs.stripe.com/terminal/payments/collect-card-payment#create-client-side).

##### Server-side

The JavaScript SDK requires you to create the `PaymentIntent` on your server.
For the other client SDKs, you might want to create the `PaymentIntent` on your
server if the information required to start a payment isn’t readily available in
your app. For more information, see [Create PaymentIntents
Server-side](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=js#create-payment).

When creating a `PaymentIntent` server-side for direct charges, set the
`Stripe-Account` header to the connected account.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_types[]"=card_present \
 -d capture_method=manual
```

### Platform owns readers

#### Note

[Contact us](mailto:stripe-terminal-betas@stripe.com) if you’re interested in
letting the platform own and manage readers with direct charges. This private
preview feature is currently available for [smart
readers](https://docs.stripe.com/terminal/smart-readers) leveraging a
[server-driven
integration](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=server-driven).
This integration works only with connected accounts that you control through a
single platform.

With this integration, device management resources like
[Locations](https://docs.stripe.com/api/terminal/locations) and
[Readers](https://docs.stripe.com/api/terminal/readers) belong to the platform
account while payment resources like
[PaymentIntents](https://docs.stripe.com/api/payment_intents) belong to the
connected account. This allows a single reader managed by the platform to
process payments for multiple different connected accounts. The connected
account is responsible for the cost of Stripe fees, refunds, and chargebacks.

In the Dashboard, you can view your Terminal device management data directly
when logged into your platform account. You can view payment data by logging in
as the connected account.

#### Create locations and readers

The best way to group Reader objects by connected account is by assigning them
to `Locations`. On your platform account, [create a
Location](https://docs.stripe.com/terminal/fleet/locations-and-zones?dashboard-or-api=dashboard#create-locations-and-zones)
for a connected account using a display name that identifies the account.

```
curl https://api.stripe.com/v1/terminal/locations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d display_name=HQ \
 -d "address[line1]"="1272 Valencia Street" \
 -d "address[city]"="San Francisco" \
 -d "address[state]"=CA \
 -d "address[country]"=US \
 -d "address[postal_code]"=94110
```

Before you can connect your application to a [smart
reader](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet),
you must register the reader to your platform account.

```
curl https://api.stripe.com/v1/terminal/readers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d registration_code={{READER_REGISTRATION_CODE}} \
 --data-urlencode label="Alice's reader" \
 -d location={{LOCATION_ID}}
```

#### Create PaymentIntents

When creating a `PaymentIntent` for direct charges, set the `Stripe-Account`
header to the connected account.

#### Note

The platform can only process PaymentIntents later if you create them for
connected accounts that you control through a single platform.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_types[]"=card_present \
 -d capture_method=manual
```

#### Process PaymentIntents

The platform can process the connected account’s `PaymentIntent` with the
platform-owned reader.

#### Note

The PaymentIntent can only be processed if you create it using the
`Stripe-Account` header.

```
curl
https://api.stripe.com/v1/terminal/readers/{{READER_ID}}/process_payment_intent
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent={{PAYMENT_INTENT_ID}}
```

## Destination charges

When using [destination
charges](https://docs.stripe.com/connect/destination-charges), API resources
like [PaymentIntents](https://docs.stripe.com/api/payment_intents) and
[Locations](https://docs.stripe.com/api/terminal/locations) belong to your
platform account. Each payment creates a transfer to a connected account
automatically.

In the Dashboard, you can view your Terminal data directly when logged into your
platform account.

### Create locations and readers Server-side

The best way to group Reader objects by connected account is by assigning them
to `Locations`. On your platform account, [create a
Location](https://docs.stripe.com/terminal/fleet/locations-and-zones?dashboard-or-api=dashboard#create-locations-and-zones)
for a connected account using a display name that identifies the account.

```
curl https://api.stripe.com/v1/terminal/locations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d display_name=HQ \
 -d "address[line1]"="1272 Valencia Street" \
 -d "address[city]"="San Francisco" \
 -d "address[state]"=CA \
 -d "address[country]"=US \
 -d "address[postal_code]"=94110
```

Before you can connect your application to a [smart
reader](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet),
you must register the reader to your platform account.

```
curl https://api.stripe.com/v1/terminal/readers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d registration_code={{READER_REGISTRATION_CODE}} \
 --data-urlencode label="Alice's reader" \
 -d location={{LOCATION_ID}}
```

### Create connection tokens Server-side

When creating a `ConnectionToken` for the Terminal SDK, use your platform
account’s secret key. Don’t set the `Stripe-Account` header. Provide a
`location` parameter to control access to readers. If you provide a location,
the `ConnectionToken` is only usable with readers assigned to that location. If
you don’t provide a location, the `ConnectionToken` is usable with all readers.

```
curl https://api.stripe.com/v1/terminal/connection_tokens \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d location={{LOCATION_ID}}
```

### Create PaymentIntents Client-side Server-side

When creating a `PaymentIntent` using destination charges, provide the
[on_behalf_of](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-on_behalf_of)
and
[transfer_data[destination]](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-transfer_data-destination),
and
[application_fee_amount](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-application_fee_amount)
parameters.

The `on_behalf_of` parameter is the ID of the connected account that becomes the
settlement merchant for the payment. For Terminal transactions, this parameter
**must** be set in cases where the platform country isn’t the same as the
Connect account country. When `on_behalf_of` is set, Stripe automatically:

- Settles charges in the country of the specified account, thereby minimizing
declines and avoiding currency conversions.
- Uses the fee structure for the connected account’s country.
- Lists the connected account’s address and phone number on the customer’s
credit card statement, as opposed to the platform’s address and phone number
(only occurs if the account and platform are in different countries).

For `transfer_data[destination]`, set the ID of the connected account that
receives the transfer.

Finally, you can withhold an application fee for your platform by providing the
[application_fee_amount](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-application_fee_amount)
parameter.

#### Client-side

With the iOS, Android, and React Native SDKs, you can create a `PaymentIntent`
client-side and provide the `onBehalfOf`, `transferDataDestination`, and
`applicationFeeAmount` parameters.

JavaScriptiOSAndroidReact Native
#### Note

Client-side `PaymentIntent` creation is possible with the other SDKs. If you’re
using the JavaScript SDK for Stripe Terminal, create a `PaymentIntent`
server-side.

#### Server-side

The JavaScript SDK requires you to create the `PaymentIntent` on your server.
For the other client SDKs, you want to create the `PaymentIntent` on your server
if the information required to start a payment isn’t readily available in your
app. For more information, see [Create PaymentIntents
Server-side](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=js#create-payment).

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_types[]"=card_present \
 -d capture_method=manual \
 -d application_fee_amount=200 \
 -d on_behalf_of={{CONNECTED_ACCOUNT_ID}} \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}
```

## See also

- [Cart display](https://docs.stripe.com/terminal/features/display)
- [Receipts](https://docs.stripe.com/terminal/features/receipts)

## Links

- [Connect](https://docs.stripe.com/connect)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [Locations](https://docs.stripe.com/api/terminal/locations)
- [Readers](https://docs.stripe.com/api/terminal/readers)
- [create a
Location](https://docs.stripe.com/terminal/fleet/locations-and-zones?dashboard-or-api=dashboard#create-locations-and-zones)
- [smart
reader](https://docs.stripe.com/terminal/payments/connect-reader?reader-type=internet)
- [Connect OAuth](https://docs.stripe.com/connect/oauth-reference)
- [ConnectionToken](https://docs.stripe.com/api/terminal/connection_tokens)
- [Create PaymentIntents
Client-side](https://docs.stripe.com/terminal/payments/collect-card-payment#create-client-side)
- [Create PaymentIntents
Server-side](https://docs.stripe.com/terminal/payments/collect-card-payment?terminal-sdk-platform=js#create-payment)
- [smart readers](https://docs.stripe.com/terminal/smart-readers)
- [server-driven
integration](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)
- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
-
[on_behalf_of](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-on_behalf_of)
-
[transfer_data[destination]](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-transfer_data-destination)
-
[application_fee_amount](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-application_fee_amount)
- [Cart display](https://docs.stripe.com/terminal/features/display)
- [Receipts](https://docs.stripe.com/terminal/features/receipts)