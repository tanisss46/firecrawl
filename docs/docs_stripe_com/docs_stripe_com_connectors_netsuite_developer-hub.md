# Developer hub

## Learn about the developer workflows for using the Stripe Connector for NetSuite.

The Stripe Connector for NetSuite is a Stripe app that syncs data between your
Stripe and NetSuite accounts, without requiring any customizations. The
connector uses the data generated in your Stripe account to create an equivalent
record in NetSuite.

### Security

The connector uses HTTPS to [securely](https://docs.stripe.com/security)
communicate with NetSuite, and the latest version of TLS supported by NetSuite.
No unauthenticated data is passed to NetSuite or any other system. In addition,
the connector uses Stripe components for payment collection and [SCA
compliance](https://docs.stripe.com/strong-customer-authentication/sca-enforcement).

### Testing

The connector includes an automated testing system that runs daily tests on
every NetSuite feature and use case. You can connect your Stripe test
environment to your NetSuite release preview to verify that the connector
functions properly with the latest NetSuite release and your other integrations.

### Developer workflow

[Stripe payment processing in NetSuiteReconcile Stripe payments from third-party
or homegrown systems into
NetSuite.](https://docs.stripe.com/connectors/netsuite/custom-payment-application)[Field
mappingConfigure the fields and records that you want to map between Stripe and
NetSuite.](https://docs.stripe.com/connectors/netsuite/field-mappings)[Stripe
and NetSuite field referencesLearn about how the connector correlates Stripe
records with NetSuite
records.](https://docs.stripe.com/connectors/netsuite/fields-references)[Real-time
eventsSync your data from Stripe to NetSuite, and learn about how the connector
handles webhook
events.](https://docs.stripe.com/connectors/netsuite/sync-data)[Error resolution
guideIdentify and resolve errors with the connector and errors syncing records
from Stripe to
NetSuite.](https://docs.stripe.com/connectors/netsuite/error-resolution)

## Links

- [securely](https://docs.stripe.com/security)
- [SCA
compliance](https://docs.stripe.com/strong-customer-authentication/sca-enforcement)
- [Stripe payment processing in NetSuiteReconcile Stripe payments from
third-party or homegrown systems into
NetSuite.](https://docs.stripe.com/connectors/netsuite/custom-payment-application)
- [Field mappingConfigure the fields and records that you want to map between
Stripe and
NetSuite.](https://docs.stripe.com/connectors/netsuite/field-mappings)
- [Stripe and NetSuite field referencesLearn about how the connector correlates
Stripe records with NetSuite
records.](https://docs.stripe.com/connectors/netsuite/fields-references)
- [Real-time eventsSync your data from Stripe to NetSuite, and learn about how
the connector handles webhook
events.](https://docs.stripe.com/connectors/netsuite/sync-data)
- [Error resolution guideIdentify and resolve errors with the connector and
errors syncing records from Stripe to
NetSuite.](https://docs.stripe.com/connectors/netsuite/error-resolution)