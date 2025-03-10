# Box component for Stripe Apps

## Use boxes to wrap other components and add custom styles and layouts.

SDK version8.x9.x
To add the `Box` component to your app:

```
import {Box} from '@stripe/ui-extension-sdk/ui';
```

Boxes are block-level elements, equivalent to a `div` HTML element. They support
[custom styles](https://docs.stripe.com/stripe-apps/style#custom-styles). If you
want to render or style inline elements, see the
[Inline](https://docs.stripe.com/stripe-apps/components/inline) component.

Loading example...
```
<Box
 css={{
 padding: 'xxlarge',
 color: 'secondary',
 backgroundColor: 'container',
 borderRadius: 'small',
 }}
>
 This is a box.
</Box>
```

### Box props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`css`

Optional
`Object`

Related types: [CSS](https://docs.stripe.com/stripe-apps/components/box#css).

### CSS

PropertyType
`alignSelfX`

Optional
`("start" | "center" | "end" | "stretch") | undefined`

Horizontal alignment. See [Layout
properties](https://docs.stripe.com/stripe-apps/style#layout-properties) for
details.

`alignSelfY`

Optional
`("top" | "center" | "baseline" | "bottom" | "stretch") | undefined`

Vertical alignment. See [Layout
properties](https://docs.stripe.com/stripe-apps/style#layout-properties) for
details.

`alignX`

Optional
`("start" | "center" | "end" | "stretch") | undefined`

Horizontal alignment. See [Layout
properties](https://docs.stripe.com/stripe-apps/style#layout-properties) for
details.

`alignY`

Optional
`("top" | "center" | "baseline" | "bottom" | "stretch") | undefined`

Vertical alignment. See [Layout
properties](https://docs.stripe.com/stripe-apps/style#layout-properties) for
details.

`backgroundColor`

Optional
`("container" | "surface") | undefined`

`bleed`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`bleedBottom`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`bleedLeft`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`bleedRight`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`bleedTop`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`bleedX`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`bleedY`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`borderBottomColor`

Optional
`("neutral" | "critical") | undefined`

`borderBottomLeftRadius`

Optional
`("none" | "xsmall" | "small" | "medium" | "large" | "rounded") | undefined`

`borderBottomRightRadius`

Optional
`("none" | "xsmall" | "small" | "medium" | "large" | "rounded") | undefined`

`borderBottomStyle`

Optional
`("dashed" | "dotted" | "double" | "groove" | "hidden" | "inherit" | "initial" |
"inset" | "none" | "outset" | "revert-layer" | "revert" | "ridge" | "solid" |
"unset") | undefined`

`borderBottomWidth`

Optional
`number | undefined`

The width of the border.

`borderColor`

Optional
`("neutral" | "critical") | undefined`

`borderLeftColor`

Optional
`("neutral" | "critical") | undefined`

`borderLeftStyle`

Optional
`("dashed" | "dotted" | "double" | "groove" | "hidden" | "inherit" | "initial" |
"inset" | "none" | "outset" | "revert-layer" | "revert" | "ridge" | "solid" |
"unset") | undefined`

`borderLeftWidth`

Optional
`number | undefined`

The width of the border.

`borderRadius`

Optional
`("none" | "xsmall" | "small" | "medium" | "large" | "rounded") | undefined`

`borderRightColor`

Optional
`("neutral" | "critical") | undefined`

`borderRightStyle`

Optional
`("dashed" | "dotted" | "double" | "groove" | "hidden" | "inherit" | "initial" |
"inset" | "none" | "outset" | "revert-layer" | "revert" | "ridge" | "solid" |
"unset") | undefined`

`borderRightWidth`

Optional
`number | undefined`

The width of the border.

`borderStyle`

Optional
`("dashed" | "dotted" | "double" | "groove" | "hidden" | "inherit" | "initial" |
"inset" | "none" | "outset" | "revert-layer" | "revert" | "ridge" | "solid" |
"unset") | undefined`

`borderTopColor`

Optional
`("neutral" | "critical") | undefined`

`borderTopLeftRadius`

Optional
`("none" | "xsmall" | "small" | "medium" | "large" | "rounded") | undefined`

`borderTopRightRadius`

Optional
`("none" | "xsmall" | "small" | "medium" | "large" | "rounded") | undefined`

`borderTopStyle`

Optional
`("dashed" | "dotted" | "double" | "groove" | "hidden" | "inherit" | "initial" |
"inset" | "none" | "outset" | "revert-layer" | "revert" | "ridge" | "solid" |
"unset") | undefined`

`borderTopWidth`

Optional
`number | undefined`

The width of the border.

`borderWidth`

Optional
`number | undefined`

The width of the border.

`bottom`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`boxShadow`

Optional
`("none" | "base" | "top" | "hover" | "focus") | undefined`

`color`

Optional
`("brand" | "primary" | "secondary" | "disabled" | "info" | "success" |
"attention" | "critical") | undefined`

`columnGap`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`display`

Optional
`"grid" | undefined`

`distribute`

Optional
`("packed" | "space-between") | undefined`

`fill`

Optional
`("brand" | "primary" | "secondary" | "disabled" | "info" | "success" |
"attention" | "critical") | undefined`

`focusRing`

Optional
`("none" | "base" | "top" | "hover" | "focus") | undefined`

`font`

Optional
`("body" | "bodyEmphasized" | "caption" | "heading" | "kicker" | "lead" |
"subheading" | "subtitle" | "title") | undefined`

`fontFamily`

Optional
`("monospace" | "ui") | undefined`

`fontWeight`

Optional
`("regular" | "semibold" | "bold") | undefined`

`gap`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`gapX`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`gapY`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`gridColumns`

Optional
`number | undefined`

`height`

Optional
`(number | "auto" | "fill" | "min" | "max" | "fit" | "1/2" | "1/3" | "2/3" |
"1/4" | "2/4" | "3/4" | "1/5" | "2/5" | "3/5" | "4/5" | "1/6" | "2/6" | "3/6" |
"4/6" | "5/6" | "1/12" | "2/12" | "3/12" | "4/12" | "5/12" | "6/12" | "7/12" |
"8/12" | "9/12" | "10/12" | "11/12") | undefined`

The height of the component. See
[Sizing](https://docs.stripe.com/stripe-apps/style#sizing) for details.

`inset`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`keyline`

Optional
`("neutral" | "critical") | undefined`

`left`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`margin`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`marginBottom`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`marginLeft`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`marginRight`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`marginTop`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`marginX`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`marginY`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`maxHeight`

Optional
`(number | "auto" | "fill" | "min" | "max" | "fit" | "1/2" | "1/3" | "2/3" |
"1/4" | "2/4" | "3/4" | "1/5" | "2/5" | "3/5" | "4/5" | "1/6" | "2/6" | "3/6" |
"4/6" | "5/6" | "1/12" | "2/12" | "3/12" | "4/12" | "5/12" | "6/12" | "7/12" |
"8/12" | "9/12" | "10/12" | "11/12") | undefined`

The height of the component. See
[Sizing](https://docs.stripe.com/stripe-apps/style#sizing) for details.

`maxWidth`

Optional
`(number | "auto" | "fill" | "min" | "max" | "fit" | "1/2" | "1/3" | "2/3" |
"1/4" | "2/4" | "3/4" | "1/5" | "2/5" | "3/5" | "4/5" | "1/6" | "2/6" | "3/6" |
"4/6" | "5/6" | "1/12" | "2/12" | "3/12" | "4/12" | "5/12" | "6/12" | "7/12" |
"8/12" | "9/12" | "10/12" | "11/12") | undefined`

The width of the component. See
[Sizing](https://docs.stripe.com/stripe-apps/style#sizing) for details.

`minHeight`

Optional
`(number | "auto" | "fill" | "min" | "max" | "fit" | "1/2" | "1/3" | "2/3" |
"1/4" | "2/4" | "3/4" | "1/5" | "2/5" | "3/5" | "4/5" | "1/6" | "2/6" | "3/6" |
"4/6" | "5/6" | "1/12" | "2/12" | "3/12" | "4/12" | "5/12" | "6/12" | "7/12" |
"8/12" | "9/12" | "10/12" | "11/12") | undefined`

The height of the component. See
[Sizing](https://docs.stripe.com/stripe-apps/style#sizing) for details.

`minTileWidth`

Optional
`(number | "1/2" | "1/3" | "2/3" | "1/4" | "2/4" | "3/4" | "1/5" | "2/5" | "3/5"
| "4/5" | "1/6" | "2/6" | "3/6" | "4/6" | "5/6" | "1/12" | "2/12" | "3/12" |
"4/12" | "5/12" | "6/12" | "7/12" | "8/12" | "9/12" | "10/12" | "11/12") |
undefined`

`minWidth`

Optional
`(number | "auto" | "fill" | "min" | "max" | "fit" | "1/2" | "1/3" | "2/3" |
"1/4" | "2/4" | "3/4" | "1/5" | "2/5" | "3/5" | "4/5" | "1/6" | "2/6" | "3/6" |
"4/6" | "5/6" | "1/12" | "2/12" | "3/12" | "4/12" | "5/12" | "6/12" | "7/12" |
"8/12" | "9/12" | "10/12" | "11/12") | undefined`

The width of the component. See
[Sizing](https://docs.stripe.com/stripe-apps/style#sizing) for details.

`overflow`

Optional
`("visible" | "hidden" | "clip" | "scroll" | "auto") | undefined`

`overflowWrap`

Optional
`("break-word" | "normal") | undefined`

`overflowX`

Optional
`("visible" | "hidden" | "clip" | "scroll" | "auto") | undefined`

`overflowY`

Optional
`("visible" | "hidden" | "clip" | "scroll" | "auto") | undefined`

`padding`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`paddingBottom`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`paddingLeft`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`paddingRight`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`paddingTop`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`paddingX`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`paddingY`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`rowGap`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`stack`

Optional
`("x" | "y" | "z") | undefined`

`textAlign`

Optional
`("center" | "end" | "justify" | "left" | "match-parent" | "right" | "start") |
undefined`

`textOverflow`

Optional
`"ellipsis" | undefined`

`textTransform`

Optional
`("capitalize" | "uppercase" | "lowercase" | "none" | "full-width" |
"full-size-kana") | undefined`

`top`

Optional
`(number | "xxsmall" | "xsmall" | "small" | "medium" | "large" | "xlarge" |
"xxlarge") | undefined`

`topShadow`

Optional
`("none" | "base" | "top" | "hover" | "focus") | undefined`

`whiteSpace`

Optional
`("normal" | "nowrap" | "pre" | "pre-wrap" | "pre-line" | "break-spaces") |
undefined`

`width`

Optional
`(number | "auto" | "fill" | "min" | "max" | "fit" | "1/2" | "1/3" | "2/3" |
"1/4" | "2/4" | "3/4" | "1/5" | "2/5" | "3/5" | "4/5" | "1/6" | "2/6" | "3/6" |
"4/6" | "5/6" | "1/12" | "2/12" | "3/12" | "4/12" | "5/12" | "6/12" | "7/12" |
"8/12" | "9/12" | "10/12" | "11/12") | undefined`

The width of the component. See
[Sizing](https://docs.stripe.com/stripe-apps/style#sizing) for details.

`wordBreak`

Optional
`("normal" | "break-all" | "keep-all" | "break-word") | undefined`

`wordWrap`

Optional
`("break-word" | "normal") | undefined`

`wrap`

Optional
`("wrap" | "nowrap" | "wrap-reverse") | undefined`

`zIndex`

Optional
`("overlay" | "partial") | undefined`

`background`

OptionalDeprecated
Use the `backgroundColor` property instead.

`("container" | "surface") | undefined`

`isolatedDependencies`

OptionalDeprecated
`string[] | undefined`

`layout`

OptionalDeprecated
Use the `stack` property instead.

`("column" | "inline" | "row" | "inline-column" | "inline-row") | undefined`

`when`

OptionalDeprecated
Use nested styles instead.

`(string | { pointer: "none" | "coarse" | "fine"; colorScheme: "dark" | "light";
motion: "supported" | "reduced"; hover: "none" | "hover"; viewportWidth: "small"
| "medium" | "large" | "xlarge"; contrast: "more" | "less"; }[] | { pointer:
"none" | "coarse" | "fine"; colorScheme: "dark" | "light"; motion: "supported" |
"reduced"; hover: "none" | "hover"; viewportWidth: "small" | "medium" | "large"
| "xlarge"; contrast: "more" | "less"; }) | undefined`

## Nesting boxes

For some components, you can use a Box to manage the layout and spacing of their
children. For example, nest a Box inside an
[AccordionItem](https://docs.stripe.com/stripe-apps/components/accordion) to add
padding:

Loading example...
```
<Box css={{backgroundColor: 'surface'}}>
 <Accordion>
 <AccordionItem title="Apples">
 <Box css={{padding: 'xlarge'}}>Accordion contents</Box>
 </AccordionItem>
 <AccordionItem title="Bananas">
 <Box css={{padding: 'xlarge'}}>Accordion contents</Box>
 </AccordionItem>
 <AccordionItem title="Peaches" subtitle="A subtitle can be provided">
 <Box css={{padding: 'xlarge'}}>Accordion contents</Box>
 </AccordionItem>
 </Accordion>
</Box>
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [custom styles](https://docs.stripe.com/stripe-apps/style#custom-styles)
- [Inline](https://docs.stripe.com/stripe-apps/components/inline)
- [Layout
properties](https://docs.stripe.com/stripe-apps/style#layout-properties)
- [Sizing](https://docs.stripe.com/stripe-apps/style#sizing)
- [AccordionItem](https://docs.stripe.com/stripe-apps/components/accordion)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)