# Record usage in the Dashboard

## Learn how to record your customer's usage in the Dashboard manually or using a CSV file.

You must record usage in Stripe to bill your customers the correct amounts each
billing period. To record usage, you can manually add usage data or upload a CSV
file with the usage data in the Dashboard. Stripe parses, validates, and
transforms the usage data into meter events.

After the events upload successfully, you can see them in the live meter feed.
You can also check the status of your uploaded files on the [Data
management](https://dashboard.stripe.com/data-management/import-set) page.

## Add usage data manually

You can manually add usage data on the
[Meters](https://dashboard.stripe.com/test/meters) page in the Stripe Dashboard.

- On the [Meters](https://dashboard.stripe.com/test/meters) page, select the
meter name.
- On the meter page, click **Add usage** > **Manually input usage**.
- On the **Add usage** page, do the following:- Select your customer from the
**Customer** dropdown.
- For **Value**, enter a sample value.
- Click **Submit**.

## Upload a CSV file with usage data

After you prepare your CSV file with the usage data, you can upload it in the
Stripe Dashboard. Make sure to format your file to match the template that’s
available in the Dashboard. The maximum file size allowed is 5 MB.

### CSV file format and fields

Make sure your CSV file follows this sample file format:

`timestamp``event_name``payload_stripe_customer_id``payload_value`2024-09-25ai_search_apicus_QMJJtcu70R1x464002024-09-26ai_search_apicus_GAXJtSu6021a6s6002024-09-27cpu_usagecus_Qz0fwcfSysB9Z3600
Follow the [Meter Event](https://docs.stripe.com/api/billing/meter-event/object)
schema when including the following fields in your file:

FieldDescription
`timestamp`

The date that the event occurred. We support the following timestamp formats:

- `yyyy-MM-dd` – For example, `2024-09-23`.
- `yyyy-MM-dd'T'HH:mm:ssZ` – For example, `2024-09-23T16:22:25+0530`.
- `Epoch` – For example, `1727108545`.
`event_name`The name of the meter event.`payload_stripe_customer_id`The
[Customer ID](https://docs.stripe.com/api/customers/object#customer_object-id)
that the event gets created against. You can obtain the `customer_id` details on
the [Customers](https://dashboard.stripe.com/customers) page.`payload_value`The
numerical usage value of the meter event, such as the number of hours to invoice
for. If you specified a different key in the `value_settings`, you must update
the column name to match the key value. For example, if you specify `tokens` in
the `value_settings`, update the column name to `payload_tokens`.
### Upload your CSV file

If your file contains errors, you can download an error file that includes the
reason for each failed record. After you fix the errors, you can upload the
updated file.

- On the [Meters](https://dashboard.stripe.com/meters) page, select the meter
name that you want to add usage events to.
- On the meter page, click **Add usage** > **Upload file to add usage**.
- On the **Upload file to add usage** page, select your file.
- Click **Upload file**.
- Verify the meter event count and aggregated value on the meter page.

## Links

- [Data management](https://dashboard.stripe.com/data-management/import-set)
- [Meters](https://dashboard.stripe.com/test/meters)
- [Meter Event](https://docs.stripe.com/api/billing/meter-event/object)
- [Customer ID](https://docs.stripe.com/api/customers/object#customer_object-id)
- [Customers](https://dashboard.stripe.com/customers)
- [Meters](https://dashboard.stripe.com/meters)