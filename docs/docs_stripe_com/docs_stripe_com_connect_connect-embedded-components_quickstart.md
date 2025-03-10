- [Go](https://github.com/stripe/stripe-go) `>=81.3.0`

Build a full, working integration using [Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components).
Use Connect embedded components to add connected account dashboard functionality
to your website in minutes. These libraries and their supporting API help you to
get up and running with almost no code, giving your users access to Stripe
products directly in your dashboard.

Download full appDon't code? Use Stripe’s [no-code
options](https://docs.stripe.com/no-code) or get help from [our
partners](https://stripe.partners/).1Set up the server
### Install the Stripe Ruby library

Install the Stripe Ruby gem and require it in your code. Alternatively, if
you’re starting from scratch and need a Gemfile, download the project files
using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe -v 13.4.1`Server
### Create an endpoint on your server

Add a new endpoint on your server for your client to call.

Server
### Delegate API access to your connected account

To make requests on behalf of your connected account, pass the connected account
ID to the [AccountSessions API](https://docs.stripe.com/api/account_sessions).

Server
### Enable specific embedded components for your connected accounts

Specify the embedded components you want to enable for your connected accounts.
For the full list of supported embedded components, see [Get started with
Connect embedded
components](https://docs.stripe.com/connect/supported-embedded-components).

Server
### Create an AccountSession

Call the `v1/account_sessions` API from your endpoint to create a new
[AccountSession](https://docs.stripe.com/api/account_sessions).

Server
### Return the client secret

Return the `client_secret` property from the AccountSession in the response.

Server2Initialize Connect.js on the client
### Load the Connect.js script

Import the [@stripe/connect-js](https://github.com/stripe/connect-js) module and
call `loadConnectAndInitialize(initParams)` to load the code necessary to
connect your client to Stripe. Connect.js loads synchronously and returns a
`StripeConnectInstance` to the client.

npmGitHub
Install the library:

`npm install --save @stripe/connect-js`Client
### Initialize Connect.js

`loadConnectAndInitialize(initParams)` returns a StripeConnectInstance object,
which is used to create a StripeConnectInstance. Initialize the
StripeConnectInstance by passing in your [publishable
key](https://docs.stripe.com/keys) and the `fetchClientSecret` function to fetch
a client secret.

Client
### Include Connect embedded components

Add Connect embedded components to the DOM. After initialization, the
StripeConnectInstance handles making requests to Stripe and updating the UI of
the web components. You can mount or unmount these elements from the DOM at any
time and make the inner elements fit seamlessly within your page by wrapping
them with your own HTML.

After a successful initialization, StripeConnectInstance manages the context for
all the Connect embedded components in your application and uses that client
secret and publishable key to contact Stripe.

Client
### Optional: Style Connect embedded components

[Customize the appearance of Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components#customize-the-look-of-connect-embedded-components)
by passing an `appearance` configuration to StripeConnect upon initialization.
Connect embedded components already inherit the font-family of the parent HTML
element, but you can make them match with the rest of your application by
passing your company’s color scheme.

Clientserver.rbindex.htmlindex.jsDownload
```
require 'sinatra'require 'stripe'
# This is a placeholder - it should be replaced with your secret API key.# Sign in to see your own test API key embedded in code samples.# Don’t submit any personally identifiable information in requests made with this key.Stripe.api_key = 'sk_INSERT_YOUR_SECRET_KEY'
set :static, trueset :port, 4242set :public_folder, 'dist'
post '/account_session' do content_type 'application/json'
begin account_session = Stripe::AccountSession.create({ account:
"{{CONNECTED_ACCOUNT_ID}}", components: { payments: { enabled: true, features: {
refund_management: true, dispute_management: true, capture_payments: true } } }
})
{ client_secret: account_session[:client_secret] }.to_json rescue => error puts
"An error occurred when calling the Stripe API to create an account session:
#{error.message}"; return [500, { error: error.message }.to_json] endend
get '/' do send_file File.join(settings.public_folder, 'index.html')end
```

## Links

- [text version of this
guide](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Ruby](https://github.com/stripe/stripe-ruby)
- [Python](https://github.com/stripe/stripe-python)
- [PHP](https://github.com/stripe/stripe-php)
- [Node](https://github.com/stripe/stripe-node)
- [.NET](https://github.com/stripe/stripe-dotnet)
- [Java](https://github.com/stripe/stripe-java)
- [Go](https://github.com/stripe/stripe-go)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [AccountSessions API](https://docs.stripe.com/api/account_sessions)
- [Get started with Connect embedded
components](https://docs.stripe.com/connect/supported-embedded-components)
- [@stripe/connect-js](https://github.com/stripe/connect-js)
- [publishable key](https://docs.stripe.com/keys)
- [Customize the appearance of Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components#customize-the-look-of-connect-embedded-components)