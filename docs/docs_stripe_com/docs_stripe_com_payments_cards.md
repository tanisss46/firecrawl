# Cards

## Learn more about accepting card payments with Stripe.

Cards are linked to a debit or credit account at a bank. To complete a payment
online, customers enter their card information at checkout. Cards are enabled by
default and are supported by [online payments integration
paths](https://docs.stripe.com/payments/online-payments#compare-features-and-availability).
You can manage payment methods from the
[Dashboard](https://dashboard.stripe.com/settings/payment_methods). Stripe
handles the return of eligible payment methods based on factors such as the
transaction’s amount, currency, and payment flow.

## Payment flow

A customer initiates a card payment at checkout by entering their credit card
information. Depending on their card network and country location, customers
have some card functionalities like additional security verification steps.

![A flowchart showing the three required and one optional step for a customer to
pay with
card.](https://b.stripecdn.com/docs-statics-srv/assets/pay-with-card.059eb99f8cad148c1aea3bb2a29b8284.svg)

Cards can act as the funding source for other Stripe payment products and
methods like [Link](https://docs.stripe.com/payments/link) and
[wallets](https://docs.stripe.com/payments/wallets). For instance, customers can
leverage Link to save their card payment data for fast checkout with any
business that has Link enabled.

With wallets, customers can store their card details in a [digital
wallet](https://docs.stripe.com/payments/payment-methods). From your end, their
payment method is managed using a `wallet`, but for the customer, the
transaction shows up in their card history as a charge from their digital wallet
provider.

## Supported card brands

Stripe supports several card brands, from large global networks like Visa and
Mastercard to local networks like Cartes Bancaires in France or Interac in
Canada. When you integrate Stripe, you can begin accepting a diversity of card
brands without any additional configurations, including:

- American Express
- China UnionPay (CUP)
- Discover & Diners Club
- eftpos Australia
- Japan Credit Bureau (JCB)
- Mastercard
- Visa

Some card brands require additional configuration, such as [Cartes
Bancaires](https://docs.stripe.com/payments/cartes-bancaires) and
[Interac](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#interac-payments).

#### Note

In integrations that [handle Link payments as card
payments](https://docs.stripe.com/payments/link/link-payment-integrations?link-integrations=link-card-integrations),
non-card payment methods saved to Link can have a card brand of `link`.

### Online card brand capabilities

The following table describes some of the different features and restrictions of
each card brand online, including limitations on countries where Stripe users
can accept the brand (Stripe Account Country), countries where most cardholders
of the brand are located (Customer Country) and support for key features like 3D
Secure Authentication, and [Wallets](https://docs.stripe.com/payments/wallets)
(like Apple Pay and Google Pay).

#### Note

Other payment scenarios like setting up [future
payments](https://docs.stripe.com/payments/save-and-reuse), [saving a
card](https://docs.stripe.com/payments/save-during-payment) or [placing a
hold](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method) are
supported across all card brands.

Stripe supports processing payments in [135+
currencies](https://docs.stripe.com/currencies), but some card brand networks
have limitations on [supported
currencies](https://docs.stripe.com/currencies#presentment-currencies) that
charges can be made with.

Card BrandStripe Account CountryCustomer Country 3D Secure Authentication
Wallets VisaAll countriesGlobalMastercardAll countriesGlobalAmerican ExpressAll
countries except Brazil, Malaysia, Thailand, and the United Arab EmiratesGlobal,
except India1Discover & Diners ClubCanada, Japan, United Kingdom, United States,
and the following European Economic Area countries: Austria, Belgium, Cyprus,
Denmark, Estonia, Finland, France, Germany, Greece, Ireland, Italy, Latvia,
Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Slovakia,
Slovenia, Spain, Sweden, and SwitzerlandGlobalChina UnionPayAustralia, Canada,
Hong Kong, Malaysia, New Zealand, Singapore, United Kingdom, United States,
Switzerland, and all countries in the European Economic Area except Croatia,
Iceland, and LichtensteinGlobalNot supportedJapan Credit Bureau (JCB)Australia,
Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom,
United States, and all countries in the European Economic Area except
IcelandGlobalHong Kong, Japan, Singapore, Switzerland, United Kingdom, and all
countries in the European Economic Area except IcelandCartes BancairesAll
countries in the [SEPA](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area)
region, as well as Canada Australia, Hong Kong, Japan, Mexico, New Zealand,
Singapore, and United StatesFrance2eftposAustraliaAustralia Not supported,
payments route to the co-brand networkNot supported
1 For more information, see [American Express card support for India-based
businesses](https://support.stripe.com/questions/american-express-card-support-for-india-based-businesses).

2 Supports Apple Pay. For more information, see [Cartes Bancaires with Apple
Pay](https://docs.stripe.com/apple-pay/cartes-bancaires).

### Exclude card brands

You can disallow the use of specific card brands in the following ways:

- If you use Stripe Radar, [set up a rule](https://docs.stripe.com/radar/rules)
to reject the desired brands.
- Add custom client-side code that checks the
[brand](https://docs.stripe.com/api/cards/object#card_object-brand) of a card.

## Geographic considerations

Stripe, along with other platforms, offer a solid infrastructure that handles
secure payments and complies with specific regulations from different regions.
This becomes particularly important with the roll-out of Strong Customer
Authentication (SCA) rules in regulated markets like Europe and India, wherein
additional verification steps are usually necessary.

It’s essential to ensure your Stripe integration is lined up with SCA rules and
3D Secure (3DS) criteria. Moreover, adjusting your approach to suit regional
nuances—like installment payments and card brand preferences—is vital for
seamless, compliant, and user-centered transactions.

### SCA and 3D Secure

Some banks, especially in regulated regions like Europe and India, might prompt
the customer to authenticate a purchase (for example, by texting the customer a
code to enter on the bank’s website). This authentication step is part of
[Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication) (SCA)
Requirements. Making sure that your integration meets SCA requirements for 3DS
can sometimes require extra steps.

[SCA](https://docs.stripe.com/strong-customer-authentication), a rule in effect
as of September 14, 2019, as part of PSD2 regulation in Europe, requires changes
to how your European customers authenticate online payments. Card payments
require a different user experience, namely
[3DS](https://docs.stripe.com/payments/3d-secure), to meet SCA requirements.

Stripe supports 3DS by default in Stripe Checkout, Payment Links, and a Hosted
Invoice Page. You can configure your integration to use 3DS with Subscriptions
and [Connect](https://docs.stripe.com/connect) with the following:

- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Setup Intents API](https://docs.stripe.com/api/setup_intents)
- Elements
- Mobile SDKs

### Installments

Some regions have card brands that support installment payments - which are
managed by the card issuer and not by creating Subscriptions or using
SetupIntents with Stripe.

If you want to create recurring payments and your region or card network doesn’t
support [Meses sin intereses](https://docs.stripe.com/payments/mx-installments),
see how to [set up future
payments](https://docs.stripe.com/payments/save-and-reuse) or
[Subscriptions](https://docs.stripe.com/billing/subscriptions/overview).

### Card brand choice

The European Union requires businesses to allow their customers the option to
pick which card brand processes their transaction because cards in the EU might
have both a local network, like Cartes Bancaires, and an affiliated card
network, like Visa or Mastercard. You can enable this choice using Elements or
Payments APIs so that [customers can choose which card
brand](https://docs.stripe.com/co-badged-cards-compliance) processes their
payment.

### Accept card payments in India

The Reserve Bank of India (RBI) has specific regulations for online transactions
that apply to Stripe accounts in India. Stripe Support includes a consolidated
list of important resources, for many payment methods in the [India
FAQs](https://support.stripe.com/questions/india-faq).

## See also

- [Integrate card payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
- [Understand card updates and change default payment
methods](https://docs.stripe.com/payments/cards/overview#card-updates)
- [Customize the way PaymentElements handle
cards](https://docs.stripe.com/payments/customize-payment-methods)

## Links

- [online payments integration
paths](https://docs.stripe.com/payments/online-payments#compare-features-and-availability)
- [Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Link](https://docs.stripe.com/payments/link)
- [wallets](https://docs.stripe.com/payments/wallets)
- [digital wallet](https://docs.stripe.com/payments/payment-methods)
- [Cartes Bancaires](https://docs.stripe.com/payments/cartes-bancaires)
-
[Interac](https://docs.stripe.com/terminal/payments/regional?integration-country=CA#interac-payments)
- [handle Link payments as card
payments](https://docs.stripe.com/payments/link/link-payment-integrations?link-integrations=link-card-integrations)
- [future payments](https://docs.stripe.com/payments/save-and-reuse)
- [saving a card](https://docs.stripe.com/payments/save-during-payment)
- [placing a
hold](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method)
- [135+ currencies](https://docs.stripe.com/currencies)
- [supported
currencies](https://docs.stripe.com/currencies#presentment-currencies)
- [SEPA](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area)
- [American Express card support for India-based
businesses](https://support.stripe.com/questions/american-express-card-support-for-india-based-businesses)
- [Cartes Bancaires with Apple
Pay](https://docs.stripe.com/apple-pay/cartes-bancaires)
- [set up a rule](https://docs.stripe.com/radar/rules)
- [brand](https://docs.stripe.com/api/cards/object#card_object-brand)
- [Strong Customer
Authentication](https://docs.stripe.com/strong-customer-authentication)
- [3DS](https://docs.stripe.com/payments/3d-secure)
- [Connect](https://docs.stripe.com/connect)
- [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
- [Setup Intents API](https://docs.stripe.com/api/setup_intents)
- [Meses sin intereses](https://docs.stripe.com/payments/mx-installments)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview)
- [customers can choose which card
brand](https://docs.stripe.com/co-badged-cards-compliance)
- [India FAQs](https://support.stripe.com/questions/india-faq)
- [Integrate card payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
- [Understand card updates and change default payment
methods](https://docs.stripe.com/payments/cards/overview#card-updates)
- [Customize the way PaymentElements handle
cards](https://docs.stripe.com/payments/customize-payment-methods)