# App manifest reference

## Learn about the app manifest, an index of all fields, types, and descriptions for your app manifest file.

An app manifest describes how your app integrates with the Stripe platform.
Every Stripe app needs a `stripe-app.json` manifest file at the root of the
project directory structure.

You can update the app manifest using the [Stripe Apps
CLI](https://docs.stripe.com/stripe-apps/reference/cli), or you can edit it
directly. For instance, you can [add a
permission](https://docs.stripe.com/stripe-apps/reference/permissions) using the
command `stripe apps grant permission`, or by adding a
[permissionRequest](https://docs.stripe.com/stripe-apps/reference/app-manifest#permissionrequest)
to the app manifest directly.

App manifest files follow a
[schema](https://docs.stripe.com/stripe-apps/reference/app-manifest#schema)
described on this page.

## Example

```
{
 "id": "com.invoicing.[YOUR_APP]",
 "version": "1.2.3",
 "name": "[YOUR APP] Shipment Invoicing",
 "icon": "./[YOUR_APP]_icon_32.png",
 "distribution_type": "public",
 "permissions": [
 {
 "permission": "invoice_write",
 "purpose": "Allows [YOUR APP] to add shipping line items to an invoice."
 },
 {
 "permission": "product_read",
"purpose": "Allows [YOUR APP] to use product sizes for calculating shipping."
 }
 ],
 "ui_extension": {
 "views": [
 {
 "viewport": "stripe.dashboard.invoice.detail",
 "component": "AddShipping"
 }
 ],
 "content_security_policy": {
 "connect-src": [
 "https://api.example.com/a_specific_endpoint",
 "https://api.example.com/a_whole_subdirectory/"
 ],
 "image-src": [
 "https://images.example.com/one_image.jpg",
 "https://images.example.com/a_whole_subdirectory/"
 ],
"purpose": "These URLs allow the app to contact [YOUR APP] for creating shipping
details and loading images of shipping partner logos"
 }
 },
 "post_install_action": {
 "type": "external",
 "url": "https://example.com"
 },
 "constants": {
 "API_BASE": "https://api.example.com"
 }
}
```

## Schema

App manifest files are JSON files with these fields:

Field nameTypeExamplesidslugcom.invoicing.myappA globally unique identifier for
your app, defined by you. Stripe validates upon initial
submission.versionstring1.2.4An app version that you define. You can use
whatever format you want for version identifiers.namestringMy AppThe name shown
in the UI when referring to your app. Public distribution apps should not
include the words “Stripe”, “app”, “free” or “paid”.iconstring./favicon.pngThe
relative path within the app bundle to a 300x300 pixel PNG icon to show
alongside attribution.distribution_type“public” | “private”“public”The
[distribution type](https://docs.stripe.com/stripe-apps/distribution-options)
for the app.sandbox_install_compatibletrue | falsetrueEnable [sandbox
installs](https://docs.stripe.com/stripe-apps/enable-sandbox-support) for the
app.stripe_api_access_type“platform” | “oauth” | “restricted_api_key”oauthThe
[API authentication
method](https://docs.stripe.com/stripe-apps/api-authentication) of your
app.allowed_redirect_urisArray<String>noneThe URLs that users are redirected to
after installing your app with OAuth or with an install
link.permissionsArray<[PermissionRequest](https://docs.stripe.com/stripe-apps/reference/app-manifest#permissionrequest)>noneThe
permissions required by the app in order to
function.ui_extension[UIExtensionManifest](https://docs.stripe.com/stripe-apps/reference/app-manifest#uiextensionmanifest)noneConfiguration
specific to the “UI Extension”
capability.post_install_action[PostInstallAction](https://docs.stripe.com/stripe-apps/reference/app-manifest#postinstallaction)noneAn
optional configuration to direct users to custom location after an app is
installed.constantsObject`{"API_BASE": "https://api.example.com/v1"}`An object
with arbitrary constant values that you can access in the [UI extension context
props](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#props)
and [override for local development using the CLI manifest
flag](https://docs.stripe.com/stripe-apps/reference/app-manifest#extended-manifest).
### PermissionRequest

A permission request has these fields:

Field nameTypeExamplepermissionstringcustomer_writePermissions that the app is
requesting. [Learn more about
permissions](https://docs.stripe.com/stripe-apps/reference/permissions).purposestring
| Map<locale, string>“This app loads images from images.example.com.”A
user-facing explanation that tells people installing your app why it needs these
permissions.namestring“Necessary for [YOUR APP] to update invoices with selected
shipping charges”A Stripe-facing explanation that tells app reviewers why your
app needs these permissions.
### UiExtensionManifest

A UI extension manifest has these fields:

Field
nameTypeExampleviewsArray<[ViewManifest](https://docs.stripe.com/stripe-apps/reference/app-manifest#viewmanifest)>noneReact
components that show up in the Dashboard in a distinct place. [Learn
more](https://docs.stripe.com/stripe-apps/design#types-of-views).content_security_policy[CSPRequest](https://docs.stripe.com/stripe-apps/reference/app-manifest#csprequest)noneRequest
for your UI extension to be granted access to specific URLs for a specific
purpose.
### ViewManifest

A view manifest has these fields:

Field nameTypeExampleviewportstringstripe.dashboard.invoice.detailAn identifier
that indicates where a UI extension might appear within the Dashboard. See the
[list of available
viewports](https://docs.stripe.com/stripe-apps/reference/viewports).componentstringAddShippingSelectorAn
exported React component that uses one of our [view
components](https://docs.stripe.com/stripe-apps/components#views).
### CSPRequest

A content security policy request has these fields:

Field
nameTypeExampleconnect-srcArray<string>https://o0.ingest.sentry.io/api/URLs of
permitted third-party APIs. If the URL ends in a slash, all of its children also
receive permission. See [Use third-party
APIs](https://docs.stripe.com/stripe-apps/build-ui#use-third-party-apis) for
details.image-srcArray<string>https://images.example.com/URLs the
[Img](https://docs.stripe.com/stripe-apps/components/img) component can load
from. If the URL ends in a slash, all of its children also receive
permission.purposestring | Map<locale, string>“This app loads images from
https://images.example.com and sends anonymous error reports to our partner
Sentry for debugging purposes."An explanation to show users when the app is
installed that explains why the plugin needs to communicate directly with these
URLs.
URLs must conform to the [CSP
spec](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP). We only allow
HTTPS schemes.

### PostInstallAction

A post-install action has these fields:

Field nameTypeExampletypestring`external`, `settings`Additional action after
users installed your app in the Stripe Dashboard. For more information, see
[Enable post-install
configuration](https://docs.stripe.com/stripe-apps/post-install-actions).urlstringhttps://example.comExternal
URL to redirect users to after installing your app. This is required only if the
post-install action type is `external`.
## Use an extended manifest file for development

During local development you may need to use different [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest) values
than those you use in production. For example, your app’s backend could be
located at `https://api.example.com/v1` but your local development backend runs
at `http://localhost:8888/v1`.

Given this example of a manifest file:

```
{
 "id": "com.invoicing.[YOUR_APP]",
 "version": "1.2.3",
 "name": "[YOUR APP] Shipment Invoicing",
 "icon": "./[YOUR_APP]_icon_32.png",
 "permissions": [],
 "ui_extension": {
 "views": [
 {
 "viewport": "stripe.dashboard.invoice.detail",
 "component": "InvoiceDetail"
 }
 ],
 "content_security_policy": {
 "connect-src": ["https://api.example.com/v1"],
 "purpose": "Allow the app to retrieve example data"
 }
 },
 "constants": {
 "API_BASE": "https://api.example.com/v1"
 }
}
```

Create another manifest file called `stripe-app.[anything].json` that extends
your main manifest and overrides it with local values. For example:

```
{
 "extends": "stripe-app.json",
 "ui_extension": {
 "content_security_policy": {
 "connect-src": ["http://localhost:8888/v1"]
 }
 },
 "constants": {
 "API_BASE": "http://localhost:8888/v1"
 }
}
```

To use the local manifest file during development, load it using the
`--manifest` flag. For example:

```
stripe apps start --manifest stripe-app.dev.json
```

Access the `constants` values in your views using [context
props](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#props).
For example:

```
import {useEffect, useState} from 'react';
import type {ExtensionContextValue} from '@stripe/ui-extension-sdk/context';
import {Box} from '@stripe/ui-extension-sdk/ui';

const InvoiceDetail = ({environment}: ExtensionContextValue) => {
 const [data, setData] = useState(null);

 useEffect(() => {
 fetch(`${environment.constants.API_BASE}/some-endpoint`)
 .then(response => response.json())
 .then(json => setData(json));
 }, []);

 return data ? <Box>Here is your message: {data.message}</Box> : 'Loading...';
};
```

## See also

- [Stripe Apps CLI reference](https://docs.stripe.com/stripe-apps/reference/cli)
- [Permissions
reference](https://docs.stripe.com/stripe-apps/reference/permissions)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)

## Links

- [Stripe Apps CLI](https://docs.stripe.com/stripe-apps/reference/cli)
- [add a permission](https://docs.stripe.com/stripe-apps/reference/permissions)
-
[https://api.example.com/a_specific_endpoint](https://api.example.com/a_specific_endpoint)
-
[https://api.example.com/a_whole_subdirectory/](https://api.example.com/a_whole_subdirectory/)
-
[https://images.example.com/one_image.jpg](https://images.example.com/one_image.jpg)
-
[https://images.example.com/a_whole_subdirectory/](https://images.example.com/a_whole_subdirectory/)
- [https://example.com](https://example.com)
- [https://api.example.com](https://api.example.com)
- [distribution type](https://docs.stripe.com/stripe-apps/distribution-options)
- [sandbox installs](https://docs.stripe.com/stripe-apps/enable-sandbox-support)
- [API authentication
method](https://docs.stripe.com/stripe-apps/api-authentication)
- [UI extension context
props](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api#props)
- [Learn more](https://docs.stripe.com/stripe-apps/design#types-of-views)
- [list of available
viewports](https://docs.stripe.com/stripe-apps/reference/viewports)
- [view components](https://docs.stripe.com/stripe-apps/components#views)
- [Use third-party
APIs](https://docs.stripe.com/stripe-apps/build-ui#use-third-party-apis)
- [Img](https://docs.stripe.com/stripe-apps/components/img)
- [CSP spec](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
- [Enable post-install
configuration](https://docs.stripe.com/stripe-apps/post-install-actions)
- [app manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [https://api.example.com/v1](https://api.example.com/v1)
- [http://localhost:8888/v1](http://localhost:8888/v1)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)