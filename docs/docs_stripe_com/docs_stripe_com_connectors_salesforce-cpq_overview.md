# Stripe Billing Connector for Salesforce CPQ

## Enable your sales team to create and manage subscriptions on Stripe without leaving Salesforce.

The Stripe Billing Connector for Salesforce CPQ enables you to automatically:

- Create a [subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
on Stripe when your sales team activates a Salesforce CPQ order.
- Update a [subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
on Stripe when your sales team amends a Salesforce CPQ order.
- Send [invoices](https://docs.stripe.com/billing/invoices/subscription) to
customers for both recurring and one-time items when you configure subscriptions
on Stripe.
- Populate Salesforce CPQ orders with links in the [Stripe
Dashboard](https://docs.stripe.com/dashboard/basics) for reviewing and managing
customers, subscriptions, and invoices in Stripe.

This example shows the connector creating a Stripe subscription schedule from an
activated Salesforce CPQ order.

## Before you begin

The connector assumes the following about your Salesforce account configuration:

- You use Salesforce CPQ.
- You use Stripe Billing.
- Collections activity won’t occur in other billing or accounting systems.
- A Salesforce order is sent to Stripe for billing and collections upon
activation. Inactive orders in Salesforce won’t be sent to Stripe for billing or
collections, by default.
- All order quantities are integers and not fractional values.
- All order amendments must co-terminate with the original order’s end date.
- Any invoices in Stripe generated as a result of activating a Salesforce CPQ
order won’t exist in Salesforce, by either creation or syncing. For Stripe to
Salesforce syncing, see the [Stripe Connector for
Salesforce](https://docs.stripe.com/connectors/stripe-connector-for-salesforce/overview).

## Install the connector

The connector is a managed package that you install from the [Salesforce
AppExchange](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000FOm4xUAD)
onto your Salesforce account.

## See also

- [Set up the
connector](https://docs.stripe.com/connectors/salesforce-cpq/setup)
- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Error
handling](https://docs.stripe.com/connectors/salesforce-cpq/error-handling)

## Links

- [subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
- [invoices](https://docs.stripe.com/billing/invoices/subscription)
- [Stripe Dashboard](https://docs.stripe.com/dashboard/basics)
- [Stripe Connector for
Salesforce](https://docs.stripe.com/connectors/stripe-connector-for-salesforce/overview)
- [Salesforce
AppExchange](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000FOm4xUAD)
- [Set up the
connector](https://docs.stripe.com/connectors/salesforce-cpq/setup)
- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Error
handling](https://docs.stripe.com/connectors/salesforce-cpq/error-handling)