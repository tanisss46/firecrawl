# MobilePay payments

## Learn about MobilePay, a popular payment method in Denmark and Finland.

MobilePay is a
[single-use](https://docs.stripe.com/payments/payment-methods#usage) card wallet
payment method used in Denmark and Finland. It allows your customer to
[authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
payments using the MobilePay app.

When your customer pays with MobilePay, Stripe performs a card transaction using
the card data we receive from MobilePay. The processing of the card transaction
is invisible to your integration, and Stripe [immediately notifies
you](https://docs.stripe.com/payments/payment-methods#payment-notification)
whether the payment succeeded or failed.

Payment method propertiesCountry availability- **Customer locations**

Denmark and Finland
- **Presentment currency**

DKK, EUR, NOK, SEK
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Digital wallet
- **Recurring payments**

No
- **Payout timing**

[Standard payout timing](https://docs.stripe.com/payouts#payout-speed) applies
- **Connect support**

Yes
- **Dispute support**

Yes
- **Manual capture support**

Yes
- **Refunds / Partial refunds**

Yes / yes

## Payment flows

Customers pay with MobilePay by using one of the following methods:

MobileDesktop
Customers follow a mobile redirect from your website or mobile app to the
MobilePay app where they authorize the payment, then return to your website or
mobile app.

## Get started

You don’t have to integrate MobilePay and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
MobilePay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add MobilePay from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links)

You can also [manually configure MobilePay as a payment
method](https://docs.stripe.com/payments/mobilepay/accept-a-payment).

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
with MobilePay to process payments. Connect users can use MobilePay with the
following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)

### Enable MobilePay for connected accounts

Connected accounts with access to the full Stripe Dashboard can enable MobilePay
in their [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). To check which
accounts have enabled MobilePay, use the `capabilities` hash in our [accounts
webhooks or
APIs](https://docs.stripe.com/api/accounts/object#account_object-capabilities-mobilepay_payments)
to see if the `mobilepay_payments` capability is set to `active`.

For connected accounts that don’t have access to the full Stripe Dashboard, see
[enable payment methods for your connected
accounts](https://docs.stripe.com/connect/account-capabilities). The name of the
connected account is the name customers see during checkout and in the MobilePay
app.

## Refunds

MobilePay supports full and partial refunds. You can also issue multiple partial
refunds up to the amount of the original charge.

## Disputes

MobilePay allows transaction disputes. Customers can open disputes directly with
their cards issuer for cases of suspected fraud, double payments, or a
difference between an order and a transaction amount. You can submit evidence to
contest a dispute directly. The dispute process is the same as that for card
payments. Learn how to [manage
disputes](https://docs.stripe.com/disputes/responding).

## Card transaction retries

MobilePay allows customers to retry payments in-app before marking a payment as
failed and redirecting to your website. When a card transaction fails, the
customer can retry a payment using a different card, which might result in a
successful payment.

## 3D Secure authentication

Certain cards or banks might require an additional card authentication step to
process the MobilePay transaction.

When this occurs, the customer is presented with a WebView dialog in the
MobilePay application, prompting them to authorize the payment. The need to
perform a [3D Secure challenge](https://docs.stripe.com/payments/3d-secure) is
invisible to your integration and there are no extra integration steps for you
to handle.

The expected impact varies, depending on customer country and card network:

CountryCard brandPayments requiring 3DS
step-upDenmarkVisa~1%DenmarkMastercard~1.5%FinlandVisa~5%FinlandMastercard~7
### Liability shift

[Liability
shift](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
doesn’t apply to MobilePay payments unless [3D Secure
authentication](https://docs.stripe.com/payments/3d-secure) has taken place.
MobilePay doesn’t allow you the option to enforce 3D Secure authentication on
the underlying card payment.

## Prohibited business categories

In addition to the categories of [businesses restricted from using
Stripe](https://stripe.com/restricted-businesses), the following categories are
specifically prohibited from using MobilePay:

- Cryptocurrencies
- Stock trade
- Gambling
- Betting
- Bonds
- Money transfers
- Debt collection
- Multi-level marketing and pyramid schemes

For more information about MobilePay eligibility for your account, review your
[Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) in the
Dashboard.

## Current limitations

### Account icons

The MobilePay transaction confirmation page displays the default Stripe account
icon instead of a configurable custom logo. Stripe will notify you when feature
improvements become available so you can update your account configuration as
needed.

![A screenshot of a successful MobilePay
payment.](https://b.stripecdn.com/docs-statics-srv/assets/mobilepay-no-merchant-logo.f6f41b7fecbbd48cfabcbff85521ec6d.png)

An example confirmation page for a successful MobilePay payment.

### Manual captures

At this time, MobilePay only supports automatic captures and [manual captures of
the full
amount](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method).
Stripe will notify you as feature improvements become available for manual
captures of partial amounts.

### Dankort support

Stripe currently doesn’t have support for the Dankort card network. If a
customer chooses to pay with a Dankort-branded card, Stripe processes the
payment on the Visa and Mastercard networks instead.

## Fees

Stripe receives card data from MobilePay to process card transactions using
Stripe’s Visa and Mastercard integrations. Because MobilePay payments are card
transactions, you incur the following fees for each successful transaction:

- Stripe processing fees associated with the card transaction
- Applicable taxes
- MobilePay transaction processing fee
- An additional monthly membership fee (applicable only to businesses registered
in Denmark)

The MobilePay transaction fee isn’t subtracted immediately from the transaction.
Instead, Stripe bills them once a day.

### Stripe processing fees and taxes

After a successful transaction, Stripe automatically deducts the Stripe
transaction fees and applicable taxes from the original transaction amount and
provides the remaining amount on your Stripe balance. These fees are identical
to a standard card transaction.

MobilePay is subject to the [standard payout schedule applicable to your
country](https://docs.stripe.com/payouts).

### MobilePay processing fee

The MobilePay processing fee isn’t presented within the net amount of a
successful transaction. Instead, Stripe bills the MobilePay processing fee once
a day, at which point we automatically deduct the sum that you owe from your
[Stripe balance](https://dashboard.stripe.com/balance).

### MobilePay monthly processing fee

MobilePay charges a fixed 35 DKK monthly membership fee to all businesses
registered in Denmark that use its services. Stripe bills this fee once a month
(if applicable), at which point we automatically deduct the sum that you owe
from your [Stripe balance](https://dashboard.stripe.com/balance).

The incurred MobilePay fees are listed as a separate entry on your monthly tax
invoice. You can find your monthly invoices in the
[Dashboard](https://dashboard.stripe.com/settings/documents).

## Links

- [single-use](https://docs.stripe.com/payments/payment-methods#usage)
- [authenticate and
approve](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediately notifies
you](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [Standard payout timing](https://docs.stripe.com/payouts#payout-speed)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure MobilePay as a payment
method](https://docs.stripe.com/payments/mobilepay/accept-a-payment)
- [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [accounts webhooks or
APIs](https://docs.stripe.com/api/accounts/object#account_object-capabilities-mobilepay_payments)
- [enable payment methods for your connected
accounts](https://docs.stripe.com/connect/account-capabilities)
- [manage disputes](https://docs.stripe.com/disputes/responding)
- [3D Secure challenge](https://docs.stripe.com/payments/3d-secure)
- [Liability
shift](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
- [businesses restricted from using
Stripe](https://stripe.com/restricted-businesses)
- [manual captures of the full
amount](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [standard payout schedule applicable to your
country](https://docs.stripe.com/payouts)
- [Stripe balance](https://dashboard.stripe.com/balance)
- [Dashboard](https://dashboard.stripe.com/settings/documents)