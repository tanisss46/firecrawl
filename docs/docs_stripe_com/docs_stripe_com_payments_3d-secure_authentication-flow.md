# Authenticate with 3D Secure

## Integrate 3D Secure (3DS) into your checkout flow.

#### Caution

Major card brands no longer support 3D Secure 1. If your implementation uses 3D
Secure 1, update it to use the [Payment
Intents](https://docs.stripe.com/api/payment_intents) and [Setup
Intents](https://docs.stripe.com/api/setup_intents) APIs. Using those APIs:

- Supports [3D Secure 2 (3DS2)](https://stripe.com/guides/3d-secure-2).
- Takes advantage of [Dynamic 3D
Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar).
- Complies with European [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
regulations.

You can integrate 3D Secure (3DS) authentication into your checkout flow on
multiple platforms, including Web, iOS, Android, and React Native. This
integration runs [3D Secure 2 (3DS2)](https://stripe.com/guides/3d-secure-2)
when supported by the customer’s bank and falls back to 3D Secure 1 otherwise.
To use Stripe’s 3DS service with other processors, [contact
support](https://support.stripe.com/contact).

WebiOSAndroid

![Checkout
screen](https://b.stripecdn.com/docs-statics-srv/assets/auth-flow-step01-confirm.399f5a4abbd7f303861689d186b79557.png)

The customer enters their payment information.

![Initiate
authentication](https://b.stripecdn.com/docs-statics-srv/assets/auth-flow-step02-processing.3877946d74743878ec86cec56dd69085.png)

The SDK presents a loading screen while the customer’s bank checks whether
authentication is required.

![Challenge flow
screen](https://b.stripecdn.com/docs-statics-srv/assets/auth-flow-step03-otp.f42397e1ce4ec5975e05f1bada72d195.png)

If required by their bank, the SDK authenticates the customer.

## Control the 3DS flow

Stripe triggers 3DS automatically if required by a regulatory mandate such as
[Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) or
requested by an issuer with the [soft
decline](https://docs.stripe.com/declines/codes) code `authentication_required`.

You can also [use Radar
rules](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
or [the
API](https://docs.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds)
to control when to prompt users to complete 3DS authentication, making a
determination for each user based on the desired parameters. However, not all
transactions support 3DS, for example wallets or off-session payments.

When a payment triggers 3DS, Stripe requires the user to perform authentication
to complete the payment if 3DS authentication is available for a card. Depending
on what frontend you use, this might require you to [display the 3DS
Flow](https://docs.stripe.com/payments/3d-secure/authentication-flow#when-to-use-3d-secure).

In a typical Payment Intent API flow that triggers 3DS:

- The user enters their payment information, which confirms a PaymentIntent,
SetupIntent, or attaches a PaymentMethod to a Customer.
- Stripe assesses if the transaction supports and requires 3DS based on
regulatory mandates, Radar rules, manual API requests, issuer soft declines, and
other criteria.
- If 3DS is:- **Not required**: For example, because of an
[exemption](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication),
Stripe attempts the charge. The PaymentIntent transitions to a status of
`processing`. If requested by the issuer with a [soft
decline](https://docs.stripe.com/declines/codes), we automatically reattempt and
continue as if required.
- **Not supported**: The PaymentIntent transitions to a status of
`requires_payment_method`. Depending on the reason 3DS was triggered it might be
permissible to continue to the authorization step for the charge. In that case,
the PaymentIntent transitions to a status of `processing`.
- **Required**: Stripe starts the 3DS authentication flow by contacting the card
issuer’s 3D Secure Access Control Server (ACS) and starting the 3DS flow.
- When Stripe receives 3DS flow information from the issuer, we attempt
authentication. The PaymentIntent transitions to a status of `requires_action`:-
See below for how to [display the required 3DS
action](https://docs.stripe.com/payments/3d-secure/authentication-flow#when-to-use-3d-secure).
Issuers might request different 3DS flow action types, which might not always
result in visibly displaying a 3DS challenge (for example, a frictionless flow).
- If the issuer doesn’t support 3DS at all or has an outage, Stripe might
attempt to complete the payment without authentication if permissible.
- Data for 3DS authentication requests is typically provided by the customer at
the time of the transaction. To reduce friction and the possibility of failed
authentication, we might complete these requests with data we infer from other
sources such as data collected from your customer during the payment flow,
records related to your customer’s past transactions with you, or relevant
information available from the customer’s card or issuers.
- If Stripe already has access to all the required 3DS data elements, our
optimized 3DS server might attempt to complete the authentication request for
you while confirming the PaymentIntent. This can result in the PaymentIntent
directly transitioning to a status of `processing` if the 3DS flow succeeds, or
to a status of `requires_action` if additional steps or data elements are
required to complete the 3DS flow.
- Depending on the 3DS authentication result:- **Authenticated**: Stripe
attempts the charge and the PaymentIntent transitions to a status of
`processing`.
- **Failure**: The PaymentIntent transitions to a status of
`requires_payment_method`, indicating that you need to try a different payment
method, or you can retry 3DS by reconfirming.
- **Other scenarios**: Depending on the reason the payment triggered 3DS, it
might be permissible to continue authorization for the charge in [edge
cases](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure-result).
For example, a result of `attempt_acknowledged` leads to a charge and the
PaymentIntent transitions to a status of `processing`.- An exception is when
creating [Indian e-mandates for recurring
payments](https://docs.stripe.com/india-recurring-payments). Anything but an
`authenticated` result is treated as failure.
- The PaymentIntent transitions to one of the following statuses, depending on
the outcome of the payment: `succeeded`, `requires_capture`, or
`requires_payment_method`.

To track whether 3DS was supported and attempted on a card payment, read the
[three_d_secure](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure)
property on the card information in the Charge’s `payment_method_details`.
Stripe populates the `three_d_secure` property when the customer attempts to
authenticate the card—`three_d_secure.result` indicates the authentication
outcome.

### Use Radar rules in the Dashboard

Stripe provides [default
Radar](https://docs.stripe.com/radar/rules#request-3d-secure) rules to
dynamically request 3DS when creating or confirming a
[PaymentIntent](https://docs.stripe.com/api/payment_intents) or
[SetupIntent](https://docs.stripe.com/api/setup_intents). You can configure
these rules in your
[Dashboard](https://dashboard.stripe.com/settings/radar/rules).

If you have [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams), you
can add [custom 3DS
rules](https://docs.stripe.com/radar/rules#request-3d-secure).

### Manually request 3DS with the API

The default method to trigger 3DS is [using Radar to dynamically request 3D
Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
based on risk level and other requirements. Triggering 3DS manually is for
advanced users integrating Stripe with their own fraud engine.

To trigger 3DS manually, set
`payment_method_options[card][request_three_d_secure]` to `any` or `challenge`
depending on what you want to optimize for when either creating or confirming a
[PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-card-request_three_d_secure)
or
[SetupIntent](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-card-request_three_d_secure),
or creating a [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card-request_three_d_secure).
This process is the same for one-time payments or when setting up a payment
method for future payments. When you provide this parameter, Stripe attempts to
perform 3DS and overrides any [dynamic 3D Secure Radar
rules](https://docs.stripe.com/radar/rules) on the PaymentIntent, SetupIntent,
or Checkout Session.

Payment Intents APISetup Intents APICheckout Session API
```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_options[card][request_three_d_secure]"=any
```

When to provide this parameter depends on when your fraud engine detects risk.
For example, if your fraud engine only inspects card details, you know whether
to request 3DS before you create the PaymentIntent or SetupIntent. If your fraud
engine inspects both card and transaction details, provide the parameter during
confirmation—when you have more information. Then pass the resulting
PaymentIntent or SetupIntent to your client to complete the process.

Explore the `request_three_d_secure` parameter’s usage for each case in the API
reference:

- [Create a
PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-card-request_three_d_secure)
- [Confirm a
PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-request_three_d_secure)
- [Create a
SetupIntent](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-card-request_three_d_secure)
- [Confirm a
SetupIntent](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_options-card-request_three_d_secure)
- [Create a Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card-request_three_d_secure)

Set `request_three_d_secure` to `any` to manually request 3DS with a preference
for a `frictionless` flow, increasing the likelihood of the authentication being
completed without any additional input from the customer.

Set `request_three_d_secure` to `challenge` to request 3DS with a preference for
a `challenge` flow, where the customer must respond to a prompt for active
authentication.

Stripe can’t guarantee your preference because the issuer determines the
ultimate authentication flow. You can find out what the ultimate authentication
flow was by inspecting the `authentication_flow` on the `three_d_secure`
property of the
[Charge](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure-authentication_flow)
or
[SetupAttempt](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-payment_method_details-card-three_d_secure-authentication_flow).
To learn more about 3DS flows, read our
[guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication).

#### Caution

Stripe only requires your customer to perform authentication to complete the
payment successfully if 3DS authentication is available for a card. If it’s not
available for the given card or if an error occurred during the authentication
process, the payment proceeds normally.

Stripe’s SCA rules run automatically, regardless of whether or not you manually
request 3DS. Any 3DS prompts from you are additional and not required for SCA.

## Display the 3DS flow

WebiOSAndroidReact Native
#### Note

[PaymentSheet](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/index.html)
and
[PaymentSheet.FlowController](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-flow-controller/index.html)
automatically support 3DS authentication. If you’re using one of these classes,
this guide doesn’t apply.

[PaymentAuthConfig.Stripe3ds2Config](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-auth-config/-stripe3ds2-config/index.html)
contains the customizable items for 3DS authentication interactions.

The [timeout
property](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-auth-config/-stripe3ds2-config/-builder/set-timeout.html)
controls how long the 3DS authentication process runs before it times out. This
duration includes both network round trips and awaiting customer input. This
value must be at least 5 minutes to remain compliant with Strong
[Customer](https://docs.stripe.com/api/customers) Authentication regulation. A
value less than 5 minutes results in an error.

The
[uiCustomization](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-auth-config/-stripe3ds2-config/-builder/set-ui-customization.html)
property allows you to provide a `StripeUiCustomization` instance to control the
look of views presented by the Android SDK during 3DS authentication. Stripe
currently supports customization parameters for colors, fonts, text, borders on
app bars, labels, text fields, and buttons. For a full explanation of each
parameter, see the [Android SDK](https://stripe.dev/stripe-android/) reference.

The Stripe Android SDK collects [basic device
information](https://support.stripe.com/questions/3d-secure-2-device-information)
during 3DS2 authentication and sends it to the issuing bank for their risk
analysis.

```
final PaymentAuthConfig.Stripe3ds2UiCustomization uiCustomization =
 new PaymentAuthConfig.Stripe3ds2UiCustomization.Builder()
 .setLabelCustomization(
new PaymentAuthConfig.Stripe3ds2LabelCustomization.Builder()
 .setTextFontSize(12)
 .build())
 .build();
 PaymentAuthConfig.init(new PaymentAuthConfig.Builder()
 .set3ds2Config(new PaymentAuthConfig.Stripe3ds2Config.Builder()
 .setTimeout(5)
 .setUiCustomization(uiCustomization)
 .build())
 .build());
```

## Test the 3DS flow

Use a Stripe test card with any CVC, postal code, and future expiration date to
trigger 3DS authentication challenge flows while in a sandbox.

When you build an integration with your test API keys, the authentication
process displays a mock authentication page. On that page, you can either
authorize or cancel the payment. Authorizing the payment simulates successful
authentication and redirects you to the specified return URL. Clicking the
**Failure** button simulates an unsuccessful attempt at authentication.

WebiOSAndroidReact Native
When testing your custom Android integration, pick a test card to trigger a
specific challenge flow.

NumberChallenge flowDescription4000582600000094Out of Band3D Secure 2
authentication must be completed on all transactions. Triggers the challenge
flow with Out of Band UI.4000582600000045One Time Passcode3D Secure 2
authentication must be completed on all transactions. Triggers the challenge
flow with One Time Passcode UI.4000582600000102Single Select3D Secure 2
authentication must be completed on all transactions. Triggers the challenge
flow with single-select UI.4000582600000110Multi Select3D Secure 2
authentication must be completed on all transactions. Triggers the challenge
flow with multi-select UI.
All other Visa and Mastercard [test cards](https://docs.stripe.com/testing)
don’t require authentication from the customer’s card issuer.

You can write [custom Radar rules in a test
environment](https://dashboard.stripe.com/settings/radar/rules) to trigger
authentication on test cards. Learn more about [testing your Radar
rules](https://docs.stripe.com/radar/testing).

## Disputes and liability shift

The liability shift rule applies to payments successfully authenticated using
[3D Secure](https://docs.stripe.com/payments/3d-secure). In some cases,
liability shift applies with equivalent cryptograms, such as [Apple
Pay](https://docs.stripe.com/apple-pay) or [Google
Pay](https://docs.stripe.com/google-pay). If a cardholder
[disputes](https://docs.stripe.com/disputes) a 3DS payment as fraudulent, the
liability typically shifts from you to the card issuer.

If a card doesn’t support 3DS or an error occurs during the authentication
process, the payment proceeds normally. When this occurs, liability doesn’t
generally shift to the issuer, because a successful 3DS authentication hasn’t
taken place.

In practice, this means you typically won’t receive disputes marked as
fraudulent if the payment is covered by the liability shift rule, but you might
still receive an [Early Fraud
Warning](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings).
You might still receive a low percentage of fraudulent disputes, and we list a
few cases below where the liability shift rule might not apply.

You might receive a [dispute
inquiry](https://docs.stripe.com/disputes/how-disputes-work#inquiries) on a
successfully authenticated payment using 3DS. This type of dispute doesn’t
precipitate a chargeback because it’s only a request for information.

If you receive an inquiry for a 3D-Secure-authenticated charge, you *must*
respond. If you don’t, the cardholder’s bank can initiate a financial chargeback
known as a “no-reply” chargeback that could invalidate the liability shift. To
prevent no-reply chargebacks on 3DS charges, submit sufficient information about
the charge. Include information about what was ordered, how it was delivered,
and who it was delivered to (whether it was physical or electronic goods, or
services).

#### Note

If a customer disputes a payment for any other reason (for example, [product not
received](https://docs.stripe.com/disputes/categories)), then the standard
dispute process applies. Make informed decisions about your business management,
especially in handling and completely avoiding disputes.

Liability shift might also occur when the card network requires 3DS, but it
isn’t available for the card or issuer. This can happen if the issuer’s 3DS
server is down or if the issuer doesn’t support it, despite the card network
requiring support. During the payment process, the cardholder isn’t prompted to
complete 3DS authentication, because the card isn’t enrolled. Although the
cardholder didn’t complete 3DS authentication, liability can still shift to the
issuer.

Stripe returns the requested Electronic Commerce Indicator (ECI) in the
`electronic_commerce_indicator` of the [3DS authentication
outcome](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure).
This indicator can aid in determining whether a charge should adhere to the
liability shift rule. As 3DS occurs subsequent to the initial payment intent
response, you typically get this from a `charge.succeeded` event that’s sent to
one of your configured [webhook endpoints or other event
destinations](https://docs.stripe.com/event-destinations). A requested ECI might
be degraded in the issuer response, which we don’t reveal.

Sometimes payments that are successfully authenticated using 3DS don’t fall
under liability shift. This is rare and can happen, for example, if you have an
excessive level of fraud on your account and are enrolled in a [fraud monitoring
program](https://docs.stripe.com/disputes/monitoring-programs#vfmp). Certain
networks have also exempted some industries from liability shift. For example,
Visa doesn’t support liability shift for businesses engaging in wire transfer or
money orders, non-financial institutions offering foreign or non-fiat currency,
or stored-value card purchase or load.

In rare cases, liability shift might get downgraded post-authorization, or the
card networks’ dispute rejection system might fail to catch liability shift for
a transaction. In these cases, if you counter the dispute, Stripe automatically
adds the requested ECI and the [3DS authentication
outcome](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure-result)
for the payment to your evidence details, but we encourage you to include
additional details to improve your odds of winning the dispute.

### Custom Radar rules for 3DS and liability shift

If you have [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams), you
can [customize your
rules](https://docs.stripe.com/radar/rules#request-3d-secure) to control when to
request 3DS and how to handle each specific authentication outcome and liability
shift. Stripe’s [Strong Customer
Authentication](https://stripe.com/guides/strong-customer-authentication) (SCA)
rules run automatically and independently of custom Radar rules, and block
unauthenticated payments unless exempted.

## See also

- [Import 3DS
results](https://docs.stripe.com/payments/payment-intents/three-d-secure-import)
- [Authentication
analytics](https://docs.stripe.com/payments/analytics/authentication)

## Links

- [Payment Intents](https://docs.stripe.com/api/payment_intents)
- [Setup Intents](https://docs.stripe.com/api/setup_intents)
- [3D Secure 2 (3DS2)](https://stripe.com/guides/3d-secure-2)
- [Dynamic 3D
Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#three-ds-radar)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [contact support](https://support.stripe.com/contact)
- [soft decline](https://docs.stripe.com/declines/codes)
-
[exemption](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)
- [edge
cases](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure-result)
- [Indian e-mandates for recurring
payments](https://docs.stripe.com/india-recurring-payments)
-
[three_d_secure](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure)
- [default Radar](https://docs.stripe.com/radar/rules#request-3d-secure)
- [Dashboard](https://dashboard.stripe.com/settings/radar/rules)
- [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams)
-
[PaymentIntent](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-card-request_three_d_secure)
-
[SetupIntent](https://docs.stripe.com/api/setup_intents/create#create_setup_intent-payment_method_options-card-request_three_d_secure)
- [Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-card-request_three_d_secure)
- [dynamic 3D Secure Radar rules](https://docs.stripe.com/radar/rules)
- [Confirm a
PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-request_three_d_secure)
- [Confirm a
SetupIntent](https://docs.stripe.com/api/setup_intents/confirm#confirm_setup_intent-payment_method_options-card-request_three_d_secure)
-
[Charge](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-three_d_secure-authentication_flow)
-
[SetupAttempt](https://docs.stripe.com/api/setup_attempts/object#setup_attempt_object-payment_method_details-card-three_d_secure-authentication_flow)
- [guide](https://stripe.com/guides/3d-secure-2#frictionless-authentication)
-
[PaymentSheet](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/index.html)
-
[PaymentSheet.FlowController](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-flow-controller/index.html)
-
[PaymentAuthConfig.Stripe3ds2Config](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-auth-config/-stripe3ds2-config/index.html)
- [timeout
property](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-auth-config/-stripe3ds2-config/-builder/set-timeout.html)
- [Customer](https://docs.stripe.com/api/customers)
-
[uiCustomization](https://stripe.dev/stripe-android/payments-core/com.stripe.android/-payment-auth-config/-stripe3ds2-config/-builder/set-ui-customization.html)
- [Android SDK](https://stripe.dev/stripe-android/)
- [basic device
information](https://support.stripe.com/questions/3d-secure-2-device-information)
- [test cards](https://docs.stripe.com/testing)
- [testing your Radar rules](https://docs.stripe.com/radar/testing)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [Apple Pay](https://docs.stripe.com/apple-pay)
- [Google Pay](https://docs.stripe.com/google-pay)
- [disputes](https://docs.stripe.com/disputes)
- [Early Fraud
Warning](https://docs.stripe.com/disputes/how-disputes-work#early-fraud-warnings)
- [dispute
inquiry](https://docs.stripe.com/disputes/how-disputes-work#inquiries)
- [product not received](https://docs.stripe.com/disputes/categories)
- [webhook endpoints or other event
destinations](https://docs.stripe.com/event-destinations)
- [fraud monitoring
program](https://docs.stripe.com/disputes/monitoring-programs#vfmp)
- [Strong Customer
Authentication](https://stripe.com/guides/strong-customer-authentication)
- [Import 3DS
results](https://docs.stripe.com/payments/payment-intents/three-d-secure-import)
- [Authentication
analytics](https://docs.stripe.com/payments/analytics/authentication)