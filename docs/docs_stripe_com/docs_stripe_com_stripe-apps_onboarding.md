# Onboarding

## Guide your users through your app's sign in and initial setup flows.

Onboarding is the process your users go through to get your app set up after
installation. It’s their first interaction with your app, and it needs to be
intuitive and polished, with minimal friction before they can start using your
app.

The required onboarding steps are different for every app, but we provide tools
and best practices to help you.

## Design patterns

View our [onboarding design
patterns](https://docs.stripe.com/stripe-apps/patterns#onboarding) for common
scenarios including activation, sign in, redirection, and so on.

## Display your onboarding view

When a user installs your app and goes to view it in the Dashboard, it’s
important that the onboarding flow is the first thing they encounter. Make sure
to:

- Create an onboarding component (using
[SignInView](https://docs.stripe.com/stripe-apps/components/signinview), if a
sign in flow is needed).
- In all of your [page-specific
views](https://docs.stripe.com/stripe-apps/reference/viewports#page-specific-availability),
check to see if the user has completed onboarding when the view first loads, and
display your onboarding component appropriately. For example:
```
import {SignInView, ContextView} from '@stripe/ui-extension-sdk/ui';
import appIcon from './icon.svg';

// This component can be defined in a separate file for reuse between views
const Onboarding = () => (
 <SignInView
 description="Connect your SuperTodo account to Stripe."
 primaryAction={{label: 'Sign in', href: 'https://supertodo.example.com'}}
 brandColor="#635bff"
 brandIcon={appIcon}
 />
);

const CustomerDetailView = () => {
 // The definition of "isSignedIn" is dependent upon your app's sign in method
 if (!isSignedIn) {
 return <Onboarding />
 }

 return (
 <ContextView title="SuperTodo customer view">
 // your signed-in content here
 </ContextView>
 );
};
```
- Do the same in your [Dashboard default
view](https://docs.stripe.com/stripe-apps/reference/viewports#dashboard-wide-availability).
If you don’t have a default view, create one so that wherever the user is in the
Dashboard, they’re presented with the right flow when they open your app. If you
don’t need a Default view for purposes other than onboarding, you can return
`null` from the view if the user has already completed onboarding and the
Dashboard displays the Stripe Dashboard default drawer that guides users to a
page-specific view. For example:
```
import {SignInView} from '@stripe/ui-extension-sdk/ui';
import appIcon from './icon.svg';

// This component can be defined in a separate file for reuse between views
const Onboarding = () => (
 <SignInView
 description="Connect your SuperTodo account to Stripe."
 primaryAction={{label: 'Sign in', href: 'https://supertodo.example.com'}}
 brandColor="#635bff"
 brandIcon={appIcon}
 />
);

const DashboardDefaultView = () => {
 // The definition of "isSignedIn" is dependent upon your app's sign in method
 if (!isSignedIn) {
 return <Onboarding />
 }

 return null;
};
```

## Rely on Stripe authentication for zero-touch user onboarding

If you’re building an app that stores data in an external backend but doesn’t
need its own concept of user accounts, you can rely on Stripe’s authentication
to offer zero-touch onboarding. Using this method, your app doesn’t require any
onboarding and is usable immediately after installation.

Start by setting up your backend to [authenticate requests from your app’s
UI](https://docs.stripe.com/stripe-apps/build-backend#authenticate-ui-to-backend).
With that in place, you can store information in your database with an added
column for the user ID or account ID provided by Stripe. Users are already
signed into the Stripe Dashboard when they use your app, so there’s no need for
additional authentication.

## See also

- [SignInView](https://docs.stripe.com/stripe-apps/components/signinview)
- [Add an app settings page](https://docs.stripe.com/stripe-apps/app-settings)

## Links

- [onboarding design
patterns](https://docs.stripe.com/stripe-apps/patterns#onboarding)
- [SignInView](https://docs.stripe.com/stripe-apps/components/signinview)
- [page-specific
views](https://docs.stripe.com/stripe-apps/reference/viewports#page-specific-availability)
- [Dashboard default
view](https://docs.stripe.com/stripe-apps/reference/viewports#dashboard-wide-availability)
- [authenticate requests from your app’s
UI](https://docs.stripe.com/stripe-apps/build-backend#authenticate-ui-to-backend)
- [Add an app settings page](https://docs.stripe.com/stripe-apps/app-settings)