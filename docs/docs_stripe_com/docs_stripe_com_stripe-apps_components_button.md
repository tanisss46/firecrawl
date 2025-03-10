# Button component for Stripe Apps

## Buttons allow users to take actions, and you can use them to direct a user's attention or warn them of outcomes.

SDK version8.x9.x
To add the `Button` component to your app:

```
import {Button} from '@stripe/ui-extension-sdk/ui';
```

There are multiple button types available:

Loading example...
```
<Button type="primary">Primary</Button>
<Button>Secondary</Button>
<Button type="destructive">Destructive</Button>
```

### Button props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`css`

Optional
`Object`

Related types: [CSS](https://docs.stripe.com/stripe-apps/components/button#css).

`disabled`

Optional
`boolean | undefined`

Whether the action is disabled.

`href`

Optional
`string | undefined`

Native `href` attribute.

`onPress`

Optional
`((event: PressEvent) => void) | undefined`

Handler that is called when the press is released over the target.

`size`

Optional
`("small" | "medium" | "large") | undefined`

The size of the component.

`target`

Optional
`("_self" | "_blank" | "_top" | "_parent") | undefined`

Where to display the linked URL, as the name for a browsing context.

`type`

Optional
`("primary" | "secondary" | "destructive") | undefined`

The type of the `Button`.

`className`

OptionalDeprecated
`string | undefined`

### CSS

PropertyType
`alignX`

Optional
`("start" | "center" | "end" | "stretch") | undefined`

Horizontal alignment. See [Layout
properties](https://docs.stripe.com/stripe-apps/style#layout-properties) for
details.

`width`

Optional
`(number | "auto" | "fill" | "min" | "max" | "fit" | "1/2" | "1/3" | "2/3" |
"1/4" | "2/4" | "3/4" | "1/5" | "2/5" | "3/5" | "4/5" | "1/6" | "2/6" | "3/6" |
"4/6" | "5/6" | "1/12" | "2/12" | "3/12" | "4/12" | "5/12" | "6/12" | "7/12" |
"8/12" | "9/12" | "10/12" | "11/12") | undefined`

The width of the component. See
[Sizing](https://docs.stripe.com/stripe-apps/style#sizing) for details.

## Content guidelines

### Use the {verb} + {noun} formula for labels

For example, **Update customer**. It’s acceptable to break this pattern in the
case of common actions like **Done**, **Close**, **Cancel**, **Add**, or
**Delete**.

### Be as descriptive as possible

When a button performs an action or navigates the user to a location, try to
name that action or location within the label.

### Use sentence case

This applies for most cases except proper nouns and phrases.

### Avoid punctuation

Avoid periods, exclamation points, and question marks.

### Use second person

When referring to the user within a button or link, always use second person
personal pronouns. Example: **Post your status**.

## Primary buttons

Primary buttons initiate the primary action of any given page or flow. Avoid
having more than one primary button available to the user at a given time.

Loading example...
```
<Button type="primary" onPress={() => console.log('Button was pressed')}>
 Primary button
</Button>
```

## Secondary buttons

Secondary buttons are the default and most common buttons in product interfaces.
In general, use the secondary style for buttons that aren’t for primary actions.

Loading example...
```
<Button onPress={() => console.log('Button was pressed')}>
 Secondary button
</Button>
```

## Destructive buttons

Use destructive buttons exclusively for actions that result in the destruction
of any object or data.

Loading example...
```
<Button
 type="destructive"
 onPress={() => console.log('Button was pressed')}
>
 Destructive button
</Button>
```

## Button sizes

Buttons are available in three sizes, which determine the height of the element.
Buttons can be as wide as needed to fill their container.

- You can use small buttons in contexts where space is limited or to match the
size of other, small text such as legal terms, and so on.
- Medium is the default size for buttons.
- You can use large buttons in contexts where a call to action (CTA) needs
increased prominence.
Loading example...
```
<Button size="small">Small button</Button>
<Button>Medium button</Button>
<Button size="large">Large button</Button>
```

## Disabled buttons

Loading example...
```
<Button type="primary" disabled>
 Hello!
</Button>
<Button disabled>Secondary</Button>
<Button type="destructive" disabled>
 Destructive
</Button>
```

## Icons in buttons

Use an [icon](https://docs.stripe.com/stripe-apps/components/icon) inside of a
button:

Loading example...
```
<Button type="primary">
 <Icon name="addCircle" />
 Add customer
</Button>
```

## Full-width buttons

Create a full-width `Button` component using the `css` prop:

Loading example...
```
<Button type="primary" css={{width: 'fill', alignX: 'center'}}>
 Full-width button
</Button>
```

## Opening links in new tabs

Loading example...
```
<Button href="https://stripe.com" target="_blank">
 Open link in new tab
</Button>
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [Layout
properties](https://docs.stripe.com/stripe-apps/style#layout-properties)
- [Sizing](https://docs.stripe.com/stripe-apps/style#sizing)
- [icon](https://docs.stripe.com/stripe-apps/components/icon)
- [https://stripe.com](https://stripe.com)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)