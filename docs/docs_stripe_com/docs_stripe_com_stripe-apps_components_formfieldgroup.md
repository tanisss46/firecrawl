# FormFieldGroup component for Stripe Apps

## Group form fields with the FormFieldGroup component.

SDK version8.x9.x
To add the `FormFieldGroup` component to your app:

```
import {FormFieldGroup} from '@stripe/ui-extension-sdk/ui';
```

Loading example...
```
<FormFieldGroup legend="Full name" description="Enter your full name">
 <TextField
 label="First name"
 placeholder="First name"
 hiddenElements={['label']}
 />
 <TextField
 label="Last name"
 placeholder="Last name"
 hiddenElements={['label']}
 />
</FormFieldGroup>
```

### FormFieldGroup props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`description`

Optional
`string | undefined`

Descriptive text that will be rendered adjacent to the group’s legend.

`disabled`

Optional
`boolean | undefined`

Disables all fields in the group. Can be overriden on a per-field basis.

`layout`

Optional
`("row" | "column") | undefined`

The layout of the fields in the group.

`legend`

Optional
`string | undefined`

The text of the group’s legend. This will be associated as a label with all
fields inside the group.

`invalid`

OptionalDeprecated
`boolean | undefined`

Marks the group as invalid. Note that this is a visual-only property, and won’t
prevent submission.

## Layouts

A `FormFieldGroup` component can support different layouts:

- `row`
- `column`

This is a preview of a `FormFieldGroup` component with two text fields in a
`row` layout:

Loading example...
```
<FormFieldGroup legend="Full name" description="Enter your full name">
 <TextField
 label="First name"
 placeholder="First name"
 hiddenElements={['label']}
 />
 <TextField
 label="Last name"
 placeholder="Last name"
 hiddenElements={['label']}
 />
</FormFieldGroup>
```

This is a preview of a `FormFieldGroup` component with two text fields in a
`column` layout:

Loading example...
```
<FormFieldGroup legend="Spiffy settings" layout="column">
 <Switch
 label="Enable transmogrifier"
 description="Scientific progress goes 'boink'"
 />
 <Switch
 label="Set zorcher on 'shake and bake'"
 description="Note: blasters may be useless against slime"
 />
</FormFieldGroup>
```

## States

A state is a way to display the usability and validity of the form to the user.
A `FormFieldGroup` component can have different types of states:

- `invalid`
- `disabled`

### Invalid state

You can mark a `FormFieldGroup` component as `invalid` to show a user that their
input values are incorrect. If the `FormFieldGroup` component is `invalid`, the
`invalid` state doesn’t also apply to dependent child controls. Consequently,
you must add errors to these child components manually by adding an `invalid`
property to them.

Loading example...
```
<FormFieldGroup
 legend="Full name"
 description="Enter your full name"
 invalid
>
 <TextField
 label="First name"
 value="Tim"
 placeholder="First name"
 hiddenElements={['label']}
 />
 <TextField
 label="Last name"
 error="Last name missing"
 placeholder="Last name"
 hiddenElements={['label']}
 />
</FormFieldGroup>
```

### Disabled state

You can mark a `FormFieldGroup` component as `disabled`, which disables all the
fields within it. You can override the `disabled` state on a per-field basis
within the `FormFieldGroup` by adding a `disabled={false}` property to the
field.

Loading example...
```
<FormFieldGroup legend="Disabling" disabled>
 <TextField
 label="Disabled"
 placeholder="Disabled"
 hiddenElements={['label']}
 />
 <TextField
 label="Not disabled"
 placeholder="Not disabled"
 disabled={false}
 hiddenElements={['label']}
 />
</FormFieldGroup>
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)