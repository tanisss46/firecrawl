# Zip payments

## Learn about Zip, a popular payment method in Australia and the US for customers to buy now and pay later.

[Zip](https://zip.co/) gives your customers in Australia and the US (beta) a way
to split purchases over a series of payments.

Customers who elect to pay with Zip are redirected to the Zip site, where they
[authorize](https://docs.stripe.com/payments/payment-methods#customer-actions)
the payment by agreeing to the terms of a payment plan. After payment terms
acceptance, Zip transfers funds to your Stripe account up front and your
customer repays Zip over time according to their agreement terms.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

Australia, United States Beta
- **Presentment currency**

AUD, USD Beta
- **Payment confirmation**

Customer-authenticated
- **Payment method family**

Buy now, pay later
- **Recurring payments**

No
- **Payout timing**

Standard
- **Connect support**

Yes
- **Dispute support**

[Yes](https://docs.stripe.com/payments/zip#disputes-and-fraud)
- **Manual capture support**

No
- **Refunds / Partial refunds**

[Yes / Yes](https://docs.stripe.com/payments/zip#refunds)

## Interested in getting early access to Zip in the US?

In the United States, Zip is currently in private preview. If you're interested
in trying it out, enter your email address below.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Payment flow

Below is a demonstration of the Zip payment flow from your checkout page:

This demo shows the customer experience when using Zip.

## Get started

You don’t have to integrate Zip and other payment methods individually. If you
use our front-end products, Stripe automatically determines the most relevant
payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Zip. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Zip from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links)

If you prefer to manually list payment methods, learn how to [manually configure
Zip as a payment](https://docs.stripe.com/payments/zip/accept-a-payment).

## Payment options

Available payment options vary by country. In Australia, Zip offers Zip Pay and
Zip Money, which have flexible repayment plans. In the US, Zip offers a Pay in 4
plan that splits repayment into 4 installments over 6 weeks. Regardless of the
payment option selected, Stripe makes the full amount of the funds (minus fees)
available to you upfront and Zip collects the purchase amount from your
customer, who repays Zip directly.

- [Zip Pay](https://zip.co/au/zip-pay): A line of credit up to 1000 AUD.
Customers can select their repayment frequency, either weekly, bi-weekly, or
monthly. Zip charges customers a monthly account fee, but waives it if the
balance is repaid in full.
- [Zip Money](https://zip.co/au/zip-money): A line of credit between 1000 AUD
and 5000 AUD, and potentially up to 50,000 AUD. Customers can adjust the
installment period with no interest for 3-36 months, depending on the retailer.
If you want to offer your customers interest-free repayment periods longer than
3 months, or credit limits higher than 5000 AUD, [contact Stripe
support](https://support.stripe.com/contact/email?question=other&topic=payment_apis&subject=ZipPayments&refcode=yN2i).
Zip charges customers an account establishment fee and a monthly fee, but waives
the monthly fee when the account balance is zero.
- [Zip pay-in-4](https://zip.co/us/how-it-works): Customers pay for purchases
over 4 installments. Zip [adds a finance
charge](https://help.us.zip.co/hc/en-us/articles/4402386045979--Are-there-any-fees-to-use-Zip)
based on the purchase amount, and splits the total amount into 4 equal
installments. Customers pay the first installment at time of purchase, then make
the 3 remaining repayments at 2-week intervals.

The following table lists total transaction limits, currency and payment options
by country:

Stripe account and customer countryCurrencyTransaction limitsZip Pay Zip Money
Zip pay-in-4 AustraliaAUD1 - 50,000* United States BetaUSD35 - 1,500
* If the purchase amount is greater than their available credit, customers can
pay the rest with cards up front.

## Prohibited business categories

In addition to standard [Stripe business
restrictions](https://stripe.com/legal/restricted-businesses), some other
business categories are prohibited from accepting Zip payments through Stripe,
depending on your country.

For detailed information, see Zip prohibited and restricted business information
for [Australia](https://help.zip.co/hc/en-us/articles/6544802536591) and the
[United
States](https://merchant-help.us.zip.co/hc/en-us/articles/12709915538971-Prohibited-and-Restricted-Business-Information).

## Add Zip branding to your website

Zip works closely with partners to test and enhance the way Zip is presented to
customers. Their integration and marketing requirements aim to benefit
businesses by converting more browsers into shoppers and increasing average
basket sizes. You must use and display Zip’s branding according to their
guidance, which varies by country:

- Australia: See [best practice
integration](https://developers.zip.co/docs/best-practice-implementation) guide
and [static visual assets and branding
guidelines](https://developers.zip.co/docs/zip-marketing-assets).
- United States: See [marketing
guidelines](https://zip.co/us/merchant-resources)

## Disputes

Customers must authenticate Zip payments by logging into their Zip account. This
requirement helps reduce the risk of fraud or unrecognized payments. While Zip
covers losses incurred from customer fraud, Stripe might contact you on behalf
of Zip and request to stop or pause shipment before any losses are incurred.
Comply promptly with these requests.

Customers can dispute Zip payments in certain cases—for example, if they receive
faulty goods or don’t receive them at all. Customers have up to 180 calendar
days from the date of purchase to file a dispute.

In Australia, Zip requires customers to first contact you directly to resolve a
dispute. If, after 14 days from the date of purchase, that doesn’t resolve it,
the customer can initiate a dispute case with Zip.

Stripe notifies you of a dispute using:

- Email
- Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to
receive [webhooks](https://docs.stripe.com/webhooks))

Stripe holds back the disputed amount from your balance until Zip resolves the
dispute.

Stripe requests that you upload compelling evidence that you fulfilled the
purchase order [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond). This evidence
can include:

- Received return confirmation (for shipped goods returned from the customer to
you)
- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as an IP address or email
receipt
- Record of purchase for services or physical goods, such as a phone number or
proof of receipt

If you would rather handle disputes programmatically, you can [respond to
disputes using the API](https://docs.stripe.com/disputes/api).

This information helps Zip determine if a dispute is valid or if they need to
reject it. Make sure the evidence you provide contains as much detail as
possible from what the customer provided at checkout. If Zip resolves the
dispute with you winning, Stripe returns the disputed amount and dispute fee to
your Stripe balance. If Zip rules in favor of the customer, the balance charge
becomes permanent.

## Refunds

Payments made with Zip can only be submitted for refund within 180 calendar days
from the date of the original charge. After 180 days, it’s no longer possible to
refund the charge.

## Additional requirements

**You acknowledge that:**

- Zip decides if customers can use Zip for purchases and has the sole right to
receive payment from Zip customers. Stripe acquires those purchases for you and
settles the funds to you.
- You must not process a Zip transaction unless delivery will be completed
within 60 days.
- You must retain information about each Zip transaction for at least 18 months.
- You can’t give return credits in cash unless required by law.
- You can’t impose fees or higher prices for Zip purchases (that is, no
surcharging).
- If a customer has questions about how Zip handles their information, you will
refer them to Zip’s privacy policy.

**If you’re in the United States, you acknowledge that:**

- All goods and services for Zip transactions must be located in the United
States.
- Zip can’t be used to pay for a gift card, gift voucher, prepaid stored value
card, or prepaid stored value voucher.
- Transactions must be recorded in US dollars.
- Zip or its lending partner may extend credit to Zip customers for a fee.

## Links

- [Zip](https://zip.co/)
- [authorize](https://docs.stripe.com/payments/payment-methods#customer-actions)
- [Yes](https://docs.stripe.com/payments/zip#disputes-and-fraud)
- [Yes / Yes](https://docs.stripe.com/payments/zip#refunds)
- [privacy policy](https://stripe.com/privacy)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure Zip as a
payment](https://docs.stripe.com/payments/zip/accept-a-payment)
- [Zip Pay](https://zip.co/au/zip-pay)
- [Zip Money](https://zip.co/au/zip-money)
- [contact Stripe
support](https://support.stripe.com/contact/email?question=other&topic=payment_apis&subject=ZipPayments&refcode=yN2i)
- [Zip pay-in-4](https://zip.co/us/how-it-works)
- [adds a finance
charge](https://help.us.zip.co/hc/en-us/articles/4402386045979--Are-there-any-fees-to-use-Zip)
- [Stripe business restrictions](https://stripe.com/legal/restricted-businesses)
- [Australia](https://help.zip.co/hc/en-us/articles/6544802536591)
- [United
States](https://merchant-help.us.zip.co/hc/en-us/articles/12709915538971-Prohibited-and-Restricted-Business-Information)
- [best practice
integration](https://developers.zip.co/docs/best-practice-implementation)
- [static visual assets and branding
guidelines](https://developers.zip.co/docs/zip-marketing-assets)
- [marketing guidelines](https://zip.co/us/merchant-resources)
- [webhooks](https://docs.stripe.com/webhooks)
- [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond)
- [respond to disputes using the API](https://docs.stripe.com/disputes/api)