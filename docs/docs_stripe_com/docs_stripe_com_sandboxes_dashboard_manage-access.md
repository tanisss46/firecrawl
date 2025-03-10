# Manage access and API keysDeveloper preview

## Manage who can access a sandbox.

#### Private developer preview

Sandboxes is currently in private developer preview. Join [Stripe
Insiders](https://insiders.stripe.dev/c/sandboxes/6), our new early access
program, to register your interest in joining the Sandboxes preview.

Use the [Stripe Dashboard](https://dashboard.stripe.com/) to grant users access
to your sandbox.

## Manage access

You can manage access to your sandbox using [Team
management](https://docs.stripe.com/get-started/account/teams) in your live
account’s settings or from within a sandbox.

You can assign a role directly to give a user access to a specific sandbox. You
can also assign a role in a sandbox different from the role the user has in
other sandboxes, or in your live account. You must also assign a user a role in
the live account to assign them a role in a sandbox.

## Manage API keys

Stripe uses the API keys associated with a sandbox to authenticate API requests
made to the applicable sandbox environment. We raise an [invalid request
error](https://docs.stripe.com/error-handling#invalid-request-errors) if you
don’t include a key and an [authentication
error](https://docs.stripe.com/error-handling#authentication-errors) if the key
is incorrect or outdated.

Use the [Developer Dashboard](https://dashboard.stripe.com/test/apikeys) within
the sandbox to reveal, revoke, and create API keys. Learn more about [API
keys](https://docs.stripe.com/keys).

## Grant users access to all sandboxes

When you assign the Sandbox Administrator role to a team member, you give them
access to every sandbox linked to your live business account.

To add more team members to all sandboxes connected to your live business
account:

- Navigate to your live account in the Dashboard.
- Click **Settings** in the top right corner.
- Click **Team and security** > **+ Add member**, then enter one or more email
addresses. Select the [Sandbox Administrator
role](https://docs.stripe.com/get-started/account/teams/roles).
- Click **Send invites**.

#### Note

When you grant a team member the Sandbox Administrator role, you’re granting
access to all sandboxes associated with your live account.

## Grant users access for testing only

When you grant a team member the Sandbox User role, you’re granting them access
to create sandboxes associated with your live business account and delete
sandboxes they’ve created.

To invite additional team members to *only* sandboxes associated with your live
business account without any access to your live business details:

- Navigate to your live business account in the Dashboard.
- Click **Settings** in the top right corner.
- Click **Team and security** > **+ Add member**, then enter one or more email
addresses. Select the [Sandbox User
role](https://docs.stripe.com/get-started/account/teams/roles).
- Click **Send invites**.

## Grant users access to a specific sandbox

To invite additional team members to a specific sandbox associated with your
live business account, or to invite a user to a specific sandbox that they
didn’t create:

- Navigate to your live account in the Dashboard.
- Click **Settings**.
- Click **Team and security** > **+ Add member**, then enter one or more email
addresses. Select a [Sandbox
role](https://docs.stripe.com/get-started/account/teams/roles).
- Click **Send invites**.
- Navigate to a sandbox in the Dashboard.
- Click **Settings**.
- Click **Team and security** > **+ Add member**, then enter the same email
addresses. Select a
[role](https://docs.stripe.com/get-started/account/teams/roles).
- Click **Send invites**.

## Revoke user access to sandboxes

To revoke a user’s access:

- Navigate to the live account or sandbox where that user has a role assignment
in the Dashboard.
- Click **Settings**.
- Click the overflow menu (), then click **Edit**.
- Remove the [Sandbox
role](https://docs.stripe.com/get-started/account/teams/roles).

## Links

- [Stripe Insiders](https://insiders.stripe.dev/c/sandboxes/6)
- [Stripe Dashboard](https://dashboard.stripe.com/)
- [Team management](https://docs.stripe.com/get-started/account/teams)
- [invalid request
error](https://docs.stripe.com/error-handling#invalid-request-errors)
- [authentication
error](https://docs.stripe.com/error-handling#authentication-errors)
- [Developer Dashboard](https://dashboard.stripe.com/test/apikeys)
- [API keys](https://docs.stripe.com/keys)
- [Sandbox Administrator
role](https://docs.stripe.com/get-started/account/teams/roles)