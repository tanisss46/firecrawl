# Accept international payments from IndiaInvite only

## When buyers of your goods or services are located outside India.

#### Note

Stripe is available by invite only in India. This means that businesses from
India can’t sign up for a new Stripe account through our website, and must
[request an invite](https://stripe.com/in/contact/sales) instead. We currently
only support a select number of businesses, with a focus on international
expansion.

Stripe supports presentment in 135+ currencies on Visa and Mastercard, and INR
or USD currencies on American Express. You can prevent declines caused by a
mistaken perception of a fraudulent charge and increase your success rates by
presenting your international payments in your customer’s local currency.

To present in a non-INR currency, you must provide additional information during
account onboarding and in API requests. Declare these transactions as exports
from India and localize your [presentment
currency](https://docs.stripe.com/currencies#presentment-currencies) to match
that of the customer’s card (for example, USD, EUR, JPY, and so on).

For more information, see our [India
FAQ](https://support.stripe.com/questions/india-faq).

## Requirements

Stripe supports both INR and non-INR presentment for customers located outside
India, provided:

- The Stripe account must be a registered Indian business (sole proprietorship,
limited liability partnership, or company).
- The Stripe business can’t be an
[individual](https://support.stripe.com/questions/how-can-i-open-a-stripe-account-in-india).
- If you sell physical goods, you must provide a valid Importer Exporter Code
(IEC).
- If you sell services, providing an IEC is optional, unless:- You accept AMEX
payments from international customers.
- You take any benefits under India’s Foreign Trade Policy.

## Onboarding

To enable export transactions, you must do the following when submitting your
account application:

- **Opt in to exports**: In the account application, under **I am exporting
products to customers located outside India**, select the applicable box. If you
don’t opt in, you can only make export charges in a
[sandbox](https://docs.stripe.com/sandboxes). This option is only available for
certain users (sole proprietorship, limited liability partnership, or company).
- **Submit your importer/exporter code (IEC)**: The IEC is a code issued by the
Indian Director General of Foreign Trade (DGFT) to Indian companies that intend
to export from India. You can apply for an IEC on the [DGFT
website](https://dgft.gov.in/CP/).

You must provide an IEC under certain conditions:

- If you plan to accept Visa or Mastercard and you sell physical goods.
- If you plan to accept [AMEX international
payments](https://support.stripe.com/questions/american-express-card-support-for-india-based-businesses)
for all export transactions, including selling physical goods and services, as
described by India’s Foreign Trade Policy.
- **Specify a transaction purpose code**: The [transaction purpose
code](https://docs.stripe.com/india-accept-international-payments#TransactionPurposeCode)
describes the nature of a payment received in foreign currency. The Reserve Bank
of India (RBI) maintains the list of valid transaction purpose codes. You must
select the code that’s closest to your product from the dropdown in the account
application.

### Opt in or update export details after account activation

You can opt into the ability to enable exports, change your IEC (if applicable),
or change your transaction purpose code at any time through the
[Dashboard](https://dashboard.stripe.com/settings/update). If needed, you can
use the same IEC for multiple export businesses, as long as the IEC is in the
name of a common beneficial owner of both businesses.

A Stripe account can only have a single transaction purpose code.

### Valid charges

Provide these additional fields for every international payment presented to a
customer holding a non-India issued card to meet regulatory reporting
requirements:

- The buyer’s `name`
- The `billing address` with a valid [2-alphabet
ISO-3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code
- The charge `description`
- The `shipping address` with a valid [2-alphabet
ISO-3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code, if you
sell physical goods

### Payouts

Stripe pays out to you in INR the funds collected from domestic and
international payments. If you process both domestic and international payments,
you might receive two payouts on the same day, with an **International** label
for the relevant [payouts in your
Dashboard](https://dashboard.stripe.com/test/payouts).

## International payments for services

Provide the following fields for every international payment for services to
meet our financial partners’ requirements:

- The buyer’s `name`
- The `billing address`
- A `description` of the service to export

You must provide this information to prevent the payment from failing.

To declare a payment as an export transaction:

- Pass the service description in the Payment Intents API:

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d description="Software development services"
```
- Pass the customer name and billing address using the [create a
customer](https://docs.stripe.com/api/customers/create) API:

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Jenny Rosen" \
 -d "address[line1]"="510 Townsend St" \
 -d "address[postal_code]"=98140 \
 -d "address[city]"="San Francisco" \
 -d "address[state]"=CA \
 -d "address[country]"=US
```

## International payments for goods

Our financial partners require the following fields for every international
payment for goods:

- The buyer’s `name`
- The `billing address`
- A `description` of the item to export
- The `shipping address`

You must provide this information to prevent the payment from failing.

To declare a payment as an export transaction:

- Pass the `description` of the item and a `shipping address` in the Payment
Intents API:

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d description="Software development services" \
 -d "shipping[name]"="Jenny Rosen" \
 -d "shipping[address][line1]"="510 Townsend St" \
 -d "shipping[address][postal_code]"=98140 \
 -d "shipping[address][city]"="San Francisco" \
 -d "shipping[address][state]"=CA \
 -d "shipping[address][country]"=US \
 -d amount=1099 \
 -d currency=usd \
 -d "payment_method_types[]"=card
```
- Pass the customer `name` and `billing address` in the [create a
customer](https://docs.stripe.com/api/customers/create) API:

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Jenny Rosen" \
 -d "address[line1]"="510 Townsend St" \
 -d "address[postal_code]"=98140 \
 -d "address[city]"="San Francisco" \
 -d "address[state]"=CA \
 -d "address[country]"=US
```

## Fight fraud

International card payments require 2-factor authentication using [3D Secure
(3DS)](https://support.stripe.com/questions/3d-secure-authentication-for-international-card-payments-to-indian-businesses).

## Accept recurring international payments

You can use [Stripe Billing](https://docs.stripe.com/billing) to bill your
international customers using
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating) and
[invoices](https://docs.stripe.com/api/invoices).

For recurring international payments related to services, you must provide a
buyer’s `name` and an `address`.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Jenny Rosen" \
 -d "address[line1]"="510 Townsend St" \
 -d "address[postal_code]"=98140 \
 -d "address[city]"="San Francisco" \
 -d "address[state]"=CA \
 -d "address[country]"=US
```

Stripe generates a `description` from the description on your invoice items.
Make sure the description on your invoice items accurately reflects your
product.

```
curl https://api.stripe.com/v1/invoiceitems \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer=cus_Ej0c314UoUXBgX \
 -d amount=2500 \
 -d currency=usd \
 -d description="One-time setup fee"
```

For recurring international payments related to physical goods, you must provide
a `shipping address` in the [create a
customer](https://docs.stripe.com/api/customers/create) API.

```
curl https://api.stripe.com/v1/customers \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "shipping[name]"="Jenny Rosen" \
 -d "shipping[address][line1]"="510 Townsend St" \
 -d "shipping[address][postal_code]"=98140 \
 -d "shipping[address][city]"="San Francisco" \
 -d "shipping[address][state]"=CA \
 -d "shipping[address][country]"=US
```

### Recurring payments best practices

When selling to international customers, 3D Secure isn’t mandatory, but you
might notice a higher dispute rate than when you sell to Indian customers.

We often see [disputes](https://docs.stripe.com/disputes) from customers
claiming that they were charged even after they canceled their subscription.
Here are some best practices to avoid these disputes:

- Make it clear on your signup page that your customers are agreeing to a
recurring payment and include information about whether or not you plan to
notify the customer before each payment. Make sure cancellation procedures are
clearly communicated to your customers, and clearly state the window during
which your customer can cancel a subscription. Include copies of these
procedures in a visible terms of service page.
- If you offer a free or discounted trial period, be sure to clearly communicate
the length of the trial and the date when your customer is billed the full
price. Clearly display the amount of the standard pricing above the payment
button on your checkout page.
- Cancel subscriptions within two business days of initial request, making sure
to pass the cancellation along to Stripe if you use our subscription
functionality. Per card network rules, you can only make eight attempts per card
after an initial decline, so be sure to close out any subscriptions that have
already reached this limit. Provide your customer with a confirmation of the
cancellation.
- Have a clear way for customers to contact you if requesting cancellation. If
customers have questions about their subscription, they’re more likely to submit
a dispute if they can’t contact you. You can track your overall dispute activity
under the Analytics section in your Dashboard.

## Monthly payment advice for export transactions

Standard Chartered Bank (SCB) issues payment advice directly to your registered
Stripe email address the same day your export payout is processed. This includes
a list of export charges that are part of the specific export payout.

## Transaction purpose codes

If you have a Stripe account, you can select the following transaction purpose
codes during account onboarding or in the Dashboard. Select the code that best
aligns with your business. Stripe can’t support codes not listed below due to
requirements from our financial partner.

Purpose code groupCodeDescriptionExports (of Goods)P0102Realization of export
bills (in respect of goods) sent on collection (full invoice value). Excludes
Nepal and Bhutan.Exports (of Goods)P0103Advance receipts against export
contracts, which are covered later by GR/PP/SOFTEX/SDF. Excludes Nepal and
Bhutan.TravelP0302Business travelComputer and Information ServicesP0801Hardware
consultancy or implementationComputer and Information ServicesP0802Software
consultancy or implementation (other than those covered in SOFTEX form)Computer
and Information ServicesP0803Database or data processing chargesComputer and
Information ServicesP0804Repair and maintenance of computer and softwareComputer
and Information ServicesP0805News agency servicesComputer and Information
ServicesP0806Other information services (for example, subscriptions to
newspapers or periodicals)Computer and Information ServicesP0807Off-site
software exportsComputer and Information ServicesP0808Telecommunication
services, including electronic mail services and voice mail servicesComputer and
Information ServicesP0809Satellite services, including space shuttles, rockets,
and so onOther Business ServicesP1002Trade related services (for example,
commission on exports or imports)Other Business ServicesP1004Legal servicesOther
Business ServicesP1005Accounting, auditing, or book keeping servicesOther
Business ServicesP1006Business and management consultancy and public relations
servicesOther Business ServicesP1007Advertising or trade fair servicesOther
Business ServicesP1008Research and development servicesOther Business
ServicesP1009Architectural servicesOther Business ServicesP1010Agricultural
services (for example, protection against insects and disease, increasing of
harvest yields, or forestry services)Other Business ServicesP1013Environmental
servicesOther Business ServicesP1014Engineering servicesOther Business
ServicesP1015Tax consulting servicesOther Business ServicesP1016Market research
and public opinion polling servicesOther Business ServicesP1017Publishing and
printing servicesOther Business ServicesP1018Mining services (for example,
on–site processing services or analysis of ores)Other Business
ServicesP1019Commission agent servicesOther Business ServicesP1020Wholesale and
retailing trade servicesOther Business ServicesP1022Other technical services
(for example, scientific services or space services)Personal, Cultural, and
Recreational ServicesP1101Audio-visual and related services (for example, motion
picture and video tape production, or distribution and projection
services)Personal, Cultural, and Recreational ServicesP1103Radio and television
production, distribution, and transmission servicesPersonal, Cultural, and
Recreational ServicesP1104Entertainment servicesPersonal, Cultural, and
Recreational ServicesP1105Museums, library, and archival servicesPersonal,
Cultural, and Recreational ServicesP1106Recreation and sporting activity
servicesPersonal, Cultural, and Recreational ServicesP1107Educational services
(for example, fees received for correspondence courses offered to non-residents
by Indian institutions)Personal, Cultural, and Recreational ServicesP1108Health
services (receipts on account of services provided by Indian hospitals, doctors,
nurses, paramedical, and similar services rendered remotely or on-site)Personal,
Cultural, and Recreational ServicesP1109Other personal, cultural, and
recreational services

## Links

- [request an invite](https://stripe.com/in/contact/sales)
- [presentment
currency](https://docs.stripe.com/currencies#presentment-currencies)
- [India FAQ](https://support.stripe.com/questions/india-faq)
-
[individual](https://support.stripe.com/questions/how-can-i-open-a-stripe-account-in-india)
- [sandbox](https://docs.stripe.com/sandboxes)
- [DGFT website](https://dgft.gov.in/CP/)
- [AMEX international
payments](https://support.stripe.com/questions/american-express-card-support-for-india-based-businesses)
- [Dashboard](https://dashboard.stripe.com/settings/update)
- [2-alphabet ISO-3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
- [payouts in your Dashboard](https://dashboard.stripe.com/test/payouts)
- [create a customer](https://docs.stripe.com/api/customers/create)
- [3D Secure
(3DS)](https://support.stripe.com/questions/3d-secure-authentication-for-international-card-payments-to-indian-businesses)
- [Stripe Billing](https://docs.stripe.com/billing)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [invoices](https://docs.stripe.com/api/invoices)
- [disputes](https://docs.stripe.com/disputes)