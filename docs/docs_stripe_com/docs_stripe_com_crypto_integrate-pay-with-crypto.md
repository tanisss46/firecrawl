# Integrate Pay with CryptoPublic preview

## Start accepting crypto by integrating Pay with Crypto.

[Pay with Crypto](https://docs.stripe.com/crypto/pay-with-crypto) works with
[Checkout](https://docs.stripe.com/payments/checkout),
[Elements](https://docs.stripe.com/payments/elements), or can be directly
integrated through the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents). If you’re a Connect
platform, see [Connect
support](https://docs.stripe.com/crypto/pay-with-crypto#connect-support).

When integrated, the option to pay with crypto appears in your checkout page,
redirecting customers to a page hosted by *crypto.link.com* for payment
completion. There, your customers can connect their wallet, and save and reuse
their account using [Link](https://docs.stripe.com/payments/link). You’re
[immediately
notified](https://docs.stripe.com/payments/payment-methods#payment-notification)
if the payment succeeds or fails. Before you get started, see our Pay with
Crypto [demo](https://buy.stripe.com/test_28o4ig0SY9Xq8co3cc).

![Let your users pay with
crypto](https://b.stripecdn.com/docs-statics-srv/assets/integrate-pay-with-crypto.9c892006170bb95a93c6a94411c3bff9.png)

Let your users pay with crypto

WebMobileStripe-hosted pageAdvanced integrationDirect APIStripe-hosted
pageAdvanced integrationDirect APIiOSAndroid
Before you can enable crypto as a payment method within the prebuilt checkout
page, go to your [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) and request the
**Crypto**. After we review your information and approve you as a user, the
**Crypto** payment method appears as active in the Stripe Dashboard.

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `crypto` to the list of `payment_method_types`.
- Make sure all `line_items` use `usd`.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d mode=payment \
 -d "payment_method_types[0]"=crypto \
 -d "line_items[0][price_data][currency]"=usd \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][unit_amount]"=2000 \
 -d "line_items[0][quantity]"=1 \
 --data-urlencode success_url="https://example.com/success"
```

## Test your integration

Test your Pay with Crypto integration with your test API keys by viewing the
redirect page. You can test the successful payment case by authenticating the
payment on the redirect page. The
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object) transitions
from `requires_action` to `succeeded`.

- In test mode, you’re redirected to a payment page where you can pay with
testnet crypto assets.
- Make sure that your wallet is configured to the test network you intend to pay
over. For example, if you want to pay with USDC on Ethereum, make sure your
wallet is set to Ethereum’s Sepolia test network.

#### Fund your wallet with test assets

You can use testnet “faucets” to top up your wallet. Here are a few:

- [Circle USDC](https://faucet.circle.com/)
- [Paxos USDP](https://faucet.paxos.com/)
- [Devnet SOL](https://faucet.solana.com/)
- [Sepolia ETH](https://faucets.chain.link/sepolia)
- [Amoy POL](https://faucet.polygon.technology/)

## Links

- [Pay with Crypto](https://docs.stripe.com/crypto/pay-with-crypto)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Elements](https://docs.stripe.com/payments/elements)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Connect
support](https://docs.stripe.com/crypto/pay-with-crypto#connect-support)
- [Link](https://docs.stripe.com/payments/link)
- [immediately
notified](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [demo](https://buy.stripe.com/test_28o4ig0SY9Xq8co3cc)
- [payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [Circle USDC](https://faucet.circle.com/)
- [Paxos USDP](https://faucet.paxos.com/)
- [Devnet SOL](https://faucet.solana.com/)
- [Sepolia ETH](https://faucets.chain.link/sepolia)
- [Amoy POL](https://faucet.polygon.technology/)