# Card verification checks

## Learn how to make use of card verification checks to protect against disputes and fraud.

When a card payment is submitted to a card network for authorization, Stripe
provides the CVC, postal code, and billing street address for them to verify (if
you collected these from the customer in your checkout flow). The card issuer
checks this against the information they have on file for the cardholder. If the
provided information doesn’t match, the verification check fails. A failed CVC
or postal code check can indicate the payment is fraudulent, so review it
carefully before fulfilling the order.

Each [Charge](https://docs.stripe.com/api#charge_object) object includes the
[verification
response](https://docs.stripe.com/api#create_charge-verification-responses) as
part of its `source` attribute. You can also find the verification results in
the [Dashboard](https://dashboard.stripe.com/test/payments) when viewing a
payment.

If no information is collected, the card issuer can’t perform a verification
check. Collect the CVC, postal code, and billing address for every payment to
avoid this issue. The results of verification checks help improve the detection
of fraudulent activity.

## Card verification code check (CVC)

The CVC (or CVV) is the three- or four-digit number printed directly on a card
that only cardholders in physical possession of the card should have access to.
When you require the CVC value with a card payment method (during payment or
when attaching the payment method to a customer’s profile), the card issuer
verifies the value during transaction authorization.

[Radar](https://docs.stripe.com/radar) allows you to block payments that fail
the card issuer verification in various situations by enabling a
[rule](https://docs.stripe.com/radar/rules#built-in-rules) through the
[Dashboard](https://dashboard.stripe.com/test/radar/rules). This doesn’t affect
payments where the CVC check couldn’t be performed or is unavailable. For
example, [wallets](https://docs.stripe.com/payments/payment-methods) like Apple
Pay or off-session payments don’t require it.

Businesses can’t store the CVC number, so fraudsters are unlikely to obtain the
CVC through a computer breach, making CVC verification an effective fraud
prevention tool. However, CVC verification doesn’t protect against the physical
theft of a card, nor computers or websites with poor security.

## Address verification (AVS)

When you require the postal code and the billing street address with a card
payment method (during payment or when attaching the payment method to a
customer’s profile), the card issuer performs an AVS check to verify that they
match the billing address on file.

[Radar](https://docs.stripe.com/radar) allows you to block payments that fail
the postal code (AVS) verification in various situations by enabling a
[rule](https://docs.stripe.com/radar/rules#built-in-rules) in the
[Dashboard](https://dashboard.stripe.com/test/radar/rules). AVS checks can fail
for legitimate payments. For example, a customer who enters their address
incorrectly or moves without notifying their card issuer might see payments
where the address check fails.

Support for AVS checks varies by country and card issuer. For example, certain
countries don’t use a postal code, and some card issuers don’t support street
address verification. Most cards issued in the United States, Canada, and the
United Kingdom support street address verification.

## See also

- [Best Practices for Preventing
Fraud](https://docs.stripe.com/disputes/prevention/best-practices)
- [Types of Fraud](https://docs.stripe.com/disputes/prevention/fraud-types)
- [Identifying
Fraud](https://docs.stripe.com/disputes/prevention/identifying-fraud)

## Links

- [Charge](https://docs.stripe.com/api#charge_object)
- [verification
response](https://docs.stripe.com/api#create_charge-verification-responses)
- [Dashboard](https://dashboard.stripe.com/test/payments)
- [Radar](https://docs.stripe.com/radar)
- [rule](https://docs.stripe.com/radar/rules#built-in-rules)
- [Dashboard](https://dashboard.stripe.com/test/radar/rules)
- [wallets](https://docs.stripe.com/payments/payment-methods)
- [Best Practices for Preventing
Fraud](https://docs.stripe.com/disputes/prevention/best-practices)
- [Types of Fraud](https://docs.stripe.com/disputes/prevention/fraud-types)
- [Identifying
Fraud](https://docs.stripe.com/disputes/prevention/identifying-fraud)