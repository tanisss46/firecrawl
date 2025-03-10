# Working with Stripe Issuing cards

## Learn how to integrate Stripe Issuing with Treasury.

[Stripe Issuing](https://docs.stripe.com/issuing) lets you create physical and
virtual cards using a financial account as the source of funds.

[Enable Issuing on connected
accounts](https://docs.stripe.com/treasury/account-management/issuing-cards#enable)
Request the `card_issuing` [account
capability](https://docs.stripe.com/connect/account-capabilities) for the
connected accounts on your platform and provide the [required
information](https://docs.stripe.com/issuing/connect#required-verification-information)
for onboarding.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "capabilities[treasury][requested]"=true \
 -d "capabilities[card_issuing][requested]"=true \
 -d "capabilities[transfers][requested]"=true
```

If successful, the response returns the connected account [Account
object](https://docs.stripe.com/api/accounts/object) with the `capabilities`
hash listing the requested capabilities as `active`.

If you haven’t already, also request access to the `card_issuing` feature on the
financial account.

```
curl
https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "treasury[access][requested]"=true \
 -d "card_issuing[access][requested]"=true
```

If successful, the response returns the financial account object with the
features listed in the `active_features` or `pending_features` array.

[Create a
card](https://docs.stripe.com/treasury/account-management/issuing-cards#create-card)
After the `card_issuing` capability is active, the sellers and service providers
that own your platform’s connected accounts can create cardholders and cards.
You can issue cards only through the API.

A [Cardholder object](https://docs.stripe.com/api/#issuing_cardholder_object)
represents an individual or business entity that you can issue cards to. You can
begin by creating a `Cardholder` with name, billing information, and whether
they’re an `individual` or `company`.

```
curl https://api.stripe.com/v1/issuing/cardholders \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d name="Jenny Rosen" \
 --data-urlencode email="jenny.rosen@example.com" \
 --data-urlencode phone_number="+18008675309" \
 -d status=active \
 -d type=individual \
 -d "individual[first_name]"=Jenny \
 -d "individual[last_name]"=Rosen \
 -d "individual[dob][day]"=1 \
 -d "individual[dob][month]"=11 \
 -d "individual[dob][year]"=1981 \
 -d "billing[address][line1]"="1234 Main Street" \
 -d "billing[address][city]"="San Francisco" \
 -d "billing[address][state]"=CA \
 -d "billing[address][postal_code]"=94111 \
 -d "billing[address][country]"=US
```

If successful, the response returns the newly created `Cardholder` object.

Create a [Card](https://docs.stripe.com/api/#issuing_card_object) and assign it
to both the `Cardholder` you just created and a financial account. To assign the
cardholder and financial account, specify the cardholder ID in the `cardholder`
parameter and the financial account ID in the `financial_account` parameter of
the `/v1/issuing/cards` request.

```
curl https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d cardholder={{CARDHOLDER_ID}} \
 -d financial_account={{FINANCIAL_ACCOUNT_ID}} \
 -d currency=usd \
 -d type=virtual \
 -d status=active
```

If successful, the response returns the newly created `Card` object.

[Handle
authorizations](https://docs.stripe.com/treasury/account-management/issuing-cards#handle-auth)
Review the [Issuing
authorizations](https://docs.stripe.com/issuing/purchases/authorizations) guide
to properly handle authorizations.

### Create test authorizations

You can test the cards you just issued by following the steps in [Testing
Issuing](https://docs.stripe.com/issuing/testing) to simulate purchases.

If the financial account associated with the issued card has
[outbound_flows](https://docs.stripe.com/api/treasury/financial_accounts/create#create_financial_account-platform_restrictions-outbound_flows)
restricted, authorizations on the card aren’t allowed.

See the [Issuing
transactions](https://docs.stripe.com/issuing/purchases/transactions#handling-other-transactions)
guide for information on different transaction types you might test against.

[Handle captures and
refunds](https://docs.stripe.com/treasury/account-management/issuing-cards#capture)
See the [Issuing
transactions](https://docs.stripe.com/issuing/purchases/transactions) guide to
learn how to handle refunds and captures.

[Handle
disputes](https://docs.stripe.com/treasury/account-management/issuing-cards#disputes)
See the [Issuing disputes](https://docs.stripe.com/issuing/purchases/disputes)
guide to learn how to properly handle disputes.

## Links

- [Stripe Issuing](https://docs.stripe.com/issuing)
- [account capability](https://docs.stripe.com/connect/account-capabilities)
- [required
information](https://docs.stripe.com/issuing/connect#required-verification-information)
- [Account object](https://docs.stripe.com/api/accounts/object)
- [Cardholder object](https://docs.stripe.com/api/#issuing_cardholder_object)
- [Card](https://docs.stripe.com/api/#issuing_card_object)
- [Issuing
authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
- [Testing Issuing](https://docs.stripe.com/issuing/testing)
-
[outbound_flows](https://docs.stripe.com/api/treasury/financial_accounts/create#create_financial_account-platform_restrictions-outbound_flows)
- [Issuing
transactions](https://docs.stripe.com/issuing/purchases/transactions#handling-other-transactions)
- [Issuing transactions](https://docs.stripe.com/issuing/purchases/transactions)
- [Issuing disputes](https://docs.stripe.com/issuing/purchases/disputes)