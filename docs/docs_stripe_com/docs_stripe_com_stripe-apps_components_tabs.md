# Tabs component for Stripe Apps

## Use tabs to display sections of content.

SDK version8.x9.x
Tabs are sections of content that display one panel of content at a time. The
list of tab elements sits along the top edge of the currently displayed panel.

To add the `Tabs` component to your app:

```
import {Tabs, Tab, TabList, TabPanel, TabPanels} from
'@stripe/ui-extension-sdk/ui';
```

Loading example...
```
<Box css={{width: 'fill'}}>
 <Tabs fitted>
 <TabList>
 {[1, 2].map((i) => (
 <Tab key={i} tabKey={i}>
 Tab {i}
 </Tab>
 ))}
 </TabList>
 <TabPanels>
 {[1, 2].map((i) => (
 <TabPanel key={i} tabKey={i}>
 <Box css={{backgroundColor: 'container', padding: 'large'}}>
 Tab panel {i}
 </Box>
 </TabPanel>
 ))}
 </TabPanels>
 </Tabs>
</Box>
```

### Tabs props

PropertyType
`children`

Required
`React.ReactNode`

One or more `TabList` or `TabPanels` components.

`fitted`

Optional
`boolean | undefined`

Whether or not the `TabList` should take up the entire width of its container.

`onSelectionChange`

Optional
`((event: React.Key) => void) | undefined`

Callback to be fired when a `Tab` is selected.

`selectedKey`

Optional
`React.Key | undefined`

Key of currently selected `TabPanel` if controlling the component.

`size`

Optional
`("small" | "medium" | "large") | undefined`

The size of the component.

## Tab

The `TabList` component supports the selection of content. `TabList` is made up
of a collection of `Tab` components. Each `Tab` can be uniquely identified with
a `tabKey` prop. If you render `Tab` components using a `map` function, you must
still add a `key` to satisfy [the rules of
React](https://reactjs.org/docs/lists-and-keys.html#keys).

### TabList props

PropertyType
`children`

Required
`React.ReactNode`

One or more `Tab` components.

### Tab props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`disabled`

Optional
`boolean | undefined`

Whether or not the tab should be disabled.

`id`

Optional
`string | undefined`

Native `id` attribute to use with the `Tabs` `selectedKey`.

`tabKey`

OptionalDeprecated
use the `id` prop instead.

`(React.Key | null) | undefined`

A unique identifier to use with the `Tabs` `selectedKey`.

## TabPanel

The `TabPanels` component supports displaying panels of content with Tabs.
`TabPanels` is made up of a collection of `TabPanel` components. Each `TabPanel`
can be uniquely identified with a `tabKey` prop. If you render `TabPanel`
components using a `map` function, you must still add a `key` to satisfy [the
rules of React](https://reactjs.org/docs/lists-and-keys.html#keys).

### TabPanel props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`id`

Optional
`string | undefined`

Native `id` attribute to use with the `Tabs` `selectedKey`.

`tabKey`

OptionalDeprecated
use the `id` prop instead.

`(React.Key | null) | undefined`

A unique identifier to use with the `Tabs` `selectedKey`.

## Small Tabs

Loading example...
```
<Box css={{width: 'fill'}}>
 <Tabs size="small">
 <TabList>
 {[1, 2, 3, 4, 5].map((i) => (
 <Tab key={i} tabKey={i}>
 Tab {i}
 </Tab>
 ))}
 </TabList>
 <TabPanels>
 {[1, 2, 3, 4, 5].map((i) => (
 <TabPanel key={i} tabKey={i}>
 <Box css={{backgroundColor: 'container', padding: 'large'}}>
 Tab panel {i}
 </Box>
 </TabPanel>
 ))}
 </TabPanels>
 </Tabs>
</Box>
```

## Disabled Tabs

Loading example...
```
<Box css={{width: 'fill'}}>
 <Tabs size="large" fitted>
 <TabList>
 <Tab tabKey="1">Tab</Tab>
 <Tab tabKey="2">Another Tab</Tab>
 <Tab tabKey="3" disabled>
 Disabled Tab
 </Tab>
 </TabList>
 <TabPanels>
 <TabPanel tabKey="1">
 <Box css={{backgroundColor: 'container', padding: 'large'}}>
 Test Tab Panel 1
 </Box>
 </TabPanel>
 <TabPanel tabKey="2">
 <Box css={{backgroundColor: 'container', padding: 'large'}}>
 Test Tab Panel 2
 </Box>
 </TabPanel>
 <TabPanel tabKey="3">
 <Box css={{backgroundColor: 'container', padding: 'large'}}>
 Test Tab Panel 3
 </Box>
 </TabPanel>
 </TabPanels>
 </Tabs>
</Box>
```

## Unsupported uses

Tabs don’t support conditional content within fragments unless the fragment
children are given the same key.

```
const [result, setResult] = React.useState(null);

return (
 <Box css={{width: 'fill'}}>
 <Tabs>
 <TabList>
 <Tab tabKey="1">
 <>
 {result ? (
 <Inline>View results</Inline>
 ) : (
 <Inline>Create results</Inline>
 )}
 </>
 </Tab>
 </TabList>
 <TabPanels>
 <TabPanel tabKey="1">
 <>
 {result ? (
 <Inline>Results</Inline>
 ) : (
 <Inline>No results yet</Inline>
 )}
 </>
 </TabPanel>
 </TabPanels>
 </Tabs>
 </Box>
)
```

To avoid unsupported uses of Tabs, use components instead of fragments.
Alternatively, give the children of fragments a shared `key`.

Loading example...
```
const [result, setResult] = React.useState(null);

return (
 <Box css={{width: 'fill'}}>
 <Tabs>
 <TabList>
 <Tab tabKey="1">
 <Box>
 {result ? (
 <Inline>View results</Inline>
 ) : (
 <Inline>Create results</Inline>
 )}
 </Box>
 </Tab>
 </TabList>
 <TabPanels>
 <TabPanel tabKey="1">
 <>
 {result ? (
 <Inline key="tab-panel-results">Results</Inline>
 ) : (
 <Inline key="tab-panel-no-results">No results yet</Inline>
 )}
 </>
 </TabPanel>
 </TabPanels>
 </Tabs>
 </Box>
)
```

## Controlled Tabs

Use the `selectedKey` prop from `Tabs` in combination with the `tabKey` prop
from `Tab` and `TabPanel` to create a controlled component.

Loading example...
```
const [key, setSelectedKey] = React.useState<React.Key>('c');

return (
 <Box css={{width: 'fill'}}>
 <Tabs selectedKey={key} onSelectionChange={setSelectedKey}>
 <TabList>
 {['a', 'b', 'c', 'd', 'e'].map((key) => (
 <Tab key={key} tabKey={key}>
 Tab {key}
 </Tab>
 ))}
 </TabList>
 <TabPanels>
 {['a', 'b', 'c', 'd', 'e'].map((key) => (
 <TabPanel key={key} tabKey={key}>
 <Box css={{backgroundColor: 'container', padding: 'large'}}>
 Tab panel {key}
 </Box>
 </TabPanel>
 ))}
 </TabPanels>
 </Tabs>
 </Box>
)
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [the rules of React](https://reactjs.org/docs/lists-and-keys.html#keys)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)