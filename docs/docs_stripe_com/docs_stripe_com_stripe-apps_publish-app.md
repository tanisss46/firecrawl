# Publish your app to the Stripe App Marketplace

## Make your app discoverable to any user by publishing it on the Stripe App Marketplace.

To share your app beyond your own team, publish it to the [Stripe App
Marketplace](https://marketplace.stripe.com/). This makes it available for
installation on any Stripe account, not just your own.

Publication comes with some restrictions:

- Your account must be
[activated](https://docs.stripe.com/get-started/account/activate).
- You can only publish one app per account.
- Currently to publish an app on the Stripe Marketplace, you can’t be a Platform
account.
- Stripe can only support language listings at this time. To support
additional languages, reach out to Stripe.
- Published apps must pass a review process. For more information, see the [app
review requirements](https://docs.stripe.com/stripe-apps/review-requirements)
and [app listing
guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines).
- If you need to remove your app from the Stripe App Marketplace later, you must
contact Stripe for removal.

These restrictions only apply to apps that you share with public users in the
Stripe App Marketplace. If your app only needs to be available to your own [team
members](https://docs.stripe.com/dashboard/teams), learn to [upload and install
your app](https://docs.stripe.com/stripe-apps/upload-install-app) instead.

## Before you begin

- If you’ve already [installed your app in live
mode](https://docs.stripe.com/stripe-apps/upload-install-app), you must
[uninstall
it](https://docs.stripe.com/stripe-apps/upload-install-app#uninstall-your-live-app)
to switch to publishing your app.
- Choose a Stripe account to associate with your app. You can only publish one
app per account.
- To understand the process for getting your app approved for listing, see [app
review requirements](https://docs.stripe.com/stripe-apps/review-requirements).
[Update the distribution
type](https://docs.stripe.com/stripe-apps/publish-app#set-your-distribution-type)-
Set your app to the public distribution.

```
stripe apps set distribution public
```

This command updates the manifest file with a `distribution_type` field set to a
`public` value.

```
{
 "id": "com.example.app",
 "version": "1.2.3",
 "name": "Example App",
 "icon": "./example_icon_32.png",
 "distribution_type": "public"
}
```

[Add
permissions](https://docs.stripe.com/stripe-apps/publish-app#add-permissions)
To add your app’s required permissions:

- Determine which objects your app calls on the Stripe API. If you’re [migrating
an extension to an app](https://docs.stripe.com/stripe-apps/migrate-extension),
you must determine which objects your extension (not your app) calls on the
Stripe API to understand which permissions to include.
- See the [list of
permissions](https://docs.stripe.com/stripe-apps/reference/permissions) you can
add to your [app
manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest).
- You can add a permission to the `permissions` array in your `stripe-app.json`
app manifest file using the following command:

```
stripe apps grant permission "PERMISSION_NAME" "EXPLANATION"
```

Populate the prompts with your permission’s information:

- `PERMISSION_NAME`: The name of the permission you’d like to add. See [possible
permission names](https://docs.stripe.com/stripe-apps/reference/permissions).
- `EXPLANATION`: Explanation for enabling access. Users see this explanation
when they install your app.

Repeat this step for each new permission that you want to add to your
application.

### Your app manifest file should look like this:

To remove a permission, you can also use the CLI:

```
stripe apps revoke permission "PERMISSION_NAME"
```

[Upload in test
mode](https://docs.stripe.com/stripe-apps/publish-app#upload-in-test-mode)
To upload your app, run the following command from your project root directory:

```
stripe apps upload
```

Stripe validates your app manifest, then uploads and installs your app to your
Stripe test account.

After this step:

- Any team member can access your app in [test
mode](https://docs.stripe.com/test-mode) at
[https://dashboard.stripe.com/test/](https://dashboard.stripe.com/test/).
- Your app can [store
secrets](https://docs.stripe.com/stripe-apps/store-secrets) in test mode.
- You can access your app’s signing secret to connect it to a
[backend](https://docs.stripe.com/stripe-apps/build-backend).
[Submit app for
review](https://docs.stripe.com/stripe-apps/publish-app#submit-app-for-review)-
Upload a new version of your app after [setting the distribution
type](https://docs.stripe.com/stripe-apps/publish-app#set-your-distribution-type).

After you make your distribution choice, Stripe automatically applies it to all
future app versions. To change how to distribute your app after you publish it
to all Stripe users, contact Stripe at [Stripe
Support](https://support.stripe.com/contact/email).
- In the Stripe Dashboard, navigate to
[Apps](https://dashboard.stripe.com/apps), then select your app to see its
details page.
- If your app has multiple versions, choose the app version you want to publish
and click **Continue**. If you can’t select a version, [activate your
account](https://docs.stripe.com/get-started/account/activate) first.
- Create your app listing by clicking **Edit listing** and providing an
overview, features, pricing and support, and resource links to help users
evaluate your app. As you complete the listing, you can see its preview on the
right side of the Dashboard.

For tips on ensuring app approval and creating a compelling listing, see [App
listing guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines).
- Click **Continue** to provide the following information before final app
submission:

- **Version**: If your app has multiple versions, select and verify the version
you want to submit for review.
- **Marketplace install URL**: This option is required for [OAUTH
apps](https://docs.stripe.com/stripe-apps/api-authentication/oauth) and
optionally available for apps that support [install
links](https://docs.stripe.com/stripe-apps/install-links). From the Stripe App
Marketplace, users are redirected to this URL to install your app.
#### Note

The URL must link to a page that can initiate the onboarding and installation
process with clear instructions.
- **Testing credentials**: If your app requires sign in, provide at least one
test account to allow Stripe to test and review your app. See the [example
testing
credentials](https://docs.stripe.com/stripe-apps/review-requirements#test-plan-and-credentials).
#### Caution

Stripe **does not** permit you to use real (non-test) accounts for the app
review process.
- **Testing guidance**: Provide user scenarios to allow Stripe to simulate the
user’s intended installation and usage of your app. To increase your chances of
passing app review, see [example testing
guidance](https://docs.stripe.com/stripe-apps/review-requirements#test-plan-and-credentials).
- **Contact emails**: Provide the email of the recipient for app review updates,
and the email of a contact for resolving security incidents.

Any changes you make after starting the review process are subject to an
additional review period. To avoid delays, ensure all information is accurate
according to [App review
requirements](https://docs.stripe.com/stripe-apps/review-requirements) before
final submission.
- To start the review process, click **Submit for review**.

After Stripe reviews and approves your app, you have the ability to publish it
to the Stripe App Marketplace. If you need to make changes, you can cancel your
app in review, and Stripe removes your position in the review queue.

To avoid delays, make sure all information is accurate according to the [App
review requirements](https://docs.stripe.com/stripe-apps/review-requirements)
before final submission. After your app is `In Review`, you won’t be able to
withdraw your submission or make changes. After Stripe reviews and approves your
app, you can publish it to the Stripe App Marketplace.
[Publish your app](https://docs.stripe.com/stripe-apps/publish-app#publish-app)
After Stripe verifies that your app meets all [app review
requirements](https://docs.stripe.com/stripe-apps/review-requirements), we send
a notification to the contact email and update your app details page with a
review decision. If your app requires additional changes, Stripe provides
guidance on the changes you need to address for approval. After you implement
the changes, you can resubmit your app for another review.

- After Stripe approves your app, go to the
[Apps](https://dashboard.stripe.com/apps) page in the Stripe Dashboard. Select
your app, and preview your listing by clicking **Review and publish**.

If you decide to make changes, clicking **Cancel and edit** requires you to
resubmit your app for review.
- To publish and list your app on the Stripe App Marketplace, click **Publish**.

After this step:

- Any user can discover your app on the Stripe App Marketplace.
- Any Stripe account user can install and use your app.
- You can view [app analytics](https://docs.stripe.com/stripe-apps/analytics) as
soon as 24 hours after publication.

## See also

- [Add deep links](https://docs.stripe.com/stripe-apps/deep-links)
- [Versions and
releases](https://docs.stripe.com/stripe-apps/versions-and-releases)

## Links

- [Stripe App Marketplace](https://marketplace.stripe.com)
- [activated](https://docs.stripe.com/get-started/account/activate)
- [app review
requirements](https://docs.stripe.com/stripe-apps/review-requirements)
- [app listing
guidelines](https://docs.stripe.com/stripe-apps/listing-guidelines)
- [team members](https://docs.stripe.com/dashboard/teams)
- [upload and install your
app](https://docs.stripe.com/stripe-apps/upload-install-app)
- [uninstall
it](https://docs.stripe.com/stripe-apps/upload-install-app#uninstall-your-live-app)
- [migrating an extension to an
app](https://docs.stripe.com/stripe-apps/migrate-extension)
- [list of
permissions](https://docs.stripe.com/stripe-apps/reference/permissions)
- [app manifest](https://docs.stripe.com/stripe-apps/reference/app-manifest)
- [test mode](https://docs.stripe.com/test-mode)
- [https://dashboard.stripe.com/test/](https://dashboard.stripe.com/test/)
- [store secrets](https://docs.stripe.com/stripe-apps/store-secrets)
- [backend](https://docs.stripe.com/stripe-apps/build-backend)
- [Stripe Support](https://support.stripe.com/contact/email)
- [Apps](https://dashboard.stripe.com/apps)
- [OAUTH apps](https://docs.stripe.com/stripe-apps/api-authentication/oauth)
- [install links](https://docs.stripe.com/stripe-apps/install-links)
- [example testing
credentials](https://docs.stripe.com/stripe-apps/review-requirements#test-plan-and-credentials)
- [app analytics](https://docs.stripe.com/stripe-apps/analytics)
- [Add deep links](https://docs.stripe.com/stripe-apps/deep-links)
- [Versions and
releases](https://docs.stripe.com/stripe-apps/versions-and-releases)