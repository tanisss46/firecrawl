# B2B Payments integration guide

## Build a B2B Payments integration with Issuing.

Build a US B2B Payments integration by using Stripe
[Issuing](https://docs.stripe.com/issuing/how-issuing-works) to create cards for
your business, employees, or contractors to make purchases on your behalf.

By the end of this guide, you’ll know how to:

- Fund your Issuing Balance
- Create virtual cards for your own business
- Use these cards to spend funds from your Issuing Balance

## Before you begin

- Sign up for a [Stripe account](https://dashboard.stripe.com/register).
- [Activate Issuing test
mode](https://dashboard.stripe.com/test/issuing/overview) in the Dashboard.
[Add
funds](https://docs.stripe.com/baas/start-integration/integration-guides/b2b-payments#add-funds)
To spend money using cards, add funds to the Issuing balance on your account.
This balance represents funds reserved for Issuing and is safely separated from
your earnings, payouts, and funds from other Stripe products.

You can add funds from your
[Dashboard](https://dashboard.stripe.com/balance/overview#issuing-summary) or
using the [create top-up](https://docs.stripe.com/api/topups/create) endpoint.

```
curl https://api.stripe.com/v1/topups \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d destination_balance=issuing \
 -d amount=2000 \
 -d currency=usd \
 -d description="Top-up for Issuing, March 9, 2025" \
 -d statement_descriptor=Top-up
```

[Create cardholders and
cards](https://docs.stripe.com/baas/start-integration/integration-guides/b2b-payments#create-cardholders-cards)
### Create a cardholder

The [Cardholder](https://docs.stripe.com/api/#issuing_cardholder_object) is the
company or business entity that’s authorized to use card funding by the Issuing
balance. The `Cardholder` object includes relevant details, such as a
[name](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-name)
to display on cards and a
[billing](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-billing)
address, which is usually the business address.

The following API call creates a new `Cardholder`:

```
curl https://api.stripe.com/v1/issuing/cardholders \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Company Card" \
 --data-urlencode email="company@example.com" \
 --data-urlencode phone_number="+18008675309" \
 -d status=active \
 -d type=company \
 -d "billing[address][line1]"="123 Main Street" \
 -d "billing[address][city]"="San Francisco" \
 -d "billing[address][state]"=CA \
 -d "billing[address][postal_code]"=94111 \
 -d "billing[address][country]"=US
```

Stripe returns a `Cardholder` object that contains the information you provided
and sends the `issuing_cardholder.created` webhook event.

### Create a card

Create a card and attach it to the `Cardholder` that you want to make the
authorized user of the card.

In the following examples, we show you how to create a [virtual
card](https://docs.stripe.com/issuing/cards/virtual). You can, however, create
[physical cards](https://docs.stripe.com/issuing/cards/physical) and ship them
to cardholders in live mode.

```
curl https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d currency=usd \
 -d type=virtual \
 -d cardholder={{CARDHOLDER_ID}}
```

Stripe returns a `Card` object on creation, and sends the `issuing_card.created`
webhook event:

```
{
 "id": "ic_1NvPjF2SSJdH5vn2OVbE7r0b",
 "object": "issuing.card",
 "brand": "Visa",
 ...
 "status": "inactive",
 "type": "virtual"
}
```

You need to activate the card before a user can use it. While you can activate
virtual cards in the same API call you used to create it, you must activate
physical cards separately. When ready, activate the card by marking the `status`
as `active`:

```
curl https://api.stripe.com/v1/issuing/cards/ic_1NvPjF2SSJdH5vn2OVbE7r0b \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d status=active
```

At this point, there’s now an active card attached to a cardholder. See the
[Issuing page](https://dashboard.stripe.com/issuing/overview) to view the card
and cardholder information.

```
{
 "id": "ic_1NvPjF2SSJdH5vn2OVbE7r0b",
 "object": "issuing.card",
 "brand": "Visa",
 ...
 "status": "active",
 "type": "virtual",
}
```

To learn more, see:

- [Virtual cards](https://docs.stripe.com/issuing/cards/virtual)
- [Physical cards](https://docs.stripe.com/issuing/cards/physical)
- [Use the Dashboard for Issuing with
Connect](https://docs.stripe.com/issuing/connect#using-dashboard-issuing)
- [Create cards with the API](https://docs.stripe.com/api/issuing/cards)
[Use the
card](https://docs.stripe.com/baas/start-integration/integration-guides/b2b-payments#use-card)
### Create an authorization

To observe the impact of card activity on the associated balance, generate a
test authorization. You can do this in the **Issuing page** of the Dashboard, or
with the following call to the [Authorization
API](https://docs.stripe.com/api/issuing/authorizations):

```
curl https://api.stripe.com/v1/test_helpers/issuing/authorizations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d card={{CARD_ID}} \
 -d amount=1000 \
 -d authorization_method=chip \
 -d "merchant_data[category]"=taxicabs_limousines \
 -d "merchant_data[city]"="San Francisco" \
 -d "merchant_data[country]"=US \
 -d "merchant_data[name]"="Rocket Rides" \
 -d "merchant_data[network_id]"=1234567890 \
 -d "merchant_data[postal_code]"=94107 \
 -d "merchant_data[state]"=CA
```

After approval, Stripe creates an `Authorization` in a `pending` state while it
waits for [capture](https://docs.stripe.com/issuing/purchases/transactions).
Note the authorization `id` that you’ll use to capture the funds:

```
{
 "id": "iauth_1NvPyY2SSJdH5vn2xZQE8C7k",
 "object": "issuing.authorization",
 "amount": 1000,
 ...
 "status": "pending",
 "transactions": [],
}
```

### Capture the funds

Capture the funds using the following code:

```
curl -X POST
https://api.stripe.com/v1/test_helpers/issuing/authorizations/{{AUTHORIZATION_ID}}/capture
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

After the authorization is captured, Stripe creates an Issuing
[Transaction](https://docs.stripe.com/issuing/purchases/transactions), the
`status` of the authorization is set to `closed`.

## See also

- [Handling real-time auth
webhooks](https://docs.stripe.com/issuing/controls/real-time-authorizations)
- [Spending
controls](https://docs.stripe.com/issuing/controls/spending-controls)
- [Issuing
authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
- [Issuing transactions](https://docs.stripe.com/issuing/purchases/transactions)
- [Testing Issuing](https://docs.stripe.com/issuing/testing)
- [Working with Stripe Issuing cards and
Treasury](https://docs.stripe.com/treasury/account-management/issuing-cards)
- [Manage transaction fraud](https://docs.stripe.com/issuing/manage-fraud)
- [Issue regulated customer
notices](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices)

## Links

- [BaaS for SaaS
Platforms](https://stripe.com/guides/introduction-to-banking-as-a-service)
- [Issuing](https://docs.stripe.com/issuing/how-issuing-works)
- [Stripe account](https://dashboard.stripe.com/register)
- [Activate Issuing test
mode](https://dashboard.stripe.com/test/issuing/overview)
- [Dashboard](https://dashboard.stripe.com/balance/overview#issuing-summary)
- [create top-up](https://docs.stripe.com/api/topups/create)
- [Cardholder](https://docs.stripe.com/api/#issuing_cardholder_object)
-
[name](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-name)
-
[billing](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-billing)
- [virtual card](https://docs.stripe.com/issuing/cards/virtual)
- [physical cards](https://docs.stripe.com/issuing/cards/physical)
- [Issuing page](https://dashboard.stripe.com/issuing/overview)
- [Use the Dashboard for Issuing with
Connect](https://docs.stripe.com/issuing/connect#using-dashboard-issuing)
- [Create cards with the API](https://docs.stripe.com/api/issuing/cards)
- [Authorization API](https://docs.stripe.com/api/issuing/authorizations)
- [capture](https://docs.stripe.com/issuing/purchases/transactions)
- [Handling real-time auth
webhooks](https://docs.stripe.com/issuing/controls/real-time-authorizations)
- [Spending
controls](https://docs.stripe.com/issuing/controls/spending-controls)
- [Issuing
authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
- [Testing Issuing](https://docs.stripe.com/issuing/testing)
- [Working with Stripe Issuing cards and
Treasury](https://docs.stripe.com/treasury/account-management/issuing-cards)
- [Manage transaction fraud](https://docs.stripe.com/issuing/manage-fraud)
- [Issue regulated customer
notices](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices)