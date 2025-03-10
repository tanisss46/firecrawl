# Collect taxes for recurring payments

## Learn how to collect and report taxes for recurring payments.

To calculate tax for recurring payments, Stripe offers Stripe Tax and Tax Rates.

- **Stripe Tax**—a paid product that automatically calculates the tax on your
transactions without the need to define the rates and rules. Fees only apply
after you’ve added at least one location where you’re registered to calculate
and remit tax. For more information, see [Stripe
Tax](https://docs.stripe.com/tax).
- **Tax Rates**—a free feature that allows you to define any number of tax rates
for [invoices](https://docs.stripe.com/api/invoices),
[subscriptions](https://docs.stripe.com/billing/subscriptions/creating), and
one-time payments that use Checkout. Stripe won’t create or maintain any tax
rates on your behalf. For more information, see [Tax
Rates](https://docs.stripe.com/api/tax_rates) and [how to use
them](https://docs.stripe.com/billing/taxes/tax-rates).
Stripe TaxTax Rates
Stripe Tax allows you to calculate the tax amount on your recurring payments
when using Stripe Billing. Use your customer’s location details to preview the
tax amount before creating a subscription and then create it with Stripe Tax
enabled when your customer is ready to pay. Stripe Tax integrates with Stripe
Billing and automatically handles tax calculation with your [pricing
model](https://docs.stripe.com/products-prices/pricing-models),
[prorations](https://docs.stripe.com/billing/subscriptions/prorations),
[discounts](https://docs.stripe.com/billing/subscriptions/coupons),
[trials](https://docs.stripe.com/billing/subscriptions/trials), and so on.

Customer

Client

Server

Stripe

Go to your checkout page

Enter address information

Estimate taxes and total

`POST /v1/invoices/create_preview`

Return a preview invoice

Return taxes and total

Submit

Submit

`POST /v1/customers/:id`

Return the updated Customer

`POST /v1/subscriptions`

Return a new subscription

Return client secret

`stripe.confirmPayment()`

Redirect to `return_url`

A diagram providing a high level overview of a Stripe Tax and Billing
integration.
This guide assumes you’re setting up Stripe Tax and Billing for the first time.
See how to [update existing
subscriptions](https://docs.stripe.com/tax/subscriptions/update).

If you’re using Stripe Checkout to create new subscriptions, see how to
[automatically collect tax on Checkout
sessions](https://docs.stripe.com/tax/checkout), or watch the short video below:

[Activate Stripe
Tax](https://docs.stripe.com/billing/taxes/collect-taxes#activate)
[Log in](https://dashboard.stripe.com/settings/tax) or [sign
up](https://dashboard.stripe.com/register) for Stripe to activate Stripe Tax.

[Update your products and prices
(optional)](https://docs.stripe.com/billing/taxes/collect-taxes#product-and-price-setup)
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

[Estimate taxes and
totalServer-side](https://docs.stripe.com/billing/taxes/collect-taxes#estimate-taxes-total)Before
address collectionAfter address collection
When a customer first enters your checkout flow, you might not have their
address information yet. In this case, [create a preview
invoice](https://docs.stripe.com/api/invoices/create_preview) and set
[customer_details.tax.ip_address](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-customer_details-tax-ip_address)
to let Stripe locate them using their IP address.

#### Caution

In most cases, Stripe can resolve an IP address to a physical area, but its
precision varies and might not reflect your customer’s actual location. We don’t
recommend relying on a customer’s IP address to determine their address beyond
an initial estimate.

```
curl https://api.stripe.com/v1/invoices/create_preview \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "automatic_tax[enabled]"=true \
 -d "customer_details[tax][ip_address]"={{IP_ADDRESS}} \
 -d "subscription_details[items][0][price]"={{PRICE_ID}}
```

Check the
[automatic_tax.status](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax-status)
of the invoice. If the status is `requires_location_inputs`, it means that the
address details are invalid or insufficient. In this case, prompt your customer
to re-enter their address details or provide accurate address details.

The invoice
[total](https://docs.stripe.com/api/invoices/object#invoice_object-total) is how
much your customer pays and
[tax](https://docs.stripe.com/api/invoices/object#invoice_object-tax) is the sum
of all tax amounts on the invoice. If you want a breakdown of taxes, see
[total_tax_amounts](https://docs.stripe.com/api/invoices/object#invoice_object-total_tax_amounts).
All amounts are in cents.

#### Zero tax

If the `tax` is zero, make sure that you have a tax registration in your
customer’s location. See how to [register for sales tax, VAT, and
GST](https://docs.stripe.com/tax/registering) and learn more about [zero tax
amounts and reverse charges](https://docs.stripe.com/tax/zero-tax).

[Collect customer
informationClient-side](https://docs.stripe.com/billing/taxes/collect-taxes#collect-customer-information)
After you have an estimate of the taxes and the total, start collecting customer
information including their shipping address (if applicable), billing address,
and their payment details. Notice that when you use Stripe Tax, you collect
payment details without an Intent. The first step is to [create an Elements
object without an
Intent](https://docs.stripe.com/js/elements_object/create_without_intent):

```
const stripe = Stripe("pk_test_TYooMQauvdEDq54NiTphI7jx");

const elements = stripe.elements({
 mode: 'subscription',
 currency: '{{CURRENCY}}',
 amount: {{TOTAL}},
});
```

Next, [create an Address
Element](https://docs.stripe.com/js/elements_object/create_address_element) and
[a Payment
Element](https://docs.stripe.com/js/elements_object/create_payment_element) and
[mount](https://docs.stripe.com/js/element/mount) both:

```
const addressElement = elements.create('address', {
 mode: 'billing' // or 'shipping', if you are shipping goods
});
addressElement.mount('#address-element');

const paymentElementOptions = { layout: 'accordion'};
const paymentElement = elements.create('payment', paymentElementOptions);
paymentElement.mount('#payment-element');
```

Then you can listen to [change
events](https://docs.stripe.com/js/element/events/on_change?type=paymentElement#element_on_change-event)
on the Address Element. When the address changes,
[re-estimate](https://docs.stripe.com/tax/subscriptions?estimate=after#estimate-taxes-total)
the taxes and the total.

```
addressElement.on('change', function(event) {
 // Throttle your requests to avoid overloading your server or hitting
 // Stripe's rate limits.
 const { tax, total } = await updateEstimate(event.value.address);

 elements.update({ amount: total });
 // Update your page to display the new tax and total to the user...
});
```

#### Common mistake

When your customer is entering their address, Address Element fires a `change`
event for each keystroke. To avoid overloading your server and hitting Stripe’s
[rate limits](https://docs.stripe.com/rate-limits), wait for some time after the
last `change` event before re-estimating the taxes and the total.

[Handle
submissionClient-side](https://docs.stripe.com/billing/taxes/collect-taxes#submission)
When your customer submits the form, call
[elements.submit()](https://docs.stripe.com/js/elements/submit) to validate the
form fields and collect any data required for wallets. You must wait for this
function’s promise to resolve before performing any other operations.

```
document.querySelector("#form").addEventListener("submit", function(event) {
 // We don't want to let default form submission happen here,
 // which would refresh the page.
 event.preventDefault();

 const { error: submitError } = await elements.submit();
 if (submitError) {
 // Handle error...
 return;
 }

 const { value: customerDetails } = await addressElement.getValue();

 // See the "Save customer details" section below to implement this
 // server-side.
 await saveCustomerDetails(customerDetails);

 // See the "Create subscription" section below to implement this server-side.
 const { clientSecret } = await createSubscription();

 const { error: confirmError } = await stripe.confirmPayment({
 elements,
 clientSecret,
 confirmParams: {
 return_url: {{RETURN_URL}},
 },
 });
 if (confirmError) {
 // Handle error...
 return;
 }

 // Upon a successful confirmation, your user will be redirected to the
 // return_url you provide before the Promise ever resolves.
});
```

[Save customer
detailsServer-side](https://docs.stripe.com/billing/taxes/collect-taxes#save-customer-details)
[Update](https://docs.stripe.com/api/customers/update) your `Customer` object
using the details you’ve collected from your customer, so that Stripe Tax can
determine their precise location for accurate results.

#### Regional considerationsUnited States

If your customer is in the United States, provide a full address if possible. We
use the term “rooftop-accurate” to mean that we can attribute your customer’s
location to a specific house or building. This provides greater accuracy, where
two houses located side-by-side on the same street might be subject to different
tax rates, because of complex jurisdiction boundaries.

If you haven’t already created a `Customer` object (for example, when your
customer first signs up on your website), you can
[create](https://docs.stripe.com/api/customers/create) one now.

Update customerCreate customer
```
curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "address[line1]"={{LINE1}} \
 -d "address[line2]"={{LINE2}} \
 -d "address[city]"={{CITY}} \
 -d "address[state]"={{STATE}} \
 -d "address[postal_code]"={{POSTAL_CODE}} \
 -d "address[country]"={{COUNTRY}} \
 -d "tax[validate_location]"=immediately
```

#### Caution

If your customer has other existing subscriptions with automatic tax enabled and
you update their address information, the tax and total amounts on their future
invoices might be different. This is because tax rates vary depending on
customer location.

The
[tax.validate_location](https://docs.stripe.com/api/customers/update#update_customer-tax-validate_location)
enum value helps you make sure that the tax location of the customer becomes (or
remains) valid as a result of this operation. If not, Stripe fails your request
with the
[customer_tax_location_invalid](https://docs.stripe.com/error-codes#customer-tax-location-invalid)
error code. This is important because you can’t create an automatic tax enabled
subscription for a customer with an invalid tax location. If you’ve been
checking the
[automatic_tax.status](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax-status)
of your preview invoices as
[advised](https://docs.stripe.com/billing/taxes/collect-taxes#estimate-taxes-total)
previously, this additional validation won’t ever fail. However, it’s good
practice to set `tax[validate_location]="immediately"` whenever you’re creating
or updating a `Customer` object.

[Create
subscriptionServer-side](https://docs.stripe.com/billing/taxes/collect-taxes#create-subscription)
[Create](https://docs.stripe.com/api/subscriptions/create) a subscription with
automatic tax enabled.

```
curl https://api.stripe.com/v1/subscriptions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "automatic_tax[enabled]"=true \
 -d customer={{CUSTOMER_ID}} \
 -d "items[0][price]"={{PRICE_ID}} \
 -d "payment_settings[save_default_payment_method]"=on_subscription \
 -d "expand[0]"="latest_invoice.payment_intent"
```

The
[latest_invoice.payment_intent.client_secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
is the [client
secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
of the [payment intent](https://docs.stripe.com/payments/payment-intents) of the
first (and the latest) invoice of the new subscription. You need to pass the
client secret to your front end to be able to
[confirm](https://docs.stripe.com/api/payment_intents/confirm) the payment
intent.

#### Security tip

Don’t store, log, or expose the client secret to anyone other than the customer.
Make sure that you have TLS enabled on any page that includes the client secret.

If your customer has a default payment method, the first invoice of the
subscription is paid automatically. You can confirm this using
[latest_invoice.status](https://docs.stripe.com/api/invoices/object#invoice_object-status)
of the subscription. If you want to use the new payment details you collected
from your customer in your checkout flow, make sure that the first invoice isn’t
paid automatically. Pass `default_incomplete` for the
[payment_behavior](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)
when you’re creating your subscription and confirm the payment intent using
[stripe.confirmPayment()](https://docs.stripe.com/js/payment_intents/confirm_payment)
as shown. See [Billing collection
methods](https://docs.stripe.com/billing/collection-method) for more
information.

[OptionalHandle
refundsServer-side](https://docs.stripe.com/billing/taxes/collect-taxes#create-credit-note)
## Use webhooks

We recommend listening to subscription events with
[webhooks](https://docs.stripe.com/webhooks) because most subscription activity
happens asynchronously.

When you start using Stripe Tax, make sure to listen to
[invoice.finalization_failed](https://docs.stripe.com/api/events/types#event_types-invoice.finalization_failed)
events. If the
[automatic_tax.status](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax-status)
of the invoice is `requires_location_inputs`, it means that the address details
of your customer are invalid or insufficient. In this case, Stripe can’t
calculate the taxes, can’t finalize the invoice, and can’t collect the payment.
Notify your customer to re-enter their address details or provide an accurate
address.

See [Using webhooks with
subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks) to learn
more.

## See also

- [Determining customer
locations](https://docs.stripe.com/tax/customer-locations)
- [Customer tax IDs](https://docs.stripe.com/billing/customer/tax-ids)
- [Reporting and filing](https://docs.stripe.com/tax/reports)
- [Tax Rates](https://docs.stripe.com/billing/taxes/tax-rates)
- [Tax Rates on Invoices](https://docs.stripe.com/invoicing/taxes/tax-rates)

## Links

- [Stripe Tax](https://docs.stripe.com/tax)
- [invoices](https://docs.stripe.com/api/invoices)
- [subscriptions](https://docs.stripe.com/billing/subscriptions/creating)
- [Tax Rates](https://docs.stripe.com/api/tax_rates)
- [how to use them](https://docs.stripe.com/billing/taxes/tax-rates)
- [pricing model](https://docs.stripe.com/products-prices/pricing-models)
- [prorations](https://docs.stripe.com/billing/subscriptions/prorations)
- [discounts](https://docs.stripe.com/billing/subscriptions/coupons)
- [trials](https://docs.stripe.com/billing/subscriptions/trials)
- [update existing
subscriptions](https://docs.stripe.com/tax/subscriptions/update)
- [automatically collect tax on Checkout
sessions](https://docs.stripe.com/tax/checkout)
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
- [create a preview
invoice](https://docs.stripe.com/api/invoices/create_preview)
-
[customer_details.tax.ip_address](https://docs.stripe.com/api/invoices/create_preview#create_create_preview-customer_details-tax-ip_address)
-
[automatic_tax.status](https://docs.stripe.com/api/invoices/object#invoice_object-automatic_tax-status)
- [total](https://docs.stripe.com/api/invoices/object#invoice_object-total)
- [tax](https://docs.stripe.com/api/invoices/object#invoice_object-tax)
-
[total_tax_amounts](https://docs.stripe.com/api/invoices/object#invoice_object-total_tax_amounts)
- [register for sales tax, VAT, and
GST](https://docs.stripe.com/tax/registering)
- [zero tax amounts and reverse charges](https://docs.stripe.com/tax/zero-tax)
- [create an Elements object without an
Intent](https://docs.stripe.com/js/elements_object/create_without_intent)
- [create an Address
Element](https://docs.stripe.com/js/elements_object/create_address_element)
- [a Payment
Element](https://docs.stripe.com/js/elements_object/create_payment_element)
- [mount](https://docs.stripe.com/js/element/mount)
- [change
events](https://docs.stripe.com/js/element/events/on_change?type=paymentElement#element_on_change-event)
-
[re-estimate](https://docs.stripe.com/tax/subscriptions?estimate=after#estimate-taxes-total)
- [rate limits](https://docs.stripe.com/rate-limits)
- [elements.submit()](https://docs.stripe.com/js/elements/submit)
- [Update](https://docs.stripe.com/api/customers/update)
- [create](https://docs.stripe.com/api/customers/create)
-
[tax.validate_location](https://docs.stripe.com/api/customers/update#update_customer-tax-validate_location)
-
[customer_tax_location_invalid](https://docs.stripe.com/error-codes#customer-tax-location-invalid)
- [Create](https://docs.stripe.com/api/subscriptions/create)
-
[latest_invoice.payment_intent.client_secret](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-client_secret)
- [payment intent](https://docs.stripe.com/payments/payment-intents)
- [confirm](https://docs.stripe.com/api/payment_intents/confirm)
-
[latest_invoice.status](https://docs.stripe.com/api/invoices/object#invoice_object-status)
-
[payment_behavior](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior)
-
[stripe.confirmPayment()](https://docs.stripe.com/js/payment_intents/confirm_payment)
- [Billing collection
methods](https://docs.stripe.com/billing/collection-method)
- [webhooks](https://docs.stripe.com/webhooks)
-
[invoice.finalization_failed](https://docs.stripe.com/api/events/types#event_types-invoice.finalization_failed)
- [Using webhooks with
subscriptions](https://docs.stripe.com/billing/subscriptions/webhooks)
- [Determining customer
locations](https://docs.stripe.com/tax/customer-locations)
- [Customer tax IDs](https://docs.stripe.com/billing/customer/tax-ids)
- [Reporting and filing](https://docs.stripe.com/tax/reports)
- [Tax Rates on Invoices](https://docs.stripe.com/invoicing/taxes/tax-rates)