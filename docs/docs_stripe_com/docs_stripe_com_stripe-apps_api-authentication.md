# API authentication methods

## Select the API authentication method that works best for your app's use case.

Your app can use one of three methods to authenticate requests to the Stripe API
on behalf of your users.

Method DescriptionUse cases [Platform
key](https://docs.stripe.com/stripe-apps/build-backend#using-stripe-apis)
DefaultYour account’s secret API key makes requests to the Stripe API on behalf
of your user’s account.- You want to manage fewer keys per install.
- Beta You want to distribute your app through Connect platforms.
[OAuth 2.0](https://docs.stripe.com/stripe-apps/api-authentication/oauth)Use
industry standard OAuth 2.0 to generate access tokens to interact with the
Stripe API. Initialize the Stripe SDK with the access token for the account
you’re operating on behalf of.- You already use OAuth to interact with other
systems.
- Users need to manage the integration from your software.
[Restricted API
key](https://docs.stripe.com/stripe-apps/api-authentication/rak)When a user
installs your app, Stripe generates a permissioned, restricted API key that
users need to copy and paste into your software to interact with Stripe.- Your
software can’t support platform or OAuth onboarding.
- Your users run your software on-premise.

## Configure

To configure the API authentication method, edit `stripe_api_access_type` in the
[app manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest). For
setup instructions, refer to the pages linked in the table above.

```
{
 "id": "com.example.app",
 "version": "0.0.1",
 "name": "Your Stripe App",
 "distribution_type": "public",
 "permissions": [],
 "stripe_api_access_type": "platform" | "oauth" | "restricted_api_key",
}
```

## See also

- [Set up OAuth
2.0](https://docs.stripe.com/stripe-apps/api-authentication/oauth)
- [Set up restricted access key
authentication](https://docs.stripe.com/stripe-apps/api-authentication/rak)

## Links

- [Platform
key](https://docs.stripe.com/stripe-apps/build-backend#using-stripe-apis)
- [OAuth 2.0](https://docs.stripe.com/stripe-apps/api-authentication/oauth)
- [Restricted API
key](https://docs.stripe.com/stripe-apps/api-authentication/rak)
- [app manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest)