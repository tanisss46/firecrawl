# Migrating your Standard Connect integration to USD Bank Transfers

## Learn how to migrate your ACH Credit Transfer Standard Connect integration to USD Bank Transfers.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently integrate with ACH Credit Transfers, you must [migrate
to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

For information about migrating to USD Bank Transfer supported by the current
APIs, refer to the documentation below.

## Reasons to migrate

If your Connect platform integrates with Standard connected accounts using ACH
Credit Transfers, you can migrate to USD Bank Transfers. USD Bank Transfers
enables your connected accounts to benefit from the most up-to-date bank
transfer processes. To learn more about the improvements we added to the USD
Bank Transfers product, see [Migrating from Sources-based Credit
Transfers](https://docs.stripe.com/payments/customer-balance/migrating-from-sources).

### Impact of not migrating

If you don’t migrate to Bank Transfers, you can continue to use the legacy ACH
Credit Transfer product. Legacy means we won’t add new functionality to the ACH
Credit Transfer going forward. To stay up to date, we recommend integrating with
USD Bank Transfers instead.

If you don’t migrate to Bank Transfers, Stripe prevents your connected accounts
from having compatibility issues:

- Users who are currently connected to your platform won’t be able to request
access to Bank Transfers through the Dashboard.
- Users who’ve used Bank Transfers with one or more customers won’t be able to
connect to your Stripe platform.

Stripe will remove these restrictions from your platform after your integration
is ready to accept Bank Transfer payments.

### Impact on the ACH Credit Transfers customers of your connected accounts

If you migrate, Stripe keeps the same bank account information for the customers
of your connected accounts, which streamlines the process for them. If you don’t
migrate, your connected account’s customers can still send funds using the
legacy ACH Credit Transfer product.

## Before you begin

- To confirm if you’re using the legacy ACH Credit Transfers product, see the
applicable **Before you begin** sections for:

- [Migrate from the Sources
API](https://docs.stripe.com/payments/customer-balance/direct-sources-migration)
- [Migrate with invoicing or
Billing](https://docs.stripe.com/payments/customer-balance/invoicing-migration)
- To confirm that you’re currently using Connect with Standard connected
accounts, navigate to the [Accounts
overview](https://dashboard.stripe.com/connect/accounts/overview) and [filter by
account
type](https://docs.stripe.com/connect/dashboard/viewing-all-accounts#filters).
If your Live mode account list includes Standard accounts with status
**Complete** or **Enabled** then you’re using Standard Connect.
- To confirm that you’re using [direct
charges](https://docs.stripe.com/connect/charges#direct) on Standard Connect,
verify the following:

- If you’re using the API to create charges, the request includes the connected
account ID as part of the `Stripe-Account` header.
- You create charges on the connected account rather than your Stripe account.
- The funds from these charges (minus Stripe’s fees) are directly available in
the connected account’s balance.
- If you’re not using ACH Credit Transfers with direct charges for Standard
connected accounts, this guide doesn’t apply to you. If you’re using ACH Credit
Transfers in other Connect configurations, see [Migrating from Sources-based
Credit
Transfers](https://docs.stripe.com/payments/customer-balance/migrating-from-sources).

## Migrate to Bank Transfers integration

Use this guide to build a Bank Transfers integration alongside your existing ACH
Credit Transfer integration. Use the new integration to migrate all the existing
ACH Credit Transfer customers of your connected accounts to the new payment
method.

[Create a test Standard connected
account](https://docs.stripe.com/payments/customer-balance/standard-connect-migration#create-test-standard)
[Create a test mode Standard connected
account](https://docs.stripe.com/connect/standard-accounts#create-account) for
the purpose of testing the new integration.

[Build a Bank Transfers
integration](https://docs.stripe.com/payments/customer-balance/standard-connect-migration#build-us-bank-transfers)Sources
APIInvoicing or Billing API- Create a test customer:

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d name="Jenny Rosen" \
 --data-urlencode email="jenny.rosen@example.com"
```
- Create an ACH Credit Transfer source and attach it to the customer

Complete the steps in the integration guide of [ACH Credit
Transfer](https://docs.stripe.com/sources/ach-credit-transfer). Make sure to
pass the `Stripe-Account` header in the API requests that create and attach the
source to the customer. Save the bank details of the Source from the
`ach_credit_transfer` field of the object to refer to later.
- Create and confirm a PaymentIntent

At this point, you’re able to create and confirm a bank transfers PaymentIntent
on the customer object of the connected account [following the respective step
in the Accept a payment
guide](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=direct-api#web-create-and-confirm-payment-intent).
The `Stripe-Account` header must be passed in order to create the PaymentIntent
on the customer of the connected account.

Creating a test mode `customer_balance` PaymentIntent always succeeds. However,
in live mode [direct charges](https://docs.stripe.com/connect/direct-charges)
require the connected account itself (not the platform) to have activated Bank
Transfers. Hence, before creating the PaymentIntent on the connected account,
the platform must use the [bank_transfer_payments
capability](https://docs.stripe.com/connect/account-capabilities#payment-methods)
to determine whether this is the case. If Bank Transfers isn’t activated, your
integration logic could fall back to the legacy ACH Credit Transfer payment
method.

```
import stripe

stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

def funding_instructions(connected_account: str, customer: stripe.Customer) ->
dict:
 bank_transfer_payments_capability = stripe.Account.retrieve_capability(
 connected_account,
 "us_bank_transfer_payments",
 )

 if bank_transfer_payments_capability["status"] == "active":
 pi = stripe.PaymentIntent.create(
 stripe_account=connected_account,
 amount=1099,
 currency="usd",
 customer=customer["id"],
 payment_method_types=["customer_balance"],
 payment_method_data={
 "type": "customer_balance",
 },
 payment_method_options={
 "customer_balance": {
 "funding_type": "bank_transfer",
 "bank_transfer": {
 "type": "us_bank_transfer",
 },
 },
 },
 confirm=True,
 )

 return pi.next_action["display_bank_transfer_instructions"]
 else:
 source = stripe.Source.retrieve(
 stripe_account=connected_account, id=customer["default_source"]
 )
 return source["ach_credit_transfer"]
```
- Confirm that the integration works

After you [test and confirm that the integration
works](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=direct-api#test-your-integration),
check if the bank details of the Credit Transfer Source have been migrated.
Navigate to the customer details page in the Dashboard, and then expand Cash
balance. The bank details of the Cash balance should match the ones obtained
from the Source in Step 2.

The customer of the connected account has been successfully migrated.
[Contact
Stripe](https://docs.stripe.com/payments/customer-balance/standard-connect-migration#contact-stripe)
After you’ve built, tested, and deployed your integration to production, and
have successfully served live traffic, **please reach out to Stripe to let us
know that your integration is compatible with Bank Transfers**. We’ll make sure
that your integration is working as expected and lift the restrictions imposed
on your connected accounts. We’ll also activate Bank Transfers for all your
connected accounts, which allows you to completely stop supporting the legacy
payment method.

## See also

- [Migrating from Sources-based Credit
Transfers](https://docs.stripe.com/payments/customer-balance/migrating-from-sources)

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [configured with
properties](https://docs.stripe.com/connect/update-to-typeless-connect)
- [Migrating from Sources-based Credit
Transfers](https://docs.stripe.com/payments/customer-balance/migrating-from-sources)
- [Migrate from the Sources
API](https://docs.stripe.com/payments/customer-balance/direct-sources-migration)
- [Migrate with invoicing or
Billing](https://docs.stripe.com/payments/customer-balance/invoicing-migration)
- [Accounts overview](https://dashboard.stripe.com/connect/accounts/overview)
- [filter by account
type](https://docs.stripe.com/connect/dashboard/viewing-all-accounts#filters)
- [direct charges](https://docs.stripe.com/connect/charges#direct)
- [Create a test mode Standard connected
account](https://docs.stripe.com/connect/standard-accounts#create-account)
- [ACH Credit Transfer](https://docs.stripe.com/sources/ach-credit-transfer)
- [following the respective step in the Accept a payment
guide](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=direct-api#web-create-and-confirm-payment-intent)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [bank_transfer_payments
capability](https://docs.stripe.com/connect/account-capabilities#payment-methods)
- [test and confirm that the integration
works](https://docs.stripe.com/payments/bank-transfers/accept-a-payment?payment-ui=direct-api#test-your-integration)