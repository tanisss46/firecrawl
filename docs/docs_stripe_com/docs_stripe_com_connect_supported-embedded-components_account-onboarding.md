# Account onboarding

## Use the Account onboarding Connect embedded component.

WebiOS
The Account onboarding component uses the [Accounts
API](https://docs.stripe.com/api/accounts) to read requirements and generate an
onboarding form that’s localized for all Stripe-supported countries and that
validates data. In addition, Embedded onboarding handles all business types,
various configurations of company representatives, document uploads, identity
verification, and verification statuses. For more information, see [Embedded
onboarding](https://docs.stripe.com/connect/embedded-onboarding).

SizeDesktopLocale (United States)This demo is read-only with limited
functionality. Visit [furever.dev](https://furever.dev/) for a fully functional
demo.
## Requirements collection options

With embedded onboarding, you can control the collection of `currently_due` or
`eventually_due` requirements, along with the inclusion of [future
requirements](https://docs.stripe.com/connect/handle-verification-updates). You
can customize this behavior by using the `collectionOptions` attribute when
integrating the account onboarding component.

## External account collection

Use the
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features-external_account_collection)
feature to control whether the component collects external account information.
This parameter is enabled by default, and only platforms responsible for
collecting updated information when requirements are due or change (including
Custom accounts) can disable it. When `external_account_collection` is enabled,
[user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
is required. You can opt out of Stripe user authentication with the
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features-disable_stripe_user_authentication)
parameter.

## Disable Stripe user authentication

Use the
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features-disable_stripe_user_authentication)
feature to control whether the component requires Stripe user authentication.
The default value is the opposite of the
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features-external_account_collection)
value. For example, if you don’t set `external_account_collection`, it defaults
to true and `disable_stripe_user_authentication` defaults to false. This value
can only be true for accounts where `controller.requirement_collection` is
`application`.

We recommend implementing 2FA or equivalent security measures as a [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs).
For account configurations that support this feature, such as Custom accounts,
you assume liability for connected accounts if they can’t pay back [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability).

## Customize policies shown to your users

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
policy](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding#link-to-your-own-agreements-and-privacy-policy).

### Link to your agreements and privacy policy

Connected accounts see the Stripe service agreement and [Privacy
Policy](https://stripe.com/privacy) throughout embedded onboarding. For the
connected accounts where you’re responsible for requirement collection, you can
replace the links with your own agreements and policy. Follow the instructions
to [incorporate the Stripe services
agreement](https://docs.stripe.com/connect/updating-service-agreements#adding-stripes-service-agreement-to-your-terms-of-service)
and [link to the Stripe Privacy
Policy](https://docs.stripe.com/connect/updating-service-agreements#disclosing-how-stripe-processes-user-data).

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
change
object](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding#the-object)
for a full reference and
[restrictions](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding#restrictions).
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
values](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding#step-values)`business_type`The
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
[Stripe Climate](https://docs.stripe.com/climate) integration.

## Links

- [Accounts API](https://docs.stripe.com/api/accounts)
- [Embedded onboarding](https://docs.stripe.com/connect/embedded-onboarding)
- [furever.dev](https://furever.dev)
- [future
requirements](https://docs.stripe.com/connect/handle-verification-updates)
-
[external_account_collection](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features-external_account_collection)
- [user
authentication](https://docs.stripe.com/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)
-
[disable_stripe_user_authentication](https://docs.stripe.com/api/account_sessions/create#create_account_session-components-account_onboarding-features-disable_stripe_user_authentication)
- [best
practice](https://docs.stripe.com/connect/risk-management/best-practices#prevent-account-take-overs)
- [negative
balances](https://docs.stripe.com/connect/risk-management/best-practices#decide-your-approach-to-negative-balance-liability)
- [Privacy Policy](https://stripe.com/privacy)
- [accepted Stripe’s services
agreement](https://docs.stripe.com/connect/service-agreement-types#accepting-the-correct-agreement)
- [collect Terms of Service
acceptance](https://docs.stripe.com/connect/updating-service-agreements#tos-acceptance)
- [incorporate the Stripe services
agreement](https://docs.stripe.com/connect/updating-service-agreements#adding-stripes-service-agreement-to-your-terms-of-service)
- [link to the Stripe Privacy
Policy](https://docs.stripe.com/connect/updating-service-agreements#disclosing-how-stripe-processes-user-data)
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