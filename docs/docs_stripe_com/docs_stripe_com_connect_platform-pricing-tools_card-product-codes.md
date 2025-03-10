# Card product codes in platform pricing tools

## Use card product codes with reference and test card numbers.

Product codes exist as a way to identify the specific program or product
associated with a credit card. Conditional fees in [pricing
schemes](https://docs.stripe.com/connect/platform-pricing-tools) can depend on
the product code of a card. The following tables contain examples of card
product codes and test card numbers.

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

- [pricing schemes](https://docs.stripe.com/connect/platform-pricing-tools)