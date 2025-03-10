# Manage sandboxesDeveloper preview

## Manage and organize your sandboxes in the Dashboard.

#### Private developer preview

Sandboxes is currently in private developer preview. Join [Stripe
Insiders](https://insiders.stripe.dev/c/sandboxes/6), our new early access
program, to register your interest in joining the Sandboxes preview.

You can use sandboxes for many common development needs. For example, you can:

- Create a sandbox development environment for each member of your team.
- Create a sandbox for a team within your organization.
- Create a sandbox specifically for testing a new Stripe feature or a Stripe API
upgrade.
- Create a sandbox that mirrors live mode, so you can test and stage changes to
your integration before you go live.

Use the [Stripe Dashboard](https://dashboard.stripe.com/) or the Stripe CLI to
manage your sandbox.

## Create a sandbox

If you have the [Sandbox Administrator, Administrator, Developer, or Sandbox
User role](https://docs.stripe.com/get-started/account/teams/roles), you can
create a new sandbox. Your account can have up to five sandboxes.

To create a sandbox:

- Click the account picker > **Sandboxes** > **Create sandbox** in the
Dashboard.
- Enter a unique name that reflects the purpose of the sandbox (for example,
“Staging”) in the **Name** field.
- Decide if you want to adjust the toggle that [copies selected
settings](https://docs.stripe.com/sandboxes/dashboard/sandbox-settings) you
already have configured in your live account. Stripe copies these settings by
default.
- Click **Create**.

Stripe automatically assigns the Super Administrator role to any user that
creates a sandbox. This role allows them to carry out all operations within that
particular sandbox.

## View a sandbox

If you have the Sandbox Administrator role, you can view all sandboxes. If you
have a Developer role, you can only view the sandboxes you’ve created. The roles
associated with a sandbox won’t change your access to test mode, allowing all
team members to continue accessing test mode.

- Click the account picker > **Sandboxes** in the Dashboard.
- Click **Open** to enter the sandbox.

The banner at the top of the Dashboard indicates that you’re in a sandbox. You
can navigate to any other part of the Dashboard.

### View your current sandbox in the CLI

To display the sandbox you’re currently using, run the following command:

```
stripe preview whoami
```

```
 Default Sandbox {{SANDBOX_ID}}

```

## Update a sandbox

Any member of your team with the Sandbox Administrator role can update the name
and details of any sandbox. Developers can only update the name and details of a
sandbox that they’ve created.

- Click the account picker > **Sandboxes** in the Dashboard, then select a
sandbox.
- Click **Settings** in the top right corner.
- Update the name or additional details about your sandbox’s account (for
example, the branding).

## Delete a sandbox

If you have the Administrator or Sandbox Administrator role, you can delete a
sandbox. Otherwise, only the sandbox’s owner can delete it.

- Click the account picker > **Sandboxes** in the Dashboard.
- Click the trash can icon associated with the sandbox.
- Confirm that you want to delete this sandbox as this action can’t be undone.
After deletion, we remove all data associated with the sandbox and revoke
access.

#### Note

Deleting a sandbox deletes all the data associated with the sandbox and removes
access for any other team members who had access to the sandbox.

## Switch to a sandbox in the CLI

You can switch the sandbox you’re operating on in your CLI. To switch to a
different sandbox, run the following command:

```
stripe preview use
```

```
You are currently operating on Default Sandbox ({{SANDBOX_ID}})

* indicates your active workspace. Use the arrow keys to navigate: ↓ ↑ → ←
? Select the sandbox you'd like to use:
 ▸ * Default Sandbox {{SANDBOX_ID}}
 QA Team Sandbox {{SANDBOX_ID}}
 Developer Sandbox {{SANDBOX_ID}}

```

Next, select the sandbox you want to switch to.

## Links

- [Stripe Insiders](https://insiders.stripe.dev/c/sandboxes/6)
- [Stripe Dashboard](https://dashboard.stripe.com/)
- [Sandbox Administrator, Administrator, Developer, or Sandbox User
role](https://docs.stripe.com/get-started/account/teams/roles)
- [copies selected
settings](https://docs.stripe.com/sandboxes/dashboard/sandbox-settings)