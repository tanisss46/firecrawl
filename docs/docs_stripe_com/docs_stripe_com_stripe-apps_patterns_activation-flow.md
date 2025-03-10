# Activation flow for Stripe Apps

## Learn how to build an activation process for users of your Stripe app.

Follow the recommended account activation guidelines on this page.

#### Warning

Make sure users never share their full credential set with Stripe.

## Before you begin

[Create an app](https://docs.stripe.com/stripe-apps/create-app).

## Flow

The ideal sign in flow is:

- **Effortless**—Users can onboard quickly and easily, while staying focused on
the task in front of them, and providing only necessary information.
- **Customizable**—The process can scale up and down according to the user
needs—making onboarding versatile, yet focused.
- **Relevant**—Users can bypass distractions by seeing short headlines and
paragraphs, and only relevant images.

!

## Suggested use

- Your sign in flow must be secure and easy to follow.
- The sign in flow must be the path of least resistance. Avoid unnecessary
steps. For example:

!

- If users need to sign in to an external site, collect sensitive credentials on
that site, not within the Stripe Dashboard to avoid compromising passwords.
- Stick to the recommended set of steps.
- Detect whether a user already has an account for your product and allow them
enter a sign in flow. For example:

!

- Keep the onboarding flow brief and include authorization to connect your
users’ Stripe accounts to your product. For example:

!

- Always redirect users back to Stripe when sign in is complete. For example:

!

## Links

- [Create an app](https://docs.stripe.com/stripe-apps/create-app)