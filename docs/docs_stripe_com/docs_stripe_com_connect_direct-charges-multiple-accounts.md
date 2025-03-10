# Share payment methods across multiple accounts for direct charges

## Save payment details on your platform and clone them to connected accounts for making direct charges.

To create direct charges on multiple connected accounts using the same saved
payment information, use this approach. Otherwise, use [our guide for creating
direct charges](https://docs.stripe.com/connect/direct-charges).

## Save payment details on your platform

When collecting payment details from your customer, set them up for future use
and save them on your platform account. You only need to set up each payment
method once.

### Create a customer on your platform

On your platform account, use the [Customers
API](https://docs.stripe.com/api/customers) to create a Customer object
representing your customer.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Jenny Rosen"
```

### Create a SetupIntent on your platform

When you collect the customer’s payment method details, use the [Setup Intents
API](https://docs.stripe.com/api/setup_intents) to create a
[SetupIntent](https://docs.stripe.com/api/setup_intents) on your platform and
associate it with the customer.

```
curl https://api.stripe.com/v1/setup_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}}
```

If your platform is in a different country than your connected accounts, the
setup performed on your platform might not be sufficient. For example, if your
platform is in the US, the setup process might not trigger the authentication
required for direct charges in countries subject to [SCA
enforcement](https://docs.stripe.com/strong-customer-authentication/sca-enforcement).
To make sure that your setup meets the requirements of the connected account’s
country, you might need to use
[on_behalf_of](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-on_behalf_of)
to specify a connected account in that country.

#### Note

You can accept a payment on your platform (not a direct charge on the connected
account) when collecting payment details to save and clone to connected
accounts. To do so, instead of creating a SetupIntent, create a PaymentIntent
with
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage).
The funds from the PaymentIntent on your platform account go directly to your
platform’s balance.

### Confirm the SetupIntent

Send the SetupIntent’s
[client_secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret)
to your front end and use our client-side SDKs or UI components to collect
payment details and confirm the SetupIntent. For example, you can [use the
Payment Element to collect payment information and confirm the
SetupIntent](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#collect-payment-details).

Confirming on the client allows the customer to go through any flows required to
set up their payment details for future use, such as authentication with [3D
Secure](https://docs.stripe.com/payments/3d-secure).

A successful confirmation creates a
[PaymentMethod](https://docs.stripe.com/api/payment_methods) and attaches it to
the customer for future use.

## Clone the PaymentMethod and create direct charges on connected accounts

After you have a PaymentMethod set up for future use on your platform, clone it
to a connected account and create a direct charge.

### Clone the PaymentMethod to the connected accounts

Use the Payment Methods API to clone the PaymentMethod saved on your platform
account to each desired connected account, as shown in the following example.
Specify the connected account ID as the Stripe account, and pass the IDs of the
Customer and PaymentMethod saved on your platform.

#### Note

You can clone only certain types of PaymentMethods. Cloning supports
PaymentMethods that have `type` set to either `card` or `us_bank_account`.

```
curl https://api.stripe.com/v1/payment_methods \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d customer={{PLATFORM_CUSTOMER_ID}} \
 -d payment_method={{PAYMENT_METHOD_ID}}
```

The cloned PaymentMethod is an independent object with a unique ID. It isn’t
linked to, or kept in sync with, the PaymentMethod on your platform. However,
the cloned PaymentMethod inherits the setup performed on your platform account,
so you don’t need to set it up again on the connected account.

### Create and confirm a PaymentIntent on a connected account

Use the [Payment Intents API](https://docs.stripe.com/api/payment_intents) to
create and confirm a
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) on a connected
account using the cloned PaymentMethod:

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d payment_method={{PAYMENT_METHOD_ID}} \
 -d currency=USD \
 -d amount=1099 \
 -d off_session=true \
 -d confirm=true
```

Creating a charge with the cloned PaymentMethod consumes it, because it’s not
attached to a customer. However, consuming the clone doesn’t affect the original
PaymentMethod saved on your platform. You can’t reuse the consumed clone, but
you can clone the platform PaymentMethod again and use the new clone for another
charge.

### Set up recurring payments on a connected account

To use a cloned PaymentMethod for recurring direct charges on a connected
account, you must create a Customer object on the connected account and attach
the cloned PaymentMethod to it. Then, instead of creating PaymentIntents, create
a [Subscription](https://docs.stripe.com/billing/subscriptions/creating) using
the cloned PaymentMethod and attached Customer.

#### Note

The Customer object you create on the connected account has no association with
the original Customer object stored on your platform account. If you update the
original customer information and want to keep them synchronized, you must also
update any corresponding customers saved on connected accounts.

## Handle customer and payment updates

If you don’t collect recurring payments, you only need to update the customer
and PaymentMethod on your platform account. You clone the PaymentMethod for each
direct charge, which ensures that you’re always using the newest version. The
customer only exists on your platform account, so you don’t need to synchronize
customer details across multiple accounts.

If you collect recurring payments, and you update the customer or PaymentMethod
on your platform account, you’re responsible for updating the corresponding
objects saved on any connected accounts. If you update the original
PaymentMethod on your platform, clone it again and attach the new clone to the
customer and subscription on the connected account. Repeat the process for each
connected account that stores a clone for recurring payments.

## Links

- [our guide for creating direct
charges](https://docs.stripe.com/connect/direct-charges)
- [Customers API](https://docs.stripe.com/api/customers)
- [Setup Intents API](https://docs.stripe.com/api/setup_intents)
- [SCA
enforcement](https://docs.stripe.com/strong-customer-authentication/sca-enforcement)
-
[on_behalf_of](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-on_behalf_of)
-
[setup_future_usage](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-setup_future_usage)
-
[client_secret](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-client_secret)
- [use the Payment Element to collect payment information and confirm the
SetupIntent](https://docs.stripe.com/payments/save-and-reuse?platform=web&ui=elements#collect-payment-details)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [Payment Intents API](https://docs.stripe.com/api/payment_intents)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [Subscription](https://docs.stripe.com/billing/subscriptions/creating)