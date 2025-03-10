# Mexico bank transfers

## Learn about Mexico bank transfers and its supported features.

#### Caution

[Learn
more](https://support.stripe.com/questions/mexico-bank-transfers-citi-migration-context-and-faqs)
about the Citibank changes and how this impacts Mexico bank transfers.

Bank transfers are a popular way to pay in Mexico. For merchants, bank transfers
help reduce customer decline rates, fraud, and chargebacks, and have lower fees
than credit cards. For customers in Mexico that have access to bank transfers in
their banking apps, it’s a convenient way to pay.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Mexico
- **Presentment currency**

MXN
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Bank transfers
- **Recurring payments**

Yes
- **Connect support**

Yes
- **Dispute support**

No
- **Manual capture support**

No
- **Refunds / Partial refunds**

Yes / Yes

## Target user segments

In particular, the Stripe bank transfer product serves users that process high
average order volume (AOV) and low-frequency payments. This includes B2C
Marketplaces with high AOV, B2B SaaS businesses, and fintech businesses.

## Product features

Citibanamex (the local Mexico unit of Citigroup, Inc.) processes payments for
the Stripe bank transfer product. Citibanamex is a member of the SPEI network
and provides the necessary basic capabilities for processing bank transfer
payments.

Our product offers automatic reconciliation and management of partial payments
and over payments, in addition to refunds. The bank transfer product is for
users who want low-code and no-code solutions in Mexico, and it allows them to
manage bank transfer payments through solutions such as
[invoices](https://docs.stripe.com/api/invoices) created in the Dashboard.

Our bank transfer product also offers successful payment confirmation
notifications. Stripe provides a message, (either in an API response or in the
Dashboard), indicating that a specific payment intent has been paid. On business
days, we expect to provide successful payment confirmation of most payments
within 30 minutes of the transfer. On non-business days, such as weekends or
bank holidays, we provide payment confirmation for most payments on the next
business day. For certain payments, you might experience delays of up to several
days, and delays because of of online system maintenance.

As soon as Stripe receives the successful payment confirmation from Citibanamex
(based on the timing described above), the Dashboard updates to show the credit
or completed payment. Funds can get paid out to the user’s bank account as soon
as 3 days after Citibanamex has confirmed the bank transfer.

#### Note

Due to reporting limitations, our product doesn’t offer immediate payment
confirmation notifications or settlements. As a result, our product is better
suited for businesses that process high AOV, low-frequency payments, such as B2B
businesses rather than consumer retail businesses.

## Get started

Get started with [accepting bank transfer
payments](https://docs.stripe.com/payments/bank-transfers/accept-a-payment) or
learn more about the [customer
balance](https://docs.stripe.com/payments/customer-balance).

## Links

- [Learn
more](https://support.stripe.com/questions/mexico-bank-transfers-citi-migration-context-and-faqs)
- [invoices](https://docs.stripe.com/api/invoices)
- [accepting bank transfer
payments](https://docs.stripe.com/payments/bank-transfers/accept-a-payment)
- [customer balance](https://docs.stripe.com/payments/customer-balance)