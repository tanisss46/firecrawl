# Activate PayPal payments

## Learn how to activate PayPal payments when you're ready to go live.

You can activate the PayPal payment method directly from the Stripe Dashboard.

- Go to the [Payment Methods settings
page](https://dashboard.stripe.com/settings/payment_methods).
- Locate PayPal in the **Wallets** section.
- Click **Turn on**.
- Select your **settlement preference**. If you select **Add PayPal funds to
your Stripe balance**, PayPal money flow is similar to other payment methods at
Stripe. If you select **Keep PayPal funds in PayPal balance**, you’ll need to
manage payouts on PayPal with the option to automate the frequency of payouts.
Find more information about [settlement
modes](https://docs.stripe.com/payments/paypal/choose-settlement-preference).
- Click **Continue to PayPal** to complete the integration and connect your
Stripe and PayPal accounts. You can connect an existing PayPal account or create
a new one as part of the process.
- After clicking **Continue to PayPal**, PayPal redirects you back to Stripe
where you can check the status of your integration on the **Payment Methods
settings** page.

#### Note

In some cases, you might see your integration appear in a **pending** state
after connecting your Stripe and PayPal accounts, which can happen for the
following reasons:

- You haven’t confirmed the email address to activate your PayPal account.
- PayPal needs to perform additional verifications on your account. If you’ve
verified all of these possibilities and think they don’t apply to your PayPal
account, please [contact Stripe Support](https://support.stripe.com/) and we’ll
help you resolve the issue.

Currently, only PayPal business accounts in the European Economic Area
(excluding Hungary), the UK, and Switzerland are supported.

### Connect users

- Check whether your Connect configuration [is compatible with
PayPal](https://docs.stripe.com/payments/paypal#connect).
- If your use case is supported, request PayPal access by submitting an
onboarding request from the [Stripe
Dashboard](https://dashboard.stripe.com/settings/payment_methods).
- Receive a confirmation email from Stripe.
- Prepare the following documents to provide to PayPal:- Your Acceptable User
Policy (AUP) or Terms & Conditions (T&C).
- Details of the controls you have in place to make sure that sellers conform to
your policies and terms. Examples of controls include web screening, ongoing
reviews of top sellers, and restricting sellers to a fixed list of items they
can offer.
- A PayPal representative contacts you directly over phone and email to complete
the onboarding. Provide them with the documents that you prepared in the
previous step.

Stripe sends email updates about the progress of onboarding requests. You can
also check your onboarding status in your [Payment Methods
settings](https://dashboard.stripe.com/settings/payment_methods).

## Switch to a different PayPal account Not supported with Stripe Connect

You can switch to a different PayPal account in your Dashboard. It can be an
existing account, or you can create a new one.

Connect platforms and connected accounts can’t switch PayPal accounts.

#### Caution

If you have recurring payments enabled, switching PayPal accounts disables them.
After switching accounts, you must re-enable recurring payments and collect
mandates from buyers again.

- Go to the [Payment Methods settings
page](https://dashboard.stripe.com/settings/payment_methods).
- In the **Wallets** section, find **Paypal**.
- Expand the **PayPal** section.
- Click **Switch account**.
- Read the information dialog.
- Click **Switch PayPal account**.

Switching accounts doesn’t take effect immediately. Payments continue to flow
through your previous account until the new account is successfully connected.

After switching PayPal accounts, payments processed with your previous account
are still eligible for refunds and disputes.

In some cases, you might see your new PayPal account appear in a pending state
on the Stripe dashboard. That can happen for the following reasons:

- You haven’t confirmed the email address to activate the new PayPal account.
- PayPal needs to perform additional verifications on the new account. If you
believe that you’ve fulfilled all of the PayPal requirements, contact Stripe
Support.

## Start accepting PayPal payments

See how to [accept PayPal
payments](https://docs.stripe.com/payments/paypal/accept-a-payment) at Stripe.

## Links

- [Payment Methods settings
page](https://dashboard.stripe.com/settings/payment_methods)
- [settlement
modes](https://docs.stripe.com/payments/paypal/choose-settlement-preference)
- [contact Stripe Support](https://support.stripe.com/)
- [is compatible with PayPal](https://docs.stripe.com/payments/paypal#connect)
- [accept PayPal
payments](https://docs.stripe.com/payments/paypal/accept-a-payment)