# Upgrade your onramp integrationPublic preview

## Learn about the API changes when upgrading your onramp beta integration.

#### Caution

Follow this guide if you integrated with the onramp API before 2023-06-21.

We made changes to the Stripe fiat-to-crypto onramp API as part of our public
release. If you integrated with onramp before 2023-06-21, you’re integrated with
the beta onramp API.

This guide covers the changes made, impact to existing integrations, and
instructions for migrating to this latest version.

## Changes from the onramp beta

- Flatted `transaction_details` into the top-level `POST
/v1/crypto/onramp_sessions` request body
- Renamed the following fields in onramp API requests and resources-
`supported_destination_currencies` is now `destination_currencies`
- `supported_destination_networks` is now `destination_networks`
- `source_exchange_amount` is now `source_amount`
- `destination_exchange_amount` is now `destination_amount`
- Changed the onramp quotes path from `/v1/crypto/onramp/quotes` to
`/v1/crypto/onramp_quotes`

Examples of what the changes look like in onramp request and responses follow:

### Fetch an onramp quote

To fetch an onramp quote, run a command similar to the following:

```
curl -G https://api.stripe.com/v1/crypto/onramp_quotes \
curl -G https://api.stripe.com/v1/crypto/onramp/quotes \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia;crypto_onramp_beta=v2" \
 -d "source_amount"="200" \
 -d "source_exchange_amount"="200" \
```

You receive a response similar to the following:

```
{
 "id": "2e5818944df6a2325c7e9c1e72d27174b9bedfc8e64ace47c081370a5b982a7b",
 "rate_fetched_at": 1674265506.3408287,
 "destination_network_quotes": {
 "ethereum": [
 {
"id": "d160a80828eabb6b6d4aeafac585eee62d95425c7fb7577866ab04b9a786df00",
 "destination_currency": "eth",
 "destination_amount": "0.253568242640499553",
 "destination_exchange_amount": "0.253568242640499553",
 "destination_network": "ethereum",
 "fees": {
 "network_fee_monetary": "1.45",
 "transaction_fee_monetary": "12.71"
 },
 "source_total_amount": "214.20"
 },
 {
"id": "53f864cb28a42f11e1d9d5aff7e43ac96b056406f74cbf618399c6fa40f3d275",
 "destination_currency": "usdc",
 "destination_amount": "200.00",
 "destination_exchange_amount": "200.00",
 "destination_network": "ethereum",
 "fees": {
 "network_fee_monetary": "5.80",
 "transaction_fee_monetary": "12.76"
 },
 "source_total_amount": "218.56"
 }
 ],
 ...
 },
 "livemode": true,
 "source_currency": "usd",
 "source_amount": "200.00",
 "source_exchange_amount": "200.00"
}
```

### Creating an onramp session

To create an onramp session, run a command similar to the following:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Version: 2025-02-24.acacia;crypto_onramp_beta=v2" \
 -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
 -d "source_currency"="usd" \
 -d "destination_amount"="0.1" \
 -d "destination_currency"="eth" \
 -d "destination_network"="ethereum" \
 -d "destination_currencies[]"="eth" \
 -d "destination_networks[]"="ethereum" \
-d
"transaction_details[wallet_addresses][ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2"
\
 -d "transaction_details[source_currency]"="usd" \
 -d "transaction_details[destination_exchange_amount]"="10" \
 -d "transaction_details[destination_currency]"="eth" \
 -d "transaction_details[destination_network]"="ethereum" \
 -d "transaction_details[supported_destination_currencies][]"="eth" \
 -d "transaction_details[supported_destination_networks][]"="ethereum"
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
 "destination_network": "ethereum",
 "fees": null,
 "lock_wallet_address": false,
 "source_currency": "usd",
 "source_amount": null,
 "destination_amount": "0.100000000000000000",
 "destination_currencies": [
 "eth"
 ],
 "destination_networks": [
 "ethereum"
 ],
 "source_exchange_amount": null,
 "destination_exchange_amount": "0.100000000000000000",
 "supported_destination_currencies": [
 "eth"
 ],
 "supported_destination_networks": [
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

## Impact to existing integrations

We released these changes in a way that doesn’t break existing beta
integrations. If you encounter any issues with your integration, please contact
[Stripe support](https://support.stripe.com/).

## Migrate from beta to the latest onramp version

#### Common mistake

Only follow this section if:

- Stripe approved your onramp onboarding application before 2023-06-21.
- You integrated with onramp before 2023-06-21.

Otherwise, these instructions don’t apply to you since you’re already on the
latest onramp version.

### Version compatibility

#### Public preview

If you want to upgrade your API version, start specifying the
`crypto_onramp_beta=v2` as part of the `Stripe-Version` header in your requests.

Beta integrations can now pass a `crypto_onramp_beta` version as part of the
`Stripe-Version` header to consume either the beta or latest onramp API version.
Use the following matrix to determine what behavior to expect based on the
`Stripe-Version` header passed.

VersionHeaderExpected API behaviorunspecified`Stripe-Version:
2025-02-24.acacia`beta`v1``Stripe-Version:
2025-02-24.acacia;crypto_onramp_beta=v1`beta`v2``Stripe-Version:
2025-02-24.acacia;crypto_onramp_beta=v2`latest
If you’d like to upgrade your API version, start specifying the
`crypto_onramp_beta=v2` as part of the `Stripe-Version` header in your requests.

## Links

- [Stripe support](https://support.stripe.com/)