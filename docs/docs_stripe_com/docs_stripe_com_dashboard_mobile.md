# Stripe Dashboard mobile app

## Learn how to use the mobile app version of the Stripe Dashboard.

Stripe offers a mobile application to access the Dashboard for both iOS and
Android devices. Use the app to view business metrics, track and manage payments
and customers, and initiate payouts. You can also accept in-person payments
(such as Tap to Pay), create payment links, basic invoices, and subscriptions.

## Download the mobile app

- If you haven’t already, 

Mobile app metrics

To explore and manage available charts for iOS:

- Tap **Edit** next to the **Reports overview** title.
- Add, remove, or reorder charts as needed.

To explore and manage available charts for Android:

- On the **Home** tab, scroll down to the bottom, and click **Add or edit
charts**.
- Add, remove, or reorder charts as needed.

### Push notifications

Push notifications are messages sent directly to a user’s device from a mobile
app. To [enable push notifications from the
app](https://support.stripe.com/questions/enabling-notifications-on-the-stripe-dashboard-mobile-app),
you must allow notifications from Stripe in the settings of your phone.

Types of notifications include:

- Daily summary
- New payments
- New customers
- Disputed payments
- Deposited transfers

### Widgets

Widgets are available on
[iOS](https://support.apple.com/guide/iphone/add-edit-and-remove-widgets-iphb8f1bf206/17.0/ios/17.0)
and
[Android](https://developer.android.com/develop/ui/views/appwidgets/overview) to
provide a faster way to manage your business metrics.

To add widgets to your iOS lock screen:

- Touch and hold the **Lock Screen** until **Customize** button appears at the
bottom of the screen
- Tap **Customize**, then tap **Lock Screen**.
- Select any of the 17+ metrics, and set the time range and account you want.
- Tap **Add** or **Done**.
Widget type iOSAndroidHome4 metric widgets, such as:- Daily gross volume
- Daily new payments
- Daily new customers
- Daily net volume
Lock screen17 metric widgets, such as:- Monthly recurring revenue
- Net volume from new sales
- High risk payments
- Dispute activity

## Accept payments on mobile

You can accept and manage in-person or online payments from the Stripe Dashboard
mobile app, such as:

Payment capability Description iOSAndroid[Tap to
pay](https://docs.stripe.com/no-code/tap-to-pay)Accept in-person payments
through a contactless card without needing a hardware reader[Manual card
entry](https://support.stripe.com/questions/b7bd8ea6-d20c-40f8-a273-4d6c4902957a)A
transaction where you enter a customer’s card details and process it in the
Stripe Dashboard[Invoices](https://docs.stripe.com/no-code/invoices)Use invoices
to collect one-time or recurring payments from a specific customer.[Payment
links](https://docs.stripe.com/no-code/payment-links) (including QR
codes)Reusable links that take your customers to a prebuilt checkout
page[Subscriptions](https://docs.stripe.com/no-code/subscriptions)Recurring
payments for your products or services
To accept payments on mobile:

- Verify you meet the following requirements:- Confirm if your [user
role](https://docs.stripe.com/get-started/account/teams/roles) can accept
payments. Users with the **Support specialist** and **View-only** roles can’t
accept payments.
- For contactless payments (such as Tap to pay), confirm if your country
[accepts in-person payment
features](https://docs.stripe.com/terminal/overview#availability).
- If you haven’t already, enable
[2FA](https://support.stripe.com/questions/update-the-phone-number-for-two-step-authentication),
and [verify your phone number](https://dashboard.stripe.com/settings/user).
- Open the Stripe Dashboard mobile app, and tap the plus symbol ().
- Select either:- **Charge a card or send an invoice**: To accept **Tap to
pay**, **Hosted Invoice**, or **Manually Charge Card**.
- **Create a payment link**: To share a link or a QR code to a customer

#### Create subscriptions on iOS

Navigate to the **Customers** tab, select a customer, and then tap the **create
icon (+)** icon in the subscription row. Alternatively, tap the overflow menu
(), and select **Create subscription**. You can only select existing products
with a recurring price.

## Manage payments

You can manage payments from your app:

### Issue a refund

- Tap the **Payments** tab.
- Select a successful payment.
- Navigate to the action bar at the bottom, and tap **Refund**.
- Enter the amount you want to refund, and select if you want to make a partial
refund.

### Send and view receipts

- Tap the **Payments** tab.
- Select a successful payment.
- Navigate to the action bar at the bottom, tap the overflow menu (), and select
**View receipt** or **Send receipt**. You can also send a receipt directly after
accepting a Tap to Pay payment from the success screen. After you complete the
payment, tap **Send receipt**.

### Activate, deactivate, or share payment links (iOS only)

- Tap the **Payments** tab.
- Tap **Payment Links**, and select the active payment link you want to change.
- You can copy the link, generate a QR code, or open the payment link in the web
Dashboard. If you deactivate a payment link, it immediately deactivates without
a confirmation prompt. If you deactivate a payment link by accident, reactivate
it by tapping **Activate** in the action bar at the bottom of the screen.

### Cancel a subscription (iOS only)

- Tap the **Payments** tab.
- Tap **Subscriptions**, and select an active subscription.
- Navigate to the action bar at the bottom, and tap **Cancel subscription**.
- Confirm if you want to cancel the subscription immediately or at the end of
the billing period.

## Create and manage payouts

- Verify you have a [debit card or external account linked to your Stripe
account](https://docs.stripe.com/get-started/account/linked-external-accounts#link-financial-account).-
Currently, you can only link these accounts through the [web
version](https://dashboard.stripe.com/settings/payouts) of the Stripe Dashboard.
- If you want to use instant payouts, use a debit card or bank account that
[supports instant
payouts](https://docs.stripe.com/payouts/instant-payouts-banks).
- Open the Stripe Dashboard mobile app on your device and log in.
- Go to the **Balances** tab at the bottom of the screen. Alternatively, you can
tap the plus symbol () at the top right of any tab and select **Pay out funds**.
- Check your balance:- **Standard payouts**: If you have a positive balance, you
can start the payout process by entering the amount you want to pay out. For
more information, see [Receive payouts](https://docs.stripe.com/payouts).
- **Instant payouts**: Funds acquired from card payments are available as soon
as the charge is complete. ACH or bank debits are only available after the
payment has settled in the Stripe account. For more information, see [Instant
payouts for Stripe Dashboard
users](https://docs.stripe.com/payouts/instant-payouts).
- Complete your payout. The time it takes for funds to settle in the bank
account depends on several factors, including whether you select a standard or
instant payout:- **Standard payouts**: The time it takes for funds to appear in
your account depends on your industry, country, and whether it’s your first
payout. It takes around 7 days for funds to settle in the applicable bank
account for your first payout.
- **Instant payouts**: After Stripe verifies your account is eligible to send
instant payouts, funds typically settle in the applicable bank account within 30
minutes.

## Create and manage customers

To create a new customer:

- Tap the plus icon () at the top right of any tab, and select **Create a
customer**.
- Enter the customer’s name, email address, and a description.

To manage existing customers:

- Tap the **Customer** icon () from the app’s navigation bar, and select a
customer. You can view their past payments, subscriptions, invoices, and payment
cards saved on file.
- Navigate to the action bar at the bottom to:- Add a card on file
- Send customers an email
- Edit their details, or open the customer details in the web Dashboard

## Links

- [iOS on App
Store](https://apps.apple.com/app/apple-store/id978516833?pt=91215812&ct=stripe-docs-mobile&mt=8)
- [Android on Google
Play](https://play.google.com/store/apps/details?id=com.stripe.android.dashboard&pli=1)
- [create a Stripe account](https://dashboard.stripe.com/register)
- [two-factor
authentication](https://support.stripe.com/questions/update-the-phone-number-for-two-step-authentication)
- [verify your phone number](https://dashboard.stripe.com/settings/user)
- [Connect](https://docs.stripe.com/connect)
- [Monitor your
business](https://docs.stripe.com/dashboard/mobile#monitor-business-metrics)
- [Accept online or in-person
payments](https://docs.stripe.com/dashboard/mobile#accept-payments-on-mobile)
- [Manage payments](https://docs.stripe.com/dashboard/mobile#manage-payments)
- [Create
payouts](https://docs.stripe.com/dashboard/mobile#create-and-manage-payouts)
- [Create and manage
customers](https://docs.stripe.com/dashboard/mobile#create-and-manage-customers)
- [User roles](https://docs.stripe.com/get-started/account/teams/roles)
- [enable push notifications from the
app](https://support.stripe.com/questions/enabling-notifications-on-the-stripe-dashboard-mobile-app)
-
[iOS](https://support.apple.com/guide/iphone/add-edit-and-remove-widgets-iphb8f1bf206/17.0/ios/17.0)
- [Android](https://developer.android.com/develop/ui/views/appwidgets/overview)
- [Tap to pay](https://docs.stripe.com/no-code/tap-to-pay)
- [Manual card
entry](https://support.stripe.com/questions/b7bd8ea6-d20c-40f8-a273-4d6c4902957a)
- [Invoices](https://docs.stripe.com/no-code/invoices)
- [Payment links](https://docs.stripe.com/no-code/payment-links)
- [Subscriptions](https://docs.stripe.com/no-code/subscriptions)
- [accepts in-person payment
features](https://docs.stripe.com/terminal/overview#availability)
- [debit card or external account linked to your Stripe
account](https://docs.stripe.com/get-started/account/linked-external-accounts#link-financial-account)
- [web version](https://dashboard.stripe.com/settings/payouts)
- [supports instant
payouts](https://docs.stripe.com/payouts/instant-payouts-banks)
- [Receive payouts](https://docs.stripe.com/payouts)
- [Instant payouts for Stripe Dashboard
users](https://docs.stripe.com/payouts/instant-payouts)