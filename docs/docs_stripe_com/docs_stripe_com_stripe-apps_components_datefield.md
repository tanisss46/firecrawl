# DateField component for Stripe Apps

## Use the DateField component to collect date information from users.

SDK version8.x9.x
To add the `DateField` component to your app:

```
import {DateField} from '@stripe/ui-extension-sdk/ui';
```

The following shows a preview of a `DateField` component with a label and a
description:

Loading example...
```
<DateField label="Date of birth" description="Enter your birthday" />
```

### DateField props

PropertyType
`defaultValue`

Optional
`string | undefined`

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

`onChange`

Optional
`((event: { target: { value: string; }; }) => void) | undefined`

An onChange-alike event that fires only when the change results in a valid date.
Identical behavior to `<input type="date" />`.

`size`

Optional
`("small" | "medium" | "large") | undefined`

The size of the component.

`value`

Optional
`string | undefined`

Controls the input’s text. When you pass this prop, you must also pass an
`onChange` handler that updates the passed value.

## Size

A `DateField` at each size will match a `TextField` at that same size. However,
you can’t make a date input wider in the same way that you can `TextField`.

Loading example...
```
<DateField
 label="Date of birth (small)"
 description="Enter your birthday"
 size="small"
/>
<DateField
 label="Date of birth (medium)"
 description="Enter your birthday"
 size="medium"
/>
<DateField
 label="Date of birth (large)"
 description="Enter your birthday"
 size="large"
/>
```

## Error

You can provide an error message to indicate a problem with the date.

Loading example...
```
<DateField
 label="Date of birth"
 description="Enter your birthday"
 defaultValue="2099-02-31"
 invalid
 error="Invalid birthday"
/>
```

## Disabled

Disable a `DateField` if the user shouldn’t modify it.

Loading example...
```
<DateField
 label="Date of birth"
 description="Enter your birthday"
 defaultValue="2011-09-01"
 disabled
/>
```

## Hide elements

You can visually hide elements of the `DateField` component, such as the label
or description, while maintaining accessibility for screen readers.

Loading example...
```
<DateField
 label="Date of birth"
 description="Enter your birthday"
 defaultValue="2011-09-01"
 hiddenElements={['description', 'label']}
/>
```

## Events

The `onChange` prop works similarly to a native `<input type="date" />` HTML
element. It only returns a value when it’s a valid date. This means that the
`onChange` handler won’t be called on every keystroke, and a `DateField` can’t
be a [controlled
input](https://reactjs.org/docs/forms.html#controlled-components).

Loading example...
```
<DateField
 label="Date of birth"
 description="Enter your birthday"
 onChange={(e) => {
 console.log(e.target.value);
 }}
/>
```

Event props (beginning with `on`) besides `onChange` fire independently for each
of the three sections of the `DateField` component: year, month, and day.

Loading example...
```
<DateField
 label="Date of birth"
 description="Enter your birthday"
 onChange={(e) => {
 console.log('change', e);
 }}
/>
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [controlled input](https://reactjs.org/docs/forms.html#controlled-components)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)