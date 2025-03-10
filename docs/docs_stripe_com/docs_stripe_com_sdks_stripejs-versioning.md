# Stripe.js versioning and support policy

## Learn about the Stripe.js versioning and support policy.

Stripe.js uses an evergreen model, which means it receives updates continuously
over time. Stripe.js v3, the scripts backing `js.stripe.com/v3`, was the most
recent version of Stripe.js for many years. We release new major versions such
as [Acacia](https://docs.stripe.com/changelog/acacia) on a biannual basis. These
versions allow us to introduce major features and breaking changes on a
predictable schedule, so you can plan your upgrades.

## Types of changes

Changes to Stripe.js fall into two main categories:

### Optimizations and new features

The most common type of change we make to Stripe.js are optimizations and new
features.

We add new features, make optimizations, and fix bugs such as critical security
issues, without any required integration changes. This happens automatically for
all Stripe.js integrations, and will continue for all versions of Stripe.js. All
versions continue to get these non-breaking updates and are regularly updated
together in our internal release process.

Some examples of optimizations we consider to be non-breaking:

- Changing the input labels in the Payment Element to be more accessible.
- Updating the UI within Payment Element for BNPL redirects to increase
conversion.
- Adding a new parameter that allows you to specify when you don’t want to
submit a postal code for a card charge.

Some changes require integration changes to gain access to, but aren’t breaking
changes. One example might be adding a new function on the Stripe object. We
safely release these features across some existing Stripe.js versions in our
regular release process. This process is called *backporting*.

### Breaking changes

The Stripe.js versioning system is a tool that enables us to release new
features that might otherwise be constrained by our need to support backward
compatibility. We release these breaking changes in the [Stripe release
trains](https://stripe.com/blog/introducing-stripes-new-api-release-process),
done twice per year.

A breaking change is something that could cause your integration to fail or
appear broken. For example:

- Removing a parameter or support for a specific option. For example, no longer
allowing `captureMethod: manual` for `stripe.elements()`.
- Removing an input field that you might rely on from a payment method. For
example, no longer collecting `country` for Klarna payments.
- Changes that could cause your checkout page to appear visually broken or
confusing. For example, changing the default behavior for Payment Element layout
from tabs to accordion could cause display issues if your page makes certain
assumptions about the element in the flow of the page.

## Usage

There are three ways to use versioned Stripe.js: with a script tag, with the
`@stripe/stripe-js` package on npm, or with the `@stripe/react-stripe-js`
package on npm.

### With a script tag

To use versioned Stripe.js, include the version name in the script tag’s URL.

```
<script src="https://js.stripe.com/acacia/stripe.js"></script>
```

We recommend that you stay up to date with the latest version of Stripe.js.
Stripe.js v3 is no longer recommended for integrations, but we’ll continue to
support it.

### With stripe-js on npm

If you use Stripe.js with the `@stripe/stripe-js` package on npm, you can
continue to consume Stripe.js this way. Starting with `@stripe/stripe-js@6.0.0`,
each major version of Stripe.js consumes a specific fixed version of Stripe.js.
For example, `@stripe/stripe-js@6.0.0` consumes Stripe.js `acacia`. For
information about the relationships between specific `@stripe/stripe-js`
versions and their corresponding Stripe.js versions, see the [releases
page](https://github.com/stripe/stripe-js/releases).

### With react-stripe-js on npm

The `@stripe/react-stripe-js` package continues to work with the
`@stripe/stripe-js` package using its `peerDependencies`.

## Version lifecycle

We release Stripe.js major versions alongside the [API release
trains](https://stripe.com/blog/introducing-stripes-new-api-release-process)
twice per year. We release non-breaking changes, including both optimizations
and backported features, on our ongoing frequent release schedule. We continue
to support and update older versions.

## Compatibility with API versions

When performing API requests, each versioned Stripe.js automatically uses the
API version associated with the Stripe.js version. That is, the Stripe.js
`acacia` version uses a compatible API version such as `2024-12-18.acacia`
(which includes the date) to represent the release date of the API version. You
can’t override the API version.

## Changelog

The [changelog](https://docs.stripe.com/changelog) shows the history of
versioned changes in Stripe.js over time. It includes all breaking changes and
other important changes and is the best place to understand what integration
changes you need to make to upgrade Stripe.js versions.

## Migrate from Stripe.js v3

Review the following considerations before you upgrade from Stripe.js v3 to a
newer version.

### API changes

When you update Stripe.js to `acacia` from v3, this might cause breaking changes
for API requests, depending on the API version you previously used for the
requests. To upgrade older accounts, we recommend that you [identify the current
API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
used in your account. Then identify the
[changes](https://docs.stripe.com/changelog) that affect your Stripe.js
integration, and upgrade the [API version used by your Stripe.js
integration](https://docs.stripe.com/js/initializing#init_stripe_js-options-apiVersion)
to `2024-12-18.acacia` gradually (if it makes sense for your needs) before
upgrading Stripe.js to `acacia`.

### API beta

API versions can contain breaking changes for
[previews](https://docs.stripe.com/release-phases) that aren’t listed in the
changelog, so you need to upgrade your Stripe.js version carefully if you’re on
a preview such as the [Elements with Checkout Sessions
beta](https://docs.stripe.com/checkout/elements-with-checkout-sessions-api/changelog).

Historically, some preview features involved adding beta headers to your
`apiVersion` used by Stripe.js requests (for example, `'2025-02-24.acacia;
custom_checkout_beta=v1'`). Because we no longer support this API version
override, you can’t explicitly add beta headers directly to API requests.
Instead, any supported Stripe.js previews add necessary headers automatically
when the corresponding beta flag (for example `custom_checkout_beta_5`) is set
when you initialize Stripe.js.

For `acacia`, this is expressly supported for `custom_checkout_beta` and
`nz_bank_account_beta`. If you provide API headers for other previews, contact
the email provided to you for preview support to determine your options for
upgrading Stripe.js or migrating to GA behavior.

### Support for Stripe.js v3

We’ll continue to support `js.stripe.com/v3` for the foreseeable future. We’ll
backport features to this version and continue to maintain Stripe.js v3 as an
evergreen version. Stripe.js v3 isn’t deprecated, but we encourage you to
regularly update your applications to the newest version of Stripe.js to access
recent features that can’t be backported because of their breaking changes.

## Links

- [Acacia](https://docs.stripe.com/changelog/acacia)
- [Stripe release
trains](https://stripe.com/blog/introducing-stripes-new-api-release-process)
-
[https://js.stripe.com/acacia/stripe.js](https://js.stripe.com/acacia/stripe.js)
- [releases page](https://github.com/stripe/stripe-js/releases)
- [changelog](https://docs.stripe.com/changelog)
- [identify the current API
version](https://docs.stripe.com/upgrades#view-your-api-version-and-the-latest-available-upgrade-in-workbench)
- [API version used by your Stripe.js
integration](https://docs.stripe.com/js/initializing#init_stripe_js-options-apiVersion)
- [previews](https://docs.stripe.com/release-phases)
- [Elements with Checkout Sessions
beta](https://docs.stripe.com/checkout/elements-with-checkout-sessions-api/changelog)