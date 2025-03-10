# [Create a card token](https://docs.stripe.com/api/tokens/create_card)

Creates a single-use token that represents a credit card’s details. You can use
this token in place of a credit card dictionary with any v1 API method. You can
only use these tokens once by [creating a new Charge
object](https://docs.stripe.com/api/tokens/create_card#create_charge) or by
attaching them to a [Customer
object](https://docs.stripe.com/api/tokens/create_card#create_customer).

To use this functionality, you need to [enable access to the raw card data
APIs](https://support.stripe.com/questions/enabling-access-to-raw-card-data-apis).
In most cases, you can use our recommended [payments
integrations](https://docs.stripe.com/payments) instead of using the API.

### Parameters

- #### cardobject | string

The card this token will represent. If you also pass in a customer, the card
must be the ID of a card belonging to the customer. Otherwise, if you do not
pass in a customer, this is a dictionary containing a user’s credit card
details, with the options described below.

Show child parameters

### Returns

Returns the created card token if it’s successful. Otherwise, this call raises
[an error](https://docs.stripe.com/api/tokens/create_card#errors).

POST /v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/tokens \ -u
"sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \ -d
"card[number]"=4242424242424242 \ -d "card[exp_month]"=5 \ -d
"card[exp_year]"=2026 \ -d "card[cvc]"=314
```

Response
```
{ "id": "tok_1N3T00LkdIwHu7ixt44h1F8k", "object": "token", "card": { "id":
"card_1N3T00LkdIwHu7ixRdxpVI1Q", "object": "card", "address_city": null,
"address_country": null, "address_line1": null, "address_line1_check": null,
"address_line2": null, "address_state": null, "address_zip": null,
"address_zip_check": null, "brand": "Visa", "country": "US", "cvc_check":
"unchecked", "dynamic_last4": null, "exp_month": 5, "exp_year": 2026,
"fingerprint": "mToisGZ01V71BCos", "funding": "credit", "last4": "4242",
"metadata": {}, "name": null, "tokenization_method": null, "wallet": null },
"client_ip": "52.35.78.6", "created": 1683071568, "livemode": false, "type":
"card", "used": false}
```

# [Create a CVC update token](https://docs.stripe.com/api/tokens/create_cvc_update)

Creates a single-use token that represents an updated CVC value that you can use
for [CVC
re-collection](https://docs.stripe.com/payments/accept-a-payment-synchronously#web-recollect-cvc).
Use this token when [you confirm a card
payment](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-cvc_token)
or use a saved card on a `PaymentIntent` with `confirmation_method: manual`.

For most cases, use our [JavaScript
library](https://docs.stripe.com/js/tokens/create_token?type=cvc_update) instead
of using the API. For a `PaymentIntent` with `confirmation_method: automatic`,
use our recommended [payments
integration](https://docs.stripe.com/payments/save-during-payment#web-recollect-cvc)
without tokenizing the CVC value.

### Parameters

- #### cvc_updateobjectRequired

The updated CVC value this token represents.

Show child parameters

### Returns

Returns the created CVC update token if it’s successful. Otherwise, this call
raises [an error](https://docs.stripe.com/api/tokens/create_card#errors).

POST /v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/tokens \ -u
"sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \ -d
"cvc_update[cvc]"=123
```

Response
```
{ "id": "cvctok_1NkWsu2eZvKYlo2CFDm6ab7X", "object": "token", "client_ip": null,
"created": 1693334608, "livemode": false, "redaction": null, "type":
"cvc_update", "used": false}
```

# [Create a person token](https://docs.stripe.com/api/tokens/create_person)

Creates a single-use token that represents the details for a person. Use this
when you create or update persons associated with a Connect account. Learn more
about [account tokens](https://docs.stripe.com/connect/account-tokens).

You can only create person tokens with your application’s publishable key and in
live mode. You can use your application’s secret key to create person tokens
only in test mode.

### Parameters

- #### personobjectRequired

Information for the person this token represents.

Show child parameters

### Returns

Returns the created person token if it’s successful. Otherwise, this call raises
[an error](https://docs.stripe.com/api/tokens/create_card#errors).

POST /v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/tokens \ -u
"sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \ -d
"person[first_name]"=Jane \ -d "person[last_name]"=Doe \ -d
"person[relationship][owner]"=true
```

Response
```
{ "id": "cpt_1EDww82eZvKYlo2CsdelTHFu", "object": "token", "client_ip":
"8.21.168.117", "created": 1552582904, "livemode": false, "redaction": null,
"type": "person", "used": false}
```

# [Create a PII token](https://docs.stripe.com/api/tokens/create_pii)

Creates a single-use token that represents the details of personally
identifiable information (PII). You can use this token in place of an
[id_number](https://docs.stripe.com/api/tokens/create_card#update_account-individual-id_number)
or
[id_number_secondary](https://docs.stripe.com/api/tokens/create_card#update_account-individual-id_number_secondary)
in Account or Person Update API methods. You can only use a PII token once.

### Parameters

- #### piiobjectRequired

The PII this token represents.

Show child parameters

### Returns

Returns the created PII token if it’s successful. Otherwise, this call raises
[an error](https://docs.stripe.com/api/tokens/create_card#errors).

POST /v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/tokens \ -u
"sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \ -d
"pii[id_number]"=000000000
```

Response
```
{ "id": "pii_18PwbX2eZvKYlo2CzRXgwN3J", "object": "token", "client_ip":
"124.123.76.134", "created": 1466783547, "livemode": false, "redaction": null,
"type": "pii", "used": false}
```

# [Retrieve a token](https://docs.stripe.com/api/tokens/retrieve)

Retrieves the token with the given ID.

### Parameters

No parameters.

### Returns

Returns a token if you provide a valid ID. Raises [an
error](https://docs.stripe.com/api/tokens/create_card#errors) otherwise.

GET /v1/tokens/:idServer-side languageStripe
CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/tokens/tok_1N3T00LkdIwHu7ixt44h1F8k \ -u
"sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

Response
```
{ "id": "tok_1N3T00LkdIwHu7ixt44h1F8k", "object": "token", "card": { "id":
"card_1N3T00LkdIwHu7ixRdxpVI1Q", "object": "card", "address_city": null,
"address_country": null, "address_line1": null, "address_line1_check": null,
"address_line2": null, "address_state": null, "address_zip": null,
"address_zip_check": null, "brand": "Visa", "country": "US", "cvc_check":
"unchecked", "dynamic_last4": null, "exp_month": 5, "exp_year": 2026,
"fingerprint": "mToisGZ01V71BCos", "funding": "credit", "last4": "4242",
"metadata": {}, "name": null, "tokenization_method": null, "wallet": null },
"client_ip": "52.35.78.6", "created": 1683071568, "livemode": false, "type":
"card", "used": false}
```

## Links

- [Create a card token](https://docs.stripe.com/api/tokens/create_card)
- [enable access to the raw card data
APIs](https://support.stripe.com/questions/enabling-access-to-raw-card-data-apis)
- [payments integrations](https://docs.stripe.com/payments)
- [Create a CVC update
token](https://docs.stripe.com/api/tokens/create_cvc_update)
- [CVC
re-collection](https://docs.stripe.com/payments/accept-a-payment-synchronously#web-recollect-cvc)
- [you confirm a card
payment](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-cvc_token)
- [JavaScript
library](https://docs.stripe.com/js/tokens/create_token?type=cvc_update)
- [payments
integration](https://docs.stripe.com/payments/save-during-payment#web-recollect-cvc)
- [Create a person token](https://docs.stripe.com/api/tokens/create_person)
- [account tokens](https://docs.stripe.com/connect/account-tokens)
- [Create a PII token](https://docs.stripe.com/api/tokens/create_pii)
- [Retrieve a token](https://docs.stripe.com/api/tokens/retrieve)