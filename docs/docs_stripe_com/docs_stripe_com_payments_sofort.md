# Sofort payments

## Learn about Sofort, a common payment method in Europe.

#### Warning

New businesses can’t accept SOFORT payments and our financial partners are in
the process of discontinuing SOFORT. For more information, read our [support
page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method).

Stripe users in Europe and the United States can use the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents)—a single integration path
for creating payments using any supported method—to accept
[Sofort](https://www.sofort.com/) payments from customers in the following
countries:

- Austria
- Belgium
- Germany
- Netherlands
- Spain

Sofort is a [single
use](https://docs.stripe.com/payments/payment-methods#usage), [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method that requires customers to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. It redirects them to their bank’s portal to authenticate the
payment, and it typically takes 2 to 14 days to receive notification of success
or failure.

#### Caution

Your use of Sofort must comply with our [Sofort Terms of
Service](https://stripe.com/sofort/legal).

Payment method propertiesCountry availability- **Customer locations**

Europe
- **Presentment currency**

EUR
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Bank debit
- **Recurring payments**

via SEPA Direct Debit
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

No
- **Manual capture support**

No
- **Refunds / Partial refunds**

Yes / yes

## Payment flow

Below is a demonstration of the Sofort payment flow from your checkout page:

## Get started

You don’t have to integrate Sofort and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Sofort. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Sofort from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)

If you prefer to manually list payment methods or want to save Sofort details
for future payments, see the following guides:

- [Manually configure Sofort as a
payment](https://docs.stripe.com/payments/sofort/accept-a-payment)
- [Save Sofort details for future
payments](https://docs.stripe.com/payments/sofort/set-up-payment)

## Disputes

The risk of fraud or unrecognized payments is low because the customer must
authenticate the payment with their bank. As a result, you won’t have disputes
that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

Sofort payments can be refunded up to 180 days after the original payment.

## Links

- [support
page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Sofort](https://www.sofort.com/)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
- [delayed
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Sofort Terms of Service](https://stripe.com/sofort/legal)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Manually configure Sofort as a
payment](https://docs.stripe.com/payments/sofort/accept-a-payment)
- [Save Sofort details for future
payments](https://docs.stripe.com/payments/sofort/set-up-payment)