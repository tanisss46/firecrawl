# Recurring payments

## Understand your options for charging customers on a recurring basis.

Stripe offers several ways to charge customers on a recurring basis. This guide
helps you understand which method or approach best supports your business.

This guide offers a few ways to understand your options:

- [Use cases](https://docs.stripe.com/recurring-payments#use-cases): Find the
right use case for your business.
- [Types of recurring
payments](https://docs.stripe.com/recurring-payments#recurring-payment-types):
See all the recurring payment types that Stripe supports.
- [Stripe products](https://docs.stripe.com/recurring-payments#stripe-products):
Check which Stripe products support your recurring payment use case.

## Use cases

[Accept recurring paymentsLet customers pay you regularly and repeatedly through
Stripe.](https://docs.stripe.com/recurring-payments#accept-recurring-payments)[Split
purchases into a few paymentsCreate installment plans to let customers pay you a
total amount in a limited number of partial
payments.](https://docs.stripe.com/recurring-payments#installment-plans)[Enable
customers to manage their own subscriptionsSet up the customer portal so your
customers can create and manage their own
subscriptions.](https://docs.stripe.com/recurring-payments#enable-customer-portal)[Accept
recurring donationsLet customers make donations to your organization on a
regular
basis.](https://docs.stripe.com/recurring-payments#recurring-donations)[Migrate
existing subscriptions to StripeMove your existing subscriptions from a
third-party service to
Stripe.](https://docs.stripe.com/recurring-payments#migrate-subscriptions)
## Types of recurring payments

The following tabs describe the different types of recurring payments that
Stripe supports.

SubscriptionsInstallmentsRecurring invoicesCharges on saved payment methods
**Overview**

Use [Stripe Billing](https://docs.stripe.com/billing) to create and manage your
subscriptions through the Dashboard or programmatically through the API.

- [Create a payment link with a recurring
product](https://docs.stripe.com/payment-links/create).
- Create a subscription through the
[Dashboard](https://dashboard.stripe.com/subscriptions) or [build a
subscriptions
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions).
- Create [subscription
schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
for complex subscription use cases.
- If you use Connect, [create
subscriptions](https://docs.stripe.com/connect/subscriptions) for connected
accounts and end customers.
Features- No coding required. (You can optionally use the Subscriptions API and
prebuilt components like Stripe Checkout and Elements to build a programmatic
subscriptions integration.)
- Customize appearance and behavior in your app.
- Supports multiple products and prices in different currencies.
- Supports responsive web and mobile native.
- Website required. You can use Stripe Elements to customize the appearance of
payment forms.
Use cases- [Accept payments from customers on a recurring
basis](https://docs.stripe.com/recurring-payments#accept-recurring-payments)
- [Accept recurring
donations](https://docs.stripe.com/recurring-payments#recurring-donations)
- [Enable customers to manage their own
subscriptions](https://docs.stripe.com/recurring-payments#enable-customer-portal)
- [Migrate existing subscriptions to
Stripe](https://docs.stripe.com/recurring-payments#migrate-subscriptions)

## Stripe products for recurring payments

The following table describes which Stripe products support recurring payments.

ProductFeaturesUse casesPayment Links- No coding
- Customize branding
- One payment link for one or more products
- Mobile support for responsive web
- No website required; share link through SMS, email, or social media
- [Stripe Tax](https://docs.stripe.com/tax) support
- [Accept recurring
payments](https://docs.stripe.com/recurring-payments#accept-recurring-payments)
- [Enable customers to manage their own
subscriptions](https://docs.stripe.com/recurring-payments#enable-customer-portal)
- [Accept recurring
donations](https://docs.stripe.com/recurring-payments#recurring-donations)
Invoicing- No coding required. (You can optionally use the [Invoices
API](https://docs.stripe.com/api/invoices) and prebuilt components like Stripe
Checkout and Elements to build a programmatic invoicing integration.)
- Customize branding and templates.
- One invoice for one or more products. Optionally combine one-time and
recurring products.
- Mobile support for responsive web.
- No website required. Share invoices through customer portal, hosted invoice
page, or as PDFs.
- [Stripe Tax](https://docs.stripe.com/tax) support.
- [Accept recurring
payments](https://docs.stripe.com/recurring-payments#accept-recurring-payments)
- [Enable customers to manage their own
subscriptions](https://docs.stripe.com/recurring-payments#enable-customer-portal)
- [Accept recurring
donations](https://docs.stripe.com/recurring-payments#recurring-donations)
Subscriptions- No coding required. (You can optionally use the [Subscriptions
API](https://docs.stripe.com/api/subscriptions) and prebuilt components like
Stripe Checkout and Elements to build a programmatic subscriptions integration.)
- Customize full appearance of payment forms and checkout experience.
- Multiple products, prices, pricing models, and currencies.
- Mobile support for responsive web.
- No website required. You can also add subscriptions to your site.
- [Stripe Tax](https://docs.stripe.com/tax) support.
- [Accept recurring
payments](https://docs.stripe.com/recurring-payments#accept-recurring-payments)
- [Enable customers to manage their own
subscriptions](https://docs.stripe.com/recurring-payments#enable-customer-portal)
- [Accept recurring
donations](https://docs.stripe.com/recurring-payments#recurring-donations)
Checkout- Minimal coding
- Customize branding
- Multiple products and prices in different currencies
- Mobile support for responsive web
- Website required, but Stripe hosts the payment page
- [Stripe Tax](https://docs.stripe.com/tax) support
- [Accept recurring
payments](https://docs.stripe.com/recurring-payments#accept-recurring-payments)
- [Enable customers to manage their own
subscriptions](https://docs.stripe.com/recurring-payments#enable-customer-portal)
- [Split purchases into a few
payments](https://docs.stripe.com/recurring-payments#installment-plans)
- [Accept recurring
donations](https://docs.stripe.com/recurring-payments#recurring-donations)
Elements- More coding
- Customize full appearance
- Multiple products and prices in different currencies
- Responsive web and mobile native
- Website required; you add Elements to your payment page
- [Stripe Tax](https://docs.stripe.com/tax) supported with your own [tax
integration](https://docs.stripe.com/tax/custom)
- [Accept recurring
payments](https://docs.stripe.com/recurring-payments#accept-recurring-payments)
- [Enable customers to manage their own
subscriptions](https://docs.stripe.com/recurring-payments#enable-customer-portal)
- [Split purchases into a few
payments](https://docs.stripe.com/recurring-payments#installment-plans)
- [Accept recurring
donations](https://docs.stripe.com/recurring-payments#recurring-donations)
API- Most coding
- Customize full appearance, accept payments through your own UI
- Multiple products and prices in different currencies
- Website required; accept payments through your own UI
- [Stripe Tax](https://docs.stripe.com/tax) supported with your own [tax
integration](https://docs.stripe.com/tax/custom)
- [Accept recurring
payments](https://docs.stripe.com/recurring-payments#accept-recurring-payments)
- [Enable customers to manage their own
subscriptions](https://docs.stripe.com/recurring-payments#enable-customer-portal)
- [Split purchases into a few
payments](https://docs.stripe.com/recurring-payments#installment-plans)
- [Accept recurring
donations](https://docs.stripe.com/recurring-payments#recurring-donations)

## Accept recurring payments

Stripe offers several ways for you to accept recurring payments. Use
Subscriptions with Stripe Billing, PaymentIntents, SetupIntents, or Invoicing.

### Use subscriptions to accept recurring payments

### Save and reuse payment information for recurring charges

### Use invoices to automatically charge customers

## Split purchases into a few payments

Offer your customers payment plans in installments with [Subscription Schedules
API](https://docs.stripe.com/api/subscription_schedules) (part of Stripe
Billing) or buy now, pay later methods. If your business is based in Mexico, you
can offer card payments in installments.

### Create an installment plan with Subscription Schedules

### Use a buy now, pay later payment method

### Accept card payments in installments

## Enable customers to manage their own subscriptions

If you want your customers to manage their own accounts and recurring
subscriptions, use the customer portal. Stripe hosts the customer portal, which
allows your customers to self-manage their payment details, download invoices,
and manage their subscriptions in one place. Read the [no-code customer portal
guide](https://docs.stripe.com/customer-management/activate-no-code-customer-portal)
for complete details.

[Integrate with the customer portal
API](https://docs.stripe.com/customer-management/integrate-customer-portal)

### Set up the customer portal

See what your customers can do in the customer portal

[View demo](https://billing.stripe.com/customer-portal-demo)

## Accept recurring donations

You can accept recurring donations with Stripe, in the same way as recurring
payments. For example, you have a llama rescue organization, Llama House, and
want to allow supporters to choose an amount for a recurring, monthly donation.
You can use Payment Links to create a link to share on social media and email.
From the same payment link, you can also generate a QR code to add to flyers,
and an embeddable buy button for your website–all from the Dashboard.

### Accept recurring donations with Payment Links

## Migrate existing subscriptions to Stripe

If you have existing subscriptions in another system, you can migrate them to
Stripe Billing. Read [the
guide](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions) for
more information.

## See also

- [Get an overview of subscriptions](https://docs.stripe.com/billing)
- [Create a payment link](https://docs.stripe.com/payment-links/create)
- [Add an Apple Pay merchant token for recurring
payments](https://docs.stripe.com/apple-pay/merchant-tokens)
- [Get started with no-code
invoices](https://docs.stripe.com/invoicing/no-code-guide)
- [Save payment details during a payment to set up future
payments](https://docs.stripe.com/payments/save-during-payment)
- [Save card details to set up future
payments](https://docs.stripe.com/payments/save-and-reuse)

## Links

- [Accept recurring paymentsLet customers pay you regularly and repeatedly
through
Stripe.](https://docs.stripe.com/recurring-payments#accept-recurring-payments)
- [Split purchases into a few paymentsCreate installment plans to let customers
pay you a total amount in a limited number of partial
payments.](https://docs.stripe.com/recurring-payments#installment-plans)
- [Enable customers to manage their own subscriptionsSet up the customer portal
so your customers can create and manage their own
subscriptions.](https://docs.stripe.com/recurring-payments#enable-customer-portal)
- [Accept recurring donationsLet customers make donations to your organization
on a regular
basis.](https://docs.stripe.com/recurring-payments#recurring-donations)
- [Migrate existing subscriptions to StripeMove your existing subscriptions from
a third-party service to
Stripe.](https://docs.stripe.com/recurring-payments#migrate-subscriptions)
- [Stripe Billing](https://docs.stripe.com/billing)
- [Create a payment link with a recurring
product](https://docs.stripe.com/payment-links/create)
- [Dashboard](https://dashboard.stripe.com/subscriptions)
- [build a subscriptions
integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
- [subscription
schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
- [create subscriptions](https://docs.stripe.com/connect/subscriptions)
- [Stripe Tax](https://docs.stripe.com/tax)
- [Invoices API](https://docs.stripe.com/api/invoices)
- [Subscriptions API](https://docs.stripe.com/api/subscriptions)
- [tax integration](https://docs.stripe.com/tax/custom)
- [Subscription Schedules
API](https://docs.stripe.com/api/subscription_schedules)
- [no-code customer portal
guide](https://docs.stripe.com/customer-management/activate-no-code-customer-portal)
- [Integrate with the customer portal
API](https://docs.stripe.com/customer-management/integrate-customer-portal)
- [View demo](https://billing.stripe.com/customer-portal-demo)
- [the
guide](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions)
- [Add an Apple Pay merchant token for recurring
payments](https://docs.stripe.com/apple-pay/merchant-tokens)
- [Get started with no-code
invoices](https://docs.stripe.com/invoicing/no-code-guide)
- [Save payment details during a payment to set up future
payments](https://docs.stripe.com/payments/save-during-payment)
- [Save card details to set up future
payments](https://docs.stripe.com/payments/save-and-reuse)