# Customer self-service with a customer portal

## Allow your customers to manage their own accounts and subscriptions.

Provide self-service functions to your customers by setting up a customer
portal. You can configure it entirely in the Dashboard, or use the API to
implement more advanced features, such as multiple configurations for different
customers or for [connected accounts](https://docs.stripe.com/connect).

You can automate many of your customer interactions by combining a customer
portal with customer communications controlled by [Stripe Billing
automations](https://docs.stripe.com/billing/automations). You create and manage
automations in the Dashboard.

## Get started with the customer portal

[Set up a customer portalNo
code](https://docs.stripe.com/customer-management/activate-no-code-customer-portal)Create
and configure a customer portal using the Dashboard.[Integrate a customer
portalAPI](https://docs.stripe.com/customer-management/integrate-customer-portal)Customize
and integrate a customer portal using code.[Streamline customer portal
interactionsAPI](https://docs.stripe.com/customer-management/portal-deep-links)Set
up custom links to specific self-service actions by coding customer portal
flows.
## Customer portal features

A customer portal allows your customers to self-manage their payment details,
invoices, and subscriptions in one place.

See what your customers can do in the customer portal

**Key customer portal features**

- Download invoices
- Update payment methods
- Cancel a subscription
- Update customer information
- Upgrade and downgrade subscriptions

[View demo](https://billing.stripe.com/customer-portal-demo)

FeatureDescriptionCustomer managementOffer your customers a self-serve method
to:- Update billing information, including their tax IDs
- Update payment methods
- Update subscriptions
- Cancel subscriptions immediately or at the end of the current billing period
- Pay, download, and view current and past invoices
Cancellation deflectionReduce churn by offering your customers a coupon when
they try to cancel their subscription. Customers who cancel anyway can share
why. You can collect those reasons through webhooks or Stripe
Sigma.InteroperabilityUse the portal with other Stripe products:-
[Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Connect](https://docs.stripe.com/connect)
- [Invoices](https://docs.stripe.com/invoicing)
- [Billing](https://docs.stripe.com/billing)
- [Stripe Tax](https://docs.stripe.com/tax)
Localization supportAutomatically localize the portal based on your customers’
preferred language. To view a localized version of the portal, set your
browser’s default language to the language you want to preview. See the full
list of supported languages in the table below.Customized brandingConfigure the
portal to match your branding, including your icon, logo, colors, and business
information.Payment methodsManage payment methods to make it convenient for your
customers to pay you. See the full list of [supported payment
methods](https://docs.stripe.com/customer-management#supported-payment-methods).
Read the [payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
guide to learn more.Invoice-only supportYes. You don’t need to use subscriptions
for the customer portal to be useful for your business and your customers. To
preview invoicing management in the portal, complete the following step- Turn on
test mode in the Dashboard (nothing you do in test mode affects your live
setup).
- Go to the [Customers page](https://dashboard.stripe.com/customers), and select
a customer.
- Create a new invoice for the customer.
- Click **Actions**, then **Open customer portal**. For security reasons, the
quick view option isn’t available for live mode customers.
Language supportLanguages supported by the customer portal- Bulgarian (bg)
- Chinese Simplified (zh)
- Chinese Traditional—Hong Kong (zh-Hant-HK)
- Chinese Traditional—Taiwan (zh-Hant-TW)
- Croatian (hr)
- Czech (cs)
- Danish (da)
- Dutch (nl)
- , US (en)
- , UK (en-GB)
- Estonian (et)
- Filipino (fil)
- Finnish (fi)
- French, France (fr)
- French, Canada (fr-CA)
- German (de)
- Greek (el)
- Hungarian (hu)
- Indonesian (id)
- Italian (it)
- Japanese (ja)
- Korean (ko)
- Latvian (lv)
- Lithuanian (lt)
- Malay (ms)
- Maltese (mt)
- Norwegian Bokmål (nb-NO)
- Polish (pl)
- Portuguese, Portugal (pt)
- Portuguese, Brazil (pt-BR)
- Romanian (ro)
- Russian (ru)
- Slovak (sk)
- Slovenian (sl)
- Spanish, Spain (es)
- Spanish, Latin America (es-419)
- Swedish (sv)
- Thai (th)
- Turkish (tr)
- Vietnamese (vi)
Stripe Connect compatibilityThe customer portal works with Stripe Connect. If
you’re using the customer portal with Stripe Connect, make sure you configure
the customer portal for the platform instead of a connected account.Ephemeral
sessionsPortal sessions are temporary. New portal sessions expire after a 5
minute period. If a customer uses it within that time period, the session
expires within 1 hour of the most recent activity.
### Customer portal limitations

The customer portal has the following limitations:

- If subscriptions use any of the following, customers can only *cancel* them in
the portal (they can’t *update* such subscriptions):

- [Multiple
products](https://docs.stripe.com/billing/subscriptions/multiple-products)
- [Usage-based
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
- Sending invoices for collection. Read more about the `collection_method`
[parameter](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method).
If you use the Dashboard to create the subscription, you make this selection in
the **Payment method** section.
- Unsupported payment methods
- Customers can’t update or cancel subscriptions that currently have an update
scheduled with a [subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules).
- Customers can only modify subscriptions if the new price has the same [tax
behavior](https://docs.stripe.com/api/prices/create#create_price-tax_behavior)
as the initial price. Additionally, no modifications are allowed if the tax
behavior is `unspecified`, even if the tax behavior of the new price is
`unspecified`. Learn more about the `tax_behavior` parameter and how it [relates
to
subscriptions](https://docs.stripe.com/billing/taxes/collect-taxes?tax-calculation=stripe-tax#product-and-price-setup).
- The portal displays the payment method section if the session allows for
payment method management, even if the portal doesn’t support the customer’s
default payment method.
- Customers can’t define multiple [Prices](https://docs.stripe.com/api/prices)
with the same `product` and `recurring.interval` values. For example, to offer a
magazine for 4.00 USD per month regular price and 3.00 USD per month for
students, create a separate student magazine
[Product](https://docs.stripe.com/api/product) version.
- Customer modifications to a `trialing` subscription will end the free trial
and create an invoice for immediate payment.
- When you [allow customers to switch
plans](https://docs.stripe.com/customer-management/configure-portal#configure-subscription-management),
you can specify a maximum of 10 products for them to choose from.
- Displaying the portal inside an iframe isn’t supported.

## Supported payment methods

[Payment
method](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)DescriptionCurrenciesBusiness
locationLimitationsACH Direct Debit (`us_bank_account`)Stripe users can receive
bank transfers directly from customers.USDUSNoneAmazon Pay (`amazon_pay`)Amazon
Pay is a wallet payment method that lets your customers check out the same way
as on Amazon.com.USDUSNoneAU BECS Debit (`au_becs_debit`)Bulk Electronic
Clearing System (BECS) Direct Debit payments from customers with an Australian
bank account.AUDAUSNoneBoleto (`boleto`)Boleto is a popular payment method in
Brazil where customers pay by using a Boleto voucher with a generated
number.BRLBRYou must have a Brazilian Stripe account to accept Boleto from your
customers.Cards (`card`)Cards, icluding Apple Pay and Google Pay, are one of the
most popular ways to pay online, with broad global reach. There are different
types of cards and several steps in the process.Most currenciesMost
locationsNoneCash App Pay (`cashapp`)Cash App is a popular consumer app in the
US that allows customers to bank, invest, send, and receive money using their
digital wallet.USDUSNoneLink (`link`)Link saves and autofills payment and
shipping information for your customers so they don’t need to enter payment
details manually.Most currenciesMost locationsNonePayPal (`paypal`)PayPal is a
payment method that enables customers in any country to pay using their PayPal
account.Most currenciesEurope[Requires
approval](https://docs.stripe.com/payments/paypal/set-up-future-payments#enable-recurring-payments-support-from-stripe-dashboard)Pre-authorized
debits (`acss_debit`)PADs are a low-cost, high volume batch processing network
for financial transactions in Canada.CAD, USDCA, USNoneSEPA direct debit
(`sepa_debit`)The Single Euro Payments Area (SEPA) is an initiative of the
European Union to simplify payments within and across member countries.EURAU,
CA, Europe, HK, JP, MX, NZ, SG, USNoneUK BACS Debit (`uk_bacs_debit`)Bacs Direct
Debit is a reusable, delayed notification payment method available to bank
account holders from the United Kingdom.GBPUKYou must have a UK Stripe account
and a UK bank account to accept UK BACS Debit from your customers.
## Other hosted resources to use with the customer portal

Stripe offers multiple prebuilt resources so you can bill your customers quickly
and maximize revenue retention and recovery.

[Payment links](https://docs.stripe.com/payment-links)Share a link with your
customers to get them signed up for your service through a payment page hosted
by Stripe.[Checkout](https://docs.stripe.com/payments/checkout)Let your
customers sign up through a prebuilt payment form. You can embed it in your site
or redirect your users to a page hosted by Stripe.[Pricing
table](https://docs.stripe.com/payments/checkout/pricing-table)Create a pricing
table in the Stripe Dashboard and embed the table in your site. Your customers
select a plan then pay through Stripe Checkout.

## Links

- [connected accounts](https://docs.stripe.com/connect)
- [Stripe Billing automations](https://docs.stripe.com/billing/automations)
- [Set up a customer portalNo
code](https://docs.stripe.com/customer-management/activate-no-code-customer-portal)
- [Integrate a customer
portalAPI](https://docs.stripe.com/customer-management/integrate-customer-portal)
- [Streamline customer portal
interactionsAPI](https://docs.stripe.com/customer-management/portal-deep-links)
- [View demo](https://billing.stripe.com/customer-portal-demo)
- [Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Links](https://docs.stripe.com/payment-links)
- [Invoices](https://docs.stripe.com/invoicing)
- [Billing](https://docs.stripe.com/billing)
- [Stripe Tax](https://docs.stripe.com/tax)
- [payment
methods](https://docs.stripe.com/payments/payment-methods/integration-options)
- [Customers page](https://dashboard.stripe.com/customers)
- [Multiple
products](https://docs.stripe.com/billing/subscriptions/multiple-products)
- [Usage-based
billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing)
-
[parameter](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method)
- [subscription
schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
- [tax
behavior](https://docs.stripe.com/api/prices/create#create_price-tax_behavior)
- [relates to
subscriptions](https://docs.stripe.com/billing/taxes/collect-taxes?tax-calculation=stripe-tax#product-and-price-setup)
- [Prices](https://docs.stripe.com/api/prices)
- [Product](https://docs.stripe.com/api/product)
- [allow customers to switch
plans](https://docs.stripe.com/customer-management/configure-portal#configure-subscription-management)
- [Payment
method](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type)
- [Requires
approval](https://docs.stripe.com/payments/paypal/set-up-future-payments#enable-recurring-payments-support-from-stripe-dashboard)
- [Pricing table](https://docs.stripe.com/payments/checkout/pricing-table)