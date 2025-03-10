# Map payment data

## Map payment data to existing Stripe Customers.

Our standard process creates new customers alongside the payment method data
from your previous provider. If you’ve been processing new transactions on
Stripe during the migration, you might already have some customers in Stripe.
Map imported payment data to these existing Stripe customers to avoid creating
duplicates.

After you submit the migration intake form, reply in the same email thread with
a CSV file that includes two columns:

- **old_customer_id**: The unique identifier from your former processor.
- **stripe_customer_id**: The corresponding Stripe customer ID in the `cus_xxxx`
format.

To download a list of customers with their Stripe IDs:

- Go to the Customers section in the [Stripe
Dashboard](https://dashboard.stripe.com/customers).
- Filter the list based on your desired parameters.
- Click **Export**.
- Select the `ID` field for export.
- Export your list.

## How it works

![Shows the migration mapping
process.](https://b.stripecdn.com/docs-statics-srv/assets/dm-mapping.5205a45bfb84e031c593db5525349ce2.jpg)

## Example mapping file

old_customer_idstripe_customer_id`PSP_buyer_ID_1``cus_NsKvEuOxdDP111``PSP_buyer_ID_2``cus_Nrt6IryCjAK222``PSP_buyer_ID_3``cus_OAiRfxde7Ya333`
## Customer data overwrite

Our current tooling preserves existing customer level data. Mapping doesn’t
overwrite any information already present in the customer’s record. Rather, it
appends data for any new cards that aren’t already included without altering the
customer level information displayed in the Dashboard. If the data file flags a
card as the default card, it overrides any previously set default cards in the
Dashboard.

## Links

- [Stripe Dashboard](https://dashboard.stripe.com/customers)