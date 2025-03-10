# Resolve webhook signature verification errors

## Learn how to fix a common error when listening to webhook events.

When processing webhook events, we recommend securing your endpoint by
[verifying](https://docs.stripe.com/webhooks#verify-official-libraries) that the
event is coming from Stripe. To do so, use the `Stripe-Signature` header and
call the `constructEvent()` function with three parameters:

- `requestBody`: the request body string sent by Stripe
- `signature`: the Stripe-Signature header in the request sent by Stripe
- `endpointSecret`: the secret associated with your endpoint

```
Stripe::Webhook.construct_event(request_body, signature, endpoint_secret)
```

This function might trigger a signature verification error.

```
Webhook signature verification failed. Err: No signatures found matching the
expected signature for payload.

```

If you get this error, at least one of the three parameters you passed to the
above function is incorrect. The following steps explain how to verify that each
parameter is correctly set.

## Check the endpoint secret

The most common error is using the wrong endpoint secret. If you’re using a
webhook endpoint created in the
[Dashboard](https://dashboard.stripe.com/test/webhooks), open the endpoint in
the Dashboard and click the **Reveal secret** link near the top of the page to
view the secret.

![Dashboard screenshot showing where to find the webhook secret
key](https://b.stripecdn.com/docs-statics-srv/assets/dashboard-secret.ea91fb644ee376b25daee8438bc6a33c.png)

If you’re using the Stripe CLI, the secret is printed in the Terminal when you
run the `stripe listen` command.

![cli screenshot showing where to find the webhook secret
key](https://b.stripecdn.com/docs-statics-srv/assets/cli-secret.43855dd95672a6d396ef8cf2eeb9e8fa.png)

In both cases, the secret starts with a `whsec_` prefix, but the secret itself
is different. Don’t verify signatures on events forwarded by the CLI using the
secret from a Dashboard-managed endpoint, or the other way around.

Finally, print the `endpointSecret` used in your code, and make sure that it
matches the one you found above.

## Check the request body

The request body must be the body string that Stripe sends in UTF-8 encoding
without any changes. When you print it as a string, it looks similar to this:

```
{
 "id": "evt_xxx",
 "object": "event",
 "data": {
 ...
 }
}

```

### Retrieve the raw request body

Some frameworks might edit the request body by doing things like adding or
removing whitespace, reordering the key-value pairs, converting the string to
JSON, or changing the encoding. All of these cases lead to a failed signature
verification.

The following is a non-exhaustive list of frameworks that might parse or mutate
the data using common configurations, and some tips on how to get the raw
request body.

FrameworkRetrieval methodstripe-node library with ExpressFollow our [integration
quickstart
guide](https://docs.stripe.com/webhooks/quickstart?lang=node).stripe-node
library with Body ParserTry solutions listed in [this GitHub
issue](https://github.com/stripe/stripe-node/issues/341).stripe-node library
with Next.js [App
Router](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)Take
a look at this [working
example](https://github.com/stripe/stripe-node/blob/master/examples/webhook-signing/nextjs/app/api/webhooks/route.ts).stripe-node
library with Next.js [Pages
Router](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)Try
disabling `bodyParser` and using `buffer(request)`, like in [this
example](https://github.com/stripe/stripe-node/blob/master/examples/webhook-signing/nextjs/pages/api/webhooks.ts).
### AWS API Gateway with Lambda function

To retrieve the raw request body for the AWS API Gateway with Lambda function,
in the API Gateway, set up a Body Mapping Template like this:

- Content-Type: `application/json`
- Template contents:

```
{
 "method": "$context.httpMethod",
 "body": $input.json('$'),
 "rawBody": "$util.escapeJavaScript($input.body).replaceAll("\\'", "'")",
 "headers": {
 #foreach($param in $input.params().header.keySet())
 "$param": "$util.escapeJavaScript($input.params().header.get($param))"
 #if($foreach.hasNext),#end
 #end
 }
}

```

Then, in the Lambda function, access the raw body with the event’s `rawBody`
property and the headers with the event’s `headers` property.

## Check the signature

Print the `signature` parameter, and confirm that it looks similar to this:

```
t=xxx,v1=yyy,v0=zzz

```

If not, check if you have an issue in your code when trying to extract the
signature from the header.

## Links

- [verifying](https://docs.stripe.com/webhooks#verify-official-libraries)
- [Dashboard](https://dashboard.stripe.com/test/webhooks)
- [integration quickstart
guide](https://docs.stripe.com/webhooks/quickstart?lang=node)
- [this GitHub issue](https://github.com/stripe/stripe-node/issues/341)
- [App
Router](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)
- [working
example](https://github.com/stripe/stripe-node/blob/master/examples/webhook-signing/nextjs/app/api/webhooks/route.ts)
- [Pages
Router](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
- [this
example](https://github.com/stripe/stripe-node/blob/master/examples/webhook-signing/nextjs/pages/api/webhooks.ts)