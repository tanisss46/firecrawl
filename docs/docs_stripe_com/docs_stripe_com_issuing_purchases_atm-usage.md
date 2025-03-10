# Use cards at automated teller machines (ATMs)

## Learn how you can use your Stripe Issuing cards at ATMs.

Stripe allows you to use your cards at ATMs for cash withdrawals if you enable
the feature for your account, and if you’ve set up valid PINs for them.

## Enable ATM withdrawals

ATM withdrawals aren’t enabled by default, so you need to request approval for
your use case [through support](https://support.stripe.com/?contact=true). In
addition, make sure all your relevant cards have PINs set up by following our
[PIN management guide](https://docs.stripe.com/issuing/cards/pin-management).

## Treatment of ATM transactions

Stripe Issuing treats ATM withdrawals as standard transactions, but a few
characteristics of the authorization signal that it’s an ATM withdrawal:

- The [merchant category
code](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-category_code)
is set to 6011—`Automated Cash Disburse`.
- An ATM [fee
value](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-amount_details-atm_fee)
might be present.
- The [PIN
check](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-verification_data-pin_check)
is a `match`.

You can approve or decline them using the same [webhook
integration](https://docs.stripe.com/issuing/controls/real-time-authorizations)
as other authorizations.

## Restrictions

- **Limits**: ATM withdrawals are subject to a daily maximum limit. Your support
representative can share your limit with you and work to increase it if it’s not
sufficient for your use case.
- **Cash Deposits**: Stripe-issued cards aren’t enrolled in any ATM cash deposit
programs and don’t have the ability to accept cash deposits. Cash
deposit-enabled ATMs won’t trigger prompts for deposits when a Stripe-issued
card is used.

## Availability

Users in the US can [contact support](https://support.stripe.com/?contact=true)
to request ATM cash withdrawals on issued cards. Withdrawals are not yet
available in the UK or EU, but users can [contact
support](https://support.stripe.com/?contact=true) for more information about
future availability in these regions.

## Fees

Stripe does not assess any fees of its own for ATM withdrawals, but ATM
operators often do. These fees are generally:

- **ATM use surcharge**: Added to the total transaction amount (this is the [atm
fee](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-amount_details-atm_fee)
amount a cardholder sees at the ATM.)
- **Dynamic Currency Conversion (DCC)**: When the cardholder is given the option
between a local currency and the card’s default currency (for example, using a
US issued card in the EU), ATMs generally apply a markup on conversion rates
when a cardholder picks the card’s default currency. While this isn’t an
explicit fee, the conversion rates functionally behave as a tax on ATM
transactions.

Neither the ATM provider nor Stripe apply any cash advance fees or annual
percentage rate (APR) to an ATM withdrawal.

Different markets have different ATM rules and fee structures that influence the
frequency and intensity of the fees charged, but the way we describe the fees
above generally applies regardless of the country. If an ATM charges a fee to a
cardholder, we’ll pass it on as part of the amount for a given authorization.
Otherwise, cardholders and issuing users won’t see any impact.

## Links

- [through support](https://support.stripe.com/?contact=true)
- [PIN management guide](https://docs.stripe.com/issuing/cards/pin-management)
- [merchant category
code](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-merchant_data-category_code)
- [fee
value](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-amount_details-atm_fee)
- [PIN
check](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-verification_data-pin_check)
- [webhook
integration](https://docs.stripe.com/issuing/controls/real-time-authorizations)