# Use the Onramp Quotes APIPublic preview

## Display quotes in your product UI.

The Onramp Quotes API lets platforms fetch estimated quotes for onramp
conversions into various cryptocurrencies on different networks. You can specify
a fixed source or destination amount and limit the quotes to a subset of
destination currencies or networks. This API allows you to display quotes in
your product UI before directing the user to the onramp widget. If the quote
expires before the user visits the onramp widget, the user might see a slightly
different quote in the onramp widget.

## Get a conversion quote

Use the `GET /v1/crypto/onramp_quotes` endpoint to get a conversion quote. The
following table captures all of the available parameters for this endpoint:

ParameterTypeDefaultDetails`source_currency`String (optional)`usd`The
[ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) currency code. We
currently only support `usd` and `eur`.`source_amount`String (optional)`100.00`A
string representation of the fiat amount that you need to onramp. If
`source_amount` is set, `destination_amount` must be null (they’re mutually
exclusive, because you can only set a fixed amount for one end of the
trade).`destination_amount`String (optional)`null`A string representation of the
amount of `destination_currency` to be purchased. If `destination_amount` is
set, `source_amount` must be null. When specifying this field, you must also set
a single value for `destination_currencies` and a single value for
`destination_networks` (so we know what cryptocurrency to
quote).`destination_currencies`Array<String> (optional)`null`- `['usdc',
'ethereum']`
The list of cryptocurrencies you want to generate quotes for. If left `null`, we
retrieve quotes for all `destination_currencies` that `destination_networks`
supports.- Currencies: `btc`, `eth`, `sol`, `matic`, `usdc`, `xlm`
`destination_networks`Array<String> (optional)`null`- `['polygon', 'bitcoin',
'solana', 'ethereum']`
The list of cryptocurrency networks you want to generate quotes for. If left
`null`, we retrieve quotes for `destination_currencies` in all networks.-
Networks: `bitcoin`, `ethereum`, `solana`, `polygon` , `stellar`

## Example quote requests

To fetch all destination currency-network pairs with a default source amount of
100 USD, run the following command:

```
curl -G https://api.stripe.com/v1/crypto/onramp_quotes \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

You receive a response similar to the following:

```
{
 "id": "cd35838481497f403988360cc0ff5ce5c5ce7451ce8938f86d379dff7157d33d",
 "rate_fetched_at": 1674265380.6883376,
 "destination_network_quotes": {
 "ethereum": [
 {
"id": "7eb9ccb7c1bffadf3773ca1f56ba3a352fe4a226328e72142925a80e7242b70c",
 "destination_currency": "eth",
 "destination_amount": "0.060232255577506866",
 "destination_network": "ethereum",
 "fees": {
 "network_fee_monetary": "1.41",
 "transaction_fee_monetary": "3.03"
 },
 "source_total_amount": "104.44"
 },
 {
"id": "398de047128b6dff1abbc41519811db68dd8bcb69939b87c4a4621b1740a1c5b",
 "destination_currency": "usdc",
 "destination_amount": "100.00",
 "destination_network": "ethereum",
 "fees": {
 "network_fee_monetary": "5.63",
 "transaction_fee_monetary": "3.07"
 },
 "source_total_amount": "108.70"
 }
 ],
 ...
 },
 "livemode": true,
 "source_currency": "usd",
 "source_amount": "100.00"
}
```

To fetch all destination currency-network pairs with a source amount of 200 USD,
run the following command:

```
curl -G https://api.stripe.com/v1/crypto/onramp_quotes \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "source_amount"="200"
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
 "source_amount": "200.00"
}
```

To fetch quotes for ETH and SOL on the Ethereum and Solana networks, run the
following command (which results in ETH on Ethereum and SOL on Solana). When you
specify `destination_currencies` and `destination_networks`, each valid
currency-network pair in their cross-product returns a quote. The default value
for `destination_currencies` is all currencies, and the default value for
`destination_networks` is all networks.

```
curl -G https://api.stripe.com/v1/crypto/onramp_quotes \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "source_amount"="200" \
 -d "destination_currencies[]"="eth" \
 -d "destination_currencies[]"="sol" \
 -d "destination_networks[]"="ethereum" \
 -d "destination_networks[]"="solana"
