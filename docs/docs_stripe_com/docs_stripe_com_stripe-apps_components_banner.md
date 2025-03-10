# Banner component for Stripe Apps

## Use the Banner to show a variety of alerts or messages you want to make explicit to the user.

SDK version8.x9.x
To add the `Banner` component to your app:

```
import {Banner} from '@stripe/ui-extension-sdk/ui';
```

## Overview

Banners take up the width of their parent container. Banners are suitable for
important information requiring user input and persistent display.

Banners come with three preset types:

- **Default**
- **Caution**
- **Critical**

The following shows a preview of the three preset types for a banner:

Loading example...
```
<Box css={{stack: 'y', gap: 'medium', width: 'fill'}}>
 <Banner
 type="default"
 onDismiss={() => console.log('hello world')}
 title="Neutral title"
 description="A short description"
 actions={
 <Button onPress={() => console.log('hello world')}>Button</Button>
 }
 />
 <Banner
 type="caution"
 title="Check your bank details"
description="Your bank account information must be verified before receiving
payouts."
 onDismiss={() => console.log('hello world')}
 actions={
 <Box css={{stack: 'x', gap: 'small'}}>
 <Button onPress={() => console.log('hello world')}>
 Update bank account
 </Button>
 <Button onPress={() => console.log('hello world')}>
 Learn more
 </Button>
 </Box>
 }
 />
 <Banner
 type="critical"
 title="Check your bank details"
description="Your bank account information must be verified before receiving
payouts."
 actions={
 <Button onPress={() => console.log('hello world')}>
 Update bank account
 </Button>
 }
 />
</Box>
```

### Banner props

PropertyType
`actions`

Optional
`React.ReactNode`

`description`

Optional
`React.ReactNode`

`onDismiss`

Optional
`(() => void) | undefined`

`title`

Optional
`React.ReactNode`

`type`

Optional
`("default" | "caution" | "critical") | undefined`

## onDismiss

Banners have the option of adding a dismiss button—add a click handler to
`onDismiss` for the **Hide Banner** button to appear:

Loading example...
```
const [open, setOpen] = React.useState(true);

return (
 <Box css={{stack: 'y', gap: 'medium', width: 'fill'}}>
 <Button onPress={() => setOpen(!open)}>
 {open ? 'Hide' : 'Show'} Banner
 </Button>
 {open && (
 <Banner
 type="default"
 onDismiss={() => setOpen(false)}
 title="Neutral title"
 description="A short description"
 actions={
 <Button onPress={() => console.log('hello world')}>Button</Button>
 }
 />
 )}
 </Box>
)
```

## Actions

Banners also take an `actions` prop that allows you to add action buttons to the
Banner:

Loading example...
```
<Box css={{width: 'fill'}}>
 <Banner
 type="default"
 title="Check your bank details"
description="Your bank account information must be verified before receiving
payouts."
 actions={
 <Button onPress={() => console.log('hello world')}>
 Update bank account
 </Button>
 }
 />
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