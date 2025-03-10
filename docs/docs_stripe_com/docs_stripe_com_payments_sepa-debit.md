# SEPA Direct Debit payments

## Learn about Single Euro Payments Area (SEPA) Direct Debit, a common payment method in the European Union.

The [Single Euro Payments Area
(SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an
initiative of the European Union to simplify payments within and across member
countries. They established and enforced banking standards to allow for the
direct debiting of every EUR-denominated bank account within the SEPA region.

In order to debit an account, businesses must collect their customer’s name and
bank account number in IBAN format. During the payment flow, customers must
accept a mandate that gives the business an authorization to debit the account.
Stripe is able to generate this mandate for businesses to present to their
customers. Locate the ID of the mandate used for this payment on the Charge
under the
[payment_method_details.sepa_debit.mandate](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-sepa_debit-mandate)
property. Then, use the mandate ID to [retrieve the
Mandate](https://docs.stripe.com/api/mandates/retrieve).

SEPA Direct Debit is a
[reusable](https://docs.stripe.com/payments/payment-methods#usage), [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method.

SEPA Direct Debit transactions have a limit of 10,000 EUR each. For new users,
there’s an additional weekly limit of 10,000 EUR, which quickly increases as you
process more SEPA direct debit payments. If you need higher limits, [contact
support.](https://support.stripe.com/contact)

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

EU
- **Payment method family**

Bank debit
- **Connect support**

[Yes](https://docs.stripe.com/payments/sepa-debit#connect)
- **Presentment currency**

EUR
- **Recurring Payments**

Yes
- **Payout timing**

See [Payouts](https://docs.stripe.com/payments/sepa-debit#payouts)
- **Dispute support**

[Yes](https://docs.stripe.com/payments/sepa-debit#disputed-payments)
- **Manual capture support**

No
- **Payment confirmation**

Business-initiated
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/sepa-debit#refunds)

## Verification Requirements

Using SEPA Direct Debit requires you to complete additional [identity
verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works)
steps. We prompt you to complete these steps after you request access from the
[Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). If you require
further assistance, please [contact
support](https://support.stripe.com/contact).

## Payment flow

!

[Customer](https://docs.stripe.com/api/customers) selects SEPA Direct Debit at
checkout

!

Customer provides full name, IBAN, and authorizes mandate

!

Customer gets notification that the payment is complete

## Get started

You don’t have to integrate SEPA Direct Debit and other payment methods
individually. If you use our front-end products, Stripe automatically determines
the most relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
SEPA Direct Debit. To get started with one of our hosted UIs, follow a
quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add SEPA Direct Debit from the
Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

If you prefer to manually list payment methods or want to save SEPA Direct Debit
details for future payments, see the following guides:

- [Manually configure SEPA Direct Debit as a
payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [Save SEPA Direct Debit details for future
payments](https://docs.stripe.com/payments/sepa-debit/set-up-payment)

## Debit notification emails

The [SEPA Direct Debit
rulebook](http://www.europeanpaymentscouncil.eu/index.cfm/sepa-direct-debit/sepa-direct-debit-core-scheme-sdd-core)
requires that you notify your customer each time you debit their account. For
this case, by default, Stripe automatically sends the customer an email.

#### Note

When processing SEPA Direct Debit payments using the Stripe [Creditor
ID](https://docs.stripe.com/payments/sepa-debit#creditor-identifiers-(creditor-id)),
debit notification emails are always sent automatically by Stripe.

If you decide to send your customer a custom notification:

- Turn off Stripe emails in the [Stripe Dashboard email
settings](https://dashboard.stripe.com/account/emails). However, if you use the
Sources API, you can only control emails using
[mandate.notification_method](https://docs.stripe.com/api/sources/update#update_source-mandate-notification_method)
(for more information, see [notifying customers of recurring
payments](https://docs.stripe.com/sources/sepa-debit#notifying-customers-of-recurring-payments)).
- Use the
[payment_intent.processing](https://docs.stripe.com/api/events/types#event_types-payment_intent.processing)
event to trigger debit initiation emails.
- The email must include:- The last 4 digits of the debtor’s bank account
- The mandate reference (`sepa_debit[reference]` on the Mandate)
- The amount to be debited
- Your SEPA creditor identifier
- Your contact information
- It’s standard to send notifications at least 14 calendar days before you
create a payment. However, SEPA rules let you send notifications closer to the
payment date—just make sure your mandate clearly states when customers can
expect to receive a notification. The mandate provided by Stripe specifies this
can happen up to two calendar days in advance of future payments, allowing you
to send notifications at payment creation. For recurring payments of the same
amount (for example, a
[subscription](https://docs.stripe.com/billing/subscriptions/creating) of a
fixed amount), you may indicate multiple upcoming debits with corresponding
dates in a single notice.

## Connect

To use SEPA Direct Debits in a [Connect](https://docs.stripe.com/connect)
integration, you must enable SEPA Direct Debit on your platform and request the
`sepa_debit_payments` capability for your connected accounts.

## Creditor Identifiers (Creditor ID)

A SEPA Creditor Identifier (Creditor ID) is an ID associated with each SEPA
Direct Debit payment that identifies the company requesting the payment. While
companies may have multiple creditor identifiers, each creditor identifier is
unique and allows your customers to easily identify the debits on their account.

By default, your Stripe account is configured to use a Stripe Creditor ID when
collecting SEPA Direct Debit Payments. The Creditor Name that appears on bank
statements is determined by the following order of priority:

- Your business name or legal entity name. For Connect, Stripe defaults to using
the connected account’s business name if available. If not, Stripe uses the
platform account’s business name.
- Your Stripe account’s custom [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors).
For Connect accounts, Stripe defaults to the connected account’s statement
descriptor if available. If not, Stripe uses the platform account’s descriptor.
- A default Stripe name (e.g., “Stripe Technologies Europe Ltd”)

We recommend:

- Configuring a recognizable statement descriptor to help customers identify
payments and reduce the risk of disputes.
- If you’re based in the EU, use your own Creditor ID to both reduce dispute
rates and improve your customer experience. You can configure your own Creditor
ID on the [Payment Method
Settings](https://dashboard.stripe.com/settings/payment_methods) page in the
Dashboard.
- If you’re using the Stripe Creditor ID, use [Stripe
Checkout](https://docs.stripe.com/payments/checkout) to collect mandates from
your customers for SEPA Direct Debits.

#### Note

After you’ve collected live SEPA Direct Debit payments on your account, you
can’t change your Creditor ID in the Dashboard. If you need help with this
issue, contact [Stripe support](https://support.stripe.com/contact) for
information about migrating to a new Creditor ID.

### Creditor identifiers and Connect

The charge type of Connect payments changes the creditor identifier and name
which appear on the customer’s bank statement.

Charge typeCreditor ID taken
from[Direct](https://docs.stripe.com/connect/direct-charges)Connected
Account[Destination](https://docs.stripe.com/connect/destination-charges)Platform[Separate
charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)Platform[Destination
(on_behalf_of)](https://docs.stripe.com/connect/destination-charges#settlement-merchant)Connected
Account[Separate charge and transfer
(on_behalf_of)](https://docs.stripe.com/connect/separate-charges-and-transfers#settlement-merchant)Connected
Account
## Failed payments

SEPA Debit payment failures can occur for a number of reasons, such as a
customer’s account being frozen or having insufficient funds.

When a payment fails, Stripe provides a failure reason in the `failure_code`
field on the `Charge`. Stripe also provides an extended description in the
`failure_message` field on the `Charge`. Stripe immediately removes funds from
your Stripe balance after failures.

The following table lists the possible SEPA Debit payment failure codes with
recommended next steps.

Failure codeExplanationNext stepsrefer_to_customerWe don’t have detailed
information about the payment failure because your customer’s bank didn’t
provide a reason code.Reach out to your customer for additional
information.insufficient_fundsThe payment process can’t be completed because
your customer’s bank account lacks the necessary funds.Reach out to your
customer to verify that they have the required funds, then retry the
transaction.debit_disputedYour customer requested that their bank refund this
payment.Reach out to your customer to resolve any dispute, then retry the
transaction.authorization_revokedYour customer revoked their authorization and
refused this payment.Reach out to your customer to understand the reasons for
this revocation, then collect a new mandate and retry the
transaction.debit_not_authorizedThe payment lacks an authorized mandate.Collect
a new mandate and retry the transaction.account_closedThe payment can’t be
processed because your customer’s bank account is closed.Reach out to your
customer for new account details, then try the transaction
again.bank_account_restrictedThe payment can’t be processed because your
customer’s bank has blocked Direct Debits, due to either the bank’s actions or
your customer’s.Reach out to your customer to understand the reason for the
block. If the bank unblocks the account, attempt the transaction
again.debit_authorization_not_matchThe transaction can’t be processed due to
missing or incorrect mandate information.Collect a new mandate from your
customer, then attempt the transaction again.recipient_deceasedThe mandate was
set up on the account of a possibly deceased individual.Verify your customer’s
status before proceeding further.branch_does_not_existThe payment can’t be
processed because the bank branch associated with your customer’s IBAN does not
exist.Reach out to your customer to provide new bank details, then attempt the
transaction again.incorrect_account_holder_nameThe transaction can’t be
processed because your customer’s account information is missing or
incorrect.Collect a new mandate and ask your customer to provide their name and
address exactly as it appears on their bank account. Then, retry the
transaction.invalid_account_numberThe transaction can’t be processed because the
IBAN provided by your customer is incorrect.Reach out to your customer for
correct bank details, then attempt the transaction
again.generic_could_not_processStripe can’t identify a particular reason for the
payment failure.Contact [Support](https://stripe.com/support) for more
information.
## Disputes

SEPA Direct Debit provides a dispute process for customers to dispute payments.

Customers can dispute a payment through their bank on a “no questions asked”
basis up to eight weeks after their account is debited. Any disputes within this
period are automatically honored.

After eight weeks and up to 13 months, a customer can only dispute a payment
with their bank if the debit is considered unauthorized. If this occurs, we
automatically provide the bank with the mandate that the customer approved. This
does not guarantee cancellation of the dispute; the bank can still decide that
the debit was unauthorized and the customer is entitled to a refund.

A dispute can also occur if the bank is unable to debit the customer’s account
because of an issue (for example, the account is frozen or has insufficient
funds), but has already provided the funds to make the charge successful. If
this occurs, the bank reclaims the funds in the form of a dispute.

When a dispute is created, a `charge.dispute.created`
[webhook](https://docs.stripe.com/webhooks) event is sent and Stripe deducts the
dispute amount and dispute fee from your Stripe balance. The dispute fee varies
based on your account’s default settlement currency:

Settlement currencyFailure feeDispute feeAUD5 AUD25 AUDBGN7 BGN30 BGNCAD5 CAD20
CADCHF3 CHF15 CHFCZK85 CZK360 CZKDKK25 DKK115 DKKEUR3.50 EUR15 EURGBP3 GBP13
GBPHKD30 HKD130 HKDHUF1350 HUF5750 HUFJPY550 JPY2375 JPYMXN65 MXN280 MXNNOK40
NOK175 NOKNZD5 NZD30 NZDPLN15 PLN65 PLNRON15 RON75 RONSEK40 SEK175 SEKSGD5 SGD20
SGDUSD5 USD15 USDZAR70 ZAR300 ZAR
Unlike [credit card disputes](https://docs.stripe.com/disputes), SEPA Direct
Debit disputes are final and there is no process for appeal. If a customer
successfully disputes a payment, you must contact them if you want to resolve
the situation. If you come to an arrangement and your customer is willing to
return the funds to you, they must make a new payment.

In general, each dispute includes the reason for its creation, but this varies
from country to country. For example, disputed payments in Germany don’t provide
additional information for privacy reasons.

If a payment is disputed, and that payment is associated with a multi-use
mandate, that mandate could be deactivated. Make sure to check the status of
such mandates after a dispute. You have to re-collect mandate acceptance from
your customers if their previous mandate is deactivated.

## Payouts

SEPA Direct Debit payments are subject to a 5 business day [payout
timing](https://docs.stripe.com/payouts#standard-payout-timing) if your current
payout timing is less than 5 business days or 7 calendar days. When you reach
35,000 USD of SEPA Direct Debit processing volume, payout timing for SEPA Direct
Debit payments returns to normal.

## Refunds

Customers can dispute a payment with their bank even after it has been refunded,
resulting in two credits for the same payment. To prevent fraud, refunds may be
disabled upon first refund attempt until your account has been reviewed. The
review can take up to 2 business days. If you need assistance processing a
refund, contact [Support](https://support.stripe.com/contact/) for further
information.

For accounts with refunds enabled, Stripe recommends issuing refunds on SEPA
Direct Debit payments only when:

- It is a trusted and verified customer
- You have confirmed with the customer that you’re refunding the payment
- 7 business days have passed since you initiated the payment

Refunds for payments made with SEPA Direct Debit must be submitted within 180
days from the date of the original payment. Refunds require additional time to
process (typically three to four business days). If you accidentally debit your
customer, contact them immediately to avoid a payment dispute.

SEPA doesn’t explicitly label refunds when the funds are deposited back to a
customer’s bank account. Instead, refunds are processed as a credit and include
a visible reference to the original payment’s statement descriptor.

When issuing a refund, you should inform your customer immediately that the
refund can take up to 5 business days to arrive in their bank account.

## Smart retries Private preview

## Request early access to SEPA Debit smart retries

Join our private preview.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

- [Single Euro Payments Area
(SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area)
-
[payment_method_details.sepa_debit.mandate](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-sepa_debit-mandate)
- [retrieve the Mandate](https://docs.stripe.com/api/mandates/retrieve)
- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [reusable](https://docs.stripe.com/payments/payment-methods#usage)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [contact support.](https://support.stripe.com/contact)
- [Yes](https://docs.stripe.com/payments/sepa-debit#connect)
- [Payouts](https://docs.stripe.com/payments/sepa-debit#payouts)
- [Yes](https://docs.stripe.com/payments/sepa-debit#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/sepa-debit#refunds)
- [identity
verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Customer](https://docs.stripe.com/api/customers)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [Manually configure SEPA Direct Debit as a
payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment)
- [Save SEPA Direct Debit details for future
payments](https://docs.stripe.com/payments/sepa-debit/set-up-payment)
- [SEPA Direct Debit
rulebook](http://www.europeanpaymentscouncil.eu/index.cfm/sepa-direct-debit/sepa-direct-debit-core-scheme-sdd-core)
- [Creditor
ID](https://docs.stripe.com/payments/sepa-debit#creditor-identifiers-(creditor-id))
- [Stripe Dashboard email settings](https://dashboard.stripe.com/account/emails)
-
[mandate.notification_method](https://docs.stripe.com/api/sources/update#update_source-mandate-notification_method)
- [notifying customers of recurring
payments](https://docs.stripe.com/sources/sepa-debit#notifying-customers-of-recurring-payments)
-
[payment_intent.processing](https://docs.stripe.com/api/events/types#event_types-payment_intent.processing)
- [subscription](https://docs.stripe.com/billing/subscriptions/creating)
- [Connect](https://docs.stripe.com/connect)
- [statement
descriptor](https://docs.stripe.com/get-started/account/statement-descriptors)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Destination
(on_behalf_of)](https://docs.stripe.com/connect/destination-charges#settlement-merchant)
- [Separate charge and transfer
(on_behalf_of)](https://docs.stripe.com/connect/separate-charges-and-transfers#settlement-merchant)
- [Support](https://stripe.com/support)
- [webhook](https://docs.stripe.com/webhooks)
- [credit card disputes](https://docs.stripe.com/disputes)
- [payout timing](https://docs.stripe.com/payouts#standard-payout-timing)
- [Support](https://support.stripe.com/contact/)
- [privacy policy](https://stripe.com/privacy)