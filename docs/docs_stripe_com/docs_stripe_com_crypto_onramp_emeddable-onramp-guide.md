# Set up an emeddable onramp integrationPublic preview

## Use this guide to fully customize the embeddable onramp.

To integrate with the onramp SDK:

- [Install the SDK and client
library](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide#install).
- [Generate a crypto onramp
session](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide#onramp-session)
on your backend.
- [Render the onramp
UI](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide#onramp-ui) on
your website.
- [View your integration’s usage in the Stripe
Dashboard](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide#dashboard).
[Install the SDK and client
libraryclient-sideserver-side](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide#install)
### Client-side

Include the following scripts using script tags within the `<head>` element of
your HTML. These scripts must always load directly from Stripe’s domains
(https://js.stripe.com and https://crypto-js.stripe.com) for compatibility and
[PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance).
Don’t include the scripts in a bundle or host a copy yourself. If you do, your
integration might break without warning.

```
<head>
 <title>Onramp</title>
 <script src="https://js.stripe.com/v3/"></script>
 <script src="https://crypto-js.stripe.com/crypto-onramp-outer.js"></script>
</head>
```

### Use the Onramp JS SDK as a module

Use the npm package to load the onramp JS SDK as an [ES
module](https://docs.stripe.com/crypto/onramp/esmodule). The package includes
Typescript type definitions.

```
npm install --save @stripe/stripe-js @stripe/crypto

```

### Server-side

Our official libraries don’t contain built-in support for the API endpoints
because the onramp API is in limited beta. As a result, our examples use curl
for backend interactions.

[Generate a crypto onramp
sessionserver-side](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide#onramp-session)
Generate a [crypto onramp
session](https://docs.stripe.com/crypto/onramp/api-reference#api-reference) by
running the following curl command in your terminal:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"
 # add as many parameters as you'd like
```

You receive a response similar to the following:

```
{
 "id": "cos_0MYfrA589O8KAxCGEDdIVYy3",
 "object": "crypto.onramp_session",
"client_secret":
"cos_0MYfrA589O8KAxCGEDdIVYy3_secret_rnpnWaxQbYQOvp6nVMvEeczx300NRU4hErZ",
 "created": 1675732824,
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
 "usdc"
 ],
 "destination_networks": [
 "bitcoin",
 "ethereum",
 "solana"
 ],
 "transaction_id": null,
 "wallet_address": null,
 "wallet_addresses": {
 "bitcoin": null,
 "ethereum": "0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2",
 "polygon": null,
 "solana": null
 }
 }
}
```

See the [Onramp API
reference](https://docs.stripe.com/crypto/onramp/api-reference#api-reference)
for the full parameter list you can pass in when creating a session.

[Render the Onramp
UIclient-side](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide#onramp-ui)JavaScriptReact
Import both the StripeJS and the OnrampJS bundles:

```
<!DOCTYPE html>
<html lang="en">
 <head>
 <meta charset="utf-8" />
 <title>Crypto Onramp</title>
 <meta name="description" content="A demo of the hosted onramp" />
 <meta name="viewport" content="width=device-width, initial-scale=1" />
 <script src="https://js.stripe.com/v3/"></script>
 <script src="https://crypto-js.stripe.com/crypto-onramp-outer.js"></script>
 <script src="onramp.js" defer></script>
 </head>
 <body>
 <div id="onramp-element" />
 </body>
</html>
```

Use the client_secret from your server-side call in the previous step to
initiate and mount the onramp session:

```
const stripeOnramp = StripeOnramp("pk_test_TYooMQauvdEDq54NiTphI7jx");
initialize();
// Initialize the onramp element with a client secret
function initialize() {
// IMPORTANT: replace the following with your logic of how to mint/retrieve the
client secret
const clientSecret =
"cos_1Lb6vsAY1pjOSNXVWF3nUtkV_secret_8fuPvTzBaxj3XRh14C6tqvdl600rpW7hG4G";
 const onrampSession = stripeOnramp.createSession({clientSecret});
 onrampSession
 .mount("#onramp-element");
}
```

After running the script, the onramp renders the following dialog:

![Stripe's fiat-to-crypto onramp being embedded into a third-party
application](https://b.stripecdn.com/docs-statics-srv/assets/crypto-onramp-overview.c9ec889d4c12403f4b2dbc17600dc640.png)

Stripe’s fiat-to-crypto onramp embedded within a third-party application

### Test mode values

#### Warning

Test mode transaction amounts are overridden by our pre-decided limits.

Use the following values to complete an onramp transaction in [test
mode](https://docs.stripe.com/test-mode):

- On the OTP screen, use `000000` for the verification code.
- On the personal information screen, use `000000000` for the SSN and
`address_full_match` for address line 1.
- On the payment details screen, use the test credit card number
`4242424242424242`.
[View integration
usage](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide#dashboard)
After you’ve launched the onramp, you can view customized usage reports in the
[Stripe Dashboard](https://dashboard.stripe.com/crypto-onramp/reports). You can
also return to the [onboarding
page](https://dashboard.stripe.com/crypto-onramp/onboarding) to update the
domains where you plan to host the onramp, and check the status of any
onboarding tasks.

## Links

- [PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
-
[https://crypto-js.stripe.com/crypto-onramp-outer.js](https://crypto-js.stripe.com/crypto-onramp-outer.js)
- [ES module](https://docs.stripe.com/crypto/onramp/esmodule)
- [crypto onramp
session](https://docs.stripe.com/crypto/onramp/api-reference#api-reference)
- [test mode](https://docs.stripe.com/test-mode)
- [Stripe Dashboard](https://dashboard.stripe.com/crypto-onramp/reports)
- [onboarding page](https://dashboard.stripe.com/crypto-onramp/onboarding)