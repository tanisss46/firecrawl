# South Korean payment methods

## Accept wallets and all local cards in South Korea without a local entity.

You can localize your customer experience and accept payments from the majority
of payment methods available in South Korea without a local South Korean entity
by using Stripe and our local processor partner.

Card usage is popular in South Korea, with many different card issuers but not a
single predominant brand. Customers typically pay by selecting their card issuer
and authenticating through their card or bank’s app rather than manually
entering their card details. Wallets are also becoming more popular in South
Korea. To provide a familiar experience to customers and increase conversion
rates, offer a selection of local wallets and cards.

## Payment flow

Customers who pay with a local card are redirected to the local processor to
select their issuer. In this demo, the customer is paying with their Shinhan
card.

After the customer enters their information in Stripe’s checkout page and clicks
**Pay**, they’re redirected to the checkout page of the payment method provider
or local processor to complete the payment.

## Available payment methods

You can accept popular local wallets and all local cards.

Popular local wallets include:

- [Naver Pay](https://pay.naver.com/)
- [Kakao Pay](https://www.kakaopay.com/)
- [Samsung Pay](https://www.samsung.com/us/apps/samsung-wallet/)
- [PAYCO](https://www.payco.com/)

All locally issued cards are supported, including:

- [Shinhan Card](https://www.shinhancard.com/)
- [Hyundai Card](https://www.hyundaicard.com/)
- [Samsung
Card](https://www.samsungcard.com/company/english/main/UHPPCI0245M0.jsp)

#### Caution

Make sure that in providing goods and services to South Korean customers, your
business complies with South Korean legal and tax requirements. Use Stripe Tax
to [collect tax in South
Korea](https://docs.stripe.com/tax/supported-countries/asia-pacific/south-korea).

Payment method propertiesCountry availability- **Customer locations**

South Korea
- **Presentment currency**

KRW
- **Payment confirmation**

Customer-authenticated
- **Payment method family**

Countries
- **Recurring payments**

Yes
- **Payout timing**

[T + 4 availability](https://docs.stripe.com/payouts#payout-speed)
- **Connect support**

Yes
- **Dispute support**

Yes
- **Manual capture support**

Yes
- **Refunds / Partial refunds**

Yes / Yes

## Get started

You don’t have to integrate South Korean payment methods and other payment
methods individually. If you use our front-end products, Stripe automatically
determines the most relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
South Korean payment methods. To get started with one of our hosted UIs, follow
a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add South Korean payment methods from
the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

### Integrate through the API

You can also use the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents) to accept payments from
South Korean customers using local cards and local payment methods. Follow our
guide to [test your integration’s redirect-handling logic by simulating a
payment that uses a redirect
flow](https://docs.stripe.com/testing?testing-method=payment-methods#redirects).

## Payment process

Customers who elect to pay with South Korean cards or payment methods are
redirected to the local processor or underlying payment method provider’s
checkout page as applicable, where they [authorize the
transaction](https://docs.stripe.com/payments/payment-methods#customer-actions).
After the payment is approved, funds are available in your Stripe account after
4 days.

## Payment methods

We currently support all local South Korean cards and the majority of South
Korean payment methods.

One-timeRecurring[All local
cards](https://docs.stripe.com/payments/kr-card/accept-a-payment)YesYes[Kakao
Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment)YesYes[Naver
Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment)YesYes[Samsung
Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment)[PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment)
## Installments

Local card issuers in South Korea can offer installments on purchases 50,000 KRW
and above. This lets customers pay for their purchase over time, for example, to
complete the payment over 3 months. Installments are popular with customers who
want to purchase goods with higher order values.

Installments are solely between customers and their card issuers. As a business,
you receive the full amount for your purchase up front, and your customer is
responsible for completing the installment payments to the issuer. In the event
that your customer is unable to complete their installments to their issuer, you
keep the funds.

## Refunds

Payments made with South Korean payment methods can only be submitted for refund
within 365 calendar days from the date of the original charge. After 365 days,
it’s no longer possible to refund the charge.

## Disputes

Local cards and payment methods in South Korea enforce strong authentication,
which helps reduce the risk of fraud or unrecognized payments. Customers have up
to 365 calendar days from the date of purchase to file a dispute. Stripe might
request you to provide information and documentation in cases of customer
disputes. After a customer files a dispute, you have up to 5 days to submit
evidence upon notification. Make sure you comply promptly with these requests.
Dispute decisions are made within 7 days of evidence submission. When using
South Korean payment methods, you must make a reasonable effort to detect fraud
or unauthorized transactions, and to minimize disputes.

## Links

- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [Naver Pay](https://pay.naver.com/)
- [Kakao Pay](https://www.kakaopay.com/)
- [Samsung Pay](https://www.samsung.com/us/apps/samsung-wallet/)
- [PAYCO](https://www.payco.com/)
- [Shinhan Card](https://www.shinhancard.com/)
- [Hyundai Card](https://www.hyundaicard.com/)
- [Samsung
Card](https://www.samsungcard.com/company/english/main/UHPPCI0245M0.jsp)
- [collect tax in South
Korea](https://docs.stripe.com/tax/supported-countries/asia-pacific/south-korea)
- [T + 4 availability](https://docs.stripe.com/payouts#payout-speed)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [test your integration’s redirect-handling logic by simulating a payment that
uses a redirect
flow](https://docs.stripe.com/testing?testing-method=payment-methods#redirects)
- [authorize the
transaction](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [All local cards](https://docs.stripe.com/payments/kr-card/accept-a-payment)
- [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment)
- [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment)
- [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment)
- [PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment)