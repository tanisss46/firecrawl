# UI extension developer tools

## Typecheck, lint, and test your code using bundled developer tools.

When you [create an app](https://docs.stripe.com/stripe-apps/create-app) using
the Stripe CLI, the generated package includes development environment tooling
with best practices built in to help you build a UI extension. This document
details the tools that we include and how to modify them (if desired) to suit
your app.

## Type checking

Apps come with [Typescript](https://www.typescriptlang.org/) support, and all of
the supporting packages we ship have type definitions to aid development.
Typescript warnings display in supported code editors automatically, but you can
also check your code using the command line:

```
yarn tsc
```

Your app’s root directory has a `tsconfig.json` file that extends our
recommended configuration in the `@stripe/ui-extension-tools` package. Most
developers won’t need to modify this file, but advanced users can add their own
properties or even remove the `extends` property and create their own Typescript
configuration.

To enable image imports, we include a `ui-extensions.d.ts` type definition file
that references type definitions from the `@stripe/ui-extension-tools` package.
We don’t recommend removing this file because it’s a helpful indicator of what
image types our CLI can process.

## Linting

Linting (checking code for syntax and formatting errors) is an invaluable
developer tool, and apps come with an [ESLint](https://eslint.org/)
configuration. We include best-practice linter rules and also Stripe-specfic
rules to prevent common mistakes. Linting warnings display in supported code
editors automatically, but you can also check your code using the command line:

```
yarn lint
```

The ESLint configuration is in the `package.json` file in the `eslintConfig`
property. It extends the configuration in the `@stripe/ui-extension-tools`
package. Most developers won’t need to modify this configuration, but advanced
users can add their own properties or even remove the `extends` property and
create their own set of linting rules.

## Testing

App developers can [write unit
tests](https://docs.stripe.com/stripe-apps/ui-testing) for their React
components and utility functions using the bundled test harness built with
[Jest](https://jestjs.io/). Run your tests on the command line:

```
yarn test
```

Your app’s root directory has a `jest.config.js` file that extends our
recommended configuration in the `@stripe/ui-extension-tools` package. Most
developers won’t need to modify this file, but advanced users can add their own
properties or even remove the import and create their own configuration.

[OptionalUpdate older apps to use the ui-extension-tools
package](https://docs.stripe.com/stripe-apps/ui-extension-developer-tools#migrating-ui-extension-tools)
## See also

- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)
- [UI testing](https://docs.stripe.com/stripe-apps/ui-testing)

## Links

- [create an app](https://docs.stripe.com/stripe-apps/create-app)
- [Typescript](https://www.typescriptlang.org)
- [ESLint](https://eslint.org)
- [write unit tests](https://docs.stripe.com/stripe-apps/ui-testing)
- [Jest](https://jestjs.io)
- [How UI extensions
work](https://docs.stripe.com/stripe-apps/how-ui-extensions-work)