# Menu component for Stripe Apps

## A menu presents a group of actions that a user can choose from, often related to a particular object or context.

SDK version8.x9.x
To add the `Menu` component to your app:

```
import {Menu, MenuItem, MenuGroup} from '@stripe/ui-extension-sdk/ui';
```

A basic menu is made up of an element to trigger the menu, and a series of
MenuItems.

Loading example...
```
<Menu trigger={<Button>Menu</Button>}>
 <MenuItem>Edit</MenuItem>
 <MenuItem></MenuItem>
 <MenuItem>Paste</MenuItem>
</Menu>
```

### Menu props

PropertyType
`children`

Required
`React.ReactNode`

One or more `MenuGroup` or `MenuItem` components.

`onAction`

Optional
`((key: React.Key) => void) | undefined`

Handler that is called when an item is selected.

`trigger`

Optional
`React.ReactNode`

The trigger Element to show/hide the `Menu`. Must be a component that supports
press events, such as a `Button` or `Link`.

## Items

Menus contain multiple vertically arranged items.

Loading example...
```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <Menu aria-label="Menu">
 <MenuItem>Edit</MenuItem>
 <MenuItem disabled></MenuItem>
 <MenuItem>Paste</MenuItem>
 </Menu>
</Box>
```

### MenuItem props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`disabled`

Optional
`boolean | undefined`

Marks an item as disabled. Disabled items cannot be selected, focused, or
otherwise interacted with.

`id`

Optional
`string | undefined`

The id of the item. This will be passed into the `onAction` handler of `Menu`.

`onAction`

Optional
`((key: React.Key) => void) | undefined`

Handler that is called when an item is selected.

## Groups

You can divide items in a menu into groups.

Loading example...
```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <Menu aria-label="Menu">
 <MenuGroup title="Actions">
 <MenuItem>Duplicate</MenuItem>
 <MenuItem>Edit</MenuItem>
 <MenuItem>Cancel</MenuItem>
 </MenuGroup>
 <MenuGroup title="Connections">
 <MenuItem>View customer</MenuItem>
 <MenuItem>View subscription</MenuItem>
 </MenuGroup>
 </Menu>
</Box>
```

### MenuGroup props

PropertyType
`children`

Required
`React.ReactNode`

One or more `MenuItem` components.

`title`

Optional
`React.ReactNode`

## Events

Use the `onAction` prop as a callback to handle `press` events on items. You can
provide the `onAction` prop to the `Menu` to handle item activation across all
items, or to the `MenuItem` directly to handle activation for individual items.

Loading example...
```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <Menu
 aria-label="Menu"
 onAction={(id) => console.log(`Item ${id} was pressed.`)}
 >
 <MenuGroup title="Actions">
 <MenuItem id="duplicate">Duplicate</MenuItem>
 <MenuItem id="edit">Edit</MenuItem>
 <MenuItem id="cancel">Cancel</MenuItem>
 </MenuGroup>
 <MenuGroup title="Connections">
 <MenuItem
 id="View customer"
 onAction={() => console.log('View customer was pressed.')}
 >
 View customer
 </MenuItem>
 <MenuItem id="View subscription">View subscription</MenuItem>
 </MenuGroup>
 </Menu>
</Box>
```

## Triggers

The menu `trigger` property works together with the menu to link the menu’s open
state with a trigger’s pressed state.

Loading example...
```
<Menu trigger={<Button>Menu</Button>}>
 <MenuGroup title="Actions">
 <MenuItem>Duplicate</MenuItem>
 <MenuItem disabled>Edit</MenuItem>
 <MenuItem>Cancel</MenuItem>
 </MenuGroup>
 <MenuGroup title="Connections">
 <MenuItem>View customer</MenuItem>
 <MenuItem>View subscription</MenuItem>
 </MenuGroup>
</Menu>
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)