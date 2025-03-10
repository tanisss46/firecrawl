# Platform tax reporting for Connect platformsPrivate preview

## Prepare reports for DAC7 and other OECD regulations for sellers in the EU, Canada, United Kingdom, Australia, and New Zealand.

Under the
[MRDP](https://www.oecd.org/en/topics/sub-issues/international-tax-compliance-policies-and-best-practices/model-reporting-rules-for-digital-platforms.html),
certain Connect platforms are required to report income information regarding
their connected accounts to tax authorities. These requirements are for economic
activities facilitated by digital platforms. Several countries have now rolled
out binding regulations based on MRDP–including DAC-7, SERR, ITA Part XX.

Broadly, these regulations require that platforms collect and submit information
to both regulators and each of their users (except in Australia, where end users
don’t need to receive a copy). Stripe offers tools to help platforms through
this process.

Platform tax reporting provides the following:

- A way to collect verified tax information from Connected Accounts. Your
connected accounts can submit their tax information on the same interface that
they onboard to Stripe with. They won’t be asked to provide any information
they’ve already provided, but they can make necessary updates.
- A dashboard to import and edit information and generate reports for the
appropriate authorities and generate seller statements for your users.

#### Limitation of liability

Platform tax reporting services isn’t a comprehensive tax solution or tax
advising service. Stripe accepts no liability for the use of information
collected or reports generated and strongly recommends consulting with a
professional tax advisor for any tax-related concerns. Users remain fully
responsible for the accuracy of the information and obligation to pay any fine,
penalty, or other sanction imposed by a governmental authority.

## Product features

- Support for CA, UK, certain EU countries (FR, DE, IT, SE, ES, NL), NZ, and AU
- Collect, validate, and verify (where applicable) information from sellers
through Connect interfaces- Connect interfaces include the Stripe Dashboard,
Express Dashboard, and hosted onboarding
- A Dashboard to view and manage tax information
- Form editing with CSVs
- Report generation to AU, CA, NL (for EU), and UK XML schemas
- Role-based access control and two-step authentication (2FA)
- E-delivery of tax information statements using the API

## Collect identity information

Apply the `tax_reporting` additional verification to your connected accounts to
collect, validate, and verify the necessary information from your sellers. You
can use the same integration type for every region where your platform has tax
reporting obligations (outside of the US), and your platform doesn’t need to
change their existing Connect integration.

- Platforms can enable or disable for whatever subset of connected accounts they
choose.
- Stripe handles the tax information collection, which varies by country. Stripe
automatically determines which requirements to apply based on the account’s
country and business type.
- Any added countries follow the same integration type.

As with other requirements, those added by the `tax_reporting` additional
verification are presented to connected accounts in any Connect onboarding
interface. The verification requirements disable an account’s capabilities if
not completed before reaching the threshold you set. You can set the following
enforcement limits to impose the disabling of payouts or payments:

- **Up front**: Block payouts or payments if a verified TIN isn’t on file
immediately.
- **Volume**: Block payouts or payments if a verified TIN isn’t on file after
processing *x* USD.
- **Time**: Block payouts or payments if a verified TIN isn’t on file after *x*
days.
- **Combination**: Block payouts or payments if a verified TIN isn’t on file
after *x* days or after processing *x* USD.

You can also disable these additional requirements at your own discretion.

## Preparing and generating your reports

Stripe auto-populates the Dashboard view and CSVs with identity data that’s
already been collected from connected accounts.

Review your connected accounts’ information in the Dashboard. Import transaction
totals, identity overrides, and standalone sellers (sellers not attached to a
Connected Account) by uploading CSV files.

![Seller list
view](https://b.stripecdn.com/docs-statics-srv/assets/global-tax-reporting-seller-view.9874379a85397e9a41f0910dd0235b8e.png)

Seller list view in the Dashboard

![Seller
details](https://b.stripecdn.com/docs-statics-srv/assets/global-tax-reporting-seller-details-full.47bd6156fb3dcfc8f5f7de5412ddd5c6.png)

Seller information details

When you’re ready, generate XML reports for your sellers.

## Deliver tax statements to your users

You might be required to provide a copy of the information submitted to tax
authorities to your sellers. Stripe generates a PDF translated into the user’s
preferred language to display this information. You can download it separately
for each individual seller in the Dashboard, or you can access it with the API.
We support this for sellers, regardless of whether they have a connected
account.

## Request early access

## Interested in getting access to Platform Tax Reporting private preview?

Platform tax reporting is currently limited to Connect platforms. To join the
waitlist for the private preview, enter your email address below. If you have an
account representative, reach out to them. Access to this feature isn't
guaranteed.

Collect EmailSign upRead our [privacy policy](https://stripe.com/privacy).

## Links

-
[MRDP](https://www.oecd.org/en/topics/sub-issues/international-tax-compliance-policies-and-best-practices/model-reporting-rules-for-digital-platforms.html)
- [privacy policy](https://stripe.com/privacy)