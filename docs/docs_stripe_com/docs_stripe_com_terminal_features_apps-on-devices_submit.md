# Submit your app for review

## Learn how to submit your Android app to Stripe.

After you finalize your app, you must submit it to Stripe for [app
review](https://docs.stripe.com/terminal/features/apps-on-devices/app-review).
You can upload your app using the Stripe Dashboard.

Make sure to follow the [app review
guidelines](https://docs.stripe.com/terminal/features/apps-on-devices/app-review#app-review-guidelines)
to help with a timely and successful review. For example, verify the
instructions that you intend to provide for the Stripe reviewer. Following your
instructions to make sure they’re complete can help prevent failing the app
review.

### Upload your app

- In the Stripe Dashboard, click **Developers** > **Apps**.
- On the [Terminal
apps](https://dashboard.stripe.com/terminal/apps_on_devices/apps) tab, click
**Create app**.
- In the **App information** window, enter the name of your app and the package
name, then click **Create app**.
- Complete the following steps in the **Upload your APK** window:- Choose the
compatible devices for your app.
- Upload your APK file.
- Add
[instructions](https://docs.stripe.com/terminal/features/apps-on-devices/app-review#instructions)
for the Stripe reviewer.
- Enter the email address where Stripe can send updates about your app review.
You can enter one or multiple email addresses.
- Click **Submit for review**.

## Monitor the review status

After you submit your app for review, you can monitor the following for status
updates:

Delivery methodDescriptionEmailStripe sends an email notification of your app
review results to the email address you provided during submission.DashboardYour
app review status appears on the [app
details](https://dashboard.stripe.com/terminal/apps_on_devices/apps) page.
Webhook

Stripe sends a [webhook](https://docs.stripe.com/webhooks) to your webhook
endpoint:

- `terminal.device_asset_version.app_review_approved` - Stripe approves your app
for deployment.
- `terminal.device_asset_version.app_review_rejected` - The app reviewer
couldn’t approve your app. You must fix the problem and resubmit your app for
review.

You can find all webhook events on the
[Events](https://dashboard.stripe.com/events) page.

## Next steps

- [Deploy your
app](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API)

## Links

- [app
review](https://docs.stripe.com/terminal/features/apps-on-devices/app-review)
- [app review
guidelines](https://docs.stripe.com/terminal/features/apps-on-devices/app-review#app-review-guidelines)
- [Terminal apps](https://dashboard.stripe.com/terminal/apps_on_devices/apps)
-
[instructions](https://docs.stripe.com/terminal/features/apps-on-devices/app-review#instructions)
- [webhook](https://docs.stripe.com/webhooks)
- [Events](https://dashboard.stripe.com/events)
- [Deploy your
app](https://docs.stripe.com/terminal/features/apps-on-devices/deploy-with-API)