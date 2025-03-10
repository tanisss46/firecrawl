# Add custom fields

## Add additional fields to a prebuilt payment page with Checkout.

Stripe-hosted pageEmbedded formEmbedded componentsPublic preview
You can add custom fields on the payment form to collect additional information
from your customers. The information is available after the payment is complete
and is useful for fulfilling the purchase.

Custom fields have the following limitations:

- Up to three fields allowed.
- Not available in `setup` mode.
- Support for up to 255 characters on text fields.
- Support for up to 255 digits on numeric fields.
- Support for up to 200 options on dropdown fields.

#### Caution

Don’t use custom fields to collect personal, protected, or sensitive data, or
information restricted by law.

[Create a Checkout
Session](https://docs.stripe.com/payments/checkout/custom-fields#create-session)
Create a Checkout Session while specifying an array of [custom
fields](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_fields).
Each field must have a unique `key` that your integration uses to reconcile the
field. Also provide a label for the field that you display to your customer.
Labels for custom fields aren’t translated, but you can use the
[locale](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-locale)
parameter to set the language of your Checkout Session to match the same
language as your labels.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "custom_fields[0][key]"=engraving \
 -d "custom_fields[0][label][type]"=custom \
 -d "custom_fields[0][label][custom]"="Personalized engraving" \
 -d "custom_fields[0][type]"=text
```

![A checkout page with custom
fields](https://b.stripecdn.com/docs-statics-srv/assets/required.ba6d59544fa4519cf4eb2a1764e016cf.png)

[Retrieve custom
fields](https://docs.stripe.com/payments/checkout/custom-fields#retrieve-fields)
When your customer completes the Checkout Session, we send a
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
[webhook](https://docs.stripe.com/webhooks) with the completed fields.

Example `checkout.session.completed` payload:

```
{
 "id": "evt_1Ep24XHssDVaQm2PpwS19Yt0",
 "object": "event",
 "api_version": "2022-11-15",
 "created": 1664928000,
 "data": {
 "object": {
 "id": "cs_test_MlZAaTXUMHjWZ7DcXjusJnDU4MxPalbtL5eYrmS2GKxqscDtpJq8QM0k",
 "object": "checkout.session",
 "custom_fields": [{
 "key": "engraving",
 "label": {
 "type": "custom",
 "custom": "Personalized engraving"
 },
 "optional": false,
 "type": "text",
 "text": {
 "value": "Jane",
 }
 }],
 "mode": "payment",
 }
 },
 "livemode": false,
 "pending_webhooks": 1,
 "request": {
 "id": null,
 "idempotency_key": null
 },
 "type": "checkout.session.completed"
}
```

[Use a custom
field](https://docs.stripe.com/payments/checkout/custom-fields#use-custom-field)
### Mark a field as optional

By default, customers must complete all fields before completing payment. To
mark a field as optional, pass in `optional=true`.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "custom_fields[0][key]"=engraving \
 -d "custom_fields[0][label][type]"=custom \
 -d "custom_fields[0][label][custom]"="Personalized engraving" \
 -d "custom_fields[0][type]"=text \
 -d "custom_fields[0][optional]"=true
```

!

### Add a dropdown field

A dropdown field presents your customers with a list of options to select from.
To create a dropdown field, specify `type=dropdown` and a list of options, each
with a `label` and a `value`. The `label` displays to the customer while your
integration uses the `value` to reconcile which option the customer selected.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "custom_fields[0][key]"=sample \
 -d "custom_fields[0][label][type]"=custom \
 -d "custom_fields[0][label][custom]"="Free sample" \
 -d "custom_fields[0][optional]"=true \
 -d "custom_fields[0][type]"=dropdown \
 -d "custom_fields[0][dropdown][options][0][label]"="Balm sample" \
 -d "custom_fields[0][dropdown][options][0][value]"=balm \
 -d "custom_fields[0][dropdown][options][1][label]"="BB cream sample" \
 -d "custom_fields[0][dropdown][options][1][value]"=cream
```

![A checkout page with a dropdown
field](https://b.stripecdn.com/docs-statics-srv/assets/dropdown.4501d199ebe009030c2be6935cfdf2dd.png)

### Add a numbers only field

A numbers-only field provides your customers a text field that only accepts
numerical values, up to 255 digits. To create a numbers-only field, specify
`type=numeric`.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "custom_fields[0][key]"=invoice \
 -d "custom_fields[0][label][type]"=custom \
 -d "custom_fields[0][label][custom]"="Invoice number" \
 -d "custom_fields[0][type]"=numeric
```

### Retrieve custom fields for a subscription

You can retrieve the custom fields associated with a subscription by querying
for the Checkout Session that created it using the
[subscription](https://docs.stripe.com/api/checkout/sessions/list#list_checkout_sessions-subscription)
parameter.

```
curl -G https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d subscription={{SUBSCRIPTION_ID}}
```

### Add character length validations

You can optionally specify a minimum and maximum character length
[requirement](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_fields-numeric-maximum_length)
for `text` and `numeric` field types.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "custom_fields[0][key]"=engraving \
 -d "custom_fields[0][label][type]"=custom \
 -d "custom_fields[0][label][custom]"="Personalized engraving" \
 -d "custom_fields[0][type]"=text \
 -d "custom_fields[0][text][minimum_length]"=10 \
 -d "custom_fields[0][text][maximum_length]"=20 \
 -d "custom_fields[0][optional]"=true
```

![A field with character
limits](https://b.stripecdn.com/docs-statics-srv/assets/between-validation.20431cd8e0c03a028843945d1f1ea314.png)

### Add default values

You can optionally provide a default value for the
[text](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_fields-text-default_value),
[numeric](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_fields-numeric-default_value),
and
[dropdown](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_fields-dropdown-default_value)
field types. Default values are prefilled on the payment page.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d mode=payment \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel" \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "custom_fields[0][key]"=engraving \
 -d "custom_fields[0][label][type]"=custom \
 -d "custom_fields[0][label][custom]"="Personalized engraving" \
 -d "custom_fields[0][type]"=text \
 -d "custom_fields[0][text][default_value]"=Stella \
 -d "custom_fields[1][key]"=size \
 -d "custom_fields[1][label][type]"=custom \
 -d "custom_fields[1][label][custom]"=Size \
 -d "custom_fields[1][type]"=dropdown \
 -d "custom_fields[1][dropdown][default_value]"=small \
 -d "custom_fields[1][dropdown][options][0][value]"=small \
 -d "custom_fields[1][dropdown][options][0][label]"=Small \
 -d "custom_fields[1][dropdown][options][1][value]"=large \
 -d "custom_fields[1][dropdown][options][1][label]"=Large
```

## Links

- [custom
fields](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_fields)
-
[locale](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-locale)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [webhook](https://docs.stripe.com/webhooks)
-
[subscription](https://docs.stripe.com/api/checkout/sessions/list#list_checkout_sessions-subscription)
-
[requirement](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_fields-numeric-maximum_length)
-
[text](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_fields-text-default_value)
-
[numeric](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_fields-numeric-default_value)
-
[dropdown](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-custom_fields-dropdown-default_value)