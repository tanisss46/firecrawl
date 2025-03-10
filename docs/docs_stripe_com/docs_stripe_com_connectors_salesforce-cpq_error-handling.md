# Error handling

## Learn how to handle errors when syncing Salesforce records using the connector.

If you encounter errors when using the Stripe Billing Connector for Salesforce
CPQ to sync records from Salesforce to Stripe, use the following list to
identify and resolve the errors. In most cases, you must modify the Salesforce
record data, then manually sync the record to recover from the error.

## Data errors

The table below contains the errors you might encounter when syncing Salesforce
orders and how to resolve them.

ErrorDescriptionRecommendationUnsupported field value for `days_until_due`.The
mapped field value for `days_until_due` must be an integer or supported `CPQ
Payment Term` value.Update the mapped field value for `days_until_due` with an
integer or a supported `CPQ Payment Term` value (for example, Net-15, Net-30,
Net-45, Net-60, or Net-90).Required mappings were empty for the Stripe
object.The connector requires specific fields on the order and order
items.Navigate to the Stripe Billing app in Salesforce and open the data mapper.
Make sure that you set all required fields under `Subscription Schedule`,
`Subscription Item`, and `Price Order Item`.The order line was deleted or not
activated.The order item’s fields indicate that it was deleted or not
activated.Verify that all order items are activated and not deleted.The
connector attempted to sync the amendment order when the initial order was
skipped, because it didn’t match custom sync filters.You can specify custom
order filters in the Stripe Billing app in Salesforce. These filters determine
whether or not to sync the Salesforce order.You can’t sync amendment Salesforce
orders before syncing the corresponding initial Salesforce order. This error
indicates that the initial Salesforce order failed to sync because it didn’t
pass the order filter criteria, even though the amendment Salesforce order
passed.
## Amendment errors

The table below contains the errors related to amendment orders and how to
resolve them.

