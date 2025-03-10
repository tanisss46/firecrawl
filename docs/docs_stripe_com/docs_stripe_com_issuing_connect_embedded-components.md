# Embed Issuing card management into your website

## Use prebuilt UI components to embed Issuing card management into your website.

Give your connected accounts access to Issuing card management functionality on
your website by using [Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components).
Connect embedded components allow you to create complex integrations with Stripe
products that require minimal coding and configuration out of the box.

Stripe offers two different components for Issuing card management:

- Issuing Card component
- Issuing Cards List component

#### Security tip

These components are for **admin users** of connected accounts, who can access
sensitive card and cardholder data of the entire connected account. These
components shouldn’t be used to render UI for individual cardholders in any
circumstance.

## Quickstart

Issuing Connect embedded components requires access to [Issuing and
Connect](https://docs.stripe.com/issuing/connect).

To learn how embedded components work, see the [Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
guide. The corresponding [embedded components
quickstart](https://docs.stripe.com/connect/connect-embedded-components/quickstart)
can help you set up your environment.

To embed Issuing card management into your website:

- Follow the steps to [create a connected account with Issuing
capabilities](https://docs.stripe.com/issuing/connect#create-connected-accounts-with-issuing-capabilities).
- [Create a cardholder and
cards](https://docs.stripe.com/issuing/connect/cardholders-and-cards) for that
connected account.
- [Create an
AccountSession](https://docs.stripe.com/connect/connect-embedded-components/quickstart#server-endpoint)
with `issuing_card: {enabled: true}` or `issuing_cards_list: {enabled: true}`.
- [Add the issuing-card or issuing-cards-list component to the
DOM](https://docs.stripe.com/connect/connect-embedded-components/quickstart#embedded-component).

## Issuing Card component

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
The Issuing Card component allows an admin to view individual card details. From
this view, they can set spend controls, as well as activate, deactivate
(freeze), or cancel cards. If you implement [sensitive data
display](https://docs.stripe.com/issuing/connect/embedded-components#sensitive-data-display),
they can also view card numbers (PANs) and CVVs or CVCs for virtual cards.

### Issuing Card configuration

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescription`setShowSpendControls``boolean`Specifies
whether to render the Spend controls tab. Default value is
false.`setDefaultCard``string`Sets the Issuing
[Card](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-id)
ID to display upon initial load.`setCardSwitching``boolean`Sets whether or not
to render the card dropdown selector. Sets to `true` by
default.`setFetchEphemeralKey``Function`Sets the callback that fetches the
ephemeral key for the card. See [sensitive data
display](https://docs.stripe.com/issuing/connect/embedded-components#sensitive-data-display).
## Issuing Cards List component

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
The Issuing Cards List component allows an admin to view all the cards on a
connected account. They can filter cards by cardholder, creation date, and card
type.

When the admin clicks on a row in the table, they see a view of the selected
card where they can activate, deactivate (freeze), or cancel the card. If you
implement [sensitive data
display](https://docs.stripe.com/issuing/connect/embedded-components#sensitive-data-display),
they can also view card numbers (PANs) and CVC or CVVs for virtual cards.

### Issuing Cards List configuration

This embedded component supports the following parameters:

HTML + JSReactMethodTypeDescription`setShowSpendControls``boolean`Specifies
whether to render the Spend controls tab. Default value is
false.`setFetchEphemeralKey``Function`Sets the callback that fetches the
ephemeral key for the currently selected card. See [sensitive data
display](https://docs.stripe.com/issuing/connect/embedded-components#sensitive-data-display).
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

## Additional configuration

You can customize and configure your Connect embedded components to match your
website’s look and feel. You can set this configuration when you initialize the
`StripeConnectInstance`. See [customize the look of Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components#customize-the-look-of-connect-embedded-components)
for more details.

## Links

- [Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Issuing and Connect](https://docs.stripe.com/issuing/connect)
- [embedded components
quickstart](https://docs.stripe.com/connect/connect-embedded-components/quickstart)
- [create a connected account with Issuing
capabilities](https://docs.stripe.com/issuing/connect#create-connected-accounts-with-issuing-capabilities)
- [Create a cardholder and
cards](https://docs.stripe.com/issuing/connect/cardholders-and-cards)
- [Create an
AccountSession](https://docs.stripe.com/connect/connect-embedded-components/quickstart#server-endpoint)
- [Add the issuing-card or issuing-cards-list component to the
DOM](https://docs.stripe.com/connect/connect-embedded-components/quickstart#embedded-component)
- [furever.dev](https://furever.dev)
-
[Card](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-id)
- [spending
controls](https://docs.stripe.com/issuing/controls/spending-controls)
- [Issuing Elements](https://docs.stripe.com/issuing/elements)
- [https://youtu.be/rPR2aJ6XnAc](https://youtu.be/rPR2aJ6XnAc)
- [customize the look of Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components#customize-the-look-of-connect-embedded-components)