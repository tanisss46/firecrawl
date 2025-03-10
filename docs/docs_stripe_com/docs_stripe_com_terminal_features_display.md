# Display cart details

## Dynamically update cart details on the reader screen.

The built-in screen of the [Verifone
P400](https://docs.stripe.com/terminal/readers/verifone-p400), [BBPOS WisePOS
E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e) and [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700) can display
line items. During the checkout process, you can update the reader’s screen to
show individual items in the transaction, along with the total price.

![Cart
details](https://b.stripecdn.com/docs-statics-srv/assets/set-reader-display-pre-dip.d32fa58c6645790c373a05cf39d9c416.png)

Cart details screen

## Set the reader display

To display the line items and total on the reader, call `setReaderDisplay`
before processing the payment and pass the information in the
[cart](https://docs.stripe.com/api/terminal/readers/set_reader_display#set_reader_display-cart)
parameter.

The amounts passed to the `setReaderDisplay` method are only used for display
purposes. The reader won’t automatically calculate tax or the total—your
application must calculate the tax and total before displaying the values. You
can use the [Stripe Tax API](https://docs.stripe.com/tax/custom#calculate-tax)
to calculate taxes. Similarly, the total passed to `setReaderDisplay` doesn’t
control the amount charged to the customer. Make sure the amount displayed on
the reader matches the amount you’re charging your customer.

Server-drivenJavaScriptiOSAndroidReact Native
```
curl https://api.stripe.com/v1/terminal/readers/tmr_xxx/set_reader_display \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d type=cart \
 -d "cart[line_items][0][description]"="Caramel latte" \
 -d "cart[line_items][0][amount]"=659 \
 -d "cart[line_items][0][quantity]"=1 \
 -d "cart[line_items][1][description]"="Dozen donuts" \
 -d "cart[line_items][1][amount]"=1239 \
 -d "cart[line_items][1][quantity]"=1 \
 -d "cart[currency]"=usd \
 -d "cart[tax]"=100 \
 -d "cart[total]"=1998
```

To clear reader display on the server-driven integration, call the
[cancel_action](https://docs.stripe.com/api/terminal/readers/cancel_action)
endpoint.

## Pre-dip a card

#### Note

Pre-dipping a card is only supported for payments in the US.

The [Verifone P400](https://docs.stripe.com/terminal/readers/verifone-p400),
[BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e), and
[Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700) support the
ability to present a card to the reader before the transaction amount is
finalized.

This option—known as *pre-dip*, *pre-tap*, or *pre-swipe*—can help speed up
transaction times by allowing a customer to present a payment method before the
end of the transaction.

The `setReaderDisplay` method prepares the reader for pre-dipping. Your customer
can present a payment method at any point after this method is called. You can
call `setReaderDisplay` multiple times to update the information displayed
without impacting the pre-dipping process. Updating the display doesn’t
invalidate a pre-dip, if one has already occurred.

Pre-dipping only allows your customer to present a card early in the payment
process, it doesn’t move the payment process forward. Your integration can’t
tell if pre-dipping has occurred, and you must implement the full payment flow
for all transactions, regardless of pre-dipping.

## Pre-dip disabled

If pre-dip isn’t available in your country, the screen shows only the subtotal
and line items.

![Pre-dip
disabled](https://b.stripecdn.com/docs-statics-srv/assets/set-reader-display-no-pre-dip.63f146b9e0b0ded9f57fe83d2b9e4a7d.png)

Pre-dip disabled

## Links

- [Verifone P400](https://docs.stripe.com/terminal/readers/verifone-p400)
- [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e)
- [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700)
- [setReaderDisplay
(iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)setReaderDisplay:completion:)
- [setReaderDisplay
(Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/set-reader-display.html)
- [setReaderDisplay
(JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk#set-reader-display)
- [setReaderDisplay (React
Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#setReaderDisplay)
- [setReaderDisplay
(Java)](https://stripe.dev/stripe-terminal-java/core/com.stripe.stripeterminal/-terminal/set-reader-display.html)
-
[cart](https://docs.stripe.com/api/terminal/readers/set_reader_display#set_reader_display-cart)
- [Stripe Tax API](https://docs.stripe.com/tax/custom#calculate-tax)
- [cancel_action](https://docs.stripe.com/api/terminal/readers/cancel_action)