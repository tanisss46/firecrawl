# Integration security guide

## Ensure PCI compliance and secure customer-server communications.

PCI DSS is the global security standard for all entities that store, process, or
transmit cardholder or sensitive authentication data. PCI DSS sets a baseline
level of protection for consumers and helps reduce fraud and data breaches
across the entire payment ecosystem. Anyone involved with the processing,
transmission, or storage of card data must comply with the [Payment Card
Industry Data Security
Standard](https://www.pcisecuritystandards.org/pci_security/) (PCI DSS).

## Validate your PCI compliance

PCI compliance is a shared responsibility and applies to both Stripe and your
business:

- Stripe is certified annually by an independent PCI Qualified Security Assessor
(QSA) as a [PCI Level
1](https://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=stripe,%20inc)
Service Provider meeting all PCI requirements.
- As a business accepting payments, you must do so in a PCI-compliant manner,
and annually attest to this compliance.

Review the documentation requirements for your business in your
[Dashboard](https://dashboard.stripe.com/settings/compliance/documents) and
continue reading this guide to learn how Stripe can help you become PCI
compliant.

## Use low risk integrations

Some business models require the intake of untokenized PANs on a payment page.
If your business handles sensitive credit card data directly when accepting
payments, you might be required to meet the more than 300+ security controls in
PCI DSS. This might require you to purchase, implement, and maintain dedicated
security software and hardware, and hire external auditors to support your
annual assessment requirements.

Many business models don’t need to handle sensitive card data. You can instead
use one of our low risk [payment integrations](https://docs.stripe.com/payments)
to securely collect and transmit payment information directly to Stripe without
it passing through your servers, reducing your PCI obligations.

### Out-of-scope card data that you can safely store

Stripe returns non-sensitive card information in the response to a charge
request. This includes the card type, the last four digits of the card, and the
expiration date. This information isn’t subject to PCI compliance, so you can
store any of these properties in your database. Additionally, you can store
anything returned by our [API](https://docs.stripe.com/api).

## Use TLS and HTTPS

TLS refers to the process of securely transmitting data between the client—the
app or browser that your customer is using—and your server. The Secure Sockets
Layer (SSL) protocol originally performed this, but is outdated and no longer
secure. TLS replaced SSL, but the term *SSL* continues to be used colloquially
when referring to TLS and its function to protect transmitted data.

Payment pages must use a recent version (TLS 1.2 or above) because it
significantly reduces the risk of man-in-the-middle attacks for both you and
your customers. TLS attempts to accomplish the following:

- Encrypt and verify the integrity of traffic between the client and your
server.
- Verify that the client is communicating with the correct server. In practice,
this usually means verifying that the owner of the domain and the owner of the
server are the same entity. This helps prevent man-in-the-middle attacks.
Without it, there’s no guarantee that you’re encrypting traffic to the right
recipient.

Using TLS requires a *digital certificate*—a file issued by a certification
authority (CA). Installing this certificate assures the client that it’s
actually communicating with the server it expects to be talking to, and not an
impostor. Obtain a digital certificate from a reputable certificate provider,
such as:

- [Let’s Encrypt](https://letsencrypt.org/)
- [DigiCert](https://www.digicert.com/tls-ssl/basic-tls-ssl-certificates)
- [NameCheap](https://www.namecheap.com/security/ssl-certificates.aspx)

You can [test](https://docs.stripe.com/testing) your integration without using
HTTPS if you need to, and enable it when you’re ready to accept live charges.
However, all interactions between your server and Stripe must use HTTPS (that
is, when using our libraries).

### Set up TLS

To set up TLS:

- Purchase a certificate from a suitable provider.
- Configure your server to use the certificate. This step is complex, so follow
the installation guide of the provider you use.

As TLS is a complex suite of cryptographic tools, it’s easy to miss a few
details. We recommend using the [SSL Server
Test](https://www.ssllabs.com/ssltest/) by Qualys SSL Labs to make sure you set
up everything in a secure way.

## Security considerations

Including JavaScript from other sites makes your security dependent on theirs
and poses a security risk. If they’re ever compromised, an attacker could
execute arbitrary code on your page. In practice, many sites use JavaScript for
services like Google Analytics, even on secure pages. Nonetheless, we recommend
trying to minimize it.

If you’re using [webhooks](https://docs.stripe.com/webhooks), use TLS for the
endpoint to avoid traffic being intercepted and having notifications altered
(sensitive information is never included in a webhook event).

While complying with the Data Security Standards is important, it shouldn’t be
where you stop thinking about security. Some good resources to learn about web
security are:

- [OWASP](https://owasp.org/)
- [SANS](https://www.sans.org/reading-room/)
- [NIST](http://csrc.nist.gov/)

### Content Security Policy

If you’ve deployed a [Content Security
Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), the full set of
directives that Checkout, Connect embedded components, and Stripe.js require
are:

CheckoutConnect embedded componentsStripe.js- `connect-src`,
`https://checkout.stripe.com`
- `frame-src`, `https://checkout.stripe.com`
- `script-src`, `https://checkout.stripe.com`
- `img-src`, `https://*.stripe.com`

### Cross-origin isolation support

Currently, we don’t support [Cross-origin isolated
sites](https://web.dev/articles/cross-origin-isolation-guide).

Cross-origin isolation requires support by all dependencies, and several key
dependencies that enable our payment offerings don’t yet provide support for
this feature.

## See also

- [What is PCI DSS compliance](https://stripe.com/guides/pci-compliance)
- [Declines and failed payments](https://docs.stripe.com/declines)
- [Disputes overview](https://docs.stripe.com/disputes)

## Links

- [Payment Card Industry Data Security
Standard](https://www.pcisecuritystandards.org/pci_security/)
- [PCI Level
1](https://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=stripe,%20inc)
- [Dashboard](https://dashboard.stripe.com/settings/compliance/documents)
- [payment integrations](https://docs.stripe.com/payments)
- [API](https://docs.stripe.com/api)
- [mixed content warning](https://web.dev/what-is-mixed-content/)
- [Let’s Encrypt](https://letsencrypt.org/)
- [DigiCert](https://www.digicert.com/tls-ssl/basic-tls-ssl-certificates)
- [NameCheap](https://www.namecheap.com/security/ssl-certificates.aspx)
- [test](https://docs.stripe.com/testing)
- [SSL Server Test](https://www.ssllabs.com/ssltest/)
- [webhooks](https://docs.stripe.com/webhooks)
- [OWASP](https://owasp.org/)
- [SANS](https://www.sans.org/reading-room/)
- [NIST](http://csrc.nist.gov/)
- [Content Security
Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
- [Cross-origin isolated
sites](https://web.dev/articles/cross-origin-isolation-guide)
- [What is PCI DSS compliance](https://stripe.com/guides/pci-compliance)
- [Declines and failed payments](https://docs.stripe.com/declines)
- [Disputes overview](https://docs.stripe.com/disputes)