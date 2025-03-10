# Embed a promotional tile

## Increase adoption for your Capital program by more prominently displaying offers.

## Overview

A promotional tile highlights available financing offers to your users to
increase awareness. This guide describes how to embed a 
guide.

That guide covers:

- Establishing a back-end route to use the Create Account Session API
- Setting up Connect.js
- Loading and initializing Connect.js

After completing that guide, you can proceed with the promotional tile
implementation.

## 2. Enable capital_financing_promotion in the Account Session route

When [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create), enable the
Capital financing promotion component by specifying
`capital_financing_promotion` in the `components` parameter.

```
curl https://api.stripe.com/v1/account_sessions \
 -u "sk_test_BQokikJOvBiI2HlWgH4olfQ2:" \
 -H "Stripe-Version: 2025-02-24.acacia; embedded_connect_beta=v2;" \
 -d account={{CONNECTED_ACCOUNT_ID}} \
 -d "components[capital_financing_promotion][enabled]"=true
```

## 2. Render the promotional tile

After creating the account session and initializing ConnectJS, you can render
the Capital financing promotion component in the front end:

```
// Include this element in your HTML
const capitalFinancingPromotion =
stripeConnectInstance.create('capital-financing-promotion');
capitalFinancingPromotion.setLayout('banner');
container.appendChild(capitalFinancingPromotion);
```

## 4. Customize the component’s appearance

You can [customize the look and feel of embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components?platform=web#customize-the-look-of-connect-embedded-components).
The Capital financing promotion component supports a set of styling options to
match your design system. This ensures the promotional tile feels like a native
part of your platform rather than a third-party element.

You can customize colors, typography, border radius, and [other visual
elements](https://docs.stripe.com/connect/embedded-appearance-options) through
the Connect.js configuration. You can also try out different options before
implementation using the [embedded component appearance preview
tool](https://docs.stripe.com/connect/customize-connect-embedded-components).

For more granular control, you can initialize multiple Connect.js instances if
your promotional tile requires different styling from other embedded components.
This approach allows you to maintain distinct appearance configurations for
different components throughout your platform.

## 5. Understanding display states

The component adapts its display based on the connected account’s financing
status:

- **With active offer**: Shows full offer details with a **Start application**
button
- **Active financing in progress**: The component doesn’t render (returns null)
- **No active financing**: Displays generic eligibility information about the
lending program

As described above, consider implementing the promotional tile on your main
homepage or other high-visibility pages where users make business decisions.

## 6. Optional: Hide the tile if there is no offer

A common styling preference is to hide the card entirely unless there is an
eligible offer. To accomplish this you can use the available
`onEligibleFinancingOfferLoaded` callback:

```
// Include this element in your HTML
const capitalFinancingPromotion =
stripeConnectInstance.create('capital-financing-promotion');
container.appendChild(capitalFinancingPromotion);
capitalFinancingPromotion.setOnEligibleFinancingOfferLoaded({productType}) => {
 switch (productType) {
 case 'none':
 capitalFinancingPromotion.parentElement.style.display = 'none';
 break;
 case 'standard':
 case 'refill':
 capitalFinancingPromotion.parentElement.style.display = 'block';
 break;
 }
}
```

## 7. Finding additional component documentation

The promotional tile is one of several embedded components available for
Capital.

For more information on additional configuration options for this component, see
the [Capital Financing Promotion
component](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion)
documentation.

You can also learn more about embedded components in our [Capital for Platforms
Embedded
Components](https://docs.stripe.com/capital/embedded-component-integration)
guide.

## Post-implementation steps

After implementing the promotional tile:

- **Consider A/B testing**: Segment users and measure the impact of the
promotional tile on application rates.
- **Extend your integration**: Extend your integration to other embedded
components, such as the [Capital application
flow](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application)

Need implementation support? Contact our [Capital for Platforms partnerships
team](mailto:capital-review@stripe.com) for personalized guidance.

## Links

- [Capital Financing Promotion
component](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion)
- [Get started with Connect embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components?platform=web#account-sessions)
- [creating an Account
Session](https://docs.stripe.com/api/account_sessions/create)
- [customize the look and feel of embedded
components](https://docs.stripe.com/connect/get-started-connect-embedded-components?platform=web#customize-the-look-of-connect-embedded-components)
- [other visual
elements](https://docs.stripe.com/connect/embedded-appearance-options)
- [embedded component appearance preview
tool](https://docs.stripe.com/connect/customize-connect-embedded-components)
- [Capital for Platforms Embedded
Components](https://docs.stripe.com/capital/embedded-component-integration)
- [Capital application
flow](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application)