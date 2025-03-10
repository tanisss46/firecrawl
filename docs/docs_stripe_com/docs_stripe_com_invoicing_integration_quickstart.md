using the link in the code editor.

TerminalBundlerGitHub
Install the gem:

`gem install stripe`Server
### Manage Products, Prices, and Customers

First, create a price for your product in the
[Dashboard](https://docs.stripe.com/invoicing/products-prices) or through the
[API](https://docs.stripe.com/api/prices/create). After you create a price and
associate it with a product, store its ID in your database.

Next, look up a [Customer](https://docs.stripe.com/api/customers) in your
database by
[email](https://docs.stripe.com/api/customers/object?lang=dotnet#customer_object-email).
If that customer doesn’t exist, create the `Customer` and store their ID for
future purchases. The next step, for example, uses the
[id](https://docs.stripe.com/api/customers/object#customer_object-id) of
[Customer object](https://docs.stripe.com/api/customers/object) to create an
invoice.

#### Note

The `Customer` object represents the customer purchasing your product. It’s
required for creating an invoice.

Server2Create an Invoice item and Invoice
### Create an Empty Invoice

Set the
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
attribute to `send_invoice`. For Stripe to mark an invoice as past due, you must
add the
[days_until_due](https://docs.stripe.com/api/invoices/create#create_invoice-days_until_due)
parameter. When you send an invoice, Stripe emails the invoice to the customer
with payment instructions.

#### Note

The other available collection method is `charge_automatically`. When charging
automatically, Stripe attempts to immediately pay the invoice using the default
source that’s attached to the customer. Here, we use `send_invoice` to prevent
an immediate, undesired customer charge.

Server
### Create an Invoice Item

Create an invoice item by passing in the customer `id`, product `price`, and
invoice ID `invoice`.

The maximum number of invoice items is 250.

#### Note

If invoice items are created before an invoice is created, set the
[pending_invoice_items_behavior](https://docs.stripe.com/api/invoices/create#create_invoice-pending_invoice_items_behavior)
to `include` when creating the invoice so that all pending invoice items are
automatically added to the invoice. In this case, only add invoice items to a
single customer at a time to avoid adding them to the wrong customer.

Creating an invoice adds up to 250 pending invoice items with the remainder to
be added on the next invoice. To see your customer’s pending invoice items, see
the **Customer details** page or set the
[pending](https://docs.stripe.com/api/invoiceitems/list#list_invoiceitems-pending)
attribute to `true` when you use the API to list all of the invoice items.

Server3Send an Invoice
Send the invoice to the email address associated with the customer. As soon as
you send an invoice, Stripe finalizes it. Many jurisdictions consider finalized
invoices a legal document making certain fields unalterable. If you send
invoices that have already been paid, there’s no reference to the payment in the
email.

With any finalized invoice, you can either download and send a
[PDF](https://docs.stripe.com/api/invoices/object#invoice_object-invoice_pdf) or
[link](https://docs.stripe.com/api/invoices/object#invoice_object-hosted_invoice_url)
to the associated [Hosted Invoice
Page](https://docs.stripe.com/invoicing/hosted-invoice-page).

Server
## Congratulations!

You’ve created and sent your first invoice. Take your integration further and
learn how to quickly automate tax collection through the API.

### Automate tax collection

Calculate and collect the right amount of tax on your Stripe transactions. Learn
more about [Stripe Tax](https://docs.stripe.com/tax), and how to [activate
it](https://dashboard.stripe.com/settings/tax/activate) in the Dashboard before
you integrate it.

## Next steps

#### [Use incoming webhooks to get real-time updates](https://docs.stripe.com/webhooks)

Listen for events on your Stripe account so your integration can automatically
trigger reactions.

#### [Customize invoices](https://docs.stripe.com/invoicing/customize)

You can use the [Invoice
template](https://dashboard.stripe.com/account/billing/invoice) to customize
​​the content of an invoice. You can also set a customer preferred language and
include public information in your [account
details](https://dashboard.stripe.com/settings/account/?support_details=true).

#### [Invoicing API](https://docs.stripe.com/api/invoices)

Learn more about the Invoicing API.

#### [Stripe CLI](https://docs.stripe.com/stripe-cli)

The Stripe CLI has several commands that can help you test your Stripe
application beyond invoicing.

server.rbwebhook.rbDownload
```
# Create and send an invoice
Create and send a Stripe-hosted invoice in minutes.
## Running the sample
1. Build the server
~~~bundle install~~~
2. Run the server
~~~ruby server.rb -o 0.0.0.0~~~

## Testing the webhook
Use the Stripe CLI to test your webhook locally. Download [the
CLI](https://github.com/stripe/stripe-cli) and log in with your Stripe account.
Alternatively, use a service like ngrok to make your local endpoint publicly
accessible.
Set up event forwarding with the CLI to send all Stripe events in test mode to
your local webhook endpoint.
~~~stripe listen --forward-to localhost:4242/webhook~~~
Use the CLI to simulate specific events that test your webhook application logic
by sending a POST request to your webhook endpoint with a mocked Stripe event
object.
~~~stripe trigger payment_intent.succeeded~~~
```

## Links

- [text version of this
guide](https://docs.stripe.com/payments/accept-a-payment)
- [View the text-based guide](https://docs.stripe.com/invoicing/integration)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [Dashboard](https://docs.stripe.com/invoicing/products-prices)
- [API](https://docs.stripe.com/api/prices/create)
- [Customer](https://docs.stripe.com/api/customers)
-
[email](https://docs.stripe.com/api/customers/object?lang=dotnet#customer_object-email)
- [id](https://docs.stripe.com/api/customers/object#customer_object-id)
- [Customer object](https://docs.stripe.com/api/customers/object)
-
[collection_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method)
-
[days_until_due](https://docs.stripe.com/api/invoices/create#create_invoice-days_until_due)
-
[pending_invoice_items_behavior](https://docs.stripe.com/api/invoices/create#create_invoice-pending_invoice_items_behavior)
-
[pending](https://docs.stripe.com/api/invoiceitems/list#list_invoiceitems-pending)
- [PDF](https://docs.stripe.com/api/invoices/object#invoice_object-invoice_pdf)
-
[link](https://docs.stripe.com/api/invoices/object#invoice_object-hosted_invoice_url)
- [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page)
- [Stripe Tax](https://docs.stripe.com/tax)
- [activate it](https://dashboard.stripe.com/settings/tax/activate)
- [Use incoming webhooks to get real-time
updates](https://docs.stripe.com/webhooks)
- [Customize invoices](https://docs.stripe.com/invoicing/customize)
- [Invoice template](https://dashboard.stripe.com/account/billing/invoice)
- [account
details](https://dashboard.stripe.com/settings/account/?support_details=true)
- [Invoicing API](https://docs.stripe.com/api/invoices)
- [Stripe CLI](https://docs.stripe.com/stripe-cli)