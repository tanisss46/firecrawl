# Revenue Recognition Performance Obligations APIPrivate preview

## Learn how to model performance obligation fulfillment in Stripe Revenue Recognition.

## Interested in the Revenue Recognition Performance Obligations API?

Please provide your email address below and our team will be in touch.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).
## Overview

Performance obligation fulfillment is an important part of revenue recognition
in accounting and finance. It refers to the completion of a transaction in which
the seller has delivered the goods or services promised to the customer, and can
recognize revenue for the sale. There are several scenarios where fulfillment
occurs and revenue can be recognized, including but not limited to:

- **Delivery of tangible goods**: Fulfillment occurs when the physical goods
have been shipped to the customer and they’ve taken possession of the goods. The
delivery of the goods confirms that the customer has received the promised
benefit, and therefore you can recognize the revenue from the sale.
- **Performance of a service**: In the case of a service-based sale, fulfillment
occurs when the service has been performed and the customer has accepted the
service. After the customer has accepted the service, you can recognize the
revenue.
- **Prepayment**: A customer pays for a service or goods in advance of receiving
the actual service or goods. You can recognize the revenue from the pre-payment
over time as the service is delivered or the goods are used.

This guide explains how to use the Stripe Revenue Recognition Performance
Obligations API to achieve accurate revenue reporting.

## Setup

This example uses a product named “Prepaid package.” Create the product as a
[Stripe product](https://docs.stripe.com/invoicing/products-prices)—call it
“Product Prepaid package.”

Under the Product Prepaid package, a create a
[Price](https://docs.stripe.com/invoicing/products-prices) for one unit. The
price is 1 USD per unit. Call the price “Prepaid package.”

Say you bill a customer for a 100 USD Product Prepaid package, which includes a
Price Prepaid package for 100 units. You want to defer the 100 USD upon
invoicing and to recognize it based on the usage.

### Create a subscription or an invoice

Now you can set up a subscription or a standalone invoice to bill the customer.

For a subscription, you’ll need to add a subscription item whose price is Price
Prepaid package for 100 units.

For an invoice, you’ll need to add an invoice item whose price is Price Prepaid
for 100 units.

### Create a Revenue Recognition rule

To defer the revenue upon invoicing, you’ll need to create a [Revenue
Recognition rule](https://docs.stripe.com/revenue-recognition/rules). If no
fulfillment events are ever sent, the revenue will be recognized entirely over
the specified period, which defaults to one year.

![Performance Obligations API Revenue Recognition Rule
Example](https://b.stripecdn.com/docs-statics-srv/assets/performance-obligations-api-rev-rec-rule.5a53e3837cf2eb1fd58944b46725c464.png)

## Record usages

You can record usages through the API.

If you were to create an invoice on June 1, 2022, and 10 units are used on July
29, 2022, you would send the below API request:

```
curl https://api.stripe.com/v1/revenue_recognition/performance_obligations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "target[type]"=invoice_line_item \
 -d "target[invoice_line_item]"=il_AAA \
 -d "period[start]"=1659078000 \
 -d amount=1000 \
 -d currency=usd
```

## Reporting

### Before fulfillment

If you download the debits and credits reports in June 2022, the following is
what you would see. Because no usage is recorded yet, the whole invoice line
item will be deferred and recognized 12 months later.

AccountJun 2022Jun 2023AccountsReceivable+100DeferredRevenue+100-100Revenue+100
### Partial fulfillment

With the usage recorded in the section above, the reports would look like the
following in July 2022:

AccountJun 2022Jul 2022Jun
2023AccountsReceivable+100DeferredRevenue+100-10-90Revenue+10+90
### Full fulfillment

Suppose another usage is recorded on Aug 10, 2022 with the remaining amount (90
USD). The deferred revenue will be converted to revenue completely in Aug 2022:

AccountJun 2022Jul 2022Aug
2022AccountsReceivable+100DeferredRevenue+100-10-90Revenue+10+90

## Links

- [privacy policy](https://stripe.com/privacy)
- [Stripe product](https://docs.stripe.com/invoicing/products-prices)
- [Revenue Recognition rule](https://docs.stripe.com/revenue-recognition/rules)