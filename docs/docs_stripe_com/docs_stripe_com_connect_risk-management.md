# Risk management with Connect

## Learn how Connect can help you manage risk and losses.

All business owners assume a certain amount of risk when accepting payments for
goods and services. This guide defines the risks to consider as a Connect
platform owner and the approaches you can take to mitigate those risks.

## Components of payments risk

Any approach to risk management involves many potential sources of payments
risk, which can be split into two general categories:

- **Transaction risk**: The risk that a customer might charge back a
transaction, such as [disputes](https://docs.stripe.com/disputes) or fraud
identified from card testing. With [direct
charges](https://docs.stripe.com/connect/direct-charges), transaction risk
primarily affects connected accounts; with [destination
charges](https://docs.stripe.com/connect/destination-charges) and [separate
charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers),
transaction risk primarily affects platforms.
- **Merchant risk**: The risk that a connected account is unable or unwilling to
cover the costs of chargebacks on its transactions, leading to unrecoverable
negative balances. Merchant risk primarily affects platforms.

There are two main types of merchant risk: credit risk and fraud risk. Both can
result in chargebacks and unrecoverable negative balances.

TypeDescriptionExamplesCredit riskThe risk that connected accounts are unable to
fulfill their obligations to their customers, such as failing to deliver orders
due to unforeseen supply issues. If a connected account accumulates more refunds
and chargebacks than it can financially cover, it can result in default.During
the COVID pandemic, some hotels and short-term accommodation providers
represented by connected accounts went out of business. As a result, customers
who had pre-paid for future stays submitted chargebacks, which were covered by
the platforms that processed those payments.Fraud riskThe risk that dishonest
owners or employees of connected accounts intentionally don’t fulfill their
obligations to their customers, such as taking orders for unavailable goods and
services.- **No intent to deliver**: A fraudulent online storefront charged
customers for goods that they didn’t intend to deliver. The connected account
then paid out the money to their external bank account. When the customers
realized that their orders were never going to arrive, they submitted
chargebacks, which were covered by the platform.
- **Payment method cashing**: A fraudster stole a customer’s credit card number,
opened a connected account, and made purchases through that account using the
stolen payment method credentials. When the customer discovered the fraudulent
charges, they submitted chargebacks, which were covered by the platform.

## Connect merchant risk options

Each connected account’s Account object has a
[controller.losses.payments](https://docs.stripe.com/api/accounts/object#account_object-controller-losses-payments)
property that determines who’s [responsible for covering any negative payments
balance](https://docs.stripe.com/connect/risk-management) on that account.

#### Note

The `controller.losses.payments` property applies only to the connected
account’s payments balance. It doesn’t affect responsibility for covering
negative Issuing or Treasury balances.

You can select whether you or Stripe is responsible for negative balance
liabilities on your accounts. Because your choice of negative balance liability
can significantly impact your platform and connected accounts, consider it
carefully before onboarding any accounts. This table describes some important
elements of the decision:

StripePlatform[API
value](https://docs.stripe.com/api/accounts/object#account_object-controller-losses-payments)`stripe``application`LossesStripe
covers losses due to your connected accounts’ negative balances.Your platform
can incur losses due to your connected accounts’ negative balances.Operational
responsibilitiesStripe’s risk teams fully manage all payments-related merchant
risk.The platform maintains an internal risk team capable of adequately managing
all payments-related merchant risk.Connected account experienceStripe directly
contacts your connected accounts to prevent, mitigate, and resolve payments
risk-related issues, and in some cases can take action against them.Your
platform has a greater degree of control over the payments risk-related
experience of your connected accounts.Stripe feesIf you pay Stripe’s listed
prices for other fees, we don’t charge additional fees for negative balance
liability.Stripe charges no additional fees.
We recommend that new platforms have Stripe take responsibility for negative
balances on connected accounts. Only consider taking responsibility as the
platform if you’re highly confident in your ability to manage merchant risk.

## Stripe solutions for risk management

Stripe provides a variety of solutions to help manage both transaction and
merchant risk. These solutions fall into two categories:

- **Tools to manage risk**: Tools that Stripe provides to help platforms manage
risks without Stripe being liable for any resulting losses.
- **Full service risk management**: Risk-management services that Stripe
provides where Stripe covers the costs of any resulting losses.

This table describes the main solution that Stripe provides in each category for
each type of risk:

Risk typeTools to manage riskFull service risk managementTransaction
risk[Radar](https://docs.stripe.com/radar): Scans every payment to help detect
and prevent fraud.Merchant riskMerchant risk tooling: Tools that help your risk
teams prevent, detect, and mitigate risks posed by your connected
accounts.[Stripe Managed
Risk](https://docs.stripe.com/connect/risk-management/managed-risk): A
full-service solution that protects your platform by managing risk and covering
any negative balances on your connected accounts.
## Know Your Customer (KYC) and compliance

In addition to operational risk management solutions, Stripe provides KYC and
risk-based screening to help onboard connected accounts and maintain compliance
with evolving regulations. Stripe screens include the following:

- Identity verifications
- Risk-based KYC and AML checks for individuals and businesses
- Sanctions screening
- MATCH (Member Alert To Control High-risk businesses) list checks
- Secure credit card data tokenization for PCI compliance
- Money transmitter licenses (MTL) in the US and e-money (EMI) licenses in the
EU
- [Prohibited business checks](https://stripe.com/legal/restricted-businesses)

## Links

- [disputes](https://docs.stripe.com/disputes)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
-
[controller.losses.payments](https://docs.stripe.com/api/accounts/object#account_object-controller-losses-payments)
- [responsible for covering any negative payments
balance](https://docs.stripe.com/connect/risk-management)
- [Radar](https://docs.stripe.com/radar)
- [Stripe Managed
Risk](https://docs.stripe.com/connect/risk-management/managed-risk)
- [Prohibited business checks](https://stripe.com/legal/restricted-businesses)