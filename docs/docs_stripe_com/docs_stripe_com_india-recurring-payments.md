# India recurring paymentsPublic preview

## Learn how to update an integration to support RBI e-mandates.

The Reserve Bank of India (RBI) issued a
[directive](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668)
(amended subsequently in [December
2020](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12002) and [March
2021](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12051&Mode=0))
that introduces additional security measures for recurring payments on India
issued cards. These measures include:

- Banks need to register cardholders and create an e-mandate through a one-time
process, using additional factor authentication (AFA) like [3D Secure
(3DS)](https://docs.stripe.com/payments/3d-secure).
- Banks must alert cardholders at least 24 hours before charges take place and
give them the ability to opt out of transactions.
- Recurring transactions over 15,000 INR (or equivalent in other currencies)
must go through AFA each time.

If you’re an India-based Stripe user or an international (non-IN) Stripe user,
your business is impacted if you have customers who use India cards for:

- Off-session payments
- Subscriptions or Invoices where the `collection_method` is set to
`charge_automatically`

## How payments work with an e-mandate

Stripe has worked with a partner platform to support registering e-mandates and
issuing pre-debit notifications to customers.

#### Note

We don’t currently offer the use of e-mandates to Stripe users in Mexico and
Japan.

Depending on how you’ve integrated with Stripe, you might need to send Stripe
additional information to set up a mandate. The customer must go through AFA
(3DS) to register the mandate.

Subsequent off-session payments or auto-debits for a Subscription undergo a
significant change. Customers need to receive a pre-debit notification at least
24 hours before the actual payment with the exact debit amount mentioned. The
pre-debit notification contains information about the payment and an option to
cancel the mandate. If the payment amount is above 15,000 INR or the mandate’s
maximum amount, the pre-debit notification contains a link to perform AFA (3DS)
to authorize the payment.

Because Stripe is integrating with a partner platform, we wait 26 hours before
charging the customer after receiving a payment request (we add a buffer for
possible downstream issues, which necessitates the 26 hours advance
notification). This means that Stripe delays collecting payment by 26 hours.

Without a mandate for an off-session payment, the payment will be declined.

## Integration

The RBI regulations impact Subscriptions that use
`collection_method=charge_automatically` to charge India issued cards.

#### Note

Stripe doesn’t support e-mandates for India recurring payments with
`PaymentIntents` or `SetupIntents`. To manage mandates for recurring payments,
use Subscriptions, as described below.

### Subscription creation

Custom codeStripe-hosted page
When creating a new Subscription with the API,

- If you have a default payment method set, the Subscription uses the latest
SetupIntent on the payment method, and attempts to find a corresponding mandate.
- If no mandate is in place, Stripe automatically attempts to create one even if
you don’t pass in the relevant parameters in
[mandate_options](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_settings-payment_method_options-card-mandate_options).
The customer then needs to authenticate the payment.

To learn how to create a new Subscription, see [Build a subscriptions
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions).

### Subscription Revenue Recovery

Stripe provides a number of automated recovery features to help collect payments
that might’ve been unsuccessful. If you want to handle these payment failures on
your own, refer to [Build your own handling for recurring charge
failures](https://docs.stripe.com/india-recurring-payments#handle-recurring-charge-failures)
for guidance. Otherwise, some recommendations are listed below.

#### Note

Payments from India issued cards are attempted only once. This behavior is
independent of your payment retry settings. If the payment from an India issued
card fails, your Subscription and Invoice status will still be updated based on
what you configured in your [Subscriptions and emails
settings](https://dashboard.stripe.com/settings/billing/automatic) for “If all
retries for a payment fail”.

#### 3D Secure emails

If a mandate doesn’t exist on the default payment method during Subscription
renewals or updates, Stripe attempts to create a new one. To register the
mandate, the customer needs to complete AFA (3DS). Enable the [Subscriptions and
emails settings](https://dashboard.stripe.com/settings/billing/automatic) to
`Send a Stripe-hosted link for customers to confirm their payments when
required` so that customers can be brought back on-session to complete
authentication if required.

#### Note

Stripe doesn’t attempt to create a new mandate if the current mandate used by
the Subscription is `inactive`.

#### Manage failed payments

We recommend enabling notifications to your customers if their Subscription
payments fail and their Subscription is paused. Stripe can send emails to
customers to update failed card payment methods if you enable it in the
[Subscriptions and emails
settings](https://dashboard.stripe.com/settings/billing/automatic).

### Mandate creation

If you rely on Stripe to automatically create the mandate, the mandate details
are returned in the Invoice’s underlying PaymentIntent and corresponding Charge,
or the SetupIntent if you’re creating the Subscription with a trial.

Stripe doesn’t return a mandate ID if any of the following is true:

- A card isn’t an India issued card.
- The currency for the mandate isn’t supported by either the issuer or for the
Stripe account’s country.
- The India issued card is neither Visa nor Mastercard. Stripe only supports
mandates for these two card brands.

Stripe supports INR mandates for all businesses. The following currencies are
supported only for international (non-IN) businesses:

- USD
- EUR
- GBP
- SGD
- CAD
- CHF
- SEK
- AED
- JPY
- NOK
- MYR
- HKD

There are over 100 issuing banks in India and the process of fully adapting to
the new requirements is expected to take some time. An issuer might not support
e-mandates for a particular currency yet. If so, Stripe doesn’t return a mandate
ID.

### Mandate status and troubleshooting

If Stripe can’t create a mandate, you can suggest using a different card, or you
can offer alternative options such as setting
[collection_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method)
as `send_invoice` for the Subscription instead.

Also, a previously active mandate can become inactive, for instance if the
customer cancels it. In that case, the mandate becomes `inactive` and Stripe
sends a `mandate.updated` event.

For more information on receiving webhooks, see [Steps to receive
webhooks](https://docs.stripe.com/webhooks#webhooks-summary).

### Subscription updates

The pre-debit notification that the bank sends tells the cardholder, at minimum,
about the name of the business, the transaction amount, the date or time of the
debit, the reference number of the mandate, and the reason for debit. Make sure
that your mandate details match what you’re actually debiting the customer for
to avoid confusion or declines.

If you depend on Stripe to automatically create mandates for your Subscription
and want to update a Subscription, we recommend that you bring the customer back
on-session to cancel the original Subscription. Doing so creates a new
subscription in the following scenarios, and creates a new mandate that reflects
the Subscription details accurately:

- Changes to the billing interval of a Subscription
- Upgrades to a Subscription where the customer wants to avoid having to
authorize the payment each renewal. For context, Stripe creates the mandate with
`amount_type=maximum` by default. A customer can still be charged more than the
maximum amount with `amount_type=maximum`. However, the customer must authorize
payments for amounts more than the `mandate_options[amount]` or 15,000 INR
(whichever is less).

Examples:

- If you have `amount_type=maximum` , `amount=100000`, the customer would need
to authenticate for amounts over 1,000 INR.
- If you have `amount=2000000`, the customer would need to authenticate for
amounts over 15,000 INR.

### Pre-debit notification

When the off-session PaymentIntent is
[confirmed](https://docs.stripe.com/api/payment_intents/confirm), the issuing
bank sends the customer the pre-debit notification. The PaymentIntent
transitions to a `processing` state for the entire duration of the pre-debit
notification period (26 hours) and can’t be canceled.

```
{
 "object": "payment_intent",
 ...
 "processing": {
 "card": {
 "customer_notification": {
 "approval_requested": true,
 "completes_at": 1677307005
 }
 },
 "type": "card"
 },
 ...
 "status": "processing",
 ...
}
```

If
[processing.card.customer_notification.approval_requested](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-processing-card-customer_notification-approval_requested)
is `true`, the customer needs to authenticate the payment using the pre-debit
notification sent to them by the issuing bank.

The
[processing.card.customer_notification.completes_at](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-processing-card-customer_notification-completes_at)
attribute specifies the time that the Stripe attempts to charge the card. If
successfully processing the payment requires customer approval, they need to
authenticate the payment by the specified time.

### Error and decline codes

We return error
[codes](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-decline_code)
for the following scenarios:

Error codeDescription`payment_intent_mandate_invalid`Attempting a recurring
payment using an inactive mandate returns this code. You can prevent this by
checking the mandate status before attempting to
charge.`india_recurring_payment_mandate_canceled`Attempting a recurring payment
using a canceled mandate returns this code. This can happen when we only learn
that a mandate has been canceled at this point.`processing_error`Discovery of a
(usually transient) processing error returns this code.
In the context of e-mandates, certain [decline
codes](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-decline_code)
have potentially more specific explanations than [in general
scenarios](https://docs.stripe.com/declines/codes):

Decline codeDescription`transaction_not_approved`Attempting a subsequent payment
when the customer has paused permissions to auto-debit, or doesn’t authenticate
the payment when it’s required returns this code.
## Testing

You can use these [test card
numbers](https://docs.stripe.com/testing#testing-interactively) to simulate
different scenarios.

In a [sandbox](https://docs.stripe.com/sandboxes), it takes approximately 15
minutes for an off-session PaymentIntent to transition out of the `processing`
state. The on-session PaymentIntent for an initial payment never enters the
`processing` state.

Card numbersPaymentMethodsNumberScenario4000003560000123Simulates successful
mandate setup and renewals.4000003560000297Simulates a cardholder receiving a
pre-debit notification for an off-session payment either canceling or pausing
the payment for a mandate of any amount.4000003560000248Simulates the issuing
bank’s failure to send a pre-debit notification to the cardholder during
off-session payment for a mandate of any amount.4000003560000263Simulates a
cardholder canceling a mandate of any amount.
## Limitations

Keep in mind the following limitations:

- Stripe attempts to automatically create mandates only on Subscriptions created
after October 1, 2021. If you have a Subscription created before then, cancel
and create a new Subscription to make sure a mandate is created.
- You can’t create a mandate using the
[Charges](https://docs.stripe.com/api/charges) and
[Sources](https://docs.stripe.com/api/sources) APIs.
- You can’t pass an existing mandate to a Subscription.
- You can’t cancel or update a mandate.

## Links

- [directive](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668)
- [December 2020](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12002)
- [March
2021](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12051&Mode=0)
- [3D Secure (3DS)](https://docs.stripe.com/payments/3d-secure)
-
[mandate_options](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_settings-payment_method_options-card-mandate_options)
- [Build a subscriptions
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [Subscriptions and emails
settings](https://dashboard.stripe.com/settings/billing/automatic)
-
[collection_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method)
- [Steps to receive webhooks](https://docs.stripe.com/webhooks#webhooks-summary)
- [confirmed](https://docs.stripe.com/api/payment_intents/confirm)
-
[processing.card.customer_notification.approval_requested](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-processing-card-customer_notification-approval_requested)
-
[processing.card.customer_notification.completes_at](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-processing-card-customer_notification-completes_at)
-
[codes](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error-decline_code)
- [in general scenarios](https://docs.stripe.com/declines/codes)
- [test card numbers](https://docs.stripe.com/testing#testing-interactively)
- [sandbox](https://docs.stripe.com/sandboxes)
- [Charges](https://docs.stripe.com/api/charges)
- [Sources](https://docs.stripe.com/api/sources)