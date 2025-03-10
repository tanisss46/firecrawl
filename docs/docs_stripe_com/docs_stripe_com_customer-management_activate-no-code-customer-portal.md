# Activate the no-code customer portal

## Set up Stripe's customer portal with a no-code configuration.

First, you need a Stripe account. [Register
now](https://dashboard.stripe.com/register/).

Activate a link that you add to your website or share with your customers,
allowing them to self-manage their payment details, invoices, and subscriptions.
We’ll also add the link to your customer emails. You can set up the customer
portal in a few minutes, without writing any code.

See how your customers can log in with the portal login link

[Set up the customer
portal](https://docs.stripe.com/customer-management/activate-no-code-customer-portal#set-up-customer-portal)-
**Activate a customer portal link** On the [customer portal
configuration](https://dashboard.stripe.com/settings/billing/portal) page, click
**Activate link** in the **Ways to get started** section.
- **Configure the portal** Go to the [customer portal
configuration](https://dashboard.stripe.com/settings/billing/portal) page and
select your configuration options. Learn more about [configuration
options](https://docs.stripe.com/customer-management/configure-portal).
- **Share the portal login link** Add the link you activated to your site, or
send it directly to your customers. They can log in to the portal with their
email address and a one-time passcode.

Make sure your customers have an
[email](https://docs.stripe.com/api/customers/object#customer_object-email) set.
If multiple customers have the same email address, Stripe selects the most
recently created customer that has both that email and an active subscription.

For security purposes:

- Customers can’t update their email address through this link.
- If a customer doesn’t receive a one-time passcode after clicking the login
link, make sure their email address matches the email address of an existing
customer. To check, enter the email address in the search bar of your [Stripe
dashboard](https://dashboard.stripe.com/).
[OptionalCustomize
branding](https://docs.stripe.com/customer-management/activate-no-code-customer-portal#branding)[OptionalPrefill
customer
email](https://docs.stripe.com/customer-management/activate-no-code-customer-portal#url-parameters)

## Links

- [Register now](https://dashboard.stripe.com/register/)
- [customer portal
configuration](https://dashboard.stripe.com/settings/billing/portal)
- [configuration
options](https://docs.stripe.com/customer-management/configure-portal)
- [email](https://docs.stripe.com/api/customers/object#customer_object-email)
- [Stripe dashboard](https://dashboard.stripe.com/)