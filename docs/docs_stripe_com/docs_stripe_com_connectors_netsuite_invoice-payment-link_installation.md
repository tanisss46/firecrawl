# Install the NetSuite connector invoice payment link

## Learn how to self-serve onboard and set up the Stripe Connector for NetSuite payment link.

You can use the free, self-serve version of the Stripe Connector for NetSuite to
integrate Stripe payment links into your NetSuite Enterprise Resource Planning
(ERP) system and accept payments.

#### Full version

If you’re interested in learning more about the full [Stripe Connector for
NetSuite](https://docs.stripe.com/connectors/netsuite/overview), [install the
app](https://marketplace.stripe.com/apps/netsuite-connector) and request a demo.

## Before you begin

Make sure you have the following:

- A [Stripe account](https://docs.stripe.com/get-started/account)
- A NetSuite account
- Administrator or equivalent access to both accounts
- A clear understanding of the invoice creation process in NetSuite
[Obtain your Stripe account
ID](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation#stripe-account-id)
You must find and make a note of the Stripe account ID for each account you want
to connect. If you’re setting up multiple subsidiaries, repeat the following
steps for all accounts.

- In the Stripe Dashboard, go to the [Business
settings](https://dashboard.stripe.com/settings/account) page.
- On the **Account details** tab, copy the **Account ID**. This value is case
sensitive.
[Install the
app](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation#install-app)
In the Stripe App Marketplace, on the [Stripe Connector for
NetSuite](https://marketplace.stripe.com/apps/netsuite-connector) page, click
**Install app**.

If you need to set up multiple accounts, make sure you provide Stripe sales with
all of the account IDs you want to set up. You then need to install the app for
each account.

[Connect your Stripe and NetSuite
accounts](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation#connect-accounts)
Use token-based authentication to securely connect your Stripe and NetSuite
accounts.

To do so, log in to your NetSuite account and navigate to **Setup** >
**Company** > **Enabled Features**. On the **SuiteCloud** tab, enable the
following:

- SOAP web services
- Token-based authentication

Some services, like token-based authentication, can take a day to propagate when
enabled.

Install the `Stripe Token Based Authentication` bundle (ID 178262). Then, add
the `Stripe Limited Access` role created from the bundle to your preferred
employee. We recommend using a dedicated employee.

### Handle NetSuite subsidiaries

Do the following if you have subsidiaries in NetSuite, even if only one
subsidiary uses the payment link:

- Open the `Stripe Limited Access` role.
- For **Accessible Subsidiaries**, select **All Subsidiaries**.
- Enable **Allow Cross-Subsidiary Record Viewing**.
- Under **Permissions** > **Lists**, add View permissions for your subsidiaries.

### Obtain your NetSuite account ID

Log in to your NetSuite account, and navigate to **Setup** > **Company** >
**Company Information**. Make a note of your NetSuite account ID, which is case
sensitive.

### Create an access token

Navigate to **Setup** > **Users/Roles** > **Access Tokens**, and click **New**
to create an access token with the following values:

- Application name: Stripe Connector for NetSuite
- User: [employee record]
- Role: Stripe Limited Access
- Token name: Stripe Connector for NetSuite - [Main Contact], Stripe Limited
Access

When finished, click **Save**, but don’t close the window.

### Add a token to the NetSuite connector app

In the Stripe Dashboard, on the app dock, click the Stripe Connector for
NetSuite app icon.

On the **App Settings** page, under **NetSuite credentials**, enter the
following:

- NetSuite account ID
- Token ID
- Token secret
[Install and configure the payment link
field](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation#payment-link-field)-
In your NetSuite account, go to **Customization** > **SuiteBundler** > **Search
& Install Bundles**.
- Search for `449983` to find and install the `Stripe Invoice Payment Page`
bundle.
- After installation completes, navigate to **Customization** > **Lists,
Records, & Fields** > **Transaction Body Fields**.
- Edit the **Stripe payment page**, and then navigate to the **Validation &
Defaulting** tab.
- Update the **Default Value** field as follows:

- To install the payment link on *one NetSuite subsidiary*, edit the formula to
use your Stripe account ID in either test mode or live mode. For example:
`https://netsuite-connector.stripe.com/payment/acct_1M6zZFLzNi11nE9A/test/invoice/184BB28E2462B9ABE0630F192E0A1219_32590401`.
- To install the payment link on *two or more NetSuite subsidiaries* within a
OneWorld account, edit the formula to replace `acct_REPLACE_ME` with the dynamic
value `'||{subsidiary.custrecord_stripe_account_id}||'`. For example:
`https://netsuite-connector.stripe.com/payment/'||{subsidiary.custrecord_stripe_account_id}||'/test/invoice/`.

On a new browser tab in your NetSuite account, go to **Customization** >
**SuiteBundler** > **Search & Install Bundles**. Search for `218349` to find and
install the `Stripe Subsidiary Stripe Account ID` bundle. For each subsidiary
that you want to have use a payment link, edit its entity record to add the
Stripe account ID that corresponds to that subsidiary.
- On the invoice forms that you want to use to collect payment, add the `Stripe
Payment Page` and `Stripe Payment Page GUID` transaction body fields.
[Validate the payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation#validate-payment-link)
Create a NetSuite invoice, and make sure the payment link appears for **Stripe
Payment Page**.

Validate the payment link’s structure by copying the URL and checking the
following:

- The correct Stripe account ID is present.
- The correct mode is present: test or live.
- The URL matches this structure:
`/payment/acct_id/test/invoice/RandomString_InternalId`.
[Enable the
integration](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation#enable-integration)
In the [Stripe Dashboard](https://dashboard.stripe.com/dashboard), on the app
dock, click the Stripe Connector for NetSuite app icon.

On the **App Settings** page, under **Connection settings**, click **Turn on**
to enable the full integration.

Click the payment link URL on the NetSuite invoice you created to validate that
a Stripe Checkout page automatically creates to collect payment.

[OptionalFull
version](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation#full-version)
## See also

- [Stripe Connector for NetSuite invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/overview)
-
[Troubleshooting](https://docs.stripe.com/connectors/netsuite/error-resolution)

## Links

- [Stripe Connector for
NetSuite](https://docs.stripe.com/connectors/netsuite/overview)
- [install the app](https://marketplace.stripe.com/apps/netsuite-connector)
- [Stripe account](https://docs.stripe.com/get-started/account)
- [Business settings](https://dashboard.stripe.com/settings/account)
- [Stripe Dashboard](https://dashboard.stripe.com/dashboard)
- [Stripe Connector for NetSuite invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/overview)
-
[Troubleshooting](https://docs.stripe.com/connectors/netsuite/error-resolution)