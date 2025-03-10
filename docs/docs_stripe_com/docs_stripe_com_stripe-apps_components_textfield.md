# TextField component for Stripe Apps

## Use TextField to create a text input field.

SDK version8.x9.x
To add the `TextField` component to your app:

```
import {TextField} from '@stripe/ui-extension-sdk/ui';
```

Loading example...
```
<TextField
 label="Business name"
 placeholder="Acme Inc…"
 onChange={(e) => {
 console.log(e.target.value);
 }}
/>
```

### TextField props

PropertyType
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

Related types:
[CSS](https://docs.stripe.com/stripe-apps/components/textfield#css).

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

`maxLength`

Optional
`number | undefined`

Specifies the maximum length of text.

`minLength`

Optional
`number | undefined`

Specifies the minimum length of text.

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

`onKeyDown`

Optional
`((event: React.KeyboardEvent<HTMLInputElement>) => void) | undefined`

Fires when a key is pressed.

`onKeyUp`

Optional
`((event: React.KeyboardEvent<HTMLInputElement>) => void) | undefined`

Fires when a key is released.

`placeholder`

Optional
`string | undefined`

Displayed in a dimmed color when the input value is empty.

`readOnly`

Optional
`boolean | undefined`

If `true`, the input is not editable by the user.

`required`

Optional
`boolean | undefined`

If `true`, the value must be provided for the form to submit.

`size`

Optional
`("small" | "medium" | "large") | undefined`

The size of the component.

`spellCheck`

Optional
`boolean | "true" | "false" | undefined`

If explicitly set to `true` or `false`, enables or disables spellchecking.

`tabIndex`

Optional
`number | undefined`

Overrides the default tab key behavior. Avoid using values other than `-1` and
`0`.

`type`

Optional
`("number" | "text" | "search" | "tel" | "url" | "email" | "password") |
undefined`

Choose between the text-alike types on an input.

`value`

Optional
`string | undefined`

Controls the input’s text. When you pass this prop, you must also pass an
`onChange` handler that updates the passed value.

`onKeyPress`

OptionalDeprecated
`((event: React.KeyboardEvent<HTMLInputElement>) => void) | undefined`

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

## Invalid

You can set `invalid` on a TextField element to render the component with a red
outline as a visual indicator that the value provided isn’t acceptable. Omitting
this property defaults to `false`.

Loading example...
```
<TextField label="Current year" defaultValue="1892" invalid />
```

## Type

You can set the `type` property for the TextField to render it differently
depending on the type of text value expected. This is similar to the type
attribute on an `<input />`, but is restricted to types that allow text.
Omitting this property defaults to `text`.

Loading example...
```
<TextField label="Text" type="text" />
<TextField label="Password" type="password" />
<TextField label="Search" type="search" />
<TextField label="Number" type="number" />
```

## Size

Changing the `size` allows you to choose variants with slightly more or slightly
less room than the default. In general you don’t want to mix and match different
sizes within the same form. The default is `medium`.

Loading example...
```
<TextField label="Small" size="small" />
<TextField label="Medium" size="medium" />
<TextField label="Large" size="large" />
```

## Disabled and read only

You can mark a field as `disabled`, which prevents any interaction and changes
the styling. Disabled means that no data from that form element is submitted
when the form is submitted.

You can also make a field as `readOnly`. Read-only means any data from within
the element will be submitted, but the user can’t change it.

Loading example...
```
<TextField label="Disabled" defaultValue="Field is disabled" disabled />
<TextField label="Readonly" defaultValue="Field is readonly" readOnly />
```

## State management

Use the `TextField` component as an [uncontrolled
input](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions):

Loading example...
```
<TextField
 onChange={(e) => {
 console.log(e);
 }}
 label="First name"
/>
```

## Width

Set the width of a `TextField` component using [the available
values](https://docs.stripe.com/stripe-apps/style#sizing) with the `css` prop:

Loading example...
```
<TextField label="Search" type="search" css={{width: 'fill'}} />
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