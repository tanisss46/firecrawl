# Capital financing applicationPrivate preview

## Show an end-to-end application flow for Capital financing.

Render a UI component for connected accounts to complete a financing
application. Connected accounts can select their offer amount and terms, view
contractual details, and submit their application.

This component is functionally similar to the [Capital financing
promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion)
component, but it invokes the application directly without including educational
or promotional content. Use it to provide a different application entry point
than the Capital financing promotion component.

SizeDesktopLocale (United States)This demo is read-only. Write operations
(like performing a refund or saving account information) are not supported for
this demo.
## Component lifecycle

### Determining when to render the component

To determine whether a connected account has an eligible financing offer, call
the Capital [list Financing
Offers](https://docs.stripe.com/api/capital/financing_offers/list) endpoint and
pass the connected account ID in the `connected_account` parameter.

If an account has no eligible financing offer, then the Capital financing
application component renders as null.

### Post-submission

If a connected account has already submitted their financing application, the
Capital financing application component renders an empty screen. We recommend
that you listen to the `onApplicationSubmitted` event to display a confirmation
screen.

## Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
financing application component by specifying `capital_financing_application` in
the `components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; embedded_connect_beta=v2;" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[capital_financing_application][enabled]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the Capital financing application component in the front end:

```
// Include this element in your HTML
const capitalFinancingApplication =
stripeConnectInstance.create('capital-financing-application');
container.appendChild(capitalFinancingApplication);
```

HTML + JSReactMethodTypeDescriptionDefault`setOnApplicationSubmitted``() =>
void`The connected account has successfully submitted their application for
financing.`setPrivacyPolicyUrl``string`Absolute URL of a page containing your
privacy
policy.`https://stripe.com/privacy``setHowCapitalWorksUrl``string`Absolute URL
of a page with information about the Capital
program.`https://docs.stripe.com/capital/how-stripe-capital-works`

## Links

- [Capital financing
promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion)
- [list Financing
Offers](https://docs.stripe.com/api/capital/financing_offers/list)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)