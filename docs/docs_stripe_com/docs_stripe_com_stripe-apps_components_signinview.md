# SignInView component for Stripe Apps

## SignInView allows apps to render a sign in screen.

SDK version8.x9.x
Use the `SignInView` component to display a graphic with your app’s icon next to
Stripe’s, a short description of your sign in process, action buttons, and so
on. If your app requires users to sign in, the `SignInView` component is
required to make sure users clearly understand that they’re connecting to
Stripe.

!

A SignInView example displayed in the drawer.

!

SignInView used on the [settings
page](https://docs.stripe.com/stripe-apps/app-settings).

### SignInView props

PropertyType
`brandColor`

Optional
`string | undefined`

A CSS color that contrasts well with `brandIcon`.

`brandIcon`

Optional
`string | undefined`

A square, 1-color SVG that contrasts well with `brandColor`.

`description`

Optional
`string | undefined`

A paragraph description of the app and its features.

`descriptionActionContents`

Optional
`React.ReactNode`

Description action contents that open in a `FocusView`.

`descriptionActionLabel`

Optional
`string | undefined`

An action label (“Learn more” or “View demo”, for example) below the
description.

`descriptionActionTitle`

Optional
`string | undefined`

The title in the `FocusView` for the description action.

`footerContent`

Optional
`React.ReactNode`

React node below the primary action in the footer.

`primaryAction`

Optional
`(SignInActionWithHref | SignInActionWithOnPress) | undefined`

Related types:
[SignInActionWithHref](https://docs.stripe.com/stripe-apps/components/signinview#signinactionwithhref),
[SignInActionWithOnPress](https://docs.stripe.com/stripe-apps/components/signinview#signinactionwithonpress).

`secondaryAction`

Optional
`(SignInActionWithHref | SignInActionWithOnPress) | undefined`

Related types:
[SignInActionWithHref](https://docs.stripe.com/stripe-apps/components/signinview#signinactionwithhref),
[SignInActionWithOnPress](https://docs.stripe.com/stripe-apps/components/signinview#signinactionwithonpress).

### SignInActionWithHref

PropertyType
`href`

Required
`string`

`label`

Required
`string`

`onPress`

Optional
`(() => void) | undefined`

`target`

Optional
`string | undefined`

### SignInActionWithOnPress

PropertyType
`label`

Required
`string`

`onPress`

Required
`() => void`

`href`

Optional
`string | undefined`

`target`

Optional
`string | undefined`

## Example

```
import {Link, SignInView} from '@stripe/ui-extension-sdk/ui';
import appIcon from './icon.svg';

const Onboarding = (
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

## Additional context

Before a user signs in, you might want to display a demo, a detailed description
of your app, or screenshots. Remember that at this point the user has already
installed your app so they should be motivated to sign in, but if you want to
show additional context, you can do it in a focused view using the
`descriptionActionLabel`, `descriptionActionTitle`, and
`descriptionActionContents` properties. For example:

!

```
import {Img, Link, SignInView} from '@stripe/ui-extension-sdk/ui';
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
 brandColor="#635bff"
 brandIcon={appIcon}
 descriptionActionLabel="Learn more"
 descriptionActionTitle="Learn more"
 descriptionActionContents={
 <>
 <Img src="https://example.com/screenshot.png" />
 To import existing data from SuperTodo, you will need to connect your
 SuperTodo account to Stripe.
 </>
 }
 />
);
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [settings page](https://docs.stripe.com/stripe-apps/app-settings)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)