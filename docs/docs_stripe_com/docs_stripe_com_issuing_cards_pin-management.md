# PIN management

## Let your cardholders manage their personal identification numbers.

Some Point-of-Sale and ATM card terminals require cardholders to enter their
card’s PIN to authenticate transactions. Cardholders also need to use their PINs
with physical cards in many regions of the world. You can use the Stripe API and
[Stripe Elements](https://docs.stripe.com/payments/elements) to manage and view
PINs on your issued cards.

Both [physical card](https://docs.stripe.com/issuing/cards/physical) and
[virtual card](https://docs.stripe.com/issuing/cards/virtual) PINs are set to a
random value at creation. Cards created as a [replacement
for](https://docs.stripe.com/api/issuing/cards/create#create_issuing_card-replacement_for)
other cards won’t inherit the old card’s PIN. In [test
mode](https://docs.stripe.com/test-mode), all PINs are set to 0000 by default.

## Set a card’s initial PIN at creation

When issuing a new card through the API, you can provide a desired PIN to be
pre-set on the card. This is optional, and if you don’t provide an initial PIN,
we randomly generate one for you. You can always [view a card’s
PIN](https://docs.stripe.com/issuing/cards/pin-management#viewing-a-cards-pin).

To pre-set a PIN when issuing a new card, pass it in encrypted form as the
`pin.encrypted_number` parameter to the Create Card API method:

```
curl https://api.stripe.com/v1/issuing/cards \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "cardholder"="ich_1D4b3fdsa" \
 -d "pin[encrypted_number]"="eyJhbGciOiJSU0..."
 -d "type"="virtual" \
 -d "currency"="usd"
```

See [Encrypting
PINs](https://docs.stripe.com/issuing/cards/pin-management#encrypting-pins) for
more information about how to encrypt a PIN before passing it to the Stripe API
or your own servers.

#### Note

When setting a card’s initial PIN in a request to the Create Card API method,
the response to the creation request won’t return the PIN (in either encrypted
or plain-text form).

## View a card’s PIN

You can use [Issuing Elements](https://docs.stripe.com/issuing/elements) to
retrieve a card’s PIN in a
[PCI-DSS](https://docs.stripe.com/security/guide#validating-pci-compliance)-compliant
way.

### Use Issuing Elements

Stripe provides a browser-side JavaScript library that allows you to display the
sensitive data (including PINs) of your Issuing cards in a PCI-compliant manner.
The PIN renders inside of a Stripe-hosted `iframe` and never touches your
servers. Stripe offers this library as a part of
[Stripe.js](https://docs.stripe.com/js).

All Issuing users, whether they’re PCI-compliant or not, can use Issuing
Elements to retrieve PINs.

To retrieve a card’s PIN using Issuing Elements, first [create an Issuing
Elements integration](https://docs.stripe.com/issuing/elements), and then use it
to display the `issuingCardPinDisplay` Element:

```
const stripe = Stripe("pk_test_TYooMQauvdEDq54NiTphI7jx");

const cardId = 'ic_abc123'; // ID of the issued Card you want to retrieve the
PIN for
const ephemeralKeyNonce = ...;
const ephemeralKey = ...;

// create the PIN Element with Stripe.js
const pinElement = stripe.elements().create('issuingCardPinDisplay', {
 issuingCard: cardId,
 nonce: ephemeralKeyNonce,
 ephemeralKeySecret: ephemeralKey.secret,
});

// Mount the PIN element onto DOM elements on your web page
pinElement.mount('#card-pin');
```

## Change a card’s PIN

### Change a card’s PIN with the Cards API

You can change the PIN for an issued card using the [Card Update
API](https://docs.stripe.com/api/issuing/cards/update). However, depending on
the region the card is used in, the new PIN might not be immediately usable. See
[Online and offline
PINs](https://docs.stripe.com/issuing/cards/pin-management#online-and-offline-pins)
for further guidance.

You can also [change a card’s PIN at an
ATM](https://docs.stripe.com/issuing/cards/pin-management#changing-a-cards-pin-at-an-atm)
(if supported by ATMs in your region). PIN changes at an ATM are instantaneous.

To change the PIN for a given card using the API, pass it in encrypted form as
the `pin.encrypted_number` parameter to the Update Card API method:

See [Encrypting
PINs](https://docs.stripe.com/issuing/cards/pin-management#encrypting-pins) for
more information about how to encrypt a PIN before passing it to the Stripe API
or your own servers.

#### Note

When changing a card’s PIN in a request to the Update Card API method, the
response to the update request won’t return the PIN (in either encrypted or
plain-text form).

### Change a card’s PIN at an ATM

Cardholders can change the PIN for their Stripe Issuing card at most ATMs. The
cardholder must know the card’s current PIN to change it at an ATM. You can
[retrieve a card’s
PIN](https://docs.stripe.com/issuing/cards/pin-management#viewing-a-cards-pin)
before changing it. Some countries, such as France, don’t provide PIN management
features at ATMs.

#### Note

ATMs are the recommended way to change PINs on Issuing cards because they avoid
offline PIN synchronization issues that are possible when changing PINs with the
[Cards API](https://docs.stripe.com/api/issuing/cards). See [Online and offline
PINs](https://docs.stripe.com/issuing/cards/pin-management#online-and-offline-pins)
for more details.

## Unblock a card’s PIN

If you incorrectly enter a card’s PIN three consecutive times, the PIN becomes
blocked. No further PIN-authenticated payments can be made through the card
until the PIN is unblocked. Additionally, when a card’s online PIN is blocked,
the card’s status is set to `inactive`, and no payments of any kind can be made
until the card is reactivated.

To unblock a card’s online PIN, and reactivate the card, use the Cards API to
set its
[status](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-status)
to `active`. You can also reactivate a card in your Stripe Dashboard.

To unblock a card’s offline PIN, change the card’s PIN using the [Cards
API](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-pin-encrypted_number).
Changing a card’s PIN, even to the same value as before, unblocks the card’s
offline PIN. Alternatively, in most countries, cardholders can also unblock a
card’s offline PIN at an ATM.

#### Note

After unblocking a card’s offline PIN with the Cards API, the next offline PIN
transaction might still fail once. When this happens, the cardholder needs to
retry the transaction. After the retry, the card’s offline PIN is unblocked.

## Encrypting PINs

To enable you to set a card’s PIN in a way that doesn’t require it to pass
through your servers in plain text, the Stripe API expects you to provide PINs
in an encrypted form.

Encrypt the desired PIN (for example, `"0123"`) in JWE (JSON Web Encryption)
format using [Stripe’s RSA public key](https://issuing-key.stripe.com/v1/keys).
When encrypting, use the `RSA-OAEP` algorithm for key wrapping and
`A128CBC-HS256` for content encryption.

Stripe provides its public key for PIN encryption in both PKCS#8 and JWK format.
Depending on your client environment and the library used, one might be easier
to use than the other.

### PIN encryption best practices

- Don’t cache, store, or reuse encrypted PINs for longer than necessary to call
the Stripe API.
- Don’t encrypt PINs on your servers. Instead, perform encryption as soon as
your user provides the PIN (for example, in your mobile application or in your
web application’s frontend) and pass the encrypted form to your servers, and
then on to the Stripe API.
- Don’t cache Stripe’s Issuing public key: we can change it or rotate it without
notice. Instead, fetch it for every PIN operation you perform on the Stripe API.
- Don’t roll your own cryptography. JWE libraries are available for most common
languages and platforms.

### PIN encryption examples

```
import fetch from 'node-fetch';
import { importJWK, CompactEncrypt } from 'jose'

async function encryptPin(myNewPin) {
 // Fetch Stripe's RSA public key
 const keyData = await fetch('https://issuing-key.stripe.com/v1/keys')
 .then(r => r.json());

 // Import the public key. Here, we choose to import the JWK-formatted key,
 // but it will also be available in PKCS#8 format as `keyData.pkcs8`
 const publicKey = await importJWK(keyData.jwk, 'RSA');

 // Encrypt the new PIN with the given public key, using the RSA-OAEP
 // algorithm to wrap the key, and A128CBC-HS256 to produce the ciphertext
 const jwe = await new CompactEncrypt(new TextEncoder().encode(myNewPin))
.setProtectedHeader({ alg: 'RSA-OAEP', enc: 'A128CBC-HS256', kid: keyData.key_id
})
 .encrypt(publicKey);

 // Return our JWE (JWEs are base64url-encoded)
 return jwe;
}

await encryptPin("0123");
// => eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkExMjhDQkMtSFMyNTYiLCJraWQiOiJz...
```

The example above encrypts a PIN (0123) using JSON Object Signing and Encryption
libraries for various languages. Equivalent libraries exist for other languages:

LanguageLibraryJavaScript[jose](https://github.com/panva/jose)Python[jwcrypto](https://github.com/latchset/jwcrypto)Ruby[ruby-jose](https://github.com/potatosalad/ruby-jose)Go[go-jose](https://github.com/square/go-jose)Swift[JOSESwift](https://github.com/airsidemobile/JOSESwift)Java[jose4j](https://bitbucket.org/b_c/jose4j/wiki/Home).NET[jose-jwt](https://github.com/dvsekhvalnov/jose-jwt)
## Online and offline PINs

The physical cards that Stripe issues have EMV chips. One function of an EMV
chip is to store the card’s PIN. This allows card terminals to verify an entered
PIN against the card itself, without needing to verify it online, directly with
the issuer. This is known as an “offline” PIN (or cardholder) verification.

When a cardholder is asked to enter their PIN, depending on where they’re using
it, the card terminal might use either an online or an offline verification.
Some countries use online PIN verifications, and others use offline. For
example, card terminals in the US and Germany generally use an online PIN
verification, while those in the UK, Ireland, or France use offline PIN.

### Change a PIN in regions that use offline PIN verification

Even when a card has an EMV chip, its PIN is also stored online, with the issuer
(Stripe). Because a card’s PIN is stored in two places, changing it using the
Stripe API only takes effect immediately for online PIN verifications.

After changing a PIN with the Stripe API, and then using it in an offline PIN
region, the cardholder must first make a successful transaction using their
previous PIN. An “offline” card terminal only updates the offline PIN stored on
the EMV chip with the new one given to the Stripe API after it successfully
completes a PIN verification.

In addition to using the Stripe API, you can also allow a cardholder change a
card’s PIN at an ATM—but only in regions where ATMs support PIN changes. When
changed at an ATM, the PIN simultaneously updates on both the EMV chip and at
the issuer. PIN changes at ATMs take effect immediately for both online and
offline PIN verifications.

Country PIN change behavior- Ireland
- Mexico
- United Arab Emirates
- United Kingdom
- PIN verifications generally happen offline
- After changing a card’s PIN using the Stripe API, the card must complete one
transaction using the card’s previous PIN. After that, the new PIN takes effect
- PIN changes at ATMs take effect immediately for all PIN verifications
- France
- PIN verifications generally happen offline
- After changing a card’s PIN using the Stripe API, the card must complete one
transaction using the card’s previous PIN. After that, the new PIN takes effect
- PINs can’t be changed at ATMs, so can only be changed using the Stripe API
- Belgium
- Brazil
- Cyprus
- Germany
- Greece
- Italy
- Netherlands
- Poland
- Portugal
- Romania
- Spain
- Switzerland
- Turkey
- United States
- PIN verifications generally happen online
- Changes to a card’s PIN made with the Stripe API take effect immediately for
online PIN verifications
- PIN changes at ATMs take effect immediately for all PIN verifications

If the country your cardholders want to use cards in isn’t listed above,
[contact Issuing support](mailto:support-issuing@stripe.com) for PIN guidance in
your region.

## PIN verification during authorization

If a transaction requires PIN verification, the cardholder must enter their
card’s PIN on the card terminal. If the cardholder enters their PIN incorrectly,
then the transaction is declined, and no `issuing_authorization.request` webhook
is sent.

The timing to create PIN verification authorization objects depends on whether
the transaction used the card’s online or offline PIN. The authorization’s
[verification_data.pin_check](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-verification_data-pin_check)
attribute tells you the type of PIN verification used and the result.

### Online PIN verification

[Authorizations](https://docs.stripe.com/api/issuing/authorizations/object) with
online PIN verifications have a `pin_check` value of `online_pin_match` or
`online_pin_mismatch`. A mismatch means that the cardholder entered the wrong
PIN, so Stripe declined the transaction. Every PIN verification attempt creates
an Authorization object.

After three consecutive online PIN verification failures, the card’s online PIN
is blocked and the card’s `status` is set to `inactive`. The cardholder can’t
make any further transactions, PIN-verified or otherwise, until the card becomes
[active
again](https://docs.stripe.com/issuing/cards/pin-management#unblock-a-cards-pin).

Authorizations declined because of a blocked online PIN have a `reason` of
`pin_blocked` in the
[request_history](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)
array.

### Offline PIN verification

[Authorizations](https://docs.stripe.com/api/issuing/authorizations/object) with
offline PIN verifications have a `pin_check` value of `offline_pin_match` or
`offline_pin_mismatch`. A mismatch means that the cardholder entered the wrong
PIN, so Stripe declined the transaction.

However, because the terminal performs offline PIN verification, Stripe isn’t
notified of every failed PIN attempt. we only create an Authorization object
after authorization either succeeds or the cardholder fails all three PIN
attempts.

Three incorrect PIN attempts blocks the card’s offline PIN. The cardholder can’t
attempt a PIN-verified transaction until the offline PIN is
[unblocked](https://docs.stripe.com/issuing/cards/pin-management#unblock-a-cards-pin).
In contrast to online PIN blocks, the cardholder can still use the card for
non-PIN-verified transactions (such as e-commerce transactions) while the
offline PIN is blocked.

A terminal that performs offline PIN verification won’t attempt to authorize an
inserted card with a blocked offline PIN. Instead, the terminal might display a
message to the cardholder stating that the card’s PIN is blocked, suggesting
that the cardholder contact their issuer.

## Links

- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [physical card](https://docs.stripe.com/issuing/cards/physical)
- [virtual card](https://docs.stripe.com/issuing/cards/virtual)
- [replacement
for](https://docs.stripe.com/api/issuing/cards/create#create_issuing_card-replacement_for)
- [test mode](https://docs.stripe.com/test-mode)
- [Issuing Elements](https://docs.stripe.com/issuing/elements)
- [PCI-DSS](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [Stripe.js](https://docs.stripe.com/js)
- [Card Update API](https://docs.stripe.com/api/issuing/cards/update)
- [Cards API](https://docs.stripe.com/api/issuing/cards)
-
[status](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-status)
- [Cards
API](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-pin-encrypted_number)
- [Stripe’s RSA public key](https://issuing-key.stripe.com/v1/keys)
- [jose](https://github.com/panva/jose)
- [jwcrypto](https://github.com/latchset/jwcrypto)
- [ruby-jose](https://github.com/potatosalad/ruby-jose)
- [go-jose](https://github.com/square/go-jose)
- [JOSESwift](https://github.com/airsidemobile/JOSESwift)
- [jose4j](https://bitbucket.org/b_c/jose4j/wiki/Home)
- [jose-jwt](https://github.com/dvsekhvalnov/jose-jwt)
-
[verification_data.pin_check](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-verification_data-pin_check)
- [Authorizations](https://docs.stripe.com/api/issuing/authorizations/object)
-
[request_history](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)