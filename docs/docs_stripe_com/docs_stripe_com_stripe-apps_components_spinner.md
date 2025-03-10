# Spinner component for Stripe Apps

## Use the Spinner component to indicate something is loading.

SDK version8.x9.x
To add the `Spinner` component to your app:

```
import {Spinner} from '@stripe/ui-extension-sdk/ui';
```

This is a preview of a `Spinner` component in three sizes:

Loading example...
```
<Box
 css={{
 stack: 'y',
 gap: 'medium',
 alignX: 'center',
 backgroundColor: 'surface',
 padding: 'medium',
 borderRadius: 'medium',
 }}
>
 <Spinner size="small" />
 <Spinner />
 <Spinner size="large" />
</Box>
```

### Spinner props

PropertyType
`delay`

Optional
`number | undefined`

Delay applied to animation.

`size`

Optional
`("small" | "medium" | "large") | undefined`

The size of the component.

## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)