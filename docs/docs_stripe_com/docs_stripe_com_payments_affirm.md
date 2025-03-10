# Affirm payments

## Offer your US and Canadian customers flexible financing while getting paid upfront with Affirm

[Affirm](https://www.affirm.com/) is a popular payment method in the US and
Canada that gives your customers a way to split purchases over a series of
payments. Pay in 4 interest-free installments or in monthly installments of up
to 36 months.

To pay with Affirm, customers are redirected to Affirm’s site, where they
[authorize](https://docs.stripe.com/payments/payment-methods#customer-actions)
the payment by agreeing to the terms of a payment plan, then return to your
website to complete the order. Affirm offers payment options based on factors
such as customer credit, prior account history, order amount, and the type of
goods or services being underwritten. After payment acceptance, the full amount
of the order (minus fees) is made available to your Stripe account upfront, and
Affirm collects the purchase amount from your customer, who repays Affirm
directly over time.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

United States, Canada
- **Presentment currency**

USD or CAD
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Buy now, pay later
- **Recurring payments**

No
- **Payout timing**

Standard
- **Connect support**

Yes
- **Dispute support**

[Yes, by email from
Stripe](https://docs.stripe.com/payments/affirm#disputes-and-fraud)
- **Manual capture support**

Yes
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/affirm#refunds)

#### Note

Affirm only supports domestic transactions, meaning you can only sell to
customers in the same country as your business. If you’re using [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods),
Stripe handles a customer’s payment method eligibility automatically. If you use
[payment_method_types](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_types),
you must either configure your integration so that it only presents Affirm to
eligible customers, or use dynamic payment methods.

## Payment flow

Below is a demonstration of the Affirm payment flow from your checkout page:

## Get started

You don’t have to integrate Affirm and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Affirm. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

[Payment Links](https://docs.stripe.com/payment-links) also supports adding
Affirm from the Dashboard.

If you prefer to manually list payment methods, learn how to [manually configure
Affirm as a payment](https://docs.stripe.com/payments/affirm/accept-a-payment).

You can also let customers know Affirm payments are available by including the
[Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging) on your
product, cart, and payment pages. We recommend adding a site messaging Element
to help drive conversion.

## Payment options

Depending on the cart order size, Affirm presents customers with Pay in 4,
monthly installments, or both.

- **Pay in 4**: customers pay for purchases in four or fewer interest-free,
bi-weekly payments over an 8 week term. Available for cart sizes between $50 and
$250*.
- **Monthly Installments**: customers pay for purchases over a longer term of up
to 36 months, which might include interest. Available for cart sizes between 100
USD and 30,000 USD*.

* Term lengths and cart ranges are determined by Affirm and might change at
their discretion.

## Prohibited and restricted business categories

In addition to the categories of [businesses restricted from using Stripe
overall](https://stripe.com/restricted-businesses), the following categories are
prohibited from using Affirm.

- Business to business services
- Home improvement services, including contractors and special trade contractors
- Titled goods and auto loans, including entire cars, boats, and other motor
vehicles (parts and services allowed)
- Professional services (including legal, consulting, and accounting)
- NFTs
- Pre-orders

Healthcare services are approved to use Affirm, however they’re subject to
additional requirements. For the complete list of prohibited businesses and
additional requirements, see [the Affirm Payment
Terms](https://stripe.com/legal/affirm).

## Add Affirm branding to your website

Use the [Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging) on your site
to let customers know that you offer Affirm ahead of checkout. You must comply
with Affirm’s [marketing compliance
guides](https://docs.affirm.com/developers/docs/compliance_and_guidelines) and
use the Affirm
[guide](https://businesshub.affirm.com/hc/en-us/articles/10653174159636-Affirm-Marketing-Compliance-Guides)
that relates to the Affirm payment options you offer your customers.

## Refunds

Returns are subject to the return policy that you display on your website. If
your business allows returns, you can [refund](https://docs.stripe.com/refunds)
Affirm transactions as you normally would for card payments. Affirm supports
partial or full refunds for up to 120 days after the original purchase, and
processes them asynchronously. After Stripe initiates a refund, Affirm pauses
the customer’s payment plan and refunds the customer for any payments they’ve
already made, minus any interest paid. Stripe doesn’t credit back the processing
fees in the event of a refund.

## Disputes

Customers must authenticate Affirm payments by logging into their Affirm
account. This requirement helps reduce the risk of fraud or unrecognized
payments. While Affirm covers losses incurred from customer fraud, Stripe might
contact you on behalf of Affirm and request to stop or pause shipment before any
losses are incurred. Comply promptly with these requests.

Customers can dispute Affirm payments in certain cases—for example, if they
receive faulty goods or don’t receive them at all. Customers can file a dispute
after the date of purchase and there isn’t a time limitation for filing. The
dispute process works like this:

After the customer initiates a dispute, Stripe notifies you using:

- Email notification
- Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to
receive [webhooks](https://docs.stripe.com/webhooks))

Stripe holds back the disputed amount from your balance until Affirm resolves
the dispute, which can take a maximum of 30 calendar days from dispute creation.

Stripe requests that you upload compelling evidence that you fulfilled the
purchase order [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond). This evidence
can include:

- Received return confirmation (for shipped goods returned from the customer to
you)
- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or
proof of receipt

If you prefer to handle disputes programmatically, you can [respond to disputes
using the API](https://docs.stripe.com/disputes/api).

This information helps Affirm determine if a dispute is valid or if they should
reject it. Make sure the evidence you provide contains as much detail as
possible from what the customer provided at checkout. You must submit the
requested information within 15 calendar days. Affirm makes a decision within 15
calendar days of evidence submission. If Affirm resolves the dispute with you
winning, Stripe returns the disputed amount to your Stripe balance. If Affirm
rules in favor of the customer, the balance charge becomes permanent.

## Customer emails

After a customer uses Affirm to make a purchase, Affirm emails the customer with
updates. These updates include information about the following events:

- Affirm confirms or denies a loan. Affirms sends these updates when the
payment_intent succeeds or when Affirm denies the loan.
- A [refund](https://docs.stripe.com/refunds) completes.
- A payment is cancelled, which results in Affirm cancellling the loan.
- The customer completes a payment as part of the payment plan.

Affirm only sends email updates about Affirm’s loan issuance to your customer.
Continue to separately send emails related to the purchase such as order
confirmation and shipping updates.

## Connect

You can use [Stripe Connect](https://docs.stripe.com/connect) with Affirm to
process payments on behalf of a connected account.
[Connect](https://docs.stripe.com/connect) users can use Affirm with the
following charge types:

- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate Charges and
Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)

### Request Affirm capability

Make sure you
[request](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting)
the `affirm_payments` capability and it’s set to `active` on both your platform
account and any connected accounts you want to enable.

### Set correct MCC

Stripe and Affirm rely on merchant category codes (MCC) to determine eligibility
of the connected accounts against the Affirm [prohibited business
categories](https://docs.stripe.com/payments/affirm#prohibited-and-restricted-business-categories).
Make sure that you set [correct
MCCs](https://docs.stripe.com/connect/setting-mcc) for your connected accounts
that use the Express Dashboard or a dashboard that isn’t hosted by Stripe.

### Merchant of record

The [charge type](https://docs.stripe.com/connect/charges) of Connect payments
might change the merchant name that appears on Affirm’s website or app during
the redirect. The merchant of record determines the Stripe account authorized to
create payments with a particular
[PaymentMethod](https://docs.stripe.com/api/payment_methods/object).

## Links

- [Affirm](https://www.affirm.com/)
- [pricing details](https://stripe.com/pricing/local-payment-methods)
- [authorize](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Yes, by email from
Stripe](https://docs.stripe.com/payments/affirm#disputes-and-fraud)
- [Yes / Yes](https://docs.stripe.com/payments/affirm#refunds)
- [Dynamic payment
methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods)
-
[payment_method_types](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_types)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure Affirm as a
payment](https://docs.stripe.com/payments/affirm/accept-a-payment)
- [Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging)
- [businesses restricted from using Stripe
overall](https://stripe.com/restricted-businesses)
- [the Affirm Payment Terms](https://stripe.com/legal/affirm)
- [marketing compliance
guides](https://docs.affirm.com/developers/docs/compliance_and_guidelines)
-
[guide](https://businesshub.affirm.com/hc/en-us/articles/10653174159636-Affirm-Marketing-Compliance-Guides)
- [refund](https://docs.stripe.com/refunds)
- [webhooks](https://docs.stripe.com/webhooks)
- [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond)
- [respond to disputes using the API](https://docs.stripe.com/disputes/api)
- [Stripe Connect](https://docs.stripe.com/connect)
- [Direct](https://docs.stripe.com/connect/direct-charges)
- [Destination](https://docs.stripe.com/connect/destination-charges)
- [Separate Charges and
Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
-
[request](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting)
- [prohibited business
categories](https://docs.stripe.com/payments/affirm#prohibited-and-restricted-business-categories)
- [correct MCCs](https://docs.stripe.com/connect/setting-mcc)
- [charge type](https://docs.stripe.com/connect/charges)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods/object)