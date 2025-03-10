# Upgrade the Stripe CLI

## Learn how to upgrade the CLI.

Take advantage of the latest features of the Stripe CLI.

## Homebrew

To upgrade the Stripe CLI with [homebrew](https://brew.sh/), run:

```
brew upgrade stripe/stripe-cli/stripe
```

## Scoop

To upgrade the Stripe CLI with [Scoop](https://scoop.sh/), run:

```
scoop update stripe
```

## macOS

To upgrade the Stripe CLI on macOS without homebrew:

- Download the latest `mac-os` tar.gz file of your cpu architecture type from
[GitHub](https://github.com/stripe/stripe-cli/releases/latest).
- Unzip the file: `tar -xvf stripe_[X.X.X]_mac-os_[ARCH_TYPE].tar.gz`.

Optionally, install the binary in a location where you can execute it globally
(for example, `/usr/local/bin`).

## Linux

To upgrade the Stripe CLI on Linux without a package manager:

- Download the latest `linux` tar.gz file from
[GitHub](https://github.com/stripe/stripe-cli/releases/latest).
- Unzip the file: `tar -xvf stripe_X.X.X_linux_x86_64.tar.gz`.
- Move `./stripe` to your execution path.

## Windows

To upgrade the Stripe CLI on Windows without Scoop:

- Download the latest `windows` zip file from
[GitHub](https://github.com/stripe/stripe-cli/releases/latest).
- Unzip the `stripe_X.X.X_windows_x86_64.zip` file.
- Add the path to the unzipped `stripe.exe` file to your `Path` environment
variable. To learn how to update environment variables, see the [Microsoft
PowerShell
documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3#saving-changes-to-environment-variables).

#### Note

Windows anti-virus scanners occasionally flag the Stripe CLI as unsafe. This is
very likely a false positive. For more information, see [issue
#692](https://github.com/stripe/stripe-cli/issues/692) in the GitHub repository.

## Docker

The Stripe CLI is also available as a [Docker
image](https://hub.docker.com/r/stripe/stripe-cli). To install the latest
version, run:

```
docker run --rm -it stripe/stripe-cli:latest
```

## Links

- [homebrew](https://brew.sh/)
- [Scoop](https://scoop.sh/)
- [GitHub](https://github.com/stripe/stripe-cli/releases/latest)
- [Microsoft PowerShell
documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3#saving-changes-to-environment-variables)
- [issue #692](https://github.com/stripe/stripe-cli/issues/692)
- [Docker image](https://hub.docker.com/r/stripe/stripe-cli)