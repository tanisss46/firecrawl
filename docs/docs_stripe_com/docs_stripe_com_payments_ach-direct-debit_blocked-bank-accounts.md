# Blocked bank accounts

## Learn how to unblock ACH debit bank accounts and avoid future payment failures from blocked accounts.

Bank accounts can become blocked for reasons other than insufficient funds, and
can become blocked for legitimate reasons or because of an error. You can
minimize the chances of an account being blocked, and you can take actions to
unblock accounts if you understand the underlying reasons.

## Reasons for blocked bank accounts

When ACH Debits are returned for reasons other than insufficient funds (for
example, an account is closed or frozen), NACHA rules require originators of an
ACH Debit to review and confirm the bank account or take other action before
reinitiating a debit. To comply with these Rules, Stripe blocks certain bank
accounts until we can confirm that the issue causing the returns has been
resolved. In addition to ensuring compliance with the NACHA rules, this process
helps businesses reduce fraud and avoid repeated dispute and return fees. We
don’t block bank accounts because of past insufficient funds returns.

## Minimizing blocked customer bank accounts

You can minimize the risk of dealing with blocked customer bank accounts by
taking a few preventative steps. To minimize this risk, we recommend that you:

- **Verify accounts using Financial Connections Instant Verification**—This
helps confirm accurate account details and verify account ownership.
- **Prevent accidental disputes**—Use clear [statement
descriptors](https://support.stripe.com/questions/update-business-name-shown-on-customer-bank-statements)
for your business name that customers can easily recognize on their bank
statements, which minimizes the chance that a confused customer unintentionally
disputes your payments.
- **Reduce bank auto-blocks**—Some banks and business accounts automatically
reject ACH Debits attempts from unknown entities. To prevent this, have your
customer provide [Stripe Company
IDs](https://support.stripe.com/questions/ach-direct-debit-company-ids-for-stripe)
to their bank to enable debits initiated by Stripe.

## Identifying blocked accounts

In the Dashboard, ACH Debits that failed because blocked accounts are labeled
`blocked` with an error message. When attempting to confirm a Payment Intent or
Setup Intent, these blocked requests return an `HTTP 402` status and contain the
`bank_account_unusable` error code. [Payment
Intents](https://docs.stripe.com/api/payment_intents) also generate a failed
charge, while [Setup Intents](https://docs.stripe.com/api/setup_intents) create
a failed Setup Attempt instead.

### Payment method status details

After creating a US bank account payment method, the
[us_bank_account.status_details.blocked](https://docs.stripe.com/api/payment_methods/object#payment_method_object-us_bank_account-status_details-blocked)
field renders if the account is blocked. You must make requests using a secret
key for the field to appear.

You can access the
[network_code](https://docs.stripe.com/api/payment_methods/object#payment_method_object-us_bank_account-status_details-blocked-network_code)
and [reason
properties](https://docs.stripe.com/api/payment_methods/object#payment_method_object-us_bank_account-status_details-blocked-reason)
inside the PaymentMethod object to understand the details behind each block. The
`network_code` contains the raw ACH return code associated with a previous
failed payment or dispute made with this account, while the `reason` is a
summary category that corresponds with the code’s semantic meaning.

For more information on removing blocks, consult the section on [handling
blocked bank
accounts](https://docs.stripe.com/payments/ach-direct-debit/blocked-bank-accounts#block-category-table)
below for each `reason` value. When Stripe removes the block, the
`us_bank_account.status_details.blocked` field stops rendering on all previously
affected payment methods.

### Listening to status changes

Stripe sends the
[payment_method.automatically_updated](https://docs.stripe.com/api/events/types#event_types-payment_method.automatically_updated)
event for all saved payment methods when a blockable ACH return is received.
This also includes any verified customer bank accounts that were created using
the Stripe [legacy ACH
integration](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges).

Consuming these events can provide advance notice if your business model relies
on recurring payments that need to be processed before a certain date. Inspect
the event data for the `us_bank_account.status_details.blocked` field, then work
with your customer to unblock or switch bank accounts before initiating future
payments.

You receive equivalent events when the block is removed, indicating that payment
methods can be reused immediately, if an active mandate exists or you re-collect
one.

## Handling blocked bank accounts

If a customer’s ACH bank account becomes blocked, the action you take depends on
the reason the account was blocked. To find the reason, go to the Payment Intent
in the Dashboard and navigate down to the **All activity** section. Then, find
the `402 Error - A Request to create a PaymentIntent failed` event and locate
the `code` value in the `last_payment_error` field.

ReasonRecommended actionRequired documentation- `bank_account_closed`

Contact the customer to make sure their bank account is still active, and that
other information associated with the account is current and correct. If the
customer’s bank account is no longer valid or active, ask them to update their
payment method for future debits.

If, after contacting the customer, you believe the bank account was blocked in
error, contact [Stripe Support](https://support.stripe.com/contact) with the
required documentation. After we confirm this information, we can unblock the
account for future use.

Recent screenshot of an online bank portal that shows the full routing number,
account number, and name of the account holder.

OR

Letter from the bank noting the account is still active, including the full
routing number, account number, and name of the account holder.

- `bank_account_frozen`
- `bank_account_restricted`

Contact the customer to make sure their bank account is still active, and that
other information associated with the account is current and correct. If the
customer’s bank account is no longer valid or active, ask them to update their
payment method for future debits.

If, after contacting the customer, you believe the bank account was blocked in
error, contact [Stripe Support](https://support.stripe.com/contact) with the
required documentation. After we confirm this information, we can unblock the
account for future use.

Recent letter from the bank indicating that the account supports debits,
including the full routing number, account number, and name of the account
holder.

OR

Bank statement that shows recent debit activity, including the full routing
number, account number, and name of the account holder.

- `bank_account_invalid_details`

Contact the customer to make sure their bank account is still valid, and that
other information associated with the account is current and correct. If the
customer’s bank account is no longer valid or active, ask them to update their
payment method for future debits.

If, after contacting the customer, you believe the bank account was blocked in
error, contact [Stripe Support](https://support.stripe.com/contact) with the
required documentation. After we confirm this information, we can unblock the
account for future use.

Voided check that shows the full routing number, account number, and name of the
account holder.

OR

Recent screenshot of an online bank portal that shows the full routing number,
account number, and name of the account holder.

- `debit_not_authorized`
- `bank_account_unusable`

When a customer disputes a payment as unauthorized, contact them before
attempting any additional debits. After their first dispute, Stripe revokes the
associated mandate and requires them to accept a new mandate authorization
before additional debits can be attempted. If they dispute a second payment, the
bank account is blocked.

If, after contacting the customer, you believe they unintentionally disputed
these payments, contact [Stripe Support](https://support.stripe.com/contact)
with the required documentation. After we confirm this information, we can
unblock the account for future use.

Written communication from the bank with confirmation that the [Stripe ACH ID
was added to the
allowlist](https://support.stripe.com/questions/ach-direct-debit-company-ids-for-stripe)
and authorization restrictions are lifted. The written communication must
confirm that the customer has authorized future debits to this payment method
and must include the account details, such as account number, routing number,
and name of the account holder.

## Links

- [statement
descriptors](https://support.stripe.com/questions/update-business-name-shown-on-customer-bank-statements)
- [Stripe Company
IDs](https://support.stripe.com/questions/ach-direct-debit-company-ids-for-stripe)
- [Payment Intents](https://docs.stripe.com/api/payment_intents)
- [Setup Intents](https://docs.stripe.com/api/setup_intents)
-
[us_bank_account.status_details.blocked](https://docs.stripe.com/api/payment_methods/object#payment_method_object-us_bank_account-status_details-blocked)
-
[network_code](https://docs.stripe.com/api/payment_methods/object#payment_method_object-us_bank_account-status_details-blocked-network_code)
- [reason
properties](https://docs.stripe.com/api/payment_methods/object#payment_method_object-us_bank_account-status_details-blocked-reason)
- [handling blocked bank
accounts](https://docs.stripe.com/payments/ach-direct-debit/blocked-bank-accounts#block-category-table)
-
[payment_method.automatically_updated](https://docs.stripe.com/api/events/types#event_types-payment_method.automatically_updated)
- [legacy ACH
integration](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges)
- [Stripe Support](https://support.stripe.com/contact)