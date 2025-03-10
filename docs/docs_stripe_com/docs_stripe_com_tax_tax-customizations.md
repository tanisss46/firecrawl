# Tax customizations

## Learn how to customize tax behavior using Stripe Tax.

Set up Stripe Tax to fit your business needs with tax customizations. Create
rules that apply to a product tax code in any supported location.

For example, you can:

- Change the [Software as a service (SaaS) - personal
use](https://docs.stripe.com/tax/tax-codes?tax_code=txcd_10103000) tax code from
taxable to non-taxable in Louisiana to reflect the uncertainty of how SaaS might
be taxed.
- Apply a 5% tax rate to the
[Newspapers](https://docs.stripe.com/tax/tax-codes?tax_code=txcd_35020100%09)
tax code in Poland, instead of the applied rate of 8%, to reflect that your
product is a regional newspaper and not a national one.
- Treat the [Food for non-immediate
consumption](https://docs.stripe.com/tax/tax-codes?tax_code=txcd_40040000) tax
code as taxable at the standard rate in New York, to reflect that you sell a
bagels with cream cheese.

After you create a tax customization, you’re responsible for keeping the rate
and taxability up to date with any changes in tax law. When you remove a tax
customizations, Stripe manages the updates.

## Access tax customizations

Calculations and transactions with tax customizations applied incur no
additional charge over other tax calculations or transactions. To enable access
to tax customizations on your account:

- In the [tax settings](https://dashboard.stripe.com/settings/tax) Dashboard,
scroll to the **Advanced options** section.
- Select the **+ Create rules** button in the **Custom tax rules** section.
- Review the information about tax customizations and click **Continue**.
- The **Customizations** tab now appears in your [tax
Dashboard](https://dashboard.stripe.com/tax/).

## Create a tax customization

Create your first tax customization in a sandbox to make sure you get the tax
outcome you expect:

- In the Dashboard, navigate to the [Customizations
tab](https://dashboard.stripe.com/tax/customizations) in the Tax page.
- Click **+ Create customization**.
- In the section **Product tax code**, choose the product tax code your
customization applies to.
- *(Optional)* Specify the date and time for the customization rule to become
effective under **Effective date**. For example, you can set the customization
rule to start from the first day of the month. If you don’t set a date, the rule
takes effect immediately.
- In the section **Rule location**, choose a jurisdiction where your
customization applies.- You can create a rule that applies to a country or
state.
- For US jurisdictions, you can also create a rule that only applies to a
specific city, county, or district.
- For **Tax type**, choose the type of tax your customization applies to.
- Click the Tax behavior you want to apply. We indicate whether the product tax
code you chose is taxable or non-taxable in that specific location and for the
particular tax type (for example, sales tax or VAT).- If you choose **Taxable**,
you have two options:- Apply the standard rate. This means that your rule always
uses the standard rate that Stripe has determined for that product tax code,
tax, and location. If the standard rate changes, that change also applies to
your products.
- Apply a custom rate. This means that your rule uses the tax rate that you set.
If the standard rate changes for that product, your custom rate still applies.

#### Regional considerationsUnited States

You can’t apply a custom rate in the US when creating a rule for a state that
applies to all jurisdictions in a state because several cities and counties have
different tax rates. To determine a custom rate for these jurisdictions, select
a specific city, county, or district in the jurisdiction dropdown.
- Verify that all of the details in the **Summary** panel are correct. The
**Rate preview** displays the expected tax rate that applies for a location
within the jurisdiction you chose.- The calculated tax might vary for other
addresses within the same jurisdiction.
- In some cases, the tax code, tax, and location you select might be taxed at
the location of your business, rather than the destination of the customer. In
these cases, the preview displays how tax applies in your business location. We
don’t use your tax customization rule in these cases.
- Click **Create rule** to apply your rule immediately, or at the time and date
you chose.

## View and maintain your tax customizations

View all your customization rules in the [Customizations
tab](https://dashboard.stripe.com/tax/customizations). Click a customization to
view the following information:

- When the rule was created or edited.
- Who created or edited the rule.
- The taxability and rate that’s applied.
- The tax code, location, and tax the rule applies to.

If you have a customization in place, Stripe won’t automatically update the
taxability or custom rate of your product if something changes. It’s your
responsibility to maintain your tax customizations to make sure they reflect
what’s needed for your business.

## Edit a tax customization

If your customization is scheduled to start in the future, you can edit the
start or end time of your customization rule. If your rule is already active,
you can edit the end date and time. To change the tax code, location, or tax
rate, you must archive the rule and create a new one in its place.

To edit your tax rule:

- In the Dashboard, navigate to the [Customizations
tab](https://dashboard.stripe.com/tax/customizations) in the Tax page.
- Find the customization rule you want to edit.
- Click the overflow menu () next to the rule and choose **Edit rule**.
- Make your changes to the time and date.
- Click **Save**.

## Archive a tax customization

You can archive a customization that you created. After you archive a
customization rule, it no longer applies to your tax transactions and Stripe’s
default behavior applies instead. Rules can’t be unarchived, but you can create
a new rule instead.

To archive your tax customization:

- In the Dashboard, navigate to the [Customizations
tab](https://dashboard.stripe.com/tax/customizations) in the Tax page.
- Find the tax customization you want to archive.
- Click the overflow menu () next to the rule and choose **Archive rule**.
- Confirm your changes, then click **Archive**.

## Verify which transactions have a tax customization rule applied

To verify which tax customization applies to a transaction, view the
**customizations_applied_ids** column of the [itemized
export](https://docs.stripe.com/tax/reports?#itemized-exports).

We don’t include transactions that contain tax customizations in the US-specific
location reports or summarized reports. Learn more about the [different tax
reports](https://docs.stripe.com/tax/reports).

## How we pick which customization applies

When two rules apply to the same product in the same jurisdiction, Stripe only
applies the more specific rule.

For example, this might apply if Stripe treats your product as taxable in the
state of Colorado, but you want to treat it as non-taxable in all of Colorado
except for the city of Boulder, where it should be taxed at the standard rate.

To change this, you can create a rule for the tax code that you apply to your
product for the state of Colorado:

- Navigate to the [Customizations
tab](https://dashboard.stripe.com/tax/customizations) in the Tax page, then
choose **Colorado** from the **Rule location** dropdown.
- Enable **Include all jurisdictions**.
- Choose **Sales Tax** from the **Tax type** dropdown.
- Set **Non-taxable** as the **Tax behavior**.

Additionally, you can create a second rule for the same tax code to apply tax in
Boulder, but not elsewhere in Colorado:

- Navigate to the [Customizations
tab](https://dashboard.stripe.com/tax/customizations) in the Tax page, then
choose **Colorado** from the **Choose location** dropdown under **Rule
location**.
- Disable **Include all jurisdictions**.
- Choose **Boulder** from the *Choose a jurisdiction** dropdown.
- Choose **Sales Tax** from the **Tax type** dropdown.
- Set **Standard rate** as the **Tax behavior**.

You can’t create a tax customization that applies to the same specific
jurisdiction (for example, Boulder) for the same tax code, during the same time
period.

## When you can’t use customizations

Some parts of a tax calculation can’t be overridden. The following things will
continue to affect the final tax calculation:

- **Sourcing rules**: These rules determine whether tax is calculated using the
destination of the buyer or the origin of the seller. If you create a
customization that applies to a jurisdiction, but your product is sourced to the
origin instead, your customization rule won’t apply.
- Tiers, thresholds, and taxable basis apply in some jurisdictions:- **Taxable
basis**: In certain locations, only a specific portion of the tax code is
taxable. For example, in Texas, only 80% of the cost of Software as a service is
subject to tax.
- **Treatment based on price**: Products might be treated differently based on
their price. For example, in New York, clothing is exempt from tax if it costs
under 110 USD, but taxable if it exceeds that amount. Even if you create a rule
for New York City with a custom rate, sales of clothing in New York under 110
USD is still considered exempt.

#### Regional considerationsUnited States

Tax customizations in Stripe don’t transfer to TaxJar. When using TaxJar for
filing, these customizations aren’t taken into account when TaxJar recalculates
the tax you’re expected to file. As a result, tax customizations might not be
suitable for your specific use case.

## Tax customizations for Connect platforms

### Connect use cases that qualify for tax customizations

- [Marketplaces](https://docs.stripe.com/tax/tax-for-marketplaces) (Connect
platforms that assume responsibility for collecting and remitting taxes for
their connected accounts)
- Connected accounts with access to the Stripe Dashboard and that are liable for
collecting taxes

### Connect software platforms partially supported by tax customizations

A software platform can create a customization for their connected account by
doing the following:

- Navigate to the connected account details page from the [Connected
accounts](https://dashboard.stripe.com/connect/accounts/overview) page.
- Log in as the connected account.
- Create a [tax customization in the
Dashboard](https://docs.stripe.com/tax/tax-customizations#create-a-tax-customization).

However, you can’t create a tax customization at the software platform level
that applies to all of your connected accounts.

## Links

- [Software as a service (SaaS) - personal
use](https://docs.stripe.com/tax/tax-codes?tax_code=txcd_10103000)
- [Newspapers](https://docs.stripe.com/tax/tax-codes?tax_code=txcd_35020100%09)
- [Food for non-immediate
consumption](https://docs.stripe.com/tax/tax-codes?tax_code=txcd_40040000)
- [tax settings](https://dashboard.stripe.com/settings/tax)
- [tax Dashboard](https://dashboard.stripe.com/tax/)
- [Customizations tab](https://dashboard.stripe.com/tax/customizations)
- [itemized export](https://docs.stripe.com/tax/reports?#itemized-exports)
- [different tax reports](https://docs.stripe.com/tax/reports)
- [Marketplaces](https://docs.stripe.com/tax/tax-for-marketplaces)
- [Connected accounts](https://dashboard.stripe.com/connect/accounts/overview)