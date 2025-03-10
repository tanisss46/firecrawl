# Przelewy24 payments

## Learn about Przelewy24, a common payment method in Poland.

Przelewy24 is a Poland-based payment method aggregator that allows customers to
complete transactions online using bank transfers and other methods. Bank
transfers account for 30% of online payments in Poland and Przelewy24 provides a
way for customers to pay with over 165 banks.

Przelewy24 redirects customers to their website to [authenticate a
payment](https://docs.stripe.com/payments/payment-methods#customer-actions) and
there is [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
about the success or failure of a payment.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Poland
- **Presentment currency**

EUR or PLN
- **Payment confirmation**

Customer-authenticated
- **Payment method family**

Authenticated bank debit
- **Recurring payments**

No
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

[No](https://docs.stripe.com/payments/p24#disputed-payments)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/p24#refunds)

## Payment flow

!

Customer selects Przelewy24 at checkout

!

Customer is redirected to Przelewy24 and chooses bank

!

Customer enters account credentials

!

Customer completes authorization process

!

Customer is notified that payment is complete

!

(Optional) Customer returns back to business’s site for payment confirmation

## Get started

You don’t have to integrate Przelewy24 and other payment methods individually.
If you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Przelewy24. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Przelewy24 from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)

If your integration requires manually listing payment methods, learn how to
[manually configure Przelewy24 as a
payment](https://docs.stripe.com/payments/p24/accept-a-payment).

## Prohibited business categories

In addition to the industry and business categories listed in [Prohibited and
restricted businesses](https://stripe.com/restricted-businesses), Przelewy24
prohibits the following business categories:

- Dropshipping businesses
- Businesses selling online training

To learn more about P24 eligibility for your account, see your [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods) in the
Dashboard.

## Additional requirements

Przelewy24 requires that your website or app be publicly available and contain
the following information:

- A list of the products and services you sell and their prices
- Your company’s legal details, including: address, tax number, and registration
number
- Links to your refund policy and privacy policies

Przelewy24 has the right to suspend or terminate your use of Przelewy24 for
breaching the prohibited business categories or failing to meet the additional
requirements listed above.

## Disputes

The risk of fraud or unrecognized payments is low because the customer must
authenticate the payment with their bank. As a result, you won’t have disputes
that turn into chargebacks, with funds withdrawn from your Stripe account.

## Refunds

Payments made with Przelewy24 can only be submitted for refund within 180 days
from the date of the original charge. After 180 days, it is no longer possible
to refund the charge.

## Links

- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [authenticate a
payment](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
- [No](https://docs.stripe.com/payments/p24#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/p24#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure Przelewy24 as a
payment](https://docs.stripe.com/payments/p24/accept-a-payment)
- [Prohibited and restricted
businesses](https://stripe.com/restricted-businesses)