# Tax settings

## Learn how to allow connected accounts to set up Stripe Tax.

The Tax settings component allows your connected accounts to [set up Stripe
Tax](https://docs.stripe.com/tax/set-up) in your platform. Connected accounts
can change their head office address and [preset tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#product-tax-code)
with this component. This component is suitable for [software
platforms](https://docs.stripe.com/tax/tax-for-platforms), which means that your
connected accounts are liable to collect taxes.

To calculate taxes on payments of your connected accounts you have to collect
four data points of information:

- The head office address
- The type of product the connected account sells
- The address of the customer
- The registrations of the connected account with the tax authorities

The tax settings component helps you to collect the first two pieces of
information of your connected accounts with minimal integration effort.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
The embedded tax settings component uses the [Tax Settings
API](https://docs.stripe.com/tax/settings-api) to display the head office
address and [preset tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#product-tax-code)
to your connected accounts.

## Requirements

- Your integration must follow the [software platforms
guide](https://docs.stripe.com/tax/tax-for-platforms) for [Tax on
Connect](https://docs.stripe.com/tax/connect). This means that your connected
accounts are liable to collect taxes.
- After integrating the Tax settings component, render the [Tax registrations
component](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations)
to collect tax registration information of your connected accounts. This is a
requirement for Tax to calculate tax in a specific location.

## Integrate the tax settings component

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable tax
settings by specifying `tax_settings` in the `components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[tax_settings][enabled]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the tax settings component in the frontend:

```
// Include this React component
import {
 ConnectTaxSettings,
 ConnectComponentsProvider,
} from "@stripe/react-connect-js";

return (
 <ConnectComponentsProvider connectInstance={stripeConnectInstance}>
 <div>
 <h2>Tax Settings</h2>
 <ConnectTaxSettings
 // Optional
 // displayHeadOfficeCountries={["US", "CA", "DE"]}
// onTaxSettingsUpdated={({id: settingsId}) => console.log({settingsId})}
 // hideProductTaxCodeSelector
 />
 </div>
 </ConnectComponentsProvider>
);
```

HTML +
JSReactMethodTypeDescriptionDefault`setDisplayHeadOfficeCountries``string[]`Array
of [two-letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
that the connected account can choose from for their head office.undefined (all
countries permitted)`setOnTaxSettingsUpdated``({id: string}) => void`Callback
executed with an object containing the newly updated tax settings IDundefined
(not a required method)`setHideProductTaxCodeSelector`BooleanSet to true to hide
the tab where users select a default Product Tax Codefalse (users can by default
set a default PTC)
To give your connected accounts full control over their tax compliance, you need
to integrate the tax registrations component as well. Please follow the guide
for [tax compliance for software
platforms](https://docs.stripe.com/tax/tax-for-platforms). The guide also covers
how to calculate and collect the taxes and help your connected accounts to
report their taxes.

## See also

- [Tax on Connect](https://docs.stripe.com/tax/connect)
- [Tax for software platforms](https://docs.stripe.com/tax/tax-for-platforms)
- [Tax registrations
component](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations)

## Links

- [set up Stripe Tax](https://docs.stripe.com/tax/set-up)
- [preset tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#product-tax-code)
- [software platforms](https://docs.stripe.com/tax/tax-for-platforms)
- [furever.dev](https://furever.dev)
- [Tax Settings API](https://docs.stripe.com/tax/settings-api)
- [Tax on Connect](https://docs.stripe.com/tax/connect)
- [Tax registrations
component](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [two-letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)