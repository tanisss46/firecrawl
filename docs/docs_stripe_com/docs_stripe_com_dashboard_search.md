# Perform searches in the Dashboard

## Use the Dashboard to search for payments, customers, and more.

Use the Dashboard’s built-in search feature to find important resources and
navigate across different Stripe resources, like [connected
accounts](https://docs.stripe.com/connect),
[Coupons](https://docs.stripe.com/api/coupons),
[Customers](https://docs.stripe.com/api/customers),
[Invoices](https://docs.stripe.com/api/invoices) (and [Invoice
Items](https://docs.stripe.com/api/invoiceitems)),
[Payouts](https://docs.stripe.com/payouts), and
[Products](https://docs.stripe.com/api/products). When you perform a search, the
top results appear immediately. View all of the matches by clicking **Show all
results for** or pressing **Enter**. From the resulting groups of search
results, click **View all** to see an expanded display with column headings,
some of which provide sorting options.

![Dashboard's search suggested
filters](https://b.stripecdn.com/docs-statics-srv/assets/dashboard-search.bc1d683e4a7eca1a760873ab03b03aae.png)

Use suggested filters when searching

## Get started

Use different pieces of information as search terms:

- The last four digits of a card (**4242**).
- The payment method type (**iDEAL**).
- The business name of a connected Stripe account (**Rocketship**).
- The email receipt number (**1817-9523**).

For searches that require dates, you can use different formats, like **08/22**,
**2020-07-12**, or **last week**. Use object identifiers (dispute ID) to take
you directly to the object you’re looking for. No additional context is
necessary for most searches. The Dashboard automatically looks for the most
relevant information based on your search query. You can make use of search
filters and operators for more granular control.

## Search filters and operators

By default, the Dashboard looks for values that match your search term in the
most logical fields within objects. (For example, it’ll look for an email
address in the `email` field or an object description.) You can use filters and
operators to further refine your searches. The more terms you provide in your
search query, the fewer the number of results.

FiltersOperators
Use filters to limit your search terms so that they only apply to specific
fields within applicable objects. Preface a search term with one of these
filters. If your search term must include a space, wrap it in quotation marks
(`name:"John Doe"`). Many fields are shared across different objects. For
instance, the `amount` field applies to payments, invoices, payouts, and so on.

FilterDescriptionExample`amount:`The amount of an object. For decimal
currencies, use a decimal point for both currency units (for example, dollars
and cents).amount:149.99`brand:`The brand of card associated with an
object.brand:visa`country:`The two-letter [ISO
code](https://en.wikipedia.org/wiki/ISO_3166-1) representing the country
associated with an object.country:GB`created:`The date an object was created
(identical to `date`).created:2020/07/12`currency:`The three-letter [ISO
code](https://en.wikipedia.org/wiki/ISO_4217) representing the currency of an
object.currency:EUR`date:`The date an object was created (identical to
`created`).date:yesterday`email:`The email (either full address or part of one)
of an object.email:jenny.rosen@example.com`exp:`The expiration date of the card
associated with an object.exp:08/22`flow:`The type of [flow for customer
action](https://docs.stripe.com/sources#flow-for-customer-action) that applies
to a [Sources](https://docs.stripe.com/sources) payment.flow:redirect`last4:`The
last four digits of the card associated with an
object.last4:4080`metadata:`[Metadata](https://docs.stripe.com/api#metadata)
value on a supported object. Additional [search
options](https://docs.stripe.com/dashboard/search#metadata-searches) for
metadata are also available.metadata:555-5555`name:`The cardholder or customer
name associated with an object.name:jenny`number:`The unique number identifying
an invoice.number:06b2b1a642-0023`postal:`The ZIP or postal code associated with
an object.postal:12345`receipt:`The receipt number used in a payment or refund
email receipt.receipt:3330-2392`risk_level:`The [risk
level](https://docs.stripe.com/radar/risk-evaluation) of a payment determined by
[Radar](https://docs.stripe.com/radar).risk_level:elevated`status:`The status of
an object.status:canceled`type:`The type of
[PaymentMethod](https://docs.stripe.com/payments/payment-methods) or
[Source](https://docs.stripe.com/sources) used to create a
payment.type:ideal`usage:`The
[usage](https://docs.stripe.com/sources#single-use-or-reusable) availability of
a [Sources](https://docs.stripe.com/sources) payment
method.usage:single_use`zip:`The ZIP or postal code associated with an
object.zip:12345
### Combine and negate search terms

Use more than one search term to narrow down your search and reduce the number
of results. You can also negate any search filter with a hyphen (`-`) so that
matches for it aren’t included.

ExampleDescription`last4:4242 exp:08/22`The last four digits of the card are
`4242` and expiration date is `08/22`.`last4:4242 -exp:08/22`The last four
digits of the card are `4242` and expiration date is not `08/22`.`type:ideal
status:canceled`iDEAL payments where the source has been canceled and not used
to complete a payment.
To search for an entire phrase, use quotation marks. For example, **“Stripe
Shop”** provides matches for that full phrase, but **Stripe Shop** searches the
words **Stripe** and **Shop** separately.

### Metadata searches

You can search for [metadata](https://docs.stripe.com/api#metadata) that you
added to objects that support it. For example, you can find documents that have
metadata key `order_id` with corresponding metadata value `xyn712` using any of
the following search queries:

- `xyn712`
- `order_id:xyn712`
- `metadata:xyn712`
- `metadata:order_id=xyn712`

## Search across accounts in an organization

After you add multiple Stripe accounts to an
[organization](https://docs.stripe.com/get-started/account/orgs), users can
search across all accounts they have access to within that organization.

By default, searches display results from all accounts you have access to in the
organization. To narrow your search to within your current account, select the
account dropdown to the right of the search bar in the Dashboard.

![Search across the organization or current
account.](https://b.stripecdn.com/docs-statics-srv/assets/org-search.ad9ff17e4e187a926dd0d12f0dcecda9.png)

Search across the organization by default or narrow your searches to your
current account.

When you search within an organization, both the dropdown search results and the
full results page display the associated account for each result.

![Organization-wide search
results](https://b.stripecdn.com/docs-statics-srv/assets/org-search-results-dropdown.f05bff944bdf38d6ed06e4a4d2e7953a.png)

Search results in the dropdown display the associated account for each result.

## Best practices

Many searches can be performed with a single search term. Use something that
would be fairly specific, such as a name or email address. If you’re seeing too
few results, make the search term less specific. If there are too many results,
include additional terms, one at a time.

Use a wider range of values when using dates or amounts as search terms.
Currency conversions and time zone differences between you and your customer are
a common source of confusion when looking up information about a payment. In
these cases, additional search terms or even different ones altogether can help.

#### Bookmark searches

As search terms are included in the URL, you can bookmark the search or share it
with other team members as you would any other web page.

## Links

- [connected accounts](https://docs.stripe.com/connect)
- [Coupons](https://docs.stripe.com/api/coupons)
- [Customers](https://docs.stripe.com/api/customers)
- [Invoices](https://docs.stripe.com/api/invoices)
- [Invoice Items](https://docs.stripe.com/api/invoiceitems)
- [Payouts](https://docs.stripe.com/payouts)
- [Products](https://docs.stripe.com/api/products)
- [Stripe Sigma](https://docs.stripe.com/stripe-data)
- [ISO code](https://en.wikipedia.org/wiki/ISO_3166-1)
- [ISO code](https://en.wikipedia.org/wiki/ISO_4217)
- [flow for customer
action](https://docs.stripe.com/sources#flow-for-customer-action)
- [Sources](https://docs.stripe.com/sources)
- [Metadata](https://docs.stripe.com/api#metadata)
- [risk level](https://docs.stripe.com/radar/risk-evaluation)
- [Radar](https://docs.stripe.com/radar)
- [PaymentMethod](https://docs.stripe.com/payments/payment-methods)
- [usage](https://docs.stripe.com/sources#single-use-or-reusable)
- [organization](https://docs.stripe.com/get-started/account/orgs)