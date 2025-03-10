# SaaS platform payments with subscription billing using Accounts v2Private preview

## Learn how a SaaS platform charges its connected accounts with Stripe Billing using Accounts v2.

SaaS (Software as a Service) platforms using
[Connect](https://docs.stripe.com/connect) often charge subscription fees for
providing their platform services. Accounts v1 requires platforms to maintain
separate Stripe objects to enable a single business to both pay for a
subscription (as a `Customer`) and operate on the platform (as an `Account`).
Accounts v2 allows you to manage all your interactions with your connected
accounts through a single, multi-configuration object.

## Interested in getting early access to Accounts v2?

Accounts v2 is currently limited to preview users. If you’re interested in
trying it out, enter your email address below.

Collect EmailSubmitRead our [privacy policy](https://stripe.com/privacy).
## Using Connect and Billing in API v1 with Accounts and Customers

In API v1, `Account` objects support only Connect features. To charge a
connected account using a subscription, a platform must create a `Customer`
object representing the same connected account. Accounts v1 and Customers v1
have no explicit relationship, so the platform must manage those objects
separately and maintain a map of `Account` IDs to `Customer` IDs.

#### SaaS platform relationships with Accounts and Customers in API v1

PlatformConnected accountCustomerCreate paymentsBill by subscriptionRelationship
of a SaaS platform with pairs of Accounts and Customers in API v1
## Using Connect and Billing in API v2 with Accounts

With Accounts v2, a connected account that collects payments and pays you a
subscription fee doesn’t require both an `Account` object and a `Customer`
object. Instead, you represent it by assigning the applicable configurations to
the `Account`.

To enable a connected account to collect payments from customers, assign the
Merchant configuration to the corresponding `Account`.

#### Platform and Account with Merchant configuration

Platform
Account (Merchant)

Shopper

Payment

Direct paymentApplication feesPayment less feesAn Accounts v2 platform
integration with accounts that have the Merchant configuration
To enable the platform to collect payments, including subscription payments,
from the connected account, add the Customer configuration to the `Account`.

#### Platform and Account with Merchant and Customer configurations

Platform
Account (Merchant + Customer)

Shopper

Payment

Subscription

Direct paymentApplication feesPayment less feesPaymentPaymentAn Accounts v2
platform integration with accounts that have the Merchant and Customer
configurations
#### Note

You can collect application fees from an `Account` with the Merchant
configuration. Assigning the Customer configuration to it doesn’t affect that
ability.

## The Accounts API v2

In API v2, `Account` objects can have multiple configurations. Each
configuration represents a different type of business relationship and enables
different Stripe products. By assigning multiple configurations to an `Account`,
a SaaS platform can enable both Connect and Billing for it without also having
to create a `Customer`.

The Accounts API v2 provides:

- **Unified representation:** A single `Account` object can represent multiple
relationships between connected accounts and your platform.
- **Flexible configurations:** Enable or change Stripe products and features by
changing the configurations assigned to an `Account`.
- **Centralized identity data:** The `Account` object stores all of a connected
account’s identity data. When you add a configuration to an existing `Account`,
you don’t have to collect requirements that they already provided.

## Private preview considerations

The [private preview release](https://docs.stripe.com/release-phases) of
Accounts v2 has some limitations. Consider the following:

- **Stripe products:** The preview integration uses Billing to collect
subscription fees and Connect to enable embedded payments.
- **Dashboard access and account types:** Your connected accounts can’t use the
full or Express Stripe Dashboard. Build a custom interface or use [Connect
embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components).
- **Payment methods:** `Accounts` with the Merchant configuration can accept
only card payments. They can’t accept wallet payments or Link payments,
regardless of the Link integration.
- **Charge types:** The preview integration supports only [direct
charges](https://docs.stripe.com/connect/direct-charges) and [destination
charges](https://docs.stripe.com/connect/destination-charges) with the
`on_behalf_of` parameter. You can’t use destination charges without
`on_behalf_of` or separate charges and transfers.

## Links

- [Connect](https://docs.stripe.com/connect)
- [privacy policy](https://stripe.com/privacy)
- [private preview release](https://docs.stripe.com/release-phases)
- [Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)