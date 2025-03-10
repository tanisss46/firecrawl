# Alipay payments

## Learn about Alipay, a digital wallet popular with customers from China.

Alipay is a digital wallet in China that has more than a billion active users
worldwide.

Alipay users can pay on the web or on a mobile device using login credentials or
their Alipay app. Alipay has a low dispute rate and reduces fraud by
authenticating payments using the customer’s login credentials.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Chinese consumers, overseas Chinese, and Chinese travelers
- **Presentment currency**

CNY, AUD, CAD, EUR, GBP, HKD, JPY, SGD, MYR, NZD, USD (depending on business
locations)
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Wallets
- **Recurring payments**

[Requires approval](https://support.stripe.com/contact)
- **Payout timing**

Standard payout timing applies
- **Connect support**

Partial (request an invite to create charges [on behalf
of](https://docs.stripe.com/connect/charges#on_behalf_of) other accounts)
- **Dispute support**

[No](https://docs.stripe.com/payments/alipay#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/alipay#refunds)

## Prohibited business categories

Both Stripe and Alipay maintain a list of prohibited businesses that aren’t
allowed to use their services. To use Alipay on Stripe, your business can’t be
[restricted from using Stripe](https://stripe.com/restricted-businesses) or
appear on Alipay’s [prohibited business list](https://stripe.com/legal/alipay).
If you’re not sure if your business is a prohibited business, or have questions
about how these requirements apply to you, please [contact
support](https://support.stripe.com/contact/login).

For more information about Alipay eligibility for your account, navigate to your
[Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

## Get started

You don’t have to integrate Alipay and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Alipay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

[Payment Links](https://docs.stripe.com/payment-links) also supports adding
Alipay from the Dashboard.

If you prefer to manually list payment methods, learn how to [manually configure
Alipay as a payment](https://docs.stripe.com/payments/alipay/accept-a-payment).

## Disputes

Alipay payments have a low risk of fraud or unrecognized payments because the
customer must authenticate the payment, so no dispute process exists that could
create chargebacks and withdraw funds from your Stripe account. If an Alipay
user contacts them about a problem with a transaction, they might direct that
user to you for a resolution.

## Refunds

You can refund Alipay payments up to 90 days after the original payment. Refunds
for Alipay payments are asynchronous and take up to 5 minutes to complete.
Stripe notifies you of the final refund status using the `refund.updated` or
`refund.failed` [webhook](https://docs.stripe.com/webhooks) event. When a refund
succeeds, the status of the [Refund](https://docs.stripe.com/api/refunds/object)
object transitions to `succeeded`. If a refund fails, the status of the Refund
object transitions to `failed` and Stripe returns the amount to your Stripe
balance. You then need to arrange an alternative way of providing your customer
with a refund.

## Supported currencies

You can create Alipay payments in the currencies that map to your country. The
default local currency for Alipay is `cny` and customers also see their purchase
amount in `cny`.

CurrencyCountry`cny`Any country`aud`Australia`cad`Canada`eur`Austria, Belgium,
Bulgaria, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany,
Greece, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands,
Norway, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden,
Switzerland`gbp`United Kingdom`hkd`Hong Kong`jpy`Japan`myr`Malaysia`nzd`New
Zealand`sgd`Singapore`usd`United States
If you have a bank account in another currency and would like to create an
Alipay payment in that currency, you can [contact
support](https://support.stripe.com/email). Support for additional currencies is
provided on a case-by-case basis.

## Connect

Alipay has partial [Connect](https://stripe.com/connect) support depending on
the [charge type](https://docs.stripe.com/connect/charges).

Destination chargesSeparate charges and transfersDirect charges`on_behalf_of`
For connected accounts with standard Dashboard access, individual connected
accounts can enable Alipay in the Dashboard.

For connected accounts without standard Dashboard access, the platform needs to
request the `alipay_payments` capability. This is a private preview feature;
contact Stripe Support to request access.

## Links

- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [Requires approval](https://support.stripe.com/contact)
- [on behalf of](https://docs.stripe.com/connect/charges#on_behalf_of)
- [No](https://docs.stripe.com/payments/alipay#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/alipay#refunds)
- [restricted from using Stripe](https://stripe.com/restricted-businesses)
- [prohibited business list](https://stripe.com/legal/alipay)
- [contact support](https://support.stripe.com/contact/login)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure Alipay as a
payment](https://docs.stripe.com/payments/alipay/accept-a-payment)
- [webhook](https://docs.stripe.com/webhooks)
- [Refund](https://docs.stripe.com/api/refunds/object)
- [contact support](https://support.stripe.com/email)
- [Connect](https://stripe.com/connect)
- [charge type](https://docs.stripe.com/connect/charges)