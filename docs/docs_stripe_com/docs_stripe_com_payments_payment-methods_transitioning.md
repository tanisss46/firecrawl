# Transition to the Payment Intents and Payment Methods APIs

## Learn how to transition from the Sources and Tokens APIs to the Payment Methods API.

The [Payment Methods API](https://docs.stripe.com/api/payment_methods) replaces
the existing [Tokens](https://docs.stripe.com/api/tokens) and
[Sources](https://docs.stripe.com/api/sources) APIs as the recommended way for
integrations to collect and store payment information. It works with the
[Payment Intents API](https://docs.stripe.com/payments/payment-intents) to
create payments for a wide range of payment methods.

We plan to turn off Sources API support for local payment methods. If you
currently handle any local payment methods using the Sources API, you must
[migrate them to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning#migrate-local-payment-methods).
We’ll send email communication with more information about the end of support
for the Sources and Tokens APIs.

While we don’t plan to turn off support for card payment methods, we still
recommend that you migrate them to the Payment Methods and Payment Intents APIs.
For more information about migrating card payment methods, see [Migrating to the
Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration).

## Migrate local payment methods from the Sources API to the Payment Intents API

To migrate your integration for local payment methods, update your server and
front end to use the [PaymentIntents
API](https://docs.stripe.com/api/payment_intents). There are three typical
integration options:

- Redirect to [Stripe Checkout](https://docs.stripe.com/payments/checkout) for
your payment flow.
- Use the Stripe [Payment
Element](https://docs.stripe.com/payments/payment-element) on your own payment
page.
- Build your own form and use the Stripe JS SDK to complete the payment.

If you use Stripe Checkout or the Payment Element, you can add and manage most
payment methods from the Stripe Dashboard without making code changes.

For specific information about integrating a local payment method using the
Payment Methods API, see the instructions for that payment method in [the
payment methods
documentation](https://docs.stripe.com/payments/payment-methods/overview). The
following table provides a high-level comparison of the different payment types.

Old integrationStripe CheckoutPayment ElementOwn form
Low complexity

Medium complexity

High complexity

Create a Source on the front end or on the serverCreate a Checkout Session on
the serverCreate a PaymentIntent on the serverCreate a PaymentIntent on the
serverAuthorize payment by loading a widget or redirecting to a third partyNot
neededPass the client secret to the front end and use the Stripe JS SDK to
render a Payment Element to complete the paymentPass the client secret to the
front end, use your own form to collect details from your customer, and complete
the payment according to the payment methodConfirm the source is chargeable and
charge the SourceNot neededNot neededNot neededConfirm the Charge succeeded
asynchronously with the `charge.succeeded` webhookConfirm the Checkout session
succeeded with the `payment_intent.succeeded` webhookConfirm the PaymentIntent
succeeded with the `payment_intent.succeeded` webhookConfirm the PaymentIntent
succeeded with the `payment_intent.succeeded` webhook
#### Caution

A PaymentIntent object represents a payment in the new integration, and it
creates a Charge when you confirm the payment on the front end. If you
previously stored references to the Charge, you can continue to do so by
fetching the Charge ID from the PaymentIntent after the customer completes the
payment. However, we also recommend that you store the PaymentIntent ID.

### Checking payment status

Previously, your integration should have checked both the status of the Source
and the status of the Charge after each API call. You no longer need to check
two statuses—you only need to check the status of the PaymentIntent or the
Checkout Session after you confirm it on the front end.

payment_intent.statusMeaningSpecial instructions`succeeded`The payment
succeeded.Not applicable`requires_payment_method`The payment failed.Not
applicable`requires_action`The customer hasn’t completed authorizing the
payment.If the customer doesn’t complete the payment within 48 hours, then the
PaymentIntent transitions to `requires_payment_method` and you can retry the
confirmation.
Always confirm the status of the PaymentIntent by fetching it on your server or
listening for the webhooks on your server. Don’t rely solely on the user
returning to the `return_url` that’s provided when you confirm the
PaymentIntent.

### Refunds

You can continue to call the Refunds API with a Charge that the PaymentIntent
creates. The ID of the Charge is accessible on the `latest_charge` parameter.

Alternatively, you can provide the PaymentIntent ID to the Refunds API instead
of the Charge.

### Error handling

Previously, you had to handle errors on the Sources. With PaymentIntents,
instead of checking for errors on a Source, you check for errors on the
PaymentIntent when it’s created and after the customer has authorized the
payment. Most errors on the PaymentIntent are of `invalid_request_error` type,
returned in an invalid request.

When you migrate your integration, keep in mind that PaymentIntent error codes
can differ from the corresponding error codes for Sources.

### Webhooks

If you previously listened to Source events, you might need to update your
integration to listen to new event types. The following table shows some
examples.

Old webhookNew webhook on CheckoutNew webhook on PaymentIntentsSpecial
instructions`source.chargeable`Not applicableNot applicable`source.failed`Not
applicableNot applicable`source.canceled`Not applicableNot
applicable`charge.succeeded``checkout.session.completed``payment_intent.succeeded`The
`charge.succeeded` webhook is also sent, so you don’t have to update your
integration to listen to the new webhook.`charge.failed`Not applicable - The
customer can re-attempt the payment on the same Checkout Session until it
[expires](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-expires_at),
at which point you receive a `checkout.session.expired`
event.`payment_intent.payment_failed`The `charge.failed` webhook is also sent,
so you don’t have to update your integration to listen to the new
webhook.`charge.dispute.created``charge.dispute.created``charge.dispute.created`
## Transitioning to the Payment Methods API

The main difference between the Payment Methods and Sources APIs is that Sources
describes the transaction state through the
[status](https://docs.stripe.com/api/sources/object#source_object-status)
property. That means that each `Source` object must transition to a chargeable
state before you can use it for a payment. By contrast, a `PaymentMethod` is
stateless, relying on the
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) object to
represent payment state.

#### Note

The following table isn’t a comprehensive list of payment methods. If you
integrate other payment methods with the Sources API, migrate them to the
Payment Methods API as well.

FlowsIntegrate Payment Method with Payment Intents API Tokens or Sources with
Charges API Cards[Card
payments](https://docs.stripe.com/payments/cards)[Supported on
Tokens](https://docs.stripe.com/payments/charges-api); Not recommended on
SourcesACH Direct Debit[US bank account direct
debits](https://docs.stripe.com/payments/ach-direct-debit)[Supported on
Tokens](https://docs.stripe.com/ach-deprecated) Not supported on
SourcesAlipay[Alipay
payments](https://docs.stripe.com/payments/alipay)[Deprecated](https://docs.stripe.com/sources/alipay)Bancontact[Bancontact
payments](https://docs.stripe.com/payments/bancontact)[Deprecated](https://docs.stripe.com/sources/bancontact)EPS[EPS
payments](https://docs.stripe.com/payments/eps)Deprecatedgiropay[giropay
payments](https://docs.stripe.com/payments/giropay)[Deprecated](https://docs.stripe.com/sources/giropay)iDEAL[iDEAL
payments](https://docs.stripe.com/payments/ideal)[Deprecated](https://docs.stripe.com/sources/ideal)Klarna[Klarna
payments](https://docs.stripe.com/payments/klarna)DeprecatedMultibanco[Multibanco
payments](https://docs.stripe.com/payments/multibanco)[Deprecated
Beta](https://docs.stripe.com/sources/multibanco)Przelewy24[Przelewy24
payments](https://docs.stripe.com/payments/p24)[Deprecated](https://docs.stripe.com/sources/p24)SEPA
Direct Debit[Single Euro Payments Area direct
debits](https://docs.stripe.com/payments/sepa-debit)[Deprecated](https://docs.stripe.com/sources/sepa-debit)Sofort[Sofort
payments](https://docs.stripe.com/payments/sofort)DeprecatedWeChat Pay[WeChat
Pay
payments](https://docs.stripe.com/payments/wechat-pay)[Deprecated](https://docs.stripe.com/sources/wechat-pay)
After you choose the API to integrate with, use the [guide to payment
methods](https://stripe.com/payments/payment-methods-guide) to help you
determine the right payment method types you need to support.

This guide includes detailed descriptions of each payment method and describes
the differences in the customer-facing flows, along with the [geographic
regions](https://stripe.com/payments/payment-methods-guide#payment-methods-fact-sheets)
where they’re most relevant. You can enable any payment method available to you
within the [Dashboard](https://dashboard.stripe.com/account/payments/settings).
Activation is generally instantaneous and doesn’t require additional contracts.

## Compatibility with legacy reusable payment methods

If you previously processed any of the following reusable payment methods using
[Sources](https://docs.stripe.com/sources), the existing saved sources don’t
migrate automatically:

- Alipay
- Bacs Direct Debit
- SEPA Direct Debit

To preserve your existing customers’ saved payment methods, you must convert
those sources to payment methods using a data migration tool in the Stripe
Dashboard. For instructions on how to convert them, see [the support
page](https://support.stripe.com/questions/reusable-object-migration).

## Compatibility with legacy card objects

If you previously collected card customer payment details with Stripe using
[cards](https://docs.stripe.com/saving-cards) or
[Sources](https://docs.stripe.com/sources), you can start using the Payment
Methods API immediately without migrating any payment information.

Compatible payment instruments that have been saved to a
[Customer](https://docs.stripe.com/api/customers) are usable in any API that
accepts a [PaymentMethod](https://docs.stripe.com/api/payment_methods) object.
For example, you can use a saved card as a PaymentMethod when creating a
PaymentIntent:

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "payment_method_types[]"=card \
 -d amount=1099 \
 -d currency=usd \
 -d customer={{CUSTOMER_ID}} \
 -d payment_method={{CARD_ID}}
```

Remember to provide the customer ID that your compatible payment instrument is
saved to when attaching the object to a PaymentIntent.

You can [retrieve](https://docs.stripe.com/api/payment_methods/retrieve) all
saved compatible payment instruments through the Payment Methods API.

CardCard Source
```
{
 "id": "card_1EBXBSDuWL9wT9brGOaALeD2",
 "object": "card",
 "address_city": "San Francisco",
 "address_country": "US",
 "address_line1": "1234 Fake Street",
 "address_line1_check": null,
 "address_line2": null,
 "address_state": null,
 "address_zip": null,
```

See all 26 lines
```
{
 "id": "card_1EBXBSDuWL9wT9brGOaALeD2",
 "object": "payment_method",
 "billing_details": {
 "address": {
 "city": "San Francisco",
 "country": "US",
 "line1": "1234 Fake Street",
 "line2": null,
 "postal_code": null,
```

See all 41 lines
With this compatibility, no new objects are created; the Payment Methods API
provides a different view of the same underlying object. For example, updates to
a compatible payment instrument through the Payment Methods API is visible
through the Sources API, and vice versa.

## See also

- [Guide to payment methods](https://stripe.com/payments/payment-methods-guide)
- [Connect payments](https://docs.stripe.com/connect/charges)
- [Payment Methods API reference](https://docs.stripe.com/api/payment_methods)

## Links

- [Payment Methods API](https://docs.stripe.com/api/payment_methods)
- [Tokens](https://docs.stripe.com/api/tokens)
- [Sources](https://docs.stripe.com/api/sources)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Migrating to the Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration)
- [PaymentIntents API](https://docs.stripe.com/api/payment_intents)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [the payment methods
documentation](https://docs.stripe.com/payments/payment-methods/overview)
-
[expires](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-expires_at)
- [status](https://docs.stripe.com/api/sources/object#source_object-status)
- [Card payments](https://docs.stripe.com/payments/cards)
- [Supported on Tokens](https://docs.stripe.com/payments/charges-api)
- [US bank account direct
debits](https://docs.stripe.com/payments/ach-direct-debit)
- [Supported on Tokens](https://docs.stripe.com/ach-deprecated)
- [Alipay payments](https://docs.stripe.com/payments/alipay)
- [Deprecated](https://docs.stripe.com/sources/alipay)
- [Bancontact payments](https://docs.stripe.com/payments/bancontact)
- [Deprecated](https://docs.stripe.com/sources/bancontact)
- [EPS payments](https://docs.stripe.com/payments/eps)
- [giropay payments](https://docs.stripe.com/payments/giropay)
- [Deprecated](https://docs.stripe.com/sources/giropay)
- [iDEAL payments](https://docs.stripe.com/payments/ideal)
- [Deprecated](https://docs.stripe.com/sources/ideal)
- [Klarna payments](https://docs.stripe.com/payments/klarna)
- [Multibanco payments](https://docs.stripe.com/payments/multibanco)
- [Deprecated Beta](https://docs.stripe.com/sources/multibanco)
- [Przelewy24 payments](https://docs.stripe.com/payments/p24)
- [Deprecated](https://docs.stripe.com/sources/p24)
- [Single Euro Payments Area direct
debits](https://docs.stripe.com/payments/sepa-debit)
- [Deprecated](https://docs.stripe.com/sources/sepa-debit)
- [Sofort payments](https://docs.stripe.com/payments/sofort)
- [WeChat Pay payments](https://docs.stripe.com/payments/wechat-pay)
- [Deprecated](https://docs.stripe.com/sources/wechat-pay)
- [guide to payment methods](https://stripe.com/payments/payment-methods-guide)
- [geographic
regions](https://stripe.com/payments/payment-methods-guide#payment-methods-fact-sheets)
- [Dashboard](https://dashboard.stripe.com/account/payments/settings)
- [Sources](https://docs.stripe.com/sources)
- [the support
page](https://support.stripe.com/questions/reusable-object-migration)
- [cards](https://docs.stripe.com/saving-cards)
- [Customer](https://docs.stripe.com/api/customers)
- [retrieve](https://docs.stripe.com/api/payment_methods/retrieve)
- [Connect payments](https://docs.stripe.com/connect/charges)