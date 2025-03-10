connected accounts. We’ve customized the connected account properties based on
your choices when onboarding your platform account to Connect. Changes made here
don’t update your platform settings and aren’t reflected in the Stripe
Dashboard.

See [Design an
integration](https://docs.stripe.com/connect/design-an-integration) to learn
more about making these choices.

Server
### Choose how your connected accounts onboard to Stripe

Your choice of onboarding method affects the availability of other account
options below.

Onboarding:HostedEmbeddedAPI
Redirect your connected accounts to Stripe-hosted onboarding using an Account
Link.

Server
### Choose where your connected accounts manage their payments and account details

Dashboard access:StripeExpressNone
Give your connected accounts access to the Stripe Dashboard.

Server
### Choose your charge type

Charge type:DirectDestinationSeparate charges and transfers
Create charges directly on your connected accounts.

Server
### Choose who pays fees

Who pays fees:Your connected accountsYour platform
Stripe takes Stripe fees from your connected accounts.

Server
### Choose who is liable for negative balances

Negative balance liability:StripePlatform
Your platform isn’t liable for negative account balances. Stripe is responsible
for collecting updated information when requirements are due or change.

Server2Set up dependencies
### Install the Stripe Ruby library

Install the Stripe Ruby gem and require it in your code. Alternatively, if
you’re starting from scratch and need a Gemfile, download the project files
using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe -v 9.1.0`Server
### Set your secret key

Add your secret key to your server.

Server
### Set your publishable key

Add your publishable key to a `.env` file. React automatically loads it into
your application as an [environment
variable](https://create-react-app.dev/docs/adding-custom-environment-variables/).

Client
### Add your platform branding

To use Stripe-hosted onboarding, first go to your [onboarding
settings](https://dashboard.stripe.com/settings/connect/onboarding-interface)
and customize your branding. You need to set a business name, icon, and brand
color.

Server3Create a connected account
### Add an endpoint for creating a connected account

Set up an endpoint on your server for your client to call to handle creating a
connected account.

Server
### Create a connected account

Create a connected account by calling the Stripe API. We’ve configured the
attributes used based on the preferences you’ve selected above. You can prefill
verification information, the business profile of the user, and other fields on
the [account](https://docs.stripe.com/api/accounts/create) if your platform has
already collected it.

Server
### Call the endpoint to create a connected account

Call the endpoint you added above to create a connected account.

Client4Onboard the connected account
### Overview

Per [your preference
selection](https://docs.stripe.com/connect/onboarding/quickstart#choose-onboarding-surface),
you selected Stripe-hosted onboarding. Your platform redirects your connected
accounts to a Stripe-hosted, co-branded onboarding interface using an [Account
Link](https://docs.stripe.com/api/account_links).

Server
### Create an Account Links endpoint

Add an endpoint on your server to create an Account Link.

Server
### Provide a return URL

When your connected account completes the onboarding flow, it redirects them to
the return URL. That doesn’t mean that all information has been collected or
that the connected account has no outstanding requirements. It only means that
they entered and exited the flow properly.

Server
### Provide a refresh URL

Stripe redirects your connected account to the refresh URL when the link is
expired, the link has already been visited, your platform can’t access the
connected account, or the account is rejected. Have the refresh URL create a new
onboarding Account Link and redirect your user to it.

Server
### Call the endpoint to create an Account link

Provide the connected account ID.

Client
### Redirect the user to the URL

Send the user to Stripe to complete onboarding. They’re redirected back to your
app when onboarding is complete.

Client
### Handle the connected account returning

Show the connected account a useful page when they exit the Stripe-hosted
onboarding flow.

Client
### Handle the Account Link refreshing

Call your endpoint for refreshing the Account Link at the refresh URL.

Client5Next steps
### Accept payments

Now that you have onboarded a connected account, continue to [create direct
charges](https://docs.stripe.com/connect/direct-charges).

ServerWas this page
helpful?server.rbApp.jsx.envRefresh.jsxReturn.jsxHome.jsxDownload
```
require 'sinatra'require 'stripe'
# This is a placeholder - it should be replaced with your secret API key.# Sign in to see your own test API key embedded in code samples.# Don’t submit any personally identifiable information in requests made with this key.Stripe.api_key = 'sk_INSERT_YOUR_SECRET_KEY'
Stripe.api_version = '2023-10-16'
set :static, trueset :port, 4242set :public_folder, 'dist'
post '/account_link' do content_type 'application/json'
 body = JSON.parse(request.body.read) connected_account_id = body["account"]
begin account_link = Stripe::AccountLink.create({ account: connected_account_id,
return_url: "http://localhost:4242/return/#{connected_account_id}", refresh_url:
"http://localhost:4242/refresh/#{connected_account_id}", type:
"account_onboarding", })
{ url: account_link.url }.to_json rescue => error puts "An error occurred when
calling the Stripe API to create an account link: #{error.message}"; return
[500, { error: error.message }.to_json] endend
post '/account' do content_type 'application/json'
 begin account = Stripe::Account.create
{ account: account[:id] }.to_json rescue => error puts "An error occurred when
calling the Stripe API to create an account: #{error.message}"; return [500, {
error: error.message }.to_json] endend
get '/*path' do send_file File.join(settings.public_folder, 'index.html')end
```

## Links

- [text version of this
guide](https://docs.stripe.com/payments/accept-a-payment)
- [View the text-based
guide](https://docs.stripe.com/connect/design-an-integration)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [environment
variable](https://create-react-app.dev/docs/adding-custom-environment-variables/)
- [onboarding
settings](https://dashboard.stripe.com/settings/connect/onboarding-interface)
- [account](https://docs.stripe.com/api/accounts/create)
- [Account Link](https://docs.stripe.com/api/account_links)
- [create direct charges](https://docs.stripe.com/connect/direct-charges)