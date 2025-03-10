# List component for Stripe Apps

## Display a list of information in a variety of preconfigured formats.

SDK version8.x9.x
To add the `List` component to your app:

```
import {List, ListItem} from '@stripe/ui-extension-sdk/ui';
```

You can use the `onAction` handler to respond to `press` events on list items.

```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <List
 onAction={(id: string | number) => console.log(`Pressed row #${id}`)}
 aria-label="Example of a List"
 >
 <ListItem
 value="$100.00"
 id="1"
 title={<Box>Payment #1862</Box>}
 secondaryTitle={<Box>customer@test.com</Box>}
 />
 <ListItem
 value="$63.00"
 id="2"
 title={<Box>Payment #9273</Box>}
 secondaryTitle={<Box>frank@example.com</Box>}
 />
 <ListItem
 value="$7,471.62"
 id="3"
 title={<Box>Payment #643</Box>}
 secondaryTitle={<Box>robert@google.com</Box>}
 />
 <ListItem
 value="$871.01"
 id="4"
 title={<Box>Payment #123</Box>}
 secondaryTitle={<Box>example@gmail.com</Box>}
 />
 </List>
</Box>
```

### List props

PropertyType
`children`

Required
`React.ReactNode`

One or more `ListItem` components.

`onAction`

Optional
`((id: React.Key) => void) | undefined`

Press event handler which receives the corresponding key of the `ListItem` that
was pressed.

## List items

Every list is made up of a collection of `ListItem` components. Uniquely
identify each list item using the `key` prop.

```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <List
 onAction={(id: string | number) => console.log(id)}
 aria-label="Example of a List"
 >
 <ListItem id="apple" title={<Box>Apple</Box>} />
 <ListItem id="orange" title={<Box>Orange</Box>} />
 <ListItem id="banana" title={<Box>Banana</Box>} />
 </List>
</Box>
```

### ListItem props

PropertyType
`icon`

Optional
`React.ReactNode`

Icon that appears to the left of the content and description. Will be overridden
by `image` if both are present.

`id`

Optional
`string | undefined`

The id of the item. This will be passed into the `onAction` handler of `List`.

`image`

Optional
`React.ReactNode`

Image that appears to the left of the content and description. Will override
`icon` if both are present.

`secondaryTitle`

Optional
`React.ReactNode`

Secondary content for the `ListItem` component.

`size`

Optional
`("default" | "large") | undefined`

Size of the `ListItem` component.

`title`

Optional
`React.ReactNode`

Title content for the `ListItem` component.

`value`

Optional
`React.ReactNode`

The value to display on the right-hand side of the item.

## Secondary title

You can add a secondary title to a list item using the `secondaryTitle`
property.

```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <List
 onAction={(id: string | number) => console.log(id)}
 aria-label="Example of a List"
 >
 <ListItem
 id="1"
 title={<Box>John Smith</Box>}
 secondaryTitle={<Box>johnsmith@test.com</Box>}
 />
 <ListItem
 id="2"
 title={<Box>Jane Doe</Box>}
 secondaryTitle={<Box>janedoe@test.com</Box>}
 />
 <ListItem
 id="3"
 title={<Box>Mark Foster</Box>}
 secondaryTitle={<Box>markfoster@test.com</Box>}
 />
 </List>
</Box>
```

## Values

The `ListItem` `value` prop can take arbitrary JSX.

```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <List onAction={(id) => console.log(id)} aria-label="Example of a List">
 <ListItem
 value={
 <Box css={{marginLeft: 'medium', marginRight: 'xsmall'}}>
 <Icon name="truck" />
 </Box>
 }
 id="1"
 title={<Box>Payment #123</Box>}
 secondaryTitle={<Box>example@gmail.com</Box>}
 />
 <ListItem
 value={
 <Box css={{marginLeft: 'medium'}}>
 <Button onPress={() => console.log('delete')} type="destructive">
 <Box css={{marginRight: 'xsmall'}}>
 <Icon name="trash" />
 </Box>
 Delete
 </Button>
 </Box>
 }
 id="2"
 title={<Box>Payment #456</Box>}
 secondaryTitle={<Box>example@gmail.com</Box>}
 />
 <ListItem
 value={
 <Box css={{marginLeft: 'medium'}}>
 <Button onPress={() => console.log('edit')} type="primary">
 Edit
 </Button>
 </Box>
 }
 id="3"
 title={<Box>Payment #789</Box>}
 secondaryTitle={<Box>example@gmail.com</Box>}
 />
 </List>
</Box>
```

### Unsupported components

Note that certain interactive components **won’t** work as `value` props in a
`ListItem`:

- [Select](https://docs.stripe.com/stripe-apps/components/select)
- [TextArea](https://docs.stripe.com/stripe-apps/components/textarea)
- [TextField](https://docs.stripe.com/stripe-apps/components/textfield)

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [Select](https://docs.stripe.com/stripe-apps/components/select)
- [TextArea](https://docs.stripe.com/stripe-apps/components/textarea)
- [TextField](https://docs.stripe.com/stripe-apps/components/textfield)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)