# Express Dashboard

## Learn about the features of the Express Dashboard.

The Express Dashboard is a user interface that’s available to your platform’s
connected accounts. They can use the Express Dashboard to monitor their
available balance, view upcoming [payouts](https://docs.stripe.com/payouts), and
track their earnings in real time. This guide outlines the features of the
Express Dashboard and how your connected accounts can access it.

## Express Dashboard features

The Express Dashboard displays the connected account’s balance transactions and
net volume.

### Transactions list

The **Transactions** list displays a connected account’s balance transactions,
including charges, transfers, and payouts. The **Transactions** list organizes
each transaction by type, date, and amount. By default, it displays generic
descriptions of charges and transfers, such as `Payment from {YOUR PLATFORM}`.
To learn how to create custom descriptions, see [Customize the Express
Dashboard](https://docs.stripe.com/connect/customize-express-dashboard).

### Earnings chart

The **Earnings** chart displays the net volume of the account’s charges and
transfers over time. They can select different time intervals to view.

## Accessing the Express Dashboard

There are two ways to access the Express Dashboard, login links and
self-service. We recommend using login links.

### Platform login links

You can generate single-use account-specific login links that redirect connected
accounts from your platform application to the Express Dashboard login page.
They then log into the Dashboard using SMS authentication.

To learn about using login links, see [Integrate the Express Dashboard in your
platform](https://docs.stripe.com/connect/integrate-express-dashboard).

### Self-serve access

Connected accounts can access the Express Dashboard by logging into [Stripe
Express](https://connect.stripe.com/express_login) using their account email and
SMS authentication.

#### Note

Only live mode accounts can log into Stripe Express. For testing, use [login
links](https://docs.stripe.com/connect/integrate-express-dashboard).

To learn more about self-serve access, see the [Stripe Express support
article](https://support.stripe.com/express/questions/how-do-i-login-to-my-stripe-express-account).

## Supported browsers

The Express Dashboard supports the same browsers that the [full Stripe Dashboard
supports](https://docs.stripe.com/dashboard/basics). Express users must access
the Dashboard in a web browser, not in embedded web views inside mobile or
desktop applications.

## See also

- [Integrate the Express
Dashboard](https://docs.stripe.com/connect/integrate-express-dashboard)
- [Customize the Express
Dashboard](https://docs.stripe.com/connect/customize-express-dashboard)

## Links

- [configured with
properties](https://docs.stripe.com/connect/update-to-typeless-connect)
- [payouts](https://docs.stripe.com/payouts)
- [Customize the Express
Dashboard](https://docs.stripe.com/connect/customize-express-dashboard)
- [Integrate the Express Dashboard in your
platform](https://docs.stripe.com/connect/integrate-express-dashboard)
- [Stripe Express](https://connect.stripe.com/express_login)
- [Stripe Express support
article](https://support.stripe.com/express/questions/how-do-i-login-to-my-stripe-express-account)
- [full Stripe Dashboard supports](https://docs.stripe.com/dashboard/basics)