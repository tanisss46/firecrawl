# Send quotes

## Send a quote and convert it to a payment or subscription.

With quotes, provide price estimates to your customers that you can convert into
[invoices](https://docs.stripe.com/api/invoices) or
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating). You can
combine recurring and one-off line items, including any discounts or taxes.

![Quote
PDF](https://b.stripecdn.com/docs-statics-srv/assets/quote-pdf.fbd3abb09a59b6be9f1c692ab402691c.png)

The generated quote PDF

[Create a quote](https://docs.stripe.com/no-code/quotes#create-quote-dashboard)
To create a quote in the Stripe Dashboard:

- Go to the [Billing tab](https://dashboard.stripe.com/billing).
- Click **Quick actions** > **Create quote** (or go directly to the [quote
editor](https://dashboard.stripe.com/test/quotes/create)).
- Select **+ Add new customer**. At a minimum, enter your customer’s **Name**
and **Account email**. Click **Add customer**.
- Under **Items**, add or select a product. (You can also add a coupon.)
- Choose an expiration date.
- (Optional) Write a memo, and add a custom header and footer. You can set the
future default text for the header and footer in the [quote
template](https://dashboard.stripe.com/settings/billing/quote).
- To preview the quote PDF (which shows the generated quote number) click
**Download preview**.
- Click **Finalize quote**.

![Quote
editor](https://b.stripecdn.com/docs-statics-srv/assets/create-quote-editor.b0567a67946f35c4844e0979f2bc7019.png)

Quote editor

After you finalize the quote, send it to your customer:

- To download the quote, go to **Quotes details page** > **Quote PDF**.
- Use an external email address to send the PDF to your customer for review.
[Mark a quote as
accepted](https://docs.stripe.com/no-code/quotes#accept-quote-dashboard)
After your customer accepts the quote, bill them by converting the quote into an
invoice or subscription.

You can only create one-off invoices if a quote *only* has one-time prices.

If a quote has at least one recurring price, you can only convert it to a
subscription.

### Convert a quote to an invoice

- To mark a quote as accepted and create a draft invoice, go to **Convert to
invoice** > **Quotes details**.
- Use the [invoice editor](https://dashboard.stripe.com/test/invoices/create) to
modify the draft invoice as needed.
- Email the invoice or automatically charge the customer.

### Convert a quote to a subscription

- In the quote editor, choose a customer and create or select a product with a
recurring price.
- Enter the quote details and choose to either **Start the subscription
immediately** or **Schedule a subscription start date**.
- Finalize the quote. This marks the quote as **Accepted**.
- Go to **Convert to subscription** > **Quotes details**.
- Enter or modify the subscription details, then click **Create subscription**.

If you schedule the subscription to start immediately, Stripe creates an active
subscription along with a draft invoice for the initial payment. Stripe
finalizes the draft invoice automatically in 1 hour. Otherwise, the subscription
begins on the scheduled start date. Depending on the subscription’s payment
terms, Stripe collects payment by either charging the customer’s payment method
on file or sending them an invoice.

## See also

- [Accessing quotes](https://support.stripe.com/questions/how-to-access-quotes)
- [How quotes work](https://docs.stripe.com/quotes/overview)

## Links

- [Pay-as-you-go](https://stripe.com/pricing)
- [Stripe Billing pricing](https://stripe.com/billing/pricing)
- [Invoicing pricing](https://stripe.com/invoicing/pricing)
- [invoices](https://docs.stripe.com/api/invoices)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Billing tab](https://dashboard.stripe.com/billing)
- [quote editor](https://dashboard.stripe.com/test/quotes/create)
- [quote template](https://dashboard.stripe.com/settings/billing/quote)
- [invoice editor](https://dashboard.stripe.com/test/invoices/create)
- [Accessing quotes](https://support.stripe.com/questions/how-to-access-quotes)
- [How quotes work](https://docs.stripe.com/quotes/overview)