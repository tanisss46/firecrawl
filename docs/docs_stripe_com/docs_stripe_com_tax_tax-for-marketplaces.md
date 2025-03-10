# Tax for marketplaces

## Learn about tax requirements for platforms and marketplaces, and how to enable Stripe Tax to collect tax on transactions when the Connect platform is liable.

## Tax requirements for platforms and marketplaces

Many countries and US states require marketplace operators to collect sales tax
and VAT on their facilitated sales. The US refers to these businesses as
marketplace facilitators, while other regions, such as Europe, might refer to
them as deemed sellers.

As a marketplace operator, your tax collection requirements differ depending on
the country or state. However, if your electronic interface enables transactions
between buyers and sellers and you directly or indirectly collect customer
payments, you might need to fulfill tax collection responsibilities.

If your businesses operates a marketplace or platform, you must first determine
whether they qualify as a marketplace facilitator or a deemed seller, then make
sure that they maintain tax compliance. If you’re unsure about your business’s
tax requirements, consult a tax advisor.

If your business operates a marketplace and wants to collect tax on sales
facilitated through this marketplace, refer to details below to enable Stripe
Tax for marketplaces.

## Enable Stripe Tax for marketplaces

Stripe Tax enables businesses to calculate, collect, and file indirect taxes in
over 40 countries, across hundreds of product categories.

Use this guide if your platform is responsible for collecting, filing, and
reporting taxes.

#### Note

We use the platform’s head office location, preset tax code, and tax
registrations to calculate taxes. However, we don’t use the connected account
information for tax purposes.

- [Configure your platform account for tax
collection](https://docs.stripe.com/tax/tax-for-marketplaces#set-up)
- (Optional) [Assign tax codes to product
catalog](https://docs.stripe.com/tax/tax-for-marketplaces#assign-product-tax-codes)
- [Integrate tax calculation and
collection](https://docs.stripe.com/tax/tax-for-marketplaces#enable-tax-collection)
- [Withhold the collected tax
amount](https://docs.stripe.com/tax/tax-for-marketplaces#tax-withholding)
- [Access Stripe Tax
reports](https://docs.stripe.com/tax/tax-for-marketplaces#access-reports)
[Configure your platform account for tax
collection](https://docs.stripe.com/tax/tax-for-marketplaces#set-up)
To collect taxes, you need the platform account’s tax settings and
registrations.

### Use the Stripe Dashboard

### Use the Stripe API

[Assign tax codes to your product
catalog](https://docs.stripe.com/tax/tax-for-marketplaces#assign-product-tax-codes)
To calculate taxes, Stripe Tax requires that you classify products into tax
codes. You can do so by supplying [a preset tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#preset-tax-codes)
for the platform account, which might be sufficient if you typically sell a
single category of items or services.

Additionally, you can [map tax codes to each
product](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)
to give you more control over tax categorization. You might have to map each
product that a seller sets up on your marketplace. You can find a list of
supported tax codes from [available tax
codes](https://docs.stripe.com/tax/tax-codes) or retrieve it from the Stripe
[Tax Code API](https://docs.stripe.com/api/tax_codes).

[Integrate tax calculation and
collection](https://docs.stripe.com/tax/tax-for-marketplaces#enable-tax-collection)
You need to integrate with Stripe Tax to estimate taxes as part of your checkout
flow.

### Payment Links

### Payment Links for one-time payments

### Payment Links for subscriptions

### Checkout

### Checkout Sessions for one-time payments

### Checkout Sessions for subscriptions

### Billing

### Subscriptions

### Invoicing

### Custom flows using the Stripe Tax API

### Payment Intents

### Off-Stripe payments

After you implement it, Stripe automatically starts collecting tax in
jurisdictions where you have an active registration.

#### Caution

Independent of the payment APIs, we credit the transaction amount to the
connected account. You need to withhold the collected tax amount on the platform
because the platform is [liable for tax](https://docs.stripe.com/tax/connect).

[Withhold collected tax
amount](https://docs.stripe.com/tax/tax-for-marketplaces#tax-withholding)
You must make sure that the tax collected is transferred to your marketplace
account, so that you can then remit the tax to relevant jurisdictions.

### Checkout and Payment Links

### Invoicing

### Subscriptions

### Payment Intents with Stripe Tax API

[Access Stripe Tax
Reports](https://docs.stripe.com/tax/tax-for-marketplaces#access-reports)
### Use the Stripe Dashboard

### Use the Stripe API

## See also

- [Calculate tax in your custom checkout
flow](https://docs.stripe.com/tax/custom)

## Links

- [a preset tax
code](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#preset-tax-codes)
- [map tax codes to each
product](https://docs.stripe.com/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)
- [available tax codes](https://docs.stripe.com/tax/tax-codes)
- [Tax Code API](https://docs.stripe.com/api/tax_codes)
- [liable for tax](https://docs.stripe.com/tax/connect)
- [Calculate tax in your custom checkout
flow](https://docs.stripe.com/tax/custom)