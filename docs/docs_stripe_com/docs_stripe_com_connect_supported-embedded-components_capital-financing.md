# Capital financingPrivate preview

## Allow a connected account to view and manage their active Capital financing.

The Capital financing component allows connected accounts to view and manage
their financing. Connected accounts can monitor repayment progress, review
transaction history, and make payments.

SizeDesktopLocale (United States)This demo is read-only. Write operations
(like performing a refund or saving account information) are not supported for
this demo.
## Component lifecycle

### No financing

For connected accounts without any financing history, the Capital financing
component displays a “No financing” message. We recommend listening to the
`onFinancingsLoaded` event to render a custom message or hide the component for
accounts with no history.

### In-review financing

When a connected account has recently submitted a financing application, the
Capital financing component shows an application tracker view. It informs the
connected account of their application status.

After an account first submits their application, you must reload this component
for it to render the application tracker.

## Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
Capital financing component by specifying `capital_financing` in the
`components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; embedded_connect_beta=v2;" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[capital_financing][enabled]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the Capital financing component in the front end:

```
// Include this element in your HTML
const capitalFinancing = stripeConnectInstance.create('capital-financing');
container.appendChild(capitalFinancing);
```

HTML +
JSReactMethodTypeDescriptionDefault`setDefaultFinancingOffer``string`[Financing
Offer](https://docs.stripe.com/api/capital/financing_offers) ID to render on
initial load of the component. By default, the component displays the active or
most recent financing.`setShowFinancingSelector``boolean`If true, render the
financing dropdown selector to allow the connected account to change the
displayed financing.`true``setOnFinancingsLoaded``({total: number}) => void`The
component loaded the connected account’s financing
history.`setSupportUrl``string`Absolute URL of your support
site.`https://support.stripe.com/``setHowCapitalWorksUrl``string`Absolute URL of
a page with information about the Capital
program.`https://docs.stripe.com/capital/how-stripe-capital-works`

## Links

- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [Financing Offer](https://docs.stripe.com/api/capital/financing_offers)