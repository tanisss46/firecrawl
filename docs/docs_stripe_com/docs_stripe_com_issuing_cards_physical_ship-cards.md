# Ship cards

## Select the shipping speed for your card.

Stripe offers two options for how to ship your cards: individual and bulk.

- **Individual**: Each card is affixed to a carrier and shipped in an envelope
addressed to the cardholder.
- **Bulk**: All cards issued to the same shipping address and shipment recipient
name on a given day are batched together into a single box and are shipped
without carriers or envelopes. There is a maximum of 2,000 cards per box. The
recipient of a bulk issuance must meet all applicable PCI certification
requirements. For more details, see [Bulk
issuance](https://docs.stripe.com/issuing/cards/physical/bulk-issuance).

## Select service type

Stripe offers a variety of shipping services with different cost points,
shipping speeds, and tracking capabilities.

- Cards created are batched and sent to our printer for fulfillment at 6 am
(UTC) the next day.
- Card orders have tracking numbers where indicated. These are available in the
Dashboard 24 hours after card creation.
- You can ship card orders to any [non-restricted
country](https://docs.stripe.com/issuing/cards/physical/ship-cards#shipping-country-restrictions).
- After your card order ships, we deduct associated card fees directly from your
Stripe balance. You can see all of your account’s card fees in the
[Dashboard](https://dashboard.stripe.com/test/balance/overview).
United StatesEurope (UK merchants)Europe (EU merchants)
The following shipping options and pricing apply to shipments originating from
the US:

- Use the shipping service parameter to set the delivery service: standard,
express, or priority.
- Use the shipping type parameter to set your shipment packaging: individual or
bulk.
- Use the `require_signature` shipping parameter to set the signature
preference. Not all shipping methods support signatures on delivery.
- Use the `shipping phone_number` to specify a phone number our courier partners
can use to contact the shipping recipient in the event of a card delivery issue.
For individual shipments to the EU or UK, if a phone number isn’t provided, we
provide the carrier with the phone number of the cardholder.

You can only send shipments without tracking numbers to addresses in the US or
Canada.

DestinationServiceEstimated arrival timeTrackingIndividual costBulk
costSignature on delivery1DomesticStandard (USPS)5-8 business days0.632
USDExpress4-5 business days13 USD27 USD+3Priority2-3 business days27 USD45
USD+3InternationalStandard (Canada only)8-12 business days1.503 USDExpress4-9
business days30 USD50 USD+4Priority3-6 business days40 USD60 USD+4
1No signature is the default setting. The above charges apply when signature on
delivery is selected. 2The Domestic Standard Individual rate is based on the
current metered letter rate as set by USPS and prices are subject to change.
3The International Standard Individual rate is based on the current first-class
mail international rate as set by USPS and prices are subject to change.

## Best practices for shipping cards

To make sure we successfully deliver your cards, follow the below
recommendations. We also offer address validation features to avoid unsuccessful
delivery attempts.

- **Business name inclusion**: Include the business name as part of address line
1 or line 2 when delivering to business addresses, especially when multiple
businesses share a building.
- **Apartment numbers**: Always provide apartment numbers when applicable for
residential addresses.
- **Consignee phone number**: When placing Express and Priority card orders,
include a local phone number. In the event of delivery issues, the courier
contacts you through this number.
- **Shipping to an APO, FPO, or PO Box**: When sending shipments to an army post
office (APO), fleet post office (FPO), or PO Box, shipping must be through USPS.
- **EORI numbers for UK and EU shipments**: To expedite customs when shipping to
the UK or European Union, provide an Economic Operators Registration and
Identification (EORI) reference number. The format is typically a two-letter
country code followed by 12-15 numbers (for example, GB123456789123456). For
bulk issuance, the EORI reference number is mandatory. For more information, see
the [shipping.customs.eori_number
field](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-customs-eori_number).
- **Canadian postal codes**: Don’t include a space. For example, enter M5V 3L9
as M5V3L9.
- **Validate the address**: Use the [address validation
API](https://docs.stripe.com/issuing/cards/physical/address-validation) to make
sure your shipping address is deliverable.

## Shipping country restrictions

You can ship a card to any country except for the following:

- Afghanistan
- Albania
- Algeria
- Angola
- Bangladesh
- Barbados
- Belarus
- Belize
- Benin
- Bolivia
- Brazil
- Burkina Faso
- Burundi
- Cambodia
- Cameroon
- Cape Verde
- Cayman Islands
- Central African Republic
- Chad
- China
- Colombia
- Comoros
- Congo, Dem. Rep.
- Congo, Rep.
- Cote d’Ivoire
- Cuba
- Egypt
- Equatorial Guinea
- Eritrea
- Ethiopia
- Fiji
- Gabon
- Guinea
- Guinea-Bissau
- Haiti
- Honduras
- India
- Iran
- Iraq
- Jamaica
- Jordan
- Kenya
- North Korea
- Kyrgyz Republic
- Lao PDR
- Lebanon
- Lesotho
- Liberia
- Libya
- Madagascar
- Maldives
- Mali
- Marshall Islands
- Mauritania
- Mexico
- Morocco
- Mozambique
- Myanmar
- Nepal
- Nicaragua
- Niger
- Nigeria
- Pakistan
- Palau
- Palestinian Territories
- Panama
- Papua New Guinea
- Paraguay
- Philippines
- Russian Federation
- Rwanda
- Sao Tome and Principe
- Senegal
- Seychelles
- Sierra Leone
- Solomon Islands
- Somalia
- South Africa
- South Sudan
- Sri Lanka
- St. Lucia
- Sudan
- Suriname
- Swaziland
- Syrian Arab Republic
- Tajikistan
- Tanzania
- Thailand
- Timor-Leste
- Togo
- Tonga
- Tunisia
- Turkey
- Turkmenistan
- Uganda
- Ukraine
- Vanuatu
- Venezuela
- Vietnam
- Yemen
- Zambia
- Zimbabwe

## Update or cancel card shipments

You can update your card’s
[shipment](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-shipping)
even after issuing your card, including the shipping service and address,
through the [Dashboard](https://dashboard.stripe.com/issuing/cards) and [Update
a card API](https://docs.stripe.com/api/issuing/card/update). After the card is
submitted to the third-party printer for fulfillment, you can no longer update
your shipment.

You can cancel a card at any time to make it inactive and unusable. If it’s
submitted to the vendor before the cancellation occurs, it’s still billed and
shipped.

## Links

- [Bulk issuance](https://docs.stripe.com/issuing/cards/physical/bulk-issuance)
- [Dashboard](https://dashboard.stripe.com/test/balance/overview)
- [shipping.customs.eori_number
field](https://docs.stripe.com/api/issuing/cards/object#issuing_card_object-shipping-customs-eori_number)
- [address validation
API](https://docs.stripe.com/issuing/cards/physical/address-validation)
-
[shipment](https://docs.stripe.com/api/issuing/cards/update#update_issuing_card-shipping)
- [Dashboard](https://dashboard.stripe.com/issuing/cards)
- [Update a card API](https://docs.stripe.com/api/issuing/card/update)