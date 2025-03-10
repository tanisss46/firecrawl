# Send your first Stripe API request

## Get started with the Stripe API.

Every call to a Stripe API must include an API secret key. After you create a
Stripe account, we generate two pairs of [API
keys](https://docs.stripe.com/keys) for you—a publishable client-side key and a
secret server-side key—for both [test](https://docs.stripe.com/test-mode) and
live modes. To start moving real money with your live-mode keys, you need to
[activate your account](https://docs.stripe.com/get-started/account/activate).

[Before you
begin](https://docs.stripe.com/get-started/api-request#before-you-begin)
This guide walks you through a simple interaction with the Stripe API—creating a
customer. For a better understanding of Stripe API objects and how they fit
together, take a [tour of the API](https://docs.stripe.com/payments-api/tour) or
visit the [API reference](https://docs.stripe.com/api). If you’re ready to start
accepting payments, see our
[quickstart](https://docs.stripe.com/payments/quickstart).

[Send your first API
request](https://docs.stripe.com/get-started/api-request#send-first-api-request)
You can begin exploring Stripe APIs using the [Stripe
Shell](https://docs.stripe.com/stripe-shell/overview). The Stripe Shell allows
you to execute Stripe CLI commands directly within the Stripe docs site. As it
operates in a [sandbox](https://docs.stripe.com/sandboxes) environment only, you
don’t have to worry about initiating any real money-moving transactions.

- To [create a customer](https://docs.stripe.com/api/customers/create) using the
Stripe Shell, enter the following command:

```
stripe customers create --email=jane.smith@email.com --name="Jane Smith"
--description="My First Stripe Customer"
```

If everything worked, the command line displays the following response:

```
{
 "id": "cus_LfctGLAICpokzr",
 "object": "customer",
```

See all 31 lines
- (Optional) Run the same command by passing in your API secret key in a
sandbox:

```
stripe customers create --email=jane.smith@email.com --name="Jane Smith"
--description="My First Stripe Customer" --api-key
sk_test_BQokikJOvBiI2HlWgH4olfQ2
```

If everything worked, the command line displays the following response:

```
{
 "id": "cus_LfdZgLFhah76qf",
 "object": "customer",
```

See all 32 lines
[View logs and
events](https://docs.stripe.com/get-started/api-request#view-logs-events-dashboard)
Whenever you make a call to Stripe APIs, Stripe creates and stores API and
[Events](https://docs.stripe.com/api/events) objects for your Stripe [user
account](https://docs.stripe.com/get-started/account). The API key you specify
for the request determines whether the objects are stored in a sandbox
environment or in live mode. For example, the last request used your API secret
key, so Stripe stored the objects in a sandbox.

- To view the API request log:

- Open the [Logs](https://dashboard.stripe.com/test/workbench/logs) page.
- Click **200 OK POST /v1 customers**.
- To view the Event log:

- Open the [Events](https://dashboard.stripe.com/test/workbench/events) page.
- Click **jane.smith@email.com is a new customer**.
[Store your API
keys](https://docs.stripe.com/get-started/api-request#store-api-keys)
All accounts have a total of four API keys by default—two in a
[sandbox](https://docs.stripe.com/sandboxes), and two in live mode:

- **Sandbox secret key**: Use this key to authenticate requests on your server
when you’re testing in a sandbox. By default, you can use this key to perform
any API request without restriction.
- **Sandbox publishable key**: Use this key for testing purposes in your web or
mobile app’s client-side code.
- **Live mode secret key**: Use this key to authenticate requests on your server
when in live mode. By default, you can use this key to perform any API request
without restriction.
- **Live mode publishable key**: Use this key, when you’re ready to launch your
app, in your web or mobile app’s client-side code.

#### Testing and development

Use only your test API keys for testing and development. This ensures that you
don’t accidentally modify your live customers or charges.

You can find your secret and publishable keys in [API
keys](https://dashboard.stripe.com/test/apikeys). When you’re logged in,
Stripe’s documentation automatically populates code examples with your test API
keys (only you can see these values). If you’re not logged in, our code examples
include randomly generated API keys. You can replace them with your own test
keys or [log
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fapi-request)
to see the code examples populated with your test API keys. If you can’t view
your API keys, ask the owner of your Stripe account to add you to their
[team](https://docs.stripe.com/get-started/account/teams), with the proper
permissions.

The following table shows randomly generated examples of secret and publishable
test API keys:

#### Restricted API keys

The Dashboard can also generate restricted API keys, enabling customizable and
limited access to the API. However, Stripe doesn’t offer any restricted keys by
default.

Type Value When to useSecret`sk_test_BQokikJOvBiI2HlWgH4olfQ2`On the server
side: Must be secret and stored securely in your web or mobile app’s server-side
code (such as in an environment variable or credential management system) to
call Stripe APIs. Don’t expose this key on a website or embed it in a mobile
application.Publishable`pk_test_TYooMQauvdEDq54NiTphI7jx`On the client side: Can
be publicly accessible in your web or mobile app’s client-side code (such as
checkout.js) to securely collect payment information, such as with [Stripe
Elements](https://docs.stripe.com/payments/elements). By default, [Stripe
Checkout](https://docs.stripe.com/payments/checkout) securely collects payment
information.RestrictedA string that starts with `rk_test_`In microservices: Must
be secret and stored securely in your microservice code to call Stripe APIs.
Don’t expose this key on a website or embed it in a mobile application.
## See also

- [Set up your development
environment](https://docs.stripe.com/get-started/development-environment)
- [Stripe Shell](https://docs.stripe.com/stripe-shell/overview)

## Links

- [API keys](https://docs.stripe.com/keys)
- [test](https://docs.stripe.com/test-mode)
- [activate your account](https://docs.stripe.com/get-started/account/activate)
- [tour of the API](https://docs.stripe.com/payments-api/tour)
- [API reference](https://docs.stripe.com/api)
- [quickstart](https://docs.stripe.com/payments/quickstart)
- [Stripe Shell](https://docs.stripe.com/stripe-shell/overview)
- [sandbox](https://docs.stripe.com/sandboxes)
- [create a customer](https://docs.stripe.com/api/customers/create)
- [Events](https://docs.stripe.com/api/events)
- [user account](https://docs.stripe.com/get-started/account)
- [Logs](https://dashboard.stripe.com/test/workbench/logs)
- [Events](https://dashboard.stripe.com/test/workbench/events)
- [API keys](https://dashboard.stripe.com/test/apikeys)
- [log
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fapi-request)
- [team](https://docs.stripe.com/get-started/account/teams)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Set up your development
environment](https://docs.stripe.com/get-started/development-environment)