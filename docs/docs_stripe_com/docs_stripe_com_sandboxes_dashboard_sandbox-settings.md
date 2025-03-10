# Sandbox settingsDeveloper preview

## Learn about how settings work in sandboxes.

#### Private developer preview

Sandboxes is currently in private developer preview. Join [Stripe
Insiders](https://insiders.stripe.dev/c/sandboxes/6), our new early access
program, to register your interest in joining the Sandboxes preview.

When creating a sandbox, you must choose your starting configuration.

To copy settings and capabilities from your existing account, click **Create
sandbox** > **Preconfigured**. Stripe provides placeholder business data to help
you start testing most Stripe features. This sandbox includes placeholder data
in the same country as your existing account.

To create a blank sandbox where nothing is copied from your existing account,
click **Create sandbox** > **Blank configuration**.

Starting with the same settings and capabilities as your existing account
eliminates the need to spend time manually verifying that your sandboxes behave
like your existing account. We don’t synchronize settings and capabilities. As a
result, they can diverge from live settings and capabilities at any time. This
allows for testing how settings and capabilities changes affect integration
behavior. See the
[settings](https://docs.stripe.com/sandboxes/dashboard/sandbox-settings#payment-settings)
and
[capabilities](https://docs.stripe.com/sandboxes/dashboard/sandbox-settings#account-capabilities)
copied when you choose the **Preconfigured** option.

### Create a sandbox with a country different from your live account

To create a sandbox with a country different from your live account, choose the
**Blank** configuration. Then, set the country in the **Account details** tab of
the sandbox’s **Business settings**.

## Payments settings

To open your payments settings, click **Settings** in the top right corner of
the Dashboard, then click **Payments**. Stripe excludes a subset of the payments
settings when you’re setting up a new sandbox with the **Preconfigured**
configuration. These include:

Payment settings pageFunctionality`Checkout and Payment Links`Stripe doesn’t
copy the `Conversion testing program` setting. To join this program, adjust this
setting in your live account.`Payment methods`Stripe enables all payment methods
that are enabled or pending in your live account. We automatically enable some
payment methods for testing purposes.`Payment method domains`Stripe doesn’t copy
domains from your live account. You must add a new domain to test it in a
sandbox.
## Billing settings

To open your billing settings, click **Settings** in the top right corner of the
Dashboard, then click **Billing**. Stripe excludes a subset of the billing
settings when you’re setting up a new sandbox with the **Preconfigured**
configuration. These include:

Billing settings pageFunctionality`Customer portal`Stripe doesn’t copy domains
from your live account. You must add a new domain to test it in a
sandbox.`Automations`Stripe doesn’t copy automations or their states from your
live account.
## Connect settings

To open your Connect settings, click **Settings** in the top right corner of the
Dashboard, then click **Connect**. Stripe excludes a subset of the Connect
settings when you’re setting up a new sandbox with the **Preconfigured**
configuration. These include:

Connect settings pageFunctionality`Onboarding options - OAuth`Stripe doesn’t
copy redirect URIs from your live platform. You must add a redirect URI to test
it in a sandbox.`Onboarding options - Tax`Stripe only copies these settings if
Tax is enabled on your live platform.`Tax reporting`Stripe only copies these
settings if Tax is enabled on your live platform.`Emails`Stripe doesn’t copy
email domains from your live platform. You must add a new email domain to test
it in a sandbox.
## Business settings

To open your business settings, click **Settings** in the top right corner of
the Dashboard, then click **Business**. Stripe excludes a subset of the Business
settings when you’re setting up a new sandbox with the **Preconfigured**
configuration. These include:

Business settings pageFunctionality`Custom domains`Stripe doesn’t copy domains
from your live account. You must add a new domain to test it in a
sandbox.`Public details`Stripe doesn’t copy domains from your live account.
Instead, we add placeholder domains to enable payments in a sandbox.
## Account capabilities

The account capabilities listed below are copied when you set up a new sandbox
with the **Preconfigured** configuration.

CapabilityFunctionality`payouts`A sandbox is configured to perform
[payouts](https://docs.stripe.com/treasury/moving-money/payouts#payouts).`link_payments`A
sandbox is configured to process [Link](https://docs.stripe.com/payments/link)
payments.`affirm_payments`A sandbox is configured to process
[Affirm](https://docs.stripe.com/payments/affirm)
payments.`us_bank_account_ach_payments`A sandbox is configured to process [ACH
Direct Debit](https://docs.stripe.com/payments/ach-direct-debit)
payments.`afterpay_clearpay_payments`A sandbox is configured to process
[Afterpay Clearpay](https://docs.stripe.com/payments/afterpay-clearpay)
payments.`p24_payments`A sandbox is configured to process
[P24](https://docs.stripe.com/payments/p24) payments.`transfers`A sandbox is
configured to [transfer
funds](https://docs.stripe.com/connect/account-capabilities#transfers) as a
Connect platform to connected accounts.

## Links

- [Stripe Insiders](https://insiders.stripe.dev/c/sandboxes/6)
- [payouts](https://docs.stripe.com/treasury/moving-money/payouts#payouts)
- [Link](https://docs.stripe.com/payments/link)
- [Affirm](https://docs.stripe.com/payments/affirm)
- [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit)
- [Afterpay Clearpay](https://docs.stripe.com/payments/afterpay-clearpay)
- [P24](https://docs.stripe.com/payments/p24)
- [transfer
funds](https://docs.stripe.com/connect/account-capabilities#transfers)