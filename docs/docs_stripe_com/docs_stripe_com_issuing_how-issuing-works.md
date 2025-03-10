# How Issuing works

## Learn how to start building your commercial card program.

[Stripe Issuing](https://stripe.com/issuing) is part of Stripe’s
banking-as-a-service APIs that allows you to create, manage, and scale a
commercial card program for your users without setup fees. You can get started
quickly and programmatically control every detail of your program, from card
design to approving transactions in real time. Many users build Stripe Issuing
in conjunction with [Stripe Treasury](https://docs.stripe.com/treasury) to
attach cards to open loop wallets to offer their users additional money movement
functionalities.

[Contact sales](https://stripe.com/contact/sales) to start the process and
determine your eligibility to use Issuing. If you’re interested in using
Treasury with your Issuing integration, fill out the [Treasury
form](https://go.stripe.global/treasury-inquiry) instead.

Issuing is currently available in the US, UK, and many [European Economic
Area](https://en.wikipedia.org/wiki/European_Economic_Area) (EEA) countries. In
the US, you can provide cards to individuals who reside in the same country
where business is established. If your business is established in the EU or the
UK, you can provide cards to individuals residing in EEA countries and the UK.
Read more about [global issuing](https://docs.stripe.com/issuing/global) and see
a full list of supported countries.

A common use case for Issuing is spend management, which enables customers to
store funds on your platform and manage spending with branded cards.

## Building blocks for financial offerings

Stripe Issuing provides the tools and components needed to build a full-featured
financial offering for your customers.

Creating accountsIssuing CardsControlling SpendFunding with an Issuing
BalanceUsing Issuing with Treasury- [Identity
verification](https://docs.stripe.com/connect/identity-verification)- Reduce
risk
- Perform KYC checks
- Run sanctions screening

We’ve partnered with multiple trusted banks to provide the banking-as-a-service
infrastructure for you to build new financial service offerings.

We also partner with both Mastercard and Visa card networks so you can choose
the network on which you want to issue cards. You can also issue cards on both
networks.

## Issuing architecture

With Stripe [Connect](https://docs.stripe.com/connect), you onboard customers to
your platform with connected accounts. For each of these connected accounts, you
can create accountholders and provide cards to authorized users. The following
diagram demonstrates a platform with a Stripe Issuing integration using an
Issuing balance and a Treasury balance:

Issuing balance funding sourceTreasury balance funding sourcePlatformConnected
accountConnected account
Issuing Balance

Issuing Balance

BankBank
Cardholder

Cardholder

Card

Card

Top-upTop-upDiagram of a platform integrated with Issuing
### Connected accounts

Issuing only supports connected accounts that don’t use a Stripe-hosted
Dashboard, and where your platform is responsible for requirements collection
and loss liability, also known as a Custom connected account. Learn how to
[create connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
that work with Issuing.

### Issuing balance

An Issuing balance is a funding source attached to a connected account that
provides the funds for spending with the associated card account. Funds can be
added to the connected account’s Issuing balance either by transferring from the
connected account’s Stripe account balance, or through a top up from an external
bank account. Funds can also be paid out from the Issuing balance to an external
bank account.

Connected accounts can also use a Stripe Treasury account to fund cards for a
full banking-as-a-service solution.

## See also

- [Learn how to set up Issuing as a Connect
platform](https://docs.stripe.com/issuing/connect)
- [Review compliance requirements pertaining to
Issuing](https://docs.stripe.com/issuing/compliance-us)
- [Review best practices and tools for testing an Issuing
integration](https://docs.stripe.com/issuing/testing)
- [Learn about setting card rules to control
spending](https://docs.stripe.com/issuing/controls/spending-controls)
- [Learn about fraud controls and tools offered through Stripe
Issuing](https://docs.stripe.com/issuing/manage-fraud)

## Links

- [Stripe Issuing](https://stripe.com/issuing)
- [Stripe Treasury](https://docs.stripe.com/treasury)
- [Contact sales](https://stripe.com/contact/sales)
- [Treasury form](https://go.stripe.global/treasury-inquiry)
- [European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)
- [global issuing](https://docs.stripe.com/issuing/global)
- [Identity verification](https://docs.stripe.com/connect/identity-verification)
- [Connect](https://docs.stripe.com/connect)
- [create connected
accounts](https://docs.stripe.com/connect/design-an-integration?connect-onboarding-surface=api&connect-dashboard-type=none&connect-economic-model=buy-rate&connect-loss-liability-owner=platform&connect-charge-type=direct)
- [Learn how to set up Issuing as a Connect
platform](https://docs.stripe.com/issuing/connect)
- [Review compliance requirements pertaining to
Issuing](https://docs.stripe.com/issuing/compliance-us)
- [Review best practices and tools for testing an Issuing
integration](https://docs.stripe.com/issuing/testing)
- [Learn about setting card rules to control
spending](https://docs.stripe.com/issuing/controls/spending-controls)
- [Learn about fraud controls and tools offered through Stripe
Issuing](https://docs.stripe.com/issuing/manage-fraud)