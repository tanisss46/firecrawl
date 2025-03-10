# Style your app

## Learn how to style UI components in your app.

You can style a Stripe App using design tokens that we provide. This helps you
match the Dashboard visually, provide consistency, and maintain a high quality
bar.

- The `Box` and `Inline` components support [custom
styles](https://docs.stripe.com/stripe-apps/style#custom-styles).
- Other components have [preset
styles](https://docs.stripe.com/stripe-apps/style#preset-styles) which you can
sometimes adjust.

## Custom styles

The [Box](https://docs.stripe.com/stripe-apps/components/box) and
[Inline](https://docs.stripe.com/stripe-apps/components/inline) components
support custom styles. `Box` and `Inline` are styleable containers like HTML
`div` and `span`. To style them, use their `css` prop. They use CSS syntax, with
a few differences from vanilla CSS.

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

Unlike in vanilla CSS, you can’t choose arbitrary font faces and styles. Use the
`font` and `fontWeight` properties. For more information, see
[Typography](https://docs.stripe.com/stripe-apps/style#typograpphy).

Loading example...
```
<Inline css={{font: 'body', color: 'primary', fontWeight: 'semibold'}}>
 This text is emphasized
</Inline>
```

Layout also works differently than it does in vanilla CSS. Instead, Stripe Apps
use the same layout system Stripe uses internally. For more information, see
[Layout](https://docs.stripe.com/stripe-apps/style#layout).

```
<Box
 css={{
 stack: 'x',
 gap: 'medium',
 }}
>
 <Box css={{width: '1/4', padding: 'medium', keyline: 'neutral'}} />
 <Box css={{width: '3/4', padding: 'medium', keyline: 'neutral'}} />
</Box>
```

All styling tokens are exposed through TypeScript, which means you’ll get a
dropdown in your editor to autocomplete from the available values.

## Color

Set colors in your custom styles by using the following values.

### Backgrounds

To set the background color of a
[Box](https://docs.stripe.com/stripe-apps/components/box) or
[Inline](https://docs.stripe.com/stripe-apps/components/inline) component, use
the CSS `backgroundColor` property:

```
<Box css={{ backgroundColor: 'container' }}>
 Box with a darker background.
</Box>
```

Use the following tokens as values for `backgroundColor`:

ExampleTokenUsage`surface`Used for the background of apps`container`Used for
cards and sections within an app
### Borders

To add a border to a [Box](https://docs.stripe.com/stripe-apps/components/box)
or [Inline](https://docs.stripe.com/stripe-apps/components/inline) component,
use the CSS `keyline` property:

```
<Box css={{ keyline: 'neutral' }}>
 Box with a neutral border.
</Box>
```

Use the following tokens as values for `keyline`:

ExampleTokenUsage`neutral`The default color for all borders and
dividers`critical`Used for content which is critically urgent to the user
### Text & icons

To set a color for all text or icons in a
[Box](https://docs.stripe.com/stripe-apps/components/box) or
[Inline](https://docs.stripe.com/stripe-apps/components/inline) component, use
the CSS `color` property:

```
<Box css={{ color: 'success' }}>
 Box with green text.
</Box>
```

For an icon that contrasts with the other children of its container, use `fill`.
Otherwise, icons match the text around them.

```
<Box css={{ color: 'primary' }}>
 <Icon css={{ fill: 'success' }}/>
 Box with normal text and a green icon.
</Box>
```

Use the following tokens as values for `color` and `fill`:

ExampleTokenUsage`primary`The default color for text and icons`secondary`Used to
for text and icons which are less prominent`disabled`Used for elements which are
disabled`info`Used for content that is neutral and informational`success`Used
for content which indicates the success of some action`attention`Used for
content which is should grab the user’s attention`critical`Used for content
which is critically urgent to the user. Should be used sparingly.
## Typography

To change the style of text in a
[Box](https://docs.stripe.com/stripe-apps/components/box) or
[Inline](https://docs.stripe.com/stripe-apps/components/inline) component, use
the custom `font` property:

```
<Inline css={{font: 'heading'}}>Heading</Inline>
```

The following styles are available:

TokenUsageExampleheadingUsed for labeling a section of your appThe quick brown
fox jumps over the lazy dog.subheadingUsed for labeling content within a section
of your appThe quick brown fox jumps over the lazy dog.bodyPrimary body text of
the appThe quick brown fox jumps over the lazy dog.captionUsed for text that
should be less prominent than body textThe quick brown fox jumps over the lazy
dog.
### Text overflow and wrapping

To change how overflow text is handled in a
[Box](https://docs.stripe.com/stripe-apps/components/box) component, use the
`textOverflow`, `overflow`, `whiteSpace`, and `overflowWrap` properties:

```
<Box css={{textOverflow: 'ellipsis', overflow: 'hidden', overflowWrap:
'normal'}}>
 Box where long text is cut off with an ellipsis
</Box>
```

CSSUsageExample{textOverflow: 'ellipsis', overflow: 'hidden', overflowWrap:
'normal'}Used for adding an ellipsis (...) to text that overflows the available
spaceSupercalifragilisticexpialidociousSupercalifragilisticexpialidociousSupercalifragilisticexpialidocious{overflowWrap:
'break-word'}Used for breaking up long
wordsSupercalifragilisticexpialidociousSupercalifragilisticexpialidocious{whiteSpace:
'nowrap'}Used to prevent lines from wrappingThis text is too long for the
container.
For for more overflow and text wrapping scenarios, see [Wrapping and Breaking
Text](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Text/Wrapping_Text).

### Text transformation

You can transform text in a
[Box](https://docs.stripe.com/stripe-apps/components/box) or
[Inline](https://docs.stripe.com/stripe-apps/components/inline) component using
the `textTransform` property:

```
<Box css={{textTransform: 'uppercase'}}>
 Box where all text appears uppercase
</Box>
```

Here are some common values that can be used for the `textTransform` property:

TokenUsageBeforeAftercapitalizeUsed to convert the first letter of each word to
uppercaseLorem ipsum dolor sit ametLorem ipsum dolor sit ametuppercaseUsed to
convert all letters to uppercaseLorem ipsum dolor sit ametLorem ipsum dolor sit
ametlowercaseUsed to convert all letters to lowercaseLorem ipsum dolor sit
ametLorem ipsum dolor sit ametnoneUsed to prevent the case of letters from being
changedloREM iPSUm DOLor SIt AMetloREM iPSUm DOLor SIt AMet
See
[text-transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
for the full list.

### Text alignment

You can change the alignment of text in a
[Box](https://docs.stripe.com/stripe-apps/components/box) component using the
`textAlign` property:

```
<Box css={{textAlign: 'center'}}>
 Box where text is centered
</Box>
```

Use the following token values for `textAlign`:

TokenUsageExampleleftUsed to algin text to the leftThis text is left
alignedrightUsed to align text to the rightThis text is right alignedstartUsed
align text to the start directionThis text is start alignedendUsed to align text
to the end directionThis text is end alignedcenterUsed to center textThis text
is centeredjustifyUsed to justify textThis is some text that is justified
## Layout

The Stripe Apps layout styling API allows you to write styles that can take
advantage of our design tokens and includes other improvements over vanilla CSS.
Use these tokens in a [Box](https://docs.stripe.com/stripe-apps/components/box)
component to control layout for its children. Other containers, like
[List](https://docs.stripe.com/stripe-apps/components/list), handle layout
automatically.

We conceptualize layouts as “stacks.”

### Horizontal stacks

To stack elements horizontally and match widths:

```
<Box
 css={{
 stack: 'x',
 gap: 'medium',
 alignX: 'stretch', // This is the default and can be omitted
 }}
>
```

To stack elements horizontally with fractional widths:

```
<Box
 css={{
 stack: 'x',
 gap: 'medium',
 }}
>
 <Box css={{width: '1/4', padding: 'medium', keyline: 'neutral'}} />
 <Box css={{width: '3/4', padding: 'medium', keyline: 'neutral'}} />
</Box>
```

To stack elements horizontally with a fractional width for one element and the
rest of the elements stretched:

```
<Box
 css={{
 stack: 'x',
 gap: 'medium',
 }}
>
 <Box css={{padding: 'medium', keyline: 'neutral'}} />
 <Box css={{width: '1/4', padding: 'medium', keyline: 'neutral'}} />
 <Box css={{padding: 'medium', keyline: 'neutral'}} />
</Box>
```

To align elements to the start with a gap:

```
<Box
 css={{
 stack: 'x',
 gap: 'medium',
 alignX: 'start',
 }}
>
```

To distribute elements:

```
<Box
 css={{
 stack: 'x',
 distribute: 'space-between',
 }}
>
```

To align elements to the end with a gap:

```
<Box
 css={{
 stack: 'x',
 gap: 'medium',
 alignX: 'end',
 }}
>
```

To vertically align elements to the bottom:

```
<Box
 css={{
 stack: 'x',
 gap: 'medium',
 alignX: 'start',
 alignY: 'bottom',
 }}
>
```

To include dividers between elements:

```
<Box
 css={{
 stack: 'x',
 gap: 'small',
 alignX: 'start',
 }}
>
 <Box css={{padding: 'medium', keyline: 'neutral'}} />
 <Divider />
 <Box css={{padding: 'medium', keyline: 'neutral'}} />
 <Divider />
 <Box css={{padding: 'medium', keyline: 'neutral'}} />
</Box>
```

To wrap items into rows:

```
<Box
 css={{
 stack: 'x',
 gap: 'medium',
 wrap: 'wrap',
 alignX: 'start',
 }}
>
```

To have a different horizontal and vertical gap:

```
<Box
 css={{
 stack: 'x',
 gapX: 'small',
 gapY: 'large',
 wrap: 'wrap',
 alignX: 'start',
 }}
>
```

To center elements horizontally while wrapping:

```
<Box
 css={{
 stack: 'x',
 gap: 'medium',
 wrap: 'wrap',
 alignX: 'center',
 }}
>
```

To center elements vertically while wrapping:

```
<Box
 css={{
 stack: 'x',
 gap: 'medium',
 wrap: 'wrap',
 alignX: 'start',
 alignY: 'center',
 }}
>
```

### Vertical stacks

To stack elements vertically and match widths:

```
<Box
 css={{
 stack: 'y',
 gap: 'medium',
 }}
>
```

To stack elements vertically while centering horizontally:

```
<Box
 css={{
 stack: 'y',
 gap: 'medium',
 alignX: 'center',
 }}
>
 <Box css={{width: '1/4', padding: 'medium', keyline: 'neutral'}} />
 <Box css={{width: '2/3', padding: 'medium', keyline: 'neutral'}} />
 <Box css={{width: '1/3', padding: 'medium', keyline: 'neutral'}} />
</Box>
```

### Layered stacks

To display elements atop one another:

```
<Box
 css={{
 stack: 'z',
 alignX: 'center',
 alignY: 'center',
 }}
>
 <Box css={{padding: 'xxlarge', keyline: 'neutral'}} />
 <Box css={{padding: 'large', keyline: 'neutral'}} />
 <Box css={{padding: 'small', keyline: 'neutral'}} />
</Box>
```

### Layout properties

PropertyValues`alignX``'start' | 'center' | 'end' | 'stretch'``alignY``'top' |
'center' | 'baseline' | 'bottom' | 'stretch'``distribute``'space-between' |
'packed'``gap`See
[Spacing](https://docs.stripe.com/stripe-apps/style#spacing)`overflowX |
overflowY``'visible' | 'hidden' | 'scroll' | 'auto'``stack``'x' | 'y' |
'z'``wrap``'wrap'`
## Spacing

You can specify margins, padding, and layout gaps using the values listed below.

```
<Box css={{margin: 'small'}} />
```

TokenValue`0`0px`xxsmall`2px`xsmall`4px`small`8px`medium`16px`large`24px`xlarge`32px`xxlarge`48px
## Sizing

You can specify width and height using fractions or content-based sizing tokens.

```
<Box css={{width: '1/2'}} />
```

### Fractional sizing

The available fractions include halves, thirds, quarters, fifths, sixths and,
twelfths. The `fill` token enables a component to match the size of its
container.

TokenValue`0`0px`1/2`50%`1/3`, `2/3`33.333333%, 66.666667%`1/4`, `2/4`,
`3/4`,25%, 50%, 75%`1/5`, `2/5`, `3/5`, `4/5`20%, 40%, 60%, 80%`1/6`, `2/6`,
`3/6`, `4/6`, `5/6`16.666667%, 33.333333%, 50%, 66.666667%, 83.333333%`1/12`,
`2/12`, `3/12`, `4/12`, `5/12`, `6/12`, `7/12`, `8/12`, `9/12`, `10/12`,
`11/12`8.333333%, 16.666667%, 25%, 33.333333%, 41.666667%, 50%, 58.333333%,
66.666667%, 75%, 83.333333%, 91.666667%`fill`100
### Content-based sizing

You can size a `Box` relative to the content within it.

TokenUsage`min`Content inside the component takes all wrapping opportunities,
becoming as small as the longest contents.`max`Represents the maximum possible
width of the content. When applied to text, the text won’t wrap, even if it
causes the text to extend outside the bounds of its container.`fit`Fills the
available space, but only up to the maximum size of the content.
## Preset styles

Components other than `Box` and `Inline` have preset styles, which helps
maintain consistency. You can sometimes control or override the presets in a
specific way.

### Automatic styling

Some components style themselves automatically. For example,
[Chips](https://docs.stripe.com/stripe-apps/components/chip) automatically
change their appearance depending on what callbacks they implement. This helps
the user understand their behavior. To avoid confusion, you can’t override these
details.

Loading example...
```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <ChipList>
 <Chip
 label="Currency"
 value="USD"
 onDropdown={() => {
 console.log('Dropdown function triggered');
 }}
 onClose={() => {
 console.log('Close function triggered');
 }}
 />
 <Chip
 label="Status"
 value="Succeeded"
 onDropdown={() => {
 console.log('Dropdown function triggered');
 }}
 onClose={() => {
 console.log('Close function triggered');
 }}
 />
 <Chip
 label="Amount"
 onAddSuggestion={() => {
 console.log('Add Amount suggestion');
 }}
 />
 <Chip
 label="Date"
 onAddSuggestion={() => {
 console.log('Add Date suggestion');
 }}
 />
 </ChipList>
</Box>
```

### Several presets

Some components, like
[Buttons](https://docs.stripe.com/stripe-apps/components/button), have a few
styles you can select using a prop. See the documentation for each component for
details.

Loading example...
```
<Button type="primary">Primary</Button>
<Button>Secondary</Button>
<Button type="destructive">Destructive</Button>
```

### Limited CSS

Some components support specific CSS properties. For example,
[Icons](https://docs.stripe.com/stripe-apps/components/icon) support color using
the `fill` property. See the documentation for each component for details.

Loading example...
```
<Icon name="cancelCircle" css={{fill: 'critical'}} />
```

## See also

- [Extension SDK API
reference](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api)
- [Stripe Apps UI Components](https://docs.stripe.com/stripe-apps/components)
- [Build a UI](https://docs.stripe.com/stripe-apps/build-ui)

## Links

- [Box](https://docs.stripe.com/stripe-apps/components/box)
- [Inline](https://docs.stripe.com/stripe-apps/components/inline)
- [Wrapping and Breaking
Text](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Text/Wrapping_Text)
-
[text-transform](https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform)
- [List](https://docs.stripe.com/stripe-apps/components/list)
- [Chips](https://docs.stripe.com/stripe-apps/components/chip)
- [Buttons](https://docs.stripe.com/stripe-apps/components/button)
- [Icons](https://docs.stripe.com/stripe-apps/components/icon)
- [Extension SDK API
reference](https://docs.stripe.com/stripe-apps/reference/extensions-sdk-api)
- [Stripe Apps UI Components](https://docs.stripe.com/stripe-apps/components)
- [Build a UI](https://docs.stripe.com/stripe-apps/build-ui)