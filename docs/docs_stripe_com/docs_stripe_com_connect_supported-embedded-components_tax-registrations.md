# Tax registrations

## Learn how to allow connected accounts to manage their tax registrations for Stripe Tax.

The Tax registrations component gives your connected accounts control over their
tax compliance. Your connected accounts interact with this component by managing
their tax registrations directly in your platform. This component is suitable
for [software platforms](https://docs.stripe.com/tax/tax-for-platforms), which
means that your connected accounts are liable to collect taxes.

If you’re a platform integrating Stripe Tax, you must collect information about
the [registrations with tax
authorities](https://docs.stripe.com/tax/registering) of your connected accounts
in the applicable jurisdictions. Your connected accounts need to register with
their tax authorities before they add their tax registrations in your platform.
To correctly calculate and collect taxes for your platform, you must collect the
tax registrations of your connected accounts.

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
The Tax registrations component uses the [Tax Registrations
API](https://docs.stripe.com/tax/registrations-api) to display a list of tax
registrations to your connected accounts. To calculate tax on their payments in
a location, connected accounts need to add their tax registration with the Tax
registrations component. If the connected account wish to stop calculating tax
in a certain location, they can end the tax registration in the component.

## Requirements

- Your integration must follow the [software platforms
guide](https://docs.stripe.com/tax/tax-for-platforms) for [Tax on
Connect](https://docs.stripe.com/tax/connect). This means that your connected
accounts are liable to collect taxes.
- If you haven’t already, render the [Tax settings
component](https://docs.stripe.com/connect/supported-embedded-components/tax-settings).
You need both the Tax settings component and the Tax registrations component to
provide tax compliance control to your connected accounts.

## Integrate the tax registrations component

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable tax
registrations by specifying `tax_registrations` in the `components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[tax_registrations][enabled]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the tax registrations component in the frontend:

```
// Include this React component
import {
 ConnectTaxRegistrations,
 ConnectComponentsProvider,
} from "@stripe/react-connect-js";

return (
 <ConnectComponentsProvider connectInstance={stripeConnectInstance}>
 <div>
 <h2>Tax Registrations</h2>
 <ConnectTaxRegistrations
 // Optional
 // displayCountries={["US", "CA", "DE"]}
// onAfterTaxRegistrationAdded={({id: registrationId}) =>
console.log({registrationId})}
 />
 </div>
 </ConnectComponentsProvider>
);
```

HTML + JSReactMethodTypeDescriptionDefault`setDisplayCountries``string[]`Array
of [two-letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
that the connected account can [choose from for a new tax
registration](https://docs.stripe.com/api/tax/registrations/object#tax_registration_object-country_options).undefined
(all countries permitted)`setOnAfterTaxRegistrationAdded``({id: string}) =>
void`Callback executed with an object containing the newly added tax
registration IDundefined (not a required method)
## Limitations

The following features are available in the Dashboard and the API, but aren’t
currently supported by the Tax registrations component:

- Scheduling start or end dates for registrations. You can only create or end
registrations immediately.
- Specifying US state sales tax elections when creating tax registrations.

## See also

- [Tax on Connect](https://docs.stripe.com/tax/connect)
- [Tax for software platforms](https://docs.stripe.com/tax/tax-for-platforms)
- [Tax settings
component](https://docs.stripe.com/connect/supported-embedded-components/tax-settings)

## Links

- [software platforms](https://docs.stripe.com/tax/tax-for-platforms)
- [registrations with tax authorities](https://docs.stripe.com/tax/registering)
- [furever.dev](https://furever.dev)
- [Tax Registrations API](https://docs.stripe.com/tax/registrations-api)
- [Tax on Connect](https://docs.stripe.com/tax/connect)
- [Tax settings
component](https://docs.stripe.com/connect/supported-embedded-components/tax-settings)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [two-letter country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
- [choose from for a new tax
registration](https://docs.stripe.com/api/tax/registrations/object#tax_registration_object-country_options)