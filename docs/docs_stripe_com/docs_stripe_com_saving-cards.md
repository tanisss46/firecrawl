# Saving cards with the Charges API

## Learn how to save and update card details to charge customers later.

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

When you collect a customer’s payment information, a Stripe token is created.
This token can only be used once, but that doesn’t mean you have to request your
customer’s card details for every payment.

Stripe provides a [Customer](https://docs.stripe.com/api#customer_object) object
so you can save this—and other—information for later use. You can use `Customer`
objects for creating [subscriptions](https://docs.stripe.com/billing) or future
one-off charges.

## Saving credit card details for later

To make a card available for later charging, including
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating), create
a new `Customer` instead of a `Charge` by providing their email address and
tokenized card information.

Be certain to store the customer ID on your side for later use. You can
subsequently charge that customer by passing the customer ID—instead of a card
representation—in the charge request.

```
# Create a Customer:
curl https://api.stripe.com/v1/customers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d source=tok_mastercard \
 -d email="paying.user@example.com"

# Charge the Customer instead of the card:
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount=1000 \
 -d currency=usd \
 -d customer=cus_7sqFSKcBzzYEAf

# YOUR CODE: Save the customer ID and other info in a database for later.

# When it's time to charge the customer again, retrieve the customer ID.
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount=1500 \
 -d currency=usd \
 -d customer=cus_7sqFSKcBzzYEAf
```

Charges using saved card details can be customized in the same ways as [one-time
charges](https://docs.stripe.com/payments/charges-api).

#### Note

**Stripe typically validates card information when it is saved.** For more
details on when this happens, see [Check if a card is valid without a
charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge).
As a result of this process, customers may see a [temporary
authorization](https://support.stripe.com/questions/why-does-my-customer-see-an-extra-1-00-charge-on-their-statement)
for a small charge in their local currency on their statement. This doesn’t
guarantee that any future charges succeed (for example, the card no longer has
sufficient funds, is reported lost or stolen, or if the account is closed). This
process also updates the results of any checks, including traditional bank
checks by Radar (for example, CVC or postal code), that may have been performed.

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

## Changing the default payment method

Although many of the cards you save can be automatically updated, you should
still adopt a process that allows customers to update or replace the cards on
file (for example, a customer wants to change the card being billed or their
card can’t be automatically updated). The end of the process requires an [update
customer](https://docs.stripe.com/api#update_customer) call, providing a new
token for the `source` parameter.

```
curl https://api.stripe.com/v1/customers/cus_V9T7vofUbZMqpv \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d source=tok_visa
```

This sets the new card as the default payment method for future payments. It
also deletes the previously saved card.

## Multiple payment methods

[Customers](https://docs.stripe.com/api/customers) can also store multiple
payment methods. The first one saved to a customer is set as the
`default_source`. This is used for subscription payments and whenever a charge
request is made with just a customer ID.

You can manage the payment methods saved to a customer (for example,
[create](https://docs.stripe.com/api#create_card) or
[remove](https://docs.stripe.com/api#delete_card) cards) and you can
[update](https://docs.stripe.com/api#update_customer) the customer to change
`default_source` to another stored payment method at any time.

## See also

- [Guide to Payment Methods](https://stripe.com/payments/payment-methods-guide)
- [Creating Charges](https://docs.stripe.com/payments/charges-api)
- [Billing](https://docs.stripe.com/billing)

## Links

- [Payment Intents API](https://docs.stripe.com/payments/accept-a-payment)
- [Bank requests for card
authentication](https://docs.stripe.com/payments/cards/overview)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [Customer](https://docs.stripe.com/api#customer_object)
- [subscriptions](https://docs.stripe.com/billing)
- [save and reuse
cards](https://docs.stripe.com/payments/more-payment-scenarios)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [one-time charges](https://docs.stripe.com/payments/charges-api)
- [Check if a card is valid without a
charge](https://support.stripe.com/questions/check-if-a-card-is-valid-without-a-charge)
- [temporary
authorization](https://support.stripe.com/questions/why-does-my-customer-see-an-extra-1-00-charge-on-their-statement)
- [webhooks](https://docs.stripe.com/webhooks)
-
[fingerprint](https://docs.stripe.com/api/payment_methods/object#payment_method_object-card-fingerprint)
- [update](https://docs.stripe.com/api#update_card)
- [update customer](https://docs.stripe.com/api#update_customer)
- [Customers](https://docs.stripe.com/api/customers)
- [create](https://docs.stripe.com/api#create_card)
- [remove](https://docs.stripe.com/api#delete_card)
- [Guide to Payment Methods](https://stripe.com/payments/payment-methods-guide)