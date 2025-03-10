# Stripe for Salesforce Platform configure events guide

Stripe for Salesforce Platform allows for the automatic creation of webhooks
inside of Stripe, and configures a listener for the Salesforce organization.
These webhooks become records that are captured as
[events](https://docs.stripe.com/api/events) for the [Customer
object](https://docs.stripe.com/api/customers).

- To configure **Stripe Events**, launch the Stripe Connector for Salesforce App
wizard, navigate to **App Launcher > Stripe Universal Connector for Salesforce**

!
- Select the **Stripe Account** to configure events on. 

!
- Click **All Webhook Events**. 

!
- Select the Stripe Object to enable events for by clicking on the **Stripe
Object** dropdown.

!
- Toggle the Events to listen for, and click **Save**.
- Login to the **Stripe Dashboard** for the account the events were enabled for.
- In the **Stripe Dashboard** Navigate to **Developers > Webhooks**. This will
show newly created **Hosted Endpoint**.

!

## Use Stripe Event DLM operations

Capture real-time Stripe Events via Webhooks and store them in the custom object
“Stripe Events” within Salesforce. Utilize standard Data Lifecycle Management
(DLM) triggers to automate interactions between Stripe and Salesforce,
leveraging record trigger flows and APEX triggers.

### Create a Salesforce flow trigger

To create a **record trigger** Salesforce flow for the **Stripe Events**,
complete the following steps:

- In Salesforce From Setup, in the Quick Find box, enter Flow, and then select
Flows.
- Click **New Flow**.
- Click **Record-Triggered Flow**, and then click Create. 

!
- For **Select Object** select **Stripe Event**(stripeGC__Stripe_Event__c). 

!
- Under **Set Entry Conditions** use stripeGC__Event_Name__c to define what
event from Stripe this Salesforce Flow is for. Stripe Event Name
**customer.created** is used for this example.

!
- Click **Done**. The **Stripe Connector for Salesforce Platform** has **cast
to** flow actions. These actions are part of the package in Salesforce.

## Stripe Events Object and Location

This Salesforce package comes with a Stripe Events custom object in order to
capture Stripe webhooks. The Stripe Events object tab is found by navigating to
**App Launcher > Stripe for Salesforce Platform Lightning app**. **Example
Stripe Event Object**

!

## See also

-
[Enablement](https://docs.stripe.com/connectors/stripe-connector-for-salesforce/enablement)
- [Installation
guide](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/installation-guide)

## Links

- [events](https://docs.stripe.com/api/events)
- [Customer object](https://docs.stripe.com/api/customers)
-
[Enablement](https://docs.stripe.com/connectors/stripe-connector-for-salesforce/enablement)
- [Installation
guide](https://docs.stripe.com/plugins/stripe-connector-for-salesforce/installation-guide)