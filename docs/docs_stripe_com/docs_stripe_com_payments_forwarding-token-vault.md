# Forward card details to your own token vault

## Update your in-house vault with card details stored on Stripe.

Create a [PaymentMethod](https://docs.stripe.com/api/payment_methods) and
[forward](https://docs.stripe.com/api/forwarding/request) the payment method to
your token vault.

#### Request access

To gain access to use Stripe’s forwarding service, contact [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F).

Server

Stripe

Token vault

Create a PaymentMethod

Stripe returns a PaymentMethod object

Call the Vault and Forward API with the PaymentMethod you provide

Stripe forwards the request with card data

Token vault endpoint returns a response

Stripe redacts identified PCI sensitive data and relays the response

Forward card details to your own token vault[Create a
PaymentMethod](https://docs.stripe.com/payments/forwarding-token-vault#create-payment-method)
To collect card details and send them to Stripe for use with the Vault and
Forward API, use the Payment Element to create [a
PaymentMethod](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy?type=payment#create-pm).
After you create a PaymentMethod, we automatically store card details in
Stripe’s PCI compliant vault. If you have your own frontend, you can still use
the Vault and Forward API by [creating a PaymentMethod
directly](https://docs.stripe.com/api/payment_methods/create).

[Create a
ForwardingRequest](https://docs.stripe.com/payments/forwarding-token-vault#create-forwarding-request)
Pass the PaymentMethod ID to the Request endpoint on your server. Stripe
provides a test endpoint (`https://forwarding-api-demo.stripedemos.com/tokens`)
and a test payment method (`pm_card_visa`) to verify that you can successfully
retrieve card credentials from Stripe’s vault. Send the card details to this
test endpoint before you connect your integration with your in-house vault.

```
curl https://api.stripe.com/v1/forwarding/requests \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_method=pm_card_visa \
 --data-urlencode url="https://forwarding-api-demo.stripedemos.com/tokens" \
 -d "request[headers][0][name]"=Authorization \
-d "request[headers][0][value]"="Bearer
eyJhbGciOiJIUzI1NiJ9.Zm9yd2FyZGluZy1hcGktZGVtbw.2qoK37CNBmMjMDRERSYUSE-YrjsTgGhHnxMeqOxjrAg"
\
--data-urlencode "request[body]"="{\"metadata\":{\"reference\":\"Your Token
Reference\"},\"card\":{\"number\":\"\",\"exp_month\":\"\",\"exp_year\":\"\",\"cvc\":\"\",\"name\":\"\"}}"
\
 -d "replacements[0]"=card_number \
 -d "replacements[1]"=card_expiry \
 -d "replacements[2]"=card_cvc \
 -d "replacements[3]"=cardholder_name
```

[Configure your in-house token vault
endpoint](https://docs.stripe.com/payments/forwarding-token-vault#configuring-in-house-vault)
To receive Primary Account Numbers (PANs) from the Vault and Forward API, your
token vault must comply with the following specifications.

### PCI compliance

Make sure that your vault is PCI compliant and provide a valid PCI Attestation
of Compliance to Stripe support. You must refresh this Attestation annually.

### API Requirements

Your vault must contain HTTPS-based APIs that accept JSON and return JSON
responses; other formats, such as XML or ISO 8583, aren’t supported.

Make sure that the API contains a single, static URL. Configure this in the
Vault and Forward API for security measures. Don’t change it between requests.

### Authentication

Use the Vault and Forward API to authenticate with your vault using HTTP header
based authentication schemes, including bearer tokens.

Make sure that every forwarded API call includes the authentication header to
authenticate with your vault.

We don’t support client certificate authentication.

### Request headers

You can include additional headers in the forwarded request to your vault.
However, you must verify that the configuration for your vault explicitly
supports these headers. Reach out to Stripe support before you begin your
integration to verify that the required additional headers are properly
configured. Additionally, make sure that the headers don’t include any sensitive
information, except for the bearer token.

### Request body

Make sure that your vault receives a JSON object with the following shape.

```
{
 "card": {
 "number": "4242424242424242",
 "exp_month": "12",
 "exp_year": "2023",
 "name": "John Doe",
 "cvc": "123"
 },
 "metadata": {
 // Put your additional fields here
 }
}
```

You can include additional fields as needed under the metadata key in this
request. We pass them through without any additional processing.

The Vault and Forward API places the decrypted data into the following fields:

Field nameTypeDescription`number`StringThe 15- or 16- digit PAN of the
card`exp_month`StringThe month of the card expiry`exp_year`StringThe four-digit
year of the card expiry`name`StringThe cardholder name`cvc`StringThe card
verification value. This only becomes available for the first API request to
Stripe after tokenization. We remove this information from our system after a
short time period. Don’t store this value.
You don’t need to support all of these fields in your vault. The Vault and
Forward API places values into the request only if they’re present in the
request body that you send to the Vault and Forward API. Additionally, you can
include additional fields in the request body, which the Vault and Forward API
passes to the receiving endpoint.

### Response body

The Vault and Forward API doesn’t require any response body from your vault. If
you provide a body, we return it to the caller of the Vault and Forward API.
Don’t include any sensitive fields in your response.

### Response codes

The Vault and Forward API treats any response as a “success” and returns the
same response code sent by the token vault endpoint back to the caller through
Stripe. For example, when the upstream returns a status code of `400` to Stripe,
the Vault and Forward API responds with a status code of `200`. The response
body includes the upstream’s `400` response and error message.

[Verify your integration with your token
vault](https://docs.stripe.com/payments/forwarding-token-vault#verifying-your-integration)
To confirm the correct functionality of your integration with the vault
endpoint, replace Stripe’s endpoint with your vault configuration. Then,
initiate a ForwardingRequest using the PaymentMethod you created.

[Update your token vault with the latest
credentials](https://docs.stripe.com/payments/forwarding-token-vault#update-your-vault)
Listen to Stripe webhooks to [learn if a card has been
updated](https://docs.stripe.com/payments/cards/overview#automatic-card-updates).
Call the Vault and Forward API to forward the updated PaymentMethod to your
token vault.

## Links

- [PaymentMethod](https://docs.stripe.com/api/payment_methods)
- [forward](https://docs.stripe.com/api/forwarding/request)
- [Stripe
support](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fsupport.stripe.com%2Fcontact%2Femail%3Fquestion%3Dother%26topic%3Dpayment_apis%26subject%3DHow%2520can%2520I%2520access%2520the%2520Vault%2520and%2520Forward%2520API%3F%26body%3DWhat%2520endpoint%28s%29%2520would%2520you%2520like%2520to%2520forward%2520card%2520details%2520to%3F)
- [a
PaymentMethod](https://docs.stripe.com/payments/finalize-payments-on-the-server-legacy?type=payment#create-pm)
- [creating a PaymentMethod
directly](https://docs.stripe.com/api/payment_methods/create)
-
[https://forwarding-api-demo.stripedemos.com/tokens](https://forwarding-api-demo.stripedemos.com/tokens)
- [learn if a card has been
updated](https://docs.stripe.com/payments/cards/overview#automatic-card-updates)