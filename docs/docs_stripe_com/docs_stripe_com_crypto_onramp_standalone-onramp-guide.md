# Use the Stripe-hosted, standalone onrampPublic preview

## Generate a redirect URL and mint a session for the standalone onramp.

The Stripe-hosted, standalone onramp is a prebuilt frontend integration of the
crypto onramp hosted at [https://crypto.link.com](https://crypto.link.com/).
Platforms can integrate the crypto onramp by redirecting their users to the
standalone onramp, rather than hosting an embedded version of the onramp within
their application. To [embed the
onramp](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide), you must
submit an
[application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication).

Generate a redirect URLMint a session with a redirect URLOverviewGenerate a
redirect URL in the frontend without a Stripe account.Mint a session with a
redirect URL in the backend with a Stripe account.CustomizationCustomize the
suggested source or destination amount, destination currency, and network.Allows
full customization, including the destination wallet address. For a full list of
parameters, see [Pre-populate transaction
parameters](https://docs.stripe.com/crypto/onramp/standalone-onramp-guide#prepopulate-transaction-parameters).Best
forPlatforms that only want a lightweight front-end integration with light
customization and no branding.Platforms that want a fully customized onramp with
branding.
## Generate a redirect URL

Include the following scripts using script tags within the `<head>` element of
your HTML. These scripts must always load directly from Stripe domains
(*https://js.stripe.com* and *https://crypto-js.stripe.com*) for compatibility
and [PCI
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

Generate a redirect URL using the `Standalone` function, passing in the desired
parameters:

```
const standaloneOnramp = window.StripeOnramp.Standalone({
 source_currency: 'usd',
 amount: {source_amount: '42'},
 destination_networks: ['ethereum', 'bitcoin'],
 destination_currencies: ['eth', 'btc'],
 destination_currency: 'btc',
 destination_network: 'bitcoin'
});
const redirectUrl = standaloneOnramp.getUrl();
```

You can pre-populate these parameters:

- `source_currency`: The fiat currency for the transaction (`usd` and `eur`).
- `amount`: The fixed amount of fiat currency or cryptocurrency for this
purchase. Specify a fiat amount by passing in `source_amount` (`{source_amount:
42}`) . Specify a cryptocurrency amount by passing in `destination_amount`
(`{destination_amount: 42}`). You can only specify one amount.
- `destination_currencies`: An array of cryptocurrencies you want to restrict to
(`[eth, usdc]`).
- `destination_networks`: An array of crypto networks you want to restrict to
(`[ethereum, polygon]`).
- `destination_network`: The default crypto network for this onramp
(`ethereum`).
- `destination_currency`: The default cryptocurrency for this onramp session
(`eth`).

Redirect your users to the URL for a prebuilt front-end integration of the
crypto onramp on the standalone onramp.

## Mint a session with a redirect URL

Similar to other integrations, you need to implement a server endpoint to
[create a new onramp
session](https://docs.stripe.com/crypto/onramp/api-reference) for every user
visit. The onramp session creation request returns a `redirect_url`. Redirect
your users to the URL for a fully customized and branded crypto onramp on the
standalone onramp.

Generate a [crypto onramp
session](https://docs.stripe.com/crypto/onramp/api-reference#api-reference) with
a `redirect_url` by running the following curl command:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

You receive a response similar to the following:

```
{
 "id": "cos_0MpKNb589O8KAxCGjmaOVF8T",
 "object": "crypto.onramp_session",
"client_secret":
"cos_0MpKNb589O8KAxCGjmaOVF8T_secret_fqV1TAdhSCFeO9FW5HnygRXca00AwEHIOu8",
 "created": 1679701843,
 "livemode": false,
"redirect_url":
"https://crypto.link.com?session_hash=CCwaGwoZYWNjdF8yOERUNTg5TzhLQXhDR2JMbXh5WijU7vigBjIGmyBbkqO4Oi10eFHEaFln9gFSsTGQBoQf5qRZK-A0NhiEIeH3QaCMrz-d4oYotirrAd_Bkz4",
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

## Links

- [https://crypto.link.com](https://crypto.link.com)
- [embed the
onramp](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide)
-
[application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication)
- [PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
-
[https://crypto-js.stripe.com/crypto-onramp-outer.js](https://crypto-js.stripe.com/crypto-onramp-outer.js)
- [create a new onramp
session](https://docs.stripe.com/crypto/onramp/api-reference)
- [crypto onramp
session](https://docs.stripe.com/crypto/onramp/api-reference#api-reference)
-
[https://crypto.link.com?session_hash=CCwaGwoZYWNjdF8yOERUNTg5TzhLQXhDR2JMbXh5WijU7vigBjIGmyBbkqO4Oi10eFHEaFln9gFSsTGQBoQf5qRZK-A0NhiEIeH3QaCMrz-d4oYotirrAd_Bkz4](https://crypto.link.com?session_hash=CCwaGwoZYWNjdF8yOERUNTg5TzhLQXhDR2JMbXh5WijU7vigBjIGmyBbkqO4Oi10eFHEaFln9gFSsTGQBoQf5qRZK-A0NhiEIeH3QaCMrz-d4oYotirrAd_Bkz4)