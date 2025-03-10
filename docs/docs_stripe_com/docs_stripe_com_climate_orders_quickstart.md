using the link in the code editor.

Install the libraries:

`npm install --save stripe @stripe/stripe-js next`Server
### Create an endpoint to handle the request

Add an endpoint on your server that creates a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions). The Checkout Session
controls what your customer sees on the payment page.

Server
### Create a carbon removal order

A [Climate Order](https://docs.stripe.com/api/climate/order) reserves the carbon
removal and tracks it through delivery. The total amount is deducted from your
[Stripe balance](https://docs.stripe.com/api/balance).

#### Note

For production code, move creating the Climate Order to an offline process and
handle duplicate events. See [Best practices for using
webhooks](https://docs.stripe.com/webhooks#best-practices) for more details.

Server2Build your frontend
### Add an order page

Create a page in your application to place an order.

Client
### Download the asset kit

Use [the asset
kit](https://stripe-images.s3.amazonaws.com/content-store/climate/APIAssetKit.zip)
to introduce your customers to carbon removal products.

3Test your page
### Set your environment variables

Add your publishable and secret keys to a `.env` file. Next.js automatically
loads them into your application as [environment
variables](https://nextjs.org/docs/basic-features/environment-variables). Also
include a webhook secret, which you can create in the
[Dashboard](https://dashboard.stripe.com/webhooks) or with the [Stripe
CLI](https://docs.stripe.com/stripe-cli).

Server
### Run the application

Start your app with `npm run dev` and navigate to
[http://localhost:3000](http://localhost:3000/).

Client
### Verify your carbon removal order

View the `Climate Order` in the [Stripe
Dashboard](https://dashboard.stripe.com/climate/orders) to confirm that it’s
been created successfully.

pages/index.jspages/api/climate_order.js.envDownload
```
import React from "react";
export default function App() { return ( <section> <div className="product">
<img src="https://frontierclimate.com/images/airhive.jpg" alt="" /> <div
className="description"> <h3>Frontier's 2027 offtake portfolio</h3>
<h5>$550.00/ton</h5> </div> </div> <form action="/api/climate_order"
method="POST"> <button type="submit"> Place order </button> </form> <style jsx
global> {` body { display: flex; justify-content: center; align-items: center;
background: #242d60; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
'Roboto', 'Helvetica Neue', 'Ubuntu', sans-serif; height: 100vh; margin: 0;
-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
section { background: #ffffff; display: flex; flex-direction: column; width:
400px; height: 112px; border-radius: 6px; justify-content: space-between; }
.product { display: flex; } .description { display: flex; flex-direction:
column; justify-content: center; } p { font-style: normal; font-weight: 500;
font-size: 14px; line-height: 20px; letter-spacing: -0.154px; color: #242d60;
height: 100%; width: 100%; padding: 0 20px; display: flex; align-items: center;
justify-content: center; box-sizing: border-box; } img { object-fit: cover;
border-radius: 6px; margin: 10px; width: 54px; height: 57px; } h3, h5 {
font-style: normal; font-weight: 500; font-size: 14px; line-height: 20px;
letter-spacing: -0.154px; color: #242d60; margin: 0; } h5 { opacity: 0.5; }
button { height: 36px; background: #556cd6; color: white; width: 100%;
font-size: 14px; border: 0; font-weight: 500; cursor: pointer; letter-spacing:
0.6; border-radius: 0 0 6px 6px; transition: all 0.2s ease; box-shadow: 0px 4px
5.5px 0px rgba(0, 0, 0, 0.07); } button:hover { opacity: 0.8; } `} </style>
</section> );}
```

## Links

- [text version of this
guide](https://docs.stripe.com/payments/accept-a-payment)
- [View the text-based
guide](https://docs.stripe.com/climate/orders/order-carbon-removal)
- [Climate Orders API](https://docs.stripe.com/api/climate/order)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [Stripe balance](https://docs.stripe.com/api/balance)
- [Best practices for using
webhooks](https://docs.stripe.com/webhooks#best-practices)
- [the asset
kit](https://stripe-images.s3.amazonaws.com/content-store/climate/APIAssetKit.zip)
- [environment
variables](https://nextjs.org/docs/basic-features/environment-variables)
- [Dashboard](https://dashboard.stripe.com/webhooks)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)
- [http://localhost:3000](http://localhost:3000)
- [Stripe Dashboard](https://dashboard.stripe.com/climate/orders)