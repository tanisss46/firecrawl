# Handling different modesPublic preview

## Learn how to adapt your app to handle both live mode and test mode.

During installation, users can choose which mode to install your app into.

![The location of the mode selection option during the Stripe App installation
flow](https://b.stripecdn.com/docs-statics-srv/assets/mode-selector.2f3a4f6e4859b919ef569502676ab6a0.png)

## Try it in test mode option

In the App Marketplace, potential users see a `Try in test mode` option to
encourage them to try out an app.

![The location of the "Try it in test mode" call to action in the App
Marketplace](https://b.stripecdn.com/docs-statics-srv/assets/try-in-test.5be4b5aa707d1ebf58051bbf9fa40078.png)

#### Caution

If your app uses the OAuth API access type or an external install url, the `Try
in test mode` option won’t be shown in the App Marketplace.

## Shortcut to install in opposite mode

If a user has one mode installed, you can install the other mode directly from
the Stripe Dashboard.

![The location of the button in the Stripe Dashboard to install the app in the
opposite
mode](https://b.stripecdn.com/docs-statics-srv/assets/install-other-mode.88bf3eb2939060f4f0fe172822587ee8.png)

## Webhooks

If your app is set up to [listen to events for your installed users
accounts](https://docs.stripe.com/stripe-apps/events), it requires additional
setup to make sure you can handle having your app installed in test mode.

If a user installs your app into live mode only, any applicable live mode events
are sent to your live mode webhook endpoints. If a user installs your app into
test mode only, any applicable test mode events are sent to your test mode
webhook endpoints. If a user installs your app into both live mode and test
mode, test mode events are sent to your test mode *and* live mode webhook
endpoints and live mode events are sent only to your live mode webhook
endpoints.

#### Note

We recommend that you set up both live mode and test mode webhook endpoints to
make sure that both modes are properly supported. See [event
behavior](https://docs.stripe.com/stripe-apps/build-backend#event-behavior-depends-on-install-mode)
for more information and examples about how the install mode affects event
behavior.

## OAuth test mode links

OAuth apps initiate app installation from within their platform. The developer
is responsible for implementing a test mode install link if you want test mode
support. The Stripe Dashboard provides a test mode OAuth install link.

![The location of public OAuth links within the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/public-oauth-links.bef9bbbf32bcac8e16ff9515fc4169e4.png)

The Stripe Apps OAuth documentation has more information on [creating OAuth
install
links](https://docs.stripe.com/stripe-apps/api-authentication/oauth#create-install-link).

## See also

- [Webhooks](https://docs.stripe.com/webhooks)
- [Event destinations](https://docs.stripe.com/event-destinations)
- [Server-side logic](https://docs.stripe.com/stripe-apps/build-backend)
- [OAuth 2.0 API Authentication
Type](https://docs.stripe.com/stripe-apps/api-authentication/oauth)

## Links

- [listen to events for your installed users
accounts](https://docs.stripe.com/stripe-apps/events)
- [event
behavior](https://docs.stripe.com/stripe-apps/build-backend#event-behavior-depends-on-install-mode)
- [creating OAuth install
links](https://docs.stripe.com/stripe-apps/api-authentication/oauth#create-install-link)
- [Webhooks](https://docs.stripe.com/webhooks)
- [Event destinations](https://docs.stripe.com/event-destinations)
- [Server-side logic](https://docs.stripe.com/stripe-apps/build-backend)
- [OAuth 2.0 API Authentication
Type](https://docs.stripe.com/stripe-apps/api-authentication/oauth)