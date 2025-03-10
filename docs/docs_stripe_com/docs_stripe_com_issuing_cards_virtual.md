# Virtual cards with Issuing

## Learn about virtual cards created with Issuing.

You can retrieve or display virtual card details through the Dashboard, the API,
or by using [Issuing Elements](https://docs.stripe.com/issuing/elements).
[PCI-DSS](https://stripe.com/guides/pci-compliance) rules protect cardholder
data, and not all methods of card information retrieval are PCI-DSS compliant.

## Display virtual card details to cardholders

You can use [Issuing Elements](https://docs.stripe.com/issuing/elements) to
display virtual card details to your cardholders without this information
passing through your servers. This method is fully PCI-DSS compliant, and we
recommend it for most Issuing users. Stripe offers Issuing Elements as a part of
[Stripe.js](https://docs.stripe.com/js).

## Retrieve virtual card details

For PCI-DSS compliance, we recommend limiting retrieval of virtual card
information to the Dashboard or Issuing Elements. If you use the API to retrieve
card information, or if you export virtual card information from the Dashboard,
store it in a password manager or otherwise encrypt it.

You can retrieve both the full unredacted card number and CVC from the API. For
security reasons, you can only use these fields with virtual cards in live mode,
and we omit them unless you explicitly request them with the
[expand](https://docs.stripe.com/api/expanding_objects) property. You can only
retrieve these fields for physical cards in [test
mode](https://docs.stripe.com/keys#test-live-modes). Additionally, you can only
access them through the [Retrieve a
card](https://docs.stripe.com/api/issuing/cards/retrieve) endpoint.

```
curl -G https://api.stripe.com/v1/issuing/cards \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=number \
 -d "expand[]"=cvc
```

## Details about PCI-DSS

If you are generating virtual cards for your own use, you are not required to
attain PCI-DSS compliance for Issuing activity. If you are generating virtual
cards for use by your users, you may be considered a Service Provider under
PCI-DSS rules. Service Providers must be PCI-DSS compliant.

If you accept payments through Stripe, read more about your [PCI-DSS
obligations](https://stripe.com/guides/pci-compliance). These obligations are in
addition to requirements noted above.

## Links

- [Issuing Elements](https://docs.stripe.com/issuing/elements)
- [PCI-DSS](https://stripe.com/guides/pci-compliance)
- [Stripe.js](https://docs.stripe.com/js)
- [expand](https://docs.stripe.com/api/expanding_objects)
- [test mode](https://docs.stripe.com/keys#test-live-modes)
- [Retrieve a card](https://docs.stripe.com/api/issuing/cards/retrieve)