# Python PGP key

## Learn how to use the Python client library PGP key.

If you’re unfamiliar with PGP, see [GPG](http://gnupg.org/) and start by
[importing a public key](http://www.gnupg.org/gph/en/manual.html#AEN84). After
you familiarize yourself with the basics of PGP, use this PGP key as it’s marked
as trusted for the [Python client
library](https://github.com/stripe/stripe-python).

#### Note

If you have any questions, or encounter any issues, please contact us at
[support-migrations@stripe.com](mailto:support-migrations@stripe.com).

### Python PGP key

After you import the key, you can encrypt files by running:

```
gpg --encrypt --recipient 05D02D3D57ABFF46 FILENAME

```

This creates **FILENAME.gpg** with the following information:

- **Key ID**: `05D02D3D57ABFF46`
- **Key type**: RSA
- **Key size**: 2048 bits
- **Fingerprint**: `C330 33E4 B583 FE61 2EDE 877C 05D0 2D3D 57AB FF46`
- **User ID**: `Stripe <security@stripe.com>`

## Links

- [GPG](http://gnupg.org)
- [importing a public key](http://www.gnupg.org/gph/en/manual.html#AEN84)
- [Python client library](https://github.com/stripe/stripe-python)