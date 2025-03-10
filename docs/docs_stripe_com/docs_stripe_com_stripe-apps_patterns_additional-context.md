# Additional context for Stripe Apps

## Learn about how additional contexts in onboarding can help users better understand your app.

If you need to share any additional context before users sign in, dedicate a
space for it on a separate screen.

## Before you begin

[Create an app](https://docs.stripe.com/stripe-apps/create-app).

## Suggested use

- Use a [FocusView](https://docs.stripe.com/stripe-apps/components/focusview)
component to provide additional context, or to show a
[demo](https://docs.stripe.com/stripe-apps/patterns/demo) screen of how your app
works.
- Make sure the sign in screen is focused on onboarding tasks. Any additional
context should be brief and contextualized. For example:

!

## Example

The following sample shows additional content displayed within a `SignInView`
component:

```
import {SignInView, Img, Link} from '@stripe/ui-extension-sdk/ui';
import appIcon from './icon.svg';

const Onboarding = () => (
 <SignInView
 description="Connect your SuperTodo account with Stripe."
 primaryAction={{label: 'Sign in', href: 'https://example.com'}}
 footerContent={
 <>
 Don't have an account? <Link href="https://example.com">Sign up</Link>
 </>
 }
 descriptionActionLabel="Learn more"
 descriptionActionTitle="Learn more"
 descriptionActionContents={
 <>
 <Img href="https://example.com/screenshot.png" />
To import existing data from SuperTodo, you will need to connect your SuperTodo
account to Stripe.
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
- [demo](https://docs.stripe.com/stripe-apps/patterns/demo)