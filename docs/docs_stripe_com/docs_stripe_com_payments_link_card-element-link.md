# Link in the Card Element

## Enable checkout using Link with the Card Element.

#### Caution

Stripe no longer recommends using the Card Element as part of your Web Elements
integration. To integrate Link, use one of our preferred Elements: the Link
Authentication Element, Express Checkout Element, or Payment Element.

Use [Link](https://docs.stripe.com/payments/link) in the Card Element to save
and autofill payment information for your customers, so they don’t need to enter
their payment details manually.

The Card Element can take on two forms: a single line [Card
Element](https://docs.stripe.com/js/element/other_element?type=card) or split
Elements (like [Card
Number](https://docs.stripe.com/js/element/other_element?type=cardNumber),
[Expiry](https://docs.stripe.com/js/element/other_element?type=cardExpiry), and
[CVC](https://docs.stripe.com/js/element/other_element?type=cardCvc)). When
referring to the Card Element, the following information applies to both forms.

## The Link flow

Single line Card ElementSplit Elements
When Link is enabled, the card input form displays a **Link** button, which an
authenticated customer can click to autofill their payment details. They only
need to authenticate their account once every 90 days on any Link-enabled
business.

![Link autofilling customer payment
details](https://b.stripecdn.com/docs-statics-srv/assets/link-single-ce-returning-user.e50d94e96551810ac4f95c2fabfd33b9.png)

Link autofilling customer payment details

If a customer hasn’t signed up for Link and they click the **Link** button,
they’re asked to add their email address, phone number, and payment method. A
customer can also enter their card details into the Card Element first, and save
that card in a Link account.

![A customer signing up for
Link](https://b.stripecdn.com/docs-statics-srv/assets/link-single-ce-new-user.b8495f2e5258b8cf04b5d43e3a290ec0.png)

A customer signing up for Link

If a returning Link customer clicks the **Link** button and needs to
authenticate, Link asks them to do it with an SMS or email code. After the
customer authenticates, Link loads their previously saved payment details,
allowing them to check out faster.

![Link authenticating a
customer](https://b.stripecdn.com/docs-statics-srv/assets/link-in-ce-dialog.ec3340f0aaa847f610249e7dcc3fb7ad.png)

Link authenticating a customer

We’re continuously optimizing Link to improve checkout conversion, and may
selectively show Link when it’s most beneficial to customers at checkout. You
can expect to see changes over time, including how and when Link appears.

## Link enablement

Link is supported in the [Card
Element](https://docs.stripe.com/js/element/other_element?type=card) globally
for all businesses with granted access and doesn’t require additional fees or
code changes (see note below for details). Link is fully compatible with the
other features you receive from card payments.

Stripe automatically enables Link in the Card Element. You can disable Link for
all instances of the Card Element in your [Payment Method
settings](https://dashboard.stripe.com/settings/payment_methods). In the Link
section, click the overflow menu () next to the Link row, and disable **Link in
Card Element**. This setting applies to both forms of the Card Element. You can
also set the
[disableLink](https://docs.stripe.com/js/elements_object/create_element?type=card#elements_create-options-disableLink)
parameter to `true` to disable Link in the Card Element. You only need to use
one of these controls to hide Link in the Card Element.

Link *isn’t* visible in the Card Element if:

- The parent container that the Card Element is mounted in is too short in
height or narrow in width to display the Link button. Typically, we require a
minimum width of 350px and height of 28px. However, other factors such as font
size, locale, placeholder text, and card icon visibility can also affect these
requirements.
- The Card Element is displayed on a browser that doesn’t support pop-ups,
including in-app browsers. View information about [supported
browsers](https://docs.stripe.com/payments/link/card-element-link#test-link-in-the-card-element).
- The
[Cross-Origin-Opener-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy)
is set to `same-origin`. The Link pop-up must communicate with the page that
opened it, so Link in the Card Element isn’t compatible with configurations that
block this communication.

#### Note

We’re releasing Link in the Card Element in phases. Link for the [single line
Card Element](https://docs.stripe.com/js/element/other_element?type=card) was
released in 2023, followed by Link in [split
Elements](https://docs.stripe.com/js/element/other_element?type=cardNumber) in
late 2023 and early 2024. Only accounts with granted access can see Link in the
Card Element in their [Payment Method
settings](https://dashboard.stripe.com/settings/link) or use Link in production
or in a sandbox. Link isn’t currently supported for Stripe accounts based in
India.

## Use the Card Element and Payment Request Button

You can also use Link with the [Payment Request
Button](https://docs.stripe.com/payments/link/payment-request-button-link). Link
in the Card Element operates independently from Link in the Payment Request
button. If you use both the Payment Request Button and the Card Element, Link
might appear in both during checkout. For more information on when Link appears
in the Payment Request Button, see [Link in the Payment Request
Button](https://docs.stripe.com/payments/link/payment-request-button-link).

## Link and Connect platforms

Link is automatically available to any accounts that access the Card Element
through a Connect platform integration. Depending on a platform’s integration, a
platform may be able to give its users ([connected
accounts](https://docs.stripe.com/connect/enable-payment-acceptance-guide?platform=web#create-account))
the ability to customize their own Link settings in the Dashboard:

### Eligibility requirements for connected platforms

If the following conditions are all met by your platform, then your connected
accounts can manage their Link settings directly in their own Dashboard.

- You use [direct charges](https://docs.stripe.com/connect/direct-charges).
- You create and charge payment methods on your connected accounts.
- Your connected accounts have access to the full Stripe Dashboard.

To set the default state for all connected accounts on your platform:

- Click **Edit settings** under **Your connected accounts** in [Payment Method
settings](https://dashboard.stripe.com/settings/connect/payment_methods).
- Navigate to **Link in the Card Element** in the Link section.

### Ineligible connected platforms

In the following cases, Link is controlled by your platform account settings,
and your connected accounts can’t customize their Link settings for payments
processed through your platform:

- You create payment methods on your platform and then [clone payment
methods](https://docs.stripe.com/connect/direct-charges-multiple-accounts#clone-and-create-direct-charges)
to your connected accounts.
- You use [destination
charges](https://docs.stripe.com/connect/destination-charges) or [separate
charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers).
- Your connected accounts don’t have access to the full Stripe Dashboard.

To manage your platform account settings:

- Click **Edit settings** under **Your Account** in [Payment Method
settings](https://dashboard.stripe.com/settings/connect/payment_methods).
- Navigate to **Link in the Card Element** in the Link section. If you want to
turn Link off for only specific connected accounts, you can use the
[disableLink](https://docs.stripe.com/js/elements_object/create_element?type=card#elements_create-options-disableLink)
parameter.

### Payment processing for connected accounts

- If your platform offers you the ability to customize your Link settings for
platform payments, then you can manage your Link in Card Element settings within
[Payment Method settings](https://dashboard.stripe.com/settings/payment_methods)
by selecting your platform from the dropdown menu at the top of the page.
- If your platform isn’t able to offer you settings customization, then the
platform determines Link’s availability for all payments processed through the
platform, and you won’t have settings control for platform payments in your
Dashboard.
- For payments you process without a platform, you can manage Link in your
[Payment Method settings](https://dashboard.stripe.com/settings/payment_methods)
by selecting “no platform” from the dropdown menu at the top of the page.

## Test Link in the Card Element

#### Caution

Don’t store real user data in [sandbox](https://docs.stripe.com/sandboxes) Link
accounts. Treat them as if they’re publicly available, because these test
accounts are associated with your publishable key.

Link works with the following browsers:

- Chrome, Chrome Mobile, and Microsoft Edge.
- Safari on desktop and iOS (last 3 major versions).

Link is available in both production and in a sandbox. You can create sandbox
Link accounts using any valid email address. The following table shows the fixed
one-time passcode values that Stripe accepts for authenticating Link sandbox
accounts:

ValueOutcomeAny other 6 digits not listed belowSuccess000001Error, code
invalid000002Error, code expired000003Error, max attempts exceeded
Enabling Link in a sandbox presents Link on all Card Element sandbox sessions
that meet the [enablement
requirements](https://docs.stripe.com/payments/link/card-element-link#enable-link).
In production, Link’s visibility might vary to maximize Link’s conversion
benefits in each checkout session.

## See also

- [Stripe Web Elements](https://docs.stripe.com/payments/elements)
- [Link Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element)
- [Payment Element](https://docs.stripe.com/payments/payment-element)

## Links

- [Link](https://docs.stripe.com/payments/link)
- [Card Element](https://docs.stripe.com/js/element/other_element?type=card)
- [Card
Number](https://docs.stripe.com/js/element/other_element?type=cardNumber)
- [Expiry](https://docs.stripe.com/js/element/other_element?type=cardExpiry)
- [CVC](https://docs.stripe.com/js/element/other_element?type=cardCvc)
- [Payment Method
settings](https://dashboard.stripe.com/settings/payment_methods)
-
[disableLink](https://docs.stripe.com/js/elements_object/create_element?type=card#elements_create-options-disableLink)
-
[Cross-Origin-Opener-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy)
- [Payment Method settings](https://dashboard.stripe.com/settings/link)
- [Payment Request
Button](https://docs.stripe.com/payments/link/payment-request-button-link)
- [connected
accounts](https://docs.stripe.com/connect/enable-payment-acceptance-guide?platform=web#create-account)
- [direct charges](https://docs.stripe.com/connect/direct-charges)
- [Payment Method
settings](https://dashboard.stripe.com/settings/connect/payment_methods)
- [clone payment
methods](https://docs.stripe.com/connect/direct-charges-multiple-accounts#clone-and-create-direct-charges)
- [destination charges](https://docs.stripe.com/connect/destination-charges)
- [separate charges and
transfers](https://docs.stripe.com/connect/separate-charges-and-transfers)
- [sandbox](https://docs.stripe.com/sandboxes)
- [Stripe Web Elements](https://docs.stripe.com/payments/elements)
- [Link Authentication
Element](https://docs.stripe.com/payments/elements/link-authentication-element)
- [Payment Element](https://docs.stripe.com/payments/payment-element)