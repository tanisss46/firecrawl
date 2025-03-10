# API keys

## Use API keys to authenticate API requests.

Stripe authenticates your API requests using your account’s API keys. If a
request doesn’t include a valid key, Stripe returns an [invalid request
error](https://docs.stripe.com/error-handling#invalid-request-errors). If a
request includes a deleted or expired key, Stripe returns an [authentication
error](https://docs.stripe.com/error-handling#authentication-errors).

Use the [Developers Dashboard](https://dashboard.stripe.com/test/apikeys) to
create, reveal, delete, and roll API keys. To access your v1 API keys, select
the **API Keys** tab in your Dashboard.

## Sandbox versus live mode

All Stripe API requests occur in either a
[sandbox](https://docs.stripe.com/sandboxes) or live mode. Use a sandbox to
access test data, and live mode to access actual account data. Each mode has its
own set of API keys. Objects in one mode aren’t accessible to the other. For
instance, a sandbox [product
object](https://docs.stripe.com/api/products/object) can’t be part of a
live-mode payment.

#### Live mode key access

You can only reveal a live mode secret or restricted API key one time. If you
lose it, you can’t retrieve it from the Dashboard. In that case, roll it or
delete it and create a new one.

Type When to useObjectsHow to useConsiderationssandboxesUse a sandbox, and its
associated test API keys, as you build your integration. In a sandbox, card
networks and payment providers don’t process payments.API calls return simulated
objects. For example, you can retrieve and use test `account`, `payment`,
`customer`, `charge`, `refund`, `transfer`, `balance`, and `subscription`
objects.Use [test credit cards and
accounts](https://docs.stripe.com/testing#cards). You can’t accept real payment
methods or work with real accounts.[Identity](https://docs.stripe.com/identity)
doesn’t perform any verification checks. Also, Connect [account
objects](https://docs.stripe.com/api/accounts/object) don’t return sensitive
fields.live modeUse live mode, and its associated live API keys, when you’re
ready to launch your integration and accept real money. In live mode, card
networks and payment providers do process payments.API calls return real
objects. For example, you can retrieve and use real `account`, `payment`,
`customer`, `charge`, `refund`, `transfer`, `balance`, and `subscription`
objects.Accept real credit cards and work with customer accounts. You can accept
actual payment authorizations, charges, and captures for credit cards and
accounts.Disputes have a more nuanced flow and a simpler [testing
process](https://docs.stripe.com/testing#disputes). Also, some [payment
methods](https://docs.stripe.com/payments/payment-methods) have a more nuanced
flow and require more steps.
## Secret and publishable keys

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
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fkeys)
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
### Keep your keys safe

Anyone can use your live mode secret API key to make any API call on behalf of
your account, such as creating a charge or performing a refund. Keep your keys
safe by following the [secret API keys best
practices](https://docs.stripe.com/keys-best-practices).

#### Customize API access with restricted API keys

To provide limited access to the API, [create restricted API
keys](https://dashboard.stripe.com/test/apikeys/create). You can configure a
restricted API key to allow read or write access to specific API resources. When
using microservices that interact with the API on your behalf, define restricted
keys that allow only the minimum access those microservices require. For
example, if you use a dispute monitoring service, create a restricted key that
only provides read access to dispute-related resources. That key allows the
service to get the data it needs, but doesn’t allow it to make any changes or
access any other data.

Restricted keys can’t interact with many parts of Stripe’s API because they’re
only intended to reduce risk when using or building microservices. Don’t use
restricted keys as an alternative to your account’s secret or publishable API
keys during development of your Stripe integration.

#### Permission errors

If you use a restricted API key in a call it doesn’t have access to, Stripe
raises a [permission
error](https://docs.stripe.com/error-handling#permission-errors).

#### Limit the IP addresses that can send API requests

You can increase the security of a secret or restricted key by limiting the IP
addresses that can use it to send API requests. Additionally, you can [restrict
a key to one or more IP addresses or to a range of IP
addresses](https://docs.stripe.com/keys#limit-api-secret-keys-ip-address).

## Reveal a secret API key in a sandbox

With sandboxes, you can reveal a secret API key as many times as you want.

To reveal a secret key in a sandbox:

- In the Developers Dashboard, select the [API
keys](https://dashboard.stripe.com/test/apikeys) tab.
- In the **Standard keys** list, in the **Secret key** row, click **Reveal test
key**.
- the key value by clicking it.
- Save the key value.
- Click **Hide test key**.

## Reveal a secret or restricted API key for live mode

For security, in live mode Stripe only shows you a secret or restricted API key
one time. Store the key in a safe place where you won’t lose it. To help
yourself remember where you stored it, you can leave a note on the key in the
Dashboard. If you lose the key, you can roll it or delete it and create another.

#### You can't reveal a live mode secret key that you created

After you create a secret or restricted API key in live mode, we display the
value before you save it. You must copy the value before saving it because you
can’t reveal it later. You can only reveal a default secret key or a key
generated by a scheduled roll.

To reveal a secret or restricted key in live mode and attach a note:

#### Note

The `API keys` link here opens in live mode.

- In the Developers Dashboard, select the [API
keys](https://dashboard.stripe.com/apikeys) tab.
- In the **Standard keys** list or **Restricted keys** list, in the row for the
key you want to reveal, click **Reveal live key**.
- the key value by clicking it.
- Save the key value.
- Click **Hide test key**.
- Click the overflow menu () next to the key, then select **Edit key**.
- In the **Note** field, enter the location where you saved the key, then click
**Save**.
- If you created the key before Stripe introduced this feature, click **Hide
live key**.

#### Note

Keys that you created before Stripe introduced this feature aren’t automatically
hidden when they’re revealed. You must manually hide them.

## Roll an API key

Rolling a key revokes it and generates a replacement key. You can roll a key
immediately or schedule a key to roll after a certain time. Roll a key in
scenarios such as the following examples:

- If you’re in live mode and you lose a secret key or restricted key, you can’t
recover it from the Dashboard and must replace it.
- If a secret or restricted key is compromised, you need to revoke it to block
any potentially malicious API requests that might use it.
- Your policy requires rotating keys at certain intervals.

To roll an API key:

- Open the [API keys](https://dashboard.stripe.com/test/apikeys) page.
- In the row for the key you want to roll, click the overflow menu (), then
select **Roll key**.
- Choose an expiration date from the **Expiration** dropdown.
- Click **Roll API key**.
- The dialog displays the new key value. it by clicking it.
- Save the key value. You can’t retrieve it later.
- In the **Add a note** field, enter the location where you saved the key and
click **Done** or **Save**.

If you chose **Now** for the **Expiration**, we delete the old key. If you
selected a different time, you can see the time remaining until the key expires
below its name.

Regardless of the old key’s expiration time, the new key is ready to use
immediately.

When you roll a publishable key, the replacement key’s name is always
`Publishable key`. When you roll a secret key, the replacement key’s name is
always `Secret key`. When you roll a restricted key, the replacement key’s name
is the same as the rolled key. You can rename a secret or restricted key by
clicking its overflow menu and selecting **Edit key**.

## Delete a secret or restricted API key

If you delete a key, any code that uses that key can no longer make API calls.
Create a new key and update the code to use it.

#### Note

You can’t delete a publishable key.

To delete a key:

- In the Developers Dashboard, select the [API
keys](https://dashboard.stripe.com/test/apikeys) tab.
- Locate the key you want to delete in either the **Standard keys** or
**Restricted keys** list. Click the overflow menu icon () in the row of that
key, then select **Delete key**.
- In the Delete API key dialog, if you’re sure that you want to delete the key,
click **Delete key**. Otherwise, click **Cancel**.

## Create a secret API key

To create a secret API key:

- Open the [API keys](https://dashboard.stripe.com/test/apikeys) page.
- Click **Create secret key**.
- Stripe sends a verification code to your email address or in a text message.
(As with any email or text message, it might not arrive immediately.) Enter the
code in the dialog. If the dialog doesn’t continue automatically, click
**Continue**.
- Enter a name in the **Key name** field.
- Click **Create**.
- The dialog displays the new key value. it by clicking it.
- Save the key value. You can’t retrieve it later.
- In the **Add a note** field, enter the location where you saved the key and
click **Done**.

## Create a restricted API key

A [restricted API key](https://docs.stripe.com/keys#limit-access) only allows
the level of access that you specify.

To create a restricted API key:

- Open the [API keys](https://dashboard.stripe.com/test/apikeys) page.
- You can create a restricted key from scratch or start by cloning an existing
restricted key.- To create a restricted key from scratch, click **Create
restricted key**. In this case, the default value for all permissions is
**None**.
- To clone an existing key, in the row for the key you want to clone, click the
overflow menu (), then select **Duplicate key**. In this case, the default value
for each permission is its value in the cloned key.
- In the **Key name** field, enter a name. If you cloned an existing key, the
default name is the cloned key’s name.
- For each resource you want the new key to access, select the permission for
this key to allow. If you use Connect, you can also select the permission for
this key to allow when accessing connected accounts. Available permissions are
**None**, **Read**, or **Write**.
- Click **Create key**.
- Stripe sends a verification code to your email address or in a text message.
(As with any email or text message, it might not arrive immediately.) Enter the
code in the dialog. If the dialog doesn’t continue automatically, click
**Continue**.
- The dialog displays the new key value. it by clicking it.
- Save the key value. You can’t retrieve it later.
- In the **Add a note** field, enter the location where you saved the key and
click **Done**.

## Limit secret or restricted keys to a list or range of IP addresses

To limit API requests using a key to one or more specific IP addresses or to a
range of IP addresses:

#### Valid IP address ranges

You can specify any valid CIDR range. For example, a valid range could be
`100.10.38.0 - 100.10.38.255`, specified as `100.10.38.0/24`. All addresses in
the range must start with `100.10.38`.

- Open the [API keys](https://dashboard.stripe.com/test/apikeys) page.
- In the **Standard keys** list or **Restricted keys** list, in the row for the
key you want to reveal, click the overflow menu (), then select **Manage IP
restrictions**.
- Click **Limit use to a set of IP addresses**.
- Enter an IP address or range of IP addresses:- For an individual IP address,
enter it in the **IP address** field.
- For a range of IP addresses, enter the range in Classless Inter-Domain Routing
(CIDR) notation. In the **IP Address** field, enter the first address in the
range. In the **CIDR** field, enter the network prefix size.
- You can also select the **Bulk manage** tab and enter individual IP addresses
and ranges, separated by spaces. Changes you make in one tab appear in the other
tab.
- To add another address or range, click **+ Add**.
- Click **Save**.

## Change a secret or restricted API key’s name or note

To change the name or note text of a secret or restricted key:

- Open the [API keys](https://dashboard.stripe.com/test/apikeys) page.
- In the row for the key you want to change, click the overflow menu (), then
select **Edit key**.
- If you want to change the name, in **Key name**, enter the new name.
- If you want to change the note text, in **Note**, enter the new note text.
- Click **Save**.

## View the API request logs

To [open the API request
logs](https://docs.stripe.com/development/dashboard/request-logs), click the
overflow menu () for any key, then select **View request logs**. Opening the
logs redirects you to the main Stripe Dashboard.

## Links

- [invalid request
error](https://docs.stripe.com/error-handling#invalid-request-errors)
- [authentication
error](https://docs.stripe.com/error-handling#authentication-errors)
- [Developers Dashboard](https://dashboard.stripe.com/test/apikeys)
- [sandbox](https://docs.stripe.com/sandboxes)
- [product object](https://docs.stripe.com/api/products/object)
- [test credit cards and accounts](https://docs.stripe.com/testing#cards)
- [Identity](https://docs.stripe.com/identity)
- [account objects](https://docs.stripe.com/api/accounts/object)
- [testing process](https://docs.stripe.com/testing#disputes)
- [payment methods](https://docs.stripe.com/payments/payment-methods)
- [log
in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fkeys)
- [team](https://docs.stripe.com/get-started/account/teams)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [secret API keys best practices](https://docs.stripe.com/keys-best-practices)
- [create restricted API keys](https://dashboard.stripe.com/test/apikeys/create)
- [permission error](https://docs.stripe.com/error-handling#permission-errors)
- [API keys](https://dashboard.stripe.com/apikeys)
- [restricted API key](https://docs.stripe.com/keys#limit-access)
- [open the API request
logs](https://docs.stripe.com/development/dashboard/request-logs)