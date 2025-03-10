# Testing Stripe Connect

## Before going live, test your Connect integration for account creation, identity verification, and payouts.

Use testing to make sure your [Connect](https://docs.stripe.com/connect)
integration handles different flows correctly. Use [test
mode](https://docs.stripe.com/test-mode) to simulate live mode while taking
advantage of Stripe-provided special tokens to use in your tests. Take a look at
our [payments testing guide](https://docs.stripe.com/testing) for more
information on testing charges, disputes, and so on.

## Create test accounts

You can create multiple test accounts and use any [account
type](https://docs.stripe.com/connect/accounts) or [controller
properties](https://docs.stripe.com/connect/migrate-to-controller-properties)
you might need (for example, representing multiple countries).

You can create test accounts using the [Accounts
API](https://docs.stripe.com/api/accounts/create) or in the [Stripe
Dashboard](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#creating-accounts).

Use `000-000` as the SMS code when prompted for test accounts.

## Test the OAuth flow

You can test your OAuth integration with connected accounts that use a
Stripe-hosted dashboard using your test mode `client_id`.

Your test mode `client_id` is `ca_FkyHCg7X8mlvCUdMDao4mMxagUfhIwXb`. You can
find this in your [Connect OAuth
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/oauth).

Your test mode `client_id` allows you to:

- Set your `redirect_uri` to a non-HTTPS URL
- Set your `redirect_uri` to **localhost**
- Force-skip the account form instead of having to fill out an entire account
application (Stripe Dashboard accounts only)
- Get test access tokens for connected accounts

To test the [OAuth](https://docs.stripe.com/connect/oauth-standard-accounts)
flow, create a new account after clicking the OAuth link. You can also test
connecting an existing Stripe account only if the email is different from your
platform account.

## Identity verification

After creating a test connected account, you can use tokens to test different
verification statuses to make sure you’re handling different requirements and
account states. You can use the following tokens to test verification with test
accounts.

### Test dates of birth

Use these dates of birth (DOB) to trigger certain verification conditions.

DOBType`1901-01-01`Successful verification. Any other DOB results in
unsuccessful verification.`1902-01-01`Successful, immediate verification. The
verification result is returned directly in the response, not as part of a
[webhook](https://docs.stripe.com/webhooks) event.`1900-01-01`This DOB triggers
an Office of Foreign Assets Control (OFAC) alert.
### Test addresses

Use these addresses for `line1` to trigger certain verification conditions. You
must pass in legitimate values for the `city`, `state`, and `postal_code`
arguments.

TokenType`address_full_match`​Successful
verification.`address_no_match`Unsuccessful
verification.`address_line1_no_match`Unsuccessful verification from partial
address match.
### Test personal ID numbers

Use these personal ID numbers for
[individual.id_number](https://docs.stripe.com/api/accounts/create#create_account-individual-id_number)
or the
[id_number](https://docs.stripe.com/api/persons/create#create_person-id_number)
attribute on the `Person` object to trigger certain verification conditions.

NumberType`000000000`Successful verification. 0000 also works for SSN last 4
verification.`111111111`Unsuccessful verification (identity
mismatch).`222222222`Successful, immediate verification. The verification result
is returned directly in the response, not as part of a
[webhook](https://docs.stripe.com/webhooks) event.
### Test identity documents

For testing, use test images or file tokens instead of uploading your own test
IDs. For details, refer to [Uploading a
file](https://docs.stripe.com/connect/handling-api-verification#upload-a-file).

### Test document images

You can use a [verified
image](https://d37ugbyn3rpeym.cloudfront.net/docs/identity/success.png) that
causes the user to be automatically marked `verified`. You can use an
[unverified
image](https://d37ugbyn3rpeym.cloudfront.net/docs/identity/failed.png) that
causes the user to be automatically marked `unverified`.

#### Note

Test images take precedence over test ID numbers. If you upload a verified
image, verification succeeds, even if you also provide an unsuccessful test ID
value. Similarly, an unverified image automatically fails verification
regardless of the value of other test artifacts.

### Test file tokens

Use these file tokens to trigger certain identity verification conditions.

TokenType`file_identity_document_success`Uses the verified image and marks that
document requirement as satisfied.`file_identity_document_failure`Uses the
unverified image and marks that document requirement as not satisfied.
## Business information verification

### Business address validation

In some countries, the business address associated with your connected account
must be validated before charges, [payouts](https://docs.stripe.com/payouts), or
both can be enabled on the connected account.

### Test business addresses

Use these addresses for `line1` to trigger certain validation conditions. You
must pass in legitimate values for the `city`, `state`, and `postal_code`
arguments.

Make sure you start with an address token that has the least permissive
validation condition you want to test for. This is because you can’t use an
address token that has a more restrictive validation condition than the previous
token used. For example, if you provided `address_full_match` to have both
charges and payouts enabled, you can’t disable payouts or charges afterward by
changing the token to an invalid one. You can work around this by creating a new
account with the relevant token.

TokenType`address_full_match`​Both charges and payouts are enabled on the
account.`address_no_match`​Only charges are enabled on the account. Since
validation failed on the `line1` attribute, it becomes listed again in the
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
hash.`address_line1_no_match`Neither charges nor payouts are enabled on the
account. Since validation failed, the address attributes become listed again in
the
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
hash.
### Test business tax IDs

Use these business tax ID numbers for
[company.tax_id](https://docs.stripe.com/api/accounts/create#create_account-company-tax_id)
to trigger certain verification conditions. The test behavior might change
depending on the Connected Account countries and the regulations in those
countries. Depending on the country’s regulation, a valid tax document can mark
tax ID verified in these countries.

NumberType`000000000`Successful verification.`000000001`Successful verification
as a non-profit.`111111111`Unsuccessful verification (identity
mismatch).`111111112`Unsuccessful verification (tax ID not
issued).`222222222`Successful, immediate verification. The verification result
is returned directly in the response, not as part of a
[webhook](https://docs.stripe.com/webhooks) event.
### Test directorship verification

Stripe performs directorship verification by comparing the list of directors on
the `Account` object against a list retrieved from local registries. If the
country requires it, you can trigger verification for an `Account` object by
using these tokens for the
[person.first_name](https://docs.stripe.com/api/persons/object#person_object-first_name)
attribute and setting the
[person.relationship.director](https://docs.stripe.com/api/persons/object#person_object-relationship-director)
attribute to true.

TokenType`mismatch_director`Unsuccessful verification of director due to a
mismatched name. This can trigger a `verification_directors_mismatch`
verification error.`missing_director`Unsuccessful verification due to directors
missing on the account. This can trigger a `verification_missing_directors`
verification error.`extraneous_director`Unsuccessful verification due to too
many directors on the account. This can trigger a
`verification_extraneous_directors` verification error.
The verification errors can trigger if multiple directors on the `Account`
object use these magic tokens.

### Test company name verification

Trigger company name verification for an `Account` object by using this token
for the
[company.name](https://docs.stripe.com/api/accounts/object#account_object-company-name)
attribute.

TokenType`mismatch_business_name`Unsuccessful verification due to a mismatched
business name.`disallowed_name`Unsuccessful verification due to a generic or
well-known business name.`match_name_relationships`Successful verification of
the business name.`match_name_only`Unsuccessful verification due to a business
name discrepancy.
### Test statement descriptor verification

Trigger statement descriptor verification for an `Account` object by using this
token for the
[settings.payments.statement_descriptor](https://docs.stripe.com/api/accounts/object#account_object-settings-payments-statement_descriptor)
attribute.

TokenType`mismatch`Trigger an `invalid_statement_descriptor_business_mismatch`
verification error.`disallowed`Trigger an
`invalid_statement_descriptor_denylisted` verification error.
Trigger statement descriptor prefix verification for an `Account` object by
using this token for the
[settings.card_payments.statement_descriptor_prefix](https://docs.stripe.com/api/accounts/object#account_object-settings-card_payments-statement_descriptor_prefix)
attribute.

TokenType`mismatch`Trigger an `invalid_statement_descriptor_prefix_mismatch`
verification error.`disallowed`Trigger an
`invalid_statement_descriptor_prefix_denylisted` verification error.
### Test business URL verification

Trigger URL verification for an `Account` object by using this token for the
[business_profile.url](https://docs.stripe.com/api/accounts/object#account_object-business_profile-url)
attribute.

TokenType`https://disallowed.stripe.com`Trigger an `invalid_url_denylisted`
verification error.`https://geoblocked.stripe.com`Trigger an
`invalid_url_website_inaccessible_geoblocked` verification
error.`https://problem.stripe.com`Trigger an `invalid_url_website_other`
verification error.`https://missing.stripe.com`Trigger an
`invalid_url_website_incomplete` verification
error.`https://mismatch.stripe.com`Trigger an
`invalid_url_website_business_information_mismatch` verification
error.`https://passwordprotected.stripe.com`Trigger an
`invalid_url_website_inaccessible_password_protected` verification
error.`https://accessible.stripe.com`Trigger a successful validation of the
URL.`https://underconstruction.stripe.com`Trigger an
`invalid_url_website_incomplete_under_construction` verification
error.`https://inaccessible.stripe.com`Trigger an
`invalid_url_website_inaccessible` verification error.
### Test Doing Business As (DBA) verification

Trigger DBA verification for an `Account` object by using this token for the
[business_profile.name](https://docs.stripe.com/api/accounts/object#account_object-business_profile-name)
attribute.

TokenType`disallowed_dba`Trigger an `invalid_business_profile_name_denylisted`
verification error.`invalid_dba`Trigger an `invalid_business_profile_name`
verification error.
### Test product description verification

Trigger product description verification for an `Account` object by using this
token for the
[business_profile.product_description](https://docs.stripe.com/api/accounts/object#account_object-business_profile-product_description)
attribute.

TokenType`require_url`Trigger an `invalid_url_web_presence_detected`
verification error.
### Test phone number validation

Clear phone number validation for an
[Account](https://docs.stripe.com/api/accounts) object by using this token for
the following attributes:

-
[business_profile.support_phone](https://docs.stripe.com/api/accounts/object#account_object-business_profile-support_phone)
-
[company.phone](https://docs.stripe.com/api/accounts/object#account_object-company-phone)
-
[individual.phone](https://docs.stripe.com/api/accounts/object#account_object-individual-phone)

Clear phone number validation for a
[Person](https://docs.stripe.com/api/persons) object by using this token for the
[phone](https://docs.stripe.com/api/persons/object#person_object-phone)
attribute.

TokenType`0000000000`Successful validation
### Test capability disabled reasons

Trigger assignment of a specific
[requirements.disabled_reason](https://docs.stripe.com/api/capabilities/object#capability_object-requirements-disabled_reason)
to all of an `Account` object’s inactive `Capability` objects by using this
token for the account’s
[business_profile.url](https://docs.stripe.com/api/accounts/object#account_object-business_profile-url)
attribute.

TokenType`https://inactivity.stripe.com`Set an account with no recent activity
as inactive and pause all verifications for it. Set the disabled reason for any
inactive capabilities to `paused.inactivity` (`rejected.other` for API versions
prior to `2024-06-20`).
## Trigger or advance verification

### Trigger cards

Use these card numbers to trigger various conditions when you’re testing both
requirements and tiered verification. For the trigger actions to work, you must
use these cards with a Connect charge by setting
[on_behalf_of](https://docs.stripe.com/connect/separate-charges-and-transfers#settlement-merchant),
or creating the charge [directly on the connected
account](https://docs.stripe.com/connect/direct-charges).

NumberTokenType4000000000004202`tok_visa_triggerNextRequirements`Changes the
next set of eventually due requirements to currently
due.4000000000004210`tok_visa_triggerChargeBlock`Triggers a charge
block.4000000000004236`tok_visa_triggerPayoutBlock`Triggers a payout block.
#### Trigger next requirements

Live mode can require additional verification information when a connected
account processes a certain amount of volume. This card sets any additional
verification information to be required immediately. If no additional
information is required, nothing appears.

#### Trigger a charge or payout block

If required information isn’t provided by the deadline, Stripe disables the
connected account’s charges or payouts. These cards disable the connected
account and move any currently due requirements to overdue. These cards have no
effect until an account provides the initial information that’s required to
enable charges and payouts.

### Trigger bank account ownership verification

Connected accounts in the United States and India are subject to [Bank account
ownership
verification](https://support.stripe.com/questions/bank-account-ownership-verification).
You can complete this verification by uploading supporting documents with the
Connect Dashboard or with the API through the
[documents[bank_account_ownership_verification]](https://docs.stripe.com/api/accounts/update#update_account-documents-bank_account_ownership_verification-files)
hash.

In test mode, you can simulate the US bank account ownership verification
process. Use the following test bank account numbers to trigger the verification
process. One number presumes successful verification and the other prompts you
to upload test images or file tokens to complete the verification process. These
test accounts are only available for US accounts.

RoutingAccountType`110000000``000999999991`Triggers and completes the bank
account ownership verification process after a short
delay`110000000``000999999992`Triggers the bank account ownership verification
process after a short delay and requests for document upload
### Simulate requirements

If your platform has connected accounts in different countries or plans to, you
might need to verify a person’s address as well as their identity (depending on
the country). Stripe provides a sample [date of
birth](https://docs.stripe.com/connect/testing#test-dobs) (DOB) and sample
[addresses](https://docs.stripe.com/connect/testing#test-verification-addresses)
to test for this requirement.

Information providedPerson verification
status`requirements.currently_due`Verified date of birth and verified
addressVerifiedNoneVerified date of birth and unverified
addressUnverified`verification.additional_document`Unverified date of birth and
verified addressUnverified`verification.document`Unverified date of birth and
unverified addressUnverified`verification.additional_document`,
`verification.document`
## Add funds to Stripe balance

To test [adding funds](https://docs.stripe.com/connect/top-ups) to your Stripe
balance from a bank account in the Dashboard, enable test mode and select the
desired test bank account in the drop-down menu within the **Add to balance**
dialog. You can simulate success or failure due to insufficient funds.

To test adding funds in the API, use the following test bank tokens as the
source while in test mode. Each token simulates a specific kind of event.

TokenType`btok_us_verified`Successful`btok_us_verified_noAccount`Unsuccessful
with a `no_account` code`btok_us_verified_accountClosed`Unsuccessful with an
`account_closed` code`btok_us_verified_insufficientFunds`Unsuccessful with an
`insufficient_funds` code`btok_us_verified_debitNotAuthorized`Unsuccessful with
a `debit_not_authorized` code`btok_us_verified_invalidCurrency`Unsuccessful with
an `invalid_currency` code
## Payouts

Use the following test bank and debit card numbers to trigger certain events
during [payout](https://docs.stripe.com/connect/payouts-connected-accounts)
testing. You can only use these values in test mode with test secret keys.

Test mode payouts simulate a live payout but aren’t processed with the bank.
Test mode accounts with Stripe Dashboard access always have payouts enabled, as
long as valid external bank information and other relevant conditions are met,
and never requires real identity verification.

#### Note

You can’t use test bank and debit card numbers in the Stripe Dashboard on a live
mode connected account. If you’ve entered your bank account information on a
live mode account, you can still use test mode, and test mode payouts will
simulate a live payout without processing actual money.

### Bank numbers

Use these test bank account numbers to test payouts. You can only use them with
test secret keys.

AlbaniaAlgeriaAngolaAntigua &
BarbudaArgentinaArmeniaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBelgiumBeninBhutanBoliviaBosnia
& HerzegovinaBotswanaBrazilBruneiBulgariaCambodiaCanadaChileColombiaCosta
RicaCôte d’IvoireCroatiaCyprusCzech RepublicDenmarkDominican
RepublicEcuadorEgyptEl
SalvadorEstoniaEthiopiaFinlandFranceGabonGambiaGermanyGhanaGibraltarGreeceGuatemalaGuyanaHong
KongHungaryIcelandIndiaIndonesiaIrelandIsraelItalyJamaicaJapanJordanKazakhstanKenyaKuwaitLaosLatviaLiechtensteinLithuaniaLuxembourgMacao
SAR
ChinaMadagascarMalaysiaMaltaMauritiusMexicoMoldovaMonacoMongoliaMoroccoMozambiqueNamibiaNetherlandsNew
ZealandNigerNigeriaNorth
MacedoniaNorwayOmanPakistanPanamaParaguayPeruPhilippinesPolandPortugalQatarRomaniaRwandaSan
MarinoSaudi ArabiaSenegalSerbiaSingaporeSlovakiaSloveniaSouth AfricaSouth
KoreaSpainSri LankaSt. LuciaSwedenSwitzerlandTaiwanTanzaniaThailandTrinidad &
TobagoTunisiaTurkeyUnited Arab EmiratesUnited Kingdom (IBAN)United Kingdom (Sort
Code)United
StatesUruguayUzbekistanVietnamRoutingAccountType`110000000``000123456789`Payout
succeeds.`110000000``000111111116`Payout fails with a `no_account`
code.`110000000``000111111113`Payout fails with a `account_closed`
code.`110000000``000222222227`Payout fails with a `insufficient_funds`
code.`110000000``000333333335`Payout fails with a `debit_not_authorized`
code.`110000000``000444444440`Payout fails with a `invalid_currency`
code.`110000000``000888888883`Payout fails if `method` is `instant`. Bank
account is not eligible for Instant Payouts.
### Debit card numbers

Use these test debit card numbers to test payouts to a debit card. These can
only be used with test secret keys.

United
StatesCanadaSingaporeAustraliaNumberTokenType4000056655665556`tok_visa_debit_us_transferSuccess`Visa
debit. Payout succeeds.4000056655665572`tok_visa_debit_us_transferFail`Visa
debit. Payout fails with a `could_not_process`
code.4000056755665555`tok_visa_debit_us_instantPayoutUnsupported`Visa debit.
Card isn’t eligible for Instant
Payouts.5200828282828210`tok_mastercard_debit_us_transferSuccess`Mastercard
debit. Payout
succeeds.6011981111111113`tok_discover_debit_us_transferSuccess`Discover debit.
Payout succeeds.

## Links

- [Connect](https://docs.stripe.com/connect)
- [test mode](https://docs.stripe.com/test-mode)
- [payments testing guide](https://docs.stripe.com/testing)
- [account type](https://docs.stripe.com/connect/accounts)
- [controller
properties](https://docs.stripe.com/connect/migrate-to-controller-properties)
- [Accounts API](https://docs.stripe.com/api/accounts/create)
- [Stripe
Dashboard](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#creating-accounts)
- [Connect OAuth
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/oauth)
- [OAuth](https://docs.stripe.com/connect/oauth-standard-accounts)
- [guide to testing
verification](https://docs.stripe.com/connect/testing-verification)
- [webhook](https://docs.stripe.com/webhooks)
-
[individual.id_number](https://docs.stripe.com/api/accounts/create#create_account-individual-id_number)
-
[id_number](https://docs.stripe.com/api/persons/create#create_person-id_number)
- [Uploading a
file](https://docs.stripe.com/connect/handling-api-verification#upload-a-file)
- [verified
image](https://d37ugbyn3rpeym.cloudfront.net/docs/identity/success.png)
- [unverified
image](https://d37ugbyn3rpeym.cloudfront.net/docs/identity/failed.png)
- [payouts](https://docs.stripe.com/payouts)
-
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
-
[company.tax_id](https://docs.stripe.com/api/accounts/create#create_account-company-tax_id)
-
[person.first_name](https://docs.stripe.com/api/persons/object#person_object-first_name)
-
[person.relationship.director](https://docs.stripe.com/api/persons/object#person_object-relationship-director)
-
[company.name](https://docs.stripe.com/api/accounts/object#account_object-company-name)
-
[settings.payments.statement_descriptor](https://docs.stripe.com/api/accounts/object#account_object-settings-payments-statement_descriptor)
-
[settings.card_payments.statement_descriptor_prefix](https://docs.stripe.com/api/accounts/object#account_object-settings-card_payments-statement_descriptor_prefix)
-
[business_profile.url](https://docs.stripe.com/api/accounts/object#account_object-business_profile-url)
-
[business_profile.name](https://docs.stripe.com/api/accounts/object#account_object-business_profile-name)
-
[business_profile.product_description](https://docs.stripe.com/api/accounts/object#account_object-business_profile-product_description)
- [Account](https://docs.stripe.com/api/accounts)
-
[business_profile.support_phone](https://docs.stripe.com/api/accounts/object#account_object-business_profile-support_phone)
-
[company.phone](https://docs.stripe.com/api/accounts/object#account_object-company-phone)
-
[individual.phone](https://docs.stripe.com/api/accounts/object#account_object-individual-phone)
- [Person](https://docs.stripe.com/api/persons)
- [phone](https://docs.stripe.com/api/persons/object#person_object-phone)
-
[requirements.disabled_reason](https://docs.stripe.com/api/capabilities/object#capability_object-requirements-disabled_reason)
-
[on_behalf_of](https://docs.stripe.com/connect/separate-charges-and-transfers#settlement-merchant)
- [directly on the connected
account](https://docs.stripe.com/connect/direct-charges)
- [Bank account ownership
verification](https://support.stripe.com/questions/bank-account-ownership-verification)
-
[documents[bank_account_ownership_verification]](https://docs.stripe.com/api/accounts/update#update_account-documents-bank_account_ownership_verification-files)
- [adding funds](https://docs.stripe.com/connect/top-ups)
- [payout](https://docs.stripe.com/connect/payouts-connected-accounts)