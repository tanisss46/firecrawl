# eftpos Australia

## Learn about eftpos Australia, a common payment method in Australia.

[Eftpos](https://www.eftposaustralia.com.au/) is Australia’s local debit card
network. More than 90% of eftpos cards are co-branded with either Visa or
Mastercard, meaning you can process these cards over either network supported by
the card.

Stripe processes co-branded eftpos cards over eftpos, plus either Visa or
Mastercard, in accordance with [least cost routing
requirements](https://support.stripe.com/questions/supporting-dual-network-debit-cards-in-australia)
and depending on the [type of
transaction](https://docs.stripe.com/payments/eftpos-australia#identify-which-network-a-payment-was-processed-on).

#### Note

Eftpos-only cards (also known as “proprietary eftpos cards”) only support
in-person payments and can’t be used for online transactions.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Australia
- **Presentment currency**

AUD
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Cards
- **Payment method type**

Debit and prepaid cards
- **Recurring payments**

Yes
- **Payout timing**

Standard payout timing applies
- **Connect support**

Yes
- **Dispute support**

Yes
- **Manual capture support**

No
- **Refunds / Partial refunds**

Yes / Yes

## Availability

Eftpos is available to any business that uses Stripe in Australia, with the
following exceptions:

- Massage parlors ([MCC](https://docs.stripe.com/connect/setting-mcc) 7297)
- Financial institutions—manual cash disbursements
([MCC](https://docs.stripe.com/connect/setting-mcc) 6010)
- Financial institutions—merchandise and services
([MCC](https://docs.stripe.com/connect/setting-mcc) 6012)
- Non-financial institutions—foreign currency, money orders and travelers’
checks. ([MCC](https://docs.stripe.com/connect/setting-mcc) 6051)
- Remote stored value load—merchant
([MCC](https://docs.stripe.com/connect/setting-mcc) 6530)
- Stored value card purchase/load
([MCC](https://docs.stripe.com/connect/setting-mcc) 6540)
- Wires, money orders ([MCC](https://docs.stripe.com/connect/setting-mcc) 4829)

## Integration

If your integration can already [accept card
payments](https://docs.stripe.com/payments/accept-a-payment), you can also
accept eftpos without additional updates.

Eftpos is the default network for payment. Unless you change the default
network, you must inform your customers that whenever they use a dual-network
debit card, their payments might be processed through the debit network,
regardless of the logo that appears when they enter their payment information.

We recommend you notify your customers based on the type of payment transaction:

- For single payment transactions, display a notification to the customer before
the completion of the checkout process.
- For new recurring payment transactions, display a notification to the customer
at the time of setup.
- For existing recurring payment transactions, notify your customers in advance
of future transactions.

You must notify your customers about how network routing functions, and how
payments processing works. You can use the suggested notification message below:

#### Note

Notwithstanding the payment brand logo displayed when you enter your payment
information, whenever you use a dual-network debit card displaying eftpos and
another payment brand, your payment (including any future recurring debit
payments authorized by you) might be processed through either network. See the
[Terms and Conditions] or [FAQs] for more information.

We recommend that you provide further information in your Terms and Conditions
or FAQs on how network routing functions and how payments processing works. For
guidelines on best practices, see the Australian Payments Network [MCR Online
Notification
Guidelines](https://www.auspaynet.com.au/resources/cards-and-devices).

## Understand which network processes payments

Stripe dynamically routes between the international scheme (Visa or Mastercard)
and eftpos, depending on the type of payment, technical availability and
authorization rate considerations:

- If a payment requires [placing a hold on the
card](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method) (in
other words, if there’s a delay between authorization and capture), or if it
requires [3D Secure](https://docs.stripe.com/payments/3d-secure), Stripe always
routes to the international scheme.
- For other types of payments, Stripe generally defaults to the eftpos network.

If you require that eftpos is never the default network for any payments, please
contact [support](https://support.stripe.com/contact).

To identify which network a payment was processed on, inspect the
[network](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-network)
field on the [Charge](https://docs.stripe.com/api/charges/object) object
associated with a successful [Payment
Intent](https://docs.stripe.com/api/payment_intents/object):

```
{
 "id": "ch_1Ff52K2eZvKYlo2CWe10i0s7",
 "object": "charge",
 ...
 "payment_method_details": {
 "card": {
 "brand": "visa",
 ...
 "network": "eftpos_au"
 },
 "type": "card"
 }
}
```

## See also

- [Migrating from Charges API to the Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration)
- [Available eftpos test cards](https://docs.stripe.com/testing#cards)

## Links

- [Eftpos](https://www.eftposaustralia.com.au/)
- [least cost routing
requirements](https://support.stripe.com/questions/supporting-dual-network-debit-cards-in-australia)
- [type of
transaction](https://docs.stripe.com/payments/eftpos-australia#identify-which-network-a-payment-was-processed-on)
- [MCC](https://docs.stripe.com/connect/setting-mcc)
- [accept card payments](https://docs.stripe.com/payments/accept-a-payment)
- [MCR Online Notification
Guidelines](https://www.auspaynet.com.au/resources/cards-and-devices)
- [placing a hold on the
card](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [support](https://support.stripe.com/contact)
-
[network](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card-network)
- [Charge](https://docs.stripe.com/api/charges/object)
- [Payment Intent](https://docs.stripe.com/api/payment_intents/object)
- [Migrating from Charges API to the Payment Intents
API](https://docs.stripe.com/payments/payment-intents/migration)
- [Available eftpos test cards](https://docs.stripe.com/testing#cards)