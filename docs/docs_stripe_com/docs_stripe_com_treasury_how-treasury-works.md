# How Treasury works

## Learn about connected accounts, financial accounts, and moving money with Treasury.

[Stripe Treasury](https://stripe.com/treasury) is a Banking as a Service (BaaS)
API for Stripe [Connect](https://docs.stripe.com/connect) platforms that allows
you to embed financial services in your product.

Stripe provides the infrastructure in partnership with trusted banks. You can
use Treasury to enable your connected accounts to hold funds, pay bills, earn
cash back, and manage their cash flow.

## Building blocks for financial services

Stripe Treasury provides modular components for building a full-featured,
scalable financial product.

Create accountsStore fundsMove moneyAttach payment cards
Set up your connected accounts as Treasury customers, verify their identity, and
provision Treasury financial accounts with one of our bank partners.

- ID verification
- [KYC](https://en.wikipedia.org/wiki/Know_your_customer) checks
- Sanctions screening

## Treasury use cases

The following are examples of some common Stripe Treasury use cases:

Use caseDescriptionSpend managementBuild a spend management product for your
customers to store funds on your platform and manage spending with branded
cards.Store and spend accountCreate FDIC insurance-eligible accounts that allow
businesses to store funds, earn cash back, accept checks, and pay contractors
and vendors with ACH and wire transfers.Programmatic money movementFacilitate
money movement between your platform’s connected accounts and from connected
accounts to third-party accounts.
## Treasury account architecture

Using [Connect](https://docs.stripe.com/connect), you onboard customers to your
platform as connected accounts. You can create a Treasury account for each
connected account to access your financial products. The following diagram
illustrates an overview of a platform with Stripe Treasury integration.

![Diagram of a platform integrated with Treasury, showing customers, platform,
connected and financial accounts, external bank accounts, payment cards, and
money
movement.](https://b.stripecdn.com/docs-statics-srv/assets/architecture.59cac501261250e0ebe9785c6f9701ce.png)

Treasury account architecture

![Diagram of a platform integrated with Treasury, showing customers, platform,
connected and financial accounts, external bank accounts, payment cards, and
money
movement.](https://b.stripecdn.com/docs-statics-srv/assets/architecture.59cac501261250e0ebe9785c6f9701ce.png)

### Connected accounts

Connected accounts are sellers or service providers that use a platform. For
example, if you’re a digital storefront platform owner, you provide an
e-commerce framework that businesses use to establish online stores and collect
payments. Each business that uses your storefront platform is a connected
account.

Treasury only supports connected accounts that don’t use a Stripe-hosted
dashboard and where your platform is responsible for requirements collection and
loss liability, including Custom connected accounts. Learn how to [create
connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
that work with Treasury.

#### Private preview

Enabling Treasury on non-custom connected accounts is a new feature. Email
[treasury-support@stripe.com](mailto:treasury-support@stripe.com) to request
access.

As a platform with connected accounts, you’re responsible for maintaining a
minimum API version, communicating terms of service updates to your connected
accounts, handling information requests from them, and providing them with
support. Because your platform is ultimately responsible for the losses your
connected accounts incur, you’re also responsible for vetting them for fraud. To
learn more, read the [Treasury fraud
guide](https://docs.stripe.com/treasury/examples/fraud-guide).

### Financial accounts

You can use the Treasury endpoints of the [Stripe
API](https://docs.stripe.com/api) to create financial accounts, and attach them
to connected accounts in a one-to-one relationship (unless you’re enrolled in
the [Multi FA
beta](https://docs.stripe.com/treasury/account-management/financial-accounts#create-a-financialaccount)).

You can fund the financial accounts of your platform’s connected accounts and
move money between them. Your connected accounts can also fund their Treasury
financial accounts using a bank external to Stripe. If your platform uses Stripe
Issuing, you can provide payment cards linked to the financial account balance
of your connected accounts.

Treasury financial accounts have routing numbers because they’re backed by US
banking partners, and balances are eligible for FDIC pass-through insurance.

## Sample integration

Follow our two-part sample integration to see how Treasury works:

- [Use Treasury to set up financial accounts and create cards with
Issuing](https://docs.stripe.com/treasury/examples/financial-accounts)
- [Use Treasury with SetupIntents and PaymentMethods to move
money](https://docs.stripe.com/treasury/examples/moving-money)

Stripe Treasury is provided in the US by Stripe Payments Company, licensed money
transmitter, with funds held at Stripe’s bank partners, Members FDIC. Card and
other credit products are provided by Celtic Bank, Member FDIC and serviced by
Stripe, Inc. and its affiliate Stripe Servicing, Inc.

## See also

- [Treasury accounts
structure](https://docs.stripe.com/treasury/account-management/treasury-accounts-structure)
- [Working with connected
accounts](https://docs.stripe.com/treasury/account-management/connected-accounts)
- [Working with financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)

## Links

- [Stripe Treasury](https://stripe.com/treasury)
- [Connect](https://docs.stripe.com/connect)
- [KYC](https://en.wikipedia.org/wiki/Know_your_customer)
- [create connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
- [Treasury fraud guide](https://docs.stripe.com/treasury/examples/fraud-guide)
- [Stripe API](https://docs.stripe.com/api)
- [Multi FA
beta](https://docs.stripe.com/treasury/account-management/financial-accounts#create-a-financialaccount)
- [Use Treasury to set up financial accounts and create cards with
Issuing](https://docs.stripe.com/treasury/examples/financial-accounts)
- [Use Treasury with SetupIntents and PaymentMethods to move
money](https://docs.stripe.com/treasury/examples/moving-money)
- [Treasury accounts
structure](https://docs.stripe.com/treasury/account-management/treasury-accounts-structure)
- [Working with connected
accounts](https://docs.stripe.com/treasury/account-management/connected-accounts)
- [Working with financial
accounts](https://docs.stripe.com/treasury/account-management/financial-accounts)