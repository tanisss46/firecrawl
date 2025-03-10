# Collect customer phone numbers

## Collect a phone number for shipping or invoicing when your customer makes a payment.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
You can enable phone number collection on all `payment` and `subscription`
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
Sessions (phone number collection isn’t supported in `setup` mode). Only collect
phone numbers if you need them for the transaction.

[Enable phone number
collection](https://docs.stripe.com/payments/checkout/phone-numbers#create-session)
To enable phone number collection, set
[phone_number_collection[enabled]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-phone_number_collection-enabled)
to `true` when creating a Checkout Session.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "line_items[0][price_data][unit_amount]"=1000 \
 -d "line_items[0][price_data][product_data][name]"=T-shirt \
 -d "line_items[0][price_data][currency]"=eur \
 -d "line_items[0][quantity]"=2 \
 -d "phone_number_collection[enabled]"=true \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

With phone number collection enabled, Checkout adds a *required* phone number
field to the payment form. If you’re collecting a shipping address, the phone
number field displays under the address fields. Otherwise, Checkout displays the
phone number field below the email input. Customers can only enter one phone
number per session.

[Retrieve the phone
number](https://docs.stripe.com/payments/checkout/phone-numbers#after-session)
After the session, you can retrieve customer phone numbers from the resulting
[Customer](https://docs.stripe.com/api/customers), or [Checkout
Session](https://docs.stripe.com/api/checkout/sessions) objects:

- [On the Customer](https://docs.stripe.com/api/customers): Checkout saves
collected phone numbers onto the
[phone](https://docs.stripe.com/api/customers/object#customer_object-phone)
property of the Customer object, which you can access programmatically by either
fetching the Customer object directly with the
[API](https://docs.stripe.com/api/customers/retrieve), or by listening for the
[customer.created](https://docs.stripe.com/api/events/types#event_types-customer.created)
event in a [webhook](https://docs.stripe.com/webhooks). You can also view the
customer’s phone number in the
[dashboard](https://dashboard.stripe.com/customers).
- [On the Checkout Session](https://docs.stripe.com/api/checkout/sessions): The
customer’s phone number is also saved in the
[customer_details](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details)
hash of the Checkout Session object, under
[customer_details.phone](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details-phone).
After each successful Checkout Session, Stripe emits the
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
event containing the Checkout Session object (and phone number), which you can
listen for in a [webhook](https://docs.stripe.com/webhooks).
[Collect phone numbers for existing
customers](https://docs.stripe.com/payments/checkout/phone-numbers#existing-customers)
Passing in an existing [Customer](https://docs.stripe.com/api/customers) with a
populated
[phone](https://docs.stripe.com/api/customers/object#customer_object-phone)
property to the [Checkout
Session](https://docs.stripe.com/api/checkout/sessions) results in the phone
number field being prefilled.

If the customer updates their phone number, this updated value persists on the
[phone](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-phone)
property on the [Customer object](https://docs.stripe.com/api/customers) ,
overwriting any previously saved phone number.

### Update phone numbers with the customer portal

You can allow customers to manage their own accounts (which includes [updating
their phone
numbers](https://docs.stripe.com/api/customer_portal/configurations/create#create_portal_configuration-features-customer_update-allowed_updates))
in the customer portal.

## See also

- [Integrate the customer portal](https://docs.stripe.com/customer-management)

## Links

-
[mode](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-mode)
-
[phone_number_collection[enabled]](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-phone_number_collection-enabled)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Google Pay](https://docs.stripe.com/google-pay)
- [E.164](https://en.wikipedia.org/wiki/E.164)
- [Customer](https://docs.stripe.com/api/customers)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [phone](https://docs.stripe.com/api/customers/object#customer_object-phone)
- [API](https://docs.stripe.com/api/customers/retrieve)
-
[customer.created](https://docs.stripe.com/api/events/types#event_types-customer.created)
- [webhook](https://docs.stripe.com/webhooks)
- [dashboard](https://dashboard.stripe.com/customers)
-
[customer_details](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details)
-
[customer_details.phone](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-customer_details-phone)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
-
[phone](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-phone)
- [updating their phone
numbers](https://docs.stripe.com/api/customer_portal/configurations/create#create_portal_configuration-features-customer_update-allowed_updates)
- [Integrate the customer portal](https://docs.stripe.com/customer-management)