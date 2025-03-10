# Migrate to direct webhook response

## Learn how to migrate Issuing real-time authorizations from API calls to direct webhook responses.

You can now [respond directly to a issuing_authorization.request
webhook](https://docs.stripe.com/issuing/controls/real-time-authorizations) with
a real-time authorization decision instead of making an API call to
[approve](https://docs.stripe.com/api/issuing/authorizations/approve) and
[decline](https://docs.stripe.com/api/issuing/authorizations/decline) endpoints
during the webhook.

Responding directly to the webhook event simplifies real-time authorizations,
and removes an extra API call that can negatively impact your authorization rate
with time outs.

If you’re building a new integration, use the new direct webhook response
instead of making approve and decline API calls. We are deprecating the approve
and decline endpoints, but existing users will continue to have access until at
least the end of 2024. If you have an existing integration with real-time
authorization, plan to migrate to direct webhook responses.

#### Note

This guide only applies if you use the `/approve` and `/decline` endpoints for
real-time authorizations.

## Legacy API call flow

Previously, you needed to make an API call to `/approve` or `/decline` to make a
decision for an incoming authorization request before responding to the
`issuing_authorization.request` webhook.

Cardholder

Stripe

User

Attempt purchase

`POST issuing_authorization.request`

Make decision

`POST /approve`

200 Response to `/approve`

Close webhook request

200 Response to `issuing_authorization.request`

Purchase approved

## New direct webhook response flow

You can now respond directly to the `issuing_authorization.request` webhook with
a decision in the response body, without needing to make a separate API call.
After the decision, an `issuing_authorization.created` or
`issuing_authorization.updated` webhook event is still sent.

Learn more about this API in the [real-time authorization
documentation](https://docs.stripe.com/issuing/controls/real-time-authorizations),
and build an integration with [our interactive
guide](https://docs.stripe.com/issuing/controls/real-time-authorizations/quickstart).

Cardholder

Stripe

User

Attempt purchase

`POST issuing_authorization.request`

Make decision

200 Response to `issuing_authorization.request` `{approved: true}` and
`Stripe-Version` header set

Purchase approved

You must respond with an HTTP status code of `200`, a `Stripe-Version` header
set to a specific API version, and a Boolean of `approved` in the JSON body. The
JSON body must correspond with the [specified API
version](https://docs.stripe.com/api/versioning).

For controllable amount authorizations, [partial
approvals](https://docs.stripe.com/issuing/purchases/authorizations?issuing-authorization-type=incremental_authorization#handling-other-authorizations)
optionally include `amount`.

### Direct webhook Authorization API changes

For direct webhook response
[Authorizations](https://docs.stripe.com/api/issuing/authorizations/object),
we’ve made several additions:

- Added value `webhook_error` to
[request_history.reason](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason).
This value is present if the webhook response fails due to validation errors.
- New field `request_history.reason_message`, which includes a detailed error
message if the `request_history.reason` is `webhook_error`.

## Migrate to direct response

You can try the direct webhook response in test mode. As a best practice, we
recommend gradually shifting over from the legacy API call to responding
directly to the webhook.

If you call an API method and include the direct webhook response body, the API
method decision takes priority.

Here’s an example of what a migration to the direct webhook might look like in
Ruby. For other languages, see [our interactive
guide](https://docs.stripe.com/issuing/controls/real-time-authorizations/quickstart).

```
# User's existing API call webhook handling code, using Sinatra.
# In this example, the synchronous webhook and normal webhook share an endpoint.
post '/webhook' do
 payload = request.body.read

 if event['type'] == 'issuing_authorization.request'
 auth = event['data']['object']
 # Approve with legacy API call.
 Stripe::Issuing::Authorization.approve(auth["id"])
 status 200
 elsif event['type'] == 'issuing_authorization.created'
 auth = event['data']['object']
 # If approved, will print "webhook_approved"
 puts "#{auth["request_history"][-1]["reason"]}"
 status 200
 end
end
```

After testing in test mode, gradually shift traffic to the direct webhook
response.

```
# User's API call and direct response webhook handling code, using Sinatra.
# In this example, the synchronous webhook and normal webhook share an endpoint.
post '/webhook' do
 payload = request.body.read

 if event['type'] == 'issuing_authorization.request'
 auth = event['data']['object']

 # Gradually shift traffic over from API approval to direct webhook response.
 if should_use_direct_webhook_response?(auth["id"])
 # Direct webhook response.

 body {
 # Required field, containing decision.
 "approved": true,
 }.to_json

 header {
# Required in header. Versions can be found in
https://stripe.com/docs/api/versioning
 "Stripe-Version": "2023-08-16"
 }

 # Must respond with a 200.
 status 200
 else
# Legacy API call. Plan to remove this after traffic is completely shifted.
 Stripe::Issuing::Authorization.approve(auth["id"])
 status 200
 end
 elsif event['type'] == 'issuing_authorization.created'
 auth = event['data']['object']

 # If approved, will print "webhook_approved"
 puts "#{auth["request_history"][-1]["reason"]}"

 # Handle new reason value and field
 if auth["request_history"][-1]["reason"] == "webhook_error"
puts "Direct webhook response decision failed:
#{auth["request_history"][-1]["reason_message"]}"
 end
 status 200
 end
end
```

## Links

- [respond directly to a issuing_authorization.request
webhook](https://docs.stripe.com/issuing/controls/real-time-authorizations)
- [approve](https://docs.stripe.com/api/issuing/authorizations/approve)
- [decline](https://docs.stripe.com/api/issuing/authorizations/decline)
- [our interactive
guide](https://docs.stripe.com/issuing/controls/real-time-authorizations/quickstart)
- [specified API version](https://docs.stripe.com/api/versioning)
- [partial
approvals](https://docs.stripe.com/issuing/purchases/authorizations?issuing-authorization-type=incremental_authorization#handling-other-authorizations)
- [Authorizations](https://docs.stripe.com/api/issuing/authorizations/object)
-
[request_history.reason](https://docs.stripe.com/api/issuing/authorizations/object#issuing_authorization_object-request_history-reason)
-
[https://stripe.com/docs/api/versioning](https://stripe.com/docs/api/versioning)