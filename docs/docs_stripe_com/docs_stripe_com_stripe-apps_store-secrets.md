# Store secret credentials and tokens in your app

## Use the Secret Store API to persist sensitive data, like authentication credentials.

The [Secret Store API](https://docs.stripe.com/api/secret_management) is a way
to securely set, find, list, and delete persistent secrets used in Stripe Apps.
These credentials, also known as secrets, are only accessible to your app and
the users who own them.

## Overview

The Secret Store API enables your app to:

- Securely store and retrieve authentication credentials
- Keep users authenticated with third-party services, even if they sign out of
`stripe.com` and sign in again
- Securely pass secrets between your UI extension and backend

#### Caution

Stripe **does not** permit you to store sensitive personal data, personal
account numbers such as credit card numbers, and other data within [PCI
Compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
using the Secret Store API.

### Scopes

The secrets of an uploaded app are only accessible by other apps that you’ve
uploaded. You can only publish one app on an account, so published apps can
never share secrets. Requests made by third-party apps can’t ever access your
app’s secrets.

Use scopes to further specify the accessibility of a given secret. A scope is a
collection of secrets identified by its accessibility.

The Secret Store API supports the following scope types:

Scope typeScope limitsStores up toUse forAccessible to[account
scope](https://docs.stripe.com/api/apps/secret_store/secret_resource#secret_object-scope)There’s
one `account` scope per app. Example: third-party API keyA maximum of 10
[Secrets](https://docs.stripe.com/api/apps/secret_store/secret_resource)Secrets
that apply to all users of a Stripe account that installs your appAll Dashboard
users of a Stripe account and the app’s backend, on a per-app basis[user
scope](https://docs.stripe.com/api/apps/secret_store/secret_resource#secret_object-scope)Each
user has one `user` scope per app. Example: OAuth access tokenA maximum of 10
[Secrets](https://docs.stripe.com/api/apps/secret_store/secret_resource)Secrets
that only apply to a specific user of a Stripe accountA specific Dashboard user
of a Stripe account and the app’s backend, on a per-app basis
The diagram below shows the secret scoping between the following:

- The Stripe account: “The Cactus Practice Stripe account”
- Two users sharing the same Stripe account: “User 1”, “User 2”
- Two different apps installed by the Stripe account: “Installed App A”,
“Installed App B”
- `account` scoped secrets: “Foo API key” secret for App A, “Bar API key” for
App B
- `user` scoped secrets: “OAuth access token”, “OAuth refresh token”

![account secret
relationship](https://b.stripecdn.com/docs-statics-srv/assets/secret_scoping_diagram.32c3c7d35e007d261389cf593bec470f.png)

The scoped secrets of two different apps installed by the Cactus Practice Stripe
account.

### Expiration

If a secret becomes invalid at some point in the future, you can specify an
expiration time by setting the optional
[expires_at](https://docs.stripe.com/api/apps/secret_store/secret_resource#secret_object-expires_at)
parameter when you [set a
secret](https://docs.stripe.com/stripe-apps/store-secrets#set-a-secret). This
parameter takes in a Unix timestamp (the number of seconds elapsed since the
Unix epoch).

After the `expires_at` date has passed, the secret is automatically deleted from
the Secret Store API.

Expiration times can’t be in the past and can’t be more than 100 years in the
future.

## Set a secret

- Add the `secret_write` permission to your app:

```
stripe apps grant permission "secret_write" "Allows storing secrets between page
reloads"
```
- Set a secret by name and scope in the Secret Store API. You can use the
following example code in your app’s UI extension or backend:

```
import { createHttpClient, STRIPE_API_KEY } from
'@stripe/ui-extension-sdk/http_client';
import Stripe from 'stripe';
import type { ExtensionContextValue } from '@stripe/ui-extension-sdk/context';
import { useEffect } from 'react';

// Create an instance of a Stripe object to access customer information.
// You don't need an API Key here, because the app uses the
// dashboard credentials to make requests.
const stripe: Stripe = new Stripe(STRIPE_API_KEY, {
 httpClient: createHttpClient() as Stripe.HttpClient,
 apiVersion: '2025-02-24.acacia',
});

const App = ({userContext}: ExtensionContextValue) => {
 useEffect(() => {
 stripe.apps.secrets.create({
 scope: { type: 'user', user: userContext.id },
 name: 'secret_name',
 payload: 'secret value',
 expires_at: 1956528000 // optional
 }).then(resp => console.log(resp));
 }, []);

 return null;
};

export default App;
```

For more information, see the API reference documentation on [setting a
secret](https://docs.stripe.com/api/apps/secret_store/set).

## Find a secret

You can find a secret by name and scope in the Secret Store API. For example,
use the following example code in your app’s UI extension or backend:

```
import Stripe from 'stripe';
import { createHttpClient, STRIPE_API_KEY } from
'@stripe/ui-extension-sdk/http_client';
import type { ExtensionContextValue } from '@stripe/ui-extension-sdk/context';
import { useEffect } from 'react';

// Create an instance of a Stripe object to access customer information.
// You don't need to use an API key, because the app uses the
// dashboard credentials to make requests.
const stripe: Stripe = new Stripe(STRIPE_API_KEY, {
 httpClient: createHttpClient() as Stripe.HttpClient,
 apiVersion: '2025-02-24.acacia',
});

const App = ({userContext}: ExtensionContextValue) => {
 useEffect(() => {
 stripe.apps.secrets.find({
 scope: { type: 'user', user: userContext.id },
 name: 'secret_name',
 expand: ['payload'],
 }).then(resp => console.log(resp.payload));
 }, []);

 return null;
};

export default App;
```

For more information, see [Find a
secret](https://docs.stripe.com/api/apps/secret_store/find).

## Delete a secret

To delete a secret by name and scope in the Secret Store API, you can use the
following example code in your app’s UI extension or backend:

```
import Stripe from 'stripe';
import { createHttpClient, STRIPE_API_KEY } from
'@stripe/ui-extension-sdk/http_client';
import type { ExtensionContextValue } from '@stripe/ui-extension-sdk/context';
import { useEffect } from 'react';

// Create an instance of a Stripe object to access customer information.
// Note that you don't need to use an API key, because the app uses the
// dashboard credentials to make requests.
const stripe: Stripe = new Stripe(STRIPE_API_KEY, {
 httpClient: createHttpClient() as Stripe.HttpClient,
 apiVersion: '2025-02-24.acacia',
});

const App = ({userContext}: ExtensionContextValue) => {
 useEffect(() => {
 stripe.apps.secrets.deleteWhere({
 scope: { type: 'user', user: userContext.id },
 name: 'secret_name',
 }).then(resp => console.log(resp));
 }, []);

 return null;
};

export default App;
```

For more information, see [Delete a
secret](https://docs.stripe.com/api/apps/secret_store/delete).

## List secrets

If you stored the maximum amount of secrets in an `account` or `user` scope and
want to add another secret, you must delete at least 1 of the 10 secrets. To
determine which secrets to delete, you can list all the secrets for a given
scope.

To list the secrets of an `account` or `user` scope, you can use the following
example code in your app’s UI extension or backend:

```
import Stripe from 'stripe';
import { createHttpClient, STRIPE_API_KEY } from
'@stripe/ui-extension-sdk/http_client';
import type { ExtensionContextValue } from '@stripe/ui-extension-sdk/context';
import { useEffect } from 'react';

// Create an instance of a Stripe object to access customer information.
// Note that you don't need to use an API key, because the app uses the
// dashboard credentials to make requests.
const stripe: Stripe = new Stripe(STRIPE_API_KEY, {
 httpClient: createHttpClient() as Stripe.HttpClient,
 apiVersion: '2025-02-24.acacia',
});

const App = ({userContext}: ExtensionContextValue) => {
 useEffect(() => {
 stripe.apps.secrets.list({
 scope: { type: 'user', user: userContext.id },
 }).then(resp => console.log(resp.data));
 }, []);

 return null;
};

export default App;
```

For more information, see [List
secrets](https://docs.stripe.com/api/apps/secret_store/list).

## Example apps

The following example apps demonstrate how to use the Secret Store API:

- [Simple demo
app](https://github.com/stripe/stripe-apps/tree/master/examples/secret-store)
- [Dropbox OAuth with PKCE
app](https://github.com/stripe/stripe-apps/tree/master/examples/dropbox-oauth-pkce)

## See also

- [Authorization flows](https://docs.stripe.com/stripe-apps/pkce-oauth-flow)
- [Server-side logic](https://docs.stripe.com/stripe-apps/build-backend)
- [Build a UI](https://docs.stripe.com/stripe-apps/build-ui)

## Links

- [Secret Store API](https://docs.stripe.com/api/secret_management)
- [PCI
Compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [account
scope](https://docs.stripe.com/api/apps/secret_store/secret_resource#secret_object-scope)
- [Secrets](https://docs.stripe.com/api/apps/secret_store/secret_resource)
-
[expires_at](https://docs.stripe.com/api/apps/secret_store/secret_resource#secret_object-expires_at)
- [set a secret](https://docs.stripe.com/stripe-apps/store-secrets#set-a-secret)
- [setting a secret](https://docs.stripe.com/api/apps/secret_store/set)
- [Find a secret](https://docs.stripe.com/api/apps/secret_store/find)
- [Delete a secret](https://docs.stripe.com/api/apps/secret_store/delete)
- [List secrets](https://docs.stripe.com/api/apps/secret_store/list)
- [Simple demo
app](https://github.com/stripe/stripe-apps/tree/master/examples/secret-store)
- [Dropbox OAuth with PKCE
app](https://github.com/stripe/stripe-apps/tree/master/examples/dropbox-oauth-pkce)
- [Authorization flows](https://docs.stripe.com/stripe-apps/pkce-oauth-flow)
- [Server-side logic](https://docs.stripe.com/stripe-apps/build-backend)
- [Build a UI](https://docs.stripe.com/stripe-apps/build-ui)