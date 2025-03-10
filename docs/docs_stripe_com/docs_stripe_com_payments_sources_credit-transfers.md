# Credit transfers (Sources)Deprecated

## Learn about bank transfers with Stripe.

#### Warning

Stripe doesn’t recommend using credit transfers, which you integrate using the
deprecated [Sources API](https://docs.stripe.com/api/sources). Use the
[PaymentIntents](https://docs.stripe.com/api/payment_intents) and
[PaymentMethods](https://docs.stripe.com/api/payment_methods) APIs to [accept
bank transfer payments](https://docs.stripe.com/payments/bank-transfers).

Credit transfers let customers send money to you directly from their bank
account. Credit transfers are often used by:

- Software or services businesses accepting large, one-off payments from other
businesses.
- Businesses that want a low-cost alternative to cards for large one-time
consumer payments, like car or auction purchases.

Credit transfers might not be a good fit for your business if:

- You accept many low value transactions. Customers have to initiate credit
transfers through their bank account, and can send the wrong amount.
- You need payments to complete at a specific time. It might take a customer
hours or even days to send payment through their bank and credit transfers have
varying speeds by market.
- You frequently send refunds. Most credit transfer methods don’t support
refunds directly. To refund a transaction, Stripe contacts the customer to find
the best way to refund them. The customer might not always respond.

## Payment flow

At checkout, you instruct the customer to send funds to an account number
provided by Stripe (known as a “virtual account number”). The customer initiates
the transfer from their bank’s site, app, ATM, or in-person branch.

![Figure describing the four step payment flow. First, customer elects pay by
credit transfer. Next, they receive a virtual bank account number created by
Stripe. Then, they send payment through their bank to the virtual account
number. Finally, they're notified payment is
complete.](https://b.stripecdn.com/docs-statics-srv/assets/payment_flow.eb89dee4d8cf3a2bd038b6c790fd0cf4.svg)

Some credit transfer methods let you control the amount the customer sends, or
reuse virtual account numbers.

## Product support

Payment method Customer country PaymentIntents Checkout Connect Invoicing
Subscriptions Payment Element Payment Links Mobile Payment Element [Multibanco
(beta)](https://docs.stripe.com/sources/multibanco)Portugal

## Links

- [Sources API](https://docs.stripe.com/api/sources)
- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
- [PaymentMethods](https://docs.stripe.com/api/payment_methods)
- [accept bank transfer
payments](https://docs.stripe.com/payments/bank-transfers)
- [Multibanco (beta)](https://docs.stripe.com/sources/multibanco)