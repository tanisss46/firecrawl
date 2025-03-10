# Navigate the Stripe Tax Dashboard

## Manage your tax registrations in the Dashboard.

The Stripe Tax Dashboard consists of the following tabs:

- **Thresholds**
- **Registrations**

#### Note

To manage your Tax settings, see [Tax
Settings](https://dashboard.stripe.com/settings/tax).

## Thresholds

Stripe Tax provides insights about your potential tax registration obligations
(called economic nexus in the US). We help you understand which state or country
you might have such obligations in, even if your business doesn’t have a
physical presence there.

We group your registration obligations into the following categories:

- Exceeded: Your estimated sales or transactions exceed the location’s
registration threshold, and your business likely needs to register for tax. You
can [use Stripe to
register](https://docs.stripe.com/tax/use-stripe-to-register).
- Upcoming: Your estimated sales or transactions exceed 85% of the location’s
threshold. We expect you to exceed the threshold soon.
- Monitoring: We’re actively monitoring your obligations for the location and
will let you know when you’re approaching its threshold.
- Not monitoring: We aren’t monitoring your obligations in the location. This is
because either:- Your [preset product tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#product-tax-code)
is non-taxable in the location.
- We only support monitoring [digital
products](https://docs.stripe.com/tax/tax-codes?type=digital) there, and your
[preset product tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#product-tax-code)
is non-digital. For more details, see the [countries supported by Stripe
Tax](https://docs.stripe.com/tax/supported-countries).
- Undetermined: For [marketplace
facilitators](https://docs.stripe.com/tax/tax-for-marketplaces), we support
monitoring only in the UK, US, and EU. In the UK and EU, we support monitoring
only for [digital products](https://docs.stripe.com/tax/tax-codes?type=digital).

When Stripe Tax can’t determine the location for a transaction, we group its
information into an **Unattributed revenue** category. Where possible, we
separate US unattributed revenue from global unattributed revenue.

For more information, see [Monitor your
obligations](https://docs.stripe.com/tax/monitoring).

## Registrations

Use the **Registrations** tab to manage locations and access reports where you
have a tax registration. Registrations enable you to calculate and collect tax
with Stripe. Locations are either **Active**, **Scheduled**, or **Expired**.

CategoryDefinitionActiveA registration that is currently calculating and
collecting tax.ScheduledA registration that will start calculating tax based on
your inputted start date (provided by the local tax authority).ExpiredA
registration that’s no longer calculating tax as it has passed the inputted end
date (provided by the local tax authority)
### Add a registration

To start calculating and collecting tax for a location, you must add a
registration in Stripe Tax. You need to identify each state, province, and
country where you have tax obligations. You need to register with the local tax
authority to collect tax for each tax obligation. Registration requirements vary
by each location (often referred to as nexus in the US). If you have not already
registered, you can use [Stripe to
register](https://docs.stripe.com/tax/use-stripe-to-register) on your behalf.

To add a registration in the Dashboard:

- Click **+Add registration** and select the country and the applicable state or
province.
- Add the date to start tax collection as provided by your local tax authority.
- Save your changes.

### Edit a registration

To maintain your compliance, you might need to edit your registration. Your
local tax authority will inform you of any updates to your information or dates.

To edit a registration:

- Click the overflow menu () next to the applicable registration.
- Click **Edit registration**.
- Save your changes.

### End a registration

To stop calculating and collecting tax for a location, you must end the tax
obligation’s registration.

To end a registration:

- Click the overflow menu () next to the applicable registration.
- Add the date (provided by your local tax authority) to stop tax collection.
- Save your changes.

### Export transactions

You can export your transaction data into either an itemized or summarized
report at the line item, imposition, and jurisdiction level for all locations
where you have Stripe Tax is enabled.

To export transaction data:

- Click **Export transactions**.
- Select either **Itemized export** or **Summarized export** as needed.
- Click **Download**.

After you download the report, click **View Report**.

### US location reports

US location reports aggregate your transaction data in the chosen location for a
specific filing period based on the state filing requirements. You can create
them for any US location where you have Stripe Tax enabled.

### See also

- [Set up Stripe Tax](https://docs.stripe.com/tax/set-up)
- [Monitor your tax obligations](https://docs.stripe.com/tax/monitoring)
- [Understand when you need to collect tax in each
location](https://docs.stripe.com/tax/supported-countries)
- [Use Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register)

## Links

- [Tax Settings](https://dashboard.stripe.com/settings/tax)
- [use Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register)
- [preset product tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#product-tax-code)
- [digital products](https://docs.stripe.com/tax/tax-codes?type=digital)
- [countries supported by Stripe
Tax](https://docs.stripe.com/tax/supported-countries)
- [marketplace facilitators](https://docs.stripe.com/tax/tax-for-marketplaces)
- [Monitor your obligations](https://docs.stripe.com/tax/monitoring)
- [Set up Stripe Tax](https://docs.stripe.com/tax/set-up)