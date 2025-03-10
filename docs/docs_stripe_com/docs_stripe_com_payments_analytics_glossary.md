# GlossaryPublic preview

## Understand the terminology used in payments analytics.

Use this glossary to understand the common terms referenced in the [Payments
analytics](https://dashboard.stripe.com/acceptance) page in the Stripe
Dashboard.

#### Public preview

[Payments analytics](https://dashboard.stripe.com/acceptance) is in public
preview. If you want access to the public preview, [join the
waitlist](https://docs.stripe.com/payments/analytics).

## Acceptance analytics

The following are [Acceptance
analytics](https://docs.stripe.com/payments/analytics/acceptance) terms:

TermDefinitionAdaptive acceptanceA Stripe payment optimization feature that uses
machine-learning to selectively optimize transactions in real-time. Shows the
increase in payment success rate and payment volume from payments that [Adaptive
Acceptance](https://dashboard.stripe.com/settings/optimizations) successfully
retried after a decline.Authorized paymentsTotal number of card payments
approved by card issuers.Authorization ratePercentage of card payments approved
by card issuers, out of all attempted card payments. Excludes blocked payments
and payments that didn’t complete 3D Secure authentication.Authorized
volumeTotal amount of approved card payments. Defaults to your [settlement
currency](https://docs.stripe.com/currencies/conversions).Blocked by
StripeIndicates that Stripe blocked the payment due to risk factors, such as
[card testing](https://docs.stripe.com/disputes/prevention/card-testing).Blocked
paymentsTotal number of card payments blocked by Stripe or Radar. Payments might
be blocked for several reasons, such as risk of fraud or configured [Radar
rules](https://docs.stripe.com/radar/rules).Blocked payment ratePercentage of
blocked card payments, out of all attempted payments.Blocked payment volumeTotal
amount of blocked card payments. Defaults to your [settlement
currency](https://docs.stripe.com/currencies/conversions).Card account
updater[Card account
updater](https://docs.stripe.com/get-started/data-migrations/card-imports#cau)
automatically maintains up-to-date card information for your customers. Uplift
shown is from successful payments that had updates to cards using the card
account updater within 180 days of the payment date.Failed paymentsTotal number
of unsuccessful card payments due to reasons such as insufficient funds, expired
cards, fraud prevention, and
[more](https://docs.stripe.com/declines/card).Failed payment ratePercentage of
unsuccessful card payments, out of all attempted card payments.Failed payment
volumeTotal amount of unsuccessful card payments. Defaults to your [settlement
currency](https://docs.stripe.com/currencies/conversions).High risk - RadarCard
payment blocked by [Radar](https://docs.stripe.com/radar) due to a high risk
score.Network tokensA non-sensitive, 16-digit numeric substitute for a card
number, also known as a primary account number (PAN), that ensures only the most
current card information is used for processing payments. Uplift shown is from
successful payments with [network
tokens](https://dashboard.stripe.com/settings/optimizations) that had updates to
underlying card information within 180 days of the payment date.PaymentsTotal
number of all card payments, including successful and unsuccessful
payments.Payment success ratePercentage of card payments approved by card
issuers, out of all attempted card payments. Unlike authorization rate, this
includes blocked payments and payments that didn’t complete 3D Secure
authentication.Payment success rate increaseUplift in payment success rate
within a specific period of time.Payment volumeTotal amount of all successful
card payments. Defaults to your [settlement
currency](https://docs.stripe.com/currencies/conversions).Post-authorization
rule match - RadarPayment blocked that [Radar](https://docs.stripe.com/radar)
blocked because of a rule match after authorization. For example, a rule that
blocks payments that fail CVC or postal code verification.Revenue increaseUplift
in payment volume over the selected time period. Revenue volume is the total
amount of revenue defaulted to your [settlement
currency](https://docs.stripe.com/currencies/conversions).Rule match -
RadarPayment that Radar blocked because of a rule match before authorization.
## Authentication analytics

The following are [Authentication
analytics](https://docs.stripe.com/payments/analytics/authentication) terms:

TermDefinition3D Secure challengeA security step that requires the cardholder to
verify their identity to ensure the legitimacy of online transactions.3DS
failuresTotal number of payments that failed 3D Secure.3DS failure
ratePercentage of all payments where 3D Secure failed, out of all payments where
3DS was requested.3DS failure volumeTotal amount of payments that failed 3D
Secure.3DS not actionedPayments where the customer didn’t enter the 3D Secure
flow, or there was a technical issue.3DS requestsTotal number of payments where
3D Secure was requested. Excludes requests related to card validation.3DS
requested by APIPayments where you requested 3D Secure authentication through
the API. Learn more about [manual requests in the
API](https://docs.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds).3DS
requested by Card issuerPayments where the customer’s bank requested 3D
Secure.3DS requested by RadarPayments that matched a Radar rule to request 3D
Secure authentication. [View
rules](https://dashboard.stripe.com/settings/radar/rules).3DS requested by
StripePayments where Stripe requested 3D Secure authentication to comply with
regulations.3DS unavailablePayments where the card issuer didn’t support 3D
Secure or returned an error.All other exemptionsAll other reasons that in-scope
payments were exempt from Strong Customer Authentication.Authentication
ratePercentage of card payments where 3D Secure authentication was attempted,
out of all card payments.Authentication success ratePercentage of payments where
3D Secure authentication was successful, out of all 3DS requests.Challenge
ratePercentage of card payments where the customer received an authentication
challenge, out of all 3D Secure requests.Challenge success ratePercentage of
payments where a challenge was successfully completed, out of all the payments
that received a challenge.Failed 3DS challengePayments where customer didn’t
complete 3D Secure challenge, or the card issuer rejected it.In-scope
paymentsTotal number of card payments that are subject to Strong Customer
Authentication. Includes in-scope payments that receive exemptions. Excludes
out-of-scope payments such as merchant-initiated transactions (MITs) and mail
order/telephone order (MOTO) payments. Also excludes payments that customers
make using digital wallets like Apple Pay and Google Pay, because these wallets
don’t use 3DS.Low-value exemptionCard payments that successfully received
low-value exemptions. Learn more about [low-value
exemptions](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions).Low-risk
exemptionCard payments deemed to have a low likelihood of being fraudulent. For
example, on payments that Stripe exempted with [Transaction Risk
Analysis](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions).Non-exemptIn-scope
payments that weren’t exempt from Strong Customer Authentication.SCA
exemptionsTotal number of in-scope card payments that received an exemption from
Strong Customer Authentication.SCA exemption ratePercentage of card payments
exempt from Strong Customer Authentication (SCA) regulations, out of all
in-scope payments.Successful 3DS challenge flow3D Secure challenge completed
successfully.Successful 3DS frictionless flow3D Secure authentication completed
successfully without a challenge.
## See also

- [Authentication
analytics](https://docs.stripe.com/payments/analytics/authentication)
- [Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance)

## Links

- [Payments analytics](https://dashboard.stripe.com/acceptance)
- [join the waitlist](https://docs.stripe.com/payments/analytics)
- [Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance)
- [Adaptive Acceptance](https://dashboard.stripe.com/settings/optimizations)
- [settlement currency](https://docs.stripe.com/currencies/conversions)
- [card testing](https://docs.stripe.com/disputes/prevention/card-testing)
- [Radar rules](https://docs.stripe.com/radar/rules)
- [Card account
updater](https://docs.stripe.com/get-started/data-migrations/card-imports#cau)
- [more](https://docs.stripe.com/declines/card)
- [Radar](https://docs.stripe.com/radar)
- [Authentication
analytics](https://docs.stripe.com/payments/analytics/authentication)
- [manual requests in the
API](https://docs.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds)
- [View rules](https://dashboard.stripe.com/settings/radar/rules)
- [low-value
exemptions](https://docs.stripe.com/payments/3d-secure/strong-customer-authentication-exemptions)