# Stripe Connect and the Charges API

#### Legacy API

The content of this section refers to a Legacy feature. Use the [Payment Intents
API](https://docs.stripe.com/payments/accept-a-payment) instead.

The Charges API doesn’t support the following features, many of which are
required for credit card compliance:

- Merchants in India
- [Bank requests for card
authentication](https://docs.stripe.com/payments/cards/overview)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)

Learn how [Connect](https://docs.stripe.com/connect) lets you make charges and
issue transfers for [connected
accounts](https://docs.stripe.com/connect/accounts). How you configure these
options determines your Stripe fees.

Connect supports [three approaches to creating payments for a connected
account](https://docs.stripe.com/connect/charges). For more information about
the different types of Connect charges, see [the documentation on choosing an
approach](https://docs.stripe.com/connect/charges#types). Stripe fees are
determined by how you configure these options.

This page explains only how to make calls to the Charges API for connected
accounts. Check the linked pages for more information about calls to other APIs
for related operations.

## Direct charges

To create a direct charge on the connected account, create a Charge object and
add the `Stripe-Account` header with a value of the connected account ID:

```
curl https://api.stripe.com/v1/charges \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d amount=1000 \
 -d currency=usd \
 -d source=tok_visa
```

This example uses a [test
token](https://docs.stripe.com/testing#cards)—**tok_visa**—but you could
tokenize a test card using [Stripe.js and
Elements](https://docs.stripe.com/payments/elements) instead.

See [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment-charges) for more
details.

### Collect application fees on direct charges

With Connect, your platform can take an application fee on direct charges. To
assess an application fee on a charge, pass an optional `application_fee_amount`
value as a positive integer:

```
curl https://api.stripe.com/v1/charges \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d amount=1000 \
 -d currency=usd \
 -d source=tok_visa \
 -d application_fee_amount=123
```

See [Direct charges](https://docs.stripe.com/connect/direct-charges) for
information on transfer availability, refunds, and so on.

## Destination charges

To create a destination charge, pass the connected account’s ID in the
`transfer_data[destination]` attribute:

```
curl https://api.stripe.com/v1/charges \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d source=tok_visa \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}
```

This example uses a [test
token](https://docs.stripe.com/testing#cards)—**tok_visa**—but you could
tokenize a test card using [Stripe.js and
Elements](https://docs.stripe.com/payments/elements) instead.

See [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment-charges) for more
details.

### Collect fees on destination charges with application_fee_amount

When creating destination charges with an `application_fee_amount`, the full
charge amount is immediately transferred from the platform to the
`transfer_data[destination]` account after the charge is captured. The
`application_fee_amount` (capped at the full amount of the charge) is then
transferred back to the platform.

```
curl https://api.stripe.com/v1/charges \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d source=tok_visa \
 -d application_fee_amount=123 \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}
```

To provide a better reporting experience, an application fee object is created
after the application fee is collected. Use the `amount` property on the
application fee object for reporting. You can then access these objects with the
[Application Fees](https://docs.stripe.com/api/application_fees/list) endpoint.

### Collect fees on destination charges with transfer_data[amount]

You can also take a fee by using
[transfer_data[amount]](https://docs.stripe.com/api/charges/object#charge_object-transfer_data-amount).

The `transfer_data[amount]` is a positive integer reflecting the amount of the
charge that’s transferred to the `transfer_data[destination]`. You subtract your
platform’s fees from the charge amount, then pass the result of this calculation
as the `transfer_data[amount]`:

```
curl https://api.stripe.com/v1/charges \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d source=tok_visa \
 -d "transfer_data[amount]"=877 \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}
```

See [Destination charges](https://docs.stripe.com/connect/destination-charges)
for information on transfer availability, refunds, and so on.

## Separate charges and transfers

#### Caution

You can only use separate charges and transfers if both your platform and the
connected account are in the same region. For example, if your platform account
is in Europe, the connected needs to be in Europe too.

To create a charge and set up the associated transfer, create a `transfer_group`
and assign the charge to the `transfer_group`.

```
# Create a Charge:
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=10000 \
 -d "currency"="usd" \
 -d "source"="tok_visa" \
 -d "transfer_group"="{ORDER10}"
```

```
# Create a Transfer to a connected account (later):
curl https://api.stripe.com/v1/transfers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=7000 \
 -d "currency"="usd" \
 -d "destination"="{{CONNECTED_STRIPE_ACCOUNT_ID}}" \
 -d "transfer_group"="{ORDER10}"
```

```
# Create a second Transfer to another connected account (later):
curl https://api.stripe.com/v1/transfers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=2000 \
 -d "currency"="usd" \
 -d "destination"="{{OTHER_CONNECTED_STRIPE_ACCOUNT_ID}}" \
 -d "transfer_group"="{ORDER10}"
```

This example uses a [test
token](https://docs.stripe.com/testing#cards)—**tok_visa**—but you could
tokenize a test card using [Stripe.js and
Elements](https://docs.stripe.com/payments/elements) instead.

See [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment-charges) for more
information.

### Using on_behalf_of with separate charges and transfers

With separate charges and transfers, by default:

- Charges are settled in the platform’s country
- The fee structure for the platform’s country is used
- The platform’s information is displayed on the customer’s credit card
statement

To use the connected account’s country and to display their information instead,
use the `on_behalf_of` argument.

#### Caution

You can only use `on_behalf_of` with separate charges and transfers for
connected accounts with the
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments)
capability.

```
curl https://api.stripe.com/v1/charges \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d source=tok_visa \
 -d on_behalf_of={{CONNECTED_ACCOUNT_ID}}
```

See [Creating separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) for
information on transfer availability, refunds, and so on.

## Links

- [Payment Intents API](https://docs.stripe.com/payments/accept-a-payment)
- [Bank requests for card
authentication](https://docs.stripe.com/payments/cards/overview)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [Connect](https://docs.stripe.com/connect)
- [connected accounts](https://docs.stripe.com/connect/accounts)
- [three approaches to creating payments for a connected
account](https://docs.stripe.com/connect/charges)
- [the documentation on choosing an
approach](https://docs.stripe.com/connect/charges#types)
- [test token](https://docs.stripe.com/testing#cards)
- [Stripe.js and Elements](https://docs.stripe.com/payments/elements)
- [Accept a payment](https://docs.stripe.com/payments/accept-a-payment-charges)
- [Direct charges](https://docs.stripe.com/connect/direct-charges)
- [Application Fees](https://docs.stripe.com/api/application_fees/list)
-
[transfer_data[amount]](https://docs.stripe.com/api/charges/object#charge_object-transfer_data-amount)
- [Destination charges](https://docs.stripe.com/connect/destination-charges)
-
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments)
- [Creating separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)