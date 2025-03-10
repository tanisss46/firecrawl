# Issuing balance

## Learn how to make funds available to your cards.

To spend money using cards, add funds to the Issuing balance on your account.
This balance represents funds reserved for Issuing and is safely separated from
your earnings, payouts, and funds from other Stripe products.

Push fundingFunding from Stripe BalancePull funding (US-only)
Using the Stripe Dashboard or API, you can access the bank account and routing
information you need to push funds from your external bank account. When that
account receives funds, they’re immediately available as a
[top-up](https://docs.stripe.com/api/topups) to your Stripe account’s Issuing
balance.

For a given currency, the provided bank account information will be unique and
able to receive funds any number of times. Funds always arrive in your Issuing
balance in the specified currency. In some cases, your bank might perform
currency conversion.

RegionPayment SchemeCurrency SupportedSpeedMaximum amount acceptedUnited
StatesBeta Wire Transfer from US banks onlyUSDA few minutes to 1 business
dayVaries by bank, usually many millionsACH Credit TransferUSDSeveral hours to
several business daysVaries by bank, usually less than $25kEuro area SEPA Credit
TransferEURAbout a day€999,999,999.99United Kingdom FPSGBPAbout 2 hours during a
bank’s business hours, or at the start of the next banking day.£1
millionBACSGBP2-3 business days£20 million
Select region:

United States (beta)Euro areaUnited Kingdom
## Access account information for push funding in the Dashboard

To access account information for push funding:

- Navigate to the [Balances page](https://dashboard.stripe.com/balance/overview)
in the Dashboard.
- Scroll down to the **Issuing balance** heading and click **Add to balance**.
- Choose your **Issuing balance** and specify how much to add. Click **Next**.
- Select **Wire transfer** from the dropdown, and expand **Show instructions**
to see the information you need to send a wire.

To send a wire from your bank, use the routing and account number, along with
the beneficiary information.

Wires from banks outside the US aren’t allowed. Funds received from an
international wire are returned to the sender’s bank account, which can take up
to 3 business days.

### Request early access

Access to US push funding is currently limited to US beta users. You must be an
Issuing customer to join the beta. To request access to the beta, log in to your
Stripe account and refresh the page. [Contact
Stripe](https://stripe.com/contact/sales) for more information.

## Enable notifications about your balance

You can enable email notifications to help monitor your Issuing balance from
your settings. To configure these notifications:

- Visit your Balance notifications
[settings](https://dashboard.stripe.com/settings/issuing/balance-notifications)
page.
- Choose from two types of alerting thresholds:- Fixed amount: Receive an alert
whenever your Issuing balance falls below this amount.
- Ratio of balance to rolling spend: Receive an alert whenever the ratio of your
Issuing balance to your spend over the previous 24 hours falls below the
threshold. For example, if you set your threshold to 80% and your spend over the
past day is 100 USD, you receive an alert whenever your balance falls below 80
USD.

## Links

- [top-up](https://docs.stripe.com/api/topups)
- [Balances page](https://dashboard.stripe.com/balance/overview)
- [Contact Stripe](https://stripe.com/contact/sales)
-
[settings](https://dashboard.stripe.com/settings/issuing/balance-notifications)