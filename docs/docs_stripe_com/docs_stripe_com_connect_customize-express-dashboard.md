# Customize the Express Dashboard

## Learn how to customize the Express Dashboard for your users.

The Express Dashboard allows a platform’s users (connected accounts) to view
their available balance, see upcoming
[payouts](https://docs.stripe.com/payouts), and track their earnings in real
time. It displays an **Activity** feed, an **Earnings** chart, and your
platform’s brand name and icon. Learn how to customize the Express Dashboard for
your users in this guide.

To learn more about each feature in the Express Dashboard, see [Express
Dashboard](https://docs.stripe.com/connect/express-dashboard).

[Add your platform's brand name and
icon](https://docs.stripe.com/connect/customize-express-dashboard#add-platform-branding)
You can display your platform’s brand name, icon, and customize theming in the
Express Dashboard.

Access your [Express branding
settings](https://dashboard.stripe.com/settings/connect/express-dashboard/branding),
enter your platform’s `business_name`, upload your platform’s icon, and
customize your theming settings. When satisfied with the preview, save your
changes. If you already saved your brand information before reading this guide,
skip this step.

[Set custom descriptions for charges and
transfers](https://docs.stripe.com/connect/customize-express-dashboard#set-custom-descriptions)
By default, the **Transactions** list on the Express Dashboard displays generic
descriptions for charges and transfers (for example: `Payment on
{YOUR_PLATFORM}`).

First, determine which type of charge your platform uses. The two recommended
charge types for Express connected accounts are [Destination
Charges](https://docs.stripe.com/connect/charges#destination) and [Separate
Charges and
Transfers](https://docs.stripe.com/connect/charges#separate-charges-transfers).

After you determine the charge type, use the following instructions to update
your integration.

### Destination charges

To update the
[description](https://docs.stripe.com/api/charges/object#charge_object-description)
on a payment object that’s visible to your platform’s users, you need to use the
Stripe API. This applies to all platforms that use [destination
charges](https://docs.stripe.com/connect/destination-charges).

- Find the existing transfer object you created for an account by finding the
latest
[charge](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-charges)
created on the
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object).
- Use the charge object to find the
[transfer](https://docs.stripe.com/api/charges/object#charge_object-transfer)
object associated with the charge.
- Use the transfer object to find the
[destination_payment](https://docs.stripe.com/api/transfers/object#transfer_object-destination_payment)
ID that exists on the transfer.
- Call the [Update Charge](https://docs.stripe.com/api/charges/update) API to
update the
[description](https://docs.stripe.com/api/charges/update#update_charge-description)
on the destination payment using the `destination_payment` ID.

#### Note

The
[destination_payment](https://docs.stripe.com/api/transfers/object#transfer_object-destination_payment)
object belongs to the connected account, so you’ll need to set [the
Stripe-Account header](https://docs.stripe.com/connect/authentication) to the
connected account’s ID to make this call.

```
curl https://api.stripe.com/v1/charges/{{PAYMENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d description="My custom description"
```

This description becomes visible on the charge after you’ve written this field.

Learn more about [creating destination charges on your
platform](https://docs.stripe.com/connect/destination-charges).

### Separate charges and transfers

To update the
[description](https://docs.stripe.com/api/charges/object#charge_object-description)
on a payment object that’s visible to your platform’s users, you need to use the
Stripe API. This applies to platforms that use [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers).

- Use the transfer object to find the
[destination_payment](https://docs.stripe.com/api/transfers/object#transfer_object-destination_payment)
ID that exists on the transfer.
- Call the [Update Charge](https://docs.stripe.com/api/charges/update) API to
update the
[description](https://docs.stripe.com/api/charges/update#update_charge-description)
on the destination payment using the `destination_payment` ID found in the
previous step.

#### Note

The
[destination_payment](https://docs.stripe.com/api/transfers/object#transfer_object-destination_payment)
object belongs to the connected account, so you’ll need to set [the
Stripe-Account header](https://docs.stripe.com/connect/authentication) to the
connected account’s ID to make this call.

```
curl https://api.stripe.com/v1/charges/{{PAYMENT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d description="My custom description"
```

This description becomes visible on the charge after you’ve written this field.

Learn more about [creating separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers).

## See also

- [Collect payments and then pay
out](https://docs.stripe.com/connect/collect-then-transfer-guide) (if you
process payments with Stripe)
- [Pay out money](https://docs.stripe.com/connect/add-and-pay-out-guide) (if you
add money from a bank account to pay out)

## Links

- [payouts](https://docs.stripe.com/payouts)
- [Express Dashboard](https://docs.stripe.com/connect/express-dashboard)
- [Express branding
settings](https://dashboard.stripe.com/settings/connect/express-dashboard/branding)
- [Destination Charges](https://docs.stripe.com/connect/charges#destination)
- [Separate Charges and
Transfers](https://docs.stripe.com/connect/charges#separate-charges-transfers)
-
[description](https://docs.stripe.com/api/charges/object#charge_object-description)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
-
[charge](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-charges)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
- [transfer](https://docs.stripe.com/api/charges/object#charge_object-transfer)
-
[destination_payment](https://docs.stripe.com/api/transfers/object#transfer_object-destination_payment)
- [Update Charge](https://docs.stripe.com/api/charges/update)
-
[description](https://docs.stripe.com/api/charges/update#update_charge-description)
- [the Stripe-Account header](https://docs.stripe.com/connect/authentication)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Collect payments and then pay
out](https://docs.stripe.com/connect/collect-then-transfer-guide)
- [Pay out money](https://docs.stripe.com/connect/add-and-pay-out-guide)