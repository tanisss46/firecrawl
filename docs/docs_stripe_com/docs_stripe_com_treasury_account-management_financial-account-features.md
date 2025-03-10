# Financial account features

## Learn about the features available for financial accounts.

You add features to [financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
to provide the functionality that enables you to move money between accounts,
attach payment cards, and more. You typically assign the `Feature` objects you
want when creating `FinancialAccount` objects, but you can add or remove them at
any time. Some `Features` require that the connected account associated with the
financial account have particular capabilities active. For example, a connected
account must have the `card_issuing` capability active before you can request
the `card_issuing` feature on the financial account attached to that connected
account.

## Available features

The following table lists the available `Features` for a `FinancialAccount` and
the capabilities the associated connected account must have active to add them.

#### Note

You must request or have the following capabilities active before you can
request the `treasury` capability for connected accounts:

- `transfers`
- `card_payments`
FeatureDescriptionRequired capabilities`card_issuing`Allows the creation of a
[Card object](https://docs.stripe.com/api/#issuing_card_object) associated with
this financial account.`card_issuing``deposit_insurance`Requests FDIC insurance
eligibility for the financial
account.`treasury``financial_addresses.aba`Triggers the creation of a
`FinancialAddress` object of type ABA associated with this financial account.
When this feature is active, the address can receive money over ACH or wire, and
external bank accounts can debit it.`treasury``inbound_transfers.ach`Allows
creation of `InboundTransfer` objects to fund the financial account by debiting
an external US bank account.`treasury`,
`us_bank_account_ach_payments``intra_stripe_flows`Enables this financial account
to send money to or receive money from other financial accounts over the
`stripe` network. Both financial accounts (originator and recipient) need this
feature enabled for `stripe` network outbound payments to
work.`treasury``outbound_payments.ach`Allows this financial account to send ACH
transfers using the `OutboundPayment` objects of the Stripe API.`treasury`,
`us_bank_account_ach_payments``outbound_payments.us_domestic_wire`Allows this
financial account to send US domestic wire transfers using `OutboundPayment`
objects of the Stripe API.`treasury``outbound_transfers.ach`Allows this
financial account to send ACH transfers using `OutboundTransfer` objects of the
Stripe API.`treasury`,
`us_bank_account_ach_payments``outbound_transfers.us_domestic_wire`Allows this
financial account to send US domestic wire transfers using `OutboundTransfer`
objects of the Stripe API.`treasury`
### Same-day ACH

#### Private preview

Same-day ACH is currently in preview with limited availability, subject to
Stripe review and approval. To request access, email
[treasury-support@stripe.com](mailto:treasury-support@stripe.com).

If you don’t have access, API calls that include same-day ACH features or
parameters return an error.

The following features enable financial accounts to use same-day ACH
functionality. You must request the corresponding `*.ach` feature on a financial
account to use it. For example, to enable a financial account to send a same-day
[OutboundPayment](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments),
you must request `outbound_payments.ach` and `outbound_payments.ach.same_day` on
that financial account:

FeatureDescriptionRequired capabilities`outbound_payments.ach.same_day`Allows
this financial account to send ACH transfers using `OutboundPayment` objects
that arrive in the destination account within the same business day.`treasury`,
`us_bank_account_ach_payments``outbound_transfers.ach.same_day`Allows this
financial account to send ACH transfers using `OutboundTransfer` objects that
arrive in the destination account within the same business day.`treasury`,
`us_bank_account_ach_payments``inbound_payments.ach.same_day`Allows creation of
`InboundTransfer` objects to fund the financial account within the same business
day.`treasury`, `us_bank_account_ach_payments`
## Requesting features

Typically, you request features on your Treasury financial account when you
[create the financial
account](https://docs.stripe.com/treasury/account-management/financial-accounts#create-a-financialaccount).
The following request creates a financial account and requests features in the
same call.

```
curl https://api.stripe.com/v1/treasury/financial_accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "supported_currencies[]"=usd \
 -d "features[card_issuing][requested]"=true \
 -d "features[financial_addresses][aba][requested]"=true
```

If you’re working with existing financial accounts, use `POST
/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features` to request
additional features.

```
curl
https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "card_issuing[requested]"=true \
 -d "deposit_insurance[requested]"=true \
 -d "financial_addresses[aba][requested]"=true \
 -d "inbound_transfers[ach][requested]"=true \
 -d "intra_stripe_flows[requested]"=true \
 -d "outbound_payments[ach][requested]"=true \
 -d "outbound_payments[us_domestic_wire][requested]"=true \
 -d "outbound_transfers[ach][requested]"=true \
 -d "outbound_transfers[us_domestic_wire][requested]"=true
```

### Feature activation

After you request a feature and satisfy all verification requirements to onboard
the connected account to your platform, the feature activates. For some
features, activation can be instantaneous (for example, `card_issuing`). Other
features, like `financial_addresses.aba`, [activate
asynchronously](https://docs.stripe.com/treasury/account-management/financial-account-features#webhooks).
The following API call creates a financial account and requests the
‘financial_addresses.aba’ and ‘card_issuing’ features.

```
curl https://api.stripe.com/v1/treasury/financial_accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "supported_currencies[]"=usd \
 -d "features[financial_addresses][aba][requested]"=true \
 -d "features[card_issuing][requested]"=true
```

When you request features on financial account creation, the response indicates
their status in the `active_features`, `pending_features`, and
`restricted_features` properties. For more information, see the [Retrieving
features](https://docs.stripe.com/treasury/account-management/financial-account-features#retrieving-features)
section.

```
{
 "object": "treasury.financial_account",
 "created": 1612927106,
 "id": "fa_123",
 "country": "US",
 "supported_currencies": ["usd"],
 "active_features": ["card_issuing"],
 "pending_features": ["financial_addresses.aba"],
 "restricted_features": [],
// No FinancialAddress added as the financial_addresses.aba feature is not yet
active
 "financial_addresses": [],
 "livemode": true,
 "status": "open",
 ...
}
```

You can use `GET
/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features` to retrieve
the features for the financial account created in the previous example.

```
curl
https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

The response shows `financial_addresses.aba` with a `status` of `pending` and
`status_details` with a `code` of `activating`.

```
{
 "object": "treasury.financial_account_features",
 "financial_addresses": {
 "aba": {
 "requested": true,
 "status": "pending",
 "status_details": [
 {
 "code": "activating"
 }
 ]
 }
 },
 "card_issuing": {
 "requested": true,
 "status": "active",
 "status_details": []
 },
 ...
}
```

A feature can remain in this state for up to 30 minutes while Stripe
communicates with external systems. When the `financial_addresses.aba` feature
activates, the financial account receives a `FinancialAddress` object and
triggers a `treasury.financial_account.features_status_updated`
[webhook](https://docs.stripe.com/webhooks).

The following request retrieves the `FinancialAccount` details with the
`financial_addresses.aba` details expanded.

```
curl https://api.stripe.com/v1/treasury/financial_accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "expand[]"="financial_addresses.aba.account_number" \
 -d "supported_currencies[]"=usd
```

The response provides the account details, including the complete financial
address information.

```
{
 "object": "treasury.financial_account",
 "id": "{{FINANCIAL_ACCOUNT_ID}}",
 "country": "US",
 "supported_currencies": ["usd"],
 "active_features": ["card_issuing", "financial_addresses.aba"],
 "pending_features": [],
 "restricted_features": [],
 "financial_addresses": [
 {
 "type": "aba",
 "supported_networks": ["ach", "domestic_wire_us"],
 "aba": {
 "account_number_last4": "7890",
 "account_number": "1234567890",
 "routing_number": "000000001",
 "bank_name": "Goldman Sachs"
 }
 }
 ],
 "livemode": true,
 ...
}
```

The financial account can now receive credits or debits to this ABA financial
address.

## Removing features

To remove a feature, use `POST
/v1/treasury/financial_accounts/{{FINANCIALACCOUNT_ID}}/features` and set the
value of the feature to `false`.

```
curl
https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "card_issuing[requested]"=false
```

If successful, you receive the [Features
object](https://docs.stripe.com/api/treasury/financial_account_features) as a
response with the feature you removed absent from the object.

## Retrieving features

To retrieve the features of a financial account, use `GET
/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features`.

```
curl
https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

The JSON response provides the feature details defined by three properties:

- `requested`: Indicates whether the feature has been requested.
- `status`: Describes the current state of the feature: `active`, `pending`, or
`restricted`.
- `status_details`: Array of hashes containing a code and resolution.

```
{
 "card_issuing": {
 "requested": true,
 "status": "active",
 "status_details": []
 },
 "deposit_insurance": {
 "requested": true,
 "status": "restricted",
 "status_details": [
 {
 "code": "requirements_past_due",
 "resolution": "provide_information"
 }
 ]
 }
}
```

The following table identifies the possible combinations of `status` and
`status_details`.

StatusStatus details codeStatus details
resolutionDescription`pending``activating`Stripe is currently activating the
feature.`pending``requirements_pending_verification`The requirements for the
associated capability on the connected account have been submitted but haven’t
completed
verification.`restricted``requirements_past_due``provide_information`The
connected account has requirements that must be fulfilled before this feature
can be enabled.`restricted``rejected_unsupported_business``contact_stripe`The
account is rejected because this type of business isn’t currently supported. For
more information, email
[treasury-support@stripe.com](mailto:treasury-support@stripe.com).`restricted``rejected_other``contact_stripe`The
account is rejected for other reasons. For more information, email
[treasury-support@stripe.com](mailto:treasury-support@stripe.com).`restricted``restricted_by_platform``remove_restriction`The
platform has restricted this feature using the
[platform_restrictions](https://docs.stripe.com/api/treasury/financial_accounts/object#financial_account_object-platform_restrictions)
hash.`restricted``financial_account_closed`This feature is unavailable because
the financial account is
closed.`restricted``restricted_other``contact_stripe`This feature is restricted
for other reasons. For more information, email
[treasury-support@stripe.com](mailto:treasury-support@stripe.com).
## Restricted features

You can restrict money movement in financial accounts on your platform to
disallow inbound flows (`inbound_flows`), outbound flows (`outbound_flows`), or
both types of flows. To do so, use the
[platform_restrictions](https://docs.stripe.com/api/treasury/financial_accounts/object#financial_account_object-platform_restrictions)
hash. Restricting a flow impacts the financial account’s features that rely
completely or partially on that flow. For example, to prevent money from moving
out of a financial account, call `POST
/v1/treasury/financial_accounts/{{FINANCIALACCOUNT_ID}}`.

```
curl
https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d "platform_restrictions[outbound_flows]"=restricted
```

If successful, the response returns the financial account object with the
appropriate flow set as `restricted`.

```
{
 "object": "treasury.financial_account",
 "id": "{{FINANCIAL_ACCOUNT_ID}}",
 "status": "open",
 ...
 "platform_restrictions": {
 "inbound_flows": "unrestricted",
 "outbound_flows": "restricted"
 },
"active_features": ["card_issuing", "deposit_insurance",
"inbound_transfers.ach"],
 "pending_features": [],
"restricted_features": ["financial_addresses.aba", "intra_stripe_flows",
"outbound_payments.ach", "outbound_payments.us_domestic_wire",
"outbound_transfers.ach", "outbound_transfers.us_domestic_wire"]
}
```

As the previous response shows, restricting `outbound_flows` on the
FinancialAccount adds `financial_addresses.aba`, `intra_stripe_flows`, and
`inbound_transfers.ach` to the `restricted_features` array.

Features in the `restricted_features` array can be fully or partially
restricted. For example, `financial_addresses.aba` is part of the
`restricted_features` array in the preceding response because restricting
`outbound_flows` prevents debits to the financial address. However, that
financial address can still receive ACH or wire transfers, because
`inbound_flows` aren’t restricted.

Similarly, the `intra_stripe_flows` feature is restricted because the
`outbound_flows` restriction prevents using this financial account as the source
of an outbound payment to another financial account. However, the financial
account can still be the destination of an outbound payment, so the feature
isn’t completely restricted.

The following request retrieves feature details for a financial account with
restricted flows.

```
curl
https://api.stripe.com/v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}}/features
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

The response provides the `Feature` object that includes `status_details` with a
code of `restricted_by_platform`. The `restriction` property provides a
reference to the `platform_restriction` applied.

```
{
 "object": "treasury.financial_account_features",
 "financial_addresses": {
 "aba": {
 "requested": true,
 "status": "restricted",
 "status_details": [
 {
 "code": "restricted_by_platform",
 "resolution": "remove_restriction",
 "restriction": "inbound_flows"
 }
 ]
 }
 },
 ...
}
```

The following table outlines the impacts to features by `platform_restrictions`.

#### Note

Restricting inbound flows for the `financial_addresses.aba` feature doesn’t
block inbound wires.

### Impact of platform restrictions on features

The following table shows the effects of `inbound_flows` and `outbound_flows`
platform restrictions on individual features:

Feature
inbound_flowsoutbound_flows`card_issuing`N/AN/A`deposit_insurance`N/AN/A`financial_addresses.aba`Prevents
the ABA financial address from receiving credits over ACH.Prevents debits from
the ABA financial address.`inbound_transfers.ach`Disables the
feature.N/A`intra_stripe_flows`Prevents the financial account from receiving
outbound payments from other financial accounts.Outbound payments can’t be made
from this financial account to other financial
accounts.`outbound_payments.ach`N/ADisables the
feature.`outbound_payments.us_domestic_wire`N/ADisables the
feature.`outbound_transfers.ach`N/ADisables the
feature.`outbound_transfers.us_domestic_wire`N/ADisables the feature.
## Webhooks

To perform an action with [webhooks](https://docs.stripe.com/webhooks) when one
or more features have transitioned to a certain status, compare your local state
with the latest state of the feature. While the `previous_attributes` property
of the `treasury.financial_account.features_status_updated` webhook also
indicates which features have changed from one status to another, events can be
duplicated or received out of order. For more information, see the [webhooks
best practices](https://docs.stripe.com/webhooks#best-practices).

- `account.updated`- When requesting new features, the platform might get an
`account.updated` webhook indicating that the `requirements` hash has changed
with fields added to `pending_verification`.
- `treasury.financial_account.features_status_updated`- Indicates that one or
more features have changed status, reflected in changes to the
`active_features`, `pending_features` or `restricted_features` arrays.

## Links

- [financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)
- [Card object](https://docs.stripe.com/api/#issuing_card_object)
-
[OutboundPayment](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments)
- [create the financial
account](https://docs.stripe.com/treasury/account-management/financial-accounts#create-a-financialaccount)
- [webhook](https://docs.stripe.com/webhooks)
- [Features
object](https://docs.stripe.com/api/treasury/financial_account_features)
-
[platform_restrictions](https://docs.stripe.com/api/treasury/financial_accounts/object#financial_account_object-platform_restrictions)
- [webhooks best practices](https://docs.stripe.com/webhooks#best-practices)