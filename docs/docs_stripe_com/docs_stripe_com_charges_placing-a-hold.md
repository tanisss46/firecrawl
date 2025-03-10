# Placing a hold on a cardCharges API

#### Legacy API

The content of this section refers to a Legacy feature. Use the [Payment Intents
API](https://docs.stripe.com/payments/accept-a-payment) instead.

The Charges API doesn’t support the following features, many of which are
required for credit card compliance:

- Merchants in India
- [Bank requests for card
authentication](https://docs.stripe.com/payments/cards/overview)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)

Use the Charges API to authorize a payment now, capture funds later.

Stripe supports two-step card payments so you can first authorize a charge, then
wait to settle (capture) it later. When a charge is authorized, the card issuer
guarantees the funds and holds the amount on the customer’s card for, usually,
up to 7 days, or 2 days for in-person payments using
[Terminal](https://docs.stripe.com/terminal). The
[payment_method_details.card.capture_before](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-capture_before)
attribute on the charge indicates the time when the authorization expires.

If the charge isn’t captured within this time, the authorization is canceled and
funds released.

## Authorize a payment

To authorize a payment without capturing it, make a charge request that also
includes the `capture` parameter with a value of **false**. This instructs
Stripe to only authorize the amount on the customer’s card.

#### Caution

**Only some payment methods support separate authorization and capture.** For
example, card payments, Afterpay, and Klarna support separating these steps.
With payment methods that don’t support this functionality, like
[ACH](https://docs.stripe.com/payments/ach-direct-debit) or
[iDEAL](https://docs.stripe.com/payments/ideal), you can’t capture manually.
Refer to the [full list of payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support#additional-api-supportability)
that support manual capture.

If you need to cancel an authorization, you can release it by
[refunding](https://docs.stripe.com/api#create_refund) the relevant `Charge`
object.

```
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=999 \
 -d "currency"="usd" \
 -d "description"="Example charge" \
 -d "source"="tok_visa" \
 -d "capture"="false"
```

## Capture the funds

To settle an authorized charge, make a [capture
charge](https://docs.stripe.com/api#capture_charge) request. The total
authorized amount is captured by default, and you cannot capture more than this.
To capture less than the initial amount (for example, 8 USD of a 10 USD
authorization), pass the `amount` parameter. Partially capturing a charge
automatically releases the remaining amount.

```
curl -X POST https://api.stripe.com/v1/charges/{{CHARGE_ID}}/capture \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

Card statements from some issuers do not distinguish between authorizations and
captured (settled) charges, which can sometimes lead to confusion for your
customers. In addition, authorized charges can only be captured once. If you
partially capture a charge, you cannot perform another capture for the
difference. Depending on your requirements, you may be better served by [saving
customer’s card details for later](https://docs.stripe.com/saving-cards) and
creating charges as needed.

## Links

- [Payment Intents API](https://docs.stripe.com/payments/accept-a-payment)
- [Bank requests for card
authentication](https://docs.stripe.com/payments/cards/overview)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [Terminal](https://docs.stripe.com/terminal)
-
[payment_method_details.card.capture_before](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-capture_before)
- [ACH](https://docs.stripe.com/payments/ach-direct-debit)
- [iDEAL](https://docs.stripe.com/payments/ideal)
- [full list of payment
methods](https://docs.stripe.com/payments/payment-methods/payment-method-support#additional-api-supportability)
- [refunding](https://docs.stripe.com/api#create_refund)
- [capture charge](https://docs.stripe.com/api#capture_charge)
- [saving customer’s card details for
later](https://docs.stripe.com/saving-cards)