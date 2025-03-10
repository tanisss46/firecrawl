# Calculate tax with Avalara

## Learn how the Stripe Connector for NetSuite supports the Avalara AvaTax Connector for Stripe Invoicing to calculate tax.

The Stripe Connector for NetSuite supports using the [Avalara
AvaTax](https://marketplace.stripe.com/apps/avalara-avatax) connector to
calculate tax with Avalara on Stripe invoices. The NetSuite connector syncs
these invoices to NetSuite and records the calculated tax.

## How it works

The Avalara AvaTax connector calculates the tax and then adds it to the Stripe
invoice as a standalone invoice item. Stripe invoices must remain open for a
period of time for Avalara to apply the calculated tax amount. The tax amount
appears as an additional line item (or Stripe [Invoice
Item](https://docs.stripe.com/api/invoiceitems)) labeled `Sales Tax`.

To use this functionality, enable the `pay_immediately` parameter on your
account. Tax calculation then occurs automatically after the first billing
cycle. You can also calculate tax with just a postal code. Consult your tax
professional about the best approach for your business.

#### Warning

Avalara has limited support for the Avalara Connector for Stripe Invoicing and
use of this connector with the Stripe Connector for NetSuite is at your own
risk.

## Set up Avalara

You must have an Avalara test environment to fully test the Stripe Connector for
NetSuite with Avalara. Stripe live mode and test mode transactions can’t process
at the same time.

Configure the Avalara environment to match your Stripe test account:

- For **Tax On Invoices**, select **Recurring** and **Normal**.
- Set up the item mapping to determine the Stripe items for Avalara to tax.

When you successfully integrate Avalara with Stripe, address information gets
added on Stripe customer metadata fields that are specific to Avalara. When
Stripe initiates a subscription, we make sure tax gets added to a payment by
using the `pay_immediately: false` parameter to delay immediate payment. When
Stripe generates an invoice for the next subscription billing period, an Avalara
line item gets added automatically to the Stripe invoice.

### Webhook setup

Avalara doesn’t automatically receive webhooks from your Stripe account. You
must manually add the Avalara webhook URL to each environment that you want to
test Avalara. To do so, copy the Avalara webhook endpoint from the AvaTax setup
and add it to the Stripe webhooks admin (**API** > **Webhooks**).

To process test webhooks, connect to Avalara’s sandbox system through the
[AvaTax for Stripe](https://avataxforstripe.com/) dashboard. You can only
connect to one Avalara environment at a time. Learn about how to use [Avalara
AvaTax](https://knowledge.avalara.com/bundle/wgx1671615018330_wgx1671615018330/page/ale1671617118294.html)
for tax calculation.

## AvaTax tax code

If you use a tax engine in NetSuite, it likely calculates and records taxes due
on any invoices created in NetSuite. If you use Stripe Billing invoices, Avalara
calculates and records the tax amount before the invoice syncs to NetSuite. To
make sure that Avalara doesn’t calculate taxes in NetSuite, the connector sets
the tax code on the invoice and line item level to `Not Taxable`.

If a Stripe price links to a NetSuite item that has an AvaTax tax code, the
Avalara tax system overrides the Stripe Connector defaults and calculates the
tax twice. Make sure that all NetSuite items linked to Stripe prices don’t have
an AvaTax tax code.

## Tax representation in NetSuite

Stripe represents the taxes calculated by Avalara as a Stripe Tax line item on
the NetSuite invoice. You can rename the line item, edit the liability account,
or edit other aspects of the item. Customize the name and account to align with
how you manage taxes in NetSuite.

If you use Avalara outside of the NetSuite environment to calculate tax, you
can’t use the `Avatax` sales tax item to represent tax in NetSuite. This special
tax item triggers a call to Avalara that records the taxes for that order again.
Taxes calculated by Avalara outside of NetSuite aren’t represented by tax codes
or groups.

## Avalara race condition

The Avalara Connector has a race condition to consider. If you use the
`invoice.created` webhook, Avalara might calculate taxes after you add
usage-based billing through Stripe standalone invoice items. This means tax
might not calculate and record properly.

## Links

- [Avalara AvaTax](https://marketplace.stripe.com/apps/avalara-avatax)
- [Invoice Item](https://docs.stripe.com/api/invoiceitems)
- [AvaTax for Stripe](https://avataxforstripe.com)
- [Avalara
AvaTax](https://knowledge.avalara.com/bundle/wgx1671615018330_wgx1671615018330/page/ale1671617118294.html)