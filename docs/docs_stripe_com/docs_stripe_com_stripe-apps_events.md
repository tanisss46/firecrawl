# Listen for events

## Listen for events on your installed users accounts

Apps can use [Webhooks](https://docs.stripe.com/webhooks) to get alerts about
events happening on their users’ accounts. This helps app developers keep
information in sync or trigger actions within their app when something changes.

## Get started

- [Handle webhook events in your app’s back
end](https://docs.stripe.com/webhooks#webhook-endpoint-def).
- [Register a webhook
endpoint](https://docs.stripe.com/webhooks#webhooks-summary) in the Stripe
Dashboard, and select **Listen to events on Connected accounts**.
- Register a test mode webhook endpoint in the Stripe Dashboard. Apps can be
installed in both live and [test
mode](https://docs.stripe.com/stripe-apps/build-backend#event-behavior-depends-on-install-mode).
We also recommend setting up a test mode endpoint to handle test mode events.
Recommended
- Add the required permissions to your app by running `stripe apps grant
permission` for each one.
```
stripe apps grant permission "PERMISSION_NAME" "EXPLANATION"
```

Replace:- `PERMISSION_NAME` with the permission name.
- `EXPLANATION` with an explanation for enabling access. Users see this
explanation when they install your app.

You must add the `event_read` permission, plus any permissions associated with
the specific events you want to handle. For information about which permissions
a particular event requires, see [Event
permissions](https://docs.stripe.com/stripe-apps/reference/permissions#event).

For example, if you want to handle the `payment_intent.succeeded` and
`setup_intent.succeeded` events, run the following commands:

```
stripe apps grant permission "event_read" "Read webhook event data"
stripe apps grant permission "checkout_session_read" "Read Checkout Session data
in webhook events"
stripe apps grant permission "payment_intent_read" "Read PaymentIntent data in
webhook events"
stripe apps grant permission "setup_intent_read" "Read SetupIntent data in
webhook events"
```

After you run those commands, your app manifest file might look like this:

```
{
 "id": "com.example.app",
 "version": "1.2.3",
 "name": "Example App",
 "icon": "./example_icon_32.png",
 "permissions": [
 {
 "permission": "event_read",
 "purpose": "Read webhook event data"
 }
 {
 "permission": "checkout_session_read",
 "purpose": "Read Checkout Session data in webhook events"
 }
 {
 "permission": "payment_intent_read",
 "purpose": "Read PaymentIntent data in webhook events"
 }
 {
 "permission": "setup_intent_read",
 "purpose": "Read SetupIntent data in webhook events"
 }
 ],
}
```

## Listen for events on your account

To receive events for an app that’s private to users on your account only:

- Handle [webhook events](https://docs.stripe.com/webhooks#webhook-endpoint-def)
in your app’s back end.
- [Register a webhook
endpoint](https://docs.stripe.com/webhooks#webhooks-summary) in the Stripe
Dashboard.

## Receive event notifications about your app

Listen for events (such as user installs or uninstalls) on your Stripe app using
incoming [webhooks](https://docs.stripe.com/webhooks) so your integration can
automatically trigger reactions in your back end such as:

- Creating user accounts
- Updating permissions
- Disabling a user’s account and removing data

In addition to the [types of events Stripe
supports](https://docs.stripe.com/api/events/types), Stripe Apps also supports
the following events:

Merchant actionResulting webhook event sent to the app’s backendConnect or
install your
app[account.application.authorized](https://docs.stripe.com/api/events/types#event_types-account.application.authorized)Disconnect
or uninstall your
app[account.application.deauthorized](https://docs.stripe.com/api/events/types#event_types-account.application.deauthorized)
## Test webhooks locally

You can test webhooks locally for:

- An app that’s only available to all users on your account and listens to
events on your own account
- An app that’s available on the Stripe App Marketplace and listens to events on
accounts that have installed your app

To test webhooks locally:

- [Install the Stripe CLI](https://docs.stripe.com/stripe-cli).
- Authenticate your account:

```
stripe login
```
- Open two terminal windows:

- In one terminal window, [Set up event
forwarding](https://docs.stripe.com/webhooks#local-listener):

Public listing on App MarketplacePrivate to your account only
```
stripe listen --forward-connect-to localhost:{{PORT}}/webhook
```
- In the other terminal window, [Trigger events to test your webhooks
integration](https://docs.stripe.com/webhooks#trigger-test-events):

Public listing on App MarketplacePrivate to your account only
```
stripe trigger --stripe-account {{EVENT_NAME}}
```

For more information, see our docs on [testing a webhook
endpoint](https://docs.stripe.com/webhooks#local-listener).

## See also

- [Server-side logic](https://docs.stripe.com/stripe-apps/build-backend)
- [Permissions
reference](https://docs.stripe.com/stripe-apps/reference/permissions)
- [API Authentication
Types](https://docs.stripe.com/stripe-apps/api-authentication)
- [Event destinations](https://docs.stripe.com/event-destinations)
- [Webhooks](https://docs.stripe.com/webhooks)

## Links

- [Webhooks](https://docs.stripe.com/webhooks)
- [Handle webhook events in your app’s back
end](https://docs.stripe.com/webhooks#webhook-endpoint-def)
- [Register a webhook
endpoint](https://docs.stripe.com/webhooks#webhooks-summary)
- [test
mode](https://docs.stripe.com/stripe-apps/build-backend#event-behavior-depends-on-install-mode)
- [Event
permissions](https://docs.stripe.com/stripe-apps/reference/permissions#event)
- [types of events Stripe supports](https://docs.stripe.com/api/events/types)
-
[account.application.authorized](https://docs.stripe.com/api/events/types#event_types-account.application.authorized)
-
[account.application.deauthorized](https://docs.stripe.com/api/events/types#event_types-account.application.deauthorized)
- [Install the Stripe CLI](https://docs.stripe.com/stripe-cli)
- [Set up event forwarding](https://docs.stripe.com/webhooks#local-listener)
- [Trigger events to test your webhooks
integration](https://docs.stripe.com/webhooks#trigger-test-events)
- [Server-side logic](https://docs.stripe.com/stripe-apps/build-backend)
- [Permissions
reference](https://docs.stripe.com/stripe-apps/reference/permissions)
- [API Authentication
Types](https://docs.stripe.com/stripe-apps/api-authentication)
- [Event destinations](https://docs.stripe.com/event-destinations)