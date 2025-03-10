# Protect yourself from card testing

## Learn about this fraudulent activity and how to protect yourself against it.

Card testing is a type of fraudulent activity where someone tries to determine
whether stolen card information is valid so that they can use it to make
purchases. A fraudster might do this by purchasing stolen credit card
information, and then attempting to validate or make purchases with those cards
to determine which cards are still valid. Other common terms for card testing
are “carding”, “account testing”, “enumeration”, and “card checking.”

Fraudulent activity such as card testing is an unavoidable part of online
commerce. Card testing, however, has consequences for the entire payments
ecosystem, so merchants, card networks, and Stripe share responsibility to
prevent it. At Stripe, we’re constantly improving our tools and systems to
detect and reduce fraud, but you must remain vigilant with respect to fraud.

## How card testing works

Card testers use both card setup and payments to determine whether the stolen or
enumerated card information they have is valid or not. To quickly validate many
card numbers, fraudsters use scripts to test a large amount of card information
at once, and collect 3DS or issuer responses to validate which card information
is valid. After they have identified the valid cards, they can cash them with
merchants or resell confirmed cards on the dark web.

- **Card Setup**—This is a method preferred by fraudsters, as card validation
and authorizations during card setup don’t typically show up on cardholder
statements. This reduces the likelihood of card holders noticing and reporting
the fraudulent activity.
- **Payments**—Card testers create small amount payments, which are cardholders
are less likely to notice and reported as fraudulent.

## Card testing consequences

Card testing has many negative outcomes, some of which get worse over time as
card testing continues:

- **Disputes**— Many types of card testing involve payments, some of which
succeed. Customers notice successful payments and report them as fraud, which
result in , the

- [transactions](https://dashboard.stripe.com/payments)
- [Developers](https://dashboard.stripe.com/developers)
- [failed Logs](https://dashboard.stripe.com/logs?error_type=card_error)
- [outcome of “generic_decline”](https://docs.stripe.com/declines/codes)
- [recommended
integrations](https://docs.stripe.com/payments/online-payments#compare-features-and-availability)
- [CAPTCHA](https://www.hcaptcha.com/)
- [Stripe Support](https://support.stripe.com/contact/login)
- [from the same signals used by
Radar](https://docs.stripe.com/radar/integration)
- [Advanced fraud
detection](https://docs.stripe.com/disputes/prevention/advanced-fraud-detection)
- [the safeguards that protect against cross-site request forgery (CSRF)
attacks](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [detect and prevent unusual
behavior](https://docs.stripe.com/disputes/prevention/card-testing#prevent-unusual-behavior)
- [webhooks](https://docs.stripe.com/webhooks)
- [Stripe Sigma or Data
Pipelines](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)
- [custom rules](https://docs.stripe.com/radar/rules/reference#velocity-rules)
- [Smart
Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries#non-retryable-decline-codes)
- [bank checks](https://docs.stripe.com/radar/rules#traditional-bank-checks)
- [CVC](https://docs.stripe.com/disputes/prevention/verification)
- [Radar 101
guide](https://stripe.com/guides/radar-rules-101#rules-that-help-prevent-card-testing-or-card-cashing)
- [Keeping your keys safe](https://docs.stripe.com/keys#safe-keys)
- [Radar 101 guide](https://stripe.com/guides/radar-rules-101)