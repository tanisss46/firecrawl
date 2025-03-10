# Set up the Stripe Billing Connector for Salesforce CPQ

## Configure and use the connector.

The Stripe Billing Connector for Salesforce CPQ syncs your products, prices,
accounts, and orders from Salesforce to Stripe Billing. After you set up the
connector and create data mappings, the service syncs this information from
Salesforce and completes the collection and provisioning workflows in Stripe
Billing.

[Install the
connector](https://docs.stripe.com/connectors/salesforce-cpq/setup#install-connector)
The connector is a managed package that you install from the [Salesforce
AppExchange](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000FOm4xUAD)
onto your Salesforce account.

During the installation process, choose **Install for Admins Only**. Follow the
on-screen prompts and approve third-party access. In Salesforce, search for
“Stripe Billing Connector” to continue the setup process.

In the Stripe Billing Connector, follow the on-screen steps to:

- Authorize access between your Salesforce environment and your Stripe account.
- Define how data maps between Salesforce and Stripe.
- Configure synchronization preferences.
[Define how data maps between Salesforce and
Stripe](https://docs.stripe.com/connectors/salesforce-cpq/setup#data-map)
Use the **Define Data Mapping** step to map the fields from the Salesforce
objects to corresponding fields on the Stripe objects. For example, for a custom
field that stores whether a price book entry is metered or licensed, specify
that field to map to
[recurring.usage_type](https://docs.stripe.com/api/prices/object#price_object-recurring-usage_type)
on the Stripe `Price` object.

The connector automatically maps the following Salesforce objects to the
corresponding Stripe objects:

Salesforce objectStripe
objectProduct2[Product](https://docs.stripe.com/api/products/object)Price book
entry[Price](https://docs.stripe.com/api/prices/object)Account[Customer](https://docs.stripe.com/api/customers/object)Order[Subscription
Schedule](https://docs.stripe.com/api/subscription_schedules/object) and
[Subscription](https://docs.stripe.com/api/subscriptions/object)Order
product[Subscription
Item](https://docs.stripe.com/api/subscription_items/object)
You can also map information within Salesforce objects or to metadata fields
within corresponding Stripe objects by [defining field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings).

[Configure synchronization
preferences](https://docs.stripe.com/connectors/salesforce-cpq/setup#preferences)
Use the **Configure Sync Preferences** step to specify:

- **Sync record retention**: The number of sync records retained in Salesforce.
- **Start date**: After you [enable live
syncing](https://docs.stripe.com/connectors/salesforce-cpq/setup#activate-syncing),
the connector begins to sync data for activated orders to Stripe on or after
this date. You can specify a date in the past.
- **Sync filters**: Adds filters to determine when to sync Salesforce orders,
accounts, products, and pricebook entries. By default, the connector syncs
orders when `Status = Activated`, but you can customize this behavior for your
workflows.

After setup completes and you [activate live
syncing](https://docs.stripe.com/connectors/salesforce-cpq/setup#activate-syncing)
for your integration, newly activated orders automatically:

- Create or update a `Customer` object in Stripe for the account that
corresponds to the order. The `id` on the Stripe customer is available as a
custom field called `Stripe ID` on the Salesforce account.
- Create or update products and prices in Stripe for each product in the order.
- Create a subscription schedule in Stripe for the activated order.
- Create a `Sync Record` custom object in Salesforce to indicate the sync status
and any errors that arise.

### Sync limitations

- **Refunds**: Use the Stripe Dashboard link on the Salesforce object to issue
refunds through Stripe.
- **Payment and subscription status**: Use the Stripe Dashboard link to see an
order’s subscription status, payment information, and related invoices.
- **Taxes**: Tax information isn’t synced between Salesforce and Stripe. To
collect taxes on an invoice, use [Stripe Tax](https://docs.stripe.com/tax) to
automatically calculate and apply taxes to the subscription or Stripe invoice
for an order.
[Activate live
syncing](https://docs.stripe.com/connectors/salesforce-cpq/setup#activate-syncing)
In the final step of the post-installation flow, you can enable live syncing
now, or enable it later. Live syncing allows your integration to pull activated
Salesforce orders into Stripe in real time. You can enable or disable live
syncing of orders any time on the **Sync Preferences** tab of the application.

You can manually sync individual orders to test your integration, even when live
syncing is disabled.

[OptionalImplement custom
workflows](https://docs.stripe.com/connectors/salesforce-cpq/setup#custom-workflows)[OptionalAdd
custom fields to page
layouts](https://docs.stripe.com/connectors/salesforce-cpq/setup#page-layouts)[OptionalManage
permissions](https://docs.stripe.com/connectors/salesforce-cpq/setup#manage-permissions)
## See also

- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Accounts and
contacts](https://docs.stripe.com/connectors/salesforce-cpq/accounts-contacts)
- [Products and
prices](https://docs.stripe.com/connectors/salesforce-cpq/products-prices)

## Links

- [Salesforce
AppExchange](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000FOm4xUAD)
-
[recurring.usage_type](https://docs.stripe.com/api/prices/object#price_object-recurring-usage_type)
- [Product](https://docs.stripe.com/api/products/object)
- [Price](https://docs.stripe.com/api/prices/object)
- [Customer](https://docs.stripe.com/api/customers/object)
- [Subscription
Schedule](https://docs.stripe.com/api/subscription_schedules/object)
- [Subscription](https://docs.stripe.com/api/subscriptions/object)
- [Subscription Item](https://docs.stripe.com/api/subscription_items/object)
- [defining field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Stripe Tax](https://docs.stripe.com/tax)
- [Accounts and
contacts](https://docs.stripe.com/connectors/salesforce-cpq/accounts-contacts)
- [Products and
prices](https://docs.stripe.com/connectors/salesforce-cpq/products-prices)