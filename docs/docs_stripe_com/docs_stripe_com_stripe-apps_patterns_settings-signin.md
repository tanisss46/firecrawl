# Settings sign in for Stripe Apps

## Learn how to onboard users on a settings page.

If you’re building a connect extension or a back-end only app, onboard users
with a settings page.

## Before you begin

[Create an app](https://docs.stripe.com/stripe-apps/create-app).

## Suggested use

- Use a settings page to sign in users.
- Apply this design pattern the same way you would in a drawer. Avoid additional
context that isn’t helpful when onboarding users. For example:

!

- When you need to add additional context to users, use a
[FocusView](https://docs.stripe.com/stripe-apps/components/focusview) component
to provide the information. For example:

!

## Example

To add the `SignInView` component to your settings view, display it
conditionally with the `SettingsView` component based on the user’s sign in
state:

```
import {SignInView, SettingsView} from '@stripe/ui-extension-sdk/ui';
import appIcon from './icon.svg';

const AppSettings = () => {
 // Set this variable based on your app's concept of sign in state
 const isUserSignedIn = ...;
 return isUserSignedIn ? (
 <SettingsView>
 {/* Add your settings view content. */}
 </SettingsView>
 ) : (
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
 );
```

## Links

- [Create an app](https://docs.stripe.com/stripe-apps/create-app)
- [FocusView](https://docs.stripe.com/stripe-apps/components/focusview)