# ButtonGroup component for Stripe Apps

## Use ButtonGroup to handle the layout for multiple buttons and collapse them into an overflow menu when space is limited.

SDK version8.x9.x
To add the `ButtonGroup` component to your app:

```
import {ButtonGroup} from '@stripe/ui-extension-sdk/ui';
```

Loading example...
```
<ButtonGroup>
 <Button
 onPress={() => {
 console.log('Filter');
 }}
 >
 Filter
 </Button>
 <Button
 onPress={() => {
 console.log('Export');
 }}
 >
 Export
 </Button>
 <Button
 type="primary"
 onPress={() => {
 console.log('Save');
 }}
 >
 Save
 </Button>
</ButtonGroup>
```

### ButtonGroup props

PropertyType
`children`

Required
`React.ReactNode`

One or more `Button` components.

`collapse`

Optional
`("auto" | "none") | undefined`

Controls whether or not `Buttons` within the group collapse when there isn’t
enough space to display them without overflowing.

`direction`

Optional
`("row" | "column") | undefined`

Controls which axis the `ButtonGroup` should span.

`menuTrigger`

Optional
`React.ReactNode`

Allows overriding the trigger element used for an overflow menu. Must be a
component that supports press events.

## Overflow collapsing

Button groups responsively adapt to the space available in their container by
collapsing buttons into an overflow menu. Primary buttons collapse after any
other buttons, and larger buttons collapse first.

Loading example...
```
<Box css={{width: 'fill'}}>
 <ButtonGroup>
 <Button
 onPress={() => {
 console.log('Filter');
 }}
 >
 Filter
 </Button>
 <Button
 onPress={() => {
 console.log('Export');
 }}
 >
 Export
 </Button>
 <Button
 type="primary"
 onPress={() => {
 console.log('Save');
 }}
 >
 Save
 </Button>
 </ButtonGroup>
</Box>
```

### Disabling collapse behavior

If you want to turn off collapsing behavior, you can specify the
`collapse="none"` prop value.

Loading example...
```
<Box css={{width: 'fill'}}>
 <ButtonGroup collapse="none">
 <Button
 onPress={() => {
 console.log('Filter');
 }}
 >
 Filter
 </Button>
 <Button
 onPress={() => {
 console.log('Export');
 }}
 >
 Export
 </Button>
 <Button
 type="primary"
 onPress={() => {
 console.log('Save');
 }}
 >
 Save
 </Button>
 </ButtonGroup>
</Box>
```

## Customizing the overflow menu trigger

You can replace the default overflow menu trigger with any element that supports
`onPress` events. To adhere to best practices, remember to add an appropriate
`aria-label` to your trigger element if it doesn’t contain descriptive text.

Loading example...
```
<Box css={{width: 'fill'}}>
 <ButtonGroup menuTrigger={<Button>More actions</Button>}>
 <Button
 onPress={() => {
 console.log('Filter');
 }}
 >
 Filter
 </Button>
 <Button
 onPress={() => {
 console.log('Export');
 }}
 >
 Export
 </Button>
 <Button
 type="primary"
 onPress={() => {
 console.log('Save');
 }}
 >
 Save
 </Button>
 </ButtonGroup>
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