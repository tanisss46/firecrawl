# Embedded Connect Support

## Use Stripe support management features from your own website.

In some configurations that use embedded components, Stripe provides targeted
support for your connected accounts. That support is available when your
connected accounts don’t have access to a Stripe-hosted Dashboard and your
platform isn’t liable for their negative balances. It includes:

- A Stripe-hosted support site with self-serve content specific to Stripe’s
embedded components
- Access to email and live chat support for your connected accounts
- Links to the self-serve support site in your embedded components and
co-branded risk and compliance emails

Your connected accounts might need help with payment processing-specific issues
like responding to disputes or confirming expected fund settlement times. They
can also have questions about risk interventions where only Stripe has full
visibility and control. Providing direct access to Stripe Support for such
situations greatly reduces your platform support team’s operational load. In
addition, you can implement a complete self-serve solution for risk
interventions by combining that support access with [Stripe Managed
Risk](https://docs.stripe.com/connect/embedded-risk).

## Prerequisites

Set up your platform with [a fully embedded connect
configuration](https://docs.stripe.com/connect/build-full-embedded-integration).
The Stripe-hosted self-serve support site becomes discoverable to your users
after you implement the required [embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
for your configuration.

## Access the support site

Your users can access the Stripe-hosted support site at
`https://support.stripe.com/embedded-connect/`.

Embedded components include **Contact support** links in the bottom right of
each dialog. We also include links in flows where users are most likely to need
Stripe’s help.

![Dialog showing contact support
link](https://b.stripecdn.com/docs-statics-srv/assets/embedded-support-link.8b61571aab6de31dc1c643f8616b0ca0.png)

Each of the following embedded components contains links to contact support:

- Account management- Edit Professional details
- Edit Public details
- Edit Personal details
- Edit Payout details
- Notification banner- Compliance forms
- Risk forms
- Onboarding
- Authentication dialog

## Self-serve help

The support site includes articles and related questions across several topic
areas, including the following:

- Accounts
- Declines
- Disputes
- Fraud
- Legal
- Payments
- Payouts
- Privacy
- Refunds
- Reserves
- Verification

![Example support site
article](https://b.stripecdn.com/docs-statics-srv/assets/support-site-article-example.2094c3de78b4ddf05bd4008ea5aa00fc.png)

## Contacting support

**Contact support** links appear on the right side of each page on the
self-serve support site.

If the user is authenticated (for example, provided an SMS OTP), clicking the
link opens a support widget. The widget lets them start a real-time chat with
Support or send an email.

![Contact support through the support
site](https://b.stripecdn.com/docs-statics-srv/assets/support-site-contact-auth.17ef846eb63e7144f1b6f4855fc05f8f.png)

Clicking the link while not authenticated, or clicking **Send us an email** in
the widget, opens a form to open a support case by email.

![Chat with support through the support
site](https://b.stripecdn.com/docs-statics-srv/assets/support-site-email-form.51af965dc976df6654d3909442e33ffe.png)

## Links

- [Stripe Managed Risk](https://docs.stripe.com/connect/embedded-risk)
- [a fully embedded connect
configuration](https://docs.stripe.com/connect/build-full-embedded-integration)
- [embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)