# How SetupIntents work

## Learn how SetupIntents work within the payment flow.

Asynchronous payment flows can be complex to manage because they depend on
customer interactions that happen outside of your application.
[PaymentIntents](https://docs.stripe.com/api/payment_intents) and
[SetupIntents](https://docs.stripe.com/api/setup_intents) simplify management by
tracking the status of the flow.

requires_payment_method
When the SetupIntent is created, it has a status of `requires_payment_method`1
until a payment method is attached.

requires_confirmationOptional
After the customer provides their payment method information, the SetupIntent is
ready to be confirmed.

In most integrations, this state is skipped because payment method information
is submitted at the same time that the SetupIntent is confirmed.

requires_action
If the setup requires additional actions, such as authenticating with 3D Secure
, the SetupIntent has a status of `requires_action`1.

processing
After required actions are handled, the SetupIntent moves to `processing`.
Although some payment methods (for example, cards) can process quickly, other
payment methods can take up to several days to process.

succeeded
A SetupIntent with a status of `succeeded` means that the setup is successful.

You can now attach this payment method to a Customer object and use this payment
method for future payments.

requires_payment_method
If the setup fails, SetupIntent’s status returns to `requires_payment_method`.

canceled
You can cancel a SetupIntent at any point before it is `processing` or
`succeeded`.

1 Versions of the API before
[2019-02-11](https://docs.stripe.com/upgrades#2019-02-11) show `requires_source`
instead of `requires_payment_method` and `requires_source_action` instead of
`requires_action`.

## Links

- [PaymentIntents](https://docs.stripe.com/api/payment_intents)
- [SetupIntents](https://docs.stripe.com/api/setup_intents)
- [2019-02-11](https://docs.stripe.com/upgrades#2019-02-11)