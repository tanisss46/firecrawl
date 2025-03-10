# Adds risk verification details for connected accountsBreaking changes

## What’s new

Upgrading to this version helps you better understand the causes of
supportability verification issues for your connected accounts. You can see the
verification error in the
[requirements.errors.code](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors-code)
enum.

The new error includes text that describes the requirement for the following
risk requirements:

- `supportability_rejection_appeal`
- `business_model_verification`
- `restricted_or_prohibited_industry_diligence`
- `other_supportability_inquiry`

For example, if a verification fails because your connected account is selling
alcohol, this message is shown in the `reason` field: “We can’t accept payments
for age-restricted goods such as alcohol under the Stripe Services Agreement, as
mentioned in [the prohibited and restricted businesses
list](https://stripe.com/legal/restricted-businesses).”

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 // ...
 "requirements": {
 "disabled_reason": "other",
"past_due": ["interv_abc123.restricted_or_prohibited_industry_diligence.form"],
 "pending_verification": [],
 "errors": [
 {
 "code": "verification_supportability",
"reason": "We can't accept payments for age-resticted goods such as alcohol
under the Stripe Services Agreement, as mentioned in the restricted businesses
list.",
"requirement": "interv_abc123.restricted_or_prohibited_industry_diligence.form"
 }
 ],
 "alternatives": []
 // ...
 }
}
```

Learn more about [handling risk
verifications](https://docs.stripe.com/connect/handling-api-verification#handle-risk-verifications).

## Why is this a breaking change?

This is a breaking change because it adds the new `verification_supportability`
value to the requirements [error code
enumeration](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors-code).

## Impact

You can use the details to send notifications to connected accounts and guide
them to a form where they can address the requirements.

## Changes

REST
APIRubyPythonPHPJavaNodeGo.NETValueChangeEnumsverification_supportabilityAdded[Account.future_requirements.errors[].code](https://docs.stripe.com/api/accounts/object#account_object-future_requirements-errors-code)[Account.requirements.errors[].code](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors-code)[BankAccount.future_requirements.errors[].code](https://docs.stripe.com/api/external_account_bank_accounts/object#account_bank_account_object-future_requirements-errors-code)
+ 1 more
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-09-30.acacia`
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

-
[requirements.errors.code](https://docs.stripe.com/api/accounts/object#account_object-requirements-errors-code)
- [the prohibited and restricted businesses
list](https://stripe.com/legal/restricted-businesses)
- [handling risk
verifications](https://docs.stripe.com/connect/handling-api-verification#handle-risk-verifications)
-
[Account.future_requirements.errors[].code](https://docs.stripe.com/api/accounts/object#account_object-future_requirements-errors-code)
-
[BankAccount.future_requirements.errors[].code](https://docs.stripe.com/api/external_account_bank_accounts/object#account_bank_account_object-future_requirements-errors-code)
-
[BankAccount.requirements.errors[].code](https://docs.stripe.com/api/external_account_bank_accounts/object#account_bank_account_object-requirements)
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