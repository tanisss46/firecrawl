# Standard accounts guide

## Learn about the changes to Connect onboarding requirements, and how your connected accounts will be affected in Australia, Europe, New Zealand, and the United States.

To adapt to changes in financial regulations, Stripe has made important updates
to [Connect](https://docs.stripe.com/connect) that affect the information
collection requirements. Many of these requirements relate to gathering
information to verify companies and individuals. Stripe already manages this
information collection for Standard accounts. Stripe will start collecting
updated requirements from new businesses when they sign up for your platform. If
you have existing users that are affected by these changes, Stripe will contact
them to collect updated information. You don’t need to take action.

## Updated requirement: beneficial owners

Information about the [beneficial owners of a
business](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
is required for accounts in Australia, Europe, New Zealand, and the United
States.

- Owner: Any individual who owns a significant percentage of the company (often
25% or more).
- Executive (sometimes referred to as a controller): Any individual who
exercises significant control over your company. Individuals considered to
*exercise significant control* over the company are those responsible for
managing and directing the business and may include executive officers or senior
managers such as CEO, CFO, COO, Managing Member, General Partner, President,
Vice President, or Treasurer.
- Representative: The individual responsible for creating and maintaining the
account. This is typically the end user who is interacting with your platform on
behalf of the business.

For detailed information about the required information that Stripe collects
from your Standard accounts, see [Required Verification
Information](https://docs.stripe.com/connect/required-verification-information).

## Impact to your connected accounts

Stripe has updated the Dashboard to collect the required information for your
new connected accounts.

Existing accounts that need to update their information will be contacted by
Stripe later this year. They’ll receive emails and Stripe Dashboard
notifications that will guide them through the information collection process.

## Recommended actions

If you have any customer-facing documentation that references onboarding onto
Stripe, you might want to update it to reflect the updated information
requirements.

To provide a better user experience, it’s a best practice to identify accounts
that can’t process payments. An account can be unable to process payments
because of verification issues or missing information. Stripe works to resolve
these cases directly with your customers, but you should also monitor your
connected accounts and tell customers who can’t process payments to log into
their Stripe account to resolve the issue. To determine whether or not an
account can process payments, check the `charges_enabled` attribute on the
[Account
object](https://docs.stripe.com/api/accounts/object#account_object-charges_enabled).

For more information about requirements, see the [company
ownership](https://support.stripe.com/questions/owners-and-directors) and
[beneficial
owners](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
support articles.

## Links

- [Connect](https://docs.stripe.com/connect)
- [beneficial owners of a
business](https://support.stripe.com/questions/beneficial-owner-and-director-definitions)
- [Required Verification
Information](https://docs.stripe.com/connect/required-verification-information)
- [Account
object](https://docs.stripe.com/api/accounts/object#account_object-charges_enabled)
- [company ownership](https://support.stripe.com/questions/owners-and-directors)