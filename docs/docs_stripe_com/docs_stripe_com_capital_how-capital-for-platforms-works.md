# How Stripe Capital for Platforms worksPrivate preview

## Learn the basics of Stripe Capital for Platforms.

Before you begin using Stripe Capital, familiarize yourself with the eligibility
requirements, lending process, and structure of financing offers.

## Capital eligibility

Stripe determines eligibility and financing terms for each user based on their
payment activity on Stripe. We automatically determine eligibility as set by our
bank partner on a daily basis and without action from your platform. While our
goal is to offer access to financing to as many users (connected accounts) as
possible, not all users will be eligible for financing.

Stripe Capital is currently limited to businesses that:

- Are based in the US (business representatives must also provide a physical US
home address).
- Are for-profit. Additional restrictions might apply to government, utility,
and travel businesses. Email
[capital-review@stripe.com](mailto:capital-review@stripe.com) if your users fit
within the non-profit category.
- Have an email address linked to their Stripe account (necessary for marketing
and ongoing servicing). Many Connect platforms don’t automatically provide
linked email addresses for their users to Stripe. The Stripe Capital team can
work with you to upload and manage these email addresses if your platform
doesn’t automatically share emails with Stripe.

## Capital lending process

Capital uses Stripe’s existing knowledge about your user’s business to offer an
end-to-end lending process. The following are the five phases of the process:

PhaseDescriptionRisk and underwritingStripe Capital automatically underwrites a
user based on their Stripe transaction history and volume. This means each user
that receives an offer is already pre-qualified for their loan.Offer and
applicationsNotify eligible customers with Stripe’s no-code email service or
build custom notifications in your own site with the Capital API. All offers
link to a co-branded application flow hosted by Stripe. Relevant business
information is pre-populated for your user to review for a quick application
process.Fund disbursementStripe handles sourcing all Capital funds and deposits
them to your user’s Stripe account within 2 business days.RepaymentRepayment is
fully automated and adjusts to daily sales. Stripe deducts a fixed percentage
from each of your user’s sales until they completely repay the total they
owe.Servicing and collectionsStripe handles servicing and collections if a user
fails to satisfy on-time payments.
## Capital offer structure

Each financing offer has four components:

Offer componentDefinitionPrincipal amountThe amount the account is pre-qualified
to receiveRepayment rateThe percentage of each future transaction to be withheld
for repaymentPremium amountA flat fee on top of the principal amount that the
connected account user must pay backMinimum paymentA minimum amount that must be
paid over a specific time period, usually 60 days
For example, if there is a financing offer for 20,000 USD at a 15% repayment
rate with a 2,000 USD flat fee, the loan will have a 2,444.45 USD, 60-day
minimum payment. After the application is reviewed and approved, the user
receives a 20,000 USD payout and Stripe Capital withholds 15% of each
transaction processed through Stripe until the user pays back the full
outstanding balance of 22,000 USD. If the user misses a minimum payment, Stripe
automatically debits them the remaining balance for the relevant time period.

See how this example offer appears in the co-branded application flow:

![anatomy
offer](https://b.stripecdn.com/docs-statics-srv/assets/offer-anatomy.25435a5c27bd4804965991bf4ba77e00.png)

A user’s financing offer. All loans are issued by Celtic Bank

## Capital emails

Throughout the lending process, Stripe sends transactional and collections
emails to your connected accounts. These emails are sent by Stripe and aren’t
platform owned. Because the primary purpose of these emails is to communicate a
financing update, these are classified as transactional emails, and are
delivered even to suppressed or unsubscribed emails.

### Preview and customize emails

You can customize the core set of transactional co-branded emails that we send
to your connected accounts in your [Capital communication
settings](https://dashboard.stripe.com/settings/connect/communication/email_preview?activeProduct=capital_for_platforms).

#### Customize branding

You can set your Business name, Logo, Icon, Brand color, and Accent color.
Stripe uses these values in the co-branded emails that we send to your connected
accounts.

#### Customize email domain

By default, emails are sent from a stripe.com address. You can [customize the
domain](https://docs.stripe.com/get-started/account/email-domain), but not the
specific address. We set the address automatically [based on the context of the
message](https://support.stripe.com/questions/custom-email-domain).

#### Preview and test emails

When you customize co-branded Stripe Capital emails, you can check their
appearance and test their links in the preview on the right side of the page.
Select a specific email from the **Preview** dropdown list. You can also send
test emails to verify that they’re working correctly by clicking **Send email**.

#### View the history of emails sent to connected accounts

You can see the emails that Stripe has sent to your connected accounts on the
account details page under **Emails to this account**. To see the details of an
email, including its exact contents, its To: address, and its status (such as
whether it was delivered successfully or was opened), click it in the list.

## Capital collections

A loan is characterized as delinquent—and its delinquency level increases—each
time any scheduled loan payment remains unpaid by the next minimum due date. A
scheduled loan payment is missed when an unsuccessful ACH debit attempt occurs
due to insufficient funds in the related bank account, closure of the related
bank account, revoked access to the ACH account, or any event resulting in
non-payment of scheduled loan minimum payments. Once an account becomes
delinquent, the automated loan payment collection process implements specific
business rules to collect past-due payments. Alongside the automated collection
process, the loan enters a recovery-focused collection queue once it becomes
delinquent.

Stripe Capital has designed a collection process strategy for delinquent loans.
Stripe Capital tries to contact all users who haven’t met or risk not satisfying
their minimum payments, making sure these contacts comply with professional
standards and legal regulations. Collection representatives work with users to
try to maintain a business relationship and satisfy minimum payments according
to the contractual agreement outlined in the loan agreement

As part of our strategy to aid users facing business challenges, Stripe Capital
may offer extended payment plans to help users make smaller payments and meet
their loan obligations. Users who wish to discuss their financial obligations
can reach out to Stripe Capital at
[capital-support@stripe.com](mailto:capital-support@stripe.com).

Eligibility for payment plans is determined by several factors, including a:

- user’s delinquency level.
- user’s possession of a debitable bank account on file with Stripe.
- user’s ability to make a qualifying payment.
- user’s bankruptcy status.
- user’s ability to pay off balance with terms not exceeding 50% of the original
loan terms.

## See also

- [Set up Capital](https://docs.stripe.com/capital/getting-started)
- [How to market Capital](https://docs.stripe.com/capital/marketing)
- [Regulatory compliance](https://docs.stripe.com/capital/regulatory-compliance)

## Links

- [Capital communication
settings](https://dashboard.stripe.com/settings/connect/communication/email_preview?activeProduct=capital_for_platforms)
- [customize the
domain](https://docs.stripe.com/get-started/account/email-domain)
- [based on the context of the
message](https://support.stripe.com/questions/custom-email-domain)
- [Set up Capital](https://docs.stripe.com/capital/getting-started)
- [How to market Capital](https://docs.stripe.com/capital/marketing)
- [Regulatory compliance](https://docs.stripe.com/capital/regulatory-compliance)