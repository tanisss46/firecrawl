# Switch component for Stripe Apps

## Similar to Checkboxes, you can use Switches to indicate or control boolean values.

SDK version8.x9.x
To add the `Switch` component to your app:

```
import {Switch} from '@stripe/ui-extension-sdk/ui';
```

A common use of Switches is for settings that you save immediately—in other
words, `Switch` is rarely part of a larger form that needs to be submitted
separately.

Here’s a simple example of a `Switch`.

Loading example...
```
<Switch
 label="This is a Switch."
 onChange={(e) => {
 console.log(e.target.checked);
 }}
/>
```

### Switch props

PropertyType
`autoFocus`

Optional
`boolean | undefined`

If `true`, React will focus the element on mount.

`checked`

Optional
`boolean | undefined`

Controls whether the input is selected. When you pass this prop, you must also
pass an `onChange` handler that updates the passed value.

`defaultChecked`

Optional
`boolean | undefined`

Specifies the initial value that a user can change.

`description`

Optional
`string | undefined`

Descriptive text that will be rendered adjacent to the control’s label.

`disabled`

Optional
`boolean | undefined`

Sets whether or not the element should be disabled. Prevents selection.

`error`

Optional
`string | undefined`

Error text that will be rendered below the control.

`form`

Optional
`string | undefined`

Specifies the `id` of the `<form>` this input belongs to. If omitted, it’s the
closest parent form.

`hiddenElements`

Optional
`("label" | "description" | "error")[] | undefined`

Visually hides the specified elements. The hidden elements will still be present
and visible to screen readers.

`invalid`

Optional
`boolean | undefined`

Sets whether or not the element is in an invalid state. This is a display-only
prop, and will not prevent form submission.

`label`

Optional
`React.ReactNode`

Text that describes the control. Will be both visible and clickable.

`name`

Optional
`string | undefined`

Specifies the name for this input that’s submitted with the form.

`onChange`

Optional
`((event: React.ChangeEvent<HTMLInputElement>) => void) | undefined`

Required for controlled inputs. Fires immediately when the input’s value is
changed by the user (for example, it fires on every keystroke). Behaves like the
browser input event.

`readOnly`

Optional
`boolean | undefined`

If `true`, the input is not editable by the user.

`required`

Optional
`boolean | undefined`

If `true`, the value must be provided for the form to submit.

`tabIndex`

Optional
`number | undefined`

Overrides the default tab key behavior. Avoid using values other than `-1` and
`0`.

`value`

Optional
`string | undefined`

Controls the input’s text. When you pass this prop, you must also pass an
`onChange` handler that updates the passed value.

## State management

Use the `Switch` component as an [uncontrolled
input](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions):

Loading example...
```
<Switch
 onChange={(e) => {
 console.log(e.target.checked);
 }}
 defaultChecked
 label="This Switch is uncontrolled."
/>
```

## Disabled

You can disable a `Switch` component, which prevents changes.

Loading example...
```
<Switch label="This Switch is disabled." defaultChecked disabled />
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [uncontrolled
input](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)