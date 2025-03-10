# Migrate to USD bank transfers from a Direct Integration using the Sources or Charges API

## Learn how to migrate your Sources API integration to USD Bank Transfers.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently integrate with ACH Credit Transfers, you must [migrate
to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

For information about migrating to USD Bank Transfer supported by the current
APIs, refer to the documentation below.

See [Migrating from Sources-based Credit
Transfers](https://docs.stripe.com/payments/customer-balance/migrating-from-sources)
if you want to learn about the reasons to migrate.

## Before you begin

Confirm if you’re currently using the legacy ACH Credit Transfers product:

- Navigate to the list of payment methods in your [Payment Method
settings](https://dashboard.stripe.com/settings/payment_methods), and click the
**Eligible** tab. If you don’t see ACH Credit Transfers in this list, you’re not
using the ACH Credit Transfer product.
- If ACH Credit Transfers is displayed in the list of available payment methods,
check to see if you pass the `ach_credit_transfer` payment method type when
integrating with the Sources API. If you’re not passing this payment method
type, you’re not using the ACH Credit Transfer product.

If you’re not using ACH Credit Transfers with the Sources or Charges API, you
can skip this guide because it doesn’t apply to you.

[Activate USD bank
transfers](https://docs.stripe.com/payments/customer-balance/direct-sources-migration#activate-bank-transfers)
To turn on bank transfer payments, navigate to your [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

[OptionalTest bank transfers with an individual
customer](https://docs.stripe.com/payments/customer-balance/direct-sources-migration#activate-us-bank-transfers)
Before you migrate, you can test bank transfers:

- Create a test customer with a Credit Transfer source attached. Complete the
steps in the integration guide of [ACH Credit
Transfer](https://docs.stripe.com/sources/ach-credit-transfer). Save the bank
details of the Source from the `ach_credit_transfer` field of the object to
refer to later.
- Build the new Bank Transfers integration on Payment Intents by following the
[Accept a
Payment](https://docs.stripe.com/payments/bank-transfers/accept-a-payment) guide
with the test customer you created above. Your integration now supports Bank
Transfers on Payment Intents, while still supporting the existing implementation
on Sources.
- After you [test and confirm that the integration
works](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=direct-api#test-your-integration),
confirm if the bank details of the Credit Transfer Source have been migrated.
Navigate to the customer details page in the Dashboard, and then expand **Cash
balance**.
- Click **View balance details** to find the funding instructions of the
customer and confirm that they match the bank details of the Credit Transfer
Source. You can also use the [Funding Instructions
API](https://docs.stripe.com/payments/customer-balance/funding-instructions) to
get the funding instructions.
[Drop the legacy
integration](https://docs.stripe.com/payments/customer-balance/direct-sources-migration#drop-legacy-integration)
After you verify that the migration works for individual customers in both test
and live mode, remove your Sources or Charges API integration. You can now rely
entirely on the Bank Transfers integration on Payment Intents.

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [Migrating from Sources-based Credit
Transfers](https://docs.stripe.com/payments/customer-balance/migrating-from-sources)
- [Payment Method
settings](https://dashboard.stripe.com/settings/payment_methods)
- [ACH Credit Transfer](https://docs.stripe.com/sources/ach-credit-transfer)
- [Accept a
Payment](https://docs.stripe.com/payments/bank-transfers/accept-a-payment)
- [test and confirm that the integration
works](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=direct-api#test-your-integration)
- [Funding Instructions
API](https://docs.stripe.com/payments/customer-balance/funding-instructions)