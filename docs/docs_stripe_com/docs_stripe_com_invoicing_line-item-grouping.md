# Invoice summary itemsPrivate preview

## Learn how to use the Invoicing APIs to summarize and hide invoice line items.

This guide describes how to use the underlying API (Invoice summary items) that
enables the grouping of invoice line items. With the summary item feature, you
can group invoice line items with the API.

If you want to categorize and display invoice line items dynamically, see [Group
invoice line items](https://docs.stripe.com/invoicing/group-line-items).

## Interested in getting early access to Invoice Summary Items?

Please provide your email address below and our team will contact you soon.

Collect EmailSign upRead our [privacy
policy](https://stripe.com/privacy).[Create summary
items](https://docs.stripe.com/invoicing/line-item-grouping#create-summary-items)
For an existing draft invoice, create an invoice summary item as described
below. The summary item represents a group that you can assign line items to,
and the `description` field of the summary item renders as the group header for
these line items.

By default, Stripe renders all the line items assigned to the summary item. You
can also hide all line items assigned to the summary item and only display the
group header by setting `display_items=none` as a parameter on the summary item.
If you set `display_items=none`, it hides all line items assigned to the summary
item. It is not possible to selectively hide some line items but not others,
except for line items with a value of 0 USD (see **Hide individual $0 line
items** section).

```
curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/summary_items \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d description="Summary item 1" \
 -d display_items="none"
```

Instead of creating the summary items one-by-one, you can also bulk create with
the [create](https://docs.stripe.com/api/invoices/create) or
[update](https://docs.stripe.com/api/invoices/update) invoice endpoints. The
example code below creates a draft invoice with two empty summary items

```
curl https://api.stripe.com/v1/invoices \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "rendering[summary_items_data][0][description]"="Summary item 1" \
 -d "rendering[summary_items_data][0][display_items]"="none" \
 -d "rendering[summary_items_data][1][description]"="Summary item 2" \
 -d "expand[]"="rendering.summary_items"
```

Remember to expand `rendering.summary_items` so you can see the list of summary
items in the response.

[Assign summary
item](https://docs.stripe.com/invoicing/line-item-grouping#assign-summary-items)
Now that the invoice contains empty summary items (assuming that the invoice
already contains line items), we can assign a summary item to the line item.

```
curl
https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/lines/{{INVOICE_LINE_ITEM_ID}}
\
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "rendering[summary_item]"={{SUMMARY_ITEM_ID}}
```

You can update the summary item that the line item belongs to, or un-group the
line item by using the same endpoint.

[Update summary
items](https://docs.stripe.com/invoicing/line-item-grouping#update-summary-items)
Using the [update](https://docs.stripe.com/api/invoices/update) invoice
endpoint, you can re-order, delete, or update the summary items. For example, in
the code below, the order is reversed for the first and second summary item.

```
curl https://api.stripe.com/v1/invoices \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "rendering[summary_items_data][0][id]"="{{SUMMARY_ITEM_2_ID}}" \
 -d "rendering[summary_items_data][1][id]"="{{SUMMARY_ITEM_1_ID}}" \
 -d "expand[]"="rendering.summary_items"
```

To delete all existing summary items from an invoice, use the same endpoint to
unset the `rendering[summary_items_data]` field like the following:

```
curl https://api.stripe.com/v1/invoices \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "rendering[summary_items_data]"="" \
 -d "expand[]"="rendering.summary_items"
```

When you delete the summary items, all associated line items are no longer
grouped.

Alternatively, you can delete a single summary item like the following:

```
curl
https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/summary_items/{{SUMARY_ITEM_ID}}
\
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -x DELETE
```

[Hide individual $0 line
items](https://docs.stripe.com/invoicing/line-item-grouping#hide-line-items)
The API also supports hiding individual 0 USD line items. For a specific line
item on the invoice, you can set `rendering[display]=hidden_if_zero` like the
following:

```
curl
https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/lines/{{INVOICE_LINE_ITEM_ID}}
\
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "rendering[display]"= "hidden_if_zero"
```

Then, if the line item is 0 USD, it is automatically hidden anywhere the
customer sees the invoice.

## Links

- [Group invoice line items](https://docs.stripe.com/invoicing/group-line-items)
- [privacy policy](https://stripe.com/privacy)
- [create](https://docs.stripe.com/api/invoices/create)
- [update](https://docs.stripe.com/api/invoices/update)