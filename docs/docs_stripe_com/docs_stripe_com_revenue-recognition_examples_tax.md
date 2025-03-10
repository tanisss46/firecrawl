# Tax examples

## Learn about revenue recognition with tax examples.

Unless stated otherwise, these tax examples assume that revenue recognition
takes place on a per-day basis.

## Tax exempt

Your [customers](https://docs.stripe.com/api/customers) can have a [tax
exemption
status](https://docs.stripe.com/billing/taxes/tax-rates#tax-exempt-and-reverse-charge)
of either `exempt` or `reverse`. No tax is calculated on the invoice in either
case.

In this example, a customer with a tax exemption status of `reverse` starts a
monthly subscription on January 1 at 00:00:00 UTC. It costs 31 USD per month and
has a tax-inclusive rate of 10%. Because the customer is tax exempt, the total
amount due is 27.90 USD. The subscription generates an invoice, the invoice
finalizes, and the customer pays the invoice on the same day. Your journal entry
would look like this:

AccountDebitCreditRevenue+27.90Cash+27.90
## Tax-inclusive rate on invoice items

An invoice item can include a tax-inclusive rate. When you add an invoice item
to an invoice, it can use the same accounting period or a different accounting
period from its creation date.

### Same accounting period

In this example, a customer starts a service for a period of 1 month on January
1 at 00:00:00 UTC. The total amount due is 34.10 USD and has a tax-inclusive
rate of 10%. You add the invoice item to an invoice on January 1, the invoice
finalizes, and the customer pays the invoice on the same day. Your journal entry
would look like this:

AccountDebitCreditRevenue+31.00Cash+34.10TaxLiability+3.10
### Different accounting period

In this example, a customer starts a service for a 3 month period on January 1
at 00:00:00 UTC. The total amount due is 100.00 USD and has a tax-inclusive rate
of 10%. You add the invoice item to an invoice on March 1, the invoice
finalizes, and the customer pays the invoice on the same day. Your journal entry
would look like this:

AccountJanFebMarRevenue-34.10-30.80-31.00Cash+100.00TaxLiability-10.00UnbilledAccountsReceivable+34.10+30.80-64.90UnbilledVoids+5.90
## Tax liability

Invoices and invoice line items can be [assigned tax
rates](https://docs.stripe.com/invoicing/taxes/tax-rates). When tax rates are
assigned, the Revenue Recognition reports can compute tax liability.

Below is an example using an exclusive tax rate with the following assumptions:

- On January 1, at 00:00:00 UTC, a customer starts a monthly subscription that
costs 31 USD with an exclusive tax rate of 10%. The total due amount is 34.10
USD.
- The subscription generates an invoice.
- The invoice finalizes and is paid on the same day.
AccountJanRevenue+31.00Cash+34.10TaxLiability+3.10
Below is an example using an inclusive tax rate with the following assumptions:

- On January 1, at 00:00:00 UTC, a customer starts a monthly subscription that
costs 31 USD with an inclusive tax rate of 10%. The total due amount is 31 USD.
- The subscription generates an invoice.
- The invoice finalizes and is paid on the same day.
AccountJanRevenue+27.90Cash+31.00TaxLiability+3.10

## Links

- [customers](https://docs.stripe.com/api/customers)
- [tax exemption
status](https://docs.stripe.com/billing/taxes/tax-rates#tax-exempt-and-reverse-charge)
- [assigned tax rates](https://docs.stripe.com/invoicing/taxes/tax-rates)