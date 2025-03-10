[Skip to content](https://docs.stripe.com/agents#main-content)

Overview

[Create account](https://dashboard.stripe.com/register) or [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fagents)

[The Stripe Docs logo](https://docs.stripe.com/)

Search the docs or ask a question

`/`

[Create account](https://dashboard.stripe.com/register)

[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fagents)

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

[Overview](https://docs.stripe.com/development)

Versioning

Changelog

[Upgrade your API version](https://docs.stripe.com/upgrades)

Upgrade your SDK version

Developer tools

SDKs

API

Testing

Workbench

Event Destinations

Stripe CLI

Stripe Shell

Developers Dashboard

Agent toolkit

Overview

[Quickstart](https://docs.stripe.com/agents/quickstart "Build a basic chatbot and bill for usage")

[Stripe for Visual Studio Code](https://docs.stripe.com/stripe-vscode "Stripe for Visual Studio Code") [File uploads](https://docs.stripe.com/file-upload)

Security

Security

Extend Stripe

Stripe Apps

Stripe Connectors

Partners

[Partner ecosystem](https://docs.stripe.com/partners "Learn about the Stripe Partner Program") [Partner certification](https://docs.stripe.com/partners/training-and-certification "Become a Stripe-certified architect or developer")

United States

English (United States)

[Home](https://docs.stripe.com/ "Home")[Developer tools](https://docs.stripe.com/development "Developer tools")Agent toolkit

# Add Stripe to your agentic workflowsDeveloper preview

## Use financial services with agents.

Use Stripe to run your agent business and enhance your agents’ functionality. By enabling access to financial services and tools, you allow your agents to help you earn and spend funds, expanding their capabilities.

[Create Stripe objects\\
\\
Automate common payment workflows with function calling.](https://docs.stripe.com/agents#create-objects "Create Stripe objects")

[Charge for agent usage\\
\\
Bill users with usage-based billing.](https://docs.stripe.com/agents#metered-billing "Charge for agent usage")

[Buy goods online\\
\\
Use single-use virtual cards to purchase goods.](https://docs.stripe.com/agents#online-purchasing "Buy goods online")

## Create Stripe objects ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Use function calling to create and manage Stripe objects. For example, dynamically create [Payment Links](https://docs.stripe.com/payment-links) to accept funds, integrate into your support workflows to help customers, and scaffold test data.

The Stripe agent toolkit supports Vercel’s AI SDK, LangChain, and CrewAI. It works with any LLM provider that supports function calling and is compatible with Python and TypeScript.

Vercel AI SDK

LangChain

CrewAI

Select a languageNode

```CodeBlock-code

import { StripeAgentToolkit } from '@stripe/agent-toolkit/ai-sdk';
import { openai } from '@ai-sdk/openai';
import { generateText } from 'ai';

const stripeAgentToolkit = new StripeAgentToolkit({
  secretKey: process.env.STRIPE_SECRET_KEY!,
  configuration: {
    actions: {
      paymentLinks: {
        create: true,
      },
      products: {
        create: true,
      },
      prices: {
        create: true,
      },
    },
  },
});

const result = await generateText({
  model: openai('gpt-4o'),
  tools: {
    ...stripeAgentToolkit.getTools(),
  },
  maxSteps: 5,
  prompt: 'Create a payment link for a new product called \"Test\" with a price of $100.',
})
```

#### Developer preview

Explore this SDK to integrate Stripe into agentic workflows. Because agent behavior is non-deterministic, use the SDK in [test mode](https://docs.stripe.com/test-mode) and run evaluations to assess your application’s performance. Additionally, use [restricted API keys](https://docs.stripe.com/keys#create-restricted-api-secret-key) to limit access to the functionality your agent requires.

## Charge for agent usage ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Integrate [usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based) to record usage. The Stripe agent toolkit offers native support for billing by prompt and completion token usage in the Vercel AI SDK. You can forward LLM costs directly to your users using a [Customer](https://docs.stripe.com/api/customers/object) and `event_name` s for input and output [Meter Events](https://docs.stripe.com/api/billing/meter-event/object).

```CodeBlock-code

import { StripeAgentToolkit } from '@stripe/agent-toolkit/ai-sdk';
import { openai } from '@ai-sdk/openai';
import {
  experimental_wrapLanguageModel as wrapLanguageModel,
} from 'ai';

const model = wrapLanguageModel({
  model: openai('gpt-4o'),
  middleware: stripeAgentToolkit.middleware({
    billing: {
      customer: process.env.STRIPE_CUSTOMER_ID!,
      meters: {
        input: process.env.STRIPE_METER_INPUT!,
        output: process.env.STRIPE_METER_OUTPUT!,
      },
    },
  }),
});
```

Usage-based billing gives you the flexibility to charge for any unit, such as by time. You can emit billing events directly, such as measuring duration:

```CodeBlock-code

import stripe
import time

start = time.time()

# Run your agent workflow, LLM execution, etc.
execute_agent()

end = time.time()

stripe.billing.MeterEvent.

create(


event_name="agent_execution",


payload={
    "value": end - start,
    "stripe_customer_id": "{{CUSTOMER_ID}}"
  },
)
```

## Buy goods online ![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Use [Stripe Issuing](https://docs.stripe.com/issuing) to create single-use virtual cards for your business purchases. This allows your agents to spend funds. The Issuing APIs allow you to programmatically approve or decline authorizations, ensuring your purchase intent matches the authorization. Spending controls allow you to set budgets and limit spending for your agents.

## Next steps![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- See the [Agent quickstart](https://docs.stripe.com/agents/quickstart) for a full code example
- Download the [agent toolkit on GitHub](https://github.com/stripe/agent-toolkit)
- [Follow our guide](https://docs.stripe.com/baas/start-integration/integration-guides/b2b-payments) to build a B2B Payments integration with Issuing

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

## Interested in adding Stripe to your agent workflows?

Enter your email address below.

Collect Email

Sign up

Read our [privacy policy](https://stripe.com/privacy).

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

[Create Stripe objects](https://docs.stripe.com/agents#create-objects "Create Stripe objects")

[Charge for agent usage](https://docs.stripe.com/agents#metered-billing "Charge for agent usage")

[Buy goods online](https://docs.stripe.com/agents#online-purchasing "Buy goods online")

[Next steps](https://docs.stripe.com/agents#next-steps "Next steps")

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

Pixels![](https://dsum-sec.casalemedia.com/rum?cm_dsp_id=18&expiry=1757517445&external_user_id=319b6883-c118-43a1-8642-47c3fd8456c4)![](https://partners.tremorhub.com/sync?UIDM=319b6883-c118-43a1-8642-47c3fd8456c4)![](https://pixel.rubiconproject.com/tap.php?nid=5578&put=319b6883-c118-43a1-8642-47c3fd8456c4&v=1181926)

![](https://id.rlcdn.com/464526.gif)![](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ea4a8864-291b-438f-980b-bdbde20c5ea8&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=75823b3b-471e-41c2-b241-9ebb31d29e4a&tw_document_href=https%3A%2F%2Fdocs.stripe.com%2F&tw_document_referrer=https%3A%2F%2Fdocs.stripe.com%2F&tw_iframe_status=1&txn_id=o5ygk&type=javascript&version=2.3.31)![](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%261280%261024%264%2624%261280%261024%260%26na&eci=3&event=%7B%7D&event_id=ea4a8864-291b-438f-980b-bdbde20c5ea8&integration=gtm&p_id=Twitter&p_user_id=0&pl_id=75823b3b-471e-41c2-b241-9ebb31d29e4a&tw_document_href=https%3A%2F%2Fdocs.stripe.com%2F&tw_document_referrer=https%3A%2F%2Fdocs.stripe.com%2F&tw_iframe_status=1&txn_id=o5ygk&type=javascript&version=2.3.31)

StripeM-Inner