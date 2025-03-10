# Badge component for Stripe Apps

## Use badges to indicate the state of an item or object.

SDK version8.x9.x
Unlike [buttons](https://docs.stripe.com/stripe-apps/components/button), badges
are read-only and don’t perform any actions, such as `onPress` events. Use
badges to indicate the state of an item or object in your applications user
interface.

To add the `Badge` component to your app:

```
import {Badge} from '@stripe/ui-extension-sdk/ui';
```

The following types of badges are available:

- **Neutral**: Neutral label, no action required, everything is working as
expected
- **Info**: Identifies an object or action with an important attribute or a key
state
- **Positive**: Positive, neutral and important outcome or category, no action
required
- **Negative**: Negative, important outcome or category, no action required
- **Warning**: Needs immediate action, optional to resolve
- **Urgent**: Needs immediate action, strong requirement to resolve
Loading example...
```
<Badge>Neutral</Badge>

<Badge type="info">Info</Badge>

<Badge type="positive">Positive</Badge>

<Badge type="negative">Negative</Badge>

<Badge type="warning">Warning</Badge>

<Badge type="urgent">Urgent</Badge>
```

### Badge props

PropertyType
`children`

Required
`React.ReactNode`

The contents of the component.

`type`

Optional
`("neutral" | "urgent" | "warning" | "negative" | "positive" | "info") |
undefined`

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [buttons](https://docs.stripe.com/stripe-apps/components/button)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)