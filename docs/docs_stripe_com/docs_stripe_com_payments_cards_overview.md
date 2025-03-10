# How cards work

## Learn how an online credit or debit card payment works.

[Cards](https://docs.stripe.com/payments/cards) are one of the most popular ways
to pay online, with broad global reach. There are different types of cards and
several steps in the process. To build a Stripe integration that supports all of
your customers, see what goes on behind the scenes of a card payment.

Checking card details
Stripe checks that the details provided are formatted correctly (for example,
the expiry date isn’t in the past). There’s no guarantee that the card itself is
valid yet.

Customer authentication
Some banks, especially in regulated regions like Europe and India, may prompt
the customer to authenticate a purchase (for example, by texting the customer a
code to enter on the bank’s website). [Watch our
video](https://www.youtube.com/watch?v=2kc-FjU2-mY) to learn more.

Authorization
The bank checks for sufficient funds and, if successful, holds the amount on the
customer’s account to guarantee it for the Stripe user.

Capture
The money moves from the issuing bank to the Stripe user’s account.

## Card updates

[Updating a saved card](https://docs.stripe.com/api/cards/update) can only
change its name, billing address, expiration date, or metadata. To make any
other changes, you must delete the card and create a new one.

To let your customers manage their own payment methods, implement processes that
allow them to manually update and replace their saved cards.

To change a customer’s default payment method for invoices and subscriptions,
make an API call to [update
customer](https://docs.stripe.com/api#update_customer) and provide a new value
for the `invoice_settings.default_payment_method` property.

```
curl https://api.stripe.com/v1/customers/cus_V9T7vofUbZMqpv \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "invoice_settings[default_payment_method]"=pm_1Msy7wLkdIwHu7ixsxmFvcz7
```

For information on how Checkout handles saved payment methods, see the [create
session](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer)
API reference. To consider default payment methods in other scenarios, use
custom code.

## Automatic card updates

Saved payment method details can continue to work even if the issuing bank
replaces the physical card. Stripe works with card networks and automatically
attempts to update saved card details whenever a customer receives a new card
(for example, replacing an expired card or one that was reported lost or
stolen). This allows your customers to continue using your service without
interruption and reduces the need for you to collect new card details whenever a
card is replaced.

Automatic card updates require card issuers to participate with the network and
provide this information. It’s widely supported in the United States, allowing
Stripe to automatically update most American Express, Visa, Mastercard, and
Discover cards issued there. International support varies from country to
country. It isn’t possible to identify cards that support automatic updates.

You can listen for Stripe [webhooks](https://docs.stripe.com/webhooks) to learn
of card update activity:

- The `payment_method.updated` event notifies you of updates to a card through
an API call.
- The `payment_method.automatically_updated` event notifies you of automatic
card updates from the network.

These events include the card’s new expiration date and last four digits, so you
can update your own records as needed. If the card update includes a new card
number, the
[fingerprint](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-fingerprint)
changes.

## See also

- [Cards](https://docs.stripe.com/payments/cards)
- [Co-badged cards
compliance](https://docs.stripe.com/co-badged-cards-compliance)
- [Payment method integration
options](https://docs.stripe.com/payments/payment-methods/integration-options)

## Links

- [local payment method
pricing](https://stripe.com/pricing/local-payment-methods)
- [Cards](https://docs.stripe.com/payments/cards)
- [Watch our video](https://www.youtube.com/watch?v=2kc-FjU2-mY)
- [Updating a saved card](https://docs.stripe.com/api/cards/update)
- [update customer](https://docs.stripe.com/api#update_customer)
- [create
session](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-customer)
- [webhooks](https://docs.stripe.com/webhooks)
-
[fingerprint](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-fingerprint)
- [Co-badged cards
compliance](https://docs.stripe.com/co-badged-cards-compliance)
- [Payment method integration
options](https://docs.stripe.com/payments/payment-methods/integration-options)