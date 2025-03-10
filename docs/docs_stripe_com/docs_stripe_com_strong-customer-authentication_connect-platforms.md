# SCA migration guide for Connect platforms

## Learn how to update your Connect platform for Strong Customer Authentication (SCA).

[Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) applies
to businesses based in the [European Economic
Area](https://en.wikipedia.org/wiki/European_Economic_Area) (EEA) that accept
online payments from customers located in the EEA. Many card payments require
additional authentication through [3D
Secure](https://docs.stripe.com/payments/3d-secure). As of September 14, 2019,
transactions that don’t follow the new authentication guidelines might be
declined by a customer’s bank.

You need to update your platform if you create any of the following charges:

- [Direct charges](https://docs.stripe.com/connect/direct-charges) on a
connected account based in the EEA.
- [Destination charges](https://docs.stripe.com/connect/destination-charges) if
the `on_behalf_of` parameter is set and specifies a connected account based in
the EEA.
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers) if
your platform is based in the EEA or if the `on_behalf_of` parameter is set and
specifies a connected account based in the EEA.
[Choose an SCA-ready
integration](https://docs.stripe.com/strong-customer-authentication/connect-platforms#choose-integration)
You need to update your Stripe integration to meet SCA requirements. For
example, SCA requires off-session payments to be authenticated when customers
enter payment details, and subsequent off-session payments might require
notifying the customer to return to the application to re-authenticate.

Choose [Stripe Checkout](https://docs.stripe.com/payments/checkout) if it
supports the features your integration requires. Checkout is a hosted payment
page that can be branded by businesses, supports recurring
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating), and
supports SCA for your connected accounts. It supports creating [direct
charges](https://docs.stripe.com/connect/direct-charges) and [destination
charges](https://docs.stripe.com/connect/destination-charges) for
[Connect](https://docs.stripe.com/connect).

If you want to build custom payments, use the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents) as the legacy Charges API
isn’t SCA-ready. The Payment Intents API supports the same set of Connect
features as the Charges API.

[Examine Connect-specific
changes](https://docs.stripe.com/strong-customer-authentication/connect-platforms#examine-connect-specific-changes)
### Destination charge changes

If you’re using the `destination`, `destination[account]`, or
`destination[amount]` parameters with the Charges API, note that these
parameters have been replaced with `transfer_data[destination]` and
`transfer_data[amount]` in both the Charges and the Payment Intents APIs. See
the following table for more information.

Use case Charges APIPayment Intents APIYour platform is the merchant of record,
but you wish to create a transfer to a connected account after the payment
completesNot possibleSet
[transfer_data[destination]](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-transfer_data-destination)
to the connected account’s IDYou want your connected account to be the
settlement merchant without creating a separate transfer after the payment
completesSet `on_behalf_of` to the connected account’s IDNo changeYou want your
connected account to be the settlement merchant and you wish to create a
transfer to that account after the payment completesSet `destination` or
`destination[account]` to the connected account’s IDSet
[transfer_data[destination]](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-transfer_data-destination)
and
[on_behalf_of](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-on_behalf_of)
to the connected account’s IDYou wish to collect an application feeSet
`application_fee` to the amount desiredSet
[application_fee_amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-application_fee_amount)
to the amount desiredYou wish to transfer a partial amount to your connected
account after the payment completesSet `destination[amount]` to the amount to
transferSet
[transfer_data[amount]](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-transfer_data)
to the amount to transfer
### 3D Secure and Radar rules

Stripe Checkout and the Payment Intents API triggers [dynamic 3D Secure
authentication](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
based on [Radar rules](https://docs.stripe.com/radar/rules). With Connect, the
rules you create only apply to payments created on the platform account.
Payments [created directly on the connected
account](https://docs.stripe.com/connect/direct-charges) are subject to the
connected account’s rules. Configure your default rules and test your
integration with [3D Secure test
cards](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-cards).

### SCA impact on saving payment methods

Under SCA, authentication is required when saving a card in order to collect
customer permission and qualify for [off-session
exemptions](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)
for subsequent off-session payments. To reduce the rate of customers having to
authenticate their payment method, update your integration to use off-session
payments with the Payment Intents API [in a checkout
flow](https://docs.stripe.com/payments/save-during-payment) or [outside the
checkout
flow](https://docs.stripe.com/payments/save-and-reuse?platform=checkout).

If you [clone saved payment
methods](https://docs.stripe.com/connect/cloning-customers-across-accounts) to
reuse across multiple connected accounts, sharing a payment method with a
connected account automatically shares customer permission as well. This allows
the platform to make off-session payments on any of their connected accounts
without requiring the customer to authenticate their payment method again.

[Determine whether connected accounts need to make
changes](https://docs.stripe.com/strong-customer-authentication/connect-platforms#connected-account-changes)
In most cases, after you update your payments integration for SCA, your
connected accounts don’t have to do any additional work.

If you provide your own payments API to your connected accounts in addition to
or on top of Stripe’s API, your connected accounts might need to make changes to
continue accepting payments on your platform. For example, if you run a
subscriptions platform on Stripe in which your connected accounts pass payment
information to you using your own API, and then you pass those payment details
to Stripe’s API, both APIs must be SCA-ready. If this is the case for your
platform, provide guidance to your connected accounts on any changes they need
to make.

[Implement and test the new integration
path](https://docs.stripe.com/strong-customer-authentication/connect-platforms#implement-changes)
After you have identified your integration path and determined if your connected
accounts need to make changes, follow the relevant migration guides for [Stripe
Checkout](https://docs.stripe.com/payments/checkout/migration), [Stripe
Billing](https://docs.stripe.com/billing/migration/strong-customer-authentication),
or the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration).

Once implementation is complete, configure your [Dynamic 3D Secure
rules](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
to test your integration using [3D Secure test
cards](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-cards).
Make sure to test both cases when the authentication is successful and
unsuccessful.

[Educate your connected
accounts](https://docs.stripe.com/strong-customer-authentication/connect-platforms#educate)
Finally, inform your connected accounts about how SCA can affect them and when
your platform will be SCA-ready, regardless of whether they need to [make any
changes](https://docs.stripe.com/strong-customer-authentication/connect-platforms#implement-changes).

In particular, provide them with the following information, tailored for your
business:

Strong [Customer](https://docs.stripe.com/api/customers) Authentication (SCA) is
a new European regulatory requirement to reduce fraud and make online payments
more secure. Since SCA took effect September 14, 2019, online payments require
additional customer authentication. Transactions that don’t adhere to the new
guidelines may be declined by your customers’ banks. This regulation applies to
transactions where both the business and the cardholder’s bank are located in
the European Economic Area (EEA).

If you’d like, you can also send along the [SCA
video](https://stripe.com/payments/strong-customer-authentication) and
[guide](https://stripe.com/guides/strong-customer-authentication).

### How your platform should support SCA

If you’re not migrating to an SCA-ready solution, reach out to any of your
connected accounts with significant business from European customers so they can
move to a new solution before experiencing declines due to SCA.

### Any actions your connected accounts need to take

If no action is required on their end, let your connected accounts know.
Similarly, if action is required, provide them with instructions on the
necessary changes.

### How SCA can affect their business

SCA changes the checkout flow for card payments. Payments that require
authentication ask for [3D Secure](https://docs.stripe.com/payments/3d-secure)
(often known by its brand names, “Verified by Visa” or “Mastercard SecureCode”),
which typically adds an extra step in which the cardholder must provide
additional information, such as a one-time passcode or biometric ID.

## Links

- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [Direct charges](https://docs.stripe.com/connect/direct-charges)
- [Destination charges](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Connect](https://docs.stripe.com/connect)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
-
[transfer_data[destination]](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-transfer_data-destination)
-
[on_behalf_of](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-on_behalf_of)
-
[application_fee_amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-application_fee_amount)
-
[transfer_data[amount]](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-transfer_data)
- [dynamic 3D Secure
authentication](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
- [Radar rules](https://docs.stripe.com/radar/rules)
- [3D Secure test
cards](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-cards)
- [off-session
exemptions](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)
- [in a checkout flow](https://docs.stripe.com/payments/save-during-payment)
- [outside the checkout
flow](https://docs.stripe.com/payments/save-and-reuse?platform=checkout)
- [clone saved payment
methods](https://docs.stripe.com/connect/cloning-customers-across-accounts)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout/migration)
- [Stripe
Billing](https://docs.stripe.com/billing/migration/strong-customer-authentication)
- [Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration)
- [Customer](https://docs.stripe.com/api/customers)
- [SCA video](https://stripe.com/payments/strong-customer-authentication)
- [guide](https://stripe.com/guides/strong-customer-authentication)