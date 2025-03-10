# Save details for future payments with ACH Direct Debit

## Learn how to save payment method details for future ACH Direct Debit payments.

Stripe-hosted pageAdvanced integrationiOSAndroidReact Native
You can use Checkout in [setup
mode](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-mode)
to collect payment method details in advance, with the final amount or payment
date determined later. This is useful for:

- Saving payment methods to a wallet to streamline future purchases
- Collecting surcharges after fulfilling a service
- Starting a free trial for a
[subscription](https://docs.stripe.com/billing/subscriptions/creating)

#### Note

ACH Direct Debit is a [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method, which means that funds aren’t immediately available after
payment. A payment typically takes 4 business days to arrive in your account.

## Before you begin

This guide shows you how to extend the foundational [set up future
payments](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=stripe-hosted)
Checkout integration to add support for ACH Direct Debit payments.

[Create or retrieve a
customerRecommendedServer-side](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#web-create-customer)
Create a [Customer](https://docs.stripe.com/api/customers) object when your user
creates an account with your business, or retrieve an existing Customer
associated with this user. Associating the ID of the Customer object with your
own internal representation of a customer enables you to retrieve and use the
stored payment method details later. Include an email address on the Customer to
enable Financial Connections’ [return user
optimization](https://docs.stripe.com/financial-connections/fundamentals#return-user-optimization).

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d email={{CUSTOMER_EMAIL}}
```

[Enable ACH Direct Debit as a payment
method](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#setup-a-payment)
When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `us_bank_account` to the list of `payment_method_types`.
- Make sure all your `line_items` use the `usd` currency.
- Set the `permissions` parameter to include `payment_method`.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=setup \
 -d customer={{CUSTOMER_ID}} \
 -d "payment_method_types[]"=card \
 -d "payment_method_types[]"=us_bank_account \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

By default, collecting bank account payment information uses [Financial
Connections](https://docs.stripe.com/financial-connections) to instantly verify
your customer’s account, with a fallback option of manual account number entry
and microdeposit verification. See the [Financial Connections
docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments)
to learn how to configure Financial Connections and access additional account
data to optimize your ACH integration. For example, you can use Financial
Connections to check an account’s balance before initiating the ACH payment.

#### Note

To expand access to additional data after a customer authenticates their
account, they must re-link their account with expanded permissions.

During the Checkout session, the customer sees a dialog that gives them the
option to use instant verification or provide bank account details for
microdeposit verification.

If the customer opts for microdeposit verification, Stripe automatically sends
two small deposits to the provided bank account. These deposits can take 1-2
business days to appear on the customer’s online bank statement. When the
deposits arrive, the customer receives an email with a link to confirm these
amounts and verify the bank account with Stripe. After verification completes,
the payment begins processing.

[Test your
integration](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#test-integration)
Learn how to test scenarios with instant verifications using [Financial
Connections](https://docs.stripe.com/financial-connections/testing#web-how-to-use-test-accounts).

### Send transaction emails in test mode

After you collect the bank account details and accept a mandate, send the
mandate confirmation and microdeposit verification emails in test mode. To do
this, provide an email in the `payment_method_data.billing_details[email]` field
in the form of `{any-prefix}+test_email@{any_domain}` when you collect the
[payment method
details](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#web-collect-details).

#### Common mistake

You need to [activate your Stripe
account](https://docs.stripe.com/get-started/account/activate) before you can
trigger these emails in Test mode.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can
use to make sure your integration for manually-entered bank accounts is ready
for production.

Account numberTokenRouting
numberBehavior`000123456789``pm_usBankAccount_success``110000000`The payment
succeeds.`000111111113``pm_usBankAccount_accountClosed``110000000`The payment
fails because the account is
closed.`000111111116``pm_usBankAccount_noAccount``110000000`The payment fails
because no account is
found.`000222222227``pm_usBankAccount_insufficientFunds``110000000`The payment
fails due to insufficient
funds.`000333333335``pm_usBankAccount_debitNotAuthorized``110000000`The payment
fails because debits aren’t
authorized.`000444444440``pm_usBankAccount_invalidCurrency``110000000`The
payment fails due to invalid
currency.`000666666661``pm_usBankAccount_failMicrodeposits``110000000`The
payment fails to send
microdeposits.`000555555559``pm_usBankAccount_dispute``110000000`The payment
triggers a dispute.`000000000009``pm_usBankAccount_processing``110000000`The
payment stays in processing indefinitely. Useful for testing [PaymentIntent
cancellation](https://docs.stripe.com/api/payment_intents/cancel).`000777777771``pm_usBankAccount_weeklyLimitExceeded``110000000`The
payment fails due to payment amount causing the account to exceed its weekly
payment volume limit.
Before test transactions can complete, you need to verify all test accounts that
automatically succeed or fail the payment. To do so, use the test microdeposit
amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts *or* 0.01
descriptor code values.

Microdeposit values0.01 descriptor code valuesScenario`32` and
`45`SM11AASimulates verifying the account.`10` and `11`SM33CCSimulates exceeding
the number of allowed verification attempts.`40` and `41`SM44DDSimulates a
microdeposit timeout.[Use the payment
method](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#use-the-payment-method)
After completing the Checkout Session, you can
[collect](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=stripe-hosted#retrieve-checkout-session)
the [PaymentMethod](https://docs.stripe.com/api/payment_methods) ID. You can use
these PaymentMethod IDs to initiate future payments without having to prompt the
customer for their bank account a second time.

When [creating a
PaymentIntent](https://docs.stripe.com/api/payment_intents/create), provide the
`payment_method` and customer IDs to charge your customer using their saved bank
account information.

[OptionalInstant only
verification](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#instant-only-verification)[OptionalAccess
data on a Financial Connections bank
account](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#access-data-on-a-financial-connections-bank-account)[OptionalUpdating
the default payment
method](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#update-default-payment-method)

## Links

- [setup
mode](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-mode)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [set up future
payments](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=stripe-hosted)
- [Customer](https://docs.stripe.com/api/customers)
- [return user
optimization](https://docs.stripe.com/financial-connections/fundamentals#return-user-optimization)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [pricing details](https://stripe.com/financial-connections#pricing)
- [Financial Connections](https://docs.stripe.com/financial-connections)
- [Financial Connections
docs](https://docs.stripe.com/financial-connections/ach-direct-debit-payments)
- [Financial
Connections](https://docs.stripe.com/financial-connections/testing#web-how-to-use-test-accounts)
- [activate your Stripe
account](https://docs.stripe.com/get-started/account/activate)
- [PaymentIntent
cancellation](https://docs.stripe.com/api/payment_intents/cancel)
-
[collect](https://docs.stripe.com/payments/checkout/save-and-reuse?payment-ui=stripe-hosted#retrieve-checkout-session)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [creating a PaymentIntent](https://docs.stripe.com/api/payment_intents/create)