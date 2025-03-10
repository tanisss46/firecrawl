# TextArea component for Stripe Apps

## Use TextArea to create an input field for multiple lines of text.

SDK version8.x9.x
To add the `TextArea` component to your app:

```
import {TextArea} from '@stripe/ui-extension-sdk/ui';
```

Loading example...
```
<TextArea
 label="Description"
 placeholder="Acme Inc was founded in…"
 defaultValue="Stripe Apps lets you embed custom…"
 onChange={(e) => {
 console.log(e.target.value);
 }}
/>
```

### TextArea props

PropertyType
`autoComplete`

Optional
`string | undefined`

Specifies one of the possible autocomplete behaviors.

`autoFocus`

Optional
`boolean | undefined`

If `true`, React will focus the element on mount.

`cols`

Optional
`number | undefined`

`css`

Optional
`Object`

Related types:
[CSS](https://docs.stripe.com/stripe-apps/components/textarea#css).

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

`resizeable`

Optional
`boolean | undefined`

`rows`

Optional
`number | undefined`

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

`value`

Optional
`string | undefined`

Controls the input’s text. When you pass this prop, you must also pass an
`onChange` handler that updates the passed value.

`wrap`

Optional
`string | undefined`

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

You can mark a `TextArea` as invalid by setting the `invalid` prop on the
element. This is purely visual. It defaults to `false`.

Loading example...
```
<TextArea
 label="Favorite word"
 defaultValue="Stripe Apps lets you embed custom…"
 invalid
/>
```

## Resizeable

By default, `TextArea` is vertically resizable. Users who need more space
typically prefer this. If you need to prevent the element from resizing, set
`resizeable` to `false`.

Loading example...
```
<TextArea
 label="Resizable bio"
 defaultValue="Stripe Apps lets you embed custom…"
/>
<TextArea
 label="Unresizable bio"
 resizeable={false}
 defaultValue="Stripe Apps lets you embed custom…"
/>
```

## Size

Changing the `size` allows you to choose variants with slightly more or slightly
less room than the default. In general you don’t want to mix and match different
sizes within the same form. The default is `medium`.

Loading example...
```
<TextArea
 label="Description (large)"
 size="large"
 defaultValue="Stripe Apps lets you embed custom…"
/>
<TextArea
 label="Description (medium, default)"
 size="medium"
 defaultValue="Stripe Apps lets you embed custom…"
/>
<TextArea
 label="Description (small)"
 size="small"
 defaultValue="Stripe Apps lets you embed custom…"
/>
```

## Disable and read only

You can mark a field as `disabled`, which prevents any interaction and changes
the styling. Disabled means that no data from that form element is submitted
when the form is submitted.

You can also make a field as `readOnly`. Read-only means any data from within
the element is submitted, but the user can’t change it.

Loading example...
```
<TextArea
 label="Disabled"
 defaultValue="Stripe Apps lets you embed custom…"
 disabled
/>
<TextArea
 label="Readonly"
 defaultValue="Stripe Apps lets you embed custom…"
 readOnly
/>
```

## Rows

A `TextArea` uses rows to control its height rather than using a traditional
height in pixels, just like a regular `<TextArea />`. This allows the element to
size itself based on multiples of the font size, rather than a raw pixel value.
It prevents text from being partially obscured by default.

The vertical height of your `TextArea` component also changes depending on what
size value you set, because that changes the line height of the text inside the
input.

Loading example...
```
<TextArea
 label="Description (3 rows, default)"
 defaultValue="Stripe Apps lets you embed custom…"
/>
<TextArea
 label="Description (6 rows)"
 rows={6}
 defaultValue="Stripe Apps lets you embed custom…"
/>
```

## State management

Use the `TextArea` component as an [uncontrolled
input](https://docs.stripe.com/stripe-apps/how-ui-extensions-work#use-uncontrolled-components-for-interactions):

Loading example...
```
<TextArea
 onChange={(e) => {
 console.log(e);
 }}
 label="About your business"
 placeholder="Our business is…"
/>
```

## Width

Set the width of a `TexaArea` component using [the available
values](https://docs.stripe.com/stripe-apps/style#sizing) with the `css` prop:

Loading example...
```
<TextArea
 label="App feedback"
 defaultValue="Stripe Apps lets you embed custom…"
 css={{width: 'fill'}}
/>
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