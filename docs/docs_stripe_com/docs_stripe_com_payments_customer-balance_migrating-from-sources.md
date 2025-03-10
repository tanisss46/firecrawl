# Migrating from Sources-based Credit Transfers

## Learn how to migrate your Sources-based ACH Credit Transfer payment method to USD Bank Transfers.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently integrate with ACH Credit Transfer payments using the
Sources API, you must [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning). We’ll send
email communications with more information about this end of support.

For information about migrating to USD Bank Transfer supported by the current
APIs, refer to the documentation below.

## Reasons to migrate

The bank transfers payment method adds many improvements compared to [ACH Credit
Transfers](https://docs.stripe.com/sources/ach-credit-transfer). It’s compatible
with Stripe [PaymentIntents](https://docs.stripe.com/api/payment_intents),
supports [Stripe Checkout](https://docs.stripe.com/payments/checkout), and the
Payment Element, and takes less effort to operate, reconcile, and refund.

### Impact of not migrating

Stripe plans to disable support for payment methods in the Sources API. If you
handle any payment methods using the Sources API, you must migrate them to the
Payment Methods API. We’ll provide further information about this end of support
through email.

### Impact on ACH Credit Transfers customers

When you migrate, Stripe keeps the same bank account information for customers
when you add bank transfers, making the process seamless for them. If you don’t
migrate, customers can still send funds using the legacy ACH Credit Transfer
product.

## Credit transfers versus Bank transfers

The following table details the differences between the new bank transfers
payment method and ACH Credit Transfers:

FeatureACH Credit TransferBank transfers[Checkout
Support](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=stripe-hosted)No
Yes [Payment Element
Support](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=elements)No
Yes [Dynamic payment methods
support](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)No
Yes RefundsRequire customer actionPartially automatedFunds land inSource[Cash
balance](https://docs.stripe.com/payments/customer-balance)APISourcesPayment
IntentsUnreconciled balancesMoved to your balanceReturned to the customer
### How Stripe migrates objects to support bank transfers

When you activate bank transfers, Stripe automatically enables your customer
objects to support the new cash balance, one of the primary features of the bank
transfers product.

- For a customer with no attached Credit Transfer Sources, Stripe provisions a
new virtual account number for the cash balance.
- For a customer with attached Credit Transfer Sources, Stripe consumes the
Credit Transfer Source object and moves the full remaining amount into the
customer’s cash balance. See new transfers sent by the customer to the Source
bank account number in the customer’s cash balance instead. The virtual account
number stays consistent throughout the migration process, and you don’t need to
communicate any new destinations to the customer. Single customers are
automatically migrated after you perform one of the following actions:- Request
of [Customer Balance Funding
Instructions](https://docs.stripe.com/payments/customer-balance/funding-instructions)
(recommended if you’re upgrading your integration)
- Confirmation of a `customer_balance` Payment Intent
- Creation of an invoice or subscription using bank transfers
- For [test mode](https://docs.stripe.com/test-mode) customers, [simulation of a
funding
transaction](https://docs.stripe.com/payments/bank-transfers/accept-a-payment#test-your-integration)
- After the migration process is complete, it’s no longer possible to delete the
customer. In return, we guarantee that funds sent to the virtual account at any
point in the future are added to the correct customer cash balance.

## Migrating your Connect integration

If your Connect platform integrates with Standard connected accounts using ACH
Credit Transfers, follow the steps in the [Connect integration
guide](https://docs.stripe.com/payments/customer-balance/standard-connect-migration).

## Migrating for Invoicing or Billing

If you’re using ACH Credit Transfer payments with Invoicing or Billing and want
to migrate, follow the steps in the [Invoicing migration
guide](https://docs.stripe.com/payments/customer-balance/invoicing-migration).

## Migration for a direct integration with the Sources or Charges API

If you’re using ACH Credit Transfers using the Sources API, follow the steps in
the [Sources migration
guide](https://docs.stripe.com/payments/customer-balance/direct-sources-migration).

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [ACH Credit Transfers](https://docs.stripe.com/sources/ach-credit-transfer)
- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Checkout
Support](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=stripe-hosted)
- [Payment Element
Support](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=elements)
- [Dynamic payment methods
support](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Cash balance](https://docs.stripe.com/payments/customer-balance)
- [Customer Balance Funding
Instructions](https://docs.stripe.com/payments/customer-balance/funding-instructions)
- [test mode](https://docs.stripe.com/test-mode)
- [simulation of a funding
transaction](https://docs.stripe.com/payments/bank-transfers/accept-a-payment#test-your-integration)
- [configured with
properties](https://docs.stripe.com/connect/update-to-typeless-connect)
- [Connect integration
guide](https://docs.stripe.com/payments/customer-balance/standard-connect-migration)
- [Invoicing migration
guide](https://docs.stripe.com/payments/customer-balance/invoicing-migration)
- [Sources migration
guide](https://docs.stripe.com/payments/customer-balance/direct-sources-migration)