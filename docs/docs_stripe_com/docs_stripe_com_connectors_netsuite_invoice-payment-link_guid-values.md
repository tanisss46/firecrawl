# Add GUID values to NetSuite invoices

## Learn how to add GUID values to NetSuite invoices that you created before setting up the payment link.

When you [install the
connector](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation)
with the payment page link, the installation includes a Stripe GUID field. The
GUID is a unique number that’s added to the URL link structure for each unique
payment link. Only invoices created after installation receive a GUID value.

The payment link won’t contain a GUID in the URL link structure in the following
cases:

- If you send an invoice created before installing the connector. In this case,
the payment page results in a “Page not found” error visible to your customer.
- If you create an invoice from a sales order created before installing the
connector. The sales order might be a subscription record for the NetSuite
billing engine, and resulting invoices won’t contain a GUID.

#### Note

If you need to update the GUID for invoices created from previously created
sales orders, ask your implementation partner to alter the workflow installed by
the bundle.

## Add a GUID value to NetSuite invoices in bulk

You can update invoices created before installing the connector to add a GUID
value to the existing GUID field, which makes the payment link available on
those invoices.

- In your NetSuite dashboard, use the global search tool to find `Search &
Install bundles`.
- Install the `[MHI] Invoice GUID Update` bundle (ID 494647). Myers-Holum Inc.
(MHI) is an approved Stripe partner and created this free bundle.
- After the installation completes, go to **Lists** > **Mass Update** > **Mass
Updates** in the NetSuite Center.
- Select **Workflows**, and use **Command+F** to search for `GUID`.
- Select **Initiate Update Invoice GUIDs**.
- On the Mass Update configuration page, do the following:

- Edit the **Title of Action** field to use a title that’s recognizable, for
example, `Stripe GUID update for invoice payment links`.
- Add the following criteria:

- **Main Line**: `is true`
- **Status**: `is Invoice:Open`
- **Subsidiary**: Select the desired subsidiary for the invoice payment page.
You can select multiple subsidiaries. For international accounts, you can add
criteria for the **Entity**.

You can add more criteria as needed. For example, if you have 50,000 open
invoices from previous years, you can add a criteria for the date, based on how
far back to collect payment for invoices.
- Click **Preview** to see the number of invoices selected.

Verify that you’re capturing the desired invoices to update. The update might
take a few hours, depending on the number of invoices.
- Click **Save** to start the bulk update.

To check on the progress of the update, click **Refresh**. The update continues
even if you navigate away from the progress page.
- After the update completes, you can use the invoice payment page link for each
invoice.

#### Note

If there are any errors, the progress page updates to display an error report
page. You can view the report for each invoice to learn more about the error.

## See also

- [NetSuite invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/overview)
- [Set up payment method
rules](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/payment-method-rules)

## Links

- [install the
connector](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/installation)
- [NetSuite invoice payment
link](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/overview)
- [Set up payment method
rules](https://docs.stripe.com/connectors/netsuite/invoice-payment-link/payment-method-rules)