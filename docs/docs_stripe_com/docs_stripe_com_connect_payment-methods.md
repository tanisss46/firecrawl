# Adding payment method capabilities

## Onboard your connected accounts to accept different payment methods.

This guide provides an overview for existing platforms on how to check the
eligibility of connected accounts to accept different payment methods and apply
[capabilities](https://docs.stripe.com/connect/account-capabilities) to those
accounts using the Dashboard.

[Navigate to the Connected Account Payment Method Settings
Page](https://docs.stripe.com/connect/payment-methods#goto-settings-page)
To navigate to the settings page of the Payment methods for your connected
accounts, do the following:

- From the [Dashboard](https://dashboard.stripe.com/dashboard), in the upper
right corner, select **Settings > Connect > Payment Methods**.
- Under [Your connected
accounts](https://dashboard.stripe.com/settings/extensions/payment_methods),
select [Edit
Settings](https://dashboard.stripe.com/settings/payment_methods/connected_accounts).

Result: You can now manage the types of payment methods that users of your
connected account can accept.

[View
eligibility](https://docs.stripe.com/connect/payment-methods#view-eligibility)
From the connected accounts [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods), navigate to
the payment method you’re interested in.

Use the arrow on the left side of the payment method to expand the details of
the payment method. Within this view, you can see the eligibility of each of
your connected accounts to use the payment method.

#### Note

This view includes connected accounts that:

- Have processed a payment in the last 90 days and are older than 30 days.
- Are less than 30 days old, regardless of their payment activity.

Each connected account appears in one of four different categories:

CategoryDescriptionEnabledThese businesses already have the capability for this
payment method set to `active`.EligibleThese businesses have met all compliance
requirements and passed any relevant MCC checks to have the payment method
capability set to `active` when requested.Missing InfoThese businesses are
missing some compliance plan information needed to add the payment
method.IneligibleThese businesses aren’t eligible for the payment method, either
due to country location or MCC.
Countries you have connected accounts in that aren’t supported by the payment
method appear grayed out.

[Enable payment
method](https://docs.stripe.com/connect/payment-methods#enable-payment-method)
To enable the payment method for your connected accounts:

- Apply the [capability](https://docs.stripe.com/connect/account-capabilities)
to your connected accounts by selecting **On by default** from the top-level
dropdown located to the right of the payment method.
- *(Optional)* Edit the setting to `Off` for any countries where you want to
disable the payment method.
- Select **Review Changes** to confirm your selections.

After you review and confirm your update, Stripe converts all `Eligible`
connected accounts to `Enabled`, with a capability status of `active`. Stripe
also automatically applies the capability to new accounts as they become
eligible. This could happen because a new account signs up for your platform and
finishes inputting their information or because an account updates their
information to become eligible for the payment method, such as updating their
MCC from one that’s ineligible to one that’s eligible.

![The button to review
changes](https://b.stripecdn.com/docs-statics-srv/assets/review-changes.d8ab55ad8f1d32cf8502520366aa6de8.png)

Review changes

#### Private preview

The **embedded payment method settings component** allows connected accounts to
configure the payment methods they offer at checkout without the need to access
the Stripe Dashboard. [Request
access](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings#request-access)
and learn how to [integrate with Payment Method
Configurations](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings#integration).

[Gather required
information](https://docs.stripe.com/connect/payment-methods#gather-information)
Stripe doesn’t apply an enabled payment method to any accounts in the `Missing
Info` category. After you
[update](https://docs.stripe.com/connect/update-verified-information) the
account to provide the specific missing information for those accounts, Stripe
applies the capability.

[OptionalExport
list](https://docs.stripe.com/connect/payment-methods#export-list)
## See also

- [Account capabilities](https://docs.stripe.com/connect/account-capabilities)
- [Upgrading to dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods)

## Links

- [capabilities](https://docs.stripe.com/connect/account-capabilities)
- [Dashboard](https://dashboard.stripe.com/dashboard)
- [Settings](https://dashboard.stripe.com/settings)
- [Connect](https://dashboard.stripe.com/settings/connect)
- [Payment
Methods](https://dashboard.stripe.com/settings/connect/payment_methods)
- [Your connected
accounts](https://dashboard.stripe.com/settings/extensions/payment_methods)
- [Edit
Settings](https://dashboard.stripe.com/settings/payment_methods/connected_accounts)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Request
access](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings#request-access)
- [integrate with Payment Method
Configurations](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings#integration)
- [update](https://docs.stripe.com/connect/update-verified-information)
- [Upgrading to dynamic payment
methods](https://docs.stripe.com/connect/dynamic-payment-methods)