# Stripe-hosted, standalone onramp quickstartPublic preview

## Customize and generate a redirect URL to the Stripe-hosted, standalone onramp.

Direct users can purchase crypto with a link to the Stripe-hosted, standalone
onramp at [https://crypto.link.com](https://crypto.link.com/). The standalone
onramp redirect URL supports parameter customization and lets you prefill fields
such as the destination currency and the source amount or destination amount.
Share the link by sending it directly to users or by displaying it with a
button, as in the following demo.

You can also generate a redirect URL with code using the `Standalone` function
and passing in the desired fields. See the [standalone onramp extended
guide](https://docs.stripe.com/crypto/onramp/standalone-onramp-guide) to add
more capabilities or customize parameters.

#### Pre-populate the wallet address or embed the onramp

Submit an
[application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication)
to try the [embeddable
version](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide) of the
onramp.

Source amountDestination amountSource amount (USD)Enter the amount of fiat you
want to exchange into crypto$ValueDestination currencySelect a destination
currencyBitcoinEthereumSolanaMaticUSDC (Ethereum)USDC (Polygon)USDC (Solana)
Send users to this URL directly

`https://crypto.link.com?ref=lb` to clipboardLivemode
Example button with redirect URL

[Buy Crypto](https://crypto.link.com/?ref=lb)
Generate a redirect URL with code

```
const standaloneOnramp = window.StripeOnramp.Standalone();
const redirectUrl = standaloneOnramp.getUrl();

return (
 <a href={redirectUrl}>
 Buy Crypto
 </a>
);
```

## Links

- [https://crypto.link.com](https://crypto.link.com)
- [standalone onramp extended
guide](https://docs.stripe.com/crypto/onramp/standalone-onramp-guide)
-
[application](https://dashboard.stripe.com/register?redirect=%2Fcrypto-onramp%2Fapplication)
- [embeddable
version](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide)
- [Buy Crypto](https://crypto.link.com?ref=lb)