ErrorDescriptionRecommendationOrder amendments must co-terminate with the
initial order.The Salesforce amendment order must end on the same date as the
initial Salesforce order.Update the Salesforce order amendment so that the end
date co-terminates with the initial order. This likely occurs when you update
the subscription term.The Stripe subscription for the evergreen order has
already been canceled and can’t be modified.The connector synced an evergreen
Salesforce amendment order that’s attempting to amend a canceled Stripe
subscription.The Salesforce amendment order can’t be synced.The Stripe
subscription schedule has already been canceled and can’t be modified.The
connector synced a Salesforce amendment order that’s attempting to amend a
canceled Stripe subscription schedule.The Salesforce amendment order can’t be
synced.Amendment orders must start on the same day of the month as the initial
order. Enable the feature for non-anniversary amendments to sync amendments on
any day of the month.The Salesforce amendment order starts on a different day of
the month than the initial order.Update the Salesforce amendment order to start
on the same day of the month as the initial Salesforce order, or contact support
to enable non-anniversary amendments in your account.The amendment order
subscription term doesn’t equal a number of whole months between the start and
end date.This occurs when a non-anniversary amendment is synced and the
subscription term for the quote is unexpected.Update the subscription term for
the Salesforce amendment order to be a number of whole months between the start
and end date of the Salesforce order.Unable to find the corresponding Stripe
subscription schedule for the amendment order.An amendment Salesforce order
modifies an initial Salesforce order that previously synced. This error
indicates that the corresponding Stripe subscription schedule created during the
initial Salesforce order sync can’t be found because it was deleted.The
Salesforce amendment order can’t be synced.The backend prorated order amendment
case isn’t supported.A Salesforce amendment order modifies an initial order that
was backend prorated, but the start dates don’t align.The connector doesn’t
support this use case. Contact [support](https://support.stripe.com/) for next
steps.The amendment order represents all one-time invoices.The amendment order
must amend the initial order.To sync an order with one-time invoice items, you
must create and sync a new order with the one-time invoice items.More than one
contract was found for the amendment order.The connector detected multiple
contracts associated with the amendment order.Make sure the amendment order has
only one contract associated with it.More than one quote was found for the
amendment order.The connector detected multiple quotes associated with the
amendment order.Ensure there is only one quote tied to the amendment order.The
order amendment isn’t associated with a quote.The connector couldn’t find a
corresponding quote associated with the amendment order.Make sure each amendment
order has a related quote.
## Quote errors

The table below contains the errors related to CPQ quotes and how to resolve
them.

ErrorDescriptionRecommendationThere’s no CPQ quote associated with the
Salesforce order. Orders pushed to Stripe must have a related CPQ quote.All
Salesforce orders need a corresponding CPQ quote. This error indicates that the
connector couldn’t find a corresponding quote.Regenerate the Salesforce order
from a Salesforce CPQ quote.Unable to find the initial Salesforce CPQ quote
associated with the order amendment.All Salesforce orders that the connector
syncs need an associated Salesforce CPQ quote.Regenerate the Salesforce order
from a Salesforce CPQ quote.You can’t specify the subscription term as a decimal
value.The subscription term represents the contract duration in number of
months. This value can’t be a decimal.Update the mapped subscription term with a
whole number.Billing frequency isn’t a supported `CPQ Billing Frequency`
option.CPQ supports Monthly, Quarterly, Semiannual, and Annual as values for the
`SBQQ__BillingFrequency__c` field.Update the `CPQ Billing Frequency` field value
to `Monthly`, `Quarterly`, `Semiannual`, or `Annual`.
## Price errors

The table below contains the errors related to prices and how to resolve them.

ErrorDescriptionRecommendationFound a corresponding Stripe price for the
Salesforce price, but the price data has changed.The Salesforce pricebook entry
that’s linked to the order item previously synced, and the corresponding Stripe
price data has changed.Clear the Stripe ID from the Salesforce pricebook entry
and sync the Salesforce order again. This results in a newly created Stripe
price for the pricebook entry.More than one consumption schedule is linked to a
pricebook, but there can only be one.The connector found more than one
consumption schedule linked to a pricebook, when there can only be one.Delete
one of the consumption schedules attached to the pricebook entry.The
subscription term can’t be a decimal value.The subscription term represents the
contract duration in number of months. This value can’t be a decimal.Update the
mapped subscription term to a whole number.A decimal value was provided for the
upper tier bound, but consumption rate tier bounds must be integers.The
connector found a decimal value for the upper tier bound of the Salesforce
consumption rate.Update the tier bound for the Salesforce consumption rate to an
integer.The pricing method on the consumption rate isn’t supported.The
`SBQQ__PricingMethod__c` field accepts a value of `PerUnit` or `FlatFee`.Update
the `SBQQ__PricingMethod__c` field value to either `PerUnit` or `FlatFee`.The
consumption schedule type isn’t supported.The `Consumption Schedule Type` field
accepts a value of `Range` or `Slab`.Update the `Consumption Schedule Type` to
either `Range` or `Slab`.The `unit_amount_decimal` field can’t be empty for
Stripe price objects.The connector found an empty value for the mapped
Salesforce value, and prices can’t be empty.Update the mapped Salesforce value
to a positive integer.Unexpected `billing_scheme` value on Stripe price.The
billing scheme isn’t set to a valid value.Update the billing scheme to either
`per_unit` or `tiered`.The pricing interval isn’t supported.The pricing interval
isn’t set to a valid value.Update the pricing interval to either `Month` or
`Year`.The retrieved Stripe price was empty.The corresponding Stripe price must
have a value.Remove the Stripe price ID from the corresponding Salesforce
record, and then retry syncing the failed order.Two tiers were found with an
infinite boundary on the same price.The connector found two Salesforce
`ConsumptionRate` objects associated with a single `ConsumptionSchedule`, both
with their upper bounds set to infinity.Update one of the `ConsumptionRate`
records to have a finite upper bound, breaking the infinite boundary
condition.The default currency isn’t specified on your account configuration.The
connector couldn’t find a default currency.Set the default currency for your
organization in Salesforce, and make sure the connector’s setting for `Billing
Currency` shows the correct currency.
## Product errors

The table below contains the errors related to Salesforce products and how to
resolve them.

ErrorDescriptionRecommendationProduct billing type isn’t a supported `CPQ
Product Billing Type` option.The product billing type (`SBQQ__BillingType__c`)
accepts a value of `Advance` or `Arrears`.Update the product’s
`SBQQ__BillingType__c` field to either `Advance` or `Arrears`.Adding Salesforce
products with a renewable type to evergreen orders isn’t supported.Salesforce
CPQ products accept a value of Renewable or Evergreen.The connector doesn’t
support both product types in a single Salesforce order. To sync the Salesforce
order, you must remove one of the order items.
## Termination errors

The table below contains the errors related to termination orders and how to
resolve them.

ErrorDescriptionRecommendationA termination order is processing, but more
amendments are queued.The connector is processing a termination order that
cancels the subscription schedule, but there are more amendment orders to
process.To terminate a Salesforce order, you must delete or deactivate any
amendment orders that are activated after the termination order. To amend a
Salesforce order before terminating it, you must delete or deactivate the
termination Salesforce order so the amendment order is processed, then sync the
termination Salesforce order.Termination quantity is greater than the aggregate
quantity for the order item.You’re attempting to reduce an order item’s quantity
by more than the existing quantity, resulting in a negative quantity.Update the
order item quantity to 0 or more.
## Stripe errors

The table below contains common Stripe errors and how to resolve them. The
connector displays all Stripe errors that occur directly to the user.

ErrorDescriptionRecommendationThe request rate limit was exceeded.Learn more
about [rate limits](https://docs.stripe.com/rate-limits).The connector
automatically retries syncing the order at a later time. You can also use the
Manual Sync function to force a manual sync of the failed order.
## Connector errors

The table below contains common connector errors. If you encounter any of these
issues, [contact Stripe support](https://support.stripe.com/) to investigate
further.

ErrorDescriptionRecommendationThe number of Quote or Quote Line Associations
differs from the Order or Item coupons.The connector failed to automatically
generate an Order coupon for a Quote or Quote Line coupon.Contact Stripe support
to resolve this issue and generate the coupons before syncing.The calculated
price multiplier differs from the CPQ price multiplier.The Order failed to sync
because the connector calculated a different price multiplier than CPQ.Confirm
that your Salesforce CPQ Proration Precision matches the settings in your
Salesforce CPQ app. If they don’t match, update them to match. If the settings
match, contact Stripe support to resolve this issue and investigate further.More
than one backend proration phase found.While syncing the Order, the connector
discovered the subscription schedule in an unexpected state that it didn’t know
how to handle.Contact Stripe support to resolve this issue and investigate
further.
## See also

- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Products and
prices](https://docs.stripe.com/connectors/salesforce-cpq/products-prices)
- [Order
amendments](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)

## Links

- [support](https://support.stripe.com/)
- [rate limits](https://docs.stripe.com/rate-limits)
- [Field defaults and custom
mappings](https://docs.stripe.com/connectors/salesforce-cpq/field-mappings)
- [Products and
prices](https://docs.stripe.com/connectors/salesforce-cpq/products-prices)
- [Order
amendments](https://docs.stripe.com/connectors/salesforce-cpq/subscription-order-amendments)
- [Subscription
orders](https://docs.stripe.com/connectors/salesforce-cpq/subscriptions)