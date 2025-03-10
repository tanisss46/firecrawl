# NetSuite customer payment page

## Allow customers to make payments toward their NetSuite balance using Stripe.

Use the customer payment page to collect payments that you can then apply to
multiple invoices as partial payments, or to support other payment applications
beyond single invoices. The Stripe Connector for NetSuite automatically sets the
amount due on your NetSuite customer payment page to the NetSuite customer
balance total. But the connector allows customers to modify the amount they pay
to any amount, up to the outstanding balance amount. Every accepted payment
includes automated payment processing, deposit automation, and fee calculation.

You can enable the [payment
methods](https://dashboard.stripe.com/test/settings/payment_methods) available
to your customers in your Stripe account.

A customer payment gets created and associated with the NetSuite customer. You
can also designate how you want to apply payments, based on your business needs.
For example, you can automate the payment application to specific invoices using
native NetSuite settings, a custom workflow, or a custom SuiteScript.

## How it works

- When you create a NetSuite customer, it creates the payment page link and adds
it immediately. The payment page includes the following information:

- NetSuite customer name
- NetSuite total outstanding balance
- Payment methods based on the customer region
- Currency used in NetSuite (if [supported by
Stripe](https://docs.stripe.com/currencies))
- Provide the customer payment page link to your customer in a NetSuite invoice
email, invoice PDF template, a portal on your website, or another communication
method. The customer accesses the payment page and can pay any amount up to the
full customer balance.
- The connector syncs the payment into NetSuite and creates an unapplied payment
that’s associated with the NetSuite customer.
- In NetSuite, you can use the auto-apply feature to apply payments to the
oldest open invoices, until the total amount of the payment is used. The
connector can automatically enable NetSuite auto-apply to the payment from the
customer payment page.
- After the Stripe payout syncs as a bank deposit to NetSuite, the connector
reconciles the payment against the corresponding bank deposit, and records
processing fees and any currency conversion. This workflow is called [deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation).
[Disputes](https://docs.stripe.com/connectors/netsuite/stripe-disputes-netsuite)
and
[refunds](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite)
sync to NetSuite automatically.

NetSuite

Business

Customer

Stripe

NetSuite creates invoice and automatically generates payment page link

You send the payment link to your customer (automatically or manually)

Customer submits payment through Stripe Checkout

Stripe creates payment

NetSuite syncs customer payment as an unapplied payment

Two business days later, Stripe sends payout to your bank account

NetSuite creates deposit and moves payment from Undeposited Funds account to
general ledger account

A diagram providing a high level overview of the customer payment page flow
outlined in this doc
## Customer payment page details

Creating an invoice immediately creates a [Checkout payment
page](https://docs.stripe.com/payments/checkout) with a unique, secure URL. You
can access this URL in the customer payment page field
(`custentity_customer_payment_page_link`).

If you implement the payment page for an existing NetSuite customer, the payment
page uses the customer record creation date. If you implement the payment page
for a new NetSuite customer, the payment page uses a randomly-generated GUID
(`custentity_customer_payment_page_guid`).

If there’s a remaining balance greater than 0.50 after the customer makes a
payment, the payment page remains reusable for 24 hours.

You can configure the connector to use auto-apply by adding the following to the
**Field mappings** in the app settings:

```
{
 "customer_payment":{
 "metadata.netsuite_auto_apply": "auto-apply"
 }
}

```

The customer’s payment method is only saved for future use if you select **Save
payment method to Stripe customers** on the connector’s **Control** tab, under
**NetSuite payment pages**. Saved payment methods are created under a new or
existing Stripe customer and linked to the NetSuite customer.

You can find the record sync and related record links in the Stripe Connector
for NetSuite app dashboard.

## Automate bank reconciliation

The payment page includes [deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation),
which automates the bank reconciliation process for all payments, refunds, and
disputes from a Stripe payout to a NetSuite bank deposit.

## Support multiple currencies and payment methods

Accept payments in the [supported presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies) in your
region. The payment page displays the currency that’s specified on the NetSuite
invoice. Stripe then creates a payment based on that currency.

You can enable the payment methods you want to accept on the [Payment
methods](https://dashboard.stripe.com/settings/payment_methods) page. Stripe
supports many categories of [payment
methods](https://docs.stripe.com/payments/payment-methods/overview) based on
your region and business needs.

## Save payment methods for future use

You can use the payment page to save a payment method for future use if needed.
For example, a connector add-on (such as Auto-Pay) might use the saved payment
method to charge a customer for future invoices. Stripe saves the payment method
to a new or existing [Customer](https://docs.stripe.com/api/customers) object.

#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. For example, if you
want to save a payment method for future use, you need their agreement to be
billed outside of the connector’s payment flow. Getting that agreement up front
allows you to save their payment details, and potentially charge them for future
invoices if needed.

If you plan to charge the customer while they’re offline, make sure that your
terms also cover the following, at minimum:

- The customer’s agreement to your initiating a payment or a series of payments
on their behalf for specified transactions.
- The anticipated timing and frequency of payments (for example, whether charges
are for scheduled installment or subscription payments, or for unscheduled
top-ups).
- How the payment amount is determined.
- Your cancellation policy, if you’re setting up the payment method for a
subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

## Customize the payment page

You can customize the look and feel of the payment page to match the design of
your site. Modify the payment page color and design on the [Branding
settings](https://dashboard.stripe.com/settings/branding) page in the Stripe
Dashboard. Modify your name and statement descriptor on the [Public
details](https://dashboard.stripe.com/settings/public) page.

## Add the payment page to your communications

You can integrate the payment page into your customer communications in
NetSuite. For example, you might want to map the payment page’s unique link to a
[Pay
Now](https://support.stripe.com/questions/stripe-connector-for-netsuite-pay-now-button)
button in your NetSuite email templates, invoice PDF templates, or manual
outreach.

## Send email receipts for payments

You have two options for sending email receipts to your customers:

- Use Stripe to automatically send email receipts. The connector provides the
invoice ID and NetSuite customer email. To use this option, enable **Successful
payments** on the [Customer emails
settings](https://dashboard.stripe.com/settings/emails) page in the Stripe
Dashboard.
- Use NetSuite to send email receipts for payments. You must disable email
receipts in the Stripe Dashboard and then set up a workflow to send customized
email receipts from NetSuite.

## See also

- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)
- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Refunds](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite)
-
[Disputes](https://docs.stripe.com/connectors/netsuite/stripe-disputes-netsuite)

## Links

- [Stripe App
Marketplace](https://marketplace.stripe.com/apps/netsuite-connector)
- [payment methods](https://dashboard.stripe.com/test/settings/payment_methods)
- [supported by Stripe](https://docs.stripe.com/currencies)
- [deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
-
[Disputes](https://docs.stripe.com/connectors/netsuite/stripe-disputes-netsuite)
- [refunds](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite)
- [Checkout payment page](https://docs.stripe.com/payments/checkout)
- [supported presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies)
- [Payment methods](https://dashboard.stripe.com/settings/payment_methods)
- [payment methods](https://docs.stripe.com/payments/payment-methods/overview)
- [Customer](https://docs.stripe.com/api/customers)
- [Branding settings](https://dashboard.stripe.com/settings/branding)
- [Public details](https://dashboard.stripe.com/settings/public)
- [Pay
Now](https://support.stripe.com/questions/stripe-connector-for-netsuite-pay-now-button)
- [Customer emails settings](https://dashboard.stripe.com/settings/emails)
- [Invoice payment
page](https://docs.stripe.com/connectors/netsuite/invoice-payment-page)