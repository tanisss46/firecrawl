# Automatically collect tax on Payment Links

## Learn how to calculate and collect tax on a payment page without writing any code.

You can use Stripe Tax with [Payment
Links](https://stripe.com/payments/payment-links) to automatically calculate and
collect tax on a payment page and share a link to it with your customers,
without writing any code.

[Activate Stripe Tax](https://docs.stripe.com/tax/payment-links#activate)
[Log in](https://dashboard.stripe.com/settings/tax) or [sign
up](https://dashboard.stripe.com/register) for Stripe to activate Stripe Tax.

[Update your products and prices
(optional)](https://docs.stripe.com/tax/payment-links#product-and-price-setup)
Stripe Tax uses information stored on
[products](https://docs.stripe.com/api/products) and
[prices](https://docs.stripe.com/api/prices) to calculate tax, such as [tax
code](https://docs.stripe.com/api/products/object#product_object-tax_code) and
[tax
behavior](https://docs.stripe.com/api/prices/object#price_object-tax_behavior).
If you don’t explicitly specify these configurations, Stripe Tax will use the
default tax code selected in [Tax
Settings](https://dashboard.stripe.com/settings/tax).

For more information, see [Specify product tax codes and tax
behaviour](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior).

[Create a
link](https://docs.stripe.com/tax/payment-links#create-link)DashboardAPI
To [create a payment link](https://docs.stripe.com/payment-links/create) in the
Dashboard:

- Open the [Payment Links](https://dashboard.stripe.com/payment-links) page.
- Click **+ New**.
- Fill out the details.
- Make sure that **Collect tax automatically** under options is on.

To update an existing payment link in the Dashboard:

- Open the [Payment Links](https://dashboard.stripe.com/payment-links) page.
- Select the payment link you want to update.
- On the payment link details page, click the overflow menu (), then click
**Edit**.
- In the payment link editor, select **Collect tax automatically** to enable
automatic tax collection on this payment link.
- (Optional) Select **Collect customers’ addresses** to help with more accurate
tax calculation. The more information you can provide, the more precise the
calculation.
- Click **Update link** to save your changes.

## See also

- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)

## Links

- [Payment Links](https://stripe.com/payments/payment-links)
- [Log in](https://dashboard.stripe.com/settings/tax)
- [sign up](https://dashboard.stripe.com/register)
- [products](https://docs.stripe.com/api/products)
- [prices](https://docs.stripe.com/api/prices)
- [tax
code](https://docs.stripe.com/api/products/object#product_object-tax_code)
- [tax
behavior](https://docs.stripe.com/api/prices/object#price_object-tax_behavior)
- [Specify product tax codes and tax
behaviour](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
- [create a payment link](https://docs.stripe.com/payment-links/create)
- [Payment Links](https://dashboard.stripe.com/payment-links)
- [Use Stripe Tax with Connect](https://docs.stripe.com/tax/connect)