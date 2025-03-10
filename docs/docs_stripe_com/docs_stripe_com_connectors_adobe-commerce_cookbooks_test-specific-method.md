# Test why a specific payment method doesn't appear

## Force a payment method to appear so you can test it.

Some payment methods only appear when specific conditions are met. For cases
where you can’t get a specific payment method to appear, you can force-enable it
with a small change in the Stripe module. If you then navigate to the checkout
page, it displays an error that explains the reason the payment method is
unavailable.

## Debugging approach

For example, say that Klarna doesn’t appear at checkout. To find out the reason,
open `Helper/PaymentMethodTypes.php` and make the following adjustment:

```
@@ -15,6 +15,8 @@ class PaymentMethodTypes

 public function getPaymentMethodTypes()
 {
 return ['klarna'];
 }

```

If you now navigate to the checkout page, an error is displayed explaining why
klarna is unavailable.

For more payment method codes, [click
here](https://docs.stripe.com/connect/account-capabilities#payment-methods).

## Links

- [click
here](https://docs.stripe.com/connect/account-capabilities#payment-methods)