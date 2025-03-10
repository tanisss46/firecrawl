# Konbini payments

## Learn how to accept payments at convenience stores with Konbini.

Konbini allows customers in Japan to pay for bills and online purchases at
convenience stores with cash.

To complete a transaction, customers receive payment codes for specific
convenience stores along with a confirmation number. Customers then bring the
information to a convenience store to make a cash payment. You will receive
payment confirmation instantly, and funds will be available for
[payout](https://docs.stripe.com/payouts) after 4 business days.

Customers can pay at FamilyMart, Lawson, Ministop, and Seicomart stores across
Japan.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Japan
- **Payment method family**

Cash-based payment method
- **Connect support**

Partial: [request an
invite](https://support.stripe.com/contact/email?topic=payment_apis) to create
charges [on behalf of](https://docs.stripe.com/connect/charges#on_behalf_of)
other accounts.
- **Billing support**

[Yes](https://docs.stripe.com/payments/konbini#billing)
- **Presentment currency**

JPY
- **Dispute support**

[No](https://docs.stripe.com/payments/konbini#disputed-payments)
- **Manual capture support**

No
- **Payment confirmation**

Customer-initiated
- **Payout timing**

Standard payout timing applies
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/konbini#refunds)
- **Minimum charge amount**

120 JPY
- **Maximum charge amount**

300,000 JPY

## Payment flow

!

1. Selects Konbini at checkout

!

2. Receives payment codes and a confirmation number

!

3. Makes a cash payment with the appropriate payment code and confirmation
number at a convenience store

!

4. Receives notification that payment is complete

## Get started

You don’t have to integrate Konbini and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Konbini. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Konbini from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)

If you prefer to manually list payment methods, learn how to [manually configure
Konbini as a
payment](https://docs.stripe.com/payments/konbini/accept-a-payment).

## Disputes

Konbini payments have a low risk of fraud or unrecognized payments because the
customer must provide cash payment in person at a convenience store. Generally
Konbini payments can’t be disputed by the customer. However, in some instances
irregularities similar to disputes (by the convenience store) might occur, (for
example, due to mishandling). In these cases, Stripe will need to reach out to
you for next steps.

## Refunds

Konbini payments can be refunded either through the
[Dashboard](https://dashboard.stripe.com/payments) or
[API](https://docs.stripe.com/api#create_refund). To complete a refund, your
customer must provide account information where funds should be returned to.
Stripe automatically contacts the customer at the email address provided at time
of PaymentIntent confirmation and requests this information from them, after
which the refund is processed automatically.

## Billing

Use [Stripe Billing](https://stripe.com/billing) to create Konbini supported
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating) and
[invoices](https://docs.stripe.com/api/invoices).

Due to the in-person nature of Konbini payments, [automatically
charged](https://docs.stripe.com/invoicing/automatic-charging) invoices are not
supported.

Invoices and subscriptions need to be configured with a
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
of `send_invoice`.

## Prohibited business categories

On top of the categories of [businesses restricted from using Stripe
overall](https://stripe.com/restricted-businesses), the following categories are
specifically prohibited from using Konbini.

- Sole proprietors who have been doing business for less than 3 years
- Real Money Trading (RMT), that is, sale of virtual (in-game) characters,
currency, and so on.
- Gambling
- Information selling, in particular:- Money making schemes
- Investment related information
- Gambling strategies for horse racing, pachinko, slot machines, and so on
- Multi-level marketing and pyramid schemes
- Gore content or products
- Unscientific and superstition-based content or products
- Prohibited medical products (per the Japanese Pharmaceutical Affairs Act)
- Content or products offensive to public order or moral
- Personal import facilitation (forwarding)
- Foreign money transfer
- Loans
- Dating sites
- E-cigarettes (vaping), waterpipes (shisha, hookah), and so on
- Fortune-telling

Our financial partner and convenience store chains might reject businesses at
their discretion regardless of category.

## Links

- [payout](https://docs.stripe.com/payouts)
- [request an
invite](https://support.stripe.com/contact/email?topic=payment_apis)
- [on behalf of](https://docs.stripe.com/connect/charges#on_behalf_of)
- [Yes](https://docs.stripe.com/payments/konbini#billing)
- [No](https://docs.stripe.com/payments/konbini#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/konbini#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [manually configure Konbini as a
payment](https://docs.stripe.com/payments/konbini/accept-a-payment)
- [Dashboard](https://dashboard.stripe.com/payments)
- [API](https://docs.stripe.com/api#create_refund)
- [Stripe Billing](https://stripe.com/billing)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [invoices](https://docs.stripe.com/api/invoices)
- [automatically charged](https://docs.stripe.com/invoicing/automatic-charging)
-
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
- [businesses restricted from using Stripe
overall](https://stripe.com/restricted-businesses)