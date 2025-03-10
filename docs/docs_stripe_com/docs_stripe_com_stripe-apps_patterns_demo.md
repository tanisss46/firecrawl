# Demo content for Stripe Apps

## Learn tips for displaying a demo of your app.

When building a demo of your app, keep the content brief and only highlight the
top functionality that your app offers.

## Before you begin

[Create an app](https://docs.stripe.com/stripe-apps/create-app).

## Suggested use

- Add a dedicated page view that doesn’t interfere with the onboarding flow.
- Provide “just enough” information to communicate the main functionality of
your app. For example:

!

## Example

The following sample shows demo content displayed within a `SignInView`
component:

```
import {SignInView, Banner, Button} from '@stripe/ui-extension-sdk/ui';
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
 descriptionActionLabel="View demo"
 descriptionActionTitle="Todo lists"
 descriptionActionContents={
 <>
 <Box css={{marginBottom: 'small'}}>
 <Button type="primary" css={{width: 'fill', alignX: 'center'}}>
 Create list
 </Button>
 </Box>
 <Banner
 type="caution"
 title="You're viewing demo content"
 description="Your data will be visible once you sign in."
 />
 ...continued app demo content.
 </>
 }
 brandColor="#635bff"
 brandIcon={appIcon}
 />
);
```

## Links

- [Create an app](https://docs.stripe.com/stripe-apps/create-app)