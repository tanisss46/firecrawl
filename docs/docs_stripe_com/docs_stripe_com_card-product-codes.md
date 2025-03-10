# Card Product Codes

## Learn about product codes for cards.

Product codes exist as a way to identify the specific program or product
associated with a credit card.

## Retrieving product codes

When using the [Payment Intents
API](https://docs.stripe.com/payments/payment-intents) for e-commerce payments,
Stripe stores the product code on the
[PaymentMethod](https://docs.stripe.com/api#payment_methods) object, in the
`brand_product` field within the `card_present` hash. After successfully
confirming a PaymentIntent, the `brand_product` field also includes the product
code in the
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)
for the corresponding charge in the API response for
[card_present](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present)
payments (using [Terminal](https://docs.stripe.com/terminal)).

The `brand_product` field might be `null` if the product code hasn’t been
collected yet (for example, when creating a card) or the product codes for the
particular card network aren’t supported. We currently support Visa and
Mastercard product codes only.

## Product codes

The following table lists product code values for each card brand:

VisaMastercardProduct code Product description ATraditionalBTraditional
RewardsCSignatureDSignature PreferredDSDistributionFClassicF2Visa Flexible
CredentialF3Visa Flexible Credential StandardGBusinessG1Signature
BusinessG3Platinum BusinessG4Infinite BusinessG5Business RewardsGVGovernment
DisbursementIInfiniteI1Infinite
PrivilegeI2UHNWJ3HealthcareKCorporateK1Government
CorporateLElectronNPlatinumN1RewardsN2SelectPGoldPPPayrollQPrivate
LabelQ2Private Label BasicQ3Private Label StandardQ4Private Label
EnhancedQ5Private Label SpecializedQ6Private Label
PremiumRProprietarySPurchasingS1Purchasing With FleetS2Government
PurchasingS3Government Purchasing With FleetS4Commercial AgricultureS5Commercial
TransportS6Commercial MarketplaceS7DistributionUTravel MoneyVV PayXVisa
Commercial Choice TravelX1Visa Commercial Choice Omni
## Testing

While in test mode, use the following test cards to simulate purchases made with
specific card product codes, which are returned in the `brand_product` field.
Each test card takes any future date as the expiration, any three-digit value as
the CVV, and any postal code.

Description NumberProduct codeMastercard Standard
Debit5555050360000007MDSMastercard Platinum Debit5555050360000015MDPMastercard
World Credit5200000360000076MCWMastercard World Elite
Credit5200000360000068MWEMastercard World Elite for Business
Credit5200500000100004MAB

## Links

- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [PaymentMethod](https://docs.stripe.com/api#payment_methods)
-
[payment_method_details](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details)
-
[card_present](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present)
- [Terminal](https://docs.stripe.com/terminal)