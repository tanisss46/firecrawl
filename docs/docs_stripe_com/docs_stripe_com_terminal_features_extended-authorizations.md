# Extended authorizations

## Capture a confirmed Stripe Terminal payment later.

Extended authorizations allow you to capture a
[confirmed](https://docs.stripe.com/api/payment_intents/confirm)
[PaymentIntent](https://docs.stripe.com/api/payment_intents/object) up to 30
days later, depending on the card brand and whether your business is in an
eligible category. This is helpful if you need more than the typical 48 hours
(or 5 days for Visa) between authorization and payment capture. For example, a
hotel authorizes a payment in full when a guest checks in, but captures the
payment when the guest checks out.

## Availability

Extended authorization is available on Visa, Mastercard, American Express and
Discover. Extended authorizations are not supported on single-message payment
methods like
[Interac](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#interac-payments)
and
[eftpos](https://docs.stripe.com/terminal/payments/regional?integration-country=AU#eftpos-payments).

#### Note

You can contact [support](https://support.stripe.com/contact) if you’re unsure
about the eligibility of your merchant business category. If you’re a
[Connect](https://docs.stripe.com/connect) user, [set the merchant category
code](https://docs.stripe.com/connect/setting-mcc) for your connected accounts
to match their businesses.

## Request extended authorization support

When you create a `PaymentIntent`, you can request to extend the capture window
of the payment. Set the
[request_extended_authorization](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_extended_authorization)
field to `true` and the
[capture_method](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
to `manual`.

Server-sideiOSAndroidReact Native
```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_types[]"=card_present \
 -d capture_method=manual \
 -d "payment_method_options[card_present][request_extended_authorization]"=true
```

In the response, the
[capture_before](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-capture_before)
field indicates the time when the authorization expires. Failure to capture the
payment by this time cancels the authorization and releases the funds. When this
happens, the [PaymentIntent
status](https://docs.stripe.com/payments/paymentintents/lifecycle) transitions
to `canceled`.

## Authorization validity

Every card network and card brand has a different rule for how long an
authorization is valid. With Terminal, an authorization for in-person payments
is valid for at least two days. Because authorization rules can change without
prior notice, use the
[capture_before](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-capture_before)
field to determine the validity window for an authorization.

#### Note

The `capture_before` field is located on the
[Charge](https://docs.stripe.com/api/charges/object), so it is only present
after the `PaymentIntent` is confirmed.

Card brand Merchant category Extended authorization validity window VisaHotel,
lodging, vehicle rental, and cruise line30 days*
**Visa**

Aircraft rental, bicycle rental (including electric scooters), boat rental,
clothing and costume rental, DVD and video rental, equipment and tool rental,
furniture rental, motor home rental, motorcycle rental, and trailer parks and
campgrounds

10 days**

Mastercard (not including Maestro or Cirrus cards)All merchant categories30
daysAmerican ExpressLodging and vehicle rental30 days***DiscoverAirline, bus
charter/tour, car rental, cruise line, local/suburban commuter, passenger
transportation including ferries, hotel, lodging, and passenger railway30 days
* The exact extended authorization window is 29 days and 18 hours, to allow time
for clearing processes.** The exact extended authorization window is 9 days and
18 hours, to allow time for clearing processes.*** While your validity window is
extended to 30 days, you must capture the authorized funds no later than the end
of the duration of your customer’s stay or rental.

## Links

- [confirmed](https://docs.stripe.com/api/payment_intents/confirm)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents/object)
-
[Interac](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#interac-payments)
-
[eftpos](https://docs.stripe.com/terminal/payments/regional?integration-country=AU#eftpos-payments)
- [support](https://support.stripe.com/contact)
- [Connect](https://docs.stripe.com/connect)
- [set the merchant category code](https://docs.stripe.com/connect/setting-mcc)
-
[request_extended_authorization](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_extended_authorization)
-
[capture_method](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
-
[capture_before](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-capture_before)
- [PaymentIntent
status](https://docs.stripe.com/payments/paymentintents/lifecycle)
- [Charge](https://docs.stripe.com/api/charges/object)