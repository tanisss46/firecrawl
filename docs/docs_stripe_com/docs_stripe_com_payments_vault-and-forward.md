# Forward card details to third-party API endpoints

## Use the Vault and Forward API to securely share card details across multiple processors.

The Vault and Forward API allows you to tokenize and store card details in
Stripe’s PCI-compliant vault and route that data to supported processors or
endpoints. Leverage the API to:

- Use the [Payment Element](https://docs.stripe.com/payments/payment-element)
[across multiple
processors](https://docs.stripe.com/payments/forwarding-third-party-processors).
- Use Stripe as your primary vault for card details across processors.
- Route card details to your own [PCI compliant token
vault](https://docs.stripe.com/payments/forwarding-token-vault).

#### Request access

To gain access to use Stripe’s forwarding service, contact [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).

## Forward requests to destination endpoints and populate card details from Stripe’s vault

Server

Stripe

Destination endpoint

Create a PaymentMethod

Stripe returns a PaymentMethod object

Call the Vault and Forward API with the PaymentMethod you provide

Stripe forwards the request with card data

Destination endpoint returns a response

Stripe redacts identified PCI sensitive data and relays the response

API flows for forwarding card details[Collect card details and create a
PaymentMethod](https://docs.stripe.com/payments/vault-and-forward#collect-card-details)
To collect card details, use the Payment Element to create [a
PaymentMethod](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy?type=payment#create-pm).
After you create a PaymentMethod, we automatically store card details in
Stripe’s PCI compliant vault. If you have your own frontend, you can still use
the Vault and Forward API by [creating a PaymentMethod
directly](https://docs.stripe.com/api/payment_methods/create).

Typically, you can only reuse PaymentMethods by attaching them to a Customer.
However, the Vault and Forward API accepts all PaymentMethod objects, including
those not attached to a customer.

Similarly, the Vault and Forward API doesn’t
[confirm](https://docs.stripe.com/api/payment_intents/confirm) or
[capture](https://docs.stripe.com/api/payment_intents/capture) PaymentIntents.
As a result, you might unintentionally use them to capture a payment on Stripe
that was already captured on another processor.

CVCs expire automatically after a certain time period and also expire when used
with the Vault and Forward API. If you require a CVC after either of these
conditions are met, you must re-collect the card details.

[Create a
ForwardingRequest](https://docs.stripe.com/payments/vault-and-forward#create-fwd-request)
To send card details from Stripe’s vault, you must [Create a
ForwardingRequest](https://docs.stripe.com/api/forwarding/forwarding_requests/create)
and include the following parameters:

- `payment_method`: Object that enables Stripe to identify your customer’s card
details within Stripe’s vault and insert that data into the request body.
- `url`: The exact destination endpoint of your request.
- `request.body`: The API request body that you want to send to the destination
endpoint (for example, the payments request you send to another processor).
Leave any field where you normally input your customer’s card details blank.
- `replacements`: Fields that you want Stripe to substitute in the
`request.body`. The [available
fields](https://docs.stripe.com/api/forwarding/forwarding_requests/create#forwarding_request_create-replacements)
that we recommend always setting are `card_number`, `card_expiry`, `card_cvc`,
and `cardholder_name`. For example, including `card_number` in the
`replacements` array replaces the appropriate card number field for your
destination endpoint in the `request.body`.

#### Caution

Stripe might be more lenient than other processors in validating the cardholder
name field. If you use the `cardholder_name` replacements field, you’re
responsible for making sure that the names you use pass any validation enforced
by the destination endpoint. For example, if the destination endpoint expects
all names to only contain the letters A-Z with no accent marks or other writing
systems, you must make sure the card details you forward meet this requirement.
An alternative is to not use the `cardholder_name` replacements field and
specify the cardholder name in your request body directly in your request.

You must format your request based on the data that the destination endpoint
expects. In the example below, the destination endpoint expects an
`Idempotency-Key` header and accepts a JSON body with the payment details.

```
curl https://api.stripe.com/v1/forwarding/requests \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Idempotency-Key: {{IDEMPOTENCY_KEY}}" \
 -d payment_method={{PAYMENT_METHOD_ID}} \
 --data-urlencode url="https://endpoint-url/v1/payments" \
 -d "request[headers][0][name]"=Destination-API-Key \
 -d "request[headers][0][value]"={{DESTINATION_API_KEY}} \
 -d "request[headers][1][name]"=Destination-Idempotency-Key \
 -d "request[headers][1][value]"={{DESTINATION_IDEMPOTENCY_KEY}} \
--data-urlencode
"request[body]"="{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}"
\
 -d "replacements[0]"=card_number \
 -d "replacements[1]"=card_expiry \
 -d "replacements[2]"=card_cvc \
 -d "replacements[3]"=cardholder_name
```

#### Security tip

We require you to pass API keys for the destination endpoint on each API
request. Stripe forwards the request using the API keys you provide, and only
retains hashed and encrypted versions of destination endpoint API keys.

#### Caution

You can provide a `Idempotency-Key` to make sure that requests with the same key
result in only one outbound request. Use a different and unique key for Stripe
and any idempotency keys you provide on the underlying third-party request.

Use a new `Idempotency-Key` every time you make updates to `request.body` or
`request.header` fields. Passing in the older idempotency key results in the API
replaying older responses, including any previous validation errors or
destination endpoint errors. We recommend that you use a new idempotency key
when retrying requests that encountered an error reaching the destination
endpoint to make sure the request is retried at the destination.

[Forward the request with card
details](https://docs.stripe.com/payments/vault-and-forward#forward-request)
Stripe makes a request to the destination endpoint on your behalf by inserting
the card details from the PaymentMethod into the `request.body`. Where enabled
and available, the Card Account Updater (CAU) automatically attempts to update
and provide the latest available card details for requests.

Stripe then forwards the request to the destination endpoint. For example:

- Stripe makes a POST request to the endpoint:

```
POST /v1/payments HTTP/1.1
User-Agent: Stripe
Accept: */*
Host: endpoint-url
Content-Type: application/json
Content-Length: 321

```
- Stripe includes the following headers:

```
Destination-API-Key: {{DESTINATION_API_KEY}}
Destination-Idempotency-Key: {{DESTINATION_IDEMPOTENCY_KEY}}

```
- Stripe includes the following JSON body in the request:

```
{
 amount: {
 value: 1000,
 currency: 'usd'
 },
 paymentMethod: {
 number: '4242424242424242',
 expiryMonth: '03',
 expiryYear: '2030',
 cvc: '123',
 holderName: 'First Last',
 },
 reference: '{{REFERENCE_ID}}'
}

```

#### Note

If you’re using the Vault and the Forward API to make an authorization request,
you must handle any post-transaction actions, such as refunds or disputes,
directly with the third-party processor. Contact Stripe support if you require
3DS authentication across your multiprocessor setup.

[Handle the response from the destination
endpoint](https://docs.stripe.com/payments/vault-and-forward#return-response)
When you use the Vault and Forward API to forward card details to a third-party
processor, Stripe synchronously waits for a response from the destination
endpoint. The timeout period for this response is less than a minute. Stripe
redacts identified PCI-sensitive data, stores the redacted response from the
destination endpoint, and returns a
[ForwardingRequest](https://docs.stripe.com/api/forwarding/request/object)
object, which contains data about the request and response.

#### Caution

When you use the Vault and Forward API to forward card details to a third-party
processor, Stripe can’t guarantee that the processor will provide any particular
response to your forwarded API requests. If the third-party processor is
unresponsive, you must reach out directly to that processor to resolve the
issue.

```
{
 id: "fwdreq_123",
 object: "forwarding.request",
 payment_method: "{{PAYMENT_METHOD}}",
 request_details: {
 body: '{
 "amount": {
 "value": 1000,
 "currency": "usd"
 },
 "paymentMethod": {
 "number": "424242******4242",
 "expiryMonth": "03",
 "expiryYear": "2030",
 "cvc": "***",
 "holderName": "First Last",
 },
 "reference": "{{REFERENCE_ID}}"
 }',
 headers: [
 {
 name: "Content-Type",
 value: "application/json",
 },
 {
 name: "Destination-API-Key",
 value: "{{DESTINATION_API_KEY}}",
 },
 {
 name: "Destination-Idempotency-Key",
 value: "{{DESTINATION_IDEMPOTENCY_KEY}}",
 },
 ...
 ]
 },
 request_context: {
 "destination_duration": 234,
 "destination_ip_address": "35.190.113.80"
 },
 response_details: {
 body: '{
 // Response from the third-party endpoint goes here
 ...
 }',
 headers: [
 ...
 ],
 status: 200,
 },
 replacements: [
 "card_number",
 "card_expiry",
 "card_cvc",
 "cardholder_name"
 ]
 ...
}
```

## Configure your Vault and Forward API endpoint

To set up your Vault and Forward API endpoint, you must:

- [Confirm that we support the destination
endpoint](https://docs.stripe.com/payments/vault-and-forward#confirm-endpoint).
- Provide a test and production account with [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).
- [Share the production
details](https://docs.stripe.com/payments/vault-and-forward#share-production-details)
for the destination endpoint with [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).

### Confirm that we support the destination endpoint

Stripe supports forwarding API requests to the following endpoints:

- **Adyen**:- `[prefix]-checkout-live.adyenpayments.com/v68/payments`
- `[prefix]-checkout-live.adyenpayments.com/v68/storedPaymentMethods`
- `[prefix]-checkout-live.adyenpayments.com/v69/payments`
- `[prefix]-checkout-live.adyenpayments.com/v69/storedPaymentMethods`
- `[prefix]-checkout-live.adyenpayments.com/v70/payments`
- `[prefix]-checkout-live.adyenpayments.com/v70/storedPaymentMethods`
- `[prefix]-checkout-live.adyenpayments.com/v71/payments`
- `[prefix]-checkout-live.adyenpayments.com/v71/storedPaymentMethods`
- **Braintree**:- `payments.braintree-api.com/graphql`
- **Checkout**:- `api.checkout.com/tokens`
- `api.checkout.com/payments`
- **Fat Zebra**:- `gateway.pmnts.io/v1.0/credit_cards`
- **FlexPay**:- `api.flexpay.io/v1/gateways/charge`
- **GMO Payment Gateway**:- `p01.mul-pay.jp/payment/ExecTran.json`
- **PaymentsOS**:- `api.paymentsos.com/tokens`
- **SoftBank**- `stbfep.sps-system.com/api/xmlapi.do`
- **Spreedly**:- `core.spreedly.com/v1/payment_methods.json`
- **TabaPay**:- `[prefix]/v1/clients/[ClientID]/accounts`
- **Worldpay**:- `access.worldpay.com/api/payments`
- `access.worldpay.com/cardPayments/customerInitiatedTransactions`
- `access.worldpay.com/tokens`
- `secure.worldpay.com/jsp/merchant/xml/paymentService`
- [Your own PCI-compliant token
vault](https://docs.stripe.com/payments/forwarding-token-vault)

Stripe supports HTTPS-based APIs that accept JSON/XML requests and return
JSON/XML responses. If your destination endpoint isn’t supported or you require
a different API format, share the endpoint details with [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520Access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F)
to get support for your specific needs.

### Supported countries

The Vault and Forward API can only forward requests to the following countries:

### Countries eligible for request forwarding

Additionally, ensure that your Stripe account is registered in one of these
countries:

### Countries eligible for the Vault and Forward API

### Provide test accounts to Stripe support

To access the Vault and Forward API, share the [account
IDs](https://dashboard.stripe.com/settings/account) (`acct_xxxx`) for your test
accounts with [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).

### Share production details

Share the production details for destination endpoint with [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).
These include the following for destination endpoint: URL, HTTP method,
documentation, fields, request headers, and encryption keys. Stripe then sets up
destination endpoint for use with the Vault and Forward API in live mode.

To share third-party API keys, you must encrypt them by using the Stripe public
key that’s specific to the Vault and Forward API. Start by [importing a public
key](http://www.gnupg.org/gph/en/manual.html#AEN84) using [the GNU Privacy Guard
(PGP)](http://gnupg.org/). After you familiarize yourself with the basics of
PGP, use the following PGP key to encrypt your third-party API keys:

### Vault and Forward API PGP key

To encrypt your third-party API keys with the Vault and Forward API PGP key:

- Calculate the `SHA256` hash of your private key and hex encode the hash. Treat
this hash as a secret.

```
echo -n "{{THIRD_PARTY_SECRET_KEY}}" | sha256sum
```
- Encrypt the `SHA256` hash with Stripe’s public key, `Base64` encode the
result, and set the Stripe key as `trusted`.

```
echo -n "{{SHA256_HASH}}" | gpg -e -r AE863ADA1603150856C0A853A7B203177D034588
--always-trust | base64 > encrypted_base64.txt
```
- Verify `encrypted_base64.txt` by running the following command:

```
cat encrypted_base64.txt | base64 -d | gpg --list-only --list-packets
```

Make sure that `encrypted_base64.txt` contains the following characteristics:

- **Key ID**: `27E4B9436302901A`
- **Key type**: RSA
- **Key size**: 4096 bits
- **User ID**: `Forward API Secret Encryption Key (Forward API Secret Encryption
Key) <multiprocessor-ext@stripe.com>`

## Test your integration

To confirm that your integration works correctly with destination endpoint,
initiate a ForwardingRequest using the PaymentMethod you created. This example
uses `pm_card_visa` as a payment method.

```
curl https://api.stripe.com/v1/forwarding/requests \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Idempotency-Key: {{IDEMPOTENCY_KEY}}" \
 -d payment_method=pm_card_visa \
 -d url="{{DESTINATION ENDPOINT}}" \
 -d "request[headers][0][name]"=Destination-API-Key \
 -d "request[headers][0][value]"={{DESTINATION_API_KEY}} \
 -d "request[headers][1][name]"=Destination-Idempotency-Key \
 -d "request[headers][1][value]"={{DESTINATION_IDEMPOTENCY_KEY}} \
--data-urlencode
"request[body]"="{\"amount\":{\"value\":1000,\"currency\":\"usd\"},\"paymentMethod\":{\"number\":\"\",\"expiryMonth\":\"\",\"expiryYear\":\"\",\"cvc\":\"\",\"holderName\":\"\"},\"reference\":\"{{REFERENCE_ID}}\"}"
\
 -d "replacements[0]"=card_number \
 -d "replacements[1]"=card_expiry \
 -d "replacements[2]"=card_cvc \
 -d "replacements[3]"=cardholder_name
```

#### Caution

The Vault and Forward API treats any response from the destination endpoint as a
`success` and returns a `200`, along with the destination endpoint’s response
code in the `response.body`. For example, when the destination endpoint returns
a status code of `400` to Stripe, the Vault and Forward API responds with a
status code of `200`. The `response.body` includes the destination endpoint’s
`400` response and error message. Separately test the API request that you send
to your destination endpoint to make sure that you don’t have any errors.

### View your request logs in the Dashboard

You can view request logs and errors related to the Vault and Forward API in
[Workbench](https://docs.stripe.com/workbench#request-logs). Additionally, you
can use the [List
API](https://docs.stripe.com/api/forwarding/forwarding_requests/list) to fetch
the logs from Stripe.

#### Security tip

The `request.headers` and `request.body` in the incoming request are encrypted
and appear as `encrypted_request` in the Dashboard.

## Links

- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [across multiple
processors](https://docs.stripe.com/payments/forwarding-third-party-processors)
- [PCI compliant token
vault](https://docs.stripe.com/payments/forwarding-token-vault)
- [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F)
- [a
PaymentMethod](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy?type=payment#create-pm)
- [creating a PaymentMethod
directly](https://docs.stripe.com/api/payment_methods/create)
- [confirm](https://docs.stripe.com/api/payment_intents/confirm)
- [capture](https://docs.stripe.com/api/payment_intents/capture)
- [Create a
ForwardingRequest](https://docs.stripe.com/api/forwarding/forwarding_requests/create)
- [available
fields](https://docs.stripe.com/api/forwarding/forwarding_requests/create#forwarding_request_create-replacements)
- [ForwardingRequest](https://docs.stripe.com/api/forwarding/request/object)
- [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520Access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F)
- [account IDs](https://dashboard.stripe.com/settings/account)
- [importing a public key](http://www.gnupg.org/gph/en/manual.html#AEN84)
- [the GNU Privacy Guard (PGP)](http://gnupg.org)
- [Workbench](https://docs.stripe.com/workbench#request-logs)
- [List API](https://docs.stripe.com/api/forwarding/forwarding_requests/list)