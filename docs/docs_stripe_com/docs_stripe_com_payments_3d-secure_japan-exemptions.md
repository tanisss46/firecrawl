# Japan 3DS mandate exemptions

## Use exemptions to reduce cardholder friction on eligible payments.

Industry guidelines in Japan require online businesses to use [3D Secure
(3DS)](https://docs.stripe.com/payments/3d-secure) by the end of March 2025. For
more information about the guidelines, see the [Stripe Support
article](https://support.stripe.com/questions/3ds-mandate-in-japan).

In cases where the guidelines allow exemptions, Stripe does not force 3DS on
your payments.

In general, Stripe attempts to process a 3DS authentication on all cards at
least once, either when the card is saved or when it’s first used. Stripe
doesn’t require 3DS on payments made using cards that are already 3DS
authenticated.

#### Note

When payments are made without 3DS by using an exemption, liability shift for
fraudulent payments doesn’t apply. If you want to apply 3DS liability shift to
3DS-exempt payments, you must request 3DS by setting `request_three_d_secure` to
`any` in your PaymentIntent or SetupIntent.

CategoryDescriptionExisting cardsCards entered before Apr 1, 2025, or that were
migrated to Stripe from other processors, are treated as if they were previously
authenticated with 3DS.
Situations where 3DS isn’t possible

Stripe doesn’t automatically use 3DS for:

- Debit cards and prepaid cards
- Apple Pay and Google Pay
- [MOTO
payments](https://support.stripe.com/questions/mail-order-telephone-order-(moto)-transactions-when-to-categorize-transactions-as-moto)

If any of the following cases apply to your integration, you must request
enablement by contacting [Stripe
Support](https://support.stripe.com/contact/email).

- You don’t use Stripe Customer objects. For example, you create payments with
raw card numbers.
- You store and authenticate cards outside of Stripe.
- You process payments from devices that don’t support 3DS, such as game
consoles or smart speakers.

[Customer-Initiated Transactions
(CIT)](https://docs.stripe.com/payments/cits-and-mits)

(For example, saving a card on an e-commerce website for later purchases)

- Saving a card by creating a SetupIntent with `usage=on_session` doesn’t use
3DS unless you [request
it](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method_options-card-request_three_d_secure).
- If you don’t authenticate a card with 3DS when you save it, the first payment
with that card requires 3DS.
- After a saved card is authenticated with 3DS, Stripe treats it as exempt and
doesn’t force 3DS on future payments with that card. However, your integration
must conduct a risk analysis at the time of each subsequent payment and request
3DS if the analysis determines that it’s appropriate. You can use [Stripe
Radar](https://stripe.com/radar) to conduct the risk analysis.
- Design your customer login process to meet at least two of the following five
[Credit Card Transactions Security Measures Council Security
Checklist](https://support.stripe.com/questions/japan-security-checklist)
requirements. If it doesn’t, you must manually request 3DS for each payment by
setting
[request_three_d_secure](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-card-request_three_d_secure)
to `any`.- Restrict access from suspicious IP addresses, to counter attacks from
overseas.
- Limit login attempts, to prevent account password cracking.
- Authenticate users through two-factor authentication or a similar measure, to
notify users of fraudulent login attempts.
- Send email or SMS notifications, throttle attempts, or take other similar
measures when your customer logs in.
- Use “device fingerprinting” or similar measures.
- Payments with [Link](https://docs.stripe.com/payments/link) are exempted
because Link’s login process implements the following measures:- Limits login
attempts to prevent account password cracking.
- Sends email or SMS notifications, throttle attempts, or take other similar
measures when your customer logs in.
[Merchant-Initiated Transactions
(MIT)](https://docs.stripe.com/payments/cits-and-mits), including Stripe
Billing- Saving a card by creating a SetupIntent with `usage=off_session`
requires 3DS.
- If a card is 3DS authenticated when it’s saved, payments using that card don’t
require 3DS.
- If any change to a contract, service, or product requires customer approval,
the associated payment must be customer-initiated
([CIT](https://docs.stripe.com/payments/cits-and-mits)) and must [explicitly
request
3DS](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-card-request_three_d_secure).

## Links

- [3D Secure (3DS)](https://docs.stripe.com/payments/3d-secure)
- [Stripe Support
article](https://support.stripe.com/questions/3ds-mandate-in-japan)
- [MOTO
payments](https://support.stripe.com/questions/mail-order-telephone-order-(moto)-transactions-when-to-categorize-transactions-as-moto)
- [Stripe Support](https://support.stripe.com/contact/email)
- [Customer-Initiated Transactions
(CIT)](https://docs.stripe.com/payments/cits-and-mits)
- [request
it](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-payment_method_options-card-request_three_d_secure)
- [Stripe Radar](https://stripe.com/radar)
- [Credit Card Transactions Security Measures Council Security
Checklist](https://support.stripe.com/questions/japan-security-checklist)
-
[request_three_d_secure](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_options-card-request_three_d_secure)
- [Link](https://docs.stripe.com/payments/link)