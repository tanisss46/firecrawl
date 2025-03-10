# Flexible coupons and promotion codes

## Add discounts to subscriptions and subscription items using coupons and promotion codes.

Redeem coupons to apply discounts to the subscriptions you offer. You can also
use coupons to create promotion codes to share with your customers. Customers
can redeem these promotion codes to apply discounts to their subscriptions.

You can use coupons and promotion codes to:

- Apply one or more discounts to every
[invoice](https://docs.stripe.com/api/invoices), a specific invoice, or for a
certain duration of time
- Apply one or more discounts to every subscription a customer has or to
specific subscriptions
- Apply one or more discounts to specific subscription items
- Reduce invoice amounts by a percentage or a flat amount

You can also define a coupon that a customer must redeem by a certain date, or
that’s limited to a set number of redemptions across all of your customers.

To use discounts for one-time payments, see [Add discounts for one-time
payments](https://docs.stripe.com/payments/checkout/discounts).

## Coupons

To apply discounts to a customer or a customer’s charges, redeem coupons into
discounts. Learn how to create and manage coupons in the following sections.

### Create a coupon

Create coupons in the Dashboard or with the
[API](https://docs.stripe.com/api/coupons/create):

DashboardAPI- In the Dashboard, open the
[Products](https://dashboard.stripe.com/test/products?active=true) page.
- Click **Coupons**.
- Click **+New**.
- In the **Create a coupon** dialog, enter the coupon’s parameters.
- Click **Create coupon**.

Here are all the settings for coupons.

SettingDescriptionNameThe name of the coupon that appears on receipts and
invoices.ID optionalA unique identifier for the coupon in the API. If you leave
this field blank, Stripe generates an ID for you.TypeDetermines whether a coupon
discounts a subscription by a fixed amount or by a percentage.
**Percentage off** or **Discount amount**

Indicates how much the coupon actually discounts.

If you sell in multiple currencies, a single coupon can define different
discount amounts for different currencies. Multi-currency coupons follow the
same rules as [multi-currency
prices](https://docs.stripe.com/products-prices/pricing-models#multicurrency).

Apply to specific products optionalLimits the type of items that the coupon can
apply to.DurationIndicates how long the coupon is valid for.Redemption limits
optionalAllows you to limit when a customer can redeem the coupon and the number
of times a coupon can be redeemed.Codes optionalAllows you to create [promotion
codes](https://docs.stripe.com/billing/subscriptions/coupons#promotion-codes--promotion-codes)
for the coupon.
You can only edit the name of the coupon after creation.

### Set eligible products

DashboardAPI
To set the products that are eligible for discounts, add the relevant product in
the **Apply to specific product** field. Any promotion codes that are associated
with the coupon are also restricted to this list of eligible products.

If you configure a coupon to apply to specific products and a subscription
doesn’t have any applicable products, no discount is applied when you add the
coupon to the subscription.

When you [make changes](https://docs.stripe.com/billing/subscriptions/change) to
a subscription, any existing discounts are applied when proration is calculated.
You can’t discount proration line items further on the invoice that’s generated.

### Apply coupons to subscriptions

After you’ve created coupons, create a discount by applying them to a
subscription. You can apply the coupon when you create the subscription or by
[updating a customer’s existing
subscription](https://docs.stripe.com/api#update_subscription).

DashboardAPI- In the Dashboard, open the **Billing** page and click
**Subscriptions**.
- Click the relevant subscription.
- Click **Actions**.
- Click **Update subscription**.
- Click **Add coupon**.
- Select one or more coupons from the dropdown menus and click **Submit**.

You can still create a subscription when a customer doesn’t have a stored
payment method if no immediate payment is required after you apply coupons to
it.

### Apply coupons to customers

If you add a coupon to a customer, the coupon applies to all subscriptions for
that customer, including subscriptions added later. To prevent discounting all
recurring charges for a customer, add coupons to subscriptions instead of
customers.

A coupon attached to a subscription takes priority over a coupon attached to a
customer. If you add coupons to a subscription, any coupons attached to the
customer are not automatically applied. You must add the customer coupons to the
subscription if you want those to apply as well.

DashboardAPI- In the Dashboard, open the
[Customers](https://dashboard.stripe.com/test/customers) page and select the
customer.
- Click **Actions**
- Click **Apply coupon**.
- Select a coupon from the dropdown menu and click **Submit**.

### Apply coupons to Checkout

Apply coupons to subscriptions in a Checkout Session by setting the `discounts`
parameter in the
[API](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-discounts).
To create a session with an applied discount, pass the coupon ID in the `coupon`
parameter of the `discounts` array. This coupon overrides any coupon on the
customer.

If you’re creating a subscription with an existing customer, any coupon
associated with the customer is applied to the subscription’s invoices.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -d "payment_method_types[]"=card \
 -d "line_items[][price]"={{PRICE_ID}} \
 -d "line_items[][quantity]"=1 \
 -d mode=subscription \
 -d "discounts[][coupon]"="{{COUPON_ID}}" \
 -d success_url="https://example.com/success" \
 -d cancel_url="https://example.com/cancel"
```

### Delete coupons

You can delete coupons with the Dashboard or the
[API](https://docs.stripe.com/api/coupons/delete).

Deleting a coupon prevents it from being applied to future subscriptions or
customers, but it doesn’t remove the discount from any subscription or customer
that already has it.

DashboardAPI- In the Dashboard, open the
[Products](https://dashboard.stripe.com/test/products?active=true) page.
- Click **Coupons**
- Click the relevant coupon.
- Click the overflow menu ().
- Click **Delete coupon**.

### Coupon duration

A coupon’s duration indicates how long the redeemed
[discount](https://docs.stripe.com/api/#discounts) is valid for. For example, a
coupon for 50% off with a duration of 4 months applies to all invoices in the 4
month period starting when the coupon is first applied. If a customer applies
this coupon to a yearly subscription during the coupon’s 4 month period, the 50%
discount applies to the entire yearly subscription. In a monthly subscription,
the coupon applies to the first 4 months. For a weekly subscription, a 4 month
coupon applies to every invoice in the first 4 months.

If you’re configuring a coupon’s duration in the API, when you use the value
`repeating` you must specify `duration_in_months` as the number of months that
the coupon repeatedly applies to. If you set the duration to `once`, the coupon
applies only to the first invoice. If you set the duration to `forever`, the
coupon applies to all invoices indefinitely.

### Redemption limits

Redemption limits apply to the coupon across every customer. For example, if you
limit the number of times a coupon can be redeemed to 50, you can apply it to
your customers only 50 times. This can be one time each for 50 different
customers, one customer 50 times, or multiple customers multiple times until the
max of 50 times.

If you set a coupon to last forever when a customer uses it but the coupon has
an expiration date, any customer given that coupon will have that coupon’s
discount forever. No new customers can apply the coupon after the expiration
date.

## Promotion codes

Promotion codes are customer-facing codes that you create for coupons. For
example, FALLPROMO and SPRINGPROMO can both point to a single 25% off coupon.
You can share promotion codes directly with your customers to use at checkout.

If you’ve implemented the [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal) and
turned on promotion codes, customers can apply a discount when upgrading or
downgrading their existing subscriptions in the portal.

Customize controls and limits on promotion codes by specifying eligible
customers, first time orders, minimum order values, expiration dates, and
redemption limits.

### Restrictions

There are some restrictions to promotion codes.

- You can’t apply a promotion code with amount restrictions on:- [Customer
objects](https://docs.stripe.com/api/customers/object)
- [Subscription Item
objects](https://docs.stripe.com/api/subscription_items/object)
- [Invoice Item objects](https://docs.stripe.com/api/subscription_items/object)
- [Subscriptions objects](https://docs.stripe.com/api/subscriptions/object) when
you make an update
- Future phases on [Subscription Schedule
objects](https://docs.stripe.com/api/subscription_schedules/object)

### Create promotion codes

DashboardAPI
You can create a promotion code in the Dashboard when you [create a
coupon](https://docs.stripe.com/billing/subscriptions/coupons#create-coupons--create-coupons).

The **Code** is case-insensitive and unique across active promotion codes for
any customer. For example:

- You can create multiple customer-restricted promotion codes with the same
**Code**, but you can’t reuse that **Code** for a promotion code that any
customer can redeem.
- If you create a promotion code that is redeemable by any customer, you can’t
create another active promotion code with the same **code**.
- You can create a promotion code with one **Code**,
[inactivate](https://docs.stripe.com/billing/subscriptions/coupons#inactive-promotions--inactivate)
it, and then create a new promotion code with the same **Code**.
- In the Dashboard on the [Create a
coupon](https://dashboard.stripe.com/test/coupons/create) page, click the **Use
customer-facing coupon codes** button.
- Enter a code. This is the code that a customer enters at checkout to redeem
the discount. If you don’t set a code, Stripe generates one for you.
- Select requirements for the promotion code. For example, you can restrict the
coupon to only being valid on first-time orders.

When you create a promotion code, it inherits the configuration of the
associated coupon.

### Promotion code configurations

By configuring the promotion code settings, you can customize the following:

- Which customers are eligible to use a promotion code
- How many times a customer can redeem a promotion code
- When a promotion code expires
- Set a minimum amount a promotion code can apply to

### Limit by customer

DashboardAPI
To limit a promotion code to a particular customer complete these steps:

- On the [Create a coupon](https://dashboard.stripe.com/test/coupons/create)
page, select **Limit to a specific customer**.
- Select the relevant customer. If you don’t specify a customer, any customer
can redeem the promotion code.

### Limit by first time order

DashboardAPI
To limit a promotion code to a customer’s first order, on the [Create a
coupon](https://dashboard.stripe.com/test/coupons/create) page, select
**Eligible for first-time order only**.

### Set a minimum amount

DashboardAPI
To set an minimum amount that is eligible for a promotion code, on the [Create a
coupon](https://dashboard.stripe.com/test/coupons/create) page, select **Require
minimum order value** and enter the minimum value.

Because promotion code restrictions are checked at redemption time, the minimum
transaction amount only applies to the initial payment for a subscription.

If the coupon supports multiple currencies, the minimum amount can be different
per-currency.

### Customize expirations

DashboardAPI
To set an expiration date for a promotion code, on the [Create a
coupon](https://dashboard.stripe.com/test/coupons/create) page, select **Add an
expiration date** and the date and time at which the promotion code expires.

If the underlying coupon already has an expiration date set, then the promotion
code’s expiration date can’t be later than the coupon’s.

For example, you might have plans to support a coupon for a year, but you only
want it to be redeemable for one week after a customer receives it. To do this,
set the coupon’s expiration date to one year from now, and set each the
promotion code’s expiration date to one week after it is created.

### Limit redemptions

DashboardAPI
To set the number of times a customer can redeem the promotion code, on the
[Create a coupon](https://dashboard.stripe.com/test/coupons/create) page, select
**Limit the number of times this code can be redeemed** and enter the number.

If the underlying coupon already has a maximum number of times set, then the
promotion code’s maximum redemptions can’t be greater than the coupon’s.

### Deactivate promotion codes

DashboardAPI
To deactivate a promotion code, doing the following steps:

- In the Dashboard, open the
[Products](https://dashboard.stripe.com/test/products?active=true) page.
- Click **Coupons**.
- Click the coupon whose promotion code you want to deactivate.
- In the relevant promotion code row, click the overflow menu ().
- Click **Archive promotion code**.

However, if the underlying coupon for a promotion code becomes invalid, all of
its promotion codes become permanently inactive. Similarly, if a promotion code
reaches its maximum redemption limit or its expiration date, it becomes
permanently inactive. These promotion codes can’t be reactivated.

### Apply promotion codes to subscriptions

After you create a promotion code, redeem a discount by applying the promotion
code to a subscription. You can apply promotion codes two ways:

- When you [create a
subscription](https://docs.stripe.com/api#create_subscription)
- When you [update a customer’s existing
subscription](https://docs.stripe.com/api#update_subscription)
DashboardAPI- In the Dashboard, go to **Billing** > **Subscriptions**.
- Click the relevant subscription.
- Click **Actions** > **Update subscription** > **Add coupon**.
- Click a promotion code from the dropdown menu and click **Submit**.

### Add promotion codes to Checkout

Enable promotion codes with the API by setting the
[allow_promotion_codes](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-allow_promotion_codes)
parameter in Checkout Sessions. When `allow_promotion_codes` is enabled on a
Checkout Session, Checkout includes a promotion code redemption box for your
customers to use.

![Promotion code field at
checkout](https://b.stripecdn.com/docs-statics-srv/assets/promo_code_checkout.c07ef6d4f0b1b3f9a8a7e4bbba83d56f.png)

Promotion code field at checkout

## Stackable coupons and promotion codes

You can add multiple coupons, promotion codes, or redeemed
[discounts](https://docs.stripe.com/api/#discounts) to a customer’s list of
charges. You can do this when [creating a
subscription](https://docs.stripe.com/api#create_subscription) or by [updating a
customer’s existing
subscription](https://docs.stripe.com/api#update_subscription).

We support multiple discounts on both subscriptions and subscription items.

When you create a subscription with stackable discounts, each discount applies
in order to all items on the subscription. The order of the discounts is
important if you use both `amount_off` and `percent_off`. For example, the
following stacked discounts apply differently:

- 20% off *then* $5 off
- $5 off *then* 20% off
DashboardAPI- In the Dashboard, go to **Billing** > **Subscriptions**.
- Click the relevant subscription.
- Click **Actions** > **Update subscription** > **Add coupon**.
- Click coupons from the dropdown menus and click **Submit**.
- Click the relevant product.
- Click **Add coupons**.
- Click coupons from the dropdown menus and click **Submit**.

#### Note

You can start using the new `discounts` parameter on any subscription. We
automatically clear out the singular `discount` field when `discounts` with more
than one entry is passed in an update.

### Restrictions

There are some restrictions to using multiple discounts.

- You can set up to 20 entries in the `discounts` parameter.
- Each entry in `discounts` has to be unique.
- You can not pass in a coupon and a promotion code created from the same
coupon.
- You can not pass in a coupon and a discount that is generated from the same
coupon.
- Redeemed discounts must already be attached to the customer or subscription
that you’re updating.

### Update a subscription

You don’t need to set `discounts` if you don’t intend to make changes to
existing discounts.

When updating `discounts`, you need to pass in any previously set `coupon`,
`promotion_code` or `discount` you want to keep on the subscription.

Pass `discounts = ""` to clear all discounts from the subscription. When a
subscription has no discounts, the customer-level discount, if any, applies to
invoices.

If you have already set more than one discount on a subscription with the new
`discounts` parameter, you can not update the subscription with the deprecated
`coupon` or `promotion_code` parameter. Similarly, you can not update a
schedule’s phases with the deprecated `coupon` or `promotion_code` parameter if
you have set more than one discount on a prior phase.

Updating `discounts` does not incur prorations or generate an invoice on its
own. The new discounts are applied the next time the subscription creates an
invoice.

## Alternative discount methods

Although coupons are the most common way to discount a subscription, you can
also do the following:

- Add a negative [customer
balance](https://docs.stripe.com/api#customer_object-balance) to the customer.
- Add negative [invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items).
- Add a [second
price](https://docs.stripe.com/products-prices/manage-prices#create-price) that
is a cheaper version of a product’s usual price.

Of these methods, negative invoice items provide more detailed information as to
what discount was created, when, and why.

## See also

- [Changing subscriptions](https://docs.stripe.com/billing/subscriptions/change)
- [Working with invoices](https://docs.stripe.com/billing/invoices/subscription)
- [Coupons API](https://docs.stripe.com/api#coupons)
- [Promotion codes API](https://docs.stripe.com/api#promotion_codes)

## Links

- [invoice](https://docs.stripe.com/api/invoices)
- [Add discounts for one-time
payments](https://docs.stripe.com/payments/checkout/discounts)
- [API](https://docs.stripe.com/api/coupons/create)
- [Products](https://dashboard.stripe.com/test/products?active=true)
- [multi-currency
prices](https://docs.stripe.com/products-prices/pricing-models#multicurrency)
- [make changes](https://docs.stripe.com/billing/subscriptions/change)
- [updating a customer’s existing
subscription](https://docs.stripe.com/api#update_subscription)
- [Customers](https://dashboard.stripe.com/test/customers)
-
[API](https://docs.stripe.com/api/checkout/sessions/create#create_checkout_session-discounts)
- [API](https://docs.stripe.com/api/coupons/delete)
- [discount](https://docs.stripe.com/api/#discounts)
- [customer
portal](https://docs.stripe.com/billing/subscriptions/customer-portal)
- [Customer objects](https://docs.stripe.com/api/customers/object)
- [Subscription Item
objects](https://docs.stripe.com/api/subscription_items/object)
- [Subscriptions objects](https://docs.stripe.com/api/subscriptions/object)
- [Subscription Schedule
objects](https://docs.stripe.com/api/subscription_schedules/object)
- [Create a coupon](https://dashboard.stripe.com/test/coupons/create)
- [create a subscription](https://docs.stripe.com/api#create_subscription)
-
[allow_promotion_codes](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-allow_promotion_codes)
- [customer balance](https://docs.stripe.com/api#customer_object-balance)
- [invoice
items](https://docs.stripe.com/billing/invoices/subscription#adding-draft-invoice-items)
- [second
price](https://docs.stripe.com/products-prices/manage-prices#create-price)
- [Working with invoices](https://docs.stripe.com/billing/invoices/subscription)
- [Coupons API](https://docs.stripe.com/api#coupons)
- [Promotion codes API](https://docs.stripe.com/api#promotion_codes)