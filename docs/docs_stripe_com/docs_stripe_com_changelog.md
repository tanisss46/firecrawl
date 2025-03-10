# Changelog

## Keep track of changes and upgrades to the Stripe API.

ProductBreaking changes
## Acacia

[Learn what's changing in Acacia](https://docs.stripe.com/changelog/acacia)
### 2025-02-24.acacia

#### Improved workflows for Checkout Sessions

[Adds support for blocking specific card brands in Checkout
SessionsCheckout](https://docs.stripe.com/changelog/acacia/2025-02-24/checkout_add_brands_blocked)[Checkout
Sessions now group customer information in one
fieldCheckout](https://docs.stripe.com/changelog/acacia/2025-02-24/checkout-sessions-collected-info)
#### More granular control of credit grants

[Credit grants can now be applied to specific
pricesBilling](https://docs.stripe.com/changelog/acacia/2025-02-24/billing-credits-price-level-applicability)[Credit
grants can now be
prioritizedBilling](https://docs.stripe.com/changelog/acacia/2025-02-24/billing-credits-priority)
#### More flexibility for buy now, pay later methods

[Makes shipping information an optional parameter for Afterpay
paymentsPayments](https://docs.stripe.com/changelog/acacia/2025-02-24/afterpay-shipping-details-optional)[Makes
billing country and email fields optional for Klarna
paymentsPayments](https://docs.stripe.com/changelog/acacia/2025-02-24/cs_make_billing_country_and_email_field_optional_for_klarna_payments)
#### Additional updates

[Adds metadata field to the Products API for creating an inline default
priceBilling](https://docs.stripe.com/changelog/acacia/2025-02-24/products-default-price-data-metadata-field)[Adds
ability to schedule debit payments for a specific
datePayments](https://docs.stripe.com/changelog/acacia/2025-02-24/target-date)
### 2025-01-27.acacia

#### Company details for Accounts

[Adds support for ownership exemption reason to the Accounts
APIConnect](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api)[Adds
directorship declaration to the Accounts
APIConnect](https://docs.stripe.com/changelog/acacia/2025-01-27/directorship-declaration)[Adds
proof of ultimate beneficial ownership as a document
typeConnect](https://docs.stripe.com/changelog/acacia/2025-01-27/proof-of-ultimate-beneficial-ownership-document-support)
#### Payment method enhancements

[Adds support for the Pay by Bank local payment methodCheckout+ 1
more](https://docs.stripe.com/changelog/acacia/2025-01-27/pay-by-bank-lpm)[Adds
PayPal country property to the PaymentMethods and Charge
objectsPayments](https://docs.stripe.com/changelog/acacia/2025-01-27/paypal-country)
#### Checkout enhancements

[Adds discounts field to Checkout
SessionsCheckout](https://docs.stripe.com/changelog/acacia/2025-01-27/checkout-sessions-discounts-field)[Adds
Sudan to allowed shipping countries for
CheckoutCheckout](https://docs.stripe.com/changelog/acacia/2025-01-27/checkout-sudan-shipping-support)
#### Additional updates

[Adds advice code to
ChargesPayments](https://docs.stripe.com/changelog/acacia/2025-01-27/charge-outcome-advice-code)[Modify
phone number collection on Payment LinksPayment
Links](https://docs.stripe.com/changelog/acacia/2025-01-27/add-phone-number-collection-update-payment-links-api)[Makes
Issuing and Treasury embedded components generally availableIssuing+ 1
more](https://docs.stripe.com/changelog/acacia/2025-01-27/issuing-treasury-embedded-components)[Adds
support for multiple financial accounts per
businessTreasury](https://docs.stripe.com/changelog/acacia/2025-01-27/multi-fa)[Adds
support for collecting tips in JPY currency to
TerminalTerminal](https://docs.stripe.com/changelog/acacia/2025-01-27/terminal-jp-supported-country)
### 2024-12-18.acacia

#### Payout enhancements

[Adds SDK support for trace
IDsPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/trace-id-sdk)[Adds
new balance transaction types to support minimum
balancePayouts](https://docs.stripe.com/changelog/acacia/2024-12-18/payout-minimum-balance)
#### Issuing enhancements

[Issuing authorizations now include merchant tax ID
numberIssuing](https://docs.stripe.com/changelog/acacia/2024-12-18/issuing-merchant-tax-id)[Creates
Issuing authorizations when Stripe is
unavailableIssuing](https://docs.stripe.com/changelog/acacia/2024-12-18/issuing-auths-when-stripe-unavailable)
#### Payment method enhancements

[Adds additional beneficiary information for bank transfer
paymentsPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/new-bank-transfer-beneficiary-information)[Adds
funding details to Amazon Pay and Revolut Pay
chargesPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/charge-pm-details)[Adds
support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefixCheckout+ 1
more](https://docs.stripe.com/changelog/acacia/2024-12-18/mandate-reference-prefix)
#### Tax enhancements

[Adds disabled reason to invoices, subscriptions, and schedulesTax+ 2
more](https://docs.stripe.com/changelog/acacia/2024-12-18/add-disabled-reason)[Adds
support for tax ID types in 19 new
countriesTax](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-ids-19-new-countries)[Adds
support for 21 new countries to the Tax Registration
APITax](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-registration-21-new-countries)
#### Billing enhancements

[Adds support for reinstating Billing Credits on Invoice voidingBilling+ 1
more](https://docs.stripe.com/changelog/acacia/2024-12-18/billing-credits-invoice-voiding)[Modify
trial subscriptions created by Payment LinksPayment
Links](https://docs.stripe.com/changelog/acacia/2024-12-18/add-trial-days-update-payment-links-api)[Billing
Portal Configuration always returns period end date in
responsesBilling](https://docs.stripe.com/changelog/acacia/2024-12-18/portal-config-schedule-at-period-end-required)
#### Additional updates

[Adds signature request as a replacement option for the Vault and Forward
APIAffects all
products](https://docs.stripe.com/changelog/acacia/2024-12-18/vault-and-forward-request-signature-replacement)[Adds
network advice and decline
codesPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/network-advice-code-network-decline-code)[Supports
redisplaying payment methods for Cards and
SourcesPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/cards-sources-allow-redisplay)[Adds
field-level permissions for revenue and worker count in an Account’s business
profileConnect](https://docs.stripe.com/changelog/acacia/2024-12-18/business-profile-revenue-worker-count)[Adds
network transaction ID to
chargesPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/charge-display-network-transaction-id)[Adds
regulated status field to card objects in several
APIsPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/regulated-status)
### 2024-11-20.acacia

#### Support for new tax types

[Adds support for Service Tax
typeTax](https://docs.stripe.com/changelog/acacia/2024-11-20/service_tax)[Adds
tax ID support for Liechtenstein
VATTax](https://docs.stripe.com/changelog/acacia/2024-11-20/li_vat)
#### Issuing enhancements

[Adds support for merchant amount and currency for test mode
authorizationsIssuing](https://docs.stripe.com/changelog/acacia/2024-11-20/add-merchant-currency-and-merchant-amount-on-create-testmode-authorization-method)[Adds
support for issuing fraud
challengesIssuing](https://docs.stripe.com/changelog/acacia/2024-11-20/issuing-fraud-challenges)
#### Additional payment flexibility

[Adds support for enabling Adaptive Pricing per Checkout
SessionCheckout](https://docs.stripe.com/changelog/acacia/2024-11-20/adaptive-pricing-param)[Customize
the submit button recurring Payment Links and Checkout SessionsCheckout+ 1
more](https://docs.stripe.com/changelog/acacia/2024-11-20/submit-type-recurring-cpl)[Adds
support for advanced card features on Checkout
SessionsCheckout](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features)[Allows
Link card-only integrations to accept non-card payments under Link card
brandPayments](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand)[Adds
additional beneficiary information for bank transfer
paymentsPayments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information)
#### Payment method enhancements

[Adds network decline code field for Swish and BLIK
refundsPayments](https://docs.stripe.com/changelog/acacia/2024-11-20/refunds-network-decline-code)[Adds
support for SEPA Direct Debit and Bacs Direct Debit mandate reference prefixes
in Checkout
SessionsCheckout](https://docs.stripe.com/changelog/acacia/2024-11-20/checkout-sessions-sepa-debit-bacs-debit-mandate-options)[Specifying
an originating payment method for Inbound Transfers is now
optionalTreasury](https://docs.stripe.com/changelog/acacia/2024-11-20/inbound-transfers-optional-pm)[Use
configurable capture methods and set up future usage for South Korean payment
methodsCheckout](https://docs.stripe.com/changelog/acacia/2024-11-20/south-korea-payment-methods)
#### Additional updates

[Trace payouts with a unique
identifierPayouts](https://docs.stripe.com/changelog/acacia/2024-11-20/payout-trace-id-api)[Converts
properties on the Account object from a String to an
enumConnect](https://docs.stripe.com/changelog/acacia/2024-11-20/account-disabled-reason)[Adds
indicator for connected accounts that must log in before using embedded
componentsConnect](https://docs.stripe.com/changelog/acacia/2024-11-20/account-sessions-stripe-authentication-response)[Adds
support for authorizers to Person
APIConnect](https://docs.stripe.com/changelog/acacia/2024-11-20/authorizer-person-api)
### 2024-10-28.acacia

#### Billing credit grants

[Adds Credit Grant APIs and resourcesBilling+ 1
more](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-apis)[Adds
support for pre-tax credit amount information to invoicesBilling+ 1
more](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-invoice)[Adds
support for pre-tax credit amount information to credit notesBilling+ 1
more](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-credit-note)
#### New payment methods

[Adds support for new South Korean payment methodsBilling+ 5
more](https://docs.stripe.com/changelog/acacia/2024-10-28/south-korean-payment-methods)[Adds
support for Alma in FranceCheckout+ 3
more](https://docs.stripe.com/changelog/acacia/2024-10-28/alma)
#### Event destinations and event types

[Adds Event Destinations v2 API endpointAffects all
products](https://docs.stripe.com/changelog/acacia/2024-10-28/event-destinations-api)[Adds
event type for updated receipt data in Issuing
transactionsIssuing](https://docs.stripe.com/changelog/acacia/2024-10-28/issuing-transactions-updated-receipt-event)
#### Payment method enhancements

[Adds a metadata field to the Vault and Forward
APIPayments](https://docs.stripe.com/changelog/acacia/2024-10-28/forwarding-api-metadata-field)[Adds
Polish PLN currency support to Terminal tipping
configurationTerminal](https://docs.stripe.com/changelog/acacia/2024-10-28/terminal-tipping-pln)[Supports
domain registration for Amazon
PayElements](https://docs.stripe.com/changelog/acacia/2024-10-28/amazon-pay-domain-registration)
#### Additional tax registration options

[Adds support for new countries to the Tax Registration
APITax](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-registration-new-countries)[Adds
support for tax ID types in several new
countriesTax](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-ids)[Adds
support for collecting retail delivery
feesTax](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-retail-delivery-fee)[Adds
option to automatically validate customer tax location during an
updateTax](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-validate-location-auto)
#### Additional updates

[Adds support for disabling Stripe user authentication for certain embedded
componentsConnect](https://docs.stripe.com/changelog/acacia/2024-10-28/disable-stripe-user-authentication-account-sessions)[Adds
a test helper that updates the shipping status for physical
cardsIssuing](https://docs.stripe.com/changelog/acacia/2024-10-28/testmode-helper-shipping-status)[Adds
created, updated, and failed events for all refund
typesPayments](https://docs.stripe.com/changelog/acacia/2024-10-28/refund-webhook-update)[Adds
pricing groups to the Accounts APIConnect+ 1
more](https://docs.stripe.com/changelog/acacia/2024-10-28/pricing-groups-account-objects)[Adds
scheduled subscription downgrades in the customer
portalBilling](https://docs.stripe.com/changelog/acacia/2024-10-28/customer-portal-schedule-downgrades)[Makes
business profile optional for customer portal
configurationBilling](https://docs.stripe.com/changelog/acacia/2024-10-28/customer-portal-config-business-profile)[Uses
Visa’s Compelling Evidence 3.0 to respond to qualifying disputesAffects all
products](https://docs.stripe.com/changelog/acacia/2024-10-28/visa-compelling-evidence-3-0)[Adds
support for scheduling invoice
finalizationInvoicing](https://docs.stripe.com/changelog/acacia/2024-10-28/schedule-invoice-finalization)
### 2024-09-30.acacia

Breaking changes
#### Add alerts, monitoring, and reporting to usage-based billing

[Adds contextual filters to billing
alertsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-contextualizing-filters)[Adds
an Alerts API for usage-based
billingBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-api)[Adds
an event for triggered billing
alertsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-trigger-event)[Adds
support for listening to triggered billing
alertsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-webhook-listener)[Adds
billing alert resources and
endpointsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints)[Adds
support for subscriptions and subscription items to billing alertsBilling+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions)[Adds
Meter Event v2 API
endpointsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/usage-based-billing-v2-meter-events-api)
#### Enhancements for Terminal readers and integrations

[Updates consent modeling for saving cards with
TerminalTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay)[Adds
support for configuring the reboot time
settingTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reboot-window)[Adds
the Stripe S700 reader as a valid device
typeTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700)[Adds
details about offline collection on card_present PaymentMethod
objectsTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-offline-details-card-present-paymentmethods)
#### Payment method enhancements

[Adds option to retrieve CVC tokens on Confirmation
TokensElements](https://docs.stripe.com/changelog/acacia/2024-09-30/support-payment-method-options-confirmation)[Adds
customer ID to payment method preview on a confirmation
tokenElements](https://docs.stripe.com/changelog/acacia/2024-09-30/support-customer-payment-method-preview)[Adds
support for identifying the unique payer for the BLIK payment
methodPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/buyer-id-blik)[Adds
support for Affirm transaction
IDsPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/affirm-transaction-id-dashboard)[Adds
support for in-person payment methods, including Interac
cardsTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/card-interac-present-support)[Displays
authorization_code for
ChargesPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/displays-authorization-code-for-charges)[Adds
wallet details for card_present Charges and Payment
MethodsTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-offline-details-card-present-paymentmethods)[Adds
country field for Charges that use
KlarnaPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/charges-klarna-payer-details-country)[Displays
Amazon Pay dispute type on
DisputesPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/display-amazonpay-dispute-type)
#### Add support for new payment methods

[Adds support for three new payment methods: Multibanco, Twint, and ZipPayment
Links](https://docs.stripe.com/changelog/acacia/2024-09-30/payment-links-new-payment-methods)[Adds
support for using the Multibanco payment method with
billingBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-mutlibanco-support)[Adds
Twint to the PaymentMethodConfiguration
APIPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/twint-support-payment-method-configuration)[Adds
Girocard as a PaymentMethod brand and
networkPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-girocard-paymentmethod-brand-network)
#### Add tax IDs for Switzerland and Croatia, and optional tax ID requirement

[Adds Switzerland UID as a supported customer tax IDInvoicing+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/switzerland-tax-uid)[Adds
Croatian Personal Identification Number to supported Tax IDsBilling+ 2
more](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-tax-id-type-hr_oib-croatian-personal-id-number)[Adds
support for requiring a customer tax ID on Checkout and Payment LinksCheckout+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/requiring-customer-tax-id-checkout-session-paymentlink)
#### Add filtering support for Financial Connections

[Adds support for filtering by account subcategories on Financial
ConnectionsFinancial
Connections](https://docs.stripe.com/changelog/acacia/2024-09-30/financial-connections-filters)[Expands
filtering support for Financial Connections SessionsFinancial
Connections](https://docs.stripe.com/changelog/acacia/2024-09-30/financial-connections-additional-filters)
#### New error codes for more robust testing

[Adds error code for exceeded transaction limitsInvoicing+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/error-code-transaction-limit)[Adds
new error code for invalid mandate prefixes to Bacs Direct Debit and SEPA Direct
Debit
paymentsPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/error-code-invalid-mandate-reference-prefix)
#### Add new Invoice Rendering Template resource

[Adds Invoice Rendering Templates for
InvoicesInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-resource)[Adds
retrieve and archive methods for Invoice Rendering
TemplatesInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-methods)[Adds
support for templates to Invoices and
CustomersInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-parameter)[Adds
version support for Invoice Rendering
TemplatesInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-version)
#### Improve address validation and dispute and regulatory management for Issuing

[Updates the default value for shipping address
validationIssuing](https://docs.stripe.com/changelog/acacia/2024-09-30/card-shipping-status-submitted-address-validation)[Adds
address validation for physical
cardsIssuing](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-address-validation)[Adds
a new webhook event for when funds are deducted as part of a
disputeIssuing](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-webhook-fund-deduction)
#### Streamline invoice processing

[Adds support for bulk invoice line item
operationsInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/invoicing-bulk-line-item-operations)[Adds
webhook events for when an invoice is due or
overdueBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-due-date-webhooks)[Adds
option to automatically finalize
invoicesInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/automatically-finalizes-at-invoice)
#### Tax enhancements

[Adds support for posting time on tax transaction
creationTax](https://docs.stripe.com/changelog/acacia/2024-09-30/tax-posting-time-on-creation)[Adds
support for tax settings and registrations for Embedded ComponentsConnect+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/tax-registrations-settings-embedded-components)[Adds
new method to retrieve a Tax
CalculationTax](https://docs.stripe.com/changelog/acacia/2024-09-30/retrieves-tax-calculation-api)[Adds
support for specifying US state sales tax elections while creating tax
registrationsTax](https://docs.stripe.com/changelog/acacia/2024-09-30/support-us-state-sales-tax-elections-api)
#### Additional updates

[Adds risk verification details for connected
accountsConnect](https://docs.stripe.com/changelog/acacia/2024-09-30/additional-risk-verification-details-connected-accounts)[Adds
support for email types to Credit
NotesInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/credit-note-email-type)[Adds
support for the Payment Element on a Customer
SessionElements](https://docs.stripe.com/changelog/acacia/2024-09-30/support-payment-element-customer-session)[Adds
support for identifying the case type for card
disputesPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/disputes-case-type-card)[Adds
a method to update the metadata for Checkout
SessionsCheckout](https://docs.stripe.com/changelog/acacia/2024-09-30/checkout-update-method)[Adds
parameter to link Verification Sessions to
CustomersIdentity](https://docs.stripe.com/changelog/acacia/2024-09-30/identity-verification-session-related-customer)[Displays
CHIPS tracking details for outbound wire payments and
transfersTreasury](https://docs.stripe.com/changelog/acacia/2024-09-30/displays-chips-tracking-details-treasury-outbound-wires)[Adds
additional reasonable defaulting to the Account Link API
v1Connect](https://docs.stripe.com/changelog/acacia/2024-09-30/account-link-api-default-fields-v1)[Makes
LineItem.description
optionalCheckout](https://docs.stripe.com/changelog/acacia/2024-09-30/description-optional-checkout-session-line-item)[Adds
target_frozen_time for advancing test_helpers.test_clock
objectsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/support-status-details-test-clock)[Makes
status details for Test Clock test helpers
requiredBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/make-testclock-status-details-required)[Adds
a new enum value representing a ReceivedDebit failure due to an international
transactionTreasury](https://docs.stripe.com/changelog/acacia/2024-09-30/ef-features)[Makes
it optional to update the products and prices of a
subscriptionBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-portal-updates-optional)[Add
support for custom_unit_amount during product creationCheckout+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/products-custom-unit-amount)[Adds
support for retrieving thin
eventsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/api-v2-thin-events)
## 2024

[2024-06-20](https://docs.stripe.com/changelog/2024-06-20)Breaking
changes[Renames a fuel attribute of the Authorization
objectIssuing](https://docs.stripe.com/changelog/2024-06-20/renames-fuel-attribute-authorization-object)[Renames
a purchase_details attribute of the Transaction
objectIssuing](https://docs.stripe.com/changelog/2024-06-20/renames-purchase-details-transaction-object)[Removes
undocumented fuel
fieldsIssuing](https://docs.stripe.com/changelog/2024-06-20/removes-undocumented-fuel-fields-issuing)[Removes
undocumented fleet
fieldsIssuing](https://docs.stripe.com/changelog/2024-06-20/removes-undocumented-fleet-fields-issuing)[Adds
enum values for fuel
unitsIssuing](https://docs.stripe.com/changelog/2024-06-20/adds-enum-fuel-units-issuing)[Deprecates
alphanumeric_id for Issuing
AuthorizationIssuing](https://docs.stripe.com/changelog/2024-06-20/deprecates-alphanumeric-id-issuing)[Adds
enum values for disabled
reasonsConnect](https://docs.stripe.com/changelog/2024-06-20/adds-enum-disabled-reasons-capabilities)[Deprecates
the bank_transfer_payments capability type in favor of newer capability
typesConnect](https://docs.stripe.com/changelog/2024-06-20/deprecates-bank-transfer-payments-capabilities)[Adds
new enum values for request history
reasonsIssuing](https://docs.stripe.com/changelog/2024-06-20/adds-enum-request-history-reasons-issuing)[2024-04-10](https://docs.stripe.com/changelog/2024-04-10)Breaking
changes[Makes automatic sync the default capture method for PaymentIntents when
not
specifiedPayments](https://docs.stripe.com/changelog/2024-04-10/automatic-sync-default-paymenintents)[Renames
the rendering_options attribute for invoices to renderingInvoicing+ 1
more](https://docs.stripe.com/changelog/2024-04-10/renames-rendering-options-invoicing)[Renames
the features attribute of the Product objectInvoicing+ 1
more](https://docs.stripe.com/changelog/2024-04-10/renames-features-attribute-product-object)
## 2023

[2023-10-16](https://docs.stripe.com/changelog/2023-10-16)Breaking changes[Adds
new account requirement error codes to the Accounts
APIConnect](https://docs.stripe.com/changelog/2023-10-16/adds-account-requirement-error-accounts)[Auto-populates
the statement descriptor and prefix in the Accounts
APIConnect](https://docs.stripe.com/changelog/2023-10-16/auto-populates-statement-descriptor-accounts)[2023-08-16](https://docs.stripe.com/changelog/2023-08-16)Breaking
changes[Enables automatic payment methods by default for PaymentIntents and
SetupIntentsPayments+ 1
more](https://docs.stripe.com/changelog/2023-08-16/automatic-payment-methods)[One-time
payments in Checkout Sessions support no-cost
ordersCheckout](https://docs.stripe.com/changelog/2023-08-16/no-cost-orders-checkout-session)[Platform-scope
rendering for select PaymentMethod fingerprintsConnect+ 2
more](https://docs.stripe.com/changelog/2023-08-16/platform-scope-rendering-payment-method)[Adds
specific error codes for failed Klarna paymentsPayments+ 1
more](https://docs.stripe.com/changelog/2023-08-16/klarna-payment-failure-error-code)[Adds
new director verification error codes to the Accounts
APIConnect](https://docs.stripe.com/changelog/2023-08-16/adds-director-verfication-error-accounts)
## 2022

[2022-11-15](https://docs.stripe.com/changelog/2022-11-15)Breaking changes[The
Charges object no longer auto-expands refunds by
defaultPayments](https://docs.stripe.com/changelog/2022-11-15/deprecates-charges-auto-expand)[Removes
the charges attribute from the PaymentIntent
objectPayments](https://docs.stripe.com/changelog/2022-11-15/removes-charges-attribute-paymentintent)[Adds
new decline codes to the PaymentIntent and PaymentMethod
APIsPayments](https://docs.stripe.com/changelog/2022-11-15/adds-decline-codes-paymentintent-paymentmethod)[Adds
new decline codes to the SetupIntent
APIPayments](https://docs.stripe.com/changelog/2022-11-15/adds-decline-codes-setupintent)[Adds
a new structure error code to the Accounts
APIConnect](https://docs.stripe.com/changelog/2022-11-15/adds-structure-error-code-accounts)[2022-08-01](https://docs.stripe.com/changelog/2022-08-01)Breaking
changes[Removes the include_and_require value when creating
invoicesInvoicing](https://docs.stripe.com/changelog/2022-08-01/removes-include-require-value-invoices)[Default
customer creation in Checkout Session payment mode changed to
if_requiredCheckout](https://docs.stripe.com/changelog/2022-08-01/default-customer-creation-checkout-session)[Deferred
PaymentIntent creation in Checkout Session payment modeCheckout+ 1
more](https://docs.stripe.com/changelog/2022-08-01/deferred-paymentintent-checkout-session)[Removes
the setup_intent property from Checkout Sessions in subscription
modeCheckout](https://docs.stripe.com/changelog/2022-08-01/removes-setupintent-checkout-session)[Replaces
line item parameters from the Create Checkout Session
endpointCheckout](https://docs.stripe.com/changelog/2022-08-01/replaces-line-item-create-checkout-session)[Removes
the subscription data parameter from the Create Checkout Session
endpointCheckout+ 1
more](https://docs.stripe.com/changelog/2022-08-01/removes-subscription-data-create-checkout-session)[Removes
the shipping rate parameter from Create Checkout Session
endpointCheckout](https://docs.stripe.com/changelog/2022-08-01/removes-shipping-rate-create-checkout-session)[Updates
Checkout Session shipping
propertiesCheckout](https://docs.stripe.com/changelog/2022-08-01/updates-shipping-property-checkout-session)[Adds
3D Secure exemption status to card
chargesPayments](https://docs.stripe.com/changelog/2022-08-01/adds-3d-secure-exemption-charges)[New
error code for invalid terms of service acceptance in Accounts
APIConnect](https://docs.stripe.com/changelog/2022-08-01/error-code-invalid-tos-accounts)[New
endpoints for managing a physical card’s shipping status in test
modeIssuing](https://docs.stripe.com/changelog/2022-08-01/endpoints-shipping-status-cards)[Adds
design_rejected as a possible cancellation reason for issued
cardsIssuing](https://docs.stripe.com/changelog/2022-08-01/adds-design-rejected-value-cards)[Removes
the default_currency attribute from the Customer objectAffects all
products](https://docs.stripe.com/changelog/2022-08-01/removes-default-currency-customer-object)
## 2020

[2020-08-27](https://docs.stripe.com/changelog/2020-08-27)Breaking
changes[Removes the tax_percent attributeCheckout+ 2
more](https://docs.stripe.com/changelog/2020-08-27/removes-tax-percent-attribute)[Renames
phases attributes in subscription
schedulesBilling](https://docs.stripe.com/changelog/2020-08-27/renames-phases-attributes-subscription-schedules)[Renames
event type that triggers on automatic
updatesPayments](https://docs.stripe.com/changelog/2020-08-27/renames-automatically-updated-event-type)[Removes
the display_items property from Checkout
SessionsCheckout](https://docs.stripe.com/changelog/2020-08-27/removes-display-items-checkout-session)[Formats
requirements for key persons associated with
accountsConnect](https://docs.stripe.com/changelog/2020-08-27/formats-requirements-key-persons-accounts)[Adds
new error codes to the Accounts, Persons, and Capabilities
APIsConnect](https://docs.stripe.com/changelog/2020-08-27/adds-error-codes-accounts-persons-capabilities)[Updates
to 3D Secure details in Charge
objectPayments](https://docs.stripe.com/changelog/2020-08-27/updates-3d-scure-charge-object)[Customer
subscriptions are no longer auto-expanded by
defaultBilling](https://docs.stripe.com/changelog/2020-08-27/deprecates-auto-expansion-customer-subscriptions)[Plan
tiers are no longer auto-expanded by
defaultBilling](https://docs.stripe.com/changelog/2020-08-27/deprecates-auto-expansion-plan-tiers)[Customer
sources are no longer auto-expanded by defaultPayments+ 2
more](https://docs.stripe.com/changelog/2020-08-27/deprecates-auto-expansion-customer-sources)[Tax
IDs are no longer auto-expanded on the Customer objectAffects all
products](https://docs.stripe.com/changelog/2020-08-27/deprecates-auto-expansion-tax-id-customer)[Deprecates
subscription prorate and subscription_prorate
parametersBilling](https://docs.stripe.com/changelog/2020-08-27/deprecates-prorate-parameters-subscriptions)[2020-03-02](https://docs.stripe.com/changelog/2020-03-02)Breaking
changes[Invoices can now be numbered sequentially across your accountBilling+ 1
more](https://docs.stripe.com/changelog/2020-03-02/sequentially-number-invoices)
## 2019

[2019-12-03](https://docs.stripe.com/changelog/2019-12-03)Breaking
changes[Standardizes invoice line item IDsBilling+ 1
more](https://docs.stripe.com/changelog/2019-12-03/standardizes-invoice-line-item-ids)[New
requirement for out_of_band_amount when creating post-payment credit
notesBilling+ 1
more](https://docs.stripe.com/changelog/2019-12-03/post-payment-credit-note-requirement)[Customer
balances are now returned when voiding invoicesBilling+ 1
more](https://docs.stripe.com/changelog/2019-12-03/customer-balances-returned-voided-invoices)[Removes
deprecated tax information fields from the Customer objectAffects all
products](https://docs.stripe.com/changelog/2019-12-03/removes-deprecated-tax-information-fields)[2019-11-05](https://docs.stripe.com/changelog/2019-11-05)Breaking
changes[Adds requirement for requested_capabilities on custom account
creationConnect](https://docs.stripe.com/changelog/2019-11-05/adds-requested-capabilities-requirement-custom-account)[Nested
subscription schedule settings under
default_settingsBilling](https://docs.stripe.com/changelog/2019-11-05/nests-subscription-schedule-settings)[2019-10-17](https://docs.stripe.com/changelog/2019-10-17)Breaking
changes[Renames and updates subscription schedule renewal
propertiesBilling](https://docs.stripe.com/changelog/2019-10-17/updates-subscription-renewal-properties)[Replaces
the subscription start field with
start_dateBilling](https://docs.stripe.com/changelog/2019-10-17/replaces-subscription-start-field)[Renames
billing to collection_method on invoices, subscriptions, and subscription
schedulesBilling+ 1
more](https://docs.stripe.com/changelog/2019-10-17/renames-billing-attribute)[The
due_date property is always null on auto-billed invoicesBilling+ 1
more](https://docs.stripe.com/changelog/2019-10-17/invoice-due-date-null)[Renames
account_balance to balance on Customer objectBilling+ 1
more](https://docs.stripe.com/changelog/2019-10-17/renames-account-balance-customer-object)[2019-10-08](https://docs.stripe.com/changelog/2019-10-08)Breaking
changes[Renames a Person object relationship
attributeConnect](https://docs.stripe.com/changelog/2019-10-08/renames-person-object-relationship-attribute)[2019-09-09](https://docs.stripe.com/changelog/2019-09-09)Breaking
changes[Accounts in many countries now require specifying capabilities at
creation
timeConnect](https://docs.stripe.com/changelog/2019-09-09/2019-09-09-1)[Adds new
details_code values to person document
verificationConnect](https://docs.stripe.com/changelog/2019-09-09/adds-detail-code-person-document-verification)[2019-08-14](https://docs.stripe.com/changelog/2019-08-14)Breaking
changes[Renames the platform_payments capability for accounts to card_payments,
requiring the manual specification of the added transfers
capabilityConnect](https://docs.stripe.com/changelog/2019-08-14/configuring-person-account-opener-no-longer-sets-executive)[Configuring
a person as an account opener no longer automatically sets them as an
executiveConnect](https://docs.stripe.com/changelog/2019-08-14/accounts-many-countries-require-specifying-capabilities)[2019-05-16](https://docs.stripe.com/changelog/2019-05-16)Breaking
changes[Bank pull payments no longer expose internal system refunds on
failurePayments](https://docs.stripe.com/changelog/2019-05-16/renames-platform-payments-capability-card-payments)[2019-03-14](https://docs.stripe.com/changelog/2019-03-14)Breaking
changes[Renames application_fee on invoices to application_fee_amountConnect+ 1
more](https://docs.stripe.com/changelog/2019-03-14/renames-application-fee-invoices-application-fee-amount)[Subscriptions
are now successfully created even if the first payment
failsBilling](https://docs.stripe.com/changelog/2019-03-14/subscriptions-successfully-created-first-payment-fails)[Invoices
now provide timestamps for each state transitionBilling+ 1
more](https://docs.stripe.com/changelog/2019-03-14/invoices-provide-timestamps-state-transitions)[Renames
the date field for invoices to createdBilling+ 1
more](https://docs.stripe.com/changelog/2019-03-14/renames-date-field-invoices-created)[Invoices
now specify when they’re finalized alongside other status transitionsBilling+ 1
more](https://docs.stripe.com/changelog/2019-03-14/invoices-specify-finalized-alongside-status-transitions)[2019-02-19](https://docs.stripe.com/changelog/2019-02-19)Breaking
changes[Changes statement descriptor behaviors for card payments created with
ChargesPayments](https://docs.stripe.com/changelog/2019-02-19/changes-statement-descriptor-behaviors-charges)[Several
account fields have been refactored to better describe legal entity,
verification status and requirements, and configurable
settingsConnect](https://docs.stripe.com/changelog/2019-02-19/several-fields-accounts-refactored)[Several
fields describing an account’s business details have moved to the
business_profile
subhashConnect](https://docs.stripe.com/changelog/2019-02-19/business-details-moved-business-profile-object)[Verification
of accounts or persons now supports uploading both front and back
sidesConnect](https://docs.stripe.com/changelog/2019-02-19/verification-accounts-persons-supports-front-back)[Accounts
no longer provide a keys field. Platforms should use their own API key to
authenticate as their connected
accountsConnect](https://docs.stripe.com/changelog/2019-02-19/accounts-no-longer-provide-keys-field)[Accounts
in the US now require specifying capabilities at creation
timeConnect](https://docs.stripe.com/changelog/2019-02-19/accounts-us-require-specifying-capabilities-creation)[Renames
the business_id_number for an account’s legal entity to
business_registration_numberConnect](https://docs.stripe.com/changelog/2019-02-19/renames-business-id-number-business-registration-number)[2019-02-11](https://docs.stripe.com/changelog/2019-02-11)Breaking
changes[Renames several statuses for
PaymentIntentsPayments](https://docs.stripe.com/changelog/2019-02-11/renames-several-statuses-payment-intents)[Renames
the save_source_to_customer field for sources to
save_payment_methodPayments](https://docs.stripe.com/changelog/2019-02-11/renames-save-source-to-customer-save-payment-method)[Renames
the allowed_source_types field for sources to
payment_method_typesPayments](https://docs.stripe.com/changelog/2019-02-11/renames-allowed-source-types-payment-method-types)[Renames
the next_source_action field for Payment Intents to
next_actionPayments](https://docs.stripe.com/changelog/2019-02-11/renames-next-source-action-next-action)[Renames
the authorize_with_url field for Payment Intents to
redirect_to_urlPayments](https://docs.stripe.com/changelog/2019-02-11/renames-authorize-with-url-redirect-to-url)
## 2018

[2018-11-08](https://docs.stripe.com/changelog/2018-11-08)Breaking
changes[Invoices now specify their automatic collection behavior using the
auto_advance fieldInvoicing+ 1
more](https://docs.stripe.com/changelog/2018-11-08/invoices-specify-auto-advance-field)[One-off
Invoices no longer automatically collect payment by
defaultInvoicing](https://docs.stripe.com/changelog/2018-11-08/one-off-invoices-no-longer-auto-collect-payment)[Replaces
the forgiven field with a new uncollectible status for invoicesInvoicing+ 1
more](https://docs.stripe.com/changelog/2018-11-08/mark-invoice-uncollectible-instead-forgiven)[Renames
an invoice error code to invoice_already_finalizedInvoicing+ 1
more](https://docs.stripe.com/changelog/2018-11-08/renames-invoice-error-code-invoice-already-finalized)[Includes
several changes for users of the Payment Intents API private
betaPayments](https://docs.stripe.com/changelog/2018-11-08/several-changes-payment-intents-private-beta)[2018-10-31](https://docs.stripe.com/changelog/2018-10-31)Breaking
changes[Descriptions for customers now have a character limitAffects all
products](https://docs.stripe.com/changelog/2018-10-31/descriptions-customers-character-limit)[Product
names now have a character limitBilling+ 1
more](https://docs.stripe.com/changelog/2018-10-31/names-products-character-limit)[Descriptions
for invoice line items now have a character limitBilling+ 1
more](https://docs.stripe.com/changelog/2018-10-31/descriptions-invoice-line-items-character-limit)[The
billing_reason of the first invoice of a subscription is now
subscription_createBilling+ 1
more](https://docs.stripe.com/changelog/2018-10-31/first-invoice-subscription-billing-reason-subscription-create)[2018-09-24](https://docs.stripe.com/changelog/2018-09-24)Breaking
changes[Renames the FileUpload object to Files, which now require secret keys to
download filesAffects all
products](https://docs.stripe.com/changelog/2018-09-24/file-uploads-renamed-files-require-secret-keys)[2018-09-06](https://docs.stripe.com/changelog/2018-09-06)Breaking
changes[SKU values no longer need to be
uniqueCheckout](https://docs.stripe.com/changelog/2018-09-06/sku-values-no-longer-need-unique)[2018-08-23](https://docs.stripe.com/changelog/2018-08-23)Breaking
changes[A subscription’s ending period can no longer be configured while
canceling
itBilling](https://docs.stripe.com/changelog/2018-08-23/subscription-ending-period-cannot-configured-canceling)[Customers
now provide a tax_info object with their tax ID detailsAffects all
products](https://docs.stripe.com/changelog/2018-08-23/customers-provide-tax-info-object)[Renames
the amount field for plan tiers to
unit_amountBilling](https://docs.stripe.com/changelog/2018-08-23/renames-amount-field-plan-tiers-unit-amount)[2018-07-27](https://docs.stripe.com/changelog/2018-07-27)Breaking
changes[Subscriptions no longer support modifying the source parameter
directlyBilling](https://docs.stripe.com/changelog/2018-07-27/subscriptions-no-longer-support-modifying-source)[Ending
a subscription trial now uses the timestamp of that API
requestBilling](https://docs.stripe.com/changelog/2018-07-27/ending-subscription-trial-uses-request-timestamp)[Coupons
now use floats rather than integers to specify percent_offBilling+ 1
more](https://docs.stripe.com/changelog/2018-07-27/coupons-use-floats-specify-percent-off)[Stripe
now validates email addresses when creating or updating customersAffects all
products](https://docs.stripe.com/changelog/2018-07-27/stripe-validates-email-addresses-customers)[2018-05-21](https://docs.stripe.com/changelog/2018-05-21)Breaking
changes[Products no longer embed lists of
SKUsCheckout](https://docs.stripe.com/changelog/2018-05-21/products-no-longer-embed-sku-lists)[Invoice
line items now have unique IDs andcan’t be used in place of a
subscriptionBilling+ 1
more](https://docs.stripe.com/changelog/2018-05-21/invoice-line-items-have-unique-ids-cannot-use-subscription)[Coupons,
SKUs, customers, products, and plans now limit the valid characters for
IDsBilling+ 1
more](https://docs.stripe.com/changelog/2018-05-21/valid-characters-ids-coupons-skus-customers-products-plans)[Subscriptions
now default to not defining their trial periods depending on a
planBilling](https://docs.stripe.com/changelog/2018-05-21/subscriptions-default-no-trial-period-plan)[Changing
a subscription to a new plan with a trial now extends the trial
periodBilling](https://docs.stripe.com/changelog/2018-05-21/changing-subscription-new-plan-extends-trial)[2018-02-28](https://docs.stripe.com/changelog/2018-02-28)Breaking
changes[Updating a canceled subscription on a future date no longer resets its
statusBilling](https://docs.stripe.com/changelog/2018-02-28/updating-canceled-subscription-no-longer-resets-status)[2018-02-06](https://docs.stripe.com/changelog/2018-02-06)Breaking
changes[Sources now provide a recommended value when the issuer advises using 3D
SecurePayments](https://docs.stripe.com/changelog/2018-02-06/sources-provide-recommended-use-3d-secure)[2018-02-05](https://docs.stripe.com/changelog/2018-02-05)Breaking
changes[Free plans with prorations now produce zero-dollar
invoicesBilling](https://docs.stripe.com/changelog/2018-02-05/free-plans-with-prorations-produce-zero-dollar-invoices)[Subscriptions
can now delay the first full invoice to a future date (and optionally include a
free
trial)Billing](https://docs.stripe.com/changelog/2018-02-05/subscriptions-delay-first-full-invoice-future-date)[Plans
now link to individual products, with several fields moving to the product
resourceBilling](https://docs.stripe.com/changelog/2018-02-05/plans-link-individual-products-several-fields-moved)[Products
now require a type field, differentiating their use with order SKUs or
subscriptions and plansBilling+ 1
more](https://docs.stripe.com/changelog/2018-02-05/products-require-type-field-differentiating-use)[2018-01-23](https://docs.stripe.com/changelog/2018-01-23)Breaking
changes[Connect platforms can identify reused card or bank accounts across
connected accounts as they now will share the same
fingerprintConnect](https://docs.stripe.com/changelog/2018-01-23/connect-platforms-identify-reused-cards-bank-accounts)
## 2017

[2017-12-14](https://docs.stripe.com/changelog/2017-12-14)Breaking
changes[Invoice line items now must always set a descriptionInvoicing+ 1
more](https://docs.stripe.com/changelog/2017-12-14/invoice-line-items-must-set-description)[Invoice
payment failures now return a card_error when a charge is declinedInvoicing+ 1
more](https://docs.stripe.com/changelog/2017-12-14/invoice-payment-failures-return-card-error)[2017-08-15](https://docs.stripe.com/changelog/2017-08-15)Breaking
changes[Sources can now specify that an authentication redirect isn’t
requiredPayments](https://docs.stripe.com/changelog/2017-08-15/sources-specify-no-authentication-redirect-required)[2017-06-05](https://docs.stripe.com/changelog/2017-06-05)Breaking
changes[Accounts can now specify why an account isn’t enabled with the new
reason
under_reviewConnect](https://docs.stripe.com/changelog/2017-06-05/accounts-specify-under-review-reason)[2017-05-25](https://docs.stripe.com/changelog/2017-05-25)Breaking
changes[Events for Connect now specify the originating connected account using
the account
fieldConnect](https://docs.stripe.com/changelog/2017-05-25/events-connect-specify-originating-account)[The
request field of the Events object now specifies both the request ID and
idempotency keyAffects all
products](https://docs.stripe.com/changelog/2017-05-25/events-specify-request-id-idempotency-key)[Events
with the previous_attributes field now render the complete affected
sub-arrayAffects all
products](https://docs.stripe.com/changelog/2017-05-25/events-previous-attributes-render-complete-sub-array)[Accounts
must now specify one of three types (Standard, Express, or
Custom)Connect](https://docs.stripe.com/changelog/2017-05-25/accounts-specify-type-standard-express-custom)[2017-04-06](https://docs.stripe.com/changelog/2017-04-06)Breaking
changes[Transfers are now split into payouts and
transfersConnect](https://docs.stripe.com/changelog/2017-04-06/transfers-split-payouts-transfers)[2017-02-14](https://docs.stripe.com/changelog/2017-02-14)Breaking
changes[Charges now specify the ID for the rule blocking a transaction, which
can be expandedPayments+ 1
more](https://docs.stripe.com/changelog/2017-02-14/charges-specify-rule-blocking-transaction)[Charges
now specify the ID for the dispute associated with a transaction, which can be
expandedPayments](https://docs.stripe.com/changelog/2017-02-14/charges-specify-dispute-associated-transaction)[2017-01-27](https://docs.stripe.com/changelog/2017-01-27)Breaking
changes[Balance transactions no longer include the sourced_transfers
fieldPayments+ 1
more](https://docs.stripe.com/changelog/2017-01-27/balance-transactions-no-longer-include-sourced-transfers)
## 2016

[2016-10-19](https://docs.stripe.com/changelog/2016-10-19)Breaking changes[Using
insufficient permissions to make API requests now throws an HTTP 403
errorAffects all
products](https://docs.stripe.com/changelog/2016-10-19/insufficient-permissions-throw-403-error)[2016-07-06](https://docs.stripe.com/changelog/2016-07-06)Breaking
changes[Filter lists of subscriptions for canceled
subscriptionsBilling](https://docs.stripe.com/changelog/2016-07-06/filter-canceled-subscriptions-retrieve-individually)[2016-06-15](https://docs.stripe.com/changelog/2016-06-15)Breaking
changes[Deactivating a product no longer automatically deactivates its
SKUsBilling](https://docs.stripe.com/changelog/2016-06-15/deactivating-product-deactivates-skus)[2016-03-07](https://docs.stripe.com/changelog/2016-03-07)Breaking
changes[Supported currencies are defined on the country spec for an account’s
countryPayments](https://docs.stripe.com/changelog/2016-03-07/supported-currencies-defined-country-spec)[2016-02-29](https://docs.stripe.com/changelog/2016-02-29)Breaking
changes[Creating or updating an account now validates the postal code for its
legal
entityConnect](https://docs.stripe.com/changelog/2016-02-29/creating-updating-account-validates-postal-code)[2016-02-23](https://docs.stripe.com/changelog/2016-02-23)Breaking
changes[Orders that are paid or fulfilled, and then become canceled or returned,
now automatically refund associated
chargesPayments](https://docs.stripe.com/changelog/2016-02-23/orders-paid-fulfilled-refund-associated-charges)[2016-02-22](https://docs.stripe.com/changelog/2016-02-22)Breaking
changes[You can no longer add more than 250 invoice items to an invoiceBilling+
1
more](https://docs.stripe.com/changelog/2016-02-22/no-more-than-250-invoice-items)[2016-02-19](https://docs.stripe.com/changelog/2016-02-19)Breaking
changes[Renames the name field on Bank Accounts to
account_holder_namePayments](https://docs.stripe.com/changelog/2016-02-19/renames-name-field-bank-accounts-account-holder-name)[2016-02-03](https://docs.stripe.com/changelog/2016-02-03)Breaking
changes[Accounts now only show country-specific subfields for the legal_entity
fieldConnect](https://docs.stripe.com/changelog/2016-02-03/accounts-only-show-country-fields-legal-entity)
## 2015

[2015-10-16](https://docs.stripe.com/changelog/2015-10-16)Breaking
changes[Creating or updating customers must now include a plan if a tax
percentage is
specifiedBilling](https://docs.stripe.com/changelog/2015-10-16/customers-must-include-plan-tax-percentage)[2015-10-12](https://docs.stripe.com/changelog/2015-10-12)Breaking
changes[Using invalid parameters to create cards or bank accounts for tokens,
sources, or external bank accounts now throws an HTTP 400
errorPayments](https://docs.stripe.com/changelog/2015-10-12/invalid-parameters-throw-400-error)[2015-10-01](https://docs.stripe.com/changelog/2015-10-01)Breaking
changes[Bank account information renamed to external accounts on user
profilesConnect](https://docs.stripe.com/changelog/2015-10-01/accounts-include-external-accounts-field)[Accounts
now include an external_accounts
fieldConnect](https://docs.stripe.com/changelog/2015-10-01/accounts-specify-additional-fields-bank-accounts)[2015-09-23](https://docs.stripe.com/changelog/2015-09-23)Breaking
changes[The charge field now always reflects the latest charge on
invoicesInvoicing+ 1
more](https://docs.stripe.com/changelog/2015-09-23/invoice-charge-field-reflect-latest-charge)[Invoices
no longer include the payment propertyInvoicing+ 1
more](https://docs.stripe.com/changelog/2015-09-23/invoices-no-longer-include-payment-field)[Listing
all charges now includes payments from all funding
sourcesPayments](https://docs.stripe.com/changelog/2015-09-23/listing-charges-includes-payments-funding-sources)[Charges
only support an offset for list pagination when filtering by
sourcePayments](https://docs.stripe.com/changelog/2015-09-23/charges-support-offset-list-pagination-source)[2015-09-08](https://docs.stripe.com/changelog/2015-09-08)Breaking
changes[Rate-limited requests now return an HTTP 429 error, no longer including
the rate_limit fieldAffects all
products](https://docs.stripe.com/changelog/2015-09-08/rate-limited-requests-return-429-no-rate-limit)[2015-09-03](https://docs.stripe.com/changelog/2015-09-03)Breaking
changes[Requests that reuse idempotency tokens but alter request parameters now
throw an errorAffects all
products](https://docs.stripe.com/changelog/2015-09-03/reuse-idempotency-tokens-alter-error)[2015-08-19](https://docs.stripe.com/changelog/2015-08-19)Breaking
changes[Balance transactions with refunds or disputes now specify the
corresponding ID in the source
fieldPayments](https://docs.stripe.com/changelog/2015-08-19/balance-transactions-refunds-disputes-specify-source)[2015-08-07](https://docs.stripe.com/changelog/2015-08-07)Breaking
changes[Stripe now ensures the tos_acceptance[date] field on accounts is a valid
timestampConnect](https://docs.stripe.com/changelog/2015-08-07/stripe-ensures-tos-acceptance-date-valid-timestamp)[2015-07-28](https://docs.stripe.com/changelog/2015-07-28)Breaking
changes[Transfers that are immediately processed now trigger the
balance.available
eventConnect](https://docs.stripe.com/changelog/2015-07-28/transfers-immediately-processed-trigger-balance-available)[2015-07-13](https://docs.stripe.com/changelog/2015-07-13)Breaking
changes[Accounts now include the verification[disabled_reason] field to describe
why theycan’t make transfers or
chargesConnect](https://docs.stripe.com/changelog/2015-07-13/accounts-include-verification-disabled-reason-field)[2015-07-07](https://docs.stripe.com/changelog/2015-07-07)Breaking
changes[Transfers submitted to the bank that haven’t arrived now provide an
in_transit
statusConnect](https://docs.stripe.com/changelog/2015-07-07/transfers-in-transit-provide-status)[2015-06-15](https://docs.stripe.com/changelog/2015-06-15)Breaking
changes[Accounts on manual payout schedules now throw a new
errorConnect](https://docs.stripe.com/changelog/2015-06-15/accounts-manual-payout-schedules-throw-error)[2015-04-07](https://docs.stripe.com/changelog/2015-04-07)Breaking
changes[Updates how ending periods are calculated on prorated invoice line
itemsBilling](https://docs.stripe.com/changelog/2015-04-07/updates-ending-periods-prorated-invoice-line-items)[Changes
the sorting order of lines for invoicesBilling+ 1
more](https://docs.stripe.com/changelog/2015-04-07/changes-sorting-order-lines-invoices)[2015-03-24](https://docs.stripe.com/changelog/2015-03-24)Breaking
changes[By default, coupons no longer apply to invoice items with negative
amountsBilling+ 1
more](https://docs.stripe.com/changelog/2015-03-24/coupons-no-longer-apply-negative-invoice-items)[2015-02-18](https://docs.stripe.com/changelog/2015-02-18)Breaking
changes[Charges that succeed now have a succeeded
statusPayments](https://docs.stripe.com/changelog/2015-02-18/charges-succeed-have-succeeded-status)[Charges
now have a source field that accepts a source or
cardPayments](https://docs.stripe.com/changelog/2015-02-18/charges-have-source-field-accepts-source-card)[Customers
now have a source field that accepts a source or card, and updates related event
typesPayments](https://docs.stripe.com/changelog/2015-02-18/customers-have-source-field-accepts-source-card)[2015-02-16](https://docs.stripe.com/changelog/2015-02-16)Breaking
changes[Renames the transfer.canceled event type to
transfer.reversedConnect](https://docs.stripe.com/changelog/2015-02-16/renames-transfer-canceled-event-transfer-reversed)[2015-02-10](https://docs.stripe.com/changelog/2015-02-10)Breaking
changes[Dispute statuses now include the warning_closed
valuePayments](https://docs.stripe.com/changelog/2015-02-10/dispute-statuses-include-warning-closed)[Transfers
now require a sufficient account balance in test mode to better simulate live
modeConnect](https://docs.stripe.com/changelog/2015-02-10/transfers-require-sufficient-balance-test-mode)[2015-01-26](https://docs.stripe.com/changelog/2015-01-26)Breaking
changes[Events with the previous_attributes field now only render the
differences to objects across updatesAffects all
products](https://docs.stripe.com/changelog/2015-01-26/events-previous-attributes-render-differences)[Subscriptions
now only report the timestamp for API or invoice payment failures for the
canceled_at
fieldBilling](https://docs.stripe.com/changelog/2015-01-26/subscriptions-report-api-invoice-failures)[2015-01-11](https://docs.stripe.com/changelog/2015-01-11)Breaking
changes[File uploads describe their file type with the simpler type field and
formatAffects all
products](https://docs.stripe.com/changelog/2015-01-11/file-uploads-describe-type-format)
## 2014

[2014-12-22](https://docs.stripe.com/changelog/2014-12-22)Breaking changes[Cards
now use both the unchecked and unavailable values to describe address and CVC
checks by issuing
banksPayments](https://docs.stripe.com/changelog/2014-12-22/cards-use-unchecked-unavailable-address-cvc-checks)[Tokens
with cards no longer include the customer
fieldPayments](https://docs.stripe.com/changelog/2014-12-22/tokens-cards-no-longer-include-customer-field)[2014-12-17](https://docs.stripe.com/changelog/2014-12-17)Breaking
changes[Introduces the statement_description field and logic for how charges,
invoices, plans, and transfers render statement descriptorsPayments+ 3
more](https://docs.stripe.com/changelog/2014-12-17/introduces-statement-description-field-logic)[Creating
accounts using the API requires the 2014-12-17 version or
newerConnect](https://docs.stripe.com/changelog/2014-12-17/creating-accounts-requires-2014-12-17-version)[2014-12-08](https://docs.stripe.com/changelog/2014-12-08)Breaking
changes[Disputes now include an evidence_details object for evidence
documentationPayments](https://docs.stripe.com/changelog/2014-12-08/disputes-include-evidence-details-object)[2014-11-20](https://docs.stripe.com/changelog/2014-11-20)Breaking
changes[Disputes are now reported as won even if the charge is
refundedPayments](https://docs.stripe.com/changelog/2014-11-20/disputes-reported-won-refunded-charge)[Invoice
items now reflect the metadata for their associated subscription, rather than
planBilling](https://docs.stripe.com/changelog/2014-11-20/invoice-items-reflect-subscription-metadata)[2014-11-05](https://docs.stripe.com/changelog/2014-11-05)Breaking
changes[Account activation status terms updated for payments and
transfersConnect](https://docs.stripe.com/changelog/2014-11-05/renames-charge-account-enabled-fields)[2014-10-07](https://docs.stripe.com/changelog/2014-10-07)Breaking
changes[You can no longer retrieve tokens with publishable
keysElements](https://docs.stripe.com/changelog/2014-10-07/no-longer-retrieve-tokens-publishable-keys)[Creating
a Card or Bank Account with a publishable key omits fingerprints in API
responsesElements](https://docs.stripe.com/changelog/2014-10-07/create-card-bank-account-omit-fingerprints)[2014-09-08](https://docs.stripe.com/changelog/2014-09-08)Breaking
changes[Bank Accounts now include a status enum that replace multiple
fieldsPayments](https://docs.stripe.com/changelog/2014-09-08/bank-accounts-include-status-enum)[2014-08-20](https://docs.stripe.com/changelog/2014-08-20)Breaking
changes[Disputes now provide several new
statusesPayments](https://docs.stripe.com/changelog/2014-08-20/disputes-provide-several-new-statuses)[Disputes
now include multiple balance
transactionsPayments](https://docs.stripe.com/changelog/2014-08-20/disputes-include-multiple-balance-transactions)[2014-08-04](https://docs.stripe.com/changelog/2014-08-04)Breaking
changes[You can now retrieve balance histories rather than relying on Transfer
fieldsConnect](https://docs.stripe.com/changelog/2014-08-04/retrieve-balance-histories-transfer-fields)[2014-07-26](https://docs.stripe.com/changelog/2014-07-26)Breaking
changes[Application fees now include a sublist of refunds through the refunds
fieldConnect](https://docs.stripe.com/changelog/2014-07-26/application-fees-include-refunds-sublist-refunds-field)[2014-07-22](https://docs.stripe.com/changelog/2014-07-22)Breaking
changes[Invoice line items now include subscription plans and
quantitiesInvoicing+ 1
more](https://docs.stripe.com/changelog/2014-07-22/invoice-line-items-include-subscription-plans-quantities)[2014-06-17](https://docs.stripe.com/changelog/2014-06-17)Breaking
changes[Invoices now include a sublist of refunds through the refunds
fieldInvoicing+ 1
more](https://docs.stripe.com/changelog/2014-06-17/invoices-include-refunds-sublist-refunds-field)[2014-06-13](https://docs.stripe.com/changelog/2014-06-13)Breaking
changes[Renames the type field on cards to brandPayments+ 1
more](https://docs.stripe.com/changelog/2014-06-13/renames-type-field-cards-brand)[2014-05-19](https://docs.stripe.com/changelog/2014-05-19)Breaking
changes[Replaces the account field on transfersConnect+ 1
more](https://docs.stripe.com/changelog/2014-05-19/renames-account-field-transfers-bank-account)[2014-03-28](https://docs.stripe.com/changelog/2014-03-28)Breaking
changes[Lists no longer include the count fieldAffects all
products](https://docs.stripe.com/changelog/2014-03-28/lists-no-longer-include-count-field)[2014-03-13](https://docs.stripe.com/changelog/2014-03-13)Breaking
changes[Renames the statement descriptor
fieldConnect](https://docs.stripe.com/changelog/2014-03-13/renames-statement-descriptor-field-transfers)[2014-01-31](https://docs.stripe.com/changelog/2014-01-31)Breaking
changes[Customers now support multiple
subscriptionsBilling](https://docs.stripe.com/changelog/2014-01-31/customers-support-multiple-subscriptions)[Trial
end dates are no longer computed for canceled
subscriptionsBilling](https://docs.stripe.com/changelog/2014-01-31/trial-end-dates-canceled-subscriptions)
## 2013

[2013-12-03](https://docs.stripe.com/changelog/2013-12-03)Breaking
changes[Application fees now provide an expandable account field to obtain user
detailsConnect](https://docs.stripe.com/changelog/2013-12-03/application-fees-provide-expandable-account-field)[Application
fee refunds are now proportional to the charged
amountConnect](https://docs.stripe.com/changelog/2013-12-03/application-fee-refunds-proportional-charged-amount)[2013-10-29](https://docs.stripe.com/changelog/2013-10-29)Breaking
changes[Coupons only apply to an invoice’s total balance, no longer applying to
zero-cost invoicesInvoicing+ 1
more](https://docs.stripe.com/changelog/2013-10-29/coupons-apply-invoice-total-balance)[2013-08-13](https://docs.stripe.com/changelog/2013-08-13)Breaking
changes[Fee details have moved from charges to their corresponding balance
transactionsPayments](https://docs.stripe.com/changelog/2013-08-13/fee-details-moved-balance-transactions)[Fee
details have moved from transfers to their corresponding balance
transactionsPayments](https://docs.stripe.com/changelog/2013-08-13/fee-details-moved-balance-transactions-transfers)[2013-08-12](https://docs.stripe.com/changelog/2013-08-12)Breaking
changes[Lets the description and email fields be null on several
objectsPayments+ 2
more](https://docs.stripe.com/changelog/2013-08-12/allows-description-email-fields-null)[2013-07-05](https://docs.stripe.com/changelog/2013-07-05)Breaking
changes[Customers now include a cards sublist and default_card fieldPayments+ 2
more](https://docs.stripe.com/changelog/2013-07-05/customers-include-cards-sublist-default-card-field)[2013-02-13](https://docs.stripe.com/changelog/2013-02-13)Breaking
changes[Disputes on charges are now tracked through the stripe_fee field and
included in the fee
totalPayments](https://docs.stripe.com/changelog/2013-02-13/disputes-tracked-stripe-fee-field-fee-total)[2013-02-11](https://docs.stripe.com/changelog/2013-02-11)Breaking
changes[Failed invoice payments now return an HTTP errorInvoicing+ 1
more](https://docs.stripe.com/changelog/2013-02-11/failed-invoice-payments-return-http-error)
## 2012

[2012-11-07](https://docs.stripe.com/changelog/2012-11-07)Breaking
changes[Renames the disputed field for Charges to
disputePayments](https://docs.stripe.com/changelog/2012-11-07/renames-disputed-field-charges-dispute)[2012-10-26](https://docs.stripe.com/changelog/2012-10-26)Breaking
changes[Invoices now include a sublist of invoice line itemsBilling+ 1
more](https://docs.stripe.com/changelog/2012-10-26/invoices-include-invoice-line-items-sublist)[2012-09-24](https://docs.stripe.com/changelog/2012-09-24)Breaking
changes[Discounts no longer include an extraneous id fieldBilling+ 1
more](https://docs.stripe.com/changelog/2012-09-24/discounts-no-longer-extraneous-id-field)[2012-07-09](https://docs.stripe.com/changelog/2012-07-09)Breaking
changes[Customers no longer include the uncaptured
fieldPayments](https://docs.stripe.com/changelog/2012-07-09/customers-no-longer-uncaptured-field)[2012-06-18](https://docs.stripe.com/changelog/2012-06-18)Breaking
changes[Tokens no longer include the amount and currency propertiesElements+ 1
more](https://docs.stripe.com/changelog/2012-06-18/tokens-no-longer-amount-currency-fields)[2012-03-25](https://docs.stripe.com/changelog/2012-03-25)Breaking
changes[Customers no longer include a next_recurring_charge
fieldBilling](https://docs.stripe.com/changelog/2012-03-25/customers-no-longer-next-recurring-charge-field)[2012-02-23](https://docs.stripe.com/changelog/2012-02-23)Breaking
changes[Fields with null values are now included in API responsesAffects all
products](https://docs.stripe.com/changelog/2012-02-23/fields-null-values-included-api-responses)
## 2011

[2011-09-15](https://docs.stripe.com/changelog/2011-09-15)Breaking changes[Cards
validate differently when creating tokensElements+ 1
more](https://docs.stripe.com/changelog/2011-09-15/cards-validate-differently-creating-tokens)[2011-08-01](https://docs.stripe.com/changelog/2011-08-01)Breaking
changes[Lists now provide a total count of items and a data fieldAffects all
products](https://docs.stripe.com/changelog/2011-08-01/lists-provide-total-count-data-field)[2011-06-28](https://docs.stripe.com/changelog/2011-06-28)Breaking
changes[Plans no longer include the identifier
fieldBilling](https://docs.stripe.com/changelog/2011-06-28/plans-no-longer-identifier-field)[2011-06-21](https://docs.stripe.com/changelog/2011-06-21)Breaking
changes[Errors now produce exceptions for unrecognized API parametersAffects all
products](https://docs.stripe.com/changelog/2011-06-21/exceptions-unrecognized-api-parameters)

## Links

- [Learn what's changing in Acacia](https://docs.stripe.com/changelog/acacia)
- [Adds support for blocking specific card brands in Checkout
SessionsCheckout](https://docs.stripe.com/changelog/acacia/2025-02-24/checkout_add_brands_blocked)
- [Checkout Sessions now group customer information in one
fieldCheckout](https://docs.stripe.com/changelog/acacia/2025-02-24/checkout-sessions-collected-info)
- [Credit grants can now be applied to specific
pricesBilling](https://docs.stripe.com/changelog/acacia/2025-02-24/billing-credits-price-level-applicability)
- [Credit grants can now be
prioritizedBilling](https://docs.stripe.com/changelog/acacia/2025-02-24/billing-credits-priority)
- [Makes shipping information an optional parameter for Afterpay
paymentsPayments](https://docs.stripe.com/changelog/acacia/2025-02-24/afterpay-shipping-details-optional)
- [Makes billing country and email fields optional for Klarna
paymentsPayments](https://docs.stripe.com/changelog/acacia/2025-02-24/cs_make_billing_country_and_email_field_optional_for_klarna_payments)
- [Adds metadata field to the Products API for creating an inline default
priceBilling](https://docs.stripe.com/changelog/acacia/2025-02-24/products-default-price-data-metadata-field)
- [Adds ability to schedule debit payments for a specific
datePayments](https://docs.stripe.com/changelog/acacia/2025-02-24/target-date)
- [Adds support for ownership exemption reason to the Accounts
APIConnect](https://docs.stripe.com/changelog/acacia/2025-01-27/ownership-exemption-reason-accounts-api)
- [Adds directorship declaration to the Accounts
APIConnect](https://docs.stripe.com/changelog/acacia/2025-01-27/directorship-declaration)
- [Adds proof of ultimate beneficial ownership as a document
typeConnect](https://docs.stripe.com/changelog/acacia/2025-01-27/proof-of-ultimate-beneficial-ownership-document-support)
- [Adds support for the Pay by Bank local payment methodCheckout+ 1
more](https://docs.stripe.com/changelog/acacia/2025-01-27/pay-by-bank-lpm)
- [Adds PayPal country property to the PaymentMethods and Charge
objectsPayments](https://docs.stripe.com/changelog/acacia/2025-01-27/paypal-country)
- [Adds discounts field to Checkout
SessionsCheckout](https://docs.stripe.com/changelog/acacia/2025-01-27/checkout-sessions-discounts-field)
- [Adds Sudan to allowed shipping countries for
CheckoutCheckout](https://docs.stripe.com/changelog/acacia/2025-01-27/checkout-sudan-shipping-support)
- [Adds advice code to
ChargesPayments](https://docs.stripe.com/changelog/acacia/2025-01-27/charge-outcome-advice-code)
- [Modify phone number collection on Payment LinksPayment
Links](https://docs.stripe.com/changelog/acacia/2025-01-27/add-phone-number-collection-update-payment-links-api)
- [Makes Issuing and Treasury embedded components generally availableIssuing+ 1
more](https://docs.stripe.com/changelog/acacia/2025-01-27/issuing-treasury-embedded-components)
- [Adds support for multiple financial accounts per
businessTreasury](https://docs.stripe.com/changelog/acacia/2025-01-27/multi-fa)
- [Adds support for collecting tips in JPY currency to
TerminalTerminal](https://docs.stripe.com/changelog/acacia/2025-01-27/terminal-jp-supported-country)
- [Adds SDK support for trace
IDsPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/trace-id-sdk)
- [Adds new balance transaction types to support minimum
balancePayouts](https://docs.stripe.com/changelog/acacia/2024-12-18/payout-minimum-balance)
- [Issuing authorizations now include merchant tax ID
numberIssuing](https://docs.stripe.com/changelog/acacia/2024-12-18/issuing-merchant-tax-id)
- [Creates Issuing authorizations when Stripe is
unavailableIssuing](https://docs.stripe.com/changelog/acacia/2024-12-18/issuing-auths-when-stripe-unavailable)
- [Adds additional beneficiary information for bank transfer
paymentsPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/new-bank-transfer-beneficiary-information)
- [Adds funding details to Amazon Pay and Revolut Pay
chargesPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/charge-pm-details)
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefixCheckout+ 1
more](https://docs.stripe.com/changelog/acacia/2024-12-18/mandate-reference-prefix)
- [Adds disabled reason to invoices, subscriptions, and schedulesTax+ 2
more](https://docs.stripe.com/changelog/acacia/2024-12-18/add-disabled-reason)
- [Adds support for tax ID types in 19 new
countriesTax](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-ids-19-new-countries)
- [Adds support for 21 new countries to the Tax Registration
APITax](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-registration-21-new-countries)
- [Adds support for reinstating Billing Credits on Invoice voidingBilling+ 1
more](https://docs.stripe.com/changelog/acacia/2024-12-18/billing-credits-invoice-voiding)
- [Modify trial subscriptions created by Payment LinksPayment
Links](https://docs.stripe.com/changelog/acacia/2024-12-18/add-trial-days-update-payment-links-api)
- [Billing Portal Configuration always returns period end date in
responsesBilling](https://docs.stripe.com/changelog/acacia/2024-12-18/portal-config-schedule-at-period-end-required)
- [Adds signature request as a replacement option for the Vault and Forward
APIAffects all
products](https://docs.stripe.com/changelog/acacia/2024-12-18/vault-and-forward-request-signature-replacement)
- [Adds network advice and decline
codesPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/network-advice-code-network-decline-code)
- [Supports redisplaying payment methods for Cards and
SourcesPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/cards-sources-allow-redisplay)
- [Adds field-level permissions for revenue and worker count in an Account’s
business
profileConnect](https://docs.stripe.com/changelog/acacia/2024-12-18/business-profile-revenue-worker-count)
- [Adds network transaction ID to
chargesPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/charge-display-network-transaction-id)
- [Adds regulated status field to card objects in several
APIsPayments](https://docs.stripe.com/changelog/acacia/2024-12-18/regulated-status)
- [Adds support for Service Tax
typeTax](https://docs.stripe.com/changelog/acacia/2024-11-20/service_tax)
- [Adds tax ID support for Liechtenstein
VATTax](https://docs.stripe.com/changelog/acacia/2024-11-20/li_vat)
- [Adds support for merchant amount and currency for test mode
authorizationsIssuing](https://docs.stripe.com/changelog/acacia/2024-11-20/add-merchant-currency-and-merchant-amount-on-create-testmode-authorization-method)
- [Adds support for issuing fraud
challengesIssuing](https://docs.stripe.com/changelog/acacia/2024-11-20/issuing-fraud-challenges)
- [Adds support for enabling Adaptive Pricing per Checkout
SessionCheckout](https://docs.stripe.com/changelog/acacia/2024-11-20/adaptive-pricing-param)
- [Customize the submit button recurring Payment Links and Checkout
SessionsCheckout+ 1
more](https://docs.stripe.com/changelog/acacia/2024-11-20/submit-type-recurring-cpl)
- [Adds support for advanced card features on Checkout
SessionsCheckout](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features)
- [Allows Link card-only integrations to accept non-card payments under Link
card
brandPayments](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand)
- [Adds additional beneficiary information for bank transfer
paymentsPayments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information)
- [Adds network decline code field for Swish and BLIK
refundsPayments](https://docs.stripe.com/changelog/acacia/2024-11-20/refunds-network-decline-code)
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference
prefixes in Checkout
SessionsCheckout](https://docs.stripe.com/changelog/acacia/2024-11-20/checkout-sessions-sepa-debit-bacs-debit-mandate-options)
- [Specifying an originating payment method for Inbound Transfers is now
optionalTreasury](https://docs.stripe.com/changelog/acacia/2024-11-20/inbound-transfers-optional-pm)
- [Use configurable capture methods and set up future usage for South Korean
payment
methodsCheckout](https://docs.stripe.com/changelog/acacia/2024-11-20/south-korea-payment-methods)
- [Trace payouts with a unique
identifierPayouts](https://docs.stripe.com/changelog/acacia/2024-11-20/payout-trace-id-api)
- [Converts properties on the Account object from a String to an
enumConnect](https://docs.stripe.com/changelog/acacia/2024-11-20/account-disabled-reason)
- [Adds indicator for connected accounts that must log in before using embedded
componentsConnect](https://docs.stripe.com/changelog/acacia/2024-11-20/account-sessions-stripe-authentication-response)
- [Adds support for authorizers to Person
APIConnect](https://docs.stripe.com/changelog/acacia/2024-11-20/authorizer-person-api)
- [Adds Credit Grant APIs and resourcesBilling+ 1
more](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-apis)
- [Adds support for pre-tax credit amount information to invoicesBilling+ 1
more](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-invoice)
- [Adds support for pre-tax credit amount information to credit notesBilling+ 1
more](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-credit-note)
- [Adds support for new South Korean payment methodsBilling+ 5
more](https://docs.stripe.com/changelog/acacia/2024-10-28/south-korean-payment-methods)
- [Adds support for Alma in FranceCheckout+ 3
more](https://docs.stripe.com/changelog/acacia/2024-10-28/alma)
- [Adds Event Destinations v2 API endpointAffects all
products](https://docs.stripe.com/changelog/acacia/2024-10-28/event-destinations-api)
- [Adds event type for updated receipt data in Issuing
transactionsIssuing](https://docs.stripe.com/changelog/acacia/2024-10-28/issuing-transactions-updated-receipt-event)
- [Adds a metadata field to the Vault and Forward
APIPayments](https://docs.stripe.com/changelog/acacia/2024-10-28/forwarding-api-metadata-field)
- [Adds Polish PLN currency support to Terminal tipping
configurationTerminal](https://docs.stripe.com/changelog/acacia/2024-10-28/terminal-tipping-pln)
- [Supports domain registration for Amazon
PayElements](https://docs.stripe.com/changelog/acacia/2024-10-28/amazon-pay-domain-registration)
- [Adds support for new countries to the Tax Registration
APITax](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-registration-new-countries)
- [Adds support for tax ID types in several new
countriesTax](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-ids)
- [Adds support for collecting retail delivery
feesTax](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-retail-delivery-fee)
- [Adds option to automatically validate customer tax location during an
updateTax](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-validate-location-auto)
- [Adds support for disabling Stripe user authentication for certain embedded
componentsConnect](https://docs.stripe.com/changelog/acacia/2024-10-28/disable-stripe-user-authentication-account-sessions)
- [Adds a test helper that updates the shipping status for physical
cardsIssuing](https://docs.stripe.com/changelog/acacia/2024-10-28/testmode-helper-shipping-status)
- [Adds created, updated, and failed events for all refund
typesPayments](https://docs.stripe.com/changelog/acacia/2024-10-28/refund-webhook-update)
- [Adds pricing groups to the Accounts APIConnect+ 1
more](https://docs.stripe.com/changelog/acacia/2024-10-28/pricing-groups-account-objects)
- [Adds scheduled subscription downgrades in the customer
portalBilling](https://docs.stripe.com/changelog/acacia/2024-10-28/customer-portal-schedule-downgrades)
- [Makes business profile optional for customer portal
configurationBilling](https://docs.stripe.com/changelog/acacia/2024-10-28/customer-portal-config-business-profile)
- [Uses Visa’s Compelling Evidence 3.0 to respond to qualifying disputesAffects
all
products](https://docs.stripe.com/changelog/acacia/2024-10-28/visa-compelling-evidence-3-0)
- [Adds support for scheduling invoice
finalizationInvoicing](https://docs.stripe.com/changelog/acacia/2024-10-28/schedule-invoice-finalization)
- [Adds contextual filters to billing
alertsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-contextualizing-filters)
- [Adds an Alerts API for usage-based
billingBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-api)
- [Adds an event for triggered billing
alertsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-trigger-event)
- [Adds support for listening to triggered billing
alertsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alert-webhook-listener)
- [Adds billing alert resources and
endpointsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-billing-alert-resources-endpoints)
- [Adds support for subscriptions and subscription items to billing
alertsBilling+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-alerts-subscription-items-subscriptions)
- [Adds Meter Event v2 API
endpointsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/usage-based-billing-v2-meter-events-api)
- [Updates consent modeling for saving cards with
TerminalTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay)
- [Adds support for configuring the reboot time
settingTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reboot-window)
- [Adds the Stripe S700 reader as a valid device
typeTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700)
- [Adds details about offline collection on card_present PaymentMethod
objectsTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-offline-details-card-present-paymentmethods)
- [Adds option to retrieve CVC tokens on Confirmation
TokensElements](https://docs.stripe.com/changelog/acacia/2024-09-30/support-payment-method-options-confirmation)
- [Adds customer ID to payment method preview on a confirmation
tokenElements](https://docs.stripe.com/changelog/acacia/2024-09-30/support-customer-payment-method-preview)
- [Adds support for identifying the unique payer for the BLIK payment
methodPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/buyer-id-blik)
- [Adds support for Affirm transaction
IDsPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/affirm-transaction-id-dashboard)
- [Adds support for in-person payment methods, including Interac
cardsTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/card-interac-present-support)
- [Displays authorization_code for
ChargesPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/displays-authorization-code-for-charges)
- [Adds wallet details for card_present Charges and Payment
MethodsTerminal](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-offline-details-card-present-paymentmethods)
- [Adds country field for Charges that use
KlarnaPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/charges-klarna-payer-details-country)
- [Displays Amazon Pay dispute type on
DisputesPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/display-amazonpay-dispute-type)
- [Adds support for three new payment methods: Multibanco, Twint, and ZipPayment
Links](https://docs.stripe.com/changelog/acacia/2024-09-30/payment-links-new-payment-methods)
- [Adds support for using the Multibanco payment method with
billingBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-mutlibanco-support)
- [Adds Twint to the PaymentMethodConfiguration
APIPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/twint-support-payment-method-configuration)
- [Adds Girocard as a PaymentMethod brand and
networkPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-girocard-paymentmethod-brand-network)
- [Adds Switzerland UID as a supported customer tax IDInvoicing+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/switzerland-tax-uid)
- [Adds Croatian Personal Identification Number to supported Tax IDsBilling+ 2
more](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-tax-id-type-hr_oib-croatian-personal-id-number)
- [Adds support for requiring a customer tax ID on Checkout and Payment
LinksCheckout+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/requiring-customer-tax-id-checkout-session-paymentlink)
- [Adds support for filtering by account subcategories on Financial
ConnectionsFinancial
Connections](https://docs.stripe.com/changelog/acacia/2024-09-30/financial-connections-filters)
- [Expands filtering support for Financial Connections SessionsFinancial
Connections](https://docs.stripe.com/changelog/acacia/2024-09-30/financial-connections-additional-filters)
- [Adds error code for exceeded transaction limitsInvoicing+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/error-code-transaction-limit)
- [Adds new error code for invalid mandate prefixes to Bacs Direct Debit and
SEPA Direct Debit
paymentsPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/error-code-invalid-mandate-reference-prefix)
- [Adds Invoice Rendering Templates for
InvoicesInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-resource)
- [Adds retrieve and archive methods for Invoice Rendering
TemplatesInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-methods)
- [Adds support for templates to Invoices and
CustomersInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-parameter)
- [Adds version support for Invoice Rendering
TemplatesInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-version)
- [Updates the default value for shipping address
validationIssuing](https://docs.stripe.com/changelog/acacia/2024-09-30/card-shipping-status-submitted-address-validation)
- [Adds address validation for physical
cardsIssuing](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-address-validation)
- [Adds a new webhook event for when funds are deducted as part of a
disputeIssuing](https://docs.stripe.com/changelog/acacia/2024-09-30/issuing-webhook-fund-deduction)
- [Adds support for bulk invoice line item
operationsInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/invoicing-bulk-line-item-operations)
- [Adds webhook events for when an invoice is due or
overdueBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-due-date-webhooks)
- [Adds option to automatically finalize
invoicesInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/automatically-finalizes-at-invoice)
- [Adds support for posting time on tax transaction
creationTax](https://docs.stripe.com/changelog/acacia/2024-09-30/tax-posting-time-on-creation)
- [Adds support for tax settings and registrations for Embedded
ComponentsConnect+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/tax-registrations-settings-embedded-components)
- [Adds new method to retrieve a Tax
CalculationTax](https://docs.stripe.com/changelog/acacia/2024-09-30/retrieves-tax-calculation-api)
- [Adds support for specifying US state sales tax elections while creating tax
registrationsTax](https://docs.stripe.com/changelog/acacia/2024-09-30/support-us-state-sales-tax-elections-api)
- [Adds risk verification details for connected
accountsConnect](https://docs.stripe.com/changelog/acacia/2024-09-30/additional-risk-verification-details-connected-accounts)
- [Adds support for email types to Credit
NotesInvoicing](https://docs.stripe.com/changelog/acacia/2024-09-30/credit-note-email-type)
- [Adds support for the Payment Element on a Customer
SessionElements](https://docs.stripe.com/changelog/acacia/2024-09-30/support-payment-element-customer-session)
- [Adds support for identifying the case type for card
disputesPayments](https://docs.stripe.com/changelog/acacia/2024-09-30/disputes-case-type-card)
- [Adds a method to update the metadata for Checkout
SessionsCheckout](https://docs.stripe.com/changelog/acacia/2024-09-30/checkout-update-method)
- [Adds parameter to link Verification Sessions to
CustomersIdentity](https://docs.stripe.com/changelog/acacia/2024-09-30/identity-verification-session-related-customer)
- [Displays CHIPS tracking details for outbound wire payments and
transfersTreasury](https://docs.stripe.com/changelog/acacia/2024-09-30/displays-chips-tracking-details-treasury-outbound-wires)
- [Adds additional reasonable defaulting to the Account Link API
v1Connect](https://docs.stripe.com/changelog/acacia/2024-09-30/account-link-api-default-fields-v1)
- [Makes LineItem.description
optionalCheckout](https://docs.stripe.com/changelog/acacia/2024-09-30/description-optional-checkout-session-line-item)
- [Adds target_frozen_time for advancing test_helpers.test_clock
objectsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/support-status-details-test-clock)
- [Makes status details for Test Clock test helpers
requiredBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/make-testclock-status-details-required)
- [Adds a new enum value representing a ReceivedDebit failure due to an
international
transactionTreasury](https://docs.stripe.com/changelog/acacia/2024-09-30/ef-features)
- [Makes it optional to update the products and prices of a
subscriptionBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-portal-updates-optional)
- [Add support for custom_unit_amount during product creationCheckout+ 1
more](https://docs.stripe.com/changelog/acacia/2024-09-30/products-custom-unit-amount)
- [Adds support for retrieving thin
eventsBilling](https://docs.stripe.com/changelog/acacia/2024-09-30/api-v2-thin-events)
- [2024-06-20](https://docs.stripe.com/changelog/2024-06-20)
- [Renames a fuel attribute of the Authorization
objectIssuing](https://docs.stripe.com/changelog/2024-06-20/renames-fuel-attribute-authorization-object)
- [Renames a purchase_details attribute of the Transaction
objectIssuing](https://docs.stripe.com/changelog/2024-06-20/renames-purchase-details-transaction-object)
- [Removes undocumented fuel
fieldsIssuing](https://docs.stripe.com/changelog/2024-06-20/removes-undocumented-fuel-fields-issuing)
- [Removes undocumented fleet
fieldsIssuing](https://docs.stripe.com/changelog/2024-06-20/removes-undocumented-fleet-fields-issuing)
- [Adds enum values for fuel
unitsIssuing](https://docs.stripe.com/changelog/2024-06-20/adds-enum-fuel-units-issuing)
- [Deprecates alphanumeric_id for Issuing
AuthorizationIssuing](https://docs.stripe.com/changelog/2024-06-20/deprecates-alphanumeric-id-issuing)
- [Adds enum values for disabled
reasonsConnect](https://docs.stripe.com/changelog/2024-06-20/adds-enum-disabled-reasons-capabilities)
- [Deprecates the bank_transfer_payments capability type in favor of newer
capability
typesConnect](https://docs.stripe.com/changelog/2024-06-20/deprecates-bank-transfer-payments-capabilities)
- [Adds new enum values for request history
reasonsIssuing](https://docs.stripe.com/changelog/2024-06-20/adds-enum-request-history-reasons-issuing)
- [2024-04-10](https://docs.stripe.com/changelog/2024-04-10)
- [Makes automatic sync the default capture method for PaymentIntents when not
specifiedPayments](https://docs.stripe.com/changelog/2024-04-10/automatic-sync-default-paymenintents)
- [Renames the rendering_options attribute for invoices to renderingInvoicing+ 1
more](https://docs.stripe.com/changelog/2024-04-10/renames-rendering-options-invoicing)
- [Renames the features attribute of the Product objectInvoicing+ 1
more](https://docs.stripe.com/changelog/2024-04-10/renames-features-attribute-product-object)
- [2023-10-16](https://docs.stripe.com/changelog/2023-10-16)
- [Adds new account requirement error codes to the Accounts
APIConnect](https://docs.stripe.com/changelog/2023-10-16/adds-account-requirement-error-accounts)
- [Auto-populates the statement descriptor and prefix in the Accounts
APIConnect](https://docs.stripe.com/changelog/2023-10-16/auto-populates-statement-descriptor-accounts)
- [2023-08-16](https://docs.stripe.com/changelog/2023-08-16)
- [Enables automatic payment methods by default for PaymentIntents and
SetupIntentsPayments+ 1
more](https://docs.stripe.com/changelog/2023-08-16/automatic-payment-methods)
- [One-time payments in Checkout Sessions support no-cost
ordersCheckout](https://docs.stripe.com/changelog/2023-08-16/no-cost-orders-checkout-session)
- [Platform-scope rendering for select PaymentMethod fingerprintsConnect+ 2
more](https://docs.stripe.com/changelog/2023-08-16/platform-scope-rendering-payment-method)
- [Adds specific error codes for failed Klarna paymentsPayments+ 1
more](https://docs.stripe.com/changelog/2023-08-16/klarna-payment-failure-error-code)
- [Adds new director verification error codes to the Accounts
APIConnect](https://docs.stripe.com/changelog/2023-08-16/adds-director-verfication-error-accounts)
- [2022-11-15](https://docs.stripe.com/changelog/2022-11-15)
- [The Charges object no longer auto-expands refunds by
defaultPayments](https://docs.stripe.com/changelog/2022-11-15/deprecates-charges-auto-expand)
- [Removes the charges attribute from the PaymentIntent
objectPayments](https://docs.stripe.com/changelog/2022-11-15/removes-charges-attribute-paymentintent)
- [Adds new decline codes to the PaymentIntent and PaymentMethod
APIsPayments](https://docs.stripe.com/changelog/2022-11-15/adds-decline-codes-paymentintent-paymentmethod)
- [Adds new decline codes to the SetupIntent
APIPayments](https://docs.stripe.com/changelog/2022-11-15/adds-decline-codes-setupintent)
- [Adds a new structure error code to the Accounts
APIConnect](https://docs.stripe.com/changelog/2022-11-15/adds-structure-error-code-accounts)
- [2022-08-01](https://docs.stripe.com/changelog/2022-08-01)
- [Removes the include_and_require value when creating
invoicesInvoicing](https://docs.stripe.com/changelog/2022-08-01/removes-include-require-value-invoices)
- [Default customer creation in Checkout Session payment mode changed to
if_requiredCheckout](https://docs.stripe.com/changelog/2022-08-01/default-customer-creation-checkout-session)
- [Deferred PaymentIntent creation in Checkout Session payment modeCheckout+ 1
more](https://docs.stripe.com/changelog/2022-08-01/deferred-paymentintent-checkout-session)
- [Removes the setup_intent property from Checkout Sessions in subscription
modeCheckout](https://docs.stripe.com/changelog/2022-08-01/removes-setupintent-checkout-session)
- [Replaces line item parameters from the Create Checkout Session
endpointCheckout](https://docs.stripe.com/changelog/2022-08-01/replaces-line-item-create-checkout-session)
- [Removes the subscription data parameter from the Create Checkout Session
endpointCheckout+ 1
more](https://docs.stripe.com/changelog/2022-08-01/removes-subscription-data-create-checkout-session)
- [Removes the shipping rate parameter from Create Checkout Session
endpointCheckout](https://docs.stripe.com/changelog/2022-08-01/removes-shipping-rate-create-checkout-session)
- [Updates Checkout Session shipping
propertiesCheckout](https://docs.stripe.com/changelog/2022-08-01/updates-shipping-property-checkout-session)
- [Adds 3D Secure exemption status to card
chargesPayments](https://docs.stripe.com/changelog/2022-08-01/adds-3d-secure-exemption-charges)
- [New error code for invalid terms of service acceptance in Accounts
APIConnect](https://docs.stripe.com/changelog/2022-08-01/error-code-invalid-tos-accounts)
- [New endpoints for managing a physical card’s shipping status in test
modeIssuing](https://docs.stripe.com/changelog/2022-08-01/endpoints-shipping-status-cards)
- [Adds design_rejected as a possible cancellation reason for issued
cardsIssuing](https://docs.stripe.com/changelog/2022-08-01/adds-design-rejected-value-cards)
- [Removes the default_currency attribute from the Customer objectAffects all
products](https://docs.stripe.com/changelog/2022-08-01/removes-default-currency-customer-object)
- [2020-08-27](https://docs.stripe.com/changelog/2020-08-27)
- [Removes the tax_percent attributeCheckout+ 2
more](https://docs.stripe.com/changelog/2020-08-27/removes-tax-percent-attribute)
- [Renames phases attributes in subscription
schedulesBilling](https://docs.stripe.com/changelog/2020-08-27/renames-phases-attributes-subscription-schedules)
- [Renames event type that triggers on automatic
updatesPayments](https://docs.stripe.com/changelog/2020-08-27/renames-automatically-updated-event-type)
- [Removes the display_items property from Checkout
SessionsCheckout](https://docs.stripe.com/changelog/2020-08-27/removes-display-items-checkout-session)
- [Formats requirements for key persons associated with
accountsConnect](https://docs.stripe.com/changelog/2020-08-27/formats-requirements-key-persons-accounts)
- [Adds new error codes to the Accounts, Persons, and Capabilities
APIsConnect](https://docs.stripe.com/changelog/2020-08-27/adds-error-codes-accounts-persons-capabilities)
- [Updates to 3D Secure details in Charge
objectPayments](https://docs.stripe.com/changelog/2020-08-27/updates-3d-scure-charge-object)
- [Customer subscriptions are no longer auto-expanded by
defaultBilling](https://docs.stripe.com/changelog/2020-08-27/deprecates-auto-expansion-customer-subscriptions)
- [Plan tiers are no longer auto-expanded by
defaultBilling](https://docs.stripe.com/changelog/2020-08-27/deprecates-auto-expansion-plan-tiers)
- [Customer sources are no longer auto-expanded by defaultPayments+ 2
more](https://docs.stripe.com/changelog/2020-08-27/deprecates-auto-expansion-customer-sources)
- [Tax IDs are no longer auto-expanded on the Customer objectAffects all
products](https://docs.stripe.com/changelog/2020-08-27/deprecates-auto-expansion-tax-id-customer)
- [Deprecates subscription prorate and subscription_prorate
parametersBilling](https://docs.stripe.com/changelog/2020-08-27/deprecates-prorate-parameters-subscriptions)
- [2020-03-02](https://docs.stripe.com/changelog/2020-03-02)
- [Invoices can now be numbered sequentially across your accountBilling+ 1
more](https://docs.stripe.com/changelog/2020-03-02/sequentially-number-invoices)
- [2019-12-03](https://docs.stripe.com/changelog/2019-12-03)
- [Standardizes invoice line item IDsBilling+ 1
more](https://docs.stripe.com/changelog/2019-12-03/standardizes-invoice-line-item-ids)
- [New requirement for out_of_band_amount when creating post-payment credit
notesBilling+ 1
more](https://docs.stripe.com/changelog/2019-12-03/post-payment-credit-note-requirement)
- [Customer balances are now returned when voiding invoicesBilling+ 1
more](https://docs.stripe.com/changelog/2019-12-03/customer-balances-returned-voided-invoices)
- [Removes deprecated tax information fields from the Customer objectAffects all
products](https://docs.stripe.com/changelog/2019-12-03/removes-deprecated-tax-information-fields)
- [2019-11-05](https://docs.stripe.com/changelog/2019-11-05)
- [Adds requirement for requested_capabilities on custom account
creationConnect](https://docs.stripe.com/changelog/2019-11-05/adds-requested-capabilities-requirement-custom-account)
- [Nested subscription schedule settings under
default_settingsBilling](https://docs.stripe.com/changelog/2019-11-05/nests-subscription-schedule-settings)
- [2019-10-17](https://docs.stripe.com/changelog/2019-10-17)
- [Renames and updates subscription schedule renewal
propertiesBilling](https://docs.stripe.com/changelog/2019-10-17/updates-subscription-renewal-properties)
- [Replaces the subscription start field with
start_dateBilling](https://docs.stripe.com/changelog/2019-10-17/replaces-subscription-start-field)
- [Renames billing to collection_method on invoices, subscriptions, and
subscription schedulesBilling+ 1
more](https://docs.stripe.com/changelog/2019-10-17/renames-billing-attribute)
- [The due_date property is always null on auto-billed invoicesBilling+ 1
more](https://docs.stripe.com/changelog/2019-10-17/invoice-due-date-null)
- [Renames account_balance to balance on Customer objectBilling+ 1
more](https://docs.stripe.com/changelog/2019-10-17/renames-account-balance-customer-object)
- [2019-10-08](https://docs.stripe.com/changelog/2019-10-08)
- [Renames a Person object relationship
attributeConnect](https://docs.stripe.com/changelog/2019-10-08/renames-person-object-relationship-attribute)
- [2019-09-09](https://docs.stripe.com/changelog/2019-09-09)
- [Accounts in many countries now require specifying capabilities at creation
timeConnect](https://docs.stripe.com/changelog/2019-09-09/2019-09-09-1)
- [Adds new details_code values to person document
verificationConnect](https://docs.stripe.com/changelog/2019-09-09/adds-detail-code-person-document-verification)
- [2019-08-14](https://docs.stripe.com/changelog/2019-08-14)
- [Renames the platform_payments capability for accounts to card_payments,
requiring the manual specification of the added transfers
capabilityConnect](https://docs.stripe.com/changelog/2019-08-14/configuring-person-account-opener-no-longer-sets-executive)
- [Configuring a person as an account opener no longer automatically sets them
as an
executiveConnect](https://docs.stripe.com/changelog/2019-08-14/accounts-many-countries-require-specifying-capabilities)
- [2019-05-16](https://docs.stripe.com/changelog/2019-05-16)
- [Bank pull payments no longer expose internal system refunds on
failurePayments](https://docs.stripe.com/changelog/2019-05-16/renames-platform-payments-capability-card-payments)
- [2019-03-14](https://docs.stripe.com/changelog/2019-03-14)
- [Renames application_fee on invoices to application_fee_amountConnect+ 1
more](https://docs.stripe.com/changelog/2019-03-14/renames-application-fee-invoices-application-fee-amount)
- [Subscriptions are now successfully created even if the first payment
failsBilling](https://docs.stripe.com/changelog/2019-03-14/subscriptions-successfully-created-first-payment-fails)
- [Invoices now provide timestamps for each state transitionBilling+ 1
more](https://docs.stripe.com/changelog/2019-03-14/invoices-provide-timestamps-state-transitions)
- [Renames the date field for invoices to createdBilling+ 1
more](https://docs.stripe.com/changelog/2019-03-14/renames-date-field-invoices-created)
- [Invoices now specify when they’re finalized alongside other status
transitionsBilling+ 1
more](https://docs.stripe.com/changelog/2019-03-14/invoices-specify-finalized-alongside-status-transitions)
- [2019-02-19](https://docs.stripe.com/changelog/2019-02-19)
- [Changes statement descriptor behaviors for card payments created with
ChargesPayments](https://docs.stripe.com/changelog/2019-02-19/changes-statement-descriptor-behaviors-charges)
- [Several account fields have been refactored to better describe legal entity,
verification status and requirements, and configurable
settingsConnect](https://docs.stripe.com/changelog/2019-02-19/several-fields-accounts-refactored)
- [Several fields describing an account’s business details have moved to the
business_profile
subhashConnect](https://docs.stripe.com/changelog/2019-02-19/business-details-moved-business-profile-object)
- [Verification of accounts or persons now supports uploading both front and
back
sidesConnect](https://docs.stripe.com/changelog/2019-02-19/verification-accounts-persons-supports-front-back)
- [Accounts no longer provide a keys field. Platforms should use their own API
key to authenticate as their connected
accountsConnect](https://docs.stripe.com/changelog/2019-02-19/accounts-no-longer-provide-keys-field)
- [Accounts in the US now require specifying capabilities at creation
timeConnect](https://docs.stripe.com/changelog/2019-02-19/accounts-us-require-specifying-capabilities-creation)
- [Renames the business_id_number for an account’s legal entity to
business_registration_numberConnect](https://docs.stripe.com/changelog/2019-02-19/renames-business-id-number-business-registration-number)
- [2019-02-11](https://docs.stripe.com/changelog/2019-02-11)
- [Renames several statuses for
PaymentIntentsPayments](https://docs.stripe.com/changelog/2019-02-11/renames-several-statuses-payment-intents)
- [Renames the save_source_to_customer field for sources to
save_payment_methodPayments](https://docs.stripe.com/changelog/2019-02-11/renames-save-source-to-customer-save-payment-method)
- [Renames the allowed_source_types field for sources to
payment_method_typesPayments](https://docs.stripe.com/changelog/2019-02-11/renames-allowed-source-types-payment-method-types)
- [Renames the next_source_action field for Payment Intents to
next_actionPayments](https://docs.stripe.com/changelog/2019-02-11/renames-next-source-action-next-action)
- [Renames the authorize_with_url field for Payment Intents to
redirect_to_urlPayments](https://docs.stripe.com/changelog/2019-02-11/renames-authorize-with-url-redirect-to-url)
- [2018-11-08](https://docs.stripe.com/changelog/2018-11-08)
- [Invoices now specify their automatic collection behavior using the
auto_advance fieldInvoicing+ 1
more](https://docs.stripe.com/changelog/2018-11-08/invoices-specify-auto-advance-field)
- [One-off Invoices no longer automatically collect payment by
defaultInvoicing](https://docs.stripe.com/changelog/2018-11-08/one-off-invoices-no-longer-auto-collect-payment)
- [Replaces the forgiven field with a new uncollectible status for
invoicesInvoicing+ 1
more](https://docs.stripe.com/changelog/2018-11-08/mark-invoice-uncollectible-instead-forgiven)
- [Renames an invoice error code to invoice_already_finalizedInvoicing+ 1
more](https://docs.stripe.com/changelog/2018-11-08/renames-invoice-error-code-invoice-already-finalized)
- [Includes several changes for users of the Payment Intents API private
betaPayments](https://docs.stripe.com/changelog/2018-11-08/several-changes-payment-intents-private-beta)
- [2018-10-31](https://docs.stripe.com/changelog/2018-10-31)
- [Descriptions for customers now have a character limitAffects all
products](https://docs.stripe.com/changelog/2018-10-31/descriptions-customers-character-limit)
- [Product names now have a character limitBilling+ 1
more](https://docs.stripe.com/changelog/2018-10-31/names-products-character-limit)
- [Descriptions for invoice line items now have a character limitBilling+ 1
more](https://docs.stripe.com/changelog/2018-10-31/descriptions-invoice-line-items-character-limit)
- [The billing_reason of the first invoice of a subscription is now
subscription_createBilling+ 1
more](https://docs.stripe.com/changelog/2018-10-31/first-invoice-subscription-billing-reason-subscription-create)
- [2018-09-24](https://docs.stripe.com/changelog/2018-09-24)
- [Renames the FileUpload object to Files, which now require secret keys to
download filesAffects all
products](https://docs.stripe.com/changelog/2018-09-24/file-uploads-renamed-files-require-secret-keys)
- [2018-09-06](https://docs.stripe.com/changelog/2018-09-06)
- [SKU values no longer need to be
uniqueCheckout](https://docs.stripe.com/changelog/2018-09-06/sku-values-no-longer-need-unique)
- [2018-08-23](https://docs.stripe.com/changelog/2018-08-23)
- [A subscription’s ending period can no longer be configured while canceling
itBilling](https://docs.stripe.com/changelog/2018-08-23/subscription-ending-period-cannot-configured-canceling)
- [Customers now provide a tax_info object with their tax ID detailsAffects all
products](https://docs.stripe.com/changelog/2018-08-23/customers-provide-tax-info-object)
- [Renames the amount field for plan tiers to
unit_amountBilling](https://docs.stripe.com/changelog/2018-08-23/renames-amount-field-plan-tiers-unit-amount)
- [2018-07-27](https://docs.stripe.com/changelog/2018-07-27)
- [Subscriptions no longer support modifying the source parameter
directlyBilling](https://docs.stripe.com/changelog/2018-07-27/subscriptions-no-longer-support-modifying-source)
- [Ending a subscription trial now uses the timestamp of that API
requestBilling](https://docs.stripe.com/changelog/2018-07-27/ending-subscription-trial-uses-request-timestamp)
- [Coupons now use floats rather than integers to specify percent_offBilling+ 1
more](https://docs.stripe.com/changelog/2018-07-27/coupons-use-floats-specify-percent-off)
- [Stripe now validates email addresses when creating or updating
customersAffects all
products](https://docs.stripe.com/changelog/2018-07-27/stripe-validates-email-addresses-customers)
- [2018-05-21](https://docs.stripe.com/changelog/2018-05-21)
- [Products no longer embed lists of
SKUsCheckout](https://docs.stripe.com/changelog/2018-05-21/products-no-longer-embed-sku-lists)
- [Invoice line items now have unique IDs andcan’t be used in place of a
subscriptionBilling+ 1
more](https://docs.stripe.com/changelog/2018-05-21/invoice-line-items-have-unique-ids-cannot-use-subscription)
- [Coupons, SKUs, customers, products, and plans now limit the valid characters
for IDsBilling+ 1
more](https://docs.stripe.com/changelog/2018-05-21/valid-characters-ids-coupons-skus-customers-products-plans)
- [Subscriptions now default to not defining their trial periods depending on a
planBilling](https://docs.stripe.com/changelog/2018-05-21/subscriptions-default-no-trial-period-plan)
- [Changing a subscription to a new plan with a trial now extends the trial
periodBilling](https://docs.stripe.com/changelog/2018-05-21/changing-subscription-new-plan-extends-trial)
- [2018-02-28](https://docs.stripe.com/changelog/2018-02-28)
- [Updating a canceled subscription on a future date no longer resets its
statusBilling](https://docs.stripe.com/changelog/2018-02-28/updating-canceled-subscription-no-longer-resets-status)
- [2018-02-06](https://docs.stripe.com/changelog/2018-02-06)
- [Sources now provide a recommended value when the issuer advises using 3D
SecurePayments](https://docs.stripe.com/changelog/2018-02-06/sources-provide-recommended-use-3d-secure)
- [2018-02-05](https://docs.stripe.com/changelog/2018-02-05)
- [Free plans with prorations now produce zero-dollar
invoicesBilling](https://docs.stripe.com/changelog/2018-02-05/free-plans-with-prorations-produce-zero-dollar-invoices)
- [Subscriptions can now delay the first full invoice to a future date (and
optionally include a free
trial)Billing](https://docs.stripe.com/changelog/2018-02-05/subscriptions-delay-first-full-invoice-future-date)
- [Plans now link to individual products, with several fields moving to the
product
resourceBilling](https://docs.stripe.com/changelog/2018-02-05/plans-link-individual-products-several-fields-moved)
- [Products now require a type field, differentiating their use with order SKUs
or subscriptions and plansBilling+ 1
more](https://docs.stripe.com/changelog/2018-02-05/products-require-type-field-differentiating-use)
- [2018-01-23](https://docs.stripe.com/changelog/2018-01-23)
- [Connect platforms can identify reused card or bank accounts across connected
accounts as they now will share the same
fingerprintConnect](https://docs.stripe.com/changelog/2018-01-23/connect-platforms-identify-reused-cards-bank-accounts)
- [2017-12-14](https://docs.stripe.com/changelog/2017-12-14)
- [Invoice line items now must always set a descriptionInvoicing+ 1
more](https://docs.stripe.com/changelog/2017-12-14/invoice-line-items-must-set-description)
- [Invoice payment failures now return a card_error when a charge is
declinedInvoicing+ 1
more](https://docs.stripe.com/changelog/2017-12-14/invoice-payment-failures-return-card-error)
- [2017-08-15](https://docs.stripe.com/changelog/2017-08-15)
- [Sources can now specify that an authentication redirect isn’t
requiredPayments](https://docs.stripe.com/changelog/2017-08-15/sources-specify-no-authentication-redirect-required)
- [2017-06-05](https://docs.stripe.com/changelog/2017-06-05)
- [Accounts can now specify why an account isn’t enabled with the new reason
under_reviewConnect](https://docs.stripe.com/changelog/2017-06-05/accounts-specify-under-review-reason)
- [2017-05-25](https://docs.stripe.com/changelog/2017-05-25)
- [Events for Connect now specify the originating connected account using the
account
fieldConnect](https://docs.stripe.com/changelog/2017-05-25/events-connect-specify-originating-account)
- [The request field of the Events object now specifies both the request ID and
idempotency keyAffects all
products](https://docs.stripe.com/changelog/2017-05-25/events-specify-request-id-idempotency-key)
- [Events with the previous_attributes field now render the complete affected
sub-arrayAffects all
products](https://docs.stripe.com/changelog/2017-05-25/events-previous-attributes-render-complete-sub-array)
- [Accounts must now specify one of three types (Standard, Express, or
Custom)Connect](https://docs.stripe.com/changelog/2017-05-25/accounts-specify-type-standard-express-custom)
- [2017-04-06](https://docs.stripe.com/changelog/2017-04-06)
- [Transfers are now split into payouts and
transfersConnect](https://docs.stripe.com/changelog/2017-04-06/transfers-split-payouts-transfers)
- [2017-02-14](https://docs.stripe.com/changelog/2017-02-14)
- [Charges now specify the ID for the rule blocking a transaction, which can be
expandedPayments+ 1
more](https://docs.stripe.com/changelog/2017-02-14/charges-specify-rule-blocking-transaction)
- [Charges now specify the ID for the dispute associated with a transaction,
which can be
expandedPayments](https://docs.stripe.com/changelog/2017-02-14/charges-specify-dispute-associated-transaction)
- [2017-01-27](https://docs.stripe.com/changelog/2017-01-27)
- [Balance transactions no longer include the sourced_transfers fieldPayments+ 1
more](https://docs.stripe.com/changelog/2017-01-27/balance-transactions-no-longer-include-sourced-transfers)
- [2016-10-19](https://docs.stripe.com/changelog/2016-10-19)
- [Using insufficient permissions to make API requests now throws an HTTP 403
errorAffects all
products](https://docs.stripe.com/changelog/2016-10-19/insufficient-permissions-throw-403-error)
- [2016-07-06](https://docs.stripe.com/changelog/2016-07-06)
- [Filter lists of subscriptions for canceled
subscriptionsBilling](https://docs.stripe.com/changelog/2016-07-06/filter-canceled-subscriptions-retrieve-individually)
- [2016-06-15](https://docs.stripe.com/changelog/2016-06-15)
- [Deactivating a product no longer automatically deactivates its
SKUsBilling](https://docs.stripe.com/changelog/2016-06-15/deactivating-product-deactivates-skus)
- [2016-03-07](https://docs.stripe.com/changelog/2016-03-07)
- [Supported currencies are defined on the country spec for an account’s
countryPayments](https://docs.stripe.com/changelog/2016-03-07/supported-currencies-defined-country-spec)
- [2016-02-29](https://docs.stripe.com/changelog/2016-02-29)
- [Creating or updating an account now validates the postal code for its legal
entityConnect](https://docs.stripe.com/changelog/2016-02-29/creating-updating-account-validates-postal-code)
- [2016-02-23](https://docs.stripe.com/changelog/2016-02-23)
- [Orders that are paid or fulfilled, and then become canceled or returned, now
automatically refund associated
chargesPayments](https://docs.stripe.com/changelog/2016-02-23/orders-paid-fulfilled-refund-associated-charges)
- [2016-02-22](https://docs.stripe.com/changelog/2016-02-22)
- [You can no longer add more than 250 invoice items to an invoiceBilling+ 1
more](https://docs.stripe.com/changelog/2016-02-22/no-more-than-250-invoice-items)
- [2016-02-19](https://docs.stripe.com/changelog/2016-02-19)
- [Renames the name field on Bank Accounts to
account_holder_namePayments](https://docs.stripe.com/changelog/2016-02-19/renames-name-field-bank-accounts-account-holder-name)
- [2016-02-03](https://docs.stripe.com/changelog/2016-02-03)
- [Accounts now only show country-specific subfields for the legal_entity
fieldConnect](https://docs.stripe.com/changelog/2016-02-03/accounts-only-show-country-fields-legal-entity)
- [2015-10-16](https://docs.stripe.com/changelog/2015-10-16)
- [Creating or updating customers must now include a plan if a tax percentage is
specifiedBilling](https://docs.stripe.com/changelog/2015-10-16/customers-must-include-plan-tax-percentage)
- [2015-10-12](https://docs.stripe.com/changelog/2015-10-12)
- [Using invalid parameters to create cards or bank accounts for tokens,
sources, or external bank accounts now throws an HTTP 400
errorPayments](https://docs.stripe.com/changelog/2015-10-12/invalid-parameters-throw-400-error)
- [2015-10-01](https://docs.stripe.com/changelog/2015-10-01)
- [Bank account information renamed to external accounts on user
profilesConnect](https://docs.stripe.com/changelog/2015-10-01/accounts-include-external-accounts-field)
- [Accounts now include an external_accounts
fieldConnect](https://docs.stripe.com/changelog/2015-10-01/accounts-specify-additional-fields-bank-accounts)
- [2015-09-23](https://docs.stripe.com/changelog/2015-09-23)
- [The charge field now always reflects the latest charge on invoicesInvoicing+
1
more](https://docs.stripe.com/changelog/2015-09-23/invoice-charge-field-reflect-latest-charge)
- [Invoices no longer include the payment propertyInvoicing+ 1
more](https://docs.stripe.com/changelog/2015-09-23/invoices-no-longer-include-payment-field)
- [Listing all charges now includes payments from all funding
sourcesPayments](https://docs.stripe.com/changelog/2015-09-23/listing-charges-includes-payments-funding-sources)
- [Charges only support an offset for list pagination when filtering by
sourcePayments](https://docs.stripe.com/changelog/2015-09-23/charges-support-offset-list-pagination-source)
- [2015-09-08](https://docs.stripe.com/changelog/2015-09-08)
- [Rate-limited requests now return an HTTP 429 error, no longer including the
rate_limit fieldAffects all
products](https://docs.stripe.com/changelog/2015-09-08/rate-limited-requests-return-429-no-rate-limit)
- [2015-09-03](https://docs.stripe.com/changelog/2015-09-03)
- [Requests that reuse idempotency tokens but alter request parameters now throw
an errorAffects all
products](https://docs.stripe.com/changelog/2015-09-03/reuse-idempotency-tokens-alter-error)
- [2015-08-19](https://docs.stripe.com/changelog/2015-08-19)
- [Balance transactions with refunds or disputes now specify the corresponding
ID in the source
fieldPayments](https://docs.stripe.com/changelog/2015-08-19/balance-transactions-refunds-disputes-specify-source)
- [2015-08-07](https://docs.stripe.com/changelog/2015-08-07)
- [Stripe now ensures the tos_acceptance[date] field on accounts is a valid
timestampConnect](https://docs.stripe.com/changelog/2015-08-07/stripe-ensures-tos-acceptance-date-valid-timestamp)
- [2015-07-28](https://docs.stripe.com/changelog/2015-07-28)
- [Transfers that are immediately processed now trigger the balance.available
eventConnect](https://docs.stripe.com/changelog/2015-07-28/transfers-immediately-processed-trigger-balance-available)
- [2015-07-13](https://docs.stripe.com/changelog/2015-07-13)
- [Accounts now include the verification[disabled_reason] field to describe why
theycan’t make transfers or
chargesConnect](https://docs.stripe.com/changelog/2015-07-13/accounts-include-verification-disabled-reason-field)
- [2015-07-07](https://docs.stripe.com/changelog/2015-07-07)
- [Transfers submitted to the bank that haven’t arrived now provide an
in_transit
statusConnect](https://docs.stripe.com/changelog/2015-07-07/transfers-in-transit-provide-status)
- [2015-06-15](https://docs.stripe.com/changelog/2015-06-15)
- [Accounts on manual payout schedules now throw a new
errorConnect](https://docs.stripe.com/changelog/2015-06-15/accounts-manual-payout-schedules-throw-error)
- [2015-04-07](https://docs.stripe.com/changelog/2015-04-07)
- [Updates how ending periods are calculated on prorated invoice line
itemsBilling](https://docs.stripe.com/changelog/2015-04-07/updates-ending-periods-prorated-invoice-line-items)
- [Changes the sorting order of lines for invoicesBilling+ 1
more](https://docs.stripe.com/changelog/2015-04-07/changes-sorting-order-lines-invoices)
- [2015-03-24](https://docs.stripe.com/changelog/2015-03-24)
- [By default, coupons no longer apply to invoice items with negative
amountsBilling+ 1
more](https://docs.stripe.com/changelog/2015-03-24/coupons-no-longer-apply-negative-invoice-items)
- [2015-02-18](https://docs.stripe.com/changelog/2015-02-18)
- [Charges that succeed now have a succeeded
statusPayments](https://docs.stripe.com/changelog/2015-02-18/charges-succeed-have-succeeded-status)
- [Charges now have a source field that accepts a source or
cardPayments](https://docs.stripe.com/changelog/2015-02-18/charges-have-source-field-accepts-source-card)
- [Customers now have a source field that accepts a source or card, and updates
related event
typesPayments](https://docs.stripe.com/changelog/2015-02-18/customers-have-source-field-accepts-source-card)
- [2015-02-16](https://docs.stripe.com/changelog/2015-02-16)
- [Renames the transfer.canceled event type to
transfer.reversedConnect](https://docs.stripe.com/changelog/2015-02-16/renames-transfer-canceled-event-transfer-reversed)
- [2015-02-10](https://docs.stripe.com/changelog/2015-02-10)
- [Dispute statuses now include the warning_closed
valuePayments](https://docs.stripe.com/changelog/2015-02-10/dispute-statuses-include-warning-closed)
- [Transfers now require a sufficient account balance in test mode to better
simulate live
modeConnect](https://docs.stripe.com/changelog/2015-02-10/transfers-require-sufficient-balance-test-mode)
- [2015-01-26](https://docs.stripe.com/changelog/2015-01-26)
- [Events with the previous_attributes field now only render the differences to
objects across updatesAffects all
products](https://docs.stripe.com/changelog/2015-01-26/events-previous-attributes-render-differences)
- [Subscriptions now only report the timestamp for API or invoice payment
failures for the canceled_at
fieldBilling](https://docs.stripe.com/changelog/2015-01-26/subscriptions-report-api-invoice-failures)
- [2015-01-11](https://docs.stripe.com/changelog/2015-01-11)
- [File uploads describe their file type with the simpler type field and
formatAffects all
products](https://docs.stripe.com/changelog/2015-01-11/file-uploads-describe-type-format)
- [2014-12-22](https://docs.stripe.com/changelog/2014-12-22)
- [Cards now use both the unchecked and unavailable values to describe address
and CVC checks by issuing
banksPayments](https://docs.stripe.com/changelog/2014-12-22/cards-use-unchecked-unavailable-address-cvc-checks)
- [Tokens with cards no longer include the customer
fieldPayments](https://docs.stripe.com/changelog/2014-12-22/tokens-cards-no-longer-include-customer-field)
- [2014-12-17](https://docs.stripe.com/changelog/2014-12-17)
- [Introduces the statement_description field and logic for how charges,
invoices, plans, and transfers render statement descriptorsPayments+ 3
more](https://docs.stripe.com/changelog/2014-12-17/introduces-statement-description-field-logic)
- [Creating accounts using the API requires the 2014-12-17 version or
newerConnect](https://docs.stripe.com/changelog/2014-12-17/creating-accounts-requires-2014-12-17-version)
- [2014-12-08](https://docs.stripe.com/changelog/2014-12-08)
- [Disputes now include an evidence_details object for evidence
documentationPayments](https://docs.stripe.com/changelog/2014-12-08/disputes-include-evidence-details-object)
- [2014-11-20](https://docs.stripe.com/changelog/2014-11-20)
- [Disputes are now reported as won even if the charge is
refundedPayments](https://docs.stripe.com/changelog/2014-11-20/disputes-reported-won-refunded-charge)
- [Invoice items now reflect the metadata for their associated subscription,
rather than
planBilling](https://docs.stripe.com/changelog/2014-11-20/invoice-items-reflect-subscription-metadata)
- [2014-11-05](https://docs.stripe.com/changelog/2014-11-05)
- [Account activation status terms updated for payments and
transfersConnect](https://docs.stripe.com/changelog/2014-11-05/renames-charge-account-enabled-fields)
- [2014-10-07](https://docs.stripe.com/changelog/2014-10-07)
- [You can no longer retrieve tokens with publishable
keysElements](https://docs.stripe.com/changelog/2014-10-07/no-longer-retrieve-tokens-publishable-keys)
- [Creating a Card or Bank Account with a publishable key omits fingerprints in
API
responsesElements](https://docs.stripe.com/changelog/2014-10-07/create-card-bank-account-omit-fingerprints)
- [2014-09-08](https://docs.stripe.com/changelog/2014-09-08)
- [Bank Accounts now include a status enum that replace multiple
fieldsPayments](https://docs.stripe.com/changelog/2014-09-08/bank-accounts-include-status-enum)
- [2014-08-20](https://docs.stripe.com/changelog/2014-08-20)
- [Disputes now provide several new
statusesPayments](https://docs.stripe.com/changelog/2014-08-20/disputes-provide-several-new-statuses)
- [Disputes now include multiple balance
transactionsPayments](https://docs.stripe.com/changelog/2014-08-20/disputes-include-multiple-balance-transactions)
- [2014-08-04](https://docs.stripe.com/changelog/2014-08-04)
- [You can now retrieve balance histories rather than relying on Transfer
fieldsConnect](https://docs.stripe.com/changelog/2014-08-04/retrieve-balance-histories-transfer-fields)
- [2014-07-26](https://docs.stripe.com/changelog/2014-07-26)
- [Application fees now include a sublist of refunds through the refunds
fieldConnect](https://docs.stripe.com/changelog/2014-07-26/application-fees-include-refunds-sublist-refunds-field)
- [2014-07-22](https://docs.stripe.com/changelog/2014-07-22)
- [Invoice line items now include subscription plans and quantitiesInvoicing+ 1
more](https://docs.stripe.com/changelog/2014-07-22/invoice-line-items-include-subscription-plans-quantities)
- [2014-06-17](https://docs.stripe.com/changelog/2014-06-17)
- [Invoices now include a sublist of refunds through the refunds fieldInvoicing+
1
more](https://docs.stripe.com/changelog/2014-06-17/invoices-include-refunds-sublist-refunds-field)
- [2014-06-13](https://docs.stripe.com/changelog/2014-06-13)
- [Renames the type field on cards to brandPayments+ 1
more](https://docs.stripe.com/changelog/2014-06-13/renames-type-field-cards-brand)
- [2014-05-19](https://docs.stripe.com/changelog/2014-05-19)
- [Replaces the account field on transfersConnect+ 1
more](https://docs.stripe.com/changelog/2014-05-19/renames-account-field-transfers-bank-account)
- [2014-03-28](https://docs.stripe.com/changelog/2014-03-28)
- [Lists no longer include the count fieldAffects all
products](https://docs.stripe.com/changelog/2014-03-28/lists-no-longer-include-count-field)
- [2014-03-13](https://docs.stripe.com/changelog/2014-03-13)
- [Renames the statement descriptor
fieldConnect](https://docs.stripe.com/changelog/2014-03-13/renames-statement-descriptor-field-transfers)
- [2014-01-31](https://docs.stripe.com/changelog/2014-01-31)
- [Customers now support multiple
subscriptionsBilling](https://docs.stripe.com/changelog/2014-01-31/customers-support-multiple-subscriptions)
- [Trial end dates are no longer computed for canceled
subscriptionsBilling](https://docs.stripe.com/changelog/2014-01-31/trial-end-dates-canceled-subscriptions)
- [2013-12-03](https://docs.stripe.com/changelog/2013-12-03)
- [Application fees now provide an expandable account field to obtain user
detailsConnect](https://docs.stripe.com/changelog/2013-12-03/application-fees-provide-expandable-account-field)
- [Application fee refunds are now proportional to the charged
amountConnect](https://docs.stripe.com/changelog/2013-12-03/application-fee-refunds-proportional-charged-amount)
- [2013-10-29](https://docs.stripe.com/changelog/2013-10-29)
- [Coupons only apply to an invoice’s total balance, no longer applying to
zero-cost invoicesInvoicing+ 1
more](https://docs.stripe.com/changelog/2013-10-29/coupons-apply-invoice-total-balance)
- [2013-08-13](https://docs.stripe.com/changelog/2013-08-13)
- [Fee details have moved from charges to their corresponding balance
transactionsPayments](https://docs.stripe.com/changelog/2013-08-13/fee-details-moved-balance-transactions)
- [Fee details have moved from transfers to their corresponding balance
transactionsPayments](https://docs.stripe.com/changelog/2013-08-13/fee-details-moved-balance-transactions-transfers)
- [2013-08-12](https://docs.stripe.com/changelog/2013-08-12)
- [Lets the description and email fields be null on several objectsPayments+ 2
more](https://docs.stripe.com/changelog/2013-08-12/allows-description-email-fields-null)
- [2013-07-05](https://docs.stripe.com/changelog/2013-07-05)
- [Customers now include a cards sublist and default_card fieldPayments+ 2
more](https://docs.stripe.com/changelog/2013-07-05/customers-include-cards-sublist-default-card-field)
- [2013-02-13](https://docs.stripe.com/changelog/2013-02-13)
- [Disputes on charges are now tracked through the stripe_fee field and included
in the fee
totalPayments](https://docs.stripe.com/changelog/2013-02-13/disputes-tracked-stripe-fee-field-fee-total)
- [2013-02-11](https://docs.stripe.com/changelog/2013-02-11)
- [Failed invoice payments now return an HTTP errorInvoicing+ 1
more](https://docs.stripe.com/changelog/2013-02-11/failed-invoice-payments-return-http-error)
- [2012-11-07](https://docs.stripe.com/changelog/2012-11-07)
- [Renames the disputed field for Charges to
disputePayments](https://docs.stripe.com/changelog/2012-11-07/renames-disputed-field-charges-dispute)
- [2012-10-26](https://docs.stripe.com/changelog/2012-10-26)
- [Invoices now include a sublist of invoice line itemsBilling+ 1
more](https://docs.stripe.com/changelog/2012-10-26/invoices-include-invoice-line-items-sublist)
- [2012-09-24](https://docs.stripe.com/changelog/2012-09-24)
- [Discounts no longer include an extraneous id fieldBilling+ 1
more](https://docs.stripe.com/changelog/2012-09-24/discounts-no-longer-extraneous-id-field)
- [2012-07-09](https://docs.stripe.com/changelog/2012-07-09)
- [Customers no longer include the uncaptured
fieldPayments](https://docs.stripe.com/changelog/2012-07-09/customers-no-longer-uncaptured-field)
- [2012-06-18](https://docs.stripe.com/changelog/2012-06-18)
- [Tokens no longer include the amount and currency propertiesElements+ 1
more](https://docs.stripe.com/changelog/2012-06-18/tokens-no-longer-amount-currency-fields)
- [2012-03-25](https://docs.stripe.com/changelog/2012-03-25)
- [Customers no longer include a next_recurring_charge
fieldBilling](https://docs.stripe.com/changelog/2012-03-25/customers-no-longer-next-recurring-charge-field)
- [2012-02-23](https://docs.stripe.com/changelog/2012-02-23)
- [Fields with null values are now included in API responsesAffects all
products](https://docs.stripe.com/changelog/2012-02-23/fields-null-values-included-api-responses)
- [2011-09-15](https://docs.stripe.com/changelog/2011-09-15)
- [Cards validate differently when creating tokensElements+ 1
more](https://docs.stripe.com/changelog/2011-09-15/cards-validate-differently-creating-tokens)
- [2011-08-01](https://docs.stripe.com/changelog/2011-08-01)
- [Lists now provide a total count of items and a data fieldAffects all
products](https://docs.stripe.com/changelog/2011-08-01/lists-provide-total-count-data-field)
- [2011-06-28](https://docs.stripe.com/changelog/2011-06-28)
- [Plans no longer include the identifier
fieldBilling](https://docs.stripe.com/changelog/2011-06-28/plans-no-longer-identifier-field)
- [2011-06-21](https://docs.stripe.com/changelog/2011-06-21)
- [Errors now produce exceptions for unrecognized API parametersAffects all
products](https://docs.stripe.com/changelog/2011-06-21/exceptions-unrecognized-api-parameters)