# Connect margin reports

## Compute your margins by analyzing your Connect volume, revenue, and fees associated with activity where you're responsible for pricing and fees.

The Connect margin reports show platforms their aggregated and transaction-level
payment volumes, revenue, and fees associated with activity where the platform
is responsible for [pricing and
fees](https://docs.stripe.com/api/accounts/create#create_account-controller-fees-payer).
Use these reports to calculate your margins and set your fees appropriately
given your underlying Stripe fees and network costs.

## Platform support

These reports only support platforms that [explicitly state an application
fee](https://docs.stripe.com/connect/destination-charges?fee-type=application-fee#collect-fees),
either directly in the API or through [Platform Pricing
Tools](https://docs.stripe.com/connect/platform-pricing-tools). They don’t
include revenue from account debits or
[transfer_data.amount](https://docs.stripe.com/connect/destination-charges?fee-type=transfer-amount#collect-fees).

## Available margin reports

Report typeDescriptionUsageSummaryPlatform-level aggregated view of Connect
volume, revenue, and feesCalculate monthly margins for your platformConnected
AccountConnected account-level view of Connect volume, revenue, and feesIdentify
which connected accounts drive margins up or downTransactionTransaction-level
view of Connect volume, revenue, and feesIdentify which transactions drive
margins up or down

![Example of a summary margin
report](https://b.stripecdn.com/docs-statics-srv/assets/summary-margin-report.4b348d78a47df2e2ab99328136a93cb4.png)

Summary margin report example

## Access the margin reports

- Go to the [Connect Margin Report](https://dashboard.stripe.com/connect/margin)
page. It’s also available in the [Reports
hub](https://dashboard.stripe.com/reports/hub) in your Stripe Dashboard. Margin
Reports are only available in live mode, not in test mode or sandboxes.
- Using the month picker, select the **time-period**, then click **Download** on
your desired Margin Report type. The report for a month is available 7 days
after the end of that month.

## User access

Users with the following [user
roles](https://docs.stripe.com/get-started/account/teams/roles) can access the
Margin Reports:

- Administrator
- Analyst
- Data Migration Specialist
- Developer
- Tax Analyst
- View only

## Margin report data

Margin reports include charges based on the timestamp of the originating event,
not the timestamp when a fee is assessed. For example, to view a fee assessed on
February 1 for a charge created on January 31, run the report for January. These
reports only support platforms that [explicitly state an application
fee](https://docs.stripe.com/connect/destination-charges?fee-type=application-fee#collect-fees),
either directly in the API or through [Platform Pricing
Tools](https://docs.stripe.com/connect/platform-pricing-tools). They don’t
include revenue from account debits or
[transfer_data.amount](https://docs.stripe.com/connect/destination-charges?fee-type=transfer-amount#collect-fees).

A margin report includes data for the following types of charges:

- [Connect direct charges](https://docs.stripe.com/connect/direct-charges) where
the platform collects application fees
- [Destination charges](https://docs.stripe.com/connect/destination-charges)
where the platform collects application fees, with or without on_behalf_of

It also includes application fees and Stripe fees paid for [Instant
Payouts](https://docs.stripe.com/connect/instant-payouts).

It doesn’t include data for the following types of charges:

- Direct charges where the connected account is responsible for fees
- Direct charges on the platform (such as SaaS subscriptions they run on the
same account)
- Separate charges and transfers
- Direct charges initiated by a connected account
- Direct charges for connected accounts that are no longer connected to your
platform when you generate the report

#### Note

A margin report normalizes all values to USD using the conversion rate at the
time of activity. We plan to add other normalization currencies in a future
release.

## Available columns for each margin report

The Summary and Connected Account margin reports show aggregated monthly data,
whereas the Transaction margin report shows data for individual transactions.

#### Note

The total amounts shown in the Summary and Connected Account margin reports are
normally greater than the sum of the amounts in the Transaction margin report.
That’s because the Transaction report includes only fees that apply at a
transaction level. It doesn’t include out-of-band fees, such as Card Account
Updater fees or non-transactional scheme fees.

### Summary margin report

This report shows the aggregated volume, revenue, and fees for the platform for
the entire selected month. You can calculate the net volume, revenue, or fees as
the sum of all values in their category. To determine the net margin, add the
net revenue and net fees.

You can calculate net take rate in several ways. One common method is (net
margin)/net volume)×10000.

Amount fields include:

- **subtotal_amount**: Amount excluding any tax
- **tax_amount**: Amount of tax
- **total_amount**: sum of `subtotal_amount` and `tax_amount`

The Summary margin report includes the following data for the selected time
period:

TypeCategoryDescriptionVolume Charges, Payment method = {payment method}Volume
of charges for the {payment method} payment methodRefundsVolume of
refundsDisputesVolume of disputesRevenue Application fee, payment method =
{payment method}Amount of application fees for the {payment method} payment
methodApplication fee refundsAmount of application fees refunded by the
platformNetwork fee (assessed by card networks) Card payments - Transaction
network costsInterchange (or discount, for Amex) fees and transaction-level
scheme fees; a single charge typically incurs one interchange fee and one or
more scheme feesCard payments - Other network costsNon-transactional scheme fees
such as FANF (Fixed Acquirer Network Fee from Visa) directly attributable to a
connected accountCard payments - Other network costs (platform
level)Non-transactional scheme fees directly attributable to the platform
itselfStripe fee Stripe processing fees - {payment method}Stripe processing fees
for cards and other payment methodsConnect - {fee type}Connect fees, such as
Account Volume Billing, Active Account Billing, and (for Stripe Managed Risk and
Support) Loss LiabilityVariesOther product fees that apply to the platform and
are directly attributable to a connected account, such as for Radar and Card
Account UpdaterVaries (platform level)Other product fees that apply to the
platform and are directly attributable to the platform itself, such as Card
Account Updater fees for cards created on the platform
Disconnecting an account from your platform can affect the values in the Summary
margin report.

### Connected Account margin report

This report shows all volume, revenue, and fees attributed to each connected
account for the entire selected month. It doesn’t include any connected accounts
that have been deleted or disconnected from your platform. You can use it to
understand which connected accounts are margin-positive, margin-neutral, or
margin-negative for your platform.

Because fees appear as negative numbers, you can calculate a connected account’s
margin as the sum of its associated revenues and fees.

Connected account detail fields include:

- **connected_account_id**: Unique identifier of the connected account
associated with the charge
- **business_name**
- **display_name**
- **connected_account_country**: Two-letter ISO code representing the country of
the transaction account

The Connected Account margin report includes the following data for the selected
time period:

TypeCategoryDescriptionVolume amountSum of the amounts of all charges on the
connected account, excluding any taxcharge_countNumber of charges on the
connected accountamount_refundedSum of the amounts of all refunds for charges on
the connected accountrefund_countNumber of charges on the connected account that
were refundedamount_disputedSum of the disputed amounts on charges on the
connected accountdispute_countNumber of charges on the connected account that
were disputedRevenue application_fee_amountSum of the amounts requested by the
platform to be deducted from the charge amounts across all charges on the
connected accountapplication_fee_amount_refundedTotal amount of the
application_fee_amount that was refunded to the connected
accountapplication_fee_instant_payouts_amountSum of the application fees earned
by monetizing Instant Payouts to the connected
accountapplication_fee_instant_payouts_amount_refundedTotal amount of the
application_fee_instant_payouts_amount that was refunded to the connected
accountFees network_costs_subtotal_amountSum of the Interchange (or discount,
for American Express) fees and transaction-level scheme fees attributed to the
connected accountother_network_costs_subtotal_amountSum of the non-transactional
scheme fees, such as the Fixed Acquirer Network Fee (FANF) from Visa, attributed
to the connected accountstripe_per_auth_fee_subtotal_amountSum of the
per-authorization fees charged by Stripe for card processing with IC+ pricing
attributed to the connected accountstripe_volume_fee_subtotal_amountSum of the
Volume fees charged by Stripe for card processing with IC+ pricing attributed to
the connected accountstripe_other_card_payments_fees_subtotal_amountSum of the
other card processing fees charged by Stripe for card processing, such as
per-dispute and per-sale fees, attributed to the connected
accountstripe_processing_fees_subtotal_amountSum of the fees charged by Stripe
for payments processing for users with IC+ pricing, such as fees for using
payment methods like Affirm or AfterPay, not including Stripe card payments fees
or network costs, attributed to the connected
accountstripe_dispute_fees_subtotal_amountSum of the dispute fees paid by the
platform attributed to the connected
accountstripe_refund_fees_subtotal_amountSum of the refund fees paid by the
platform attributed to the connected
accountadaptive_acceptance_fee_subtotal_amountSum of the adaptive acceptance
fees attributed to the connected
accountcard_account_updater_fee_subtotal_amountSum of the card account updater
fees attributed to the connected
accountconnect_account_initiation_billing_fee_subtotal_amountSum of the account
initialization fees attributed to the connected
accountconnect_loss_liability_fee_subtotal_amountSum of the fees charged by
Stripe to cover risk losses attributed to the connected
accountconnect_crossborder_transfer_fee_subtotal_amountSum of the the
[cross-border payout](https://docs.stripe.com/connect/cross-border-payouts)
transfer fees attributed to the connected
accountconnect_instant_payout_fee_subtotal_amountSum of the Instant Payout fees
attributed to the connected
accountconnect_active_account_billing_fee_subtotal_amountSum of the active
connected account fees attributed to the connected account (when calculating
this value, an account that didn’t receive any payouts to a bank account or
debit card is not considered active)connect_payout_fee_subtotal_amountSum of the
connect payout fixed fees attributed to the connected
accountconnect_account_volume_billing_fee_subtotal_amountSum of the connect
payout volume fees attributed to the connected
accountconnections_verification_fee_subtotal_amountSum of the bank account
verification fees attributed to the connected
accountnetwork_token_fee_subtotal_amountSum of the network token fees attributed
to the connected accountradar_fees_subtotal_amountSum of the radar fees,
including radar for fraud teams, attributed to the connected
accountstripe_billing_fees_subtotal_amountSum of the Stripe Billing fees
attributed to the connected accountstripe_tax_fees_subtotal_amountSum of the
Stripe tax fees attributed to the connected
accountterminal_fees_subtotal_amountSum of the terminal fees, such as tap to
pay, P2PE, per-auth, and per-sale services fees, attributed to the connected
accountother_fees_subtotal_amountSum of all other fees charged to the connected
account that aren’t included in another fieldtax_amountSum of the taxes that
Stripe has charged for transactions attributed to the connected
accountcurrencyCurrency of the values
### Transaction margin report

This report shows a transaction-level breakdown of volume, revenue, and fees for
the entire selected month. It doesn’t include non-transactional revenue or fees.
You can use it to understand which transactions are margin-positive,
margin-neutral, or margin-negative.

Because fees appear as negative numbers, you can calculate a transaction’s
margin as the sum of its associated revenues and fees.

#### Note

Don’t use the Transaction margin report to understand profitability at the level
of a connected account. Use the Connected Account margin report.

Charge detail fields include:

- **charge_id**: Unique identifier of the charge
- **connected_account_id**: Unique identifier of the connected account
associated with the charge
- **activity_at**: Time in UTC at which we attribute the line item
- **payment_method_type**: Type of payment method used for the transaction, such
as `card`, `ACH credit transfer`, or `link`
- **card_funding**: Card [funding
type](https://docs.stripe.com/api/external_account_cards/object#account_card_object-funding);
can be `credit`, `debit`, `prepaid`, or `unknown`
- **card_brand**: Card [brand](https://docs.stripe.com/api#card_object-brand);
can be `American Express`, `Diners Club`, `Discover`, `Eftpos Australia`, `JCB`,
`MasterCard`, `UnionPay`, `Visa`, or `Unknown`
- **card_network**: Identifies which
[network](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-network)
processed the transaction; examples include `amex`, `cartes_bancaires`,
`diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `mastercard`, `unionpay`,
`visa`, `unknown`
- **card_country**: Two-letter ISO code representing the country of the
transaction card
- **connected_account_country**: Two-letter ISO code representing the country of
the transaction account
- **charge_type**: Type of the charge: `destination` (always included) or
`direct` (included only for accounts that are connected at the time the report
is generated)

The Transaction margin report includes the following data for the selected time
period:

TypeCategoryDescriptionVolume amountAmount of the charge, excluding any
taxamount_refundedAmount of the charge that was refundedamount_disputedAmount of
the charge that was disputed by the customerRevenue application_fee_amountAmount
requested by the platform to be deducted from the charge
amountapplication_fee_amount_refundedApplication fee amount that was
refundedCost stripe_processing_fees_subtotal_amountFees charged by Stripe for
payments processing, such as fees for using payment methods like Affirm or
AfterPay; for users with IC+ pricing, does not include Stripe card payments fees
or network costsstripe_processing_fees_tax_amountTax on the fees charged by
Stripe for payments processingstripe_dispute_fees_subtotal_amountDispute fees
charged by Stripestripe_dispute_fees_tax_amountTax on the dispute fees charged
by Stripestripe_refund_fees_subtotal_amountStripe processing fees that were
refundedstripe_refund_fees_tax_amountTax on the Stripe processing fees that were
refundednetwork_costs_subtotal_amountInterchange (or discount, for Amex) fees
and transaction-level scheme fees; a single charge typically incurs one
interchange fee and one or more scheme feesnetwork_costs_tax_amountTax on the
transaction-level network costs charged to the
platformstripe_per_auth_fee_subtotal_amountPer-authorization fees charged by
Stripe for card processing with IC+ pricingstripe_per_auth_fee_tax_amountTax on
the per-authorization fees charged by Stripe for card processing with IC+
pricingstripe_volume_fee_subtotal_amountVolume fees charged by Stripe for card
processing with IC+ pricingstripe_volume_fee_tax_amountTax on the volume fees
charged by Stripe for card processing with IC+
pricingstripe_other_cardpayments_fees_subtotal_amountOther fees charged by
Stripe for card processing with IC+
pricingstripe_other_cardpayments_fees_tax_amountTax on the other fees charged by
Stripe for card processing with IC+
pricingstripe_radar_fees_subtotal_amountRadar fees charged to the
platformstripe_radar_fees_tax_amountTax on the Radar fees charged to the
platformstripe_adaptive_acceptance_fee_subtotal_amountAdaptive acceptance fees
charged to the platformstripe_adaptive_acceptance_fee_tax_amountTax on the
adaptive acceptance fees charged to the
platformstripe_connect_loss_liability_fee_subtotal_amountLoss liability fees
charged by Stripe to manage risk on the
transactionstripe_connect_loss_liability_fee_tax_amountTax on the loss liability
fees charged by Stripe to manage risk on the
transactionstripe_other_fees_subtotal_amountAll other fees charged on the
transaction that aren’t explicitly included in another
fieldstripe_other_fees_tax_amountTax charged on the other feescurrencyCurrency
of the charge and fees

## Links

- [pricing and
fees](https://docs.stripe.com/api/accounts/create#create_account-controller-fees-payer)
- [explicitly state an application
fee](https://docs.stripe.com/connect/destination-charges?fee-type=application-fee#collect-fees)
- [Platform Pricing
Tools](https://docs.stripe.com/connect/platform-pricing-tools)
-
[transfer_data.amount](https://docs.stripe.com/connect/destination-charges?fee-type=transfer-amount#collect-fees)
- [Connect Margin Report](https://dashboard.stripe.com/connect/margin)
- [Reports hub](https://dashboard.stripe.com/reports/hub)
- [user roles](https://docs.stripe.com/get-started/account/teams/roles)
- [Connect direct charges](https://docs.stripe.com/connect/direct-charges)
- [Destination charges](https://docs.stripe.com/connect/destination-charges)
- [Instant Payouts](https://docs.stripe.com/connect/instant-payouts)
- [cross-border payout](https://docs.stripe.com/connect/cross-border-payouts)
- [funding
type](https://docs.stripe.com/api/external_account_cards/object#account_card_object-funding)
- [brand](https://docs.stripe.com/api#card_object-brand)
-
[network](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-network)