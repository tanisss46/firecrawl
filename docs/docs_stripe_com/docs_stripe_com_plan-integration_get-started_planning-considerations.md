# Planning considerations

## Identify essential integration decisions and considerations.

Before you start building your integration, make sure that everyone impacted by
the move to Stripe understands their requirements. This guide identifies the
integration decisions and considerations you need when using Stripe for the
first time.

## Structure your Stripe accounts

One of the first questions to answer is whether you’ll need a single Stripe
account, or several. To learn more, see our [account
overview](https://docs.stripe.com/get-started/account).

### Considerations

- **Which countries will you operate in?**

If more than one, consider creating ​​Stripe accounts where you have legal
entities to take advantage of local acquiring for local customers.

In some countries, Stripe supports adding [multiple bank accounts for different
currencies](https://docs.stripe.com/payouts#supported-accounts-and-settlement-currencies),
which might impact the number of accounts you create.

For example, if you have legal entities in the United States, Canada, and the
Netherlands, and plan to pay out to bank accounts in multiple currencies, you
might choose to have a US account for USD
[payouts](https://docs.stripe.com/payouts), a CA account for CAD payouts, and
one NL account capable of settling in EUR, GBP, and DKK. This account
organization allows you to benefit from local acquiring and separate payouts by
business line.
- **Do you need to direct funds to more than one bank account?**

If both bank accounts are in the same currency, create separate Stripe accounts
to take advantage of automatic payouts and avoid manually switching between bank
accounts for each payout.
- **How will you create your accounts?**

You need to complete account setup for each Stripe account. To set up regional
Stripe accounts, add new accounts using your [first Stripe
account](https://docs.stripe.com/get-started/account/multiple-accounts) to
streamline authentication and access.

If your integration requires multiple Stripe accounts, it’s important to know
which account you’re operating in. You need to specify the [secret
key](https://docs.stripe.com/api/authentication) on each API request to
correctly identify the regional account.

If you’re going to use a single account for Stripe transactions and charge
customers in every currency, you only need to go through account setup one time.
This account organization guarantees that all data is available in a single
account, which streamlines the integration and reporting process. You can also
create additional Stripe accounts later for different geographies if needed.
- **Can you benefit from local acquiring?**

To benefit from local acquiring, you need to have regional accounts.
- **Do you need centralized reporting in a single Stripe account?**

OptionsRegionalUnifiedDescriptionA more complex integration that uses multiple
regional Stripe accounts to manage multiple bank accounts or acquire in local
currencies. Requires a local legal entity for each Stripe account.The simplest
integration that uses a single Stripe account for charging customers in every
currency and specific payment methods depending on the account’s
location.Benefits- Acquire in the local market with the most support for new
payment methods.
- Eliminate FX and settles into like currency.
- Achieve higher authorization rates and lower network costs
- Unify reporting under a single Stripe account for all markets.
- Avoid developing internal logic for routing customer transactions to the
correct Stripe account for processing.
Limitations- Adds complexity to reporting and integration.
- Lacks a holistic Dashboard view of data.
- Some payment methods might not be compatible.
- Necessitates cross-border acquiring and settlement FX.

## Accept payments

[PaymentIntents](https://docs.stripe.com/payments/payment-intents) is our
default API. PaymentIntents track the lifecycle of a customer’s payment flow
​​and enable you to integrate against asynchronous payment flows like [3D
Secure](https://docs.stripe.com/payments/3d-secure). Asynchronous flows are
especially important when it comes to supporting global expansion (for example,
[SCA](https://docs.stripe.com/strong-customer-authentication), compliance with
3D Secure in Europe (and similar regulations in India), and introducing other
payment methods such as SEPA Direct Debit or SOFORT in Europe.

### Considerations

- **Which payment methods will you offer your customers?**

To see which payment methods the PaymentMethods API supports, check for [digital
wallets](https://docs.stripe.com/payments/wallets#product-support), [bank
debits](https://docs.stripe.com/payments/bank-debits#product-support), [bank
redirects](https://docs.stripe.com/payments/bank-redirects#product-support),
[buy now, pay
later](https://docs.stripe.com/payments/buy-now-pay-later#product-support), and
[vouchers](https://docs.stripe.com/payments/vouchers#product-support).
- **Which countries will you operate in?**

If your business is based in the [European Economic
Area](https://en.wikipedia.org/wiki/European_Economic_Area) (EEA) and you serve
customers in the EEA, you must integrate on PaymentIntents to comply with SCA
regulations. ​​If your business is based in India and serving customers in
India, we also recommend using PaymentIntents.
- **Which payment methods and countries are on your roadmap?**

If you don’t require PaymentIntents today but plan to expand to new payment
methods or countries, we recommend that you integrate with PaymentIntents for
all methods that are currently available as PaymentMethods, and plan your
[migration to
PaymentIntents](https://docs.stripe.com/payments/payment-intents/migration) for
the remaining methods when they become available on the [PaymentMethods
API](https://docs.stripe.com/payments/payment-methods).

## Capture customer payment details

The client-side integration process typically involves building components for
Stripe. Use our [website
checklist](https://docs.stripe.com/get-started/checklist/website) to make sure
you’re following best practices and standards for your frontend development.

The [Integration security guide](https://docs.stripe.com/security) helps you
ensure [PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
and explains the importance of secure communication between your customer and
your servers.

### Considerations

- **Is your business already PCI-compliant?**

If yes, and you want to process cards without tokenizing, speak to your Stripe
contact or [support.stripe.com](https://support.stripe.com/).
- **Will you be using multiple payment processors?**

If yes, consider dual-tokenization when processing card payments.
Dual-tokenizing can help you to continue to run charges on your other payment
processor without prompting your customers for their credit card details again.
- **How will you manage fraud in the checkout experience?**

To provide Stripe with additional fraud signals, include
[Stripe.js](https://docs.stripe.com/payments/elements) on every page that a
customer interacts with related to the checkout process. This includes product
and payment pages.
- **How much control do you need over the checkout experience?**

Stripe offers two main ways to create payment forms:
[Elements](https://docs.stripe.com/payments/elements) and
[Checkout](https://docs.stripe.com/payments/checkout). Both are secure,
optimized for conversion, and PCI-compliant, though they differ in terms of
customizability and time to integrate.

OptionsStripe CheckoutStripe.JS and ElementsDescriptionStripe Checkout is a
secure, Stripe-hosted page that lets you collect payments. It works across
devices and can help increase your conversion.Elements is a set of prebuilt UI
components, like inputs and buttons, for building your checkout flow. Stripe.js
tokenizes sensitive payment details without ever letting it touch your
server.Benefits- Simplified integration.
- Up-to-date with available payment methods.
- Optimized conversion.
- Co-branded with your business logo and colors.
- Optimized conversion with dynamic inputs.
- Simplified PCI compliance with SAQ A reporting because all sensitive
information is handled by Stripe.js.
- Customizable styling to match the appearance of your checkout flow.
Limitations- Temporarily redirects customers off your web domain.
- Fewer options for customization.
- Increased integration time and effort compared to Checkout.
- Elements doesn’t support all payment methods, requiring that you build
additional fields to use unsupported methods.

### Create a PaymentMethod with Stripe.js or a mobile SDK

If you’re using Stripe.js and Elements, tokenize payment details from a customer
before creating a charge.

At a high level, this process involves using a [publishable
key](https://support.stripe.com/questions/where-do-i-find-my-api-keys) to
transmit card (or other payment method) details from a client browser or mobile
app directly to Stripe’s servers.

Stripe ingests these sensitive payment details and returns a
[PaymentMethod](https://docs.stripe.com/api/payment_methods) that can be
charged. For users accessing the service using a web browser, use
[Stripe.js](https://docs.stripe.com/payments/elements).

If the user is submitting payment details using an
[iOS](https://docs.stripe.com/payments/accept-a-payment?platform=ios) or
[Android](https://docs.stripe.com/payments/accept-a-payment?platform=android)
app, use one of Stripe’s libraries.

## Reconcile payments and payouts

​​Involve your finance team early in your scoping so that they can advise you on
your new reconciliation process and reporting needs. To learn more about your
options, start by reviewing the Payments and payouts and Financial reports
Guides. Depending on your needs, you may use a combination of Financial Reports,
Dashboard exports, Sigma, and the API.

### Considerations

- **Do you require fast and frequent access to transaction data and payouts?**

- [Reports](https://docs.stripe.com/stripe-reports) and
[Sigma](https://docs.stripe.com/stripe-data) make your data available by 12:00
UTC the following day.
- Dashboard exports, while available immediately, take longer to generate, which
makes them best for pulling small increments of data on the order of several
thousand records—not tens of thousands.
- Building custom reporting using the Stripe APIs provides access to the
specific data you need as it becomes available. However, it’s resource-intensive
to both build and maintain.
- **Do you have data analytics tooling?**

Sigma is our custom reporting tool that makes all of your transactional data
available as an interactive SQL environment in the
[Dashboard](https://dashboard.stripe.com/test/get-started/sigma). You can use it
to gain insights into anything from ARPU to customer churn, and identify new
business opportunities.
- **Which data points do you use to reconcile your finances? Are any of these
fields custom and generated by your team (for example, an order or booking
ID)?**

Make sure ​​your custom data is included as
[metadata](https://docs.stripe.com/payments/payment-intents#storing-information-in-metadata)
on any relevant reporting objects.
OptionsFinancial reportsSigmaCustom reportsDescriptionView the financial data
within your Stripe account, helping to streamline your business workflowsProcess
business data using SQL. Use SQL to explore your Stripe data, revenue, and
create customized reportsBuild your own reporting through Dashboard exports, the
API, and webhooksBenefits- Prebuilt
- Downloadable with the Dashboard or API
- Leverages feature development
- Flexibility to create the reports you need
- Downloadable with the Dashboard or API
- Leverages feature development
- Complete flexibility and access to raw data

**Limitations**

- Limited to reports available
- Requires SQL to build reports
- Requires significant time and resources to build
- Maintained entirely by your team

### Considerations

- **Does your business require that you pay out specific amounts to your bank
account?**

If you don’t need to control your payouts, use automatic payouts to sweep your
entire balance automatically into your bank account on your payout schedule.

If you do need to deposit specific amounts, you can use manual payouts to
delimit the amount you transfer to your bank account. Manual payouts don’t allow
you to link the payout amount to specific transactions.

Alternatively, consider [Instant
Payouts](https://docs.stripe.com/payouts/instant-payouts-banks) to a debit card,
which facilitates remaining on automatic payouts.
- **Do you want to retain a balance in your account?**

Manual and Instant Payouts allow you to keep a Stripe balance of your choosing.
- **Do you plan to reconcile between transactions on your account and payouts to
your bank?**

If yes, use automatic payouts.
OptionsManualAutomatic and instant payoutsDescriptionManually create payouts for
the specified amount and currency to the bank account of your
choosing.Automatically pay out funds when they’re available and after
settlement, either daily, weekly, or monthly. Take advantage of Instant Payouts
while your account is configured for automatic payouts.Benefits- Supports custom
payout schedules that you can be trigger from the API or manually from your
Dashboard.
- You can trigger manual payouts by specific events or at the discretion of your
account.
- Automatically includes failed payouts in the next payout.
- Allows transaction-level mapping to payout amount for straightforward
reconciliation.
- Where regionally available, can use Instant Payouts to manually initiate
immediate payment to a debit card on file.
Limitations- Absent payout triggers, available funds may stay in account balance
for extended periods of time.
- Need to implement retry logic using `payout.failed` webhook.
- Can’t determine which transactions are included in a given manual payout.
- Can’t use Instant Payouts while configured for manual payouts.
- Can’t accommodate biweekly, bimonthly, or other custom payout schedules.

## Protect your business from fraud and disputes

As an e-commerce business, it’s essential to keep fraud rates low and handle
customer disputes. Stripe offers [Radar](https://docs.stripe.com/radar), which
helps you fine-tune your fraud prevention environment, get insights about
suspicious charges, and assess your fraud management performance from a unified
dashboard. For businesses in many markets, and more generally for e-commerce,
fighting fraud is fundamental to success.

### Considerations

- **Do you encounter moderate or high fraud and dispute rates?**

Consider employing some of these [best
practices](https://docs.stripe.com/disputes/prevention/best-practices) as part
of your overall fraud strategy to avoid excessive chargebacks and reduce
potential customer burden and losses.
- **Would your business benefit from granular control in your fraud prevention
tooling?**

Radar allows you to choose your risk tolerance, write your own Rules to
fine-tune your protection using a variety of transaction attributes, and manage
custom block and review lists that enable you to quickly take action on fraud.

## Links

- [account overview](https://docs.stripe.com/get-started/account)
- [multiple bank accounts for different
currencies](https://docs.stripe.com/payouts#supported-accounts-and-settlement-currencies)
- [payouts](https://docs.stripe.com/payouts)
- [first Stripe
account](https://docs.stripe.com/get-started/account/multiple-accounts)
- [secret key](https://docs.stripe.com/api/authentication)
- [PaymentIntents](https://docs.stripe.com/payments/payment-intents)
- [3D Secure](https://docs.stripe.com/payments/3d-secure)
- [SCA](https://docs.stripe.com/strong-customer-authentication)
- [payment methods](https://docs.stripe.com/payments/payment-methods)
- [digital wallets](https://docs.stripe.com/payments/wallets#product-support)
- [bank debits](https://docs.stripe.com/payments/bank-debits#product-support)
- [bank
redirects](https://docs.stripe.com/payments/bank-redirects#product-support)
- [buy now, pay
later](https://docs.stripe.com/payments/buy-now-pay-later#product-support)
- [vouchers](https://docs.stripe.com/payments/vouchers#product-support)
- [European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)
- [migration to
PaymentIntents](https://docs.stripe.com/payments/payment-intents/migration)
- [website checklist](https://docs.stripe.com/get-started/checklist/website)
- [Integration security guide](https://docs.stripe.com/security)
- [PCI
compliance](https://docs.stripe.com/security/guide#validating-pci-compliance)
- [support.stripe.com](https://support.stripe.com/)
- [Stripe.js](https://docs.stripe.com/payments/elements)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [publishable
key](https://support.stripe.com/questions/where-do-i-find-my-api-keys)
- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [iOS](https://docs.stripe.com/payments/accept-a-payment?platform=ios)
- [Android](https://docs.stripe.com/payments/accept-a-payment?platform=android)
- [Reports](https://docs.stripe.com/stripe-reports)
- [Sigma](https://docs.stripe.com/stripe-data)
- [Dashboard](https://dashboard.stripe.com/test/get-started/sigma)
-
[metadata](https://docs.stripe.com/payments/payment-intents#storing-information-in-metadata)
- [Instant Payouts](https://docs.stripe.com/payouts/instant-payouts-banks)
- [Radar](https://docs.stripe.com/radar)
- [best practices](https://docs.stripe.com/disputes/prevention/best-practices)