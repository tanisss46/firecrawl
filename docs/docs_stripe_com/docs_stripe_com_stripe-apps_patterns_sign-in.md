# Sign in template for Stripe Apps

## Learn how to use the SignInView component with your app.

If your app requires users to sign in, the `SignInView` component is required to
ensure users clearly understand that they’re connecting to Stripe.

## Before you begin

[Create an app](https://docs.stripe.com/stripe-apps/create-app).

## Suggested use

- To avoid compromising users’ passwords, never ask users to share their full
set of credentials with Stripe.
- Keep content lightweight and focused. Avoid any links that might take users
away from the onboarding flow. For example:

!

!

- Provide users the option to sign into an existing account or sign up for a new
account.
- Use call-to-action labels that are consistent with your own onboarding flow
outside of Stripe. For example:

!

## Example

To add the component to your app:

```
import {SignInView} from '@stripe/ui-extension-sdk/ui';
```

The following sample shows a `SignInView` component:

```
<SignInView
 description="Connect your SuperTodo account with Stripe."
 primaryAction={{label: 'Sign in', href: 'https://example.com'}}
 footerContent={
 <>
 Don't have an account? <Link href="https://example.com">Sign up</Link>
 </>
 }
 brandColor="#635bff"
 brandIcon={appIcon}
/>
```

## Links

- [Create an app](https://docs.stripe.com/stripe-apps/create-app)