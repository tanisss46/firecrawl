# Chip component for Stripe Apps

## Use chips to display and allow users to manipulate values.

SDK version8.x9.x
To add the `Chip` component to your app:

```
import {Chip, ChipList} from '@stripe/ui-extension-sdk/ui';
```

This is a preview of several `Chip` components in a `ChipList` component with
different property configurations:

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

### ChipList props

PropertyType
`children`

Required
`React.ReactNode`

One or more `Chip` components.

`direction`

Optional
`("row" | "row-reverse") | undefined`

### Chip props

PropertyType
`label`

Optional
`string | undefined`

A string that uniquely identifies the `Chip` amongst other `Chips` that may be
presented alongside it. If this property is present without a `value`, the
`Chip` will be rendered in the “suggested” style.

`onAddSuggestion`

Optional
`(() => void) | undefined`

The function to be called when the user clicks a “suggested” `Chip` in order to
activate it.

`onClose`

Optional
`(() => void) | undefined`

The function to be called when the user clicks the icon to remove a `Chip`.

`onDropdown`

Optional
`(() => void) | undefined`

The function to be called when the user clicks the right side of an active
`Chip` in order to edit the selected value.

`value`

Optional
`(string | string[]) | undefined`

The currently selected value of a `Chip`.

## Suggested chip

To suggest to the user with a `plus` icon that they add something represented by
a chip, pass a callback function to the `onAddSuggestion` property.

Loading example...
```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <Chip
 label="Date"
 onAddSuggestion={() => {
 console.log('Suggestion function triggered');
 }}
 />
</Box>
```

## Chip with dropdown

If you want to allow the user to edit the value of a chip after they’ve made
their initial selection, provide an `onDropdown` callback function to open a
selection interface needed for making edits.

Loading example...
```
const [open, setOpen] = React.useState(false);

return (
 <Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 stack: 'y',
 gap: 'medium',
 }}
 >
 <Chip
 label="Status"
 value="Succeeded"
 onDropdown={() => setOpen(!open)}
 onClose={() => {
 console.log('Close function triggered');
 }}
 />
 {open && (
 <Box
 css={{
 font: 'caption',
 borderRadius: 'medium',
 backgroundColor: 'container',
 margin: 'small',
 padding: 'medium',
 color: 'secondary',
 }}
 >
 Dropdown contents
 </Box>
 )}
 </Box>
)
```

## Representing multiple values

When you populate the `Chip` component’s `value` property with an array of
values, they’re listed within the chip.

Loading example...
```
<Box
 css={{
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <Chip
 label="Status"
 value={['Refunded', 'Succeeded']}
 onDropdown={() => {
 console.log('Dropdown function triggered');
 }}
 onClose={() => {
 console.log('Close function triggered');
 }}
 />
</Box>
```

## Presenting chips in a list

In many cases, chips aren’t presented on their own—they’re alongside other
chips. The `ChipList` component handles the appropriate spacing and wrapping of
chips in a list, and also provides for convenient keyboard navigation of chips
using the right and left arrow keys.

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
 value="jenny.rosen@stripe.com"
 onClose={() => {
 console.log('Closed jenny.rosen');
 }}
 />
 <Chip
 value="usr_0As2kXSWDS1lTZsH5agB"
 onClose={() => {
 console.log('Closed usr_0As2kXSWDS1lTZsH5agB');
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

## Non-closeable chip

When a `Chip` represents a required value, it can be useful to present a chip
without an `add` or `cancel` icon. Exclude the `onAddSuggestion` and `onClose`
callbacks to present users with a non-closeable chip.

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
 label="Amount"
 value="$10"
 onDropdown={() => {
 console.log('Dropdown function triggered');
 }}
 />
 <Chip
 label="Age"
 value="18-24"
 onDropdown={() => {
 console.log('Dropdown function triggered');
 }}
 />
 </ChipList>
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