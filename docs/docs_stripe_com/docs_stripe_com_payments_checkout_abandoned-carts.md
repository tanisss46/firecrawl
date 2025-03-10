# Recover abandoned carts

## Learn how to recover abandoned Checkout pages and boost revenue.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
In e-commerce, [cart
abandonment](https://docs.stripe.com/payments/checkout/compliant-promotional-emails)
is when customers leave the checkout flow before completing their purchase. To
help bring customers back to Checkout, create a recovery flow where you follow
up with customers over email to complete their purchases.

Cart abandonment emails fall into the broader category of *promotional emails*,
which includes emails that inform customers of new products and that share
coupons and discounts. Customers must agree to receive promotional emails before
you can contact them. Checkout helps you:

- Collect consent from customers to send them promotional emails.
- Get notified when customers abandon Checkout so you can send cart abandonment
emails.
[Collect promotional
consent](https://docs.stripe.com/payments/checkout/abandoned-carts#collect-promotional-consent)
Configure Checkout to [collect consent for promotional
content](https://docs.stripe.com/payments/checkout/promotional-emails-consent).
If you collect the customer’s email address and request consent for promotional
content before redirecting to Checkout, you can skip using
`consent_collection[promotions]`.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d customer={{CUSTOMER_ID}} \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 -d "consent_collection[promotions]"=auto
```

[Configure
recovery](https://docs.stripe.com/payments/checkout/abandoned-carts#configure-recovery)
A Checkout Session becomes abandoned when it reaches its
[expires_at](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-expires_at)
timestamp and the customer hasn’t completed checking out. When this occurs, the
session is no longer accessible and Stripe fires the `checkout.session.expired`
[webhook](https://docs.stripe.com/webhooks), which you can listen to and try to
bring the customer back to a new Checkout Session to complete their purchase. To
use this feature, enable `after_expiration.recovery` when you create the
session.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 -d customer={{CUSTOMER_ID}} \
 -d "consent_collection[promotions]"=auto \
 -d "after_expiration[recovery][enabled]"=true \
 -d "after_expiration[recovery][allow_promotion_codes]"=true
```

[Get notified of
abandonment](https://docs.stripe.com/payments/checkout/abandoned-carts#webhook)
Listen to the `checkout.session.expired` webhook to be notified when customers
abandon Checkout and sessions expire. When the session expires with recovery
enabled, the webhook payload contains
[after_expiration](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-after_expiration-recovery),
which includes a URL denoted by `after_expiration.recovery.url` that you can
embed in cart abandonment emails. When the customer opens this URL, **it creates
a new Checkout Session that’s a copy of the original expired session**. The
customer uses this copied session to complete the purchase.

#### Note

For security purposes, the recovery URL for a session is usable for 30 days,
denoted by the `after_expiration.recovery.expires_at` timestamp.

```
{
 "id": "evt_123456789",
 "object": "event",
 "type": "checkout.session.expired",
 // ...other webhook attributes
 "data": {
 "object": {
 "id": "cs_12356789",
 "object": "checkout.session",
 // ...other Checkout Session attributes
 "consent_collection": {
 "promotions": "auto",
 },
 "consent": {
 "promotions": "opt_in"
 },
 "after_expiration": {
 "recovery": {
 "enabled": true,
 "url": "https://buy.stripe.com/r/live_asAb1724",
 "allow_promotion_code": true,
 "expires_at": 1622908282,
 }
 }
 }
 }
}
```

[Send recovery
emails](https://docs.stripe.com/payments/checkout/abandoned-carts#send-recovery-emails)
To send recovery emails, create a webhook handler for expired sessions and send
an email that embeds the session’s recovery URL. A customer might abandon
multiple Checkout Sessions, each triggering its own `checkout.session.expired`
event so make sure to record when you send recovery emails to customers and
avoid spamming them.

```
// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = 'whsec_...';

// Using Express
const app = require('express')();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

const sendRecoveryEmail = (email, recoveryUrl) => {
 // TODO: fill me in
 console.log("Sending recovery email", email, recoveryUrl);
}

app.post('/webhook', bodyParser.raw({type: 'application/json'}), (request,
response) => {
 const payload = request.body;
 const sig = request.headers['stripe-signature'];

 let event;

 try {
 event = stripe.webhooks.constructEvent(payload, sig, endpointSecret);
 } catch (err) {
 return response.status(400).send(`Webhook Error: ${err.message}`);
 }

 // Handle the checkout.session.expired event
 if (event.type === 'checkout.session.expired') {
 const session = event.data.object;

 // When a Checkout Session expires, the customer's email isn't returned in
 // the webhook payload unless they give consent for promotional content
 const email = session.customer_details?.email
 const recoveryUrl = session.after_expiration?.recovery?.url

 // Do nothing if the Checkout Session has no email or recovery URL
 if (!email || !recoveryUrl) {
 return response.status(200).end();
 }

 // Check if the customer has consented to promotional emails and
 // avoid spamming people who abandon Checkout multiple times
 if (
 session.consent?.promotions === 'opt_in'
 && !hasSentRecoveryEmailToCustomer(email)
 ) {
 sendRecoveryEmail(email, recoveryUrl)
 }
 }
 response.status(200).end();
});
```

[OptionalAdjust session
expiration](https://docs.stripe.com/payments/checkout/abandoned-carts#adjust-session-expiration)[OptionalTrack
conversion](https://docs.stripe.com/payments/checkout/abandoned-carts#track-conversion)[OptionalOffer
promotion codes in recovery
emails](https://docs.stripe.com/payments/checkout/abandoned-carts#promotion-codes)

## Links

- [cart
abandonment](https://docs.stripe.com/payments/checkout/compliant-promotional-emails)
- [collect consent for promotional
content](https://docs.stripe.com/payments/checkout/promotional-emails-consent)
- [https://example.com/success](https://example.com/success)
-
[expires_at](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-expires_at)
- [webhook](https://docs.stripe.com/webhooks)
-
[after_expiration](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-after_expiration-recovery)
-
[https://buy.stripe.com/r/live_asAb1724](https://buy.stripe.com/r/live_asAb1724)