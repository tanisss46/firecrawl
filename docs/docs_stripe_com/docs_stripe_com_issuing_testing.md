# Testing Issuing

## Learn how to test your integration and simulate purchases.

You can issue cards and simulate purchases using your own Stripe integration in
test mode. This allows you to test your integration before you go live without
having to make real purchases. You can only use these cards for testing within
your Stripe account and not for external purchases.

#### Caution

When testing your [authorization
endpoint](https://docs.stripe.com/issuing/purchases/authorizations), make sure
that you have set the endpoint for test mode in your [Issuing
settings](https://dashboard.stripe.com/account/issuing). Toggle **View test
data** to switch between test and live mode data and settings.

## Fund your test mode Issuing balance

Before you create test mode transactions, you must add test mode funds to the
Issuing balance on your account. These aren’t real funds, and you can only use
them for simulating purchases in test mode.

### Issuing users in the US

Issuing users in the US use “pull” funding, and use *Top-ups* to fund their
Issuing balance. You can create test mode top-ups in the Dashboard, or with the
[Top-ups API](https://docs.stripe.com/api/topups/create). Learn more about
funding Issuing balances for [US
users](https://docs.stripe.com/issuing/funding/balance?push-pull-preference=pull).

### Issuing users in the UK and euro area

To top up their balance, Issuing users in the UK and Europe “push” funds using
*Funding Instructions*. You can do this in the test mode Dashboard, or with the
[Funding Instructions API](https://docs.stripe.com/api/funding_instructions).
Learn more about funding Issuing balances for [UK and euro area
users](https://docs.stripe.com/issuing/funding/balance?push-pull-preference=push).

Without codeWith code
You can simulate a card purchase by specifying authorization details in the
Dashboard.

[Create a
cardDashboard](https://docs.stripe.com/issuing/testing#without-code-create-card)
Use the [API](https://docs.stripe.com/api/issuing/cards) or the
[Dashboard](https://dashboard.stripe.com/issuing/cards) to create a cardholder
and card in test mode.

[Create a test
purchaseDashboard](https://docs.stripe.com/issuing/testing#without-code-create-test-purchase)
Navigate to the [Issuing Cards page](https://dashboard.stripe.com/issuing/cards)
in test mode, find your newly-created card, then click **Create test purchase**.

You can select to create either an
[Authorization](https://docs.stripe.com/api/issuing/authorizations/object) or
[Transaction](https://docs.stripe.com/api/issuing/transactions/object) by force
capture.

Depending on your selection, you can provide a number of properties, such as
amount, business data, and so on.

Click **Submit** to create the purchase. If you selected authorization and have
configured your [synchronous
webhook](https://docs.stripe.com/issuing/controls/real-time-authorizations), you
can use it to approve or decline the authorization. The browser redirects to the
page for the newly-created authorization.

[Create a
captureDashboard](https://docs.stripe.com/issuing/testing#without-code-create-test-capture)
To create a test capture with an authorization in the Dashboard, enter test mode
and complete the following steps:

- Navigate to the
[Authorizations](https://dashboard.stripe.com/issuing/authorizations) page under
**Issued Cards**.
- Click the authorization you want to capture, then click **Capture**.

You can capture an authorization for an amount that’s lesser, greater, or
equivalent to the authorized total. You can also [capture multiple
times](https://docs.stripe.com/issuing/purchases/transactions?issuing-capture-type=multi_capture)
regardless of the authorization’s current state.

Enter the amount you want to capture, then click **Submit** to create the
capture. The browser redirects you to the Transactions page and selects the
newly created transaction.

## Links

- [testing](https://docs.stripe.com/testing)
- [authorization
endpoint](https://docs.stripe.com/issuing/purchases/authorizations)
- [Issuing settings](https://dashboard.stripe.com/account/issuing)
- [Top-ups API](https://docs.stripe.com/api/topups/create)
- [US
users](https://docs.stripe.com/issuing/funding/balance?push-pull-preference=pull)
- [Funding Instructions API](https://docs.stripe.com/api/funding_instructions)
- [UK and euro area
users](https://docs.stripe.com/issuing/funding/balance?push-pull-preference=push)
- [API](https://docs.stripe.com/api/issuing/cards)
- [Dashboard](https://dashboard.stripe.com/issuing/cards)
- [Authorization](https://docs.stripe.com/api/issuing/authorizations/object)
- [Transaction](https://docs.stripe.com/api/issuing/transactions/object)
- [synchronous
webhook](https://docs.stripe.com/issuing/controls/real-time-authorizations)
- [Authorizations](https://dashboard.stripe.com/issuing/authorizations)
- [capture multiple
times](https://docs.stripe.com/issuing/purchases/transactions?issuing-capture-type=multi_capture)