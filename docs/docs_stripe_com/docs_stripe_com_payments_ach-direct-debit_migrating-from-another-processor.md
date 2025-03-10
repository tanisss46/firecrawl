# Migrating from another processor

## Migrate verified bank accounts from another payment processor with the Payment Methods API.

If you have verified bank accounts that you’ve used to process ACH Direct Debit
payments on another processor, you can migrate them to Stripe to begin accepting
payments.

You and Stripe both share responsibility for maintaining proof of authorization
to debit, as well as verification of the bank account.

## Request a data migration with Stripe

Stripe works with you and your current payment processor to migrate data into
your Stripe account. After the import completes, Stripe provides you with a CSV
or JSON Mapping File to help you match the old customer IDs to the imported
Stripe object IDs.

To request this option, submit an [intake
form](https://support.stripe.com/contact/email?topic=migrations) and select the
ACH payment type.

## Manually migrate bank accounts from another payment processor

If you choose to migrate yourself, Stripe temporarily allows you to bypass bank
account verification. To request this temporary capability, contact [Stripe
support](https://support.stripe.com/contact) and include details about how your
business:

- Collects authorization from customers
- Verifies customer bank accounts

After Stripe enables this option, process each bank account and create a
[SetupIntent](https://docs.stripe.com/api/setup_intents) for each account:

- Create a new [Customer object](https://docs.stripe.com/api/customers) or
retrieve an existing one to associate with this bank account.

```
curl -X POST https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

- Create and confirm a SetupIntent with your saved bank account details and the
date of your customer’s original authorization to debit the account.

```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "payment_method_types[]"=us_bank_account \
 -d customer={{CUSTOMER_ID}} \
 -d confirm=true \
 -d "payment_method_options[us_bank_account][verification_method]"=skip \
 -d "payment_method_data[type]"=us_bank_account \
 -d "payment_method_data[billing_details][name]"={{ACCOUNT_HOLDER_NAME}} \
 -d "payment_method_data[us_bank_account][routing_number]"={{ROUTING_NUMBER}} \
 -d "payment_method_data[us_bank_account][account_number]"={{ACCOUNT_NUMBER}} \
 -d "payment_method_data[us_bank_account][account_holder_type]"=individual \
 -d "mandate_data[customer_acceptance][type]"=offline \
 -d "mandate_data[customer_acceptance][accepted_at]"=1692821946
```

- Retrieve and store the [PaymentMethod
ID](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method)
from the response to use for [future
payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#web-future-payments).
You can also retrieve it by
[listing](https://docs.stripe.com/api/payment_methods/list) all PaymentMethods
for the customer.

## Links

- [intake form](https://support.stripe.com/contact/email?topic=migrations)
- [Stripe support](https://support.stripe.com/contact)
- [SetupIntent](https://docs.stripe.com/api/setup_intents)
- [Customer object](https://docs.stripe.com/api/customers)
- [PaymentMethod
ID](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method)
- [future
payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#web-future-payments)
- [listing](https://docs.stripe.com/api/payment_methods/list)