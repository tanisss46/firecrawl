# Send complete fraud signals

## Learn about Stripe's recommendations for using Stripe Radar to send a complete set of fraud signals.

Stripe [Radar](https://docs.stripe.com/radar)’s machine learning models use many
signals to distinguish between fraudulent and legitimate payments. We compute
some of these signals automatically, but many of them depend on the information
that your integration provides. In general, the more data your integration
provides, the more successful fraud prevention can be.

If you don’t collect enough information from your customers, it can reduce the
effectiveness of fraud detection. Conversely, if you collect too much
information, it can negatively impact the checkout experience and result in a
lower conversion rate.

## Integration types

Stripe Radar uses data from the Stripe network to effectively detect and block
fraudulent transactions, regardless of how you integrate with Stripe. However,
the way you integrate with Stripe to process payments can significantly impact
the completeness of the fraud signals you send us. The more information you send
about a payment, the better Stripe Radar is at detecting and preventing fraud.
Using one of our recommended payment integrations allows you to get the most out
of Radar. If you can’t use a recommended integration, consider including as much
additional data as possible, as explained in our
[recommendations](https://docs.stripe.com/radar/integration#recommendations)
below.

Integration typeRadar integration quality[Stripe Payment
Links](https://docs.stripe.com/payment-links) RecommendedExcellent[Stripe
Checkout](https://docs.stripe.com/payments/checkout) RecommendedExcellent[Stripe
Elements](https://docs.stripe.com/payments/elements) with Customer signals
RecommendedExcellentDirect [API](https://docs.stripe.com/api) integration with
[Radar Sessions](https://docs.stripe.com/radar/radar-session) and Customer
signalsExcellentDirect [API](https://docs.stripe.com/api) integration with
client and Customer signalsVery goodDirect [API](https://docs.stripe.com/api)
integration with client signalsGoodDirect [API](https://docs.stripe.com/api)
integration with Customer signalsFairDirect [API](https://docs.stripe.com/api)
integration with no additional signalsPoor
## Important signals to send to Stripe

Including the following information with your payments can have a significant
impact on the performance of Stripe Radar’s fraud detection models. Our
recommended integrations enable you to collect this information, while direct
integrations might need to explicitly include this data.

DataEstimated fraud model improvement[Advanced fraud
signals](https://docs.stripe.com/disputes/prevention/advanced-fraud-detection)36%IP
address12%Customer email11%Customer name3%Billing address1
## Recommendations

We’ve tested the following recommendations to make sure that your conversion
rate remains high while maximizing the performance of our machine learning
models.

#### Checklist progress

As you complete each item and check it off, the state of each checkbox is stored
within your browser’s cache. You can refer back to this page at any time to see
what you’ve completed so far.

- Collect advanced fraud signals automatically by using Payment Links, Checkout,
Elements, or our mobile SDKs
The most important action you can take to guard against fraud is to collect
customer payment information using one of our [online payments
integrations](https://docs.stripe.com/payments/online-payments). Each method
automatically collects important high-signal data, such as device information
and IP addresses. To further improve fraud detection, collect the cardholder
name, full billing address, postal code, and the card’s CVC code during
checkout.

You can build a seamless checkout flow within your website or app using any of
these methods, and securely pass sensitive card information directly to Stripe
without passing it through your servers—greatly simplifying your [PCI
compliance](https://docs.stripe.com/security/guide). Determine which integration
makes the most sense for your business and product goals, but any of these
integration methods help optimize your integration for fraud prevention.

#### Note

If you’re not using one of the recommended payment integrations, consider using
[Radar Sessions](https://docs.stripe.com/radar/radar-session) to automatically
collect [advanced fraud
signals](https://docs.stripe.com/disputes/prevention/advanced-fraud-detection)
to send to Stripe. You can also pass a subset of our advanced fraud signals
directly using our APIs, as shown below.

```
curl https://api.stripe.com/v1/payment_intents \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=2000 \
 -d currency=usd \
 -d "payment_method_data[type]"=card \
 -d "payment_method_data[card][number]"=4000002500003155 \
 -d "payment_method_data[card][exp_month]"=12 \
 -d "payment_method_data[card][exp_year]"=29 \
 -d "payment_method_data[card][cvc]"=123 \
 -d "payment_method_data[ip]"="62.132.141.1" \
--data-urlencode "payment_method_data[user_agent]"="Mozilla/5.0 (compatible;
MSIE 9.0; Windows NT 6.1; Trident/5.0)" \
--data-urlencode
"payment_method_data[referrer]"="https://example.com/payment-page"
```

```
curl https://api.stripe.com/v1/charges \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d amount=2000 \
 -d currency=usd \
 -d source=tok_visa \
 -d ip="62.132.141.1" \
--data-urlencode user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1;
Trident/5.0)" \
 --data-urlencode referrer="https://example.com/payment-page"
```
- Create payments using the Customer object, where possible
Using [Customer](https://docs.stripe.com/api#customers) objects when creating
payments allows Stripe to track the payment patterns for each customer over
time. This significantly increases our ability to identify irregularities in
purchasing behavior. To do this, you should:

- [Set up Payment Methods for future
use](https://docs.stripe.com/payments/save-and-reuse) and add a [billing
address](https://docs.stripe.com/api/customers/object#customer_object-address)
to `Customer` objects and use them to create subsequent payments.
- Provide your customer’s [email
address](https://docs.stripe.com/api#customer_object-email) when creating a
`Customer` object.
- Provide your customer’s
[name](https://docs.stripe.com/api/#customer_object-name) when you tokenize
their card information.
- If you ship physical goods, we also recommend collecting the customer’s
[shipping address](https://docs.stripe.com/api#customer_object-shipping) and
saving this to their associated `Customer` object.

Each `Customer` object can also store [multiple payment
methods](https://docs.stripe.com/saving-cards#multiple-payment-methods), so you
can enhance checkout by offering to save multiple cards. Stripe can continue to
track payment patterns for each customer, regardless of which one they use.

If you’re creating a
[PaymentIntent](https://docs.stripe.com/api/payment_intents) manually, make sure
to handle [declines](https://docs.stripe.com/declines). If you reuse the
PaymentIntent, you can track repeated attempts to help counter [card
testing](https://docs.stripe.com/disputes/prevention/card-testing).
- Include Stripe.js on every page of your site
Include [Stripe.js](https://docs.stripe.com/payments/elements) on every page of
your site, not just the checkout page where your customer enters their payment
information. By doing so, Stripe can detect anomalous behavior that may be
indicative of fraud as customers browse your website—[providing additional
signals](https://docs.stripe.com/disputes/prevention/advanced-fraud-detection)
that increase the effectiveness of our detection.

```
<script async src="https://js.stripe.com/v3/"></script>
```

#### Note

Always load Stripe.js directly from **https://js.stripe.com/v3/**. We don’t
support using a local copy of Stripe.js-it can result in user-visible errors,
and reduces the effectiveness of our fraud detection.
- Update your privacy policy if necessary
Radar collects information on anomalous device or user behavior that might be
indicative of fraud. Make sure that your own privacy policy tells your customers
about this type of collection. Here’s a paragraph you could add to your policy
if it doesn’t already include such a disclosure:

We use Stripe for payment, analytics, and other business services. Stripe
collects identifying information about the devices that connect to its services.
Stripe uses this information to operate and improve the services it provides to
us, including for fraud detection. You can learn more about Stripe and read its
privacy policy at https://stripe.com/privacy.
- Consider enabling Radar for future use
Radar operates on a per-charge level, which means that during a [PaymentIntent
lifecycle](https://docs.stripe.com/payments/paymentintents/lifecycle), Radar
might scan multiple charges if the payment has retries. By default, Radar
doesn’t scan if you [set up a Payment Method for future
use](https://docs.stripe.com/payments/save-and-reuse) *without* a charge. If you
want to scan [SetupIntents](https://docs.stripe.com/api/setup_intents), go to
the [Radar settings](https://dashboard.stripe.com/settings/radar) and enable
**Use Radar on payment methods saved for future use**.

## Links

- [Radar](https://docs.stripe.com/radar)
- [recommendations](https://docs.stripe.com/radar/integration#recommendations)
- [Stripe Payment Links](https://docs.stripe.com/payment-links)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Stripe Elements](https://docs.stripe.com/payments/elements)
- [API](https://docs.stripe.com/api)
- [Radar Sessions](https://docs.stripe.com/radar/radar-session)
- [Advanced fraud
signals](https://docs.stripe.com/disputes/prevention/advanced-fraud-detection)
- [online payments
integrations](https://docs.stripe.com/payments/online-payments)
- [PCI compliance](https://docs.stripe.com/security/guide)
- [https://example.com/payment-page](https://example.com/payment-page)
- [Customer](https://docs.stripe.com/api#customers)
- [Set up Payment Methods for future
use](https://docs.stripe.com/payments/save-and-reuse)
- [billing
address](https://docs.stripe.com/api/customers/object#customer_object-address)
- [email address](https://docs.stripe.com/api#customer_object-email)
- [name](https://docs.stripe.com/api/#customer_object-name)
- [shipping address](https://docs.stripe.com/api#customer_object-shipping)
- [multiple payment
methods](https://docs.stripe.com/saving-cards#multiple-payment-methods)
- [PaymentIntent](https://docs.stripe.com/api/payment_intents)
- [declines](https://docs.stripe.com/declines)
- [card testing](https://docs.stripe.com/disputes/prevention/card-testing)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [PaymentIntent
lifecycle](https://docs.stripe.com/payments/paymentintents/lifecycle)
- [SetupIntents](https://docs.stripe.com/api/setup_intents)
- [Radar settings](https://dashboard.stripe.com/settings/radar)