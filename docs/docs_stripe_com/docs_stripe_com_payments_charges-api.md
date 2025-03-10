# Card payments on the Charges APILegacy

## Learn how to charge, save, and authenticate cards with Stripe's legacy APIs.

#### Legacy API

The content of this section refers to a Legacy feature. Use the [Payment Intents
API](https://docs.stripe.com/payments/accept-a-payment) instead.

The Charges API doesn’t support the following features, many of which are
required for credit card compliance:

- Merchants in India
- [Bank requests for card
authentication](https://docs.stripe.com/payments/cards/overview)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)

The [Charges](https://docs.stripe.com/api/charges) and
[Tokens](https://docs.stripe.com/api/tokens) APIs are legacy APIs used in older
Stripe integrations to accept debit and credit card payments. Use
[PaymentIntents](https://docs.stripe.com/payments/accept-a-payment) for new
integrations.

The Charges API limits your ability to take advantage of Stripe features. To get
the latest features, use [Stripe
Checkout](https://docs.stripe.com/payments/checkout) or [migrate to the Payment
Intents API](https://docs.stripe.com/payments/payment-intents/migration).

## Payment flow

In most cases, the PaymentIntents API offers more flexibility and integration
options.

Charges APIPayment Intents API- Collect the customer’s payment information in
the browser with Elements.
- Tokenize the payment information with Stripe.js.
- Perform a request to send the token to your server.
- Use the token to create a charge on your server with the desired amount and
currency.
- Fulfill the customer’s order if payment is successful.
- Create a PaymentIntent on your server with the desired amount and currency.
- Send the PaymentIntent’s client secret to the client side.
- Collect the customer’s payment information in the browser with Elements.
- Use Stripe.js or the mobile SDKs to handle [3D
Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
and complete the payment on the client.
- Use webhooks to fulfill the customer’s order if the payment is successful.

## Refunds

To refund a payment via the API, create a
[Refund](https://docs.stripe.com/api#create_refund) and provide the ID of the
charge to be refunded.

```
curl https://api.stripe.com/v1/refunds \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d charge={{CHARGE_ID}}
```

To refund part of a payment, provide an `amount` parameter, as an integer in
cents (or the charge currency’s smallest currency unit).

```
curl https://api.stripe.com/v1/refunds \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d charge={{CHARGE_ID}} \
 -d amount=1000
```

## Apple Pay

When your customer approves the payment, your app receives a
[PKPayment](https://developer.apple.com/documentation/passkit/pkpayment)
instance containing their encrypted card details by implementing the
[PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate)
methods.

- Use the
[createTokenWithPayment](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPAPIClient.html#/c:@CM@StripePayments@StripeCore@objc(cs)STPAPIClient(im)createTokenWithPayment:completion:)
SDK method to turn the `PKPayment` into a Stripe `Token`
- Use this `Token` to [create a
charge](https://docs.stripe.com/payments/accept-a-payment-charges#ios-create-charge).

```
extension CheckoutViewController: PKPaymentAuthorizationViewControllerDelegate {

func paymentAuthorizationViewController(_ controller:
PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment,
handler: @escaping (PKPaymentAuthorizationResult) -> Void) {
 // Convert the PKPayment into a Token
 STPAPIClient.shared.createToken(withPayment: payment) { token, error in
 guard let token = token else {
 // Handle the error
 return
 }
 let tokenID = token.tokenId
 // Send the token identifier to your server to create a Charge...
// If the server responds successfully, set self.paymentSucceeded to YES
 }
 }

func paymentAuthorizationViewControllerDidFinish(_ controller:
PKPaymentAuthorizationViewController) {
```

See all 26 lines
## Dynamic statement descriptor

By default, your Stripe account’s [statement
descriptor](https://docs.stripe.com/get-started/account/activate#public-business-information)
appears on customer statements whenever you charge their card. Additionally, you
can set the statement descriptor dynamically on every charge request with the
`statement_descriptor` argument on the Charge object.

```
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=999 \
 -d "currency"="usd" \
 -d "description"="Example charge" \
 -d "source"="tok_visa" \
 -d "statement_descriptor"="Custom descriptor"
```

Statement descriptors are limited to 22 characters, can’t use the special
characters `<`, `>`, `'`, `"`, or `*`, and must not consist solely of numbers.

When setting the statement descriptor dynamically on credit and debit card
charges, the dynamic portion is appended to the settlement merchant’s statement
descriptor (separated by an `*` and an empty space). For example, a statement
descriptor for a business, named FreeCookies, that includes the kind of cookie
purchased might look like `FREECOOKIES* SUGAR`.

The `*` and empty space count towards the 22 character limit and Stripe
automatically allots 10 characters for the dynamic statement descriptor. This
means that the settlement merchant’s descriptor might be truncated if it’s
longer than 10 characters (assuming the dynamic statement descriptor is also
greater than 10 characters). If the dynamic statement descriptor is also greater
than 10 characters, both descriptors are truncated at 10 characters.

If you’re having issues with the character limits, you can set a [shortened
descriptor](https://dashboard.stripe.com/settings/public) in the Stripe
Dashboard to shorten the settlement merchant’s descriptor. This allows more room
for the dynamic statement descriptor. The shortened descriptor:

- Replaces the settlement merchant’s statement descriptor when using dynamic
descriptors.
- Can be between 2 and 10 characters.

#### Note

If your account’s statement descriptor is longer than 10 characters, set a
[shortened descriptor](https://dashboard.stripe.com/settings/public) in the
Dashboard or use `statement_descriptor_prefix`. This prevents your statement
descriptor from being truncated in unpredictable ways.

If you’re not sure what the statement descriptors look like when they’re
combined, you can check them in the [Stripe
Dashboard](https://dashboard.stripe.com/settings/public).

## Storing information in metadata

Stripe supports adding [metadata](https://docs.stripe.com/api#metadata) to the
most common requests you make, such as processing charges. Metadata isn’t shown
to customers or factored into whether or not a charge is declined or blocked by
our fraud prevention system.

Through metadata, you can associate other information—meaningful to you—with
Stripe activity. Any metadata you include is viewable in the Dashboard (for
example, when looking at the page for an individual charge), and is also
available in common reports and exports. As an example, your store’s order ID
can be attached to the charge used to pay for that order. Doing so allows you,
your accountant, or your finance team to easily reconcile charges in Stripe to
orders in your system.

If you are using [Radar](https://docs.stripe.com/radar), consider passing any
additional customer information and order information as metadata. By doing so,
you can write [Radar rules using metadata
attributes](https://docs.stripe.com/radar/rules/reference#metadata-attributes)
and have more information about the payment available within the Dashboard which
can expedite your review process.

```
curl https://api.stripe.com/v1/charges \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "amount"=999 \
 -d "currency"="usd" \
 -d "description"="Example charge" \
 -d "source"="tok_visa" \
 -d "metadata[order_id]"=6735
```

#### Caution

Don’t store any sensitive information (personally identifiable information, card
details, and so on) as metadata or in the charge’s `description` parameter.

## Declines

If you want your integration to respond to payment failures automatically, you
can access a charge’s `outcome` in two ways.

- [Handle the API error](https://docs.stripe.com/api#error_handling) that’s
returned when a payment fails. For blocked and card issuer-declined payments,
the error includes the charge’s ID, which you can then use to
[retrieve](https://docs.stripe.com/api#retrieve_charge) the charge.
- Use [webhooks](https://docs.stripe.com/webhooks) to monitor status updates.
For example, the `charge.failed` event triggers when a payment is unsuccessful.

## Links

- [Payment Intents API](https://docs.stripe.com/payments/accept-a-payment)
- [Bank requests for card
authentication](https://docs.stripe.com/payments/cards/overview)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [Charges](https://docs.stripe.com/api/charges)
- [Tokens](https://docs.stripe.com/api/tokens)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [migrate to the Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration)
- [3D
Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
- [Refund](https://docs.stripe.com/api#create_refund)
- [PKPayment](https://developer.apple.com/documentation/passkit/pkpayment)
-
[PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate)
-
[createTokenWithPayment](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPAPIClient.html#/c:@CM@StripePayments@StripeCore@objc(cs)STPAPIClient(im)createTokenWithPayment:completion:)
- [create a
charge](https://docs.stripe.com/payments/accept-a-payment-charges#ios-create-charge)
- [statement
descriptor](https://docs.stripe.com/get-started/account/activate#public-business-information)
- [shortened descriptor](https://dashboard.stripe.com/settings/public)
- [metadata](https://docs.stripe.com/api#metadata)
- [Radar](https://docs.stripe.com/radar)
- [Radar rules using metadata
attributes](https://docs.stripe.com/radar/rules/reference#metadata-attributes)
- [Handle the API error](https://docs.stripe.com/api#error_handling)
- [retrieve](https://docs.stripe.com/api#retrieve_charge)
- [webhooks](https://docs.stripe.com/webhooks)