# TLS Certificates

## Learn how to make sure your integration securely communicates with Stripe.

Your integration connects to Stripe’s API securely over
[HTTPS](https://en.wikipedia.org/wiki/HTTPS)–the HTTP protocol encrypted over a
[Transport Security Layer
(TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) connection.
Whether you use Stripe managed SDKs, curl, or other HTTP clients to connect to
Stripe APIs, TLS ensures that you’re connecting to Stripe servers and that third
parties can’t read or modify API requests or responses.

## TLS certificates

[TLS certificates](https://www.digicert.com/tls-ssl/tls-ssl-certificates) are
how your integration verifies it’s connecting to a Stripe-owned server. A
digital certificate includes (but isn’t limited to) the host name of the server,
information about the owner of the server/domain, duration of validity, and the
identity of a trusted [certificate authority
(CA)](https://en.wikipedia.org/wiki/Certificate_authority) that issued or signed
this certificate. A client connecting to the server performs [path
validation](https://en.wikipedia.org/wiki/Certification_path_validation_algorithm)
on the certificate where it verifies that the subject field of the certificate
matches the domain name of the server that it’s trying to connect to, the
certificate isn’t expired, and that a trusted CA issued the certificate. For
more details, you can [read about
certificates](https://en.wikipedia.org/wiki/Public_key_certificate).

## Certificate pinning

When you connect to Stripe API endpoints, certificates load from a CA
certificates bundle that your operating system provides, or from browser or
Stripe Bindings (depending on the HTTP client used for this connection). These
certificates are treated as valid trusted certificates during certificate path
validation. Certificate pinning is the process of restricting which certificates
are considered valid for a particular HTTPS website or endpoint. Stripe
recommends against certificate pinning to avoid complications with your
integration when we roll out new certificates for our systems. DigiCert, one of
the major CAs, also recommends against [certificate
pinning](https://www.digicert.com/blog/certificate-pinning-what-is-certificate-pinning).

As a Stripe user, if you must use certificate pinning for some reason, make sure
you pin *only* (and **all** of) the **root** certificates listed
[below](https://docs.stripe.com/tls-certificates#root-certificates-for-stripe-domains).
Do **NOT** pin the entire certificate chain, the intermediate certificate, or
the end-entity (leaf) certificate. If you do, you run a high risk of breaking
your integration as Stripe updates certificates for our systems every few
months, including the intermediate CA certificates.

Our root certificates listed below might also change in the future, both
routinely and on an emergency basis. For routine changes to the list of root
certificates, Stripe will give seven days notice through the [API announce
mailing list](https://groups.google.com/a/lists.stripe.com/g/api-announce)
before we roll out the change. You **must** make sure that all your clients that
connect to Stripe APIs, including mobile applications, can handle this
certificate list changing with seven days notice. Emergency rotations might have
a shorter interval between notification and change.

### Root certificates for Stripe domains

- **DigiCert Global Root CA**

- Serial #: `08:3b:e0:56:90:42:46:b1:a1:75:6a:c9:59:91:c7:4a`
- SHA1 Fingerprint:
`a8:98:5d:3a:65:e5:e5:c4:b2:d7:d6:6d:40:c6:dd:2f:b1:9c:54:36`
- **DigiCert Global Root G2**

- Serial #: `03:3a:f1:e6:a7:11:a9:a0:bb:28:64:b1:1d:09:fa:e5`
- SHA1 Fingerprint:
`df:3c:24:f9:bf:d6:66:76:1b:26:80:73:fe:06:d1:cc:8d:4f:82:a4`
- **DigiCert Global Root G3**

- Serial #: `05:55:56:bc:f2:5e:a4:35:35:c3:a4:0f:d5:ab:45:72`
- SHA1 Fingerprint:
`7e:04:de:89:6a:3e:66:6d:00:e6:87:d3:3f:fa:d9:3b:e8:3d:34:9e`
- **DigiCert High Assurance EV Root CA**

- Serial #: `02:ac:5c:26:6a:0b:40:9b:8f:0b:79:f2:ae:46:25:77`
- SHA1 Fingerprint:
`5f:b7:ee:06:33:e2:59:db:ad:0c:4c:9a:e6:d3:8f:1a:61:c7:dc:25`
- **GlobalSign Root R3**

- Serial #: `04:00:00:00:00:01:21:58:53:08:a2`
- SHA1 Fingerprint:
`d6:9b:56:11:48:f0:1c:77:c5:45:78:c1:09:26:df:5b:85:69:76:ad`
- **GlobalSign Root R6**

- Serial #: `45:e6:bb:03:83:33:c3:85:65:48:e6:ff:45:51`
- SHA1 Fingerprint:
`80:94:64:0e:b5:a7:a1:ca:11:9c:1f:dd:d5:9f:81:02:63:a7:fb:d1`
- **GlobalSign ECC Root R5**

- Serial #: `60:59:49:e0:26:2e:bb:55:f9:0a:77:8a:71:f9:4a:d8:6c`
- SHA1 Fingerprint:
`1f:24:c6:30:cd:a4:18:ef:20:69:ff:ad:4f:dd:5f:46:3a:1b:69:aa`

You can verify and download the above root CA certificates from
[DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm) and
[GlobalSign](https://support.globalsign.com/ca-certificates/root-certificates/globalsign-root-certificates).

## Links

- [API announce mailing
list](https://groups.google.com/a/lists.stripe.com/g/api-announce)
- [HTTPS](https://en.wikipedia.org/wiki/HTTPS)
- [Transport Security Layer
(TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [TLS certificates](https://www.digicert.com/tls-ssl/tls-ssl-certificates)
- [certificate authority
(CA)](https://en.wikipedia.org/wiki/Certificate_authority)
- [path
validation](https://en.wikipedia.org/wiki/Certification_path_validation_algorithm)
- [read about
certificates](https://en.wikipedia.org/wiki/Public_key_certificate)
- [certificate
pinning](https://www.digicert.com/blog/certificate-pinning-what-is-certificate-pinning)
- [DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm)
-
[GlobalSign](https://support.globalsign.com/ca-certificates/root-certificates/globalsign-root-certificates)