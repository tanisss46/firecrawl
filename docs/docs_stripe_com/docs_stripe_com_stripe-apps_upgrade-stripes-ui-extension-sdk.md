# Upgrade Stripe's UI extension SDK

## Upgrade your app to the latest version of @stripe/ui-extension-sdk.

This page provides a comprehensive guide to help you navigate the breaking
changes introduced in each major version of the
[@stripe/ui-extension-sdk](https://www.npmjs.com/package/@stripe/ui-extension-sdk)
and outlines the necessary changes to upgrade your application.

We recommend upgrading the Stripe Apps CLI plugin by running `stripe plugin
upgrade apps` before updating the @stripe/ui-extension-sdk version. This ensures
optimal compatibility, incorporation of the latest features, and security fixes.

## @stripe/ui-extension-sdk v9

### What’s new in v9

Version 9 of `@stripe/ui-extension-sdk` introduces property validation for all
of its components. This version is more secure, mitigates bugs, and promotes
adherence to coding best practices. After you install it, pay attention to
TypeScript errors arising from invalid property values, as they could throw
validation errors causing the application to crash.

### Component changes

We made visual updates to several components. After you install the latest
version, review your app to make sure that the components appear as they should.

ComponentBreaking changesButton- `className` prop has been removed
DateField- `onChange` prop now directly receives the value instead of the change
event.
FormFieldGroup- `layout` prop values has changed from `row` and `column` to
`horizontal` and `vertical`
- `invalid` prop has been removed
Link- `className` prop has been removed
Tab- `tabKey` prop has been replaced by `id`
TabPanel- `tabKey` prop has been replaced by `id`
TextArea- `onKeyPress` prop has been removed
TextField- `onChange` callback signature has changed

## Changelog

### 9.0.0

- Add `PlatformConfigurationView` component to enable setup for embedded apps.
- Add runtime component prop validation to enforce type safe properties.
- Add `pending` prop to `Button` component.
- Add `new` variant value to `type` prop in `Badge` component.
- Add more format options to `BarChart` and `LineChart` components:- Add format
style `decimal`.
- Add `nice` option to have more pleasing axis limits.
- Add `ticks` to specify the number of markets along an axis.
- Add `tickFormat` to modify the display of the tick labels.
- Add `zero` to control the visibility of the zero value.
- Add `fractionalDigits` option to currency formats to control the precision of
numeric values.
- Remove deprecated `tabKey` prop from `Tab` and `TabPanel` components. Use the
`id` prop instead.
- Remove deprecated `background` property on `Box` and `Inline` components’
`css` prop. Use the `backgroundColor` property instead.
- Remove deprecated `className` prop from `Button` and `Link` components.
- Remove deprecated `invalid` prop from `FormFieldGroup` component.
- Remove deprecated `layout` property on `Box` and `Inline` components’ `css`
prop. Use the `stack` property instead.
- Remove deprecated `onClose` prop from `FocusView` component. Use the
`setShown` prop instead.
- Remove deprecated `onKeyPress` prop from `TextArea` and `TextField`
components.
- The `onChange` prop in the `DateField` component now directly receives the
value instead of the change event.
- The `layout` prop values in the `FormFieldGroup` component have changed from
`row` and `column` to `horizontal` and `vertical`.

### 8.9.2

- Fix `minTileWidth` prop types to accept only compatible values.
- Remove `React.RefObject` type from the `Tooltip` component’s `trigger` prop,
as it is not supported at runtime.
- Add `id` prop to `Tab` and `TabPanel` components to replace `tabKey`.
- Remove deprecation notice from border color properties (`borderColor`,
`borderBottomColor`, `borderLeftColor`, `borderRightColor`, `borderTopColor`) in
the `css` prop of `Box` and `Inline` components.
- Add border style and width properties (`borderStyle`, `borderWidth`,
`borderBottomStyle`, `borderBottomWidth`, `borderLeftStyle`, `borderLeftWidth`,
`borderRightStyle`, `borderRightWidth`, `borderTopStyle`, `borderTopWidth`) to
the `css` prop of `Box` and `Inline` components.
- Add literal types to the `name` prop on the `Icon` component.

### 8.9.1

- Use fixed dependency versions.
- Fix test wrapper find methods.

### 8.9.0

- Add `value` prop to `DateField` component.
- Add deprecation notice to the `background` property on `Box` and `Inline`
components’ `css` prop. Use the `backgroundColor` property instead.
- Add deprecation notice to the `className` prop on `Button` and `Link`
components.
- Add deprecation notice to the `invalid` prop on `FormFieldGroup` component.
- Add deprecation notice to the `layout` property on `Box` and `Inline`
components’ `css` prop. Use the `stack` property instead.
- Add deprecation notice to the `tabKey` prop on `Tab` and `TabPanel`
components.
- Add deprecation notice to the border color properties (`borderColor`,
`borderTopColor`, `borderRightColor`, `borderBottomColor`, `borderLeftColor`) on
`Box` and `Inline` components’ `css` prop. Use the `keyline` property for border
styling instead.
- Remove deprecation notice from `value` and `checked` props.

### 8.8.0

- Add `StripeFileUploader` component.
- Add `platform` prop to environment context.
- Add `appContext` to the `ExtensionContextValue` type.
- Add types for `AuthorizedPermission` and `AuthorizedContentSecurityPolicy`.
- Add some utility functions for interacting with `appContext`:-
`getUserAuthorizedPermissions`: Gets the intersection of the app’s authorized
permissions and those of the current Dashboard user.
- `isPermissionAuthorized`: Indicates if a permission is in the app’s authorized
permissions.
- `isSourceInAuthorizedCSP`: Indicates if a URL is in the app’s authorized
connect or image sources.

### 8.7.0

- Add `roles` to the account passed to extensions in the `userContext` property.

### 8.6.0

- Add `secondaryAction` prop to `SignInView`.
- Add `target` to `SignInView` action props.
- Allow both `href` and `onPress` on `SignInView` action props.

### 8.5.0

- Add `constants` prop to environment context.

### 8.4.1

- Add `SignInView` component.

### 8.3.0

- Remove unsupported `contentUses` property from `TableCell` and
`TableHeaderCell` typing.
- Updated `useToast` to return `show` and `dismiss` utility methods.

### 8.2.0

- `StripeAppsHttpResponse.prototype.toJSON()` now returns a rejected promise if
the HTTP response body was empty.
- Add support for calling `fetchStripeSignature` with nested JSON.
- Fix `debug` to filter props according to `all` option.
- Add `tabKey` to `Tab` and `TabPanel`.
- Upgrade `stripe` package dependency to `^9.11.0`.
- Add `external` to `Link`.
- Add `setShown` prop to `FocusView`.
- Add `showToast` utility function for rendering toast notifications at the
bottom of an app’s view.

### 8.1.0

- Fix `ExtensionContextValue` typing to mark `name` and `objectContext` values
as possibly `null`.
- Add `textAlign` to `Box` `css`.
- Make `onSave` prop optional for `SettingsView` components.
- Upgrade to `@remote-ui/react` 4.5.2.
- Add `Sparkline` component.

### 8.0.0

- Add deprecation notice to the `value` prop on `TextArea`, `TextField`, and
`Select` components.
- Add deprecation notice to the `checked` prop on `Checkbox`, `Radio`, and
`Switch` components.
- Remove unsupported `outerRef` props from inputs.

### 7.1.0

- Add `brandIcon` and `brandColor` to `ContextView`.

### 7.0.0

- Deprecate `Notice` component; use `Banner` instead.
- Add `overflowX` and `overflowY` to `Box` `css`.

### 6.3.1

- Internal update, no user-facing changes.

### 6.3.0

- Add `Banner` component.
- Add deprecation warning for `Notice` component.
- Add `locale` to `ExtensionContextValue['oauthContext']`.
- Add `overflowWrap` and `wordBreak` to `Box` `css` properties.
- Add `textTransform` to `Box` and `Inline` `css` properties.
- Add `primaryAction`, `secondaryAction`, and `footerContent` properties to
`ContextView`.
- Add `whiteSpace` to `Box` `css` properties.

### 6.2.0

- `BarChart` and `LineChart` improvements:- Configurable axis formatting.
- Configurable value formatting.
- Configurable channel domains.
- Configurable channel ranges.
- Show/hide axis labels and ticks in charts.
- Show/hide grid lines in charts.
- Show/hide tooltips in chart presets.
- Show/hide legends in chart presets.

### 6.1.0

- Add a confirmation dialog to `FocusView`.
- Add `Chip` and `ChipList` components.
- Update the `getDashboardUserEmail` utility to return the email directly and
reject the promise if there’s an error.
- Fix React components not being accepted in the `label` prop of form elements.
- Expose `text-overflow: ellipsis` and `word-wrap: normal | break-word` on `Box`
`css`.
- Add `country` to the account passed to extensions in the `userContext`
property.
- Add `data:` URL support for the `Img` component. Learn more about [the Img
component](https://docs.stripe.com/stripe-apps/components/img?app-sdk-version=8#data-urls).

### 6.0.0

- Deprecate email in view context.
- Consolidated utilities in `/utils` path.
- Fixed react-reconciler dependency issue affecting unit tests.

### 5.0.1

- Fix prop types for `Switch`, `Checkbox` and `Radio`.

### 5.0.0

- Adds the `Accordion`, `Icon`, `Spinner`, and `Tooltip` components.
- Adds tooltips to `BarChart` and `LineChart`.
- Fix prop typing for `BarChart` and `LineChart`.
- Deprecates legacy view context parameters.
- Enables setting width through `css={{ width: .. }}` on `Select`, `TextArea`,
`TextField`, `Button`, and `Link`.
- Enables setting internal horizontal alignment through `css={{ alignX: .. }}`
on `Button` and `Link`.
- Adds the `clipboardWriteText` function.
- Adds the `getDashboardUserEmail` function.

### 4.0.0

- Deprecates the `slot` property.

### 3.2.0

- Adds the `createOAuthState` function.
- Adds `oauthContext` to the `ExtensionContextValue` type.

### 3.1.0

- Adds the `Img` component.

### 3.0.0

- Adds support for the `Notice`, `Charts`, and `Tabs` components.
- Breaking changes:- `ListItem`: Previously, content passed as children would be
the primary content rendered in the component. Now, main content is passed to
the `title` prop. The `description` slot has also been reassigned to a
`secondaryTitle` prop.
- `MenuTrigger`: This component has been deprecated in favor of a `trigger` prop
on the `Menu` component. Slot API usage has also been removed.
- Removed permissions from being passed into the user context.

### 2.2.1

- Expose `docs.json` files in `dist`.

### 2.2.0

- Add `actions` prop to `ContextView`.

### 2.1.0

- Introduces `ButtonGroup` component.
- Removes `margin-bottom` from form controls.
- Gives Button `white-space: nowrap` and `alignY: center` by default.
- Button themes now set a `min-height` on all size variants.
- Makes `Link` and `Button` shrink to fit their content.
- Exposes `defaultValue` attribute on `TextField` and `TextArea`.
- Allows `error` and `description` to be hidden on form controls through the
`hiddenElements` prop.
- Exposes `invalid` and `size` props on `Select` and `TextArea`.
- Exposes `defaultChecked` attribute on `Radio`.
- Exposes `resizeable` and `rows` props on `TextArea`.
- Fixes invalid state on control components.
- Fixes `Chip` `onDropdown` firing twice.
- Fixes `Divider` rendering.

### 2.0.3

- Returns a promise from `useRefreshDashboardData` that resolves after dashboard
data is refreshed.
- Adds `fetchStripeSignature` method that optionally accepts additional request
payload. Signature can be used to make authenticated request to your app’s
backend.
- Fixes an issue where the test element check method `.is` would sometimes fail
to identify a component.

### 2.0.2

- Fixes an issue with the `testing` package in which comopnents with fragment
props were not findable using `wrapper.find()`.

### 2.0.1

- Pulls in updated dependency that fixes
[#55](https://github.com/stripe/stripe-apps/issues/55) and
[#161](https://github.com/stripe/stripe-apps/issues/161).

### 2.0.0

- Fixes a render error with `SettingsView`.
- Updates `SettingsView` types to match the available component props.
- Adds a `getMockContextProps` helper for testing. Learn more about [context
props](https://docs.stripe.com/stripe-apps/ui-testing#mock-context-props).
- List component now accepts `React.ReactNode` as a valid type to the `value`
prop, rather than just a `string`.
- Adds hover state to ListItem components.
- Updates ListItem component such that hover state is only visible when there is
an action associated.
- Fix Select rendering when multiple is true.
- Fix Checkbox onChange firing twice.

### 1.1.7

- Adds a “testing” module, which includes helpers for writing Jest tests for
apps. Learn more about [UI
testing](https://docs.stripe.com/stripe-apps/ui-testing).
- Fixes some components that take React nodes as props:- `MenuGroup` now
supports the `title` prop.
- `FocusView` now supports the `footerContent` prop.
- `SettingsView` now supports the `headerActions` prop.
- Some type fixes and grammar updates.

### 1.1.6

- Added types for `FocusView`, `SettingsView`, and `ContextView`.
- Exporting a new constant `STRIPE_API_KEY` from http_client to be used when
initializing the Stripe API client.

## Links

-
[@stripe/ui-extension-sdk](https://www.npmjs.com/package/@stripe/ui-extension-sdk)
- [the Img
component](https://docs.stripe.com/stripe-apps/components/img?app-sdk-version=8#data-urls)
- [#55](https://github.com/stripe/stripe-apps/issues/55)
- [#161](https://github.com/stripe/stripe-apps/issues/161)
- [context
props](https://docs.stripe.com/stripe-apps/ui-testing#mock-context-props)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)