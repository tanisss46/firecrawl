# NetSuite invoice payment page

## Allow customers to use a Stripe payment flow to pay NetSuite invoices.

The Stripe Connector for NetSuite creates a payment page for each of your
NetSuite invoices. Customers can pay invoices using a Stripe payment flow, and
pay with any of the [payment
methods](https://dashboard.stripe.com/test/settings/payment_methods) that you
enable. Every accepted payment includes automated payment processing, cash
application, deposit automation, and fee calculation.

#### Note

You can also install the [free, self-serve
version](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/overview)
of the connector. This version allows you to accept payments with a Stripe
payment link, without syncing payments or other data to NetSuite.

## How it works

- When you create a NetSuite invoice, the payment page link is created and added
immediately. The payment page includes the following information:

- NetSuite invoice number
- NetSuite total amount due
- Payment methods based on the customer region
- Currency of the NetSuite invoice (if [supported by
Stripe](https://docs.stripe.com/currencies))
- Provide the invoice payment page link to your customer in a NetSuite invoice
email, invoice PDF template, a portal on your website, or another communication
method. The customer pays the full amount due on the NetSuite invoice.
- The connector syncs the payment into NetSuite and applies it against the
invoice.
- After the Stripe payout syncs as a bank deposit to NetSuite, the connector
reconciles the payment against the corresponding bank deposit, recording
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

NetSuite creates an invoice and automatically generates a payment page link

You send the payment link to your customer (automatically or manually)

The customer submits payment through Stripe Checkout

Stripe creates a payment

NetSuite syncs the customer payment and applies it to the original invoice

2 business days later, Stripe sends a payout to your bank account

NetSuite creates a deposit and moves the payment from the `Undeposited Funds`
account to a general ledger account

A high level overview of the invoice payment page flow
## Payment page details

Creating an invoice immediately creates a [Checkout payment
page](https://docs.stripe.com/payments/checkout) with a unique, secure URL
that’s single-use to prevent duplicate payments on the same invoice. You can
access this URL in the custom transaction body field.

The payment page only works for new invoices. If you want to use the payment
page with past invoices, contact your implementation partner for a script that
enables access to past invoices.

You can view payment information in the Stripe Dashboard, and a link to the
NetSuite customer payment in the metadata.

The customer’s payment method is only saved for future use if you select **Save
payment method to Stripe customers** on the connector’s **Control** tab, under
**NetSuite payment pages**. Saved payment methods are created under a new or
existing Stripe customer and linked to the NetSuite customer.

You can find the record sync and related record links in the [Stripe
Dashboard](https://dashboard.stripe.com/test/dashboard).

## Automate bank reconciliation

The payment page includes [deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation),
which automates the bank reconciliation process for all payments, refunds, and
disputes from a Stripe payout to a NetSuite bank deposit.

## Support multiple subsidiaries

The payment page is compatible with either single subsidiary (entity) or
multi-subsidiary (OneWorld) NetSuite accounts. You can enable the payment page
on any subsidiaries that have an individual Stripe Connector for NetSuite
connection within a multi-subsidiary account. The custom transaction body field
for the payment link applies to the NetSuite invoice forms.

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

You can use the payment page to save payment methods for future use. For
example, a connector add-on (such as Auto-Pay) might use the saved payment
method to charge a customer for future invoices. Stripe saves the payment method
to a new or existing [Customer](https://docs.stripe.com/api/customers) object.

#### Compliance

You’re responsible for your compliance with all applicable laws, regulations,
and network rules when saving a customer’s payment details. For example, if you
want to save a customer’s payment method for future use, you need their
agreement to be billed outside of the connector’s payment flow. Getting that
agreement up front allows you to save the payment details, and to charge the
customer for future invoices if needed.

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
NetSuite. For example, you might choose to map the payment page’s unique link to
a [Pay Now
button](https://support.stripe.com/questions/stripe-connector-for-netsuite-pay-now-button)
in your NetSuite email templates, invoice PDF templates, or manual outreach.

## Send email receipts for payments

You have two options for sending email receipts to your customers:

- Use Stripe to automatically send email receipts. To use this option, enable
**Successful payments** on the [Customer emails
settings](https://dashboard.stripe.com/settings/emails) page in the Stripe
Dashboard. By default, the payment page attaches the NetSuite customer email to
the payment created in the Checkout session. If no email exists, the Checkout
session prompts the customer to provide one during payment.
- Use NetSuite to send email receipts for payments. You must disable email
receipts in the Stripe Dashboard. Then, create a script or workflow to send
customized email receipts when the connector creates a customer payment in
NetSuite.

You can also [customize your
receipts](https://docs.stripe.com/receipts?payment-ui=payment-links#customizing-receipts).
To test email receipts, you need to manually trigger the receipts in the Stripe
Dashboard.

## Test the invoice payment page

You can test the NetSuite invoice payment page in Stripe test mode or the
NetSuite sandbox.

#### Note

If you’re experiencing issues despite a correct configuration, you can contact
your implementation partner during the post-live support period.

- In NetSuite, create an invoice for your use case. For example, an invoice with
the same types of line items and taxes that you use in production mode. The
invoice must have a balance greater than 0.50 for the payment page to populate.
- On the newly created invoice, verify that the invoice payment page field
appears. If it’s missing, go to the invoice form and make sure the field is
configured and applied to the appropriate forms.
- Click the customer payment page link to confirm it populates correctly. If it
doesn’t, verify that the default value is configured correctly in the custom
transaction body field for the page. For example,
`https://netsuite-connector.stripe.com/payment/[Stripe Account ID]/[“test” or
“live”]/invoice/[guid code_Internal ID]`.
- Make payments with various [test payment
methods](https://docs.stripe.com/testing) and payment scenarios.
- Click **Pay** and verify that the payment record is created in Stripe and
NetSuite. This typically occurs within 30 seconds. Look for the synced records
in the Stripe Connector for NetSuite app in the Stripe Dashboard.
- Accessing the customer payment page creates a Stripe customer object and
attaches it to the NetSuite customer. Verify this customer exists in the Stripe
Dashboard. If you chose to save payment methods, the connector saves the payment
method to the Stripe `Customer` object when the payment completes.
- Verify that the NetSuite customer payment was created and applied correctly by
checking the original invoice:

- The invoice status changes from `Open` to `Paid in Full`.
- The payment shows as `Undeposited`.
- The general ledger account shows as `Undeposited Funds`.

## See also

- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)
- [Deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
- [Refunds](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite)
-
[Disputes](https://docs.stripe.com/connectors/netsuite/stripe-disputes-netsuite)

## Links

- [Stripe App
Marketplace](https://marketplace.stripe.com/apps/netsuite-connector)
- [payment methods](https://dashboard.stripe.com/test/settings/payment_methods)
- [free, self-serve
version](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/overview)
- [supported by Stripe](https://docs.stripe.com/currencies)
- [deposit
automation](https://docs.stripe.com/connectors/netsuite/deposit-automation)
-
[Disputes](https://docs.stripe.com/connectors/netsuite/stripe-disputes-netsuite)
- [refunds](https://docs.stripe.com/connectors/netsuite/stripe-refunds-netsuite)
- [Checkout payment page](https://docs.stripe.com/payments/checkout)
- [Stripe Dashboard](https://dashboard.stripe.com/test/dashboard)
- [supported presentment
currencies](https://docs.stripe.com/currencies#presentment-currencies)
- [Payment methods](https://dashboard.stripe.com/settings/payment_methods)
- [payment methods](https://docs.stripe.com/payments/payment-methods/overview)
- [Customer](https://docs.stripe.com/api/customers)
- [Branding settings](https://dashboard.stripe.com/settings/branding)
- [Public details](https://dashboard.stripe.com/settings/public)
- [Pay Now
button](https://support.stripe.com/questions/stripe-connector-for-netsuite-pay-now-button)
- [Customer emails settings](https://dashboard.stripe.com/settings/emails)
- [customize your
receipts](https://docs.stripe.com/receipts?payment-ui=payment-links#customizing-receipts)
- [test payment methods](https://docs.stripe.com/testing)
- [Customer payment
page](https://docs.stripe.com/connectors/netsuite/customer-payment-page)