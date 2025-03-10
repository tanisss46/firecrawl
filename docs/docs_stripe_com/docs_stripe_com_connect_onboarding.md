# Choose your onboarding configuration

## Learn about the different options for onboarding your connected accounts.

Stripe offers several different onboarding options:

- **Stripe-hosted onboarding**: Your connected accounts go through the
onboarding flow in a Stripe-hosted web form.
- **Embedded onboarding**: You embed the Account onboarding component directly
in your application and your connected accounts go through the onboarding flow
without leaving your application.
- **API onboarding**: You use Stripe’s APIs to build your own customized
onboarding UI.

Choose the onboarding option that best fits your business. Stripe recommends
using Stripe-hosted onboarding or Embedded onboarding. These options
automatically update to handle changing requirements when they apply to a
connected account.

[STRIPE-HOSTED
ONBOARDING](https://docs.stripe.com/connect/hosted-onboarding)[EMBEDDED
ONBOARDING](https://docs.stripe.com/connect/embedded-onboarding)[API
ONBOARDING](https://docs.stripe.com/connect/api-onboarding)INTEGRATION
EFFORTMinimal, go live quicklyMore effort, go live quicklyMost effort, can delay
going liveCUSTOMIZATIONStripe-branded with limited platform branding[Highly
themeable](https://docs.stripe.com/connect/customize-connect-embedded-components)
with limited Stripe brandingFull control over your own UIAUTOMATIC UPDATES FOR
NEW COMPLIANCE REQUIREMENTSImmediateImmediateRequires integration changesSUPPORT
NEW COUNTRIES WITHOUT INTEGRATION CHANGESSUPPORT LEGAL ENTITY SHARINGFLOW
LOGICLimited controlLimited controlFull controlIDEAL FORPlatforms that want
Stripe to handle onboardingPlatforms that want a branded onboarding flow within
their applicationPlatforms that require full control of the onboarding flow and
have the resources to build and maintain it
## Stripe-hosted onboarding

Stripe-hosted onboarding is a web form hosted by Stripe with your brand’s name,
color, and icon. Stripe-hosted onboarding uses the [Accounts
API](https://docs.stripe.com/api/accounts) to read the requirements and generate
an onboarding form with robust data validation and is localized for all
Stripe-supported countries.

Stripe-hosted onboarding supports [Legal Entity
Sharing](https://docs.stripe.com/connect/legal-entity-sharing), which allows
owners of multiple Stripe accounts to share certain business information between
them. When they onboard an account, they can reuse that information from an
existing account instead of resubmitting it.

Use Stripe-hosted onboarding if you want Stripe to handle onboarding with little
effort from your platform.

[Learn more about Stripe-hosted
onboarding](https://docs.stripe.com/connect/hosted-onboarding)

## Embedded onboarding

Embedded onboarding is a highly themeable onboarding UI with limited Stripe
branding. Your platform embeds the [Account onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
in your application, and your connected accounts interact with the embedded
component without ever leaving your application. Embedded onboarding uses the
[Accounts API](https://docs.stripe.com/api/accounts) to read the requirements
and generate an onboarding form with robust data validation and is localized for
all Stripe-supported countries.

Embedded onboarding supports [Legal Entity
Sharing](https://docs.stripe.com/connect/legal-entity-sharing), which allows
owners of multiple Stripe accounts to share certain business information between
them. When they onboard an account, they can reuse that information from an
existing account instead of resubmitting it.

With embedded onboarding, you get a customized onboarding flow without the
complexity and maintenance associated with updating your onboarding integration
as compliance requirements change.

[Learn more about Embedded
onboarding](https://docs.stripe.com/connect/embedded-onboarding)

## API onboarding

You use the [Accounts API](https://docs.stripe.com/api/accounts) to build an
onboarding flow and handle identity verification, localization, and error
handling for each country your connected accounts onboard in. Stripe can be
completely invisible to the account holder. Your platform is responsible for all
interactions with your connected accounts and for collecting all the information
needed to verify each account. Verification requirements are updated as laws and
regulations change around the world. You must plan on reviewing and updating
onboarding requirements at least every six months.

Stripe doesn’t recommend this option unless you’re fully committed to the
operational complexity required to build and maintain an API onboarding flow.
For a customized onboarding flow, Stripe strongly recommends embedded
onboarding.

[Learn more about API
onboarding](https://docs.stripe.com/connect/api-onboarding)

## Links

- [STRIPE-HOSTED ONBOARDING](https://docs.stripe.com/connect/hosted-onboarding)
- [EMBEDDED ONBOARDING](https://docs.stripe.com/connect/embedded-onboarding)
- [API ONBOARDING](https://docs.stripe.com/connect/api-onboarding)
- [Highly
themeable](https://docs.stripe.com/connect/customize-connect-embedded-components)
- [Accounts API](https://docs.stripe.com/api/accounts)
- [Legal Entity Sharing](https://docs.stripe.com/connect/legal-entity-sharing)
- [Account onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)