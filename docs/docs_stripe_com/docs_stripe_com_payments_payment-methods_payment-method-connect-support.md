# Payment method support for platforms and marketplaces

## Learn about requirements and limitations when enabling payment methods for platforms and marketplaces.

When using [Connect](https://docs.stripe.com/connect) for platforms and
marketplaces, different payment methods are available depending on factors such
as country location, business type, account type, and charge type. Select a
payment method to learn about its level of Connect support.

For more information about enabling payment methods with Connect, refer to the
following:

- [Account
capabilities](https://docs.stripe.com/connect/account-capabilities#payment-methods)
- [Adding payment method
capabilities](https://docs.stripe.com/connect/payment-methods)
- [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)

## Payment methods

Payment method:ACH Direct DebitAffirmAfterpay / ClearpayAlipayAlmaBank
transfersBillieBLIKCapchase PayCash App PayIndonesian bank
transfersKlarnaKriyaMB WayMexican installmentsMobilePayMonduMultibancoPay by
BankPayPalPayToScalapaySeQursSunbitSepa Direct DebitSwishTWINTWechat Pay
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
cloning](https://docs.stripe.com/payments/payment-methods/payment-method-connect-support#payment-method-and-mandate-cloning).

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

## Links

- [Connect](https://docs.stripe.com/connect)
- [Account
capabilities](https://docs.stripe.com/connect/account-capabilities#payment-methods)
- [Adding payment method
capabilities](https://docs.stripe.com/connect/payment-methods)
- [Payment method
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
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