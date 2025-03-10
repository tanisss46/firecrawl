# Physical cards address validation

## Enable and manage address validation features for physical cards.

Stripe Issuing needs accurate and properly formatted shipping addresses to
ensure successful delivery of physical cards to their intended recipient. Cards
sent to invalid addresses get returned to Stripe, but the delivery attempt and
the eventual return can take over 2 weeks to complete. Returned cards can create
an operational burden, increase your overall costs, and delay your cardholders’
receipt of your physical cards.

To maximize your delivery success, Stripe’s Cards API has built-in address
normalization and validation. Stripe compares the shipping address you provide
to a third-party address database and identifies or fixes any issues with the
address.

## Address normalization

Normalization ensures that your addresses adhere to the standards of the
shipment’s country while also correcting any obvious errors in your addresses.

Examples of normalization include:

### Address standardization to ensure proper formatting

```
// Before
"shipping": {
 "address": {
"line1": "354 Oyster Point Blvd South San Francisco, CA 94080", // incorrectly
formatted line1
 "city": "South San Francisco",
 "postal_code": "94080",
 "state": "CA",
 "country": "US"
 }
}

// After
"shipping": {
 "address": {
 "line1": "354 OYSTER POINT BLVD",
 "city": "SOUTH SAN FRANCISCO",
 "postal_code": "94080",
 "state": "CA",
 "country": "US"
 }
}
```

### Address correction to apply corrections found from matching with an existing validated address

```
// Before
"shipping": {
 "address": {
 "line1": "354 Oyster Point",
 "city": "South San Francisco",
 "postal_code": "94080",
 "state": "NM", // incorrect state with an available correction
 "country": "US"
 }
}

// After
"shipping": {
 "address": {
 "line1": "354 OYSTER POINT BLVD", // added BLVD suffix
 "city": "SOUTH SAN FRANCISCO",
 "postal_code": "94080",
 "state": "CA", // corrected state
 "country": "US"
 }
}
```

The normalized address is included in the [address
validation](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation)
hash that is returned after successfully creating a physical card or updating a
card’s shipping address with address normalization enabled.

### Sample address validation

```
"shipping": {
 // address supplied during card creation
 "address": {
 "line1": "354 Oyster Point Blvd South San Francisco, TX 94080",
 "city": "South San Francisco",
 "postal_code": "94080",
 "state": "TX",
 "country": "US"
 },
 // address validation hash
 "address_validation": {
 // the normalized address
 "normalized_address": {
 "line1": "354 OYSTER POINT BLVD",
 "city": "SOUTH SAN FRANCISCO",
 "state": "CA",
 "postal_code": "94080",
 "country": "US"
 },
 "mode": "validation_and_normalization",
 "result": "likely_deliverable"
 }
}
```

## Address validation

Validation determines whether your address is deliverable by attempting to match
to an existing, validated address and is done after applying normalization.

The result of this validation is included in the address validation hash.
Depending on the [address validation
mode](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation-mode)
used this might result in an API error.

ResultDescription`likely_deliverable`If a partially matching or fully matching
address is found in our third party database, your address is considered likely
deliverable.`likely_undeliverable`If no matching or partially matching address
is found in our third party database, your address is considered likely
undeliverable.`indeterminate`The deliverability of the address couldn’t be
determined.
For example, the previous example showed the validation result of
`likely_deliverable`.

```
"address_validation": {
 // the normalized address
 "normalized_address": {
 "line1": "354 OYSTER POINT BLVD",
 "city": "SOUTH SAN FRANCISCO",
 "state": "CA",
 "postal_code": "94080",
 "country": "US"
 },
 "mode": "validation_and_normalization",
 // the result showing that address was validated to be likely deliverable
 "result": "likely_deliverable"
}
```

## Managing address validation features with address validation modes

