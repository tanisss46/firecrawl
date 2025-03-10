# Bank transfer payments

## Learn about bank transfers and managing payments with the customer balance.

Available in: 
Bank transfers provide a safe way for customers to send money over bank rails.
When accepting bank transfers with Stripe, you provide customers with a virtual
bank account number that they can push money to from their own online bank
interface or in-person bank branch. Stripe uses this virtual account number to
automate reconciliation and prevent exposing your real account details to
customers.

## Bank transfer methods

Stripe supports the following bank transfer methods:

- JPY bank transfers in Japan
- GBP bank transfers in the UK
- EUR bank transfers in the UK, US, and SEPA countries
- MXN bank transfers in Mexico
- USD bank transfers in the US, UK, and SEPA countries

Please [contact us](https://support.stripe.com/contact) to request another bank
transfer method. Learn more about [country and currency
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#country-currency-support).

## Get started

You don’t have to integrate Bank Transfers and other payment methods
individually. If you use our front-end products, Stripe automatically determines
the most relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Bank Transfers. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Bank Transfers from the
Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

#### Checkout requirement

Enabling bank transfers on the checkout page requires specifying the
[customer](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer)
in the checkout session.

If you prefer to manually list payment methods, or want to learn more about how
bank transfers work with invoicing and subscriptions, see the following guides:

- [Accept a bank transfer
payment](https://docs.stripe.com/payments/bank-transfers/accept-a-payment)
- [Send an invoice with bank transfer
instructions](https://docs.stripe.com/invoicing/bank-transfer)
- [Set up a subscription with bank transfers as a payment
method](https://docs.stripe.com/billing/subscriptions/bank-transfer)

## Customer balance

Unlike most payment methods, bank transfers don’t allow you to control the
amount a customer sends to you, which means that customers might send too much
or too little money by accident. To manage common overpayment and underpayment
issues, Stripe holds your customer’s bank transfers in a [customer
balance](https://docs.stripe.com/payments/customer-balance) that you can
reconcile payments from. This allows you to track how much your customers owe,
regardless of how much or how often they send funds. If funds are held in the
customer balance for more than 75 days, Stripe automatically attempts to return
the funds to the customer’s bank account. For further information on what
happens when funds remain unreconciled, see the [reconciliation
documentation](https://docs.stripe.com/payments/customer-balance/reconciliation#cash-unreconciled-funds).

## International payments

Bank transfers users in the United States can accept international wire
transfers (SWIFT). International wire transfers may incur fees on the way to
Stripe, which can result in an amount received that’s less than what the
customer originally sent. Stripe-incurred fees appear on the balances page in
the Dashboard, alongside other relevant Stripe fees. The amount shown in the
cash balance is the amount that Stripe received from the customer.

International transfers can take a longer period of time to settle into the
customer balance.

Stripe doesn’t support refunds for international wires. You’re responsible for
executing any refunds related to these payments.

#### Note on currencies

The accounts that support international payments only support their own
currency. For example, US accounts support SWIFT transfers in USD only.

## Cross-border payments

Bank transfers users in the United States can accept EUR payments from customers
in SEPA countries.

With cross-border bank transfers, you create payments in the currency local to
the customer’s country and the customer gets a virtual bank account number local
to their country. You don’t have to have an account setup for the customer’s
country to use cross-border bank transfers. Cross-border bank transfers incur
additional fees that are visible in the Dashboard.

Offering payments to a local bank account with a customer’s local currency helps
reduce the friction and cost involved in sending money abroad.

### Implement cross-border payments

To accept cross-border payments, create an additional bank transfers account
under the customer with the relevant currency. This generates the relevant
funding instructions.

![Add a payment
method](https://b.stripecdn.com/docs-statics-srv/assets/payment-methods-add.566463d538eb9f0e714db1f13abcc458.png)

Add a payment method

![Add a bank transfer
account](https://b.stripecdn.com/docs-statics-srv/assets/add-bank-transfer-account.0e869fea5fbcb29d17aa1060435eaa7f.png)

Add a bank transfer account

## Refunds

You can refund customer balance payments:

- Directly to the customer’s bank account
- Back to the customer’s cash balance, where the refund can be used towards
another customer balance payment

To refund to the customer’s bank account, Stripe requires the customer’s bank
account details. In some cases, Stripe receives these details when the customer
transfers funds. When these details aren’t available, Stripe sends an email to
the customer to collect bank account details and initiate a transfer when we
receive those details.

If your customer has excess funds in their customer balance, you can initiate a
return of funds through the Dashboard or the API. For more information, see
[Refund bank transfer
payments](https://docs.stripe.com/payments/customer-balance/refunding).

## Funding instructions

You can show bank account details to your customer before they make their first
payment through the Dashboard or the API. See [Funding
instructions](https://docs.stripe.com/payments/customer-balance/funding-instructions)
for more details.

## Sender information

You can determine the sender details of an incoming bank transfer through either
the Dashboard or the API. Those details can include the name of the sender, the
reference, and the network through which the transfer arrived.

DashboardAPI- In the [Dashboard](https://dashboard.stripe.com/customers),
navigate to the customer’s page.
- Under **Payment Methods**, expand the cash balance tab.
- Open the Cash Balance page by clicking **View balance details**.

![Payment methods
section](https://b.stripecdn.com/docs-statics-srv/assets/payment-methods-section.98d98636d90fbf8ea6e5834dcdde1133.png)

Payment methods section

On the cash balance page, the **Transactions** section displays a list of the
customer’s incoming and outgoing cash balance transactions.

![List of all customer cash balance
transactions](https://b.stripecdn.com/docs-statics-srv/assets/transactions-list.f8e2bee93047bd6c85021cfb3db52348.png)

List of all customer cash balance transactions

Incoming transfers have type **Funding**. Find the transfer you’re interested in
and open its details page by clicking its description.

![Funding details sender
information](https://b.stripecdn.com/docs-statics-srv/assets/funding-details-sender-info.b78a278b7f04e003480c0d4308af206b.png)

Funding details sender information

## Disputes

Bank transfer payments can’t be reversed except for USD and CAD transactions.

### USD disputes

USD bank transfers that go through the ACH network in the US can be reversed.
After you push a transfer, you can request that your bank reverse it. You must
provide the bank with evidence as to why they should reverse the transfer. The
remitting bank then sends a reversal to the beneficiary bank. A reversal must be
sent no later than 5 days after the payment.

### CAD disputes

CAD bank transfers that go through ACH reversals are always initiated by the
remitting bank, and the beneficiary bank must honor them.

## Connect

[Stripe Connect](https://docs.stripe.com/connect/how-connect-works) can be used
with bank transfers to process payments on behalf of connected accounts.
[Connect](https://docs.stripe.com/connect) platforms can use bank transfers with
[any type of charges](https://docs.stripe.com/connect/charges#types).

The [on_behalf_of
attribute](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-on_behalf_of)
isn’t supported.

### Accepting bank transfer payments as the connected account

[Direct charges](https://docs.stripe.com/connect/direct-charges) require the
connected account itself (not the platform) to have activated the bank transfers
payment method—Connect platforms can use the [relevant bank transfers
capability](https://docs.stripe.com/connect/account-capabilities#payment-methods)
to determine whether this is the case for a connected account. [Standard Connect
accounts](https://docs.stripe.com/connect/standard-accounts) can request the
relevant capability from their Stripe Dashboard.

### Activation process

The process varies by country, but in general for bank transfer payments, the
[required
information](https://docs.stripe.com/connect/required-verification-information)
is the same as what’s necessary to activate a Stripe account for payments. If
the account doesn’t fulfill all the required information, the capability remains
`inactive` with any issues highlighted on the [capability
object](https://docs.stripe.com/api/capabilities/object) in the
`requirements.currently_due` and `requirements.disabled_reason` fields until
these issues have been addressed. After all the highlighted issues are resolved,
the capability’s `status` changes to `active`, unless there are issues
activating the account in general, in which case Stripe sends the Connect
platform owner an email.

## Product support

Payment
method[Connect](https://docs.stripe.com/connect)[Checkout](https://docs.stripe.com/payments/checkout)[Payment
Links](https://docs.stripe.com/payment-links)[Payment
Element](https://docs.stripe.com/payments/payment-element)[Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)[Mobile
Payment
Element](https://docs.stripe.com/payments/mobile)[Subscriptions](https://docs.stripe.com/subscriptions)[Invoicing](https://docs.stripe.com/invoicing)[Customer
Portal](https://docs.stripe.com/customer-management)Bank transfers1,2
1 Not supported when using Checkout in subscription mode.2 Not supported when
using Checkout in setup mode.

## API support

Payment methodAPI
enum[PaymentIntents](https://docs.stripe.com/payments/payment-intents)[SetupIntents](https://docs.stripe.com/payments/setup-intents)[Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)[Setup
future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)1Requires
redirect2Bank transfers`customer_balance`No
1 Cards and bank debit methods including SEPA debit, AU BECS direct debit, and
ACSS debit support both `on_session` and `off_session` with [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
All other payment method types either don’t support `setup_future_usage` or only
support `off_session`.2 Payment methods might require confirmation with
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
to indicate where Stripe should redirect your customer after they complete the
payment.

## Unsupported businesses

Stripe can’t accept payments for certain types of businesses. In addition to the
[Restricted Business list](https://stripe.com/restricted-businesses), Stripe
doesn’t support bank transfers if your business falls into any of the following
categories:

EUUK- Automated Cash Disburse
- Charity
- Manual Cash Disburse
- Membership organization (other)
- Miscellaneous and Specialty Retail Stores
- Political organization
- Religious organization
- Social, fraternity, sports organization

## Unsupported products and features

Bank transfers don’t support Payment Links.

## Interested in getting early access to cross-border bank transfers?

This feature allows you to accept bank transfers in currencies outside of your
region. Please provide your email address for us to review your suitability and
our team will contact you soon.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [contact us](https://support.stripe.com/contact)
- [country and currency
support](https://docs.stripe.com/payments/payment-methods/payment-method-support#country-currency-support)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
-
[customer](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer)
- [Accept a bank transfer
payment](https://docs.stripe.com/payments/bank-transfers/accept-a-payment)
- [Send an invoice with bank transfer
instructions](https://docs.stripe.com/invoicing/bank-transfer)
- [Set up a subscription with bank transfers as a payment
method](https://docs.stripe.com/billing/subscriptions/bank-transfer)
- [customer balance](https://docs.stripe.com/payments/customer-balance)
- [reconciliation
documentation](https://docs.stripe.com/payments/customer-balance/reconciliation#cash-unreconciled-funds)
- [Refund bank transfer
payments](https://docs.stripe.com/payments/customer-balance/refunding)
- [Funding
instructions](https://docs.stripe.com/payments/customer-balance/funding-instructions)
- [Dashboard](https://dashboard.stripe.com/customers)
- [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
- [Connect](https://docs.stripe.com/connect)
- [any type of charges](https://docs.stripe.com/connect/charges#types)
- [on_behalf_of
attribute](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-on_behalf_of)
- [Direct charges](https://docs.stripe.com/connect/direct-charges)
- [relevant bank transfers
capability](https://docs.stripe.com/connect/account-capabilities#payment-methods)
- [Standard Connect accounts](https://docs.stripe.com/connect/standard-accounts)
- [required
information](https://docs.stripe.com/connect/required-verification-information)
- [capability object](https://docs.stripe.com/api/capabilities/object)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Express Checkout
Element](https://docs.stripe.com/elements/express-checkout-element)
- [Mobile Payment Element](https://docs.stripe.com/payments/mobile)
- [Subscriptions](https://docs.stripe.com/subscriptions)
- [Invoicing](https://docs.stripe.com/invoicing)
- [Customer Portal](https://docs.stripe.com/customer-management)
- [PaymentIntents](https://docs.stripe.com/payments/payment-intents)
- [SetupIntents](https://docs.stripe.com/payments/setup-intents)
- [Manual
capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [Setup future
usage](https://docs.stripe.com/payments/save-during-payment?platform=web&ui=elements)
- [setup future
usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
-
[return_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url)
- [Restricted Business list](https://stripe.com/restricted-businesses)
- [privacy policy](https://stripe.com/privacy)