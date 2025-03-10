# Migrate your Connect integration to use controller properties instead of account types

## Learn how to work with account controller properties instead of specifying account types.

You can now configure connected accounts using account controller properties
instead of defining accounts as Standard, Express, or Custom. These controller
properties let you specify discrete account behaviors like which Stripe-hosted
dashboard the account can access or who Stripe collects fees from. This
modularity allows for more flexible configuration options.

Using account controller properties doesn’t require you to update your API
version. **Migrating your integration to use controller properties is
optional**. If you only use one type of connected account and aren’t interested
in using a new configuration, you don’t need to update your integration.

We recommend you update your integration to take advantage of the increased
modularity and new configurations available. The new properties are fully
backwards compatible, so you can migrate your integration incrementally while
continuing to work with account types.

Each account type maps to a set of controller properties. We automatically set
those properties on your existing connected accounts and on any accounts that
you create with account types going forward. When you update your integration to
work with controller properties, you don’t have to update any of your connected
accounts.

#### Note

You can start using features such as [embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
without making any of the changes in this guide.

## Before you begin

- Learn how account controller properties work and how they map to your existing
connected accounts.
- Determine which of the new account configurations make sense for your
integration.

Updating your integration involves:

- Identifying code in your integration that references the account type, and
updating it to reference the corresponding controller properties instead.
- Updating your account creation process to specify controller properties
instead of `type`. Specifying `type` is no longer required.

## Account controller properties

You can specify values for the controller properties when you create a connected
account using the [Accounts
API](https://docs.stripe.com/api/accounts/create#create_account-controller). Any
property that you don’t specify is set to a default value that has the least
complex integration requirements.

If you’re building a new integration, you can get a configuration recommendation
by completing [Connect platform
onboarding](https://dashboard.stripe.com/connect/set-up).

PropertyDefault
valueDescription[controller.losses.payments](https://docs.stripe.com/api/accounts/create#create_account-controller-losses-payments)`stripe`Possible
values:- `application`: Your platform is [responsible for negative
balances](https://docs.stripe.com/connect/risk-management) and manages credit
and fraud risk on the connected account, which requires you to review and
acknowledge your responsibilities in [the
Dashboard](https://dashboard.stripe.com/settings/connect/platform_profile)
- `stripe`: Stripe is liable when this account can’t pay back negative balances
resulting from payments. Your platform is still liable for a negative balance on
your platform account.

[controller.fees.payer](https://docs.stripe.com/api/accounts/create#create_account-controller-fees-payer)

`account`

Possible values:

- `account`: The connected account pays all Stripe fees directly to Stripe,
inclusive of payment processing fees
- `application`: The Connect platform pays all Stripe fees, inclusive of payment
processing fees
- `application_custom`: The account was created with type=custom
- `application_express`: The account was created with type=express

When you create an account, you can only specify `application` or `account`.

`application_express` and `application_custom` are not valid creation
parameters.

For a comprehensive description of Stripe fee payment models, see the [fee
behavior
documentation](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior).

[controller.requirement_collection](https://docs.stripe.com/api/accounts/create#create_account-controller-requirement_collection)`stripe`Possible
values:- `application`: Your platform is responsible for collecting updated
information when [requirements are due or
change](https://docs.stripe.com/connect/required-verification-information)
- `stripe`: Stripe is responsible for collecting updated information when
[requirements are due or
change](https://docs.stripe.com/connect/required-verification-information)

[controller.stripe_dashboard.type](https://docs.stripe.com/api/accounts/create#create_account-controller-stripe_dashboard-type)`full`Possible
values:- `express`: The connected account can access the Express Dashboard
- `full`: The connected account can access the full Stripe Dashboard
- `none`: The account can’t access the Express or Stripe Dashboard

[type](https://docs.stripe.com/api/accounts/create#create_account-type)

See the description

Possible values:

- `custom`: The account was created as a Custom connected account
- `express`: The account was created as an Express connected account
- `standard`: The account was created as a Standard connected account or with
controller properties matching Standard accounts
- `none`: The account was created with no type value and its controller
properties don’t match any of the three account types

Specifying `type` is optional. If you create an account using `type`, you can
only specify `custom`, `express`, or `standard`. `none` isn’t a valid account
creation parameter.

## Mapping account types to controller parameters

Each of the three account types maps to values in the `controller` hash of
`v1/accounts` that match the behavior of that type.

### Standard

If you create an account without specifying any controller properties, the
default values match the behavior of a Standard account. You can also create the
equivalent of a Standard account by specifying the values that map to Standard
account behavior.

These values map to a Standard account’s behavior:

- `losses.payments`: `stripe`
- `fees.payer`: `account`
- `requirement_collection`: `stripe`
- `stripe_dashboard.type`: `full`
Creation with controller propertiesCreation with type
Request (using default values for all properties):

```
curl -X POST https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

Response:

```
{
 controller: {
 type: "application",
 is_controller: true,
 losses: {
 payments: "stripe"
 },
 requirement_collection: "stripe",
 fees: {
 payer: "account",
 },
 stripe_dashboard: {
 type: "full"
 }
 },
 type: "standard"
}

```

### Express

These values map to an Express account’s behavior:

- `losses.payments`: `application`
- `fees.payer`: `application` (see note)
- `requirement_collection`: `stripe`
- `stripe_dashboard.type`: `express`

#### Note

Creating an Express account using `type`, sets the `controller.fees.payer`
property to `application_express` instead of `application`. This difference
denotes a variation in Stripe [fee billing
behavior](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior)
when your platform is using Direct charges.

Creation with controller propertiesCreation with type
Request:

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "controller[stripe_dashboard][type]"=express \
 -d "controller[fees][payer]"=application \
 -d "controller[losses][payments]"=application
```

Response:

```
{
 controller: {
 type: "application",
 is_controller: true,
 losses: {
 payments: "application"
 },
 requirement_collection: "stripe",
 fees: {
 payer: "application",
 },
 stripe_dashboard: {
 type: "express"
 }
 },
 type: "none"
}
```

### Custom

These values map to a Custom account’s behavior:

- `losses.payments`: `application`
- `fees.payer`: `application` (see note)
- `requirement_collection`: `application`
- `stripe_dashboard.type`: `none`

You must also specify the account country when creating a Custom account, and
request the `card_payments` and `transfers` capabilities.

#### Note

Creating a Custom account using `type`, sets the `controller.fees.payer`
property to `application_custom` instead of `application`. This difference
denotes a variation in Stripe [fee billing
behavior](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior)
when your platform is using Direct charges.

Creation with controller propertiesCreation with type
Request:

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[fees][payer]"=application \
 -d "controller[losses][payments]"=application \
 -d "controller[requirement_collection]"=application \
 -d "capabilities[transfers][requested]"=true \
 -d country=US
```

Response:

```
{
 controller: {
 type: "application",
 is_controller: true,
 losses: {
 payments: "application"
 },
 requirement_collection: "application",
 fees: {
 payer: "application",
 },
 stripe_dashboard: {
 type: "none"
 }
 },
 type: "none"
}
```

## Migrate code to use controller properties

In addition to updating your account creation process to use controller
properties, update your integration by reviewing your code and looking for
references to account types.

For each reference to an account type, determine which controller property or
properties are relevant and update the code accordingly.

For example, say that your code includes a conditional statement that applies to
Express and Custom accounts because it relates to your platform being
responsible for negative balances. Update that logic from `if type == express`
or `if type == custom` to `if controller.losses.payments == application`.

If you create connected accounts that don’t match an account type, consider
their controller properties as well when updating your code. The logic for
handling those accounts can differ from your existing logic that’s based on
account types.

You can use this table to identify the controller properties associated with
each account type:

Account
Typelosses.paymentsfees.payerrequirement_collectionstripe_dashboard.typeCustom`application``application_custom``application``none`Express`application``application_express``stripe``express`Standard`stripe``account``stripe``full`
#### Note

Remember that Express and Custom accounts have a different value for
`fees.payer` than equivalent accounts created using controller properties. When
updating code related to collecting fees, you must take into account the
difference in behavior.

## Unsupported configurations

When creating accounts with controller properties, the following combinations
aren’t supported:

`controller.requirement_collection` = `application` isn’t compatible with any of
the following values:

- `controller.losses.payments` = `stripe`
- `controller.fees.payer` = `account`
- `controller.stripe_dashboard.type` = `express`
- `controller.stripe_dashboard.type` = `full`

`controller.stripe_dashboard.type` = `express` isn’t compatible with any of the
following values:

- `controller.losses.payments` = `stripe`
- `controller.fees.payer` = `account`
- `controller.requirement_collection` = `application`

`controller.stripe_dashboard.type` = `full` isn’t compatible with any of the
following values:

- `controller.losses.payments` = `application`
- `controller.fees.payer` = `application`
- `controller.requirement_collection` = `application`

`controller.stripe_dashboard.type` = `none` isn’t supported when both of the
following values are set (it’s supported when only one of them is set):

- `controller.requirement_collection` = `stripe`
- `controller.losses.payments` = `application`

## Links

- [embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Accounts
API](https://docs.stripe.com/api/accounts/create#create_account-controller)
- [Connect platform onboarding](https://dashboard.stripe.com/connect/set-up)
-
[controller.losses.payments](https://docs.stripe.com/api/accounts/create#create_account-controller-losses-payments)
- [responsible for negative
balances](https://docs.stripe.com/connect/risk-management)
- [the
Dashboard](https://dashboard.stripe.com/settings/connect/platform_profile)
-
[controller.fees.payer](https://docs.stripe.com/api/accounts/create#create_account-controller-fees-payer)
- [fee behavior
documentation](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior)
-
[controller.requirement_collection](https://docs.stripe.com/api/accounts/create#create_account-controller-requirement_collection)
- [requirements are due or
change](https://docs.stripe.com/connect/required-verification-information)
-
[controller.stripe_dashboard.type](https://docs.stripe.com/api/accounts/create#create_account-controller-stripe_dashboard-type)
- [type](https://docs.stripe.com/api/accounts/create#create_account-type)