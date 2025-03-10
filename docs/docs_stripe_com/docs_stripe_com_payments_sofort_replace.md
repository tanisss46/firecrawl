# Remove and replace SOFORT in your integration

## Learn how to discontinue SOFORT as a payment method and discover suitable alternatives.

#### Warning

New businesses can’t accept SOFORT payments and our financial partners are in
the process of discontinuing SOFORT. For more information, read our [support
page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method).

Effective March 31, 2025 , Stripe is discontinuing support for SOFORT as a
separate payment method for any business on Stripe. You must remove SOFORT
before March 31, 2025 to avoid any SOFORT payment failures.

#### Deadline extended

Our financial partner extended the original November 29, 2024 deadline for
discontinuing SOFORT as a standalone payment method to March 31, 2025 to give
Stripe users more time to make updates to their integration.

This guide provides instructions to:

- Remove SOFORT from your current payment integration.
- Explore alternative payment methods for your business and region. These
include [Klarna’s](https://docs.stripe.com/payments/klarna) “pay in full"
(previously known as “Pay Now”) payment option.
[Remove SOFORT from your payments
integration](https://docs.stripe.com/payments/sofort/replace#remove-sofort)
Removing SOFORT as a payment method affects several aspects of your integration
and customer communication. The following sections outline key impact areas,
some of which might not apply to your business.

### Update your payments integration

The steps to remove SOFORT depend on which type of integration you use. If
you’re using dynamic payment methods with any of Stripe’s prebuilt payment UIs
(Checkout, Payment Element, Invoicing, Payment Links), Stripe automatically
hides SOFORT from the UI.

Integration typeRemoval stepsPayment Element (mobile and web)- Remove `sofort`
from the `payment_method_types` specified at [PaymentIntent
creation](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types).
- Stop sending `sofort` as the selected payment method type at
[confirmation](https://docs.stripe.com/js/payment_intents/confirm_sofort_payment).
Stripe CheckoutRemove `sofort` from the `payment_method_types` specified at
[CheckoutSession
creation](https://docs.stripe.com/payments/sofort/accept-a-payment?web-or-mobile=web&payment-ui=stripe-hosted#accept-a-payment).Stripe
InvoicingRemove `sofort` from the `payment_settings.payment_method_types`
specified at the invoice’s [PaymentIntent
creation](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings-payment_method_types).Direct
API- Remove `sofort` from the `payment_method_types` specified at [PaymentIntent
creation](https://docs.stripe.com/payments/sofort/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#create-payment-intent)(or
from the sources types, if you’re using the [Sources
API](https://docs.stripe.com/api/sources/object#source_object-type)).
- Remove SOFORT from available options in your checkout.

### Update future payments and subscriptions

If you use [SOFORT to set up future
payments](https://docs.stripe.com/payments/sofort/set-up-payment) or process
recurring payments using SEPA Direct Debit, you must also update those
integration paths to prevent future payments from using SOFORT.

#### Note

Existing SEPA direct debit [mandates](https://docs.stripe.com/api/mandates)
initiated by SOFORT payments remain active, since SEPA Direct Debit and SOFORT
are distinct payment methods.

Integration typeRemoval stepsPayment Element (mobile and web)- Remove `sofort`
from the `payment_method_types` specified at [PaymentIntent
creation](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
for any subscriptions.
- Remove `sofort` from the `payment_method_types` specified at [SetupIntent
creation](https://docs.stripe.com/payments/sofort/save-during-payment?platform=web#create-payment-intent)
for future off-session payments.
Stripe CheckoutRemove `sofort` from the `payment_method_types` specified at
[CheckoutSession
creation](https://docs.stripe.com/payments/sofort/accept-a-payment?web-or-mobile=web&payment-ui=stripe-hosted#accept-a-payment).Stripe
InvoicingRemove `sofort` from the `payment_settings.payment_method_types`
specified at the invoice’s [PaymentIntent
creation](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings-payment_method_types)
for recurring invoices.Direct API- Remove `sofort` from the
`payment_method_types` specified at [PaymentIntent
creation](https://docs.stripe.com/payments/sofort/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#create-payment-intent)(or
from the sources types, if you’re using the [Sources
API](https://docs.stripe.com/api/sources/object#source_object-type)) for any
subscriptions.
- Remove `sofort` from the `payment_method_types` specified at [SetupIntent
creation](https://docs.stripe.com/payments/sofort/save-during-payment?platform=web#create-payment-intent)
for future off-session payments.
- Remove SOFORT from available options in your checkout.

### Update Connect platform integrations

To discontinue SOFORT for platforms, connectors, or Stripe apps, you must update
your payments and onboarding integrations.

- For new connected accounts, in the Payment methods settings page of your
[Dashboard](https://dashboard.stripe.com/settings/connect/payment_methods),
choose **Edit settings** for your connected accounts, then set **Off by
default** for SOFORT to block connected accounts from re-requesting the
`sofort_payments`
[capability](https://docs.stripe.com/connect/account-capabilities).
- Update your support articles, dashboard, and documentation to advise your
users that SOFORT is no longer available.

### Refunds

Refunds continue to process as normal beyond the discontinuation date. SOFORT
payments support refunds up to 180 days after the original payment.

### Disputes

SOFORT doesn’t support disputes. Any disputes raised on SEPA direct debits
payments are subject to the [SEPA Direct Debit dispute
process](https://docs.stripe.com/payments/sepa-debit#disputed-payments).

[Migrate your payment flow to an alternative payment
method](https://docs.stripe.com/payments/sofort/replace#alternative-payment-methods)
Stripe offers many payment method options that might be suitable alternatives to
SOFORT. How you integrate alternative payment methods depends on:

- Which payment method you choose to migrate to from SOFORT. For example:-
Klarna’s “Pay Now” payment option enabling bank transfer payments is the closest
payment flow to SOFORT.
- We also support [Pay By Bank](https://docs.stripe.com/payments/pay-by-bank) in
the UK and we’re collecting early interest in expansion to Germany.
- How you use Stripe: are you a platform or marketplace, or a connector or app
developer?
- Your payments integration: do you use a Stripe UI or a custom API integration?

### Compare alternative payment methods

We’ve included a high-level comparison to help you review your options. For
information about integrating any of these alternatives, click the payment
method column heading to see its complete documentation.

SOFORT[Klarna](https://docs.stripe.com/payments/klarna) Recommended[SEPA Direct
Debit](https://docs.stripe.com/payments/sepa-debit)[Bank
Transfers](https://docs.stripe.com/payments/bank-transfers)SummarySOFORT
redirects customers to their bank’s portal to authenticate the payment, and it
typically takes 2 to 14 days to receive notification of success or
failure.Klarna is a global payment method that also offers a “pay in full”
option leveraging SOFORT to support its bank transfers.SEPA Direct Debit is a
reusable, delayed notification payment method.Bank transfers is a push payment
method requiring buyers to log in to their bank outside of the context of the
checkout to push a payment to a virtual IBAN.Payment
confirmationCustomer-initiatedCustomer-initiatedBusiness-initiatedBusiness-initiatedRecurring
paymentsYes, with SEPA Direct DebitYes Private PreviewSign upYesYesPayout
timingStandard payout timing applies.Standard payout timing applies.Standard
payout timing applied at 35,000 USD of SEPA Direct Debit volume. Below this
threshold, 5 business days.Standard payout timing applies.Connect
supportYesYesYesYesDispute supportNoYesYes1NoManual capture
supportNoNoRefunds / Partial refundsYes / YesYes / YesYes / YesYes / Yes
(except for international wires)
1 Automatically honored up to 8 weeks after the account debit.

## Links

- [support
page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method)
- [Klarna’s](https://docs.stripe.com/payments/klarna)
- [PaymentIntent
creation](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
-
[confirmation](https://docs.stripe.com/js/payment_intents/confirm_sofort_payment)
- [CheckoutSession
creation](https://docs.stripe.com/payments/sofort/accept-a-payment?web-or-mobile=web&payment-ui=stripe-hosted#accept-a-payment)
- [PaymentIntent
creation](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings-payment_method_types)
- [PaymentIntent
creation](https://docs.stripe.com/payments/sofort/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#create-payment-intent)
- [Sources API](https://docs.stripe.com/api/sources/object#source_object-type)
- [SOFORT to set up future
payments](https://docs.stripe.com/payments/sofort/set-up-payment)
- [mandates](https://docs.stripe.com/api/mandates)
- [SetupIntent
creation](https://docs.stripe.com/payments/sofort/save-during-payment?platform=web#create-payment-intent)
- [Dashboard](https://dashboard.stripe.com/settings/connect/payment_methods)
- [capability](https://docs.stripe.com/connect/account-capabilities)
- [SEPA Direct Debit dispute
process](https://docs.stripe.com/payments/sepa-debit#disputed-payments)
- [Pay By Bank](https://docs.stripe.com/payments/pay-by-bank)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit)
- [Bank Transfers](https://docs.stripe.com/payments/bank-transfers)