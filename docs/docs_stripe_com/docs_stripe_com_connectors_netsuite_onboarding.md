# Prepare for onboarding

## Prepare your Stripe and NetSuite accounts for onboarding.

If you want to use the Stripe Connector for NetSuite, you must work with an
official implementation partner to set up the connector.

Before you begin, make sure to prepare your Stripe and NetSuite accounts for
onboarding using the guidance below.

- [Activate your Stripe
account](https://docs.stripe.com/connectors/netsuite/onboarding#stripe-account)
- [Set up a NetSuite test
account](https://docs.stripe.com/connectors/netsuite/onboarding#netsuite-sandbox)
- [Create a dedicated NetSuite user to operate the
connector](https://docs.stripe.com/connectors/netsuite/onboarding#netsuite-user)
- [Provide temporary admin access for the implementation
partner](https://docs.stripe.com/connectors/netsuite/onboarding#admin-access)
- (Optional) [Set up Stripe
Billing](https://docs.stripe.com/connectors/netsuite/onboarding#stripe-billing)

## Activate your Stripe account

If you haven’t already, [activate your Stripe
account](https://docs.stripe.com/get-started/account/activate).

## Set up a NetSuite sandbox

We recommend setting up a NetSuite sandbox environment to test the connector.
You can set up the connector to sync Stripe test data to your NetSuite
production account, but you must remember to manually delete the test data from
the production instance.

## Create a dedicated NetSuite user

To prevent any settings changes from inadvertently affecting the connector’s
ability to operate, we recommend creating a dedicated NetSuite user to operate
the connector. With a dedicated user, you can also identify actions taken or
changes made by that user in the NetSuite system log.

If you can’t provide a dedicated user, you can provide a shared user that isn’t
used for other integrations. Any changes to that user can negatively impact the
connector. For example, if you use an existing user login and that employee
leaves the company, deleting their NetSuite user can break the connector and
stop record syncing.

## Prepare to grant admin access

The implementation partner requires temporary admin access during onboarding for
the following:

- Testing in the sandbox environment
- Implementing the connector live in production
- Troubleshooting issues specific to your NetSuite account

If you must restrict access, we recommend providing admin and GUI access in the
sandbox environment, and then removing permissions before you move to
production.

Your implementation partner can provide further instructions for granting
access.

## (Optional) Set up Stripe Billing

If you use Stripe Billing and have existing Stripe prices and NetSuite items,
you need to do the following to prepare for onboarding:

- Prepare a data sheet to map IDs for existing Stripe and NetSuite customers.
- Prepare a data sheet to map IDs for existing Stripe prices and NetSuite items.
- Determine the rule for the connector to use for NetSuite revenue recognition.
- Determine the start date to sync records.

## Links

- [Install the app](https://marketplace.stripe.com/apps/netsuite-connector)
- [Activate your Stripe
account](https://docs.stripe.com/connectors/netsuite/onboarding#stripe-account)
- [Set up a NetSuite test
account](https://docs.stripe.com/connectors/netsuite/onboarding#netsuite-sandbox)
- [Create a dedicated NetSuite user to operate the
connector](https://docs.stripe.com/connectors/netsuite/onboarding#netsuite-user)
- [Provide temporary admin access for the implementation
partner](https://docs.stripe.com/connectors/netsuite/onboarding#admin-access)
- [Set up Stripe
Billing](https://docs.stripe.com/connectors/netsuite/onboarding#stripe-billing)
- [activate your Stripe
account](https://docs.stripe.com/get-started/account/activate)