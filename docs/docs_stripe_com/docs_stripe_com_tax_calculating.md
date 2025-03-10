# Calculate tax

## Learn how to calculate tax with Stripe Tax.

The most common forms of indirect taxes for your business are sales tax,
[VAT](https://stripe.com/guides/introduction-to-eu-vat-and-european-vat-oss),
and [GST](https://stripe.com/guides/tax-registration-process-canada). These
taxes apply on the sale of physical goods, digital goods, and services.

Stripe calculates tax on a transaction taking into account some or all of the
following factors:

- The location of the seller
- The location of the customer
- The type of the product sold
- Whether the transaction involves a [reverse
charge](https://docs.stripe.com/tax/zero-tax#reverse-charges)
- The status of the customer (for example, whether they’re a VAT-registered
business, private person or an exempt organization)

## How Stripe uses addresses

Stripe uses a single address as the customer’s location, or transaction
destination, when calculating taxes. For more information, see [which customer
address we
use](https://docs.stripe.com/tax/customer-locations#address-hierarchy).

In certain scenarios, it’s important to identify the origin of a transaction.
Stripe generally uses the address where your business is located as the origin
of a transaction. This address is defined as your origin address in the
Dashboard or as `head_office` if using the tax settings object.

### How to use ship-from addresses

You can add ship-from addresses that differ from your business address for tax
calculation. To add them, use the `ship_from_address` transaction object. You
can add ship-from locations only using the [Stripe Tax
API](https://docs.stripe.com/tax/custom). They aren’t available in integrations
of Stripe Tax with Payment Links, Checkout, or Billing and Invoicing. If you
enter an unrecognized ship-from address, Stripe returns a
`shipping_address_invalid` error.

Stripe Tax can designate only one address as the origin of a transaction even
though in some countries the determination of origin can vary by product type.
If you provide the ship-from address, Stripe Tax uses it to calculate tax for
both services and physical goods. If you don’t provide a ship-from address,
Stripe Tax assumes that the origin of the transaction is the address where your
business is located. When selling a combination of products that require
different origin locations, consider splitting the transaction accordingly.

[Specify product tax codes and tax behaviorLearn how to set up products and
prices to automatically calculate
tax.](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)[Collect
customer addressesLearn how to collect customer addresses to automatically
calculate tax.](https://docs.stripe.com/tax/customer-locations)[Zero tax amounts
and reverse chargesLearn about cases when Stripe calculates zero
tax.](https://docs.stripe.com/tax/zero-tax)[Customize tax behaviorSet up Tax to
fit your business needs with tax
customizations.](https://docs.stripe.com/tax/tax-customizations)[Countries
supported by Stripe TaxLearn how to use Stripe to calculate, collect, and report
tax in different countries](https://docs.stripe.com/tax/supported-countries)

## Links

- [VAT](https://stripe.com/guides/introduction-to-eu-vat-and-european-vat-oss)
- [GST](https://stripe.com/guides/tax-registration-process-canada)
- [reverse charge](https://docs.stripe.com/tax/zero-tax#reverse-charges)
- [which customer address we
use](https://docs.stripe.com/tax/customer-locations#address-hierarchy)
- [Stripe Tax API](https://docs.stripe.com/tax/custom)
- [Specify product tax codes and tax behaviorLearn how to set up products and
prices to automatically calculate
tax.](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
- [Collect customer addressesLearn how to collect customer addresses to
automatically calculate tax.](https://docs.stripe.com/tax/customer-locations)
- [Zero tax amounts and reverse chargesLearn about cases when Stripe calculates
zero tax.](https://docs.stripe.com/tax/zero-tax)
- [Customize tax behaviorSet up Tax to fit your business needs with tax
customizations.](https://docs.stripe.com/tax/tax-customizations)
- [Countries supported by Stripe TaxLearn how to use Stripe to calculate,
collect, and report tax in different
countries](https://docs.stripe.com/tax/supported-countries)