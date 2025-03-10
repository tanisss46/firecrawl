# Preview an invoice

## Learn how to create a preview of an invoice.

You can create a preview of an invoice for your customer while they’re
considering a purchase. [Create a
preview](https://docs.stripe.com/api/invoices/create_preview) to calculate the
total invoice amount, retrieve each invoice line, and include any relevant taxes
or discounts. Creating a preview allows you to show the total payment amount to
your customer without the need to create an invoice.

For example, if you operate a company that provides repair services to
businesses, you might present your customers with multiple items that each have
different prices and billing schedules:

- Item 1: 299 USD one-time service fee
- Item 2: 29 USD repair material A
- Item 3: 99 USD repair material B
- Item 4: 49 USD per month support plan

Customers might want to know how much different combinations of your goods and
services cost. If they intend to purchase items 1 and 3 while applying the
`WINTERSALE` promo code for 15% off, run the following API call:

```
curl https://api.stripe.com/v1/invoices/create_preview \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "invoice_items[0][price]"=price_item_1 \
 -d "invoice_items[0][quantity]"=1 \
 -d "invoice_items[1][price]"=price_item_3 \
 -d "invoice_items[1][quantity]"=1 \
 -d "discounts[0][promotion_code]"=promo_WINTERSALE
```

Stripe returns an [invoice](https://docs.stripe.com/api/invoices/object) preview
with each of the lines, with the discount applied, and the total amount:

```
{
 "id": "upcoming_in_1OujwkClCIKljWvsq5v2ICAN",
 "object": "invoice",
 "account_country": "US",
 "account_name": "Stripe Docs",
 "account_tax_ids": null,
 "amount_due": 39800,
 "amount_paid": 0,
 "amount_remaining": 39800,
 "amount_shipping": 0,
```

See all 230 lines
Additionally, the resulting invoice preview can be retrieved via the
[/v1/invoices/:id](https://docs.stripe.com/api/invoices/retrieve) endpoint for
the following 72 hours:

```
curl https://api.stripe.com/v1/invoices/upcoming_in_1OujwkClCIKljWvsq5v2ICAN \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

## Include Stripe Tax

To preview tax amounts from Stripe Tax, set `automatic_tax[enabled] = true` and
pass the customer’s address in `customer_details[address]`:

```
curl https://api.stripe.com/v1/invoices/create_preview \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "customer_details[address][line1]"="920 5th Ave" \
 -d "customer_details[address][city]"=Seattle \
 -d "customer_details[address][state]"=WA \
 -d "customer_details[address][postal_code]"=98104 \
 -d "customer_details[address][country]"=US \
 -d "automatic_tax[enabled]"=true \
 -d "invoice_items[0][price]"=price_item_1 \
 -d "invoice_items[0][quantity]"=1 \
 -d "invoice_items[1][price]"=price_item_3 \
 -d "invoice_items[1][quantity]"=1 \
 -d "discounts[0][promotion_code]"=promo_WINTERSALE
```

## Preview invoices with subscriptions

To preview the first invoice with a recurring price, use the
[subscription_details.items](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-subscription_details-items)
parameter:

```
curl https://api.stripe.com/v1/invoices/create_preview \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "subscription_details[items][0][price]"=price_recurring_4 \
 -d "subscription_details[items][0][quantity]"=1 \
 -d "invoice_items[0][price]"=price_item_1 \
 -d "invoice_items[0][quantity]"=1 \
 -d "invoice_items[1][price]"=price_item_3 \
 -d "invoice_items[1][quantity]"=1 \
 -d "discounts[0][promotion_code]"=promo_WINTERSALE
```

To preview changes to an existing subscription, provide the [subscription or
subscription schedule
ID](https://docs.stripe.com/billing/subscriptions/subscription-schedules#preview-an-invoice).

## Preview the recurring charges only

Your customer might want a recurring subscription along with one-time items, or
temporary credits or discounts to use with their purchase. If they want to know
what the recurring charges are after any adjustments, use the
[preview_mode](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-preview_mode)
parameter to offer them a preview of the total.

For example, if `WINTERSALE` is a one-time 15% discount and the customer wants
to purchase items 1, 3, and 4, you can retrieve the recurring charge amount with
this API call:

```
curl https://api.stripe.com/v1/invoices/create_preview \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d preview_mode=recurring \
 -d "subscription_details[items][0][price]"=price_recurring_4 \
 -d "subscription_details[items][0][quantity]"=1 \
 -d "invoice_items[0][price]"=price_item_1 \
 -d "invoice_items[0][quantity]"=1 \
 -d "invoice_items[1][price]"=price_item_3 \
 -d "invoice_items[1][quantity]"=1 \
 -d "discounts[0][promotion_code]"=promo_WINTERSALE
```

The resulting invoice only contains the 49 USD per month support plan with no
discounts. Similarly, you can combine `preview_mode` with `subscription` or
`subscription_schedule` to display the expected recurring charge, excluding
one-off items and discounts.

## Invoice Line pagination

For invoices with more than 10 lines, you can [retrieve a paginated view of the
lines](https://docs.stripe.com/api/invoices/invoice_lines):

```
curl
https://api.stripe.com/v1/invoices/upcoming_in_1OujwkClCIKljWvsq5v2ICAN/lines \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

## Links

- [Create a preview](https://docs.stripe.com/api/invoices/create_preview)
- [invoice](https://docs.stripe.com/api/invoices/object)
- [/v1/invoices/:id](https://docs.stripe.com/api/invoices/retrieve)
-
[subscription_details.items](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-subscription_details-items)
- [subscription or subscription schedule
ID](https://docs.stripe.com/billing/subscriptions/subscription-schedules#preview-an-invoice)
-
[preview_mode](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-preview_mode)
- [retrieve a paginated view of the
lines](https://docs.stripe.com/api/invoices/invoice_lines)