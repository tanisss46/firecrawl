# Migrating from the Charges API

## Upgrade to the Payment Intents API.

If you previously collected customer payment details with Stripe using the [Bank
Accounts API](https://docs.stripe.com/ach-deprecated), you can continue using
the saved `BankAccount` as a
[PaymentMethod](https://docs.stripe.com/api/payment_methods). You can use
customer [bank accounts](https://docs.stripe.com/api/customer_bank_accounts)
with the [Payment Intents API](https://docs.stripe.com/api/payment_intents)
after you meet the following requirements:

- The customer’s bank account has been verified.
- An [active
mandate](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges#mandate-acknowledgement)
exists for that bank account.

## Compatibility with the Bank Accounts API

### Create a PaymentIntent with a Bank Account

[Bank Accounts](https://docs.stripe.com/api/customer_bank_accounts) that are
already [verified](https://docs.stripe.com/ach-deprecated#verifying) and have
been attached to a [Customer](https://docs.stripe.com/api/customers) are usable
in any API that accepts a `PaymentMethod` object. You can use a saved
`BankAccount` as a [PaymentMethod](https://docs.stripe.com/api/payment_methods)
when creating a PaymentIntent. This eliminates the need to recollect payment
details. However, make sure that you also [update your
integration](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment)
to begin creating PaymentMethods instead.

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=1099 \
 -d "currency"="usd" \
 -d "customer"="{{CUSTOMER_ID}}" \
 -d "payment_method_types[]"="us_bank_account" \
 -d "payment_method"="{{BANK_ACCOUNT_ID}}"
```

Similarly, you can use a saved BankAccount as a PaymentMethod when creating a
SetupIntent.

```
curl https://api.stripe.com/v1/setup_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"="us_bank_account" \
 -d "customer"="{{CUSTOMER_ID}}" \
 -d "payment_method"="{{BANK_ACCOUNT_ID}}"
```

### Collect mandate acknowledgement

Confirming a PaymentIntent or SetupIntent requires having your customer
authorize a
[mandate](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-mandate_data)
to debit the account. Learn more about [SEC
codes](https://docs.stripe.com/payments/ach-direct-debit/sec-codes) to
understand which authorization type is right for your business.

In some cases, you might have pre-authorization from your customer from an
earlier purchase or SetupIntent that you can use to create an off-session
payment. For example:

- If you previously collected an online mandate from the customer, you can use
both the IP address and user agent information to create a mandate object.
- If you previously collected payment and mandate information offline on paper,
you can create a [PPD
mandate](https://docs.stripe.com/payments/ach-direct-debit/sec-codes#ppd-sec-code).

To create an off-session payment, you can use offline mandate acceptance to
provide a record of your customer’s original authorization.

Authorization is only required the first time you use a `BankAccount` object
with the PaymentIntents API. After that, you can use the `BankAccount` object as
a PaymentMethod to [accept future
payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#web-future-payments).

```
curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/confirm \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "mandate_data[customer_acceptance][type]"="offline" \
-d "mandate_data[customer_acceptance][accepted_at]"="{{ACCEPTANCE_TIMESTAMP}}" \
-d
"payment_method_options[us_bank_account][mandate_data][collection_method]"="paper"
```

### Retrieving a BankAccount as a PaymentMethod

You can retrieve saved BankAccounts through the [Payment Methods
API](https://docs.stripe.com/api/payment_methods).

```
curl https://api.stripe.com/v1/payment_methods/ba_1IsleZ2eZvKYlo2CI3To1g72 \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

When using a BankAccount as a PaymentMethod, no new objects are created. The
Payment Methods API simply provides a different view of the same underlying
object.

PaymentMethod ViewBankAccount View
```
{
 "id": "ba_1IsleZ2eZvKYlo2CI3To1g72",
 "object": "payment_method",
 "billing_details": {
 "address": {
 "city": null,
 "country": null,
 "line1": null,
 "line2": null,
 "postal_code": null,
 "state": null
 },
 "email": null,
 "name": "Jenny Rosen",
 "phone": null
 },
 "us_bank_account": {
 "last4": "6789",
 "routing_number": "110000000",
 "fingerprint": "1JWtPxqbdX5Gamtc",
 "account_holder_type": "individual",
 "bank_name": "STRIPE TEST BANK",
 },
 "created": 123456789,
 "customer": "cus_CY5bH92D99f4mn",
 "livemode": false,
 "metadata": {},
 "type": "us_bank_account"
}
```

## Links

- [Bank Accounts API](https://docs.stripe.com/ach-deprecated)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [bank accounts](https://docs.stripe.com/api/customer_bank_accounts)
- [Payment Intents API](https://docs.stripe.com/api/payment_intents)
- [verified](https://docs.stripe.com/ach-deprecated#verifying)
- [Customer](https://docs.stripe.com/api/customers)
- [update your
integration](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment)
-
[mandate](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-mandate_data)
- [SEC codes](https://docs.stripe.com/payments/ach-direct-debit/sec-codes)
- [PPD
mandate](https://docs.stripe.com/payments/ach-direct-debit/sec-codes#ppd-sec-code)
- [accept future
payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment#web-future-payments)