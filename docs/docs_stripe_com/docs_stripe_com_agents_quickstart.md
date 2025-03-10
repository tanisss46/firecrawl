Download full appDon't code? Use Stripe’s [no-code
options](https://docs.stripe.com/no-code) or get help from [our
partners](https://stripe.partners/).1 Set up the server
### Install the Stripe Agent Toolkit

Install the package and import it into your code.

npmGitHub
Install the library:

`npm install --save @stripe/agent-toolkit`Server
### Create an endpoint to handle the request

Add an endpoint on your server that handles the new chat input.

Server
### Initialize the toolkit

Using your Stripe API key, create a new instance of the `StripeAgentToolkit`.
The toolkit allows you to insert billing middleware and also access Stripe
functionality.

Server
### Provide the middleware to the model

Using middleware, you can report the prompt and completion token usage to Stripe
through the Meter API. The `billing` configuration requires you to provide a
[Customer](https://docs.stripe.com/api/customers/object) ID and input and output
[Meter Events](https://docs.stripe.com/api/billing/meter-event/object).

Learn how to [setup usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide).

Server
### Call the model

Use Vercel’s AI SDK to call the model and stream back results to the client.
Your request includes the existing message log and a system prompt to provide
initial instructions to the model.

Server2Build your frontend
### Create a chat interface

Use Next.js and Vercel’s AI SDK to build a basic chat interface to call into the
backend you built.

Client3Test your page
### Set your environment variables

Add your publishable and secret keys to a `.env` file. Next.js automatically
loads them into your application as [environment
variables](https://nextjs.org/docs/basic-features/environment-variables).

Server
### Run the application

Start your app with `npm run dev` and navigate to
[http://localhost:3000](http://localhost:3000/).

Client
### Testing

To test this functionality, send a message to the chat.

### View usage in the Dashboard

View your Meters in the [Stripe Dashboard](https://dashboard.stripe.com/meters)
to confirm that events are sent successfully.

app/api/chat/route.tsapp/page.tsx.envDownload
```
import { StripeAgentToolkit } from '@stripe/agent-toolkit/ai-sdk';import {
openai } from '@ai-sdk/openai';import { convertToCoreMessages,
experimental_wrapLanguageModel as wrapLanguageModel, streamText} from 'ai';
// Instantiate a new Stripe Agent Toolkit.const stripeAgentToolkit = new
StripeAgentToolkit({ secretKey: process.env.STRIPE_SECRET_KEY!, configuration:
{},});
export async function POST(req: Request) { const { messages } = await
req.json();
// Wrap the language model and include the // billing middleware. const model =
wrapLanguageModel({ model: openai('gpt-4o'), middleware:
stripeAgentToolkit.middleware({ billing: { customer:
process.env.STRIPE_CUSTOMER_ID!, meters: { input:
process.env.STRIPE_METER_INPUT!, output: process.env.STRIPE_METER_OUTPUT!, }, },
}), });
// Call the model and stream back the results. const result = await streamText({
model: model, system: SYSTEM_PROMPT, messages: convertToCoreMessages(messages),
});
 return result.toDataStreamResponse();}
```

## Links

- [text version of this
guide](https://docs.stripe.com/payments/accept-a-payment)
- [sandbox](https://docs.stripe.com/sandboxes)
- [restricted API
keys](https://docs.stripe.com/keys#create-restricted-api-secret-key)
- [no-code options](https://docs.stripe.com/no-code)
- [our partners](https://stripe.partners)
- [Customer](https://docs.stripe.com/api/customers/object)
- [Meter Events](https://docs.stripe.com/api/billing/meter-event/object)
- [setup usage-based
billing](https://docs.stripe.com/billing/subscriptions/usage-based/implementation-guide)
- [environment
variables](https://nextjs.org/docs/basic-features/environment-variables)
- [http://localhost:3000](http://localhost:3000)
- [Stripe Dashboard](https://dashboard.stripe.com/meters)