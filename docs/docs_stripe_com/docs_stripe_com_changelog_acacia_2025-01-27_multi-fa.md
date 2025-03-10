# Adds support for multiple financial accounts per business

## What’s new

Support for multiple [Financial
Accounts](https://docs.stripe.com/api/treasury/financial_accounts) per business
is now generally available. This means that each of your accounts with
[Treasury](https://docs.stripe.com/treasury) enabled can have more than one
financial account.

## Changes

REST APIRubyPythonPHPJavaNodeGo.NET
 Endpoint

ChangeResourcecloseAdded[Treasury.FinancialAccount](https://docs.stripe.com/api/treasury/financial_accounts/object)ParametersChangeResources
or
endpointsis_defaultnicknameAdded[Treasury.FinancialAccount](https://docs.stripe.com/api/treasury/financial_accounts/object)destination_payment_method_dataAdded[Treasury.OutboundTransfer#create](https://docs.stripe.com/api/treasury/outbound_transfers/create)financial_accountAdded[Treasury.OutboundTransfer.destination_payment_method_details](https://docs.stripe.com/api/treasury/outbound_transfers/object#outbound_transfer_object-destination_payment_method_details)outbound_transferAdded[Treasury.ReceivedCredit.linked_flows.source_flow_details](https://docs.stripe.com/api/treasury/received_credits/object#received_credit_object-linked_flows-source_flow_details)ValueChangeEnumsoutbound_transferAdded`Treasury.ReceivedCredit#list.linked_flows.source_flow_type``Treasury.ReceivedCredit.linked_flows.source_flow_details.type`FieldChangeFrom
→
toTreasury.OutboundTransfer.destination_payment_method_details.typeChanged`literal('us_bank_account')
→ enum('financial_account'|'us_bank_account')`
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2025-01-27.acacia`
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

- [Financial Accounts](https://docs.stripe.com/api/treasury/financial_accounts)
- [Treasury](https://docs.stripe.com/treasury)
-
[Treasury.FinancialAccount](https://docs.stripe.com/api/treasury/financial_accounts/object)
-
[Treasury.OutboundTransfer#create](https://docs.stripe.com/api/treasury/outbound_transfers/create)
-
[Treasury.OutboundTransfer.destination_payment_method_details](https://docs.stripe.com/api/treasury/outbound_transfers/object#outbound_transfer_object-destination_payment_method_details)
-
[Treasury.ReceivedCredit.linked_flows.source_flow_details](https://docs.stripe.com/api/treasury/received_credits/object#received_credit_object-linked_flows-source_flow_details)
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