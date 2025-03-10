# Get started with the Stripe Shell

## Get started with the Stripe Shell on any page in the Stripe docs site.

This page describes how to launch the Stripe Shell terminal window from any page
on the Stripe docs site and how to get started.

## Initial setup

- To begin, you need a Stripe account. If you don’t already have one, [follow
these instructions](https://dashboard.stripe.com/register).
- Click **Sign in** to authenticate with your Stripe account’s test API *secret
key*.
[Listen for events](https://docs.stripe.com/stripe-shell/launch#listen)- Press
the `Control` + `Backtick` (on Windows, Linux or macOS) keys on your keyboard to
launch the Stripe Shell.
- Click the **stripe listen** command to listen for
[events](https://docs.stripe.com/event-destinations), or type the command and
press the **Enter** key on your keyboard.

```
stripe listen
```

This launches a Stripe Shell session inside a new frame at the bottom of the
site and displays a command-line terminal.

[Run your first request](https://docs.stripe.com/stripe-shell/launch#first)-
Press the `Alt` + `Shift` + `D` (on Windows, Linux) or `Command` + `D` (on
macOS) keys on your keyboard to open a new pane.
- Click the green *play* button to run the command, or copy and paste the
command and press the `Enter` key on your keyboard.
- the Stripe resource identifier (in `id`) in the response for subsequent
requests.

```
stripe products create \
--name="Introductory offer (Monthly)" \
--description="$0.99 per month"
```

This creates a product with a name and description.

[Get started with a
video](https://docs.stripe.com/stripe-shell/launch#get-started)
Watch this video to learn all of the different ways to use the Stripe Shell.

## Next steps

- [Keyboard shortcuts in the Stripe
Shell](https://docs.stripe.com/stripe-shell/keyboard-shortcuts)

## Links

- [follow these instructions](https://dashboard.stripe.com/register)
- [events](https://docs.stripe.com/event-destinations)
- [Keyboard shortcuts in the Stripe
Shell](https://docs.stripe.com/stripe-shell/keyboard-shortcuts)