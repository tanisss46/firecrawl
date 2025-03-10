# Issuing card

## Show an individual issued card.

Issuing card renders the details of an individual
[card](https://docs.stripe.com/api/issuing/cards) issued to your connected
accounts.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
The permission boundary for this component is at the connected account level,
not at the individual card level. This UI should be shown to users that have
access to all cards, not to users that have restricted access to a single card.

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
Issuing card component by specifying `issuing_card` in the `components`
parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[issuing_card][enabled]"=true \
 -d "components[issuing_card][features][card_management]"=true \
 -d "components[issuing_card][features][cardholder_management]"=true \
 -d "components[issuing_card][features][card_spend_dispute_management]"=true \
 -d "components[issuing_card][features][spend_control_management]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the Issuing card component in the front end:

```
// Include this element in your HTML
const issuingCard = stripeConnectInstance.create('issuing-card');
issuingCard.setDefaultCard('{{ISSUING_CARD_ID_ID');
issuingCard.setShowSpendControls(true);
container.appendChild(issuingCard);
```

This embedded component supports the following attributes:

HTML + JSReactSetterTypeDescription`setDefaultCard``(string) => void`Sets the
Issuing
[Card](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-id)
ID to display upon initial load.`setCardSwitching``(boolean) => void`Sets
whether to render the card dropdown selector. Defaults to
true.`setFetchEphemeralKey``(function) => void`Sets the callback that fetches
the ephemeral key for the card. See [sensitive data
display](https://docs.stripe.com/connect/supported-embedded-components/issuing-card#sensitive-data-display).
## Set spending controls

You can use Issuing Connect embedded components to view and, optionally, edit
[spending controls](https://docs.stripe.com/issuing/controls/spending-controls)
on your cards by turning on the Issuing component’s `showSpendControls`
attribute.

```
const issuingCard = stripeConnectInstance.create('issuing-card');
issuingCard.setShowSpendControls(true);
document.body.appendChild(issuingCard);
```

To enable editing spend controls in the component, pass
`spend_control_management: true` as a feature when you [create an
AccountSession](https://docs.stripe.com/connect/connect-embedded-components/quickstart#server-endpoint).

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[issuing_card][enabled]"=true \
 -d "components[issuing_card][features][spend_control_management]"=true
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

- [card](https://docs.stripe.com/api/issuing/cards)
- [furever.dev](https://furever.dev)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
-
[Card](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-id)
- [spending
controls](https://docs.stripe.com/issuing/controls/spending-controls)
- [create an
AccountSession](https://docs.stripe.com/connect/connect-embedded-components/quickstart#server-endpoint)
- [Issuing Elements](https://docs.stripe.com/issuing/elements)
- [https://youtu.be/rPR2aJ6XnAc](https://youtu.be/rPR2aJ6XnAc)