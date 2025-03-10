# Back-end integration best practicesPublic preview

## Safely integrate the onramp for different web3 use cases.

To make onramp appear to be part of your product UI, frame the onramp as a
native component of your application. In addition to front-end design, consider
pre-populating onramp parameters when creating an onramp session in the back
end.

## Wallet

Wallet users have two main onramp entry points: wallet funding and transaction
top-ups.

### Wallet funding

You can proactively prompt users to fund their wallet after they create a new
wallet or when their funds are critically low.

In these cases, consider specifying the following parameters:

- `wallet_addresses`: Use the wallet address already in use.
- `destination_networks`: Set to the default or selected network to reduce user
confusion.
- `destination_currencies`: You can leave this blank, but you can also restrict
it to the native gas token or any desired cryptocurrencies. For example, if you
offer a DeFi service in USDC, consider that the user likely needs both USDC and
the gas token.
- `destination_network`: Leave this blank to inherit the first value of the
supported network.
- `destination_currency`: Leave this blank to inherit the first value of the
supported cryptocurrencies.

The following code example shows the creation of an onramp session using several
of these parameters:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer_ip_address"="8.8.8.8" \
 -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
 -d "wallet_addresses[solana]"="bufoH37MTiMTNAfBS4VEZ94dCEwMsmeSijD2vZRShuV" \
 -d "destination_networks[]"="ethereum" \
 -d "destination_networks[]"="solana"
```

### Transaction top-ups

When a Dapp or the user proposes a transaction, you might detect that the
transaction fails because of insufficient funds. In this case, you can calculate
the delta required for the transaction to complete. However, it’s often
difficult to detect the requested amount or cryptocurrency for ERC or SPL
tokens.

In these cases, consider specifying the following:

- `wallet_addresses`: Use the wallet address in use.
- `destination_networks`: Set to the selected network.
- `destination_currencies`: Restrict to the missing currencies when possible.
- `destination_network`: Set to the selected network (a required value if you
want to set the amount).
- `destination_currency`: Set to the target currency (a required value if you
want to set the amount).
- `destination_amount`: Set to the balance differences, leaving enough of a
buffer for gas when applicable.

The following code example shows the creation of an onramp session using several
of these parameters:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer_ip_address"="8.8.8.8" \
 -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
 -d "destination_networks[]"="ethereum" \
 -d "destination_currencies[]"="usdc" \
 -d "destination_network"="ethereum" \
 -d "destination_currency"="usdc" \
 -d "destination_amount"="10"
```

## Dapp or NFT checkout

You can use the onramp in checkout when you know the destination amount. For
example, a Dapp might sell memberships for a fixed price, or a user might want
to buy a specific NFT from a marketplace.

In these cases, consider specifying the following:

- `wallet_addresses`: Use the connected wallet address.
- `destination_networks`: Use the connected network.
- `destination_currencies`: Use the presentment currency (the price in the
currency the goods are quoted in).
- `destination_network`: Set to the selected network above (required if you want
to set the amount).
- `destination_currency`: Set to the target currency above (required if you want
to set the amount).
- `destination_amount`: Set it to either the balance difference or to cover the
entire purchase amount. Some users adopt both, using on-chain analytics with an
almost even split. A user might choose the full amount to simplify their tax
cost basis or to avoid spending accumulated assets. In both cases, leave room
for gas.

The following code example shows the creation of an onramp session using several
of these parameters:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer_ip_address"="8.8.8.8" \
 -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
 -d "destination_networks[]"="ethereum" \
 -d "destination_currencies[]"="eth" \
 -d "destination_network"="ethereum" \
 -d "destination_currency"="eth" \
 -d "destination_amount"="0.2343"
```

## DEX

A DEX offers a unique opportunity to let users buy any cryptocurrency with fiat.
While a DEX can prompt users to top up crypto when exchanging arbitrary crypto
pairs using an existing interface, it’s better to have a dedicated user flow
that focuses on fiat to crypto only.

As the onramp lets you control your brand and UI, a DEX can build an onramp
widget that uses Stripe’s ability to process fiat into select cryptocurrencies.
The DEX can then complete the final exchange to arbitrary currencies. A DEX can
also build an onramp widget for a specific token. For example, a DAO might
endorse a specific liquidity pool and use a DEX to distribute their tokens and
onboard new users with fiat.

In these cases, consider specifying the following:

- `wallet_addresses`: Use the wallet address already in use.
- `destination_networks`: Set to the selected network.
- `destination_currencies`: Restrict to the selected cryptocurrency.
- `destination_network`: Set to the selected network (required if you want to
set the amount).
- `destination_currency`: Set to the target currency (required if you want to
set the amount).
- `destination_amount`: Set only if you can collect the user’s intent ahead of
time—leave blank for Stripe to suggest smart default values.

The following code example shows the creation of an onramp session using several
of these parameters:

```
curl -X POST https://api.stripe.com/v1/crypto/onramp_sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "customer_ip_address"="8.8.8.8" \
 -d "wallet_addresses[ethereum]"="0xB00F0759DbeeF5E543Cc3E3B07A6442F5f3928a2" \
 -d "destination_networks[]"="ethereum" \
 -d "destination_currencies[]"="eth" \
 -d "destination_network"="ethereum" \
 -d "destination_currency"="eth"
```