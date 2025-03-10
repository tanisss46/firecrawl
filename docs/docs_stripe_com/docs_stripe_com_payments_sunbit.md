# Sunbit paymentsPrivate preview

## Offer customers the ability to pay in 3, 6, 12 (or more) monthly installments while getting paid instantly.

[Sunbit](https://sunbit.com/) is a buy now, pay later payment method available
in the US that gives your customers the flexibility to choose the number of
monthly installments they want to use for payment. When customers select Sunbit
as their payment method, Stripe redirects them to Sunbit’s website, where they
get the ability to choose between 3, 6, or 12-month flexible payment plans to
complete their purchase. You are paid up front. Sunbit handles the customer’s
payments and collections.

Payment method propertiesBusiness locationsProduct support- **Customer
locations**

US Customers
- **Presentment currency**

USD
- **Payment confirmation**

Customer-initiated
- **Payment method family**

Buy Now, Pay Later
- **Recurring payments**

No
- **Payout timing**

Standard
- **Connect support**

Yes
- **Dispute support**

Yes
- **Manual capture support**

Yes
- **Refunds / Partial refunds**

Yes / Yes

## Interested in getting early access to Sunbit?

To learn more or get early access, enter your email address below. We’ll work
with you to determine your eligibility and add you to the waitlist if you
qualify.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Payment flow

Below is a demonstration of the Sunbit payment flow from your checkout page:

## Get started

You don’t have to integrate Sunbit and other payment methods individually. If
you use our front-end products, Stripe automatically determines the most
relevant payment methods to display. Go to the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable
Sunbit. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart): Our prebuilt, hosted
checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart): Our drop-in UI
components.

### Other payment products

The following Stripe products also let you add Sunbit from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links)

If your integration requires manually listing payment methods, learn how to
[manually configure Sunbit as a
payment](https://docs.stripe.com/payments/sunbit/accept-a-payment).

## Payment options

The minimum charge limit is 60.00 USD.

The maximum charge limit is 9,999.99 USD.

## Prohibited and restricted business categories

In addition to the categories of goods or services sold and businesses
[restricted from using Stripe
overall](https://stripe.com/restricted-businesses), the following categories are
prohibited from using Sunbit:

- Agricultural Cooperative
- Dry Cleaners
- Family Clothing Stores
- Intra-Company Purchases
- Lumber, Building Materials Stores
- Nursing/Personal Care
- Parking Lots, Garages
- Stamp and Coin Stores
- Used Merchandise and Secondhand Stores
- Other categories at the discretion of Sunbit

## Additional requirements

You acknowledge that:

- Sunbit (and/or its partner bank) decides if customers can use Sunbit for
purchases and has the sole right to receive payment from Sunbit customers.
Stripe acquires those purchases for you and settles the funds to you.
- Customers must complete their own applications and review all terms related to
your goods and services and the use of Sunbit.
- You can’t impose fees or higher prices for Sunbit purchases (that is, no
surcharging).
- The amount financed including any down payment entered on the customer
application for Sunbit purchases must be equal to or less than the price of
goods/services delivered/rendered to the customer.

## Disputes

Sunbit has a claims process that allows transaction disputes. Customers can open
disputes for cases of suspected fraud, double payments, or a difference between
an order and a transaction amount.

After the customer initiates a dispute, Stripe notifies you using:

- Email
- The Stripe Dashboard
- An API `charge.dispute.created` event (if your integration is set up to
receive [webhooks](https://docs.stripe.com/webhooks))

Stripe holds back the disputed amount from your balance until Sunbit resolves
the dispute.

We request that you upload compelling evidence proving that you fulfilled the
purchase order [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond). This evidence
can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or
proof of receipt
- Record of refund (for purchase you’ve already refunded)

To handle disputes programmatically, [respond to disputes using the
API](https://docs.stripe.com/disputes/api).

This information helps Sunbit determine if a dispute is valid. Make sure the
evidence you provide contains as much detail as possible from what the customer
provided at checkout. You must submit the requested information within 12
calendar days. If Sunbit resolves the dispute with you winning, we return the
disputed amount to your Stripe balance. If Sunbit rules in favor of the
customer, the balance charge becomes permanent.

## Refunds

Sunbit supports full and partial refunds. The refund period is up to 180 days
after the purchase. Refunds for Sunbit payments are asynchronous and take up to
5 minutes to complete. Stripe notifies you of the final refund status using the
`refund.updated` or `refund.failed` [webhook](https://docs.stripe.com/webhooks)
event. When a refund succeeds, the
[Refund](https://docs.stripe.com/api/refunds/object) object’s status transitions
to `succeeded`. If a refund fails, the `Refund` object’s status transitions to
`failed` and we return the amount to your Stripe balance. You’ll then need to
arrange an alternative way of providing your customer with a refund.

## Connect

If you use [Connect](https://docs.stripe.com/connect), you must consider the
following before you enable and use Sunbit.

### Request Sunbit capabilities for your connected accounts

Set the `sunbit_payments` capability to `active` on your platform account, and
on any connected accounts you want to enable Sunbit for. You can also [request
more account
capabilities](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting).

### Merchant of record and statement descriptors

The [charge type](https://docs.stripe.com/connect/charges) of Connect payments
might change the default statement descriptor and the merchant name that appears
on the customer’s banking application and confirmation emails.

Charge typeDescriptor taken fromDirectConnected
accountDestinationPlatformSeparate charge and transferPlatformDestination (with
`on_behalf_of`)Connected accountSeparate charge and transfer (with
`on_behalf_of`)Connected account
## Supported currencies

You can create Sunbit payments in the currencies that map to your country. The
default local currency for Sunbit is `usd` and customers also see their purchase
amount in `usd`.

CurrencyCountry`usd`United States

## Links

- [Sunbit](https://sunbit.com/)
- [privacy policy](https://stripe.com/privacy)
- [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)
- [Checkout](https://docs.stripe.com/checkout/quickstart)
- [Elements](https://docs.stripe.com/payments/quickstart)
- [Payment Links](https://docs.stripe.com/payment-links)
- [manually configure Sunbit as a
payment](https://docs.stripe.com/payments/sunbit/accept-a-payment)
- [restricted from using Stripe
overall](https://stripe.com/restricted-businesses)
- [webhooks](https://docs.stripe.com/webhooks)
- [using the Stripe
Dashboard](https://docs.stripe.com/disputes/responding#respond)
- [respond to disputes using the API](https://docs.stripe.com/disputes/api)
- [Refund](https://docs.stripe.com/api/refunds/object)
- [Connect](https://docs.stripe.com/connect)
- [request more account
capabilities](https://docs.stripe.com/connect/account-capabilities#requesting-unrequesting)
- [charge type](https://docs.stripe.com/connect/charges)