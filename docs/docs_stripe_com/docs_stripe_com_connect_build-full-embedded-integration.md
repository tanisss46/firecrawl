# Fully embedded Connect platform integration

## Provide Connect features to your connected accounts through your own website.

Connect embedded components let you add Stripe-managed functionality to a custom
interface that you provide to your connected accounts. They can perform
payment-related activities there instead of through the Stripe Dashboard. In a
fully embedded integration:

- Connected accounts access Stripe-related data, forms, and notifications
through embedded components in your platform’s application. They don’t have
access to a Stripe Dashboard.
- Stripe manages credit and fraud risk on your connected accounts. For any risk
or compliance actions, we communicate directly with connected accounts and they
respond by interacting with embedded components.
- Stripe email notifications direct your connected accounts to embedded
components on your website to review information or take required action. You
must provide Stripe with the URLs for those components.

## View the demo site

We’ve built a complete [demo site for our fictitious business,
Furever](http://furever.dev/). Furever is a platform providing software for
pet-groomers that allows their users to collect payments. In this demo, you can
interact with many embedded components, including account onboarding and account
management.

## Before you begin

Before you can build an embedded integration, complete the following
prerequisites:

- [Register your platform](https://dashboard.stripe.com/connect/set-up).
- Add business details to [activate your
account](https://dashboard.stripe.com/account/onboarding).
- [Complete your platform
profile](https://dashboard.stripe.com/connect/settings/profile).
- [Customize your brand
settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding).
Add a business name, icon, and brand color.

You must also decide whether your platform will own pricing, in which case
Stripe collects payment fees from your platform and you bill your connected
accounts. Otherwise, Stripe owns pricing and collects payment fees directly from
your connected accounts.

[Create a connected
account](https://docs.stripe.com/connect/build-full-embedded-integration#create-a-connected-account)
The following example creates an account where Stripe [manages
risk](https://docs.stripe.com/connect/risk-management), controls pricing, and
assumes responsibility for account onboarding requirements. Your platform uses
embedded components and isn’t liable for negative balances. Your connected
accounts don’t have access to Stripe-hosted dashboards.

#### Note

Because Stripe controls pricing in this example, you must integrate the
Documents embedded component. In addition, Stripe notifies connected accounts by
email when their tax invoices or 1099s are ready for download. If you create
accounts where your platform controls pricing, the Documents component isn’t
required, and Stripe doesn’t send notifications to connected accounts about tax
invoices or 1099s.

You can request additional capabilities, such as specific payment methods, after
the account onboards.

Call [/v1/accounts](https://docs.stripe.com/api/accounts/create) with the
following parameters:

- `country` of the account
- `controller.stripe_dashboard.type` = `none`
- request the `card_payments` and `transfers` capabilities

```
curl https://api.stripe.com/v1/accounts \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d country=US \
 -d "controller[stripe_dashboard][type]"=none \
 -d "capabilities[card_payments][requested]"=true \
 -d "capabilities[transfers][requested]"=true
```

```
{
 "id": "{{CONNECTED_ACCOUNT_ID}}",
 "object": "account",
 "controller": {
 "type": "application",
 "is_controller": true,
 "losses": {"payments": "stripe"},
 "fees": {"payer": "account"},
 "requirement_collection": "stripe",
 "stripe_dashboard": {
 "type": "none",
 },
 },
 "type": "none",
 ...
}
```

[Set up embedded
components](https://docs.stripe.com/connect/build-full-embedded-integration#setup-embedded-components)
Connected accounts access their accounts, as well as core payments
functionality, directly in your platform and don’t have access to a
Stripe-hosted Dashboard, so you must provide access through your site.

Your integration must include the following embedded components:

- Account onboarding component
- Account management component
- Notification banner component
- Documents component (when Stripe collects Stripe fees directly from connected
accounts)

For any other [optional
components](https://docs.stripe.com/connect/supported-embedded-components), you
can use our embedded components or build your own UI.

Make sure you [set up embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
before onboarding connected accounts.

[Onboard connected
accounts](https://docs.stripe.com/connect/build-full-embedded-integration#onboard-connected-accounts)
Stripe uses an [Account Session](https://docs.stripe.com/api/account_sessions)
to express your intent to provide embedded component access to the connected
account. Using an Account Session, the embedded account onboarding component
collects all required information based on your requested capabilities.

### Prefill the account

The embedded account onboarding component collects all required information
based on your requested capabilities.

You can streamline the onboarding flow for your users by prefilling account
fields with known information before you create an Account Session. Prefill as
much account information as possible, including company, individual, and
external account information, following these steps:

- Review the [required verification
information](https://docs.stripe.com/connect/required-verification-information)
docs to learn more about how the combination of countries and capabilities you
select for connected accounts affects their requirements.
- To determine the information that Stripe requires from a connected account,
retrieve the account’s
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
property.
- Collect prefillable information.
- Record the information on the account by calling [Update
Account](https://docs.stripe.com/api/accounts/update).

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d business_type=individual \
 --data-urlencode email="jenny.rosen@example.com" \
 -d "individual[first_name]"=Jenny \
 -d "individual[last_name]"=Rosen \
 --data-urlencode "individual[email]"="jenny.rosen@example.com" \
 -d "individual[address][line1]"="354 Oyster Point Blvd" \
 -d "individual[address][city]"="South San Francisco" \
 -d "individual[address][state]"=CA \
 -d "individual[address][postal_code]"=94080 \
 -d external_account={{BANK_ACCOUNT_TOKEN_ID}}
```

After the connected account completes onboarding through the Account Onboarding
embedded component, your platform can no longer update certain information such
as payout accounts or legal entity information. The connected account must make
any updates to that information because the platform isn’t responsible for
negative balances.

### Onboard users through the embedded onboarding component

Connected accounts must go through onboarding and provide required information
to enable charges and payouts. To onboard a connected account, host the
[onboarding embedded
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
on your site and direct new accounts there.

### Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/connect/get-started-connect-embedded-components),
enable account management by specifying `account_onboarding` in the `components`
parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[account_onboarding][enabled]"=true \
-d "components[account_onboarding][features][external_account_collection]"=true
```

After creating the Account Session and initializing ConnectJS, you can render
the Account onboarding component in the front end:

```
// Include this element in your HTML
const accountOnboarding = stripeConnectInstance.create('account-onboarding');
accountOnboarding.setOnExit(() => {
 console.log('User exited the onboarding flow');
});
container.appendChild(accountOnboarding);
```

Present the onboarding flow to the account’s primary owner. The primary owner
sets up authentication with Stripe, and is the user who can edit the account
details and respond to risk interventions. The connected account has only a
single set of authentication credentials with Stripe. The user with
authentication credentials can authenticate using one-time SMS codes to perform
more sensitive actions like updating bank accounts for payout destinations or
providing updated legal entity information.

### Listen for onboarding events

As the account proceeds through onboarding,
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
events are also sent to your configured [Connect
webhooks](https://docs.stripe.com/connect/webhooks). When the account finishes
submitting their details, the `details_submitted` field on the Account changes
to true. Check the status by looking for `details_submitted: true` in the
`account.updated` event body in your webhook handler or by [retrieving the
Account](https://docs.stripe.com/api/account/retrieve). If `details_submitted`
is false, show the embedded onboarding component again. If the account submitted
some information, the embedded onboarding component skips it and only collects
the unsubmitted requirements.

When a connected account submits their details and completes the onboarding
flow, the embedded onboarding component calls the `onExit` handler that you [set
when you render the
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding).
Use the callback to direct the account to their next action. If you don’t set an
exit handler, or take action inside of the handler, the account sees a
completion message without a clear next step.

### Request additional capabilities (optional)

Your platform can continue to request additional
[capabilities](https://docs.stripe.com/connect/account-capabilities) after
onboarding a connected account. For example, you must request the capabilities
for any payment methods you want to enable for an account.

```
curl https://api.stripe.com/v1/accounts/{{CONNECTED_ACCOUNT_ID}} \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d "capabilities[bancontact_payments][requested]"=true \
 -d "capabilities[eps_payments][requested]"=true \
 -d "capabilities[ideal_payments][requested]"=true \
 -d "capabilities[p24_payments][requested]"=true \
 -d "capabilities[sepa_debit_payments][requested]"=true
```

If any requested capabilities require additional information, the connected
account receives a notification through the [embedded notification
banner](https://docs.stripe.com/connect/build-full-embedded-integration#embed-the-notification-banner).

[Handle ongoing compliance and risk
updates](https://docs.stripe.com/connect/build-full-embedded-integration#handle-compliance-and-risk-updates)
Because Stripe manages credit and fraud risk for your connected accounts, your
accounts must be able to see and respond to alerts from Stripe. To facilitate
that, your platform must integrate the notification banner and account
management embedded components. For more information about how Stripe supports
your connected accounts through these components, see [Embedded Connect
support](https://docs.stripe.com/connect/embedded-support).

## Embed the notification banner

Stripe uses the [notification banner embedded
component](https://docs.stripe.com/connect/supported-embedded-components/notification-banner)
to notify connected accounts of outstanding compliance requirements and other
[risk-related requests](https://docs.stripe.com/connect/embedded-risk).
Responding to these notifications allows an account to remain compliant so it
can process payments and receive payouts. If there are no outstanding
notifications, the embedded notification banner doesn’t render.

Integrate the notification banner in a highly visible and easily accessible
location on your website. For example, you can integrate it at the top of your
payments page.

### Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable
notification banner by specifying `notification_banner` in the `components`
parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[notification_banner][enabled]"=true \
-d "components[notification_banner][features][external_account_collection]"=true
```

### Render the notification banner component

```
// Include this element in your HTML
const notificationBanner = stripeConnectInstance.create('notification-banner');
container.appendChild(notificationBanner);

// Optional:
// notificationBanner.setCollectionOptions({
// fields: 'eventually_due',
// futureRequirements: 'include',
// })
```

To respond to a banner notification, the account can click a button in the
notification. You don’t need to redirect them to the account management embedded
component.

## Embed account management

Stripe requires the [account management embedded
component](https://docs.stripe.com/connect/supported-embedded-components/account-management)
when managing risk. Integrate the component in your website where an account
updates their settings or profile.

### Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable account
management by specifying `account_management` in the `components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[account_management][enabled]"=true \
-d "components[account_management][features][external_account_collection]"=true
```

### Render the account management component

```
// Include this element in your HTML
const accountManagement = stripeConnectInstance.create('account-management');
container.appendChild(accountManagement);

// Optional:
// accountManagement.setCollectionOptions({
// fields: 'eventually_due',
// futureRequirements: 'include',
// })
```

This component allows an account to update their account details, respond to
compliance requirements that are due, and update their authentication
credentials.

[Integrate
payments](https://docs.stripe.com/connect/build-full-embedded-integration#integrate-payments)
Set up the payments integration after integrating required embedded components.
You can add the payments and payout embedded components to your platform or
build your own workflows.

Configure [Connect webhooks](https://docs.stripe.com/connect/webhooks) and
listen for the `account.updated` event. A connected account is ready to receive
payments when its `charges_enabled` property is true.

## Integrate embedded payments and payouts

Add the
[payments](https://docs.stripe.com/connect/supported-embedded-components/payments)
and
[payouts](https://docs.stripe.com/connect/supported-embedded-components/payouts)
embedded components to your platform *before* building your payments
integration. That way, an account can easily access and manage their core
payment workflows.

The payments component shows a list of the connected account’s payments, and
includes filtering and individual payment detail views. An account can issue
refunds and respond to disputes with evidence on individual payments through
this component.

### Create an Account Session

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
payments embedded component by specifying `payments` in the `components`
parameter. You can turn on or off an individual feature of the payments
component by specifying the `features` parameter under `payments`:

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[payments][enabled]"=true \
 -d "components[payments][features][refund_management]"=true \
 -d "components[payments][features][dispute_management]"=true \
 -d "components[payments][features][capture_payments]"=true \
-d
"components[payments][features][destination_on_behalf_of_charge_management]"=false
```

Your connected accounts can view the complete set of information about direct
charges. They can also manage refunds, manage disputes, and capture payments if
you enable the corresponding features when creating an account session.

### Render the payments component

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the payments component in the front end:

```
// Include this element in your HTML
const payments = stripeConnectInstance.create('payments');
container.appendChild(payments);

// Optional: specify filters to apply on load
// payments.setDefaultFilters({
// amount: {greaterThan: 100},
// date: {before: new Date(2024, 0, 1)},
// status: ['partially_refunded', 'refund_pending', 'refunded'],
// paymentMethod: 'card',});
```

The payouts component shows the connected account’s recent payouts, current
balance, and when funds will become available.

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
payouts embedded component by specifying `payouts` in the `components`
parameter. You can enable or disable individual features of the payouts
component by specifying the `features` parameter under `payouts`:

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[payouts][enabled]"=true \
 -d "components[payouts][features][instant_payouts]"=true \
 -d "components[payouts][features][standard_payouts]"=true \
 -d "components[payouts][features][edit_payout_schedule]"=true \
 -d "components[payouts][features][external_account_collection]"=true
```

After creating the account session and [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions),
you can render the payouts component in the front end:

```
// Include this element in your HTML
const payouts = stripeConnectInstance.create('payouts');
container.appendChild(payouts);
```

For an immersive guide to implementing embedded components, follow the [Connect
embedded components integration
quickstart](https://docs.stripe.com/connect/connect-embedded-components/quickstart).

## Accept a payment

If your connected accounts transact directly with customers, use [direct
charges](https://docs.stripe.com/connect/direct-charges).

Stripe assesses payment transaction fees to your platform when
`controller.fees.payer` is not set to `account` for the
[Account](https://docs.stripe.com/api/accounts/object). In turn, you’re
responsible for charging payment processing fees on your connected accounts. You
can specify a value for the [application
fee](https://docs.stripe.com/connect/direct-charges#collect-fees) on each
payment to automatically take fees from connected accounts without having to
build it into your integration.

CustomerConnected account
10 USD charge

0.59 USD application fee

BankPlatformBankStripeDirect charge$9.41 net($0.23) Stripe0.36 USD net
We recommend using [Stripe Checkout](https://docs.stripe.com/payments/checkout),
a prebuilt Stripe-hosted page, to accept payments. Checkout supports multiple
payment methods and automatically shows the most relevant ones to your customer.

You can also use the [Payment
Element](https://docs.stripe.com/payments/payment-element), a prebuilt UI
component you can embed to accept additional payment methods with a single
integration.

CheckoutPayment Element
### Create a Checkout Session Client-side Server-side

A Checkout Session controls what a customer sees in the Stripe-hosted payment
page such as line items, the order amount and currency, and acceptable payment
methods. When performing direct charges, Checkout uses the connected account’s
branding settings. For more information, see [Customize
branding](https://docs.stripe.com/connect/direct-charges?platform=web&ui=stripe-hosted#branding).

Unlike destination charges or separate charges and transfers, connected accounts
are responsible for handling disputes on direct charges—it’s not the
responsibility of the platform.

To create a Checkout Session, add a checkout button to your website that calls a
server-side endpoint.

```
<html>
 <head>
 <title>Checkout</title>
 </head>
 <body>
 <form action="/create-checkout-session" method="POST">
 <button type="submit">Pay</button>
 </form>
 </body>
</html>
```

On your server, make the following call to the Stripe API. After creating a
Checkout Session, redirect your customer to the
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
returned in the response.

```
curl https://api.stripe.com/v1/checkout/sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
 -d mode=payment \
 -d "line_items[0][price]"={{PRICE_ID}} \
 -d "line_items[0][quantity]"=1 \
 -d "payment_intent_data[application_fee_amount]"=123 \
 --data-urlencode success_url="https://example.com/success" \
 --data-urlencode cancel_url="https://example.com/cancel"
```

- `line_items`—This parameter represents items that your customer is purchasing
and that show up in the hosted user interface.
- `success_url`—This argument redirects a customer after they complete a
payment.
- `cancel_url`—This argument redirects a customer after they click **cancel**.
- `Stripe-Account`—This header indicates a [direct
charge](https://docs.stripe.com/connect/direct-charges) for your connected
account. With direct charges, the connected account is responsible for Stripe
fees, refunds, and chargebacks. Checkout uses the connected account’s branding,
which allows their customers to feel like they’re interacting directly with the
connected account instead of your platform.
- (Optional) `payment_intent_data[application_fee_amount]`—This argument
specifies the amount your platform plans to take from the transaction. After the
payment is processed on the connected account, the `application_fee_amount` is
transferred to the platform and the Stripe fee is deducted from the connected
account’s balance.

### Handle post-payment events Server-side

Stripe sends a
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
event when the payment completes. [Use a webhook to receive these
events](https://docs.stripe.com/webhooks/quickstart) and run actions, such as
sending an order confirmation email to your customer, logging the sale in a
database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On
the client, the customer could close the browser window or quit the app before
the callback executes. Some payment methods also take 2-14 days for payment
confirmation. Setting up your integration to listen for asynchronous events
enables you to accept multiple [payment
methods](https://stripe.com/payments/payment-methods-guide) with a single
integration.

In addition to handling the `checkout.session.completed` event, we recommend
handling two other events when collecting payments with Checkout:

EventDescriptionNext
steps[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)The
customer has successfully authorized the payment by submitting the Checkout
form.Wait for the payment to succeed or
fail.[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)The
customer’s payment succeeded.Fulfill the purchased goods or
services.[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)The
payment was declined, or it failed for some other reason.Contact the customer
through email and request that they place a new order.
These events all include the [Checkout
Session](https://docs.stripe.com/api/checkout/sessions) object. After the
payment succeeds, the underlying
[PaymentIntent](https://docs.stripe.com/payments/payment-intents) status changes
from `processing` to `succeeded`.

[Set up email communications to connected
accounts](https://docs.stripe.com/connect/build-full-embedded-integration#setup-email-communications)
Stripe communicates with your connected accounts on your behalf to manage risk
and ensure ongoing compliance. You can customize and brand these email
communications with your own email domain and platform branding.

We send the following emails to your connected accounts:

- **Account emails** verify an account’s information, such as additions or
changes to an email address, phone number, or bank account.
- **Compliance emails** notify accounts to provide required information. Stripe
often needs to collect further information to maintain compliance with our
financial partners.
- **Risk emails** notify accounts when they’re under a risk review. These emails
often provide instructions on how to submit information to resolve a risk
action; for example, to remove a pause on payouts.
- **Tax emails** (only when Stripe collects Stripe fees directly from connected
accounts) notify users when their tax invoices or 1099s are ready to download.

If you want to send any other payments-related emails to your connected
accounts, you must send them yourself. For example, to send emails for new
disputes, [listen for](https://docs.stripe.com/webhooks) the
`charge.dispute.created` event on a connected account. When that event occurs,
use [the Disputes API](https://docs.stripe.com/api/disputes) to get the details
and email them to the account.

You must [update your Connect settings with the
URLs](https://dashboard.stripe.com/settings/connect/site-links) of your payments
and account workflows so Stripe’s email communications can include links for
your accounts to respond. You must update these links before [creating an
account session](https://docs.stripe.com/api/account_sessions/create) or an
[account link](https://docs.stripe.com/api/account_links/create) in livemode.

## Handle redirects from email links

Emails sent by Stripe that contain a call to action need to include a link to
that action. For example, if we send an email directing action on a connected
account, it must include a link to your Account management component.

Before you can create a live mode Account Session, you must provide the URLs
where you have integrated the embedded components into your website. Configure
the sending email domain and embedded component URLs in the **Site links**
section of [your platform’s Connect
settings](https://dashboard.stripe.com/settings/connect/embedded_ui).

#### Note

Test mode environments use the same URLs as live mode.

For embedded components integrated in your site, select **Yes** and enter the
URL of the page that hosts the component. For any actions not handled by an
embedded component, select **No** and enter the URL of the page on your site
where the account can perform the action. After entering the URLs, test them to
verify that they open the right pages.

You must set URLs for the following:

- Notification banner
- Account management
- Payments
- Payouts
- Balances
- Documents (when Stripe collects Stripe fees directly from connected accounts)

When sending an email, Stripe automatically appends the connected account ID to
the redirect URL as the `stripe_account_id` parameter. Use that parameter to
identify the account and verify that they’re authenticated. Set up the route on
your server to read the parameters and display the correct embedded component.

For more information about configuring Stripe emails to your connected accounts,
see [Email communications in embedded Connect
integrations](https://docs.stripe.com/connect/embedded-comms)

## Configure email branding and settings

Stripe can send emails reflecting your platform’s brand settings from your own
email domain to your connected accounts. To configure Stripe emails to your
connected accounts, visit
[Emails](https://dashboard.stripe.com/settings/connect/emails) in your platform
Dashboard.

[Go
live](https://docs.stripe.com/connect/build-full-embedded-integration#go-live)
At this point, you’ve configured your platform integration by doing the
following:

- Created connected accounts in the correct configuration
- Integrated embedded components to allow connected accounts to onboard, manage
their account, and respond to risk actions through your website
- Set up payments using Direct charges with an application fee
- Set up branded email communications to enable Stripe to communicate with your
users for compliance, risk actions, and necessary documents

## Test your integration

Test your account creation flow by using the embedded account onboarding
integrated in your platform. Test the settings of your payment methods for your
connected accounts by logging into one of your test accounts and navigating to
the [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods). Test your
checkout flow with your test keys and a test account. You can use our [test
cards](https://docs.stripe.com/testing) to test your payments flow and simulate
various payment outcomes.

## Links

- [demo site for our fictitious business, Furever](http://furever.dev)
- [Register your platform](https://dashboard.stripe.com/connect/set-up)
- [activate your account](https://dashboard.stripe.com/account/onboarding)
- [Complete your platform
profile](https://dashboard.stripe.com/connect/settings/profile)
- [Customize your brand
settings](https://dashboard.stripe.com/settings/connect/stripe-dashboard/branding)
- [manages risk](https://docs.stripe.com/connect/risk-management)
- [/v1/accounts](https://docs.stripe.com/api/accounts/create)
- [optional
components](https://docs.stripe.com/connect/supported-embedded-components)
- [set up embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components)
- [Account Session](https://docs.stripe.com/api/account_sessions)
- [required verification
information](https://docs.stripe.com/connect/required-verification-information)
-
[requirements](https://docs.stripe.com/api/accounts/object#account_object-requirements)
- [Update Account](https://docs.stripe.com/api/accounts/update)
- [Furever demo site](https://furever.dev)
- [onboarding embedded
component](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding)
-
[account.updated](https://docs.stripe.com/api/events/types#event_types-account.updated)
- [Connect webhooks](https://docs.stripe.com/connect/webhooks)
- [retrieving the Account](https://docs.stripe.com/api/account/retrieve)
- [capabilities](https://docs.stripe.com/connect/account-capabilities)
- [Embedded Connect support](https://docs.stripe.com/connect/embedded-support)
- [notification banner embedded
component](https://docs.stripe.com/connect/supported-embedded-components/notification-banner)
- [risk-related requests](https://docs.stripe.com/connect/embedded-risk)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [account management embedded
component](https://docs.stripe.com/connect/supported-embedded-components/account-management)
-
[payments](https://docs.stripe.com/connect/supported-embedded-components/payments)
-
[payouts](https://docs.stripe.com/connect/supported-embedded-components/payouts)
- [initializing
ConnectJS](https://docs.stripe.com/connect/get-started-connect-embedded-components#account-sessions)
- [Connect embedded components integration
quickstart](https://docs.stripe.com/connect/connect-embedded-components/quickstart)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [Account](https://docs.stripe.com/api/accounts/object)
- [application fee](https://docs.stripe.com/connect/direct-charges#collect-fees)
- [Stripe Checkout](https://docs.stripe.com/payments/checkout)
- [Payment Element](https://docs.stripe.com/payments/payment-element)
- [Customize
branding](https://docs.stripe.com/connect/direct-charges?platform=web&ui=stripe-hosted#branding)
-
[URL](https://docs.stripe.com/api/checkout/sessions/object#checkout_session_object-url)
- [https://example.com/success](https://example.com/success)
- [https://example.com/cancel](https://example.com/cancel)
-
[checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed)
- [Use a webhook to receive these
events](https://docs.stripe.com/webhooks/quickstart)
- [payment methods](https://stripe.com/payments/payment-methods-guide)
-
[checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_succeeded)
-
[checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types#event_types-checkout.session.async_payment_failed)
- [Checkout Session](https://docs.stripe.com/api/checkout/sessions)
- [PaymentIntent](https://docs.stripe.com/payments/payment-intents)
- [listen for](https://docs.stripe.com/webhooks)
- [the Disputes API](https://docs.stripe.com/api/disputes)
- [update your Connect settings with the
URLs](https://dashboard.stripe.com/settings/connect/site-links)
- [account link](https://docs.stripe.com/api/account_links/create)
- [your platform’s Connect
settings](https://dashboard.stripe.com/settings/connect/embedded_ui)
- [Email communications in embedded Connect
integrations](https://docs.stripe.com/connect/embedded-comms)
- [Emails](https://dashboard.stripe.com/settings/connect/emails)
- [Payment methods
settings](https://dashboard.stripe.com/settings/payment_methods)
- [test cards](https://docs.stripe.com/testing)