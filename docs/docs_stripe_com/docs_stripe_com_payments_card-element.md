To accept other payment methods, use the Payment Element. Learn more about
[migrating to the Payment
Element](https://docs.stripe.com/payments/payment-element/migration).

Download full appDon't code? Use Stripe’s [no-code
options](https://docs.stripe.com/no-code) or get help from [our
partners](https://stripe.partners/).1 Set up the server
### Install the Stripe Ruby library

Install the Stripe ruby gem and require it in your code. Alternatively, if
you’re starting from scratch and need a Gemfile, download the project files
using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe`Server
### Create a PaymentIntent

Add an endpoint on your server that creates a
[PaymentIntent](https://docs.stripe.com/api/payment_intents). A PaymentIntent
tracks the customer’s payment lifecycle, keeping track of any failed payment
attempts and ensuring the customer is only charged once. Return the
PaymentIntent’s client secret in the response to finish the payment on the
client.

Server2 Build a checkout page on the client
### Load Stripe.js

Use Stripe.js to remain PCI compliant by ensuring that card details are sent
directly to Stripe without hitting your server. Always load Stripe.js from
js.stripe.com to remain compliant. Do not include the script in a bundle or host
it yourself.

Client
### Define the payment form

Add an empty placeholder `div` to your checkout form. Stripe inserts an iframe
into this `div` that securely collects card information.

Client
### Initialize Stripe.js

Initialize Stripe.js with your publishable API keys. You will use Stripe.js to
create the card input field and complete the payment on the client.

Client
### Fetch a PaymentIntent

Immediately make a request to the endpoint on your server to create a new
PaymentIntent as soon as the page loads.

Client
### Initialize Stripe Elements

Initialize the [Stripe Elements UI
library](https://docs.stripe.com/js/elements_object/create_without_intent).
Elements manages the UI components you need to collect card details.

If you’re a Connect user and you specified the
[on_behalf_of](https://docs.stripe.com/connect/charges#on_behalf_of) property
when creating your Payment or Setup intent, you must pass the same value to the
Elements group using the
[onBehalfOf](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-onBehalfOf)
option.

Client
### Create the Card Element

Create a Card Element and mount it to the placeholder `'<div'>` in your payment
form. This creates a single input that collects the card number, expiry date,
CVC, and postal code. Stripe Elements displays localized placeholder text of the
postal code field based on your customer’s [browser
locale](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-locale)
(for example, showing “ZIP” for US cardholders, “Postcode” for U.K.
cardholders).

Client
### Listen for load errors

Listen to [load errors](https://docs.stripe.com/js/element/events/on_loaderror)
that trigger if the `Element` fails to load.

Client
### Optional: Style the card input

Stripe embeds an iframe to securely collect card details. Customize the iframe
by passing a [style](https://docs.stripe.com/js/appendix/style) object. Use your
company’s color scheme and font to make it match the rest of your checkout page.
Use custom fonts (for example, from Google Fonts) by initializing Elements with
a [font
set](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-fonts).

Client
### Initialize Stripe Elements

Initialize the [Stripe Elements UI
library](https://docs.stripe.com/js/elements_object/create). Elements manages
the UI components you need to collect card details.

Client
### Create the Card Element

Create a Card Element and mount it to the placeholder `'<div'>` in your payment
form. This creates a single input that collects the card number, expiry date,
CVC, and postal code. Stripe Elements displays localized placeholder text of the
postal code field based on your customer’s [browser
locale](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-locale)
(for example, showing “ZIP” for US cardholders, “Postcode” for U.K.
cardholders).

Client
### Optional: Style the card input

Stripe embeds an iframe to securely collect card details. Customize the iframe
by passing a [style](https://docs.stripe.com/js/appendix/style) object. Use your
company’s color scheme and font to make it match the rest of your checkout page.
Use custom fonts (for example, from Google Fonts) by initializing Elements with
a [font
set](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-fonts).

Client
### Optional: Expose card errors

Listen to changes on the Card Element to immediately expose card errors (for
example, the expiry date is in the past) and disable the button if the Element
is empty.

Client3 Complete the payment on the client
### Handle the submit event

Listen to the form’s submit event to know when to confirm the payment through
the Stripe API.

Client
### Complete the payment

Call `confirmCardPayment()` passing along the client secret and Card Element, to
complete the payment. Stripe automatically displays a modal if the card
[requires authentication](https://www.youtube.com/watch?v=2kc-FjU2-mY) like 3D
Secure, where the customer must enter a passcode or other piece of identifying
information to finalize the purchase.

Client
### Handle the API response

If no error occurred, tell your customer the payment was successful! For any
important post-payment actions (such as shipping packages, sending email
receipts) we recommend [setting up a
webhook](https://docs.stripe.com/payments/handling-payment-events). If your
customer’s card is declined, Stripe.js returns an error. Show that error message
to your customer so they can try again with a different card

Client4 Test the integration
### Run the application

Run the server and go to the checkout page.

Server
### Make a test payment

Use a test card number to try your integration. These card numbers work in test
mode with any CVC, postal code, and future expiry date. Stripe also has a set of
[international test cards](https://docs.stripe.com/testing#international-cards)
to test specific postal code formats (for example, only allow numerical values
for US zip codes).

Payment succeeds4242 4242 4242 4242Payment requires authentication4000 0025 0000
3155Payment is declined4000 0000 0000 9995
## Congratulations!

You’re ready to accept payments with Stripe. Continue with the steps below to
add more features.

### Send an email receipt

Stripe can send an email receipt to your customer using your brand logo and
color theme, configurable in [the
Dashboard](https://dashboard.stripe.com/settings/branding).

### Save card after payment

SaaS or e-commerce businesses often save card details for recurring customers.

## See also

#### [Payouts](https://docs.stripe.com/payouts)

Learn how to move funds out of your Stripe account into your bank account.

#### [Refunds](https://docs.stripe.com/refunds)

Handle requests for refunds by using the Stripe API or Dashboard.

#### [Fulfillment](https://docs.stripe.com/webhooks/quickstart)

Set up a webhook to fulfill orders after a payment succeeds. Webhooks are the
most reliable way to handle business-critical events.

PreviewPay nowMake a test
paymentserver.rbcheckout.htmlstyle.cssclient.jsDownload
```
require 'sinatra'require 'stripe'# This is a public sample test API key.# Don’t
submit any personally identifiable information in requests made with this key.#
Sign in to see your own test API key embedded in code samples.Stripe.api_key =
'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
set :static, trueset :port, 4242
def calculate_order_amount(_items) # Replace this constant with a calculation of
the order's amount # Calculate the order total on the server to prevent # people
from directly manipulating the amount on the client 1400end
# An endpoint to start the payment processpost '/create-payment-intent' do content_type 'application/json' data = JSON.parse(request.body.read)
# Create a PaymentIntent with amount and currency payment_intent =
Stripe::PaymentIntent.create( amount: calculate_order_amount(data['items']),
currency: 'usd' )
 { clientSecret: payment_intent['client_secret'], }.to_jsonend
```

## Links

- [text version of this
guide](https://docs.stripe.com/payments/accept-a-payment)
- [Payment Element](https://docs.stripe.com/payments/quickstart)
- [the Card Element and Payment
Element](https://docs.stripe.com/payments/payment-card-element-comparison)
- [migrating to the Payment
Element](https://docs.stripe.com/payments/payment-element/migration)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [Stripe Elements UI
library](https://docs.stripe.com/js/elements_object/create_without_intent)
- [on_behalf_of](https://docs.stripe.com/connect/charges#on_behalf_of)
-
[onBehalfOf](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-onBehalfOf)
- [browser
locale](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-locale)
- [load errors](https://docs.stripe.com/js/element/events/on_loaderror)
- [style](https://docs.stripe.com/js/appendix/style)
- [font
set](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-fonts)
- [Stripe Elements UI
library](https://docs.stripe.com/js/elements_object/create)
- [browser
locale](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-locale)
- [font
set](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-fonts)
- [requires authentication](https://www.youtube.com/watch?v=2kc-FjU2-mY)
- [setting up a
webhook](https://docs.stripe.com/payments/handling-payment-events)
- [international test
cards](https://docs.stripe.com/testing#international-cards)
- [the Dashboard](https://dashboard.stripe.com/settings/branding)
- [Payouts](https://docs.stripe.com/payouts)
- [Refunds](https://docs.stripe.com/refunds)
- [Fulfillment](https://docs.stripe.com/webhooks/quickstart)