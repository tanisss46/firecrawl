# Set up Stripe Tax

## Enable Stripe Tax to automatically calculate and collect tax.

To set up Stripe Tax, configure your tax settings through the Dashboard on the
[tax settings page](https://dashboard.stripe.com/settings/tax). Alternatively,
you can use the [Tax Settings API](https://docs.stripe.com/api/tax/settings).
Depending on your integration, add [one line of
code](https://docs.stripe.com/tax/set-up#integrate) to enable tax.

If you’re a platform that wants to set up Stripe Tax for your connected accounts
that are responsible for collecting, filing, and reporting taxes, see [Tax for
software platforms](https://docs.stripe.com/tax/tax-for-platforms).

#### Note

[Log in](https://dashboard.stripe.com/settings/tax) or [sign
up](https://dashboard.stripe.com/register) for Stripe to enable Stripe Tax.

## Get started with a video demo

This short video shows you how to enable automatic tax collection through the
Dashboard.

[Set your origin address](https://docs.stripe.com/tax/set-up#origin-address)
Origin address is where your business is located or, if you sell physical goods,
the address where you’re shipping goods from.

By default, we set your origin address to your Stripe business address so you
only need to review and confirm that your details are correct on the [tax
settings page](https://dashboard.stripe.com/settings/tax). Alternatively, you
can [retrieve](https://docs.stripe.com/api/tax/settings/retrieve) and
[update](https://docs.stripe.com/api/tax/settings/update) your origin address
using the API.

[Select your preset tax
code](https://docs.stripe.com/tax/set-up#preset-tax-code)
A tax code is a classification of your product or service for Stripe Tax. We use
this to make sure that the correct tax rate is applied to your transactions.

- **Preset product tax code:** The preset product tax code is the default tax
code that applies to your
[Products](https://docs.stripe.com/api/products/object) when you don’t
explicitly specify a
[tax_code](https://docs.stripe.com/api/products/object#product_object-tax_code).
To learn more about the relationship between products, prices, and tax codes,
and how they impact tax behavior, see the [products, prices, and tax
codes](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
documentation.

You must select the most appropriate product tax code for every product or
service you sell. Visit the [tax settings
page](https://dashboard.stripe.com/settings/tax) to select a preset product tax
code to serve as the default. Afterwards, visit the [product
catalogue](https://dashboard.stripe.com/products?active=true&has_tax_code=false)
to confirm that the default is correct for your existing products. If not, edit
each product to select a more appropriate product tax code for it.

- **Default shipping tax code:** The tax treatment type applied to shipping or
delivery fees added to your charge. Some countries levy a distinct tax rate
specifically on shipping fees. The default shipping tax code is used to identify
this unique tax treatment.

If you’re selling digital goods or services, or if your business is based in the
EU, you typically don’t need to select a tax treatment. However, if neither of
these conditions apply to your business, select the tax treatment that’s most
relevant to you. In the absence of a specific shipping tax code on a shipping
rate, we default to using the tax treatment you’ve selected.

[Select whether prices include tax by
default](https://docs.stripe.com/tax/set-up#default-tax-behavior)
Tax behavior is a setting that determines whether Stripe should add taxes on top
of your price, or if the price already includes taxes. This ensures that taxes
don’t affect the total amount charged to your customers.

To calculate the total amount, Stripe needs to know the tax behavior of each
price in the transaction. The default tax behavior is the default setting that
applies when you don’t explicitly specify the
[tax_behavior](https://docs.stripe.com/api/prices/object#price_object-tax_behavior)
on a [Price object](https://docs.stripe.com/api/prices).

You have three options:

- **Exclusive:** You want to exclude tax from prices so that you add tax on top.
- **Inclusive:** You want to include tax in prices so that tax doesn’t affect
the total.
- **Automatic:** You want to use the
[currency](https://docs.stripe.com/api/prices/object#price_object-currency) of
prices to let Stripe decide whether to include or exclude tax. Stripe excludes
tax from prices in USD and CAD, but includes it in prices for all other
currencies.

Learn about [tax behavior for products and
prices](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-behavior).

[Add registrations](https://docs.stripe.com/tax/set-up#add-registrations)
Before you start collecting tax from your customers, you must
[register](https://docs.stripe.com/tax/registering) with the local tax
authority. A [tax registration](https://docs.stripe.com/api/tax/registrations)
lets Stripe know that your business is registered to collect tax on payments
within a region, enabling you to automatically collect tax. Our [monitoring tool
in the Dashboard](https://dashboard.stripe.com/tax/transactions) helps you
understand where you might need to register with the local tax authority.

Visit [Registrations](https://dashboard.stripe.com/tax/registrations) in the
Dashboard to add your tax registrations. If you haven’t registered yet but are
planning to, you can also schedule a tax registration to take effect at a date
in the future. You can also use [Stripe to
register](https://docs.stripe.com/tax/use-stripe-to-register) on your behalf.

[Enable Tax in your Stripe integration or use the Stripe Tax
API](https://docs.stripe.com/tax/set-up#integrate)
The final step in setting up Stripe Tax is to enable automatic tax on your
Stripe integration. Here’s how:

No-codeLow-code
After you click **Get started**, Stripe Tax is automatically enabled for new
transactions that you create in the Dashboard. To disable it, go to your [tax
settings](https://dashboard.stripe.com/settings/tax).

![Stripe Dashboard with the automatic tax toggle set to
true](https://b.stripecdn.com/docs-statics-srv/assets/dashboard_automatic_tax.2338adf39e3a07ad9acd79c036e7c637.png)

Stripe Dashboard with the automatic tax toggle set to true

Integration
Definition[Invoicing](https://docs.stripe.com/tax/invoicing)Automatically
calculate tax on your invoices using the Dashboard without any
code.[Subscriptions](https://docs.stripe.com/tax/subscriptions/update)Calculate
the tax to collect on your recurring payments when using Stripe Billing.[Payment
Links](https://docs.stripe.com/tax/payment-links)Use Stripe Tax with Payment
Links to automatically calculate and collect tax on a payment page and share a
link to it with your customers, without writing any code.

## Links

- [tax settings page](https://dashboard.stripe.com/settings/tax)
- [Tax Settings API](https://docs.stripe.com/api/tax/settings)
- [Tax for software platforms](https://docs.stripe.com/tax/tax-for-platforms)
- [sign up](https://dashboard.stripe.com/register)
- [retrieve](https://docs.stripe.com/api/tax/settings/retrieve)
- [update](https://docs.stripe.com/api/tax/settings/update)
- [Products](https://docs.stripe.com/api/products/object)
-
[tax_code](https://docs.stripe.com/api/products/object#product_object-tax_code)
- [products, prices, and tax
codes](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior)
- [product
catalogue](https://dashboard.stripe.com/products?active=true&has_tax_code=false)
-
[tax_behavior](https://docs.stripe.com/api/prices/object#price_object-tax_behavior)
- [Price object](https://docs.stripe.com/api/prices)
- [currency](https://docs.stripe.com/api/prices/object#price_object-currency)
- [tax behavior for products and
prices](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-behavior)
- [register](https://docs.stripe.com/tax/registering)
- [tax registration](https://docs.stripe.com/api/tax/registrations)
- [monitoring tool in the
Dashboard](https://dashboard.stripe.com/tax/transactions)
- [Registrations](https://dashboard.stripe.com/tax/registrations)
- [Stripe to register](https://docs.stripe.com/tax/use-stripe-to-register)
- [Invoicing](https://docs.stripe.com/tax/invoicing)
- [Subscriptions](https://docs.stripe.com/tax/subscriptions/update)
- [Payment Links](https://docs.stripe.com/tax/payment-links)