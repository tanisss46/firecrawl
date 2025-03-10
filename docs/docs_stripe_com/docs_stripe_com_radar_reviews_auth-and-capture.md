# Reviewing uncaptured payments

## Learn how to use reviews if your Stripe integration uses auth and capture.

By default, you [create Stripe
payments](https://docs.stripe.com/payments/accept-a-payment) in one step, which
requires no further action on your part to send the funds to your bank account.

However, Stripe also supports two-step payments, often called [auth and
capture](https://support.stripe.com/questions/does-stripe-support-authorize-and-capture).
If your integration uses this technique, keep in mind that **approving a review
and capturing a payment are separate actions.**

## Reviewing uncaptured payments in the Dashboard

When Stripe places an uncaptured payment in review, the Dashboard displays a
**Capture** button in addition to the set of buttons for closing the review by
approving or refunding it. Also, because refunding uncaptured payments is often
called “releasing” or
“[reversing](https://docs.stripe.com/refunds#refund-requests),” uncaptured
payments have a **Cancel** button instead of a **Refund** button.

#### Note

Approving the review doesn’t automatically capture the charge. You still need to
click **Capture**.

!

## Using the API to automatically capture approved payments

Through the API, you can set up your integration to:

- Immediately capture payments *not* placed in `review`
- Leave payments placed in `review` uncaptured
- When the review is approved, capture the payment

### Immediately capture payments not placed in review

To create an uncaptured payment, set the capture behavior accordingly in the API
request. On success, check the payment intent’s
[review](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-review)
attribute. If the attribute is empty, capture the charge.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

# Get the credit card details submitted by the form
# Create a PaymentIntent with manual capture
payment_intent = Stripe::PaymentIntent.create({
 amount: 1000,
 currency: 'usd',
 payment_method: '{{PAYMENT_METHOD_ID}}',
 description: 'Example charge',
 confirm: true,
 capture_method: 'manual',
})

# Check if the payment is in review. If not, capture it.
if !payment_intent.review
 payment_intent.capture
end
```

### Capturing a payment after a review is approved

By design, the previous step left the payments in `review` uncaptured. In this
step, use [webhooks](https://docs.stripe.com/webhooks) to automate the process
of capturing these payments upon approval.

Start by [configuring your
webhooks](https://docs.stripe.com/webhooks#register-webhook) to listen for the
`review.closed` event. The event data includes the [review
object](https://docs.stripe.com/api#review_object), and the object’s `reason`
attribute indicates whether the review was approved, or if it was closed for
some other reason (for example, the payment was refunded).

```
// Review object included in review.closed event webhook.
{
 "id": "prv_08voh1589O8KAxCGPcIQpmkz",
 "object": "review",
 "payment_intent": "pi_1D0CsEITpIrAk4QYdrWDnbRS",
 "created": 1474379631,
 "livemode": false,
 "open": false,
 "reason": "approved"
}
```

If `reason` is `approved`, capture the charge.

```
# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_BQokikJOvBiI2HlWgH4olfQ2'

post "/my/webhook/url" do
 event_json = JSON.parse(request.body.read)
 event = Stripe::Event.retrieve(event_json["id"])

 if event.type == 'review.closed'
 review = event.object
 if review.reason == 'approved'
 pi = Stripe::PaymentIntent.retrieve(review.payment_intent)
 pi.capture
 end
 end

 status 200
end
```

To capture approved payments, the review process must be completed within 7
days. Otherwise, as with any other uncaptured payment, the authorization
automatically expires and you can no longer capture the payment.

## Links

- [create Stripe payments](https://docs.stripe.com/payments/accept-a-payment)
- [auth and
capture](https://support.stripe.com/questions/does-stripe-support-authorize-and-capture)
- [reversing](https://docs.stripe.com/refunds#refund-requests)
-
[review](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-review)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [webhooks](https://docs.stripe.com/webhooks)
- [configuring your webhooks](https://docs.stripe.com/webhooks#register-webhook)
- [review object](https://docs.stripe.com/api#review_object)