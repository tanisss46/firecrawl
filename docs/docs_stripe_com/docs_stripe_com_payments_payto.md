# PayTo paymentsInvite only

## Learn about PayTo, a real-time payment method in Australia.

PayTo is a real-time payment method in Australia for accepting one-time and
recurring payments. When paying with PayTo, customers [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
agreements using their mobile banking app.

You get [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
on whether the payment succeeded or failed. Stripe typically sends a
notification of the final status of the payment within 30 seconds of the
agreement authorization.

Payment method propertiesCountry availability- **Customer locations**

Australia
- **Presentment currency**

AUD
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Real-time payments
- **Recurring payments**

Yes
- **Payout timing**

[Standard payout timing](https://docs.stripe.com/payouts#payout-speed) applies
- **Connect support**

Yes
- **Dispute support**

No
- **Manual capture support**

No
- **Refunds and partial refunds**

Yes, yes

## Interested in getting early access to PayTo?

To learn more or get early access, enter your email address below. We’ll work
with you to determine your eligibility, and from there, add you to the waitlist.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Payment flows

Customers pay with PayTo by using one of the following methods:

- **PayID**: Customers can provide a PayID, a unique identifier linked to a
customer’s bank account, to initiate agreement authorization.
- **Account and BSB Numbers**: Customers can provide their bank account details
to initiate agreement authorization.

In both cases, customers receive a request from their bank to authorize the
PayTo agreement. This request typically surfaces through a push notification or
by email.

## Get started

PayTo is only available on the [Payment
Element](https://docs.stripe.com/payments/payto/accept-a-payment?ui=elements) or
through a [direct API
integration](https://docs.stripe.com/payments/payto/accept-a-payment?ui=direct-api).
It isn’t available in any other Stripe-hosted UIs. PayTo is available as a
[Dynamic payment
method](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods),
which means you don’t have to individually integrate PayTo and other payment
methods. If you use the Payment Element, Stripe automatically determines the
most relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
PayTo.

If you prefer to manually list payment methods, learn how to [manually
configure](https://docs.stripe.com/payments/payto/accept-a-payment) PayTo as a
payment.

## Refunds

Refund PayTo payments by calling the [Stripe Refunds
API](https://docs.stripe.com/api/refunds) or using the Dashboard. You can refund
a PayTo payment up to 2 years after the original payment. Customers typically
receive refunds in their bank accounts within 2 days, but some banks might take
up to 10 days to process a PayTo refund.

PayTo supports full and partial refunds. You can also issue multiple partial
refunds up to the amount of the original charge.

For PayTo payments made using PayID, Stripe sends an email to the customer to
collect their bank account details before processing the refund.

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
with PayTo to process payments on behalf of a connected account. Connect users
can use PayTo with the following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)

### Enable PayTo for connected accounts that use the Stripe Dashboard

Reach out to your Stripe representative to enable PayTo for connected accounts
that use the Stripe Dashboard or [email us](mailto:payto-support@stripe.com).
These connect accounts must onboard manually.

### Enable PayTo for connected accounts that use the Express Dashboard or a dashboard that isn’t hosted by Stripe

To onboard connected accounts that use the Express Dashboard or a dashboard that
isn’t hosted by Stripe, request the `payto_payments` capability using the
[Capabilities API](https://docs.stripe.com/api/capabilities). For more details,
follow the instructions to [enable payment methods for your connected
accounts](https://docs.stripe.com/connect/account-capabilities).

## Transaction limits and other considerations

Across the banks, PayTo performs best for recurring transactions, and
transactions below 1,000 AUD. PayTo performance might vary depending on the
buyer’s bank, their account type, and the frequency of payments. Each bank can
enforce additional measures to manage risk and prevent fraud.

See the documentation linked below for more details on bank-specific
considerations.

Bank nameAdditional notes[ANZ (Australia and New Zealand Banking
Group)](https://www.anz.com.au/personal/ways-to-bank/more/pay-to)Payments over
25,000 AUD are not accepted by ANZ.[CBA (Commonwealth Bank of
Australia)](https://www.commbank.com.au/digital-banking/pay-to.html)[NAB
(National Australia
Bank)](https://www.nab.com.au/personal/online-banking/digital-payments/payto)[Westpac](https://www.westpac.com.au/personal-banking/mobile-wallets/payto)Payments
over 25,000 AUD are not accepted by Westpac. Ad-hoc payments for amounts over
1,000 AUD are also declined. Recurring payments with no maximum amount might be
declined.[Australian Mutual
Bank](https://australianmutual.bank/banking/access/payto)[Australian Unity
Bank](https://www.australianunity.com.au/banking/payto)[Bank Australia
Limited](https://www.bankaust.com.au/payto)[BankWaW](https://www.bankwaw.com.au/Support/Ways-To-Bank/PayTo)[Bendigo
and Adelaide Bank
Limited](https://www.bendigobank.com.au/ways-to-bank/payto)[Beyond Bank
Australia
Limited](https://www.beyondbank.com.au/banking/bank-with-us/payto.html)[Community
First Bank](https://communityfirst.com.au/support/payto)[Credit Union
SA](https://www.creditunionsa.com.au/digital-banking/real-time-payments/payto)[Defence
Bank Limited](https://www.defencebank.com.au/tools-and-advice/payto/)[First
Option Bank](https://firstoptionbank.com.au/payto-tcs/)[Goulburn Murray Credit
Union](https://www.gmcu.com.au/pages/22-pages/2-products-a-services/280-payto)[Great
Southern
Bank](https://www.greatsouthernbank.com.au/digital-banking/payto)[Macquarie Bank
Limited](https://www.macquarie.com.au/help/personal/payments-transfers-and-deposits/payto/whats-payto-and-how-does-it-work.html)[P&N
Bank (Police & Nurses
Bank)](https://www.pnbank.com.au/help-and-support/payments/what-is-a-payto-agreement)[People’s
Choice Credit
Union](https://www.peopleschoice.com.au/help-and-support/faqs/fast-payments/what-is-payto-and-how-can-it-be-used)[Queensland
Country Bank
Limited](https://www.queenslandcountry.bank/help-info/faqs/payto)[RACQ
Bank](https://www.racq.com.au/banking/online-banking/payto)[Regional Australia
Bank](https://www.regionalaustraliabank.com.au/the-inside-story/articles/introducing-payto)[St.
George](https://www.stgeorge.com.au/online-services/ways-to-pay/payto)[Suncorp
Australia](https://www.suncorpbank.com.au/help-support/ways-to-bank/payto.html)[Teachers
Mutual Bank
Limited](https://www.tmbank.com.au/ways-to-bank/npp-payto/introducing-payto)[The
Mac Credit
Union](https://themaccu.com.au/support/faqs/payto-faqs)[Ubank](https://www.ubank.com.au/help/current/app-and-online-banking/payto)[Unity
Bank](https://www.unitybank.com.au/help/access-options/osko-payments)

## Links

- [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Standard payout timing](https://docs.stripe.com/payouts#payout-speed)
- [privacy policy](https://stripe.com/privacy)
- [Payment
Element](https://docs.stripe.com/payments/payto/accept-a-payment?ui=elements)
- [direct API
integration](https://docs.stripe.com/payments/payto/accept-a-payment?ui=direct-api)
- [Dynamic payment
method](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [manually configure](https://docs.stripe.com/payments/payto/accept-a-payment)
- [Stripe Refunds API](https://docs.stripe.com/api/refunds)
- [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Capabilities API](https://docs.stripe.com/api/capabilities)
- [enable payment methods for your connected
accounts](https://docs.stripe.com/connect/account-capabilities)
- [ANZ (Australia and New Zealand Banking
Group)](https://www.anz.com.au/personal/ways-to-bank/more/pay-to)
- [CBA (Commonwealth Bank of
Australia)](https://www.commbank.com.au/digital-banking/pay-to.html)
- [NAB (National Australia
Bank)](https://www.nab.com.au/personal/online-banking/digital-payments/payto)
- [Westpac](https://www.westpac.com.au/personal-banking/mobile-wallets/payto)
- [Australian Mutual Bank](https://australianmutual.bank/banking/access/payto)
- [Australian Unity Bank](https://www.australianunity.com.au/banking/payto)
- [Bank Australia Limited](https://www.bankaust.com.au/payto)
- [BankWaW](https://www.bankwaw.com.au/Support/Ways-To-Bank/PayTo)
- [Bendigo and Adelaide Bank
Limited](https://www.bendigobank.com.au/ways-to-bank/payto)
- [Beyond Bank Australia
Limited](https://www.beyondbank.com.au/banking/bank-with-us/payto.html)
- [Community First Bank](https://communityfirst.com.au/support/payto)
- [Credit Union
SA](https://www.creditunionsa.com.au/digital-banking/real-time-payments/payto)
- [Defence Bank Limited](https://www.defencebank.com.au/tools-and-advice/payto/)
- [First Option Bank](https://firstoptionbank.com.au/payto-tcs/)
- [Goulburn Murray Credit
Union](https://www.gmcu.com.au/pages/22-pages/2-products-a-services/280-payto)
- [Great Southern
Bank](https://www.greatsouthernbank.com.au/digital-banking/payto)
- [Macquarie Bank
Limited](https://www.macquarie.com.au/help/personal/payments-transfers-and-deposits/payto/whats-payto-and-how-does-it-work.html)
- [P&N Bank (Police & Nurses
Bank)](https://www.pnbank.com.au/help-and-support/payments/what-is-a-payto-agreement)
- [People’s Choice Credit
Union](https://www.peopleschoice.com.au/help-and-support/faqs/fast-payments/what-is-payto-and-how-can-it-be-used)
- [Queensland Country Bank
Limited](https://www.queenslandcountry.bank/help-info/faqs/payto)
- [RACQ Bank](https://www.racq.com.au/banking/online-banking/payto)
- [Regional Australia
Bank](https://www.regionalaustraliabank.com.au/the-inside-story/articles/introducing-payto)
- [St. George](https://www.stgeorge.com.au/online-services/ways-to-pay/payto)
- [Suncorp
Australia](https://www.suncorpbank.com.au/help-support/ways-to-bank/payto.html)
- [Teachers Mutual Bank
Limited](https://www.tmbank.com.au/ways-to-bank/npp-payto/introducing-payto)
- [The Mac Credit Union](https://themaccu.com.au/support/faqs/payto-faqs)
- [Ubank](https://www.ubank.com.au/help/current/app-and-online-banking/payto)
- [Unity Bank](https://www.unitybank.com.au/help/access-options/osko-payments)