# Automatic migration to Bank Transfers

## Learn what changes you can expect when Bank Transfers replace ACH Credit Transfers.

#### Warning

We deprecated the Sources API and plan to remove support for local payment
methods. If you currently integrate with ACH Credit Transfers, you must [migrate
to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning).

For information about migrating to USD Bank Transfer supported by the current
APIs, refer to the documentation below.

Stripe is replacing the ACH Credit Transfers payment method with [Bank
Transfers](https://docs.stripe.com/payments/bank-transfers). As part of the
[Sources API](https://docs.stripe.com/sources) deprecation, Stripe is replacing
the ACH Credit Transfers payment method with Bank Transfers, so you won’t be
able to use ACH Credit Transfers in your workflows moving forward. This
migration occurs automatically for accounts processing ACH Credit Transfers
through invoices or subscriptions.

You might need to adjust your integration if:

- Your setup includes webhook endpoints listening for
`source.transaction.created`, `source.chargeable`,
`source.refund_attributes_required`, or `customer.source.created` events. Learn
more about [changes to
webhooks](https://docs.stripe.com/payments/customer-balance/ach-ct-automigration#webhooks).
- You use the Billing API and depend on ACH Credit Transfer source objects.
Learn more about [changes to the
API](https://docs.stripe.com/payments/customer-balance/ach-ct-automigration#api-changes).

Otherwise, you don’t need to take any action, and the migration won’t disrupt
your operations or those of your customers.

During the migration to Bank Transfers:

- There won’t be any change to the bank account information that your customers
currently use to send credit transfers.
- The automatic migration appears seamless from your customer’s perspective. The
structure of the hosted invoice page or PDF that you currently share with your
customer won’t change.
- Existing open invoices and subscriptions with ACH Credit Transfer as an
enabled payment method update to present Bank Transfers instead.

### Bank Transfer improvements

Bank Transfers allow you to:

- **Reconcile multiple invoices**: You can reconcile multiple invoices with a
single transfer using our [reconciliation
algorithm](https://docs.stripe.com/payments/customer-balance/reconciliation),
allowing your customers to pay batches of invoices with one bank transfer. You
can also use manual reconciliation mode, configurable at an account or customer
level.
- **Use an enhanced refund process**: This includes a customer refund email
outreach flow with a UI that allows your customers to enter their bank account
details for refunds.
- **Use test mode**: You can simulate bank transfer fundings in [test
mode](https://docs.stripe.com/payments/bank-transfers/accept-a-payment#test-your-integration)
to test edge cases of overfunding or underfunding, and fundings associated with
specific banking rails such as ACH, Fedwire, or SWIFT.
- **Generate a self-serve VBAN ownership letter**: You can generate a self-serve
VBAN ownership letter for your customers through the Dashboard.
- **Add the USD Cash Balance payment method**: Stripe removes and replaces the
ACH Credit Transfer payment method linked to your customers with the USD Cash
Balance payment method.

## Dashboard changes

### Invoice page

Access the Invoice page through `dashboard.stripe.com/invoices/:id`.

BeforeAfter

![Enabled payment methods on an ACH CT finalized
invoice](https://b.stripecdn.com/docs-statics-srv/assets/finalized-invoice-ach-ct.2d503b8307cc702dd79874644d867dd0.png)

![Enabled payment methods on an US BT finalized
invoice](https://b.stripecdn.com/docs-statics-srv/assets/finalized-invoice-bank-transfers.841f376519d6ae28c46f872b6c68e9e3.png)

### Subscription page

Access the Subscription page through `dashboard.stripe.com/subscriptions/:id`.

BeforeAfter

![Enabled payment methods on an active ACH CT
subscription](https://b.stripecdn.com/docs-statics-srv/assets/active-sub-ach-ct.acaaa32f29f6e3e823876a2ebfff67d0.png)

![Enabled payment methods on an active US BT
subscription](https://b.stripecdn.com/docs-statics-srv/assets/active-sub-bank-transfers.b5bd09779d0526f003c458d63226b667.png)

Stripe removes and replaces the ACH Credit Transfer payment method linked to
your customers with the USD Cash Balance payment method. If your customer has
unreconciled funds in their ACH Credit Transfer payment method, those funds move
to their cash balance. You’ll no longer have the ability to use the ACH Credit
Transfer payment method for any operation. This change appears in the Payment
methods section of the Customer page.

### Customer page

Access the Customer page through `dashboard.stripe.com/customers/:id`.

BeforeAfter

![Customer payment methods include an ACH CT
Source](https://b.stripecdn.com/docs-statics-srv/assets/payment-methods-ach-ct.96b39208706968c8917fae2daa6f6256.png)

![Customer payment methods include an cash
balance](https://b.stripecdn.com/docs-statics-srv/assets/payment-methods-usd-cash-balance.56d2bed995e79c1b8c92ed62c0b2e912.png)

### Payment method view

Access the Payment method view through `dashboard.stripe.com/sources/:id` for
ACH credit transfers and
`dashboard.stripe.com/customers/:id/cash_balance_transactions/usd` for Bank
Transfers.

BeforeAfter

![Source
page](https://b.stripecdn.com/docs-statics-srv/assets/payment-method-view-source.985dc3570620fdfbd688eb0957362ef8.png)

Source object view

![Customer cash balance
page](https://b.stripecdn.com/docs-statics-srv/assets/payment-method-view-cash-balance.e501f43fc23e6869b81f9d2ad974ab71.png)

View balance details page
### Balance details view

The **Balance details** view for a customer offers a comprehensive overview of
all bank transfer data associated with that customer:

- Shows the customer’s bank account information.
- Lists all transactions applied to the customer’s cash balance.
- Records all bank transfer refunds.
- Allows you to download a PDF letter confirming the ownership of the bank
account that you share with the customer. We encourage you to share this PDF
with your customers if they request it.

### Charge invoices

If you’re manually charging invoices through the Dashboard, you can continue
doing so using the same **Charge customer** button on
`dashboard.stripe.com/invoices/:id`:

![Manually charge
invoice](https://b.stripecdn.com/docs-statics-srv/assets/manually-charge-invoice.d4087ee1491e2fe486fd6283fb03d564.png)

In the **Charge customer** dialog, select **Cash Balance** instead of **ACH
Credit Transfer**:

BeforeAfter

![Manually charge invoice with ACH CT
modal](https://b.stripecdn.com/docs-statics-srv/assets/charge-invoice-modal-ach-ct.408e05878c43907eb572e38f0dc0f257.png)

![Manually charge invoice with US BT
modal](https://b.stripecdn.com/docs-statics-srv/assets/charge-invoice-modal-cash-balance.0357e549a456a527d450363cf78125c9.png)

#### Note

You can charge old ACH credit transfer invoices using the **Cash Balance** if
they don’t have bank transfer as an enabled payment method.

### ACH Credit Transfer settings

If you currently set ACH Credit Transfer as enabled by default for all your
invoices, you see a change in your account’s [invoice
settings](https://dashboard.stripe.com/settings/billing/invoice) under **Default
payment terms**:

![Invoice template
settings](https://b.stripecdn.com/docs-statics-srv/assets/invoice-template-settings.beffb3d4689b00cad766ded9094b5271.png)

Because Bank Transfers have automatically been enabled in your invoice settings,
all new invoices generated on your account (either manually or through existing
or new subscriptions) will enable Bank Transfers by default.

If ACH Credit Transfer is currently disabled (meaning, it’s not included by
default on all your invoices), Stripe doesn’t update your account’s invoice
settings.

### Reconciliation

Overall, the reconciliation logic of Bank Transfers aligns with Credit Transfers
when a transfer reaches Stripe:

- First, it attempts to match the bank transfer reference with the [invoice
number](https://docs.stripe.com/api/invoices/object#invoice_object-number).
- If that doesn’t work, it then tries to match the transfer amount with the
amount of the customer’s open invoices.
- If there’s no exact amount match, the algorithm funds as many invoices as
possible in full, prioritizing the oldest finalized invoices first.

However, there’s a slight difference in the detailed logic of the step where
Stripe matches by exact amount:

- In ACH Credit Transfer, Stripe attempts to match only one invoice by the exact
amount.
- With Bank Transfers, Stripe searches for a group of 1-5 invoices that total
the exact amount the user sent. Stripe then sorts those groups based on their
size and finalization date, enabling your customers to batch pay multiple
invoices with the same transfer.

Learn more about how [Bank Transfers reconciliation
works](https://docs.stripe.com/payments/customer-balance/reconciliation).

### Refunds

Overall, the refund logic of Bank Transfers aligns with ACH Credit Transfers:

- You issue a credit or bank transfer invoice to your customer.
- Your customer sends a transfer to the specified bank account.
- The transfer reaches Stripe and gets reconciled to the open invoice. The
invoice status changes to paid.
- You issue a refund for the payment related to that invoice.
- The customer receives an email prompting them to enter their bank account
details for the refund.
- Stripe processes the refund to the provided bank account.

You can process refunds using the same interface you currently use. Learn more
about [refunding a
customer](https://support.stripe.com/questions/refund-a-customer).

You can send the refunded funds to the cash balance instead of sending them to
the customer’s bank account. This allows you to use those funds for the
customer’s future invoices:

![Refund to customer cash
balance](https://b.stripecdn.com/docs-statics-srv/assets/refund-to-cash-balance.cc751b7e154b3bb74595ed59691bc224.png)

We have also updated the user interface that your customers use to enter their
bank account details in response to the email outreach:

BeforeAfter

![ACH CT refund
email](https://b.stripecdn.com/docs-statics-srv/assets/refund-email-ui-ach-ct.a618f929730f65438b568003a6c8f6a9.png)

![US BT refund
email](https://b.stripecdn.com/docs-statics-srv/assets/refund-email-ui-bank-transfers.af683982e61f0400eda5ce6ce8bbb25f.png)

Learn more about [bank transfer
refunds](https://docs.stripe.com/payments/customer-balance/refunding).

### Unreconciled funds

Similar to ACH Credit Transfers, Bank Transfers can manage cases of
over-funding. In the deprecated product, the remaining funds are stored in the
`Source` object, but in Bank Transfers, unreconciled funds go to the customer’s
cash balance. In both situations, you can either capture those funds by creating
a payment or choose to return them to the sender. If the unreconciled funds
remain unclaimed for a certain period, Stripe performs specific actions to
address it.

FunctionalityBeforeAfterStorage of unreconciled fundsSource objectCustomer cash
balanceInspect unreconciled funds

![Uncharged sources
page](https://b.stripecdn.com/docs-statics-srv/assets/uncharged-sources.4cc4b4b82ecce74a63b35b0127c22aa3.png)

[dashboard.stripe.com/uncharged_sources](https://dashboard.stripe.com/uncharged_sources)

![Unreconciled customer balances
page](https://b.stripecdn.com/docs-statics-srv/assets/unreconciled-balances.4877326166c7e61bd25549ed75b8be56.png)

Remaining Balances tab
of[dashboard.stripe.com/customers](https://dashboard.stripe.com/customers)Take
action on unreconciled funds

![Actioning uncharged
source](https://b.stripecdn.com/docs-statics-srv/assets/action-uncharged-source.3f6505dc80624d94a3f89a3c16a40e43.png)

[dashboard.stripe.com/uncharged_sources](https://dashboard.stripe.com/uncharged_sources)

![Actioning unreconciled customer
balance](https://b.stripecdn.com/docs-statics-srv/assets/action-unreconciled-cash-balance.c2998d0e9aa3c6477a0e4da50582401d.png)

[dashboard.stripe.com/customers](https://dashboard.stripe.com/customers)Failing
to timely action unreconciled fundsIf an unreconciled funding remains at the
Source for more than 45 days, it automatically sweeps to your account balance.
The sweeping process is executed on a monthly basis (on the 15th of each month)
and sweeps fundings that are older than 45 days. Hence, a funding can remain
un-actioned in the source from 45 to 60 days.An unreconciled funding can remain
un-actioned in the cash balance of a customer for 75 days. At that point, Stripe
attempts to automatically refund the funds back to the customer. If the refund
to your customer fails (for example, if the customer doesn’t enter their bank
information following the email outreach), Stripe leaves the funds in the cash
balance for another 15 days. At the 90-day mark, Stripe sweeps the unreconciled
funding to your Stripe account balance.
Learn more about [how unreconciled funds are handled in Bank
Transfers](https://docs.stripe.com/payments/customer-balance/reconciliation?#cash-unreconciled-funds).

## Webhooks

#### Note

Skip this section if you haven’t configured webhook endpoints listening for
`source.transaction.created`, `source.chargeable`,
`source.refund_attributes_required`, or `customer.source.created` events. See
what endpoints you’ve configured in the
[Dashboard](https://dashboard.stripe.com/webhooks).

After your account automatically migrates to Bank Transfers, the following
webhook events related to ACH Credit Transfer stop:

- `source.transaction.created`
- `source.chargeable`
- `customer.source.created`
- `source.refund_attributes_required`

Verify that the suspension of ACH Credit Transfer webhook events won’t impact
your workflows. If your integration depends on these events (for example, a
plugin or app installed on your Stripe account might be listening for them),
[contact
us](https://support.stripe.com/contact/email?question=other&topic=api_integration&subject=%20Support%20with%20Sources%20migration%20requirement&refcode=U5tB).

## Changes with the Billing API

#### Note

Skip this section if you don’t integrate with the Stripe API for Billing.

The [Invoice](https://docs.stripe.com/api/invoices) objects created as part of
your Billing API integration start referencing `customer_balance` (the payment
method type of Bank Transfers) instead of `ach_credit_transfer`.

Invoices APISubscriptions API
To create an invoice, send the following request:

```
curl https://api.stripe.com/v1/invoices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d currency=usd \
 -d collection_method=send_invoice \
 -d days_until_due=30
```

To finalize an invoice, send the following request:

```
curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}}/finalize \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "expand[]"=payment_intent
```

Here’s the finalized [Invoice](https://docs.stripe.com/api/invoices) object:

```
{
 "id": "{{INVOICE_ID}}",
 "object": "invoice",
 "payment_intent": {
 "object": "payment_intent",
 "id": "{{PAYMENT_INTENT_ID}}",
 "payment_method_types": [
 "ach_credit_transfer",
 "customer_balance"
 ]
 }
}
```

If you create [Invoice](https://docs.stripe.com/api/invoices) and
[Subscription](https://docs.stripe.com/api/subscriptions) objects by explicitly
including `ach_credit_transfer` in the
[payment_settings.payment_method_types](https://docs.stripe.com/api/invoices/create#create_invoice-payment_settings-payment_method_types)
array parameter, your integration still functions properly and you can continue
to pass `ach_credit_transfer` as part of your request. However, Stripe adjusts
your request, and the `Invoice` and `Subscription` objects you created list
`customer_balance` instead of `ach_credit_transfer`:

```
curl https://api.stripe.com/v1/invoices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d customer={{CUSTOMER_ID}} \
 -d currency=usd \
 -d collection_method=send_invoice \
 -d days_until_due=30 \
 -d "payment_settings[payment_method_types][]"=ach_credit_transfer \
 -d "payment_settings[payment_method_types][]"=card
```

Here’s the finalized `Invoice` and `PaymentIntent` objects:

```
{
 "id": "{{INVOICE_ID}}",
 "object": "invoice",
 "payment_settings": {
 "payment_method_types": [
 "ach_credit_transfer",
 "card",
 "customer_balance"
 ]
 },
 "payment_intent": {
 "object": "payment_intent",
 "id": "{{PAYMENT_INTENT_ID}}",
 "payment_method_types": [
 "ach_credit_transfer",
 "customer_balance"
 ]
 }
}
```

Stripe also updates historical `Subscription` objects in your account that you
created with `ach_credit_transfer` included in the
[payment_settings.payment_method_types](https://docs.stripe.com/api/invoices/create#create_invoice-payment_settings-payment_method_types)
array parameter. The `payment_settings.payment_method_types` array of your
existing `Subscription` objects updates to include `customer_balance` instead of
`ach_credit_transfer`.

If your API integration relies on `ach_credit_transfer` being present in any of
the following API response fields, [contact
us](https://support.stripe.com/contact/email?question=other&topic=api_integration&subject=%20Support%20with%20Sources%20migration%20requirement&refcode=U5tB)
because the automatic migration might disrupt your integration:

- The Invoice object’s
[payment_settings.payment_method_types](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings-payment_method_types)
- The Subscription object’s
[payment_settings.payment_method_types](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-payment_method_types)
- The Payment Intent object’s
[payment_method_types](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_types)

The ACH Credit Transfer `Source` objects detach from your customers. This means
that if you depend on the
[Customer.default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source)
field being present, you might find that it starts returning as `null` instead
of the `src_` ID of the ACH Credit Transfer source previously attached to the
customer.

## Opt out

To exclude your account from the automatic migration, [contact
us](https://support.stripe.com/contact/email?question=other&topic=api_integration&subject=%20Support%20with%20Sources%20migration%20requirement&refcode=U5tB).
We’ll provide you with a deadline to manually migrate your account to Bank
Transfers. You won’t be able to continue using the deprecated ACH Credit
Transfer product.

## Links

- [migrate to the Payment Methods
API](https://docs.stripe.com/payments/payment-methods/transitioning)
- [Bank Transfers](https://docs.stripe.com/payments/bank-transfers)
- [Sources API](https://docs.stripe.com/sources)
- [reconciliation
algorithm](https://docs.stripe.com/payments/customer-balance/reconciliation)
- [test
mode](https://docs.stripe.com/payments/bank-transfers/accept-a-payment#test-your-integration)
- [invoice settings](https://dashboard.stripe.com/settings/billing/invoice)
- [invoice
number](https://docs.stripe.com/api/invoices/object#invoice_object-number)
- [refunding a customer](https://support.stripe.com/questions/refund-a-customer)
- [bank transfer
refunds](https://docs.stripe.com/payments/customer-balance/refunding)
-
[dashboard.stripe.com/uncharged_sources](https://dashboard.stripe.com/uncharged_sources)
- [dashboard.stripe.com/customers](https://dashboard.stripe.com/customers)
- [how unreconciled funds are handled in Bank
Transfers](https://docs.stripe.com/payments/customer-balance/reconciliation?#cash-unreconciled-funds)
- [Dashboard](https://dashboard.stripe.com/webhooks)
- [contact
us](https://support.stripe.com/contact/email?question=other&topic=api_integration&subject=%20Support%20with%20Sources%20migration%20requirement&refcode=U5tB)
- [Invoice](https://docs.stripe.com/api/invoices)
- [Subscription](https://docs.stripe.com/api/subscriptions)
-
[payment_settings.payment_method_types](https://docs.stripe.com/api/invoices/create#create_invoice-payment_settings-payment_method_types)
-
[payment_settings.payment_method_types](https://docs.stripe.com/api/invoices/object#invoice_object-payment_settings-payment_method_types)
-
[payment_settings.payment_method_types](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-payment_method_types)
-
[payment_method_types](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method_types)
-
[Customer.default_source](https://docs.stripe.com/api/customers/object#customer_object-default_source)