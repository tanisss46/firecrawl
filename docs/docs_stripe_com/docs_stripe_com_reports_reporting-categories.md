# Reporting categories and types

## Understand categories on BalanceTransaction objects and its distinctions.

Learn more about the `reporting_category` field on `BalanceTransaction` objects,
and how it differs from `type` and other categorizations. This topic covers:

- [Why introduce a new
categorization?](https://docs.stripe.com/reports/reporting-categories#why-new-categorization)
- [Reporting categories
reference](https://docs.stripe.com/reports/reporting-categories#reference)

## Why introduce a new categorization?

The `BalanceTransaction` object’s `reporting_category` field improves on the
`type` field by providing a more-useful grouping for most finance and reporting
purposes. The following sections highlight the new field’s advantages.

##### More-granular breakdown of `type=adjustment`

The `reporting_category` attribute separates balance transactions with
`type=adjustment` into several different categories, including disputes, dispute
reversals, and failed refunds. Additionally, several types of fees and
[Connect](https://docs.stripe.com/connect) platform-fee refunds are now
explicitly categorized with `reporting_category=fee`.

#### A separate category for partial-capture reversals

If you are [separately authorizing and
capturing](https://docs.stripe.com/charges/placing-a-hold) payments, and you
capture an amount less than the initial authorization, you will see two balance
transactions: one for the full amount of the authorization, and another
reversing the uncaptured portion. (Summing the two balance transactions yields
the captured portion of the charge.)

The balance transaction reversing the uncaptured portion has `type=refund`, just
as if you had refunded a portion of a sale at some later time. To allow separate
handling of these objects—perhaps counting them against the initial sale amount,
rather than as a separate refund—we label these with the distinct reporting
category `partial_capture_reversal`.

#### Consolidate multiple types into common categories

Using the `type` field, balance transactions arising from card-based charges are
represented with `type=charge`, while those made with [other payment
methods](https://docs.stripe.com/payments/payment-methods/overview) are
represented with `type=payment`. Similarly, refunds and failures for cards
versus alternative payment methods have the distinct types `refund` and
`payment_refund`.

We found that these distinctions made many common reporting tasks unnecessarily
awkward, and so `reporting_category` simplifies these (and other) groups of
types, as follows:

Balance transaction typesReporting category`charge`, `payment``charge``refund`,
`payment_refund``refund``payout_cancel`,
`payout_failure``payout_reversal``transfer`,
`recipient_transfer``transfer``transfer_cancel`, `transfer_failure`,
`recipient_transfer_cancel`, `recipient_transfer_failure``transfer_reversal`
##### More-descriptive category names

We’ve renamed several balance transaction types for greater clarity:

Balance transaction typeReporting
category`application_fee``platform_earning``application_fee_refund``platform_earning_refund``stripe_fee``fee``reserve_transaction``connect_reserved_funds``reserved_funds``risk_reserved_funds`
## Reporting categories reference

This reference covers four groups of reporting categories:

- [Payments-related reporting
categories](https://docs.stripe.com/reports/reporting-categories#charge_and_payment_related)
- [Balance-related reporting
categories](https://docs.stripe.com/reports/reporting-categories#balance_related)
- [Issuing-related reporting
categories](https://docs.stripe.com/reports/reporting-categories#issuing_related)
- [Connect-related reporting
categories](https://docs.stripe.com/reports/reporting-categories#connect_related)

### Payments-related reporting categories

These reporting categories are related to creating and refunding charges as part
of processing payments.

### `charge`

[Charges](https://docs.stripe.com/payments/charges-api) include payments from
cards and from [other payment
methods](https://docs.stripe.com/sources#supported-payment-methods). If you are
[separately authorizing and
capturing](https://docs.stripe.com/charges/placing-a-hold) payments, only the
captured charges will be included here.

- Balance transaction type(s): `charge`, `payment`, or `validation`
- Section(s) in the monthly report: *Payments (cards), Payments (other)*

### `charge_failure`

[ACH, direct debit](https://docs.stripe.com/sources#supported-payment-methods),
and other [asynchronous payment
methods](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
remain in a pending state until they either succeed or fail. You will see a
pending balance transaction with the reporting category `charge` appear when the
payment is created in a pending state. A `charge_failure` will appear if the
pending payment later fails.

- Balance transaction type(s): `payment_failure_refund`
- Section(s) in the monthly report: *Other Adjustments*

### `dispute`

When a customer [disputes a charge](https://docs.stripe.com/disputes), Stripe
deducts the disputed amount from your balance.

- Balance transaction type(s): `adjustment`or
`adjusted_for_overdraft_transaction`
- Section(s) in the monthly report: *Disputes*

### `dispute_reversal`

When you [win a
dispute](https://docs.stripe.com/disputes#responding-to-a-dispute), the disputed
amount is returned to your balance.

- Balance transaction type(s): `adjustment`
- Section(s) in the monthly report: *Dispute Reversals*

### `partial_capture_reversal`

If you are [separately authorizing and
capturing](https://docs.stripe.com/charges/placing-a-hold) payments, and you
capture an amount less than the initial authorization, you will see a `charge`
for the full authorization amount, and a `partial_capture_reversal` for the
uncaptured portion.

- Balance transaction type(s): `refund`
- Section(s) in the monthly report: *Payments (cards)*

### `refund`

Payments you’ve [refunded](https://docs.stripe.com/refunds) to your customers.
(Does not include charge failures or partial capture reversals, which are listed
separately.)

- Balance transaction type(s): `refund`or `payment_refund`
- Section(s) in the monthly report: *Refunds (cards), Refunds (other)*

### `refund_failure`

Created when a [credit card charge refund](https://docs.stripe.com/refunds)
fails, and Stripe returns the funds to your balance.

This may occur if your customer’s bank or card issuer is unable to correctly
process a refund (e.g., due to a closed bank account or a problem with the
card).

- Balance transaction type(s): `refund_failure`
- Section(s) in the monthly report: *Other Adjustments*

### Balance-related reporting categories

These reporting categories are related to changes that affect your Stripe
balance, such as payouts, fees, and top-ups.

### `anticipation_repayment`

Repayments made to service an anticipation loan in Brazil. These repayments go
to the financial institution to whom you have sold your receivables.

- Balance transaction type(s): `anticipation_repayment`
- Section(s) in the monthly report: *Anticipation Repayments*

### `climate_order_purchase`

Funds used to purchase carbon removal units from Frontier Climate.

- Balance transaction type(s): `climate_order_purchase`or
`climate_reservation_purchase`
- Section(s) in the monthly report: *Other Adjustments*

### `climate_order_refund`

Funds refunded to your balance when a Climate Order is canceled.

- Balance transaction type(s): `climate_order_refund`or
`climate_reservation_refund`
- Section(s) in the monthly report: *Other Adjustments*

### `contribution`

Funds contributed via Stripe to a cause (currently Stripe Climate).

- Balance transaction type(s): `contribution`
- Section(s) in the monthly report: *Other Adjustments*

### `fee`

Fees for Stripe software and services (e.g., for
[Radar](https://docs.stripe.com/radar),
[Connect](https://docs.stripe.com/connect),
[Billing](https://docs.stripe.com/billing), and
[Identity](https://docs.stripe.com/identity)).

- Balance transaction type(s): `stripe_fee`
- Section(s) in the monthly report: *Other Adjustments*

### `other_adjustment`

Miscellaneous adjustments to your Stripe balance.

- Balance transaction type(s): `adjustment`, `obligation_outbound`, or
`obligation_reversal_inbound`
- Section(s) in the monthly report: *Other Adjustments*

### `payment_network_reserve_hold`

Funds that a payment network holds in reserve (e.g. to mitigate risk).

- Balance transaction type(s): `payment_network_reserve_hold`
- Section(s) in the monthly report: *Other Adjustments*

### `payment_network_reserve_release`

Funds that a payment network releases from a reserve.

- Balance transaction type(s): `payment_network_reserve_release`
- Section(s) in the monthly report: *Other Adjustments*

### `payout`

[Payouts](https://docs.stripe.com/payouts) from your Stripe balance to your bank
account.

- Balance transaction type(s): `payout`
- Section(s) in the monthly report: *Payouts and Transfers*

### `payout_minimum_balance_hold`

Minimum balance held from a payout.

- Balance transaction type(s): `payout_minimum_balance_hold`
- Section(s) in the monthly report: *Payout minimum balance hold*

### `payout_minimum_balance_release`

Minimum balance released after a payout.

- Balance transaction type(s): `payout_minimum_balance_release`
- Section(s) in the monthly report: *Payout minimum balance release*

### `payout_reversal`

Funds returned to your balance if a payout fails after it is initially created
(e.g., due to an invalid account number or a cancellation). [Learn
more](https://docs.stripe.com/payouts#payout-failures).

- Balance transaction type(s): `payout_cancel`or `payout_failure`
- Section(s) in the monthly report: *Payouts and Transfers: Failures and
Refunds*

### `risk_reserved_funds`

When Stripe holds your funds in reserve to mitigate risk, two balance
transactions are created: one to debit the funds from your balance, and a second
to credit the funds back to your balance at the end of the reserve period.

- Balance transaction type(s): `reserved_funds`
- Section(s) in the monthly report: *Other Adjustments*

### `tax`

Taxes collected by Stripe to be remitted to the appropriate local governments.
Typically, this is a tax on Stripe fees.

- Balance transaction type(s): `tax_fee`
- Section(s) in the monthly report: *Other Adjustments*

### `topup`

Funds you transferred into your Stripe balance from your bank account. [Learn
more](https://docs.stripe.com/connect/top-ups).

- Balance transaction type(s): `topup`
- Section(s) in the monthly report: *Other Adjustments*

### `topup_reversal`

If an initially successful top-up fails or is cancelled, the credit to your
Stripe balance is reversed. [Learn
more](https://docs.stripe.com/connect/top-ups).

- Balance transaction type(s): `topup_reversal`
- Section(s) in the monthly report: *Other Adjustments*

### `unreconciled_customer_funds`

When a customer has unreconciled funds within Stripe for more than ninety days,
Stripe transfers those funds to your balance.

- Balance transaction type(s): `transferred_to_balance_transaction`
- Section(s) in the monthly report: *Other Adjustments*

### Issuing-related reporting categories

These reporting categories are created as part of using the [Issuing
API](https://docs.stripe.com/issuing).

### `issuing_authorization_hold`

When [an issued card](https://docs.stripe.com/issuing) is used to make a
purchase, an
[authorization](https://docs.stripe.com/issuing/purchases/authorizations) is
created. If the authorization is approved, a balance transaction is created with
the type `issuing_authorization_hold` to hold the authorized amount in reserve
from your account balance, until the authorization is either captured or voided.
Some merchants can also update an authorization to request an additional amount
(e.g., to extend a hotel booking or add a tip), and this is also represented as
a balance transaction with the type `issuing_authorization_hold`.

- Balance transaction type(s): `issuing_authorization_hold`
- Section(s) in the monthly report: *Other Adjustments*

### `issuing_authorization_release`

When an authorized purchase, made with [an issued
card](https://docs.stripe.com/issuing), is captured by the merchant, the funds
previously held for the authorization (`issuing_authorization_hold`) are
released with a `issuing_authorization_release` balance transaction.
Simultaneously, [an issuing
transaction](https://docs.stripe.com/issuing/transactions) is created, and the
purchase amount is deducted from your Stripe balance in another balance
transaction with the type `issuing_transaction`.

- Balance transaction type(s): `issuing_authorization_release`
- Section(s) in the monthly report: *Other Adjustments*

### `issuing_disbursement`

Credits to your balance for rewards, discounts, and other miscellaneous
adjustments.

- Balance transaction type(s): `issuing_disbursement`
- Section(s) in the monthly report: *Other Adjustments*

### `issuing_dispute`

When you dispute an [Issuing
transaction](https://docs.stripe.com/issuing/transactions) and funds return to
your Stripe balance.

- Balance transaction type(s): `issuing_dispute`
- Section(s) in the monthly report: *Other Adjustments*

### `issuing_dispute_fraud_liability_debit`

Funds deducted from your account to cover [fraud loss
liability](https://docs.stripe.com/issuing/purchases/disputes/fraud-liability)

- Balance transaction type(s): `issuing_dispute_fraud_liability_debit`
- Section(s) in the monthly report: *Other Adjustments*

### `issuing_dispute_provisional_credit`

[Provisional
Credit](https://docs.stripe.com/issuing/purchases/disputes/provisional-credits)
granted to Issuing balance

- Balance transaction type(s): `issuing_dispute_provisional_credit`
- Section(s) in the monthly report: *Other Adjustments*

### `issuing_dispute_provisional_credit_reversal`

Previous [Provisional
Credit](https://docs.stripe.com/issuing/purchases/disputes/provisional-credits)
being reversed from Issuing balance

- Balance transaction type(s): `issuing_dispute_provisional_credit_reversal`
- Section(s) in the monthly report: *Other Adjustments*

### `issuing_transaction`

When an authorized purchase, made with an [issued
card](https://docs.stripe.com/issuing), has been authorized and captured by the
merchant, [an issuing transaction](https://docs.stripe.com/issuing/transactions)
is created, and the purchase amount is deducted from your Stripe balance with a
`issuing_transaction` balance transaction.

- Balance transaction type(s): `issuing_transaction`
- Section(s) in the monthly report: *Other Adjustments*

### Connect-related reporting categories

These reporting categories are related to using the [Connect
API](https://docs.stripe.com/connect) and related APIs, such as [instant
payouts](https://docs.stripe.com/connect/instant-payouts).

### `advance`

Incrementing funds as part of an advance operation to change the date that funds
settle to your balance. For example, this can occur when you create an [instant
payout](https://docs.stripe.com/payouts/instant-payouts-with-advance-funding)
and the requested payout amount is greater than your available balance. Funds
are credited to a new `available_on` date and debited from the original
`available_on` date to cover the difference.

- Balance transaction type(s): `advance`
- Section(s) in the monthly report: *Other Adjustments*

### `advance_funding`

Decrementing funds as part of an advance operation to change the date that funds
settle to your balance. For example, this can occur when you create an [instant
payout](https://docs.stripe.com/payouts/instant-payouts-with-advance-funding)
and the requested payout amount is greater than your available balance. Funds
are credited to a new `available_on` date and debited from the original
`available_on` date to cover the difference.

- Balance transaction type(s): `advance_funding`
- Section(s) in the monthly report: *Other Adjustments*

### `connect_collection_transfer`

If one of your connected accounts has a negative balance for 180 days, Stripe
transfers a portion of your balance, to zero out that account’s balance. [Learn
more](https://docs.stripe.com/connect/account-balances#understanding-connected-reserve-balances).

- Balance transaction type(s): `connect_collection_transfer`
- Section(s) in the monthly report: *Reflected in "Reserve" section*

### `connect_reserved_funds`

If one of your connected accounts’ balances becomes negative, Stripe temporarily
reserves a portion of your balance to ensure that funds can be covered.

If one of your connected accounts’ previously negative balance becomes less
negative due to activity on account, another `reserve_transaction` is created to
release a corresponding portion of the funds held in reserve. [Learn
more](https://docs.stripe.com/connect/account-balances#understanding-connected-reserve-balances).

- Balance transaction type(s): `reserve_transaction`
- Section(s) in the monthly report: *Reflected in "Reserve" section*

### `platform_earning`

Earnings you’ve generated by collecting [platform
fees](https://docs.stripe.com/connect/direct-charges#collect-fees) via [Stripe
Connect charges](https://docs.stripe.com/connect/charges).

- Balance transaction type(s): `application_fee`
- Section(s) in the monthly report: *Application Revenue*

### `platform_earning_refund`

[Platform fees](https://docs.stripe.com/connect/direct-charges#collect-fees)
that you have returned to your connected accounts.

- Balance transaction type(s): `application_fee_refund`
- Section(s) in the monthly report: *Application Revenue Returned*

### `transfer`

Funds sent from your balance to the balance of your [connected
accounts](https://docs.stripe.com/connect/separate-charges-and-transfers).

- Balance transaction type(s): `transfer`or `recipient_transfer`
- Section(s) in the monthly report: *Payouts and Transfers*

### `transfer_reversal`

Transfers to your connected accounts that have been cancelled.

- Balance transaction type(s): `transfer_cancel`, `transfer_refund`,
`recipient_transfer_cancel`, or `recipient_transfer_failure`
- Section(s) in the monthly report: *Payouts and Transfers: Failures and
Refunds*

## Links

- [Connect](https://docs.stripe.com/connect)
- [separately authorizing and
capturing](https://docs.stripe.com/charges/placing-a-hold)
- [other payment
methods](https://docs.stripe.com/payments/payment-methods/overview)
- [Charges](https://docs.stripe.com/payments/charges-api)
- [other payment
methods](https://docs.stripe.com/sources#supported-payment-methods)
- [asynchronous payment
methods](https://docs.stripe.com/sources#synchronous-or-asynchronous-confirmation)
- [disputes a charge](https://docs.stripe.com/disputes)
- [win a dispute](https://docs.stripe.com/disputes#responding-to-a-dispute)
- [refunded](https://docs.stripe.com/refunds)
- [Radar](https://docs.stripe.com/radar)
- [Billing](https://docs.stripe.com/billing)
- [Identity](https://docs.stripe.com/identity)
- [Payouts](https://docs.stripe.com/payouts)
- [Learn more](https://docs.stripe.com/payouts#payout-failures)
- [Learn more](https://docs.stripe.com/connect/top-ups)
- [Issuing API](https://docs.stripe.com/issuing)
- [authorization](https://docs.stripe.com/issuing/purchases/authorizations)
- [an issuing transaction](https://docs.stripe.com/issuing/transactions)
- [fraud loss
liability](https://docs.stripe.com/issuing/purchases/disputes/fraud-liability)
- [Provisional
Credit](https://docs.stripe.com/issuing/purchases/disputes/provisional-credits)
- [instant payouts](https://docs.stripe.com/connect/instant-payouts)
- [instant
payout](https://docs.stripe.com/payouts/instant-payouts-with-advance-funding)
- [Learn
more](https://docs.stripe.com/connect/account-balances#understanding-connected-reserve-balances)
- [platform fees](https://docs.stripe.com/connect/direct-charges#collect-fees)
- [Stripe Connect charges](https://docs.stripe.com/connect/charges)
- [connected
accounts](https://docs.stripe.com/connect/separate-charges-and-transfers)