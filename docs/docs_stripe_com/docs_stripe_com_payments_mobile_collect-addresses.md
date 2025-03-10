# Collect physical addresses and phone numbers

## Learn how to collect addresses and phone number in your mobile app.

iOSAndroidReact Native
To collect complete addresses for billing or shipping, use the [Address
Element](https://docs.stripe.com/elements/address-element).

You can also use the Address Element to:

- Collect customer [phone
numbers](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet.addresselement/-address-launcher/-additional-fields-configuration/index.html)
- Enable
[autocomplete](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet.addresselement/-address-launcher/-configuration/index.html)
- Prefill billing information in the Payment Element by passing in a shipping
address

Stripe combines the collected address information and the payment method to
create a [PaymentIntent](https://docs.stripe.com/payments/payment-intents).

![Examples of a checkout process where a user selects the Add Shipping Address
option. They're then taken to a new screen to add their shipping address into a
form (they see auto-complete suggestions as they type in their
address).](https://b.stripecdn.com/docs-statics-srv/assets/android-overview.6061212dc737aa700b79242cb5f77782.png)

[Set up
StripeServer-sideClient-side](https://docs.stripe.com/payments/mobile/collect-addresses#set-up-stripe)
First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register).

The [React Native SDK](https://github.com/stripe/stripe-react-native) is open
source and fully documented. Internally, it uses the native
[iOS](https://github.com/stripe/stripe-ios) and
[Android](https://github.com/stripe/stripe-android) SDKs. To install Stripe’s
React Native SDK, run one of the following commands in your project’s directory
(depending on which package manager you use):

yarnnpm
```
yarn add @stripe/stripe-react-native
```

Next, install some other necessary dependencies:

- For iOS, navigate to the **ios** directory and run `pod install` to make sure
that you also install the required native dependencies.
- For Android, you don’t need to install any more dependencies.

### Stripe initialization

To initialize Stripe in your React Native app, either wrap your payment screen
with the `StripeProvider` component, or use the `initStripe` initialization
method. Only the API [publishable
key](https://docs.stripe.com/keys#obtain-api-keys) in `publishableKey` is
required. The following example shows how to initialize Stripe using the
`StripeProvider` component.

```
import { StripeProvider } from '@stripe/stripe-react-native';

function App() {
 return (
 <StripeProvider
 publishableKey="pk_test_TYooMQauvdEDq54NiTphI7jx"
 >
 // Your app code here
 </StripeProvider>
 );
}
```

#### Note

Use your API keys for [test mode](https://docs.stripe.com/keys#obtain-api-keys)
while you test and develop, and your [live
mode](https://docs.stripe.com/keys#test-live-modes) keys when you publish your
app.

[Set up address autocomplete
suggestions](https://docs.stripe.com/payments/mobile/collect-addresses#set-up-address-autocomplete)
Autocomplete is enabled by default on iOS, but to enable autocomplete
suggestions on Android, you need to include the [Google Places
SDK](https://developers.google.com/maps/documentation/places/android-sdk/overview)
dependency in your app’s `build.gradle`:

```
dependencies {
 implementation 'com.google.android.libraries.places:places:2.6.0'
}
```

Address autocomplete suggestions requires a Google Places API key. Follow the
[Google Places SDK setup
guide](https://developers.google.com/maps/documentation/places/android-sdk/cloud-setup)
to generate your API key.

[Configure the Address
Element](https://docs.stripe.com/payments/mobile/collect-addresses#configure-address-element)
You can configure the Address Element with details such as displaying default
values, setting allowed countries, customizing the appearance, and so on. See
the [list of available
options](https://github.com/stripe/stripe-react-native/blob/master/src/components/AddressSheet.tsx#L19-L51)
for more information.

```
<AddressSheet
 appearance={{
 colors: {
 primary: '#F8F8F2',
 background: '#272822'
 }
 }}
 defaultValues={{
 phone: '111-222-3333',
 address: {
 country: 'United States',
 city: 'San Francisco',
 },
 }}
 additionalFields={{
 phoneNumber: 'required',
 }}
 allowedCountries={['US', 'CA', 'GB']}
 primaryButtonTitle={'Use this address'}
 sheetTitle={'Shipping Address'}
 googlePlacesApiKey={'(optional) YOUR KEY HERE'}
/>
```

[Present the Address Element and retrieve
details](https://docs.stripe.com/payments/mobile/collect-addresses#present-address-element)
Retrieve the address details by setting the `visible` property to `true`, and
adding callback methods for the `onSubmit` and `onError` properties:

```
<AddressSheet
 visible={true}
 onSubmit={async (addressDetails) => {
 // Make sure to set `visible` back to false to dismiss the address element.
 setAddressSheetVisible(false);

 // Handle result and update your UI
 }}
 onError={(error) => {
 if (error.code === AddressSheetError.Failed) {
 Alert.alert('There was an error.', 'Check the logs for details.');
 console.log(err?.localizedMessage);
 }
 // Make sure to set `visible` back to false to dismiss the address element.
 setAddressSheetVisible(false);
 }}
/>
```

[OptionalPrefill shipping addresses in the Payment
Element](https://docs.stripe.com/payments/mobile/collect-addresses#prefill-addresses)[OptionalCustomize
the
appearance](https://docs.stripe.com/payments/mobile/collect-addresses#customize-appearance)[OptionalSet
default billing
details](https://docs.stripe.com/payments/mobile/collect-addresses#set-default-billing-details)[OptionalCustomize
billing details
collection](https://docs.stripe.com/payments/mobile/collect-addresses#customize-billing-details-collection)

## Links

- [Address Element](https://docs.stripe.com/elements/address-element)
- [phone
numbers](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet.addresselement/-address-launcher/-additional-fields-configuration/index.html)
-
[autocomplete](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet.addresselement/-address-launcher/-configuration/index.html)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [Register now](https://dashboard.stripe.com/register)
- [React Native SDK](https://github.com/stripe/stripe-react-native)
- [iOS](https://github.com/stripe/stripe-ios)
- [Android](https://github.com/stripe/stripe-android)
- [publishable key](https://docs.stripe.com/keys#obtain-api-keys)
- [live mode](https://docs.stripe.com/keys#test-live-modes)
- [Google Places
SDK](https://developers.google.com/maps/documentation/places/android-sdk/overview)
- [Google Places SDK setup
guide](https://developers.google.com/maps/documentation/places/android-sdk/cloud-setup)
- [list of available
options](https://github.com/stripe/stripe-react-native/blob/master/src/components/AddressSheet.tsx#L19-L51)