# Set up your development environment

## Get familiar with the Stripe CLI and our server-side SDKs.

Stripe’s server-side SDKs and command-line interface (CLI) allow you to interact
with Stripe’s REST APIs. Start with the Stripe CLI to streamline your
development environment and make API calls.

Use the SDKs to avoid writing boilerplate code. To start sending requests from
your environment, choose a language to follow a quickstart guide.

RubyPythonGoJavaNode.jsPHP.NET
In this quickstart, you install the [Stripe
CLI](https://docs.stripe.com/stripe-cli/overview)—an essential tool that gets
you command line access to your Stripe integration. You also install the [Stripe
Ruby server-side SDK](https://github.com/stripe/stripe-ruby) to get access to
Stripe APIs from applications written in Ruby.

## What you learn

In this quickstart, you’ll learn:

- How to call Stripe APIs without writing a line of code
- How to manage third-party dependencies using a bundler with RubyGems
- How to install the Stripe Ruby SDK v13.0.0
- How to send your first SDK request
[Set up the Stripe
CLI](https://docs.stripe.com/get-started/development-environment#setup-cli)
First, [create a Stripe account](https://dashboard.stripe.com/register) or [sign
in](https://dashboard.stripe.com/login).

### Install

From the command-line, use an install script or download and extract a versioned
archive file for your operating system to install the CLI.

homebrewaptyumScoopmacOSLinuxWindowsDocker
To install the Stripe CLI with [homebrew](https://brew.sh/), run:

```
brew install stripe/stripe-cli/stripe
```

This command fails if you run it on the Linux version of homebrew, but you can
use this alternative or follow the instructions on the Linux tab.

```
brew install stripe-cli
```

### Authenticate

Log in and authenticate your Stripe user
[Account](https://docs.stripe.com/get-started/account/activate) to generate a
set of *restricted keys*. To learn more, see [Stripe CLI keys and
permissions](https://docs.stripe.com/stripe-cli/keys).

```
stripe login
```

Press the **Enter** key on your keyboard to complete the authentication process
in your browser.

```
Your pairing code is: enjoy-enough-outwit-win
This pairing code verifies your authentication with Stripe.
Press Enter to open the browser or visit
https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1
(^C to quit)
```

### Confirm setup

Now that you’ve installed the CLI, you can make a single API request to [Create
a product](https://docs.stripe.com/api/products/create).

```
stripe products create \
--name="My First Product" \
--description="Created with the Stripe CLI"
```

Look for the product identifier (in `id`) in the response object. Save it for
the next step.

If everything worked, the command-line displays the following response.

```
{
 "id": "prod_LTenIrmp8Q67sa",
 "object": "product",
```

See all 25 lines
Next, call [Create a price](https://docs.stripe.com/api/prices/create) to attach
a price of 30 USD. Swap the placeholder in `product` with your product
identifier (for example, `prod_LTenIrmp8Q67sa`).

```
stripe prices create \
 --unit-amount=3000 \
 --currency=usd \
 --product={{PRODUCT_ID}}
```

If everything worked, the command-line displays the following response.

```
{
 "id": "price_1KzlAMJJDeE9fu01WMJJr79o",
 "object": "price",
```

See all 20 lines[Manage third-party
dependencies](https://docs.stripe.com/get-started/development-environment#sdk-deps)
We recommend managing third-party dependencies using the
[RubyGems](http://rubygems.org/) command-line tool, which allows you to add new
libraries and include them in your Ruby projects. Check whether RubyGems is
installed:

### Install RubyGems

```
gem --version
```

If you get `gem: command not found`, [download
RubyGems](http://rubygems.org/pages/download) from their downloads page.

[Install the Ruby server-side
SDK](https://docs.stripe.com/get-started/development-environment#install-sdk)
The latest version of the Stripe Ruby server-side SDK is v13.0.0. It supports
Ruby versions 2.3+.

Check your Ruby version:

```
ruby -v
```

### Install the library

[Create a gem file](https://guides.rubygems.org/make-your-own-gem/) and install
the generated gem using a bundler with [RubyGems](https://rubygems.org/).

Add the latest version of the [Stripe gem](https://rubygems.org/gems/stripe) to
a project:

```
bundle add stripe
```

Install the required gems from your specified sources:

```
bundle install
```

### Installation alternatives

[Run your first SDK
request](https://docs.stripe.com/get-started/development-environment#test-install)
Now that you have the Ruby SDK installed, you can create a subscription
[Product](https://docs.stripe.com/api/products/create) and attach a
[Price](https://docs.stripe.com/api/prices/create) with a couple API requests.
We’re using the product identifier returned in the response to create the price
in this example.

#### Note

This sample uses the default keys of your Stripe user
[account](https://docs.stripe.com/get-started/account/activate) for your
[sandbox](https://docs.stripe.com/sandboxes) environment. Only you can see these
values.

```
require 'rubygems'
require 'stripe'
Stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

starter_subscription = Stripe::Product.create(
 name: 'Starter Subscription',
 description: '$12/Month subscription',
)

starter_subscription_price = Stripe::Price.create(
 currency: 'usd',
 unit_amount: 1200,
 recurring: {interval: 'month'},
 product: starter_subscription['id'],
)

puts "Success! Here is your starter subscription product id:
#{starter_subscription.id}"
puts "Success! Here is your starter subscription price id:
#{starter_subscription_price.id}"
```

Save the file as `create_price.rb`. From the command line, `cd` to the directory
containing the file you just saved and run:

```
ruby create_price.rb
```

If everything worked, the command line shows the following response. Save these
identifiers so you can use them while building your integration.

```
Success! Here is your starter subscription product id:
prod_0KxBDl589O8KAxCG1alJgiA6
Success! Here is your starter subscription price id:
price_0KxBDm589O8KAxCGMgG7scjb
```

## See also

This wraps up the quickstart. See the links below for a few different ways to
process a payment for the product you just created.

- [Create a payment link](https://docs.stripe.com/payment-links)
- [Stripe-hosted page](https://docs.stripe.com/checkout/quickstart)
- [Advanced integration](https://docs.stripe.com/payments/quickstart)

## Links

- [no-code docs](https://docs.stripe.com/no-code)
- [prebuilt solution](https://stripe.com/partners/directory)
- [Stripe-certified expert](https://stripe.com/partners/directory?t=Consulting)
- [Stripe CLI](https://docs.stripe.com/stripe-cli/overview)
- [Stripe Ruby server-side SDK](https://github.com/stripe/stripe-ruby)
- [create a Stripe account](https://dashboard.stripe.com/register)
- [sign in](https://dashboard.stripe.com/login)
- [homebrew](https://brew.sh/)
- [Account](https://docs.stripe.com/get-started/account/activate)
- [Stripe CLI keys and permissions](https://docs.stripe.com/stripe-cli/keys)
-
[https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1](https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1)
- [Create a product](https://docs.stripe.com/api/products/create)
- [Create a price](https://docs.stripe.com/api/prices/create)
- [RubyGems](http://rubygems.org/)
- [download RubyGems](http://rubygems.org/pages/download)
- [Create a gem file](https://guides.rubygems.org/make-your-own-gem/)
- [RubyGems](https://rubygems.org/)
- [Stripe gem](https://rubygems.org/gems/stripe)
- [sandbox](https://docs.stripe.com/sandboxes)
- [Create a payment link](https://docs.stripe.com/payment-links)
- [Stripe-hosted page](https://docs.stripe.com/checkout/quickstart)
- [Advanced integration](https://docs.stripe.com/payments/quickstart)