# Add deep links

## Create deep links that navigate users to your Stripe app.

A deep link is a URL that reduces the number of navigation steps required for
the user to open your app in the Dashboard. You can share deep links in user
interfaces such as an email or website or use them when [creating OAuth
authorization workflows](https://docs.stripe.com/stripe-apps/pkce-oauth-flow).

## Before you begin

To navigate users to a Dashboard page that displays your app, you need an app
with [UI functionality](https://docs.stripe.com/stripe-apps/build-ui).

[Create the deep link
URL](https://docs.stripe.com/stripe-apps/deep-links#create-deep-link-URL)
To create the URL of the deep link, you must use:

- The URL of a Dashboard page where you’ve defined a view
- The `open_drawer_app` parameter
- Your application ID, which is specified in the [id field of your
stripe-app.json manifest
file](https://docs.stripe.com/stripe-apps/reference/app-manifest#schema)

For example, if you define a view on the Customers page in the Dashboard
(`https://dashboard.stripe.com/test/customers?`) and your application ID is
`com.example.deep-link`:

- The [test mode](https://docs.stripe.com/test-mode) deep link is:

```
<a
href="https://dashboard.stripe.com/test/customers?open_drawer_app=com.example.deep-link">Deep
Link</a>

```
- The live mode deep link is:

```
<a
href="https://dashboard.stripe.com/customers?open_drawer_app=com.example.deep-link">Deep
Link</a>

```

If a user clicks one of the deep links, it navigates them to your app that opens
in the Customers page of the Dashboard.

[Share the deep
link](https://docs.stripe.com/stripe-apps/deep-links#share-deep-link)
Make sure you use the live mode URL when you share the deep link to your users.
You can share the link anywhere for users who’ve installed your app. If the user
hasn’t installed your app before clicking the deep link, Stripe navigates them
to a closed app that can’t open in the Dashboard.

[Test the deep
link](https://docs.stripe.com/stripe-apps/deep-links#test-deep-link)- Log in to
the Dashboard as a user who has installed the app.
- Click the deep link.

If it navigates you to an app that can’t open, make sure you set the
`open_drawer_app` parameter to the correct application ID.

## See also

- [App manifest
reference](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [Versions and
releases](https://docs.stripe.com/stripe-apps/versions-and-releases)

## Links

- [creating OAuth authorization
workflows](https://docs.stripe.com/stripe-apps/pkce-oauth-flow)
- [UI functionality](https://docs.stripe.com/stripe-apps/build-ui)
- [id field of your stripe-app.json manifest
file](https://docs.stripe.com/stripe-apps/reference/app-manifest#schema)
- [test mode](https://docs.stripe.com/test-mode)
- [App manifest
reference](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [Versions and
releases](https://docs.stripe.com/stripe-apps/versions-and-releases)