# [The Token object](https://docs.stripe.com/api/tokens/object)

### Attributes

- #### idstring

Unique identifier for the object.
- #### cardnullable object

Hash describing the card used to make the charge.

Show child attributes

### More attributesExpand all

- #### objectstring
- #### bank_accountnullable object
- #### client_ipnullable string
- #### createdtimestamp
- #### descriptionnullable string
- #### livemodeboolean
- #### typestring
- #### usedboolean
The Token object
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

# [Create an account token](https://docs.stripe.com/api/tokens/create_account)

Creates a single-use token that wraps a user’s legal entity information. Use
this when creating or updating a Connect account. Learn more about [account
tokens](https://docs.stripe.com/connect/account-tokens).

In live mode, you can only create account tokens with your application’s
publishable key. In test mode, you can only create account tokens with your
secret key or publishable key.

### Parameters

- #### accountobjectRequired

Information for the account this token represents.

Show child parameters

### Returns

Returns the created account token if it’s successful. Otherwise, this call
raises [an error](https://docs.stripe.com/api/tokens/object#errors).

POST /v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/tokens \ -u
"sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \ -d
"account[business_type]"=individual \ -d "account[individual][first_name]"=Jane
\ -d "account[individual][last_name]"=Doe \ -d
"account[tos_shown_and_accepted]"=true
```

Response
```
{ "id": "ct_1BZ6xr2eZvKYlo2CsSOhuTfi", "object": "token", "client_ip":
"104.198.25.169", "created": 1513297331, "livemode": false, "redaction": null,
"type": "account", "used": false}
```

# [Create a bank account token](https://docs.stripe.com/api/tokens/create_bank_account)

Creates a single-use token that represents a bank account’s details. You can use
this token with any v1 API method in place of a bank account dictionary. You can
only use this token once. To do so, attach it to a [connected
account](https://docs.stripe.com/api/tokens/object#accounts) where
[controller.requirement_collection](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
is `application`, which includes Custom accounts.

### Parameters

- #### bank_accountobject

The bank account this token will represent.

Show child parameters

### More parametersExpand all

- #### customerstringConnect only

### Returns

Returns the created bank account token if it’s successful. Otherwise, this call
raises [an error](https://docs.stripe.com/api/tokens/object#errors).

POST /v1/tokensServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby
```
curl https://api.stripe.com/v1/tokens \ -u
"sk_test_BQokikJ...2HlWgH4olfQ2sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \ -d
"bank_account[country]"=US \ -d "bank_account[currency]"=usd \ -d
"bank_account[account_holder_name]"="Jenny Rosen" \ -d
"bank_account[account_holder_type]"=individual \ -d
"bank_account[routing_number]"=110000000 \ -d
"bank_account[account_number]"=000123456789
```

Response
```
{ "id": "tok_1N3T00LkdIwHu7ixt44h1F8k", "object": "token", "bank_account": {
"id": "ba_1NWScr2eZvKYlo2C8MgV5Cwn", "object": "bank_account",
"account_holder_name": "Jenny Rosen", "account_holder_type": "individual",
"account_type": null, "bank_name": "STRIPE TEST BANK", "country": "US",
"currency": "usd", "fingerprint": "1JWtPxqbdX5Gamtz", "last4": "6789",
"routing_number": "110000000", "status": "new" }, "client_ip": null, "created":
1689981645, "livemode": false, "redaction": null, "type": "bank_account",
"used": false}
```

# [Create a card token](https://docs.stripe.com/api/tokens/create_card)

Creates a single-use token that represents a credit card’s details. You can use
this token in place of a credit card dictionary with any v1 API method. You can
only use these tokens once by [creating a new Charge
object](https://docs.stripe.com/api/tokens/object#create_charge) or by attaching
them to a [Customer
object](https://docs.stripe.com/api/tokens/object#create_customer).

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
[an error](https://docs.stripe.com/api/tokens/object#errors).

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
raises [an error](https://docs.stripe.com/api/tokens/object#errors).

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

## Links

- [The Token object](https://docs.stripe.com/api/tokens/object)
- [Create an account token](https://docs.stripe.com/api/tokens/create_account)
- [account tokens](https://docs.stripe.com/connect/account-tokens)
- [Create a bank account
token](https://docs.stripe.com/api/tokens/create_bank_account)
-
[controller.requirement_collection](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection)
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