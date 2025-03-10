# Select component for Stripe Apps

## Use Select to pick from a set of options in a dropdown.

SDK version8.x9.x
To add the `Select` component to your app:

```
import {Select} from '@stripe/ui-extension-sdk/ui';
```

Loading example...
```
<Select
 name="demo-001"
 label="Choose a pet"
 onChange={(e) => {
 console.log(e);
 }}
>
 <option value="">Choose an option</option>
 <option value="dogs">Dogs</option>
 <option value="cats">Cats</option>
</Select>
```

### Select props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`autoComplete`

Optional
`string | undefined`

Specifies one of the possible autocomplete behaviors.

`autoFocus`

Optional
`boolean | undefined`

If `true`, React will focus the element on mount.

`css`

Optional
`Object`

Related types: [CSS](https://docs.stripe.com/stripe-apps/components/select#css).

`defaultValue`

Optional
`(string | string[]) | undefined`

A string (or an array of strings for `multiple={true}`). Specifies the initially
selected option that a user can change.

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

`multiple`

Optional
`boolean | undefined`

If `true`, the browser allows multiple selection.

`name`

Optional
`string | undefined`

Specifies the name for this input that’s submitted with the form.

`onChange`

Optional
`((event: React.ChangeEvent<HTMLSelectElement>) => void) | undefined`

Required for controlled inputs. Fires immediately when the input’s value is
changed by the user (for example, it fires on every keystroke). Behaves like the
browser input event.

`required`

Optional
`boolean | undefined`

If `true`, the value must be provided for the form to submit.

`size`

Optional
`("small" | "medium" | "large") | undefined`

The size of the component.

`value`

Optional
`(string | string[]) | undefined`

A string (or an array of strings for `multiple={true}`). Controls which option
is selected.

### CSS

PropertyType
`width`

Optional
`(number | "auto" | "fill" | "min" | "max" | "fit" | "1/2" | "1/3" | "2/3" |
"1/4" | "2/4" | "3/4" | "1/5" | "2/5" | "3/5" | "4/5" | "1/6" | "2/6" | "3/6" |
"4/6" | "5/6" | "1/12" | "2/12" | "3/12" | "4/12" | "5/12" | "6/12" | "7/12" |
"8/12" | "9/12" | "10/12" | "11/12") | undefined`

The width of the component. See
[Sizing](https://docs.stripe.com/stripe-apps/style#sizing) for details.

## State management

Use the `Select` component as an [uncontrolled
input](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions):

Loading example...
```
<Select
 name="demo-001"
 label="Choose a pet"
 onChange={(e) => {
 console.log(e);
 }}
>
 <option value="">Choose an option</option>
 <option value="dogs">Dogs</option>
 <option value="cats">Cats</option>
</Select>
```

## Disabled

You can disable a `Select` component, which prevents changes.

Loading example...
```
<Select name="demo-001" disabled label="Choose a pet">
 <option value="">Choose an option</option>
 <option value="dogs">Dogs</option>
 <option value="cats">Cats</option>
</Select>
```

## Width

Set the width of a `Select` component using [the available
values](https://docs.stripe.com/stripe-apps/style#sizing) with the `css` prop:

Loading example...
```
<Select
 css={{
 width: 'fill',
 }}
 name="demo-001"
 label="Choose a pet"
 onChange={(e) => {
 console.log(e);
 }}
>
 <option value="">Choose an option</option>
 <option value="dogs">Dogs</option>
 <option value="cats">Cats</option>
</Select>
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [Sizing](https://docs.stripe.com/stripe-apps/style#sizing)
- [uncontrolled
input](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)