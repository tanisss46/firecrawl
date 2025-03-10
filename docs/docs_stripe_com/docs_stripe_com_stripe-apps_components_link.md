# Link component for Stripe Apps

## Links are used for navigating users from one page to another, and for actions that need more subtlety than a button provides.

SDK version8.x9.x
To add the `Link` component to your app:

```
import {Link} from '@stripe/ui-extension-sdk/ui';
```

Stripe products have two types of links available: primary and secondary.

Loading example...
```
<Link href="https://www.stripe.com">Primary link</Link>
<Link type="secondary" href="https://www.stripe.com">
 Secondary link
</Link>
```

### Link props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`css`

Optional
`Object`

Related types: [CSS](https://docs.stripe.com/stripe-apps/components/link#css).

`disabled`

Optional
`boolean | undefined`

Whether the action is disabled.

`external`

Optional
`boolean | undefined`

Whether linking out to an external resource.

`href`

Optional
`string | undefined`

Native `href` attribute.

`onPress`

Optional
`((event: PressEvent) => void) | undefined`

Handler that is called when the press is released over the target.

`rel`

Optional
`string | undefined`

Native `rel` attribute.

`tabIndex`

Optional
`number | undefined`

Overrides the default tab key behavior. Avoid using values other than `-1` and
`0`.

`target`

Optional
`("_self" | "_blank" | "_top" | "_parent") | undefined`

Where to display the linked URL, as the name for a browsing context.

`type`

Optional
`("primary" | "secondary") | undefined`

The type of the `Link`.

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

## Primary link

The primary style is the default for links. Use it whenever linking out to
external resources or to other pages within the application.

Loading example...
```
<Link href="https://www.stripe.com">Primary link</Link>
<Link external href="https://www.example.com">
 External primary link
</Link>
```

## Secondary link

Use secondary links in the following situations:

- When a link would otherwise clash with another nearby primary button or link
- When a page presents many items that are each a link. Because a page full of
primary links could be overwhelming, we use secondary links in these cases.
- When linking to an object like a Customer, Payment, Product, and so on.
Wherever the UI refers to these objects, link them. Use the secondary style to
eliminate visual clutter, as one page might link many objects. .
Loading example...
```
<Link type="secondary" href="https://www.stripe.com">
 Secondary link
</Link>
```

## Disabled links

Loading example...
```
<Link disabled href="https://www.stripe.com">
 Primary link
</Link>
<Link disabled type="secondary" href="https://www.stripe.com">
 Secondary link
</Link>
```

## Opening links in new tabs

Loading example...
```
<Link href="https://stripe.com" target="_blank">
 Open link in new tab
</Link>
```

## Allowed href values

The href attribute supports relative and http or https URLs. Other values are
sanitized at runtime.

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [https://www.stripe.com](https://www.stripe.com)
- [Layout
properties](https://docs.stripe.com/stripe-apps/style#layout-properties)
- [Sizing](https://docs.stripe.com/stripe-apps/style#sizing)
- [https://www.example.com](https://www.example.com)
- [https://stripe.com](https://stripe.com)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)