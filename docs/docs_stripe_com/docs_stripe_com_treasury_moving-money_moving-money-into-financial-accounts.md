# Moving money into financial accounts

## Learn the requests available to move money into financial accounts.

You can add money to your financial account using `InboundTransfer` and
`ReceivedCredit` objects. In some scenarios, you can reverse `ReceivedCredits`,
which creates a [CreditReversal
object](https://docs.stripe.com/api/treasury/credit_reversals/object). For more
information, see the [Moving money with Treasury using CreditReversal objects
guide](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/credit-reversals).

Stripe Treasury also provides test mode objects to facilitate testing money
flows into financial accounts. The test mode endpoint for creating a
`ReceivedCredit`, for example, enables you to add money to your test mode
financial account balance to begin experimenting with other money movement
capabilities. The test mode endpoints for `InboundTransfers`, on the other hand,
enable you to test effects of your other business logic when an
`InboundTransfer` object transitions to a particular state.

## See also

- [Moving money with Treasury using InboundTransfer
objects](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/inbound-transfers)
- [Moving money with Treasury using ReceivedCredit
objects](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/received-credits)
- [Moving money with Treasury using CreditReversal
objects](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/credit-reversals)

## Links

- [CreditReversal
object](https://docs.stripe.com/api/treasury/credit_reversals/object)
- [Moving money with Treasury using CreditReversal objects
guide](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/credit-reversals)
- [Moving money with Treasury using InboundTransfer
objects](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/inbound-transfers)
- [Moving money with Treasury using ReceivedCredit
objects](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/received-credits)