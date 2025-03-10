# Stripe versioning and support policy

## Learn about Stripe's versioning and support policy.

## Stripe API versions

Starting with the 2024-09-30.acacia release, Stripe follows a [new API release
process](https://stripe.com/blog/introducing-stripes-new-api-release-process)
where we release new API versions monthly with no breaking changes. Twice a
year, we issue a new release (for example, `acacia`) that starts with an API
version that will have breaking changes.

You can expect new minor versions of the SDKs with each monthly API version and
new major versions of the SDKs with each of the twice a year major releases.

You may sometimes see a major version update to the SDKs with the monthly API
version updates if the SDKs have breaking changes to ship.

To understand what to expect from a new API version, see [API
upgrades](https://docs.stripe.com/upgrades).

## Stripe SDK versions

Stripe’s SDK versioning policy is based on the semantic versioning standard. For
example, in version 4.3.2, 4 is the *major*, 3 is the *minor*, and 2 is the
*patch*. When we release a new SDK version for new features or bug fixes, we
increment one of these three version components depending on the type of change
introduced.

- **Major**. We increment the *major* version component when the version
contains breaking changes that are backwards incompatible with the latest
version: to add a required parameter, change a type, property, method, or
parameter. For example, renaming the SDK’s exception classes.
- **Minor**. We increment the *minor* version component when the version
contains new features that are backwards compatible with the latest version: to
add a new type, property, method, optional parameter, or supported parameter
value. For example, clarifying the SDK’s metadata deletion message.
- **Patch**. We increment the *patch* version component when the version
contains backward-compatible bug fixes: to modify a behavior if correcting that
behavior doesn’t change any documented types, properties, methods, or
parameters. For example, fixing a bug where file uploads weren’t listed
properly.

You can test new features and enhancements in the
[preview](https://docs.stripe.com/release-phases) stage by using versions of our
SDKs that have the beta or b suffix. For example, 5.1.0b3 in Python and
5.1.0-beta.3 in other language SDKs.

For installation instructions or details about passing preview headers in the
Stripe-Version header, check the README files in the respective SDK GitHub
repositories.

## Stripe SDK support policy

New features and bug fixes are released on the latest *major* version of the
SDK. If you’re on an older *major* SDK version, we recommend upgrading to the
latest major version to take advantage of these features and bug fixes. Older
major versions of the package continue to be available for use, but won’t
receive any additional updates.

### Migration guides

We provide migration guides to help you upgrade from older major SDK versions.
You can find them in the wiki section of our SDK GitHub repositories.

- [Python SDK wiki](https://github.com/stripe/stripe-python/wiki)
- [.NET SDK wiki](https://github.com/stripe/stripe-dotnet/wiki)
- [Java SDK wiki](https://github.com/stripe/stripe-java/wiki)
- [Go SDK wiki](https://github.com/stripe/stripe-go/wiki)
- [PHP SDK wiki](https://github.com/stripe/stripe-php/wiki)
- [Ruby SDK wiki](https://github.com/stripe/stripe-ruby/wiki)
- [Node.js SDK wiki](https://github.com/stripe/stripe-node/wiki)

## See also

- [Set a Stripe API version](https://docs.stripe.com/sdks/set-version)

## Links

- [new API release
process](https://stripe.com/blog/introducing-stripes-new-api-release-process)
- [API upgrades](https://docs.stripe.com/upgrades)
- [preview](https://docs.stripe.com/release-phases)
- [Python SDK wiki](https://github.com/stripe/stripe-python/wiki)
- [.NET SDK wiki](https://github.com/stripe/stripe-dotnet/wiki)
- [Java SDK wiki](https://github.com/stripe/stripe-java/wiki)
- [Go SDK wiki](https://github.com/stripe/stripe-go/wiki)
- [PHP SDK wiki](https://github.com/stripe/stripe-php/wiki)
- [Ruby SDK wiki](https://github.com/stripe/stripe-ruby/wiki)
- [Node.js SDK wiki](https://github.com/stripe/stripe-node/wiki)
- [Set a Stripe API version](https://docs.stripe.com/sdks/set-version)