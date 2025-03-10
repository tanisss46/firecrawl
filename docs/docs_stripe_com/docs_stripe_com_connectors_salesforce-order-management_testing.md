# Testing the Stripe Connector for Salesforce Order Management

## Best practices for testing your Stripe Connector and Salesforce B2C Commerce integration.

Use the following steps to test your integration:

- In the Stripe Dashboard, toggle from live mode to test mode.
- Raise an order from Salesforce B2C Commerce Cloud.
- After the order is in the Salesforce Order Management environment, complete
the required steps based on your mapped business process in SFOMS to fulfill the
order or refund an order. Depending on your test case, this translates to
triggering either of the flow core actions for order management – [Ensure Funds
Async](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_om_actions_ensure_funds_async.htm&type=5)
or [Ensure Refunds
Async](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_om_actions_ensure_refunds_async.htm&type=5).
- Verify the status of your payment in the Stripe Dashboard, and check the
payment gateway logs against the order payment summary.
- If the outcome is as expected, toggle from test mode to live mode. Reauthorize
with Stripe, if required.
- If you are experiencing any issues, contact Stripe Support.

If your storefront is hosted on a Salesforce B2C environment, you should have an
`account.demandware.com` login and Business Manager access through the following
URL: https://production.demandware.net/on/demandware.store/Sites-Site.

## Verify that Salesforce Commerce Cloud cartridge can collect payments with Stripe or Salesforce payments on Commerce Cloud

Log in to your Business Manager:

!

Alternatively:

!

## Verify that your integration is enabled between SalesforceB2C Commerce Cloud and Salesforce Order Management

- In your Salesforce Order Management org, navigate to **Setup > Home > Feature
Settings > Order Management**

!
- Then use the following route: **Setup > Home > Feature Settings > Connect to
B2C Commerce > Manage Cloud-to-Cloud Connections**

!

## Verify access to the CommercePayments API enabled by the PaymentPlatform org permission

You can validate whether you have access using one of the following methods.

Confirm whether you’ve been assigned any of the following licenses:

- Salesforce Order Management
- Salesforce B2B
- Salesforce B2C

Using the following route in **Setup > Home > Company Information > Permission
Set Licenses**, check for Commerce User (`CommerceUserPsl`), Lightning Order
Management User (`LightningOrderManagementUserPsl`), B2B Buyer Permission Set
One Seat (`B2BBuyerPsl`), B2B Buyer Manager Permission Set One Seat
(`B2BBuyerManagerPsl`).

## Verify the org API version

Refer to this help document:
[https://help.salesforce.com/s/articleView?id=000334996&type=1](https://help.salesforce.com/s/articleView?id=000334996&type=1).

## Get logs of payments and refunds in Salesforce

You can view logs for transactions made through the Salesforce Platform by
navigating to **Order Summary Record > Order Payment Summary Record > Gateway
Logs** in the **Related** tab. If you don’t see the gateway logs in the
**Related** tab, contact your Salesforce administrator and include the gateway
logs in the page layout.

You can also execute this SOQL in developer console or SOQL Builder in VSCode
(Apply filters as required `OrderPaymentSummaryId` or `ReferencedEntityId`):

```
SELECT Id, OrderPaymentSummaryId, ReferencedEntityId,Request, Response,
SfRefNumber, SfResultCode, GatewayRefNumber, GatewayAuthCode, GatewayDate,
GatewayMessage, GatewayResultCode, GatewayResultCodeDescription,
InteractionStatus FROM PaymentGatewayLog
```

The `ReferencedEntityId` is a polymorphic field that points to a payment or
refund record.

## Links

- [Ensure Funds
Async](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_om_actions_ensure_funds_async.htm&type=5)
- [Ensure Refunds
Async](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_om_actions_ensure_refunds_async.htm&type=5)
-
[https://help.salesforce.com/s/articleView?id=000334996&type=1](https://help.salesforce.com/s/articleView?id=000334996&type=1)