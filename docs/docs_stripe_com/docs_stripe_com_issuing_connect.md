# Set up an Issuing and Connect integration

## Learn how to issue cards on connected accounts.

[Stripe Connect](https://docs.stripe.com/connect) provides Stripe Issuing
platforms with foundational infrastructure to manage funds flows and compliance
requirements. In a Connect integration, the platform account makes API calls on
behalf of the connected accounts.

## When to use Connect

If you need to issue cards for users that aren’t directly employed by your
business, set up Stripe Connect for your Issuing integration. For example, a
business building a new expense management product for small businesses can
integrate with Connect. Each small business that uses the expense management
product is set up as a connected account.

After you set up and onboard connected accounts, your customers can support
their card spend by funding their Issuing balance from their external bank
account (or, in certain cases, your customers’ spend can be supported by your
platform Issuing balance). Your customers can also create cardholders and cards
and set up spending controls.

[Create connected accounts with Issuing
capabilities](https://docs.stripe.com/issuing/connect#create-connected-accounts-with-issuing-capabilities)
To issue cards, each business entity must use a connected account. Issuing only
supports connected accounts that don’t use a Stripe-hosted Dashboard, and where
your platform is responsible for requirements collection and loss liability,
also known as a Custom connected account. Learn how to [create connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
that work with Issuing. All accounts must request the `card_issuing` and
`transfers` [account
capabilities](https://docs.stripe.com/connect/account-capabilities).

#### Private preview

Enabling Issuing on non-custom connected accounts is a new feature. Email
[issuing-beta-feedback@stripe.com](mailto:issuing-beta-feedback@stripe.com) to
request access.

#### Create an account

Create a new connected account [through the
Dashboard](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#creating-accounts)
or using the API with [create
Account](https://docs.stripe.com/api/accounts/create).

#### Start with test mode accounts

Test mode connected accounts can’t receive or spend real money and can’t be used
in live mode, but they’re identical in configuration and functionality.

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d country=US \
 -d "capabilities[transfers][requested]"=true \
 -d "capabilities[card_issuing][requested]"=true \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[fees][payer]"=application \
 -d "controller[losses][payments]"=application \
 -d "controller[requirement_collection]"=application
```

#### Enable Issuing on existing connected accounts

If your platform already has a Connect integration with connected accounts, you
can request Issuing on those accounts [through the
Dashboard](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#updating-capabilities)
or through the API.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "capabilities[card_issuing][requested]"=true
```

#### Issuing and Treasury accounts

If your platform already has [connected
accounts](https://docs.stripe.com/connect/accounts), make sure they have a
supported configuration for Issuing or Treasury. Issuing only supports connected
accounts that don’t use a Stripe-hosted Dashboard, and where your platform is
responsible for requirements collection and loss liability, also known as a
Custom connected account. If this isn’t the case, you must create new accounts
to use Issuing or Treasury. You can see your existing account’s configuration on
the [Connect accounts](https://dashboard.stripe.com/connect/accounts/overview)
page in your Dashboard.

You can also use the API to retrieve the account information and verify that the
`capabilities` property has the Issuing capability requested. The capability
won’t be active until all the requirements are fulfilled.

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

```
{
 "object": "list",
 "data": [
 {
 "id": "acct_1234",
 "object": "account",
 ...
 "capabilities": {
 "card_issuing": "inactive",
 "transfers": "active",
 },
 ...
 "controller": {
 "stripe_dashboard": {
 "type": "none"
 },
 "fees": {
 "payer": "application"
 },
 "losses": {
 "payments": "application"
 },
 "is_controller": true,
 "type": "application",
 "requirement_collection": "application"
 },
 },
 ...
 ]
}
```

[Start the identity verification
process](https://docs.stripe.com/issuing/connect#onboard-connected-accounts)
After you create a connected account, you need to provide more information about
the account holder. The [capability
object](https://docs.stripe.com/api/capabilities/object) has a `requirements`
hash that contains `currently_due` [identity verification
requirements](https://docs.stripe.com/connect/handling-api-verification). The
user must provide the details itemized in the `requirements` hash to enable
Issuing capabilities.

If you create an Account object in test mode and want to bypass onboarding
requirements to test functionality, use the [Accounts update
API](https://docs.stripe.com/api/accounts/update) to provide [test
values](https://docs.stripe.com/connect/testing-verification) that fulfill all
the requirements.

Depending on the [business
type](https://docs.stripe.com/connect/identity-verification#business-type), the
user provides details about the individual, company, non-profit organization, or
government entity (Stripe Treasury doesn’t support government entities).

Choose one of the following onboarding options:

Stripe-hosted onboardingEmbedded onboardingAPI onboarding
[Stripe-hosted onboarding](https://docs.stripe.com/connect/hosted-onboarding) is
a web form hosted by Stripe with your brand’s name, color, and icon.
Stripe-hosted onboarding uses the [Accounts
API](https://docs.stripe.com/api/accounts) to read the requirements and generate
an onboarding form with robust data validation and is localized for all
Stripe-supported countries.

Before using Connect Onboarding, you must provide the name, color, and icon of
your brand in the Branding section of your [Connect settings
page](https://dashboard.stripe.com/test/settings/connect).

You can use hosted onboarding to allow connected accounts to link an
`external_account` (which is required for payouts) by enabling it through your
[Connect Onboarding settings](https://dashboard.stripe.com/settings/connect).

To create an onboarding link for the connected account, use the [Account Links
API](https://docs.stripe.com/api/account_links/create).

```
curl https://api.stripe.com/v1/account_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 --data-urlencode refresh_url="https://example.com/reauth" \
 --data-urlencode return_url="https://example.com/return" \
 -d type=account_onboarding
```

#### Caution

For security reasons, don’t email, text, or send account link URLs directly to
your connected account. We recommend that you distribute the account link URL
from within your platform’s application, where their account is authenticated.

The response you receive includes the `url` parameter containing the link for
your connected account to onboard to your platform.

```
{
 "object": "account_link",
 "created": 1612927106,
 "expires_at": 1612927406,
 "url": "https://connect.stripe.com/setup/s/…"
}
```

## Collect and verify required information

When you create a connected account and request capabilities, the response
returns a list of all required information. To see the requirements specific to
a capability, [retrieve the account
capability](https://docs.stripe.com/api/capabilities/retrieve) and look at
`requirements.past_due`.

#### Note

If you don’t intend to allow your connected accounts to [pay out an Issuing
balance to an external
account](https://docs.stripe.com/issuing/connect/funding#pay-out-an-issuing-balance),
then you can ignore requirements past_due for `external_account`.

Here are the requirements to activate the `card_issuing` capability:

FIELDPARAMETERADDITIONAL NOTESLegal name`company.name` Business
address`company.address.*`The address can’t be a P.O. box, a Highway Contract
(HC) box, or a private mailbox. It must be in the US for US-based accounts, UK
for UK-based accounts, or a European country for Europe-based accounts.Business
type`business_type`The business type can be company, individual, or
non-profit.Company tax ID`company.tax_id` Phone`company.phone` Merchant category
code`business_profile.mcc` URL`business_profile.url`If the user doesn’t have a
URL, you can provide the `business_profile.product_description`
instead.Estimated worker count`business_profile.estimated_worker_count`An
estimated upper bound of your workers (employees, contractors, vendors, and so
on) currently working for the business.Annual
revenue`business_profile.annual_revenue`The user’s gross annual revenue for its
preceding fiscal year.
Terms of service

`settings.card_issuing.tos_acceptance.ip`
`settings.card_issuing.tos_acceptance.date`

Record the connected accounts [accepting the Issuing terms of
service](https://docs.stripe.com/issuing/connect/tos_acceptance).

#### Representatives and beneficial owners

Companies and non-profit organizations require additional onboarding information
for representatives (that is, directors [`relationship.director`] and executives
[`relationship.executive`]), and any beneficial owner that owns more than 25% of
the company (`relationship.owner`). Each connected account must have at least
one representative, who’s usually an executive or director, depending on where
the account is located. They must be able to certify that the information
provided is correct. Beneficial owners aren’t required.

Learn more about [beneficial owners, representatives, and
directors](https://support.stripe.com/questions/beneficial-owner-and-director-definitions).

FIELDPARAMETERADDITIONAL NOTESLegal name`first_name`, `last_name` Date of
birth`dob.day`, `dob.month`, `dob.year` Residential address`address.*`The
address can’t be a P.O. box, a Highway Contract (HC) box, or a private mailbox.
It must be in the US for US-based accounts.Email`email` Title`title`Examples for
the title include CEO or Director.Phone`phone` US Tax ID or last 4 digits of
SSN`id_number`Accounts of US-based platforms must provide a social security
number, and non-US tax ID numbers or ID documents aren’t accepted as a
substitute. You can provide either the full nine-digit social security number
(`id_number`) or the last four digits (`ssn_last_4`) initially. If verification
with the last four digits is unsuccessful, then the full nine-digit number is
required.ID document scan`verification.document`Provide an identity document if
the full nine-digit social security number can’t be verified. See the
[acceptable verification documents by
country](https://docs.stripe.com/connect/handling-api-verification#acceptable-verification-documents).[Handle
new requirements coming due and changes to the capability
status](https://docs.stripe.com/issuing/connect#handle-new-requirements-changes)
Sometimes after providing all required information, an account might need to
provide additional details or documents. These new requirements appear in the
[requirements.eventually_due](https://docs.stripe.com/api/accounts/object#account_object-requirements-eventually_due)
array or in
[requirements.currently_due](https://docs.stripe.com/api/accounts/object#account_object-requirements-currently_due).
Set up your integration to listen for changes to account requirements by [using
webhooks](https://docs.stripe.com/connect/handling-api-verification#verification-process).

If the capability is already `active` and the account doesn’t satisfy new
requirements due on that capability before the [current
deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline),
the capability becomes `inactive` until the requirements are satisfied.

### Document uploads

If an account’s information can’t be verified, Stripe might require a document
to verify the identity of a person (for example, a Passport) or to verify
information about the legal entity (for example, a letter from the tax
authority). To satisfy document requirements, platforms can send the user to
Connect Onboarding (where they’ll be [prompted to upload the
document](https://docs.stripe.com/connect/custom/hosted-onboarding#new-reqs-due)),
or collect the document from the account in another interface and [upload it
through the
API](https://docs.stripe.com/connect/handling-api-verification#upload-a-file).

### Failure to verify identity within 29 days of the initial application

After an account submits all the [required
information](https://docs.stripe.com/issuing/connect#required-verification-information)
for Issuing and accepts the Issuing terms of service, Stripe considers the
application complete. If we can’t verify an account’s information, the
capability remains `inactive` until the account provides additional information
or uploads a document.

If the account remains `inactive` 29 days after completing the application, you
must send an email notice to the account informing them that we couldn’t verify
their identity ([see the
template](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices?issuing-notices-sender=stripe#spend-card-application-rejected-for-failure-to-verify-identity)).

Stripe monitors for completed applications with unverified identities, and takes
the following action after 29 days in live mode and after 1 hour in [test
mode](https://docs.stripe.com/connect/testing):

- [Generates an account
notice](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices?issuing-notices-sender=stripe#events-that-require-a-customer-notice)
- Clears the [Issuing terms of service acceptance
hash](https://docs.stripe.com/api/accounts/object#account_object-settings-card_issuing-tos_acceptance)
so terms acceptance becomes a `currently_due` requirement

You can submit a new application at any time by updating the business
information and recording a new acceptance of Issuing’s terms.

Stripe recommends that you present the terms of service as the last step of
onboarding, which allows you to track the timing of application completion by
referring to the term’s [acceptance
date](https://docs.stripe.com/api/accounts/object#account_object-settings-card_issuing-tos_acceptance-date).

### Terms of service violations

If Stripe identifies a connect account that has violated Stripe’s terms of
service, Stripe sets the Issuing capability on the account to `inactive`,
deactivates any cards, and notifies the account (see [the email
template](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices?issuing-notices-sender=stripe#account-closed-by-stripe-for-terms-of-service-violation)).
This might happen when an account’s cards are used in relation to [prohibited or
restricted businesses](https://stripe.com/legal/restricted-businesses), such as
illegal activities, gambling, firearms, adult content, or cryptocurrencies, or
in relation to [prohibited activities for
Issuing](https://stripe.com/legal/restricted-businesses#additional-product-specific-prohibitions),
such as consumer spending, primarily international use, lending, or other
abusive or noncompliant use.

### Accounts inactive for more than 395 days

Stripe disables issuing on accounts that haven’t completed any card transactions
in the past 13 months (395 days). For accounts with additional capabilities,
Stripe only disables Issuing if there have also been no payments or Treasury
transactions in the prior 395 days, and the Treasury balance is 9.99 USD or
less. When Issuing is disabled for inactivity, the Connect account’s
card_issuing capability status changes to `inactive` and the capability
requirements show a
[disabled_reason](https://docs.stripe.com/api/capabilities/object#capability_object-requirements-disabled_reason)
of `rejected.inactivity`. Learn more about [managing inactive
accounts](https://support.stripe.com/questions/issuing-managing-inactive-connect-accounts)
with Issuing.

[Create cardholders and
cards](https://docs.stripe.com/issuing/connect#create-cardholders-and-cards)
A Cardholder object represents an individual or business entity that you can
issue cards to. Each cardholder needs to be associated with a connected account
to be issued a virtual or physical card. One connected account can have many
cardholders.

Learn more about [Cardholders and
cards](https://docs.stripe.com/issuing/connect/cardholders-and-cards).

[Add funds](https://docs.stripe.com/issuing/connect#Add-funds)
The Issuing balance is separate from the connected account’s main balance. When
issued cards are used for transactions, they draw from the Issuing balance.

Before an issued card can be used for transactions, you must first allocate
funds to the connected account’s [Issuing
balance](https://docs.stripe.com/issuing/funding/balance) associated with the
card. An Issuing Balance holds funds reserved for the card and is safely
separated from earnings, [payouts](https://docs.stripe.com/payouts), and funds
from other Stripe products. Learn how to [fund connected
accounts](https://docs.stripe.com/issuing/connect/funding) for Issuing.

Platform
Platform Issuing Balance

Connected account
Issuing Balance

Cardholder

Card

BankBank
## Use the Dashboard for Issuing with Connect

View the connected accounts on your platform and create new accounts from the
[Connect page](https://dashboard.stripe.com/connect/accounts/overview) in the
Dashboard. An account might appear as `restricted` in the Dashboard if
requirements are `past_due` for any of the requested capabilities (including
`transfers`). You can ignore this if `card_issuing` is active.

You can also do the following from the dashboard:

- View account activity for a selected account.
- Edit business and personal details for a selected account.
- Create cardholders, cards, or test authorizations on the account. To do so,
click the overflow menu (), select **View Dashboard as (account name)**, and
then navigate to **Card issuing**.
- View program details for a selected account. Follow the above steps to **View
Dashboard as (account name)**, then navigate to **Settings**, the **Issuing**
section, and click [Card
programs](https://dashboard.stripe.com/settings/issuing/card-programs).

You can also access the Issuing page for a connected account directly by
navigating to this URL and replacing `{{CONNECT_ACCOUNT_ID}}` with the
appropriate value:
`https://dashboard.stripe.com/{{CONNECT_ACCOUNT_ID}}/issuing/overview`

As the platform, only you can view the Dashboard on behalf of your connected
accounts. Your connected accounts won’t have a Stripe username or password, or
access to the Dashboard.

[OptionalSet up spending
controls](https://docs.stripe.com/issuing/connect#set-up-spending-controls)

## Links

- [Stripe Connect](https://docs.stripe.com/connect)
- [create connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
- [account capabilities](https://docs.stripe.com/connect/account-capabilities)
- [through the
Dashboard](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#creating-accounts)
- [create Account](https://docs.stripe.com/api/accounts/create)
- [through the
Dashboard](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#updating-capabilities)
- [connected accounts](https://docs.stripe.com/connect/accounts)
- [Connect accounts](https://dashboard.stripe.com/connect/accounts/overview)
- [capability object](https://docs.stripe.com/api/capabilities/object)
- [identity verification
requirements](https://docs.stripe.com/connect/handling-api-verification)
- [Accounts update API](https://docs.stripe.com/api/accounts/update)
- [test values](https://docs.stripe.com/connect/testing-verification)
- [business
type](https://docs.stripe.com/connect/identity-verification#business-type)
- [Stripe-hosted onboarding](https://docs.stripe.com/connect/hosted-onboarding)
- [Accounts API](https://docs.stripe.com/api/accounts)
- [Connect settings page](https://dashboard.stripe.com/test/settings/connect)
- [Connect Onboarding settings](https://dashboard.stripe.com/settings/connect)
- [Account Links API](https://docs.stripe.com/api/account_links/create)
- [https://connect.stripe.com/setup/s/…](https://connect.stripe.com/setup/s/…)
- [retrieve the account
capability](https://docs.stripe.com/api/capabilities/retrieve)
- [pay out an Issuing balance to an external
account](https://docs.stripe.com/issuing/connect/funding#pay-out-an-issuing-balance)
- [accepting the Issuing terms of
service](https://docs.stripe.com/issuing/connect/tos_acceptance)
- [beneficial owners, representatives, and
directors](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
- [acceptable verification documents by
country](https://docs.stripe.com/connect/handling-api-verification#acceptable-verification-documents)
-
[requirements.eventually_due](https://docs.stripe.com/api/accounts/object#account_object-requirements-eventually_due)
-
[requirements.currently_due](https://docs.stripe.com/api/accounts/object#account_object-requirements-currently_due)
- [using
webhooks](https://docs.stripe.com/connect/handling-api-verification#verification-process)
- [current
deadline](https://docs.stripe.com/api/accounts/object#account_object-requirements-current_deadline)
- [prompted to upload the
document](https://docs.stripe.com/connect/custom/hosted-onboarding#new-reqs-due)
- [upload it through the
API](https://docs.stripe.com/connect/handling-api-verification#upload-a-file)
- [required
information](https://docs.stripe.com/issuing/connect#required-verification-information)
- [see the
template](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices?issuing-notices-sender=stripe#spend-card-application-rejected-for-failure-to-verify-identity)
- [test mode](https://docs.stripe.com/connect/testing)
- [Generates an account
notice](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices?issuing-notices-sender=stripe#events-that-require-a-customer-notice)
- [Issuing terms of service acceptance
hash](https://docs.stripe.com/api/accounts/object#account_object-settings-card_issuing-tos_acceptance)
- [acceptance
date](https://docs.stripe.com/api/accounts/object#account_object-settings-card_issuing-tos_acceptance-date)
- [the email
template](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices?issuing-notices-sender=stripe#account-closed-by-stripe-for-terms-of-service-violation)
- [prohibited or restricted
businesses](https://stripe.com/legal/restricted-businesses)
- [prohibited activities for
Issuing](https://stripe.com/legal/restricted-businesses#additional-product-specific-prohibitions)
-
[disabled_reason](https://docs.stripe.com/api/capabilities/object#capability_object-requirements-disabled_reason)
- [managing inactive
accounts](https://support.stripe.com/questions/issuing-managing-inactive-connect-accounts)
- [Cardholders and
cards](https://docs.stripe.com/issuing/connect/cardholders-and-cards)
- [Issuing balance](https://docs.stripe.com/issuing/funding/balance)
- [payouts](https://docs.stripe.com/payouts)
- [fund connected accounts](https://docs.stripe.com/issuing/connect/funding)
- [Card programs](https://dashboard.stripe.com/settings/issuing/card-programs)