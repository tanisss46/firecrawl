# Enable sandbox support for your public appDeveloper preview

## Enable your public app for sandbox installation

#### Developer preview

Sandboxes is currently in developer preview. Share your feedback on [Stripe
Insiders](https://insiders.stripe.dev/c/stripe-apps), our new early access
program.

A [sandbox](https://docs.stripe.com/sandboxes) is an isolated test environment.
Use your sandbox to test Stripe functionality in your account and experiment
without affecting your live integration. Users can install apps in sandboxes to
evaluate their features and functionality.

## Managed sandboxes

A *managed sandbox* is a unique type of sandbox that Stripe automatically
creates in your account to support your public Stripe app.

- Stripe automatically creates a managed sandbox the first time you upload a
public app.
- When a user installs your app into their sandbox, it establishes a connection
to your managed sandbox.
- You can [debug and monitor](https://docs.stripe.com/workbench/guides) events
from user sandbox installs inside your managed sandbox.
- Changes made to a managed sandbox don’t affect users installing your app in
live or test mode.
- You can’t delete a managed sandbox.

### Create a managed sandbox

Stripe automatically creates a managed sandbox for you the first time you
[upload a public Stripe
app](https://docs.stripe.com/stripe-apps/upload-install-app) to your account.

For public apps uploaded before February 3, 2025, Stripe automatically created a
managed sandbox in your account.

## Enable sandbox support for your app

By default, users can’t install your public app into a sandbox without
additional work.

Similar to [test mode](https://docs.stripe.com/stripe-apps/handling-modes), you
can enable sandbox installs by updating the [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest). After you
enable sandbox support, [submit your app for
review](https://docs.stripe.com/stripe-apps/publish-app). App sandbox support is
verified as part of the [app review
process](https://docs.stripe.com/stripe-apps/review-requirements).

### Steps to enable sandbox installs for your public app

- Update the app manifest to support sandbox installs.
- *(Optional)* Create sandbox-specific event hooks inside your managed sandbox.
Update server-side logic to listen for these new endpoints.
- *(Optional)* Update server-side logic to use your [managed sandbox API
keys](https://docs.stripe.com/sandboxes/dashboard/manage-access) when making
Stripe API calls for a sandbox install.
- Upload a new version of your app to your main account (**not** your managed
sandbox).
- From your main account, [create an external test
link](https://docs.stripe.com/stripe-apps/test-app) for the sandbox-enabled
version you just uploaded.
- Create and open a new sandbox to test your updated app.
- In a browser window, visit the external test link you created earlier to
install your app.
- Test that your app works as expected when installed in a sandbox.
- Submit your new version for marketplace review.

### Update the app manifest

#### Note

As of February 3, 2025, you must declare sandbox support as true or false in the
app manifest for apps published to the marketplace.

To support installing your app in a sandbox, declare sandbox support in the [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest#schema)
with `sandbox_install_compatible`.

The following example code declares sandbox support:

```
{
 "id": "com.invoicing.[YOUR_APP]",
 "version": "1.2.3",
 "name": "[YOUR APP] Shipment Invoicing",
 "icon": "./[YOUR_APP]_icon_32.png",
 "distribution_type": "public",
 "sandbox_install_compatible": true,
 [...]
}
```

### Understanding sandbox connections

When a user installs your public app into their sandbox, a connection is made to
your managed sandbox. This differs from the behavior when your app is installed
in live mode or test mode.

- When a user installs an app into a sandbox, a connection is made to your
managed sandbox.
- When a user installs an app in live mode, a connection is made to your live
mode and test mode.
- When a user installs an app in test mode, a connection is made to your test
mode.

### Webhook events

If your app listens to events from your users’ installs, there is additional
setup to handle apps installed in sandboxes.

- Inside your managed sandbox, create new webhooks for sandbox events.
- If a user installs your app into a sandbox, Stripe sends any applicable events
only to your managed sandbox endpoints.
- Update your server-side logic to handle sandbox specific events.

#### Note

See [event
behavior](https://docs.stripe.com/stripe-apps/build-backend#event-behavior-depends-on-install-mode)
to learn more about how the install mode affects event behavior.

### API keys

Your managed sandbox has its own set of [API Keys](https://docs.stripe.com/keys)
for making calls for sandbox installs. When responding to sandbox-specific
webhooks or events you must use these [managed sandbox
keys](https://docs.stripe.com/sandboxes/dashboard/manage-access).

You can find the correct API keys to use for sandbox installs inside your
managed sandbox.

### OAuth sandbox links

#### Developer preview

Sandbox app support is currently in developer preview.

Apps in sandboxes don’t currently support testing OAuth apps. If your app uses
RAK or Platform authentication no changes are required.

## Testing your app in a sandbox

After you’ve updated your app to handle sandbox installs, you can test your app
in your own sandbox.

- From your main account, [create an External test
link](https://docs.stripe.com/stripe-apps/test-app) for the sandbox-enabled
version you just uploaded.
- Create a new sandbox to test your updated app. Open the new sandbox.
- In a new browser window visit the External test link you created earlier to
install your app.
- Test your app works as expected installed in a sandbox.

### Validating sandbox API keys and webhook behavior

You can use [Workbench](https://docs.stripe.com/workbench) to validate that your
sandbox installation works correctly.

- Inside your *test sandbox*, perform some example actions.
- Next, inside your *managed sandbox*, open Workbench.

Use Workbench to inspect your app behavior, including [reviewing API
logs](https://docs.stripe.com/workbench/guides#view-logs-by-source), and
[filtering events](https://docs.stripe.com/workbench/guides#filter-events). If
you have updated your app correctly you can see all the API calls and webhook
events for your example actions.

If you don’t see the expected events or responses, double check you’re inside
your managed sandbox. Also check you have set up your sandbox specific webhook
endpoints, and that your app is using the correct sandbox API keys as
appropriate.

### Submit your app for review

After you enable sandbox support and validate your app works as expected inside
a sandbox, you can [submit your app for
review](https://docs.stripe.com/stripe-apps/publish-app). App sandbox support is
verified as part of the [app review
process](https://docs.stripe.com/stripe-apps/review-requirements) and listed on
the details page for your app listing.

## Links

- [Stripe Insiders](https://insiders.stripe.dev/c/stripe-apps)
- [sandbox](https://docs.stripe.com/sandboxes)
- [debug and monitor](https://docs.stripe.com/workbench/guides)
- [upload a public Stripe
app](https://docs.stripe.com/stripe-apps/upload-install-app)
- [test mode](https://docs.stripe.com/stripe-apps/handling-modes)
- [app manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [submit your app for review](https://docs.stripe.com/stripe-apps/publish-app)
- [app review process](https://docs.stripe.com/stripe-apps/review-requirements)
- [managed sandbox API
keys](https://docs.stripe.com/sandboxes/dashboard/manage-access)
- [create an external test link](https://docs.stripe.com/stripe-apps/test-app)
- [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest#schema)
- [event
behavior](https://docs.stripe.com/stripe-apps/build-backend#event-behavior-depends-on-install-mode)
- [API Keys](https://docs.stripe.com/keys)
- [Workbench](https://docs.stripe.com/workbench)
- [reviewing API
logs](https://docs.stripe.com/workbench/guides#view-logs-by-source)
- [filtering events](https://docs.stripe.com/workbench/guides#filter-events)