# Build a custom Capital programPrivate preview

## Integrate with our API to build a custom Capital program.

[Stripe
Capital](https://docs.stripe.com/capital/how-capital-for-platforms-works)
enables your platform to retrieve pre-qualified financing offers for your
connected accounts, expose a compliant loan application, and provide ongoing
reporting for in-progress financing.

This guide outlines how platforms using
[Connect](https://docs.stripe.com/connect) can integrate with the [Capital
API](https://docs.stripe.com/api/capital/financing_offers).

### Capital lifecycle

To launch the program, your platform must support the three phases of the
Capital lifecycle:

- Marketing financing offers to eligible users.
- Providing access to the financing reporting page for in-progress financing.
- Continuing to provide access to the financing reporting page after users have
fully repaid their financing.

This guide explains how to:

- Retrieve financing offers for eligible users.
- Make the financing application available to users.
- Provide users access to the financing reporting page.
[Confirm your branding
settingsDashboard](https://docs.stripe.com/capital/api-integration#confirm-branding)
All users who receive Capital offers see your business name, icon, logo, and
branding color in the offer emails, application, and financing reporting page.

Navigate to your **Connect branding settings**, and make sure your platform’s
branding settings are correct.

![Capital offer application
page](https://b.stripecdn.com/docs-statics-srv/assets/offer-page.66c647c99e2b25b314b7ca8be2cc98a4.png)

[Create an undelivered financing offer in test
modeDashboard](https://docs.stripe.com/capital/api-integration#create-undelivered-offer)
We recommend using test mode tooling to build your integration. In test mode,
visit the [Capital
Dashboard](https://dashboard.stripe.com/test/connect/capital).

- Click **Create** to open the **Create financing offer** modal, which allows
you to create financing offers in test mode. The default options create an
undelivered financing offer with a 1,000 USD loan amount.
- Leave the default options, and click **Create financing offer**.
- From the Dashboard, click the row corresponding to the offer you created.

The loans and financing section of the connected account details page displays
details about the user’s financing offer.

[Retrieve financing
offersServer-side](https://docs.stripe.com/capital/api-integration#retrieve-financing-offers)
You can retrieve financing offers for all of your platform’s users with the
[List financing
offers](https://docs.stripe.com/api/capital/financing_offers/list) endpoint.

```
curl https://api.stripe.com/v1/capital/financing_offers \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

If the offer is successfully created, you receive a response similar to the
following:

```
{
 "object": "list",
 "url": "/v1/capital/financing_offers",
 "has_more": false,
 "data": [
 {
 "id": "financingoffer_abc123",
 "object": "capital.financing_offer",
 ...,
 },
 {...}
 ]
}
```

You can look up a financing offer using the [Retrieve financing
offer](https://docs.stripe.com/api/capital/financing_offers/retrieve#retrieve_financing_offer)
endpoint. Retrieve the first financing offer from the list above.

```
curl https://api.stripe.com/v1/capital/financing_offers/financingoffer_abc123 \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

[Send offer
emailServer-side](https://docs.stripe.com/capital/api-integration#send-offer-email)
Stripe sends the `capital.financing_offer.created`
[webhook](https://docs.stripe.com/webhooks) after a financing offer is created.
Update your webhook integration to listen for the
`capital.financing_offer.created` webhook. If you send your own offer emails,
the webhook is an important notification to notify the user of their offer.

#### Warning

Make sure the contents of your offer email comply with banking regulations by
reviewing the [marketing guidance](https://docs.stripe.com/capital/marketing)
page. Submit all changes to user-facing materials for review at
[capital-review@stripe.com](mailto:capital-review@stripe.com).

In the email, link users to a dedicated Capital section in your platform
dashboard. Users access the Capital financing application with [Account
Links](https://docs.stripe.com/api/account_links). Account Links expire shortly
after they’re generated, so provide a way for users to regenerate the
application link. Include a link to the financing application in your platform
dashboard by generating an Account Link of type `capital_financing_offer`.

```
curl https://api.stripe.com/v1/account_links \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d account=acct_123 \
# The URL the user will be redirected to if the account link is expired, has
been previously-visited, or is otherwise invalid.
 -d refresh_url="https://example.com/reauth" \
 # The URL the user will be redirected to after completing the linked flow.
 -d return_url="https://example.com/thanks" \
 -d type=capital_financing_offer
```

If the creation of an account link is successful, you receive a response similar
to the following:

```
{
 "object": "account_link",
 "created": 1611264596,
 "expires_at": 1611264896,
 "url": "https://connect.stripe.com/capital/offer/SrjgLUfa0O7K"
}
```

After updating your webhook integration, create another offer in the
[Dashboard](https://dashboard.stripe.com/test/connect/capital), and verify you
receive the `capital.financing_offer.created` webhook.

### Mark the offer as delivered

Update your webhook integration to [mark the financing offer as
delivered](https://docs.stripe.com/api/capital/financing_offers/mark_delivered)
after sending the offer email. Marking an offer as delivered is required and is
an affirmation that you have marketed the offer to the user.

```
curl
https://api.stripe.com/v1/capital/financing_offers/financingoffer_abc123/mark_delivered
\
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2:
```

Verify the status of the financing offer is delivered using the
[Dashboard](https://dashboard.stripe.com/test/connect/capital) or the [financing
offer API](https://docs.stripe.com/api/capital/financing_offers/retrieve).

[Listen for status
changesServer-side](https://docs.stripe.com/capital/api-integration#listen-status-changes)
In addition to the `capital.financing_offer.created` webhook, Stripe sends
additional webhooks as the financing offer transitions through different states.
The following is a full list of the webhooks you can receive:

Webhook identifierTrigger`capital.financing_offer.created`Financing offer is
created`capital.financing_offer.accepted`User submits their offer
application`capital.financing_offer.paid_out`Stripe approves the offer
application and funds are paid out to the
user`capital.financing_offer.fully_repaid`User fully repays the financing
balance`capital.financing_offer.canceled`User cancels the financing
offer`capital.financing_offer.rejected`User’s application isn’t
approved`capital.financing_offer.expired`Financing offer expires and is no
longer available`capital.financing_offer.replacement_created`Financing offer is
[replaced](https://docs.stripe.com/capital/replacements) with a new financing
offer
From the [Dashboard](https://dashboard.stripe.com/test/connect/capital), find
the offer you delivered earlier.

- Click the overflow menu ().
- Click the **Expire offer** option, which lets you simulate expiring the offer.
- Verify you receive the `capital.financing_offer.expired` webhook.

With the exception of `capital.financing_offer.canceled`, you can simulate all
webhooks using test mode tooling.

[Apply for an
offerDashboardServer-side](https://docs.stripe.com/capital/api-integration#apply-for-offer)
You can simulate the `capital.financing_offer.accepted` webhook by applying for
an offer.

- From the [Dashboard](https://dashboard.stripe.com/test/connect/capital),
create a delivered offer with a maximum loan amount of 20,000 USD.
- Generate an account link of type `capital_financing_offer`, and navigate to
the link. Here, you can preview what the application looks like for your users.
- Continue to the end of the application, and click **Submit**.
- Verify you received the `capital.financing_offer.accepted` webhook.
- View the offer in the Dashboard, and check it has status accepted.

### View the application tracker

A financing offer with status accepted is pending application review by the
Stripe [servicing](https://docs.stripe.com/capital/servicing) team. While this
review takes place, you can direct the user to the financing reporting page. The
financing reporting page contains an application tracker with an approximate
timeline of the application review.

Generate an [Account Link](https://docs.stripe.com/api/account_links) of type
`capital_financing_reporting`.

```
curl https://api.stripe.com/v1/account_links \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d account=acct_123 \
 # When the user refreshes the page, where should we redirect them
 -d refresh_url="https://example.com/reauth" \
 # When the user completes the application, where should they return
 -d return_url="https://example.com/thanks" \
 -d type=capital_financing_reporting
```

Navigate to the link, and view the application tracker.

[Approve the
applicationDashboard](https://docs.stripe.com/capital/api-integration#approve-application)
In the [Dashboard](https://dashboard.stripe.com/test/connect/capital), find the
row corresponding to the accepted offer.

- Click the overflow menu ().
- Click the **Approve and disburse funds** option, which lets you simulate an
application approval and funds disbursal.
- Verify you receive the `capital.financing_offer.paid_out` webhook, which
notifies you that the financing has been paid out.
- Generate another [Account Link](https://docs.stripe.com/api/account_links) of
type `capital_financing_reporting`. The reporting page now provides access to
payout and repayment transaction details for the user’s in-progress financing.
- Click **Make payment**, and create a payment transaction.

#### Note

It takes up to 15 minutes for the **Make payment** button to be enabled on the
reporting page for test mode financing offers.

After the transaction is processed, view the payment in the transactions table.
You can programmatically view the user’s paid-down financing amount for
in-progress financing using the [financing summary
API](https://docs.stripe.com/api/capital/financing_summary).

```
curl https://api.stripe.com/v1/capital/financing_summary \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
```

If the retrieval of the financing summary is successful, you receive a response
similar to the following:

```
{
 "object": "capital.financing_summary",
 "details": {
 "currency": "usd",
 "advance_amount": 1000000,
 "fee_amount": 100000,
 "withhold_rate": 0.2,
 "remaining_amount": 999950,
 "paid_amount": 50,
 "current_repayment_interval": {
 "due_at": 123456789,
 "remaining_amount": 50,
 "paid_amount": 50
 },
 "repayments_begin_at": 123456789,
 "advance_paid_out_at": 123456789
 }
}
```

[Fully repay the
financingDashboard](https://docs.stripe.com/capital/api-integration#fully-repay-financing)
In the [Dashboard](https://dashboard.stripe.com/test/connect/capital), find the
row corresponding to the paid-out financing.

- Click the overflow menu ().
- Click the **Repay offer** option, which lets you simulate fully paying down
the financing balance.
- Verify you receive the `capital.financing_offer.fully_repaid` webhook, which
notifies you that the financing has been fully paid down.
- Generate another [Account Link](https://docs.stripe.com/api/account_links) of
type `capital_financing_reporting`.

After a user pays down their financing, they can access past financing details
on the reporting page at any time.

[Review your test mode
integration](https://docs.stripe.com/capital/api-integration#review-test-mode-integration)
By now, your integration:

- Responds to the `capital.financing_offer.created` webhook by sending an offer
email and marking the offer as delivered
- Exposes the financing application link in your platform dashboard
- Exposes the financing reporting link in your platform dashboard

The Capital section of your platform dashboard might appear differently
depending on which phase the user’s financing is in. Review the state diagram
below for a list of possible financing offer status values.

Undelivered

Delivered

Accepted

Paid out

Fully repaid

Replaced

Expired

Rejected

Canceled

Capital financing offer state machine[Prepare to enable automatic
offers](https://docs.stripe.com/capital/api-integration#prepare-enable-auto-offers)
When automatic offers are enabled in live mode, Stripe automatically creates
financing offers for your users on a daily basis. Before enabling automatic
offers, make sure that you:

- Confirm and update email addresses for your users through [Comms
Center](https://dashboard.stripe.com/connect/comms_center/collect). To be
eligible for Capital financing, users must have an email saved with Stripe so
that they can receive transactional emails such as payment progress updates.
- [Contact us](mailto:capital-review@stripe.com) to enable live mode access to
the financing offers API.

### Enable additional features

Over time, some of your users might become eligible for refills. Refills are
additional financing offers sent to users who have made substantial repayment
progress towards their in-progress loans. Follow the [refills integration
guide](https://docs.stripe.com/capital/refills) to update your integration to
support refill financing offers.

If you want to include Capital transactions on your platform dashboard, see the
[reporting and reconciliation
guide](https://docs.stripe.com/capital/reporting-and-reconciliation).

## Links

- [Stripe
Capital](https://docs.stripe.com/capital/how-capital-for-platforms-works)
- [Connect](https://docs.stripe.com/connect)
- [Capital API](https://docs.stripe.com/api/capital/financing_offers)
- [Connect branding
settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding)
- [Capital Dashboard](https://dashboard.stripe.com/test/connect/capital)
- [List financing
offers](https://docs.stripe.com/api/capital/financing_offers/list)
- [Retrieve financing
offer](https://docs.stripe.com/api/capital/financing_offers/retrieve#retrieve_financing_offer)
- [webhook](https://docs.stripe.com/webhooks)
- [marketing guidance](https://docs.stripe.com/capital/marketing)
- [Account Links](https://docs.stripe.com/api/account_links)
- [https://example.com/reauth](https://example.com/reauth)
- [https://example.com/thanks](https://example.com/thanks)
-
[https://connect.stripe.com/capital/offer/SrjgLUfa0O7K](https://connect.stripe.com/capital/offer/SrjgLUfa0O7K)
- [mark the financing offer as
delivered](https://docs.stripe.com/api/capital/financing_offers/mark_delivered)
- [financing offer
API](https://docs.stripe.com/api/capital/financing_offers/retrieve)
- [replaced](https://docs.stripe.com/capital/replacements)
- [servicing](https://docs.stripe.com/capital/servicing)
- [financing summary API](https://docs.stripe.com/api/capital/financing_summary)
- [Comms Center](https://dashboard.stripe.com/connect/comms_center/collect)
- [refills integration guide](https://docs.stripe.com/capital/refills)
- [reporting and reconciliation
guide](https://docs.stripe.com/capital/reporting-and-reconciliation)