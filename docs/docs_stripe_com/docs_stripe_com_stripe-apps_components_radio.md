# Radio component for Stripe Apps

## Use Radios to make a selection from a mutually exclusive set of options.

SDK version8.x9.x
To add the `Radio` component to your app:

```
import {Radio} from '@stripe/ui-extension-sdk/ui';
```

Loading example...
```
<Radio label="This is a Radio." />
```

### Radio props

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

Used to collect multiple `Radios` into a single, mutually exclusive group, for
uncontrolled use cases.

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

## Disabled

You can disable a `Radio` component, which prevents changes.

Loading example...
```
<Radio name="group" label="Ah ah ah" disabled />
<Radio
 name="group"
 disabled
 defaultChecked
 label="You didn't say the magic word"
/>
```

## Invalid

`Radio` can be invalid.

Loading example...
```
<Radio label="This is an invalid input" invalid />
```

## State management

Use the `Radio` component as an [uncontrolled
input](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions):

Loading example...
```
<Radio
 name="group"
 label="Have some of Column A"
 onChange={(e) => {
 console.log(e.target.checked);
 }}
/>
<Radio
 name="group"
 label="Try all of Column B"
 onChange={(e) => {
 console.log(e.target.checked);
 }}
/>
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