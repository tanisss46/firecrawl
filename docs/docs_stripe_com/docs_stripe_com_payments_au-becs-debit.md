# Australia BECS Direct Debit payments

## Learn how to accept Australia BECS Direct Debit payments.

Stripe users in Australia can accept Australia BECS Direct Debit payments from
customers with an Australian bank account.

As part of the payment process, businesses must collect a mandate that includes
the customer’s bank account details (account holder’s name, the
Bank-State-Branch or BSB number, and the bank account number) and must also
accept the mandate Service Agreement. This gives the business an authorization
to debit the account. Stripe can generate this mandate for businesses to present
to their customers.

Australia BECS Direct Debit is a
[reusable](https://docs.stripe.com/payments/payment-methods#usage), [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method. This means that it can take up to three business days to receive
notification on the success or failure of a payment after you initiate a debit
from the customer’s account.

For new users, Australia BECS Direct Debit transactions have a default limit of
1,500 AUD per transaction and 4,500 AUD per week. If you need higher limits,
contact [support](https://support.stripe.com/contact).

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Australia
- **Presentment currency**

AUD
- **Payment confirmation**

Business-intiated
- **Payment method family**

Bank debits
- **Recurring payments**

Yes
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

[Yes](https://docs.stripe.com/payments/au-becs-debit#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/au-becs-debit#refunds)

## Verification requirements

Using Australia BECS Direct Debit requires you to complete additional [identity
verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works)
steps. We prompt you to complete these steps after you request access from the
[Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). If you require
further assistance, please [contact
support](https://support.stripe.com/contact).

## Payment flow

!

Customer selects Australia BECS Direct Debit at checkout

!

Customer completes the Direct Debit Request

!

Customer gets notification that the payment is complete

Preview the payment flow using the test information below or view the [sample
code](https://github.com/stripe-samples/au-becs-debit-payment) on GitHub.

- Any name
- Any email address
- Test BSB number: 000-000
- Test bank account number: 000123456

[Preview Australia BECS Direct Debit payment
flow](https://codesandbox.io/p/devbox/stripe-sample-au-becs-debit-payment-v0n15)

## Get started

You don’t have to integrate Australia BECS Direct Debit and other payment
methods individually. If you use our front-end products, Stripe automatically
determines the most relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Australia BECS Direct Debit. To get started with one of our hosted UIs, follow a
quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Australia BECS Direct Debit from
the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

If you prefer to manually list payment methods or want to save Australia BECS
Direct Debit details for future payments, see the following guides:

- [Accept an Australia BECS Direct Debit
payment](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment)
- [Save Australia BECS Direct Debit details for future
payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment)

## Debit notification emails

The Australia BECS Direct Debit scheme advises that you notify your customer
when a mandate is established and each time you debit their account. By default,
Stripe automatically sends emails to the customer.

If you decide to send your customer a custom notification:

- Turn off Stripe emails in the [Stripe Dashboard email
settings](https://dashboard.stripe.com/account/emails).
- Use the
[payment_intent.processing](https://docs.stripe.com/api/events/types#event_types-payment_intent.processing)
event to trigger debit initiation emails.
- It’s best to share (a link to) the mandate in the mandate notification
- The pre-debit notifications ideally includes:

- The last 4 digits of the customer’s bank account
- The amount to be debited
- Your contact information
- The day you plan to debit the customer’s bank account
- The Australia BECS Direct Debit guidelines suggest sending notifications at
least 14 calendar days before you create a payment, but this isn’t mandatory.
The default Stripe pre-debit email happens the day before the account gets
debited. These pre-debit notifications should help you avoid unnecessary debit
failures and disputes. For recurring payments of the same amount (for example, a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) of a
fixed amount), you can include multiple upcoming debits with corresponding dates
in a single notice.

## Disputes

Australia BECS Direct Debit provides a dispute process for bank account holders
to dispute payments so you should familiarize yourself with this process if you
decide to accept Australia BECS Direct Debit payments.

For up to 7 years, a customer can dispute a payment through their bank on a “no
questions asked” basis. Their bank honors all disputes within this period. If
they dispute a charge and their bank accepts the request to return the funds,
Stripe immediately removes the funds from your Stripe balance.

If a dispute gets created, Stripe sends both the `charge.dispute.created` and
`charge.dispute.closed` [webhook](https://docs.stripe.com/webhooks) events, and
deducts the amount of the dispute and associated dispute fee from your Stripe
balance.

Unlike [credit card disputes](https://docs.stripe.com/disputes), all Australia
BECS Direct Debit disputes are final and can’t be appealed. If a customer
successfully disputes a payment, contact them to resolve the situation. If you
can come to an agreement and your customer is willing to return the funds to
you, they need to make a new payment.

#### Warning

If you proactively issue your customer a refund while the customer’s bank also
initiates the dispute process, your customer might receive two credits for the
same transaction. You should follow the [refund
guidelines](https://docs.stripe.com/payments/au-becs-debit#refunds) to avoid
this.

## Mandates

During the payment process, businesses must collect a mandate that authorizes
them to debit the account. In the Australia BECS Direct Debit system, these
mandates are called Direct Debit Requests, or DDRs.

Bank account holders can request the cancellation of active mandates at any
time. To cancel a mandate, a bank account holder must either contact their bank
or the party they established the mandate with. Canceling a mandate invalidates
any future debit requests that you issue using it. If you want to accept
additional payments from your customer, establish a new mandate with them.

### Mandate events

Event nameDescription`mandate.updated`Occurs whenever a mandate is canceled by
the customer or due to a permanent debit failure. The `status` property will
change to `inactive`.
You can see the events in your Dashboard, but we recommend you still set up a
[webhook endpoint](https://docs.stripe.com/webhooks).

## Refunds

Refunds for payments made with Australia BECS Direct Debit must be issued within
90 days from the date of the original payment. Refunds require additional time
to process (typically 3-5 business days). If you accidentally debit your
customer, contact them immediately to avoid a payment dispute.

Refunds are processed only after the payment process completes. If you create a
full or partial refund on a payment that hasn’t completed yet, the refund
process starts when the `Charge` object’s status transitions to `succeeded`. If
the `Charge` object’s status transitions to `failed`, the full or partial refund
is marked as canceled because the money was never debited from the customer’s
bank account.

Australia BECS Direct Debit doesn’t explicitly label refunds when they’re
deposited back into a bank account. Instead, refunds are processed as a credit
and include a visible reference to the original payment’s statement descriptor.

Due to longer settlement time periods and how banks process Australia BECS
Direct Debit transactions, there is potential for confusion between you, your
customer, your customer’s bank, and Stripe. For example, your customer might
contact both you and their bank to dispute a payment. If you proactively issue
your customer a refund while the customer’s bank also initiates the dispute
process, your customer might receive two credits for the same transaction.

When issuing a refund, inform your customer immediately that the refund can take
up to 5 business days to arrive in their bank account. Stripe won’t
automatically send the customer any email to inform them about this.

## Statement descriptors

Every Australia BECS Direct Debit payment shows two fields on the customers’
bank statements: the *name of the merchant* and the *lodgement reference* unique
to this transaction.

For Australia BECS Direct Debit payments created with Stripe, the name of the
merchant is your Stripe account’s [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors).
You can override this default behavior for every transaction independently by
using a [dynamic statement
descriptor](https://docs.stripe.com/payments/payment-intents#dynamic-statement-descriptor).
To do so, specify the `statement_descriptor` parameter when creating the
`PaymentIntent`.

#### Caution

Your statement descriptor gets truncated to the first 9 alphanumeric characters
in the lodgement reference, followed by a unique ID. For example, if your
statement descriptor is `ROCKETRIDES`, the customer will see
`ROCKETRID_XXXXXXX`.

The table below illustrates the *merchant name* and *lodgement reference*
behavior you can expect on the customer’s bank statement:

Default statement descriptorDynamic statement descriptorMerchant nameLodgement
referenceRocket RidesUnspecified`RocketRides``RocketRid_AB1234CD`Rocket
Rides`Sunday Ride``RocketRides``SundayRid_AB1234CD`
Each bank in Australia formats these fields differently. Depending on your
customer’s bank, some fields might appear in all lowercase or all uppercase.

### Statement descriptors and Connect

The charge type of Connect payments changes the statement descriptor and the
merchant name, which appear on the customer’s bank statement.

Charge typeDescriptor taken fromDirectConnected
accountDestinationPlatformSeparate charge and transferPlatformDestination (with
`on_behalf_of`)Connected accountSeparate charge and transfer (with
`on_behalf_of`)Connected account
You can’t use a mandate collected for a `PaymentIntent` `on_behalf_of` a
connected account with a different connected account.

## Smart retries Private preview

## Request early access to Australia BECS Direct Debit smart retries

Join our private preview.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

- [reusable](https://docs.stripe.com/payments/payment-methods#usage)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [support](https://support.stripe.com/contact)
- [identity
verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [sample code](https://github.com/stripe-samples/au-becs-debit-payment)
- [Preview Australia BECS Direct Debit payment
flow](https://codesandbox.io/p/devbox/stripe-sample-au-becs-debit-payment-v0n15)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [Accept an Australia BECS Direct Debit
payment](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment)
- [Save Australia BECS Direct Debit details for future
payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment)
- [Stripe Dashboard email settings](https://dashboard.stripe.com/account/emails)
-
[payment_intent.processing](https://docs.stripe.com/api/events/types#event_types-payment_intent.processing)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [webhook](https://docs.stripe.com/webhooks)
- [credit card disputes](https://docs.stripe.com/disputes)
- [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
- [dynamic statement
descriptor](https://docs.stripe.com/payments/payment-intents#dynamic-statement-descriptor)
- [privacy policy](https://stripe.com/privacy)