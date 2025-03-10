# ACH Standard Entry Class (SEC) handling

## Learn how SEC codes are determined for ACH transfers.

Each ACH transaction has an associated Standard Entry Class (SEC) code that
describes the accounts involved and how the transaction was authorized.

Stripe Treasury determines the SEC code based on whether the account receiving
the ACH entry is owned by a company or an individual. You specify the account
holder type in
[destination_payment_method_data.us_bank_account.account_holder_type](https://docs.stripe.com/api/treasury/outbound_payments/create#create_outbound_payment-destination_payment_method_data-us_bank_account-account_holder_type)
when:

- You make
[OutboundPayments](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments)
- You set up a [stored
PaymentMethod](https://docs.stripe.com/treasury/moving-money/working-with-bankaccount-objects#setupintents)

Only send
[InboundTransfers](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/inbound-transfers)
and
[OutboundTransfers](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-transfers)
to accounts owned by the FinancialAccount owner and with a `company` owner type.

SEC codes are determined based on the receiving account’s owner type as follows:

Money movementOwner typeSEC
codeInboundTransfer`company``CCD`OutboundTransfer`company``CCD`OutboundPayment`company``CCD`OutboundPayment`individual``PPD`

## Links

-
[destination_payment_method_data.us_bank_account.account_holder_type](https://docs.stripe.com/api/treasury/outbound_payments/create#create_outbound_payment-destination_payment_method_data-us_bank_account-account_holder_type)
-
[OutboundPayments](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-payments)
- [stored
PaymentMethod](https://docs.stripe.com/treasury/moving-money/working-with-bankaccount-objects#setupintents)
-
[InboundTransfers](https://docs.stripe.com/treasury/moving-money/financial-accounts/into/inbound-transfers)
-
[OutboundTransfers](https://docs.stripe.com/treasury/moving-money/financial-accounts/out-of/outbound-transfers)