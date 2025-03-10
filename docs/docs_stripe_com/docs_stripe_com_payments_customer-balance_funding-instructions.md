# Funding instructions

## Provide customer balance funding instructions without creating a PaymentIntent.

You can show bank account details to your customer before they make their first
payment through the Dashboard or API.

## Create or retrieve funding instructions

DashboardAPI
### Create funding instructions

To create funding instructions for your customers:

- Navigate to the [customer’s page](https://dashboard.stripe.com/customers).
- Under **Payment methods**, click **+** > **Add a bank transfer account**.
- Select the currency and country you want to create a bank transfer account
for, then click **Add**. Stripe creates a cash balance with the appropriate
currency for your customer.

### Retrieve funding instructions

- Navigate to the [customer’s page](https://dashboard.stripe.com/customers).
- Under **Payment methods**, select the cash balance with the relevant currency,
then click **View balance details**.
- Review the **Bank transfer funding instructions**.

## Download confirmation of account ownership

Some customers might request additional assurance that the account they’re
transferring money into is yours, because the account might be listed as owned
by Stripe. To provide this assurance, you can generate a letter confirming your
ownership of the account to the customer. In this letter, Stripe confirms that
you’re the owner of the virtual bank account corresponding to the account
details you have passed to that customer.

To download a letter confirming account ownership:

- Navigate to the [Customers page](https://dashboard.stripe.com/customers) in
the Dashboard.
- Select the customer who has requested additional verification that you own the
account.
- Navigate to their cash balance details. This page shows the account details
that the customer must use to pay you by bank transfer.
- Click the button to download a confirmation letter in a PDF format with
today’s date.

![Button to download confirmation of account
ownership](https://b.stripecdn.com/docs-statics-srv/assets/vban-confirmation-letter-button.cfd3f902e44069f96d011b7fb8cba336.png)

Download confirmation of account ownership

## Links

- [customer’s page](https://dashboard.stripe.com/customers)