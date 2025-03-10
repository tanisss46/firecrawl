# Set statement descriptors with Connect

## Learn how statement descriptors work for charges with Connect.

Statement descriptors explain charges or payments on bank statements and include
information that banks and card networks require to help customers understand
their statements. Familiarize yourself with the [requirements for statement
descriptors](https://docs.stripe.com/get-started/account/statement-descriptors).

## Set the static component for a connected account

Statement descriptors contain a static component and, optionally, a dynamic
part. The static component refers to either:

- The entire statement descriptor is static
([settings.payments.statement_descriptor](https://docs.stripe.com/api/accounts/object#account_object-settings-payments-statement_descriptor)).
- The first half of the statement descriptor is static
([settings.card_payments.statement_descriptor_prefix](https://docs.stripe.com/api/accounts/object#account_object-settings-card_payments-statement_descriptor_prefix))
and the second half is dynamically set from the payment.

Your platform and connected accounts with the `card_payments` capability must
have a statement descriptor and, optionally, a statement descriptor prefix. Both
values must be at least 5 characters in length. For a given payment, the
statement descriptor of the platform or the connected account applies depending
on [the charge type](https://docs.stripe.com/connect/charges).

The statement descriptor is set in one of the following ways:

- With a [create or update account](https://docs.stripe.com/api/accounts) API
call
- During Stripe-hosted or embedded onboarding
- Through the full Stripe Dashboard or Express Dashboard

Connected accounts with access to a Stripe-hosted dashboard can update their own
statement descriptor settings.

You can prefill an account’s statement descriptor and prefix when you call the
[create account](https://docs.stripe.com/api/accounts/create) endpoint. During
Stripe-hosted or embedded onboarding, If
`settings.payments.statement_descriptor` or
`settings.card_payments.statement_descriptor_prefix` isn’t set, Stripe sets them
based on information provided about the account during onboarding. If sufficient
information isn’t available, Stripe prompts connected accounts to set their own
statement descriptors during onboarding.

After onboarding an account that doesn’t have access to the full Stripe
Dashboard, you can update its `settings.payments.statement_descriptor` and
`settings.card_payments.statement_descriptor_prefix` by calling the [update
account](https://docs.stripe.com/api/accounts/update) endpoint.

For accounts where the platform handles onboarding, you must set their statement
descriptor.

With controller propertiesWith account type
```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[fees][payer]"=application \
 -d "controller[losses][payments]"=application \
 -d "controller[requirement_collection]"=application \
 -d country=US \
 -d business_type=company \
 -d "business_profile[name]"="Runners Club" \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true \
 -d "settings[payments][statement_descriptor]"="RUNNERS CLUB"
```

As of [API version 2023-10-16](https://docs.stripe.com/upgrades#2023-10-16),
there is new logic around updating statement descriptors.

- If you update an account’s `business_profile.name`, `business_profile.url`, or
the name of the company or individual and the existing statement descriptor is
based on lower precedence data, Stripe automatically resets the statement
descriptor to match the higher precedence value. For example, if the statement
descriptor is automatically set based on the URL, then you set or update
`business_profile.name`, Stripe resets the statement descriptor to match the
business profile name. If the statement descriptor is automatically set based on
`business_profile.name`, and you set or update the name of the company or
individual, the statement descriptor doesn’t reset because
`business_profile.name` has higher precedence. The precedence order is
`business_profile.name`, `business_profile.url`, then the name of the company or
individual.
- Any update to an account’s full statement descriptor causes Stripe to
automatically set the statement descriptor prefix to a shortened version of the
updated statement descriptor, even if the previous prefix is manually set.

## Statement descriptor usage

The full statement descriptor is provided to the bank or card network processing
the payment. Only the first 22 characters of the full statement descriptor are
sent for card payments.

The customer’s statement uses the platform account’s [static
component](https://docs.stripe.com/connect/statement-descriptors#set-the-static-component-for-a-connected-account)
for the following charge types:

- Destination charges without `on_behalf_of`
- Separate charges and transfers without `on_behalf_of`

The customer’s statement uses the connected account’s [static
component](https://docs.stripe.com/connect/statement-descriptors#set-the-static-component-for-a-connected-account)
for the following charge types:

- Direct charges
- Destination charges with `on_behalf_of`
- Separate charges and transfers with `on_behalf_of`

Using the static component from a connected account requires the account to have
the
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments)
capability.

#### Caution

For API versions `2019-02-19` and later, the
[statement_descriptor](https://docs.stripe.com/api/charges/create#create_charge-statement_descriptor)
parameter of `/v1/charges` is treated as the dynamic component, and is
equivalent to providing `statement_descriptor_suffix`.

If both `statement_descriptor_suffix` and `statement_descriptor` are provided,
only `statement_descriptor_suffix` is used.

For API versions prior to `2019-02-19`, the statement descriptor parameters on
`/v1/charges` are ignored and the platform’s static statement descriptor is
used.

Along with a statement descriptor, additional information about the business is
sent to display on the customer’s statement (for example, address, email, phone,
and URL). The additional information defaults to the support properties of the
account’s
[business_profile](https://docs.stripe.com/api/accounts/object#account_object-business_profile).
If a support field isn’t provided, the platform support field is used. If the
platform support field isn’t available, the account’s identity information is
provided instead.

### on_behalf_of behaviors

For charges with `on_behalf_of` set, statement descriptor and business
information are first looked up from the specified account. If that information
isn’t set, the platform’s information is used.

- If the charge has a dynamic component, the connected account’s
[settings.card_payments.statement_descriptor_prefix](https://docs.stripe.com/api/accounts/object#account_object-settings-payments-statement_descriptor_prefix)
static component is used. If the connected account doesn’t have a statement
descriptor prefix set, the platform’s statement descriptor prefix is used
instead.
- If the connected account’s business profile information isn’t set, the
platform’s information is used instead (first the platform’s business profile,
then the platform’s identity information). For example, if the connected account
doesn’t have a `support_phone` set, the platform’s `support_phone` or identity
phone number is provided.

If you use a dynamic suffix on a charge that uses the connected account’s static
descriptor, we recommend setting a prefix to on the connected account so the
complete statement descriptor appears as intended.

With controller propertiesWith account type
```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[fees][payer]"=application \
 -d "controller[losses][payments]"=application \
 -d "controller[requirement_collection]"=application \
 -d country=US \
 -d business_type=company \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true \
 -d "settings[card_payments][statement_descriptor_prefix]"=RUNCLUB
```

The static prefix must contain between 2 and 10 characters, inclusive. Card
networks receive only the first 22 characters (including the `*` symbol and the
space that concatenates the static prefix and dynamic suffix) of the complete
statement descriptor.

Set the `statement_descriptor` and `statement_descriptor_prefix` for flexibility
in setting statement descriptors on charges.

If the statement descriptor is set on card charges and no prefix is set, Stripe
truncates the account statement descriptor as needed to set the prefix value.

## Set a dynamic suffix for connected account charges

Dynamic suffixes are supported only for card charges by using the
`statement_descriptor_suffix` parameter. You can read more about [dynamic
suffixes](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic)
or see the concatenated statement descriptors (prefix* suffix) in the
[Dashboard](https://dashboard.stripe.com/settings/public).

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d amount=1000 \
 -d currency=usd \
 -d "payment_method_types[]"=card \
 -d statement_descriptor_suffix="Custom suffix"
```

## Set Japanese statement descriptors

We recommend setting the static components of kanji and kana statement
descriptors for Japanese connected accounts. You can set all descriptors and
their corresponding prefixes when creating a Japanese connected account:

With controller propertiesWith account type
```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "controller[stripe_dashboard][type]"=none \
 -d "controller[fees][payer]"=application \
 -d "controller[losses][payments]"=application \
 -d "controller[requirement_collection]"=application \
 -d country=JP \
 -d business_type=company \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true \
 -d "settings[card_payments][statement_descriptor_prefix]"="example prefix" \
 -d "settings[card_payments][statement_descriptor_prefix_kanji]"="漢字プリフィックス" \
 -d "settings[card_payments][statement_descriptor_prefix_kana]"="カナプリフィックス" \
 -d "settings[payments][statement_descriptor]"="example descriptor" \
 -d "settings[payments][statement_descriptor_kanji]"="漢字明細" \
 -d "settings[payments][statement_descriptor_kana]"="カナメイサイ"
```

You can set dynamic kanji and kana suffixes when creating card charges with
`payment_method_options[card][statement_descriptor_suffix_kanji]` and
`payment_method_options[card][statement_descriptor_suffix_kana]`.

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

See [Japanese statement
descriptors](https://docs.stripe.com/get-started/account/statement-descriptors#set-japanese-statement-descriptors)
for more details.

## Links

- [requirements for statement
descriptors](https://docs.stripe.com/get-started/account/statement-descriptors)
-
[settings.payments.statement_descriptor](https://docs.stripe.com/api/accounts/object#account_object-settings-payments-statement_descriptor)
-
[settings.card_payments.statement_descriptor_prefix](https://docs.stripe.com/api/accounts/object#account_object-settings-card_payments-statement_descriptor_prefix)
- [the charge type](https://docs.stripe.com/connect/charges)
- [create or update account](https://docs.stripe.com/api/accounts)
- [create account](https://docs.stripe.com/api/accounts/create)
- [update account](https://docs.stripe.com/api/accounts/update)
- [API version 2023-10-16](https://docs.stripe.com/upgrades#2023-10-16)
-
[card_payments](https://docs.stripe.com/connect/account-capabilities#card-payments)
-
[statement_descriptor](https://docs.stripe.com/api/charges/create#create_charge-statement_descriptor)
-
[business_profile](https://docs.stripe.com/api/accounts/object#account_object-business_profile)
-
[settings.card_payments.statement_descriptor_prefix](https://docs.stripe.com/api/accounts/object#account_object-settings-payments-statement_descriptor_prefix)
- [dynamic
suffixes](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic)
- [Dashboard](https://dashboard.stripe.com/settings/public)
- [Japanese statement
descriptors](https://docs.stripe.com/get-started/account/statement-descriptors#set-japanese-statement-descriptors)