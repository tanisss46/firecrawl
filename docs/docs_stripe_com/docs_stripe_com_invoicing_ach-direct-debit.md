# Invoicing and ACH Direct Debit

## Configure, create, and process invoices using ACH Direct Debit.

To reduce costs, many merchants make card payment methods unavailable above a
certain [invoice](https://docs.stripe.com/api/invoices) total amount, and prefer
payment from bank methods like ACH Direct Debit.

This guide provides step-by-step instructions on how to configure, create, and
process invoices to use the [ACH Direct
Debit](https://docs.stripe.com/payments/ach-direct-debit) payment method. Stripe
users in the United States can accept **ACH Direct Debit** from end customers
with US bank accounts using the Automated Clearing House (ACH) payments system
operated by [Nacha](https://www.nacha.org/content/ach-network). A
[Connect](https://docs.stripe.com/connect) platform that integrates ACH Direct
Debit has more [advanced options
available](https://docs.stripe.com/invoicing/ach-direct-debit#fee-splitting). To
begin, determine whether:

- Your customers [enter bank account
information](https://docs.stripe.com/invoicing/ach-direct-debit#default-payment-method)
to pay their invoices.
- You [collect and verify bank account information
upfront](https://docs.stripe.com/invoicing/ach-direct-debit#precollected-bank-information)
and automatically process invoices.

#### Note

If you give a customer an invoice link to pay a one-off invoice, Stripe
automatically saves their bank information allowing reuse on future invoices.
You can also add the bank customer’s information directly through the customer
details page.

## Set up ACH Direct Debit

You can either set ACH Direct Debit as a default payment method, or add it when
you [create an
invoice](https://docs.stripe.com/invoicing/dashboard#create-invoice).

DashboardAPI
To set ACH Direct Debit as a default payment method type:

- On the [Billing
settings](https://dashboard.stripe.com/settings/billing/invoice) page, under
**Invoicing settings** > **Default payment methods**, click **Edit payment
methods**.
- On the **Billing Payments** page, under **Bank debits**, click **Turn on** to
enable **ACH Direct Debit** as a default payment method.

Your customers can pay an invoice by using the [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page) to enter their bank
account information or select the default payment method. If there isn’t a
default payment method, the invoice includes all available payment methods.

## Pre-collected bank information

You can collect bank account information for future payments with **ACH Direct
Debit**. After you add a customer’s ACH details, they must verify their payment
information with microdeposits, which can take up to 2 days.

DashboardAPI
To pre-collect a customer’s bank information:

- On the [Customers](https://dashboard.stripe.com/customers) page, select a
customer name.
- On the customer page, under **Payment methods**, click the plus (**+**)
symbol, and select **Add US bank account**.
- On the **Add a US bank account** page, enter the payment details, and click
**Add US bank account**.
- After verification, click the overflow menu () next to the payment method, and
select **Set as default**.

Whenever you create a new invoice for your customer, select **Charge
immediately** to automatically charge the default payment method on file. For a
finalized invoice, you can also click **Charge customer** on the invoice details
page, and select the saved ACH Direct Debit payment method to initiate the
transaction.

## Payment completions

For any invoice with ACH Direct Debit enabled as a payment method, your customer
can enter their bank account information on the Hosted Invoice Page to start a
debit payment.

Your customer must do the following to complete payment:

- On the Hosted Invoice Page, select **US bank account**.
- Search for and select the bank.
- Initiate login with the bank and agree to the terms of service.
- Select the bank account and click **Connect account**.
- After successfully connecting the account, click **Back** to go to the
invoice.
- Click **Pay** and agree to the terms of service.

## Enhanced fee splitting Connect

Payment methods (such as credit and debit cards) have a fixed percentage charged
over the whole amount. But low cost payment methods (such as **ACH Direct
Debit**) are usually capped. For platforms looking to dynamically reflect this
fee arrangement to their businesses, Stripe recommends that you separate your
charges and transfers (as opposed to using the basic `application_fee_amount`
parameter). With separate charges and transfers, your platform can transfer the
business’ share of funds minus the appropriate fee amount based on the payment
method type.

## Test the integration

You can test customer bank account entry through instant verification or
microdeposits.

### Instant verification

You can instantly verify a bank account in test mode. Refresh the page to view
the paid invoice.

- Create an invoice in test mode.
- Under **Payment collection**, select **Request payment in full** > **Manage
payment methods**.
- In the **Payment methods for this invoice** dialog, enable **ACH direct
debit**, and click **Save**.
- Enter the invoice details, and click **Send invoice**.
- On the invoice details page, under **Details**, click the **Payment page**
link.
- On the Hosted Invoice Page, select **US bank account** > **Test Institution**.
- Initiate login with the bank and agree to the terms of service.
- Select the bank account and click **Connect account**.
- After successfully connecting the account, click **Back** to go to the
invoice.
- Click **Pay** and agree to the terms of service.

### Microdeposits

You can manually verify bank accounts using microdeposits. In live mode, it
takes several days for the transaction to complete. But in test mode, the
transaction clears immediately and the invoice is paid.

- Create an invoice in test mode.
- Under **Payment collection**, select **Request payment in full** > **Manage
payment methods**.
- In the **Payment methods for this invoice** dialog, enable **ACH Direct
Debit**, and click **Save**.
- Enter the invoice details, and click **Send invoice**.
- On the invoice details page, under **Details**, click the **Payment page**
link.
- On the Hosted Invoice Page, select **US bank account**, and then click
**Pay**.
- Click **Enter bank details manually instead** to verify the bank account with
microdeposits.
- In the **Enter bank details** dialog, click **Use test account** to use a
[test routing number and bank
account](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment#test-account-numbers).
- After successfully adding the account, click **Back** to go to the invoice.

Next, finish initiating microdeposits in your Stripe account. You can expect an
email with instructions within 1-2 business days.

## See also

- [Payment methods](https://docs.stripe.com/invoicing/payment-methods)
- [Hosted invoice page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Invoicing API](https://docs.stripe.com/api/invoices)

## Links

- [invoice](https://docs.stripe.com/api/invoices)
- [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit)
- [Nacha](https://www.nacha.org/content/ach-network)
- [Connect](https://docs.stripe.com/connect)
- [create an
invoice](https://docs.stripe.com/invoicing/dashboard#create-invoice)
- [Billing settings](https://dashboard.stripe.com/settings/billing/invoice)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Customers](https://dashboard.stripe.com/customers)
- [test routing number and bank
account](https://docs.stripe.com/payments/ach-direct-debit/accept-a-payment#test-account-numbers)
- [Payment methods](https://docs.stripe.com/invoicing/payment-methods)