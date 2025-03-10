# Elements with Checkout Sessions API changelogPublic preview

## Keep track of changes to the Elements with Checkout Sessions API integration.

Elements with Checkout Sessions API uses two kinds of beta versions:

- A Stripe.js beta header (e.g., `custom_checkout_beta_5`), which is set on your
front-end integration.
- An API version beta header (e.g., `custom_checkout_beta=v1`), which is set on
your back-end integration.

## Frontend beta versions

Specify the front-end beta version when [initializing
Stripe.js](https://docs.stripe.com/checkout/custom/quickstart#set-up-frontend).

### custom_checkout_beta_5

- Breaking The `initCustomCheckout` function has been renamed to
[initCheckout](https://docs.stripe.com/js/custom_checkout/init)- Within React
Stripe.js, `CustomCheckoutProvider` has been renamed to `CheckoutProvider` and
`useCustomCheckout` has been renamed to `useCheckout`.
- Breaking To confirm the [Express Checkout
Element](https://docs.stripe.com/checkout/one-click-payment-buttons), call
[confirm](https://docs.stripe.com/js/custom_checkout/confirm), passing the
[confirm
event](https://docs.stripe.com/js/elements_object/express_checkout_element_confirm_event)
as `expressCheckoutConfirmEvent`- Previously, Express Checkout Element was
confirmed by calling `event.confirm()`.
- Breaking When [confirm](https://docs.stripe.com/js/custom_checkout/confirm) is
called, Payment Element and Address Element will validate form inputs and render
any errors.
- Breaking Error messages have been standardized and improved.- Errors
returned/resolved by a function represent known scenarios like invalid payment
details or insufficient funds. These are predictable issues that can be
communicated to your customer by displaying the `message` on the checkout page.
- Errors thrown/rejected by a function represent errors in the integration
itself, such as invalid parameters or configuration. These errors are not meant
to be displayed to your customers.
- Breaking Asynchronous methods, such as
[confirm](https://docs.stripe.com/js/custom_checkout/confirm) or
[applyPromotionCode](https://docs.stripe.com/js/custom_checkout/apply_promotion_code),
resolve with a different schema:- A `type="success"|"error"` discriminator field
has been added.
- If successful, the updated session state is populated under the `success` key.
Previously, this was under the `session` key.
- Otherwise, the error continues to be populated under the `error` key.
- Added the `email`, `phoneNumber`, `billingAddress`, and `shippingAddress`
options to [confirm](https://docs.stripe.com/js/custom_checkout/confirm).
- Breaking Address Element no longer automatically updates the
[billingAddress](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-billingAddress)
or
[shippingAddress](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-shippingAddress)
fields on the Session.- So long as Address Element is mounted, form values will
automatically be used when calling
[confirm](https://docs.stripe.com/js/custom_checkout/confirm).
- Listen to the [change
event](https://docs.stripe.com/js/element/events/on_change?type=addressElement)
to use the Address Element value before confirmation.

### custom_checkout_beta_4

- Added
[images](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-images)
to the [Session
object](https://docs.stripe.com/js/custom_checkout/session_object).
- Added
[fields](https://docs.stripe.com/js/custom_checkout/create_element?type=payment#custom_checkout_create_element-options-fields)
as an option when creating the Payment Element.
- Added
[paymentMethods](https://docs.stripe.com/js/custom_checkout/create_element?type=expressCheckout#custom_checkout_create_element-options-paymentMethods)
as an option when creating the Express Checkout Element.
- Breaking Passing invalid options to
[createElement](https://docs.stripe.com/js/custom_checkout/create_element) now
throws an error. Previously, unrecognized options would be silently ignored.
- Breaking
[updateEmail](https://docs.stripe.com/js/custom_checkout/update_email) and
[updatePhoneNumber](https://docs.stripe.com/js/custom_checkout/update_phone_number)
apply changes asynchronously. Calling these methods before the customer finishes
entering complete values might cause poor performance.- Instead of calling
`updateEmail` or `updatePhoneNumber` on each input’s change event, wait until
your customer finishes the input, such as on input blur or when they submit the
form for payment.
- `updateEmail` now validates that the input is a properly formed email address
and returns an error if an invalid input is used.
- `updatePhoneNumber` still performs no validation on the input string.

### custom_checkout_beta_3

- The following fields have been added to the [Session
object](https://docs.stripe.com/js/custom_checkout/session_object):-
[id](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-id)
-
[livemode](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-livemode)
-
[businessName](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-businessName)
- Saved cards can now be reused. Learn how to [save and
reuse](https://docs.stripe.com/payments/checkout/save-during-payment) payment
methods.
- Breaking The default
[layout](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-layout)
of the Payment Element has been changed to `accordion`.- To continue using the
previous default layout, you must explicitly specify `layout='tabs'`.
- Breaking The default behavior of
[confirm](https://docs.stripe.com/js/custom_checkout/confirm) has been changed
to always redirect to your `return_url` after a successful confirmation.-
Previously, `confirm` redirected only if the customer chooses a redirect-based
payment method. To continue using the old behavior, you must pass
[redirect=‘if_required’](https://docs.stripe.com/js/custom_checkout/confirm#custom_checkout_session_confirm-options-redirect)
to `confirm`.

### custom_checkout_beta_2

- Breaking The `lineItem.recurring.interval_count` field has been removed and
replaced with
[lineItem.recurring.intervalCount](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-recurring-intervalCount).
- Breaking The `lineItem.amount` field has been removed and replaced with the
following:-
[lineItem.amountSubtotal](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-amountSubtotal)
-
[lineItem.amountDiscount](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-amountDiscount)
-
[lineItem.amountTaxInclusive](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-amountTaxInclusive)
-
[lineItem.amountTaxExclusive](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-amountTaxExclusive)

### custom_checkout_beta_1

*This is the initial front-end beta version.*

## Back-end changelog

Specify the back-end beta version when [setting up your server
library](https://docs.stripe.com/checkout/custom/quickstart#set-up-server).

*There are no changes to the back-end beta version.*

## Links

- [initializing
Stripe.js](https://docs.stripe.com/checkout/custom/quickstart#set-up-frontend)
- [initCheckout](https://docs.stripe.com/js/custom_checkout/init)
- [Express Checkout
Element](https://docs.stripe.com/checkout/one-click-payment-buttons)
- [confirm](https://docs.stripe.com/js/custom_checkout/confirm)
- [confirm
event](https://docs.stripe.com/js/elements_object/express_checkout_element_confirm_event)
-
[applyPromotionCode](https://docs.stripe.com/js/custom_checkout/apply_promotion_code)
-
[billingAddress](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-billingAddress)
-
[shippingAddress](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-shippingAddress)
- [change
event](https://docs.stripe.com/js/element/events/on_change?type=addressElement)
-
[images](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-images)
- [Session object](https://docs.stripe.com/js/custom_checkout/session_object)
-
[fields](https://docs.stripe.com/js/custom_checkout/create_element?type=payment#custom_checkout_create_element-options-fields)
-
[paymentMethods](https://docs.stripe.com/js/custom_checkout/create_element?type=expressCheckout#custom_checkout_create_element-options-paymentMethods)
- [createElement](https://docs.stripe.com/js/custom_checkout/create_element)
- [updateEmail](https://docs.stripe.com/js/custom_checkout/update_email)
-
[updatePhoneNumber](https://docs.stripe.com/js/custom_checkout/update_phone_number)
-
[id](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-id)
-
[livemode](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-livemode)
-
[businessName](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-businessName)
- [save and
reuse](https://docs.stripe.com/payments/checkout/save-during-payment)
-
[layout](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-layout)
-
[redirect=‘if_required’](https://docs.stripe.com/js/custom_checkout/confirm#custom_checkout_session_confirm-options-redirect)
-
[lineItem.recurring.intervalCount](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-recurring-intervalCount)
-
[lineItem.amountSubtotal](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-amountSubtotal)
-
[lineItem.amountDiscount](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-amountDiscount)
-
[lineItem.amountTaxInclusive](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-amountTaxInclusive)
-
[lineItem.amountTaxExclusive](https://docs.stripe.com/js/custom_checkout/session_object#custom_checkout_session_object-lineItems-amountTaxExclusive)
- [setting up your server
library](https://docs.stripe.com/checkout/custom/quickstart#set-up-server)