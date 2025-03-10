# Communicating state for Stripe Apps

## Learn how to guide users to take actions in your app.

Keep the user informed by showing them when they need to take a certain action.

## Before you begin

[Create an app](https://docs.stripe.com/stripe-apps/create-app).

## Suggested use

- Use a [Toast](https://docs.stripe.com/stripe-apps/components/toast) component
to provide temporary feedback after users take an action.
- Use a [Banner](https://docs.stripe.com/stripe-apps/components/banner)
component to show users they need to take action on unexpected system-level
requirements, changes, or issues. For example:

![On the left, a green check Toast on download. On the right, a red Notice on
error.](https://b.stripecdn.com/docs-statics-srv/assets/communicating-state.a613d037f8e0b3bd8a6aa7199e708c8d.png)

## Examples

Consider the following attributes when choosing to deliver a message.

ToastBanner

![Green check Toast example with text 'Changes
saved'](https://b.stripecdn.com/docs-statics-srv/assets/Toast.e17b36572b25d60725b4bc24098b77b9.png)

![ Banner example with text 'New
updates'](https://b.stripecdn.com/docs-statics-srv/assets/Notice.0435a3a4999b7189e67fba5c18dae242.png)

**Display**

**Temporary**

All toasts trigger on users’ actions. Toasts dismiss automatically after a short
period or when the app closes.

**Persistent**

You can deliver banners at any time. Dismissing a banner requires an action.

**Content**

**Limited text length**

Messages for toasts should be short, and fewer than four words on one line. The
maximum character length for a toast is 30.

**Medium to long message**

Banners contain title and body text. Banners are suitable for providing
information with additional details.

**Action**

**Optional**

Provide an action as a shortcut for users to quickly enter the related event.

**Required**

Inform users to take the required action.

PositionBottom of the app drawerUnder app drawer header

## Links

- [Create an app](https://docs.stripe.com/stripe-apps/create-app)
- [Toast](https://docs.stripe.com/stripe-apps/components/toast)
- [Banner](https://docs.stripe.com/stripe-apps/components/banner)