The Cards API supports three address validation modes, which can optionally be
specified in the
[address_validation](https://docs.stripe.com/api/issuing/cards/create#create_issuing_card-shipping-address_validation)
parameter when creating a physical card or updating a card’s shipment.

ModeDescription`validation_and_normalization`Validates and normalizes your
card’s shipping address before submitting it for fulfillment. Stripe attempts to
automatically apply any appropriate corrections and formatting to your address
before determining deliverability. If the card’s shipping address is likely
undeliverable, you get an API request error.`normalization_only`Normalizes your
card’s shipping address before submitting it for fulfillment, and applies any
appropriate corrections and formatting to your address. Address deliverability
isn’t enforced, and you don’t get an API request error.`disabled`Ships your card
using the address provided as-is, without applying any normalization or
validating its deliverability. This is only recommended when an address is known
to be correct or otherwise validated.
Use `validation_and_normalization` for the address validation mode. We also
provide alternate modes depending on your scenario:

- `disabled`: If you believe a card is incorrectly blocked.
- `normalization only`: If you want to minimize API errors but still gain the
benefits of normalization. The default is `normalization_only` if not specified.

### Validation and normalization

Your card is shipped with the validated, normalized address. Address
deliverability is enforced, and the API errors if the address is likely
undeliverable. Stripe strongly recommends using this mode to ensure
deliverability for the address.

```
curl https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d cardholder=ich_1Cm3pZIyNTgGDVfzI83rasFP \
 -d type=physical \
 -d currency=usd \
 -d "shipping[name]"="Jenny Rosen" \
 -d "shipping[address][line1]"="1234 Fake St" \
 -d "shipping[address][city]"="Fake City" \
 -d "shipping[address][state]"=NY \
 -d "shipping[address][country]"=US \
 -d "shipping[address][postal_code]"=94111 \
 -d "shipping[address_validation][mode]"=validation_and_normalization
```

```
"error": {
 "message": {
"The address is undeliverable based on given inputs. Please ensure that the
address was inputted correctly and can be delivered to."
 }
}
```

### Normalization only

Your card will be shipped with the normalized address. Address deliverability
isn’t enforced, and you don’t get an API request error if the address is likely
undeliverable.

```
curl https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d cardholder=ich_1Cm3pZIyNTgGDVfzI83rasFP \
 -d type=physical \
 -d currency=usd \
 -d "shipping[name]"="Jenny Rosen" \
 -d "shipping[address][line1]"="1234 Fake St" \
 -d "shipping[address][city]"="Fake City" \
 -d "shipping[address][state]"=NY \
 -d "shipping[address][country]"=US \
 -d "shipping[address][postal_code]"=94111 \
 -d "shipping[address_validation][mode]"=normalization_only
```

```
# Example response
{
 "id": "ic_test1CDR9auHsQKan42gGK34",
 "object": "issuing.card",
 "shipping": {
 // address supplied during card creation
 "address": {
 "line1": "1234 Fake Street",
 "city": "Fake city",
 "postal_code": "94111",
 "state": "NY",
 "country": "US"
 },
 // address validation information
 "address_validation": {
 // the card will be shipped with this address
 "normalized_address": {
 "line1": "1234 FAKE ST",
 "city": "FAKE CITY",
 "state": "NY",
 "postal_code": "94111",
 "country": "US"
 },
 "mode": "normalization_only",
 "result": "likely_undeliverable"
 },
 // other fields...
 },
 // other fields...
}
```

### Disabled

This mode ships your card using the address provided as-is, without applying
normalization or validating its deliverability. A normalized address and
validation result will not be returned. This is recommended only when an address
is known to be correct or otherwise validated.

```
curl https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d cardholder=ich_1Cm3pZIyNTgGDVfzI83rasFP \
 -d type=physical \
 -d currency=usd \
 -d "shipping[name]"="Jenny Rosen" \
 -d "shipping[address][line1]"="1234 Fake St" \
 -d "shipping[address][city]"="Fake City" \
 -d "shipping[address][state]"=NY \
 -d "shipping[address][country]"=US \
 -d "shipping[address][postal_code]"=94111 \
 -d "shipping[address_validation][mode]"=disabled
```

```
// Example response
{
 "id": "ic_test1CDR9auHsQKan42gGK34",
 "object": "issuing.card",
 "shipping": {
 // address supplied during card creation
 "address": {
 "line1": "1234 Fake Street",
 "city": "Fake city",
 "postal_code": "94111",
 "state": "NY",
 "country": "US"
 },
 // address validation information
 "address_validation": {
 "mode": "disabled"
 },
 // other fields...
 },
 // other fields...
}
```

## Integrating address validation into your card creation flow

We provide several examples on how to integrate your flow with address
validation features below. These examples are not exhaustive, and are only meant
to serve as ideas to help you with your integration.

Synchronous card creationAsynchronous card creation
### Strict address validation

The best way to increase deliverability is to never bypass address validation,
requiring your customers to always submit deliverable addresses.

Customer

Your site

Stripe

Submit shipping details with an undeliverable address to order a card

Create a [Card](https://docs.stripe.com/api/issuing/cards/create) with
`validation_and_normalization`
[mode](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation-mode)

Card shipping address determined to be `likely_undeliverable`

Send error `400` undeliverable shipping address response

Prompt user to correct their invalid address

Correct and re-submit shipping address

Create a [Card](https://docs.stripe.com/api/issuing/cards/create) with
`validation_and_normalization`
[mode](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation-mode)

Card shipping address determined to be `likely_deliverable`

Return a [Card](https://docs.stripe.com/api/issuing/cards/object)

Strict address validation flow
### Address suggestions

Prompting a user to select between a suggested address and the one they provided
is a common flow that you can build yourself using our address validation
features.

Customer

Your site

Stripe

Submit shipping details to order a card

Create a [Card](https://docs.stripe.com/api/issuing/cards/create) with
`validation_and_normalization`
[mode](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation-mode)

Card shipping address is normalized and determined to be `likely_deliverable`

Return a new [Card](https://docs.stripe.com/api/issuing/cards/object) with
validated and normalized address

Suggest a better address using the card’s
[normalized_address](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation-normalized_address)

Confirm address selection

If the original address is selected, update
[Card](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-shipping)
to original address using `disabled`
[mode](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation-mode)

Return the updated [Card](https://docs.stripe.com/api/issuing/cards/object)

Address suggestion flow
### Relaxed address validation

You can gracefully handle undeliverable address errors by requiring the user to
confirm the address they submitted. By leveraging the `disabled` address
validation mode, you can make sure that your customers are able to order cards
without much friction if their address is known to be correct.

Customer

Your site

Stripe

Submit shipping details to order a card

Create a [Card](https://docs.stripe.com/api/issuing/cards/create) with
`validation_and_normalization`
[mode](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation-mode)

Card shipping address determined to be `likely_undeliverable`

Send error `400` undeliverable shipping address response

Show prompt asking if provided address is correct

Confirm submitted address is correct

Create a [Card](https://docs.stripe.com/api/issuing/cards/create) with
`disabled`
[mode](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation-mode)

Return a [Card](https://docs.stripe.com/api/issuing/cards/object)

Relaxed address validation flow
## Testing address validation

You can supply a magic value for `line1` to trigger certain validation
conditions in test mode. You must pass in legitimate values for the `city`,
`state`, and `postal_code` arguments.

ValueType`address_valid`Send a test mode request using a deliverable shipping
address.`address_invalid`Send a test mode request using an undeliverable
shipping address.
```
curl https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d cardholder=ich_1Cm3pZIyNTgGDVfzI83rasFP \
 -d type=physical \
 -d currency=usd \
 -d "shipping[name]"="Jenny Rosen" \
 -d "shipping[address][line1]"=address_invalid \
 -d "shipping[address][city]"="San Francisco" \
 -d "shipping[address][state]"=CA \
 -d "shipping[address][country]"=US \
 -d "shipping[address][postal_code]"=94111 \
 -d "shipping[address_validation][mode]"=validation_and_normalization
```

## Links

- [address
validation](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation)
- [address validation
mode](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation-mode)
-
[address_validation](https://docs.stripe.com/api/issuing/cards/create#create_issuing_card-shipping-address_validation)
- [Card](https://docs.stripe.com/api/issuing/cards/create)
- [Card](https://docs.stripe.com/api/issuing/cards/object)
-
[normalized_address](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-address_validation-normalized_address)
-
[Card](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-shipping)