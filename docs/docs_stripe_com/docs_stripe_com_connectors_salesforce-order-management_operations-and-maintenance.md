# About the Stripe Connector for Salesforce Order Management

## Learn about the core concepts of the connector.

## Payment Intents

A [Payment Intent](https://docs.stripe.com/payments/payment-intents) is a Stripe
object you can use to track a payment through its entire lifecycle, including
any required authentication steps. To find the `PaymentIntent` in Salesforce
Order Management, locate the Gateway Reference Number (`GatewayRefNumber`) field
against the payment authorization record for an order summary.

## Payment authorization

A payment authorization is relevant to both Stripe and the Salesforce OMS. An
authorized amount is a sum that a business transmits to a credit or debit card
processor to make sure a customer has sufficient funds to complete a
purchase—the approved amount of money to be charged.

There are two [capture
modes](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
in the Stripe LINK cartridge for Salesforce B2C Commerce Cloud—authorize and
capture. If the LINK cartridge is setup to authorize a payment during checkout,
then a payment authorization record is created in Salesforce Order Management.
You can view the payment authorization against an order summary using this
route:

**Order Summary Record > Order Payment Summary Record > Payment Authorizations
in Related Tab**

If you don’t see `Refunds` in the **Related** tab, contact your Salesforce
administrator and include the payment authorization related list in the page
layout (as shown):

!

The PaymentIntent ID (`pi_XXXXXX`) at Stripe is stored in the Gateway Reference
Number (`GatewayRefNumber`) field of the payment authorization record. The
Processing Mode (`ProcessingMode`) is set as `External`, which implies that the
payment authorization was processed outside the Salesforce payment platform.

## Payment

If the capture mode in the Stripe LINK cartridge is set to `Capture`, then the
payment is captured from the customer. In this case, a payment record is created
in Salesforce Order Management. You can view the payment against an Order
Summary using this route:

**Order Summary Record > Order Payment Summary Record > Payments in Related
Tab**

If you don’t see `Refunds` in the **Related tab**, contact your Salesforce
administrator and include the payments related list in the page layout (as
shown):

!

## Balance Transaction ID

The Balance Transaction ID (`txn_XXXXXXXXX`) against the PaymentIntent
(`pi_XXXXXX`) at Stripe is stored in the Gateway Reference Number
(`GatewayRefNumber`) field. The Processing Mode (`ProcessingMode`) is set as
`External`, which means the payment was processed outside the Salesforce payment
platform. In the event the payment was authorized in Salesforce B2C Commerce
Cloud Storefront, and the amount was captured in Salesforce OMS later, the
payment record is represented as shown:

!

The Salesforce Payment Gateway Id (`SFXXXXX`) against the Payment Intent
(`pi_XXXXXX`) at Stripe is stored in the Gateway Reference Number
(`GatewayRefNumber`) field. The Processing Mode (`ProcessingMode`) is set as
`Salesforce`, which implies that the payment was processed by the Salesforce
payment platform.

## Refund

If a refund is initiated from Salesforce OMS, you can trace it to a refund
record by following this route:

**Order Summary Record > Order Payment Summary Record > Refunds (in the Related
tab)**

If you don’t see `Refunds` in the **Related** tab, contact your Salesforce
administrator and include the refunds related list in the page layout (as
shown):

!

The Salesforce Payment Gateway Id (`SFXXXXX`) is stored in the Gateway Reference
Number (`GatewayRefNumber`) field. The Processing Mode (`ProcessingMode`) is set
as `Salesforce`, which implies that the refund was processed by the Salesforce
payment platform.

## Payment gateway logs

You can view logs for the transactions made with the Salesforce Platform by
navigating to **Order Summary Record > Order Payment Summary Record > Gateway
Logs** in the **Related** tab. If you don’t see the gateway logs in the
**Related** tab, contact your Salesforce administrator and include the gateway
logs in the related the page layout, or execute this SOQL in Developer Console
or SOQL Builder in VS Code:

```
SELECT Id,OrderPaymentSummaryId, ReferencedEntityId,Request, Response,
SfRefNumber, SfResultCode, GatewayRefNumber, GatewayAuthCode, GatewayDate,
GatewayMessage, GatewayResultCode, GatewayResultCodeDescription,
InteractionStatus FROM PaymentGatewayLog
```

## Next steps

-
[Testing](https://docs.stripe.com/connectors/salesforce-order-management/testing)

## Links

- [Payment Intent](https://docs.stripe.com/payments/payment-intents)
- [capture
modes](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-capture_method)
-
[Testing](https://docs.stripe.com/connectors/salesforce-order-management/testing)