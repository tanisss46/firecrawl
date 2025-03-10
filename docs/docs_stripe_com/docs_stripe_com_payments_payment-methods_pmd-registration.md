# Register domains for payment methods

## Register domains to use payment methods (including Link, Apple Pay, and Google Pay) in Elements or Checkout's embeddable payment form.

For certain payment methods, you must register every web domain that shows the
payment method if your integration uses
[Elements](https://docs.stripe.com/payments/elements) or [Checkout’s embeddable
payment
form](https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=embedded-form).
This includes registering top-level domains and subdomains. For example, if you
have the domain **yourdomain.com** and subdomains like **shop.yourdomain.com**
and **www.yourdomain.com**, this guide explains how to register them.

After you register a domain, that domain is ready for use with other payment
methods that you might enable in the future.

The following payment methods require registration:

- Google Pay
- Link
- PayPal
- Amazon Pay
- Apple Pay

#### Apple Pay and merchant validation

The Apple Pay documentation describes their process of “merchant validation,"
which Stripe handles for you behind the scenes. You don’t need to create an
Apple Merchant ID or CSR. Instead, follow the steps in this guide.

## Testing

You also need to register domains for testing. When testing locally, you can use
a tool such as [ngrok](https://ngrok.com/) to get an HTTPS domain. You can
either register in test mode, or register in live mode and the domain will also
be registered in test mode automatically. Remember to register your domains in
live mode before going live.

DashboardAPI
You can create and manage domains in the Dashboard on the [Payment method
domains page](https://dashboard.stripe.com/settings/payment_method_domains) for
use in production and testing.

#### Using Connect

Connect platforms that create direct charges must use the API to manage domains
for their [connected
accounts](https://docs.stripe.com/payments/payment-methods/pmd-registration#register-a-domain-using-connect),
not the Stripe Dashboard.

## Register your domain

To register a domain:

- On the [Payment method domains
page](https://dashboard.stripe.com/settings/payment_method_domains), click **Add
a new domain**.
- Enter your domain name.
- Click **Save and continue**.
- (Optional) Repeat steps 1-3 for additional domains that you need to register.

After completing these steps, your domain shows up on the Payment method domains
page.

### Using an iframe

- **Using an iframe with Elements**: When using an iframe, its origin must match
the top-level origin (except for Safari 17+ when specifying `allow="payment"`
attribute). Two pages have the same origin if the protocol, host (full domain
name), and port (if specified) are the same for both pages.
- **Top-level domain and iframe domain**: If the top-level domain differs from
the iframe domain, the top-level domain and the iframe’s source domain must both
be registered payment method domains on the associated account.

## Manage your domain

You can see a list of all of your domains in the Dashboard.

To disable a domain, click the row action and then click **Disable**. If a
domain is disabled, the payment methods no longer appear in Elements or
Checkout’s embeddable payment form on that domain.

To enable a disabled domain, click the row action and then click **Enable**.

## Register your domain while using Connect

Connect platforms must register all domains where Elements or Checkout’s
embeddable payment form displays the payment methods listed above. The domain
where the charge is being run needs to be registered for the user running the
charge.

If the platform creates [direct
charges](https://docs.stripe.com/connect/direct-charges), use your platform’s
secret key to authenticate the request and set the Stripe-Account header to your
connected account’s Stripe ID.

If the platform creates [destination
charges](https://docs.stripe.com/connect/destination-charges) or [separate
charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers), use
your platform’s secret key to authenticate the request and omit the
Stripe-Account header.

Learn more about [Making API calls for connected
accounts](https://docs.stripe.com/connect/authentication).

```
curl https://api.stripe.com/v1/payment_method_domains \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d domain_name="example.com"
```

## Links

- [Elements](https://docs.stripe.com/payments/elements)
- [Checkout’s embeddable payment
form](https://docs.stripe.com/payments/checkout/how-checkout-works?payment-ui=embedded-form)
- [ngrok](https://ngrok.com/)
- [Payment method domains
page](https://dashboard.stripe.com/settings/payment_method_domains)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [Making API calls for connected
accounts](https://docs.stripe.com/connect/authentication)