[Skip to content](https://docs.stripe.com/ach-deprecated#main-content)

ACH Direct Debit

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fach-deprecated)

[The Stripe Docs logo](https://docs.stripe.com/)

Search the docs or ask a question

`/`

[Create account](https://dashboard.stripe.com/register)

[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fach-deprecated)

[Get started](https://docs.stripe.com/get-started)

[Payments](https://docs.stripe.com/payments)

[Finance automation](https://docs.stripe.com/finance-automation)

[Platforms and marketplaces](https://docs.stripe.com/connect)

[Banking as a service](https://docs.stripe.com/financial-services)

[Developer tools](https://docs.stripe.com/development)

[Get started](https://docs.stripe.com/get-started)

[Payments](https://docs.stripe.com/payments)

[Finance automation](https://docs.stripe.com/finance-automation)

[Get started](https://docs.stripe.com/get-started)

[Payments](https://docs.stripe.com/payments)

[Finance automation](https://docs.stripe.com/finance-automation)

[Platforms and marketplaces](https://docs.stripe.com/connect)

[Banking as a service](https://docs.stripe.com/financial-services)

APIs & SDKs

Help

[Overview](https://docs.stripe.com/get-started) [Explore all products](https://docs.stripe.com/products "See all of Stripe's available products") [Release phases](https://docs.stripe.com/release-phases "Learn how Stripe describes product release phases")

Plan your integration

Set up Stripe

Create an account

[Accept a payment](https://docs.stripe.com/payments/accept-a-payment)

Products and prices

Use Stripe without code

Regulation support

Stripe Dashboard

Web Dashboard

[Mobile Dashboard](https://docs.stripe.com/dashboard/mobile)

For developers

Start developing

Sample projects

About the APIs

[API tour](https://docs.stripe.com/payments-api/tour "Tour of the API and its core concepts")

[Payment Intents API](https://docs.stripe.com/payments/payment-intents "About the Payment Intents API")

[Setup Intents API](https://docs.stripe.com/payments/setup-intents "About the Setup Intents API")

[Payment Methods](https://docs.stripe.com/payments/payment-methods "About the Payment Methods API")

[Older APIs](https://docs.stripe.com/payments/older-apis "Our older APIs")

[Charges](https://docs.stripe.com/payments/charges-api "Use the Charges API")

[Sources](https://docs.stripe.com/sources "About the Sources API")

[Transition to the new APIs](https://docs.stripe.com/payments/payment-methods/transitioning)

[Card Sources](https://docs.stripe.com/sources/cards)

[Sources and customers](https://docs.stripe.com/sources/customers)

ACH Direct Debit

[Connect platforms](https://docs.stripe.com/sources/connect "Connect platforms using the Sources API")

[Best practices](https://docs.stripe.com/sources/best-practices "Best practices using Sources")

[iOS](https://docs.stripe.com/mobile/ios/sources "Getting started with Sources in the iOS SDK")

[Android](https://docs.stripe.com/mobile/android/sources "Getting started with Sources in the Android SDK")

Migrate to Stripe

[Migrate customer data](https://docs.stripe.com/get-started/data-migrations "Migrate your sensitive customer data")

Migrate payment data

[Migrate subscriptions](https://docs.stripe.com/get-started/subscription-migrations "Migrate your existing subscriptions to Stripe")

Manage fraud risk

Understand fraud

Radar fraud protection

Manage disputes

Verify identities

United States

English (United States)

[Home](https://docs.stripe.com/ "Home")[Get started](https://docs.stripe.com/get-started "Get started")About the APIs[Older APIs](https://docs.stripe.com/payments/older-apis "Older APIs")[Sources](https://docs.stripe.com/sources "Sources")

# ACH Direct Debit with ChargesDeprecated

## Legacy guide for accepting ACH payments with our older Charges API.

#### Legacy

The content below describes a Legacy method for collecting ACH payments.

If you’re building a new integration, use one of our current methods for [accepting ACH payments](https://docs.stripe.com/payments/ach-direct-debit) instead.

If you have an existing integration that accepts ACH payments using the Charges API, we recommend [migrating to the Payment Intents API](https://docs.stripe.com/payments/ach-direct-debit/migrating-from-charges). The Payment Intents API includes built-in instant verification.

Stripe allows you to accept ACH payments in nearly the same way as you accept credit card payments, by providing a verified bank account as the `source` argument for a charge request. However, accepting bank accounts requires a slightly different initial workflow than accepting credit cards:

1. You must first [verify](https://docs.stripe.com/ach-deprecated#verifying) bank accounts.
2. Your customer must [authorize](https://docs.stripe.com/ach-deprecated#authorization) you to use them.

After taking both steps for a bank account, your customer can use it like other payment methods, including for recurring charges and [Connect](https://docs.stripe.com/ach-deprecated#connect) applications. The two key differences between using bank accounts and credit cards are:

- ACH payments take up to 5 business days to receive acknowledgment of their success or failure. Because of this, your Stripe balance takes up to 7 business days to reflect ACH payments in your available Stripe balance.
- You can only accept funds in USD and only from US bank accounts. In addition, your account must have a US (USD) bank account to accept ACH payments.

## Collecting and verifying bank accounts ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Before you can create an ACH charge, you must first collect and verify your customer’s bank account and routing number. In order to properly identify the bank account, you also need to collect the name of the person or business who owns the account, and if the account is owned by an individual or a company. Stripe provides two methods for doing so: instant collection and verification with [Plaid](https://plaid.com/docs/auth/partnerships/stripe/) or collection using [Stripe.js](https://docs.stripe.com/payments/elements) with delayed-verification using microdeposits. You may incur additional costs when using Plaid, depending on the size of your business. Take this into account when making your decision.

Because charging a bank account requires both verification of the account and customer authorization to use it, the best practice is to store the bank account on a `Customer` object in Stripe so you can reuse it.

## Using Plaid ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

![plaid logo](https://b.stripecdn.com/docs-statics-srv/assets/plaid.291ca97692152302c6cbab16a1c39257.png)

Plaid provides the quickest way to collect and verify your customer’s banking information. Using the Stripe + Plaid integration, you can instantly receive a verified bank account, which allows for immediate charging. This is done using [Plaid Link](https://plaid.com/docs/auth/partnerships/stripe/), and you receive the Stripe bank account token directly from Plaid.

**Step 1: Set up your Plaid account**

If you don’t have a Plaid account, [create one](https://plaid.com/docs/auth/partnerships/stripe). Your account is automatically enabled for integration access.To verify that your Plaid account is enabled for the Stripe integration, go to the [Integrations](https://dashboard.plaid.com/team/integrations) section of the account dashboard. Make sure your Stripe account is connected there.

**Step 2: Fetch a Link token**

A `link_token` is a one-time use token that initializes Plaid Link. You can create a link\_token and configure it for your specific Link flow by calling the [Create Link Token](https://plaid.com/docs/#create-link-token) endpoint from your server.

Command Line

Select a languagecurl

```CodeBlock-code

curl https://sandbox.plaid.com/link/token/create \
  -H "Content-Type: application/json" \
  -d "{\"client_id\": \"{{PLAID_CLIENT_ID}}\",\"secret\": \"{{PLAID_SECRET}}\",\"client_name\": \"My App\",\"user\": {\"client_user_id\": \"Stripe test\"},\"products\": [\"auth\"],\"country_codes\": [\"US\"],\"language\": \"en\", \"webhook\": \"https://webhook.sample.com/\"}"
```

**Step 3: Integrate with Plaid Link**

Integrating with Link only takes a few lines of client-side JavaScript and a small server-side handler to exchange the Link `public_token` for a Plaid `access_token` and a Stripe bank account token.

```CodeBlock-code

<button id="link-button">Link Account</button>

<script src="https://cdn.plaid.com/link/v2/stable/link-initialize.js"></script>
<script type="text/javascript">
(async function() {

  const configs = {
    // Pass the link_token generated in step 2.
    token: '{{LINK_TOKEN}}',
    onLoad: function() {
      // The Link module finished loading.
    },
    onSuccess: function(public_token, metadata) {
      // The onSuccess function is called when the user has
      // successfully authenticated and selected an account to
      // use.
      //
      // When called, you will send the public_token
      // and the selected account ID, metadata.accounts,
      // to your backend app server.
      //
      // sendDataToBackendServer({
      //   public_token: public_token,
      //   account_id: metadata.accounts[0].id
      // });
      console.log('Public Token: ' + public_token);
      switch (metadata.accounts.length) {
        case 0:
          // Select Account is disabled: https://dashboard.plaid.com/link/account-select
          break;
        case 1:
          console.log('Customer-selected account ID: ' + metadata.accounts[0].id);
          break;
        default:
          // Multiple Accounts is enabled: https://dashboard.plaid.com/link/account-select
      }
    },
    onExit: async function(err, metadata) {
      // The user exited the Link flow.
      if (err != null) {
          // The user encountered a Plaid API error
          // prior to exiting.
      }
      // metadata contains information about the institution
      // that the user selected and the most recent
      // API request IDs.
      // Storing this information can be helpful for support.
    },
  };

  var linkHandler = Plaid.create(configs);

  document.getElementById('link-button').onclick = function() {
    linkHandler.open();
  };
})();
</script>
```

**Step 4: Write server-side handler**

The Link module handles the entire onboarding flow securely and quickly, but doesn’t actually retrieve account data for a user. Instead, the Link module returns a `public_token` and an `accounts` array, which is a property on the `metadata` object, and part of the `onSuccess` callback.

The `accounts` array contains information about bank accounts associated with the credentials entered by the user, and may contain multiple accounts if the user has more than one bank account at the institution. To avoid any confusion about which account your user wants to use with Stripe, set [Select Account](https://dashboard.plaid.com/link/account-select) to **Enabled for one account** in the Plaid developer dashboard. When you select this setting, it means the accounts array will always contain exactly one element.

When your server has the `public_token` and `account_id`, you must make two calls to the Plaid server to get the Stripe bank account token along with the Plaid `access_token` to use for other Plaid API requests.

Command Line

Select a languagecurl

```CodeBlock-code

curl https://sandbox.plaid.com/item/public_token/exchange \
  -H "Content-Type: application/json" \
  -d "{\"client_id\": \"{{PLAID_CLIENT_ID}}\", \"secret\": \"{{PLAID_SECRET}}\", \"public_token\": \"{{PLAID_LINK_PUBLIC_TOKEN}}\"}"

curl https://sandbox.plaid.com/processor/stripe/bank_account_token/create \
  -H "Content-Type: application/json" \
  -d "{\"client_id\": \"{{PLAID_CLIENT_ID}}\", \"secret\": \"{{PLAID_SECRET}}\", \"access_token\": \"{{PLAID_ACCESS_TOKEN}}\", \"account_id\": \"{{PLAID_ACCOUNT_ID}}\"}"
```

The response contains a verified Stripe bank account token ID. You can attach this token to a Stripe `Customer` object, or create a charge directly on it.

```CodeBlock-code

{
  "stripe_bank_account_token": "btok_",
  "request_id": "[Unique request ID]"
}
```

**Step 5: Get ready for production**

Plaid uses different API hosts for test and production requests. The above request uses Plaid’s Sandbox environment, which uses simulated data. To test with live users, use Plaid’s Development environment. Plaid’s Development environment supports up to 100 live objects, which you won’t be billed for. When it’s time to go live, use [Plaid’s Production environment](https://plaid.com/docs/auth/partnerships/stripe/#step4).

## Manually collecting and verifying bank accounts![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Plaid supports instant verification for many of the most popular banks. However, if Plaid doesn’t support your customer’s bank or you don’t want to integrate with Plaid, collect and verify the customer’s bank using Stripe alone.

First, use [Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=bank_account) to securely collect your customer’s bank account information, receiving a representative token in return. When you have that, attach it to a Stripe customer in your account.To comply with [Nacha rules](https://www.nacha.org/newrules), make sure you provide a valid account holder name for the customer.

Command Line

Select a languagecurl

```CodeBlock-code

curl https://api.stripe.com/v1/customers \
  -u

sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
  -d "name"="Jenny Rosen" \
  -d "source"="btok_4XNshPRgmDRCVi"
```

[Customer](https://docs.stripe.com/api/customers "Customers") bank accounts require verification. When using Stripe without Plaid, Stripe automatically sends two small deposits for this purpose. These deposits take 1-2 business days to appear on the customer’s online statement. The statement has a description that includes `ACCTVERIFY`. Your customer must relay these amounts to you.

When accepting these amounts, be aware that the limit is three failed verification attempts. If you exceed this limit, we can’t verify the bank account. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues. As soon as you have these amounts, you can verify the bank account.

Command Line

Select a languagecurl

```CodeBlock-code

curl https://api.stripe.com/v1/customers/cus_AFGbOSiITuJVDs/sources/ba_17SHwa2eZvKYlo2CUx7nphbZ/verify \
  -u

sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
  -d "amounts[]"=32 \
  -d "amounts[]"=45
```

After we verify the bank account, you can make charges against it.

## Payment authorization ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Before creating an ACH charge, get authorization from your customer to debit their account. Doing so ensures compliance with the ACH network and helps protect you from disputes,additional fees, and reversed payments.See the [support page](https://support.stripe.com/questions/collect-ach-authorization-from-customers) for more information on authorization requirements.

## Creating an ACH charge![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To create a charge on a verified bank account, use the stored `Customer` object the same way you would when using a card.

Command Line

Select a languagecURL

```CodeBlock-code

curl https://api.stripe.com/v1/charges \
  -u "

sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
  -d amount=1500 \
  -d currency=usd \
  -d customer=cus_AFGbOSiITuJVDs
```

Attempting to charge an unverified bank account results in an error with the message “The customer’s bank account must be verified in order to create an ACH payment.”

If the customer has multiple stored sources (of any type), specify which bank account to use by passing its ID in as the [source](https://docs.stripe.com/api#create_charge-source) parameter.

## Testing this integration![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can mimic successful and failed ACH charges using the following bank routing and account numbers:

- Routing number: `110000000`
- Account number:
  - `000123456789` (success)
  - `000111111116` (failure upon use)
  - `000111111113`(account closed)
  - `000222222227` (NSF/insufficient funds)
  - `000333333335` (debit not authorized)
  - `000444444440` (invalid currency)

To mimic successful and failed bank account verifications, use these meaningful amounts:

- `[32, 45]` (success)
- `[any other number combinations]` (failure)

## ACH payments workflow![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

ACH payments take up to 5 business days to receive acknowledgment of their success or failure:

- When created, ACH charges have the initial status of `pending`.
- A _pending_ balance transaction is immediately created reflecting the payment amount, less our fee.
- Payments created on or after 22:00 UTC are currently processed on the next business day.
- During the following 4 business days, the payment transitions to either `succeeded` or `failed` depending on the customer’s bank.
- Successful ACH payments are reflected in your Stripe available balance after 7 business days, at which point the funds are available for automatic or manual transfer to your bank account.
- Failed ACH payments reverse the _pending_ balance transaction created.
- Your customer sees the payment reflected on their bank statement 1-2 days after creating the charge. (Your customer knows if the payment succeeds before the bank notifies Stripe.)

Failures can happen for a number of reasons such as insufficient funds, a bad account number, or the customer disabling debits from their bank account.

In rare situations, Stripe might receive an ACH failure from the bank after a payment has transitioned to `succeeded`. If this happens, Stripe creates a dispute with a `reason` of:

- `insufficient_funds`
- `incorrect_account_details`
- `bank_cannot_process`

Stripe charges a failure fee in this situation.

## Handling disputes in this integration![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Disputes on ACH payments are fundamentally different than those on credit card payments. If a customer’s bank accepts the request to return the funds for a disputed charge, Stripe immediately removes the funds from your Stripe account. Unlike credit card disputes, you can’t contest ACH reversals. You must contact your customer to resolve the situation.

Customers can generally dispute an ACH Direct Debit payment through their bank for up to 60 calendar days after a debit on a personal account, or up to 2 business days for a business account. In rare instances, a debit payment can be successfully disputed outside these timelines.

### Risk of double-crediting with ACH refunds and disputes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If you proactively issue your customer a refund while their bank also initiates the dispute process, they may receive two credits for the same transaction.

When issuing a refund for an ACH payment, you must notify your customer immediately that you’re issuing the refund and that it may take 2-5 business days for the funds to appear in their bank account.

## Refunds![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can refund ACH charges for up to 90 days from the date of the original payment using the [Refund endpoint](https://docs.stripe.com/api#refunds). ACH refund timing and risks differ from card refunds. Stripe doesn’t notify you of successful ACH refunds, but sends the `refund.failed` event if we can’t process an ACH refund. In failure cases, you must return the funds to your customer outside of Stripe. This is rare—normally occurring only when an account becomes frozen between the original charge and the refund request.

## ACH-specific webhook notifications![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When using ACH, you’ll receive many of the standard charge [webhook](https://docs.stripe.com/webhooks "webhook") notifications, with a couple of notable differences:

- After creating the charge, you receive a `charge.pending` notification. You won’t receive `charge.succeeded` or `charge.failed` notification until up to 5 business days later.
- You receive a `charge.succeeded` notification after the charge has transitioned to `succeeded` and the funds are available in your balance.
- You receive a `charge.failed` notification if the ACH transfer fails for any reason. The charge’s `failure_code` and `failure_message` will be set, and the funds are reversed from your Stripe pending balance at this point.
- You receive a `customer.source.updated` notification when the bank account is properly verified. The bank account’s `status` is set to `verified`.
- If the bank account couldn’t be verified because either of the two small deposits failed, you receive a `customer.source.updated` notification. The bank account’s `status` is set to `verification_failed`.

## Connect support ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

With [Connect](https://docs.stripe.com/connect "Connect"), your platform can earn money while [processing charges](https://docs.stripe.com/connect/charges). You can either:

- Create the customer on the connected account, then create a [direct charge](https://docs.stripe.com/connect/direct-charges)
- Create the customer [on the platform account](https://docs.stripe.com/connect/cloning-customers-across-accounts), then create a [destination charge](https://docs.stripe.com/connect/destination-charges) using the `transfer_data` parameter (as in the code below)

Command Line

Select a languagecURL

```CodeBlock-code

curl https://api.stripe.com/v1/charges \
  -u "

sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
  -d amount=1500 \
  -d currency=usd \
  -d customer=cus_AFGbOSiITuJVDs \
  -d "transfer_data[amount]"=850 \
  -d "transfer_data[destination]"={{CONNECTED_STRIPE_ACCOUNT_ID}}
```

## Services Agreement![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Use of the live mode API is subject to the Stripe [Services Agreement](https://stripe.com/legal). Let us know if you have any questions on that agreement.

Was this page helpful?

YesNo

Need help? [Contact Support](https://support.stripe.com/).

Join our [early access program](https://insiders.stripe.dev/).

Check out our [changelog](https://docs.stripe.com/changelog).

Questions? [Contact Sales](https://stripe.com/contact/sales).

Powered by [Markdoc](https://markdoc.dev/)

hCaptcha

hCaptcha

Afrikaans

Albanian

Amharic

Arabic

Armenian

Azerbaijani

Basque

Belarusian

Bengali

Bulgarian

Bosnian

Burmese

Catalan

Cebuano

Chinese

Chinese Simplified

Chinese Traditional

Corsican

Croatian

Czech

Danish

Dutch

English

Esperanto

Estonian

Finnish

French

Frisian

Gaelic

Galacian

Georgian

German

Greek

Gujurati

Haitian

Hausa

Hawaiian

Hebrew

Hindi

Hmong

Hungarian

Icelandic

Igbo

Indonesian

Irish

Italian

Japanese

Javanese

Kannada

Kazakh

Khmer

Kinyarwanda

Kirghiz

Korean

Kurdish

Lao

Latin

Latvian

Lithuanian

Luxembourgish

Macedonian

Malagasy

Malay

Malayalam

Maltese

Maori

Marathi

Mongolian

Nepali

Norwegian

Nyanja

Oriya

Persian

Polish

Portuguese (Brazil)

Portuguese (Portugal)

Pashto

Punjabi

Romanian

Russian

Samoan

Shona

Sindhi

Singhalese

Serbian

Slovak

Slovenian

Somani

Southern Sotho

Spanish

Sundanese

Swahili

Swedish

Tagalog

Tajik

Tamil

Tatar

Teluga

Thai

Turkish

Turkmen

Uyghur

Ukrainian

Urdu

Uzbek

Vietnamese

Welsh

Xhosa

Yiddish

Yoruba

Zulu

English

EN

Please try again. ⚠️

Verify

Sign up for developer updates:

Sign up

You can unsubscribe at any time. Read our [privacy policy](https://stripe.com/privacy).

On this page

[Collecting and verifying bank accounts](https://docs.stripe.com/ach-deprecated#verifying "Collecting and verifying bank accounts")

[Using Plaid](https://docs.stripe.com/ach-deprecated#using-plaid "Using Plaid")

[Manually collecting and verifying bank accounts](https://docs.stripe.com/ach-deprecated#manually-collecting-and-verifying-bank-accounts "Manually collecting and verifying bank accounts")

[Payment authorization](https://docs.stripe.com/ach-deprecated#authorization "Payment authorization")

[Creating an ACH charge](https://docs.stripe.com/ach-deprecated#creating-an-ach-charge "Creating an ACH charge")

[Testing this integration](https://docs.stripe.com/ach-deprecated#testing-this-integration "Testing this integration")

[ACH payments workflow](https://docs.stripe.com/ach-deprecated#ach-payments-workflow "ACH payments workflow")

[Handling disputes in this integration](https://docs.stripe.com/ach-deprecated#handling-disputes-in-this-integration "Handling disputes in this integration")

[Risk of double-crediting with ACH refunds and disputes](https://docs.stripe.com/ach-deprecated#risk-of-double-crediting-with-ach-refunds-and-disputes "Risk of double-crediting with ACH refunds and disputes")

[Refunds](https://docs.stripe.com/ach-deprecated#refunds "Refunds")

[ACH-specific webhook notifications](https://docs.stripe.com/ach-deprecated#ach-specific-webhook-notifications "ACH-specific webhook notifications")

[Connect support](https://docs.stripe.com/ach-deprecated#connect "Connect support")

[Services Agreement](https://docs.stripe.com/ach-deprecated#services-agreement "Services Agreement")

Products Used

[Payments](https://docs.stripe.com/payments)

Stripe Shell

Test mode

API Explorer

```CodeBlock

Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands:

stripe help ▶️
- Find webhook events:

stripe trigger ▶️ [event]
- Listen for webhook events:

stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g.,

stripe customers list ▶️)

```

The Stripe Shell is best experienced on desktop.

```
$
```

td.doubleclick.net

# This site can’t be reached

**td.doubleclick.net** unexpectedly closed the connection.

Try:

- Checking the connection
- [Checking the proxy and the firewall](chrome-error://chromewebdata/#buttons)

ERR\_CONNECTION\_CLOSED

Reload


Details


Check your Internet connection

Check any cables and reboot any routers, modems, or other network
devices you may be using.

Allow Chrome to access the network in your firewall or antivirus
settings.

If it is already listed as a program allowed to access the network, try
removing it from the list and adding it again.

If you use a proxy server…

Go to
the Chrome menu >
Settings
>
Show advanced settings…
>
Change proxy settings…
and make sure your configuration is set to "no proxy" or "direct."

**td.doubleclick.net** unexpectedly closed the connection.

![](<Base64-Image-Removed>)![](<Base64-Image-Removed>)

![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=bada59e0-44a6-473a-8638-cca96bb09120&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=8bc60c41-d1bf-4f07-8ee7-06d13e41e2ae&tw_document_href=https%3A%2F%2Fdocs.stripe.com%2F&tw_document_referrer=https%3A%2F%2Fdocs.stripe.com%2F&tw_iframe_status=1&txn_id=o5ygk&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=bada59e0-44a6-473a-8638-cca96bb09120&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=8bc60c41-d1bf-4f07-8ee7-06d13e41e2ae&tw_document_href=https%3A%2F%2Fdocs.stripe.com%2F&tw_document_referrer=https%3A%2F%2Fdocs.stripe.com%2F&tw_iframe_status=1&txn_id=o5ygk&type=javascript&version=2.3.31)

Pixels![](https://dsum-sec.casalemedia.com/rum?cm_dsp_id=18&expiry=1757517441&external_user_id=b3dbac09-c39e-4d79-b847-c22d5155dedd)![](https://partners.tremorhub.com/sync?UIDM=b3dbac09-c39e-4d79-b847-c22d5155dedd)![](https://pixel.rubiconproject.com/tap.php?nid=5578&put=b3dbac09-c39e-4d79-b847-c22d5155dedd&v=1181926)

![](https://id.rlcdn.com/464526.gif)