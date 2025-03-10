# Stripe for Salesforce Platform Configuration

## Switch Stripe account authentication from OAuth to API key

As of version 1.17 of the Stripe for Salesforce Platform, we no longer offer
OAuth-based authentication. To migrate your Stripe account from OAuth to use an
API key, follow these steps:

- From the Salesforce **Setup** tab, go to **App Launcher > Stripe for
Salesforce Platform**.
- In **Account Management**, click on the Stripe account you want to migrate.

!
- Click **Reauthorize using API key**.

!
- Input the Stripe API Key for this account, ensuring that the API key is for
the right mode (live or test). Click **Save**.

## Work with Sandboxes and environment clones

When creating a sandbox or copying production data, ensure the Stripe for
Salesforce Platform omits select data from the clone. Don’t copy connections and
configurations from production or other environments. Use sandbox templates that
don’t include any `stripeGC` objects.

Configure the Stripe for Salesforce Platform independently on each Salesforce
Org and run the setup process on each Salesforce Org.

!

## Remove data copied to a clone

When you copy data from the StripeGC objects to a new Salesforce Org, remove the
data by running an `Anonymous Apex` script to delete it:

```
delete [SELECT Id FROM stripeGC__Setup_Data__c];
delete [SELECT Id FROM stripeGC__Stripe_Account__c];
delete [SELECT Id FROM stripeGC__Stripe_Event__c];
delete [SELECT Id FROM stripeGC__Stripe_Webhook_Endpoint__c];
delete [SELECT Id FROM stripeGC__Sync_Log__c];
```

## Default Events excluded from recursion detection

Stripe’s Salesforce Platform has checks to prevent actions from getting stuck in
a loop. A logical loop might happen when a set of resources constantly detects
and responds to updates from another set. For example, suppose you have one flow
that listens to Stripe’s `customer.updated` events and updates a Salesforce
`Account`. Meanwhile, you have another flow that detects updates to the
Salesforce `Account` and updates a Stripe customer. This setup leads to a
recurring loop, which would continue indefinitely.

charge.capturedcharge.expiredcharge.failedcharge.pendingcharge.refundedcharge.succeededcharge.updatedcredit_note.createdcredit_note.updatedcredit_note.voidedinvoice.createdinvoice.deletedinvoice.finalization_failedInvoice.finalizedinvoice.marked_uncollectibleinvoice.paidinvoice.payment_action_requiredinvoice.payment_failedinvoice.payment_succeededinvoice.sentinvoice.upcominginvoice.updatedinvoice.voidedinvoiceitem.createdinvoiceitem.deletedinvoiceitem.updatedissuing_card.createdissuing_card.updatedissuing_cardholder.createdissuing_cardholder.updatedissuing_dispute.closedissuing_dispute.createdissuing_dispute.funds_reinstatedissuing_dispute.submittedissuing_dispute.updatedissuing_transaction.createdissuing_transaction.updatedmandate.updatedorder.createdorder.payment_failedorder.payment_succeededorder.updatedpayment_intent.amount_capturable_updatedpayment_intent.canceledpayment_intent.createdpayment_intent.partially_fundedpayment_intent.payment_failedpayment_intent.processingpayment_intent.requires_actionpayment_intent.succeededpayment_link.createdpayment_link.updatedpayment_method.attachedpayment_method.automatically_updatedpayment_method.detachedpayment_method.updatedpayout.canceledpayout.createdpayout.failedpayout.paidpayout.updatedquote.acceptedquote.canceledquote.createdquote.finalizedsetup_intent.canceledsetup_intent.createdsetup_intent.requires_actionsetup_intent.setup_failedsetup_intent.succeededcustomer.source.createdcustomer.source.deletedcustomer.source.expiringcustomer.source.updatedsource.canceledsource.chargeablesource.failedsource.mandate_notificationsource.refund_attributes_required
### Recursion detection configuration

You can include and exclude specific events from recursion detection. If you’re
an admin, you can modify these events in your settings by configuring recursion
detection.

The **Recursion Detection Configuration** can be accessed by following these
steps:

- Navigate to **Setup** > **Custom Code** > **Custom Metadata Types**.
- Under **Recursion Detection Configuration**, click **Manage Records**.
- Next to **Default**, click **Edit**.

Within this configuration, an admin can add either **Included Events** or
**Excluded Events**.

## Configure sync preferences

- To configure **Sync Preferences**, launch the Stripe Connector for Salesforce
App wizard, navigate to **App Launcher > Stripe Universal Connector for
Salesforce**

!
- Click the **Sync Preferences** button.
- Enable or disable **Enable Stripe Event Data Cleanup**.
- Modify the **Maximum Stripe Event Records Retained (Count)**.
- Enable or disable **Sync Log Records**.
- Modify the **Maximum Sync Log Records Retained (Count)**.

## See also

-
[Enablement](https://docs.stripe.com/connectors/stripe-connector-for-salesforce/enablement)
- [Installation
guide](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/installation-guide)

## Links

-
[Enablement](https://docs.stripe.com/connectors/stripe-connector-for-salesforce/enablement)
- [Installation
guide](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/installation-guide)