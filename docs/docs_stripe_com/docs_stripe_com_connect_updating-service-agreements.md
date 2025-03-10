# Updating service agreement acceptances

## Learn how to update your connected accounts and handle acceptance of the Stripe Connected Account Agreement and other disclosures.

Working with connected accounts where your platform is liable for negative
balances, including Custom and Express accounts, provides a lot of flexibility.
You can access almost every Stripe
[account](https://docs.stripe.com/api/accounts) property through the API.

Platforms can use the API to perform many account management functions,
including:

- Handle acceptance and re-acceptance of the Stripe Connected Account Agreement
(for accounts with no Stripe-hosted Dashboard access, including Custom
accounts).
- Handle [identity
verification](https://docs.stripe.com/connect/identity-verification) (for
accounts with no Stripe-hosted Dashboard access, including Custom accounts).
- Manage the connected business’s information, such as its name, logo, and URL.
- Set some charge behaviors.
- Establish [payout
handling](https://docs.stripe.com/connect/payouts-connected-accounts).

You can make those account updates with an [update
account](https://docs.stripe.com/api/accounts/update) call.

## View and update a connected account through the platform’s Dashboard

You can update some account settings in the [Connected
accounts](https://dashboard.stripe.com/connect/accounts/overview) section of
your Dashboard.

Click any connected account in the list to open that account’s details page. The
information that you can view and change depends on the account type or
controller properties. Common tasks on this page include checking the status of
payouts and searching for payments.

## Stripe’s service agreements for connected accounts

To provide Stripe Connect services to your connected accounts, Stripe must
establish a direct contractual relationship with them. That requires all
connected accounts with no Stripe-hosted Dashboard access to accept the correct
Stripe service agreement. The service agreement your accounts must accept
depends on whether they’re merchants subject to Stripe’s full terms of service
or are payment recipients subject to the recipient service agreement. You’re
responsible for making sure that your accounts agree to the correct service
agreement before accepting or receiving payments through Stripe on your
platform.

If, after onboarding, one of your connected accounts transfers its ownership or
updates its verified tax identification number, the updated account owner must
provide their agreement to the correct Stripe service agreement. You’re
responsible for obtaining that agreement.

### Referencing Stripe’s service agreement

You must present your connected accounts with a link to the correct agreement,
and they must expressly consent to it prior to using Stripe. For example, at the
point of account activation, you can present language such as the following:

Full service agreementRecipient service agreement
By registering your account, you agree to our Services Agreement and the [Stripe
Connected Account Agreement](https://stripe.com/connect-account/legal/full).

### Add Stripe’s service agreement to your terms of service

You can make accepting Stripe’s service agreement easy for connected accounts by
including it in your terms of service. In your terms, include a link to the
correct Stripe service agreement and clearly state that accepting your terms
includes accepting the Stripe service agreement. Here are some examples of text
you can include in your terms:

Full service agreementRecipient service
agreementFrenchSpanishItalianPortugueseGermanJapanese
Payment processing services for [account holder term, for example, drivers or
sellers] on [platform name] are provided by Stripe and are subject to the
[Stripe Connected Account
Agreement](https://stripe.com/connect-account/legal/full), which includes the
[Stripe Terms of Service](https://stripe.com/legal) (collectively, the “Stripe
Services Agreement”). By agreeing to [this agreement / these terms / and so on]
or continuing to operate as a [account holder term] on [platform name], you
agree to be bound by the Stripe Services Agreement, as the same may be modified
by Stripe from time to time. As a condition of [platform name] enabling payment
processing services through Stripe, you agree to provide [platform name]
accurate and complete information about you and your business, and you authorize
[platform name] to share it and transaction information related to your use of
the payment processing services provided by Stripe.

### Indicating acceptance

For connected accounts where the platform collects updated information for due
or changed requirements, you must collect the updated acceptance of Stripe’s
service agreement.

To indicate to Stripe that a connected account accepted Stripe’s service
agreement, make an [update account
call](https://docs.stripe.com/api/accounts/update), providing the acceptance
date and IP address:

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "tos_acceptance[date]"=1609798905 \
 -d "tos_acceptance[ip]"="8.8.8.8"
```

### Acquirer disclosure

To meet Stripe’s Financial Partner requirements, you must advise your connected
accounts of Stripe’s acquirers and their contact information in a clear and
conspicuous manner, including [this
disclosure](https://stripe.com/legal/acquirer-disclosure). For accounts that
fall solely under the Recipient Service Agreement, you don’t need to include
this disclosure.

If your accounts provide acceptance of Stripe’s service agreement through a
Stripe onboarding product, it includes that disclosure.

## Disclosing how Stripe processes connected account data

While providing your connected accounts with Connect services, Stripe processes
their data as explained in [Stripe’s Privacy
Policy](https://stripe.com/privacy). You must disclose that to your accounts by
providing them with a link to that policy.

In addition, connected accounts in Canada must consent to allow Stripe to obtain
information from credit agencies to verify their identities. You can obtain that
consent in your onboarding flow by incorporating language like the following
where users agree to your terms of service:

Our payment processor can obtain information from credit agencies to verify your
identity. That information will be used for the purposes described in their
Privacy Policy.

If you are using a Stripe onboarding product like embedded onboarding, but
providing a link to your own privacy policy, your privacy policy must include a
link to Stripe’s Privacy Policy and the following language:

Privacy policy link
When you provide personal data in connection with , Stripe receives that
personal data and processes it in accordance with Stripe’s Privacy Policy.

For Stripe to lawfully process personal data according to your instructions, you
can be legally required to provide additional disclosures or obtain additional
consents. Talk to your lawyer about which disclosures and consents might apply
to your platform and connected accounts.

## See also

- [Identity Verification](https://docs.stripe.com/connect/identity-verification)
- [Account Tokens](https://docs.stripe.com/connect/account-tokens)
- [Control Bank and Debit Card
Payouts](https://docs.stripe.com/connect/payouts-connected-accounts)
- [Manage bank accounts and debit
cards](https://docs.stripe.com/connect/payouts-bank-accounts)
- [Receive payouts](https://docs.stripe.com/payouts)
- [Full API reference](https://docs.stripe.com/api)

## Links

- [configured with
properties](https://docs.stripe.com/connect/update-to-typeless-connect)
- [account](https://docs.stripe.com/api/accounts)
- [identity verification](https://docs.stripe.com/connect/identity-verification)
- [payout handling](https://docs.stripe.com/connect/payouts-connected-accounts)
- [update account](https://docs.stripe.com/api/accounts/update)
- [Connected accounts](https://dashboard.stripe.com/connect/accounts/overview)
- [Stripe Connected Account
Agreement](https://stripe.com/connect-account/legal/full)
- [Stripe Terms of Service](https://stripe.com/legal)
- [this disclosure](https://stripe.com/legal/acquirer-disclosure)
- [Stripe’s Privacy Policy](https://stripe.com/privacy)
- [Account Tokens](https://docs.stripe.com/connect/account-tokens)
- [Manage bank accounts and debit
cards](https://docs.stripe.com/connect/payouts-bank-accounts)
- [Receive payouts](https://docs.stripe.com/payouts)
- [Full API reference](https://docs.stripe.com/api)