# Analyze your conversion funnel

## Analyze your Stripe Checkout conversion funnel with Google Analytics 4.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
Use Google Analytics 4 (GA4) to track users as they progress through your Stripe
Checkout purchase funnel. Before you begin, set up a [GA4
account](https://support.google.com/analytics/answer/9304153) and add a [GA4
property](https://support.google.com/analytics/answer/9744165?hl=en#zippy=%2Cin-this-article).

## Set up your site

- Create a product page with a **Checkout** button:

```
<html>
 <head>
 <title>Buy cool new product</title>
 </head>
 <body>
 <script>
 window.addEventListener("load", function () {
 document
 .getElementById("submit")
 .addEventListener("click", function (event) {
 event.preventDefault();
 fetch("/create-checkout-session", {
 method: "POST",
 })
 .then((response) => response.json())
 .then((checkoutSession) => {
 window.location.href = checkoutSession.url;
 });
 });
 });
 </script>
 <form>
 <button id="submit">Checkout</button>
 </form>
 </body>
</html>
```
- Create a server-side endpoint that creates a Checkout Session and serves the
pages:

```
// This example sets up endpoints using the Express framework.
// Watch this video to get started: https://youtu.be/rPR2aJ6XnAc.

const express = require("express");
require("dotenv").config();

const app = express();

// Set your secret key. Remember to switch to your live key in production!
// See your keys here: https://dashboard.stripe.com/apikeys

const stripe = require('stripe')('sk_test_BQokikJOvBiI2HlWgH4olfQ2');

const request = require("request");

app.post(
 "/create-checkout-session",
 express.urlencoded({ extended: false }),
 async (req, res) => {
 const session = await stripe.checkout.sessions.create({
 payment_method_types: ["card"],
 line_items: [
 {
 price_data: {
 currency: "usd",
 product_data: {
 name: "T-shirt",
 },
 unit_amount: 2000,
 },
 quantity: 1,
 },
 ],
 mode: "payment",
 success_url: req.get("origin") + "/success",
 cancel_url: req.get("origin") + "/cancel",
 });

 res.json({ url: session.url });
 }
);

app.get("/product", function (req, res) {
 res.sendFile(__dirname + "/product.html");
});

app.get("/success", function (req, res) {
 res.sendFile(__dirname + "/success.html");
});

app.get("/cancel", function (req, res) {
 res.sendFile(__dirname + "/cancel.html");
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));
```
- Create a success page:

```
<html>
 <head>
 <title>Thanks for your order!</title>
 </head>
 <body>
 <h1>Thanks for your order!</h1>
 <p>
 We appreciate your business! If you have any questions, please email
 <a href="mailto:orders@example.com">orders@example.com</a>.
 </p>
 </body>
</html>
```
- Create a canceled page:

```
<html>
 <head>
 <title>Order Canceled!</title>
 </head>
 <body>
 <p>
 <a href="/product">Start another order</a>.
 </p>
 </body>
</html>
```

## Instrumentation walkthrough

In the following example, we assume your customer has:

- Viewed your product page.
- Clicked the **Buy** button and was redirected to Stripe Checkout.
- Completed the payment and was redirected to the success page.

### Quick summary

### Add instrumentation

- Add `checkout.stripe.com` to your referral exclusion list.
- Add Google Analytics tags to your product, success, and canceled pages. Tags
automatically fire an event on page load.

```
<html>
 <head>
 <!-- START GOOGLE ANALYTICS -->
 <script
 async
src="https://www.googletagmanager.com/gtag/js?id=<GOOGLE_ANALYTICS_CLIENT_ID>"
 ></script>
 <script>
 window.dataLayer = window.dataLayer || [];
 function gtag() {
 window.dataLayer.push(arguments);
 }
 gtag("js", new Date());
 gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");
 </script>
 <!-- END GOOGLE ANALYTICS -->
 <title>Buy cool new product</title>
 </head>
 <body>
 <script>
 window.addEventListener("load", function () {
 document
 .getElementById("submit")
 .addEventListener("click", function (event) {
 event.preventDefault();
 fetch("/create-checkout-session", {
 method: "POST",
 })
 .then((response) => response.json())
 .then((checkoutSession) => {
 window.location.href = checkoutSession.url;
 });
 });
 });
 </script>
 <form>
 <button id="submit">Checkout</button>
 </form>
 </body>
</html>
```

```
<html>
 <head>
 <!-- START GOOGLE ANALYTICS -->
 <script
 async
src="https://www.googletagmanager.com/gtag/js?id=<GOOGLE_ANALYTICS_CLIENT_ID>"
 ></script>
 <script>
 window.dataLayer = window.dataLayer || [];
 function gtag() {
 window.dataLayer.push(arguments);
 }
 gtag("js", new Date());
 gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");
 </script>
 <!-- END GOOGLE ANALYTICS -->
 <title>Thanks for your order!</title>
 </head>
 <body>
 <h1>Thanks for your order!</h1>
 <p>
 We appreciate your business! If you have any questions, please email
 <a href="mailto:orders@example.com">orders@example.com</a>.
 </p>
 </body>
</html>
```

```
<html>
 <head>
 <!-- START GOOGLE ANALYTICS -->
 <script
 async
src="https://www.googletagmanager.com/gtag/js?id=<GOOGLE_ANALYTICS_CLIENT_ID>"
 ></script>
 <script>
 window.dataLayer = window.dataLayer || [];
 function gtag() {
 window.dataLayer.push(arguments);
 }
 gtag("js", new Date());
 gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");
 </script>
 <!-- END GOOGLE ANALYTICS -->
 <title>Order Canceled!</title>
 </head>
 <body>
 <p>
 <a href="/product">Start another order</a>.
 </p>
 </body>
</html>
```
- Fire an event just before redirecting to Stripe Checkout:

```
<html>
 <head>
 <!-- START GOOGLE ANALYTICS -->
 <script
 async
src="https://www.googletagmanager.com/gtag/js?id=<GOOGLE_ANALYTICS_CLIENT_ID>"
 ></script>
 <script>
 window.dataLayer = window.dataLayer || [];
 function gtag() {
 window.dataLayer.push(arguments);
 }
 gtag("js", new Date());
 gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");
 </script>
 <!-- END GOOGLE ANALYTICS -->
 <title>Buy cool new product</title>
 </head>
 <body>
 <script>
 window.addEventListener("load", function () {
 document
 .getElementById("submit")
 .addEventListener("click", function (event) {
 event.preventDefault();
 fetch("/create-checkout-session", {
 method: "POST",
 })
 .then((response) => response.json())
 .then((checkoutSession) => {
 window.location.href = checkoutSession.url;
 gtag("event", "begin_checkout", {
 event_callback: function () {
 window.location.href = checkoutSession.url;
 },
 });
 });
 });
 });
 </script>
 <form>
 <button id="submit">Checkout</button>
 </form>
 </body>
</html>
```

### Analyze your conversion funnel metrics

After you add the proper instrumentation, you can see the metrics corresponding
to each step defined in your conversion funnel:

- **product page views:** The number of page visitors who viewed the product
page.
- **begin_checkout event count:** The number of page visitors who clicked the
**Buy** button and were redirected to Stripe Checkout.
- **success page views:** The number of page visitors who completed the purchase
and were redirected to the success page.

Using these numbers, you can see where visitors are dropping off in your
conversion funnel.

[OptionalServer-side event
recording](https://docs.stripe.com/payments/checkout/analyze-conversion-funnel#server-side-event-recording)[OptionalLinking
client and server-side
events](https://docs.stripe.com/payments/checkout/analyze-conversion-funnel#link-client-and-server-side-events)[OptionalServer-side
redirects](https://docs.stripe.com/payments/checkout/analyze-conversion-funnel#server-side-redirect)

## Links

- [GA4 account](https://support.google.com/analytics/answer/9304153)
- [GA4
property](https://support.google.com/analytics/answer/9744165?hl=en#zippy=%2Cin-this-article)
- [https://youtu.be/rPR2aJ6XnAc.](https://youtu.be/rPR2aJ6XnAc)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
-
[https://www.googletagmanager.com/gtag/js?id=](https://www.googletagmanager.com/gtag/js?id=)