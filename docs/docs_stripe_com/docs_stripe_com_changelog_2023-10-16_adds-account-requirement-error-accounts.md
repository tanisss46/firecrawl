# Adds new account requirement error codes to the Accounts API Breaking changes

## What’s new

Adds the following error codes to the `requirements.errors` array in the
Accounts API. To learn more, see [Account requirements
errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors).

- `invalid_address_highway_contract_box`
- `invalid_address_private_mailbox`
- `invalid_business_profile_name`
- `invalid_business_profile_name_denylisted`
- `invalid_company_name_denylisted`
- `invalid_dob_age_over_maximum`
- `invalid_dob_age_under_minimum`
- `invalid_product_description_length`
- `invalid_product_description_url_match`
- `invalid_statement_descriptor_business_mismatch`
- `invalid_statement_descriptor_denylisted`
- `invalid_statement_descriptor_length`
- `invalid_statement_descriptor_prefix_denylisted`
- `invalid_statement_descriptor_prefix_mismatch`
- `invalid_tax_id_format`
- `invalid_url_denylisted`
- `invalid_url_format`
- `invalid_url_web_presence_detected`
- `invalid_url_website_business_information_mismatch`
- `invalid_url_website_empty`
- `invalid_url_website_inaccessible`
- `invalid_url_website_inaccessible_geoblocked`
- `invalid_url_website_inaccessible_password_protected`
- `invalid_url_website_incomplete`
- `invalid_url_website_incomplete_cancellation_policy`
- `invalid_url_website_incomplete_customer_service_details`
- `invalid_url_website_incomplete_legal_restrictions`
- `invalid_url_website_incomplete_refund_policy`
- `invalid_url_website_incomplete_return_policy`
- `invalid_url_website_incomplete_terms_and_conditions`
- `invalid_url_website_incomplete_under_construction`
- `invalid_url_website_other`

## Impact

Lets you get detailed error messages for issues with addresses, business
profiles, company names, dates of birth, product descriptions, statement
descriptors, tax IDs, and URLs.

## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2023-10-16`
- Upgrade the API version used for [webhook
endpoints](https://docs.stripe.com/webhooks/versioning).
- [Test your integration](https://docs.stripe.com/testing) against the new
version.
- If you use Connect, [test your Connect
integration](https://docs.stripe.com/connect/testing).
- In Workbench, [perform the
upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade). You can [roll
back the version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades).

## Links

- [Account requirements
errors](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors)
- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
- [API requests](https://docs.stripe.com/api/versioning)
- [webhook endpoints](https://docs.stripe.com/webhooks/versioning)
- [Test your integration](https://docs.stripe.com/testing)
- [test your Connect integration](https://docs.stripe.com/connect/testing)
- [perform the upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade)
- [roll back the
version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
- [Stripe API upgrades](https://docs.stripe.com/upgrades)