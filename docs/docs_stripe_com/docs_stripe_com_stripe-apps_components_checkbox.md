# Checkbox component for Stripe Apps

## Use checkboxes to indicate or control boolean values.

SDK version8.x9.x
To add the `Checkbox` component to your app:

```
import {Checkbox} from '@stripe/ui-extension-sdk/ui';
```

Loading example...
```
<Checkbox
 label="This is a Checkbox."
 onChange={(e) => {
 console.log(e.target.checked);
 }}
/>
```

`Checkbox` takes the following props, in addition to all the appropriate [native
DOM
attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox).

### Checkbox props

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

`indeterminate`

Optional
`boolean | undefined`

Sets whether the `Checkbox` should be rendered as indeterminate (“partially
checked”) or not. Note that this is purely visual, and will not change the
actual `checked` state of the `Checkbox`. If a `Checkbox` is both
`indeterminate` and `checked`, it will display as `indeterminate`.

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

You can set a `Checkbox` component to different states:

- `indeterminate`
- `disabled`
- `invalid`

## Indeterminate

The `Checkbox` component can be in an `indeterminate` state. This is useful when
it represents the aggregated state of some other set of checkboxes, of which
some may be checked and some may not. Note that this property is purely visual,
and does not affect the Checkbox’s underlying checked state.

Loading example...
```
const [checked1, setChecked1] = React.useState(false);
const [checked2, setChecked2] = React.useState(true);

const allChecked = checked1 && checked2;

const handleAggregateChange = () => {
 if (checked1 && checked2) {
 setChecked1(false);
 setChecked2(false);
 } else {
 setChecked1(true);
 setChecked2(true);
 }
};

return (
 <Box
 css={{
 stack: 'y',
 }}
 >
 <Checkbox
 label="This Checkbox is aggregating the state of the Checkboxes below it."
 checked={allChecked}
 indeterminate={checked1 !== checked2}
 onChange={handleAggregateChange}
 />
 <Checkbox
 label="Checkbox 1"
 checked={checked1}
 onChange={(e) => {
 setChecked1(e.target.checked);
 }}
 />
 <Checkbox
 label="Checkbox 2"
 checked={checked2}
 onChange={(e) => {
 setChecked2(e.target.checked);
 }}
 />
 </Box>
)
```

## Disabled

`Checkbox` can be `disabled`. This prevents changes.

Loading example...
```
<Checkbox label="This Checkbox is disabled." defaultChecked disabled />
<Checkbox disabled invalid label="This invalid Checkbox is disabled." />
```

## Invalid

You can mark a `Checkbox` component as `invalid`. This is a styling-only prop,
useful in form validation. It won’t prevent form submission.

Loading example...
```
<Checkbox label="This Checkbox is in an invalid state." invalid />
```

## State management

Use the `Checkbox` component as an [uncontrolled
input](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions):

Loading example...
```
<Checkbox
 onChange={(e) => {
 console.log(e.target.checked);
 }}
 defaultChecked
 label="This Checkbox is uncontrolled."
/>
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [native DOM
attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox)
- [uncontrolled
input](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)