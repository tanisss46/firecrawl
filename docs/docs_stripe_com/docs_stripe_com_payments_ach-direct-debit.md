# ACH Direct Debit

## Learn how businesses can accept payments with ACH Direct Debit.

There are two ways to accept US bank debits on Stripe: ACH Direct Debit and
[Instant Bank
Payments](https://docs.stripe.com/payments/link/instant-bank-payments). This
guide describes ACH Direct Debit and helps you choose the best bank debit type
for your business.

ACH lets you accept payments from customers with a US bank account. ACH Direct
Debit is a [reusable](https://docs.stripe.com/payments/payment-methods#usage),
[delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method. It can take [up to 4 business
days](https://docs.stripe.com/payments/ach-direct-debit#timing) to receive
acknowledgement of success or failure. Because ACH Direct Debit isn’t a
guaranteed payment method, there’s a risk of failed payments and
[disputes](https://docs.stripe.com/payments/ach-direct-debit#disputed-payments).

Accepting bank accounts is slightly different from accepting cards:

- Your customer must
[authorize](https://docs.stripe.com/payments/ach-direct-debit#mandates) the
payment terms.
- Bank accounts must be
[verified](https://docs.stripe.com/payments/ach-direct-debit#verification).
Payment method propertiesBusiness locationsProduct support- **Customer
locations**

US
- **Presentment currency**

USD
- **Payment confirmation**

Business-initiated
- **Payment method family**

Bank debit
- **Recurring payments**

Yes
- **Payout timing**

2-5 days
- **Connect support**

[Yes](https://docs.stripe.com/payments/ach-direct-debit#connect)
- **Dispute support**

[Yes](https://docs.stripe.com/payments/ach-direct-debit#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/ach-direct-debit#refunds)

## Payment flow

!

At checkout, the customer selects **ACH Direct Debit**.

!

The customer signs into their bank account to provide account information.

!

The merchant presents the mandate. The customer accepts it by completing the
purchase.

!

The customer is notified when payment is complete.

## Get started

If ACH is all you want, learn how to [accept a
payment](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment)
with ACH. Below are options to skip writing that code.

### Dynamic payment methods

You don’t have to integrate ACH Direct Debit and other payment methods
individually. If you use our front-end products, Stripe automatically determines
the most relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable ACH
Direct Debit. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add ACH Direct Debit from the
Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

### Manually add each payment method

If you prefer to manually list payment methods or want to save ACH Direct Debit
details for future payments, see the following guides:

- [Manually configure ACH Direct Debit as a
payment](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment)
- [Save ACH Direct Debit details for future
payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment)

## Timing

With ACH Direct Debit, it can take time for funds to become available in your
Stripe balance. The amount of time it takes for funds to become available is
referred to as the settlement timing. The following tables describe the
settlement timings for ACH Direct Debit payments that Stripe offers.

Initial payments made from select bank accounts that use temporary account
numbers with Financial Connections might be subject to settlement delays.

Settlement typeTimingCutoff timeAdditional informationStandard settlement (T+4)4
business days from payment creation21:00 US/EasternAfter ACH Direct Debit
payments settle to your Stripe account balance, we make payouts to your bank
account according to your set payout schedule.Faster settlement (T+2)2 business
days from payment creation14:00 US/EasternThis option is available only to
eligible US users. You can check your eligibility and activate this option on
the [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). For more
information on faster settlement, see the
[Support](https://support.stripe.com/questions/two-day-settlement-for-ach-direct-debit)
page.

!

A diagram showing the two settlement timings for ACH Direct Debit: standard (4
days) and faster (2 days).

For information on how to cancel payments, see [Refund and cancel
payments](https://docs.stripe.com/refunds#cancel-payment).

## Transaction failures

ACH Direct Debit transactions can fail any time after the payment is initiated
through payment confirmation. These failures can occur for a number of reasons,
such as:

- Insufficient funds
- An invalid account number
- A customer disabling debits from their bank account

If a payment fails after funds have been made available in your Stripe balance,
Stripe immediately removes funds from your Stripe account.

In rare situations, Stripe might receive an ACH failure from the bank after a
PaymentIntent has transitioned to `succeeded`. If this happens, Stripe creates a
dispute with a `reason` of:

- `insufficient_funds`
- `incorrect_account_details`
- `bank_cannot_process`

Stripe charges a failure fee in this situation.

## Verification

Learn about [validation and
verification](https://support.stripe.com/questions/nacha-bank-account-validation-rule)
requirements.

Stripe lets your customers securely share their financial data by linking their
financial accounts to your business. Use [Financial
Connections](https://docs.stripe.com/financial-connections) to access
customer-permissioned financial data such as tokenized account and routing
numbers, balance data, ownership details, and transaction data.

Your customers might enter their bank account manually instead of authenticating
with Stripe Financial Connections. In these cases, Stripe provides a
fully-hosted flow for collecting bank account details and verifies them with
microdeposits.

When you use [Stripe.js](https://docs.stripe.com/payments/elements), our
JavaScript library for building payment flows, Stripe provides a fully-hosted
collection of bank account details, instant bank verification, and (if needed)
delayed verification using microdeposits. This verification process is a
requirement for many businesses, and it helps reduce payment failures and
fraudulent activities.

## Mandates

ACH Direct Debit rules require that you first get authorization from a customer
to take payments before you can debit their bank account. To obtain
authorization, you present a mandate to them. This mandate specifies the terms
for one-time or recurring payments. The customer must agree to this mandate
before you can collect any payments from their bank account.

When you use Stripe to initiate ACH transactions with your customers, make sure
you have all the necessary authorizations and approvals from your customers for
Stripe to transmit an ACH debit transaction to the customer’s bank account. The
information you provide Stripe about each ACH transaction must be accurate and
complete, including the name of your customer that authorized you to initiate
the ACH transaction to their bank account.

#### Types of mandates

There are two types of mandates: online and offline.

- **Online mandates**: Appear as part of the payment flow on a website.
Customers accept online mandates through a user interface element, such as
clicking an **Accept** or **Pay** button, or by checking a box.
- **Offline mandates**: Require that you present the specific terms of the
transaction to your customer in writing or over the phone. The customer accepts
those terms when they sign the paper or verbally agree to the terms over the
phone. See the [details on the offline mandate
types](https://docs.stripe.com/payments/ach-direct-debit/sec-codes) Stripe
supports.

Stripe displays an online mandate on the payment page for you if you use one of
the following hosted products:

- Checkout
- Payment Element
- Hosted Invoices Page

### Mandates for online custom payment forms

For custom payment forms that directly integrate with the Payment Intents API,
you must display the mandate terms on your payment page before confirming the
PaymentIntent or SetupIntent.

You only need to display a mandate the first time you collect a customer’s bank
account.

#### Recommended mandate text (online)

We recommend that you use the following mandate text for your online custom
payment form. This text must include the customer’s name, bank account
information, and the date.

For details on displaying the correct business name for Connect users, see
[merchant of record and statement
descriptors](https://docs.stripe.com/payments/ach-direct-debit#connect-merchant-of-record).

By clicking [accept], you authorize Rocket Rides to debit the bank account
specified above for any amount owed for charges arising from your use of Rocket
Rides’ services and/or purchase of products from Rocket Rides, pursuant to
Rocket Rides’ website and terms, until this authorization is revoked. You may
amend or cancel this authorization at any time by providing notice to Rocket
Rides with 30 (thirty) days notice.
If you plan to use the customer’s bank account for future payments with the
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
parameter or by [saving bank
details](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment) for a
future payment, also include:

If you use Rocket Rides’ services or purchase additional products periodically
pursuant to Rocket Rides’ terms, you authorize Rocket Rides to debit your bank
account periodically. Payments that fall outside of the regular debits
authorized above will only be debited after your authorization is obtained.
#### Caution

If you originate recurring preauthorized debits, you must disclose to your
customers how these amounts are calculated or a range the customer can
anticipate. You must also give your customer at least 7 calendar days notice if
you change the timing of any recurring preauthorized debits.

### Mandate and microdeposit emails

By default, if your customer provides a [billing email
address](https://docs.stripe.com/api/payment_methods/object#payment_method_object-billing_details-email),
Stripe automatically emails your customer the following information:

- Confirmation of the mandate, per Nacha requirements.
- Notification if Stripe needs to use microdeposits to verify your customer’s
bank account. These notification emails link to a hosted verification page.

#### Sending custom mandate notifications (online)

You can send custom mandate notifications to customers.

To send custom mandate notifications:

- Turn off Stripe emails in the Stripe Dashboard [email
settings](https://dashboard.stripe.com/settings/emails)
- Send a mandate confirmation email when you receive your customer’s bank
account and mandate authorization.

In the email, include the following information:

- Authorization date
- Account holder name
- Financial institution
- Routing number
- Last four digits of the account number

The following is a sample mandate confirmation email that you can send.

Agreement DateJune 28, 2021Account Holder NameJenny RosenFinancial
InstitutionChase BankRouting Number021000021Account Number****6789Thank you for
signing up for direct debits from Rocket Rides. You have authorized Rocket Rides
to debit the bank account specified above for any amount owed for charges
arising from your use of Rocket Rides’ services and/or purchase of products from
Rocket Rides, pursuant to Rocket Rides’ website and terms, until this
authorization is revoked. You may amend or cancel this authorization at any time
by providing notice to Rocket Rides with 30 (thirty) days notice.
If you collected the customer’s bank account for future payments with the
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
parameter or by [saving bank
details](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment), also
include:

You have authorized Rocket Rides to debit your bank account periodically if and
when you use Rocket Rides’ services or purchase more than one of Rocket Rides’
products periodically pursuant to Rocket Rides’ terms. Payments that fall
outside of the regular debits authorized above will only be debited after your
authorization is obtained.
#### Caution

If you choose to send custom emails, you also need to send microdeposit reminder
emails. For detailed instructions, see [Custom microdeposit email and
verification
page](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#optional:-send-custom-email-notifications).

## Disputes

ACH Direct Debit provides a dispute process for bank account holders to dispute
payments. Customers can generally dispute a payment through their bank for up to
60 calendar days after a debit on a personal account, or up to 2 business days
for a business account. In rare instances, a debit payment can be successfully
disputed outside these timelines. This is called a late return. The late return
process is primarily managed by and ultimately decided at the discretion of the
banks involved in the transaction.

When a dispute is created, Stripe sends both the
[charge.dispute.created](https://docs.stripe.com/api/events/types#event_types-charge.dispute.created)
and
[charge.dispute.closed](https://docs.stripe.com/api/events/types#event_types-charge.dispute.closed)
[webhook](https://docs.stripe.com/webhooks) events and deducts the amount of the
dispute and associated dispute fee from your Stripe balance.

Unlike credit card disputes, all ACH Direct Debit disputes are final and there
is no process for appeal. If a customer successfully disputes a payment, you
must contact them if you want to resolve the situation.

#### Caution

If you proactively issue your customer a refund while the customer’s bank also
initiates the dispute process, your customer might receive two credits for the
same transaction. Follow the guidelines in the following section on refunds to
avoid this situation.

### Resolving disputes

When a customer disputes an ACH Direct Debit payment, it invalidates the mandate
associated with the payment method and you can’t reuse it. To attempt a charge
again, you must resolve the dispute with the customer and [collect a new mandate
authorization](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment#resolving-disputes).

If they dispute a subsequent payment, Stripe blocks the bank account from
further re-use. To learn more about resolution steps, see [Blocked bank
accounts](https://docs.stripe.com/payments/ach-direct-debit/blocked-bank-accounts).

## Refunds

You have a maximum of 180 days from the date of the original payment to submit a
refund for an ACH Direct Debit payment. Refunds require at least 3 business days
to process. Stripe waits for the original payment to succeed before submitting
the refund.

#### Avoid disputes

If you accidentally debit your customer, contact them immediately to avoid a
payment dispute. Factors such as slightly longer settlement time periods and the
way banks process ACH Direct Debit transactions can cause confusion between you,
your customer, your customer’s bank, and Stripe. For example, your customer
might contact both you and their bank to dispute a payment. If you proactively
issue your customer a refund while the customer’s bank also initiates the
dispute process, your customer might receive two credits for the same
transaction, so it’s important to communicate with your customer about the
processing time and the status of their refund.

Stripe doesn’t explicitly label ACH Direct Debit refunds as refunds when we
deposit the funds back to a customer’s bank account. Instead, we process refunds
as a credit and include a reference to the statement descriptor for the original
payment.

## Statement descriptors for ACH

Every ACH Direct Debit payment shows up on customers’ bank statements with the
*name of the merchant*. For payments created with Stripe, the name of the
merchant is your Stripe account’s [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors).
You can override this default behavior for every transaction independently by
using a [dynamic statement
descriptor](https://docs.stripe.com/payments/payment-intents#dynamic-statement-descriptor).
To do so, specify the
[statement_descriptor](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-statement_descriptor)
parameter when creating the `PaymentIntent`.

#### Caution

Your statement descriptor truncates to the first 16 alphanumeric characters on
the bank statement. For example, if your statement descriptor is
`ROCKETRIDESLIMITED`, the customer sees `ROCKETRIDESLIMIT`.

Additionally, statement descriptors cannot use the special characters `<`, `>`,
`'`, or `"`.

The table below illustrates the *merchant name* behavior you can expect on the
customer’s bank statement:

Default statement descriptorDynamic statement descriptorMerchant nameBank
statement descriptorRocket RidesUnspecified`Rocket Rides``Rocket Rides`Rocket
Rides`Sunday Ride``Rocket Rides``Sunday Ride`
Each bank formats these fields differently. Depending on your customer’s bank,
some fields may appear in all lowercase or uppercase.

## Connect

If you use [Connect](https://docs.stripe.com/connect), you must take the
following into consideration before you enable and use ACH Direct Debits.

### Request ACH Debit capabilities for your connected accounts

Set the `us_bank_account_ach_payments` capability to `active` on your platform
account, and for any connected accounts you want to enable for ACH debits. You
can also [request more account
capabilities](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting).

#### Note

Stripe automatically refunds the application fee to your platform account when
the [destination charge](https://docs.stripe.com/connect/charges#destination)
for an ACH debit fails. Learn about [fees for failed
payments](https://stripe.com/pricing/local-payment-methods#ach-direct-debit).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges) of Connect payments
might change the default statement descriptor and the merchant name that appears
on the customer’s bank statement. The charge type can also change:

- The merchant of record shown on the mandate
- The merchant shown on confirmation emails
- The merchant shown on microdeposit reminder emails

The merchant of record determines the Stripe account authorized to create
payments with a particular
[PaymentMethod](https://docs.stripe.com/api/payment_methods/object). To learn
more about sharing this authorization across multiple connected accounts, see
[PaymentMethod and Mandate
cloning](https://docs.stripe.com/payments/ach-direct-debit#payment-method-and-mandate-cloning).

Charge typeDescriptor taken fromDirectConnected
AccountDestinationPlatformSeparate charge and transferPlatformDestination (with
`on_behalf_of`)Connected AccountSeparate charge and transfer (with
`on_behalf_of`)Connected Account
### PaymentMethod and mandate cloning

You can collect customer bank accounts on the platform account and
[clone](https://docs.stripe.com/connect/direct-charges-multiple-accounts#clone-and-create-direct-charges)
ACH Direct Debit payment methods. Cloning these methods allows you to save
customer bank accounts for later use on connected accounts. When you clone ACH
Direct Debit payment methods, Stripe duplicates the mandate authorization to the
connected account, but we don’t send any new mandate confirmation emails.

#### Caution

If a mandate is authorized for a PaymentIntent or SetupIntent
[on_behalf_of](https://docs.stripe.com/connect/charges#on_behalf_of) a connected
account, you can’t use that mandate with a different connected account.

When collecting a bank account that you intend to clone to connected accounts,
you must communicate to the customer that their authorization extends to
connected accounts on your platform. For example, you can communicate this
message to a customer through the mandate terms. Failure to communicate this
message to your customers could result in customer confusion and increase the
risk of disputed payments.

### Connect and settlement

Settlement speed is generally controlled at the platform level. The table below
shows a comprehensive view of settlement timing by account and charge type.

Account TypeDirect ChargesDestination ChargesSeparate Charges and
TransfersStandard with Platform ControlThe platform controls the settlement
speed.The platform controls the settlement speed.The platform controls the
settlement speed.Standard without Platform ControlThe connected account controls
the settlement speed.The connected account controls the settlement speed.The
platform controls the settlement speed.ExpressThe platform controls the
settlement speed.The platform controls the settlement speed.The platform
controls the settlement speed.CustomThe platform controls the settlement
speed.The platform controls the settlement speed.The platform controls the
settlement speed.
## Testing ACH

Learn how to test scenarios with instant verifications using [Financial
Connections](https://docs.stripe.com/financial-connections/testing#web-how-to-use-test-accounts).

### Send transaction emails in test mode

After you collect the bank account details and accept a mandate, send the
mandate confirmation and microdeposit verification emails in test mode. To do
this, provide an email in the `payment_method_data.billing_details[email]` field
in the form of `{any-prefix}+test_email@{any_domain}` when you collect the
[payment method
details](https://docs.stripe.com/payments/ach-direct-debit#web-collect-details).

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
microdeposit timeout.
## US bank debit comparison

OptionConfirmation timePayment failure protectionAdditional information[Instant
Bank
Payments](https://docs.stripe.com/payments/link/instant-bank-payments)InstantBank-initiated
returns guaranteed by StripeFor businesses looking for instant confirmation and
faster settlement, Instant Bank Payments provides a card-like payment flow with
the cost savings of bank debits. Instant Bank Payments are available only as a
part of [Link](https://docs.stripe.com/payments/link).[ACH Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit#ach-direct-debit)Up to
4 business daysUse [Financial
Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments)
data to optimize payments.For businesses that don’t need instant confirmation,
ACH Direct Debit has lower costs than Instant Bank Payments. ACH Direct Debit is
popular for businesses with large or recurring transactions.

## Links

- [Instant Bank
Payments](https://docs.stripe.com/payments/link/instant-bank-payments)
- [reusable](https://docs.stripe.com/payments/payment-methods#usage)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [up to 4 business
days](https://docs.stripe.com/payments/ach-direct-debit#timing)
-
[disputes](https://docs.stripe.com/payments/ach-direct-debit#disputed-payments)
- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [authorize](https://docs.stripe.com/payments/ach-direct-debit#mandates)
- [Yes](https://docs.stripe.com/payments/ach-direct-debit#connect)
- [Yes / Yes](https://docs.stripe.com/payments/ach-direct-debit#refunds)
- [accept a
payment](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [Save ACH Direct Debit details for future
payments](https://docs.stripe.com/payments/ach-direct-debit/set-up-payment)
-
[Support](https://support.stripe.com/questions/two-day-settlement-for-ach-direct-debit)
- [Refund and cancel payments](https://docs.stripe.com/refunds#cancel-payment)
- [validation and
verification](https://support.stripe.com/questions/nacha-bank-account-validation-rule)
- [Financial Connections](https://docs.stripe.com/financial-connections)
- [Stripe.js](https://docs.stripe.com/payments/elements)
- [details on the offline mandate
types](https://docs.stripe.com/payments/ach-direct-debit/sec-codes)
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
- [billing email
address](https://docs.stripe.com/api/payment_methods/object#payment_method_object-billing_details-email)
- [email settings](https://dashboard.stripe.com/settings/emails)
- [Custom microdeposit email and verification
page](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#optional:-send-custom-email-notifications)
-
[charge.dispute.created](https://docs.stripe.com/api/events/types#event_types-charge.dispute.created)
-
[charge.dispute.closed](https://docs.stripe.com/api/events/types#event_types-charge.dispute.closed)
- [webhook](https://docs.stripe.com/webhooks)
- [collect a new mandate
authorization](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment#resolving-disputes)
- [Blocked bank
accounts](https://docs.stripe.com/payments/ach-direct-debit/blocked-bank-accounts)
- [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
- [dynamic statement
descriptor](https://docs.stripe.com/payments/payment-intents#dynamic-statement-descriptor)
-
[statement_descriptor](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-statement_descriptor)
- [Connect](https://docs.stripe.com/connect)
- [request more account
capabilities](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting)
- [destination charge](https://docs.stripe.com/connect/charges#destination)
- [fees for failed
payments](https://stripe.com/pricing/local-payment-methods#ach-direct-debit)
- [charge type](https://docs.stripe.com/connect/charges)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods/object)
-
[clone](https://docs.stripe.com/connect/direct-charges-multiple-accounts#clone-and-create-direct-charges)
- [on_behalf_of](https://docs.stripe.com/connect/charges#on_behalf_of)
- [Financial
Connections](https://docs.stripe.com/financial-connections/testing#web-how-to-use-test-accounts)
- [activate your Stripe
account](https://docs.stripe.com/get-started/account/activate)
- [PaymentIntent
cancellation](https://docs.stripe.com/api/payment_intents/cancel)
- [Link](https://docs.stripe.com/payments/link)
- [Financial
Connections](https://docs.stripe.com/financial-connections/ach-direct-debit-payments)