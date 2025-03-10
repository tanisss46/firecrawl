# Pre-authorized debit payments in Canada

## Learn how to accept pre-authorized debit payments in Canada.

Stripe users in Canada and the United States can accept pre-authorized debit
payments (PADs) from customers with a Canadian bank account using the Automated
Clearing Settlement System (ACSS) provided by [Payments
Canada](https://www.payments.ca/).

Before debiting a customer’s bank account, businesses must first collect a
[mandate](https://docs.stripe.com/payments/acss-debit#mandates) from the
customer defining a specific payment schedule or terms. The mandate includes the
customer’s institution number, transit number, account number, name, and email.

When you use Stripe.js, our foundational JavaScript library for building payment
flows, Stripe provides a hosted solution for collecting mandates from customers
using your preferred terms, as well as fully-hosted collection of bank account
details and instant bank verification (and delayed verification using
micro-deposits in rare cases). This verification process is a requirement to
accept PADs, and can also help to reduce payment failures and fraudulent
activities.

Canadian pre-authorized debits are a
[reusable](https://docs.stripe.com/payments/payment-methods#usage), [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method. It can take up to 5 business days after initiating a payment to
receive notification of success or failure. PADs aren’t a guaranteed payment
method. There is a risk of failed payments and
[disputes](https://docs.stripe.com/payments/acss-debit#disputed-payments).

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

CA
- **Presentment currency**

CAD, USD (in [rare
cases](https://docs.stripe.com/payments/acss-debit#presentment-currency))
- **Payment confirmation**

Business-initiated
- **Payment method family**

Bank debit
- **Recurring payments**

Yes
- **Payout timing**

5-7 days
- **Connect support**

Yes
- **Dispute support**

[Yes](https://docs.stripe.com/payments/acss-debit#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/acss-debit#refunds)

## Payment flow

!

[Customer](https://docs.stripe.com/api/customers) selects pre-authorized debit
at checkout

!

Customer provides bank information and accepts mandate

!

Customer gets notification that the payment is complete

## Get started

#### Note

Subscription mode in [Checkout](https://docs.stripe.com/payments/checkout) isn’t
yet supported. To learn about early access when this feature is available,
[contact
us](mailto:payment-methods-feedback@stripe.com?subject=PADs%20Subscription%20Mode%20User%20Interest)
to join the waitlist.

You don’t have to integrate Canadian pre-authorized debit and other payment
methods individually. If you use our front-end products, Stripe automatically
determines the most relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Canadian pre-authorized debit. To get started with one of our hosted UIs, follow
a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Canadian pre-authorized debit
from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

If you prefer to manually list payment methods or want to save Canadian
pre-authorized debit details for future payments, see the following guides:

- [Manually configure Canadian pre-authorized debit as a
payment](https://docs.stripe.com/payments/acss-debit/accept-a-payment)
- [Save Canadian pre-authorized debit details for future
payments](https://docs.stripe.com/payments/acss-debit/set-up-payment)

## Mandates

During the payment flow, Stripe helps you collect a mandate which gives your
business authorization to debit the customer’s account. In Canada, these are
called pre-authorized debit agreements or PAD agreements. The mandate
collection, confirmation and pre-debit notification requirements for
pre-authorized debits are governed by Payments Canada’s [Rule H1 for
pre-authorized debits
(PADs)](https://www.payments.ca/sites/default/files/h1eng.pdf).

Instructions for collecting mandate acceptance can be found on the [Accept a
payment](https://docs.stripe.com/payments/acss-debit/accept-a-payment) page. In
the unlikely event that your business requires a custom agreement, information
on how to create a mandate that meets Payments Canada requirements can be found
on the [Custom PAD mandate
agreements](https://docs.stripe.com/payments/acss-debit/custom-pad-agreement)
page.

Stripe will initiate the first debit immediately after mandate acceptance. Your
customers must receive confirmation of a new mandate within 5 days after they
have accepted the mandate (see [Mandate and debit notification
emails](https://docs.stripe.com/payments/acss-debit#mandate-and-debit-notification-emails)).

Customers can at any time request the cancellation of a mandate, including by
properly giving oral notice of cancellation. To cancel a mandate, a customer
must either reach out to the business they established the mandate with, or to
their bank. Canceling a mandate invalidates any further debit requests that you
issue using this mandate. If you wish to accept additional payments from the
customer, a new mandate must be established with them.

### Payment Schedule

Each PAD mandate must specify a [payment
schedule](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-acss_debit-mandate_options-payment_schedule)
that defines when and how debits can be automatically charged to a customer.

ScheduleUse Case
`interval`

Subsequent payments for set interval PADs can be charged to customers outside of
your checkout flow on a specified schedule or based on triggering events clearly
described in the mandate with an [interval
description](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-acss_debit-mandate_options-interval_description).

One or more debits that occur with predictability, such as:

- a one-time payment on a specific date
- on a set of dates
- on a regular basis (for example, weekly, monthly)
- on the occurrence of certain criteria or events

Some example `interval_description` values for which you could debit:

- on the 5th of every month
- on completion of checkout
- on acceptance of a contract
- when a customer balance owing reaches $100
- when any invoice becomes due

`sporadic`

Debits that are infrequent or irregular and not at specified or predictable
periods or time. Sporadic PADs can be charged to customers at arbitrary times,
but only with the express authorization of the customer at the time of payment
(such as logging into your website).

An example of a sporadic payment could be a balance owed by the customer where
payment is triggered by the customer rather than automatically by you at a
certain time. Collecting bank account details and a `sporadic` mandate ahead of
time would allow your customer to trigger payment with a single step.

`combined`A mandate that would allow both `interval` and `sporadic` debits.
## Mandate and debit notification emails

The [Payments Canada network
rules](https://www.payments.ca/sites/default/files/h1eng.pdf) require that you
notify your customer:

- When a mandate is established
- Each time a debit is made on their account

In addition, should your customer’s bank account need to be verified using
micro-deposits, Stripe will send reminder emails linking to a hosted
verification page.

By default, Stripe automatically sends emails to the customer for these cases.
You can [customize the colors and
logo](https://dashboard.stripe.com/account/branding) for these emails to fit the
design and branding of your business.

#### Warning

If you prefer to send custom notifications, all of these emails must be
supported. It is not possible to send custom notifications for only one of them.

To send custom notifications:

- Turn off Stripe emails in the [Stripe Dashboard email
settings](https://dashboard.stripe.com/account/emails)
- Send a **mandate confirmation** email when you have collected your customer’s
bank account and mandate authorization.- Mandate confirmation emails must be
sent no later than 5 calendar days after your customer has accepted the mandate.
Stripe will initiate the first debit immediately after mandate acceptance.
- The email must include the mandate you created for the debit (see [Custom PAD
mandate
agreements](https://docs.stripe.com/payments/acss-debit/custom-pad-agreement))
and the bank account information collected from your customer, including the
institution number, transit number and last four digits of the account number.
- Use the
[charge.pending](https://docs.stripe.com/api/events/types#event_types-charge.pending)
event to trigger **debit notification** emails.- Debit notification emails must
include: your contact information, the last 4 digits of your customer’s bank
account, and the amount to be debited.

## Disputes

Canadian pre-authorized debits provide a dispute process for bank account
holders to dispute payments. Customers can dispute a debit payment through their
bank on a “no questions asked” basis for up to 90 calendar days after a debit on
a personal account or up to 10 business days for a business account. The
customer’s bank can honor any dispute within this period.

When a dispute is created, Stripe sends both the
[charge.dispute.created](https://docs.stripe.com/api/events/types#event_types-charge.dispute.created)
and
[charge.dispute.closed](https://docs.stripe.com/api/events/types#event_types-charge.dispute.closed)
[webhook](https://docs.stripe.com/webhooks) events, and deducts the amount of
the dispute and associated dispute fee from your Stripe balance.

Unlike [credit card disputes](https://docs.stripe.com/disputes), all PAD
disputes are final and there is no process for appeal. If a customer
successfully disputes a payment, you must contact them if you want to resolve
the situation. If you’re able to come to an arrangement and your customer is
willing to return the funds to you, they must make a new payment.

#### Warning

If you proactively issue your customer a refund while the customer’s bank also
initiates the dispute process, your customer might receive two credits for the
same transaction. You should follow the guidelines in the following section on
refunds to avoid this happening.

## PADs transaction failures

PADs transactions can fail any time after the payment is initiated through
payment confirmation. These failures can occur for a number of reasons, such as:

- Insufficient funds
- An invalid account number
- A customer disabling debits from their bank account

If a payment fails after funds have been made available in your Stripe balance,
Stripe immediately removes funds from your Stripe account.

In rare situations, Stripe might receive a PADs failure from the bank after a
PaymentIntent has transitioned to `succeeded`. If this happens, Stripe creates a
dispute with a `reason` of:

- `insufficient_funds`
- `incorrect_account_details`
- `bank_cannot_process`

Stripe charges a failure fee in this situation.

## Payouts

Pre-authorized debit payments are subject to a minimum 5 business day [payout
timing](https://docs.stripe.com/payouts#standard-payout-timing) from charge
creation. If your payout timing is longer than 5 business days, payouts from PAD
payments will be unified with card payouts.

## Presentment currency Optional

Most bank accounts in Canada hold Canadian dollars (CAD), with a small number of
accounts in other currencies, including US dollars (USD). It is possible to
accept PAD payments in either CAD or USD, but choosing the correct currency for
your customer is important to avoid payment failures.

Unlike many card-based payment methods, you might not be able to successfully
debit a CAD account in USD or debit a USD account in CAD. Most often, attempting
to do so will result in a delayed payment failure that will take up to 5
business days.

To avoid these failures, it is safest to take PAD payments in CAD unless you are
confident your customer’s account will accept USD debits.

## Refunds

Refunds for PADs must be submitted within 180 days from the date of the original
payment. Refunds require additional time to process (typically 3 business days).
If you accidentally debit your customer, please contact them immediately to
avoid a payment dispute.

Refunds are processed only after the payment process is complete. If you create
a full or partial refund on a payment that hasn’t yet completed, the refund is
actioned when the `Charge` object’s status transitions to `succeeded`. If the
`Charge` object’s status transitions to `failed`, the full or partial refund is
marked as canceled because the money was never debited from the customer’s bank
account.

PAD refunds are not explicitly labeled as refunds when the funds are deposited
back to a customer’s bank account. Instead, refunds are processed as a credit
and include a reference to the original payment’s statement descriptor.

Due to longer settlement time periods and how banks process PAD transactions,
there is potential for confusion between you, your customer, your customer’s
bank, and Stripe. For example, your customer might contact both you and their
bank to dispute a payment. If you proactively issue your customer a refund while
the customer’s bank also initiates the dispute process, your customer might
receive two credits for the same transaction.

When issuing a refund, you should inform your customer immediately that the
refund typically takes 3 business days to arrive in their bank account.

## Statement descriptors

Every PAD payment shows up on customers’ bank statements with the *name of the
merchant*. For PAD payments created with Stripe, the name of the merchant is
your Stripe account’s [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors).
You can override this default behavior for every transaction independently by
using a [dynamic statement
descriptor](https://docs.stripe.com/payments/payment-intents#dynamic-statement-descriptor).
To do so, you can specify the
[statement_descriptor](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-statement_descriptor)
parameter when creating the `PaymentIntent`.

#### Caution

Your statement descriptor will be truncated to the first 15 alphanumeric
characters on the bank statement. For example, if your statement descriptor is
`ROCKETRIDESLIMITED`, the customer will see `ROCKETRIDESLIMI`.

Additionally, statement descriptors cannot use the special characters `<`, `>`,
`'`, or `"`.

The table below illustrates the *merchant name* behavior you can expect on the
customer’s bank statement:

Default statement descriptorDynamic statement descriptorMerchant nameBank
statement descriptorRocket RidesUnspecified`Rocket Rides``Rocket Rides`Rocket
Rides`Sunday Ride``Rocket Rides``Sunday Ride`
Each bank in Canada formats these fields differently. Depending on your
customer’s bank, some fields might appear in all lowercase or uppercase.

### Statement descriptors and Connect

The charge type of Connect payments changes the statement descriptor and the
merchant name, which appears on the customer’s bank statement.

Charge typeDescriptor taken fromDirectConnected
AccountDestinationPlatformSeparate charge and transferPlatformDestination (with
`on_behalf_of`)Connected AccountSeparate charge and transfer (with
`on_behalf_of`)Connected Account
A mandate collected for a `PaymentIntent` `on_behalf_of` a Connected Account
cannot be used with a different Connected Account.

## Smart retries Private preview

## Request early access to ACSS Debit smart retries

Join our private preview.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

- [Payments Canada](https://www.payments.ca)
- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [reusable](https://docs.stripe.com/payments/payment-methods#usage)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Yes](https://docs.stripe.com/payments/acss-debit#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/acss-debit#refunds)
- [Customer](https://docs.stripe.com/api/customers)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [Manually configure Canadian pre-authorized debit as a
payment](https://docs.stripe.com/payments/acss-debit/accept-a-payment)
- [Save Canadian pre-authorized debit details for future
payments](https://docs.stripe.com/payments/acss-debit/set-up-payment)
- [Rule H1 for pre-authorized debits
(PADs)](https://www.payments.ca/sites/default/files/h1eng.pdf)
- [Custom PAD mandate
agreements](https://docs.stripe.com/payments/acss-debit/custom-pad-agreement)
- [payment
schedule](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-acss_debit-mandate_options-payment_schedule)
- [interval
description](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-acss_debit-mandate_options-interval_description)
- [customize the colors and logo](https://dashboard.stripe.com/account/branding)
- [Stripe Dashboard email settings](https://dashboard.stripe.com/account/emails)
-
[charge.pending](https://docs.stripe.com/api/events/types#event_types-charge.pending)
-
[charge.dispute.created](https://docs.stripe.com/api/events/types#event_types-charge.dispute.created)
-
[charge.dispute.closed](https://docs.stripe.com/api/events/types#event_types-charge.dispute.closed)
- [webhook](https://docs.stripe.com/webhooks)
- [credit card disputes](https://docs.stripe.com/disputes)
- [payout timing](https://docs.stripe.com/payouts#standard-payout-timing)
- [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
- [dynamic statement
descriptor](https://docs.stripe.com/payments/payment-intents#dynamic-statement-descriptor)
-
[statement_descriptor](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-statement_descriptor)
- [privacy policy](https://stripe.com/privacy)