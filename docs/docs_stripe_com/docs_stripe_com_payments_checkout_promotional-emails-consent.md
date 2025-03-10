# Collect consent for promotional emailsUS only

## Learn how to collect permission from customers so that you can send them promotional emails.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
Promotional emails are often sent to inform customers of new products and to
share coupons and discounts. For example, you can use them to subscribe
customers to company newsletters or [send cart abandonment
emails](https://docs.stripe.com/payments/checkout/abandoned-carts).

![Collect consent for promotional
emails](https://b.stripecdn.com/docs-statics-srv/assets/promotional-consent-collection.444ead1668bd41537b9a07b2dbdc219a.png)

Collect consent from customers to send them promotional emails

To protect consumers from unwanted spam, customers must agree to receiving
promotional emails before you can contact them. Checkout helps you collect the
necessary consent, where applicable, to send promotional emails. Learn more
about [promotional email
requirements](https://docs.stripe.com/payments/checkout/compliant-promotional-emails).

[Collect
consent](https://docs.stripe.com/payments/checkout/promotional-emails-consent#collect-consent)
You can collect promotional email consent with Stripe Checkout when you create
the session:

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=2 \
 -d customer={{CUSTOMER_ID}} \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "consent_collection[promotions]"=auto
```

When `consent_collection.promotions='auto'`, Checkout dynamically displays a
checkbox for collecting the customer’s consent to promotional content.

#### Note

When the checkbox is shown, the default state depends on the customer’s country
and the country your business is based in. Data privacy laws vary by
jurisdiction, so Checkout disables or limits this feature when local regulations
prohibit it.

[Store consent and email
address](https://docs.stripe.com/payments/checkout/promotional-emails-consent#store-consent)
The Checkout Session’s
[consent](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-consent)
attribute records whether or not the session collected promotional consent from
the customer.

As customers complete purchases, keep track of which customers consent to
promotional content. You can create or update an existing
[webhook](https://docs.stripe.com/webhooks) handler to do this. Listen to the
`checkout.session.completed` event, check for the `consent.promotions` status,
and then store email addresses for customers who give consent.

```
// Find your endpoint's secret in your Dashboard's webhook settings
const endpointSecret = 'whsec_...';

// Using Express
const app = require('express')();

// Use body-parser to retrieve the raw body as a buffer
const bodyParser = require('body-parser');

const recordPromotionalEmailConsent = (email, promoConsent) => {
 // TODO: fill me in
 console.log("Recording promotional email consent", email, promoConsent);
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

 // Handle the checkout.session.completed event
 if (event.type === 'checkout.session.completed') {
 const session = event.data.object;
 const promoConsent = session.consent?.promotions;
 const email = session.customer_details.email;

// Record whether or not the customer has agreed to receive promotional emails
 recordPromotionalEmailConsent(email, promoConsent)

 // Handle order fulfillment
 }
 response.status(200).end();
});
```

After you’ve configured Checkout to collect consent for sending customers
promotional content, you can [recover abandoned
carts](https://docs.stripe.com/payments/checkout/abandoned-carts) by following
up with leads for customers that left the checkout flow before completing
payment.

## Links

- [send cart abandonment
emails](https://docs.stripe.com/payments/checkout/abandoned-carts)
- [promotional email
requirements](https://docs.stripe.com/payments/checkout/compliant-promotional-emails)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
-
[consent](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-consent)
- [webhook](https://docs.stripe.com/webhooks)