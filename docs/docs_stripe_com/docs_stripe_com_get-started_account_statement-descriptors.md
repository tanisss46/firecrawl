# Statement descriptors

## Learn how statement descriptors work.

Statement descriptors explain charges or payments on bank statements. Using
clear and accurate statement descriptors can reduce chargebacks and disputes.
Banks and card networks require the inclusion of certain types of information
that help customers understand their statements, and statement descriptors
provide this information.

When you activate your account, you can set a single statement descriptor
(static statement descriptor) that appears on all customer statements. For card
charges, you can also create a statement descriptor that contains a static
prefix associated with your account but with a dynamic suffix associated with
each charge. This enables you to specify details about the product, service, or
payment on bank or card statements.

Most banks display this information consistently, but some might display it
incorrectly or not at all.

## Statement descriptor requirements

A complete statement descriptor—either a single static descriptor or the
combination of a prefix and suffix—must meet the following requirements:

- Contains only Latin characters.
- Contains between 5 and 22 characters, inclusive.
- Contains at least one letter (if using a prefix and a suffix, both require at
least one letter).
- Doesn’t contain any of the following special characters: `<`, `>`, `\`, `'`
`"` `*`.
- Reflects your Doing Business As (DBA) name.
- Contains more than a single common term or common website URL. A website URL
only is acceptable if it provides a clear and accurate description of a
transaction on a customer’s statement.

A static prefix, also called a shortened descriptor in the Dashboard, must
contain between 2 and 10 characters, inclusive. The remaining characters are
reserved for the dynamic suffix.

## Set the static statement descriptor

You set a static statement descriptor or the shortened descriptor (prefix) in
the [Dashboard](https://dashboard.stripe.com/settings/public). This value
appears on all customer statements for charges or payments.

A static statement descriptor is sufficient if:

- Your business provides only a single product or service.
- Your customers understand a static value for any transaction with your
business.
- You prefer to provide the same statement descriptor for all transactions.

For card charges, consider a static prefix with dynamic suffix if:

- You provide multiple products or services.
- Your customers might not understand a single value for all their transactions
with your business.
- You prefer to provide transaction-specific details on the statement
descriptor.

You can set both the statement descriptor for non-card charges and the shortened
statement descriptor for card charges.

If you set the statement descriptor and don’t set a prefix (shortened
descriptor), then for card payments Stripe uses the statement descriptor as the
prefix. If the account statement descriptor is longer than 10 characters, we
truncate it as needed to fit the character limit.

## Set a dynamic suffix

Dynamic suffixes are supported only for card payments. Use the suffix to specify
details about the transaction so your customer can understand it clearly on
their statement. The suffix is concatenated with the prefix, the `*` symbol, and
a space to form the complete statement descriptor that your customer sees.

Make sure that the total length of the concatenated descriptor is no more than
22 characters, including the `*` symbol and the space. If the prefix is
`RUNCLUB` (7 characters), the dynamic suffix can contain up to 13 characters—for
example, `9-22-19 10K` (11 characters) or `OCT MARATHON` (12 characters). The
computed statement descriptor is `RUNCLUB* 9-22-19 10K` or `RUNCLUB* OCT
MARATHON`.

For card charges, providing a dynamic statement descriptor requires the
`statement_descriptor_suffix` value. For non-card charges, if you set a value
only for `statement_descriptor` on a PaymentIntent, Stripe uses it in place of
the account statement descriptor (static descriptor).

The following examples show how to add a suffix to the PaymentIntent object.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1099 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d statement_descriptor_suffix="example descriptor"
```

## Set the statement descriptor on non-card charges

Use the `statement_descriptor` parameter to set the complete statement
descriptor for non-card charges.

When creating a PaymentIntent, attempting to set this parameter for card charges
results in a 400 error. For payments made with a card, use
`statement_descriptor_suffix` instead.

## Set Japanese statement descriptors

Japanese businesses can set kanji and kana statement descriptors. Providing
clear and easy to understand statement descriptors is important to reduce
confusion and chargebacks. We recommend setting statement descriptors in all
three supported scripts (kanji, kana, and Latin characters).

You can change your account’s
[static](https://docs.stripe.com/get-started/account/statement-descriptors#static)
kanji and kana statement descriptors and shortened descriptors (prefix) in the
[Dashboard](https://dashboard.stripe.com/settings/public).

For card charges, you can set [dynamic
suffixes](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic)
in kanji and kana on PaymentIntents and Checkout Sessions. We compute the full
descriptor that cardholders see by concatenating the shortened prefix and
separators, in the same way as `statement_descriptor_suffix`.

The following example shows how to set kanji and kana suffixes on a
PaymentIntent.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=1000 \
 -d currency=jpy \
 -d "payment_method_types[]"=card \
 -d statement_descriptor_suffix="example descriptor" \
-d "payment_method_options[card][statement_descriptor_suffix_kanji]"="漢字サフィックス"
\
 -d "payment_method_options[card][statement_descriptor_suffix_kana]"="カナサフィックス"
```

### Requirements

While Japanese statement descriptors share some requirements with [
requirements](https://docs.stripe.com/get-started/account/statement-descriptors#requirements),
the following table shows additional requirements for kanji and kana
descriptors.

KanjiKanaMaximum total length1722Minimum prefix length12Maximum prefix
length1010Supported character typeKanji, kana, and LatinKanaValidation rule`< >
\ ' " * ＊` are not allowedOnly kana, spaces, dashes, and dots are allowed
#### Note

Total length is the length of either the static descriptor or the concatenated
descriptor (prefix + separator + suffix). Descriptors exceeding the maximum
length are truncated.

### Issuer behavior

Japanese statement descriptors are available only when both of the following are
true:

- The card is a Visa or Mastercard issued in Japan.
- The charge is processed by a Japanese business or on behalf of a Japanese
business.

For applicable charges, most issuers use a Japanese statement descriptor rather
than a Latin one. However, it’s ultimately up to the issuer to decide whether to
show kanji, kana, or Latin characters on the cardholder’s statement.

The
[calculated_statement_descriptor](https://docs.stripe.com/api/charges/object#charge_object-calculated_statement_descriptor)
in API responses is always the Latin statement descriptor, but that doesn’t
prevent the issuer from using a Japanese statement descriptor.

### Statement descriptor display timing

Kanji and kana statement descriptors are sent to issuers at time of payment
capture. As a result, they usually take a few days to appear on cardholder
statements. In the meantime a temporary descriptor might be visible to
cardholders:

- **Visa, Mastercard:** The -language statement descriptor.
- **JCB, Diners Club, and Discover:** The account’s default statement
descriptor.

## Links

- [Connect](https://docs.stripe.com/connect)
- [Set statement descriptors with
Connect](https://docs.stripe.com/connect/statement-descriptors)
- [Dashboard](https://dashboard.stripe.com/settings/public)
-
[static](https://docs.stripe.com/get-started/account/statement-descriptors#static)
- [dynamic
suffixes](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic)
- [
requirements](https://docs.stripe.com/get-started/account/statement-descriptors#requirements)
-
[calculated_statement_descriptor](https://docs.stripe.com/api/charges/object#charge_object-calculated_statement_descriptor)