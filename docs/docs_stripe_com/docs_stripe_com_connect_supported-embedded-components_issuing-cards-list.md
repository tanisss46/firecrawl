# Issuing cards list

## Show a table of all issued cards.

Issuing cards list renders a table view of all the
[cards](https://docs.stripe.com/api/issuing/cards) issued to your connected
accounts.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
The permission boundary for this component is at the connected account level,
not at the individual card level. This UI should be shown to users that have
access to all cards, not to users that have restricted access to a single card.

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
Issuing cards list component by specifying `issuing_cards_list` in the
`components` parameter. You can enable or disable individual features of the
Issuing cards list component by specifying the `features` parameter under
`issuing_cards_list`.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[issuing_cards_list][enabled]"=true \
 -d "components[issuing_cards_list][features][card_management]"=true \
 -d "components[issuing_cards_list][features][cardholder_management]"=true \
-d
"components[issuing_cards_list][features][card_spend_dispute_management]"=true \
 -d "components[issuing_cards_list][features][spend_control_management]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the Issuing cards list component in the front end:

```
// Include this element in your HTML
const issuingCardsList = stripeConnectInstance.create('issuing-cards-list');
issuingCardsList.setShowSpendControls(true);
container.appendChild(issuingCardsList);
```

## Disable Stripe user authentication

Use the
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-issuing_cards_list-features-disable_stripe_user_authentication)
feature to control whether the component requires Stripe user authentication. By
default, this parameter is false. This value can only be true for accounts where
`controller.requirement_collection` is `application`.

We recommend implementing 2FA or equivalent security measures as a [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs).
For account configurations that support this feature, such as Custom accounts,
you assume liability for connected accounts if they can’t pay back [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability).

## Set spending controls

You can use Issuing Connect embedded components to view and, optionally, edit
[spending controls](https://docs.stripe.com/issuing/controls/spending-controls)
on your cards by turning on the Issuing component’s `showSpendControls`
attribute.

```
const issuingCardsList = stripeConnectInstance.create('issuing-cards-list');
issuingCardsList.setShowSpendControls(true);
document.body.appendChild(issuingCardsList);
```

To enable editing spend controls in the component, pass
`spend_control_management: true` as a feature when you [create an
AccountSession](https://docs.stripe.com/connect/connect-embedded-components/quickstart#server-endpoint).

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[issuing_cards_list][enabled]"=true \
 -d "components[issuing_cards_list][features][spend_control_management]"=true
```

## Sensitive data display

Issuing Connect embedded components integrate with [Issuing
Elements](https://docs.stripe.com/issuing/elements) to provide a PCI-compliant
way for you to allow your admins to view card numbers (PANs) and CVV or CVCs for
virtual cards. The sensitive data renders inside Stripe-hosted iframes and never
touches your servers.

The components can use an ephemeral key to securely retrieve card information
from the Stripe API without publicly exposing your secret keys.

To enable this functionality you must:

- Set up an ephemeral key exchange on your server.
- Pass an asynchronous callback to the components.

Stripe generates a `nonce` from the [Card
ID](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-id) in
the Issuing Card or Issuing Cards List component when a card is selected or
loaded. Stripe then calls your callback function which returns an ephemeral key,
and then renders a `Show numbers` button if the ephemeral key is valid.

### Ephemeral key exchange

Your server-side endpoint needs to accept a [Card
ID](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-id) and
a `nonce`. It can then create an ephemeral key using Stripe.

Here’s how you might implement an ephemeral key creation endpoint in web
application frameworks across various languages:

```
// This example sets up an endpoint using the Express framework.
// Watch this video to get started: https://youtu.be/rPR2aJ6XnAc

const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

const stripe = require('stripe')('sk_test_BQokikJOvBiI2HlWgH4olfQ2');

app.post('/ephemeral-keys', async (request, response) => {
 const { card_id, nonce } = request.body;

 const ephemeralKey = await stripe.ephemeralKeys.create({
 nonce: nonce,
 issuing_card: card_id,
 }, {
 apiVersion: '2025-02-24.acacia',
 stripeAccount: '{{CONNECTED_ACCOUNT_ID}}',
 });

 response.json({
 ephemeralKeySecret: ephemeralKey.secret,
 nonce: nonce,
 issuingCard: card_id,
 });
});
```

### Asynchronous callback

You must define an asynchronous function that accepts a named argument with
property `issuingCard` which is a
[Card](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-id)
ID and additionally, a `nonce` property. This function must return an `Object`
with properties `issuingCard`, `nonce`, and `ephemeralKeySecret` which are
retrieved from the endpoint you set up in the previous step.

Here’s how you might implement this callback:

```
const issuingCard = stripeConnectInstance.create('issuing-card');
const fetchEphemeralKey = async (fetchParams) => {
 const { issuingCard, nonce } = fetchParams;

 // This may vary greatly based on your implementation
 const response = await myServer.getEphemeralKey({issuingCard, nonce})

 return {
 issuingCard: response.issuingCard,
 nonce: response.nonce,
 ephemeralKeySecret: response.ephemeralKeySecret
 }
}

issuingCard.setFetchEphemeralKey(fetchEphemeralKey);
document.body.appendChild(issuingCard);
```

## Links

- [cards](https://docs.stripe.com/api/issuing/cards)
- [furever.dev](https://furever.dev)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
-
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-issuing_cards_list-features-disable_stripe_user_authentication)
- [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs)
- [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability)
- [spending
controls](https://docs.stripe.com/issuing/controls/spending-controls)
- [create an
AccountSession](https://docs.stripe.com/connect/connect-embedded-components/quickstart#server-endpoint)
- [Issuing Elements](https://docs.stripe.com/issuing/elements)
- [Card
ID](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-id)
- [https://youtu.be/rPR2aJ6XnAc](https://youtu.be/rPR2aJ6XnAc)