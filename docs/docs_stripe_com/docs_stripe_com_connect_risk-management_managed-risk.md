# Stripe Managed Risk

## Let Stripe protect your platform from losses that result from negative balances on your connected accounts.

Stripe Managed Risk is an end-to-end business risk management solution for
platforms that includes ongoing monitoring and mitigation for credit and fraud
risk. In addition, Stripe assumes risk of loss in the event of unrecoverable
negative balances on connected accounts.

When Stripe manages risk for connected accounts, we monitor risk signals, apply
risk interventions in response to observed signals, and seek to recover negative
balances. You aren’t liable for unrecoverable negative balances on your
connected accounts.

## Components of Stripe Managed Risk

Stripe Managed Risk has three core components:

- Screening and detection
- Monitoring and mitigation
- Stripe negative balance liability

### Screening and detection

When you onboard new connected accounts to your platform, Stripe conducts a
number of up-front risk-based onboarding checks. These checks verify adherence
to our compliance and regulatory standards and help identify fraud and credit
risk signals.

You can implement additional onboarding verifications to meet relevant
regulations for products or services offered by your platform or connected
accounts.

### Monitoring and mitigation

Stripe performs ongoing monitoring of risk signals (KYC, transaction data, and
so on) to identify connected accounts that might pose credit or fraud risks. We
use automated processes, such as machine learning models and Stripe risk team
manual reviews. Stripe automates interventions against risky businesses to
reduce fraud and risk of loss. For example, Stripe processes might flag a risky
connected account in response to a number of signals such as elevated losses,
spikes in chargeback rates, or refunds. In response, Stripe might take targeted
action on that account using any of a large number of interventions to reduce
risk exposure. Some of the Stripe key risk interventions include:

- **Changes to capabilities**: In response to risk signals, Stripe might slow or
pause payouts, or pause a connected account’s ability to process charges.
- **Reserves**: In response to risk signals, Stripe might hold a reserve on the
connected account balance. It can be a fixed amount or a percentage of
transaction amounts.
- **Offboarding**: In the extreme case that a business poses significant risk to
Stripe or your platform (ToS violations, fraud, and so on), Stripe might
deactivate the connected account.

### Stripe negative balance liability

When you use Stripe negative balance liability for connected accounts, Stripe
assumes the risk of losses from unrecoverable negative balances on those
connected accounts. In particular, Stripe doesn’t deduct unrecoverable negative
connected account balances from your platform account.

### Requirements to use Stripe Managed Risk

Stripe Managed Risk has these requirements:

- **Radar**: You must use Radar on connected account transactions. (For users
who pay Stripe’s listed prices for payments processing, Radar is included at no
additional cost.)
- **Connected account onboarding**: When onboarding connected accounts, you must
use either Stripe-hosted onboarding or the embedded onboarding component.
Connected accounts where Stripe is liable for negative balances, including
Standard accounts, can’t complete onboarding in any other way.
- **Connected account dashboard**: Connected accounts where Stripe is liable for
negative balances must have access to a Stripe-hosted dashboard, or your
platform’s interface must include both the [Notifications
Banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner)
and [Account
Management](https://docs.stripe.com/connect/supported-embedded-components/account-management)
embedded components. Some Stripe risk interventions require them to allow
connected accounts to update their business information.
- **Connected account capability and service agreement**: When creating
connected accounts, you must request the
[card_payment](https://docs.stripe.com/connect/account-capabilities#card-payments)
capability and the
[full](https://docs.stripe.com/connect/service-agreement-types#full) Stripe
Service Agreement type.

## Stripe Managed Risk for connected accounts

You define how your connected accounts interact with Stripe Managed Risk by
configuring their onboarding flow and their dashboard or other platform
interface.

### Connected account onboarding flow

When Stripe is liable for negative balances, you can onboard connected accounts
using Stripe-hosted onboarding or the [embedded onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding).
With either option, Stripe collects the required information for risk management
and prompts the connected account to accept the Stripe terms of service. You can
prefill any information that you have previously collected in your onboarding
flow using the Accounts API.

### Connected account dashboard or platform interface

Most connected accounts are likely to have few, if any, interactions with Stripe
risk management. However, in the event that Stripe requires additional
risk-related information from one of your connected accounts, Stripe notifies
your connected account and provides a pathway for them to respond to and resolve
the intervention.

To resolve an intervention, a connected account owner might provide additional
KYC information, complete a form, or provide other documentation. Stripe reviews
their response to assess whether to lift, revise, or continue the intervention.

### Connected accounts with access to the full Stripe Dashboard

### Connected accounts with access only to embedded components

## Fees for Stripe Managed Risk

The fees for Stripe Managed Risk depend on the economic model:

- **Revenue share**: For connected accounts where the platform uses a revenue
share economic model for payments processing, including Standard accounts, we
include Stripe Managed Risk at no additional cost.
- **Buy rate**: For connected accounts where the platform uses a buy-rate
economic model, Stripe Managed Risk fees depend on the pricing arrangements:-
**Listed pricing**: For platforms that pay listed pricing for payments
processing and Connect fees, we include Stripe Managed Risk at no additional
cost.
- **Negotiated pricing**: For platforms with negotiated pricing for either
payments processing or Connect fees, Stripe Managed Risk incurs additional fees.
For more information, contact Stripe Sales.

## Links

- [Notifications
Banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner)
- [Account
Management](https://docs.stripe.com/connect/supported-embedded-components/account-management)
-
[card_payment](https://docs.stripe.com/connect/account-capabilities#card-payments)
- [full](https://docs.stripe.com/connect/service-agreement-types#full)
- [embedded onboarding
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)