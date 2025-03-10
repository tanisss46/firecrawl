# Clone customer payment information across connected accountsLegacy

## Reuse payment information across multiple connected accounts that share customers.

#### Caution

The content of this page describes a legacy feature. Support for it might end
without notice, so if you use this feature, update your integration to use the
current process for reusing payment information across connected accounts. For
more information, see [Share payment methods across multiple
accounts](https://docs.stripe.com/connect/direct-charges-multiple-accounts#clone-and-create-direct-charges).

For some business models, it’s helpful to reuse your customers’ payment
information across connected accounts. For example, a customer who makes a
purchase from one of your connected sellers shouldn’t need to re-enter their
credit card or bank account details to purchase from another seller.

With [Connect](https://docs.stripe.com/connect), you can accomplish this by
following three steps:

- [Storing
customers](https://docs.stripe.com/connect/cloning-customers-across-accounts#storing-customers),
with a payment method, on the platform account.
- [Creating
tokens](https://docs.stripe.com/connect/cloning-customers-across-accounts#creating-tokens)
to clone the payment method when it’s time to charge the customer on behalf of a
connected account.
- [Creating
charges](https://docs.stripe.com/connect/cloning-customers-across-accounts#creating-charges)
using the new tokens.
[Storing
customers](https://docs.stripe.com/connect/cloning-customers-across-accounts#storing-customers)
When not cloning payment methods, you save the Stripe [Customer
objects](https://docs.stripe.com/api#customers) on each individual connected
Stripe account. When cloning payment methods, you instead save them on the
platform Stripe account.

This is an [API call](https://docs.stripe.com/api#create_customer) but be sure
to use your own secret and publishable keys instead of the connect account’s.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode email="paying.user@example.com" \
 -d source=tok_mastercard
```

[Creating
tokens](https://docs.stripe.com/connect/cloning-customers-across-accounts#creating-tokens)
#### Caution

If your platform uses the Sources API, you must [create a Source from that
customer](https://docs.stripe.com/sources/connect#cloning-card-sources) rather
than creating a token. If your platform uses the [Payment Methods
API](https://docs.stripe.com/payments/payment-methods), you must [create a
PaymentMethod from that
customer](https://docs.stripe.com/connect/direct-charges-multiple-accounts#clone-and-create-direct-charges).
After following either of these guides, proceed to [Creating
charges](https://docs.stripe.com/connect/cloning-customers-across-accounts#creating-charges)
without creating a token.

When you’re ready to create a charge on a connected account using a customer
saved on your platform account, [create a new
token](https://docs.stripe.com/api#create_card_token) for that purpose. You’ll
need:

- The Stripe account ID of the connected account (for example,
`acct_sGvLiEp1gxuTGXsT`) that you’re creating the charge for
- The ID of the customer in your platform account (for example,
`cus_RWTsMUKl78vvTi`) being charged
- The card or bank account ID for that customer, if you want to charge a
specific card or bank account rather than the default

```
curl https://api.stripe.com/v1/tokens \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d customer={{CUSTOMER_ID}}
```

[Creating
charges](https://docs.stripe.com/connect/cloning-customers-across-accounts#creating-charges)
With the token generated in the previous step, [attach this token to a
customer](https://docs.stripe.com/api#create_customer) on the connected account.

#### Caution

Charges that are made on the cloned customer aren’t reflected on the original
customer. This feature is intended for multiple connected accounts that need to
charge the same user.

#### Caution

If your platform uses the [Payment Methods
API](https://docs.stripe.com/payments/payment-methods), you must pass the
payment method ID as the `payment_method` parameter instead of passing the
`source` parameter.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d source={{TOKEN_ID}}
```

Then, use the customer ID (for example, `cus_iq7QTdB67h4dwh`) and the payment
method ID (for example, `card_x6zUJjN1r4IpL5`) returned by the
`customers.create` call to charge the customer.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d amount=999 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{PAYMENT_METHOD_ID}}
```

## See also

- [Creating charges](https://docs.stripe.com/connect/charges)
- [Creating direct charges](https://docs.stripe.com/connect/direct-charges)

## Links

- [Share payment methods across multiple
accounts](https://docs.stripe.com/connect/direct-charges-multiple-accounts#clone-and-create-direct-charges)
- [Connect](https://docs.stripe.com/connect)
- [creating direct charges on connected
accounts](https://docs.stripe.com/connect/direct-charges)
- [Customer objects](https://docs.stripe.com/api#customers)
- [API call](https://docs.stripe.com/api#create_customer)
- [create a Source from that
customer](https://docs.stripe.com/sources/connect#cloning-card-sources)
- [Payment Methods API](https://docs.stripe.com/payments/payment-methods)
- [Creating
charges](https://docs.stripe.com/connect/cloning-customers-across-accounts#creating-charges)
- [create a new token](https://docs.stripe.com/api#create_card_token)
- [Creating charges](https://docs.stripe.com/connect/charges)