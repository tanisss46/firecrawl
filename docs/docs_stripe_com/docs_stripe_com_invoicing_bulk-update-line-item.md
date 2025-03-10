# Manage bulk invoice line itemsPublic preview

## Add, update and remove multiple invoice line items with the Invoices API.

You can edit multiple line items on an invoice by bulk adding, updating, and
removing line items with the [Invoices
API](https://docs.stripe.com/api/invoices).

## Create an invoice

To update an invoice, you need to create one first. You can [create an invoice
in the Dashboard](https://docs.stripe.com/invoicing/dashboard#create-invoice)or
with the [Invoices API](https://docs.stripe.com/api/invoices/create). You can
only update invoices in a [draft
state](https://docs.stripe.com/invoicing/overview#invoice-lifecycle).

## Add line items

To create multiple line items on the same invoice, reference the [invoice
ID](https://docs.stripe.com/api/invoices/object#invoice_object-). You can also
assign a preexisting unassigned invoice item with the [invoice item
ID](https://docs.stripe.com/api/invoiceitems/object#invoiceitem_object-). Here’s
how to create two new line items and assign an existing invoice item to this
invoice.

```
curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/add_lines \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "lines[0][amount]"=7500 \
 -d "lines[0][currency]"="usd" \
 -d "lines[1][price]"={{PRICE_ID}} \
 -d "lines[1][description]"="New line item" \
 -d "lines[2][invoice_item]"={{INVOICE_ITEM_1}}
```

#### Common mistake

Ensure that you are using the invoice item ID, using a line item ID here will
result in an error.

## Update line items

From here, you can update multiple line items on the same invoice based on the
invoice ID and line item IDs like the following:

```
curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/update_lines \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "lines[0][id]"={{LINE_ITEM_1}} \
 -d "lines[0][description]"="New description" \
 -d "lines[0][metadata][key]"="new value" \
 -d "lines[1][id]"={{LINE_ITEM_2}} \
 -d "lines[1][price]"={{PRICE_ID}} \
 -d "lines[2][id]"={{LINE_ITEM_3}} \
 -d "lines[2][discountable]"=true
```

The example above updates the description and metadata for line item 1, the
price for line item 2, and whether it’s discountable for line item 3.

## Remove line items

You can delete or unassign multiple line items on the same invoice by
referencing the invoice ID and line item IDs and distinguishing between
different removal types with the `behavior` key. Here’s how to permanently
delete `LINE_ITEM_1` and unassign `LINE_ITEM_2`. You can reassign `LINE_ITEM_2`
to another invoice in another request.

```
curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/remove_lines \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "lines[0][id]"={{LINE_ITEM_1}} \
 -d "lines[0][behavior]"="delete" \
 -d "lines[1][id]"={{LINE_ITEM_2}} \
 -d "lines[1][behavior]"="unassign"
```

## Restrictions

There are some restrictions when using this feature

- The invoice must still be in a draft state
- There are two [types of invoice line
items](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-type)-
`type: invoiceitem`: Generated when an [invoice
item](https://docs.stripe.com/api/invoiceitems) is added to an invoice.
- `type: subscription`: Automatically generated for a subscription invoice from
each subscription item. This is the [full list of fields that are
available](https://docs.stripe.com/api/invoices/update_lines#bulk_update_lines-lines)
to update for each line item. While all fields are supported for `invoiceitem`
line items, you can only update a small subset for `subscription` line items.
Fields that are supported for `subscription` line items are `tax_rates`, or
`discounts`.
- You can update a maximum of 50 line items in one API call. This limit is
subject to change and might increase or decrease.

## Invoice metadata

You can set invoice metadata in the same request for any of the above endpoints.
Here’s an example calling [update_lines](https://docs.stripe.com/api/invoices).

```
curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/update_lines \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "lines[0][id]"={{LINE_ITEM_1}} \
 -d "lines[0][description]"="New description" \
 -d "lines[1][id]"={{LINE_ITEM_1}} \
 -d "lines[2][description]"="Another description" \
 -d "invoice_metadata[is_processed]"="true"
```

## Links

- [Invoices API](https://docs.stripe.com/api/invoices)
- [create an invoice in the
Dashboard](https://docs.stripe.com/invoicing/dashboard#create-invoice)
- [Invoices API](https://docs.stripe.com/api/invoices/create)
- [draft state](https://docs.stripe.com/invoicing/overview#invoice-lifecycle)
- [invoice ID](https://docs.stripe.com/api/invoices/object#invoice_object-)
- [invoice item
ID](https://docs.stripe.com/api/invoiceitems/object#invoiceitem_object-)
- [types of invoice line
items](https://docs.stripe.com/api/invoices/line_item#invoice_line_item_object-type)
- [invoice item](https://docs.stripe.com/api/invoiceitems)
- [full list of fields that are
available](https://docs.stripe.com/api/invoices/update_lines#bulk_update_lines-lines)