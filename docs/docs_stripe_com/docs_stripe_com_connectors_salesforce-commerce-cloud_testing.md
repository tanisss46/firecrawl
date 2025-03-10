# Test your SFRA integration

## Learn about testing your SFRA integration.

After you install the cartridge and integrate it according to the instructions,
try to place an order on your sandbox to test the storefront functionality.

You can find a number of [test credit card
numbers](https://docs.stripe.com/testing) that you can use to test a variety of
scenarios. However, the test cards only work while using your test secret and
publishable API keys. You can’t use real credit card numbers with your test API
keys.

You should monitor and test the integration against the Stripe Dashboard before
going live. Stripe functions largely the same with both test and live
transactions (aside from what credit card numbers you can use) . After you’ve
completed and tested your integration, change your two Stripe API keys to take
your integration live.

## Checkout

- Add a product into the cart and view the cart page or expand the mini cart.
- Click **Checkout** and check out as a Guest or log into your account.
- Fill the shipping address or select shipping address from the saved address
and select the shipping method.
- Click **Next: Payment**.
- Fill in the billing address or select the billing address from the saved
address, fill in the email and phone number and select the payment method as
**Credit card** and enter test data from the [Stripe
docs](https://docs.stripe.com/testing) or use the card number `4242424242424242`
and any CVV and expiration date.

!
- Click on **Next: Place Order**.

!

If your test transaction was successful, the confirmation page will open.

## Checkout using the Payment Request Button

- Make sure you have at least one saved address and one credit card in your
browser (Chrome).
- Add a product into the cart and view the cart page or expand the mini cart.
- Click **Checkout** and check out as a Guest or log into your account.
- Fill in the shipping address or select the shipping address from a saved
address and select the shipping method.
- Click on **Next: Payment**.
- Click on **Pay now**.

!
- When the dialog opens, fill in the payment information and click the **Pay**.

!
- Enter any CVC code and click **Confirm**.

!
- Clicking **Confirm** redirects you to the last page of the checkout. Click
**Place Order**.

!

The confirmation page opens.

!

## Links

- [test credit card numbers](https://docs.stripe.com/testing)