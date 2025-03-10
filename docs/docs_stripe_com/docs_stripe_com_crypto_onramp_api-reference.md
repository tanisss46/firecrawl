# Onramp API referencePublic preview

## Use the onramp API reference as you build the embeddable onramp.

Refer to the following developer flows when building your onramp integration.

## Integrate the onramp into your application

Before you can use live mode, Stripe must approve your [onramp
application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication).

### Get started

To integrate an application with the onramp:

- After you [onboard](https://dashboard.stripe.com/crypto-onramp/onboarding)
onto Stripe, use the [Dashboard](https://dashboard.stripe.com/apikeys) to grab
your [secret](https://docs.stripe.com/keys#obtain-api-keys) and
[publishable](https://docs.stripe.com/keys#obtain-api-keys) API keys.
- Generate a `CryptoOnrampSession` server-side.
- On the server, expose a new API endpoint (for example,
`myserver.com/mint-onramp-session`) that makes a call to the Stripe `POST
/v1/crypto/onramp_sessions` endpoint. This “mints” an onramp session with Stripe
that you can use with new or returning users. You need to mint one session per
user.
- Run the following command:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

You receive a response similar to the following:

```
{
 "id": "cos_0MYvmj589O8KAxCGp14dTjiw",
 "object": "crypto.onramp_session",
"client_secret":
"cos_0MYvmj589O8KAxCGp14dTjiw_secret_BsxEqQLiYKANcTAoVnJ2ikH5q002b9xzouk",
 "created": 1675794053,
 "livemode": false,
 "status": "initialized",
 "transaction_details": {
 "destination_currency": null,
 "destination_amount": null,
 "destination_network": null,
 "fees": null,
 "lock_wallet_address": false,
 "source_currency": null,
 "source_amount": null,
 "destination_currencies": [
 "btc",
 "eth",
 "sol",
 "usdc",
 "xlm"
 ],
 "destination_networks": [
 "bitcoin",
 "ethereum",
 "solana",
 "stellar"
 ],
 "transaction_id": null,
 "wallet_address": null,
 "wallet_addresses": null
 }
}
```

This endpoint returns error codes if Stripe can’t create onramp sessions. See
the supportability section below to learn why this might happen. We recommend
that you render the onramp component conditional when a user gets an HTTP status
`200` during session creation, providing a fallback UI that can deal with
session creation errors.

### Use the session client_secret in the frontend

To initialize the onramp component, you need:

- Your publishable API key.
- The `client_secret` from your request to `POST /v1/crypto/onramp_sessions`.

The following code mounts an iframe on the `#onramp-element` node, which hosts
all of the onramp. You can use an event listener to improve your application’s
functionality. For example, you can resume operation in a decentralized
application (Dapp) after cryptocurrency purchases. See the [frontend
events](https://docs.stripe.com/crypto/onramp/api-reference#frontend-events) for
all of the events a user can subscribe to.

```
<!DOCTYPE html>
<html lang="en">
 <head>
 <meta charset="utf-8" />
 <title>Crypto Onramp</title>
 <meta name="description" content="A demo of hosted onramp" />
 <meta name="viewport" content="width=device-width, initial-scale=1" />

 <script src="https://js.stripe.com/v3/"></script>
<script type="text/javascript"
src="https://crypto-js.stripe.com/crypto-onramp-outer.js"></script>
 </head>
 <body>
 <div id="onramp-element" style="max-width: 500px">

 <script>
 const stripeOnramp = StripeOnramp("pk_test_TYooMQauvdEDq54NiTphI7jx");
 initialize();
 // initialize onramp element with client secret
 function initialize() {
const clientSecret =
"cos_1LLgeLF5fgi2FFcAWx8RlsMT_secret_WNA1VOkwZ0bHMc9MtOuyJ4vto00EMsLP7Io";
 const onrampSession = stripeOnramp.createSession({clientSecret});
 onrampSession
 .mount("#onramp-element");
 }
 </script>
 </body>
</html>
```

### CryptoOnramp element renders and takes over

After the above `CryptoOnramp` html element renders, the frontend client drives
the interface. As the state of the session changes and we collect more details
around `transaction_details`, the `CryptoOnrampSession` object updates
accordingly. Webhooks and frontend events are generated for every status
transition that occurs. By using frontend event listeners, you can redirect
users back to your application user flow after the onramp session completes.

### (Optional) Change the appearance of the onramp

To enable darkmode, include an appearance struct in the session creation call
from above.

```
const onrampSession = stripeOnramp.createSession({
 clientSecret: clientSecret,
 appearance: {
 theme: 'dark'
 },
});
```

If you don’t specify the appearance, the onramp defaults to a light theme. You
can also change the theme after the onramp renders by calling:

```
onrampSession.setAppearance({
 theme: newTheme
});
```

You can use [branding
settings](https://docs.stripe.com/payments/checkout/customization/appearance#branding)
to upload your logo and brand colors which automatically apply to onramp
sessions created with your platform API key.

## Pre-populate transaction parameters

To deliver a seamless onramp user flow, you can pre-populate some of the
parameters of the onramp session. For example, a Dapp or wallet would already
have a user’s `wallet_addresses`. You can achieve this during session creation
as follows:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
 -d "source_currency"="usd" \
 -d "destination_currency"="eth" \
 -d "destination_network"="ethereum" \
 -d "destination_amount"="0.1234"
```

You receive a response similar to the following:

```
{
 "id": "cos_0MYvnp589O8KAxCGwmWATYfA",
 "object": "crypto.onramp_session",
"client_secret":
"cos_0MYvnp589O8KAxCGwmWATYfA_secret_LhqXJi2lvbMCYhVHfrHGfUfX6009qtZPtV7",
 "created": 1675794121,
 "livemode": false,
 "status": "initialized",
 "transaction_details": {
 "destination_currency": "eth",
 "destination_amount": "0.123400000000000000",
 "destination_network": "ethereum",
 "fees": null,
 "lock_wallet_address": false,
 "source_currency": "usd",
 "source_amount": null,
 "destination_currencies": [
 "btc",
 "eth",
 "sol",
 "usdc",
 "xlm"
 ],
 "destination_networks": [
 "bitcoin",
 "ethereum",
 "solana",
 "stellar"
 ],
 "transaction_id": null,
 "wallet_address": null,
 "wallet_addresses": {
 "bitcoin": null,
 "ethereum": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2",
 "polygon": null,
 "solana": null,
 "stellar": null,
 "destination_tags": null
 }
 }
}
```

We allow the following parameters to be pre-populated:

- `wallet_addresses`: The suggested wallet address to deliver crypto to (the
default selection on the wallet attach screen)
- `lock_wallet_address`: Whether or not to lock the suggested wallet address
- `source_currency`: The fiat currency for the transaction (`usd` and `eur` only
for now)
- `source_amount`: The amount of fiat currency to use for the purchase of crypto
(mutually exclusive with destination amount)
- `destination_network`: The default crypto network for this onramp (for
example, `ethereum`)
- `destination_currency`: The default cryptocurrency for this onramp session
(for example, `eth`)
- `destination_amount`: The amount of cryptocurrency to purchase (mutually
exclusive with the source amount)
- `destination_currencies`: An array of cryptocurrencies you want to restrict to
(for example, `[eth, usdc]`)
- `destination_networks`: An array of crypto networks you want to restrict to
(for example, `[ethereum, polygon]`)

Refer to the API reference for more details on the specific requirements and how
they impact users in the onramp UI.

## Pre-populate customer information

To reduce user friction during the onramp flow and increase conversion, you
might want to pre-populate some of the required KYC information for the user if
you’ve already collected it within your application.

Throughout the flow, users are required to provide at least:

- Email
- First name
- Last name
- Date of birth
- SSN
- Home address (country, address line 1, address line 2, city, state, postal
code)

The onramp API provides the ability to pre-populate all of those fields except
for SSN. To pre-populate this information, you can provide it using the
`customer_information` parameter in the OnrampSession creation API.

Example request:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer_information[email]"="john@doe.com" \
 -d "customer_information[first_name]"="John" \
 -d "customer_information[last_name]"="Doe" \
 -d "customer_information[dob][year]"=1990 \
 -d "customer_information[dob][month]"=7 \
 -d "customer_information[dob][day]"=4 \
 -d "customer_information[address][country]"="US" \
 -d "customer_information[address][line1]"="354 Oyster Point Blvd" \
 -d "customer_information[address][line2]"="Apt 1A" \
 -d "customer_information[address][city]"="South San Francisco" \
 -d "customer_information[address][state]"="CA" \
 -d "customer_information[address][postal_code]"="94080"
```

Response:

```
{
 "id": "cos_1MbuUeAEFtmWU4EVBFZS0gce",
 "object": "crypto.onramp_session",
"client_secret":
"cos_1MbuUeAEFtmWU4EVBFZS0gce_secret_zPsPPytwNU6mMKh1Bmz7ymXGi00ILwwyGeG",
 "created": 1676504072,
 "livemode": false,
 "status": "initialized",
 "transaction_details": {
 "destination_currency": null,
 "destination_amount": null,
 "destination_network": null,
 "fees": null,
 "lock_wallet_address": false,
 "source_currency": null,
 "source_amount": null,
 "destination_currencies": [
 "btc",
 "eth",
 "sol",
 "usdc",
 "xlm"
 ],
 "destination_networks": [
 "bitcoin",
 "ethereum",
 "solana",
 "polygon",
 "stellar"
 ],
 "transaction_id": null,
 "wallet_address": null,
 "wallet_addresses": null
 }
}
```

We allow the following parameters to be pre-populated:

- `customer_information.email`—Freeform string for the user’s email
- `customer_information.first_name`—Freeform string for the user’s first name
- `customer_information.last_name`—Freeform string for the user’s last name
- `customer_information.dob.year`—Integer for the user’s birth year
- `customer_information.dob.month`—Integer for the user’s birth month
- `customer_information.dob.day`—Integer for the user’s birth day
- `customer_information.address.country`—String of the two letter country code
for the user’s country of residence
- `customer_information.address.line1`—Freeform string for the user’s address
line one
- `customer_information.address.line2`—Freeform string for the user’s address
line two
- `customer_information.address.city`—Freeform string for the user’s city
- `customer_information.address.state`—String of the two letter state code for
US states (the full state name also works), for example, “CA” or “California”
- `customer_information.address.postal_code`—Freeform string for the user’s
postal code

All of the fields are optional and you can provide any subset of them for
pre-population. However, if you provide date of birth, you must also provide all
of `year`, `month`, and `day` (that is, not just one or two of the birth
fields).

## Handle user supportability and fraud

Stripe enforces limitations on the onramp product for both user supportability
and in the event of fraud attacks.

### Check user supportablity

#### Regional considerationsUnited StatesEU

Onramp is only available in the United States (excluding Hawaii) and EU
countries.

Pass `customer_ip_address` during session creation so we can preemptively check
the aforementioned limitation. The endpoint returns `HTTP 400` with
`code=crypto_onramp_unsupportable_customer` if the customer is in a geography we
can’t support (based on `customer_ip_address`)

You might want to hide the onramp option from users in this case. Otherwise, our
onramp UI renders in a `disabled` state.

Here’s a sample request and response (400) illustrating this behavior:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer_ip_address"="8.8.8.8" \
```

```
{
 "error": {
 "type": "invalid_request_error",
 "code": "crypto_onramp_unsupportable_customer",
"message": "Based on the information provided about the customer, we’re
currently unable to support them."
 }
}
```

### Handle fraud attacks

Stripe serves as the business of record and takes on the liability for disputes
and fraud. Stripe has deep expertise in risk management, but we might decide to
temporarily restrict creation of onramp sessions if we detect a high risk
situation (for example, if we see active attacks and exploits).

If we need to shut off the API because of an unbounded fraud attack, we’ll
return the following when anyone attempts to create a new session:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
```

You recieve a response similar to the following:

```
{
 "error": {
 "type": "api_error",
 "code": "crypto_onramp_disabled",
"message": "The v1/crypto/onramp_sessions endpoint has been disabled
temporarily. Stripe will get in contact with you about details of the outage.",
 "updated": 1652025690
 }
}
```

## API reference

### CryptoOnrampSession resource

The `CryptoOnrampSession` resource looks as follows:

```
{
 "id": "cos_1Ke0052eZvKYlo2Clh7lJ50Q",
 "object": "crypto.onramp_session",
 // One of the most important parts of the resource is going to be this
 // client_secret. This will be passed from the server to the client to
 // drive a single session using our embedded widget.
"client_secret":
"cos_1Ke0052eZvKYlo2Clh7lJ50Q_secret_f7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8",
 "created": 1647449225,
 "livemode": true,
// A hash representing monetary details of the transaction this session
represents
 "transaction_details": {
 // The consumer's wallet address (where crypto will be sent to)
 "wallet_addresses": null |
 {
 "ethereum": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2",
 "solana": "bufoH37MTiMTNAfBS4VEZ94dCEwMsmeSijD2vZRShuV",
 "bitcoin": "1BuFoRu4W1usdnj1nPSfnNUgUm9BM6JtnV",
 "stellar": "GBUCRQX2GXV2CCPNBVB6FMXORFRNXXQMZ5RN2GMH2KZNMH7O4WON5DDN",
// Mapping of assets to the destination tag where the crypto will be sent to
(for supported assets)
 "destination_tags": null | {
 "xlm": "123456789"
 }
 },
 // A fiat currency code
 "source_currency": null | "usd", "eur",
 // The amount of fiat we intend to onramp - excluding fees
 "source_amount": null | "1.01",
 // The selected destination_currency to convert the `source` to.
 // This should be a a crypto currency, currency code
 // If destination_currencies is set, it must be a value in that array.
 "destination_currency": null | "usdc",
 // The specific crypto network the `destination_currency` is settled on.
 // If destination_networks is set, it must be a value in that array.
 "destination_network": null | "ethereum",
 // If a platform wants to lock the currencies an session will support,
// they can add supported currencies to this array. If left null, the experience
 // will allow selection of all supported destination currencies.
 "destination_currencies": null | ["eth", "usdc", "btc" , "xlm"],
// If a platform wants to lock the supported networks, they can do so through
 // this array. If left null, the experience will allow selection of all
 // supported networks.
"destination_networks": null | ["solana", "ethereum", "polygon" , "stellar"],
 // The amount of crypto the customer will get deposited into their wallet
 "destination_amount": null | "1.012345678901234567",
 // Details about the fees associated with this transaction
 // Note: The currency associated with fee is always the same as
 // source_currency
 // Note: We won't know what fees to charge until after the customer has
 // passed status=onboarding
 "fees": null | {
 // The cost associated with moving crypto from Stripe to the end
 // consumers's wallet. e.g: for ETH, this is called "gas fee",
 // for BTC this is a "miner's fee".
 "network_fee_amount": "1.23",
 // Stripe's cut of the transaction
 "transaction_fee_amount": "1.23",
 },
 // The total amount of source currency the consumer needs to give us to
 // complete the transaction. Equivalent to source_amount + fees.
 "source_total_amount": null | "3.47",
 // Pointer to the on network transaction id/hash
// This will only be set if the sessions hits the stauts=fulfillment_complete
 // and we've transferred the crypto successfully to the external wallet.
// E.g:
https://etherscan.io/tx/0xc2573af6b3a18e6f7c0e1cccc187a483f61d72cbb421f7166970d3ab45731a95
"transaction_id": null |
"0xc2573af6b3a18e6f7c0e1cccc187a483f61d72cbb421f7166970d3ab45731a95"
 },
 // The status of the OnrampSession.
 // One of = {initialized, rejected,
 // requires_payment, fulfillment_processing, fulfillment_complete}
 "status": "initialized"
}
```

### CryptoOnrampSession state machine

The `status` field represents a state machine for the session with the following
states:

![The state machine for the
CryptoOnrampSession](https://b.stripecdn.com/docs-statics-srv/assets/state-machine.2bed0615bff44c25bfc58f16f7383391.png)

- `initialized`: The application has newly minted the onramp session on the
server-side, but the customer hasn’t used it yet. Sessions are in this state
until the user onboards and is ready to pay.
- `rejected`: We rejected the customer for some reason (KYC failure, sanctions
screening issues, fraud checks).
- `requires_payment`: The user has completed onboarding or sign-in and gets to
the payment page. If they attempt payment and fail, they stay in this status.
- `fulfillment_processing`: The customer successfully completed payment. We
haven’t delivered the crypto they purchased yet.
- `fulfillment_complete`: The customer was successfully able to pay for crypto
and we have confirmed delivery.

### CryptoOnrampSession operations

All endpoints require authentication with your [API
key](https://docs.stripe.com/keys). The authentication header is omitted in the
example requests.

Applications can perform the following operations on a `CryptoOnrampSession`:

- Create a session
- Get an existing session

### Create Session

Endpoint: `POST /v1/crypto/onramp_sessions`

Parameter nameType (optional?) default: ?Detailswallet_addressesString
(optional) default: nullThe end customer’s crypto wallet address (for each
network) to use for this transaction.- When left null, the user enters their
wallet in the onramp UI.
- When set, the platform must set either `destination_networks` or
`destination_network` and we perform address validation. Users can still select
a different wallet in the onramp UI.

For assets that use destination tags or memos, you can nest a `destination_tags`
map in `wallet_addresses` that maps assets to the specified destination tag for
a user.

source_currencyString (optional) default: nullThe default source fiat currency
for the onramp session.- When left null, a default currency is selected based on
user locale.
- When set, it must be one of the fiat currencies supported by onramp. Users can
still select a different currency in the onramp UI.
source_amountString (optional) default: nullThe default amount of fiat (in
decimal) to exchange into crypto.- When left null, a default value is computed
if `destination_amount` is set.
- When set, setting `source_amount` is mutually exclusive with setting
`destination_amount` (only one or the other is supported). We don’t support
fractional pennies. If fractional minor units of a currency are passed in, it
generates an error. Users can update the value in the onramp UI.
destination_networksArray<String> (optional) default: nullThe list of
destination crypto networks user can choose from.- When left null, all supported
crypto networks are shown in the onramp UI.
- When set, it must be a non-empty array where values in the array are each a
valid crypto network. Allowed values are `{solana, ethereum, bitcoin, polygon}`.
It can be used to lock users to a specific network by passing a single value
array. Users **cannot** override this parameter.
destination_currenciesArray<String> (optional) default: nullThe list of
destination cryptocurrencies a user can choose from.- When left null, all
supported cryptocurrencies are shown in the onramp UI subject to
`destination_networks` if set.
- When set, it must be a non-empty array where all values in the array are valid
cryptocurrencies. These are `{eth, matic, sol, usdc, btc}`. You can use it to
lock users to a specific cryptocurrency by passing a single value array. Users
**cannot** override this parameter.
destination_networkString (optional) default: nullThe default destination crypto
network.- When left null, the first value of `destination_networks` is selected.
- When set, if `destination_networks` is also set, the value of
`destination_network` must be present in that array. To lock a
`destination_network`, specify that value as the single value for
`destination_networks`. Supported destination networks are `{solana, bitcoin,
ethereum, polygon}`. Users can select a different network in the onramp UI
subject to `destination_networks` if set.
destination_currencyString (optional) default: nullThe default destination
cryptocurrency.- When left null, the first value of `destination_currencies` is
selected.
- When set, if `destination_currencies` is also set, the value of
`destination_currency` must be present in that array. To lock a
`destination_currency`, specify that value as the single value for
`destination_currencies`. Supported destination currencies are `{eth, matic,
sol, usdc, btc}`. Users can select a different cryptocurrency in the onramp UI
subject to `destination_currencies` if set.
destination_amountString (optional) default: nullThe default amount of crypto to
exchange into.- When left null, a default value is computed if `source_amount`,
`destination_currency`, and `destination_network` are set.
- When set, both `destination_currency` and `destination_network` must also be
set. All cryptocurrencies are supported to their full precisions (for example,
18 decimal places for `eth`). We validate and generate an error if the amount
exceeds the supported precision based on the exchange currency. Setting
`source_amount` is mutually exclusive with setting `destination_amount` (only
one or the other is supported). Users can update the amount in the onramp UI.
customer_ip_addressString (optional) default: nullThe IP address of the customer
the platform intends to onramp. If the user’s IP is in a region we can’t
support, we return an `HTTP 400` with an appropriate error code. We support IPv4
and IPv6 addresses. Geographic supportability is checked again later in the
onramp flow, which provides a way to hide the onramp option from ineligible
users for a better user experience.
Sample request and response:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
 -d "source_currency"="usd" \
 -d "destination_currency"="eth" \
 -d "destination_network"="ethereum" \
 -d "destination_currencies[]"="eth" \
 -d "destination_networks[]"="ethereum"
```

```
{
 "id": "cos_0MYvv9589O8KAxCGPm84FhVR",
 "object": "crypto.onramp_session",
"client_secret":
"cos_0MYvv9589O8KAxCGPm84FhVR_secret_IGBYKVlTlnJL8UGxji48pKxBO00deNcBuVc",
 "created": 1675794575,
 "livemode": false,
 "status": "initialized",
 "transaction_details": {
 "destination_currency": "eth",
 "destination_amount": null,
 "destination_network": "ethereum",
 "fees": null,
 "lock_wallet_address": false,
 "source_currency": "usd",
 "source_amount": null,
 "destination_currencies": [
 "eth"
 ],
 "destination_networks": [
 "ethereum"
 ],
 "transaction_id": null,
 "wallet_address": null,
 "wallet_addresses": {
 "bitcoin": null,
 "ethereum": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2",
 "polygon": null,
 "solana": null,
 "stellar": null,
 "destination_tags": null
 }
 }
}
```

#### Get session

Endpoint: `GET /v1/crypto/onramp_sessions/:id`

Parameter nameType (optional?) default: ?DetailsNo supported parameters for this
operation!
Here’s an example request:

```
curl -X GET
https://api.stripe.com/v1/crypto/onramp_sessions/cos_0MYvv9589O8KAxCGPm84FhVR \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

You receive a response similar to the following:

```
{
 "id": "cos_0MYvv9589O8KAxCGPm84FhVR",
 "object": "crypto.onramp_session",
"client_secret":
"cos_0MYvv9589O8KAxCGPm84FhVR_secret_IGBYKVlTlnJL8UGxji48pKxBO00deNcBuVc",
 "created": 1675794575,
 "livemode": false,
 "status": "initialized",
 "transaction_details": {
 "destination_currency": "eth",
 "destination_amount": null,
 "destination_network": "ethereum",
 "fees": null,
 "lock_wallet_address": false,
 "source_currency": "usd",
 "source_amount": null,
 "destination_currencies": [
 "eth"
 ],
 "destination_networks": [
 "ethereum"
 ],
 "transaction_id": null,
 "wallet_address": null,
 "wallet_addresses": {
 "bitcoin": null,
 "ethereum": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2",
 "polygon": null,
 "solana": null,
 "stellar": null,
 "destination_tags": null
 }
 }
}
```

#### Validation and errors

ConditionHTTP statusError codeWe’re unable to mint new sessions because of an
incident400`crypto_onramp_disabled`Based on the `customer_ip_address` parameter,
we’re unable to support the given
consumer.400`crypto_onramp_unsupported_country` or
`crypto_onramp_unsupportable_customer`Malformed `customer_ip_address` is passed
in to the `/v1/crypto/onramp_session`
endpoint400`customer_ip_address``source_amount` and `destination_amount` are
mutually exclusive, but the platform set
both.400`crypto_onramp_invalid_source_destination_pair`One of
`destination_currency` and `destination_network` is set, but the other one
isn’t400`crypto_onramp_incomplete_destination_currency_and_network_pair`The
combination of `destination_currency` and `destination_network` isn’t
valid400`crypto_onramp_invalid_destination_currency_and_network_pair``source_amount`
is set, but `source_currency` isn’t
set400`crypto_onramp_missing_source_currency``source_amount` isn’t a positive
number400`crypto_onramp_invalid_source_amount``destination_amount` is set, but
`destination_currency` isn’t
set400`crypto_onramp_missing_destination_currency``destination_amount` isn’t a
positive number400`crypto_onramp_invalid_destination_amount`The combination of
`destination_currencies` and `destination_networks` doesn’t have any supported
currencies400`crypto_onramp_invalid_destination_currencies_and_networks``destination_currency`
isn’t included in
`destination_currencies`400`crypto_onramp_conflicting_destination_currency``destination_network`
isn’t included in
`destination_networks`400`crypto_onramp_conflicting_destination_network`At least
one wallet address in `wallet_addresses` is associated with a network that isn’t
included in
`destination_networks`400`crypto_onramp_wallet_addresses_not_all_networks_supported`No
wallet addresses were provided in `wallet_addresses` but `lock_wallet_address`
was set to true400`crypto_onramp_no_wallet_address_to_lock`The business hasn’t
set the `business_name` or `business_url` fields. These are populated in the
[Dashboard](https://dashboard.stripe.com/settings/public/) under `Public
business name` and `Business
website`400`crypto_onramp_merchant_not_properly_setup`
#### Get multiple sessions

Endpoint: `GET /v1/crypto/onramp_sessions`

Fetch multiple onramp sessions at the same time using the [list
endpoint](https://docs.stripe.com/api/crypto/onramp_sessions/list).

### Webhooks

We send a `crypto.onramp_session_updated` webhook every time the status of an
onramp session changes post creation. We won’t send one when a new session is
created. You can [configure webhooks](https://docs.stripe.com/webhooks) in the
Dashboard.

The resource used by the webhook will be the `CryptoOnrampSession` resource
above:

```
{
 "id": "evt_123",
 "object": "event",
 "data": {
 "object": {
 "id": "cos_0MYvv9589O8KAxCGPm84FhVR",
 "object": "crypto.onramp_session",
"client_secret":
"cos_0MYvv9589O8KAxCGPm84FhVR_secret_IGBYKVlTlnJL8UGxji48pKxBO00deNcBuVc",
 "created": 1675794575,
 "livemode": false,
 "status": "initialized",
 "transaction_details": {
 "destination_currency": "eth",
 "destination_amount": null,
 "destination_network": "ethereum",
 "fees": null,
 "lock_wallet_address": false,
 "source_currency": "usd",
 "source_amount": null,
 "destination_currencies": [
 "eth"
 ],
 "destination_networks": [
 "ethereum"
 ],
 "transaction_id": null,
 "wallet_address": null,
 "wallet_addresses": {
 "bitcoin": null,
 "ethereum": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2",
 "polygon": null,
 "solana": null,
 "stellar": null,
 "destination_tags": null
 }
 }
 }
 }
}
```

### Frontend events

Here is the list of frontend events that you can subscribe to:

```
// when the onramp UI is rendered
{
 type: 'onramp_ui_loaded',
 payload: {session: OnrampSession},
}
// when the onramp session object is updated
{
 type: 'onramp_session_updated',
 payload: {session: OnrampSession},
}

// for modal overlay render mode only
{
 type: 'onramp_ui_modal_opened',
 payload: {session: OnrampSession},
}
{
 type: 'onramp_ui_modal_closed',
 payload: {session: OnrampSession},
}
```

As shown above, events can be subscribed to and unsubscribed to using the
standard `addEventListener/removeEventListener` functions over OnrampSession.
You can use `'*'` to match all events.

### Session persistence

You can use session persistence to help you provide notifications and keep users
engaged with the onramp after fulfilling their purchase.

#### Advantages of session persistence

You might want to persist an onramp session across user visits in some
instances. For example, when a user’s onramp session is disrupted or dropped,
you could prompt them and provide ways to resume the onramp session later. Or if
a user refreshes the page after completing the payment, you can retain the
ability to notify them when a previous onramp purchase was fulfilled. For this
reason, the OnrampSession object is stateful and stored as a server side
resource. By initializing the onramp UI using a previously used OnrampSession
client secret, users return to where they left off.

#### Session persistence configuration

A client secret is a unique identifier for the onramp session that stores the
lifecycle of a session without leaking sensitive payment information. However,
it exposes private information such as wallet addresses. Don’t log it, embed it
in URLs, or expose it to anyone other than the customer. Make sure that you have
TLS on any page that includes the client secret. If you have a Web2-like account
structure, you could link OnrampSession to your user object and fetch it upon
authentication. For an account-less Web3 application, it would add user friction
to require the use of message signing for authentication. Privacy-preserving
local storage yields an acceptable user experience.

## Links

- [onramp
application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication)
- [onboard](https://dashboard.stripe.com/crypto-onramp/onboarding)
- [Dashboard](https://dashboard.stripe.com/apikeys)
- [secret](https://docs.stripe.com/keys#obtain-api-keys)
- [frontend
events](https://docs.stripe.com/crypto/onramp/api-reference#frontend-events)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
-
[https://crypto-js.stripe.com/crypto-onramp-outer.js](https://crypto-js.stripe.com/crypto-onramp-outer.js)
- [branding
settings](https://docs.stripe.com/payments/checkout/customization/appearance#branding)
-
[https://etherscan.io/tx/0xc2573af6b3a18e6f7c0e1cccc187a483f61d72cbb421f7166970d3ab45731a95](https://etherscan.io/tx/0xc2573af6b3a18e6f7c0e1cccc187a483f61d72cbb421f7166970d3ab45731a95)
- [API key](https://docs.stripe.com/keys)
- [Dashboard](https://dashboard.stripe.com/settings/public/)
- [list endpoint](https://docs.stripe.com/api/crypto/onramp_sessions/list)
- [configure webhooks](https://docs.stripe.com/webhooks)