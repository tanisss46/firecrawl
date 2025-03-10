# How sessions work

## Learn about the status and lifecycle of VerificationSessions.

Asynchronous verification flows are complex to manage because they depend on
customer interactions that happen outside of your application.
[VerificationSessions](https://docs.stripe.com/identity/verification-sessions)
simplify this by keeping track of the status of the verification flow.

requires_input
When the VerificationSession is created, it has a status of `requires_input` and
is ready for your user to [begin the verification
process](https://docs.stripe.com/identity/verify-identity-documents). We
recommend creating the VerificationSession right before the start of the
verification flow.

processing
As soon as the user submits the session, the VerificationSession moves to
`processing`. Most [verification
checks](https://docs.stripe.com/identity/verification-checks) are processed in
less than 1 minute.

verified
A VerificationSession with a status of `verified` means that the verification
flow is complete. Processing of all the verification checks are complete and
successfully verified.

requires_input
If any of the verification checks fail (for example, because of a manipulated
document), the VerificationSession’s status returns to `requires_input`. You can
find an explanation for the verification failure in the `last_error` field of
the session. If you want your user to attempt verification again, you need to
[Retrieve the
VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/retrieve)
to get a fresh URL or client secret. Details provided by the `provided_details`
field might be shown to your user.

canceled
You may [cancel a
VerificationSession](https://docs.stripe.com/identity/verification-sessions#cancel)
at any point before it’s `processing` or `verified`. This invalidates the
VerificationSession for future submission attempts, and can’t be undone.

## Session events

[Events](https://docs.stripe.com/api/events) are created every time a session
changes status. Here’s a complete list of the VerificationSession [event
types](https://docs.stripe.com/api#event_types):

Event typeDescription`identity.verification_session.created`The session was
[created](https://docs.stripe.com/identity/verification-sessions#create).`identity.verification_session.processing`The
user has successfully submitted their information, and verification checks have
started processing.`identity.verification_session.verified`Processing of all the
[verification checks](https://docs.stripe.com/identity/verification-checks) have
completed, and they’re all successfully
verified.`identity.verification_session.requires_input`Processing of all the
[verification checks](https://docs.stripe.com/identity/verification-checks) have
completed, and at least one of the checks
failed.`identity.verification_session.canceled`The session has been canceled and
future submission attempts have been disabled. This event is sent when a session
is [canceled](https://docs.stripe.com/identity/verification-sessions#cancel) or
[redacted](https://docs.stripe.com/identity/verification-sessions#redact).`identity.verification_session.redacted`The
session was
[redacted](https://docs.stripe.com/identity/verification-sessions#redact). You
must create a [webhook endpoint](https://docs.stripe.com/api/webhook_endpoints)
which explicitly subscribes to this event type to access it. Webhook endpoints
which subscribe to all events will not include this event type.
You might want to take action in response to certain events, such as emailing
your user when a verification fails or succeeds.

Stripe recommends that you listen for events with
[webhooks](https://docs.stripe.com/identity/handle-verification-outcomes).

## See also

- [The Verification Sessions
API](https://docs.stripe.com/identity/verification-sessions)
- [Handle verification
outcomes](https://docs.stripe.com/identity/handle-verification-outcomes)

## Links

- [VerificationSessions](https://docs.stripe.com/identity/verification-sessions)
- [begin the verification
process](https://docs.stripe.com/identity/verify-identity-documents)
- [verification checks](https://docs.stripe.com/identity/verification-checks)
- [Retrieve the
VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/retrieve)
- [cancel a
VerificationSession](https://docs.stripe.com/identity/verification-sessions#cancel)
- [Events](https://docs.stripe.com/api/events)
- [event types](https://docs.stripe.com/api#event_types)
- [created](https://docs.stripe.com/identity/verification-sessions#create)
- [redacted](https://docs.stripe.com/identity/verification-sessions#redact)
- [webhook endpoint](https://docs.stripe.com/api/webhook_endpoints)
- [webhooks](https://docs.stripe.com/identity/handle-verification-outcomes)