# Tooltip component for Stripe Apps

## Use Tooltips to provide additional contextual information about a particular element or subject.

SDK version8.x9.x
To add the `Tooltip` component to your app:

```
import {Tooltip} from '@stripe/ui-extension-sdk/ui';
```

This is a preview of two `Tooltip` components with each type of `label`:

Loading example...
```
<Tooltip
 type="description"
 trigger={
 <Button type="primary" disabled onPress={undefined}>
 Pay out to bank
 </Button>
 }
>
 You have no available balance to pay out. You can create payouts when
 you've accumulated a positive balance again.
</Tooltip>

<Tooltip
 type="label"
 trigger={
 <Button onPress={undefined}>
 <Icon name="notifications" />
 </Button>
 }
>
 Notifications
</Tooltip>
```

Tooltips are overlays that appear when a user hovers or focuses a target
element. Use Tooltips to provide additional contextual information about a
particular element or subject. You can use tooltips as either **descriptions**
or **labels**.

Avoid putting any interactive content such as links within a Tooltip, because
keyboard users won’t be able to access it.

### Tooltip props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`trigger`

Required
`React.ReactElement`

The target element that should be used as the `Tooltip` trigger.

`delay`

Optional
`number | undefined`

How much time in milliseconds to wait before showing the `Tooltip` on hover.

`placement`

Optional
`("bottom" | "bottom left" | "bottom right" | "bottom start" | "bottom end" |
"top" | "top left" | "top right" | "top start" | "top end" | "left" | "left top"
| "left bottom" | "start" | "start top" | "start bottom" | "right" | "right top"
| "right bottom" | "end" | "end top" | "end bottom") | undefined`

How the `Tooltip` should be placed relative to the trigger element.

`type`

Optional
`("label" | "description") | undefined`

The style variant of the `Tooltip`.

## Placement

You can place tooltips in one of four primary directions and further align them
along a secondary axis, resulting in a total of 12 possible placement options
relative to the `trigger`. The placement automatically adjusts as necessary to
ensure the Tooltip remains visible within the viewport.

Loading example...
```
const SpacerComponent = () => <Box css={{width: 28, height: 28}}>{null}</Box>;
const Row = ({children}: {children: React.ReactNode}) => (
 <Box
 css={{
 stack: 'x',
 wrap: 'wrap',
 gap: 'small',
 distribute: 'space-between',
 }}
 >
 {children}
 </Box>
);

return (
 <Box
 css={{
 padding: 'xxlarge',
 stack: 'y',
 }}
 >
 <Row>
 <SpacerComponent />
 <Tooltip
 placement="top left"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "top left"
 </Tooltip>
 <Tooltip
 placement="top"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "top"
 </Tooltip>
 <Tooltip
 placement="top right"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "top right"
 </Tooltip>
 <SpacerComponent />
 </Row>
 <Row>
 <Tooltip
 placement="left top"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "left top"
 </Tooltip>
 <SpacerComponent />
 <SpacerComponent />
 <SpacerComponent />
 <Tooltip
 placement="right top"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "right top"
 </Tooltip>
 </Row>
 <Row>
 <Tooltip
 placement="left"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "left"
 </Tooltip>
 <SpacerComponent />
 <SpacerComponent />
 <SpacerComponent />
 <Tooltip
 placement="right"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "right"
 </Tooltip>
 </Row>
 <Row>
 <Tooltip
 placement="left bottom"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "left bottom"
 </Tooltip>
 <SpacerComponent />
 <SpacerComponent />
 <SpacerComponent />
 <Tooltip
 placement="right bottom"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "right bottom"
 </Tooltip>
 </Row>
 <Row>
 <SpacerComponent />

 <Tooltip
 placement="bottom left"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "bottom left"
 </Tooltip>
 <Tooltip
 placement="bottom"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "bottom"
 </Tooltip>
 <Tooltip
 placement="bottom right"
 trigger={
 <Button onPress={undefined}>
 <Icon name="info" />
 </Button>
 }
 >
 "bottom right"
 </Tooltip>
 <SpacerComponent />
 </Row>
 </Box>
)
```

## Delay

Tooltips have a short delay for when they appear after hovering over their
trigger element. You can control the amount of time it takes for a Tooltip to
become active on hover using the `delay` prop. Tooltips always appear
immediately when their trigger element receives keyboard focus.

Loading example...
```
<Tooltip delay={0} trigger={<Button onPress={undefined}>Immediate</Button>}>
 I showed up immediately.
</Tooltip>
```

Tooltips appear immediately on hover while another Tooltip is already active.

Loading example...
```
<Tooltip trigger={<Button onPress={undefined}>Hover me</Button>}>
 I showed up after a delay.
</Tooltip>

<Tooltip trigger={<Button onPress={undefined}>Then me</Button>}>
 I showed up immediately.
</Tooltip>
```

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)