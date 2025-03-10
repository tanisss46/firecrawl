# Operate offlinePublic preview

## Accept payments with intermittent, limited, or no internet connectivity.

Bluetooth readersInternet readers
When you’re operating with intermittent, limited, or no network connectivity,
Stripe Terminal allows you to store payments locally on your POS device. When a
network connection is restored, the SDK automatically forwards any stored
payments to Stripe.

From your application’s perspective, the payment collection process is similar
to operating online. While offline, the SDK securely stores the payment
information and automatically forwards the stored payments when connectivity is
restored. The SDK allows you to handle offline-related events using callbacks to
your application.

## Availability

**Payment methods**: Visa, Mastercard, Discover, and American Express.

Customers can present a card or NFC-based mobile wallet belonging to a supported
card brand. Swiping cards isn’t allowed. If you’re collecting payments in the
[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area),
customers are required to insert their card and enter a PIN.

Interac, eftpos, and girocard aren’t supported. Co-branded eftpos cards are
routed through the international scheme instead. For more information, see
[eftpos Australia](https://docs.stripe.com/payments/eftpos-australia).

**Readers**: [BBPOS Chipper 2X
BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt), [Stripe Reader
M2](https://docs.stripe.com/terminal/readers/stripe-m2), [BBPOS WisePad
3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3)

**Connection type**: Bluetooth, USB (Android only)

**Integration types**: iOS SDK, Android SDK, React Native SDK

### Collect a payment while offline

The following diagram describes the payment collection process when the Terminal
SDK is offline. When storing payments, the SDK stores the payments to disk. You
can safely reboot the POS device even if it has stored offline payments. When
you re-initialize the SDK and it has reestablished a connection to the internet,
and the SDK resumes forwarding any remaining stored payments.

POS application

Terminal SDK

Mobile reader

Create PaymentIntent

Securely store request information

Success callback

Collect payment method

Prompt for payment method

Payment method data

Success callback

Confirm PaymentIntent

Securely store request information

Success callback

A high-level diagram that shows how offline payments are stored.
### Forward stored payments when online

The following diagram describes how stored payments are forwarded after
connectivity is restored.

Your backend

POS application

Terminal SDK

Stripe backend

Fetch connection token

Fetch connection token

POST /v1/terminal/connection_tokens

Connection token

Connection token

Connection token

Authenticate using connection token

Authentication token

Forward stored payment

Success or decline response

Forwarding event notification

A high-level diagram that shows how offline payments are forwarded to the Stripe
backend.
## See also

- [Collect card payments while
offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments)

## Links

- [European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)
- [eftpos Australia](https://docs.stripe.com/payments/eftpos-australia)
- [BBPOS Chipper 2X
BT](https://docs.stripe.com/terminal/readers/bbpos-chipper2xbt)
- [Stripe Reader M2](https://docs.stripe.com/terminal/readers/stripe-m2)
- [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3)
- [Collect card payments while
offline](https://docs.stripe.com/terminal/features/operate-offline/collect-card-payments)