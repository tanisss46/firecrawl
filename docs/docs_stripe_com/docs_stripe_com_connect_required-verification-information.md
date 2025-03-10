# Required verification information

## Learn what required verification information you need to collect for each country when using Connect.

Onboarding connected accounts to a [Connect](https://docs.stripe.com/connect)
platform requires collecting certain information for each account (which Stripe
verifies). For Custom accounts, you can build an onboarding UI yourself [using
our
API](https://docs.stripe.com/connect/custom/onboarding#api-based-onboarding).
[Embedded
onboarding](https://docs.stripe.com/connect/custom/onboarding#embedded-onboarding)
and [Stripe hosted
onboarding](https://docs.stripe.com/connect/custom/onboarding#stripe-hosted-onboarding)
are prebuilt UIs that you use to collect the required information from connected
accounts.

#### Note

If you’re onboarding Express or Standard accounts, you don’t need to collect
information because Stripe does it for you through the Stripe-provided UIs.
However, you can review the type of information that’s collected from your users
on this page.

Verification requirements differ based on:

- The origin country of the connected accounts
- The [service agreement
type](https://docs.stripe.com/connect/service-agreement-types) applicable to the
connected accounts
- The [capabilities](https://docs.stripe.com/connect/account-capabilities)
requested for the connected accounts
- The [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
(for example, individual or company) and
[company.structure](https://docs.stripe.com/api/accounts/object#account_object-company-structure)
(for example, public corporation or private partnership)

As an added convenience, most arguments in the tables below are followed by a
localized version, suitable as a label in your user interface.

Platform CountryAustralia (AU)Austria (AT)Belgium (BE)Brazil (BR)Bulgaria
(BG)Canada (CA)Costa Rica (CR)Croatia (HR)Cyprus (CY)Czech Republic (CZ)Côte
d’Ivoire (CI)Denmark (DK)Dominican Republic (DO)Estonia (EE)Finland (FI)France
(FR)Germany (DE)Gibraltar (GI)Greece (GR)Guatemala (GT)Hong Kong (HK)Hungary
(HU)India (IN)Indonesia (ID)Ireland (IE)Italy (IT)Japan (JP)Latvia
(LV)Liechtenstein (LI)Lithuania (LT)Luxembourg (LU)Malaysia (MY)Malta (MT)Mexico
(MX)Netherlands (NL)New Zealand (NZ)Norway (NO)Peru (PE)Philippines (PH)Poland
(PL)Portugal (PT)Romania (RO)Senegal (SN)Singapore (SG)Slovakia (SK)Slovenia
(SI)South Korea (KR)Spain (ES)Sweden (SE)Switzerland (CH)Thailand (TH)Trinidad &
Tobago (TT)United Arab Emirates (AE)United Kingdom (GB)United States (US)Uruguay
(UY)Account CountryAlbania (AL)Algeria (DZ)Angola (AO)Antigua & Barbuda
(AG)Argentina (AR)Armenia (AM)Australia (AU)Austria (AT)Azerbaijan (AZ)Bahamas
(BS)Bahrain (BH)Bangladesh (BD)Belgium (BE)Benin (BJ)Bhutan (BT)Bolivia
(BO)Bosnia & Herzegovina (BA)Botswana (BW)Brazil (BR)Brunei (BN)Bulgaria
(BG)Cambodia (KH)Canada (CA)Chile (CL)Colombia (CO)Costa Rica (CR)Croatia
(HR)Cyprus (CY)Czech Republic (CZ)Côte d’Ivoire (CI)Denmark (DK)Dominican
Republic (DO)Ecuador (EC)Egypt (EG)El Salvador (SV)Estonia (EE)Ethiopia
(ET)Finland (FI)France (FR)Gabon (GA)Gambia (GM)Germany (DE)Ghana (GH)Gibraltar
(GI)Greece (GR)Guatemala (GT)Guyana (GY)Hong Kong (HK)Hungary (HU)Iceland
(IS)India (IN)Indonesia (ID)Ireland (IE)Israel (IL)Italy (IT)Jamaica (JM)Japan
(JP)Jordan (JO)Kazakhstan (KZ)Kenya (KE)Kuwait (KW)Laos (LA)Latvia
(LV)Liechtenstein (LI)Lithuania (LT)Luxembourg (LU)Macao SAR China
(MO)Madagascar (MG)Malaysia (MY)Malta (MT)Mauritius (MU)Mexico (MX)Moldova
(MD)Monaco (MC)Mongolia (MN)Morocco (MA)Mozambique (MZ)Namibia (NA)Netherlands
(NL)New Zealand (NZ)Niger (NE)Nigeria (NG)North Macedonia (MK)Norway (NO)Oman
(OM)Pakistan (PK)Panama (PA)Paraguay (PY)Peru (PE)Philippines (PH)Poland
(PL)Portugal (PT)Qatar (QA)Romania (RO)Rwanda (RW)San Marino (SM)Saudi Arabia
(SA)Senegal (SN)Serbia (RS)Singapore (SG)Slovakia (SK)Slovenia (SI)South Africa
(ZA)South Korea (KR)Spain (ES)Sri Lanka (LK)St. Lucia (LC)Sweden (SE)Switzerland
(CH)Taiwan (TW)Tanzania (TZ)Thailand (TH)Trinidad & Tobago (TT)Tunisia
(TN)Turkey (TR)United Arab Emirates (AE)United Kingdom (GB)United States
(US)Uruguay (UY)Uzbekistan (UZ)Vietnam (VN)Dashboard TypefullexpressnoneService
AgreementfullBusiness
Typeindividualcompanynon_profitgovernment_entityCapabilityAdd a
capability...`card_payments``transfers`The `transfers` capability is required
when the `card_payments` capability is requested.Minimum verification
requirements for connected accounts in United States matching the above
selections.Required beforeRequirementsSelectionsBusiness
type`business_type=individual`Account informationMerchant category codeFirst
chargeFirst payout`business_profile.mcc`URLFirst chargeVerifiedFirst
payoutVerifiedPayouts`business_profile.url`Must be a reachable, unique URL that
describes the account's business.Statement descriptorsFirst chargeVerifiedFirst
payoutVerifiedPayouts`settings.payments.statement_descriptor`Must be similar to
the business name, legal entity name, or URL of the account.Terms of
serviceFirst charge`tos_acceptance.ip``tos_acceptance.date`External accountFirst
payout`external_account`IndividualsNameFirst chargeFirst
payout`individual.first_name``individual.last_name`Date of birthFirst
chargeFirst
payout`individual.dob.day``individual.dob.month``individual.dob.year`Must be
between 13 and 120 years old.AddressFirst chargeFirst
payout`individual.address.line1``individual.address.postal_code``individual.address.city``individual.address.state`Must
be a U.S. address. PO Boxes are not allowed.EmailFirst chargeFirst
payout`individual.email`PhoneFirst chargeFirst payout`individual.phone`Must be a
U.S. phone number.Tax informationFirst chargeFirst
payout`individual.ssn_last_4`Must be the last 4 digits of a 9 digit U.S. Social
Security number (SSN).
#### Additional information on the individual

To enable card payments, a validated city, state, and ZIP code for
`individual.address` is required.

To enable payouts, `individual.address` needs to be a validated *full* address.
Payouts will be disabled if a full address hasn’t been validated before 30 days.

If the individual fails verification with `ssn_last_4`, then the full SSN is
required and their identity needs to be verified to enable card payments. Use
the
[individual.id_number](https://docs.stripe.com/api/accounts/update#update_account-individual-id_number)
argument to collect this information.

#### Additional information for minors

If the account representative is a minor, you must verify the minor’s legal
guardian. A legal guardian is a [Person](https://docs.stripe.com/api/persons) on
the account with
[relationship.legal_guardian](https://docs.stripe.com/api/persons/create#create_person-relationship-legal_guardian)
set to `true`. Additionally, the legal guardian must provide their information
and sign the Stripe terms of service, which we store on the Person object with
`relationship.legal_guardian` set to `true`. Store the legal guardian’s terms of
service acceptance in the
[additional_tos_acceptances](https://docs.stripe.com/api/persons/create#create_person-additional_tos_acceptances)
hash.

If the legal guardian fails verification with `ssn_last_4`, then the full SSN is
required and their identity needs to be verified to enable card payments. Use
the
[person.id_number](https://docs.stripe.com/api/persons/update#update_person-id_number)
argument to collect this information.

If Stripe is unable to verify the legal guardian or if the person doesn’t have
an SSN, you need to collect a scan of an [ID
document](https://docs.stripe.com/connect/handling-api-verification#acceptable-verification-documents)
to enable card payments. This information can be collected with the
[verification.document.front](https://docs.stripe.com/api/persons/object#person_object-verification-document-front)
and
[verification.document.back](https://docs.stripe.com/api/persons/object#person_object-verification-document-back)
arguments.

#### Supported business structures

While uncommon, there are circumstances where an `individual` business operates
and is treated more like a `company`, such as a single-member LLC. For these
users, you can optionally collect information on their [legal
structure](https://docs.stripe.com/connect/identity-verification#business-structure)
with the
[company.structure](https://docs.stripe.com/api/accounts/create#create_account-company-structure)
argument.

If your user’s business has only one member or owner and is registered as an LLC
with a US state, you can set the `business_type` to `company` and the
`company.structure` to `single_member_llc`. You collect the same required
information, except you use the
[company](https://docs.stripe.com/api/accounts/object#account_object-company)
hash and the [Persons](https://docs.stripe.com/api/persons) API, instead of the
`individual` hash. For any requirement in the `individual` hash, you need to map
it to the account’s representative, such as setting `representative.first_name`
instead of `individual.first_name`.

If your user has obtained a business identification (for example, has a tax ID
that’s separate from their personal ID, or a business address that’s different
than their home address), you can set the `business_type` to `company` and the
`company.structure` to `sole_proprietorship`. You collect the same required
information, except you use the
[company](https://docs.stripe.com/api/accounts/object#account_object-company)
hash and the [Persons](https://docs.stripe.com/api/persons) API, instead of the
`individual` hash since it pertains to the natural person. For any requirement
in the `individual` hash, you need to map it to the account’s representative,
such as setting `representative.first_name` instead of `individual.first_name`.

#### Tax reporting information

By default, the requirements for `transfers` do not collect all information at
the appropriate thresholds to file IRS Form 1099-K or Form 1099-MISC. If your
business has US federal 1099 filing requirements and plans to file these through
Stripe, request the [appropriate tax reporting
capability](https://docs.stripe.com/connect/account-capabilities#tax-reporting)
and make sure to collect the [necessary
information](https://docs.stripe.com/connect/required-verification-information-taxes)
from your users.

#### Threshold information

In addition to the onboarding requirements, there is a second threshold to keep
payouts enabled, which depends on your industry and Stripe’s review of your
platform profile. The `company.tax_id` (EIN) needs to be verified before 10,000
USD in charges for some platforms, and before 3,000 USD for other platforms.

- `individual.dob.day`
- `individual.dob.month`
- `individual.dob.year`
- `individual.ssn_last_4`

#### Payments threshold information

When an account with `card_payments` reaches 500,000 USD in lifetime charges, we
require a full `id_number` (SSN) for them to continue accepting payments. If
they’ve already provided the full number, they don’t have to provide it again.

For accounts with `business_type` set to `individual`, and where the owner isn’t
a minor, [update the account’s
individual.id_number](https://docs.stripe.com/api/accounts/update#update_account-individual-id_number).
For other accounts, which have persons with
[relationship.legal_guardian](https://docs.stripe.com/api/persons/object#person_object-relationship-representative),
[relationship.representative](https://docs.stripe.com/api/persons/object#person_object-relationship-representative),
or
[relationship.owner](https://docs.stripe.com/api/persons/object#person_object-relationship-owner),
[update the appropriate person’s
id_number](https://docs.stripe.com/api/persons/update#update_person-id_number).

## Links

- [Connect](https://docs.stripe.com/connect)
- [using our
API](https://docs.stripe.com/connect/custom/onboarding#api-based-onboarding)
- [Embedded
onboarding](https://docs.stripe.com/connect/custom/onboarding#embedded-onboarding)
- [Stripe hosted
onboarding](https://docs.stripe.com/connect/custom/onboarding#stripe-hosted-onboarding)
- [service agreement
type](https://docs.stripe.com/connect/service-agreement-types)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)
- [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
-
[company.structure](https://docs.stripe.com/api/accounts/object#account_object-company-structure)
- [Trade
License](https://docs.stripe.com/api/accounts/create#create_account-documents-company_license)
- [Proof of Bank
Account](https://docs.stripe.com/api/accounts/create#create_account-documents-bank_account_ownership_verification)
- [payouts](https://docs.stripe.com/payouts)
- [Memorandum of
Association](https://docs.stripe.com/api/accounts/create#create_account-documents-company_memorandum_of_association)
-
[verification.document](https://docs.stripe.com/api/persons/create#create_person-verification-document)
-
[documents](https://docs.stripe.com/api/persons/create#create_person-documents)
- [Trade
License](https://docs.stripe.com/api/accounts/update#update_account-documents-company_license)
-
[Passport](https://docs.stripe.com/api/persons/update#update_person-documents-passport)
- [company
requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements-currently_due)
- [individual
requirements](https://docs.stripe.com/api/persons/object#person_object-requirements-currently_due)
- [beneficial
owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
- [holding
company](https://support.stripe.com/questions/beneficial-ownership-by-a-trust-holding-company-or-other-legal-entity)
-
[relationship.owner](https://docs.stripe.com/api/persons/object#person_object-relationship-owner)
-
[relationship.executive](https://docs.stripe.com/api/persons/object#person_object-relationship-executive)
- [invoice](https://docs.stripe.com/api/invoices)
- [Power of
Attorney](https://docs.stripe.com/api/persons/update#update_person-documents-company_authorization)
- [business
structures](https://docs.stripe.com/connect/identity-verification#business-structure)
-
[sanctions](https://docs.stripe.com/connect/risk-management/best-practices#sanctions-concerns)
- [proof-of-entity
document](https://docs.stripe.com/connect/handling-api-verification#acceptable-verification-documents)
-
[company.verification.document.front](https://docs.stripe.com/api/accounts/object#account_object-company-verification-document-front)
-
[company.verification.document.back](https://docs.stripe.com/api/accounts/object#account_object-company-verification-document-back)
-
[individual.verification.document.front](https://docs.stripe.com/api/accounts/update#update_account-individual-verification-document-front)
-
[individual.verification.document.back](https://docs.stripe.com/api/accounts/update#update_account-individual-verification-document-back)
-
[verification.document.front](https://docs.stripe.com/api/persons/object#person_object-verification-document-front)
-
[verification.document.back](https://docs.stripe.com/api/persons/object#person_object-verification-document-back)
-
[relationship.representative](https://docs.stripe.com/api/persons/object#person_object-relationship-representative)
-
[relationship.percent_ownership](https://docs.stripe.com/api/persons/object#person_object-relationship-percent_ownership)
-
[company.directors_provided](https://docs.stripe.com/api/accounts/object#account_object-company-directors_provided)
-
[company.owners_provided](https://docs.stripe.com/api/accounts/object#account_object-company-owners_provided)
-
[company.executives_provided](https://docs.stripe.com/api/accounts/object#account_object-company-executives_provided)
- [proof-of-entity
document](https://docs.stripe.com/connect/handling-api-verification?country=CA&document-type=entity#acceptable-verification-documents)
- [ID
document](https://docs.stripe.com/connect/handling-api-verification?country=CA&document-type=identity#acceptable-verification-documents)
- [Stripe Identity](https://docs.stripe.com/identity)
- [Connect Onboarding](https://stripe.com/connect/onboarding)
-
[verification.additional_document.front](https://docs.stripe.com/api/persons/object#person_object-verification-additional_document-front)
-
[verification.additional_document.back](https://docs.stripe.com/api/persons/object#person_object-verification-additional_document-back)
- [upload them](https://docs.stripe.com/api/files/create)
-
[individual.verification.document.front](https://docs.stripe.com/api/accounts/object#account_object-individual-verification-document-front)
-
[individual.verification.document.back](https://docs.stripe.com/api/accounts/object#account_object-individual-verification-document-back)
-
[individual.verification.additional_document.front](https://docs.stripe.com/api/accounts/object#account_object-individual-verification-additional_document-front)
-
[individual.verification.additional_document.back](https://docs.stripe.com/api/accounts/object#account_object-individual-verification-additional_document-back)
- [proof of registration
document](https://docs.stripe.com/connect/handling-api-verification?country=CA&document-type=relationship#acceptable-verification-documents)
-
[documents.proof_of_registration.files](https://docs.stripe.com/api/accounts/create#create_account-documents-proof_of_registration-files)
-
[documents.company_registration_verification.files](https://docs.stripe.com/api/accounts/update#update_account-documents-company_registration_verification-files)
-
[company.ownership_declaration.date](https://docs.stripe.com/api/accounts/object#account_object-company-ownership_declaration-date)
-
[company.ownership_declaration.ip](https://docs.stripe.com/api/accounts/object#account_object-company-ownership_declaration-ip)
- [matches that of the Stripe
account](https://support.stripe.com/questions/bank-account-ownership-verification)
-
[documents.bank_account_ownership_verification.files](https://docs.stripe.com/api/accounts/update#update_account-external_account-documents-bank_account_ownership_verification)
-
[static](https://docs.stripe.com/get-started/account/statement-descriptors#static)
-
[API](https://docs.stripe.com/api/accounts/create#create_account-settings-payments-statement_descriptor)
- [Japanese statement
descriptors](https://docs.stripe.com/get-started/account/statement-descriptors#set-japanese-statement-descriptors)
-
[representative.id_number](https://docs.stripe.com/api/persons/update#update_person-id_number)
-
[owners](https://support.stripe.com/questions/beneficial-owner-and-director-definition)
- [Payment Services Act
2019](https://stripe.com/guides/sg-payment-services-act-2019)
- [MyInfo](https://www.singpass.gov.sg/main/individuals/)
- [holding
company](https://support.stripe.com/questions/beneficial-ownership-verification-for-holding-companies)
-
[disabled_reason](https://docs.stripe.com/api/accounts/object#account_object-requirements-disabled_reason)
- [Singapore Open Data License version
1.0](https://data.gov.sg/open-data-licence)
-
[registered_address](https://docs.stripe.com/api/persons/object#person_object-registered_address)
-
[id_number](https://docs.stripe.com/api/persons/create#create_person-id_number)
-
[id_number_secondary](https://docs.stripe.com/api/persons/create#create_person-id_number_secondary)
- [an IRS Letter 147C document or an IRS SS-4 confirmation
letter](https://support.stripe.com/questions/using-irs-documentation-as-reference-when-entering-business-name-and-tax-id-number-tin-for-us-based-businesses)
-
[individual.id_number](https://docs.stripe.com/api/accounts/update#update_account-individual-id_number)
- [Person](https://docs.stripe.com/api/persons)
-
[relationship.legal_guardian](https://docs.stripe.com/api/persons/create#create_person-relationship-legal_guardian)
-
[additional_tos_acceptances](https://docs.stripe.com/api/persons/create#create_person-additional_tos_acceptances)
-
[company.structure](https://docs.stripe.com/api/accounts/create#create_account-company-structure)
- [company](https://docs.stripe.com/api/accounts/object#account_object-company)
- [appropriate tax reporting
capability](https://docs.stripe.com/connect/account-capabilities#tax-reporting)
- [necessary
information](https://docs.stripe.com/connect/required-verification-information-taxes)