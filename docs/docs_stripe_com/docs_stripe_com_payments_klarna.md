# Klarna payments

## Offer flexible payment options and get paid up front with Klarna.

Klarna is a global payment method that gives customers a range of payment
options during checkout. These payment options enable customers to pay for
purchases over time.

To pay with Klarna, customers are redirected to Klarna’s site, where they select
their preferred payment option, then return to your website to complete the
order. Klarna presents payment options based on the customer’s billing address
and transaction amount. After payment acceptance, the full amount of the order
(minus fees) is made available to your Stripe account up front, and Klarna
collects the purchase amount from your customer, including any future
installment payments, if applicable.

If you’re based in the UK, Switzerland or a supported
[EEA](https://en.wikipedia.org/wiki/European_Economic_Area) country, you can
transact with consumers in the UK, Switzerland, and all EEA countries where
Klarna has a consumer offering, provided if the presentment currency matches the
currency of the customer’s country. For example, a Swedish business can present
in EUR to accept Klarna from a buyer in Germany.

If you’re based outside of the EEA, UK, or Switzerland, you can only transact
with customers within your country, and the presentment currency must be the
currency of your country. For example, an Australian business must present in
AUD, and can only transact with buyers in Australia.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Australia, Austria, Belgium, Canada, Czechia, Denmark, Finland, France, Greece,
Germany, Ireland, Italy, Netherlands, New Zealand, Norway, Poland, Portugal,
Romania, Spain, Sweden, Switzerland, United Kingdom, and the United States
- **Presentment currency**

AUD, CAD, CHF, CZK, DKK, EUR, GBP, NOK, NZD, PLN, RON, SEK, or USD
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Buy now, pay later
- **Recurring payments**

Private PreviewSign up
- **Payout timing**

Standard payout timing applies
- **Connect support**

[Yes](https://docs.stripe.com/payments/klarna#connect)
- **Dispute support**

[Yes](https://docs.stripe.com/payments/klarna#disputed-payments)
- **Manual capture support**

Yes
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/klarna#refunds)

## Payment flow

Below is a demonstration of the Klarna payment flow from your checkout page:

## Get started

You don’t have to integrate Klarna and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Klarna. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

#### Unified line items with Klarna

To maximize approval rates when you integrate with Klarna, we recommend that you
include Line Items data to represent what’s in a shopper’s cart. Reach out here
to request access.

#### Klarna on the Express Checkout Element

Klarna on the Express Checkout Element is currently in private preview with
limited availability. Reach out here to request access.

You can also [manually
list](https://docs.stripe.com/payments/klarna/accept-a-payment) Klarna as a
payment method and use it with [Payment
Links](https://docs.stripe.com/payment-links) or the [Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging).

## Payment options

Depending on the customer’s billing country and the transaction amount, Klarna
can present customers with various payment options. Cart ranges and geographic
availability for payment options are determined by Klarna and might change at
their discretion. Regardless of the underlying payment option selected, Stripe
makes the full amount of the funds (minus fees) available to you upfront and
Klarna collects the purchase amount from your customer, who repays Klarna
directly. These options include:

- **Pay now**: Customers pay for the purchase immediately using a linked card,
bank debit, or bank transfer.
- **Pay later**: Customers pay for the purchase in a single payment in 30 days.
- **Pay in 3 or 4** (also known as installments): Customers pay for the purchase
in three or four interest-free payments. The total transaction amount is
typically spread equally across the installments, but Klarna might occasionally
charge your customer more in the first installment based on the customer’s
purchase power and other credit factors.
- **Financing** (also known as monthly installments): Customers pay for the
purchase over a longer term of up to 36 months, which might include interest.
Not all customers are approved for the maximum amount, and approval is subject
to credit worthiness.

The following tables list the supported payment options for the countries in
each region. If a payment option isn’t listed for a country, it isn’t currently
supported.

North AmericaDACH and Northern EuropeNordicsRest of EuropeAPAC
### Canada

### United States

## Prohibited business categories

In addition to the industry and business categories listed in [Prohibited and
restricted business](https://stripe.com/restricted-businesses), the following
categories aren’t allowed to use Klarna:

- Charities
- Political organizations, parties, or initiatives
- B2B

For more information about Klarna eligibility for your account, navigate to your
[Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods).

## Klarna branding

Let your customers know you accept payments with Klarna by including the
[Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging) on your
product and cart pages. You must comply with Klarna’s [marketing compliance
guides](https://docs.klarna.com/marketing/solutions/grab-and-go).

If you’re in the UK, there are [FCA](https://www.fca.org.uk/) regulatory
requirements in the UK regarding advertising Klarna’s BNPL payment methods.
Failure to comply can result in criminal charges. Per these requirements, you
must only advertise Klarna with messaging approved by Klarna. You can find
Klarna approved messaging in Klarna’s [UK Financial Promotion
Rules](https://docs.klarna.com/marketing/solutions/grab-and-go/gb/Klarna-Financial-Promotion-Rules/).

## Disputes

Klarna covers disputes driven by customer fraud or inability to repay
installments provided you follow [Klarna’s shipping
policy](https://www.klarna.com/international/shipping-policies/). Merchants
aren’t involved in these disputes.

When a dispute arises, communicate directly with your customer to try and solve
the issue together. If you can’t reach a solution, Klarna intervenes to help
solve the dispute. You can manage disputes in the Stripe Dashboard and using the
API.

Normally, customers can open a dispute within 180 days of the original
transaction. However, the 180-day limit doesn’t apply to the following
situations:

- The customer reports that they never authorized the transaction
- The customer raises a legal claim with an external authority, such as the
Central Arbitration Committee
- Local consumer protection rules extend the limit, for example, the right to
object in Sweden
- The customer is contesting the transfer of the debt to an external collection
agency

### Dashboard or API disputes

Prior to November 15, 2023, you could only manage Klarna disputes through
emails. Now, all new Klarna disputes are managed in the Stripe Dashboard and
with APIs. As you transition from managing disputes through email to handling
them in the Dashboard or with the API, you must continue to respond to existing
email disputes by email.

To learn how to use the Dashboard or API to manage disputes, see [Respond to
disputes](https://docs.stripe.com/payments/klarna/disputes).

### Email disputes

Klarna reaches out to both you and the customer, requesting convincing evidence
that you fulfilled the purchase order. Klarna emails the support email address
that you list in your [Dashboard
settings](https://dashboard.stripe.com/settings/public) when you activate
Klarna. If you haven’t provided a support email address, Klarna defaults to your
primary Stripe account email address. [Contact
us](https://support.stripe.com/contact) to modify the email address Klarna uses.

Klarna might request evidence such as:

- Received return confirmation (for shipped goods returned from the customer to
you).
- Tracking ID.
- Shipping date.
- Record of purchase for intangible goods, such as IP address or email receipt.
- Record of purchase for services or physical goods, such as phone number or
proof of receipt.

This information helps Klarna determine if a dispute is valid or if they’ll
reject it. Make sure the evidence you provide contains as much detail as
possible from what the customer provided at checkout. You must submit the
requested information within 7 days. If Klarna rules in favor of the customer,
they might initiate a dispute, with funds withdrawn from your Stripe account.
Klarna dispute decisions are final, and they have no appeal process.

## Refunds

You can refund Klarna charges up to 180 days after the payment completes. Klarna
cancels any remaining payments on a refunded charge and returns the already-paid
amount to the customer. Refunds usually take 5-7 business days to complete, but
might take longer depending on the customer’s financial institution and the type
of purchase. Klarna supports full and partial refunds. You can also issue
multiple partial refunds up to the amount of the original charge. Partial
refunds update the Klarna order to reflect the new total amount.

- If the partial refund is greater than the remaining balance of the order,
Klarna deducts the refund amount from the outstanding balance and returns the
difference.
- If the partial refund is less than the remaining balance of the order, Klarna
deducts the amount from the outstanding balance and spreads refunds evenly
across the remaining payments.

## Connect

A Connect platform can use [Stripe
Connect](https://docs.stripe.com/connect/how-connect-works) with Klarna to
process connected account payments of all [charge
types](https://docs.stripe.com/connect/charges).

### Connected accounts with full Stripe Dashboard access

Connected accounts with access to the full Stripe Dashboard, including Standard
accounts, can enable Klarna through their Dashboard. To check which accounts
have enabled Klarna, use the `capabilities` hash in the [accounts webhooks or
APIs](https://docs.stripe.com/api/accounts/object#account_object-capabilities-klarna_payments)
to see if the `klarna_payments` capability is set to `active`.

### Connected accounts without full Stripe Dashboard access

To enable Klarna for connected accounts without full access to the Stripe
Dashboard, including Express and Custom accounts, request the `klarna_payments`
[capability](https://docs.stripe.com/connect/account-capabilities). Customers
see the name of your connected account during checkout and in the Klarna app.

## Termination rights

In addition to the termination and suspension rights included in the [Stripe
Services Agreement](https://stripe.com/klarna/legal), Klarna has certain
additional rights to suspend or terminate your use of Klarna, such as for breach
of the prohibited business categories listed above or for high dispute rates
that aren’t promptly remedied.

## Additional requirements

You acknowledge that:

- Klarna decides if customers can use Klarna for purchases and has the sole
right to receive payment from Klarna customers. Stripe acquires those purchases
for you and settles the funds to you.
- You must provide customers with any required or requested payment instructions
or documents (such as VAT). These documents must refer to Klarna as the payee
and not contain any of your bank details.
- You can’t impose fees or higher prices for Klarna purchases or act unfairly
towards Klarna.
- You must promptly follow Stripe’s instructions to stop an order process or
shipping to help reduce the risk of fraudulent transactions.
- You can’t use any design that’s confusingly similar to Klarna’s trademarks
(see [Klarna’s branding guidelines](https://docs.klarna.com/marketing/)).
- You must not permit use of Klarna for purchases by a person who might
reasonably be considered to share a financial interest with you, including
owners, directors, and employees of your business or any affiliated company.

If you’re in Australia, Klarna provides guidance on how to comply with the
[Design and Distribution Obligations
(DDO)](https://docs.klarna.com/marketing/au/advertising-legal-guidelines/design-and-distribution-obligations-ddo/)
when accepting Klarna in Australia. Most Stripe users don’t need to do anything
to comply. If you actively promote or recommend Klarna’s Pay in 4 product in
Australia, you may be considered a “distributor” under the DDO and may have to:

- Help Klarna as needed to comply with the DDO, including only promoting Pay in
4 consistent with Klarna’s [Target Market Determination
(TMD)](https://www.klarna.com/au/legal/target-market-determinations/)
- Promptly advise Klarna of any “significant adverse dealing” such as:- A major
complaint or large number of complaints that Pay in 4 causes a customer harm or
- A customer under 18 makes a purchase using Pay in 4
- If requested, provide Klarna with reports about any Pay in 4 complaints you
receive
- If requested, provide Klarna with information related to any reported
significant adverse dealings

## Links

- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [EEA](https://en.wikipedia.org/wiki/European_Economic_Area)
- [Yes](https://docs.stripe.com/payments/klarna#connect)
- [Yes](https://docs.stripe.com/payments/klarna#disputed-payments)
- [Yes / Yes](https://docs.stripe.com/payments/klarna#refunds)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [manually list](https://docs.stripe.com/payments/klarna/accept-a-payment)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging)
- [Prohibited and restricted business](https://stripe.com/restricted-businesses)
- [marketing compliance
guides](https://docs.klarna.com/marketing/solutions/grab-and-go)
- [FCA](https://www.fca.org.uk/)
- [UK Financial Promotion
Rules](https://docs.klarna.com/marketing/solutions/grab-and-go/gb/Klarna-Financial-Promotion-Rules/)
- [Klarna’s shipping
policy](https://www.klarna.com/international/shipping-policies/)
- [Respond to disputes](https://docs.stripe.com/payments/klarna/disputes)
- [Dashboard settings](https://dashboard.stripe.com/settings/public)
- [Contact us](https://support.stripe.com/contact)
- [Stripe Connect](https://docs.stripe.com/connect/how-connect-works)
- [charge types](https://docs.stripe.com/connect/charges)
- [accounts webhooks or
APIs](https://docs.stripe.com/api/accounts/object#account_object-capabilities-klarna_payments)
- [capability](https://docs.stripe.com/connect/account-capabilities)
- [Stripe Services Agreement](https://stripe.com/klarna/legal)
- [Klarna’s branding guidelines](https://docs.klarna.com/marketing/)
- [Design and Distribution Obligations
(DDO)](https://docs.klarna.com/marketing/au/advertising-legal-guidelines/design-and-distribution-obligations-ddo/)
- [Target Market Determination
(TMD)](https://www.klarna.com/au/legal/target-market-determinations/)