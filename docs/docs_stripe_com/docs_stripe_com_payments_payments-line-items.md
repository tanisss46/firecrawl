# Payments line itemsPrivate preview

## Send additional transaction metadata across supported Payment Method Types to access cost savings, facilitate payment reconciliation, and improve auth rates.

#### Contact to enable

Contact your sales representative or [support](https://support.stripe.com/) to
enable this private preview feature.

Payment line items is a feature in the Payment Intents API that provides
benefits for cards and local payment methods processing.

- **Cost savings for eligible commercial cards for IC+ users:** By passing
payment line items, you can participate in the Level 2/Level 3 (L2/L3) program
that major card networks administer. For eligible commercial cards, passing line
item data can provide interchange fee savings.
- **Facilitate reconciliation:** In cases where there are no cost savings,
passing line item data can facilitate reconciliation for your customers. For
example, if you primarily serve government customers, it will aid the customer
in reconciling a purchase against what shows up on their statement.
- **Improved authorization rates:** Payment methods like PayPal and Klarna use
line item data in their underwriting models, potentially allowing them to
approve more payments when line items data is passed.

## Feature restrictions

Payment line items have the following restrictions across supported payment
method types:

Cards L2/L3 programKlarnaPayPalGeographic availabilityOnly supported for US
domestic transactions (US user accepting US issued cards, excluding US
territories)Klarna is a global payment method. For business location support,
see [Klarna payments](https://docs.stripe.com/payments/klarna).Available for
customers in all locations. For business location support, see [PayPal
payments](https://docs.stripe.com/payments/paypal).Card networksOnly supported
for Visa, Mastercard, and American Express (cost savings requires direct
agreement with American Express)Not applicableNot applicableNumber of line
itemsCurrently supports 100 line items (maximum of 4 line items for American
Express)Same as cardsSame as cardsFeature compatibilityOnly auto and separate
authorization and capture modes work with payment line items. You can’t
currently use [flexible payment
scenarios](https://docs.stripe.com/payments/flexible-payments) or [decremental
authorization](https://docs.stripe.com/payments/decremental-authorization) for
transactions where you’re passing in payment line items.Same as cardsSame as
cardsIndustry specific metadataYou can’t send line items alongside industry
specific metadata (such as [car
rental/lodging](https://docs.stripe.com/travel-entertainment-data?industry-data=sending-industry-data-lodging),
and airlines).Same as cards. Klarna supports industry specific metadata with
Extra Merchant Data.Same as cardsSurfacesOnly available for payments made
through the [PaymentIntents
API](https://docs.stripe.com/payments/payment-intents).Same as cardsSame as
cards
## Cards L2/L3 Rates Eligibility

See [Industry to MCC
codes](https://docs.stripe.com/payments/payments-line-items#industry-to-mcc-codes)
to see what MCC your business might fall under.

Stripe API doesn’t reject line items that don’t meet the network MCC or tax
requirements. However, these transactions don’t qualify for the corresponding
Level 2/3 savings.

Cards L2/L3 Rates EligibilityLevel 2Level 3Card typesOnly Business, Purchasing,
and Corporate cards are eligibleOnly Purchasing and Corporate cards are
eligibleMCCsUsers with the following MCCs aren’t eligible for Level II:- For
**Mastercard**: 5812, 3501-3999, 7011, 3351-3500, 7512, 7513, 7519, 3000-3299,
4511, 4112, 8398, 4468, 5541, 5542, 5499, 5983
- For **Visa**: 5812, 5814, 3501-4010, 3351-3500, 7512, 7513, 3000-3299, 4511,
4411, 4112, 4722, 5962, 5966, and 5967
Users with the following MCCs aren’t eligible for Level III:- For
**Mastercard**: 5812, 3501-3999, 7011, 3351-3500, 7512, 7513, 7519, 3000-3299,
4511, 4112
- For **Visa**: 5812, 5814, 3501-4010, 3351-3500, 7512, 7513, 3000-3299, 4511,
4411, 4112, 4722, 5962, 5966, and 5967
Sales tax requirement- For Visa: sales tax must be between 0.1% and 22% unless
the business is one of the following MCCs - 4468, 5499, 5541, 5542, and 5983
- For Mastercard: sales tax must be between 0.1% and 30%, unless the business is
in one of the following MCCs - 4468, 5541, 5542, 5499, 5983, 7511, 9752, 4111,
4131, 4215, 4784, 8211, 8220, 8398, 8661, 9211, 9222, 9311, 9399, 9402
Not applicable
## Field Requirements

All the fields mentioned below are passed inside
[amount_details](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-amount_details).
Refer to [Sample request (Level II
data)](https://docs.stripe.com/payments/payments-line-items#sample-request-(level-ii-data))
to learn about passing data.

### Cards Supported fields

#### Private preview

Two more fields [Commodity Code] and [Unit of Measure] aren’t yet available in
private preview, but will become required for the **Visa CEDP program** (refer
to Network Cost Updates for Feb 20, 2025).

Field NameTypeValues / RestrictionsDescriptionRequired For L2/L3Required API
Fieldspayment_details[customer_reference]stringThis field isn’t available for
non-card payments.Some customers might be required by their company or
organization to provide this information. If so, provide this value. Otherwise
you can ignore this field.
payment_details[order_reference]

string

This field isn’t available for non-card payments.

If
[automatic_payment_methods.enabled](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-automatic_payment_methods-enabled)
is set to `true`, you must set this field as Card is a default [Payment
Method](https://docs.stripe.com/payments/payment-methods).

A unique value assigned by the business to identify the transaction.

✅ L2/L3

discount_amountintegerValue must be > 0The total discount applied on the
transaction represented in the [smallest currency
unit](https://docs.stripe.com/currencies#zero-decimal).shipping[to_postal_code]stringMax
length 10 chars. Value must be alphanumeric charactersIf a physical good is
being shipped, the postal code of where it’s being shipped
to.shipping[from_postal_code]stringMax length 10 chars. Value must be
alphanumeric charactersIf a physical good is being shipped, the postal code of
where it’s being shipped from.shipping[amount]integerValue must be >= 0If a
physical good is being shipped, the cost of shipping represented in the
[smallest currency
unit](https://docs.stripe.com/currencies#zero-decimal).tax[total_tax_amount]integerValue
must be >= 0The total amount of tax on the transaction.✅
L2line_items[tax][total_tax_amount]integerValue must be >= 0The total amount of
tax on a single line item represented in the [smallest currency
unit](https://docs.stripe.com/currencies#zero-decimal).✅
L3line_items[product_name]stringMax length 100 charsThe product name of the line
item.✅ L3✅line_items[product_code]stringMax length 12 charsThe product code of
the line item, such as an SKU.✅ L3line_items[unit_cost]integerValue must be >=
0The unit cost of the line item represented in the [smallest currency
unit](https://docs.stripe.com/currencies#zero-decimal).✅
L3✅line_items[quantity]integerValue must be > 0The quantity of items.✅
L3✅line_items[discount_amount]integerValue must be > 0The discount applied on
this line item represented in the [smallest currency
unit](https://docs.stripe.com/currencies#zero-decimal).
#### Note

The following fields are mutually exclusive; you can provide only one in a
request:

- Either `tax[total_tax_amount]` or `line_items[tax][total_tax_amount]`
- Either `discount_amount` or `line_items[discount_amount]`

### Additional Klarna supported fields

Klarna supports the above fields for cards, and in addition, also supports:

Field NameTypeValues and
RestrictionsDescriptionRequiredline_items[payment_method_options][klarna][product_url]stringMax
1024 characters. Rough Regex:
`https?:\/\/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,64}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)`Valid
http or https URL of the
productline_items[payment_method_options][klarna][image_url]stringMax 1024
characters. Rough Regex:
`https?:\/\/[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,64}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)`Valid
http or https URL of the image
#### Note

For Klarna transactions, total amount is implicitly derived from the formula
`(unit_cost * quantity) - discount_amount + tax.total_tax_amount`. There is no
explicit field to pass the amount.

### Additional PayPal Supported Fields

PayPal supports the above fields for cards, and in addition, also supports:

Field NameTypeValues /
RestrictionsDescriptionRequiredline_items[payment_method_options][paypal][description]stringMax
127 charactersDescription of the line
item.line_items[payment_method_options][paypal][category]enumdigital_goods,
physical_goods, donationType of the line
item.line_items[payment_method_options][paypal][sold_by]stringMax 127
charactersThe Stripe account ID of the connected account that sells the item.
## Cards-specific line items for L2/L3 rates

Pass in required data for eligible cards to qualify for L2/L3 network programs

- Level II: sales tax charged on transactions
- Level III: line item level breakdown such as product code, quantity, unit cost
Level IILevel III
### Sample request (Level II data)

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=4600 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d "payment_details[customer_reference]"=customer_reference \
 -d "payment_details[order_reference]"=order_reference \
 -d "amount_details[tax][total_tax_amount]"=500
```

### Sample response

```
{
 id: "pi_3OoMm5BLxXjrKOiR3LRyi610",
 amount: 4600,
 currency: "usd"
 amount_details: {
 tax: {
 total_tax_amount: 500
 },
 },
 status: "requires_payment_method"
}
```

### Payment Intent Confirmation

Create and confirm togetherCreate and confirm separately
```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=4600 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d payment_method=pm_card_visa \
 -d "payment_details[customer_reference]"=customer_reference \
 -d "payment_details[order_reference]"=order_reference \
 -d "amount_details[full_hash]"="as shown above" \
 -d confirm=true
```

### PaymentIntent capture

Capture the PaymentIntent separately after confirmation by passing in
`manual_capture: true` during PaymentIntent Creation or Confirmation, and then
call the Capture endpoint separately.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=4600 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d "payment_method_types[]"=paypal \
 -d "payment_details[customer_reference]"=customer_reference \
 -d "payment_details[order_reference]"=order_reference \
 -d "amount_details[full_hash]"="as shown above" \
 -d confirm=true \
 -d capture_method=manual
```

Pass in an updated `amount_details` hash during Capture if needed.

Capture the already persisted amount detailsUpdate amount details during capture
```
curl -X POST https://api.stripe.com/v1/payment_intents/pi_xxxxxxxx/capture \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

## Payment Method Specific line items

Pass in additional payment method types on a per-line-item basis all in one
place. You can pass in data related to payment methods you might not be
confirming with as well, as long as the parameter is supported. This can
simplify your integration, without requiring engineering effort to add and
remove payment method specific fields for each payment method.

#### Note

Line items are not included by default in the API response. To return line
items, [expand](https://docs.stripe.com/expand#includable-properties)
`amount_details.line_items`

### Sample request

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=4600 \
 -d currency=usd \
 -d "payment_method_types[0]"=card \
 -d "payment_method_types[1]"=paypal \
 -d "payment_method_types[2]"=klarna \
 -d "payment_details[customer_reference]"=customer_reference \
 -d "payment_details[order_reference]"=order_reference \
 -d "amount_details[discount_amount]"=0 \
 -d "amount_details[shipping][from_postal_code]"=94110 \
 -d "amount_details[shipping][to_postal_code]"=94117 \
 -d "amount_details[shipping][amount]"=100 \
 -d "amount_details[tax][total_tax_amount]"=500 \
 -d "amount_details[line_items][0][product_code]"=SKU001 \
 -d "amount_details[line_items][0][product_name]"="Product 001" \
 -d "amount_details[line_items][0][unit_cost]"=2000 \
 -d "amount_details[line_items][0][quantity]"=1 \
 -d "amount_details[line_items][0][discount_amount]"=0 \
 -d "amount_details[line_items][0][tax][total_tax_amount]"=100 \
--data-urlencode
"amount_details[line_items][0][payment_method_options][klarna][image_url]"="https://www.example.com/image.jpg"
\
--data-urlencode
"amount_details[line_items][0][payment_method_options][klarna][product_url]"="https://www.example.com/product"
\
-d
"amount_details[line_items][0][payment_method_options][paypal][description]"="This
is a sample product description unique to PayPal for SKU001" \
-d
"amount_details[line_items][0][payment_method_options][paypal][category]"=digital_goods
\
 -d "amount_details[line_items][1][product_code]"=SKU002 \
 -d "amount_details[line_items][1][product_name]"="Product 002" \
 -d "amount_details[line_items][1][unit_cost]"=1800 \
 -d "amount_details[line_items][1][quantity]"=1 \
 -d "amount_details[line_items][1][discount_amount]"=0 \
 -d "amount_details[line_items][1][tax][total_tax_amount]"=100 \
--data-urlencode
"amount_details[line_items][1][payment_method_options][klarna][image_url]"="https://www.example.com/image.jpg"
\
--data-urlencode
"amount_details[line_items][1][payment_method_options][klarna][product_url]"="https://www.example.com/product"
\
-d
"amount_details[line_items][1][payment_method_options][paypal][description]"="This
is a sample product description unique to PayPal for SKU002" \
-d
"amount_details[line_items][1][payment_method_options][paypal][category]"=physical_goods
\
 -d "expand[0]"="amount_details.line_items"
```

### Sample response

```
{
 id: "pi_3OoMm5BLxXjrKOiR3LRyi610",
 amount: 4600,
 currency: "usd"
 amount_details: {
 shipping: {
 from_postal_code: "94110",
 to_postal_code: "94117",
 amount: 100
 },
 tax: {
 total_tax_amount: 500
 },
 line_items: {
 object: "list",
url:
"/v1/payment_intents/pi_3OoMm5BLxXjrKOiR3LRyi610/amount_details_line_items",
 has_more: false,
 data: [{
 _id: "li_123",
 product_code: "SKU001",
 product_name: "Product 001",
 unit_cost: 2000,
 quantity: 1,
 discount_amount: 0,
 tax: {
 total_tax_amount: 100
 },
 payment_method_options: {
 klarna: {
 image_url: "https://www.example.com/image.jpg",
 product_url: "https://www.example.com/product"
 },
 paypal: {
description: "This is a sample product description unique to PayPal for SKU001",
 category: digital_goods,
 }
 }
 },
 {
 _id: "li_456",
 product_code: "SKU002",
 product_name: "Product 002",
 unit_cost: 1800,
 quantity: 1,
 discount_amount: 0,
 tax: {
 total_tax_amount: 100
 },
 payment_method_options: {
 klarna: {
 image_url: "https://www.example.com/image.jpg",
 product_url: "https://www.example.com/product"
 },
 paypal: {
description: "This is a sample product description unique to PayPal for SKU001",
 category: physical_goods,
 }
 }
 }
 ]
 }
 },
 status: "requires_payment_method"
}
```

## Industry to MCC codes

CategoryDescriptionFood & Beverage- **5812**: Restaurants (not fast food)
- **5814**: Fast Food Restaurants
Hospitality & Travel- **3000-3299**: Airlines
- **3501-3999, 7011**: Hotels & Lodging
- **3351-3500**: Car Rental Agencies
- **4722**: Travel Agencies and Tour Operators
- **7512**: Automobile Rental Agency
- **7513**: Truck Rental and Leasing
- **7519**: Motor Home and Recreational Vehicle Rental
- **4411**: Cruise Lines
- **4112**: Passenger Railways
- **4111**: Local and Suburban Commuter Transit
- **4215**: Courier Services
- **4784**: Bridge and Road Fees
- **4468**: Marinas, Marine Service
- **5983**: Fuel Dealers
Retail & E-Commerce- **5962**: Direct Marketing—Travel
- **5966**: Direct Marketing—Outbound Telemarketing
- **5967**: Direct Marketing—Other
Utilities & Miscellaneous- **8398**: Charitable and Social Service Organizations
- **9752**: U.K. Petrol Stations, Electronic Hot File
- **9211**: Court Costs, including Alimony and Child Support
- **9311**: Tax Payments
- **9222**: Fines
- **9402**: Postal Services – Government Only and other similar services
- **9399**: Government Services (Not Elsewhere Classified) and other similar
services
- **8661**: Religious Organizations
- **8211**: Schools and Educational Institutions
- **8220**: Colleges, Universities

## Links

- [support](https://support.stripe.com/)
- [IC+
users](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
- [Klarna payments](https://docs.stripe.com/payments/klarna)
- [PayPal payments](https://docs.stripe.com/payments/paypal)
- [flexible payment
scenarios](https://docs.stripe.com/payments/flexible-payments)
- [decremental
authorization](https://docs.stripe.com/payments/decremental-authorization)
- [car
rental/lodging](https://docs.stripe.com/travel-entertainment-data?industry-data=sending-industry-data-lodging)
- [PaymentIntents API](https://docs.stripe.com/payments/payment-intents)
-
[amount_details](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-amount_details)
-
[automatic_payment_methods.enabled](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-automatic_payment_methods-enabled)
- [Payment Method](https://docs.stripe.com/payments/payment-methods)
- [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal)
- [expand](https://docs.stripe.com/expand#includable-properties)
- [https://www.example.com/image.jpg](https://www.example.com/image.jpg)
- [https://www.example.com/product](https://www.example.com/product)