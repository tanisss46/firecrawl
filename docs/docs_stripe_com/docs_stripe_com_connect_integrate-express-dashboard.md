# Integrate the Express Dashboard in your platform

## Learn how to direct your connected accounts to their Express Dashboard using login links.

The Express Dashboard allows connected accounts to view their available balance,
see upcoming [payouts](https://docs.stripe.com/payouts), and track their
earnings in real time. This guide shows how to implement login links that
redirect connected accounts from your platform to their Express Dashboards.

Your live mode connected accounts can also access the Express Dashboard by
[logging into Stripe
Express](https://docs.stripe.com/connect/express-dashboard#self-serve-access).
However, you can provide login links from your platform to facilitate the log in
process.

[Create a login
link](https://docs.stripe.com/connect/integrate-express-dashboard#create-login-link)
Use the [Login Link](https://docs.stripe.com/api/account/create_login_link) API
to generate a URL for an account-specific Express Dashboard login page.

```
curl -X POST
https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}}/login_links \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:"
```

A successful response returns the generated login link URL:

```
{
 "object": "login_link",
 "created": 1495580507,
 "url": "https://stripe.com/express/Ln7FfnNpUcCU"
}
```

[Redirect to the login
link](https://docs.stripe.com/connect/integrate-express-dashboard#redirect-to-login-link)
Typically, you generate a login link URL on demand when a connected account
intends to visit the Express Dashboard. For example, you include an **Open
Dashboard** button in your application. When a connected account user clicks it,
your application calls the API to generate a login link and redirects them to
that URL.

#### Security tip

Don’t email, text, or otherwise send login link URLs outside of your platform.
Redirect authenticated users to it only from within your platform application.

When you redirect a connected account user to a login link, Stripe sends an SMS
authentication code to their phone number. They verify their identity on the
Express Dashboard login page by entering the code.

If they don’t have access to their account phone number, they can change it by
clicking **I no longer have access to this phone number**. This sends a
verification code to their account email. They can change the account phone
number by entering the code. If the user changes the number, Stripe redirects
them to the Express Dashboard login page and sends an SMS authentication code to
the new number.

## See also

- [Customize the Express
Dashboard](https://docs.stripe.com/connect/customize-express-dashboard)
- [Collect payments and then pay
out](https://docs.stripe.com/connect/collect-then-transfer-guide) (if you
process payments with Stripe)
- [Pay out money](https://docs.stripe.com/connect/add-and-pay-out-guide) (if you
add money from a bank account to pay out)

## Links

- [payouts](https://docs.stripe.com/payouts)
- [logging into Stripe
Express](https://docs.stripe.com/connect/express-dashboard#self-serve-access)
- [Login Link](https://docs.stripe.com/api/account/create_login_link)
- [Customize the Express
Dashboard](https://docs.stripe.com/connect/customize-express-dashboard)
- [Collect payments and then pay
out](https://docs.stripe.com/connect/collect-then-transfer-guide)
- [Pay out money](https://docs.stripe.com/connect/add-and-pay-out-guide)