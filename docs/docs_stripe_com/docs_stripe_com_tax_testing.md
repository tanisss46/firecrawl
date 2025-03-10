# Testing Stripe Tax

## Learn how to test your Stripe Tax integration.

You can use Stripe Tax in test mode to preview automatic tax calculation
behavior for different tax settings. Use test mode to:

- Preview tax calculation behavior for different customer locations and
registered jurisdictions.
- Validate that your integration handles automatic tax calculations correctly.
- Understand zero-tax outcomes.
[Configure test mode tax
settings](https://docs.stripe.com/tax/testing#tax-settings)
Stripe Tax has separate settings for test mode and live mode so you can preview
changes to your tax settings before publishing them.

When you [Set Up Stripe Tax](https://docs.stripe.com/tax/set-up), make sure you
enable testing by configuring separate [tax settings in test
mode](https://dashboard.stripe.com/test/tax/settings).

[Add a test mode
registration](https://docs.stripe.com/tax/testing#add-registration)
Stripe Tax only calculates tax in jurisdictions where you’ve added a
registration. You must add at least one test mode registration to test your
Stripe Tax integration.

Some [product tax codes](https://docs.stripe.com/tax/tax-codes) are exempt from
sales tax in certain jurisdictions, which can make them challenging to test. For
example, some classes of digital goods are exempt from sales tax in the state of
California. When you’re testing your Stripe Tax integration, we recommend adding
test mode registrations in states that have fewer product-specific exemptions,
such as Idaho or New Jersey.

Test mode registrations don’t affect live mode tax calculations, so you can
change them at any time after you’ve verified that your integration is working
correctly.

[Testing your integration](https://docs.stripe.com/tax/testing#testing)
After you’ve configured your Stripe Tax settings in test mode and added test
mode registrations, you’re ready to test.

No-codeLow-codeCustom
To test in the Dashboard, create an
[Invoice](https://docs.stripe.com/invoicing/dashboard) or [Payment
Link](https://docs.stripe.com/payment-links/create), and make sure the **Use
automatic tax calculation** toggle is on.

![Stripe Dashboard with the automatic tax toggle set to
true](https://b.stripecdn.com/docs-statics-srv/assets/dashboard_automatic_tax.2338adf39e3a07ad9acd79c036e7c637.png)

Stripe Dashboard with the automatic tax toggle set to true

[Review Calculations](https://docs.stripe.com/tax/testing#review-calculations)
### Using the payment details page

#### Note

This functionality isn’t available for tax transactions created using the [Tax
API](https://docs.stripe.com/tax/custom). For transactions recorded using the
Tax API, see [Using the tax transactions
page](https://docs.stripe.com/tax/testing#tax-transactions-page).

After you complete a payment with automatic tax calculation enabled, you can
review information about the tax calculation in the Dashboard.

- Navigate to the [Transactions](https://dashboard.stripe.com/payments) page in
the Dashboard.
- Click a payment you created with Stripe Tax enabled.
- Scroll down to the **Automatic tax calculation** section.

![Automatic tax calculation details on a payment in the Stripe
Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/automatic_tax_details.353a0264381ad5ed1db691922eb357b2.png)

The **Automatic tax calculation** section of the payment details screen. Tax
wasn’t applied to this transaction because there’s no registration for the tax
location.

The **Taxability** field shows whether tax was collected for a given transaction
or explains why no tax was applied. For more information about why Stripe Tax
applies zero tax to some transactions, see [Zero tax
amounts](https://docs.stripe.com/tax/zero-tax).

### Using the tax transactions page

You can view all tax transactions for your account on the [Tax
Transactions](https://dashboard.stripe.com/test/tax/transactions) page in the
Dashboard. Click an individual transaction to see a detailed breakdown of
calculated tax by jurisdiction, and by the individual products included in the
transaction.

## Links

- [Set Up Stripe Tax](https://docs.stripe.com/tax/set-up)
- [tax settings in test mode](https://dashboard.stripe.com/test/tax/settings)
- [product tax codes](https://docs.stripe.com/tax/tax-codes)
- [Invoice](https://docs.stripe.com/invoicing/dashboard)
- [Payment Link](https://docs.stripe.com/payment-links/create)
- [Tax API](https://docs.stripe.com/tax/custom)
- [Transactions](https://dashboard.stripe.com/payments)
- [Zero tax amounts](https://docs.stripe.com/tax/zero-tax)
- [Tax Transactions](https://dashboard.stripe.com/test/tax/transactions)