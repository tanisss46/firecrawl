# Model usage-based pricing

## Learn about the different pricing models for usage-based billing on Stripe.

Common pricing models include fixed fee and overage, pay as you go, or credit
burndown. Use the guidance below to set up these pricing models in Stripe.

## Fixed fee and overage model

Use the fixed fee and overage model to charge a flat fee per month for your
service at the beginning of the period. The flat fee has some included usage
entitlement, and any additional usage (overage) charges at the end of the
period.

You can use the Stripe Dashboard or API to set this up with two prices within
the same product.

For example, Alpaca AI introduces an advanced model called Llama AI. Priced at
200 USD per month, this model includes 100,000 tokens. We charge any usage above
the included tokens at an additional rate of 0.001 USD per token.

DashboardAPI- On the [Product
catalog](https://dashboard.stripe.com/test/products) page, click **Create
product**.
- On the **Add a product** page, do the following:

- For **Name**, enter the name of your product. For the Alpaca AI example, enter
`Llama AI`.
- (Optional) For **Description**, add a description that appears at checkout in
the [customer portal](https://docs.stripe.com/customer-management) and in
[quotes](https://docs.stripe.com/quotes).
- Under **Billing period**, select **More pricing options**.
- On the **Add price** page, do the following:

- Under **Choose your pricing model**, select **Flat rate**.
- Under **Price**, set the **Amount** to `200.00 USD`.
- Click **Next**
- To add a second recurring price to the product, click **Add another price** on
the **Add a product** page.
- On the **Add price** page,do the following:

- Under **Choose your pricing model**, select **Usage-based**, **Per tier**, and
**Graduated**.
- Under **Price**, create two graduated pricing tiers:

First unitLast unitPer unitFlat feeFor the first0100,0000.00 USD0.00 USDFor the
next100,001∞0.001 USD0.00 USD
- Under **Meter**, create a new meter to record usage. For the Alpaca AI
example, use the meter name `llama_api_tokens`.
- Click **Next**.
- Click **Add product**. When you create subscriptions, specify both prices.

## Pay as you go

The pay as you go model (also called in arrears billing) lets you track usage
incurred over a determined period, then charge the customer at the end of the
period.

You can deploy any of the following pricing strategies:

- **Per unit**: Charge the same amount for each unit.
- **Per package**: Charge an amount for a package or bundle of units or usage.
- **Tiered and volume-based pricing**: With [volume
pricing](https://docs.stripe.com/products-prices/pricing-models#volume-based-pricing),
you charge the subscription item at the tier that corresponds to the usage
amount at the end of the period.
- **Tiered and graduated pricing**: Similar to volume pricing, [graduated
pricing](https://docs.stripe.com/products-prices/pricing-models#graduated-pricing)
charges for the usage in each tier instead of applying a single price to all
usage.

This model might cause customers to accumulate significant usage, and affect
their payment method status at the end of the month.

## Credit burndown

The credit burndown model lets you collect prepayment for usage-based products
and services. Customers can use [billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
to pay an initial amount, and then apply their billing credits as they use the
product.

For example, Alpaca AI wants to sell a large enterprise contract to an existing
self-serve customer for their new Llama AI Model. The customer commits to pay
100,000 USD up front for Llama AI, so they can get 120,000 USD of billing credit
usage to use within 1 year.

DashboardAPI
### Collect prepayment from a customer

- On the [Invoices](https://dashboard.stripe.com/invoices) page, click **Create
invoice**.
- Select your customer from the **Customer** dropdown.
- Select **USD - US Dollar** from the **Currency** dropdown.
- Under **Items**, select **Add a new line item**.
- Under **Item details**, do the following:- For **Item**, enter `Llama AI
Credits`.
- For **Price**, enter `100,000`.
- Click **Save**.
- Click **Send invoice**.

After your customer pays the invoice, you can grant them billing credits.

### Grant billing credits to a customer

- On the [Customers](https://dashboard.stripe.com/test/customers) page, select
the customer name.
- On the customer page, under **Credit grants**, click the plus (**+**) symbol.
- On the **New credit grant** page, do the following:- For **Name**, enter a
name for your credit grant.
- For **Amount**, specify the amount of the credit grant. For the Alpaca AI
example, enter `120,000`.
- Under **Expiry date**, specify the date, if any, when the credits expire. For
the Alpaca AI example, select **Specific date** and set a date 12 months from
now.
- Click **Create grant**.

## Free trials

You can use [trial periods for
subscriptions](https://docs.stripe.com/billing/subscriptions/trials) with
usage-based billing. During the trial period, any usage accrued doesn’t count
toward the total charged to the customer at the end of the billing cycle. After
the trial period ends, the usage accrues and bills at the end of the next
billing cycle.

Make sure your integration properly monitors and handles [webhook
events](https://docs.stripe.com/billing/subscriptions/webhooks) related to trial
status changes.

A few days before a trial ends and the subscription moves from `trialing` to
`active`, you receive a `customer.subscription.trial_will_end` event. When you
receive this event, make sure you have a payment method on the customer account
to bill them. Optionally, provide advance notification to the customer about the
upcoming charge.

StatusDescription`trialing`The subscription is currently in a trial period and
you can safely provision your product for your customer. The subscription
transitions automatically to `active` when a customer makes the first
payment.`active`The subscription is in good standing. For `past_due`
subscriptions, paying the latest associated invoice or marking it uncollectible
transitions the subscription to `active`. Note that `active` doesn’t indicate
that all outstanding invoices associated with the subscription have been paid.
You can leave other outstanding invoices open for payment, mark them as
uncollectible, or void them as you see fit.`incomplete`The customer must make a
successful payment within 23 hours to activate the subscription. Or the payment
[requires
action](https://docs.stripe.com/billing/subscriptions/usage-based/pricing-models#requires-action),
such as customer authentication. Subscriptions can also be `incomplete` if
there’s a pending payment and the PaymentIntent status is
`processing`.`incomplete_expired`The initial payment on the subscription failed
and the customer didn’t make a successful payment within 23 hours of
subscription creation. These subscriptions don’t bill customers. This status
exists so you can track customers that failed to activate their
subscriptions.`past_due`Payment on the latest finalized invoice either failed or
wasn’t attempted. The subscription continues to create invoices. Your
[subscription
settings](https://docs.stripe.com/billing/subscriptions/overview#settings)
determine the subscription’s next state. If the invoice is still unpaid after
all attempted [smart
retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries), you
can configure the subscription to move to `canceled`, `unpaid`, or leave it as
`past_due`. To move the subscription to `active`, pay the most recent invoice
before its due date.`canceled`The subscription was canceled. During
cancellation, automatic collection for all unpaid invoices is disabled
(`auto_advance=false`). This is a terminal state that can’t be
updated.`unpaid`The latest invoice hasn’t been paid but the subscription remains
in place. The latest invoice remains open and invoices continue to generate, but
payments aren’t attempted. Revoke access to your product when the subscription
is `unpaid` because payments were already attempted and retried while
`past_due`. To move the subscription to `active`, pay the most recent invoice
before its due date.`paused`The subscription has ended its trial period without
a default payment method and the
[trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment)
is set to `pause`. Invoices are no longer created for the subscription. After
attaching a default payment method to the customer, you can [resume the
subscription](https://docs.stripe.com/billing/subscriptions/trials#resume-a-paused-subscription).
Learn more about [subscriptions and
webhooks](https://docs.stripe.com/billing/subscriptions/webhooks).

## Transform quantities

You can use the
[transform_quantity](https://docs.stripe.com/api/prices/create#create_price-transform_quantity)
option to transform usage before applying the price, which you can use when you
want pricing on packages of a product instead of individual units. This allows
you to divide the reported usage by a specific number and round the result up or
down.

#### Note

Quantity transformation isn’t compatible with [tiered
pricing](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#tiered-pricing-threshold).

For example, say you have a car rental service and you want to charge customers
for each hour they rent a car. You report usage as a number of minutes.

```
curl https://api.stripe.com/v1/products \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d name="Car Rental Service"
```

Create a price for the car rental service product. Charge 10 USD per hour, and
round up to charge for a full hour, even if the customer uses only part of the
hour.

```
curl https://api.stripe.com/v1/prices \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d nickname="Car Rental Per Hour Rate" \
 -d unit_amount=1000 \
 -d currency=usd \
 -d "recurring[interval]"=month \
 -d "recurring[usage_type]"=metered \
 -d product={{CAR_RENTAL_SERVICE_PRODUCT_ID}} \
 -d "transform_quantity[divide_by]"=60 \
 -d "transform_quantity[round]"=up
```

If a customer rents the car for 150 minutes, that customer is charged 30 USD for
3 hours of rental (2 hours and 30 minutes, rounded up).

## Links

- [Product catalog](https://dashboard.stripe.com/test/products)
- [customer portal](https://docs.stripe.com/customer-management)
- [quotes](https://docs.stripe.com/quotes)
- [volume
pricing](https://docs.stripe.com/products-prices/pricing-models#volume-based-pricing)
- [graduated
pricing](https://docs.stripe.com/products-prices/pricing-models#graduated-pricing)
- [billing
credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
- [Invoices](https://dashboard.stripe.com/invoices)
- [Customers](https://dashboard.stripe.com/test/customers)
- [trial periods for
subscriptions](https://docs.stripe.com/billing/subscriptions/trials)
- [webhook events](https://docs.stripe.com/billing/subscriptions/webhooks)
- [subscription
settings](https://docs.stripe.com/billing/subscriptions/overview#settings)
- [smart
retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries)
-
[trial_settings.end_behavior.missing_payment_method](https://docs.stripe.com/billing/subscriptions/trials#create-free-trials-without-payment)
- [resume the
subscription](https://docs.stripe.com/billing/subscriptions/trials#resume-a-paused-subscription)
-
[transform_quantity](https://docs.stripe.com/api/prices/create#create_price-transform_quantity)
- [tiered
pricing](https://docs.stripe.com/billing/subscriptions/usage-based/alerts-and-thresholds#tiered-pricing-threshold)