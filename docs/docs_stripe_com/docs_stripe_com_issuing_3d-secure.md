# Cardholder authentication using 3D Secure

## Learn about 3D Secure, an additional layer of authentication used by businesses to combat fraud.

## How 3D Secure works

[3D Secure (3DS)](https://docs.stripe.com/payments/3d-secure) uses multi-factor
authentication to reduce fraud for online transactions where a card isn’t
physically present. 3DS is triggered by businesses in online checkout flows, and
requires multi-factor authentication (usually through SMS or email-based
one-time passcode that Stripe sends) to complete.

## Example of a 3D Secure flow

![A Stripe checkout page with the payment information filled out, including the
Pay
button](https://b.stripecdn.com/docs-statics-srv/assets/3ds-flow-1-checkout-page.039294e0dee3a6dede8ea8a32185aae5.png)

Step 1: The customer enters their card details.

![A dialog that displays a loading animation after clicking the Pay button,
which now says
Processing.](https://b.stripecdn.com/docs-statics-srv/assets/3ds-flow-3-challenge-flow.9052a220f336bbdb75a51799622c6477.png)

Step 2: The acquirer requests 3DS verification. If the Stripe issuing card is
enrolled in 3DS, the cardholder sees a prompt to complete an additional
verification step.

As shown above, the additional 3D Secure step at checkout typically involves
showing the cardholder an authentication page from their Issuer, where the
cardholder sees a prompt to enter a verification code sent to their phone or
email.

## Why 3DS is important

In most cases, businesses are responsible for online fraud losses in
card-not-present transactions. To protect themselves, businesses can trigger 3DS
verification to reduce the chances of accepting a fraudulent transaction. Even
if a business triggers 3DS verification, the cardholder only needs to complete
the step if your Stripe cards are enrolled in 3DS. In the UK and EU, 3DS is the
standard for implementing the regulatory requirements of [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) (SCA).

## Liability shift

When a business triggers 3DS verification, liability for fraud shifts from the
business to the issuer in most cases. This applies whether or not your Issuing
cards are enrolled in 3DS, meaning issuers can take on increased liability
without any additional verification.

## 3DS Enrollment

- **US**: 3DS enrollment in the US is optional, and your cards won’t be enrolled
in 3DS unless you contact support to request enrollment. As part of our [best
practices](https://docs.stripe.com/issuing/manage-fraud) for managing
transaction fraud, we recommend enrolling your cards in 3DS early in your
Issuing program’s life cycle. While enrollment does increase friction for a
subset of your cardholder transactions, it helps to significantly reduce the
risk of potential losses because of transaction fraud with online,
card-not-present transactions. After you request enrollment, we enroll all
active cards associated with your account and automatically enroll all cards
created going forward.- Cardholders without a phone number or email on file
won’t be enrolled in 3DS. After requesting enrollment, you can add contact
information to [Cardholder
objects](https://docs.stripe.com/api/issuing/cardholders/object), to auto-enroll
those cards. Conversely, removing the contact info for a cardholder results in
the card being unenrolled from 3DS.
- **UK and EU**: Upon creation, cards are enrolled in 3DS by default because of
local regulations.- To allow the implementation of SCA over 3DS and comply with
local regulations, all cards issued within the EU and UK require a valid phone
number on file.

## 3DS Authentication

When a 3DS authentication request comes through for your
[cardholder](https://docs.stripe.com/api#create_issuing_cardholder), Stripe
sends them either a text message or an email containing a one-time verification
code.

The method of authentication depends on the contact information provided for the
cardholder. In the UK and EU markets supported by Stripe Issuing, cardholders
must have a phone number on file to authenticate with a one-time text message
verification code. In the US, the phone number or email on file will be used to
authenticate cardholders, but if both the phone number and email are present,
then the phone number will be used for authentication. Otherwise, the
authentication request uses whichever contact information is available. To
enable us to best secure you and your cardholders, we recommend keeping phone
numbers and email addresses up to date for cardholders. This enables us to
contact them during authentication. You can update your cardholders’ information
by changing the field to its new value through the API or Dashboard.

In the UK and EU, cardholders might also see an additional security question.
The cardholder sees a list of transactions on the card, and they can select the
transactions they recognize. If the cardholder is using the card for the first
time, they select the option indicating they don’t recognize any of the
presented transactions.

![A dialog showing a sample security question with choices of payment history.
The header has a Your Bank placeholder logo and Card Network placeholder logo.
The security question says, From the following list please identify a recent
payment you have made using this card. There are 5 options with payment
information of whether or not the payment was online, the purchase amount, and
the merchant name. The last option says None of the above. There is a blurple
button at the bottom that says
Verify.](https://b.stripecdn.com/docs-statics-srv/assets/3ds-issuing-knowledge-factor-netcetera.37258cc6c8e63cadf3dbb9b22f94d786.png)

The list of transactions the cardholder is presented with.

## Choose the 3D Secure language

The
[preferred_locales](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-preferred_locales)
field of the Cardholder object determines the display language of the 3DS flow.
The default 3DS language is .

To pick a 3DS language for a cardholder, use the API to set their
`preferred_locales` to an array of preferred languages, in order of preference.
If you want, you can provide one language only. The supported languages are
 (`en`), French (`fr`), German (`de`), Italian (`it`), and Spanish
(`es`).

```
curl https://api.stripe.com/v1/issuing/cardholders \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d type=individual \
 -d name="Jane D. Rocket" \
 --data-urlencode email="jane@example.com" \
 -d "preferred_locales[]"=fr \
 -d "preferred_locales[]"=en \
 -d "billing[address][line1]"="1234 Main Street" \
 -d "billing[address][city]"="San Francisco" \
 -d "billing[address][state]"=CA \
 -d "billing[address][country]"=US \
 -d "billing[address][postal_code]"=94111
```

In the US, Stripe also supports authentication through a native iOS and Android
application. If you want to use this functionality, [please reach out to
support](https://support.stripe.com/contact).

Regardless of the authentication method used, if a cardholder can’t complete
three consecutive 3DS attempts in a short period of time, it disables 3DS on
their cards for 60 minutes.

## Exemptions

Certain types of low-risk payments might be exempt from SCA. Exemptions limit
friction for low-risk payments by reducing the frequency of customer
authentication. By default, Stripe might claim the following exemptions for
3DS-eligible cards to limit the friction associated with transactions it deems
low risk or low value:

TypeMeaningtransaction_risk_analysis (US only)An issuer (such as Stripe) can do
a real-time risk analysis to determine whether or not to claim a low-risk
exemption to a transaction.low_value_transactionTransactions below 30 GBP/EUR
(or equivalent converted amount) are considered “low value” and might be exempt
from SCA. If the exemption has been used five times since the cardholder’s last
successful authentication or if the sum of previously exempted payments exceeds
100 GBP or EUR, then the exemption doesn’t apply, and the cardholder must be
authenticated.
#### Note

Acquirers can also request exemptions, and Stripe might honor them. In these
scenarios, loss liability stays with the acquirer and doesn’t shift to the
issuer.

When an issuer-claimed exemption is applied, the [Authorization
object](https://docs.stripe.com/api/issuing/authorizations) looks like this:

```
{
 "object": "issuing.authorization",
 ...
 "verification_data" : {
 ...
 "authentication_exemption": {
 "type": "low_value_transaction",
 "claimed_by": "issuer"
 },
 ...
 },
 ...
}
```

Conversely, when an acquirer-claimed exemption is applied, the [Authorization
object](https://docs.stripe.com/api/issuing/authorizations) looks like this:

```
{
 "object": "issuing.authorization",
 ...
 "verification_data" : {
 ...
 "authentication_exemption": {
 "type": "low_value_transaction",
 "claimed_by": "acquirer"
 },
 ...
 },
 ...
}
```

If you’re based in the UK or EU and your use case only requires virtual cards,
you can contact Stripe Support to discuss whether a Secure Corporate Payment
(SCP) exemption is applicable to your program.

## Managing fraud through 3DS

Stripe includes details about a 3DS attempt through the API in the authorization
endpoint. Use the `three_d_secure` hash in the
[verification_data](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-verification_data)
hash to determine if an authorization was successfully authenticated. If you
maintain your own authorization logic, we suggest using these values as key
inputs that determine whether to approve or reject an authorization.

Additionally, if the business didn’t attempt 3DS, the `three_d_secure` field is
null. If 3DS was exempted, then the `authentication_exemption` is present and
the `three_d_secure` field is null. An authorization can’t contain both
`three_d_secure` and `authentication_exemption`.

You can find guidelines on what the values represent and how you can use them to
combat fraud in the table below.

ResultMeaningSuggested actionattempt_acknowledgedThe business attempted to
authenticate the authorization, but the card isn’t enrolled or couldn’t reach
Stripe.There is insufficient evidence to determine if the authorization is
fraudulent or not.authenticatedThe shopper was successfully verified as the
cardholder as they entered the correct verification code sent to their phone.
The online purchase was legitimate and not fraudulent.Approve the
transaction.failedThe cardholder wasn’t authenticated as the shopper which could
mean the cardholder is not the actor making the purchase.Decline the
transaction.requiredThe authorization was declined because regulatory
requirements mandated an authentication for this transaction but it wasn’t
submitted correctly by the merchant, and they didn’t claim an applicable
exemption.Decline the transaction.
#### Note

If the card is enrolled in 3DS, when `verification_data.three_d_secure` isn’t
present, 3D Secure wasn’t attempted by the merchant on an authorization.

## How to test 3DS

Use the Stripe Payments API to test 3DS.

### Create a PaymentMethod with your issued card

You can [create a
PaymentMethod](https://docs.stripe.com/api#create_payment_method) using your own
issued card by running the following command:

```
curl https://api.stripe.com/v1/payment_methods \
 -u pk_test_TYooMQauvdEDq54NiTphI7jx: \
 -d type=card \
 -d "card[number]"=YOUR_ISSUED_CARD_NUMBER \
 -d "card[exp_month]"=YOUR_ISSUED_CARD_EXPIRATION_MONTH \
 -d "card[exp_year]"=YOUR_ISSUED_CARD_EXPIRATION_YEAR \
 -d "card[cvc]"=YOUR_ISSUED_CARD_CVC
```

Replace the following values:

- `YOUR_ISSUED_CARD_NUMBER` with the card number of your issued card
- `YOUR_ISSUED_CARD_CVC` with the CVC of your issued card
- `YOUR_ISSUED_CARD_EXPIRATION_MONTH` with the expiration month of your issued
card
- `YOUR_ISSUED_CARD_EXPIRATION_YEAR` with the expiration year of your issued
card

### Create a PaymentIntent

You can [create a
PaymentIntent](https://docs.stripe.com/api#create_payment_intent) by running the
following command:

```
curl https://api.stripe.com/v1/payment_intents \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d amount=15000 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d "payment_method_options[card][request_three_d_secure]"=any \
 -d "capture_method"=manual
```

This command creates a PaymentIntent that initiates a 3D Secure authentication
request. Use the `payment_method_options[card][request_three_d_secure]=any`
parameter to perform 3D Secure authentication. The amount must be large enough
to warrant a challenge. This example uses 150 USD.

The `"capture_method"=manual` parameter enables manual capture for the
PaymentIntent, which means the funds are authorized but not captured yet.

### Confirm the PaymentIntent

You can [confirm the
PaymentIntent](https://docs.stripe.com/api#confirm_payment_intent) by running
the following command:

```
curl https://api.stripe.com/v1/payment_intents/pi_XXX/confirm \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d payment_method=pm_XXX \
 -d return_url=https://www.example.com
```

Replace `pi_XXX` with your PaymentIntent ID and `pm_XXX` with your PaymentMethod
ID. After confirming the PaymentIntent, the response you receive contains the
`next_action` field. That field includes a URL that you can use to redirect the
user to complete 3DS authentication.

```
...
"next_action": {
 "redirect_to_url": {
 "return_url": "https://www.example.com ",
 "url": "https://hooks.stripe.com/3d_secure_2/hosted?...."
 },
 "type": "redirect_to_url"
 },
...
```

### Void the authorization

After completing the 3DS challenge and payment authorization, you can [cancel
the PaymentIntent](https://docs.stripe.com/api#cancel_payment_intent) without
capturing funds.

```
curl https://api.stripe.com/v1/payment_intents/pi_XXX/cancel \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "cancellation_reason"=abandoned
```

Replace `pi_XXX` with your PaymentIntent ID.

## Links

- [3D Secure (3DS)](https://docs.stripe.com/payments/3d-secure)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [best practices](https://docs.stripe.com/issuing/manage-fraud)
- [Cardholder objects](https://docs.stripe.com/api/issuing/cardholders/object)
- [cardholder](https://docs.stripe.com/api#create_issuing_cardholder)
-
[preferred_locales](https://docs.stripe.com/api/issuing/cardholders/object#issuing_cardholder_object-preferred_locales)
- [please reach out to support](https://support.stripe.com/contact)
- [Authorization object](https://docs.stripe.com/api/issuing/authorizations)
-
[verification_data](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-verification_data)
- [create a PaymentMethod](https://docs.stripe.com/api#create_payment_method)
- [create a PaymentIntent](https://docs.stripe.com/api#create_payment_intent)
- [confirm the
PaymentIntent](https://docs.stripe.com/api#confirm_payment_intent)
- [https://www.example.com](https://www.example.com)
-
[https://hooks.stripe.com/3d_secure_2/hosted?....](https://hooks.stripe.com/3d_secure_2/hosted?...)
- [cancel the PaymentIntent](https://docs.stripe.com/api#cancel_payment_intent)