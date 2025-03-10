# Integrate crypto for mobilePublic preview

## Configure the onramp for mobile use.

Learn how to integrate Stripe’s crypto onramp UI into mobile web views and
browsers by minting a session, hosting the onramp UI, completing the purchase,
and redirecting users back to the mobile app. Currently, Stripe Crypto doesn’t
support mobile SDKs.

## Mint a session

Similar to other integrations, you need to implement a server endpoint to
[create a new onramp
session](https://docs.stripe.com/crypto/onramp/api-reference) for every user
visit. The endpoint returns a `client_secret` that can load the onramp UI or
display an error if the onramp is unavailable.

## Host the onramp UI

Create a frontend route (*for example,
www.my-web3-wallet.com/onramp/<client_secret>*) to host the onramp UI. Your
*/onramp/<client_secret>* points to an onramp.html.

```
<!DOCTYPE html>
<html lang="en">
 <head>
 <meta charset="utf-8" />
 <title>Crypto Onramp</title>
 <meta name="description" content="A demo of the hosted onramp" />
 <meta name="viewport" content="width=device-width, initial-scale=1" />
<script type="text/javascript"
src="https://crypto-js.stripe.com/crypto-onramp-outer.js"></script>
 <script src="onramp.js" defer></script>
 </head>
 <body>
 <div id="onramp-element" />
 </body>
</html>
```

Where onramp.js consumes the `client_secret` from the URL and mounts the onramp
UI:

```
const stripeOnramp = StripeOnramp(pk_test_TYooMQauvdEDq54NiTphI7jx);
initialize();
// initialize onramp element with client secret
function initialize() {
 const url = window.location.href.replace(/\/$/, '');
 const clientSecret = url.substring(url.lastIndexOf('/') + 1);
 const onrampSession = stripeOnramp.createSession({
 clientSecret,
 // other client side options that customize the look and feel
 });
 onrampSession
 .addEventListener('onramp_session_updated', handleSessionUpdate)
 .mount("#onramp-element");
}
function handleSessionUpdate(event) {
 const session = event.payload.session;
if (session.status === 'fulfillment_complete' || session.status === 'rejected')
{
 // redirect back to mobile app via universal link
 window.location.assign('/onramp_success/' + session.id);
 }
}
```

Configure universal links to deep link `/onramp_success` back to your mobile
app. Consider providing a fallback or `onramp_success` page to prompt users to
manually switch back to your app.

## Complete the purchase

As with a standard integration, the front-end client controls the entire onramp
UI. The UI adapts to fit the screen size. As the session state changes and we
gather more `transaction_details`, the `CryptoOnrampSession` object updates
accordingly. We generate webhooks and front-end events for every status
transition. By using front-end event listeners, you can redirect users back to
your application flow when the `OnrampSession` completes.

## Redirect to the mobile app

Using a deep link or manual switch, users can resume their flow in your mobile
application. Your mobile application can use your back end to continue querying
the `CryptoOnrampSession` state.

For example, if a user is topping up their balance during initial setup, you can
redirect them back to your application as soon as the session transitions to
`fulfillment_processing`. You can allow users to explore the rest of your
application while polling the `OnrampSession` status in the background.

## Links

- [create a new onramp
session](https://docs.stripe.com/crypto/onramp/api-reference)
-
[https://crypto-js.stripe.com/crypto-onramp-outer.js](https://crypto-js.stripe.com/crypto-onramp-outer.js)