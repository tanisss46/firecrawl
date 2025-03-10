# Advanced fraud detection

## Learn about tools developers can use to maximize Stripe's ability to prevent fraudulent payments.

[Stripe.js](https://docs.stripe.com/js) is Stripe’s JavaScript library designed
to enable businesses to securely collect sensitive payment information from the
customer’s browser. The Stripe [iOS
SDK](https://docs.stripe.com/mobile/ios/basic) and [Android
SDK](https://docs.stripe.com/mobile/android/basic) are the mobile app
counterparts to Stripe.js.

Stripe.js and the mobile SDKs provide advanced fraud detection by looking at
signals about device characteristics and user activity that help distinguish
between legitimate and fraudulent transactions. These signals power Stripe’s
fraud prevention systems, such as [Radar](https://docs.stripe.com/radar). The
signals are transmitted to Stripe’s back end by periodically making requests to
the `m.stripe.com` endpoint.

Also, on each page where you load Stripe.js, it may load hCaptcha. hCaptcha is a
type of CAPTCHA that helps stop fraud and provides additional signals to Stripe
while being low friction for legitimate customers. To opt out of use of hCAPTCHA
integration, reach out to [Stripe
Support](https://support.stripe.com/contact/login).

Our goal is to maximize payments from legitimate customers while minimizing
fraud. Fraud can be one of the most challenging aspects of running an online
business. Even businesses that don’t typically see significant amounts of fraud
can see sudden, unexpected, and costly attacks. Stripe prevents more than 500
million USD in payment fraud for Stripe businesses every month. To do that, we
collect and analyze information that helps us identify bad actors and bots,
including both transactional data (such as amount, customer shipping address,
date, and so on) and advanced fraud detection signals (device and activity
signals).

The details of what we collect and how we use it are disclosed in our [privacy
policy](https://stripe.com/privacy) and [cookie
policy](https://stripe.com/cookies-policy/legal).

## Types of signals

### Device characteristics

Device characteristics are signals about a customer’s browser, screen, or
device. They help Stripe identify configurations consistent with anomalous
browsing behavior, as well as compare this behavior to similar patterns observed
across other businesses on Stripe’s network. Combinations of these parameters
that are rare or unlikely to reflect a real user’s computing environment can
expose fraudulent transactions.

### Activity indicators

Advanced fraud detection signals also include activity indicators from actual
shoppers that help us distinguish legitimate shoppers from fraudulent purchasers
and bots. For example, bots tend to move through a website and checkout form
much faster than a real person would; card numbers are also frequently
copy-pasted rather than typed. These signals include mouse activity indicators
and how long a user spends on different pages when shopping, which are both
predictive of bot-like behavior across the duration of a session.

Stripe gathers data about the contents of the page only if they correspond to
input fields in Stripe Elements. For example, Stripe might collect an email
address to prefill Link signup and login. If the Stripe Element doesn’t have an
email field, Stripe won’t collect that information from the contents of the
page. This information is never saved. Signals corresponding to user activity
are scoped to a single shopping session on a single site or app and aren’t
linked across different shopping sessions, sites, or apps.

## When signals are collected

The more activity Stripe’s fraud engines can observe, the better Stripe’s fraud
prevention will be. Stripe therefore encourages including Stripe.js on every
page of the shopping experience, not just the checkout page. This level of
Stripe.js coverage gives Stripe the richest possible set of such signals to
distinguish fraudulent purchasers from real customers.

If Stripe.js isn’t used at all, the business must take on the full
responsibility of [PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance),
and additional fraud risk.

The iOS and Android SDK collect advanced fraud detection signals for an app when
the SDK object is instantiated. The data is only transmitted to Stripe during a
tokenization request.

## Data privacy

This advanced fraud detection signal data is never used for advertising and
won’t be rented, sold, or given to advertisers, as outlined in our [privacy
policy](https://stripe.com/privacy). Stripe only uses this data for fraud
detection and security purposes, and retains it for as long as it’s useful for
the purposes of fraud detection and security.

Internally, this data is subject to strict access control policies enforced by
Stripe, and restricted to a small number of Stripe employees working on fraud
prevention and security.

## Disable advanced fraud detection

Stripe users can decide to disable the collection of advanced fraud detection
signals on their own websites and apps. Doing so increases their risk of fraud,
especially [card
testing](https://docs.stripe.com/disputes/prevention/fraud-types#card-testing).
Stripe will continue to collect fraud detection signals on Stripe domains, like
on [Stripe Checkout](https://docs.stripe.com/payments/checkout) payment pages.

Additionally, disabling advanced fraud detection doesn’t affect the collection
of events logged when a customer interacts with Stripe-managed fields in your
checkout page (we use these events to prevent fraud and make sure Stripe
Elements is working) nor basic device information collected during [3D Secure 2
authentication](https://support.stripe.com/questions/3d-secure-2-device-information)
(we’re required to send this information to the issuing bank for their risk
analysis).

### Stripe.js

To disable advanced fraud detection signals with
[Stripe.js](https://docs.stripe.com/js/including), set `advancedFraudSignals` as
a query parameter in the Stripe.js script tag, or update to the latest version
of the [Stripe.js module](https://github.com/stripe/stripe-js), use the `pure`
export, and call `setLoadParameters`:

```
<script src="https://js.stripe.com/v3/?advancedFraudSignals=false"></script>
```

### iOS SDK

To disable advanced fraud detection signals with the [Stripe iOS
SDK](https://github.com/stripe/stripe-ios), update to iOS SDK v19.1.1 or later.
When configuring the Stripe SDK, set the `advancedFraudSignalsEnabled` property:

```
StripeAPI.defaultPublishableKey = "pk_test_TYooMQauvdEDq54NiTphI7jx"
StripeAPI.setAdvancedFraudSignalsEnabled(false)
```

### Android SDK

To disable advanced fraud detection signals with the [Android
SDK](https://github.com/stripe/stripe-android), update to Android SDK v14.4.0 or
later. When configuring the Stripe SDK, set the `advancedFraudSignalsEnabled`
property before instantiating or accessing any Stripe SDK objects:

```
class MyApp : Application() {
 override fun onCreate() {
 super.onCreate()

 Stripe.advancedFraudSignalsEnabled = false

 PaymentConfiguration.init(
 applicationContext,
 "pk_test_TYooMQauvdEDq54NiTphI7jx"
 )
 }
}
```

## Links

- [Stripe.js](https://docs.stripe.com/js)
- [iOS SDK](https://docs.stripe.com/mobile/ios/basic)
- [Android SDK](https://docs.stripe.com/mobile/android/basic)
- [Radar](https://docs.stripe.com/radar)
- [Stripe Support](https://support.stripe.com/contact/login)
- [privacy policy](https://stripe.com/privacy)
- [cookie policy](https://stripe.com/cookies-policy/legal)
- [PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [card
testing](https://docs.stripe.com/disputes/prevention/fraud-types#card-testing)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [3D Secure 2
authentication](https://support.stripe.com/questions/3d-secure-2-device-information)
- [Stripe.js](https://docs.stripe.com/js/including)
- [Stripe.js module](https://github.com/stripe/stripe-js)
-
[https://js.stripe.com/v3/?advancedFraudSignals=false](https://js.stripe.com/v3/?advancedFraudSignals=false)
- [Stripe iOS SDK](https://github.com/stripe/stripe-ios)
- [Android SDK](https://github.com/stripe/stripe-android)