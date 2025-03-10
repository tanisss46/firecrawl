# Collect on-reader tips

With on-reader tipping, you can display suggested tip amounts on the reader
before the customer presents their payment method. The reader shows the customer
three suggestions based on the [tipping
option](https://docs.stripe.com/terminal/features/collecting-tips/on-reader#customize-tips-reader)
that you set up. The reader automatically shows a tipping selection screen on
every call to collect a payment. When you [confirm the
payment](https://docs.stripe.com/terminal/payments/collect-card-payment#confirm-payment),
the `PaymentIntent` is confirmed for an amount inclusive of the selected tip.

Payment screen

Tipping selection screen (percentage)

Total screen

Approved screen

### Availability

**Readers**: [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700), [BBPOS
WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e), [BBPOS
WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3)

## Enable and customize on-reader tipping

Use a [Configuration](https://docs.stripe.com/api/terminal/configuration) object
to set the tipping configuration for your reader:

- Suggest smart tips—The reader dynamically shows three percentages or amounts,
depending on the size of the pre-tip amount.
- Suggest percentages—The reader displays three percentage-based tip amounts.
- Suggest amounts—The reader displays three tip amounts.

To use the on-reader tipping feature on your BBPOS WisePad 3, you must use one
of the following Terminal SDK versions:

- Android SDK 2.8.1 or greater
- iOS SDK 2.16.1 or greater
Suggest smart tipsSuggest percentagesSuggest amounts
You can suggest three tip percentages or three tip amounts on the reader. The
reader dynamically displays either of these smart tips, depending on a pre-tip
amount threshold. Create or update a `Configuration` object as follows. The tips
you collect with on-reader tipping are post-tax tips.

```
curl https://api.stripe.com/v1/terminal/configurations \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "tipping[usd][percentages][]"=15 \
 -d "tipping[usd][percentages][]"=20 \
 -d "tipping[usd][percentages][]"=25 \
 -d "tipping[usd][fixed_amounts][]"=100 \
 -d "tipping[usd][fixed_amounts][]"=200 \
 -d "tipping[usd][fixed_amounts][]"=300 \
 -d "tipping[usd][smart_tip_threshold]"=1000
```

With the above example, the reader dynamically chooses what to suggest:

- If the pre-tip amount is below the `smart_tip_threshold` (10 USD), the reader
shows three buttons suggesting $1, $2, or $3 tips from top to bottom.
- If the pre-tip amount is at the `smart_tip_threshold` (10 USD) or above, the
reader shows three buttons suggesting tips that are 15%, 20%, or 25% of the
pre-tip total from top to bottom.

If specifying more than one currency in your `Configuration` object, you must
provide the same configuration keys for each currency. In other words, if you
only specify `percentages` for `USD`, you can’t specify `fixed_amounts` or
`smart_tip_threshold` for any other currencies.

After you create a `Configuration` object with your tipping configuration, you
can [assign the
configuration](https://docs.stripe.com/terminal/fleet/configurations-overview?dashboard-or-api=api#create-a-configuration-for-an-individual-location)
to your account or a location. BBPOS WisePad 3 readers receive new or updated
configurations when they connect to your POS application. BBPOS WisePOS E
readers can take up to 5 minutes to receive new or updated configurations.

## Collect payment

For on-reader tipping, follow the instructions for [collecting
payments](https://docs.stripe.com/terminal/payments/collect-card-payment) and
create your `PaymentIntent` with `capture_method` as `manual`.

When you [collect a payment
method](https://docs.stripe.com/terminal/payments/collect-card-payment#collect-payment),
your customer sees a tip selection screen on the reader that prompts them to
select a tip before asking for their payment method.

Depending on your [tipping
configuration](https://docs.stripe.com/terminal/features/collecting-tips/on-reader#customize-tips-reader),
the customer can choose a suggested tip, specify a custom tip, or leave no tip.

After the customer makes their selection, the reader waits for them to present a
card.

When you process the payment, the reader adds the selected tip. If the payment
is successful, the
[amount](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-amount)
in the `PaymentIntent` and `Charge` updates to include the tip amount.

Before a PaymentIntent confirmation, the tip amount returns in the `amount_tip`
field but not in the `amount`. After PaymentIntent confirmation, the
`amount_tip` field is set to zero, the `amount` includes the tip amount, and the
tip amount returns in the
[amount_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_details)
object:

Scenario[amount_details.tip.amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_details-tip-amount)
return valueOn-reader tipping is disabled`null`On-reader tipping is enabled, no
tip selected`0`On-reader tipping is enabled, tip amount selectedThe amount
selected
Customers won’t see a tipping selection screen in these cases:

- The `Configuration` object is missing a tipping configuration.
- You enabled `skipTipping` in your tipping configuration.
- The reader is in an unsupported country.
- A tipping configuration can’t be applied to the current payment currency. For
example, if the payment is in EUR but the `Configuration` object only specifies
a tipping configuration for USD.

When [testing
payments](https://docs.stripe.com/terminal/references/testing#physical-test-cards)
with the Stripe reader, the total amount (inclusive of any tip) might trigger
decline responses depending on the decimal value of the total amount.

## Skip tipping

You can ignore the tipping configuration, which allows you to hide the tip
selection screen on your reader when collecting payments.

You can hide the tip selection screen for individual transactions or temporarily
for all transactions, which allows your customers to go directly to the card
presentment screen.

For example, your restaurant might want to accept tips on the reader for takeout
orders, but only allow [on-receipt
tips](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt) for
dine-in customers.

Use one of the following options to enable bypassing the tip selection screen:

Server-drivenJavaScriptiOSAndroidReact Native
```
curl https://api.stripe.com/v1/terminal/readers/tmr_xxx/process_payment_intent \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent="<payment_intent>" \
 -d "process_config[skip_tipping]"=true
```

## Tip-eligible amounts

!

#### Note

[Contact us](mailto:stripe-terminal-betas@stripe.com) if you’re interested in
tip-eligible amounts on a [BBPOS WisePad
3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3).

When collecting a payment, you can set a tip-eligible amount that’s different
from the pre-tip amount. Setting a tip-eligible amount changes the value that
percentage-based tips are calculated from. The customer is also shown the
tip-eligible amount alongside the pre-tip amount on the tip selection screen.

You can use this setting for businesses that provide services in addition to
selling goods. For example, a salon that sells haircuts and bottles of shampoo
might want their customer to know that they calculate percentage-based tips on
haircuts only.

Server-drivenJavaScriptiOSAndroidReact Native
```
curl https://api.stripe.com/v1/terminal/readers/tmr_xxx/process_payment_intent \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d payment_intent="<payment_intent>" \
 -d "process_config[tipping][amount_eligible]"=1500
```

The above example sets a tip-eligible amount based on the currency of the
payment. For a payment in USD, the tip-eligible amount is 15 USD.

The value of `eligible_amount` must be 0 or higher. If `eligible_amount` is
equal to 0, tipping is skipped regardless of the value of `skip_tipping`. If
`eligible_amount` is equal to the PaymentIntent amount, `eligible_amount` is
ignored and the tip is calculated based on the specified amount.

#### Common mistake

Setting a tip-eligible amount that’s greater than 0 while attempting to skip
tipping results in an error.

## Links

- [tipping
option](https://docs.stripe.com/terminal/features/collecting-tips/on-reader#customize-tips-reader)
- [confirm the
payment](https://docs.stripe.com/terminal/payments/collect-card-payment#confirm-payment)
- [Stripe Reader
S700](https://docs.stripe.com/terminal/readers/stripe-reader-s700)
- [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e)
- [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3)
- [Configuration](https://docs.stripe.com/api/terminal/configuration)
- [assign the
configuration](https://docs.stripe.com/terminal/fleet/configurations-overview?dashboard-or-api=api#create-a-configuration-for-an-individual-location)
- [collecting
payments](https://docs.stripe.com/terminal/payments/collect-card-payment)
- [collect a payment
method](https://docs.stripe.com/terminal/payments/collect-card-payment#collect-payment)
-
[amount](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-amount)
-
[amount_details](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_details)
-
[amount_details.tip.amount](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-amount_details-tip-amount)
- [testing
payments](https://docs.stripe.com/terminal/references/testing#physical-test-cards)
- [on-receipt
tips](https://docs.stripe.com/terminal/features/collecting-tips/on-receipt)