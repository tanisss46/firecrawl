# Stripe and NetSuite fields and references

## Learn how the Stripe Connector for NetSuite applies fields to Stripe and NetSuite records.

Use the list below to identify the correlation between Stripe records and
NetSuite records.

## Stripe and NetSuite object mapping

NetSuite represents Stripe records as follows:

Stripe objectNetSuite recordChargeCustomer paymentCredit noteCredit memo (in
most cases) and refund (in some cases)CouponDiscount
itemCustomerCustomerDisputeCustomer refundInvoiceInvoice and credit memo (in
some cases)Invoice itemService sale item or discount
itemPayoutDepositPriceService sale itemRefundCustomer refund and credit memo (in
some cases)SubscriptionNone (monthly invoices represent subscriptions)
## NetSuite record IDs and Stripe IDs

When a Stripe record successfully syncs to NetSuite, the NetSuite internal ID
for the new record saves to the metadata of the Stripe record.

NetSuite stores the Stripe ID as follows:

RecordID placement in NetSuiteCreditMemomemo, externalIdCustomerComments (only
added if externalId is empty)CustomerPaymentmemo, externalIdDepositmemo,
externalIdDisputememo, externalIdInvoicememo, externalIdNetSuite items
(discount, service sales item, and so on)Item Name, Item ID, other display name
fields, externalId
## NetSuite memo fields

A `Stripe:` prefixes any memo fields that contain the corresponding Stripe
record ID. This allows you to identify which Stripe record corresponds to a
NetSuite record. The connector doesn’t use the memo field in NetSuite and adds
notes for informational purposes only. You can safely wipe or override the memo
field on any created records.

The connector stores additional information in the memo field for a NetSuite
record in the following cases:

- If you modify a transaction date, the memo includes the original transaction
date. This ensures successful translation of the record. For example, `Original
transaction date: 2023-04-01`.
- If a charge isn’t associated with an invoice or order, the customer payment
memo includes the charge description. For example, `Stripe description: charge
for invoice 12345`.
- If an invoice increases a customer’s balance, the NetSuite invoice includes
the amount.
- If a credit memo represents an invoice payment from a customer’s balance, the
credit memo includes the payment.

## NetSuite external IDs

The external ID for every Stripe-created NetSuite record is set to the ID of the
corresponding Stripe record. This allows you to retrieve a record from NetSuite
using the Stripe record ID.

In some exceptions, the external ID is prefixed:

- **Credit memos**: The external ID is prefixed with `ns_memo:`. For example, if
the refund ID is `re_abcd`, the credit memo external ID is `ns_memo:re_abcd`.
- **Discount items for Stripe prices**: The external ID is prefixed with the ID
of the price object that the discount is applied to.

If you have other integrations in your NetSuite instance, make sure not to
overwrite the external IDs that Stripe sets on records.

## NetSuite record fields

The connector uses the NetSuite record fields listed below, by default. These
fields must exist on the custom forms used for any records that the connector
creates or uses.

RecordFieldsNotesInvoice (read only)- amountRemaining
- status
- currency
- custbody_suitesync_authorization_code
- tranId
- memo
- createdFrom
- entity
- externalId
The `amountRemaining` is also called Amount Due.CustomerexternalIdCreditMemo-
memo
- currency
- custbody_suitesync_authorization_code
- line items sub-list
CustomerPayment- memo
- currency
- paymentMethod
- account
- payment
- tranDate
Always set the `tranDate` to the exact date of the transaction in Stripe. Set
the `paymentMethod` to the Stripe payment method (automatically created in your
account). The connector sets the `account` to the undeposited funds
account.CustomerRefund- memo
- currency
- tranDate
- paymentMethod
- account
Always set the `tranDate` to the exact date of the transaction in Stripe. Set
the `paymentMethod` to the Stripe payment method (automatically created in your
account). The connector sets the `account` to the undeposited funds
account.Deposit- currency
- memo
- all sub-lists (payment list, other deposits, cash back)

## See also

- [Field mappings](https://docs.stripe.com/connectors/netsuite/field-mappings)
- [Sync Stripe data to
NetSuite](https://docs.stripe.com/connectors/netsuite/sync-data)

## Links

- [Field mappings](https://docs.stripe.com/connectors/netsuite/field-mappings)
- [Sync Stripe data to
NetSuite](https://docs.stripe.com/connectors/netsuite/sync-data)