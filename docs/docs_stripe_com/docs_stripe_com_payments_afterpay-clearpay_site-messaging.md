# Display Afterpay or Clearpay messagingDeprecated

## Inform customers that you accept payments with Afterpay (also known as Clearpay in the UK).

#### Caution

The content in this topic refers to a Legacy feature. We recommend that you use
the [Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging) to
dynamically show your customers relevant buy now, pay later payment options for
a given purchase. Stripe continues to maintain continuity for the
`afterpayClearpayMessage` Element, but has halted new feature development.

Let your customers know you accept payments with Afterpay by including the
Afterpay messaging Element on your site. We suggest adding the messaging Element
to your product, cart, and payment pages. The
[afterpayClearpayMessage](https://docs.stripe.com/js/elements_object/create_element?type=afterpayClearpayMessage)
Element takes care of:

- Calculating and displaying the installments amount
- Displaying the Afterpay information modal
- Localizing text and currencies
The Making of Prince of Persia: Journals 1985-1993Jordan Mechner$30
or 4 interest-free payments of $7.50 withAfterpay
[ⓘ](https://static.afterpay.com/modal/en_US.html)

## Include the Element

HTML + JSReact
Use Stripe Elements to include the
[afterpayClearpayMessage](https://docs.stripe.com/js/elements_object/create_element?type=afterpayClearpayMessage)
Element on your site.

If you haven’t already, include the Stripe.js script on your page by adding it
to the `head` of your HTML file:

```
<script src="https://js.stripe.com/v3/"></script>
```

Create a placeholder element on your page where you want to mount the messaging
Element:

```
<div id="afterpay-clearpay-message"></div>
```

On your product, cart, and payment pages, include the following code to create
an instance of Stripe.js and mount the messaging Element:

```
// Set your publishable key. Remember to change this to your live publishable
key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');

const elements = stripe.elements();

const options = {
 amount: 1000, // $10.00 USD
 currency: 'USD'
};

const afterpayClearpayMessageElement =
 elements.create('afterpayClearpayMessage', options);

afterpayClearpayMessageElement.mount('#afterpay-clearpay-message');
```

## Customize the message

There are many options available to customize the appearance and contents of the
messaging Element. See the [API
reference](https://docs.stripe.com/js/elements_object/create_element?type=afterpayClearpayMessage)
for the full list of options.

#### Badge logo

Set `logoType` to `'badge'` and use the `badgeTheme` option to choose between
the following styles:

black-on-mintblack-on-whitemint-on-blackwhite-on-black
or 4 interest-free payments of $7.50 withAfterpay
[ⓘ](https://static.afterpay.com/modal/en_US.html)

or 4 interest-free payments of $7.50 withAfterpay
[ⓘ](https://static.afterpay.com/modal/en_US.html)

or 4 interest-free payments of $7.50 withAfterpay
[ⓘ](https://static.afterpay.com/modal/en_US.html)

or 4 interest-free payments of $7.50 withAfterpay
[ⓘ](https://static.afterpay.com/modal/en_US.html)

#### Lockup logo

Set `logoType` to `'lockup'` and use the `lockupTheme` option to choose between
the following styles:

blackwhitemint
or 4 interest-free payments of $7.50 withAfterpay
[ⓘ](https://static.afterpay.com/modal/en_US.html)

or 4 interest-free payments of $7.50 withAfterpay
[ⓘ](https://static.afterpay.com/modal/en_US.html)

or 4 interest-free payments of $7.50 withAfterpay
[ⓘ](https://static.afterpay.com/modal/en_US.html)

#### Note

Clearpay branding is displayed automatically based on the `locale` option. See
[Locale and
currency](https://docs.stripe.com/payments/afterpay-clearpay/site-messaging#locale-and-currency)
for details.

### Style with CSS

In addition to the configuration options, use CSS to style the messaging to
better fit the look and feel of your site. You can customize the `font-family`,
`font-size`, and `color` of the messaging:

or 4 interest-free payments of $7.50 withAfterpay
[ⓘ](https://static.afterpay.com/modal/en_US.html)

CSS
```
.AfterpayMessage {
 font-family: monospace;
 font-size: 14px;
 color: blue;
}
```

You can also control the size of the logo by setting its `width` and `height`:

or 4 interest-free payments of $7.50 withAfterpay
[ⓘ](https://static.afterpay.com/modal/en_US.html)

CSS
```
.AfterpayMessage-logoSvg {
 width: 80px;
 height: auto;
}
```

## Handle ineligible items

You can’t use Afterpay for certain [prohibited business
categories](https://docs.stripe.com/payments/afterpay-clearpay#prohibited-business-categories).
If you sell items in these categories, you can still display the messaging
Element to clearly indicate Afterpay isn’t available.

Use the `isEligible` or `isCartEligible` options to indicate that the current
product or cart isn’t eligible:

isEligible: false
Afterpayis not available for purchasing this item
[ⓘ](https://static.afterpay.com/modal/en_US.html)

isCartEligible: false
Afterpayis not available for this purchase
[ⓘ](https://static.afterpay.com/modal/en_US.html)

Afterpay also has [default transactions
limits](https://docs.stripe.com/payments/afterpay-clearpay#collection-schedule)
for each country. When the provided `amount` exceeds these limits, the Element
automatically displays ineligible price range messaging. You can customize this
message by hiding the lower or upper limit with `showLowerLimit` and
`showUpperLimit`.

(default)
Afterpayavailable for orders between $1 - $4,000
[ⓘ](https://static.afterpay.com/modal/en_US.html)

showLowerLimit: false
Afterpayavailable for orders up to $4,000
[ⓘ](https://static.afterpay.com/modal/en_US.html)

showUpperLimit: false
Afterpayavailable for orders over $1
[ⓘ](https://static.afterpay.com/modal/en_US.html)

## Locale and currency

Afterpay and clearpay support the following locales and currencies:

Supported locales: `en-US`, `en-CA`, `en-AU`, `en-NZ`, `en-GB`

Supported currencies: `USD`, `CAD`, `AUD`, `NZD`, `GBP`

Afterpay’s messaging always the appropriate number of installments a user can
pay based on their locale and country. For more information, see [payment
collection](https://docs.stripe.com/payments/afterpay-clearpay#collection-schedule).

HTML + JSReact
Set the locale of your message by passing the `locale` option into the `options`
parameter of the [elements
group](https://docs.stripe.com/js/elements_object/create) used to create the
`afterpayClearpayMessage` Element. You can then define your `currency` by
passing it to the
[element.create](https://docs.stripe.com/js/elements_object/create_element?type=afterpayClearpayMessage)
options directly.

or 4 interest-free payments of £2.50 withClearpay
[ⓘ](https://static.afterpay.com/modal/en_GB.html)

JavaScript
```
const elements = stripe.elements({
 locale: 'en-GB'
});

const options = {
 amount: 1000, // £10.00
 currency: 'GBP'
};

const afterpayClearpayMessageElement =
 elements.create('afterpayClearpayMessage', options);

afterpayClearpayMessageElement.mount('#afterpay-clearpay-message');
```

## Links

- [Payment Method Messaging
Element](https://docs.stripe.com/payments/payment-method-messaging)
-
[afterpayClearpayMessage](https://docs.stripe.com/js/elements_object/create_element?type=afterpayClearpayMessage)
- [ⓘ](https://static.afterpay.com/modal/en_US.html)
- [https://js.stripe.com/v3/](https://js.stripe.com/v3/)
- [https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)
- [prohibited business
categories](https://docs.stripe.com/payments/afterpay-clearpay#prohibited-business-categories)
- [default transactions
limits](https://docs.stripe.com/payments/afterpay-clearpay#collection-schedule)
- [elements group](https://docs.stripe.com/js/elements_object/create)
- [ⓘ](https://static.afterpay.com/modal/en_GB.html)