# Place a hold on a payment method

## Separate payment authorization and capture to create a charge now, but capture funds later.

When you create a payment, you can place a hold on an eligible payment method to
reserve funds that you can capture later. For example, hotels often authorize a
payment in full before a guest arrives, then capture the money when the guest
checks out. This is sometimes referred to as manual capture.

Authorizing a payment guarantees the amount by holding it on the customer’s
payment method. If you’re using the API, the
[payment_method_details.card.capture_before](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-capture_before)
attribute on the charge indicates when the authorization expires.

You need to capture the funds before the authorization expires. If the
authorization expires before you capture the funds, the funds are released and
the payment status changes to `canceled`. Learn more about [statuses for
asynchronous
payments](https://docs.stripe.com/payments/paymentintents/lifecycle).

## Authorization validity windows

The following tables outline validity windows for authorizing different
transaction types.

### Card-not-present transactions

Card brand [Merchant-Initiated
Transaction](https://docs.stripe.com/payments/cits-and-mits) authorization
validity window [Customer-Initiated
Transaction](https://docs.stripe.com/payments/cits-and-mits) authorization
validity window Visa5 days*7 daysMastercard7 days7 daysAmerican Express7 days7
daysDiscover7 days7 days
* The exact authorization window is 4 days and 18 hours, to allow time for
clearing processes.

### Card-present transactions (in-person payments)

Card brand Authorization validity window Visa5 days*Mastercard2 daysAmerican
Express2 daysDiscover2 days
* The exact authorization window is 4 days and 18 hours, to allow time for
clearing processes.

### 30-day authorization windows in Japan

If your account is based in Japan, you can hold JPY-denominated transactions
from Visa, Mastercard, JCB, Diners Club, and Discover for up to 30 days. Non-JPY
and American Express transactions expire after the standard 7-day window.

#### Note

As of April 14, 2024, Visa shortened the authorization window for online
[Merchant-Initiated
Transactions](https://docs.stripe.com/payments/cits-and-mits) from 7 days to 5
days. Visa also lengthened the authorization window for in-person (Terminal)
transactions from 2 days to 5 days.

## Payment method limitations

Before implementing, understand the following limitations for authorizing and
capturing separately.

- Only some payment methods support separate authorization and capture. Some
payment methods that support this include cards, Affirm, Afterpay, Cash App Pay,
Klarna, and PayPal. Some payment methods that don’t support this include
[ACH](https://docs.stripe.com/payments/ach-direct-debit) and
[iDEAL](https://docs.stripe.com/payments/ideal). Read more about [payment method
feature
support](https://docs.stripe.com/payments/payment-methods/payment-method-support).
- Beyond what is outlined in the tables above, other payment methods have
different rules and authorization windows:

- Card payments: The amount is typically on hold for 7 days for online payments
and 2 days for in-person Terminal payments (depending on the type of transaction
and the card network). You can request an extended authorization for certain
[online](https://docs.stripe.com/payments/extended-authorization) and [Terminal
payment
authorizations](https://docs.stripe.com/terminal/features/extended-authorizations)
that are eligible for extended validity periods. Card networks may also restrict
1 USD authorizations you don’t intend to capture.
-
[Affirm](https://docs.stripe.com/payments/affirm/accept-a-payment?platform=web#manual-capture):
If Affirm requires a down payment for very large order amounts, they charge the
amount during authorization and refund if the payment isn’t captured. You then
have 30 days to capture the payment balance.
- [Afterpay /
Clearpay](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#manual-capture):
During authorization, the customer pays the first repayment installment.
Afterpay refunds the payment if it’s never captured. You then have 13 days to
capture the payment balance.
- [Cash App
Pay](https://docs.stripe.com/payments/cash-app-pay/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#manual-capture):
Valid authorizations must be captured within 7 days to complete a payment.
-
[Klarna](https://docs.stripe.com/payments/klarna/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#manual-capture):
You must capture the charge by midnight of the 28th calendar day after the
charge request, otherwise the authorization expires. For example, you’d need to
capture a charge request at UTC 2020-10-01 14:00 by UTC 2020-10-29 00:00.
-
[PayPal](https://docs.stripe.com/payments/paypal/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#manual-capture):
Holds the amount for 10 days. Stripe automatically attempts to extend the hold
for another 10 days, totalling 20 days. Your [settlement
preference](https://docs.stripe.com/payments/paypal/choose-settlement-preference)
might affect the authorization period. See [separate authorization and
capture](https://docs.stripe.com/payments/paypal/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#manual-capture)
for more information.

## Use the Dashboard to authorize and capture

You can authorize a payment and capture funds separately without writing code.

- In the Dashboard, [create a new
payment](https://dashboard.stripe.com/test/payments/new). Select **One-time**.
- When you enter or select the payment method, select **More options** then
**Capture funds later**.

The payment appears in your [payments
page](https://dashboard.stripe.com/test/payments) as **Uncaptured**.

To capture the funds, go to the payment details page and click **Capture**.

## Tell Stripe to authorize only

To indicate that you want separate authorization and capture, specify
[capture_method](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
as `manual` when creating the PaymentIntent. This parameter instructs Stripe to
authorize the amount but not capture it on the customer’s payment method.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d capture_method=manual
```

With the above approach, you tell Stripe that you can only use “capture after”
for a PaymentIntent with eligible payment methods. For example, you can’t accept
card payments and SEPA Direct Debit (which doesn’t support capture after) for a
single PaymentIntent. To accept payment methods that might not all support
capture after, you can configure capture-after-per-payment-method by configuring
`capture_method=manual` on the `payment_method_options[<payment_method_type>]`
object.

For example, by configuring
`payment_method_options[card][capture_method]=manual`, you’re placing only card
payments on hold. You can manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the logic for [dynamically
displaying](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
the most relevant eligible payment methods to each customer based on factors
such as the transaction’s amount, currency, and payment flow.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d "automatic_payment_methods[enabled]"=true \
 -d "payment_method_options[card][capture_method]"=manual
```

Alternatively, you can list `card` and `sepa_debit` using [payment method
types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
like in the example below.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=eur \
 -d "payment_method_types[]"=card \
 -d "payment_method_types[]"=sepa_debit \
 -d "payment_method_options[card][capture_method]"=manual
```

Before continuing to capture, attach a payment method with card details to the
PaymentIntent, and authorize the card by confirming the PaymentIntent. You can
do this by setting the `payment_method` and `confirm` fields on the
PaymentIntent.

#### Extended authorizations

Usually, an authorization for an online card payment is valid for 7 days. To
increase the validity period, you can [place an extended hold on an online card
payment](https://docs.stripe.com/payments/extended-authorization).

## Capture the funds

After the payment method is authorized, the PaymentIntent
[status](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-status)
transitions to `requires_capture`. To capture the authorized funds, make a
PaymentIntent [capture](https://docs.stripe.com/api/payment_intents/capture)
request. This captures the total authorized amount by default. To capture less
or (for certain online card payments) more than the initial amount, pass the
[amount_to_capture](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture)
option. A partial capture automatically releases the remaining amount. If
attempting to capture more than the initial amount for an online card payment,
refer to the [overcapture
documentation](https://docs.stripe.com/payments/overcapture).

The following example demonstrates how to capture 7.50 USD of the authorized
10.99 USD payment:

```
curl https://api.stripe.com/v1/payment_intents/pi_123/capture \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount_to_capture=750
```

Although some card payments are eligible for
[multicapture](https://docs.stripe.com/payments/multicapture), you can only
perform one capture on an authorized payment for most payments. If you partially
capture a payment, you can’t perform another capture for the difference.
(Instead, consider [saving the customer’s payment method details for
later](https://docs.stripe.com/payments/save-during-payment#save-payment-details-for-future-use)
and creating future payments as needed.)

Card statements from some issuers and interfaces from payment methods don’t
always distinguish between authorizations and captured (settled) payments, which
can sometimes confuse customers.

Additionally, when a customer completes the payment process on a PaymentIntent
with manual capture, it triggers the `payment_intent.amount_capturable_updated`
event. You can inspect the PaymentIntent’s
[amount_capturable](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_capturable)
property to see the total amount that you can capture from the PaymentIntent.

## Cancel the authorization

If you need to cancel an authorization, you can [cancel the
PaymentIntent](https://docs.stripe.com/refunds#cancel-payment).

## See also

- [Separate authorization and capture with
Checkout](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted#auth-and-capture)
- [Place an extended hold on an online card
payment](https://docs.stripe.com/payments/extended-authorization)

## Links

- [sample app on GitHub](https://github.com/stripe-samples/placing-a-hold)
-
[payment_method_details.card.capture_before](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-capture_before)
- [statuses for asynchronous
payments](https://docs.stripe.com/payments/paymentintents/lifecycle)
- [Merchant-Initiated
Transaction](https://docs.stripe.com/payments/cits-and-mits)
- [ACH](https://docs.stripe.com/payments/ach-direct-debit)
- [iDEAL](https://docs.stripe.com/payments/ideal)
- [payment method feature
support](https://docs.stripe.com/payments/payment-methods/payment-method-support)
- [online](https://docs.stripe.com/payments/extended-authorization)
- [Terminal payment
authorizations](https://docs.stripe.com/terminal/features/extended-authorizations)
-
[Affirm](https://docs.stripe.com/payments/affirm/accept-a-payment?platform=web#manual-capture)
- [Afterpay /
Clearpay](https://docs.stripe.com/payments/afterpay-clearpay/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#manual-capture)
- [Cash App
Pay](https://docs.stripe.com/payments/cash-app-pay/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#manual-capture)
-
[Klarna](https://docs.stripe.com/payments/klarna/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#manual-capture)
-
[PayPal](https://docs.stripe.com/payments/paypal/accept-a-payment?web-or-mobile=web&payment-ui=direct-api#manual-capture)
- [settlement
preference](https://docs.stripe.com/payments/paypal/choose-settlement-preference)
- [create a new payment](https://dashboard.stripe.com/test/payments/new)
- [payments page](https://dashboard.stripe.com/test/payments)
-
[capture_method](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [dynamically
displaying](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
- [payment method
types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types)
-
[status](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-status)
- [capture](https://docs.stripe.com/api/payment_intents/capture)
-
[amount_to_capture](https://docs.stripe.com/api/payment_intents/capture#capture_payment_intent-amount_to_capture)
- [overcapture documentation](https://docs.stripe.com/payments/overcapture)
- [multicapture](https://docs.stripe.com/payments/multicapture)
- [saving the customer’s payment method details for
later](https://docs.stripe.com/payments/save-during-payment#save-payment-details-for-future-use)
-
[amount_capturable](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_capturable)
- [cancel the PaymentIntent](https://docs.stripe.com/refunds#cancel-payment)
- [Separate authorization and capture with
Checkout](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted#auth-and-capture)