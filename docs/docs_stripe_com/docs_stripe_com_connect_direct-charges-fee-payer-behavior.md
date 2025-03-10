# Fee behavior on connected accounts

## Understand how to configure the billing behavior for new connected accounts.

The `controller.fees.payer` property on `v1/accounts` determines the set of
billing behaviors you can expect for direct charges and product usages that
occur on this connected account. This doc details the behavior of the different
values it can have.

#### Note

Any activity occurring at the platform account level is billed to your platform
regardless of the `controller.fees.payer` value on your connected accounts. For
example, Stripe charges the platform directly for destination charges (with or
without `on_behalf_of`) and card account updates for cards stored on your
platform account.

## Selecting billing behavior

You can only set the
[controller.fees.payer](https://docs.stripe.com/api/accounts/create#create_account-controller-fees-payer)
property when you create an account.

The following sections describe the behavior of each value.

### account

Stripe collects fees directly from your connected account. We don’t charge any
[Connect fees](https://stripe.com/connect/pricing) to it or to your platform.

Any application fees that your platform bills to the connected account are in
addition to Stripe fees.

You can set the payer type to `account` when you create connected accounts.
Accounts created with `type=standard` also have this value.

### application

The platform pays payment fees for direct charges and fees for Stripe products
like Radar, Card Account Updater, and Instant Payouts. For complete details, see
[the table
below](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior#fee-payer-behaviors).

The platform also pays [Connect fees](https://stripe.com/connect/pricing) for
these accounts .

We recommend that you monetize payments and Stripe products where the platform
is billed by collecting fees from your connected accounts.

You can set the payer type to `application` when you create connected accounts.

Platforms that pay Stripe payment fees for direct charges can access dedicated
reports.

See [Platform Reporting for direct charge payment fees paid by
platform](https://docs.stripe.com/connect/direct-charge-buy-rate-reporting-overview).

### application_custom or application_express

`application_custom` and `application_express` are assigned to accounts created
with `type=custom` and `type=express`, respectively. Their billing behaviors for
direct charges and connected account usage of Stripe products matches the
historical behavior of Custom and Express accounts. For complete details, see
[the table
below](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior#fee-payer-behaviors).

We recommend that you monetize payments and Stripe products where the platform
is billed by collecting fees from your connected accounts.

You can’t set the payer type to `application_custom` or `application_express`
when you create connected accounts. They only apply to accounts created with
`type=custom` or `type=express`.

## List of fee behaviors for payer values

Product Categoryaccountapplicationapplication_customapplication_expressStripe
payment processing feesConnected AccountPlatformConnected AccountConnected
AccountInterchange Plus Payment FeesConnected
AccountPlatformPlatformPlatformDispute feesConnected AccountPlatformConnected
AccountConnected AccountInstant PayoutsConnected
AccountPlatformPlatformPlatformLPM Payment Failure FeesConnected
AccountPlatformConnected AccountConnected AccountPremium PayoutsConnected
AccountPlatformPlatformPlatformInvoicing and SubscriptionsConnected
AccountPlatformPlatformPlatformRadarConnected
AccountPlatformVariesVariesTerminal Add-onsConnected AccountPlatformConnected
AccountConnected AccountStripe TaxConnected AccountPlatformPlatformPlatform3D
SecureConnected AccountPlatformVariesVariesAdaptive AcceptanceConnected
AccountPlatformPlatformPlatformCard Account UpdaterConnected
AccountPlatformPlatformPlatformCheckout Add-onsConnected
AccountPlatformPlatformPlatformInstant bank account verificationsConnected
AccountPlatformPlatformPlatform

## Links

-
[controller.fees.payer](https://docs.stripe.com/api/accounts/create#create_account-controller-fees-payer)
- [Connect fees](https://stripe.com/connect/pricing)
- [Platform Reporting for direct charge payment fees paid by
platform](https://docs.stripe.com/connect/direct-charge-buy-rate-reporting-overview)