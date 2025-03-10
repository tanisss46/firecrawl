# Get started on dispute prevention with VerifiPublic preview

## Learn about the benefits and requirements of Stripe's dispute prevention offering powered by Verifi.

## Understanding Verifi

Stripe has built integrations with dispute prevention products offered by
Verifi, a subsidiary of Visa. The products include Order Insight (OI) and Rapid
Dispute Resolution (RDR). Our integrations allow you to use both products
without any manual integrations to help reduce your dispute rate and increase
revenue retention. Learn more about pricing on the [product overview
page](https://docs.stripe.com/disputes/verifi-beta#pricing). Because the
offering is currently in beta, the pricing and product behavior might be subject
to change.

## Rapid Dispute Resolution (RDR)

RDR allows businesses to construct a ruleset to auto-refund incoming disputes on
Visa transactions for a fee per dispute (for example, refund all potential fraud
disputes under 10 USD). Businesses pay the additional RDR fee for each incoming
dispute reviewed by RDR regardless of whether the dispute is avoided with the
auto-refund ruleset. The main benefit of RDR is that refunded disputes don’t
count towards dispute rates, helping you stay out of monitoring programs, and
you don’t pay a separate dispute fee on refunded disputes. This is helpful for
businesses in the Visa Dispute Monitoring Program (VDMP) because it allows you
to immediately reduce your dispute rates and lower dispute fees, while also
avoiding network fines and Stripe payment volume reserves.

### RDR requirements

Although there are no requirements for using RDR and no separate integration on
your end, the onboarding process requires you to set up rules to define which
transactions to refund with RDR. After you [request access to the
beta](https://docs.stripe.com/disputes/verifi-beta#request-an-invite), Stripe
will be in touch with next steps to set up your ruleset. Learn more about how to
best [set up
rules](https://support.stripe.com/questions/how-to-creating-rule-sets-for-rdr-powered-by-verifi).

## Order Insight (OI)

If a consumer checks their digital banking app or calls their issuer to say they
don’t recognize a Visa charge and you’re enrolled in OI, the issuer’s customer
support agent can send a real-time lookup (API request to Stripe) to provide
detailed descriptions of the item the consumer purchased (such as product
descriptions, quantity, shipping address, or IP address). The additional data
helps the consumer recognize the charge and prevent follow-through on disputes.
OI also uses new Visa rules such as Compelling Evidence 3.0 (CE 3.0), where if
you can send issuers data about prior successful transactions with the same
cardholder as a response to a lookup, the issuer is required to block the
cardholder from filing the dispute at all. See [Compelling Evidence 3.0 with
OI](https://docs.stripe.com/disputes/get-started/verifi##compelling-evidence-3.0-with-oi)
for more information.

Cardholders are less likely to follow through on filing a dispute if they can
recognize the charge. The chances of successfully deflecting a dispute when a
lookup is made depend on the quality of the data that Stripe can provide. Stripe
automatically pulls any available data on a charge on your behalf and sends it
to the issuer. Stripe uses the data that you provide during charge time and
doesn’t require you to build any integrations or maintain a real-time service.
See the list of fields below that are eligible as part of the lookup response.
By using the OI service, you direct Stripe to share this data with issuers and
ultimately with cardholders. Verifi might occasionally update these fields, and
your continued use of the OI service depends on your adapting to any new
operational requirements.

#### Note

For a dispute to be eligible for a block using CE 3.0 rules, Stripe must have
prior transaction data available. See [Compelling Evidence 3.0 with
OI](https://docs.stripe.com/disputes/get-started/verifi#compelling-evidence-3.0-with-oi)
for which data is required for CE 3.0 blocks. If prior transaction data isn’t
available, Stripe still sends any other available data.

ObjectFieldDescriptionReceipt orderDateOrder dateorderNumberUnique identifier
for the order defined by the businessinvoiceNumberInvoice number (alternate to
order number)subTotalAmountSubtotal amount of the purchase before tax and
shipping fees are includedshippingAndHandlingAmountShipping and Handling amount
related to the purchaseorderTotalAmountTotal amount of the orderPayment
information paymentMethodMasked representation of the card and card number of
the original purchase as displayed on the physical or digital receipt. Limited
to the last 4 digits of the card PAN.billingNameFirst and last name from the
cardpaymentTotalAmountPayment amount of the purchasecvvCheckedCard security code
validation at time of purchaseProduct purchased productDescriptionDetailed
description of the product (merchandise or service)
purchasedunitPriceAmountAmount of the individual itemquantityQuantity of the
product purchasedCustomer information firstNameCustomer’s first
namelastNameCustomer’s last namelengthOfRelationshipLength of customer
relationship with the business in number of monthsaccountIdCardholder registered
identifier to uniquely identify their account with the business. This should be
recognizable to the Cardholder (not an internal system identifier) and something
they provided the business during account creation. Examples are a unique
username, email, phone number, or other similar value.emailAddressEmail address
that customer providedBilling address address1Street address plus additional
address lines such as suite number and apartmentaddress2Street address plus
additional address lines such as suite number and apartmentcityName of
cityregionRegion or statepostalCodeZip or postal codecountryCountry codeMerchant
information merchantNameCorporate or parent company name of the business, This
might or might not be recognizable to the consumer.merchantUrlBusiness’s
corporate URL. Might be different than the websiteUrl where the customer made
the purchase from.merchantContactPhoneBusiness’s customer service phone number.
This should be the number that you would want a consumer to contact you to
discuss any questions they have about the purchase.merchantAddressBusiness’s
corporate addresstermsAndConditionsOverview of cancellation policies for
businessesstoreDetailsA business might have multiple stores or locations that
purchases are made from. The store details should indicate where the purchase
was processed or the online webstore details.Store details storeNameStore or
webstore name where the purchase was madestoreContactPhoneBusiness’s customer
service phone numberDelivery address address1Street address plus additional
address lines such as suite number and apartmentaddress2Street address plus
additional address lines such as suite number and apartmentcityName of
cityregionRegion or statepostalCodeZip or postal codecountryCountry ISO 3166-1
code alpha-3Delivery details shippingCarrierShipping
carriertrackingNumberTracking number of the shipment or
deliveryDeviceipAddressIP Address associated with the device
### Compelling Evidence 3.0 with OI

Compelling Evidence 3.0 (CE 3.0) is a program aimed to benefit businesses by
providing more aggressive tools to deflect and remedy first-party misuse (aka
“friendly fraud”) disputes on Visa transactions. CE 3.0 rules dictate which
evidence can be provided post-dispute to improve your odds of winning a dispute
([learn
more](https://support.stripe.com/questions/how-does-stripe-support-visa-compelling-evidence-3-0)).
However, if you’re enrolled in OI, you can also use CE 3.0 pre-dispute to
completely block the dispute from being filed. This works by providing the
required prior transaction data to issuers during a lookup. If prior
transactions between you and the cardholder exist, Visa automatically selects
the 2-5 of most recent non-fraud prior transactions and requests data on all of
the transactions. Stripe then automatically provides all of the above available
information. If at least 2 prior transactions exist with complete product
descriptions that have matching IP addresses and at least one of matching email
address or customer delivery address, the issuer is required to block the
dispute. As a result, the dispute is never filed and you don’t incur any dispute
fees or any increases to your dispute rate.

### OI Requirements

The onboarding flow in the Stripe Dashboard collects all the data elements that
Stripe needs to begin servicing OI lookups on your behalf. These include
Business name, Business URL, Business Phone Number, and Email. To achieve the
best possibility for deflected disputes, make sure your Stripe integration is
set up to provide as many of the above fields as possible at transaction time.
To ensure that Stripe can effectively block disputes on your behalf with CE 3.0,
make sure that all your transactions include IP Address, Customer Email Address,
Product Descriptions, and if possible, Shipping or Customer Address.

## Links

- [product overview page](https://docs.stripe.com/disputes/verifi-beta#pricing)
- [request access to the
beta](https://docs.stripe.com/disputes/verifi-beta#request-an-invite)
- [set up
rules](https://support.stripe.com/questions/how-to-creating-rule-sets-for-rdr-powered-by-verifi)
- [learn
more](https://support.stripe.com/questions/how-does-stripe-support-visa-compelling-evidence-3-0)