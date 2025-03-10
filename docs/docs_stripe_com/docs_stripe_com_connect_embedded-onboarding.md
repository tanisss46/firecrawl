# Embedded onboarding

## Provide your connected accounts a localized onboarding form that validates data.

Embedded onboarding is a highly themeable onboarding UI with limited Stripe
branding. You embed the [Account onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
in your platform application, and your connected accounts interact with the
embedded component without ever leaving your application.

The component supports [Legal Entity
Sharing](https://docs.stripe.com/connect/legal-entity-sharing), which allows
owners of multiple Stripe accounts to share business information between them.
When they onboard an account, they can reuse that information from an existing
account instead of resubmitting it.

Embedded onboarding uses the [Accounts
API](https://docs.stripe.com/api/accounts) to read the requirements and generate
an onboarding form with robust data validation, localized for all
Stripe-supported countries. In addition, embedded onboarding handles all:

- Business types
- Configurations of company representatives
- Verification document uploading
- Identity verification and statuses
- International bank accounts
- Error states
SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.[Create an account and prefill
informationServer-side](https://docs.stripe.com/connect/embedded-onboarding#create-account)
Create a [connected account](https://docs.stripe.com/api/accounts) with the
default
[controller](https://docs.stripe.com/api/accounts/create#create_account-controller)
properties. See [design an
integration](https://docs.stripe.com/connect/design-an-integration) to learn
more about controller properties. Alternatively, you can create a connected
account by specifying an account
[type](https://docs.stripe.com/api/accounts/create#create_account-type).

With controller propertiesWith account type
```
curl -X POST https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

If you know the country for your connected account, you can provide that
information when you create the account. The country defaults to the same
country as your platform if not provided.

To request [capabilities](https://docs.stripe.com/connect/account-capabilities)
for your connected account, you can provide that information when you create the
account. Stripe’s onboarding UIs automatically collect the requirements for
those capabilities. To reduce onboarding effort, request only the capabilities
you need. If you omit capabilities, and your connected account has access to the
full Stripe Dashboard or the Express Dashboard, capabilities are automatically
requested. For accounts with access to the Express dashboard, Stripe-hosted
onboarding uses the [Configuration
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/countries)
to request capabilities based on the account’s country.

If you have information about the account holder (like their name, address, or
other details), you can proactively provide this when you
[create](https://docs.stripe.com/api/accounts/create) or
[update](https://docs.stripe.com/api/accounts/update) the account. Stripe-hosted
onboarding asks the account holder to confirm the pre-filled information before
accepting the [Connect service
agreement](https://docs.stripe.com/connect/service-agreement-types). Providing
more information through the API reduces the number of prompts and enhances the
onboarding flow for your connected account.

Additionally, if you onboard an account without its own website and your
platform provides the account with a URL, prefill the account’s
[business_profile.url](https://docs.stripe.com/api/accounts/create#create_account-business_profile-url).
If the account doesn’t have a URL, you can prefill its
[business_profile.product_description](https://docs.stripe.com/api/accounts/create#create_account-business_profile-product_description)
instead.

When testing your integration, use [test
data](https://docs.stripe.com/connect/testing) to simulate different outcomes
including identity verification, business information verification, payout
failures, and more.

[Determine the information to
collect](https://docs.stripe.com/connect/embedded-onboarding#info-to-collect)
As the platform, you must decide if you want to collect the required information
from your connected accounts upfront or incrementally. Upfront onboarding
collects the `eventually_due` requirements for the account, while incremental
onboarding only collects the `currently_due` requirements.

Upfront onboarding Incremental onboarding Advantages- Entails a single request
for information (normally)
- Creates fewer problems in receiving payouts and maintaining processing ability
- Exposes potential fraudsters or connected accounts who refuse to provide
required information later
- Onboards connected accounts quickly
- Results in higher onboarding rates
Disadvantages- Onboarding connected accounts can take longer
- Some legitimate new connected accounts might turn away due to the amount of
information required before they complete the onboarding process
- Creates a higher likelihood of disrupting business of an ongoing connected
account

To determine whether to use upfront or incremental onboarding, review the
[required
information](https://docs.stripe.com/connect/required-verification-information)
for the countries where your connected accounts are located to understand the
requirements that are eventually due. While Stripe tries to minimize any impact
to connected accounts, requirements might change over time.

For connected accounts where you’re responsible for requirement collection, you
can customize the behavior of [future
requirements](https://docs.stripe.com/connect/handle-verification-updates) using
the `collection_options` parameter. Set
[collection_options.future_requirements](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options-future_requirements)
to `include` to collect the account’s future requirements.

[Customize the policies shown to your
users](https://docs.stripe.com/connect/embedded-onboarding#customize-policies-shown-to-your-users)
Connected accounts see Stripe’s service agreement and [Privacy
Policy](https://stripe.com/privacy) during embedded onboarding. Connected
account users who haven’t [accepted Stripe’s services
agreement](https://docs.stripe.com/connect/service-agreement-types#accepting-the-correct-agreement)
must accept it on the final onboarding screen. Embedded onboarding also has a
footer with links to Stripe’s service agreement and [Privacy
Policy](https://stripe.com/privacy).

For connected accounts where the platform is responsible for requirement
collection, you have additional options to customize the onboarding flow, as
outlined below.

### Handle service agreement acceptance on your own

If you’re a platform onboarding connected accounts where you’re responsible for
requirement collection, you can [collect Terms of Service
acceptance](https://docs.stripe.com/connect/updating-service-agreements#tos-acceptance)
using your own process instead of using the embedded account onboarding
component. If using your own process, the final onboarding screen only asks your
connected accounts to confirm the information they entered, and you must secure
their acceptance of Stripe’s service agreement.

Embedded onboarding still has links to the terms of service (for example, in the
footer) that you can replace by [linking to your own agreements and privacy
policy](https://docs.stripe.com/connect/embedded-onboarding#link-to-your-own-agreements-and-privacy-policy).

### Link to your agreements and privacy policy

Connected accounts see the Stripe service agreement and [Privacy
Policy](https://stripe.com/privacy) throughout embedded onboarding. For the
connected accounts where you’re responsible for requirement collection, you can
replace the links with your own agreements and policy. Follow the instructions
to [incorporate the Stripe services
agreement](https://docs.stripe.com/connect/updating-service-agreements#adding-stripes-service-agreement-to-your-terms-of-service)
and [link to the Stripe Privacy
Policy](https://docs.stripe.com/connect/updating-service-agreements#disclosing-how-stripe-processes-user-data).

[Integrate the account onboarding
componentServer-sideClient-side](https://docs.stripe.com/connect/embedded-onboarding#integrate-account-onboarding-component)
Create an [Account Session](https://docs.stripe.com/api/account_sessions) by
specifying the ID of the connected account and `account_onboarding` as the
component to enable.

## Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable account
onboarding by specifying `account_onboarding` in the `components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[account_onboarding][enabled]"=true \
-d "components[account_onboarding][features][external_account_collection]"=true
```

After creating the Account Session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the Account onboarding component in the front end:

```
// Include this element in your HTML
const accountOnboarding = stripeConnectInstance.create('account-onboarding');
accountOnboarding.setOnExit(() => {
 console.log('User exited the onboarding flow');
});
container.appendChild(accountOnboarding);

// Optional: make sure to follow our policy instructions above
// accountOnboarding.setFullTermsOfServiceUrl('{{URL}}')
// accountOnboarding.setRecipientTermsOfServiceUrl('{{URL}}')
// accountOnboarding.setPrivacyPolicyUrl('{{URL}}')
// accountOnboarding.setSkipTermsOfServiceCollection(false)
// accountOnboarding.setCollectionOptions({
// fields: 'eventually_due',
// futureRequirements: 'include',
// })
// accountOnboarding.setOnStepChange((stepChange) => {
// console.log(`User entered: ${stepChange.step}`);
// });
```

HTML +
JSReactMethodTypeDescriptionDefault`setFullTermsOfServiceUrl``string`Absolute
URL to your [full terms of
service](https://docs.stripe.com/connect/service-agreement-types#full)
agreement.[Stripe’s full service
agreement](https://stripe.com/connect-account/legal/full)`setRecipientTermsOfServiceUrl``string`Absolute
URL to your [recipient terms of
service](https://docs.stripe.com/connect/service-agreement-types#recipient)
agreement.[Stripe’s recipient service
agreement](https://stripe.com/connect-account/legal/recipient)`setPrivacyPolicyUrl``string`Absolute
URL to your privacy policy.[Stripe’s privacy
policy](https://stripe.com/privacy)`setSkipTermsOfServiceCollection``string`If
true, embedded onboarding skips terms of service collection and you must
[collect terms acceptance
yourself](https://docs.stripe.com/connect/updating-service-agreements#indicating-acceptance).false`setCollectionOptions``{
fields: 'currently_due' | 'eventually_due', future_requirements: 'omit' |
'include' }`Customizes collecting `currently_due` or `eventually_due`
requirements and controls whether to include [future
requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements).
Specifying `eventually_due` collects both `eventually_due` and `currently_due`
requirements.`{fields: 'currently_due', futureRequirements:
'omit'}``setOnExit``() => void`The connected account has exited the onboarding
process`setOnStepChange``({step}: StepChange) => void`The connected account has
navigated from one step to another within the onboarding process. See the [step
change object](https://docs.stripe.com/connect/embedded-onboarding#the-object)
for a full reference and
[restrictions](https://docs.stripe.com/connect/embedded-onboarding#restrictions).
To use this component to set up new accounts:

- Create a [connected account](https://docs.stripe.com/api/accounts). You can
prefill information on the account object in this API call.
- [Initialize Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
using the ID of the connected account.
- Include the `account-onboarding` element to show the onboarding flow to the
connected account.
- Listen for the `exit` event emitted from this component. Stripe sends this
event when the connected account exits the onboarding process.
- When `exit` triggers, retrieve account details to check the status of
[details_submitted](https://docs.stripe.com/api/accounts/object#account_object-details_submitted),
[charges_enabled](https://docs.stripe.com/api/accounts/object#account_object-charges_enabled),
[payouts_enabled](https://docs.stripe.com/api/accounts/object#account_object-payouts_enabled),
and other capabilities. If all required capabilities are enabled, you can take
the account to the next step of your flow.

#### The `stepchange` object

Every time the connected account navigates from one step to another in the
onboarding process, a `stepchange` object is passed to the step change handler
with the following properties.

NameTypeExample value`step``string` See the [possible step
values](https://docs.stripe.com/connect/embedded-onboarding#step-values)`business_type`The
unique reference to an onboarding step.
##### Restrictions

- The `stepchange` object is only for analytics.
- Steps can appear in any order and can be repeated.
- Possible `step` values can change at any time.

#### Step Values

Each page in onboarding has a unique step name. This `step` is an exhaustive
list of pages the user could see in the onboarding process. These values can
change at any time without notice.

StepsDescription`stripe_user_authentication`[User
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
includes a popup to a Stripe-owned window. The connected account must
authenticate before they can continue their workflow.`risk_intervention`Guides
the connected account to resolve risk-related
requirements.`legal_entity_sharing`Connected accounts can optionally [reuse
existing information](https://support.stripe.com/questions/legal-entity-sharing)
when onboarding new accounts.`business_type`Sets the business type of the
connected account. In certain cases the connected account can also set their
country.`business_details`Collects information related to the connected
account’s business.`business_verification`Collects a proof of entity document
establishing the business’ entity ID number, such as the company’s articles of
incorporation. Or allows users to correct wrongly entered information related to
the entity.`business_bank_account_ownership_verification`Collects documents
needed to verify that bank account information, such as the legal owner’s name
and account number, match the information on the user’s Stripe
account.`business_documents`Collects other documents and verification
requirements related to the business.`representative_details`Collects
information about the account representative.`representative_document`Collects a
government-issued ID verifying the existence of the account
representative.`representative_additional_document`Collects an additional
document to verifying the details of the account
representative.`legal_guardian_details`Collects the legal guardians consent for
accounts opened by minors.`owners`Collects information about the [beneficial
owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
of a company.`directors`Collects information about the
[directors](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
of a company.`executives`Collects information about the
[executives](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
of a company.`confirm_owners`Allows connected accounts to attest that the
beneficial owner information provided to Stripe is both current and
correct.`risa_compliance_survey`Answers questions concerning the [Revised
Installment Sales Act](https://stripe.com/guides/installment-sales-act). (only
for Japan)`treasury_and_card_issuing_terms_of_service`Collects [Treasury and
Card Issuing](https://docs.stripe.com/treasury) terms of service when requesting
those capabilities.`external_account`Collects the [external
account](https://docs.stripe.com/api/accounts/object#account_object-external_accounts)
of the connected account.`support_details`Collects information that helps
customers recognize the connected accounts business. This support information
may be visible in payment statements, invoices, and receipts.`climate`Allows a
connected account to opt into [Stripe
Climate](https://docs.stripe.com/climate).`tax`Allows a connected account to opt
into [Stripe Tax](https://docs.stripe.com/tax).`summary`Final review step of
onboarding. The connected account can update entered information from this step.
The terms of service and privacy URL is displayed in this
screen.`summary_risk`From the summary step, a connected account can update
information related to risk requirements.`summary_business_type`From the summary
step, a connected account can update information related to their business
type.`summary_business`From the summary step, a connected account can update
information related to their business.`summary_support`From the summary step, a
connected account can update information related to their businesses public
facing information.`summary_persons`From the summary step, a connected account
can update information about each person on their
account.`summary_external_account`From the summary step, a connected account can
update information related to their [external
account](https://docs.stripe.com/api/accounts/object#account_object-external_accounts).`summary_tax`From
the summary step, a connected account can update information related to their
[Stripe Tax](https://docs.stripe.com/tax)
integration.`summary_tax_identification_form`From the summary step, a connected
account can update information related to their W8/W9 certified tax information.
This is shown when Stripe must collect W8/W9 information.`summary_climate`From
the summary step, a connected account can update information related to their
[Stripe Climate](https://docs.stripe.com/climate) integration.[Handle new
requirements becoming
dueServer-side](https://docs.stripe.com/connect/embedded-onboarding#handle-new-requirements-becoming-due)
Set up your integration to [listen for
changes](https://docs.stripe.com/connect/handling-api-verification#verification-process)
to account requirements. You can test handling new requirements (and how they
might disable charges and payouts) with the [test mode trigger
cards](https://docs.stripe.com/connect/testing#trigger-cards).

Based on your application’s verification requirements, send the connected
account back through onboarding when it has `currently_due` or `eventually_due`
requirements. Use these signals to determine when it’s necessary to re-initiate
onboarding for a connected account.

You don’t need to worry about determining which requirements are missing.
Onboarding collects the necessary information. For example, if there’s a typo
preventing verification, onboarding prompts the connected account to upload an
identity document (such as a Driver’s License in the United States). If any
information is missing, onboarding requests it.

Stripe notifies you about any [upcoming requirements
updates](https://support.stripe.com/user/questions/onboarding-requirements-updates)
that affect your connected accounts. You can proactively collect this
information by reviewing the [future
requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements)
for your accounts.

### Handle verification errors

Listen to the
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
event. If the account contains any `currently_due` fields when the
`current_deadline` arrives, the corresponding functionality is disabled and
those fields are added to `past_due`.

Let your accounts remediate their verification requirements by directing them to
the [Account onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding).

[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
event

If `requirements.currently_due` contains fields

Direct account to onboarding in time to finish before
[current_deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline)

No action required

If `requirements.past_due` contains fields

Account possibly disabled; direct it to onboarding

Render the [Account onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)

YesNo
### Disable Stripe user authentication

When using embedded onboarding, [Stripe user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
is enabled by default. You can use
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features-disable_stripe_user_authentication)
to remove this behavior.

We recommend implementing two-factor authentication or equivalent security
measures as a [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs).
For account configurations that support this feature, such as Custom, you assume
liability for connected accounts if they can’t pay back [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability).

## See also

- [Get started with Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Customize embedded
components](https://docs.stripe.com/connect/customize-connect-embedded-components)

## Links

- [Account onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
- [Legal Entity Sharing](https://docs.stripe.com/connect/legal-entity-sharing)
- [Accounts API](https://docs.stripe.com/api/accounts)
- [furever.dev](https://furever.dev)
-
[controller](https://docs.stripe.com/api/accounts/create#create_account-controller)
- [design an integration](https://docs.stripe.com/connect/design-an-integration)
- [type](https://docs.stripe.com/api/accounts/create#create_account-type)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)
- [Configuration
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/countries)
- [create](https://docs.stripe.com/api/accounts/create)
- [update](https://docs.stripe.com/api/accounts/update)
- [Connect service
agreement](https://docs.stripe.com/connect/service-agreement-types)
-
[business_profile.url](https://docs.stripe.com/api/accounts/create#create_account-business_profile-url)
-
[business_profile.product_description](https://docs.stripe.com/api/accounts/create#create_account-business_profile-product_description)
- [test data](https://docs.stripe.com/connect/testing)
- [required
information](https://docs.stripe.com/connect/required-verification-information)
- [future
requirements](https://docs.stripe.com/connect/handle-verification-updates)
-
[collection_options.future_requirements](https://docs.stripe.com/api/account_links/create#create_account_link-collection_options-future_requirements)
- [Privacy Policy](https://stripe.com/privacy)
- [accepted Stripe’s services
agreement](https://docs.stripe.com/connect/service-agreement-types#accepting-the-correct-agreement)
- [collect Terms of Service
acceptance](https://docs.stripe.com/connect/updating-service-agreements#tos-acceptance)
- [incorporate the Stripe services
agreement](https://docs.stripe.com/connect/updating-service-agreements#adding-stripes-service-agreement-to-your-terms-of-service)
- [link to the Stripe Privacy
Policy](https://docs.stripe.com/connect/updating-service-agreements#disclosing-how-stripe-processes-user-data)
- [Account Session](https://docs.stripe.com/api/account_sessions)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [full terms of
service](https://docs.stripe.com/connect/service-agreement-types#full)
- [Stripe’s full service
agreement](https://stripe.com/connect-account/legal/full)
- [recipient terms of
service](https://docs.stripe.com/connect/service-agreement-types#recipient)
- [Stripe’s recipient service
agreement](https://stripe.com/connect-account/legal/recipient)
- [collect terms acceptance
yourself](https://docs.stripe.com/connect/updating-service-agreements#indicating-acceptance)
- [future
requirements](https://docs.stripe.com/api/accounts/object#account_object-future_requirements)
-
[details_submitted](https://docs.stripe.com/api/accounts/object#account_object-details_submitted)
-
[charges_enabled](https://docs.stripe.com/api/accounts/object#account_object-charges_enabled)
-
[payouts_enabled](https://docs.stripe.com/api/accounts/object#account_object-payouts_enabled)
- [User
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
- [reuse existing
information](https://support.stripe.com/questions/legal-entity-sharing)
- [beneficial
owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
- [Revised Installment Sales
Act](https://stripe.com/guides/installment-sales-act)
- [Treasury and Card Issuing](https://docs.stripe.com/treasury)
- [external
account](https://docs.stripe.com/api/accounts/object#account_object-external_accounts)
- [Stripe Climate](https://docs.stripe.com/climate)
- [Stripe Tax](https://docs.stripe.com/tax)
- [listen for
changes](https://docs.stripe.com/connect/handling-api-verification#verification-process)
- [test mode trigger
cards](https://docs.stripe.com/connect/testing#trigger-cards)
- [upcoming requirements
updates](https://support.stripe.com/user/questions/onboarding-requirements-updates)
-
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
-
[current_deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline)
-
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features-disable_stripe_user_authentication)
- [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs)
- [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability)
- [Get started with Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Customize embedded
components](https://docs.stripe.com/connect/customize-connect-embedded-components)