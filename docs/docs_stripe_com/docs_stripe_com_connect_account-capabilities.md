# Account capabilities

## Learn about capabilities you can enable for accounts and the requirements you must satisfy to use them.

The capabilities you request for a connected account determine the information
you need to collect for that account. To reduce onboarding effort, only request
the capabilities you need. The more capabilities you request, the more
information you must collect.

You can start by completing the [platform
profile](https://dashboard.stripe.com/connect/profile) to understand which
capabilities might be appropriate for your platform.

#### Note

For some capabilities, requesting them enables them permanently. Attempting to
remove or unrequest a permanent capability returns an error.

After creating an account, you can request additional capabilities and remove
existing non-permanent capabilities. For connected accounts that [other
platforms
control](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts),
you can’t unrequest capabilities.

## Supported capabilities

Following is a list of available capabilities. Click an item to expand or
collapse it.

### Transfers

### Card payments

### US tax reporting

### Payment methods

### India international payments

## Multiple capabilities

Requesting multiple capabilities for a connected account is common, but involves
the following considerations:

- Capabilities operate independently of each other.
- If a connected account has both `card_payments` and `transfers`, and the
`status` of either one is `inactive`, then both capabilities are disabled.
- You can request or unrequest a capability for a connected account at any time
during the account’s lifecycle.

Capabilities also allow you to collect information for multiple purposes at the
same time. For example, you can collect both required tax information and the
information required for a requested capability. If you’re onboarding a
connected account with the `transfers` capability and they’re required to file
an IRS form 1099-MISC (a US federal tax reporting form), you can collect
information for both at the same time.

## Create an account with capabilities

Capabilities are set on the
[Account](https://docs.stripe.com/api/accounts/object) object. To get the list
of available capabilities for an Account, use the
[list_capabilities](https://docs.stripe.com/api/capabilities/list?lang=curl)
endpoint.

Account creation and requesting capabilities differ for connected accounts in
different configurations.

- For connected accounts with access to the full Stripe Dashboard, including
Standard accounts, some capabilities are requested automatically, based on their
country. You can also request other capabilities for them.
- For connected accounts with access to the Express Dashboard, including Express
accounts, you can either request their capabilities or use the [onboarding
configuration
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/countries)
to automate capability requests.
- For connected accounts without access to a Stripe-hosted dashboard, including
Custom accounts, you must request their capabilities.
Typed AccountsController properties
```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "controller[fees][payer]"=application \
 -d "controller[losses][payments]"=application \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[requirement_collection]"=application \
 -d country=US \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true
```

Information requirements vary depending on the capability, but they often relate
to identity verification or other information specific to a payment type.

When your connected account is successfully created, you can [retrieve a
list](https://docs.stripe.com/api/accounts/retrieve) of its requirements:

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

In the response, the `requirements` hash specifies the required information. The
values for `payouts_enabled` and `charges_enabled` indicate whether payouts and
charges are enabled for the account.

## Capabilities for existing connected accounts

The following sections describe how to preview information requirements or
manage capabilities for existing connected accounts using the [Capabilities
API](https://docs.stripe.com/api/capabilities).

### Preview information requirements

You can preview what information is needed from your connected account for a
particular capability either before or after that capability has been requested.

When you request capabilities, `account.updated`
[webhooks](https://docs.stripe.com/webhooks) fire and the account’s requirements
can change. To enable a requirement faster and avoid disabling the account,
preview the requirements and collect any required information before requesting
the capability.

The following example [lists](https://docs.stripe.com/api/capabilities/retrieve)
the requirements for the `card_payments` capability for a specific account.

```
curl
https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/capabilities/card_payments
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

In the response, check the `requirements` hash to see what information is
needed:

```
{
 "id": "card_payments",
 "object": "capability",
 "account": "{{CONNECTED_ACCOUNT_ID}}",
 "requested": false,
 "requested_at": null,
 "requirements": {
 "past_due": [],
 "currently_due": ["company.tax_id", ...],
 "eventually_due": [...],
 "disabled_reason": ...,
 "current_deadline": ...,
 },
 "status": "unrequested"
}
```

The value for `status` identifies whether the capability has been requested.
When the value is
[requested](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting),
the account’s requirements are active.

In addition to previewing a capability’s requirements before requesting it, you
can use the same endpoint to view a capability’s current requirements. That can
help you stay informed when requirements change.

### Request and unrequest capabilities

To request a capability for an account, set the capability’s `requested` value
to `true` by [updating the
account](https://docs.stripe.com/api/capabilities/update). If the request
succeeds, the API returns `requested: true` in the response.

To unrequest a capability for an account, set the capability’s `requested` value
to `false` by [updating the
account](https://docs.stripe.com/api/capabilities/update). If the capability
can’t be removed, the call returns an error. If the call succeeds, the API
returns `requested: false` in the response.

You can also [request and remove an account’s
capabilities](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#updating-capabilities)
from the Dashboard. If a capability can’t be removed, its **Remove** button is
disabled.

The example below requests the `transfers` capability for a specific connected
account:

```
curl
https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/capabilities/transfers
\
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d requested=true
```

The example below requests multiple capabilities for a specific connected
account:

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "capabilities[bancontact_payments][requested]"=true \
 -d "capabilities[eps_payments][requested]"=true \
 -d "capabilities[ideal_payments][requested]"=true \
 -d "capabilities[p24_payments][requested]"=true \
 -d "capabilities[sepa_debit_payments][requested]"=true
```

## Deprecated capabilities

Capabilities described in the following sections are deprecated. If possible,
don’t request them for new accounts. If you have existing accounts that use
deprecated capabilities, we recommend that you update them to use other
capabilities instead.

### legacy_payments

The `legacy_payments` capability enables charges, payouts, and transfers. Newer
accounts enable those actions using the `card_payments` and `transfers`
capabilities, which support more flexible configurations.

We recommend that you take the following steps:

- Update your connected account onboarding process to request the appropriate
combination of `card_payments` and `transfers` instead of `legacy_payments`.
- Update your existing connected accounts to request the appropriate combination
of `card_payments` and `transfers`.
- Update any code that checks the status of `legacy_payments` to check the
status of either `legacy_payments` or the appropriate new capability. For
example, update code that relies on an account’s ability to make card payments
to run when either `legacy_payments` or `card_payments` is active. Similarly,
update code that relies on an account’s ability to accept transfers to run when
either `legacy_payments` or `transfers` is active. The updated code works
throughout the process of transitioning to the new capabilities, regardless of
when the new capabilities become active.
- After the new capabilities are active for all of your connected accounts,
remove references to `legacy_payments` from your code.

#### Note

You can’t unrequest the `legacy_payments` capability. Stripe will notify you in
advance before we remove it.

If you do business in Canada, Stripe automatically requests `card_payments` and
`transfers` for your accounts that use `legacy_payments`, in order to comply
with [updated
requirements](https://docs.stripe.com/connect/upcoming-requirements-updates?program=ca-2023).
During the process, you might see the following values in your connected
accounts’ API responses.

Before requesting new capabilitiesNew capabilities requestedNew requirements
completed
```
capabilities: {
 legacy_payments: "active"
},
charges_enabled: true,
payouts_enabled: true

```

```
capabilities: {
 card_payments: "inactive",
 legacy_payments: "active",
 transfers: "inactive"
},
charges_enabled: true,
payouts_enabled: true

```

```
capabilities: {
 card_payments: "active",
 legacy_payments: "active",
 transfers: "active"
},
charges_enabled: true,
payouts_enabled: true

```

#### Note

During the transition, `card_payments` and `transfers` requirements might appear
in `past_due`. However, if `legacy_payments` is active, then charges, transfers,
and payouts remain enabled.

## See also

- [Create a charge](https://docs.stripe.com/connect/charges)

## Links

- [platform profile](https://dashboard.stripe.com/connect/profile)
- [other platforms
control](https://docs.stripe.com/connect/platform-controls-for-stripe-dashboard-accounts)
- [Account](https://docs.stripe.com/api/accounts/object)
- [list_capabilities](https://docs.stripe.com/api/capabilities/list?lang=curl)
- [onboarding configuration
settings](https://dashboard.stripe.com/settings/connect/onboarding-options/countries)
- [retrieve a list](https://docs.stripe.com/api/accounts/retrieve)
- [Capabilities API](https://docs.stripe.com/api/capabilities)
- [webhooks](https://docs.stripe.com/webhooks)
- [lists](https://docs.stripe.com/api/capabilities/retrieve)
- [updating the account](https://docs.stripe.com/api/capabilities/update)
- [request and remove an account’s
capabilities](https://docs.stripe.com/connect/dashboard/managing-individual-accounts#updating-capabilities)
- [updated
requirements](https://docs.stripe.com/connect/upcoming-requirements-updates?program=ca-2023)
- [Create a charge](https://docs.stripe.com/connect/charges)