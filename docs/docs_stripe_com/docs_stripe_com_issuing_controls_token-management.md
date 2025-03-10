# Token Management

## Learn how to use Issuing to manage network tokens on your cards.

## About tokens

Tokens are virtual representations of issued cards that are created when a
cardholder:

- Adds a card to a digital wallet like Apple Pay or Google Pay
- Saves a payment method for their account at an online storefront or
intermediary payment method

Customers can use tokens for payment, and they don’t expose sensitive card
information every time they use them. As such, they function as substitutes for
card details including the number, expiration date, and verification code,
reducing the risk of stolen card information because of a transaction or a
fraudulent actor. Because they don’t expose sensitive card information, tokens
are generally considered a more secure form of payment than physical cards, or
the manual entry of card details into a checkout form.

Tokens are most relevant for users that:

- Allow their cardholders to spend using Apple Pay, Google Pay, or Samsung Pay
- Have significant issuing volume on Card Not Present transactions (like online
purchases)
- Want to incorporate token behavior into their business logic

## Token management

Stripe Issuing allows you to view and manage details associated with all tokens
issued through your program with the [Tokens
API](https://docs.stripe.com/api/issuing/tokens). We provide these details to
help you better understand the characteristics of your tokens and how they’re
being used. For example, you can find details on the following key
characteristics:

- **The originator of a token:** Whether a [digital wallet provider or
business](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-wallet_provider)
is requesting the token.
- **The predicted riskiness of a token:** The card network’s assessment of
[risk](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-visa-token_risk_score)
and its
[recommendation](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-wallet_provider-suggested_decision)
for a given token.
- **The device associated with a token:** Whether a watch, phone, or other
[device](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-device-type)
is requesting the token, and the [assessed
risk](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-wallet_provider-device_trust_score)
of that device.
- **The cardholder characteristics of the token originator:** Whether the
cardholder values such as the
[name](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-wallet_provider-cardholder_name)
and
[address](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-wallet_provider-cardholder_address)
match those of the cardholder in Stripe for additional verification.

In addition to visibility into token characteristics, the Tokens API allows you
to activate, suspend, or deactivate tokens based on your desired workflows. For
example, you might opt to do so to:

- Verify which existing tokens migrate to a new card when your program replaces
a card.
- Deactivate tokens suspected of fraudulent activity without impacting the
underlying card.

The `issuing.authorization` object also has a [token
field](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-token)
that populates if it uses a token.

## Risk controls

When Stripe receives a tokenization request, we assess a variety of variables to
determine whether or not we should approve the request. As a result of this
assessment, we choose one of the following:

- Approve the tokenization request, creating the token and adding it to a
digital wallet.
- Require additional authentication, triggering a one-time passcode flow through
the digital wallet provider. After the authentication successfully completes, we
create the token and add it to the corresponding digital wallet. In these
scenarios, the [status
field](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-status)
is populated as `requested` until the additional authentication completes.
- Reject the tokenization request, preventing the token from being created.

Users also have the ability to put their own additional risk controls in place
on top of Stripe’s. The Tokens API doesn’t allow for the outright rejection of a
tokenization request at the point of creation, but users can deactivate or
suspend tokens shortly after creation.

## How tokens work

Understand how tokens work to give yourself a picture of token creation and the
token lifecycle.

### Create a token

Token creation, or tokenization, is a multi-step process involving cardholders,
users, a digital wallet provider, Stripe, and a card network. The example
scenario below shows the steps the cardholder must complete and the processes
involved when using the Tokens API as part of your program.

#### Example scenario

A cardholder on your Issuing program wants to add their Stripe-issued card to a
digital wallet, such as Apple Pay. To do so, they open their digital wallet app
and complete prompts to enter their cardholder information (such as name and
billing address), and card information (such as card number and expiration
date).

This information is then submitted to the wallet provider, (in this case, Apple
Pay) which is registered with the card’s underlying network (for example, Visa
or Mastercard) as a ‘token requestor’ within the network. Next, the card network
conducts a series of validations against this data, combines it with their own
data into a tokenization request, and forwards it to Stripe to decide. Stripe
conducts its own additional validation to determine how to proceed with the
request. As noted earlier on this page, this validation step can result in three
outcomes:

- Stripe approves the tokenization, which activates the token in the wallet,
making it ready to use. Stripe sends out the `issuing_token.created` event to
any listening webhook endpoints.
- Stripe requires additional verification, which prompts an authentication
challenge to the cardholder. Stripe sends out the `issuing_token.created` event
to any listening webhook endpoints. The token becomes active when the cardholder
successfully completes this step. Stripe sends out the `issuing_token.updated`
event to any listening webhook endpoints as soon as the token becomes activated.
- Stripe declines the tokenization request, which prevents the token from being
added to the wallet. Stripe doesn’t send out the `issuing_token.created` event
to any listening webhook endpoints.

The wallet provider or the card network can halt a tokenization request from
proceeding further at any step in the tokenization process—Stripe doesn’t always
receive notification when this happens.

The sequence diagram below helps to further illustrate the tokenization process.

Cardholder

Device (for example, smartphone)

Wallet provider (for example, Apple Pay)

Card network (for example, Visa)

Stripe

Submit card information

Forward data

Send provisioning data

Send provisioning request

Send approved provisioning response

issuing_token.created
Finalize provisioning response

Forward provisioning response

Token is ready for use in wallet

Overview flow of a successful provisioning request
### Token lifecycle

After a token is created, it can exist in four distinct states in the digital
wallet:

- **Inactive**: The token request is outstanding, and the token can’t be used
for authorizations yet. An inactive token in the Tokens API has a status of
`requested`.
- **Suspended**: The token is temporarily unavailable to use in the wallet. A
cardholder or a Stripe user using the Tokens API can trigger a token suspension.
Cardholders can’t undo suspensions by a Stripe user (that is, through a digital
wallet app). Users can only reactivate suspended cards directly through the
Tokens API.
- **Active**: The token is available for use in the wallet it’s been added to.
- **Deleted**: The token has been removed from the wallet and you can no longer
use it. You can’t modify tokens in this state.

The below state diagram helps show the different states, how they’re reflected
in the API, and how you can use our APIs to modify them.

Inactive

`requested`

Active

`active`

Suspended

`suspended`

Deleted

`deleted`

cardholder onlycardholder or Stripecardholder or Stripecardholder or
Stripecardholder (if they initiated suspension) or Stripetoken lifecycle state
diagram
Stripe automatically synchronizes token status with the cardholder states and
card states when they change. Stripe also migrates tokens between card
replacements if the original card isn’t canceled first. To see which tokens are
associated with which card, use the [List
API](https://docs.stripe.com/api/issuing/tokens/list).

### Merchant tokens

Businesses can also create tokens when saving a payment method for future use at
a retailer (for example, a cardholder saving their card details for checkout at
Amazon). In these scenarios, the business originates the token creation, and the
Tokens API won’t have the [wallet_provider
field](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-wallet_provider).
To assess the underlying business that originated the token, we recommend
examining the [business
details](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data)
associated with authorizations conducted using the token. If you issue cards
from MasterCard, tokens that originate from them might populate a readable name
in the [network_data.mastercard.token_requestor_name
field](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-mastercard-token_requestor_name).

Merchant tokens are tied to the specific business (token requestor in the card
network) that originates them and can’t be used at other businesses.

### Identify when a token was used for a transaction

Authorizations or Transactions that used a token have an expandable reference to
the Token object in the `token` attribute. This field is null for Authorizations
or Transactions that didn’t use a token. Combine this with the `wallet`
attribute on the Authorization or Transaction object, or the
[wallet_provider](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-wallet_provider)
attribute on the Token object, to determine whether a digital wallet token was
used.

See the
[Authorizations](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-token)
and
[Transactions](https://docs.stripe.com/api/issuing/transactions/object#issuing_transaction_object-token)
API documentation for more details.

## Network data restrictions

The Issuing token object contains an optional, [expandable
field](https://docs.stripe.com/api/expanding_objects) called
[network_data](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data).
It contains additional, sensitive card network details about your tokens,
primarily related to the token creation process. Because this data is highly
sensitive, you must have a [restricted access
key](https://docs.stripe.com/keys#create-restricted-api-secret-key) with the
necessary permissions to access the data, and can only view the data on a token
within the first 24 hours after token creation (based on the **created** value).
This data is only available in the API to [retrieve a
token](https://docs.stripe.com/api/issuing/tokens/retrieve) and the API to
[update a token status](https://docs.stripe.com/api/issuing/tokens/update).

To access this data, configure your restricted access keys with the following
permissions:

- Issuing tokens read access for Retrieve and List methods
- Issuing tokens write access for the Update Status method
- Issuing token network data read access for accessing **network_data** within
the 24 hour time limit

If you need access to **network_data** beyond the initial 24-hour period that
it’s available for, you must [limit the IP
addresses](https://docs.stripe.com/keys#limit-api-secret-keys-ip-address) from
which your restricted access keys will use.

## Testing

An Issuer’s cardholder can create tokens for free at storefronts or in digital
wallets. We recommend creating one in a digital wallet of your choice to
understand the webhook events, API fields, and effects of updating a token. To
do so, follow the [Digital Wallets
guide](https://docs.stripe.com/issuing/cards/digital-wallets) for manual
provisioning first.

If you prefer to test Tokens API in test mode, you can create a test mode
authorization with the [wallet
field](https://docs.stripe.com/api/issuing/authorizations/test_mode_create#test_mode_create_authorization-wallet)
set to one of the available choices. The **token** field is set on the resulting
authorization. You can then use the API methods on this token as normal. In
these scenarios, not all fields are set, including **network_data**, and this
token isn’t used for subsequent test authorizations.

## The Tokens API

Token data is only accessible through the Tokens API. Below are a few examples
applications.

### Verify a successful manual provisioning example

- In this example, you subscribe to the `issuing_token.created` and
`issuing_token.updated` events.
- When you receive an `issuing_token.created` event, use the Retrieve API and
expand **network_data** to look at provisioning details. Here’s an example:

```
{
 "id": "evt_1NxBn3FUQNp5XJkna0rkKU2r",
 "object": "event",
 "api_version": "2025-02-24.acacia",
 "created": 1691100189,
 "data": {
 "object": {
 "id": "intok_1NuMIZFUQNp5XJknPmDzEz0t",
 "object": "issuing.token",
 "card": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
 "created": 1691100179,
 "device_fingerprint": "intd_1JDmgz2OpvKigH2CxnEEs",
 "last4": "9203",
 "livemode": true,
 "network": "mastercard",
 "network_updated_at": 1691100170,
 "status": "requested",
 "wallet_provider": "apple_pay"
 }
 },
 "livemode": true,
 "pending_webhooks": 0,
 "request": {
 "id": "req_ARTvFhTufhHna9",
 "idempotency_key": "49a40678-8f45-4c91-9d6f-98a5bd569f9d"
 },
 "type": "issuing_token.created"
}
```

- Check that the **wallet_provider** field is populated, which tells you that it
originates from a digital wallet, and take note of the object’s **id**. Use that
in the Retrieve API call:

```
curl https://api.stripe.com/v1/issuing/tokens/intok_1NuMIZFUQNp5XJknPmDzEz0t \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "expand[]"=network_data \
 -G
```

This yields the following response:

```
{
 "id": "intok_1NuMIZFUQNp5XJknPmDzEz0t",
 "object": "issuing.token",
 "card": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
 "created": 1691100159,
 "device_fingerprint": "intd_1JDmgz2OpvKigH2CxnEEs",
 "last4": "9203",
 "livemode": true,
 "network": "mastercard",
 "network_data": {
 "device": {
 "device_fingerprint": "intd_1JDmgz2OpvKigH2CxnEEs",
 "ip_address": null,
 "location": "+30.22/-89.10",
 "name": "AB's phone",
 "phone_number": null,
 "type": "phone"
 },
 "mastercard": {
 "card_reference_id": "...",
 "token_reference_id": "...",
 "token_requestor_id": "...",
 "token_requestor_name": "APPLE PAY"
 },
 "type": "mastercard",
 "wallet_provider": {
 "account_id": null,
 "account_trust_score": null,
 "card_number_source": "manual",
 "cardholder_address": null,
 "cardholder_name": null,
 "device_trust_score": null,
 "hashed_account_email_address": null,
 "reason_codes": [],
 "suggested_decision": null,
 "suggested_decision_version": null
 }
 },
 "network_updated_at": 1691100170,
 "status": "requested",
 "wallet_provider": "apple_pay"
}
```

- In the example, **card_number_source** is `manual`, token **status** is
`requested`, and it’s an Apple Pay wallet. This means the cardholder had the
card details with them when they put the card in their Apple Wallet, and they
need to complete additional verification before they can use the card in the
wallet.
- A few seconds later, you can see an `issuing_token.updated` event for the same
token. The token status is now in the `active` state. This means the cardholder
successfully completed the verification and can use their card for Apple Pay.

### Delete a suspicious merchant token example

- In this example, you subscribe to the `issuing_token.created` event.
- The webhook receives an `issuing_token.created` event.

```
{
 "object": {
 "id": "intok_1NuMIZuTQ2hhXJooNmDzEz0t",
 "object": "issuing.token",
 "card": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
 "created": 1691100179,
 "device_fingerprint": null,
 "last4": "9203",
 "livemode": true,
 "network": "visa",
 "network_updated_at": 1691100170,
 "status": "active"
 }
}
```

- The token has no **wallet_provider** field, so it’s a merchant token. Use the
Retrieve API and expand **network_data** to look at provisioning details.

```
curl https://api.stripe.com/v1/issuing/tokens/intok_1NuMIZFUQNp5XJknPmDzEz0t \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "expand[]"=network_data \
 -G
```

This yields the response:

```
{
 "id": "intok_1NuMIZFUQNp5XJknPmDzEz0t",
 "object": "issuing.token",
 "card": "ic_1JDmgz2eZvKYlo2CRXlTsXj6",
 "created": 1691100186,
 "device_fingerprint": null,
 "last4": "4674",
 "livemode": true,
 "network": "visa",
 "network_data": {
 "visa": {
 // ...other fields
 },
 "type": "visa",
 "wallet_provider": {
 "card_number_source": "manual",
 "cardholder_address": null,
 "cardholder_name": "abc",
 // ...other fields
 }
 },
 "network_updated_at": 1691100170,
 "status": "active",
}
```

- You can see that the cardholder name is an invalid value that doesn’t match
the expected cardholder name.
- To avoid any fraudulent activity, use the Update Status API to delete the
token before it can be used. Then follow up with the cardholder to see if the
token was actually requested by them. If they didn’t request it, cancel and
replace the card if the number was stolen, or the account compromised.

```
curl https://api.stripe.com/v1/issuing/tokens/intok_1NuMIZFUQNp5XJknPmDzEz0t \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d status=deleted
```

### Device monitoring example

As with the previous examples, subscribe to the token events, and perform a
Retrieve API request on the ID when you receive an event. In this case, you see
that a **device_fingerprint** is populated, and check the
**network_data.device.location** field. You see that the device was provisioned
in a different country using the location coordinates. You see that you received
prior notice that this cardholder was traveling abroad, and that it matches the
country that they specified they were traveling to.

## Links

- [Tokens API](https://docs.stripe.com/api/issuing/tokens)
- [digital wallet provider or
business](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-wallet_provider)
-
[risk](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-visa-token_risk_score)
-
[recommendation](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-wallet_provider-suggested_decision)
-
[device](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-device-type)
- [assessed
risk](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-wallet_provider-device_trust_score)
-
[name](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-wallet_provider-cardholder_name)
-
[address](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-wallet_provider-cardholder_address)
- [token
field](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-token)
- [status
field](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-status)
- [List API](https://docs.stripe.com/api/issuing/tokens/list)
- [business
details](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data)
- [network_data.mastercard.token_requestor_name
field](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data-mastercard-token_requestor_name)
-
[Transactions](https://docs.stripe.com/api/issuing/transactions/object#issuing_transaction_object-token)
- [expandable field](https://docs.stripe.com/api/expanding_objects)
-
[network_data](https://docs.stripe.com/api/issuing/tokens/object#issuing_token_object-network_data)
- [restricted access
key](https://docs.stripe.com/keys#create-restricted-api-secret-key)
- [retrieve a token](https://docs.stripe.com/api/issuing/tokens/retrieve)
- [update a token status](https://docs.stripe.com/api/issuing/tokens/update)
- [limit the IP
addresses](https://docs.stripe.com/keys#limit-api-secret-keys-ip-address)
- [Digital Wallets guide](https://docs.stripe.com/issuing/cards/digital-wallets)
- [wallet
field](https://docs.stripe.com/api/issuing/authorizations/test_mode_create#test_mode_create_authorization-wallet)