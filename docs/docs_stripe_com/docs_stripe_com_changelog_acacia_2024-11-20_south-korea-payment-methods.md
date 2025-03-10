# Use configurable capture methods and set up future usage for South Korean payment methods

## What’s new

The following South Korean payment methods now support setting the
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
to `manual`, which overrides the configuration for the
[Session](https://docs.stripe.com/api/checkout/sessions):

- [South Korean
cards](https://docs.stripe.com/payments/kr-card/accept-a-payment)
- [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment)
- [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment)
- [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment)
- [PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment)

The following South Korean payment methods now support
[setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage),
which you set when you create a Session:

- [South Korean
cards](https://docs.stripe.com/payments/kr-card/accept-a-payment)
- [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment)
- [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment)

## Impact

You can now override the default automatic capture of a payment transaction
using South Korean payment methods when you create a Checkout Session. Set
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
to `manual` on the `payment_method_options` parameter for the specific payment
method to [place a hold on the payment
method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method).

- [South Korean
cards](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-kr_card)
- [Naver
Pay](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-naver_pay)
- [Kakao
Pay](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-kakao_pay)
- [Samsung
Pay](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-samsung_pay)
-
[PAYCO](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-payco)

You can now specify whether to [save South Korean payment method
details](https://docs.stripe.com/payments/save-during-payment) during payment
when you [create a Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create). For example, set
[setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage)
to `off_session` in the `payment_method_options` parameter for the specific
payment method to enable charging the customer at a later time, such as for a
cancellation fee.

- [South Korean
cards](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-kr_card)
- [Naver
Pay](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-naver_pay)
- [Kakao
Pay](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-kakao_pay)

## Changes

REST APIRubyPythonPHPJavaNodeGo.NETParameterChangeResources or
endpointscapture_methodAdded[Checkout.Session#create.payment_method_options.kakao_pay](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-kakao_pay)[Checkout.Session#create.payment_method_options.kr_card](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-kr_card)[Checkout.Session#create.payment_method_options.naver_pay](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-naver_pay)
+ 2 more
## Upgrade

- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
in Workbench.
- If you use an SDK, upgrade to the corresponding SDK version for this API
version.- If you don’t use an SDK, update your [API
requests](https://docs.stripe.com/api/versioning) to include `Stripe-Version:
2024-11-20.acacia`
- Upgrade the API version used for [webhook
endpoints](https://docs.stripe.com/webhooks/versioning).
- [Test your integration](https://docs.stripe.com/testing) against the new
version.
- If you use Connect, [test your Connect
integration](https://docs.stripe.com/connect/testing).
- In Workbench, [perform the
upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade). You can [roll
back the version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades).

## Related changes

- [Adds network decline code field for Swish and BLIK
refunds](https://docs.stripe.com/changelog/acacia/2024-11-20/refunds-network-decline-code)
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefixes in Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/checkout-sessions-sepa-debit-bacs-debit-mandate-options)
- [Specifying an originating payment method for Inbound Transfers is now
optional](https://docs.stripe.com/changelog/acacia/2024-11-20/inbound-transfers-optional-pm)

## Links

-
[capture_method](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method)
- [Session](https://docs.stripe.com/api/checkout/sessions)
- [South Korean
cards](https://docs.stripe.com/payments/kr-card/accept-a-payment)
- [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment)
- [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment)
- [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment)
- [PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment)
-
[setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage)
- [place a hold on the payment
method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [South Korean
cards](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-kr_card)
- [Naver
Pay](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-naver_pay)
- [Kakao
Pay](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-kakao_pay)
- [Samsung
Pay](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-samsung_pay)
-
[PAYCO](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-payment_method_options-payco)
- [save South Korean payment method
details](https://docs.stripe.com/payments/save-during-payment)
- [create a Checkout
Session](https://docs.stripe.com/api/checkout/sessions/create)
- [View your current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
- [API requests](https://docs.stripe.com/api/versioning)
- [webhook endpoints](https://docs.stripe.com/webhooks/versioning)
- [Test your integration](https://docs.stripe.com/testing)
- [test your Connect integration](https://docs.stripe.com/connect/testing)
- [perform the upgrade](https://docs.stripe.com/upgrades#perform-the-upgrade)
- [roll back the
version](https://docs.stripe.com/upgrades#roll-back-your-api-version)
- [Stripe API upgrades](https://docs.stripe.com/upgrades)
- [Adds network decline code field for Swish and BLIK
refunds](https://docs.stripe.com/changelog/acacia/2024-11-20/refunds-network-decline-code)
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefixes in Checkout
Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/checkout-sessions-sepa-debit-bacs-debit-mandate-options)
- [Specifying an originating payment method for Inbound Transfers is now
optional](https://docs.stripe.com/changelog/acacia/2024-11-20/inbound-transfers-optional-pm)