# SandboxesDeveloper preview

## Test Stripe functionality in an isolated environment.

#### Private developer preview

Sandboxes is currently in private developer preview. Join [Stripe
Insiders](https://insiders.stripe.dev/c/sandboxes/6), our new early access
program, to register your interest in joining the Sandboxes private preview.
Email us at
[sandboxes-feedback@stripe.com](mailto:sandboxes-feedback@stripe.com) with
feedback about Sandboxes.

A sandbox is an isolated test environment. You can use your sandbox to test
Stripe functionality in your account, and experiment with new features without
affecting your live integration. For example, when testing in a sandbox, the
payments you create aren’t processed by card networks or payment providers.

## Use cases

ScenarioDescriptionSimulate Stripe events to test without real money movementUse
your sandbox to test payments functionality without real money movement. Create
payments in your business account to accumulate a fake balance or use test
helpers to simulate external events.Scale isolated sandboxes for teamsYour team
can [test in separate
sandboxes](https://docs.stripe.com/sandboxes/dashboard/manage#create-a-sandbox)
to make sure that data and actions are completely isolated from other sandboxes.
Changes made in one sandbox don’t interfere with changes in another.Invite
external users[You can invite another
user](https://docs.stripe.com/sandboxes/dashboard/manage-access#grant-users-access-to-a-specific-sandbox),
such as implementation partner or design agency, to access all sandboxes, or a
specific sandbox, without providing them access to your live mode data.Test in
the Dashboard or the CLIAccess your sandbox from the Dashboard or the [Stripe
CLI](https://docs.stripe.com/cli-preview-plugin). Test Stripe functionality
directly in the Dashboard or use familiar CLI commands and
[fixtures](https://docs.stripe.com/cli/fixtures).
## Manage sandboxes in the Dashboard

To access sandboxes, click **Sandboxes** within the Dashboard account picker.
Depending on your permissions, you can view, create, delete, and open sandboxes
from the sandboxes overview page. To manage user access and API keys for a
specific sandbox, first open the sandbox and then manage those settings directly
within the sandbox.

## Test in a sandbox

You can simulate payments and use test cards to test your integration without
moving money. Learn more about [using test cards to confirm that your
integration works correctly](https://docs.stripe.com/testing).

## Limitations

- You can’t test
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
pricing in a sandbox.
- You can’t use [Sigma](https://stripe.com/sigma) in a sandbox.
- You can’t test [Issuing](https://docs.stripe.com/issuing) in a sandbox.

## Links

- [Stripe Insiders](https://insiders.stripe.dev/c/sandboxes/6)
- [test in separate
sandboxes](https://docs.stripe.com/sandboxes/dashboard/manage#create-a-sandbox)
- [You can invite another
user](https://docs.stripe.com/sandboxes/dashboard/manage-access#grant-users-access-to-a-specific-sandbox)
- [Stripe CLI](https://docs.stripe.com/cli-preview-plugin)
- [fixtures](https://docs.stripe.com/cli/fixtures)
- [using test cards to confirm that your integration works
correctly](https://docs.stripe.com/testing)
-
[IC+](https://support.stripe.com/questions/understanding-blended-interchange-pricing)
- [Sigma](https://stripe.com/sigma)
- [Issuing](https://docs.stripe.com/issuing)