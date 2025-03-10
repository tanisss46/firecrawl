# Use the API to respond to disputes

## Learn how to manage disputes programmatically.

You can respond to disputes in the Stripe Dashboard, where we guide you through
submitting the optimal evidence for each [dispute
reason](https://docs.stripe.com/disputes/categories).

You can also programmatically manage disputes using the API. With the API, you
can upload evidence, respond to disputes, and receive dispute events using
webhooks.

## Retrieve a dispute

For details about a dispute,
[retrieve](https://docs.stripe.com/api#retrieve_dispute) a `Dispute` object:

```
curl https://api.stripe.com/v1/disputes/{{DISPUTE_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

The response contains information about the dispute and any response or evidence
that’s already been provided.

```
{
 object: "dispute"
 id: "{{DISPUTE_ID}}",
 charge: "ch_5Q4BjL06oPWwho",
 evidence: {
 customer_name: "Jane Austen",
 customer_purchase_ip: "127.0.0.1",
 product_description: "Widget ABC, color: red",
 shipping_tracking_number: "Z01234567890",
 uncategorized_text: "Additional notes and comments",
 },
 evidence_details: {
 due_by: 1403047735,
 submission_count: 1
 }
 ...
}
```

## Update a dispute

You [update](https://docs.stripe.com/api#update_dispute) the `Dispute` object
and pass structured evidence with the `evidence` parameter.

```
curl https://api.stripe.com/v1/disputes/{{DISPUTE_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 --data-urlencode "evidence[customer_email_address]"="email@example.com" \
 -d "evidence[shipping_date]"=2024-02-01 \
 -d "evidence[shipping_documentation]"={{FILE_ID}}
```

To view all available fields for the evidence parameter, see [Dispute
evidence](https://docs.stripe.com/api#dispute_evidence_object). There are two
types of evidence you can provide, depending on the field being updated:

- Text-based evidence, such as `customer_email` and `service_date`. These types
of evidence take a string of text.
- File-based evidence, such as `service_documentation` and
`customer_communication`. These take a
[file_upload](https://docs.stripe.com/api#file_object) object ID.

#### Note

The combined character count for all text-based evidence field submissions is
limited to 150,000.

You can provide documents or images (for example, a contract or screenshot) as
part of dispute evidence using the [File Upload
API](https://docs.stripe.com/file-upload). You first upload a document with the
purpose of `dispute_evidence`, which generates a `File_upload` object that you
can use when submitting evidence. Make sure the file meets [Stripe’s
recommendations](https://docs.stripe.com/disputes/best-practices#file-upload-recommendations)
before uploading it for evidence submission.

If you’re only interested in submitting a single file or a large amount of
plaintext as evidence, use `uncategorized_text` or `uncategorized_file`.
However, fill in as many fields as possible so you have the best chance at
overturning a dispute.

## Multiple disputes on a single payment

It’s not typical, but it’s possible for a customer to dispute the same payment
more than once. For example, a customer might partially dispute a payment for
one of the items in an order if it was damaged in delivery, and then file a
second dispute against a different item in the same order because the item
didn’t work properly.

Stripe distinguishes all disputes by a unique identifier, regardless of whether
they’re related to a single payment. When you [list
disputes](https://docs.stripe.com/api#list_disputes), you can filter the results
to show only disputes for a particular payment by specifying the `id` of the
`PaymentIntent` or `Charge` object and including the [payment_intent
filter](https://docs.stripe.com/api/disputes/list#list_disputes-charge) or
[charge
filter](https://docs.stripe.com/api/disputes/list#list_disputes-payment_intent).

By PaymentIntentBy Charge
```
curl -G https://api.stripe.com/v1/disputes \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent={{PAYMENT_INTENT_ID}}
```

When a payment has multiple disputes, use the `id` provided for each returned
dispute in the list to make sure you’re responding to the correct dispute by
specifying its `id` when you
[retrieve](https://docs.stripe.com/disputes/api#retrieve-a-dispute) or [update
the dispute](https://docs.stripe.com/disputes/api#update-a-dispute).

## See also

- [Dispute categories](https://docs.stripe.com/disputes/categories)
- [Measuring disputes](https://docs.stripe.com/disputes/measuring)
- [Preventing disputes and fraud](https://docs.stripe.com/disputes/prevention)

## Links

- [dispute reason](https://docs.stripe.com/disputes/categories)
- [retrieve](https://docs.stripe.com/api#retrieve_dispute)
- [update](https://docs.stripe.com/api#update_dispute)
- [Dispute evidence](https://docs.stripe.com/api#dispute_evidence_object)
- [file_upload](https://docs.stripe.com/api#file_object)
- [File Upload API](https://docs.stripe.com/file-upload)
- [Stripe’s
recommendations](https://docs.stripe.com/disputes/best-practices#file-upload-recommendations)
- [list disputes](https://docs.stripe.com/api#list_disputes)
- [payment_intent
filter](https://docs.stripe.com/api/disputes/list#list_disputes-charge)
- [charge
filter](https://docs.stripe.com/api/disputes/list#list_disputes-payment_intent)
- [Measuring disputes](https://docs.stripe.com/disputes/measuring)
- [Preventing disputes and fraud](https://docs.stripe.com/disputes/prevention)