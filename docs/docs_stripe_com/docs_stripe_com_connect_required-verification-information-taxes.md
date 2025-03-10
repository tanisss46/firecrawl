# Required Verification Information for Taxes

## Learn what account information you need to provide for your Connect accounts if you want Stripe to help you with US federal 1099 tax reporting.

#### Note

Stripe recommends that you consult a tax advisor to determine your tax filing
and reporting requirements.

## Required information (1099-K, 1099-MISC, 1099-NEC)

The following table lists the requirements for connected accounts with any of
the [1099
capabilities](https://docs.stripe.com/connect/account-capabilities#tax-reporting).
Stripe requires the business tax details except when the account is set up as a
*Single Person Entity* (SPE) with a US-based representative, in which case we’ll
use the representative’s personal tax details.

Stripe defines a Single Person Entity as follows:

- Individual: [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
is `individual`
- Sole Proprietorship: [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
is `company` and [business
structure](https://docs.stripe.com/api/accounts/create#create_account-company-structure)
is `sole_proprietorship`
- Single Member LLC: [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
is `company` and [business
structure](https://docs.stripe.com/api/accounts/create#create_account-company-structure)
is `single_member_llc`

Even if you don’t add the 1099 capabilities and want to update the information
directly in Stripe to file your 1099 forms, these are the fields to populate.

TypeSPE with US-based representativeSPE with non-US-based
representativeCompanyName- `individual.first_name`
- `individual.last_name`

`company.name``company.name`TIN`individual.id_number``company.tax_id``company.tax_id`
Address

`individual.address`

Required address fields are:

-
[individual.address.line1](https://docs.stripe.com/api/accounts/update#update_account-individual-address-line1)
-
[individual.address.postal_code](https://docs.stripe.com/api/accounts/update#update_account-individual-address-postal_code)
-
[individual.address.city](https://docs.stripe.com/api/accounts/update#update_account-individual-address-city)
-
[individual.address.state](https://docs.stripe.com/api/accounts/update#update_account-individual-address-state)

`company.address`

Required address fields are:

-
[company.address.line1](https://docs.stripe.com/api/accounts/update#update_account-company-address-line1)
-
[company.address.postal_code](https://docs.stripe.com/api/accounts/update#update_account-company-address-postal_code)
-
[company.address.city](https://docs.stripe.com/api/accounts/update#update_account-company-address-city)
-
[company.address.state](https://docs.stripe.com/api/accounts/update#update_account-company-address-state)

`company.address`

Required address fields are:

-
[company.address.line1](https://docs.stripe.com/api/accounts/update#update_account-company-address-line1)
-
[company.address.postal_code](https://docs.stripe.com/api/accounts/update#update_account-company-address-postal_code)
-
[company.address.city](https://docs.stripe.com/api/accounts/update#update_account-company-address-city)
-
[company.address.state](https://docs.stripe.com/api/accounts/update#update_account-company-address-state)

If you have any of the 1099 capabilities turned on,
[Payouts](https://docs.stripe.com/payouts) become disabled if the required
information isn’t collected and verified by 600 USD in charges.

## Links

- [1099
capabilities](https://docs.stripe.com/connect/account-capabilities#tax-reporting)
- [business
type](https://docs.stripe.com/api/accounts/object#account_object-business_type)
- [business
structure](https://docs.stripe.com/api/accounts/create#create_account-company-structure)
-
[individual.address.line1](https://docs.stripe.com/api/accounts/update#update_account-individual-address-line1)
-
[individual.address.postal_code](https://docs.stripe.com/api/accounts/update#update_account-individual-address-postal_code)
-
[individual.address.city](https://docs.stripe.com/api/accounts/update#update_account-individual-address-city)
-
[individual.address.state](https://docs.stripe.com/api/accounts/update#update_account-individual-address-state)
-
[company.address.line1](https://docs.stripe.com/api/accounts/update#update_account-company-address-line1)
-
[company.address.postal_code](https://docs.stripe.com/api/accounts/update#update_account-company-address-postal_code)
-
[company.address.city](https://docs.stripe.com/api/accounts/update#update_account-company-address-city)
-
[company.address.state](https://docs.stripe.com/api/accounts/update#update_account-company-address-state)
- [Payouts](https://docs.stripe.com/payouts)