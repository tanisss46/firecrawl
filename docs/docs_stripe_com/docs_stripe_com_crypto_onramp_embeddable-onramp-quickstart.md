options](https://docs.stripe.com/no-code) or get help from [our
partners](https://stripe.partners/).1Set up the server
### Install the Stripe Ruby library

Install the Stripe ruby gem and require it in your code. Alternatively, if
you’re starting from scratch and need a Gemfile, download the project files
using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe`Server
### Create a OnrampSession

Add an endpoint on your server that creates an
[OnrampSession](https://docs.stripe.com/crypto/onramp/api-reference) object. An
`OnrampSession` object tracks the customer’s onramp lifecycle, keeping track of
order details and ensuring the customer is only charged once. Return the
`OnrampSession` object’s client secret in the response to finish the onramp on
the client.

#### Note

Our official libraries don’t contain built-in support for the API endpoints
because the onramp API is in limited beta. This guide includes custom extension
to the official Stripe libraries for minting onramp sessions. You can find them
in the downloadable sample code on the right.

Server2Build an onramp page on the client
### Load Stripe Crypto SDK

Use [Stripe.js](https://docs.stripe.com/js) and the [Stripe crypto
SDK](https://docs.stripe.com/crypto/onramp/esmodule) to remain [PCI
compliant](https://docs.stripe.com/security/guide#validating-pci-compliance).
These scripts must always load directly from Stripe’s domains
(https://js.stripe.com and https://crypto-js.stripe.com) for compatibility.
Don’t include the scripts in a bundle or host a copy yourself. If you do, your
integration might break without warning.

Client
### Define the onramp container

Add one empty placeholder `div` to your page to host the onramp widget. Stripe
inserts an iframe to securely collect the customer’s payment and other sensitive
information.

Client
### Initialize Stripe crypto SDK

Initialize Stripe crypto SDK with your publishable API keys. You’ll use it to
retrieve the `OnrampSession` object and complete the onramp on the client.

Client
### Fetch an OnrampSession

Immediately make a request to the endpoint on your server to create a new
`OnrampSession` object as soon as your page loads. The clientSecret returned by
your endpoint is used to complete the onramp.

Client
### Create the OnrampElement

Create an `OnrampSession` instance and mount it to the placeholder `<div>` on
your page. It embeds an iframe with a dynamic UI that collects necessary order,
identity, and payment details to complete the purchase and delivery of crypto.

#### Note

Use the [values provided
here](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide#test-mode-values)
to complete an onramp transaction in [test
mode](https://docs.stripe.com/test-mode).

Client
## Enhance your integration

You’re ready to let users securely purchase cryptocurrencies directly from your
platform or Dapp at checkout. Continue with the steps below to add more
features.

### Style the onramp widget

Customize the Onramp UI with [brand
settings](https://dashboard.stripe.com/settings/branding) in your dashboard. Use
your company’s color scheme to make it match with the rest of your onramp page.

### Dark mode

Apply dark mode to the onramp widget with the `theme` parameter.

Client
### Set up OnrampSession state listeners

Initialize listeners to provide a responsive user interface when an onramp
session completes. For example, you can direct users to resume their previous
task or return to their intended destination.

Client
## Next steps

#### [Onramp API](https://docs.stripe.com/crypto/onramp/api-reference)

Customize the `OnrampSession`, such as pre-populating customer information and
setting default cryptocurrencies.

#### [Onramp Quotes API](https://docs.stripe.com/crypto/onramp/quotes-api)

Use the Onramp Quotes API to fetch estimated quotes for onramp conversions into
various cryptocurrencies on different networks.

#### [Back-end integration best practices](https://docs.stripe.com/crypto/onramp/backend-best-practices)

Review the suggested `OnrampSession` parameters to set based on your product use
case.

server.rbonramp.htmlonramp.jsonramp.cssDownload
```
require 'sinatra'require 'stripe'# This is a public sample test API key.# Don’t
submit any personally identifiable information in requests made with this key.#
Sign in to see your own test API key embedded in code samples.Stripe.api_key =
'sk_test_BQokikJOvBiI2HlWgH4olfQ2'
set :static, trueset :port, 4242
# An endpoint to create a new onramp sessionpost '/create-onramp-session' do content_type 'application/json' data = JSON.parse(request.body.read)
# Create an OnrampSession with amount and currency onramp_session =
Stripe::APIResource.request( :post, '/v1/crypto/onramp_sessions', {
transaction_details: { destination_currency:
data['transaction_details']['destination_currency'],
destination_exchange_amount:
data['transaction_details']['destination_exchange_amount'], destination_network:
data['transaction_details']['destination_network'] }, customer_ip_address:
request.ip } )[0].data
 { clientSecret: onramp_session[:client_secret] }.to_jsonend
```

## Links

- [text version of this
guide](https://docs.stripe.com/payments/accept-a-payment)
- [View the text-based
guide](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide)
- [fiat-to-crypto onramp](https://docs.stripe.com/crypto/onramp)
- [test mode](https://docs.stripe.com/test-mode)
- [branding settings](https://dashboard.stripe.com/account/branding)
- [domain
allowlist](https://dashboard.stripe.com/crypto-onramp/allowlist-domains)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [OnrampSession](https://docs.stripe.com/crypto/onramp/api-reference)
- [Stripe.js](https://docs.stripe.com/js)
- [Stripe crypto SDK](https://docs.stripe.com/crypto/onramp/esmodule)
- [PCI
compliant](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [values provided
here](https://docs.stripe.com/crypto/onramp/emeddable-onramp-guide#test-mode-values)
- [brand settings](https://dashboard.stripe.com/settings/branding)
- [Onramp Quotes API](https://docs.stripe.com/crypto/onramp/quotes-api)
- [Back-end integration best
practices](https://docs.stripe.com/crypto/onramp/backend-best-practices)