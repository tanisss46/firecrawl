# Verification flows

## Apply a reusable configuration across your integration.

Flows provide a way to save and reuse the same configuration across all of your
integration interfaces. You can use each flow to create verification sessions
through the API, in the Dashboard, or through the flow’s static link. Flows
support the management of different verification use cases and can help ensure
consistency across your integration.

## Create flows

To set up your Identity integration, first create a flow to store your desired
configuration:

- Visit the [Verification
flows](https://dashboard.stripe.com/identity/verification-sessions) page in your
Dashboard.
- Name the flow.
- Configure the verification behavior you want.
- Click **Save**.

### Manage flows

The [Verification
flows](https://dashboard.stripe.com/identity/verification-flows) page displays
all of your flows. You can create distinct flows for different use-cases, such
as:

- Marketing campaigns
- High-value versus low-value transactions
- Known high-risk users versus trusted users
- Any other relevant use case

After you create a flow, you can visit the details page to:

- View details and edit the flow
- View a list of all the verifications created from the flow
- Activate or deactivate the flow’s static link

### Update flows

You can use flows to deploy a new configuration to production. For example, if
you want to add selfie checks to your document verifications, you can edit the
flow in the Dashboard to add selfie verification. Any future verifications you
create with this flow automatically adopt the updated configuration, so make
sure to only apply changes that you want to adopt for future verifications.

## Use flows to verify users

After you create a flow, you have two options for how to initiate an identity
verification using it.

APINo-code
To use flows in your API integration, copy the flow ID from the details page and
pass it in the
[verification_flow](https://docs.stripe.com/api/identity/verification_sessions/create#create_identity_verification_session-verification_flow)
parameter when you create a verification session.

```
curl https://api.stripe.com/v1/identity/verification_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d verification_flow={{VERIFICATION_FLOW_ID}}
```

### Include user-specific details

As with any verification session that you create with the API, you can attach
user-specific data with the
[metadata](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-metadata)
and
[provided_details](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-provided_details)
parameters. The
[client_reference_id](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-client_reference_id)
parameter provides a reference to a user in your system that you can look up
later.

For example, here’s how you can attach a user-specific phone number, email
address, and `client_reference_id` to a verification session:

```
curl https://api.stripe.com/v1/identity/verification_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -d verification_flow={{VERIFICATION_FLOW_ID}} \
 -d "provided_details[phone]"=5555551212 \
 --data-urlencode "provided_details[email]"="user@domain.com" \
 -d client_reference_id=reference-token
```

## Links

- [Verification
flows](https://dashboard.stripe.com/identity/verification-sessions)
- [Verification flows](https://dashboard.stripe.com/identity/verification-flows)
-
[verification_flow](https://docs.stripe.com/api/identity/verification_sessions/create#create_identity_verification_session-verification_flow)
-
[metadata](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-metadata)
-
[provided_details](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-provided_details)
-
[client_reference_id](https://docs.stripe.com/api/identity/verification_sessions/object#identity_verification_session_object-client_reference_id)