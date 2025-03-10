# Icon component for Stripe Apps

## Display an icon graphic in a compatible format.

SDK version8.x9.x
To add the `Icon` component to your app:

```
import {Icon} from '@stripe/ui-extension-sdk/ui';
```

This is a preview of an `Icon` component:

Loading example...
```
<Icon name="addCircle" />
```

### Icon props

PropertyType
`name`

Required
`"accept" | "add" | "addCircle" | "addCircleFilled" | "api" | "apps" |
"arrowDown" | "arrowDownCircle" | "arrowExport" | "arrowExportCircle" |
"arrowIncrease" | "arrowLeft" | "arrowLeftCircle" | "arrowRight" |
"arrowRightCircle" | "arrowsInward" | "arrowsLoop" | "arrowsOutward" | "arrowUp"
| "arrowUpCircle" | "arrowUpDown" | "arrowUpRight" | "arrowUpRightCircle" |
"balance" | "bank" | "bankLightning" | "barChart" | "barGraph" | "beta" |
"billing" | "billingQuote" | "block" | "business" | "calculator" | "calendar" |
"call" | "camera" | "cancel" | "cancelCircle" | "cancelCircleFilled" | "card" |
"caretDown" | "caretLeft" | "caretRight" | "caretUp" | "cart" | "certificate" |
"change" | "changeCircle" | "charge" | "chat" | "check" | "checkCircle" |
"checkCircleFilled" | "checkmark" | "chevronDown" | "chevronDownCircle" |
"chevronLeft" | "chevronLeftCircle" | "chevronRight" | "chevronRightCircle" |
"chevronUp" | "chevronUpCircle" | "circle" | "clipboard" | "clipboardCheck" |
"clock" | "cloud" | "code" | "collapse" | "compliance" | "connectPayments" |
"convert" | "coupon" | "createCards" | "createIdentityVerification" | "cross" |
"crypto" | "customer" | "customerPortal" | "customers" | "customizeBrand" |
"data" | "dataExport" | "delete" | "deploy" | "desktop" | "dispute" |
"disputeProtection" | "doc" | "document" | "download" | "dragHandle" |
"earlyFraudWarning" | "edit" | "editCircle" | "email" | "expand" | "explorer" |
"export" | "exportCircle" | "external" | "externalTest" | "eyeClosed" |
"eyeOpen" | "fee" | "filter" | "financialActivity" | "fingerprint" | "flag" |
"folder" | "gavel" | "gift" | "globe" | "gridView" | "growth" | "guide" |
"heart" | "heartFilled" | "help" | "hide" | "history" | "home" |
"identityVerification" | "import" | "info" | "insight" | "invite" | "invoice" |
"iosShare" | "lab" | "lightBulb" | "lightningBolt" | "link" | "list" |
"listView" | "locationPin" | "lock" | "menu" | "miniPlayer" | "mobileWallet" |
"moneyMovement" | "more" | "moreCircle" | "moved" | "navClock" | "negative" |
"negativeCircle" | "negativeCircleFilled" | "new" | "next" | "note" |
"notifications" | "office" | "openLock" | "order" | "orgChart" | "overflow" |
"pane" | "panelArrowLeft" | "panelArrowRight" | "paperclip" | "passkey" |
"pause" | "payByBank" | "payment" | "paymentLink" | "payout" | "person" |
"personWithKey" | "phone" | "pieChart" | "pin" | "pinAdd" | "pinFilled" | "ping"
| "pinOutline" | "plan" | "platform" | "play" | "playCircle" | "positive" |
"previous" | "product" | "productSubscription" | "qrCode" | "recurring" |
"recurringInvoice" | "refresh" | "refreshCircle" | "refund" | "refundCircle" |
"reporting" | "reserve" | "review" | "risk" | "rocket" | "rule" | "safe" |
"sandbox" | "search" | "send" | "settings" | "share" | "shield" | "shieldCheck"
| "shoppingBag" | "show" | "signed" | "signOut" | "soundOff" | "soundOn" |
"source" | "sparkle" | "spinner" | "star" | "starFilled" | "subscription" |
"support" | "tag" | "tasks" | "terminal" | "thumbsDown" | "thumbsUp" | "topup" |
"transfer" | "trash" | "trial" | "truck" | "upload" | "usage" | "vault" |
"video" | "wallet" | "warning" | "warningCircle" | "webhook" | "website" |
"wifi" | "withdrawal"`

`css`

Optional
`Object`

Related types: [CSS](https://docs.stripe.com/stripe-apps/components/icon#css).

`size`

Optional
`("xsmall" | "small" | "medium" | "large" | "xlarge") | undefined`

### CSS

PropertyType
`fill`

Optional
[text and icon color
token](https://docs.stripe.com/stripe-apps/style#text-&-icons)

Contrasting color. See [Color](https://docs.stripe.com/stripe-apps/style#color)
for details.

If you don’t specify a fill value, the `Icon` gets its color from its parent.

## Size

Icons use the `size` prop for sizing. They can have one of five sizes:

- `xsmall`: `12px`
- `small`: `16px`
- `medium`: `20px` (default)
- `large`: `32px`
- `xlarge`: `64px`
Loading example...
```
<Icon name="business" size="xsmall" />
<Icon name="business" size="small" />
<Icon name="business" size="medium" />
<Icon name="business" size="large" />
<Icon name="business" size="xlarge" />
```

## Color and fill

You can give the `Icon` component color with the `fill` property of the `css`
prop.

Loading example...
```
<Icon name="cancelCircle" css={{fill: 'critical'}} />
```

### Default color behavior

By default, icons are the same color as the text around them.

Loading example...
```
<Inline css={{color: 'attention'}}>
 <Icon name="chat" /> new messages
</Inline>
```

## Accessibility

By default, there is an `aria-hidden` attribute on icons ([read more about
ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)). In the
rare situations the icon has semantic value to screen-reader users, you can
manually set `aria-hidden={false}`. In these situations it’s often a good idea
to add an `aria-label` as well. In general, it’s better to have text labels
rather than making visual-only icons important for a workflow.

Loading example...
```
<Icon name="addCircle" aria-hidden={false} aria-label="Add another item" />
```

## Icons in Button and Badge components

You can place an `Icon` component inside of a `Button` or `Badge` component.

Loading example...
```
<Button>
 <Icon name="chat" size="xsmall" />
 <Inline>New messages</Inline>
</Button>
<Badge type="positive">
 <Icon name="chat" size="xsmall" />
 New messages
</Badge>
```

## Icon reference

Loading example...
## See also

- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [text and icon color
token](https://docs.stripe.com/stripe-apps/style#text-&-icons)
- [Color](https://docs.stripe.com/stripe-apps/style#color)
- [read more about
ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
- [Design patterns to follow](https://docs.stripe.com/stripe-apps/patterns)
- [Style your app](https://docs.stripe.com/stripe-apps/style)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)