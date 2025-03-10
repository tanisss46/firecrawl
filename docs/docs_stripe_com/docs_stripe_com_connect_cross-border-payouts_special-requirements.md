# Country-specific considerations for cross-border payouts

## Learn about country-specific requirements for receiving payments from other countries.

The minimum payout amounts for cross-border payouts depend on the recipient
connected account’s country. Also, cross-border payouts to connected accounts in
certain countries might have additional bank or fund flow restrictions.

## Cross-border minimum payout amounts

The minimum cross-border payout amount for a given country depends on the lowest
amount that Stripe can support with our banking partners. Typically, the minimum
is one base unit of the recipient account’s local currency. In some cases,
Stripe sets a higher minimum to account for possible bank fees.

### Cross-border minimum payout amounts per country

## Bank restrictions

Most banks can accept payments from other countries without any special
requirements. Some banks in certain countries require additional information
about recipient identity or transactions for risk and compliance purposes. The
receiving bank often has discretion over what they require for cross-border
transactions, which can differ between banks, even within the same country.

If a connected account onboards to your platform in a country with special
restrictions, we send an email to alert them about the possibility of additional
requirements. If the receiving bank requires additional information about the
connected account, direct them to contact the account.

Some country-specific bank requirements can result in additional fees for a
connected account to receive payouts. In those countries, Stripe might also set
a higher minimum payout to account for those fees.

The following list of country-specific requirements isn’t exhaustive, because
Stripe has no control over them and can’t guarantee notification of changes. If
you encounter additional requirements that aren’t listed, please notify [Stripe
support](https://support.stripe.com/).

Possible special requirements include:

### Bangladesh

- Submitting a remittance form.
- Providing a receipt or invoice as proof that the recipient is legitimately
receiving the payment.
- Paying additional fees.

### Japan

- Visiting a bank location to submit a copy of their ID and additional
paperwork, if they haven’t previously done so. Banks require a national ID card
number (MyNumber) to be submitted and on file before they can receive or send
international transfers.
- Providing a receipt or invoice as proof that the recipient is legitimately
receiving the payment.
- Paying additional fees.
- Supporting payouts only to banks participating in the Foreign Exchange Yen
Clearing System (FXYCS).

### Serbia

- Providing additional information on the purpose of the payment.
- Providing a receipt or invoice as proof that the recipient is legitimately
receiving the payment.
- Submitting a remittance form.

## Fund flow restrictions

The following fund flows are generally supported in countries for cross-border
payouts:

- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
without the `on_behalf_of` parameter
- Top-up and transfers
- [Destination charges](https://docs.stripe.com/connect/destination-charges)

Direct charges and destination charges *with* the `on_behalf_of` parameter
aren’t supported. However, some countries have additional limitations.

For Brazil,
[India](https://support.stripe.com/questions/stripe-india-support-for-marketplaces),
and
[Thailand](https://support.stripe.com/questions/stripe-thailand-support-for-marketplaces),
only the following fund flows are supported:

- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
without the `on_behalf_of` parameter
- Top-up and transfers

## Links

- [Stripe support](https://support.stripe.com/)
- [Separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Destination charges](https://docs.stripe.com/connect/destination-charges)
-
[India](https://support.stripe.com/questions/stripe-india-support-for-marketplaces)
-
[Thailand](https://support.stripe.com/questions/stripe-thailand-support-for-marketplaces)