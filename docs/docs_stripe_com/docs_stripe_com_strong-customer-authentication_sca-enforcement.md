# SCA enforcement

## Learn how European regulators enforce Strong Customer Authentication (SCA).

Although Europe is phasing it in unevenly, you should prepare your payment flows
to be ready for SCA as soon as possible if SCA regulations impact you. Preparing
for SCA helps prevent an increase in declines from European cards, and prepares
you in case of early enforcement by banks. Read more about how [enforcement
varies by
country](https://support.stripe.com/questions/strong-customer-authentication-sca-enforcement-date).

## Make sure your integration is SCA-ready

Your integration is SCA-ready when you process all of your payments volume using
[SCA-ready
products](https://docs.stripe.com/strong-customer-authentication#preparing).
Your business must use an SCA-ready product, such as a recent version of Stripe
Checkout, Billing, the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents), or an SCA-ready partner
solution. Additionally, you should:

- Test [3D Secure](https://docs.stripe.com/payments/3d-secure) (3DS)
authentication thoroughly. Use our [regulatory test
cards](https://docs.stripe.com/testing#regulatory-cards) to ensure that your
integration can handle 3DS.
- For off-session payments, make sure you set up and authenticate the card when
saving the payment method, and use the API to [flag off-session
payments](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method).
- If your business uses the Stripe Billing
[Subscriptions](https://docs.stripe.com/billing/subscriptions/creating) or
[Invoice](https://docs.stripe.com/api/invoices) APIs, make sure your integration
can handle [incomplete
statuses](https://docs.stripe.com/billing/migration/strong-customer-authentication).

## Understand incomplete, declined, or failed payments

Payments can be unsuccessful for a number of reasons, including incomplete,
declined, or failed payments. If you look in the Dashboard and see that your
payments aren’t advancing past the incomplete status (`requires_action` in the
API):

- Make sure that your customer isn’t in the process of authenticating. If
they’re authenticating and it’s an on-session payment, they may expect to see
this. It’s also possible that they’ve abandoned the checkout flow.
- Check that you’re [handling next
actions](https://docs.stripe.com/payments/payment-intents/verifying-status#next-actions)
such as authentication—next actions failures can also cause payments to fail.
- For off-session payments, set
[off_session](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-off_session)
to `true` when creating the payment.

Banks can decline payments that require 3DS authentication but don’t have 3DS
enabled. Go to the Dashboard to see which payments were declined for this
reason. For off-session payments, [filter by failed
payments](https://dashboard.stripe.com/payments?status%5B%5D=failed) in the
Dashboard. Hovering over the status badge highlights the decline reason (for
example, authentication required). You can view on-session payments by applying
the [incomplete payments
filter](https://dashboard.stripe.com/payments?status%5B%5D=incomplete) and
seeing if the payment is incomplete, since it requires authentication.

You may see off-session payments failing even though you think they’re exempt
from SCA requirements. For off-session payments, make sure that you’re
authenticating the card when saving card details, either without a payment or
during a payment. When saving cards without a payment, use the Setup Intents API
and set usage to `off_session`. When saving cards during a payment, set
setup_future_usage to `off_session`. Finally, be aware that exemptions aren’t
guaranteed and off-session payments may still require authentication by the
bank.

## Monitor disputes

When monitoring disputes, be aware that payments successfully authenticated
through 3DS fall under the *liability shift* rule. If a cardholder [disputes a
3D Secure
payment](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
as fraudulent, the liability typically shifts from you to the card issuer. If
the card issuer applies exemptions, the payment isn’t authenticated through 3D
Secure, and liability shift doesn’t apply.

## Collect permission to reuse cards

When you set up your payment flow to properly save a card with the Payment
Intents or Setup Intents API, Stripe marks any subsequent off-session payment as
a [merchant-initiated
transaction](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)
(MIT) to reduce the need to authenticate. Merchant-initiated transactions
require an agreement (also known as a *mandate*) between you and your customer.
Add terms to your website or application on how you plan to process payments
that your customer can opt into. At a minimum, make sure that your terms cover
the following:

- The customer’s permission for you to initiate a payment or a series of
payments on their behalf
- The anticipated frequency of payments (that is, one-time or recurring)
- How you determine the payment amount

Add text in your checkout flow that references the terms of the payment, for
example: I authorize [your business name] to send instructions to the financial
institution that issued my card to take payments from my card account in
accordance with the terms of my agreement with you.

## Use SCA-ready Stripe plugins

If you’re searching for an SCA-ready plugin, refer to [Stripe
Partners](https://stripe.com/partners/directory). If you want to migrate an
existing Stripe plugin or developer library to support SCA, refer to the [SCA
migration guide for plugins and developer
libraries](https://docs.stripe.com/strong-customer-authentication/plugins).

## See also

- [SCA readiness](https://docs.stripe.com/strong-customer-authentication)

## Links

- [enforcement varies by
country](https://support.stripe.com/questions/strong-customer-authentication-sca-enforcement-date)
- [SCA-ready
products](https://docs.stripe.com/strong-customer-authentication#preparing)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [regulatory test cards](https://docs.stripe.com/testing#regulatory-cards)
- [flag off-session
payments](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Invoice](https://docs.stripe.com/api/invoices)
- [incomplete
statuses](https://docs.stripe.com/billing/migration/strong-customer-authentication)
- [handling next
actions](https://docs.stripe.com/payments/payment-intents/verifying-status#next-actions)
-
[off_session](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-off_session)
- [filter by failed
payments](https://dashboard.stripe.com/payments?status%5B%5D=failed)
- [incomplete payments
filter](https://dashboard.stripe.com/payments?status%5B%5D=incomplete)
- [disputes a 3D Secure
payment](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments)
- [merchant-initiated
transaction](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)
- [Stripe Partners](https://stripe.com/partners/directory)
- [SCA migration guide for plugins and developer
libraries](https://docs.stripe.com/strong-customer-authentication/plugins)
- [SCA readiness](https://docs.stripe.com/strong-customer-authentication)