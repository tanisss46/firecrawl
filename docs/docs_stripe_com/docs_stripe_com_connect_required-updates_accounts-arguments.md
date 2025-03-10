# Accounts API Argument Changes

## This page maps old Accounts API arguments to the new argument names.

Individuals and companies used to share many of the same arguments. With the new
[Persons API](https://docs.stripe.com/api/persons) and other changes, many of
these arguments now have new names specific to individuals and companies.
Existing [Account](https://docs.stripe.com/api/accounts) arguments that have not
changed are not listed on this page.

## Individuals

Old argumentNew
argument`business_name``business_profile.name``business_url``business_profile.url``debit_negative_balances``settings.payouts.debit_negative_balances``decline_charge_on``settings.card_payments.decline_on``keys`Authenticate
using the [Stripe-Account
header](https://docs.stripe.com/connect/authentication#stripe-account-header).`legal_entity``business_type``legal_entity.additional_owners`Argument
removed.
`legal_entity.address`

`individual.address`

`individual.address_kana` (Japan) `individual.address_kanji` (Japan)

`legal_entity.dob``individual.dob``legal_entity.first_name``individual.first_name``legal_entity.last_name``individual.last_name``legal_entity.personal_address``individual.address``legal_entity.personal_phone_number``individual.phone``legal_entity.personal_id_number``individual.id_number``legal_entity.personal_id_number_provided``individual.id_number_provided``legal_entity.ssn_last_4``individual.ssn_last_4``legal_entity.ssn_last_4_provided``individual.ssn_last_4_provided``legal_entity.type``business_type``legal_entity.verification``individual.verification``mcc``business_profile.mcc``payout_schedule``settings.payouts.schedule``payout_statement_descriptor``settings.payouts.statement_descriptor``product_description``business_profile.product_description``statement_descriptor``settings.payments.statement_descriptor``support_email``business_profile.support_email``support_phone``business_profile.support_phone``support_address``business_profile.support_address``verification.disabled_reason``requirements.disabled_reason``verification.due_by``requirements.current_deadline``verification.fields_needed``requirements.past_due,
requirements.currently_due, requirements.eventually_due`
## Companies

Old argumentNew
argument`business_name``business_profile.name``business_url``business_profile.url``debit_negative_balances``settings.payouts.debit_negative_balances``decline_charge_on``settings.card_payments.decline_on``keys`Authenticate
using the [Stripe-Account
header](https://docs.stripe.com/connect/authentication#stripe-account-header).`legal_entity`Argument
removed and replaced with `company`.`legal_entity.additional_owners`Argument
removed.
`legal_entity.address`

`company.address`

`company.address_kana` (Japan) `company.address_kanji` (Japan)

`legal_entity.business_name`

`company.name`

`company.name_kana` (Japan)

`company.name_kanji` (Japan)

`legal_entity.business_tax_id``company.tax_id``legal_entity.business_tax_id_provided``company.tax_id_provided``legal_entity.dob`Now
managed with the
[Persons](https://docs.stripe.com/api/persons/object#person_object-dob)
object.`legal_entity.first_name`Now managed with the
[Persons](https://docs.stripe.com/api/persons/object#person_object-first_name)
object.`legal_entity.last_name`Now managed with the
[Persons](https://docs.stripe.com/api/persons/object#person_object-last_name)
object.`legal_entity.personal_address`Now managed with the
[Persons](https://docs.stripe.com/api/persons/object#person_object-address)
object.`legal_entity.phone_number``company.phone``legal_entity.personal_id_number`Now
managed with the
[Persons](https://docs.stripe.com/api/persons/create#create_person-personal_id_number)
object.`legal_entity.personal_id_number_provided`Now managed with the
[Persons](https://docs.stripe.com/api/persons/object#person_object-personal_id_number_provided)
object.`legal_entity.ssn_last_4`Now managed with the
[Persons](https://docs.stripe.com/api/persons/create#create_person-ssn_last_4)
object.`legal_entity.ssn_last_4_provided`Now managed with the
[Persons](https://docs.stripe.com/api/persons/object#person_object-ssn_last_4_provided)
object.`legal_entity.type``business_type``legal_entity.verification`Now managed
with the
[Persons](https://docs.stripe.com/api/persons/object#person_object-requirements)
object.`mcc``business_profile.mcc``payout_schedule``settings.payouts.schedule``payout_statement_descriptor``settings.payouts.statement_descriptor``product_description``business_profile.product_description``statement_descriptor``settings.payments.statement_descriptor``support_email``business_profile.support_email``support_phone``business_profile.support_phone``support_address``business_profile.support_address``verification.disabled_reason``requirements.disabled_reason``verification.due_by``requirements.current_deadline``verification.fields_needed``requirements.past_due,
requirements.currently_due, requirements.eventually_due`

## Links

- [Persons API](https://docs.stripe.com/api/persons)
- [Account](https://docs.stripe.com/api/accounts)
- [Stripe-Account
header](https://docs.stripe.com/connect/authentication#stripe-account-header)
- [Persons](https://docs.stripe.com/api/persons/object#person_object-dob)
- [Persons](https://docs.stripe.com/api/persons/object#person_object-first_name)
- [Persons](https://docs.stripe.com/api/persons/object#person_object-last_name)
- [Persons](https://docs.stripe.com/api/persons/object#person_object-address)
-
[Persons](https://docs.stripe.com/api/persons/create#create_person-personal_id_number)
-
[Persons](https://docs.stripe.com/api/persons/object#person_object-personal_id_number_provided)
- [Persons](https://docs.stripe.com/api/persons/create#create_person-ssn_last_4)
-
[Persons](https://docs.stripe.com/api/persons/object#person_object-ssn_last_4_provided)
-
[Persons](https://docs.stripe.com/api/persons/object#person_object-requirements)