# Set up Capital embedded componentsPrivate preview

## Embed a financing flow into your website.

Use Capital embedded components to integrate financing directly into your
application. You can use these prebuilt components to:

- Manage the user application process, display financing offers, and handle
repayment logic
- Promote and present offer details in a user-friendly and compliant way
- Customize the styling to provide a white-labeled integration that fits your
application’s interface

To learn more, see [Get Started with Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components).

![Example UI using Capital Financing embedded
component](https://b.stripecdn.com/docs-statics-srv/assets/embedded-component-ui-example.bde9ace29803254898f43a96da6ae9d2.png)

An example website that features the Capital financing component

Capital provides three key embedded components:

ComponentDescription[Capital financing
promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion)Promote
new offers and educate your customers about eligibility and offer terms. Render
the promotion component to upsell your financing program, and provide an entry
point for your customers to apply for an offer.[Capital
financing](https://docs.stripe.com/connect/supported-embedded-components/capital-financing)Display
active financing offers, repayment progress, transaction history, and facilitate
user’s payments toward their financing. Embed the financing component in your
application’s Capital dashboard or reporting page.[Capital financing
application](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application)Host
and manage the complete application flow for your customers. Use the standalone
application component only if you want to offer a more customized frontend.
Otherwise, the [financing promotion
component](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion)
enables your customers to complete the application flow in a
dialog.[Setup](https://docs.stripe.com/capital/embedded-component-integration#setup)
Capital components are currently in private preview and require the use of beta
SDKs.

Install a beta version of the Stripe SDKs to create account sessions for private
preview components:

- [Ruby](https://github.com/stripe/stripe-ruby/#beta-sdks) `>=13.4.0-beta.4`
- [Python](https://github.com/stripe/stripe-python/#beta-sdks) `>=11.5.0b3`
- [PHP](https://github.com/stripe/stripe-php/#beta-sdks) `>=16.5.0-beta.3`
- [Node](https://github.com/stripe/stripe-node/#beta-sdks) `>=17.6.0-beta.3`
- [.NET](https://github.com/stripe/stripe-dotnet#beta-sdks) `>=47.3.0-beta.3`
- [Java](https://github.com/stripe/stripe-java#beta-sdks) `>=28.3.0-beta.3`
- [Go](https://github.com/stripe/stripe-go#beta-sdks) `>=81.3.0-beta.3`

Use the beta version of the Stripe’s client-side libraries to render private
preview components:

npmGitHub
Install the library:

`npm install --save @stripe/connect-js@preview`
If you’re using React in your application:

`npm install --save @stripe/react-connect-js@preview`
To test your embedded component integration, use [Capital test mode
tooling](https://docs.stripe.com/capital/test-mode-tooling) in the
[Dashboard](https://dashboard.stripe.com/connect/capital) to create a test
financing offer.

[Create an Account
Session](https://docs.stripe.com/capital/embedded-component-integration#create-account-session)
Create an [Account Session](https://docs.stripe.com/api/account_sessions/create)
to give your connected accounts access to an embedded component. To use the
Capital embedded components, make sure to include the
`capital_financing_promotion`, `capital_financing_application`, and
`capital_financing` in the components parameter of your request.

Capital components are in private preview and require the inclusion of the beta
header on the Account Session creation request: `embedded_connect_beta=v2;`

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; embedded_connect_beta=v2;" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[capital_financing][enabled]"=true \
 -d "components[capital_financing_promotion][enabled]"=true \
 -d "components[capital_financing_application][enabled]"=true
```

[Render the Capital
component](https://docs.stripe.com/capital/embedded-component-integration#render-component)
After creating the Account Session, initialize a `StripeConnectInstance` using
the returned client secret. To learn more about how to initialize and configure
Connect.js, see [Load and Initialize
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components?platform=web#load-and-initialize-connect.js).

After you initialize `StripeConnectInstance`, you can render the Capital
components on the frontend. Each component features custom events and callback
functions, allowing you to tailor them to fit your website’s specific needs. The
components also offer the option to provide custom URLs for a fully
white-labeled integration for your customers.

```
// Include these elements
const capitalFinancing = stripeConnectInstance.create('capital-financing');
const capitalFinancingPromotion =
stripeConnectInstance.create('capital-financing-promotion');
const capitalFinancingApplication =
stripeConnectInstance.create('capital-financing-application');
container.appendChild(capitalFinancing);
container.appendChild(capitalFinancingPromotion);
container.appendChild(capitalFinancingApplication);
```

[Style and customize the
components](https://docs.stripe.com/capital/embedded-component-integration#style-component)
You have the ability to customize embedded components to align with your
company’s branding. For detailed instructions on how to adjust the UI to match
your brand’s design, see [Customizing Connect Embedded
Components](https://docs.stripe.com/connect/customize-connect-embedded-components).

## See also

- [Capital
financing](https://docs.stripe.com/connect/supported-embedded-components/capital-financing)
- [Capital financing
promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion)
- [Capital financing
application](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application)

## Links

- [Get Started with Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Capital financing
promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion)
- [Capital
financing](https://docs.stripe.com/connect/supported-embedded-components/capital-financing)
- [Capital financing
application](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application)
- [Ruby](https://github.com/stripe/stripe-ruby/#beta-sdks)
- [Python](https://github.com/stripe/stripe-python/#beta-sdks)
- [PHP](https://github.com/stripe/stripe-php/#beta-sdks)
- [Node](https://github.com/stripe/stripe-node/#beta-sdks)
- [.NET](https://github.com/stripe/stripe-dotnet#beta-sdks)
- [Java](https://github.com/stripe/stripe-java#beta-sdks)
- [Go](https://github.com/stripe/stripe-go#beta-sdks)
- [Capital test mode tooling](https://docs.stripe.com/capital/test-mode-tooling)
- [Dashboard](https://dashboard.stripe.com/connect/capital)
- [Account Session](https://docs.stripe.com/api/account_sessions/create)
- [Load and Initialize
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components?platform=web#load-and-initialize-connect.js)
- [Customizing Connect Embedded
Components](https://docs.stripe.com/connect/customize-connect-embedded-components)