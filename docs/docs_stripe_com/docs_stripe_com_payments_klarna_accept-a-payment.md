# Accept a Klarna payment

## Learn how to accept Klarna, a global buy now, pay later payment method.

#### Unified line items with Klarna

To maximize approval rates when you integrate with Klarna, we recommend that you
include Line Items data to represent what’s in a shopper’s cart. Reach out here
to request access.

#### Klarna on the Express Checkout Element

Klarna on the Express Checkout Element is currently in private preview with
limited availability. Reach out here to request access.

WebMobileStripe-hosted pageDirect API
#### Caution

Stripe automatically presents your customers payment method options by
evaluating their currency, payment method restrictions, and other parameters. We
recommend that you configure your payment methods from the Stripe Dashboard
using the instructions in [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted).

If you want to continue manually configuring the payment methods you present to
your customers with Checkout, use this guide. Otherwise, update your integration
to [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods).

Klarna is a [single
use](https://docs.stripe.com/payments/payment-methods#usage), [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
payment method that requires customers to
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
their payment. Customers are redirected to a Klarna page, where they select
among multiple payment options (immediate full payment, payment in installments,
or deferred payment). When the customer accepts the terms, Klarna guarantees
that the funds are available to the customer and transfers the funds to your
Stripe account. The customer repays Klarna according to their selected payment
option.

#### Note

Before you start the integration, make sure your account is eligible for Klarna
by navigating to your [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

[Determine
compatibility](https://docs.stripe.com/payments/klarna/accept-a-payment#compatibility)
A Checkout Session must satisfy all of the following conditions to support
Klarna payments:

- [Prices](https://docs.stripe.com/api/prices) for all line items must be in the
same currency. If you have line items in different currencies, create separate
Checkout Sessions for each currency.

#### Private preview

To create recurring or off-session payments with Klarna, sign up for the private
preview.

[Accept a
payment](https://docs.stripe.com/payments/klarna/accept-a-payment#accept-a-payment)
#### Note

Build an integration to [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
with Checkout before using this guide.

Use this guide to learn how to enable Klarna—it shows the differences between
accepting a card payment and using Klarna.

### Enable Klarna as a payment method

When creating a new [Checkout
Session](https://docs.stripe.com/api/checkout/sessions), you need to:

- Add `klarna` to the list of `payment_method_types`
- Make sure all your `line_items` use the same currency.

```
Stripe::Checkout::Session.create({
 mode: 'payment',
 payment_method_types: ['card'],
 payment_method_types: ['card', 'klarna'],
 line_items: [{
 price_data: {
 currency: 'usd',
# To accept `klarna`, all line items must have currency: eur, dkk, gbp, nok,
sek, usd, czk, ron, aud, nzd, cad, pln, chf
 currency: 'eur',
 product_data: {
 name: 'T-shirt',
 },
 unit_amount: 2000,
 },
 quantity: 1,
 }],
 success_url: 'https://example.com/success',
 cancel_url: 'https://example.com/cancel',
})
```

### Fulfill your orders

After accepting a payment, learn how to [fulfill
orders](https://docs.stripe.com/checkout/fulfillment).

[Test your
integration](https://docs.stripe.com/payments/klarna/accept-a-payment#test-integration)
When testing your Checkout integration, select Klarna as the payment method and
click the **Pay** button. In test mode, you can then simulate different outcomes
within Klarna’s redirect.

Below, we have specially selected test data for the currently supported customer
countries. In test mode, Klarna approves or denies a transaction based on the
supplied email address.

AustraliaAustriaBelgiumCanadaCzechiaDenmarkFinlandFranceGermanyGreeceIrelandItalyNetherlandsNew
ZealandNorwayPolandPortugalRomaniaSpainSwedenSwitzerlandUnited KingdomUnited
StatesApprovedDeniedDate of Birth10-07-197003-05-1994First NameTestJohnLast
NamePerson-ausnowStreetWharf StSilverwater RdHouse number41-5Postal
Code48772128CityPort
DouglasSilverwaterRegionQLDNSWPhone+61473752244+61473763254Emailcustomer@email.aucustomer+denied@email.au
For production testing, you can use an amount of `3500` in your local currency
to test all Klarna payment options besides Financing. For example, if you want
to test “Pay in 3” in Italy, you can use a transaction of 35.00 EUR.

### Two-step authentication

Any six digit number is a valid two-step authentication code. Use `999999` for
authentication to fail.

### Repayment method

Inside the Klarna flow, you can use the following test values to try various
repayment types:

TypeValueDirect DebitDE11520513735120710131Bank transferDemo BankCredit Card-
Number: 4111 1111 1111 1111
- CVV: 123
- Expiration: any valid date in the future
Debit Card- Number: 4012 8888 8888 1881
- CVV: 123
- Expiration: any valid date in the future
[Handle refunds and
disputes](https://docs.stripe.com/payments/klarna/accept-a-payment#refunds-and-disputes)
Learn more about Klarna
[disputes](https://docs.stripe.com/payments/klarna#disputed-payments) and
[refunds](https://docs.stripe.com/payments/klarna#refunds).

## Links

- [Accept a
payment](https://docs.stripe.com/payments/accept-a-payment?platform=web&ui=stripe-hosted)
- [configure payment methods in the
Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods)
- [single use](https://docs.stripe.com/payments/payment-methods#usage)
- [immediate
notification](https://docs.stripe.com/payments/payment-methods#payment-notification)
-
[authenticate](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [Prices](https://docs.stripe.com/api/prices)
- [accept a
payment](https://docs.stripe.com/payments/accept-a-payment?integration=checkout)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
- [fulfill orders](https://docs.stripe.com/checkout/fulfillment)
- [disputes](https://docs.stripe.com/payments/klarna#disputed-payments)
- [refunds](https://docs.stripe.com/payments/klarna#refunds)