```

You receive a response similar to the following:

```
{
 "id": "c9ab6fd14f87290ef94b583f0dd346de8e197321e029776c12b7790cd83fb78c",
 "rate_fetched_at": 1674265576.8238478,
 "destination_network_quotes": {
 "bitcoin": [],
 "ethereum": [
 {
"id": "97bbd7b9f8bc1a029264cdc28b47b636e989f8bcab96a80a3bded2094131e311",
 "destination_currency": "eth",
 "destination_amount": "0.253433817682353791",
 "destination_network": "ethereum",
 "fees": {
 "network_fee_monetary": "1.46",
 "transaction_fee_monetary": "12.71"
 },
 "source_total_amount": "214.17"
 }
 ],
 "polygon": [],
 "solana": [
 {
"id": "79f00923b96543aa69d140172c7cefd0e73a2ed089d8935e63dcf21028698e23",
 "destination_currency": "sol",
 "destination_amount": "16.767237943",
 "destination_network": "solana",
 "fees": {
 "network_fee_monetary": "0.01",
 "transaction_fee_monetary": "12.70"
 },
 "source_total_amount": "212.71"
 }
 ]
 },
 "livemode": true,
 "source_currency": "usd",
 "source_amount": "200.00"
}
```

To fetch quotes for USDC on Ethereum and Solana, run the following command:

```
curl -G https://api.stripe.com/v1/crypto/onramp_quotes \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "source_amount"="200" \
 -d "destination_currencies[]"="usdc" \
 -d "destination_networks[]"="ethereum" \
 -d "destination_networks[]"="solana"
```

You receive a response similar to the following:

```
{
 "id": "8727e8de9a22915aea079973028054e31d362a328758a5953cee6ba1b6f22569",
 "rate_fetched_at": 1674268717.432479,
 "destination_network_quotes": {
 "bitcoin": [],
 "ethereum": [
 {
"id": "603f29933c921d59b169572cf2d61da7d88f2a6973da0d6fcb686b3dec3de223",
 "destination_currency": "usdc",
 "destination_amount": "200.00",
 "destination_network": "ethereum",
 "fees": {
 "network_fee_monetary": "5.88",
 "transaction_fee_monetary": "12.76"
 },
 "source_total_amount": "218.64"
 }
 ],
 "polygon": [],
 "solana": [
 {
"id": "38b8388072e6272e7a0c0d5ee1161d3d747362a574f54fe76f1554ff60e3a007",
 "destination_currency": "usdc",
 "destination_amount": "200.00",
 "destination_network": "solana",
 "fees": {
 "network_fee_monetary": "0.01",
 "transaction_fee_monetary": "12.70"
 },
 "source_total_amount": "212.71"
 }
 ]
 },
 "livemode": true,
 "source_currency": "usd",
 "source_amount": "200.00"
}
```

To fetch a quote for a single destination currency-network pair (ETH on
Ethereum) with `destination_amount` specified, run the following command:

```
curl -G https://api.stripe.com/v1/crypto/onramp_quotes \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "destination_amount"="0.42" \
 -d "destination_currencies[]"="eth" \
 -d "destination_networks[]"="ethereum"
```

You receive a response similar to the following:

```
{
 "id": "74f73859a8836293ce4f1e6757dc258c9f1016deea7b075faba8b5755d163168",
 "rate_fetched_at": 1674268804.6989243,
 "destination_network_quotes": {
 "bitcoin": null,
 "ethereum": [
 {
"id": "f1adad5680b081031b03b89c174d25ce6b609416fc82f976423e95a089a10334",
 "destination_currency": "eth",
 "destination_amount": "0.420000000000000000",
 "destination_network": "ethereum",
 "fees": {
 "network_fee_monetary": "1.45",
 "transaction_fee_monetary": "21.06"
 },
 "source_total_amount": "719.53"
 }
 ],
 "polygon": null,
 "solana": null
 },
 "livemode": true,
 "source_currency": "usd",
 "source_amount": "697.02"
}
```

## Links

- [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html)