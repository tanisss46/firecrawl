# Get started with the Stripe CLI

## Build, test, and manage your Stripe integration directly from the command line.

The Stripe CLI is a developer tool to help you build, test, and manage your
integration with Stripe directly from the command line. It works on macOS,
Windows, and Linux, and offers a range of functionality to enhance your
developer experience with Stripe. You can use the Stripe CLI to:

- Create, retrieve, update, or delete any of your Stripe resources in a sandbox
(for example, create a product)
- Stream real-time API requests and events happening in your account
- Trigger events to test your webhooks integration

[View the full CLI reference](https://docs.stripe.com/cli).

Try it online[Install the Stripe
CLI](https://docs.stripe.com/stripe-cli#install)
From the command-line, use an install script or download and extract a versioned
archive file for your operating system to install the CLI.

homebrewaptyumScoopmacOSLinuxWindowsDocker
To install the Stripe CLI with [homebrew](https://brew.sh/), run:

```
brew install stripe/stripe-cli/stripe
```

[Log in to the CLI](https://docs.stripe.com/stripe-cli#login-account)- Log in
and authenticate your Stripe user
[Account](https://docs.stripe.com/get-started/account/activate) to generate a
set of *restricted keys*. To learn more, see [Stripe CLI keys and
permissions](https://docs.stripe.com/stripe-cli/keys).

```
stripe login
```

Press the **Enter** key on your keyboard to complete the authentication process
in your browser.

```
Your pairing code is: enjoy-enough-outwit-win
This pairing code verifies your authentication with Stripe.
Press Enter to open the browser or visit
https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1
(^C to quit)
```

- (Optional) If you don’t want to use a browser, use the `--interactive` flag to
authenticate with an existing API secret key or restricted key. This is helpful
when authenticating to the CLI without a browser, such as in a CI/CD pipeline.

```
stripe login --interactive
```

- (Optional) Use the `--api-key` flag to specify your API secret key inline each
time you send a request.

```
stripe login --api-key sk_test_BQokikJOvBiI2HlWgH4olfQ2
```

[Get started with a video](https://docs.stripe.com/stripe-cli#get-started)
Watch this video to learn different ways to use the Stripe CLI. It covers how to
configure the CLI, download sample code, and work with Stripe objects.

## Next steps

- [Stream real-time events with the Stripe
CLI](https://docs.stripe.com/webhooks#local-listener)
- [View the full CLI reference](https://docs.stripe.com/cli)

## Links

- [View the full CLI reference](https://docs.stripe.com/cli)
- [homebrew](https://brew.sh/)
- [Account](https://docs.stripe.com/get-started/account/activate)
- [Stripe CLI keys and permissions](https://docs.stripe.com/stripe-cli/keys)
-
[https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1](https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1)
- [Stream real-time events with the Stripe
CLI](https://docs.stripe.com/webhooks#local-listener)