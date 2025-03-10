# Use digital wallets with Issuing

## Learn how to use Issuing to add cards to digital wallets.

Issuing allows users to add cards to digital wallets like Apple Pay and Google
Pay. Stripe supports the addition of cards through two methods:

- **Manual Provisioning:** cardholders enter their card details into a phone’s
wallet application to add it to their digital wallets.
- **Push Provisioning:** mobile applications allow users to add cards to their
digital wallets straight from the app.

When a card is added to a digital wallet, a tokenized representation of that
card is created. Network tokens are managed separately from cards. For more
information about network tokens and how they work, see [Token
Management](https://docs.stripe.com/issuing/controls/token-management).

## Manual Provisioning

Cardholders can add Stripe Issuing [virtual
cards](https://docs.stripe.com/issuing/cards/virtual) and [physical
cards](https://docs.stripe.com/issuing/cards/physical) to their Apple Pay,
Google Pay, and Samsung Pay wallets through manual provisioning.

To do so, cardholders open the wallet app on their phone and enter their card
details. Stripe then sends a 6-digit verification code to the `phone_number` or
`email` of the cardholder associated with the card.

A *card not supported* error displays if neither field is set on the cardholder
when the card was provisioned.

No code is required to implement manual provisioning, but the process to set it
up can vary depending on the digital wallet provider and the country you’re
based in:

### US

Apple Pay wallets require approval from Apple. Check your [digital wallets
settings](https://dashboard.stripe.com/settings/issuing/digital-wallets) to view
the status of Apple Pay in your account. You might need to submit an application
before using Apple Pay.

Google Pay and Samsung Pay have no additional required steps.

### EU/UK

Digital wallet integrations require additional approval from the Stripe
partnership team. Get in touch with your account representative or [contact
Stripe](https://stripe.com/contact/sales) for more information.

Apple Pay wallets require additional approval. Check your [digital wallets
settings](https://dashboard.stripe.com/settings/issuing/digital-wallets) to view
the status of Apple Pay in your account. You might need to submit an application
before using Apple Pay.

## Push Provisioning

With push provisioning, cardholders can add their Stripe Issuing cards to their
digital wallets using your app, by pressing an “add to wallet” button like the
ones shown below.

Users must first complete manual provisioning steps in order to enable push
provisioning in the US. In addition to manual provisioning approval, push
provisioning requires you to integrate with the Stripe SDK.

This requires both approval processes through Stripe and code integration with
the Stripe SDK for each platform you wish to support push provisioning on.
Platform approvals cascade down to all of their connected accounts.

Samsung Pay push provisioning isn’t supported with our SDKs.

iOSAndroidReact Native

![A white UI button that says Add to G Pay. The G has Google's colors of red,
yellow, green, and
blue.](https://b.stripecdn.com/docs-statics-srv/assets/add_to_google_pay.749ba35cf98e7dc87dac0108ea7f688a.png)

[Request
Access](https://docs.stripe.com/issuing/cards/digital-wallets#request-access)
Stripe provides an SDK wrapper around a private Google library for push
provisioning. To distribute your app on the Google Pay Store with push
provisioning you need to:

- [Request access to Google
Pay](https://developers.google.com/pay/issuers/requesting-access?api=true).
After you complete the form, expect approval within a few hours to a day.
- After receiving approval, download Google’s [TapAndPay private
SDK](https://developers.google.com/pay/issuers/apis/push-provisioning/android/releases).
The most recently tested version of the TapAndPay SDK is version 18.
- [Request access to the push provisioning
API](https://support.google.com/faqs/contact/pp_api_allowlist) for your app. You
must provide your [application
ID](https://developer.android.com/studio/build/application-id) to be added to
Google’s allowlist. Details on this process are available in Google’s
[documentation](https://developers.google.com/pay/issuers/apis/push-provisioning/android/allowlist).
After the process is complete, Google grants push provisioning entitlements.
- After Google has granted push provisioning entitlements, [contact
Stripe](mailto:support-issuing@stripe.com) with your application name and
application ID to complete this step.
[Update your
appClient-side](https://docs.stripe.com/issuing/cards/digital-wallets#update-your-app)-
Import Google’s [private
SDK](https://developers.google.com/pay/issuers/apis/push-provisioning/android/setup).
- Import Stripe’s SDK.

```
dependencies {
 [... your dependencies]
 implementation 'com.stripe:stripe-android-issuing-push-provisioning:1.2.2'
}
```

For more context, see the code snippets and references to the sample app at each
step. For this step, see how the [sample
app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/app/build.gradle.kts#L111-L118)
imports these SDKs.

- Prepare your backend to create ephemeral keys for your cards. [See section
below](https://docs.stripe.com/issuing/cards/digital-wallets#backend-changes).
- Create an `EphemeralKeyProvider` that extends
`PushProvisioningEphemeralKeyProvider`. As the ephemeral key provider will be
passed to another activity, it also needs to implement `Parcelable` (see
[Parcelable](https://developer.android.com/reference/android/os/Parcelable)).
For more context, see how the [sample
app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/app/src/main/java/com/stripe/android/pushprovisioning/network/BackendPushProvisioningEphemeralKeyProvider.kt#L20-L43)
defines its `EphemeralKeyProvider`.
- Implement the **Add to Google Pay** button [according to Google’s
specifications](https://developers.google.com/pay/issuers/apis/push-provisioning/android/branding-guidelines).
The [sample
app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/app/src/main/res/layout/card_picker_item.xml#L19-L25)
provides an example of the button adhering to branding guidelines.

#### Caution

As
[recommended](https://developers.google.com/pay/issuers/apis/push-provisioning/android/faq#implementation_questions)
by Google, don’t require your users to install the Google Pay app, or check its
existence programmatically. The app is only a frontend and you don’t need it for
Google Pay to work. Users can manage their cards from within their Google
settings in the “Settings” app.

#### Caution

Google requires that the **Add to Google Pay** button only displays when a card
doesn’t already exist on the user’s device, and that users with cards pending
verification complete the final guided activation process. Use Google’s [list of
checkpoints](https://developers.google.com/pay/issuers/apis/push-provisioning/android/test-cases)
to help you verify that your implementation is correct.

To check the status of your users’ cards, use
[listTokens()](https://developers.google.com/pay/issuers/apis/push-provisioning/android/reading-wallet#listtokens)
to retrieve a list of all of your cards already present on the device. Compare
the value of `getFpanLastFour()` on each returned object to Stripe’s
[last4](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-last4))
property of the [Issued Card
object](https://docs.stripe.com/api/issuing/cards/object) for the card you want
to add. Discard all non-matching objects from the response list.

- If the resulting list is empty, it means that the card you intend to add isn’t
present on the device yet. You can proceed with displaying the button as
described below.
- If the resulting list contains a `TokenInfo` object, check its
[TokenState](https://developers.google.com/pay/issuers/apis/push-provisioning/android/enumerated-values#token_status)
by invoking `getTokenState()`.- If the status is
`TOKEN_STATE_NEEDS_IDENTITY_VERIFICATION`, your user has already attempted to
manually add the given card to their device. Display the **Add to Google Pay**
button, but help them to recover from this situation by wiring the
`onActivityResult` listener to the `tokenize()` method as [outlined in Google’s
documentation](https://developers.google.com/pay/issuers/apis/push-provisioning/android/wallet-operations#resolving_yellow_path).
- If the status is anything else, the card is already present on the device.
**Do not display a Google Pay button.**

Make sure to provide your application ID to Stripe before starting internal
testing. Setup can take more than a week, and the consequences of an incomplete
setup include receiving inconsistent responses to these two methods. The result
of `listTokens()` **only contains cards added after** Stripe completes the
setup.

- When a user taps the button, launch Stripe’s `PushProvisioningActivity` using
the `PushProvisioningActivityStarter`.

```
new PushProvisioningActivityStarter(
this, // The Activity or Fragment you are initiating the push provisioning from
 new PushProvisioningActivityStarter.Args(
 "Stripe Card", // The name that will appear on the push provisioning UI
 ephemeralKeyProvider, // Your instance of EphemeralKeyProvider
 false // If you want to enable logs or not
)).startForResult();
```

For more context, see how the [sample
app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/app/src/main/java/com/stripe/android/pushprovisioning/MainActivity.kt#L119-L124)
launches `PushProvisioningActivity`.

This prepares the push provisioning and launches the UI to add the card to the
wallet. Implement the callback in your `onActivityResult`.

```
protected void onActivityResult(int requestCode, int resultCode, @Nullable
Intent data) {
 if (requestCode == PushProvisioningActivityStarter.REQUEST_CODE) {
 if (resultCode == PushProvisioningActivity.RESULT_OK) {
PushProvisioningActivityStarter.Result success =
PushProvisioningActivityStarter.Result.fromIntent(data);
 } else if (resultCode == PushProvisioningActivity.RESULT_ERROR) {
PushProvisioningActivityStarter.Error error =
PushProvisioningActivityStarter.Error.fromIntent(data);
 }
 }
}
```

For more context, see how the [sample
app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/app/src/main/java/com/stripe/android/pushprovisioning/MainActivity.kt#L132-L167)
implements `onActivityResult`.

If the provisioning was successful, you’ll receive a
`PushProvisioningActivityStarter.Result` containing a `cardTokenId` which is
Google’s ID for the card in the active wallet. You can use the rest of the
wallet functions with this ID.

If the provisioning encountered an error, a
`PushProvisioningActivityStarter.Error` will be returned with a `code` and a
`message`. The `message` is a developer-friendly text explaining the error. The
`code` can have the following values:

EnumMeaningUSER_CANCELEDThe user canceled the provisioning.CARD_CANCELEDThe card
has been canceled or is lost or stolen and cannot be
provisioned.EPHEMERAL_KEY_ERRORThere was an error retrieving the ephemeral
key.TAP_AND_PAY_UNAVAILABLEThe TapAndPay library can’t be used, most likely
because the app isn’t added to an allowlist.NO_STABLE_HARDWARE_IDThis can happen
in the development emulator. The app can’t retrieve the stable hardware
ID.NO_ACTIVE_WALLET_FOUNDNo active wallet available. Note that emulators
generally don’t have Google Pay.PUSH_PROVISIONING_ENCRYPTED_PAYLOAD_ERRORThere
was an error contacting Stripe’s servers to get the encrypted payload for push
provisioning.UNKNOWN_ERRORAn unexpected error occurred. The `message` will have
additional information.[Update your
backendServer-side](https://docs.stripe.com/issuing/cards/digital-wallets#update-your-backend)
The push provisioning implementation exposes methods that expect you to
communicate with your own backend to create a Stripe Ephemeral Key and return a
JSON of it to your app. This key is a short-lived API credential that you can
use to retrieve the encrypted card details for a single instance of a card
object.

To make sure that the object returned by the Stripe API is compatible with the
version of the iOS or Android SDK you’re using, the Stripe SDK lets you know
what API version it prefers. You must explicitly pass this API version to our
API when creating the key.

```
curl https://api.stripe.com/v1/ephemeral_keys \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "issuing_card"="{{ISSUING_CARD_ID}}" \
 -H "Stripe-Version: {{API_VERSION}}"
```

```
{
 "id": "ephkey_1G4V6eEEs6YsaMZ2P1diLWdj",
 "object": "ephemeral_key",
 "associated_objects": [
 {
 "id": "ic_1GWQp6EESaYspYZ9uSEZOcq9",
 "type": "issuing.card"
 }
 ],
 "created": 1586556828,
 "expires": 1586560428,
 "livemode": false,
"secret":
"ek_test_YWNjdF8xRmdlTjZFRHelWWxwWVo5LEtLWFk0amJ2N0JOa0htU1JzEZkd2RpYkpJdnM_00z2ftxCGG"
}
```

For more context, see how the [sample
backend](https://github.com/stripe-samples/push-provisioning-samples/blob/main/server/ruby/README.md)
creates a [Stripe Ephemeral
Key](https://github.com/stripe-samples/push-provisioning-samples/blob/main/server/ruby/server.rb#L68-L88).

[Testing](https://docs.stripe.com/issuing/cards/digital-wallets#testapp)
All testing must be done in live mode, with live Issuing cards, and on physical
devices.

To build the sample app, follow the steps in the
[readme](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/README.md).
You don’t need to build the app to follow the instructions above.

## Links

- [Token Management](https://docs.stripe.com/issuing/controls/token-management)
- [virtual cards](https://docs.stripe.com/issuing/cards/virtual)
- [physical cards](https://docs.stripe.com/issuing/cards/physical)
- [digital wallets
settings](https://dashboard.stripe.com/settings/issuing/digital-wallets)
- [contact Stripe](https://stripe.com/contact/sales)
- [Request access to Google
Pay](https://developers.google.com/pay/issuers/requesting-access?api=true)
- [TapAndPay private
SDK](https://developers.google.com/pay/issuers/apis/push-provisioning/android/releases)
- [Request access to the push provisioning
API](https://support.google.com/faqs/contact/pp_api_allowlist)
- [application ID](https://developer.android.com/studio/build/application-id)
-
[documentation](https://developers.google.com/pay/issuers/apis/push-provisioning/android/allowlist)
- [private
SDK](https://developers.google.com/pay/issuers/apis/push-provisioning/android/setup)
- [sample
app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/app/build.gradle.kts#L111-L118)
- [Parcelable](https://developer.android.com/reference/android/os/Parcelable)
- [sample
app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/app/src/main/java/com/stripe/android/pushprovisioning/network/BackendPushProvisioningEphemeralKeyProvider.kt#L20-L43)
- [according to Google’s
specifications](https://developers.google.com/pay/issuers/apis/push-provisioning/android/branding-guidelines)
- [sample
app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/app/src/main/res/layout/card_picker_item.xml#L19-L25)
-
[recommended](https://developers.google.com/pay/issuers/apis/push-provisioning/android/faq#implementation_questions)
- [list of
checkpoints](https://developers.google.com/pay/issuers/apis/push-provisioning/android/test-cases)
-
[listTokens()](https://developers.google.com/pay/issuers/apis/push-provisioning/android/reading-wallet#listtokens)
-
[last4](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-last4)
- [Issued Card object](https://docs.stripe.com/api/issuing/cards/object)
-
[TokenState](https://developers.google.com/pay/issuers/apis/push-provisioning/android/enumerated-values#token_status)
- [outlined in Google’s
documentation](https://developers.google.com/pay/issuers/apis/push-provisioning/android/wallet-operations#resolving_yellow_path)
- [sample
app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/app/src/main/java/com/stripe/android/pushprovisioning/MainActivity.kt#L119-L124)
- [sample
app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/app/src/main/java/com/stripe/android/pushprovisioning/MainActivity.kt#L132-L167)
- [sample
backend](https://github.com/stripe-samples/push-provisioning-samples/blob/main/server/ruby/README.md)
- [Stripe Ephemeral
Key](https://github.com/stripe-samples/push-provisioning-samples/blob/main/server/ruby/server.rb#L68-L88)
-
[readme](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/android/README.md)