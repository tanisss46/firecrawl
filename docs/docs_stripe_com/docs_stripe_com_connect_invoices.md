# Create invoices with Connect

## With Connect, you can create invoices for connected accounts, optionally taking fees in the process.

You can create [invoices](https://docs.stripe.com/api/invoices) for connected
accounts, which support [several
approaches](https://docs.stripe.com/connect/charges) for collecting payments.
You can use [direct charges](https://docs.stripe.com/connect/direct-charges) to
create them directly on the connected account. Alternatively, you can create
invoices on the platform with transfers to the connected account by using
[destination charges](https://docs.stripe.com/connect/destination-charges). You
can also take an application fee on these invoices.

#### Note

Invoice transactions are based on [Invoicing
pricing](https://stripe.com/invoicing/pricing).

## Create an invoice using direct charges

To create an invoice that directly charges on a connected account, [create an
invoice](https://docs.stripe.com/api#create_invoice) while
[authenticated](https://docs.stripe.com/connect/authentication#stripe-account-header)
as the connected account. For this to work, the customer must be defined on the
connected account.

```
curl https://api.stripe.com/v1/invoices \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d customer={{CUSTOMER_ID}} \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

As with [creating a direct
charge](https://docs.stripe.com/connect/direct-charges#collect-fees) on a
connected account, you can create a customer on a connected account by using
either the platform’s publishable key or the connected account’s publishable
key. You can also create a token by using [shared
customers](https://docs.stripe.com/connect/cloning-customers-across-accounts).
When you use direct charges, the connected account is responsible for the cost
of the Stripe fees, refunds, and chargebacks.

## Create an invoice using destination charges

To create an invoice that charges on the platform and creates automatic
transfers to a connected account, [create an
invoice](https://docs.stripe.com/api#create_invoice) while providing the
connected account ID as the `transfer_data[destination]`
[value](https://docs.stripe.com/api/invoices/object#invoice_object-transfer_data).

```
curl https://api.stripe.com/v1/invoices \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d customer={{CUSTOMER_ID}} \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}
```

For this to work, the customer must be defined on the platform account, and you
must create the connected account token by using the platform’s publishable key.
If charging a customer, the customer must exist within the platform account.
When using automatic transfers, the platform is the business of record.

## Display Connected Account Tax IDs and Business Details on your Invoices

Certain regions have regulatory requirements for merchants to show their tax IDs
and other business details on customer-facing documents.

In some cases, you can fulfill these requirements by displaying information
about a connected account instead of information about your platform. The
following steps show how to render a connected account’s tax ID and business
details on invoice emails, invoice PDFs, Hosted Invoice Pages, and invoice
receipts:

- Create tax IDs for your connected account.
- Set default tax IDs for your connected account.
- Specify the connected account either using the [on_behalf_of
parameter](https://docs.stripe.com/connect/invoices#on-behalf-of) or as the
`issuer` on existing or new invoices, subscriptions, and subscription schedules.

### Create tax IDs for your connected account

The following example creates a single tax ID for the connected account. Stripe
stores the tax ID on the connected account. To create additional tax IDs, call
the endpoint again.

```
curl https://api.stripe.com/v1/tax_ids \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d type=eu_vat \
 -d value=DE123456789
```

### Set default tax IDs for your connected account

Stripe automatically pulls default tax IDs from the invoice `issuer`’s account
during finalization unless `account_tax_ids` is already set on the invoices.

You can set the tax IDs stored on the connected account as the default tax IDs
for that account. The following example sets existing tax IDs as default tax
IDs:

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "settings[invoices][default_account_tax_ids][0]"=atxi_123 \
 -d "settings[invoices][default_account_tax_ids][1]"=atxi_456
```

### Set issuer on existing or new invoices, subscriptions, and subscription schedules as the connected account

The following example sets `issuer` on an existing subscription. During invoice
finalization, subscription invoices pull in the issuer’s default tax IDs:

```
curl https://api.stripe.com/v1/subscriptions/{{SUBSCRIPTION_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "invoice_settings[issuer][type]"=account \
 -d "invoice_settings[issuer][account]"={{CONNECTED_ACCOUNT_ID}}
```

The following example sets `issuer` during invoice creation:

```
curl https://api.stripe.com/v1/invoices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "issuer[type]"=account \
 -d "issuer[account]"={{CONNECTED_ACCOUNT_ID}} \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}
```

Alternatively, the `on_behalf_of` parameter also prints a connected account’s
details on the invoice email, invoice PDF, Hosted Invoice Page, and invoice
receipt.

### Set account tax IDs on existing or new invoices, subscriptions, and subscription schedules

You can specify `account_tax_ids` for invoices, subscriptions, and subscription
schedules to override the default tax IDs. The following example sets
`account_tax_ids` on an existing subscription:

```
curl https://api.stripe.com/v1/subscriptions/{{SUBSCRIPTION_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "invoice_settings[issuer][type]"=account \
 -d "invoice_settings[issuer][account]"={{CONNECTED_ACCOUNT_ID}} \
 -d "invoice_settings[account_tax_ids][0]"=txi_123 \
 -d "invoice_settings[account_tax_ids][1]"=txi_456
```

The following example sets `account_tax_ids` during invoice creation:

```
curl https://api.stripe.com/v1/invoices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d "issuer[type]"=account \
 -d "issuer[account]"={{CONNECTED_ACCOUNT_ID}} \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}} \
 -d "account_tax_ids[0]"=txi_123 \
 -d "account_tax_ids[1]"=txi_456
```

### Create tax IDs stored on the platform for your connected account

The tax ID you create is stored on the platform account instead of the connected
account. The following example creates a single tax ID for the connected account
without using the `Stripe-Account` header:

```
curl https://api.stripe.com/v1/tax_ids \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d type=eu_vat \
 -d value=DE123456789 \
 -d "owner[type]"=account \
 -d "owner[account]"={{CONNECTED_ACCOUNT_ID}}
```

## Collect application fees

On the invoice, you can optionally withhold an application fee. The following
example shows an
[application_fee_amount](https://docs.stripe.com/api/subscriptions/object#subscription_object-application_fee_percent)
for an invoice with a direct charge on the connected account:

```
curl https://api.stripe.com/v1/invoices \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d customer={{CUSTOMER_ID}} \
 -d application_fee_amount="10" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"
```

This example shows an `application_fee_amount` for an invoice with a destination
charge:

```
curl https://api.stripe.com/v1/invoices \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d customer={{CUSTOMER_ID}} \
 -d application_fee_amount="10" \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}}
```

## Make the connected account the settlement merchant

To make the connected account the settlement merchant, charge the customer using
the `on_behalf_of` parameter when you create or update the invoice. You must set
`on_behalf_of` in the API before finalizing an invoice—the Dashboard doesn’t
have an interface for invoices you send on behalf of connected accounts.

Setting the `on_behalf_of` parameter applies the branding, contact information,
and account tax ID of the connected account to the invoice email, invoice PDF,
Hosted Invoice Page, and invoice receipt. However, when you use `on_behalf_of`
in test mode, emails aren’t sent—just like standard invoices sent via API. In
test mode, you can verify that Stripe created an invoice by checking the
[Invoices page](https://dashboard.stripe.com/test/invoices) of the Dashboard.

To collect payments on behalf of the connected account, the connected account
also needs to have [account
capabilities](https://docs.stripe.com/connect/account-capabilities) enabled for
the relevant payment methods. You can automatically transfer payments for
invoices created on behalf of the connected account by using destination
charges. For more information about the `on_behalf_of​` parameter, refer to the
relevant Connect documentation:

- For automatic transfers to the connected account, refer to the `on_behalf_of`
parameter details in the [Create a
charge](https://docs.stripe.com/connect/charges#on_behalf_of) guide.
- For information on how to transfer payments manually, refer to [Transfer
availability](https://docs.stripe.com/connect/separate-charges-and-transfers#transfer-availability).
- For a list of account capabilities that are required to collect payments on
behalf of the connected account, refer to [Payment method
capabilities](https://docs.stripe.com/connect/account-capabilities#payment-methods).

The following example shows how to use the `on_behalf_of` parameter for a new
invoice by using separate charges and transfers:

```
curl https://api.stripe.com/v1/invoices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d on_behalf_of={{CONNECTED_ACCOUNT_ID}} \
 -d customer={{CUSTOMER_ID}}
```

As with standard destination charges, ​​you can set an `application_fee_amount`
on invoices. This example shows how to use `on_behalf_of` with a destination
charge and application fee.

```
curl https://api.stripe.com/v1/invoices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d on_behalf_of={{CONNECTED_ACCOUNT_ID}} \
 -d application_fee_amount=10 \
 -d "transfer_data[destination]"={{CONNECTED_ACCOUNT_ID}} \
 -d customer={{CUSTOMER_ID}}
```

Invoices created on behalf of a connected account ​​don’t support bank transfers
payment methods, such as ACH Credit Transfer and paper checks.

## Integrate tax calculation and collection

You need to first determine which entity is liable for tax. The entity that’s
liable for tax might be your connected account or the platform, depending on
your business model. To learn more, see [Stripe Tax with
Connect](https://docs.stripe.com/tax/connect).

## See also

- [Create charges](https://docs.stripe.com/connect/charges)
- [Share customers across
accounts](https://docs.stripe.com/connect/cloning-customers-across-accounts)
- [Multiple currencies](https://docs.stripe.com/connect/currencies)

## Links

- [Connect](https://docs.stripe.com/connect)
- [invoices](https://docs.stripe.com/api/invoices)
- [several approaches](https://docs.stripe.com/connect/charges)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [Invoicing pricing](https://stripe.com/invoicing/pricing)
- [create an invoice](https://docs.stripe.com/api#create_invoice)
-
[authenticated](https://docs.stripe.com/connect/authentication#stripe-account-header)
- [creating a direct
charge](https://docs.stripe.com/connect/direct-charges#collect-fees)
- [shared
customers](https://docs.stripe.com/connect/cloning-customers-across-accounts)
-
[value](https://docs.stripe.com/api/invoices/object#invoice_object-transfer_data)
-
[application_fee_amount](https://docs.stripe.com/api/subscriptions/object#subscription_object-application_fee_percent)
- [Invoices page](https://dashboard.stripe.com/test/invoices)
- [account capabilities](https://docs.stripe.com/connect/account-capabilities)
- [Create a charge](https://docs.stripe.com/connect/charges#on_behalf_of)
- [Transfer
availability](https://docs.stripe.com/connect/separate-charges-and-transfers#transfer-availability)
- [Payment method
capabilities](https://docs.stripe.com/connect/account-capabilities#payment-methods)
- [Stripe Tax with Connect](https://docs.stripe.com/tax/connect)
- [Multiple currencies](https://docs.stripe.com/connect/currencies)