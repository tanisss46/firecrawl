# Test mode and use cases

## Use test mode and our uses cases to test your integration.

Stripe’s test mode allows you to test your integration without making actual
charges or payments. Test mode is a testing environment that simulates creating
real objects without the risk of affecting real transactions or moving actual
money. We recommend using our quality assurance (QA) testing use cases, and
importing our [Postman
collection](https://www.getpostman.com/collections/080102f58f29afa081d7) to aid
you in the testing process.

## Test mode

In test mode, you can charge test credit cards as well as create test products
and prices. You can also use test mode to simulate transactions to make sure
that your integration works correctly. This feature helps to identify any bugs
or errors in your Stripe implementation before you go live with actual payments.

After you create a Stripe account, you can find a set of [test API
keys](https://docs.stripe.com/keys#obtain-api-keys) in the [Stripe
Dashboard](https://dashboard.stripe.com/test/apikeys). You can use these API
keys to create and retrieve simulated data by making requests to the Stripe API.
To start accepting real payments, you need to [activate your
account](https://docs.stripe.com/get-started/account/activate), toggle off test
mode, and use the live API keys in your integration. Stripe provides a number of
resources for testing your integration.

#### Impact on live mode

In the Dashboard, changing settings in test mode might also change them in live
mode. Many Dashboard pages have a white notification box and disable live mode
settings while in test mode. In this case, any settings still enabled are safe
to use. If there’s no white callout, assume any changes made in test mode affect
live mode settings (unless you see an orange test data banner).

### Test mode versus live mode

All Stripe API requests occur in either test mode or live mode. API objects in
one mode aren’t accessible to the other. For instance, a test-mode [product
object](https://docs.stripe.com/api/products/object) can’t be part of a
live-mode payment.

Type When to useObjectsHow to useConsiderationssandboxesUse a sandbox, and its
associated test API keys, as you build your integration. In a sandbox, card
networks and payment providers don’t process payments.API calls return simulated
objects. For example, you can retrieve and use test `account`, `payment`,
`customer`, `charge`, `refund`, `transfer`, `balance`, and `subscription`
objects.Use [test credit cards and
accounts](https://docs.stripe.com/testing#cards). You can’t accept real payment
methods or work with real accounts.[Identity](https://docs.stripe.com/identity)
doesn’t perform any verification checks. Also, Connect [account
objects](https://docs.stripe.com/api/accounts/object) don’t return sensitive
fields.live modeUse live mode, and its associated live API keys, when you’re
ready to launch your integration and accept real money. In live mode, card
networks and payment providers do process payments.API calls return real
objects. For example, you can retrieve and use real `account`, `payment`,
`customer`, `charge`, `refund`, `transfer`, `balance`, and `subscription`
objects.Accept real credit cards and work with customer accounts. You can accept
actual payment authorizations, charges, and captures for credit cards and
accounts.Disputes have a more nuanced flow and a simpler [testing
process](https://docs.stripe.com/testing#disputes). Also, some [payment
methods](https://docs.stripe.com/payments/payment-methods) have a more nuanced
flow and require more steps.
The **Test mode** toggle in the Dashboard doesn’t affect your integration code.
Your test and live mode API keys affect the behavior of your code.

### Test card numbers

Stripe provides a set of [test card
numbers](https://docs.stripe.com/testing#cards) that you can use to simulate
various payment scenarios. You can use these test card numbers to create
simulated payments in test mode without processing actual payments or charges.

When you use test card numbers, you can enter any expiration date in the future
and any three-digit CVC code to simulate a successful payment. If you want to
simulate a failed payment, you can use specific test card numbers and CVC codes
provided by Stripe.

Test card numbers are only valid in test mode. Don’t use them for real payments.

### Delete test data

To delete all of your test data from your Stripe account, complete the following
steps:

- [Log in to the Dashboard](https://dashboard.stripe.com/) using your existing
Stripe account.
- While in test mode, click **Developers** > **Overview**.
- Under **Test data**, click **Review test data**. The dialog gives you a list
of all of your existing test data objects.
- Click **Delete test data** to initiate the deletion process. You can’t undo
the deletion of your test data.

Test mode is temporarily unusable while the deletion process occurs.

#### Note

You must manually delete [Meters](https://docs.stripe.com/api/billing/meter)
because the object isn’t supported by the automated test data deletion process.

### Test email

By default, Stripe doesn’t email customers in test mode. For example, paying an
invoice in test mode doesn’t send a receipt email to the customer. Invoices
finalized through the API in test mode also don’t send a receipt email to the
customer.

If you want Stripe to email customers in test mode, you can do the following in
the Dashboard:

- Create and manually send an invoice to a specific customer.
- Manually send a receipt for a paid invoice.

To verify emails for invoices and receipts, set the email address for your
[Team](https://dashboard.stripe.com/settings/team) on the `Customer` object or
`receipt_email` attribute on the PaymentIntent.

## Testing use cases

The following table contains quality assurance (QA) testing use cases:

Use caseActionCharge success (capturing immediately)- No error.
- The charge appears as **Succeeded** in the Dashboard under
[Payments](https://dashboard.stripe.com/payments).
- Stripe captures the charge.
PaymentIntent authorization success ([capturing funds for
later](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method))
```
{
 ...
 "capture_method": "manual",
 ...
 "status": "requires_capture",
 ...
}
```

PaymentIntent capture success (capturing immediately or [capturing funds for
later](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method))
```
{
 ...
 "status": "succeeded",
 ...
 }
```

Charge failThe charge appears as Failed in the Dashboard under
[Payments](https://dashboard.stripe.com/payments).
```
{
 "error": {
 "charge": "ch_",
 "code": "card_declined",
 "decline_code": "<<REASON HERE>>",
 "doc_url": "https://docs.stripe.com/error-codes#card-declined",
 "message": "Your card was declined.",
 "type": "card_error"
 }
}
```

Radar blockNo matter which version of Radar you use, it might block a charge due
to [high risk](https://docs.stripe.com/radar/risk-evaluation#high-risk) or a
[rule](https://docs.stripe.com/radar/rules). The response is the same as what
you get when a charge fails.Charge disputed- The charge appears as **Disputed**
in the Dashboard under [Payments](https://dashboard.stripe.com/payments).
- Stripe debits the charge amount plus the dispute fee from the balance, creates
a `Dispute` object along with its associated `charge.dispute.created` event.

```
{
 "object": {
 "id": "du_",
 "object": "dispute",
 "charge_id": "ch_",
 ...
 "status": "needs_response"
 }
}
```

Charge inquiry opened

Inquiries are similar to disputes, with three key distinctions: no funds are
withdrawn unless we elevate an inquiry to a dispute, they remain refundable
until disputed, and have a different set of statuses. In this case, Stripe fires
a `charge.dispute.created` event.

```
{
 "object": {
 "id": "du_",
 "object": "dispute",
 "charge_id": "ch_",
 ...
 "is_charge_refundable": true,
 ...
 "status": "warning_needs_response"
 }
}
```

Dispute won

- When a customer wins a dispute, the funds of the original charge are restored
to the account, less the dispute fee.
- Stripe updates the existing `Dispute` object, and fires a
`charge.dispute.closed` event.

```
{
 "object": {
 "id": "du_",
 "object": "dispute",
 "charge_id": "ch_",
 ...
 "status": "won"
 }
}
```

Dispute lost

When a customer loses a dispute, Stripe updates the existing `Dispute` object,
and fires a `charge.dispute.closed` event.

```
{
 "object": {
 "id": "du_",
 "object": "dispute",
 "charge_id": "ch_",
 ...
 "status": "lost"
 }
}
```

Inquiry won

When you win an inquiry, your balance remains the same, as no funds were removed
when you initially opened the inquiry. Stripe updates the existing `Dispute`
object, and fires a `charge.dispute.closed` event.

```
{
 "object": {
 "id": "du_",
 "object": "dispute",
 "charge_id": "ch_",
 ...
 "status": "warning_closed"
 }
}
```

Inquiry lost

- When you lose an inquiry, it escalates to a dispute.
- When it escalates to a dispute, its status changes with a
`charge.dispute.updated` event, and funds are withdrawn in a
`charge.dispute.funds_withdrawn` event:

```
{
 "object": {
 "id": "du_",
 "object": "dispute",
 "charge_id": "ch_",
 ...
 "status": "needs_response"
 }
}
```

Charge refunded

The charge appears as **Refunded** in the Dashboard under
[Payments](https://dashboard.stripe.com/payments).

```
{
 "id": "re_",
 "object": "refund",
 "amount": "<<FULL AMOUNT>>",
 "charge": "ch_",
 ...
 "payment_intent": "pi_", // if you're using PaymentIntents
 ...
 "status": "succeeded"
}
```

Charge partially refunded

- The charge appears as **Refunded** in the Dashboard under
[Payments](https://dashboard.stripe.com/payments).
- The refund amount is different from the charge amount, and you can still
dispute partially-refunded charges.

```
{
 "id": "re_",
 "object": "refund",
 "amount": "<<PARTIAL AMOUNT>>",
 "charge": "ch_",
 ...
 "payment_intent": "pi_", // if you are using PaymentIntents
 ...
 "status": "succeeded"
}
```

Account balance goes negativeMake sure to test for a negative balance on Stripe
and verify that your bank accounts can accept debits from us.Successful payoutIf
you enable webhooks for a [successful
payout](https://docs.stripe.com/api/events/types#event_types-payout.paid)
(recommended), test your handling of the event.Failed payoutIf you enable
webhooks for a [failed
payout](https://docs.stripe.com/api/events/types#event_types-payout.failed)
(recommended), test your handling of the event.
## Stripe’s Postman collection

Postman is a widely-used API development tool. To make integrating Stripe
easier, we provide a [Payments-specific Postman
collection](https://www.getpostman.com/collections/080102f58f29afa081d7) with
the tools you need to test the server-side component of your integration.

### Import the collection

To begin, you need to access the Postman app. You can use either the browser or
desktop version. After launching the app, import the collection.

To start this process on the web, press the **Import** button at the top-left
corner, followed by the **Link** option. Insert the [Payments
collection](https://www.getpostman.com/collections/080102f58f29afa081d7) link.
If you’re using the Postman desktop app, click **File > Import**. After
successfully importing, the collection appears under **Collections**.

![The Import
dialog](https://b.stripecdn.com/docs-statics-srv/assets/postman-import-modal.9cae305f4da63f7bd88cb89885c2e884.png)

The import dialog

### Use the collection

To use the collection, navigate to the collection you just imported and click
**Variables**. your testmode Stripe [secret
key](https://dashboard.stripe.com/test/apikeys) from the Stripe Dashboard, and
paste it into the **Initial Value** field. After you complete this step, you’re
ready to begin making requests.

Other variables are populated by scripts during the runtime of the collection.
For example, when creating a
[customer](https://docs.stripe.com/api/customers/create),
[price](https://docs.stripe.com/api/prices/create),
[charge](https://docs.stripe.com/api/charges/object) or
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object), the system
saves that ID through a script in the collection, which is then accessible for
later requests, like issuing a refund.

![The Variables Tab for the
Collection](https://b.stripecdn.com/docs-statics-srv/assets/postman-variables-tab.791bd1b3fdb2d972387aa80b9e3555de.png)

Add a secret key to a Postman collection

## See also

- [Test your integration](https://docs.stripe.com/testing)
- [Sandboxes](https://docs.stripe.com/sandboxes)

## Links

- [Postman
collection](https://www.getpostman.com/collections/080102f58f29afa081d7)
- [test API keys](https://docs.stripe.com/keys#obtain-api-keys)
- [Stripe Dashboard](https://dashboard.stripe.com/test/apikeys)
- [activate your account](https://docs.stripe.com/get-started/account/activate)
- [product object](https://docs.stripe.com/api/products/object)
- [test credit cards and accounts](https://docs.stripe.com/testing#cards)
- [Identity](https://docs.stripe.com/identity)
- [account objects](https://docs.stripe.com/api/accounts/object)
- [testing process](https://docs.stripe.com/testing#disputes)
- [payment methods](https://docs.stripe.com/payments/payment-methods)
- [Log in to the Dashboard](https://dashboard.stripe.com/)
- [Meters](https://docs.stripe.com/api/billing/meter)
- [Team](https://dashboard.stripe.com/settings/team)
- [Payments](https://dashboard.stripe.com/payments)
- [capturing funds for
later](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
-
[https://docs.stripe.com/error-codes#card-declined](https://docs.stripe.com/error-codes#card-declined)
- [high risk](https://docs.stripe.com/radar/risk-evaluation#high-risk)
- [rule](https://docs.stripe.com/radar/rules)
- [successful
payout](https://docs.stripe.com/api/events/types#event_types-payout.paid)
- [failed
payout](https://docs.stripe.com/api/events/types#event_types-payout.failed)
- [customer](https://docs.stripe.com/api/customers/create)
- [price](https://docs.stripe.com/api/prices/create)
- [charge](https://docs.stripe.com/api/charges/object)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [Test your integration](https://docs.stripe.com/testing)
- [Sandboxes](https://docs.stripe.com/sandboxes)