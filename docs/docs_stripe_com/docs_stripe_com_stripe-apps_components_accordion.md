# Accordion component for Stripe Apps

## Use accordions to split long or complex content into collapsible chunks.

SDK version8.x9.x
To add the `Accordion` component to your app:

```
import {Accordion, AccordionItem} from '@stripe/ui-extension-sdk/ui';
```

Accordions help a user to quickly scan a collection, identify elements, and
access more details without leaving the context that they’re working in.

This is a preview of an `Accordion` component with three `AccordionItem`
components inside:

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

### Accordion props

PropertyType
`children`

Required
`React.ReactNode`

One or more `AccordionItem` components.

## AccordionItem

`Accordion` components contain one or more `AccordionItem` components.

### AccordionItem props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`title`

Required
`React.ReactNode`

A title describing the `AccordionItem`.

`actions`

Optional
`React.ReactNode`

A component containing actions that a user can take on the `AccordionItem`. If
there are more than 2 actions, use an overflow menu to show the rest.

`defaultOpen`

Optional
`boolean | undefined`

Whether or not the `AccordionItem` should be open on the first render.

`media`

Optional
`React.ReactNode`

A component containing an optional `Img` or `Icon` to help identify the
`AccordionItem`.

`onChange`

Optional
`((isOpen: boolean) => void) | undefined`

Callback when the open state has changed.

`subtitle`

Optional
`React.ReactNode`

An optional subtitle with addition descriptive information.

## Titles and subtitles

Label all `AccordionItem` components with a `title` that uniquely identifies the
item. You can also use an optional `subtitle` to provide a description or
additional relevant information.

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
 <AccordionItem title="Oranges">
 <Box css={{padding: 'xlarge'}}>Accordion contents</Box>
 </AccordionItem>
 <AccordionItem title="Peaches" subtitle="A subtitle can be provided">
 <Box css={{padding: 'xlarge'}}>Accordion contents</Box>
 </AccordionItem>
 </Accordion>
</Box>
```

## Media

The `AccordionItem` component can contain a media element to show a relevant
icon or image that helps the user identify the item. Only include media when it
helps users identify items and when there’s a strong association between the
media and the item itself.

Loading example...
```
<Box css={{backgroundColor: 'surface'}}>
 <Accordion>
 <AccordionItem
 media={<Icon name="chat" />}
 title="ACH credit transfer"
 subtitle="ACH Credit Transfer enables US customers..."
 >
 <Box css={{padding: 'xlarge'}}>Accordion AccordionContents</Box>
 </AccordionItem>
 <AccordionItem
 title="Cards"
 subtitle="Accept Visa, Mastercard, American Express..."
 >
 <Box css={{padding: 'xlarge'}}>Accordion AccordionContents</Box>
 </AccordionItem>
 <AccordionItem
 title="Apple Pay"
 subtitle="Manage Apple Pay domains and certificates."
 >
 <Box css={{padding: 'xlarge'}}>Accordion AccordionContents</Box>
 </AccordionItem>
 </Accordion>
</Box>
```

## Actions

You can represent actions that an item can have performed on it with buttons or
links placed on the right-hand side of the accordion trigger.

Loading example...
```
const titles = [
 'Example using a link',
 'Example using a button',
 'Multiple buttons are cool too',
];
const actionExamples = [
 <Link key={0} onPress={() => null}>
 Edit
 </Link>,
 <Button key={1} onPress={() => null}>
 Configure
 </Button>,
 <ButtonGroup key={2}>
 <Button onPress={() => null}>Action 1</Button>
 <Button onPress={() => null}>Action 2</Button>
 </ButtonGroup>,
];

return (
 <Box css={{backgroundColor: 'surface'}}>
 <Accordion>
 {[0, 1, 2].map((i) => (
 <AccordionItem
 title={titles[i]}
 subtitle={i > 2 && 'An optional subtitle can be provided.'}
 actions={actionExamples[i]}
 key={i}
 >
 <Box css={{padding: 'xlarge'}}>Accordion AccordionContents</Box>
 </AccordionItem>
 ))}
 </Accordion>
 </Box>
)
```

## Disabling items

Instead of removing a user’s ability to interact with disabled accordion items,
disable the associated actions while still presenting as much information within
the item as possible to the user.

Loading example...
```
<Box css={{backgroundColor: 'surface'}}>
 <Accordion>
 <AccordionItem
 title="Orangesss"
 actions={
 <Button disabled onPress={() => null}>
 Edit
 </Button>
 }
 >
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

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)