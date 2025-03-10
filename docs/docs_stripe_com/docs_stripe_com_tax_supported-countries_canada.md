# Collect tax in Canada

## Learn how to use Stripe Tax to calculate, collect, and report tax in Canada.

The Canadian tax system consists of a combination of federal and provincial
taxes. The goods and services tax (GST) applies nationally. The different
provinces handle taxes in a variety of ways. Learn more in our [guide to tax in
Canada](https://stripe.com/guides/tax-registration-process-canada).

Provincial sales taxes in New Brunswick, Newfoundland and Labrador, Nova Scotia,
Ontario, and Prince Edward Island are combined with the GST to implement the
harmonized sales tax (HST), which operates in the same way as the GST.

Separate taxes are collected in:

- British Columbia—provincial sales tax (PST)
- Manitoba—retail sales tax (RST)
- Quebec—Quebec sales tax (QST)
- Saskatchewan—provincial sales tax (PST)

Alberta, Northwest Territories, Nunavut, and Yukon don’t apply any provincial
sales tax.

## When to register for tax collection

The Canadian federal government and the four provinces that levy a separate
provincial sales tax define their own tax registration thresholds and
procedures.

- If your business is based outside of Canada, Stripe monitors whether you must
collect tax at the federal level and for every province with its own tax. You
can register to collect federal tax using either a simplified or a normal
GST/HST registration.
- If your business is based in Canada, Stripe monitors whether you must collect
provincial taxes, but not for the province where your business is established.
To collect federal tax, you must register with the Canadian government using a
normal GST/HST registration.

See [Thresholds](https://dashboard.stripe.com/tax/thresholds) to get insights
about your potential tax registration obligations in Canada. Stripe also
notifies you with email and Dashboard alerts when you need to register to
collect tax. Learn more about how the [monitoring tool
works](https://docs.stripe.com/tax/monitoring).

After you’ve registered to collect tax in a province or with the government, go
to [Registrations](https://dashboard.stripe.com/tax/registrations?location=ca)
to add your registrations to Stripe in the Dashboard and start collecting tax on
your transactions in that location.

### Federal tax threshold

Canada applies different regulations to businesses outside of Canada that sell
to Canadian customers. The regulations depend on the product type, the location
the product is shipped from, and the type of business activity.

- Foreign businesses that carry on business in Canada must apply for the normal
GST/HST registration if their total taxable revenues are over 30,000 CAD in a
single calendar quarter or over the last four consecutive calendar quarters.
Find more information on what “carry on business in Canada” means on the [Canada
Revenue Agency
website](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/p-051r2/p-051r2-carrying-on-business-canada.html).
- Foreign remote businesses that sell digital products or services to Canadian
individuals qualify for simplified GST/HST registration when sales exceed 30,000
CAD over any 12-month period.
- Business based outside of Canada that sell goods shipped from a warehouse in
Canada to Canadian individuals require normal GST/HST registration when sales
exceed 30,000 CAD over any 12-month period.

Stripe only monitors the threshold applicable to sellers based outside of Canada
who do not carry on business in Canada. If you [carry on business in
Canada](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/p-051r2/p-051r2-carrying-on-business-canada.html),
the threshold doesn’t reflect your tax obligations.

**Threshold**: 30,000 CAD

**Time frame**: 12 months

**Included transactions**: Sales of digital products and services to Canadian
individuals, and sales of goods shipped from a warehouse in Canada to Canadian
individuals.

Find more information on how to register for GST/HST on the Canada Revenue
Agency websites:

- [Normal GST/HST
regsitration](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/registering-your-business/register.html#NR-BN_AccRegistrtn_Webform)
- [Simplified GST/HST
regsitration](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/register-gst-hst.html)

If a remote business sells digital services or goods into Canada exclusively
through online marketplaces that are responsible for collecting tax on these
sales, the seller isn’t required to register for GST/HST. These sales don’t
count toward the seller’s registration threshold.

### British Columbia

Businesses based outside British Columbia (BC) must register to collect PST if
their taxable sales in BC exceed 10,000 CAD in the past 12 months or are
expected to exceed that amount in the next 12 months.

**Threshold**: 10,000 CAD

**Time frame**: 12 months

**Included transactions**: Any taxable transaction.

Find more information on how to register for PST on the [British Columbia
government website](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst).

If a remote business sells digital services or goods exclusively through online
marketplaces that are responsible for collecting tax on these sales, the seller
isn’t required to register for PST. These sales don’t count toward the seller’s
registration threshold.

### Manitoba

Businesses located outside Manitoba that perform taxable sales of goods and
services in Manitoba must register to collect RST. Manitoba doesn’t apply any
monetary registration thresholds to remote sellers.

**Threshold**: 1 transaction

**Time frame**: 12 months

**Included transactions**: Any taxable transaction.

Find more information on how to register for RST on the [Manitoba government
website](https://www.gov.mb.ca/finance/taxation/forms.html#retail).

If a remote business sells digital services or goods exclusively through online
marketplaces that are responsible for collecting tax on these sales, the seller
isn’t required to register for RST. These sales don’t count towards the seller’s
registration threshold.

### Quebec

Remote businesses selling digital products or services to individuals in Quebec
must register under the specified QST regime if their sales exceed 30,000 CAD in
any 12-month period. Remote businesses selling goods to individuals in Quebec
must register under the general QST regime if their sales exceed 30,000 CAD in
any 12-month period—this applies to goods shipped from a warehouse in Quebec or
from outside Quebec by means other than mail or courier. The specified QST
regime doesn’t apply in this situation.

**Threshold**: 30,000 CAD

**Time frame**: 12 months

**Included transactions**: Sales of digital products and services and certain
sales of goods to individuals in Quebec.

Find more information on how to register for QST on the [Quebec government
website](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/).

If a remote business sells digital services or goods exclusively through online
marketplaces that are responsible for collecting tax on these sales, the seller
isn’t required to register for QST. These sales don’t count toward the seller’s
registration threshold.

### Saskatchewan

Businesses located outside Saskatchewan that sell taxable goods and services in
Saskatchewan must register to collect PST. Saskatchewan doesn’t apply any
monetary registration thresholds to remote sellers.

**Threshold**: 1 transaction

**Time frame**: 12 months

**Included transactions**: Any taxable transaction.

Find more information on how to register for PST on the [Saskatchewan government
website](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins/provincial-sales-tax).

If a remote business sells digital services or goods exclusively through online
marketplaces that are responsible for collecting tax on these sales, the seller
isn’t required to register for PST. These sales don’t count toward the seller’s
registration threshold.

## How we calculate taxes

Stripe determines whether federal tax (GST or HST), provincial tax (PST, QST, or
RST) or a combination of both types of taxes apply to the specific transaction.

Sales of goods and services within Canada are generally taxed based on the
customer’s location. Goods shipped from Canada to customers abroad are
zero-rated exports for Canadian tax purposes. While these transactions might
incur taxes and customs duties in the destination country, Stripe doesn’t
calculate them.

Stripe calculates GST/HST on sales of goods from abroad to Canadian customers if
the seller is registered under the normal GST/HST regime. If the seller is
registered under the simplified GST/HST regime, we don’t calculate GST/HST on
sales of goods from abroad to Canadian customers.

Sales of services provided from Canada to customers in other countries are
generally not taxable in Canada, but the tax of the customer’s country might
apply. Sales of services provided to Canadian customers by sellers established
in other countries are generally taxable in Canada, with the following
exceptions:

- Remote sellers registered under the simplified GST/HST regime must collect
GST/HST for sales to individuals, but not for sales to business customers who
provide their GST/HST registration number.
- Remote sellers must collect QST on sales to individuals in Quebec, but not on
sales to business customers who provide their QST registration number.
- Remote sellers must collect provincial sales taxes for sales in Manitoba,
Saskatchewan, and British Columbia regardless of individual or business
customers. To treat sales to customers in these provinces as exempt from
provincial sales taxes, set the [customer tax
status](https://docs.stripe.com/tax/zero-tax) to `exempt`.

## Report and file your taxes

Stripe Tax has filing partners—Taxually, Marosa, and Hands-off Sales Tax—to help
automate your tax filing. These partners automatically sync your tax transaction
data in real time, eliminating the need for manual data entry or file transfers.
Learn more about [tax filing](https://docs.stripe.com/tax/filing).

Stripe also provides reports of your completed tax transactions. Go to
[Registrations](https://dashboard.stripe.com/tax/registrations) to access these
reports. Learn more about [the different types of
reports](https://docs.stripe.com/tax/reports).

## Marketplace tax liability

Canada defines “digital platform operators” as marketplace operators that might
have tax collection obligations because they control a transaction between a
seller and a buyer (for example, by handling payments and passing them to the
seller). This definition excludes businesses solely listing goods or processing
payments. Digital platform operators must collect GST/HST on:

- Sales of digital products and services to Canadian individuals by remote
sellers not registered under the normal GST/HST regime.
- Sales of goods by non-registered sellers to Canadian customers if the goods
are in Canada at the time of sale.
- Provision of short-term accommodation if the property owner isn’t GST/HST
registered. This typically includes renting residential units for less than one
month. Stripe Tax doesn’t support accommodation services.

Canadian provinces with separate provincial taxes have similar rules on platform
tax collection obligations.

## Links

- [guide to tax in
Canada](https://stripe.com/guides/tax-registration-process-canada)
- [Thresholds](https://dashboard.stripe.com/tax/thresholds)
- [monitoring tool works](https://docs.stripe.com/tax/monitoring)
- [Registrations](https://dashboard.stripe.com/tax/registrations?location=ca)
- [Canada Revenue Agency
website](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/p-051r2/p-051r2-carrying-on-business-canada.html)
- [Normal GST/HST
regsitration](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/registering-your-business/register.html#NR-BN_AccRegistrtn_Webform)
- [Simplified GST/HST
regsitration](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/register-gst-hst.html)
- [British Columbia government
website](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst)
- [Manitoba government
website](https://www.gov.mb.ca/finance/taxation/forms.html#retail)
- [Quebec government
website](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/)
- [Saskatchewan government
website](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins/provincial-sales-tax)
- [customer tax status](https://docs.stripe.com/tax/zero-tax)
- [tax filing](https://docs.stripe.com/tax/filing)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [the different types of reports](https://docs.stripe.com/tax/reports)