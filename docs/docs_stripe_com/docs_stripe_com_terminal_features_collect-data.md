# Collect swiped or tapped dataPrivate preview

## Use Terminal for data collection with the reader hardware interfaces.

**Available in:**

- All supported countries for [BBPOS Chipper2X
BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt) and [Stripe
M2](https://docs.stripe.com/terminal/readers/stripe-m2) using [Android
SDK](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=android)
and [iOS
SDK](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=ios)
`3.7.0` and up
- All supported countries for [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700) and [BBPOS
WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e) on reader
software version `2.28.3.0` and up using [Android
SDK](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=android),
[Apps on
Devices](https://docs.stripe.com/terminal/features/apps-on-devices/overview),
and [iOS
SDK](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=ios)
`4.2.0` and up

Use the Terminal SDK to read non-PCI payment instruments, such as gift cards,
using the reader’s hardware interfaces like the magnetic stripe reader. This
feature isn’t available offline.

#### Private preview

Request access to the Collect data private preview by sending an email to
[terminal-collect-data@stripe.com](mailto:terminal-collect-data@stripe.com) with
the following information:

- Use case
- Terminal device and integration type
- Magstripe data format
- Provider, if using a third-party card provider

After swiping the card, the Terminal SDK provides a tokenized data object.
Securely retrieve the cleartext track data on your backend with the token.

The Terminal reader only reads and stores cleartext magstripe data that follows
these formats:

- The card data is available on track 2 only.
- The card data uses only the
[ISO/IEC-7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) track 2 start
sentinel `;` and end sentinel `?`, without the separator character.
- The card data consists only of numeric digits.

[Contact the Terminal team](mailto:terminal-collect-data@stripe.com) with your
card format and BIN ranges if your card numbers don’t match one of these
approved formats.

iOSAndroid[Collect
data](https://docs.stripe.com/terminal/features/collect-data#collect-data)
Use `Terminal.collectData()` to prompt for data collection from your point of
sale application. Specify the type of collected data you want to receive, such
as magstripe, in a configuration passed to the function. After a card is swiped,
the SDK returns a token representing the data, or an error if the swipe was
unsuccessful. Use this token in your integration to refer to the data.

```
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {
 func readGiftCard() throws {
let config = try
CollectDataConfigurationBuilder().setCollectDataType(.magstripe).build()
self.cancelable = Terminal.shared.collectData(config) { collectedData,
collectError in
 if let error = collectError {
 // Handle read errors
 print("Collect data failed: \(error)")
 } else if let data = collectedData, let stripeId = data.stripeId {
 print("Received collected data token: \(stripeId)")
 }
 }
 }
}
```

[Fetch collected
data](https://docs.stripe.com/terminal/features/collect-data#fetch-collected-data)
When you need to perform operations such as redeeming a gift card, [fetch the
cleartext data](https://docs.stripe.com/api/terminal/reader-collected_data) from
your backend using the collected data token. The collected data is stored on
Stripe’s servers for 24 hours.

```
curl https://api.stripe.com/v1/terminal/reader_collected_data/tmrcd_xxxxxxxx \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

#### Note

Stripe doesn’t perform and isn’t responsible for the authentication of collected
data or the authorization of transactions using collected data. Stripe isn’t
liable for any illegal conduct or fraud by any third party associated with the
collected data.

## Links

- [BBPOS Chipper2X
BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt)
- [Stripe M2](https://docs.stripe.com/terminal/readers/stripe-m2)
- [Android
SDK](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=android)
- [iOS
SDK](https://docs.stripe.com/terminal/payments/setup-integration?terminal-sdk-platform=ios)
- [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700)
- [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e)
- [Apps on
Devices](https://docs.stripe.com/terminal/features/apps-on-devices/overview)
- [ISO/IEC-7813](https://en.wikipedia.org/wiki/ISO/IEC_7813)
- [collectData
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)collectData:completion:)
- [fetch the cleartext
data](https://docs.stripe.com/api/terminal/reader-collected_data)