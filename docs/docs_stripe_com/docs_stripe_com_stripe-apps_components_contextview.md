# ContextView component for Stripe AppsDashboard only

## ContextView allows apps to render next to Stripe content in a drawer so users can look at them side by side and share context.

SDK version8.x9.x
The root view of your app must be a `ContextView`.

These in-context modules allow the app to meet users in their existing workflows
and provide contextual information and actions.

A user’s interaction with an app always begins with a view type called a
`ContextView` view. Each app must have a single `ContextView` view (per
[viewport](https://docs.stripe.com/stripe-apps/reference/viewports)), which acts
as the default view when the page loads (similar to the `index.html` of a
website).

![ContextView in an
application](https://b.stripecdn.com/docs-statics-srv/assets/contextview-2.b7a229ed709708c7e83e700396b82327.png)

What ContextView looks like

#### Note

To create a view within an existing `ContextView`, see
[FocusView](https://docs.stripe.com/stripe-apps/components/focusview).

### ContextView props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`title`

Required
`string`

The title of the `ContextView`. This will be displayed at the top of the drawer
under that app’s name.

`actions`

Optional
`React.ReactNode`

A React fragment containing up to three `Buttons` that will be displayed
directly under the header and above the children of the `ContextView`.

`banner`

Optional
`React.ReactElement | undefined`

A `Banner` component that will be displayed directly under the header and above
the children of the `ContextView`.

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

A description of the view’s purpose, can also be used as a subtitle.

`externalLink`

Optional
`ExternalLink | undefined`

A link to an external webpage. This should generally allow the user to view
related information on another site with more context than what the app makes
available in the app drawer.

Related types:
[ExternalLink](https://docs.stripe.com/stripe-apps/components/contextview#externallink).

`footerContent`

Optional
`React.ReactNode`

React node adjacent to any actions in the footer.

`primaryAction`

Optional
`React.ReactElement | undefined`

A primary call to action (“Save” or “Continue”) `Button` placed in the footer.

`secondaryAction`

Optional
`React.ReactElement | undefined`

A secondary call to action (“Cancel”) `Button` placed in the footer.

### ExternalLink

PropertyType
`href`

Required
`string`

URL of an external link.

`label`

Required
`string`

Label of an external link.

## Example

```
import {
 Box,
 Button,
 ContextView,
} from '@stripe/ui-extension-sdk/ui';

import appIcon from './icon.svg';

const HappyView = () => (
 <ContextView
 title="Get started with Stripe Apps"
 actions={
 <>
 <Button>Action 1</Button>
 <Button>Action 2</Button>
 </>
 }
 brandColor="#635bff"
 brandIcon={appIcon}
 >
 <Box>Example Content</Box>
 </ContextView>
);
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [viewport](https://docs.stripe.com/stripe-apps/reference/viewports)
- [FocusView](https://docs.stripe.com/stripe-apps/components/focusview)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)