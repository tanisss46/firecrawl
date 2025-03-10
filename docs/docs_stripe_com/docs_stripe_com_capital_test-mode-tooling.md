# Test mode toolingPrivate preview

## Use test mode tooling to review your Capital integration.

Send a test mode offer in the
[Dashboard](https://dashboard.stripe.com/test/connect/capital) to see the
end-to-end flow of a connected account. You can send test offers to the email
address of the authenticated account user.

## Create a test mode offer

- Go to the [Capital
Dashboard](https://dashboard.stripe.com/test/connect/capital).
- Toggle **Test Mode** to an active status.
- To generate a test offer, click **Create** and select the parameters for the
offer creation.

- For the connected account, select an existing connected account by searching
for the account’s ID or leave it blank and Stripe will generate an account for
you.
- You’ll also able to select the type of offer and if it’s a refill, the test
account, and the offer terms (amount, fee, and repayment rate).
- If you prefer to create a new connected account, visit the [Connected Accounts
Overview Page](https://dashboard.stripe.com/test/connect/accounts/overview).
- You might see a message that the connected account needs to add a bank account
or debit card. For test mode offers, you don’t need to link the bank account.

!

Connected Accounts Overview Page

Create a new connected account

Creating a connected account

View account details of your newly created connected account:
`https://dashboard.stripe.com/test/connect/accounts/:merchant_id`

- Click **Create Financing Offer** to create the offer for the test connected
account.

The result is that the financing offer in test mode hasn’t been delivered yet.
You can see each financing offer for your customers and
[Metrics](https://docs.stripe.com/capital/reporting) in the [Capital
Dashboard](https://dashboard.stripe.com/test/connect/capital).

Next, you must enable email delivery and access to the offer.

## Enable email delivery and offer access

To access the offer, mark the offer as delivered. We require offers to be in a
delivered state to confirm successful receipt and to maintain a record that
offers aren’t cherry-picked nor restricted in a discriminatory manner. Users
won’t be able to access offers that are in an undelivered state.

You can mark offers as delivered in two ways:

- You can select the delivered status when you create the test mode financing
offer since actual offer delivery in an email isn’t necessary for test mode.
- If you created a test mode financing offer with an undelivered status, you can
click the actions dropdown for that offer in the Financing offers table and
select **Mark delivered**.

!

Marking offer as Delivered

For multiple offers, select the checkbox in the upper left corner of the column
titles to select all the rows, and then click **Mark delivered** in the top
right corner.

!

Marking Finance Offers as Delivered (Bulk)

## Send test offer email

After you’ve enabled email delivery, you can send a test offer email to your
inbox. Stripe sends test mode offer emails to the authenticated user to prevent
real users from receiving unwanted test mode emails.

In the actions dropdown for the offer, select **Send offer email** and you’ll
receive the Stripe-sent test offer email that uses your platform’s [Connect
branding](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding).

!

Select Send Offer Email action

## Accepting the test offer as a user

If you use Stripe-sent test offer emails, you must complete an account claim and
verification process for security reasons. Use the following test mode values to
pass this security check:

- **Mobile number**: Use the test phone number option.
- **Email**: Add any email address as long as the top-level domain is valid. For
example, `me@mycompany.com` works in test mode, but `test@test.test` doesn’t
work.
- **Verify your phone number**: Use the test code option.

After you pass this verification process, you can view the test offer and apply
for the test loan as if you were the user.

You can also access the offer by clicking the ** Dashboard link** option and
loading the copied link in your browser.

## Approve or reject the offer

After you accept the test offer as the user, the offer transitions to an
accepted status in the Stripe Dashboard. To test the loan disbursement:

- Go to the Financing Reporting page.
- Navigate to the test offer’s detailed Financing page and click **… > approve
and disburse funds**.
- Click **Approve** to initiate the disbursal of funds.

## Financing reporting

Now that you have a financing with a `paid_out` status, retrieve the link for
the active Financing reporting page. This page displays key details around the
financing loan such as outstanding balance, repayment activity, and the ability
to make manual payments or download the contract.

To retrieve this link:

- Navigate to the test offer’s detailed Financing page and click **… > 
Dashboard link**.
- Load this copied link in your browser and pass through the standard
verification steps to access the active Financing reporting page.

## Activate automatic offers to finalize integration

After sending test and pilot offers, you can enable Stripe to send automatic
offers to all eligible and pre-approved users. Stripe disables automatic offers
by default to allow you to manually generate and test offers. To enable
automatic offers:

- Go to the [Capital Dashboard](https://dashboard.stripe.com/connect/capital).
- Select **Manage offers** and confirm that you want to activate automatic
offers. The result is that all eligible users with an email automatically
receive a financing offer as soon as it’s available.

## Links

- [Dashboard](https://dashboard.stripe.com/test/connect/capital)
- [Connected Accounts Overview
Page](https://dashboard.stripe.com/test/connect/accounts/overview)
- [Metrics](https://docs.stripe.com/capital/reporting)
- [Connect
branding](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding)
- [Capital Dashboard](https://dashboard.stripe.com/connect/capital)