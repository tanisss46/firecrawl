# Money movement timelines

## Learn about the timelines for various types of money movement in Treasury.

Stripe Treasury integrates with banking partners and payment networks, which
have varying processing and cutoff times.

## OutboundPayment and OutboundTransfer transactions

NetworkBehavior`ach``OutboundPayment` and `OutboundTransfer` requests processed
before the cutoff time are submitted to our banking partner on the same day.
These transfers are expected to arrive at the receiving bank within the next one
to two business days. Same-day ACH transactions arrive at the receiving bank the
same business day if the request is received before the cutoff
time.`us_domestic_wire``OutboundPayment` and `OutboundTransfer` requests
processed before the cutoff are expected to arrive at the receiving bank on the
same business day.`stripe``OutboundPayment` and `OutboundTransfer` requests
using the `stripe` network post immediately and arrive at the receiving
financial account within minutes, both during and outside of business hours.
### Evolve Bank & Trust

- `ach` cutoff:- Default Speed: 6pm central time (CST/CDT)
- Same Day speed: 11am central time (CST/CDT)
- `us_domestic_wire` cutoff: 3pm central time (CST/CDT)
Submission dateArrival date (by end of business
day)ACHWireMondayTuesdayMondayTuesdayWednesdayTuesdayWednesdayThursdayWednesdayThursdayFridayThursdayFridayMondayFridaySaturdayTuesdayMondaySundayTuesdayMonday
You can programmatically access the `expected_arrival_date` attribute on
[OutboundPayment](https://docs.stripe.com/api/treasury/outbound_payments/object#outbound_payment_object-expected_arrival_date)
or
[OutboundTransfer](https://docs.stripe.com/api/treasury/outbound_transfers/object#outbound_transfer_object-expected_arrival_date)
to reference when Stripe expects the funds to arrive at their destination.

Requests, including default speed requests, that are received after the cutoff
time are processed the following business day. Same-day ACH requests received
after the cutoff time arrive by the end of the following business day.

## InboundTransfer transactions

NetworkBehavior`ach``InboundTransfer` If using the default speed,
`InboundTransfer` requests processed before the cutoff time are submitted to our
banking partner on the same business day. Otherwise, they’re submitted on the
following business day. Transfers are expected to arrive in the Treasury
financial account on the morning of the fourth business day after submission to
the banking partner, if no returns are received during that time.
### Evolve Bank & Trust

Submission date, before 6pm central time (CST/CDT)Available at approximately
10am central time
(CST/CDT)MondayFridayTuesdayMondayWednesdayTuesdayThursdayWednesdayFridayThursdaySaturdayFridaySundayFriday
## ReceivedCredit and ReceivedDebit transactions

Credits and debits initiated from outside Stripe and received on a financial
account are processed as soon as Stripe receives notification of the transfer.
The time it takes to complete the transfer depends on the originating
institution.

NetworkBehavior`ach`Available same day or next business day, depending on
originating institution.`us_domestic_wire`Depends on originating institution.
Wires received by the federal wire network during a business day are typically
available in the Treasury financial account the morning of the following
business day.`stripe`Transfers using the `stripe` network post immediately and
are expected to arrive at the receiving financial account within
minutes.`card`Card transactions are typically captured within 24 hours of
authorization approval; however, some companies can capture funds up to 30 days
after authorization. See [Issuing
transactions](https://docs.stripe.com/issuing/purchases/transactions).
## Automatic payouts

All platforms using Treasury have access to standard automatic payouts, which
move money from Stripe Payments to a Treasury financial account on a T+2 or
slower schedule from the time of transaction (T+2 for card payments, slower for
ACH).

You can request a platform risk review to access faster payouts; upon approval,
your platform can use T+1 automatic payouts for connected accounts. T+1 faster
payout schedules apply to all payment types, including both card payments and
ACH payments, and the timelines start when the transaction occurs (faster
payouts eliminate the need to wait for standard payments fund settlement times).

To request access to faster payouts for your platform, email
[treasury-support@stripe.com](mailto:treasury-support@stripe.com).

For more details, see the [Automatic payouts
guide](https://docs.stripe.com/treasury/moving-money/payouts#automatic-payouts).

## Manual payouts

Platforms using Treasury also have access to standard manual payouts, which move
funds in one business day (T+1 schedule) but can only draw on an account’s
`available` payments balance. In other words, you must wait for funds from a
payment to settle in the payments balance before initiating a standard manual
payout to a Treasury financial account.

Platforms granted access to faster payouts also have access to instant manual
payouts. Instant manual payouts move funds to a connected account’s financial
account within an hour (T+0 schedule) and are available any time, including
nights, weekends, and holidays. Instant manual payouts are drawn on a connected
account’s `instant_available` balance rather than being limited to the
`available` balance.

For more details, see the [Manual payouts
guide](https://docs.stripe.com/treasury/moving-money/payouts#manual-payouts).

## Top-ups

Stripe [Connect](https://docs.stripe.com/connect) platform users can top up
their existing Stripe platform account balance using a Stripe Treasury financial
account by verifying the routing and account numbers. These funds settle to your
account balance according to [Top-ups settlement
timing](https://docs.stripe.com/connect/top-ups#settlement-timing).

For more details, see [Adding funds to your platform
balance](https://docs.stripe.com/connect/top-ups).

## Same-day ACH regulations

ACH transactions are regulated by
[Nacha](https://www.nacha.org/content/how-ach-rules-are-made). Consider the
following when using same-day ACH:

- Individual same-day ACH transactions [can’t exceed 1,000,000
USD](https://www.nacha.org/million). If you submit a larger single transaction
for same-day processing, Stripe remits the funds for processing on the following
day.
- The 1,000,000 USD limit applies only to single transactions. You can submit
multiple smaller transactions that total more than 1,000,000 USD for same-day
processing.

#### Note

ACH operators monitor for attempts to evade the limit, such as by splitting a
single large transaction into multiple smaller transactions. If they suspect an
evasion attempt, they process those transactions for next-day settlement in the
next available processing window.

## See also

- [Moving money out of financial
accounts](https://docs.stripe.com/treasury/moving-money/moving-money-out-of-financial-accounts)
- [Moving money into financial
accounts](https://docs.stripe.com/treasury/moving-money/moving-money-into-financial-accounts)
- [Payouts](https://docs.stripe.com/treasury/moving-money/payouts)

## Links

-
[OutboundPayment](https://docs.stripe.com/api/treasury/outbound_payments/object#outbound_payment_object-expected_arrival_date)
-
[OutboundTransfer](https://docs.stripe.com/api/treasury/outbound_transfers/object#outbound_transfer_object-expected_arrival_date)
- [Issuing transactions](https://docs.stripe.com/issuing/purchases/transactions)
- [Automatic payouts
guide](https://docs.stripe.com/treasury/moving-money/payouts#automatic-payouts)
- [Manual payouts
guide](https://docs.stripe.com/treasury/moving-money/payouts#manual-payouts)
- [Connect](https://docs.stripe.com/connect)
- [Top-ups settlement
timing](https://docs.stripe.com/connect/top-ups#settlement-timing)
- [Adding funds to your platform
balance](https://docs.stripe.com/connect/top-ups)
- [Nacha](https://www.nacha.org/content/how-ach-rules-are-made)
- [can’t exceed 1,000,000 USD](https://www.nacha.org/million)
- [Moving money out of financial
accounts](https://docs.stripe.com/treasury/moving-money/moving-money-out-of-financial-accounts)
- [Moving money into financial
accounts](https://docs.stripe.com/treasury/moving-money/moving-money-into-financial-accounts)
- [Payouts](https://docs.stripe.com/treasury/moving-money/payouts)